#========DATA CLEANING SCRIPT===========
# 1. Loading of the Pandas Library
import pandas as pd

# 2. Loading the merged file
data = pd.read_csv("general_data_file.csv")

# 2. Assessing the data information
print(data.head())
print(data.info())
print(data.isnull().sum())

# 3. Handling missing value in column Humidity and row number 0
data.loc[0,"Humidity"] = 60

# 4. Correction of the data types
data["Humidity"] = data["Humidity"].astype(float)

# 5. Droping invalid outliers
data = data[(data["Humidity"] >= 0) & (data["Humidity"] <= 100)]

# 6. Creating the file to store the cleaned data file
data.to_csv("cleaned_data_file.csv", index=False)

# 7. Printing the message which will show if the data was cleaned and stored in the required file
print("The data was cleaned successful and stored in the file: cleaned_data_file.csv")