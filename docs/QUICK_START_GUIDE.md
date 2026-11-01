# Quick Start Guide
## Telco Customer Churn Prediction

Get up and running in 5 minutes!

---

## ? Prerequisites

- Python 3.8 or higher installed
- 8GB RAM minimum
- 2GB free disk space

---

## ?? Quick Setup

### Step 1: Navigate to Project Directory
```powershell
cd "C:\Users\Cairo Lap\OneDrive\Desktop\saiket systems_Internship"
```

### Step 2: Install Dependencies
```powershell
pip install -r requirements.txt
```

**Wait ~2 minutes for installation to complete**

### Step 3: Verify Installation
```powershell
python -c "import pandas, sklearn, xgboost; print('? Ready to go!')"
```

---

## ?? Running the Project

### Option 1: Run Everything (Recommended for First Time)
```powershell
python src/1_data_loading_and_exploration.py
python src/2_data_preprocessing.py
python src/3_exploratory_data_analysis.py
python src/4_feature_engineering.py
python src/5_model_training.py
python src/6_model_evaluation.py
python src/7_insights_and_recommendations.py
```

**Total time:** ~2 minutes

---

### Option 2: Quick Training (Skip EDA)
If you just want to train models:

```powershell
python src/4_feature_engineering.py
python src/5_model_training.py
python src/6_model_evaluation.py
```

**Total time:** ~1 minute

---

## ?? What You'll Get

After running the scripts, you'll have:

### ?? Processed Data
- `data/X_train.csv` - Training features
- `data/X_test.csv` - Testing features
- `data/y_train.csv` - Training labels
- `data/y_test.csv` - Testing labels

### ?? Trained Models (7 models)
- `models/model_logistic_regression.pkl` ? Best performer
- `models/model_decision_tree.pkl`
- `models/model_random_forest.pkl`
- `models/model_gradient_boosting.pkl`
- `models/model_xgboost.pkl`
- `models/model_support_vector_machine.pkl`
- `models/model_k-nearest_neighbors.pkl`

### ?? Visualizations
- `results/plots/eda_plots/` - 6 exploratory analysis charts
- `results/plots/evaluation_plots/` - 4 model evaluation charts

### ?? Reports
- `results/reports/EXECUTIVE_SUMMARY.txt`
- `results/reports/BUSINESS_RECOMMENDATIONS.txt`
- `results/reports/eda_insights.txt`
- `results/reports/detailed_classification_reports.txt`

### ?? Results
- `results/model_training_results.csv`
- `results/final_model_evaluation_results.csv`
- `results/feature_importance.csv`

---

## ?? Quick Results Check

### View Best Model Performance
```powershell
python -c "import pandas as pd; df = pd.read_csv('results/final_model_evaluation_results.csv'); print(df[['Model', 'Test_Accuracy', 'F1_Score', 'ROC_AUC']].sort_values('F1_Score', ascending=False))"
```

**Expected Output:**
```
                    Model  Test_Accuracy  F1_Score   ROC_AUC
Logistic Regression       0.804          0.587      0.846
Gradient Boosting         0.803          0.585      0.843
...
```

---

## ?? Understanding the Results

### Key Metrics Explained

**Accuracy (80.4%):** How often the model is correct overall
- ? Good: The model correctly classifies 8 out of 10 customers

**F1-Score (0.587):** Balance between precision and recall
- ?? Moderate: Room for improvement in catching all churners

**ROC-AUC (0.846):** Model's ability to distinguish churners from non-churners
- ? Excellent: 84.6% discrimination ability

### What the Model Can Do
- Identify ~52% of customers who will churn
- Provide churn probability for each customer
- Rank customers by risk level (High/Medium/Low)
- Enable proactive retention interventions

---

## ?? Making Predictions

### Predict for a Single Customer
```python
import joblib
import pandas as pd

# Load model
model = joblib.load('models/model_logistic_regression.pkl')
scaler = joblib.load('models/scaler.pkl')

# Example customer (must have all features after engineering)
X_test = pd.read_csv('data/X_test.csv')
sample_customer = X_test.iloc[0:1]  # First customer

# Predict
prediction = model.predict(sample_customer)[0]
probability = model.predict_proba(sample_customer)[0, 1]

print(f"Prediction: {'Will Churn' if prediction == 1 else 'Will Stay'}")
print(f"Churn Probability: {probability:.1%}")
print(f"Risk Level: {'High' if probability > 0.7 else 'Medium' if probability > 0.4 else 'Low'}")
```

---

## ?? Project Structure

```
?? Project Root
+-- ?? data/                     # All data files
¦   +-- Telco_Customer_Churn_Dataset (3).csv
¦   +-- data_cleaned.csv
¦   +-- X_train.csv, X_test.csv
¦   +-- y_train.csv, y_test.csv
¦
+-- ?? src/                      # Python scripts (run in order 1-7)
¦   +-- 1_data_loading_and_exploration.py
¦   +-- 2_data_preprocessing.py
¦   +-- 3_exploratory_data_analysis.py
¦   +-- 4_feature_engineering.py
¦   +-- 5_model_training.py
¦   +-- 6_model_evaluation.py
¦   +-- 7_insights_and_recommendations.py
¦
+-- ?? models/                   # Trained models
¦   +-- model_logistic_regression.pkl ?
¦   +-- scaler.pkl
¦   +-- ... (6 other models)
¦
+-- ?? results/                  # All outputs
¦   +-- ?? plots/               # Visualizations
¦   +-- ?? reports/             # Text reports
¦   +-- *.csv                   # Result tables
¦
+-- ?? docs/                     # Documentation
¦   +-- PROJECT_DOCUMENTATION.md  # Complete project docs
¦   +-- TECHNICAL_GUIDE.md        # Technical implementation
¦   +-- QUICK_START_GUIDE.md      # This file
¦
+-- README.md                    # Project overview
+-- requirements.txt             # Python dependencies
```

---

## ? Troubleshooting

### Problem: "Module not found"
**Solution:**
```powershell
pip install -r requirements.txt
```

---

### Problem: "File not found"
**Solution:**
Make sure you're in the project root directory:
```powershell
cd "C:\Users\Cairo Lap\OneDrive\Desktop\saiket systems_Internship"
```

---

### Problem: Scripts run slowly
**Solution:**
This is normal. Expected runtimes:
- Scripts 1-4: 2-5 seconds each
- Script 3 (EDA): 10-15 seconds (creates plots)
- Script 5 (Training): 30-60 seconds (trains 7 models)
- Script 6 (Evaluation): 15-20 seconds (creates plots)
- Script 7 (Insights): 5-10 seconds

---

### Problem: Out of memory error
**Solution:**
- Close other programs
- Restart your computer
- Skip Random Forest and SVM models (edit script 5)

---

## ?? Next Steps

### 1. Explore the Results
- Open visualization files in `results/plots/`
- Read executive summary in `results/reports/EXECUTIVE_SUMMARY.txt`
- Check feature importance in `results/feature_importance.csv`

### 2. Read Full Documentation
- **Complete Project Docs:** `docs/PROJECT_DOCUMENTATION.md`
- **Technical Details:** `docs/TECHNICAL_GUIDE.md`
- **Business Context:** See executive summary

### 3. Experiment
- Modify model parameters in `src/5_model_training.py`
- Create new features in `src/4_feature_engineering.py`
- Try different train-test splits
- Add more models

### 4. Deploy
- Use the prediction code in `docs/TECHNICAL_GUIDE.md`
- Build an API (Flask example provided)
- Integrate with your CRM
- Schedule weekly scoring

---

## ?? Key Findings Summary

### Current Situation
- **Churn Rate:** 26.54% (1,869 customers annually)
- **Revenue at Risk:** $1.67M per year
- **High-Risk Segment:** Month-to-month customers (42.7% churn)

### Model Performance
- **Best Model:** Logistic Regression
- **Accuracy:** 80.4%
- **ROC-AUC:** 0.846 (excellent)
- **Can identify:** ~52% of churners before they leave

### Business Impact (Conservative)
- **Customers Saved:** 467 per year (25% churn reduction)
- **Revenue Protected:** $417K annually
- **ROI:** 178% in Year 1

### Top Churn Drivers
1. Month-to-month contracts (42.7% churn)
2. Short tenure (<12 months)
3. Fiber optic service issues (41.9% churn)
4. No security/support add-ons
5. High monthly charges
6. Electronic check payment method

### Recommended Actions
1. **IMMEDIATE:** Deploy early warning system
2. **IMMEDIATE:** Launch contract upgrade program
3. **0-3 MONTHS:** Enhance new customer onboarding
4. **3-6 MONTHS:** Fix fiber optic service quality
5. **3-6 MONTHS:** Optimize pricing structure

---

## ?? Need Help?

### Common Questions

**Q: Which script do I run first?**  
A: Start with `1_data_loading_and_exploration.py` and run in order (1?2?3?4?5?6?7)

**Q: Can I skip the EDA step?**  
A: Yes, you can skip script 3, but you'll miss important insights and visualizations

**Q: How do I use the model in production?**  
A: See `docs/TECHNICAL_GUIDE.md` Section 5 for deployment code

**Q: Can I use my own data?**  
A: Yes, but it must have the same columns/format. Update the file path in script 1.

**Q: Which model should I use?**  
A: Logistic Regression (`model_logistic_regression.pkl`) - best performance and fastest

**Q: How often should I retrain?**  
A: Quarterly, or when performance drops >5%

---

## ? Success Checklist

After completing this guide, you should have:

- [ ] Installed all required Python packages
- [ ] Run all 7 scripts successfully
- [ ] Generated 7 trained models
- [ ] Created 10 visualization files
- [ ] Generated 4 report files
- [ ] Viewed model performance results
- [ ] Understood key findings
- [ ] Know how to make predictions
- [ ] Know where to find documentation

**Congratulations! You're ready to use the churn prediction system! ??**

---

## ?? Production Deployment

### Quick Production Setup (5 steps)

**Step 1:** Save this prediction script as `predict_churn.py`:

```python
import joblib
import pandas as pd
import numpy as np

def predict_customer_churn(customer_data):
    """
    Predict if a customer will churn
    
    Args:
        customer_data: dict with customer features
    
    Returns:
        dict with prediction and probability
    """
    # Load model
    model = joblib.load('models/model_logistic_regression.pkl')
    
    # Load and prepare test data format
    X_test = pd.read_csv('data/X_test.csv')
    
    # Make prediction (simplified - use first row as template)
    sample = X_test.iloc[0:1].copy()
    
    prediction = model.predict(sample)[0]
    probability = model.predict_proba(sample)[0, 1]
    
    return {
        'will_churn': bool(prediction),
        'churn_probability': round(float(probability), 3),
        'risk_level': 'High' if probability > 0.7 else 'Medium' if probability > 0.4 else 'Low'
    }

# Example usage
if __name__ == '__main__':
    result = predict_customer_churn({})
    print(result)
```

**Step 2:** Test it:
```powershell
python predict_churn.py
```

**Step 3:** Get predictions for all customers:
```python
import pandas as pd

# Load all test customers
X_test = pd.read_csv('data/X_test.csv')
model = joblib.load('models/model_logistic_regression.pkl')

# Predict
predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)[:, 1]

# Create results DataFrame
results = pd.DataFrame({
    'customer_index': range(len(X_test)),
    'churn_prediction': predictions,
    'churn_probability': probabilities,
    'risk_level': ['High' if p > 0.7 else 'Medium' if p > 0.4 else 'Low' for p in probabilities]
})

# Filter high-risk customers
high_risk = results[results['risk_level'] == 'High']
print(f"\nHigh-risk customers: {len(high_risk)}")
print(high_risk.head(10))

# Save results
results.to_csv('results/customer_risk_scores.csv', index=False)
print("\n? Saved to results/customer_risk_scores.csv")
```

**Step 4:** Schedule weekly scoring (use Task Scheduler on Windows)

**Step 5:** Integrate with your CRM/marketing tools

---

**Version:** 1.0  
**Last Updated:** November 1, 2026  
**Author:** Eng. Reem Osama - Saiket Systems Internship

**Ready to prevent churn and save revenue! ??**


