"""
Task 5: Model Training
=======================
This script trains multiple machine learning models for churn prediction.

Objectives:
- Train multiple ML algorithms
- Optimize hyperparameters
- Save trained models
- Compare initial performance
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import time
import warnings
warnings.filterwarnings('ignore')

print("="*70)
print("TASK 5: MODEL TRAINING")
print("="*70)

# Load training data
print("\n1. Loading training data...")
X_train = pd.read_csv('X_train.csv')
y_train = pd.read_csv('y_train.csv').values.ravel()
X_test = pd.read_csv('X_test.csv')
y_test = pd.read_csv('y_test.csv').values.ravel()

print(f"   ✓ Training samples: {len(X_train):,}")
print(f"   ✓ Testing samples: {len(X_test):,}")
print(f"   ✓ Features: {X_train.shape[1]}")

print("\n2. Initializing Models...")

# Define models to train
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Decision Tree': DecisionTreeClassifier(random_state=42, max_depth=10),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1),
    'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, random_state=42),
    'XGBoost': XGBClassifier(n_estimators=100, random_state=42, eval_metric='logloss'),
    'K-Nearest Neighbors': KNeighborsClassifier(n_neighbors=5),
    'Support Vector Machine': SVC(kernel='rbf', random_state=42, probability=True)
}

print(f"   ✓ Initialized {len(models)} models")

print("\n3. Training Models...")
print("   " + "-"*66)

trained_models = {}
training_results = []

for name, model in models.items():
    print(f"\n   Training {name}...")
    start_time = time.time()
    
    # Train model
    model.fit(X_train, y_train)
    training_time = time.time() - start_time
    
    # Make predictions
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    
    # Calculate metrics
    train_accuracy = accuracy_score(y_train, y_pred_train)
    test_accuracy = accuracy_score(y_test, y_pred_test)
    test_precision = precision_score(y_test, y_pred_test)
    test_recall = recall_score(y_test, y_pred_test)
    test_f1 = f1_score(y_test, y_pred_test)
    
    # Store results
    results = {
        'Model': name,
        'Train_Accuracy': train_accuracy,
        'Test_Accuracy': test_accuracy,
        'Precision': test_precision,
        'Recall': test_recall,
        'F1_Score': test_f1,
        'Training_Time': training_time
    }
    training_results.append(results)
    
    # Save trained model
    model_filename = f"model_{name.replace(' ', '_').lower()}.pkl"
    joblib.dump(model, model_filename)
    trained_models[name] = model
    
    print(f"      ✓ Training completed in {training_time:.2f}s")
    print(f"      ✓ Test Accuracy: {test_accuracy:.4f}")
    print(f"      ✓ Test F1-Score: {test_f1:.4f}")
    print(f"      ✓ Model saved: {model_filename}")

print("\n   " + "-"*66)

print("\n4. Training Results Summary:")

# Create results dataframe
results_df = pd.DataFrame(training_results)
results_df = results_df.sort_values('Test_Accuracy', ascending=False)

# Display results table
print("\n" + "="*85)
print(f"{'Model':<25} {'Train Acc':<12} {'Test Acc':<12} {'Precision':<12} {'Recall':<12} {'F1-Score':<12}")
print("="*85)

for _, row in results_df.iterrows():
    print(f"{row['Model']:<25} {row['Train_Accuracy']:<12.4f} {row['Test_Accuracy']:<12.4f} "
          f"{row['Precision']:<12.4f} {row['Recall']:<12.4f} {row['F1_Score']:<12.4f}")

print("="*85)

# Save results
results_df.to_csv('model_training_results.csv', index=False)
print("\n✓ Results saved to 'model_training_results.csv'")

print("\n5. Best Model Identification:")

best_model_row = results_df.iloc[0]
print(f"\n   Best Model (by Test Accuracy): {best_model_row['Model']}")
print(f"   - Test Accuracy: {best_model_row['Test_Accuracy']:.4f}")
print(f"   - F1-Score: {best_model_row['F1_Score']:.4f}")
print(f"   - Precision: {best_model_row['Precision']:.4f}")
print(f"   - Recall: {best_model_row['Recall']:.4f}")

# Best model by F1-Score
best_f1_model = results_df.loc[results_df['F1_Score'].idxmax()]
print(f"\n   Best Model (by F1-Score): {best_f1_model['Model']}")
print(f"   - F1-Score: {best_f1_model['F1_Score']:.4f}")
print(f"   - Test Accuracy: {best_f1_model['Test_Accuracy']:.4f}")

print("\n6. Feature Importance Analysis (for tree-based models)...")

# Get feature names
feature_names = pd.read_csv('feature_names.csv')['feature'].tolist()

# Extract feature importance from Random Forest
rf_model = trained_models['Random Forest']
feature_importance = pd.DataFrame({
    'Feature': feature_names,
    'Importance': rf_model.feature_importances_
}).sort_values('Importance', ascending=False)

print("\n   Top 10 Most Important Features (Random Forest):")
for idx, row in feature_importance.head(10).iterrows():
    print(f"   {row['Feature']:<40s}: {row['Importance']:.4f}")

# Save feature importance
feature_importance.to_csv('feature_importance.csv', index=False)
print("\n   ✓ Feature importance saved to 'feature_importance.csv'")

print("\n" + "="*70)
print("TASK 5 COMPLETED SUCCESSFULLY!")
print("="*70)
print(f"\nKey Achievements:")
print(f"✓ Trained {len(models)} machine learning models")
print(f"✓ Best model: {best_model_row['Model']} (Accuracy: {best_model_row['Test_Accuracy']:.4f})")
print(f"✓ All models saved for deployment")
print(f"✓ Feature importance analyzed")
print("\nNext Step: Run 6_model_evaluation.py")
