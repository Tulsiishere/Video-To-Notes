from pathlib import Path
from datetime import datetime

def build_markdown(video_name: str, summary_data, output_path: Path):
    output_path.parent.mkdir(parents=True, exist_ok=True)

    md = f"# Video Summary: {video_name}\n\n"
    md += f"Processed on: {datetime.now()}\n\n"
    md += "## High-Level Summary\n\n"
    md += summary_data.video_summary + "\n\n"

    md += "## Highlights\n\n"

    for i, h in enumerate(summary_data.highlights, 1):
        md += f"### {i}. {h.title}\n"
        md += f"- Time: {h.start_time_seconds:.2f} - {h.end_time_seconds:.2f}\n"
        md += f"- Why Important: {h.why_important}\n"
        md += "- Key Points:\n"
        for kp in h.key_points:
            md += f"  - {kp}\n"
        md += "\n"

    md += "## Overall Takeaways\n\n"
    for t in summary_data.overall_takeaways:
        md += f"- {t}\n"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md)