---
name: pdf-large-image-heavy
description: >
  Personal addendum to the public pdf-reading skill, covering two things. (1) A general default
  for any PDF longer than ~3 pages: extract text first (pdftotext/pdfplumber), then check whether
  any chart/diagram/figure carries a number or detail that only lives in the image and isn't
  echoed in nearby text — if so, rasterize/view that specific page visually rather than assuming
  the text pass caught it. Skip this for short/simple PDFs where the overhead isn't worth it.
  (2) For PDFs that are additionally large (roughly 30+ pages) AND image-heavy — pdftotext returns
  little to nothing despite embedded fonts, pdfimages -list shows a raster image on nearly every
  page, or the content inventory flags it as a "slide-deck-style" document (books with lots of
  screenshots, design-heavy ebooks, marketing decks exported to PDF) — adds OCR (tesseract) as a
  third reading strategy alongside text extraction and page rasterization, with guidance on when
  to pick it.
---

# PDF Reading Defaults — Text-First, and OCR as a Third Option for Large Image-Heavy Docs

## Default for any PDF >3 pages: text-extraction-first

Extract text first (pdftotext/pdfplumber) rather than defaulting to native PDF vision or
rasterizing every page. After extraction, check whether any chart/diagram/figure carries a
number or detail that only lives inside the image — not also stated as a text label nearby. If
so, rasterize/view that specific page visually rather than assuming the text pass caught it.
Otherwise, work from the extracted text. Skip this workflow entirely for short/simple PDFs
(≤3 pages) where the overhead isn't worth it.

## Large Image-Heavy PDFs — OCR as a Third Option

`pdf-reading`'s decision table covers text extraction (cheap, for text-heavy docs) and
rasterize + vision (for figures/layout/scanned docs). For a large PDF where nearly every page
is a raster image — a design-heavy ebook, a slide-deck export, a book full of screenshotted
social posts — there's a third path worth weighing explicitly: **OCR the whole thing locally
with tesseract**, then read only the extracted text.

## The three-way tradeoff

| Approach | Token cost | Wall-clock cost | Fidelity |
|---|---|---|---|
| Rasterize + vision, every page | High (~1,600 tokens/page just for images, per pdf-reading's own figures — a 146-page book is ~230K tokens) | Fast (one pass, no batching needed) | Best — actually sees layout, screenshots, design |
| OCR (tesseract), then read extracted text | Low (only the text you choose to read into context, often a fraction of the total since you can sample chapters) | Slower — tesseract runs page-by-page and reliably times out past ~90-100 pages in one shell call, forcing 2-3 batched calls | Worse on graphic-heavy pages — OCR reads pixel shapes, not layout, so screenshots-within-the-PDF (e.g. a photographed LinkedIn post inside a book page) often come out garbled or lose structure |
| Rasterize only the pages that matter, vision those, OCR/text-extract the rest | Moderate | Moderate | Best of both, if you can tell upfront which pages need which treatment |

## Decision rule

This is a specific case of `token-thrift`'s general "choose method by step count" principle — the same regime split applies here:

- **If the person has signaled they want speed over cost** (explicit urgency, or this is a quick one-off lookup, not a background/batch task) → default to rasterize + vision, even for a large PDF. Don't make them wait through OCR batching to save tokens they didn't ask to save.
- **If the task already reads as token-heavy for other reasons** (per the `token-thrift` skill — many expected tool calls, large file, long agentic work) → OCR is usually the right default, since the point of that skill is trading wall-clock/setup cost for token savings. This is the case that applies most often in practice (large PDF + multi-step extraction task).
- **If ambiguous and the PDF is very large (100+ pages)** → say which way you're leaning and why, in one line, rather than silently picking — e.g. "This is 140+ pages of mostly screenshots; I'll OCR it locally to keep token cost down, which takes a bit longer than reading it directly — let me know if you'd rather I just read it visually instead." Then proceed; don't block on a reply for a low-stakes default.
- **If the images themselves carry information text alone won't capture** (a chart, a UI screenshot where positioning matters, a diagram) → rasterize + vision those specific pages regardless of which path you chose for the bulk of the document. OCR and vision aren't mutually exclusive per-page.

## Practical notes from running this

- Batch tesseract calls at ~25-30 pages per `bash_tool` call — a single loop over 100+ pages reliably hits the execution time limit.
- Background (`nohup ... &`) tesseract jobs are not reliable in this sandbox — the process appears to die silently between tool calls rather than continuing. Don't rely on backgrounding to avoid the batching above.
- Don't dump the full OCR output into context just because it's there — sample the sections relevant to the task (grep for headers/keywords, read targeted line ranges) the same way you would with a clean text extraction.
