"""
analysis.py
Financial Services Performance Analysis - CAC trend, visualization, and strategic recommendations.

Email (for verification): 24f2005641@ds.study.iitm.ac.in
LLM assistance: Code structure generated with an LLM (Jules/Codex style).
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.io as pio

# ------------------------------
# 1. DATA
# ------------------------------
quarters = ["Q1", "Q2", "Q3", "Q4"]
cac_values = [227.57, 232.60, 233.07, 236.45]
industry_target = 150
avg_cac = np.mean(cac_values)  # Should be 232.42

df = pd.DataFrame({
    "quarter": quarters,
    "cac": cac_values
})

print("Quarterly CAC values:")
print(df.to_string(index=False))
print(f"\nComputed average CAC: {avg_cac:.2f}")
print(f"Industry target: {industry_target}")


# ------------------------------
# 2. TREND ANALYSIS
# ------------------------------
# Linear slope: positive means CAC rising
slope = np.polyfit(range(1, len(cac_values) + 1), cac_values, 1)[0]
print(f"\nLinear trend slope (CAC increase per quarter): {slope:.4f}")


# ------------------------------
# 3. VISUALIZATION (PNG)
# ------------------------------
sns.set_style("whitegrid")  # FIXED: replaces old 'seaborn-whitegrid'

fig, ax = plt.subplots(figsize=(8, 4.5))

# Line plot
ax.plot(df["quarter"], df["cac"], marker="o", linewidth=2, label="CAC")

# Industry target line
ax.axhline(industry_target, color="red", linestyle="--",
           label=f"Industry Target ({industry_target})")

# Average line
ax.axhline(avg_cac, color="orange", linestyle="-.",
           label=f"Average CAC ({avg_cac:.2f})")

ax.set_title("Quarterly Customer Acquisition Cost (CAC) — 2024",
             fontsize=14, weight="bold")
ax.set_ylabel("CAC ($)")
ax.set_ylim(120, max(cac_values) + 40)
ax.legend()

# Annotate points
for i, v in enumerate(df["cac"]):
    ax.text(i, v + 2, f"{v:.2f}", ha="center", fontsize=9)

plt.tight_layout()

png_path = "cac_trend.png"
plt.savefig(png_path, dpi=150)
plt.close()

print(f"\nSaved PNG visualization: {png_path}")


# ------------------------------
# 4. HTML REPORT
# ------------------------------
html_path = "cac_report.html"

html = f"""
<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<title>CAC Analysis</title>
</head>
<body>
  <h1>Customer Acquisition Cost — 2024</h1>

  <p><strong>Verification email:</strong> 24f2005641@ds.study.iitm.ac.in</p>

  <h2>Key Numbers</h2>
  <ul>
    <li>Q1 CAC: {cac_values[0]}</li>
    <li>Q2 CAC: {cac_values[1]}</li>
    <li>Q3 CAC: {cac_values[2]}</li>
    <li>Q4 CAC: {cac_values[3]}</li>
    <li><strong>Average CAC: {avg_cac:.2f}</strong></li>
    <li><strong>Industry Target: {industry_target}</strong></li>
    <li>Trend slope: {slope:.4f} (positive means rising)</li>
  </ul>

  <h2>CAC Trend Visualization</h2>
  <img src="cac_trend.png" alt="CAC Trend Chart" style="max-width:700px;">

  <h2>Summary</h2>
  <p>The average CAC (232.42) is significantly above the industry target (150), and the upward trend indicates
     marketing efficiency issues that must be addressed.</p>

  <h2>Recommendation</h2>
  <p><strong>Primary strategic recommendation:</strong> Optimize digital marketing channels.</p>
  <p>This includes reallocating spend toward high-efficiency channels, improving conversion rates with testing,
     enhancing targeting precision, reducing wasted spend, and increasing investment in organic acquisition channels.</p>

</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Saved HTML report: {html_path}")


# ------------------------------
# 5. TEXT RECOMMENDATIONS
# ------------------------------
recommendations = [
    "Shift budget toward lower CAC channels.",
    "Improve targeting and creative with A/B testing.",
    "Enhance landing page conversion rates.",
    "Pause or reduce spend on underperforming channels.",
    "Invest in SEO and content for long-term CAC reduction."
]

txt_path = "recommendations.txt"
with open(txt_path, "w", encoding="utf-8") as f:
    f.write("Recommendations to optimize digital marketing channels:\n")
    for item in recommendations:
        f.write(f"- {item}\n")

print(f"Saved recommendations: {txt_path}")
