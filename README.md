# AGE219 Capstone Project: Soil Moisture Analysis and Visualization

## Author

**Name:** Andrea Ibrahim Deus
**Registration Number:** BPE/D/2024/0020
**Course:** AGE 219 – Basics of Computer Programming
**Institution:** Sokoine University of Agriculture (SUA)

---

## Project Overview

This project investigates the relationship between **soil moisture, temperature, humidity, and soil type** in agricultural fields. The goal is to determine whether soil moisture varies among different soil types and whether environmental factors such as temperature and humidity can be used to predict soil moisture levels.

---

## Problem Statement

Efficient water management is essential in agriculture. Understanding how soil moisture responds to environmental conditions can help improve irrigation planning and crop productivity. This project analyzes soil sensor data to identify patterns and relationships between soil moisture, temperature, humidity, and soil type.

---

## Data Source

The dataset consists of agricultural sensor observations containing:

* Soil Type
* Temperature
* Humidity
* Soil Moisture

The data were merged and processed into a single dataset for analysis.

---

## Methodology

### Data Processing (Pandas)

* Imported and merged datasets.
* Cleaned and organized the data.
* Aggregated data using `groupby()` operations.
* Prepared data for statistical analysis.

### Scientific Computing (NumPy & SciPy)

* Converted temperature values from Fahrenheit to Celsius using NumPy.
* Calculated Pearson correlation coefficients between:

  * Temperature and Moisture
  * Humidity and Moisture
* Performed Linear Regression analysis.
* Conducted One-Way ANOVA to test differences in moisture among soil types.

### Data Visualization (Matplotlib)

Generated and exported three engineering plots:

1. **Trend Analysis Plot** – Soil moisture variation across samples.
2. **Categorical Comparison Plot** – Average moisture by soil type.
3. **Correlation Plot** – Temperature versus soil moisture with a regression trend line.

---

## Results

The statistical analysis revealed:

* The relationship between temperature and soil moisture.
* The relationship between humidity and soil moisture.
* The predictive capability of temperature through linear regression.
* Whether soil moisture differs significantly across soil types based on ANOVA testing.

---

## Visualizations

### Trend Analysis Plot

### Categorical Comparison Plot

### Correlation Plot


---

## Tools and Libraries Used

* Python
* Pandas
* NumPy
* SciPy
* Matplotlib
* Git
* GitHub
* Visual Studio Code

---

## Conclusion

This project demonstrates the use of Python's scientific computing tools to transform raw agricultural data into meaningful engineering insights. Through data cleaning, statistical analysis, and visualization, relationships between environmental factors and soil moisture were explored to support data-driven agricultural decision-making.

---

## Repository Submission

Instructor GitHub Tag:

@kadefue
