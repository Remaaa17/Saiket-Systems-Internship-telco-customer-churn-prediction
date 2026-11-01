"""
Flask Web Dashboard - Traditional HTML/CSS/JavaScript
No React, no Streamlit - just simple web technologies
"""

from flask import Flask, render_template, jsonify
import pandas as pd
import numpy as np
import joblib
import os
import json

app = Flask(__name__)

# Load data
print("Loading data...")
df_clean = pd.read_csv('data/processed/data_cleaned.csv')
X_test = pd.read_csv('data/processed/X_test.csv')
y_test = pd.read_csv('data/processed/y_test.csv')

try:
    results_df = pd.read_csv('results/final_model_evaluation_results.csv')
except:
    results_df = pd.read_csv('results/model_training_results.csv')

feature_importance = pd.read_csv('results/feature_importance.csv')

# Load models
models = {}
model_names = ['logistic_regression', 'decision_tree', 'random_forest',
               'gradient_boosting', 'xgboost', 'support_vector_machine',
               'k-nearest_neighbors']

for model_name in model_names:
    model_path = f'models/model_{model_name}.pkl'
    if os.path.exists(model_path):
        models[model_name] = joblib.load(model_path)

scaler = joblib.load('models/scaler.pkl')

print("Data loaded successfully!")

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/overview')
def get_overview():
    total_customers = len(df_clean)
    churned_customers = len(df_clean[df_clean['Churn'] == 'Yes'])
    churn_rate = churned_customers / total_customers * 100
    avg_monthly_revenue = df_clean['MonthlyCharges'].mean()
    total_revenue_risk = churned_customers * avg_monthly_revenue * 12
    
    best_model = results_df.iloc[0]
    
    conservative_save = int(churned_customers * 0.25)
    conservative_revenue = conservative_save * avg_monthly_revenue * 12
    optimistic_save = int(churned_customers * 0.40)
    optimistic_revenue = optimistic_save * avg_monthly_revenue * 12
    
    return jsonify({
        'totalCustomers': total_customers,
        'churnedCustomers': churned_customers,
        'churnRate': round(churn_rate, 2),
        'avgMonthlyRevenue': round(avg_monthly_revenue, 2),
        'totalRevenueRisk': round(total_revenue_risk, 2),
        'bestModel': {
            'name': best_model['Model'],
            'accuracy': round(best_model['Test_Accuracy'] * 100, 2),
            'f1Score': round(best_model['F1_Score'], 3)
        },
        'potentialImpact': {
            'conservative': {
                'customersSaved': conservative_save,
                'revenueProtected': round(conservative_revenue, 2)
            },
            'optimistic': {
                'customersSaved': optimistic_save,
                'revenueProtected': round(optimistic_revenue, 2)
            }
        }
    })

@app.route('/api/churn-distribution')
def churn_distribution():
    churn_counts = df_clean['Churn'].value_counts()
    return jsonify({
        'labels': churn_counts.index.tolist(),
        'values': churn_counts.values.tolist()
    })

@app.route('/api/contract-analysis')
def contract_analysis():
    data = []
    for contract in df_clean['Contract'].unique():
        contract_df = df_clean[df_clean['Contract'] == contract]
        total = len(contract_df)
        churned = len(contract_df[contract_df['Churn'] == 'Yes'])
        churn_rate = (churned / total * 100) if total > 0 else 0
        data.append({
            'contract': contract,
            'churnRate': round(churn_rate, 2)
        })
    return jsonify(data)

@app.route('/api/model-performance')
def model_performance():
    data = []
    for _, row in results_df.iterrows():
        data.append({
            'model': row['Model'],
            'accuracy': round(row['Test_Accuracy'] * 100, 2),
            'f1Score': round(row['F1_Score'], 3)
        })
    return jsonify(data)

@app.route('/api/feature-importance')
def get_feature_importance():
    top_10 = feature_importance.head(10)
    return jsonify({
        'features': top_10['Feature'].tolist(),
        'importance': [round(x, 4) for x in top_10['Importance'].tolist()]
    })

@app.route('/api/predict-random')
def predict_random():
    random_idx = np.random.randint(0, len(X_test))
    customer = X_test.iloc[random_idx:random_idx+1]
    actual_churn = int(y_test.iloc[random_idx].values[0])
    
    predictions = {}
    for model_name, model in models.items():
        pred = int(model.predict(customer)[0])
        pred_proba = float(model.predict_proba(customer)[0, 1])
        predictions[model_name] = {
            'prediction': 'Will Churn' if pred == 1 else 'Will Stay',
            'probability': round(pred_proba * 100, 1),
            'riskLevel': 'HIGH' if pred_proba > 0.7 else 'MEDIUM' if pred_proba > 0.4 else 'LOW'
        }
    
    return jsonify({
        'customerId': random_idx,
        'actualChurn': 'Yes' if actual_churn == 1 else 'No',
        'predictions': predictions
    })

if __name__ == '__main__':
    print("\n" + "="*70)
    print("Telco Churn Web Dashboard")
    print("="*70)
    print("\nDashboard URL: http://localhost:5000")
    print("\nPress Ctrl+C to stop")
    print("="*70 + "\n")
    
    app.run(debug=True, port=5000, host='0.0.0.0')

