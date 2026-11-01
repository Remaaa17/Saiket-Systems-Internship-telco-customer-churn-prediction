"""
Task 4: Feature Engineering
============================
This script prepares features for machine learning models.

Objectives:
- Encode categorical variables
- Scale numerical features
- Create new features
- Prepare train/test split
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

print("="*70)
print("TASK 4: FEATURE ENGINEERING")
print("="*70)

# Load cleaned data
print("\n1. Loading cleaned data...")
df = pd.read_csv('data_cleaned.csv')
print(f"✓ Loaded {len(df):,} rows")

# Create a copy for feature engineering
df_fe = df.copy()

print("\n2. Creating New Features...")

# Feature 1: Tenure groups (will be one-hot encoded later)
df_fe['tenure_group'] = pd.cut(df_fe['tenure'], bins=[0, 12, 24, 48, 72], 
                                labels=['0-1 year', '1-2 years', '2-4 years', '4+ years'])
df_fe['tenure_group'] = df_fe['tenure_group'].astype(str)  # Convert to string for encoding
print("   ✓ Created 'tenure_group' feature")

# Feature 2: Average monthly charges per tenure month
df_fe['avg_monthly_charges'] = df_fe['TotalCharges'] / (df_fe['tenure'] + 1)  # +1 to avoid division by zero
print("   ✓ Created 'avg_monthly_charges' feature")

# Feature 3: Has multiple services
service_cols = ['PhoneService', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 
                'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']

df_fe['num_services'] = 0
for col in service_cols:
    df_fe['num_services'] += (df_fe[col].isin(['Yes', 'DSL', 'Fiber optic'])).astype(int)

print("   ✓ Created 'num_services' feature")

# Feature 4: Has premium services
df_fe['has_online_security'] = (df_fe['OnlineSecurity'] == 'Yes').astype(int)
df_fe['has_tech_support'] = (df_fe['TechSupport'] == 'Yes').astype(int)
df_fe['has_premium_services'] = df_fe['has_online_security'] + df_fe['has_tech_support']
print("   ✓ Created premium service features")

print(f"\n   Total new features created: 5")

print("\n3. Encoding Categorical Variables...")

# Drop customerID as it's not useful for prediction
df_fe = df_fe.drop('customerID', axis=1)
print("   ✓ Dropped 'customerID' column")

# Identify categorical columns
categorical_cols = df_fe.select_dtypes(include=['object']).columns.tolist()
categorical_cols.remove('Churn')  # Remove target variable

print(f"   Found {len(categorical_cols)} categorical features to encode")

# Label encode binary categorical variables
binary_cols = ['gender', 'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling', 'SeniorCitizen']
le = LabelEncoder()

for col in binary_cols:
    if col in df_fe.columns:
        df_fe[col] = le.fit_transform(df_fe[col])
        print(f"   ✓ Label encoded: {col}")

# One-hot encode multi-class categorical variables
multi_class_cols = [col for col in categorical_cols if col not in binary_cols]

print(f"\n   One-hot encoding {len(multi_class_cols)} multi-class features...")
df_fe = pd.get_dummies(df_fe, columns=multi_class_cols, drop_first=True)
print(f"   ✓ Dataset shape after encoding: {df_fe.shape}")

print("\n4. Preparing Target Variable...")

# Encode target variable (Churn)
df_fe['Churn'] = le.fit_transform(df_fe['Churn'])  # No=0, Yes=1
print("   ✓ Encoded 'Churn': No=0, Yes=1")

print("\n5. Feature Scaling...")

# Separate features and target
X = df_fe.drop('Churn', axis=1)
y = df_fe['Churn']

print(f"   Features shape: {X.shape}")
print(f"   Target shape: {y.shape}")

# Identify numerical columns for scaling
numerical_cols = ['tenure', 'MonthlyCharges', 'TotalCharges', 'avg_monthly_charges', 'num_services']

# Scale numerical features
scaler = StandardScaler()
X_scaled = X.copy()
X_scaled[numerical_cols] = scaler.fit_transform(X[numerical_cols])

print(f"   ✓ Scaled {len(numerical_cols)} numerical features")

print("\n6. Train-Test Split...")

# Split data into train and test sets (80-20 split)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, 
                                                      random_state=42, stratify=y)

print(f"   Train set size: {len(X_train):,} ({len(X_train)/len(X)*100:.1f}%)")
print(f"   Test set size:  {len(X_test):,} ({len(X_test)/len(X)*100:.1f}%)")

# Check class distribution
print("\n   Target distribution in train set:")
print(f"   - No Churn (0): {(y_train==0).sum():,} ({(y_train==0).sum()/len(y_train)*100:.1f}%)")
print(f"   - Churn (1):    {(y_train==1).sum():,} ({(y_train==1).sum()/len(y_train)*100:.1f}%)")

print("\n7. Saving Processed Data...")

# Save processed data
X_train.to_csv('X_train.csv', index=False)
X_test.to_csv('X_test.csv', index=False)
y_train.to_csv('y_train.csv', index=False)
y_test.to_csv('y_test.csv', index=False)

# Save feature names
feature_names = X_train.columns.tolist()
pd.DataFrame({'feature': feature_names}).to_csv('feature_names.csv', index=False)

# Save scaler for future use
import joblib
joblib.dump(scaler, 'scaler.pkl')

print("   ✓ X_train.csv")
print("   ✓ X_test.csv")
print("   ✓ y_train.csv")
print("   ✓ y_test.csv")
print("   ✓ feature_names.csv")
print("   ✓ scaler.pkl")

print("\n8. Feature Engineering Summary:")
print(f"   Original features: {df.shape[1]}")
print(f"   Final features: {X_train.shape[1]}")
print(f"   New features created: 5")
print(f"   Total samples: {len(df):,}")
print(f"   Training samples: {len(X_train):,}")
print(f"   Testing samples: {len(X_test):,}")

print("\n" + "="*70)
print("TASK 4 COMPLETED SUCCESSFULLY!")
print("="*70)
print("\nKey Achievements:")
print("✓ New features created")
print("✓ Categorical variables encoded")
print("✓ Numerical features scaled")
print("✓ Train-test split completed")
print("\nNext Step: Run 5_model_training.py")
