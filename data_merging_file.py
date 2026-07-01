# Here I have imported pandas library in my programme(code).
import pandas as pd # Is the Library for opening(reading) the files and contanation of the files 
#                      we have aploadedin our IDE(Vs Code)
import glob  # This is the module for command a python to look for any file matching the requirements

# Loading of the data in AGE219/
datas = glob.glob("AGE219/Practical_data/*.csv")

# Collection of all data in a list
list_of_data = [pd.read_csv(data) for data in datas]

# Data merging script
merged_data = pd.concat(list_of_data,ignore_index=True)

# Creating the file for the merged data
merged_data.to_csv("general_data_file.csv",index=False)

print("The data file merging is completed successful!👍")