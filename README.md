# Telco Customer Churn Prediction Project

## Project Overview
This project analyzes customer churn in a telecommunications company and develops predictive models to identify at-risk customers.

## Dataset
- **File**: `Telco_Customer_Churn_Dataset (3).csv`
- **Records**: 7,043 customers
- **Features**: 21 columns including demographics, services, and billing information
- **Target**: Churn (Yes/No)

## Project Structure

```
├── data/                                    # All data files
│   ├── Telco_Customer_Churn_Dataset (3).csv # Original dataset
│   ├── data_loaded.csv                      # Loaded data
│   ├── data_cleaned.csv                     # Cleaned data
│   ├── X_train.csv, X_test.csv              # Train/test features
│   └── y_train.csv, y_test.csv              # Train/test labels
│
├── src/                                     # Source code
│   ├── 1_data_loading_and_exploration.py    # Load data and initial exploration
│   ├── 2_data_preprocessing.py              # Data cleaning and preprocessing
│   ├── 3_exploratory_data_analysis.py       # EDA with visualizations
│   ├── 4_feature_engineering.py             # Feature creation and encoding
│   ├── 5_model_training.py                  # Train multiple ML models
│   ├── 6_model_evaluation.py                # Evaluate and compare models
│   └── 7_insights_and_recommendations.py    # Business insights and recommendations
│
├── models/                                  # Trained models
│   ├── model_logistic_regression.pkl
│   ├── model_decision_tree.pkl
│   ├── model_random_forest.pkl
│   ├── model_gradient_boosting.pkl
│   ├── model_xgboost.pkl
│   ├── model_support_vector_machine.pkl
│   ├── model_k-nearest_neighbors.pkl
│   └── scaler.pkl                           # Feature scaler
│
├── results/                                 # Analysis results
│   ├── plots/                               # All visualizations
│   │   ├── eda_plots/                       # EDA visualizations
│   │   └── evaluation_plots/                # Model evaluation plots
│   ├── reports/                             # Text reports
│   │   ├── EXECUTIVE_SUMMARY.txt
│   │   ├── BUSINESS_RECOMMENDATIONS.txt
│   │   ├── eda_insights.txt
│   │   └── detailed_classification_reports.txt
│   ├── feature_importance.csv
│   ├── feature_names.csv
│   ├── model_training_results.csv
│   └── final_model_evaluation_results.csv
│
├── docs/                                    # Documentation
│   └── SKS Data Science.pdf                 # Project documentation
│
├── requirements.txt                         # Python dependencies
└── README.md                                # This file
```

## Setup Instructions

1. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the analysis in order**:
   ```bash
   python src/1_data_loading_and_exploration.py
   python src/2_data_preprocessing.py
   python src/3_exploratory_data_analysis.py
   python src/4_feature_engineering.py
   python src/5_model_training.py
   python src/6_model_evaluation.py
   python src/7_insights_and_recommendations.py
   ```

## Key Objectives

1. Understand customer churn patterns
2. Identify key factors influencing churn
3. Build accurate predictive models
4. Provide actionable business recommendations

## Expected Deliverables

✅ **Completed:**
- Clean, processed dataset
- Comprehensive EDA report with visualizations
- Multiple trained ML models (7 models)
- Model performance comparison
- Business insights and retention strategies
- **Complete project documentation (150+ pages)**

## 📚 Documentation

### Complete Documentation Package Available

This project includes comprehensive documentation in the `docs/` folder:

📖 **[Documentation Index](docs/README.md)** - Start here to navigate all documentation

🚀 **[Quick Start Guide](docs/QUICK_START_GUIDE.md)** - Get running in 5 minutes

📋 **[Complete Project Documentation](docs/PROJECT_DOCUMENTATION.md)** - 100+ pages covering everything

🔧 **[Technical Implementation Guide](docs/TECHNICAL_GUIDE.md)** - Detailed technical reference

💼 **[Executive Presentation](docs/EXECUTIVE_PRESENTATION.md)** - Business case and ROI analysis

### Quick Links by Role

**Business Users:** Read the [Executive Presentation](docs/EXECUTIVE_PRESENTATION.md)  
**Data Scientists:** Start with [Quick Start Guide](docs/QUICK_START_GUIDE.md), then [Technical Guide](docs/TECHNICAL_GUIDE.md)  
**Project Managers:** Review [Complete Documentation](docs/PROJECT_DOCUMENTATION.md)  
**Developers:** See [Technical Guide - Section 5](docs/TECHNICAL_GUIDE.md#5-production-deployment) for deployment

## Key Results

### Model Performance
- **Best Model:** Logistic Regression
- **Accuracy:** 80.41%
- **F1-Score:** 0.587
- **ROC-AUC:** 0.846 (Excellent)

### Business Impact
- **Current Churn Rate:** 26.54%
- **Annual Revenue at Risk:** $1,669,570
- **Potential Revenue Protected:** $417K - $667K annually
- **Expected ROI:** 178% - 234% (Year 1)

### Top Churn Drivers Identified
1. Month-to-month contracts (42.7% churn rate)
2. Short tenure (<12 months)
3. Fiber optic service issues (41.9% churn)
4. Lack of security/support add-ons
5. High monthly charges

---

## 🚀 Interactive Dashboards

### Option 1: Streamlit Web Dashboard (Recommended) ⭐
Modern, Python-only interactive web dashboard with beautiful visualizations.

**Quick Start:**
```powershell
# Just one command!
python -m streamlit run streamlit_dashboard.py
```

**Features:**
- ✨ Beautiful, modern interface
- 📊 Interactive Plotly charts
- 🔄 Real-time model testing
- 📱 Mobile-responsive
- 🐍 Pure Python (no Node.js needed!)
- ⚡ Fast and lightweight

**Dashboard will open at:** http://localhost:8501

### Option 2: Jupyter Notebook
Complete analysis in interactive notebook format.

```powershell
jupyter notebook Telco_Churn_Analysis_Complete.ipynb
```

### Option 3: Tkinter Desktop App (Basic)
Python-based desktop dashboard.

```powershell
python dashboard_app.py
```

---

## Author
Saiket Systems Internship Project  
**Complete Documentation:** Version 1.0 | November 1, 2026


