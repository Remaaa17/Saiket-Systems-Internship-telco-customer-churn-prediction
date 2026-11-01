"""
Task 1: Data Loading and Initial Exploration
===============================================
This script loads the Telco Customer Churn dataset and performs initial exploration.

Objectives:
- Load the dataset
- Display basic information
- Check data types and structure
- Identify initial data quality issues
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

print("="*70)
print("TASK 1: DATA LOADING AND INITIAL EXPLORATION")
print("="*70)

# Load the dataset
print("\n1. Loading the dataset...")
df = pd.read_csv('Telco_Customer_Churn_Dataset  (3).csv')
print("✓ Dataset loaded successfully!")

# Display basic information
print("\n2. Dataset Shape:")
print(f"   Rows: {df.shape[0]:,}")
print(f"   Columns: {df.shape[1]}")

# Display first few rows
print("\n3. First 5 rows of the dataset:")
print(df.head())

# Display column information
print("\n4. Column Information:")
print(df.info())

# Display basic statistics
print("\n5. Basic Statistical Summary:")
print(df.describe())

# Check data types
print("\n6. Data Types:")
for col in df.columns:
    print(f"   {col:25s} : {df[col].dtype}")

# Check for missing values
print("\n7. Missing Values:")
missing = df.isnull().sum()
if missing.sum() == 0:
    print("   No missing values found!")
else:
    print(missing[missing > 0])

# Check for duplicates
print("\n8. Duplicate Rows:")
duplicates = df.duplicated().sum()
print(f"   Number of duplicate rows: {duplicates}")

# Display unique values in target variable
print("\n9. Target Variable (Churn) Distribution:")
print(df['Churn'].value_counts())
print(f"\n   Churn Rate: {(df['Churn'].value_counts()['Yes'] / len(df) * 100):.2f}%")

# Display unique values for categorical columns
print("\n10. Unique Values in Categorical Columns:")
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    print(f"   {col:25s} : {df[col].nunique()} unique values")

# Save the loaded data for next steps
print("\n11. Saving initial data...")
df.to_csv('data_loaded.csv', index=False)
print("✓ Data saved to 'data_loaded.csv'")

print("\n" + "="*70)
print("TASK 1 COMPLETED SUCCESSFULLY!")
print("="*70)
print("\nKey Findings:")
print(f"- Total customers: {len(df):,}")
print(f"- Features: {df.shape[1]}")
print(f"- Churn rate: {(df['Churn'].value_counts()['Yes'] / len(df) * 100):.2f}%")
print("\nNext Step: Run 2_data_preprocessing.py")
