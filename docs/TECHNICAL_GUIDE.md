# Technical Implementation Guide
## Telco Customer Churn Prediction

---

## Table of Contents
1. [Environment Setup](#environment-setup)
2. [Data Pipeline](#data-pipeline)
3. [Model Training Process](#model-training-process)
4. [Model Evaluation](#model-evaluation)
5. [Production Deployment](#production-deployment)
6. [API Documentation](#api-documentation)
7. [Troubleshooting](#troubleshooting)

---

## 1. Environment Setup

### 1.1 System Requirements
```
OS: Windows 10/11, Linux, macOS
Python: 3.8 or higher
RAM: 8GB minimum (16GB recommended)
Disk Space: 2GB free space
```

### 1.2 Installation Steps

#### Step 1: Clone or Download Project
```bash
cd "C:\Users\Cairo Lap\OneDrive\Desktop\saiket systems_Internship"
```

#### Step 2: Create Virtual Environment (Recommended)
```powershell
# Windows PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Dependencies
```powershell
pip install -r requirements.txt
```

#### Step 4: Verify Installation
```python
python -c "import pandas, numpy, sklearn, xgboost; print('? All packages installed')"
```

### 1.3 Required Libraries
```
pandas==2.0.3
numpy==1.24.3
scikit-learn==1.3.0
xgboost==1.7.6
matplotlib==3.7.2
seaborn==0.12.2
joblib==1.3.1
```

---

## 2. Data Pipeline

### 2.1 Data Flow Architecture
```
Raw Data ? Load ? Clean ? Explore ? Engineer Features ? 
Train Models ? Evaluate ? Generate Insights
```

### 2.2 Script Execution Order

#### Script 1: Data Loading (1_data_loading_and_exploration.py)
**Purpose:** Load dataset and perform initial exploration

```powershell
python src/1_data_loading_and_exploration.py
```

**Inputs:**
- `data/Telco_Customer_Churn_Dataset (3).csv` (raw data)

**Outputs:**
- `data/data_loaded.csv`
- Console output with dataset statistics

**Key Operations:**
- Load CSV file
- Check data types
- Identify missing values
- Display basic statistics
- Show churn distribution

**Expected Runtime:** 2-5 seconds

---

#### Script 2: Data Preprocessing (2_data_preprocessing.py)
**Purpose:** Clean data and handle data quality issues

```powershell
python src/2_data_preprocessing.py
```

**Inputs:**
- `data/data_loaded.csv`

**Outputs:**
- `data/data_cleaned.csv`

**Key Operations:**
- Convert TotalCharges to numeric
- Fill missing values (11 records)
- Remove duplicates (if any)
- Convert SeniorCitizen to categorical
- Outlier detection

**Data Quality Fixes:**
```python
# Missing TotalCharges handling
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.loc[df['tenure'] == 0, 'TotalCharges'] = 0
df.loc[mask, 'TotalCharges'] = df.loc[mask, 'MonthlyCharges'] * df.loc[mask, 'tenure']
```

**Expected Runtime:** 2-5 seconds

---

#### Script 3: Exploratory Data Analysis (3_exploratory_data_analysis.py)
**Purpose:** Analyze patterns and relationships in data

```powershell
python src/3_exploratory_data_analysis.py
```

**Inputs:**
- `data/data_cleaned.csv`

**Outputs:**
- `results/plots/eda_plots/` (6 visualizations)
  - 1_churn_distribution.png
  - 2_demographics_vs_churn.png
  - 3_services_vs_churn.png
  - 4_contract_payment_vs_churn.png
  - 5_numerical_features_distribution.png
  - 6_correlation_matrix.png
- `results/reports/eda_insights.txt`

**Visualizations Generated:**
1. **Churn Distribution:** Pie chart showing 73.46% vs 26.54%
2. **Demographics vs Churn:** Gender, senior citizen, partner, dependents
3. **Services vs Churn:** Internet, phone, add-on services
4. **Contract & Payment:** Contract type and payment method impact
5. **Numerical Distributions:** Tenure, charges distributions
6. **Correlation Matrix:** Feature relationships heatmap

**Expected Runtime:** 10-15 seconds

---

#### Script 4: Feature Engineering (4_feature_engineering.py)
**Purpose:** Prepare features for machine learning

```powershell
python src/4_feature_engineering.py
```

**Inputs:**
- `data/data_cleaned.csv`

**Outputs:**
- `data/X_train.csv` (5,634 rows × 39 features)
- `data/X_test.csv` (1,409 rows × 39 features)
- `data/y_train.csv` (5,634 rows)
- `data/y_test.csv` (1,409 rows)
- `results/feature_names.csv`
- `models/scaler.pkl`

**Feature Engineering Operations:**

**New Features Created:**
```python
# 1. Tenure groups
df['tenure_group'] = pd.cut(df['tenure'], 
                            bins=[0, 12, 24, 48, 72], 
                            labels=['0-1 year', '1-2 years', '2-4 years', '4+ years'])

# 2. Average monthly charges
df['avg_monthly_charges'] = df['TotalCharges'] / (df['tenure'] + 1)

# 3. Number of services
service_cols = ['PhoneService', 'InternetService', 'OnlineSecurity', ...]
df['num_services'] = sum of active services (0-8)

# 4. Has online security
df['has_online_security'] = (df['OnlineSecurity'] == 'Yes').astype(int)

# 5. Has tech support
df['has_tech_support'] = (df['TechSupport'] == 'Yes').astype(int)

# 6. Has premium services
df['has_premium_services'] = has_online_security + has_tech_support
```

**Encoding Strategy:**
```python
# Binary features ? Label Encoding (0/1)
binary_cols = ['gender', 'Partner', 'Dependents', 'PhoneService', 
               'PaperlessBilling', 'SeniorCitizen']
# Encoded: No=0, Yes=1

# Multi-class features ? One-Hot Encoding
multi_class_cols = ['Contract', 'PaymentMethod', 'InternetService', 
                    'MultipleLines', 'OnlineSecurity', ...]
# One-hot with drop_first=True
```

**Feature Scaling:**
```python
# StandardScaler on numerical features
numerical_cols = ['tenure', 'MonthlyCharges', 'TotalCharges', 
                  'avg_monthly_charges', 'num_services']
scaler = StandardScaler()
X_scaled[numerical_cols] = scaler.fit_transform(X[numerical_cols])
```

**Train-Test Split:**
```python
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, 
    test_size=0.2,      # 80-20 split
    random_state=42,    # Reproducibility
    stratify=y          # Maintain class distribution
)
```

**Expected Runtime:** 3-8 seconds

---

#### Script 5: Model Training (5_model_training.py)
**Purpose:** Train multiple machine learning models

```powershell
python src/5_model_training.py
```

**Inputs:**
- `data/X_train.csv`
- `data/y_train.csv`
- `data/X_test.csv`
- `data/y_test.csv`

**Outputs:**
- `models/model_logistic_regression.pkl`
- `models/model_decision_tree.pkl`
- `models/model_random_forest.pkl`
- `models/model_gradient_boosting.pkl`
- `models/model_xgboost.pkl`
- `models/model_support_vector_machine.pkl`
- `models/model_k-nearest_neighbors.pkl`
- `results/model_training_results.csv`

**Models Configuration:**

**1. Logistic Regression:**
```python
LogisticRegression(
    max_iter=1000,
    solver='lbfgs',
    class_weight='balanced',
    random_state=42
)
```

**2. Decision Tree:**
```python
DecisionTreeClassifier(
    max_depth=5,
    min_samples_split=50,
    min_samples_leaf=20,
    class_weight='balanced',
    random_state=42
)
```

**3. Random Forest:**
```python
RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    min_samples_split=50,
    class_weight='balanced',
    random_state=42,
    n_jobs=-1
)
```

**4. Gradient Boosting:**
```python
GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)
```

**5. XGBoost:**
```python
XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    scale_pos_weight=2.77,  # Handle imbalance
    random_state=42,
    use_label_encoder=False,
    eval_metric='logloss'
)
```

**6. Support Vector Machine:**
```python
SVC(
    kernel='rbf',
    C=1.0,
    gamma='scale',
    class_weight='balanced',
    probability=True,  # For ROC curves
    random_state=42
)
```

**7. K-Nearest Neighbors:**
```python
KNeighborsClassifier(
    n_neighbors=5,
    weights='uniform',
    metric='minkowski',
    n_jobs=-1
)
```

**Training Process:**
```python
for model_name, model in models.items():
    start_time = time.time()
    model.fit(X_train, y_train)
    training_time = time.time() - start_time
    
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    # Save model
    joblib.dump(model, f'models/model_{model_name}.pkl')
```

**Expected Runtime:** 30-60 seconds (SVM takes longest ~25s)

---

#### Script 6: Model Evaluation (6_model_evaluation.py)
**Purpose:** Compare models and generate evaluation visualizations

```powershell
python src/6_model_evaluation.py
```

**Inputs:**
- All 7 model files from `models/`
- `data/X_test.csv`
- `data/y_test.csv`

**Outputs:**
- `results/final_model_evaluation_results.csv`
- `results/reports/detailed_classification_reports.txt`
- `results/plots/evaluation_plots/`:
  - 1_confusion_matrices.png (7 models)
  - 2_roc_curves.png (all models overlaid)
  - 3_precision_recall_curves.png
  - 4_performance_comparison.png (bar chart)

**Evaluation Metrics:**
```python
# For each model
metrics = {
    'accuracy': accuracy_score(y_test, y_pred),
    'precision': precision_score(y_test, y_pred),
    'recall': recall_score(y_test, y_pred),
    'f1_score': f1_score(y_test, y_pred),
    'roc_auc': roc_auc_score(y_test, y_pred_proba)
}

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
# [[TN, FP],
#  [FN, TP]]

# Classification report
report = classification_report(y_test, y_pred)
```

**ROC Curve Generation:**
```python
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
roc_auc = auc(fpr, tpr)

plt.plot(fpr, tpr, label=f'{model_name} (AUC = {roc_auc:.3f})')
```

**Expected Runtime:** 15-20 seconds

---

#### Script 7: Insights and Recommendations (7_insights_and_recommendations.py)
**Purpose:** Generate business insights and recommendations

```powershell
python src/7_insights_and_recommendations.py
```

**Inputs:**
- `models/model_logistic_regression.pkl` (best model)
- `data/X_train.csv`
- `results/feature_names.csv`
- `data/data_cleaned.csv`

**Outputs:**
- `results/feature_importance.csv`
- `results/reports/EXECUTIVE_SUMMARY.txt`
- `results/reports/BUSINESS_RECOMMENDATIONS.txt`

**Feature Importance Calculation:**
```python
# Get coefficients from logistic regression
model = joblib.load('models/model_logistic_regression.pkl')
coefficients = abs(model.coef_[0])
feature_names = X_train.columns

# Normalize to get importance percentages
importance = coefficients / coefficients.sum()

# Create dataframe
feature_importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importance
}).sort_values('Importance', ascending=False)
```

**Business Metrics Calculation:**
```python
# Current state
total_customers = len(df)
churned_customers = len(df[df['Churn'] == 'Yes'])
churn_rate = churned_customers / total_customers

# Financial impact
avg_monthly_revenue = df['MonthlyCharges'].mean()
annual_revenue_at_risk = churned_customers * avg_monthly_revenue * 12

# Intervention scenarios
conservative_save_rate = 0.25
customers_saved = churned_customers * conservative_save_rate
revenue_protected = customers_saved * avg_monthly_revenue * 12
```

**Expected Runtime:** 5-10 seconds

---

## 3. Model Training Process

### 3.1 Complete Training Pipeline
```powershell
# Run all scripts in sequence
python src/1_data_loading_and_exploration.py
python src/2_data_preprocessing.py
python src/3_exploratory_data_analysis.py
python src/4_feature_engineering.py
python src/5_model_training.py
python src/6_model_evaluation.py
python src/7_insights_and_recommendations.py
```

**Total Pipeline Runtime:** ~2 minutes

### 3.2 Quick Training (Skip EDA)
```powershell
# Minimal pipeline if data is already clean
python src/4_feature_engineering.py
python src/5_model_training.py
python src/6_model_evaluation.py
```

---

## 4. Model Evaluation

### 4.1 Loading Trained Models
```python
import joblib

# Load best model
model = joblib.load('models/model_logistic_regression.pkl')

# Load scaler
scaler = joblib.load('models/scaler.pkl')

# Load feature names
feature_names = pd.read_csv('results/feature_names.csv')['feature'].tolist()
```

### 4.2 Making Predictions
```python
import pandas as pd
import numpy as np

# Load test data
X_test = pd.read_csv('data/X_test.csv')
y_test = pd.read_csv('data/y_test.csv')

# Make predictions
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]

# Get predictions with probabilities
results = pd.DataFrame({
    'actual': y_test.values.ravel(),
    'predicted': y_pred,
    'churn_probability': y_pred_proba
})

# Filter high-risk customers
high_risk = results[results['churn_probability'] > 0.7]
print(f"High-risk customers: {len(high_risk)}")
```

### 4.3 Model Interpretation
```python
# Get feature importance
feature_importance = pd.read_csv('results/feature_importance.csv')
top_10 = feature_importance.head(10)

print("Top 10 Most Important Features:")
print(top_10)
```

---

## 5. Production Deployment

### 5.1 Prediction Function
```python
import joblib
import pandas as pd
import numpy as np

def predict_churn(customer_data):
    """
    Predict churn for a single customer or batch
    
    Args:
        customer_data: dict or DataFrame with customer features
    
    Returns:
        dict with prediction, probability, and risk level
    """
    # Load model and scaler
    model = joblib.load('models/model_logistic_regression.pkl')
    scaler = joblib.load('models/scaler.pkl')
    
    # Convert to DataFrame if dict
    if isinstance(customer_data, dict):
        df = pd.DataFrame([customer_data])
    else:
        df = customer_data.copy()
    
    # Feature engineering (apply same transformations as training)
    df = engineer_features(df)
    
    # Scale numerical features
    numerical_cols = ['tenure', 'MonthlyCharges', 'TotalCharges', 
                      'avg_monthly_charges', 'num_services']
    df[numerical_cols] = scaler.transform(df[numerical_cols])
    
    # Make prediction
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0, 1]
    
    # Determine risk level
    if probability >= 0.7:
        risk_level = "High"
    elif probability >= 0.4:
        risk_level = "Medium"
    else:
        risk_level = "Low"
    
    return {
        'churn_prediction': 'Yes' if prediction == 1 else 'No',
        'churn_probability': round(probability, 3),
        'risk_level': risk_level
    }

def engineer_features(df):
    """Apply same feature engineering as training"""
    # Create tenure groups
    df['tenure_group'] = pd.cut(df['tenure'], 
                                bins=[0, 12, 24, 48, 72], 
                                labels=['0-1 year', '1-2 years', '2-4 years', '4+ years'])
    
    # Calculate average monthly charges
    df['avg_monthly_charges'] = df['TotalCharges'] / (df['tenure'] + 1)
    
    # Count services
    service_cols = ['PhoneService', 'InternetService', 'OnlineSecurity', 
                    'OnlineBackup', 'DeviceProtection', 'TechSupport', 
                    'StreamingTV', 'StreamingMovies']
    df['num_services'] = 0
    for col in service_cols:
        df['num_services'] += (df[col].isin(['Yes', 'DSL', 'Fiber optic'])).astype(int)
    
    # Premium services
    df['has_online_security'] = (df['OnlineSecurity'] == 'Yes').astype(int)
    df['has_tech_support'] = (df['TechSupport'] == 'Yes').astype(int)
    df['has_premium_services'] = df['has_online_security'] + df['has_tech_support']
    
    # Encode and one-hot encode
    # (Same logic as training script)
    
    return df
```

### 5.2 Flask API Example
```python
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model at startup
model = joblib.load('models/model_logistic_regression.pkl')
scaler = joblib.load('models/scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from request
        data = request.get_json()
        
        # Make prediction
        result = predict_churn(data)
        
        return jsonify(result), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/batch_predict', methods=['POST'])
def batch_predict():
    try:
        # Get CSV file
        file = request.files['file']
        df = pd.read_csv(file)
        
        # Make predictions
        results = []
        for idx, row in df.iterrows():
            pred = predict_churn(row.to_dict())
            pred['customer_id'] = row.get('customerID', idx)
            results.append(pred)
        
        return jsonify(results), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
```

**Start API:**
```powershell
python api.py
```

**Test API:**
```powershell
# Test health endpoint
curl http://localhost:5000/health

# Test prediction
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\"customerID\":\"1234\", \"tenure\":12, \"MonthlyCharges\":65.5, ...}"
```

---

## 6. API Documentation

### 6.1 Prediction Endpoint

**Endpoint:** `POST /predict`

**Request Format:**
```json
{
  "customerID": "7590-VHVEG",
  "gender": "Female",
  "SeniorCitizen": "No",
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "No",
  "StreamingMovies": "No",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 65.50,
  "TotalCharges": 786.00
}
```

**Response Format:**
```json
{
  "churn_prediction": "Yes",
  "churn_probability": 0.735,
  "risk_level": "High"
}
```

### 6.2 Batch Prediction Endpoint

**Endpoint:** `POST /batch_predict`

**Request:** Multipart form-data with CSV file

**Response:**
```json
[
  {
    "customer_id": "7590-VHVEG",
    "churn_prediction": "Yes",
    "churn_probability": 0.735,
    "risk_level": "High"
  },
  {
    "customer_id": "5575-GNVDE",
    "churn_prediction": "No",
    "churn_probability": 0.123,
    "risk_level": "Low"
  }
]
```

---

## 7. Troubleshooting

### 7.1 Common Issues

#### Issue: Import Error - Module not found
```
ModuleNotFoundError: No module named 'pandas'
```

**Solution:**
```powershell
pip install -r requirements.txt
# OR install individually
pip install pandas numpy scikit-learn xgboost matplotlib seaborn joblib
```

---

#### Issue: File Not Found Error
```
FileNotFoundError: data/Telco_Customer_Churn_Dataset (3).csv
```

**Solution:**
- Ensure you're running scripts from project root
- Check that data file exists in `data/` folder
- Use correct path separators for your OS

---

#### Issue: Memory Error during training
```
MemoryError: Unable to allocate array
```

**Solution:**
- Close other applications
- Reduce dataset size for testing
- Use simpler models (skip Random Forest/SVM)
- Increase system virtual memory

---

#### Issue: Scikit-learn version mismatch
```
ValueError: The feature names should match those that were passed during fit.
```

**Solution:**
```powershell
pip install scikit-learn==1.3.0 --upgrade
```

---

#### Issue: XGBoost warning about eval_metric
```
WARNING: eval_metric is deprecated
```

**Solution:** Already handled in code with:
```python
XGBClassifier(use_label_encoder=False, eval_metric='logloss')
```

---

### 7.2 Performance Optimization

#### Speed up training:
```python
# Use fewer estimators for testing
RandomForestClassifier(n_estimators=50)  # Instead of 100

# Enable parallel processing
RandomForestClassifier(n_jobs=-1)  # Use all CPU cores
```

#### Reduce memory usage:
```python
# Use float32 instead of float64
X = X.astype('float32')

# Clear variables
del df_intermediate
import gc
gc.collect()
```

---

### 7.3 Debugging Tips

#### Enable verbose logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)

# For scikit-learn models
model = RandomForestClassifier(verbose=2)
```

#### Check data at each step:
```python
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"Missing values: {df.isnull().sum().sum()}")
print(f"Data types:\n{df.dtypes}")
```

#### Validate predictions:
```python
assert len(y_pred) == len(y_test), "Prediction length mismatch"
assert all((y_pred == 0) | (y_pred == 1)), "Invalid predictions"
```

---

## 8. Advanced Usage

### 8.1 Cross-Validation
```python
from sklearn.model_selection import cross_val_score

# 5-fold cross-validation
scores = cross_val_score(model, X_train, y_train, cv=5, scoring='f1')
print(f"CV F1-Score: {scores.mean():.3f} (+/- {scores.std():.3f})")
```

### 8.2 Hyperparameter Tuning
```python
from sklearn.model_selection import GridSearchCV

# Define parameter grid
param_grid = {
    'C': [0.1, 1, 10],
    'max_iter': [500, 1000]
}

# Grid search
grid_search = GridSearchCV(LogisticRegression(), param_grid, cv=5, scoring='f1')
grid_search.fit(X_train, y_train)

print(f"Best parameters: {grid_search.best_params_}")
print(f"Best F1-score: {grid_search.best_score_:.3f}")
```

### 8.3 Feature Selection
```python
from sklearn.feature_selection import SelectKBest, f_classif

# Select top 20 features
selector = SelectKBest(f_classif, k=20)
X_train_selected = selector.fit_transform(X_train, y_train)
X_test_selected = selector.transform(X_test)

# Get selected features
selected_features = X_train.columns[selector.get_support()].tolist()
```

---

## 9. Maintenance

### 9.1 Model Retraining
**Frequency:** Quarterly or when performance drops >5%

```python
# Retrain with new data
new_data = pd.read_csv('data/new_customer_data.csv')

# Combine with existing data
df_combined = pd.concat([df_old, new_data], ignore_index=True)

# Re-run entire pipeline
# ... (same steps as initial training)
```

### 9.2 Performance Monitoring
```python
# Calculate weekly metrics
weekly_metrics = {
    'week': week_number,
    'accuracy': accuracy_score(y_true, y_pred),
    'f1_score': f1_score(y_true, y_pred),
    'num_predictions': len(y_pred)
}

# Log to tracking system
performance_log.append(weekly_metrics)

# Alert if degradation
if weekly_metrics['f1_score'] < 0.55:  # 5% drop from 0.587
    send_alert("Model performance degraded")
```

---

**Document Version:** 1.0  
**Last Updated:** November 1, 2026  
**Author:** Eng. Reem Osama - Saiket Systems Internship


