"""
Win/Loss Calculator — Quantitative analysis for CRM deal data.

Reads a CSV file with closed deal data and produces a markdown report
with win rates, segmentation analysis, and statistical flags.

Expected CSV columns:
  deal_id, outcome, deal_size, segment, competitor, loss_reason, sales_cycle_days, lead_source

Usage:
  python win_loss_calculator.py input.csv > report.md
  python win_loss_calculator.py input.csv --output report.md
"""

import csv
import sys
import math
from collections import defaultdict
from typing import Optional


# --- Configuration ---

DEAL_SIZE_BUCKETS = [
    (0, 25000, "SMB (<$25K)"),
    (25000, 75000, "Mid-Market ($25-75K)"),
    (75000, float("inf"), "Enterprise ($75K+)"),
]

MIN_SAMPLE_SIZE = 30  # Below this, flag as "directional only"
MIN_DISPLAY_SIZE = 5  # Below this, don't show the cut at all


# --- Data Loading ---

def load_deals(filepath: str) -> list[dict]:
    """Load and validate deal data from CSV."""
    deals = []
    required = {"deal_id", "outcome"}

    with open(filepath, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        headers = set(reader.fieldnames or [])

        missing = required - headers
        if missing:
            print(f"ERROR: Missing required columns: {missing}", file=sys.stderr)
            sys.exit(1)

        for row in reader:
            deal = {
                "deal_id": row.get("deal_id", "").strip(),
                "outcome": normalize_outcome(row.get("outcome", "").strip()),
                "deal_size": parse_float(row.get("deal_size", "")),
                "segment": row.get("segment", "").strip() or "Unknown",
                "competitor": row.get("competitor", "").strip() or None,
                "loss_reason": row.get("loss_reason", "").strip() or None,
                "sales_cycle_days": parse_float(row.get("sales_cycle_days", "")),
                "lead_source": row.get("lead_source", "").strip() or "Unknown",
            }
            if deal["outcome"]:
                deals.append(deal)

    return deals


def normalize_outcome(val: str) -> Optional[str]:
    """Normalize outcome values to won/lost/no_decision."""
    val = val.lower().replace("-", "_").replace(" ", "_")
    if val in ("won", "closed_won", "win"):
        return "won"
    if val in ("lost", "closed_lost", "loss"):
        return "lost"
    if val in ("no_decision", "no decision", "stalled", "disqualified"):
        return "no_decision"
    return None


def parse_float(val: str) -> Optional[float]:
    """Parse a numeric string, returning None for empty/invalid."""
    val = val.strip().replace(",", "").replace("$", "")
    try:
        return float(val)
    except (ValueError, TypeError):
        return None


def bucket_deal_size(size: Optional[float]) -> str:
    """Assign a deal to a size bucket."""
    if size is None:
        return "Unknown"
    for low, high, label in DEAL_SIZE_BUCKETS:
        if low <= size < high:
            return label
    return "Unknown"


# --- Analysis Functions ---

def win_rate(deals: list[dict]) -> tuple[float, int, int]:
    """Calculate win rate. Returns (rate, won_count, total_decidable)."""
    won = sum(1 for d in deals if d["outcome"] == "won")
    decidable = sum(1 for d in deals if d["outcome"] in ("won", "lost"))
    rate = (won / decidable * 100) if decidable > 0 else 0.0
    return rate, won, decidable


def stat_flag(n: int) -> str:
    """Return a statistical significance flag."""
    if n < MIN_DISPLAY_SIZE:
        return " *(too few deals to report)*"
    if n < MIN_SAMPLE_SIZE:
        return f" *(n={n}, directional only)*"
    return f" (n={n})"


def format_currency(val: float) -> str:
    """Format a number as currency."""
    if val >= 1_000_000:
        return f"${val / 1_000_000:.2f}M"
    if val >= 1_000:
        return f"${val / 1_000:.1f}K"
    return f"${val:,.0f}"


def safe_avg(values: list[float]) -> Optional[float]:
    """Calculate average, returning None for empty lists."""
    filtered = [v for v in values if v is not None]
    return sum(filtered) / len(filtered) if filtered else None


# --- Report Generation ---

def generate_report(deals: list[dict]) -> str:
    """Generate full markdown analysis report."""
    lines: list[str] = []

    won_deals = [d for d in deals if d["outcome"] == "won"]
    lost_deals = [d for d in deals if d["outcome"] == "lost"]
    no_dec = [d for d in deals if d["outcome"] == "no_decision"]

    # --- Headline Metrics ---
    lines.append("# Win/Loss Quantitative Analysis\n")
    lines.append(f"**Total deals analyzed:** {len(deals)}\n")

    rate, won_count, decidable = win_rate(deals)
    lines.append("## Headline Metrics\n")
    lines.append("| Metric | Value |")
    lines.append("|---|---|")
    lines.append(f"| Total deals | {len(deals)} |")
    lines.append(f"| Won | {len(won_deals)} |")
    lines.append(f"| Lost | {len(lost_deals)} |")
    lines.append(f"| No Decision | {len(no_dec)} |")
    lines.append(f"| **Win Rate** | **{rate:.1f}%**{stat_flag(decidable)} |")

    avg_won_size = safe_avg([d["deal_size"] for d in won_deals])
    avg_lost_size = safe_avg([d["deal_size"] for d in lost_deals])
    if avg_won_size is not None:
        lines.append(f"| Avg Deal Size (Won) | {format_currency(avg_won_size)} |")
    if avg_lost_size is not None:
        lines.append(f"| Avg Deal Size (Lost) | {format_currency(avg_lost_size)} |")

    avg_cycle_won = safe_avg([d["sales_cycle_days"] for d in won_deals])
    avg_cycle_lost = safe_avg([d["sales_cycle_days"] for d in lost_deals])
    if avg_cycle_won is not None:
        lines.append(f"| Avg Sales Cycle (Won) | {avg_cycle_won:.0f} days |")
    if avg_cycle_lost is not None:
        lines.append(f"| Avg Sales Cycle (Lost) | {avg_cycle_lost:.0f} days |")

    lines.append("")

    # --- Win Rate by Segment ---
    lines.append("## Win Rate by Segment\n")
    lines.append("| Segment | Won | Lost | Win Rate | Flag |")
    lines.append("|---|---|---|---|---|")

    by_segment: dict[str, list[dict]] = defaultdict(list)
    for d in deals:
        by_segment[d["segment"]].append(d)

    for seg in sorted(by_segment.keys()):
        seg_deals = by_segment[seg]
        r, w, total = win_rate(seg_deals)
        if total >= MIN_DISPLAY_SIZE:
            lines.append(f"| {seg} | {w} | {total - w} | {r:.1f}% | {stat_flag(total).strip()} |")

    lines.append("")

    # --- Win Rate by Deal Size ---
    lines.append("## Win Rate by Deal Size\n")
    lines.append("| Bucket | Won | Lost | Win Rate | Flag |")
    lines.append("|---|---|---|---|---|")

    by_size: dict[str, list[dict]] = defaultdict(list)
    for d in deals:
        bucket = bucket_deal_size(d["deal_size"])
        by_size[bucket].append(d)

    for _, _, label in DEAL_SIZE_BUCKETS:
        if label in by_size:
            bucket_deals = by_size[label]
            r, w, total = win_rate(bucket_deals)
            if total >= MIN_DISPLAY_SIZE:
                lines.append(f"| {label} | {w} | {total - w} | {r:.1f}% | {stat_flag(total).strip()} |")

    lines.append("")

    # --- Win Rate by Competitor ---
    competitors: dict[str, list[dict]] = defaultdict(list)
    for d in deals:
        if d["competitor"]:
            competitors[d["competitor"]].append(d)

    if competitors:
        lines.append("## Win Rate by Competitor\n")
        lines.append("| Competitor | Won | Lost | Win Rate | Revenue Lost | Flag |")
        lines.append("|---|---|---|---|---|---|")

        comp_sorted = sorted(
            competitors.items(),
            key=lambda x: sum(1 for d in x[1] if d["outcome"] == "lost"),
            reverse=True,
        )
        for comp, comp_deals in comp_sorted:
            r, w, total = win_rate(comp_deals)
            rev_lost = sum(d["deal_size"] or 0 for d in comp_deals if d["outcome"] == "lost")
            if total >= MIN_DISPLAY_SIZE:
                lines.append(f"| {comp} | {w} | {total - w} | {r:.1f}% | {format_currency(rev_lost)} | {stat_flag(total).strip()} |")

        lines.append("")

    # --- Win Rate by Lead Source ---
    by_source: dict[str, list[dict]] = defaultdict(list)
    for d in deals:
        by_source[d["lead_source"]].append(d)

    if len(by_source) > 1:
        lines.append("## Win Rate by Lead Source\n")
        lines.append("| Source | Won | Lost | Win Rate | Avg Deal Size | Flag |")
        lines.append("|---|---|---|---|---|---|")

        for source in sorted(by_source.keys()):
            src_deals = by_source[source]
            r, w, total = win_rate(src_deals)
            avg_size = safe_avg([d["deal_size"] for d in src_deals])
            size_str = format_currency(avg_size) if avg_size else "—"
            if total >= MIN_DISPLAY_SIZE:
                lines.append(f"| {source} | {w} | {total - w} | {r:.1f}% | {size_str} | {stat_flag(total).strip()} |")

        lines.append("")

    # --- Loss Reason Distribution ---
    if any(d["loss_reason"] for d in lost_deals):
        lines.append("## Loss Reason Distribution\n")
        lines.append("| Reason | Count | % of Losses | Revenue Lost | % of Revenue |")
        lines.append("|---|---|---|---|---|")

        by_reason: dict[str, list[dict]] = defaultdict(list)
        for d in lost_deals:
            reason = d["loss_reason"] or "Uncategorized"
            by_reason[reason].append(d)

        total_lost_rev = sum(d["deal_size"] or 0 for d in lost_deals)
        reason_sorted = sorted(by_reason.items(), key=lambda x: len(x[1]), reverse=True)

        for reason, reason_deals in reason_sorted:
            count = len(reason_deals)
            pct = count / len(lost_deals) * 100
            rev = sum(d["deal_size"] or 0 for d in reason_deals)
            rev_pct = (rev / total_lost_rev * 100) if total_lost_rev > 0 else 0
            lines.append(f"| {reason} | {count} | {pct:.1f}% | {format_currency(rev)} | {rev_pct:.1f}% |")

        lines.append("")

    # --- No-Decision Analysis ---
    if no_dec:
        lines.append("## No-Decision Analysis\n")
        lines.append(f"**{len(no_dec)} deals** ({len(no_dec)/len(deals)*100:.1f}% of pipeline) ended in no decision.\n")
        no_dec_rev = sum(d["deal_size"] or 0 for d in no_dec)
        lines.append(f"**Revenue impact:** {format_currency(no_dec_rev)} in pipeline that went nowhere.\n")

    # --- Caveats ---
    lines.append("## Data Quality Notes\n")

    missing_size = sum(1 for d in deals if d["deal_size"] is None)
    missing_cycle = sum(1 for d in deals if d["sales_cycle_days"] is None)
    missing_reason = sum(1 for d in lost_deals if not d["loss_reason"])

    if missing_size:
        lines.append(f"- **{missing_size} deals** missing deal size data — excluded from size-based analysis")
    if missing_cycle:
        lines.append(f"- **{missing_cycle} deals** missing sales cycle data — excluded from cycle analysis")
    if missing_reason:
        lines.append(f"- **{missing_reason} lost deals** missing loss reason — appears as 'Uncategorized'")
    if not any([missing_size, missing_cycle, missing_reason]):
        lines.append("- All fields populated — no missing data issues detected")

    lines.append("")
    return "\n".join(lines)


# --- Main ---

def main():
    """Run the calculator from command line."""
    if len(sys.argv) < 2:
        print("Usage: python win_loss_calculator.py <input.csv> [--output <file>]")
        print("\nExpected CSV columns:")
        print("  deal_id, outcome, deal_size, segment, competitor,")
        print("  loss_reason, sales_cycle_days, lead_source")
        sys.exit(1)

    filepath = sys.argv[1]
    output_file = None

    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            output_file = sys.argv[idx + 1]

    deals = load_deals(filepath)
    if not deals:
        print("ERROR: No valid deals found in the CSV.", file=sys.stderr)
        sys.exit(1)

    report = generate_report(deals)

    if output_file:
        with open(output_file, "w") as f:
            f.write(report)
        print(f"Report written to {output_file}")
    else:
        print(report)


if __name__ == "__main__":
    main()
