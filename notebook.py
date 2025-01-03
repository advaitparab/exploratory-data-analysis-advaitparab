#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis - Lab
# 
# ## 🔍 Overview
# The lab is designed to be self-guided, providing solutions for each exercise to check your work and assist if you get stuck. However, it is important to first attempt to solve the problem on your own as this is the best way to learn. If you become stuck, don't give up and seek help from the instructor, peers, or even a search engine like Google. Be mindful that not all answers from a search engine may be correct, so use your judgement to determine the validity of the information. Remember, the best way to learn is to try solving the problem yourself first.
# 
# This lab is designed to help you practice exploratory data analysis using Python. You will work with one dataset: auto-mpg. You will use various data visualization and analysis techniques to gain insights and identify patterns in the data, and clean and preprocess the data to make it more suitable for analysis.
# 
# ## 🎯 Objectives
# By the end of this lab, you should be able to:
# 
# - Load and preprocess data using Python libraries such as pandas
# - Clean and preprocess the data to make it more suitable for analysis
# - Use visualization techniques to explore and understand the distribution of the variables in the data
# - Apply basic statistical analysis to derive insights from the data
# - Communicate your findings through clear and effective data visualizations and summaries

# #### Package Imports
# We will keep coming back to this cell to add "import" statements, and configure libraries as we need

# In[ ]:


import pandas as pd
from scipy.stats import trim_mean

# Configure pandas to display 500 rows; otherwise it will truncate the output
pd.set_option('display.max_rows', 500)

# To plot pretty figures
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)
plt.style.use("bmh")


# ## Auto-MPG Data
# This dataset is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license.
# 
# [Dataset Source](https://archive.ics.uci.edu/ml/datasets/auto+mpg)

# ### Exercise 1:  Load the dataset
# You've had plenty of exercise in doing this. Load the dataset into a pandas dataframe.
# 
# The dataset is available in the `data/auto-mpg.data` file. Check the file to determine the delimiter and/or the appropriate pandas method to use to load the data.
# 
# Make sure you name the variable `auto_mpg_df` and that you use the appropriate pandas method to load the data.

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#     auto_mpg_df = pd.read_table('./data/auto-mpg/auto-mpg.data', sep="\t")
#   ```
# </details>
# 

# ### Exercise 2: Confirm the data loaded correctly
# Generally, after any data import, we need to make sure we got the data imported correctly. This is especially true when we're working with data that we didn't create ourselves.
# 
# One way this can be achieved is to print/display the dataframe. but this can be problematic if the dataframe is large.
# 
# Let's explore a few different ways.
# 
# #### 2.1: Display the <u>first</u> 5 rows of the dataframe
# 

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#   auto_mpg_df.head()
#   # or 
#   # auto_mpg_df.head(5)
#   # or 
#   # auto_mpg_df.head(n=5) 
#   # or 
#   # auto_mpg_df[:5] 
#   # or 
#   # auto_mpg_df.iloc[:5] 
#   # or 
#   # auto_mpg_df.iloc[0:5] 
#   # or 
#   # auto_mpg_df.iloc[[0,1,2,3,4]] 
#   ```
# </details>

# #### 2.2: Display the <u>last</u> 5 rows of the dataframe

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#   auto_mpg_df.tail()
# ```
# </details>

# #### 2.3: Display <u>random</u> 5 rows of the dataframe
# just viewing the first and last records may not be enough. We may want to see some random records to make sure we have the data we expect.

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#   auto_mpg_df.sample(5)
# ```
# </details>

# > 🚩 This is a good point to commit your code to your repository.

# ### Exercise 3: Dataset Metadata
# Now that we've confirmed the data loaded correctly, let's take a look at the metadata for the dataset.
# 
# #### 3.1: Display the number of rows and columns in the dataframe

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#   auto_mpg_df.shape
# ```
# </details>

# #### 3.2: Display a summary about the dataframe
# 

# In[ ]:





# 
# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#   auto_mpg_df.info()
# ```
# </details>

# ### 3.3: Display the statistics for the dataframe

# In[ ]:





# <details>
#   <summary>💡 Solution </summary>
#   
#   ```python
#   auto_mpg_df.describe()
#   ```
# </details>

# > 🚩 This is a good point to commit your code to your repository.

# ### Exercise 4: Data Cleaning: Checking for Duplicate Records

# #### 4.1: Count the number of exact duplicate records in the dataset
# 
# <details>
#   <summary>🦉 Hints</summary>
# 
#   - The `duplicated()` method can be used to check for duplicate records.
#   - This method returns a boolean series indicating whether a record is a duplicate or not.
#   - You'll need to chain some other method to provide a count of the duplicate records.
# 
# </details>

# In[ ]:





# 
# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#   auto_mpg_df.duplicated().sum()
# ```
# </details>

# #### 4.2: Show the duplicate records
# using the results of the duplicated() method as a predicate to filter the dataframe, displaying the duplicate records. 

# In[ ]:





# 
# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#   auto_mpg_df[
#     auto_mpg_df.duplicated()
# ]
# ```
# </details>

# #### 4.3: Count the number of duplicate records in the dataset, based on a subset of columns
# To be fair, in this exact context, it doesn't really make sense to check for duplicate records based on a subset of columns (or maybe it does). However, we'll do that for the sake of practice.
# 
# Let's check for duplicate records based on the `mpg`, `cylinders`, `acceleration`, and `origin` columns.
# 
# <details>
#   <summary>🦉 Hints</summary>
#   
#   - You can specify a subset of columns to check for duplicates by passing a list of column names to the `subset` parameter.
# </details>

# In[ ]:





# 
# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#   auto_mpg_df.duplicated(
#     subset=['mpg', 'cylinders', 'acceleration', 'origin']
# ).sum()
# ```
# </details>

# ### Exercise 5: Data Cleaning: Dropping Duplicate Records
# #### 5.1: Drop the duplicate records
# Now that we've confirmed that there are duplicate records in the dataset, let's remove them. using the `drop_duplicates()` method.
# 
# 
# <details>
#   <summary>🦉 Hints</summary>
# 
#   - The `drop_duplicates()` method can be used to remove duplicate records.
#   - Make sure you either save the results of the method to a new variable, or use the `inplace` parameter to update the dataframe in place.
# </details>

# In[ ]:





# 
# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#   auto_mpg_df.drop_duplicates(inplace=True)
# ```
# </details>

# #### 5.2: Confirm that the duplicate records were removed
# Check the number of records in the dataframe to confirm that the duplicates were removed.

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#     auto_mpg_df.shape
#   ```
# </details>

# ### Exercise 6: Data Cleaning: Checking for Missing Values
# #### 6.1: Use `info()` to check for missing values

# In[ ]:




How many and what are the missing records? ANSWER HERE

# #### 6.2: Use `isna()` to check for missing values
# 
# <details>
#   <summary>🦉 Hints</summary>
# 
#   - The `isna()` method can be used to check for missing values.
#   - This method returns a boolean dataframe indicating whether a cell in the dataframe is missing or not.
#   - You'll need to chain some other method to provide a count of the missing records.
# 
# </details>

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#     auto_mpg_df.isna().sum()
#   ```
# </details>

# #### 6.3: Use `isnull()` to check for missing values
# <details>
#   <summary>🦉 Hints</summary>
# 
#   - The `isnull()` method can be used to check for missing values.
#   - This method returns a boolean dataframe indicating whether a cell in the dataframe is missing or not.
#   - You'll need to chain some other method to provide a count of the missing records.
# 
# </details>

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#     auto_mpg_df.isnull().sum()
#   ```
# </details>

# #### What's the difference between `isna()` and `isnull()`? what's your source?
ANSWER HERE

# ### Exercise 7: Data Cleaning: Dropping Missing Values
# 
# #### 7.1: Drop the missing values of the `mpg` column
# Now that we've confirmed that there are missing values in the dataset, let's remove them. using the `dropna()` method.
# 
# Depending on the context, and on the project you're working on, you may want to drop the missing values, or you may want to replace them with a some value. 
# 
# In working with the `auto_mpg` dataset, we'll develop a model to predict the `mpg` of a car based on the other features. So, we'll drop the missing values from the `mpg` column.
# 
# <details>
#   <summary>🦉 Hints</summary>
# 
#   - Use the subset parameter to specify the column(s) to check for missing values.
#   - Either save the results of the method to a new variable, or use the `inplace` parameter to update the dataframe in place.
# 
# </details>

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#     auto_mpg_df.dropna(
#       subset=['mpg'],
#       inplace=True
#     )
#   ```
# </details>

# #### 7.2: Confirm that the missing values in `mpg` were removed

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#     auto_mpg_df.isna().sum()
#   ```
# </details>

# ### Exercise 8: Data Cleaning: Replacing Missing Values
# Before we can determine what's the best value to replace the missing values with for the `horsepower` column, we need to understand the distribution of the values in that column.

# #### 8.1: Display the distribution of the values in the `horsepower` column
# Plot a 40-bins histogram of the values in the `horsepower` column.
# 
# 
# <details>
#   <summary>🦉 Hints</summary>
# 
#   - The `plot.hist()` method can be used to plot a histogram.
#   - You can also use the `plot()` method with the `kind` parameter set to `hist` directly on the dataframe.
#   - The `%matplotlib inline` magic command is required to display the plot in the notebook. (Already done for you on the top cell of the notebook)
# 
# </details>
# 

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#     auto_mpg_df['horsepower'].plot.hist(bins=40)
#     plt.show()
#   ```
#   OR
#   ```python
#     auto_mpg_df['horsepower'].plot(kind="hist", bins= 40)
#     plt.show()
#   ```
#   OR
#   ```python
#     auto_mpg_df.plot(y='horsepower', kind="hist", bins= 40)
#     plt.show()
#   ```
#   OR
#   ```python
#     auto_mpg_df.plot.hist(y='horsepower', bins= 40)
#     plt.show()
#   ```
#   OR 
#   ```python
#     plt.hist(auto_mpg_df['horsepower'], bins=40)
#     plt.show()
#   ```
# </details>

# #### 8.2: Calculate the mean, median, and trimmed mean for the `horsepower` column
# 
# <details>
#   <summary>🦉 Hints</summary>
# 
#   - The `mean()` method can be used to calculate the mean of a column.
#   - The `median()` method can be used to calculate the median of a column.
#   - You'll need to use the scipy library to calculate the trimmed mean.
# </details>

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#     from scipy.stats import trim_mean
#     ...
#     horsepower_mean = auto_mpg_df['horsepower'].mean()
#     horsepower_median = auto_mpg_df['horsepower'].median()
#     horsepower_trimmed_mean = trim_mean(auto_mpg_df['horsepower'], 0.1)
#   ```
# </details>

# #### 8.3: Display the central tendency measures on the distribution plot

# In[ ]:


fig, ax = plt.subplots(figsize = (8,4))

auto_mpg_df['horsepower'].plot(kind="hist", density= True, bins=40, alpha = 0.65)
auto_mpg_df['horsepower'].plot(kind="kde")

ax.axvline(horsepower_mean, alpha = 0.8, linestyle = ":")
ax.axvline(horsepower_median, alpha = 0.8, linestyle = ":")
ax.axvline(horsepower_trimmed_mean, alpha = 0.8, linestyle = ":")

# ax.set_yticklabels([])
ax.set_ylabel("")

ax.text(horsepower_mean-.1, .01, "Mean", size = 10, alpha = 0.8)
ax.text(horsepower_median-.4, .0075, "Median", size = 10, alpha = 0.8)
ax.text(horsepower_trimmed_mean+.4, .0050, "Trimmed Mean", size = 10, alpha = 0.8)

ax.tick_params(left = False, bottom = False)
for ax, spine in ax.spines.items():
    spine.set_visible(False)

plt.show()


# #### 8.4: Replace the missing values in the `horsepower` column with the median value

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#     auto_mpg_df['horsepower'].fillna(horsepower_median, inplace=True)
#   ```
# </details>

# #### 8.5: Confirm that the missing values in `horsepower` were replaced

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#     auto_mpg_df.isna().sum()
#   ```
# </details>

# ### Exercise 9: Data Cleaning: Anomalies and outliers
# There are many statistical methods to detect outliers in a dataset.
# 1. Interquartile range (IQR) method:
#   * Covered in the lecture videos
#   * This method calculates the IQR of the dataset, which is the range between the 25th and 75th percentiles of the data. Data points that are more than a certain multiple of the IQR (e.g., 1.5) away from the 25th or 75th percentile are considered anomalies.
# 2. Z-score method: 
#   * This method calculates the z-score of each data point, which measures how many standard deviations a data point is away from the mean of the dataset. 
#   * Data points that have a z-score greater than a certain threshold (e.g., 3 or 4) are considered anomalies.
# 3. Percentile method: 
#   * This method identifies data points that are in the upper or lower percentiles of the dataset.
#     * For example, data points that are in the top or bottom 1% of the dataset may be considered anomalies.
# 
# We will be exploring all 3 methods in this exercise.

# #### 9.1: Display the distribution of the values in the `displacement` column using a box plot

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#     auto_mpg_df['displacement'].plot(kind="box")
#     plt.show()
#   ```
# </details>

# #### 9.2: Calculate the IQR for the `displacement` column
# * Calculate the range between the 25th and 75th percentiles of the data. (IQR)
# * Calculate the lower and upper bound of the data. using a 1.5 multiple or the IQR. 
#   * Lower bound = 25th percentile - 1.5 * IQR
#   * Upper bound = 75th percentile + 1.5 * IQR

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#     q1 = auto_mpg_df['displacement'].quantile(0.25)
#     q3 = auto_mpg_df['displacement'].quantile(0.75)
#     iqr = q3 - q1
# 
#     print(f"Q1: {q1}, Q3: {q3}, IQR: {iqr}")
# 
#     lower_limit = q1 - 1.5 * iqr
#     upper_limit = q3 + 1.5 * iqr
# 
#     print(f"Lower Limit: {lower_limit}, Upper Limit: {upper_limit}")
#   ```
# </details>

# #### 9.3: Using Pandas filtering, show records that are outliers in the `displacement` column
# 
# <details>
#   <summary>🦉 Hints</summary>
# 
#   - You'll need to provide a predicate for pandas to filter the dataframe.
#   - You can use the `|` operator to combine multiple conditions in a Pandas filter.
# </details>

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#     auto_mpg_df[
#       (auto_mpg_df['displacement'] < lower_limit) | (auto_mpg_df['displacement'] > upper_limit)
#     ]
#   ```
# </details>

# #### 9.4: Calculate the z-score for the `displacement` column
# * Calculate the mean and standard deviation of the `displacement` column.
# * Calculate the z-score for each data point in the `displacement` column.
#   * z-score = (x - mean) / standard deviation

# In[ ]:


displacement_mean = 
displacement_std = 

print(f"Mean: {displacement_mean}, Std: {displacement_std}")


# In[ ]:


z_scores = 


# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#     displacement_mean = auto_mpg_df['displacement'].mean()
#     displacement_std = auto_mpg_df['displacement'].std()
# 
#     z_scores = (auto_mpg_df['horsepower'] - displacement_mean) / displacement_std
#   ```
# </details>

# #### 9.5: Using Pandas filtering, show records that are outliers in the `displacement` column using the z-score method

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#     auto_mpg_df[
#       (z_scores < -3) | (z_scores > 3)
#     ]
#   ```
# </details>

# #### 9.6: Using Pandas filtering, show records that are outliers in the `displacement` column using the percentile method
# we'll use a 1% threshold for this exercise.

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#     quantile_1 = auto_mpg_df['displacement'].quantile(0.01)
#     quantile_99 = auto_mpg_df['displacement'].quantile(0.99)
#     auto_mpg_df[
#       (auto_mpg_df['displacement'] < quantile_1) | (auto_mpg_df['displacement'] > quantile_99)
#     ]
#   ```
# </details>

# #### 9.7: Display the distribution of the values in the `displacement` column using a histogram

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#     auto_mpg_df.plot.hist(y='displacement', bins= 40)
#     plt.show()
#   ```
# </details>

# #### 9.8: On the historgram, display the upper and lower bounds based on the IQR method

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#     bounds = [upper_limit, lower_limit]
# 
#     # Create a histogram of the 'displacement' column
#     plt.hist(auto_mpg_df['displacement'], bins=40)
# 
#     # Add vertical lines at the percentile values
#     for bound in bounds:
#         plt.axvline(bound, color='r', linestyle='--')
# 
#     plt.show()
#   ```
# </details>

# #### 9.9: Drop the outlier records from the `displacement` column
# 
# * Don't do this in place, create a new dataframe.

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#     without_outliers = auto_mpg_df[
#       (auto_mpg_df['displacement'] > lower_limit) & (auto_mpg_df['displacement'] < upper_limit)
#     ]
#   ```
#   OR
#   ```python
#     without_outliers = auto_mpg_df.drop(
#       auto_mpg_df[
#         (auto_mpg_df['displacement'] < lower_limit) | (auto_mpg_df['displacement'] > upper_limit)
#       ].index
#     )
#   ```
# </details>

# #### 9.10: Show the shape of the original dataframe and the new dataframe to show that the outliers were dropped
# 

# In[ ]:


display(auto_mpg_df.shape)
display(without_outliers.shape)


# ### Exercise 10: Further Exploration
# 
# <details>
#   <summary>📊 Data Types Diagram</summary>
# 
#  ![Data types](https://miro.medium.com/max/1400/1*kySPZcf83qLOuaqB1vJxlg.jpeg)
# </details>

# #### 10.1: # For each of the 9 columns, Identify the data type: 
# * Numerical-Continuous
# * Numerical-Discrete
# * Categorical-Ordinal
# * Categorical-nominal
1. mpg:           
2. cylinders:     
3. displacement:  
4. horsepower:    
5. weight:        
6. acceleration:  
7. model year:    
8. origin:        
9. car name:      
# #### 10.2: Show all the possible values for the `origin` column
# 
# <details>
#   <summary>🦉 Hints</summary>
# 
#   - The `value_counts()` method can be used to show the unique values in a column.
# </details>

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#     auto_mpg_df['origin'].value_counts()
#   ```
# </details>

# **What do the values in the `origin` column represent?**

# #### **BONUS**: show a scatter plot of the `horsepower` column vs the `weight` column

# ## Wrap up
# Remember to update the self reflection and self evaluations on the `README` file.

# Make sure you run the following cell; this converts this Jupyter notebook to a Python script. and will make the process of reviewing your code on GitHub easier

# In[ ]:


# 🦉: The following command converts this Jupyter notebook to a Python script.
get_ipython().system('jupyter nbconvert --to python notebook.ipynb')


# > 🚩 **Make sure** you save the notebook and make one final commit here
