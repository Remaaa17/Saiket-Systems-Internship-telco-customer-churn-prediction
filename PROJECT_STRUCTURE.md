# Telco Customer Churn Prediction - Project Structure

## Overview
This document describes the complete project organization and file structure.

## Directory Structure

```
Telco_Customer_Churn_Project/
│
├── 📁 data/                              # All dataset files
│   ├── 📁 raw/                           # Original raw data
│   │   └── Telco_Customer_Churn_Dataset_Original.csv
│   └── 📁 processed/                     # Cleaned and processed data
│       ├── data_cleaned.csv              # Cleaned full dataset
│       ├── data_loaded.csv               # Initially loaded data
│       ├── X_train.csv                   # Training features
│       ├── X_test.csv                    # Testing features
│       ├── y_train.csv                   # Training labels
│       └── y_test.csv                    # Testing labels
│
├── 📁 models/                            # Trained ML models
│   ├── model_logistic_regression.pkl     # Best model (80.2% accuracy)
│   ├── model_decision_tree.pkl
│   ├── model_random_forest.pkl
│   ├── model_gradient_boosting.pkl
│   ├── model_xgboost.pkl
│   ├── model_support_vector_machine.pkl
│   ├── model_k-nearest_neighbors.pkl
│   └── scaler.pkl                        # StandardScaler for features
│
├── 📁 results/                           # Analysis outputs
│   ├── model_training_results.csv        # Initial model results
│   ├── final_model_evaluation_results.csv # Final evaluation metrics
│   ├── feature_importance.csv            # Feature rankings
│   ├── feature_names.csv                 # Feature name mappings
│   ├── detailed_classification_reports.txt
│   ├── eda_insights.txt                  # EDA findings
│   ├── BUSINESS_RECOMMENDATIONS.txt
│   ├── EXECUTIVE_SUMMARY.txt
│   └── 📁 plots/                         # Visualization images
│       ├── eda_plots/                    # Exploratory analysis charts
│       └── evaluation_plots/             # Model evaluation charts
│
├── 📁 src/                               # Python source code
│   ├── 1_data_loading_and_exploration.py
│   ├── 2_data_preprocessing.py
│   ├── 3_exploratory_data_analysis.py
│   ├── 4_feature_engineering.py
│   ├── 5_model_training.py
│   ├── 6_model_evaluation.py
│   └── 7_insights_and_recommendations.py
│
├── 📁 notebooks/                         # Jupyter notebooks
│   └── Telco_Churn_Analysis_Complete.ipynb # Complete end-to-end analysis
│
├── 📁 docs/                              # Documentation
│   ├── PROJECT_DOCUMENTATION.md          # Comprehensive project guide (100+ pages)
│   ├── TECHNICAL_GUIDE.md                # Technical implementation details
│   ├── QUICK_START_GUIDE.md              # Quick start instructions
│   ├── EXECUTIVE_PRESENTATION.md         # Executive summary presentation
│   ├── HOW_TO_RUN_DASHBOARD.md           # Dashboard setup guide
│   └── README.md                         # Documentation index
│
├── 📁 templates/                         # HTML templates
│   └── dashboard.html                    # Main dashboard template
│
├── 📁 static/                            # Static web assets
│   ├── 📁 css/
│   │   └── style.css                     # Professional styling
│   └── 📁 js/
│       ├── chart.min.js                  # Chart.js library (local)
│       └── main.js                       # Dashboard JavaScript
│
├── web_app.py                            # Flask web application
├── README.md                             # Main project README
├── requirements.txt                      # Python dependencies
└── PROJECT_STRUCTURE.md                  # This file

```

## File Descriptions

### Data Files
- **raw/**: Original unprocessed datasets
- **processed/**: Cleaned and split datasets ready for model training

### Models
- All models saved using joblib/pickle format
- Logistic Regression is the best performing model
- Scaler is used for feature normalization

### Results
- CSV files contain numerical results and metrics
- TXT files contain textual analysis and recommendations
- Plots folders contain all visualization images

### Source Code (src/)
Complete data science pipeline in 7 sequential steps:
1. Data loading and initial exploration
2. Data cleaning and preprocessing
3. Exploratory data analysis with visualizations
4. Feature engineering and transformation
5. Model training on 7 different algorithms
6. Model evaluation and comparison
7. Business insights and recommendations

### Web Dashboard
- **web_app.py**: Flask backend with REST API endpoints
- **templates/**: HTML templates with responsive design
- **static/**: CSS styling and JavaScript functionality

### Documentation (docs/)
- Complete project documentation (150+ pages total)
- Technical guides for implementation
- Business presentations and executive summaries

## Color Scheme

### Primary Colors (Professional Classic)
- **Primary Blue**: #1e3c72 (Navigation, Headers)
- **Secondary Blue**: #2a5298 (Accents, Buttons)
- **Light Blue**: #7e8ba3 (Borders, Backgrounds)

### Metric Card Colors
- **Blue** (#2c5282): Customer metrics
- **Red** (#c53030): Risk indicators
- **Orange** (#c05621): Warning metrics
- **Green** (#276749): Success indicators
- **Purple** (#553c9a): Model metrics
- **Teal** (#285e61): Accuracy indicators
- **Indigo** (#3c366b): Performance metrics

### Neutral Colors
- **Background**: #fafbfc (Light gray)
- **Text Primary**: #1a202c (Dark)
- **Text Secondary**: #4a5568 (Medium gray)
- **Borders**: #e2e8f0 (Light gray)

## Icons Used (Font Awesome 6.4.0)

### Metric Icons
- **Users**: `fa-users` (Total Customers)
- **Chart Down**: `fa-chart-line-down` (Churn Rate)
- **Dollar**: `fa-dollar-sign` (Revenue at Risk)
- **Money**: `fa-money-bill-wave` (Average Revenue)
- **Brain**: `fa-brain` (Best Model)
- **Bullseye**: `fa-bullseye` (Accuracy)
- **Star**: `fa-star` (F1-Score)

## Key Features

### Dashboard Tabs
1. **Overview**: Business metrics, model performance, ROI scenarios
2. **EDA**: Exploratory data analysis charts
3. **Model Performance**: 7 model comparison
4. **Feature Importance**: Top predictive features
5. **Test Model**: Interactive prediction testing

### Technologies
- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Charts**: Chart.js
- **Icons**: Font Awesome 6.4.0
- **ML Models**: Scikit-learn, XGBoost

## How to Use This Structure

### For Development
1. Source code in `src/` follows numbered sequence
2. Run scripts in order: 1 → 2 → 3 → 4 → 5 → 6 → 7
3. Each script saves outputs to appropriate folders

### For Dashboard
1. Run: `python web_app.py`
2. Open: http://localhost:5000
3. All data loads automatically from organized folders

### For Documentation
1. Start with `README.md` in root
2. Read `docs/QUICK_START_GUIDE.md` for quick setup
3. Refer to `docs/PROJECT_DOCUMENTATION.md` for details

## Data Flow

```
Raw Data → Preprocessing → Feature Engineering → Model Training → Evaluation → Dashboard
    ↓            ↓                ↓                    ↓              ↓           ↓
  raw/      processed/       processed/           models/        results/    templates/
```

## Version Control Recommendations

### Important Files (Must Track)
- All source code (src/)
- Documentation (docs/)
- Configuration files (requirements.txt)
- Dashboard files (web_app.py, templates/, static/)
- Project structure (README.md, PROJECT_STRUCTURE.md)

### Large Files (Consider .gitignore)
- Model files (models/*.pkl) - Consider using Git LFS
- Large datasets (data/raw/*.csv) - Store reference link instead
- Result plots (results/plots/*.png) - Can be regenerated

### Temporary Files (Should Ignore)
- `__pycache__/`
- `.ipynb_checkpoints/`
- `.pyc` files
- Temporary CSV exports

## Maintenance

### Regular Updates
- Update requirements.txt when adding new packages
- Document new features in appropriate docs
- Keep model files synchronized with source code version
- Update this structure document when adding new directories

### Best Practices
- Keep raw data untouched
- Version model files with dates if retraining
- Archive old results before generating new ones
- Maintain consistent naming conventions

## Contact
Developed by: Eng. Reem Osama
Saiket Systems Internship
Project Date: October 2024

