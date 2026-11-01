"""
Task 2: Data Preprocessing and Cleaning
========================================
This script cleans and preprocesses the data.

Objectives:
- Handle missing values
- Fix data type issues
- Handle outliers
- Create clean dataset for analysis
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

print("="*70)
print("TASK 2: DATA PREPROCESSING AND CLEANING")
print("="*70)

# Load the data from previous step
print("\n1. Loading data...")
df = pd.read_csv('data_loaded.csv')
print(f"✓ Loaded {len(df):,} rows")

print("\n2. Data Cleaning Process:")

# Check TotalCharges column (known issue: may contain spaces instead of numbers)
print("\n   a) Checking TotalCharges column...")
print(f"      Data type: {df['TotalCharges'].dtype}")

# Convert TotalCharges to numeric (coerce errors to NaN)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
print(f"      Converted to numeric")

# Check for missing values after conversion
missing_total_charges = df['TotalCharges'].isnull().sum()
print(f"      Missing values found: {missing_total_charges}")

if missing_total_charges > 0:
    print(f"\n   b) Handling missing values in TotalCharges...")
    # For customers with 0 tenure, TotalCharges should be 0
    df.loc[df['tenure'] == 0, 'TotalCharges'] = 0
    
    # For others, fill with median or calculate from MonthlyCharges * tenure
    mask = df['TotalCharges'].isnull()
    df.loc[mask, 'TotalCharges'] = df.loc[mask, 'MonthlyCharges'] * df.loc[mask, 'tenure']
    
    print(f"      ✓ Filled {missing_total_charges} missing values")

# Check for any remaining missing values
print("\n   c) Final missing value check:")
missing = df.isnull().sum()
if missing.sum() == 0:
    print("      ✓ No missing values!")
else:
    print("      Missing values:")
    print(missing[missing > 0])

# Remove duplicates if any
print("\n   d) Checking for duplicates...")
duplicates = df.duplicated().sum()
if duplicates > 0:
    df = df.drop_duplicates()
    print(f"      ✓ Removed {duplicates} duplicate rows")
else:
    print("      No duplicates found")

# Convert SeniorCitizen to categorical
print("\n   e) Converting data types...")
df['SeniorCitizen'] = df['SeniorCitizen'].map({0: 'No', 1: 'Yes'})
print("      ✓ SeniorCitizen converted to categorical")

# Check for outliers in numerical columns
print("\n3. Outlier Detection:")
numerical_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']

for col in numerical_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()
    print(f"   {col:20s} : {outliers:4d} outliers detected")

print("\n   Note: Outliers are kept as they represent valid business cases")

# Display cleaned data summary
print("\n4. Cleaned Dataset Summary:")
print(f"   Final shape: {df.shape}")
print(f"   Total records: {len(df):,}")
print(f"   Features: {df.shape[1]}")

print("\n5. Data Types After Cleaning:")
print(df.dtypes)

print("\n6. Statistical Summary After Cleaning:")
print(df[numerical_cols].describe())

# Save cleaned data
print("\n7. Saving cleaned data...")
df.to_csv('data_cleaned.csv', index=False)
print("✓ Cleaned data saved to 'data_cleaned.csv'")

print("\n" + "="*70)
print("TASK 2 COMPLETED SUCCESSFULLY!")
print("="*70)
print("\nKey Achievements:")
print("✓ Missing values handled")
print("✓ Data types corrected")
print("✓ Duplicates removed")
print("✓ Outliers identified")
print("\nNext Step: Run 3_exploratory_data_analysis.py")
