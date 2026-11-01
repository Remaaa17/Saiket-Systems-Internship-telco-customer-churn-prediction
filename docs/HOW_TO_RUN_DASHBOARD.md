# Telco Churn Dashboard - Quick Start Guide

## Overview
This is a Flask-based web dashboard for the Telco Customer Churn Prediction project. It displays machine learning model results, exploratory data analysis, and allows interactive testing of predictions.

## Prerequisites
- Python 3.8 or higher
- Required packages (install with: `pip install -r requirements.txt`)

## How to Run the Dashboard

### Step 1: Open Terminal
Open PowerShell or Command Prompt in the project directory.

### Step 2: Run the Dashboard
```bash
python web_app.py
```

### Step 3: Open in Browser
The dashboard will start on: **http://localhost:5000**

Open your web browser and navigate to this address.

### Step 4: Stop the Dashboard
Press `Ctrl+C` in the terminal to stop the server.

## Dashboard Features

### 1. Overview Tab
- Total customers and churn rate
- Revenue at risk calculations
- Best model performance metrics
- Business impact scenarios (conservative and optimistic)

### 2. EDA Tab
- Churn distribution visualization
- Contract type vs churn rate analysis

### 3. Model Performance Tab
- Comparison of all 7 trained models
- Accuracy and F1-Score metrics
- Detailed performance table

### 4. Feature Importance Tab
- Top 10 most important features for churn prediction
- Visual bar chart display

### 5. Test Model Tab
- Test predictions on random customers
- See customer details and churn probability
- Risk level classification

## Technical Details

### Project Structure
```
project/
+-- web_app.py                 # Flask application
+-- templates/
¦   +-- dashboard.html         # Dashboard HTML template
+-- static/
¦   +-- css/
¦   ¦   +-- style.css         # Dashboard styling
¦   +-- js/
¦       +-- chart.min.js      # Chart.js library (local)
¦       +-- main.js           # Dashboard JavaScript
+-- data/                      # Dataset files
+-- models/                    # Trained ML models
+-- results/                   # Analysis results
+-- docs/                      # Project documentation
```

### Models Used
1. Logistic Regression (Best Model - 80.2% accuracy)
2. Decision Tree
3. Random Forest
4. Gradient Boosting
5. XGBoost
6. Support Vector Machine
7. K-Nearest Neighbors

### Data Files Used
- `data/data_cleaned.csv` - Cleaned dataset
- `data/X_train.csv`, `data/X_test.csv` - Training and test features
- `data/y_train.csv`, `data/y_test.csv` - Training and test labels
- `models/*.pkl` - Trained model files
- `results/final_model_evaluation_results.csv` - Model performance metrics
- `results/feature_importance.csv` - Feature importance rankings

## Troubleshooting

### Issue: Port Already in Use
If you see "Address already in use" error:
```bash
# Windows: Find and kill the process using port 5000
netstat -ano | findstr :5000
taskkill /PID <process_id> /F
```

### Issue: Module Not Found
Install missing packages:
```bash
pip install flask pandas numpy scikit-learn
```

### Issue: Charts Not Displaying
- The dashboard uses a locally downloaded Chart.js library
- No internet connection required
- Charts should display automatically

### Issue: Data Files Not Found
Make sure you're running the command from the project root directory where `web_app.py` is located.

## Support
For questions or issues, refer to:
- `README.md` - Main project documentation
- `docs/PROJECT_DOCUMENTATION.md` - Comprehensive project guide
- `docs/TECHNICAL_GUIDE.md` - Technical implementation details

## Author
Eng. Reem Osama - Saiket Systems Internship
October 2024


