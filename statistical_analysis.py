# This is our script for the statistical analysis 
# 1. Importation of the Modules in the data analysis code
import pandas as pd
import numpy as np
from scipy import stats

# 2. Loading of the data file
data = pd.read_csv("cleaned_data_file.csv")

# 3. Using of the groupby() for data Aggregation
mean_data = data.groupby("Soil Type")[["Temparature", "Humidity", "Moisture"]].mean()

# 4. Using numpy for vectorised operations for the conversion of 
data["Temparature_Celsius"] = np.round((data["Temparature"] - 32) * (5 / 9), 2)

# 5. Scipy statistical analysis

# 5.1. Correlation between Temperature and Moisture
corr_temp, p_temp = stats.pearsonr(data["Temparature"],data["Moisture"])
print("\nCorrelation between Temperature and Moisture")
print("Correlation coefficient =", round(corr_temp,3))
print("P-value =", p_temp)

# 5.2. Correlation between Humidity and Moisture
corr_hum, p_hum = stats.pearsonr(data["Humidity"],data["Moisture"])
print("\nCorrelation between Humidity and Moisture")
print("Correlation coefficient =", round(corr_hum,3))
print("P-value =", p_hum)

# 5.3. Linear Regression
# "Does soil moisture level significantly vary across different soil types, and can Temperature\n
#  and Humidity predict soil moisture in Agricultural Fields?"
slope, intercept, r_value, p_value, std_error = stats.linregress(data["Temparature"],data["Moisture"])
print("\nLinear Regression")
print("Slope =", slope)
print("Intercept =", intercept)
print("R-squared =", r_value**2)
print("P-value =", p_value)

# 5.4. Test whether siol moisture varies across different soil types
# 5.4.1 One-way ANOVA

# Create one moisture group for each soil type
groups = []

for soil in data["Soil Type"].unique():groups.append(data[data["Soil Type"] == soil]["Moisture"])
F_statistic, p_value = stats.f_oneway(*groups)

print("\nANOVA Test")
print("F-statistic =", F_statistic)
print("P-value =", p_value)

# 5.5. Interpretation

print("\nINTERPRETATION")

if p_value < 0.05:
    print("There is a statistically significant difference")
    print("in soil moisture among different soil types.")
else:
    print("There is NO statistically significant difference")
    print("in soil moisture among different soil types.")

if p_temp < 0.05:
    print("\nTemperature is significantly related to Moisture.")
else:
    print("\nTemperature is NOT significantly related to Moisture.")

if p_hum < 0.05:
    print("Humidity is significantly related to Moisture.")
else:
    print("Humidity is NOT significantly related to Moisture.")

# 6. Save the updated dataset
data.to_csv("statistical_analysed_data.csv", index=False)
print("\nAnalysis Completed Successfully!✅")