#!/usr/bin/env node

/**
 * render-og.js — Renders an HTML file to a 1200x630 OpenGraph image.
 *
 * Usage:
 *   node render-og.js <input.html> <output.[jpg|png]> [options]
 *
 * Options:
 *   --quality <1-100>     JPG quality (default: 85, ignored for PNG)
 *   --max-size <kb>       Max file size in KB (default: 600 for WhatsApp). JPG only.
 *                         The script iteratively reduces quality until the file fits.
 *   --no-shrink           Don't auto-shrink JPG quality to meet --max-size.
 *
 * Output format is auto-detected from the extension:
 *   .jpg / .jpeg → JPG (default, smaller, WhatsApp-friendly)
 *   .png         → PNG (larger, lossless, supports transparency)
 *
 * Auto-detects which headless browser library is available.
 * Tries Puppeteer first, then Playwright.
 *
 * Examples:
 *   node render-og.js og.html og-image.jpg                # JPG, max 600KB, quality auto
 *   node render-og.js og.html og-image.png                # PNG, lossless
 *   node render-og.js og.html og-image.jpg --quality 92   # JPG, start at quality 92
 *   node render-og.js og.html og-image.jpg --max-size 300 # JPG, max 300KB
 */

const path = require("path");
const fs = require("fs");

const WIDTH = 1200;
const HEIGHT = 630;
const DEFAULT_JPG_QUALITY = 85;
const DEFAULT_MAX_SIZE_KB = 600; // WhatsApp-safe ceiling
const MIN_QUALITY = 55; // Don't go below this; legibility suffers

function parseArgs(argv) {
  const args = { positional: [], quality: null, maxSize: DEFAULT_MAX_SIZE_KB, shrink: true };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--quality") args.quality = parseInt(argv[++i], 10);
    else if (a === "--max-size") args.maxSize = parseInt(argv[++i], 10);
    else if (a === "--no-shrink") args.shrink = false;
    else args.positional.push(a);
  }
  return args;
}

function detectFormat(outputPath) {
  const ext = path.extname(outputPath).toLowerCase();
  if (ext === ".jpg" || ext === ".jpeg") return "jpeg";
  if (ext === ".png") return "png";
  throw new Error(`Unsupported output extension: "${ext}". Use .jpg, .jpeg, or .png.`);
}

async function renderWithPuppeteer(htmlPath, outputPath, format, quality) {
  const puppeteer = require("puppeteer");
  const browser = await puppeteer.launch({
    headless: "new",
    args: ["--no-sandbox", "--disable-setuid-sandbox"],
  });
  try {
    const page = await browser.newPage();
    await page.setViewport({ width: WIDTH, height: HEIGHT, deviceScaleFactor: 1 });

    const fileUrl = "file://" + path.resolve(htmlPath);
    await page.goto(fileUrl, { waitUntil: "networkidle0", timeout: 15000 });

    // Brief pause to let fonts and gradients settle
    await new Promise((r) => setTimeout(r, 500));

    const screenshotOpts = {
      path: outputPath,
      type: format,
      clip: { x: 0, y: 0, width: WIDTH, height: HEIGHT },
    };
    if (format === "jpeg") screenshotOpts.quality = quality;

    await page.screenshot(screenshotOpts);
  } finally {
    await browser.close();
  }
}

async function renderWithPlaywright(htmlPath, outputPath, format, quality) {
  const { chromium } = require("playwright");
  const browser = await chromium.launch({ headless: true });
  try {
    const page = await browser.newPage({
      viewport: { width: WIDTH, height: HEIGHT },
      deviceScaleFactor: 1,
    });

    const fileUrl = "file://" + path.resolve(htmlPath);
    await page.goto(fileUrl, { waitUntil: "networkidle", timeout: 15000 });

    await page.waitForTimeout(500);

    const screenshotOpts = {
      path: outputPath,
      type: format,
      clip: { x: 0, y: 0, width: WIDTH, height: HEIGHT },
    };
    if (format === "jpeg") screenshotOpts.quality = quality;

    await page.screenshot(screenshotOpts);
  } finally {
    await browser.close();
  }
}

function tryRequire(mod) {
  try {
    require.resolve(mod);
    return true;
  } catch {
    return false;
  }
}

function fileSizeKB(p) {
  return fs.statSync(p).size / 1024;
}

async function renderOnce(htmlPath, outputPath, format, quality, engine) {
  if (engine === "puppeteer") {
    await renderWithPuppeteer(htmlPath, outputPath, format, quality);
  } else {
    await renderWithPlaywright(htmlPath, outputPath, format, quality);
  }
}

async function main() {
  const args = parseArgs(process.argv.slice(2));

  if (args.positional.length < 2) {
    console.error(
      "Usage: node render-og.js <input.html> <output.[jpg|png]> [--quality N] [--max-size KB] [--no-shrink]"
    );
    process.exit(1);
  }

  const [htmlPath, outputPath] = args.positional;

  if (!fs.existsSync(htmlPath)) {
    console.error(`Error: HTML file not found: ${htmlPath}`);
    process.exit(1);
  }

  const outDir = path.dirname(outputPath);
  if (outDir && !fs.existsSync(outDir)) {
    fs.mkdirSync(outDir, { recursive: true });
  }

  const format = detectFormat(outputPath);
  const initialQuality =
    args.quality !== null && !isNaN(args.quality) ? args.quality : DEFAULT_JPG_QUALITY;

  const hasPuppeteer = tryRequire("puppeteer");
  const hasPlaywright = tryRequire("playwright");

  if (!hasPuppeteer && !hasPlaywright) {
    console.error(
      "Error: Neither Puppeteer nor Playwright is installed.\n\n" +
        "Install one of them:\n" +
        "  npm install puppeteer\n" +
        "  # or\n" +
        "  npm install playwright && npx playwright install chromium\n"
    );
    process.exit(1);
  }

  const engine = hasPuppeteer ? "puppeteer" : "playwright";

  try {
    console.log(`Using ${engine}, rendering ${WIDTH}x${HEIGHT} ${format.toUpperCase()}...`);
    await renderOnce(htmlPath, outputPath, format, initialQuality, engine);

    let sizeKB = fileSizeKB(outputPath);
    console.log(
      `Rendered: ${outputPath} (${sizeKB.toFixed(1)} KB${
        format === "jpeg" ? `, quality ${initialQuality}` : ""
      })`
    );

    // Iteratively shrink JPG quality to fit max-size if needed
    if (format === "jpeg" && args.shrink && sizeKB > args.maxSize) {
      let quality = initialQuality;
      while (sizeKB > args.maxSize && quality > MIN_QUALITY) {
        quality -= 5;
        console.log(`Over ${args.maxSize}KB cap, re-rendering at quality ${quality}...`);
        await renderOnce(htmlPath, outputPath, format, quality, engine);
        sizeKB = fileSizeKB(outputPath);
        console.log(`  → ${sizeKB.toFixed(1)} KB`);
      }
      if (sizeKB > args.maxSize) {
        console.warn(
          `WARNING: Could not get below ${args.maxSize}KB even at quality ${MIN_QUALITY}. ` +
            `Consider simplifying the design (less gradient noise, smaller background image).`
        );
      }
    }

    console.log(
      `\nDone. Final: ${outputPath} — ${sizeKB.toFixed(1)} KB, ${WIDTH}x${HEIGHT} ${format.toUpperCase()}`
    );
  } catch (err) {
    console.error("Render failed:", err.message);
    process.exit(1);
  }
}

main();
