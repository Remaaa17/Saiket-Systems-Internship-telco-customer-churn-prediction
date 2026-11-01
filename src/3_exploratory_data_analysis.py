"""
Task 3: Exploratory Data Analysis (EDA)
========================================
This script performs comprehensive EDA with visualizations.

Objectives:
- Analyze churn distribution
- Explore feature relationships
- Create insightful visualizations
- Identify patterns and correlations
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set visualization style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

print("="*70)
print("TASK 3: EXPLORATORY DATA ANALYSIS")
print("="*70)

# Load cleaned data
print("\n1. Loading cleaned data...")
df = pd.read_csv('data_cleaned.csv')
print(f"✓ Loaded {len(df):,} rows")

# Create output directory for plots
import os
if not os.path.exists('eda_plots'):
    os.makedirs('eda_plots')
    print("✓ Created 'eda_plots' directory")

print("\n2. Analyzing Target Variable (Churn)...")
churn_counts = df['Churn'].value_counts()
churn_rate = (churn_counts['Yes'] / len(df)) * 100

print(f"\n   Churn Distribution:")
print(f"   - No:  {churn_counts['No']:,} ({churn_counts['No']/len(df)*100:.2f}%)")
print(f"   - Yes: {churn_counts['Yes']:,} ({churn_rate:.2f}%)")

# Plot 1: Churn Distribution
fig, ax = plt.subplots(1, 2, figsize=(14, 5))
df['Churn'].value_counts().plot(kind='bar', ax=ax[0], color=['#2ecc71', '#e74c3c'])
ax[0].set_title('Churn Distribution (Count)', fontsize=14, fontweight='bold')
ax[0].set_xlabel('Churn')
ax[0].set_ylabel('Count')
ax[0].set_xticklabels(['No', 'Yes'], rotation=0)

df['Churn'].value_counts(normalize=True).plot(kind='pie', ax=ax[1], autopct='%1.1f%%', 
                                               colors=['#2ecc71', '#e74c3c'], startangle=90)
ax[1].set_title('Churn Distribution (Percentage)', fontsize=14, fontweight='bold')
ax[1].set_ylabel('')
plt.tight_layout()
plt.savefig('eda_plots/1_churn_distribution.png', dpi=300, bbox_inches='tight')
print("   ✓ Plot saved: 1_churn_distribution.png")
plt.close()

print("\n3. Analyzing Demographic Features...")

# Plot 2: Demographics vs Churn
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
demographic_features = ['gender', 'SeniorCitizen', 'Partner', 'Dependents']

for idx, feature in enumerate(demographic_features):
    ax = axes[idx//2, idx%2]
    churn_data = df.groupby([feature, 'Churn']).size().unstack()
    churn_data.plot(kind='bar', ax=ax, color=['#2ecc71', '#e74c3c'])
    ax.set_title(f'Churn by {feature}', fontsize=12, fontweight='bold')
    ax.set_xlabel(feature)
    ax.set_ylabel('Count')
    ax.legend(title='Churn', labels=['No', 'Yes'])
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)

plt.tight_layout()
plt.savefig('eda_plots/2_demographics_vs_churn.png', dpi=300, bbox_inches='tight')
print("   ✓ Plot saved: 2_demographics_vs_churn.png")
plt.close()

print("\n4. Analyzing Service Features...")

# Plot 3: Services vs Churn
service_features = ['PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity']
fig, axes = plt.subplots(2, 2, figsize=(16, 10))

for idx, feature in enumerate(service_features):
    ax = axes[idx//2, idx%2]
    churn_rate_by_feature = df.groupby(feature)['Churn'].apply(lambda x: (x=='Yes').sum()/len(x)*100)
    churn_rate_by_feature.plot(kind='bar', ax=ax, color='#3498db')
    ax.set_title(f'Churn Rate by {feature}', fontsize=12, fontweight='bold')
    ax.set_xlabel(feature)
    ax.set_ylabel('Churn Rate (%)')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    ax.axhline(y=churn_rate, color='r', linestyle='--', label=f'Overall Churn Rate ({churn_rate:.1f}%)')
    ax.legend()

plt.tight_layout()
plt.savefig('eda_plots/3_services_vs_churn.png', dpi=300, bbox_inches='tight')
print("   ✓ Plot saved: 3_services_vs_churn.png")
plt.close()

print("\n5. Analyzing Contract and Payment Features...")

# Plot 4: Contract, Payment, and Billing vs Churn
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
contract_features = ['Contract', 'PaymentMethod', 'PaperlessBilling']

for idx, feature in enumerate(contract_features):
    ax = axes[idx]
    churn_rate_by_feature = df.groupby(feature)['Churn'].apply(lambda x: (x=='Yes').sum()/len(x)*100)
    churn_rate_by_feature.plot(kind='bar', ax=ax, color='#9b59b6')
    ax.set_title(f'Churn Rate by {feature}', fontsize=12, fontweight='bold')
    ax.set_xlabel(feature)
    ax.set_ylabel('Churn Rate (%)')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    ax.axhline(y=churn_rate, color='r', linestyle='--', label=f'Overall ({churn_rate:.1f}%)')
    ax.legend()

plt.tight_layout()
plt.savefig('eda_plots/4_contract_payment_vs_churn.png', dpi=300, bbox_inches='tight')
print("   ✓ Plot saved: 4_contract_payment_vs_churn.png")
plt.close()

print("\n6. Analyzing Numerical Features...")

# Plot 5: Numerical features distribution
numerical_features = ['tenure', 'MonthlyCharges', 'TotalCharges']
fig, axes = plt.subplots(3, 2, figsize=(14, 12))

for idx, feature in enumerate(numerical_features):
    # Histogram
    ax1 = axes[idx, 0]
    df[df['Churn']=='No'][feature].hist(ax=ax1, bins=30, alpha=0.7, label='No Churn', color='#2ecc71')
    df[df['Churn']=='Yes'][feature].hist(ax=ax1, bins=30, alpha=0.7, label='Churn', color='#e74c3c')
    ax1.set_title(f'{feature} Distribution by Churn', fontsize=12, fontweight='bold')
    ax1.set_xlabel(feature)
    ax1.set_ylabel('Frequency')
    ax1.legend()
    
    # Box plot
    ax2 = axes[idx, 1]
    df.boxplot(column=feature, by='Churn', ax=ax2)
    ax2.set_title(f'{feature} Box Plot by Churn', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Churn')
    ax2.set_ylabel(feature)
    plt.sca(ax2)
    plt.xticks([1, 2], ['No', 'Yes'])

plt.tight_layout()
plt.savefig('eda_plots/5_numerical_features_distribution.png', dpi=300, bbox_inches='tight')
print("   ✓ Plot saved: 5_numerical_features_distribution.png")
plt.close()

print("\n7. Correlation Analysis...")

# Create numerical version of data for correlation
df_encoded = df.copy()
# Encode binary categorical variables
binary_cols = ['gender', 'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling', 'Churn', 'SeniorCitizen']
for col in binary_cols:
    if col in df_encoded.columns:
        df_encoded[col] = df_encoded[col].map({'Yes': 1, 'No': 0, 'Male': 1, 'Female': 0})

# Plot 6: Correlation heatmap
plt.figure(figsize=(12, 8))
correlation_matrix = df_encoded[['tenure', 'MonthlyCharges', 'TotalCharges', 'Churn']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Correlation Matrix - Numerical Features', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('eda_plots/6_correlation_matrix.png', dpi=300, bbox_inches='tight')
print("   ✓ Plot saved: 6_correlation_matrix.png")
plt.close()

print("\n8. Key Insights Summary:")
print("\n   a) Churn Rate Analysis:")
print(f"      - Overall churn rate: {churn_rate:.2f}%")

print("\n   b) Contract Type Impact:")
contract_churn = df.groupby('Contract')['Churn'].apply(lambda x: (x=='Yes').sum()/len(x)*100)
for contract, rate in contract_churn.items():
    print(f"      - {contract:20s}: {rate:.2f}% churn rate")

print("\n   c) Internet Service Impact:")
internet_churn = df.groupby('InternetService')['Churn'].apply(lambda x: (x=='Yes').sum()/len(x)*100)
for service, rate in internet_churn.items():
    print(f"      - {service:20s}: {rate:.2f}% churn rate")

print("\n   d) Tenure Analysis:")
print(f"      - Churned customers avg tenure: {df[df['Churn']=='Yes']['tenure'].mean():.1f} months")
print(f"      - Retained customers avg tenure: {df[df['Churn']=='No']['tenure'].mean():.1f} months")

print("\n   e) Monthly Charges Analysis:")
print(f"      - Churned customers avg charges: ${df[df['Churn']=='Yes']['MonthlyCharges'].mean():.2f}")
print(f"      - Retained customers avg charges: ${df[df['Churn']=='No']['MonthlyCharges'].mean():.2f}")

# Save insights to file
with open('eda_insights.txt', 'w') as f:
    f.write("EXPLORATORY DATA ANALYSIS - KEY INSIGHTS\n")
    f.write("="*70 + "\n\n")
    f.write(f"Overall Churn Rate: {churn_rate:.2f}%\n\n")
    f.write("Churn Rate by Contract Type:\n")
    for contract, rate in contract_churn.items():
        f.write(f"  - {contract}: {rate:.2f}%\n")
    f.write("\nChurn Rate by Internet Service:\n")
    for service, rate in internet_churn.items():
        f.write(f"  - {service}: {rate:.2f}%\n")

print("\n✓ Insights saved to 'eda_insights.txt'")

print("\n" + "="*70)
print("TASK 3 COMPLETED SUCCESSFULLY!")
print("="*70)
print(f"\nGenerated {len(os.listdir('eda_plots'))} visualization plots in 'eda_plots' directory")
print("\nNext Step: Run 4_feature_engineering.py")
