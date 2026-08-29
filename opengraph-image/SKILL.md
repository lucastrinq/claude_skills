---
name: opengraph-image
description: Generate OpenGraph (og:image) and social preview images that look great on LinkedIn, Twitter/X, Slack, Discord, Facebook, and WhatsApp. Use this skill whenever someone wants to create, update, or fix the image that appears when a link is shared. Triggers include "og:image", "opengraph image", "OG image", "twitter card image", "social preview image", "link preview image", "meta image", "social share graphic", preview image for a blog/page/site, "make the link look good/better when shared", or complaints that a link preview "looks bad/ugly/awful" when shared. Also use when someone needs a branded sharing image for any web page. Outputs a 1200x630 JPG (or PNG) rendered from HTML/CSS, with file size kept under 600KB for WhatsApp compatibility. NOT for image resizing, compression, galleries, avatars, favicons, or PDFs.
---

# OpenGraph Image Generator

Create bold, headline-focused OpenGraph images that grab attention in social feeds and survive every platform — including WhatsApp, which silently rejects previews larger than ~600KB.

## Why this matters

An effective OG image is the single biggest lever for click-through on a shared link. Most feeds render OG images at roughly **300px wide on mobile**, so the image must be readable at thumbnail size, not just beautiful at full resolution. Bold typography, high contrast, and minimal clutter are what separate an effective OG image from a forgettable one.

WhatsApp is the strictest platform: images over ~600KB often don't preview at all, and the link falls back to a bare URL. Designing for WhatsApp means designing for everyone.

## The workflow at a glance

1. Gather context (title, subtitle, brand assets)
2. Validate and tighten the copy
3. Build a design spec (a brief structured plan, before any HTML)
4. Render to HTML and save the file
5. Convert HTML → 1200×630 JPG, auto-shrunk to fit under 600KB
6. Verify against the pre-publish checklist
7. Deliver the image and the `<meta>` tags

Do not skip the design-spec step. It catches problems (hierarchy, contrast, copy length) before you render, where they're cheap to fix.

## Step 1: Gather context

Collect the inputs. If anything material is missing, ask **at most 3 short questions** — only the ones that would actually change the output.

Priority gaps worth asking about:
- **Tone** — premium, playful, technical, editorial? (changes type and color choices)
- **Brand color preference** — if none can be detected
- **Badge/tag** — should there be a small badge like "NEW", "BETA", a category, or a date?

If the user says "no questions" or "just go", proceed with best-effort defaults and list assumptions explicitly in the final delivery.

Inputs to collect:

1. **Title text** — the main headline (≤10 words, ideally ≤7). Required.
2. **Subtitle/tagline** — a short supporting line (≤12 words). Every OG image should have one. If the user doesn't provide it, generate something contextual: a project tagline, a one-line summary, or a soft call-to-action. A title alone leaves visual dead space. Do NOT use generic filler like "Blog Post" or "Article" — those add zero information.
3. **Background image** — if relevant, look through the project for the first meaningful image:
   - Hero / featured images in the page's HTML
   - `public/`, `assets/`, `static/`, `images/` directories
   - Product screenshots or photos that match the page's topic
   - If none is found or fits, fall back to a gradient.
4. **Brand assets** — search the project for:
   - **Colors**: CSS variables, Tailwind config, theme files, `package.json` brand metadata, or the site's existing CSS
   - **Logo**: `public/`, `assets/`, `static/`, `images/` — prefer SVG, accept PNG
   - **Fonts**: CSS `@font-face` declarations, Google Fonts imports, Tailwind font config
5. **Optional**: badge text, target URL (for context, not display), specific layout preferences.

If no brand colors are detectable and the user hasn't said, default to: deep neutral background (`#111827` or `#1a1a2e`), white text, single saturated accent (`#3b82f6` or similar), Inter font stack.

## Step 2: Validate and refine the copy

Before designing anything, tighten the wording. Read the title and subtitle aloud in your head — they should land in under a second.

Rules of thumb:
- **Title** — bold claim or benefit, not a feature list. Cut filler words ("the", "a", "your") only if it doesn't damage readability.
- **Subtitle** — adds the "so what". Should answer either *why care* or *what next*.
- **Hierarchy** — three distinct levels: brand/anchor → core message → supporting line. The eye should know exactly where to land first.
- **If the title is too long** (over ~40 characters), rewrite a shorter equivalent and note this in the assumptions list. Do not just shrink the font as a workaround — the visual weight matters as much as the words.

Examples:

- ❌ "Our New Feature Helps You Better Manage Your Customer Relationships"
- ✅ "Close deals 3x faster" (subtitle: "AI-powered CRM for high-velocity sales teams")

- ❌ "Welcome to Acme — A Solution for Your Business Needs"
- ✅ "Books that pay for themselves" (subtitle: "Automated bookkeeping for Belgian freelancers")

## Step 3: Build the design spec

Before writing any HTML, produce a brief design spec for the user. This catches misalignment early. Keep it tight — no fluff.

Use this exact structure:

```
### Design direction
- 3–5 bullets: concept, mood, intended scanning flow.

### Layout blueprint
- Zone-by-zone: top / middle / bottom (or left / center / right).
- Alignment (left-aligned by default unless the design calls for centered).
- What sits where and why.

### Typography system
- Font pairing (or style category if exact fonts are unknown).
- Scale: at least 3 distinct levels with px sizes.
- Weights, case, line-height for each level.

### Color system
- Background / primary / accent — with contrast rationale.
- Fallback palette if brand colors weren't detected.

### Copy hierarchy (final mock text)
- The exact on-image text, line by line, as it will appear.

### Production notes
- Format (JPG default, PNG only if transparency or extreme precision is needed).
- Compression target (<600KB hard ceiling for WhatsApp).
- Safe margins (40px minimum on all sides — some platforms crop).
- Thumbnail-legibility check (will every text element survive at 300px wide?).

### Assumptions
- List anything inferred because the user didn't specify it.
```

Show this spec to the user before rendering, unless they've explicitly said "just make it". For tight, transactional requests with all inputs provided, you can skip the user-facing spec step and go straight to rendering — but the same reasoning still has to happen internally.

## Step 4: Create or reuse the HTML template

Check the project for an existing OG template (`og-templates/`, `og-image.html`, `og-template.html`). If found, reuse and adapt. If not, create one.

### Two layout modes

**Mode A — Background image with text card** (preferred when a relevant image exists)

A full-bleed background image with a solid (or near-solid, ≥85% opacity) colored card holding the text. The card guarantees legibility regardless of what the image shows. Don't use a semi-transparent gradient overlay on the whole image — use a distinct card shape.

**Mode B — Gradient or solid background** (fallback)

A bold gradient or solid color with text directly on it. Cleaner, faster to render, smaller file size. Use this whenever no image clearly belongs.

### Template requirements

Self-contained HTML (inline CSS, optionally Google Fonts via `<link>`):

- **Viewport**: exactly 1200×630 px (the OpenGraph standard, 1.91:1 ratio, WhatsApp-safe)
- **Layout**: flexbox or grid. **Left-aligned by default** — feels more editorial and less template-y than centered. Use centered only when the user asks for it or the design clearly demands symmetry.
- **Typography scale**: at least 3 levels.
  - Title: 64–88px, weight 800–900, line-height 1.05–1.1, letter-spacing slightly tight (`-0.02em`)
  - Subtitle: 28–34px, weight 600–700, line-height 1.3
  - Brand/badge/eyebrow: 18–22px, weight 600, uppercase optional, generous tracking (`0.08em`)
  - **Never go below 22px** on a 1200px canvas — anything smaller is unreadable at thumbnail size.
- **Contrast**: WCAG AA minimum (4.5:1 for body, 3:1 for large text). When in doubt, push to white-on-deep-dark or deep-dark-on-white.
- **Logo** (if available): top-left or bottom-left, max 56px tall.
- **Safe zones**: 48px minimum padding on all sides. Some platforms crop the edges.
- **Decorative flair**: at most one. A soft gradient, a geometric accent, a slight text shadow — pick one, no more.

### Example: Mode A — background image with text card

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@600;700;900&display=swap" rel="stylesheet">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      width: 1200px;
      height: 630px;
      position: relative;
      font-family: 'Inter', system-ui, sans-serif;
      color: #ffffff;
      overflow: hidden;
    }
    .bg {
      position: absolute;
      inset: 0;
      background: url('BACKGROUND_IMAGE_PATH') center/cover no-repeat;
    }
    .bg::after {
      content: '';
      position: absolute;
      inset: 0;
      background: rgba(0, 0, 0, 0.35);
    }
    .card {
      position: absolute;
      left: 48px;
      bottom: 48px;
      right: 48px;
      background: rgba(17, 24, 39, 0.94);
      border-radius: 16px;
      padding: 40px 48px;
    }
    .eyebrow {
      font-size: 20px;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      opacity: 0.7;
      margin-bottom: 16px;
    }
    h1 {
      font-size: 72px;
      font-weight: 900;
      line-height: 1.05;
      letter-spacing: -0.02em;
    }
    .subtitle {
      font-size: 30px;
      font-weight: 600;
      margin-top: 16px;
      opacity: 0.85;
      line-height: 1.3;
    }
  </style>
</head>
<body>
  <div class="bg"></div>
  <div class="card">
    <div class="eyebrow">BRAND OR CATEGORY</div>
    <h1>Your Bold Headline Here</h1>
    <p class="subtitle">A short, compelling tagline goes here</p>
  </div>
</body>
</html>
```

### Example: Mode B — gradient only

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@600;700;900&display=swap" rel="stylesheet">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      width: 1200px;
      height: 630px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: flex-start;
      padding: 80px 96px;
      background: linear-gradient(135deg, #0f172a 0%, #1e293b 60%, #0c4a6e 100%);
      font-family: 'Inter', system-ui, sans-serif;
      color: #ffffff;
      overflow: hidden;
    }
    .eyebrow {
      font-size: 22px;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      opacity: 0.7;
      margin-bottom: 24px;
    }
    h1 {
      font-size: 80px;
      font-weight: 900;
      line-height: 1.05;
      letter-spacing: -0.02em;
      max-width: 980px;
    }
    .subtitle {
      font-size: 32px;
      font-weight: 600;
      margin-top: 24px;
      opacity: 0.85;
      max-width: 880px;
      line-height: 1.3;
    }
  </style>
</head>
<body>
  <div class="eyebrow">BRAND OR CATEGORY</div>
  <h1>Your Bold Headline Here</h1>
  <p class="subtitle">A short, compelling tagline goes here</p>
</body>
</html>
```

Save the filled HTML somewhere stable in the project, typically `og-templates/og-<slug>.html`, so it stays reusable and can be regenerated when copy changes.

## Step 5: Render to JPG

Use the bundled render script. It outputs a 1200×630 image and **automatically reduces JPG quality** until the file fits under the 600KB WhatsApp ceiling.

```bash
node <skill-path>/scripts/render-og.js <html-file> <output.jpg>
```

Defaults:
- Format: detected from extension (`.jpg`/`.jpeg` → JPG, `.png` → PNG)
- JPG initial quality: 85
- Max size: 600KB (JPG only; PNG output skips the size loop)
- Auto-shrink: on (JPG quality drops in steps of 5 until the file fits or quality hits 55)

Examples:

```bash
# Default: JPG, max 600KB, WhatsApp-safe
node scripts/render-og.js og-templates/og-launch.html public/og-launch.jpg

# Higher starting quality
node scripts/render-og.js og-templates/og-launch.html public/og-launch.jpg --quality 92

# Tighter size cap (some email clients prefer ≤300KB)
node scripts/render-og.js og-templates/og-launch.html public/og-launch.jpg --max-size 300

# PNG if you specifically need transparency or lossless
node scripts/render-og.js og-templates/og-launch.html public/og-launch.png
```

The script auto-detects Puppeteer or Playwright. If neither is installed, it prints install instructions.

## Step 6: Pre-publish checklist

Run through every item. Skipping these is how broken previews ship.

- [ ] **Dimensions** are exactly 1200×630 (the script enforces this, but verify)
- [ ] **File size** is under 600KB (the script enforces this for JPG; verify for PNG)
- [ ] **Title is legible at 300px wide** — squint at the image. If you can't read it, the title is too small or the contrast is too low.
- [ ] **Subtitle is legible at 300px wide** — same test.
- [ ] **No text within 32px of any edge** — some platforms (notably LinkedIn on mobile) crop.
- [ ] **Title is ≤10 words and subtitle is ≤12 words** — otherwise it'll wrap awkwardly or get truncated.
- [ ] **Contrast passes WCAG AA** — title against background ≥3:1 for large text, ideally ≥4.5:1.
- [ ] **Brand is identifiable in under a second** — logo, brand color, or distinctive type. If a stranger glanced at it, would they know who it's from?
- [ ] **Open the file** — actually preview it. Don't assume the render is correct.

Three additional **mobile preview sanity checks** you can do quickly:
1. Resize the image to 300px wide in any image viewer — every text element should still be readable.
2. Convert it to grayscale mentally — does the hierarchy still work without color?
3. Squint hard — what do you see first? That should be the most important element (usually the title, occasionally the brand).

## Step 7: Deliver and suggest meta tags

1. Tell the user where the image was saved and what its final size is.
2. If you can locate the page's HTML or layout template (`index.html`, `_app.tsx`, `layout.tsx`, a `<head>` partial, etc.), check whether `og:image` tags exist. If not, suggest adding:

```html
<meta property="og:title" content="Your Bold Headline Here">
<meta property="og:description" content="A short, compelling tagline goes here">
<meta property="og:image" content="https://example.com/og-launch.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:alt" content="Plain-language description of the image">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://example.com/og-launch.jpg">
```

Remind the user to replace `https://example.com/og-launch.jpg` with the actual deployed URL — relative paths don't work for OG images, they must be absolute.

3. **Suggest a validator pass**: have the user test the live URL in:
   - [opengraph.dev](https://www.opengraph.dev/) — quickest overall preview
   - LinkedIn's [Post Inspector](https://www.linkedin.com/post-inspector/)
   - Twitter/X's preview (just paste the URL in a draft tweet — they killed the card validator)
   - WhatsApp (send the link to yourself in any chat)

If the preview doesn't update after a deploy, mention that some platforms cache aggressively — LinkedIn especially. The Post Inspector forces a re-scrape.

## Troubleshooting

- **"Neither Puppeteer nor Playwright is installed"** — run `npm install puppeteer` (simplest) or `npm install playwright && npx playwright install chromium`.
- **Fonts don't load in the render** — Google Fonts requires network access during rendering. If you're offline, swap to a system font stack (`-apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif`) or embed the font as base64 in the CSS.
- **Image looks fine in Chrome but renders wrong** — open the HTML in a real browser at exactly 1200×630 first to debug. Most rendering issues are CSS issues, not Puppeteer issues.
- **File is over 600KB even at quality 55** — the design is too heavy. Common causes: a large background photo at full resolution (pre-resize it), heavy gradients with banding, or a lot of fine textural noise. Switch to Mode B or simplify.
- **Text gets cut off** — title or subtitle is too long. Either rewrite shorter or scale the font down — but don't go below the 22px floor.
- **Preview won't update on LinkedIn/Facebook** — they cache for 7+ days. Use their official inspector tools to force a re-scrape; appending `?v=2` to the image URL works as a last resort.
- **WhatsApp shows no preview** — the file is almost certainly over the size ceiling, the URL isn't reachable, or the meta tags use a relative path. Check those three first.
