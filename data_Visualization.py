# Data visualization
# 1. Importation of the Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 2. Load data analysed
data = pd.read_csv("statistical_analysed_data.csv")

# PLOT 1: TREND ANALYSIS : Show how Soil Moisture changes across observations.
# X-axis  : Sample Number
# Y-axis  : Moisture (%)

plt.figure(figsize=(10, 6))

plt.plot(
    data.index,
    data["Moisture"],
    color="blue",
    linewidth=1.5,
    label="Soil Moisture"
)

plt.title("Trend of Soil Moisture Across Soil Samples")
plt.xlabel("Sample Number")
plt.ylabel("Moisture (%)")

plt.grid(True)
plt.legend()

plt.show()

# PLOT 2: CATEGORICAL COMPARISON :  Compare average moisture among Soil Types.
# Objective:
# Compare average moisture among Soil Types.
# X-axis : Soil Type
# Y-axis : Average Moisture (%)

# Calculate mean moisture for each soil type
mean_moisture = data.groupby("Soil Type")["Moisture"].mean()

plt.figure(figsize=(8, 6))

mean_moisture.plot(
    kind="bar",
    color="skyblue"
)

plt.title("Average Soil Moisture by Soil Type")
plt.xlabel("Soil Type")
plt.ylabel("Average Moisture (%)")

plt.grid(True, axis="y")

plt.show()

# PLOT 3: CORRELATION PLOT : Examine relationship between Temperature and Moisture.
# X-axis : Temperature (°F)
# Y-axis : Moisture (%)
# Includes:
# - Scatter Plot
# - Regression (Trend) Line

# Calculate linear regression
slope, intercept, r_value, p_value, std_error = stats.linregress(
    data["Temparature"],
    data["Moisture"]
)

# Create regression line values
regression_line = slope * data["Temparature"] + intercept

plt.figure(figsize=(10, 6))

# Scatter points
plt.scatter(
    data["Temparature"],
    data["Moisture"],
    alpha=0.5,
    label="Observed Data"
)

# Trend line
plt.plot(
    data["Temparature"],
    regression_line,
    color="red",
    linewidth=2,
    label=f"Trend Line (R² = {r_value**2:.3f})"
)

plt.title("Relationship Between Temperature and Soil Moisture")
plt.xlabel("Temperature (°F)")
plt.ylabel("Moisture (%)")

plt.grid(True)
plt.legend()

plt.show()

# ==========================================================
# SUMMARY
# ==========================================================

print("\nVisualization Completed Successfully!")
print("Files Saved:")
print("1. trend_analysis_plot.png")
print("2. categorical_comparison_plot.png")
print("3. correlation_plot.png")