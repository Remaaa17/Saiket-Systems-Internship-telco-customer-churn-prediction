"""
Task 6: Model Evaluation
=========================
This script performs comprehensive evaluation of trained models.

Objectives:
- Evaluate models with multiple metrics
- Create confusion matrices
- Plot ROC curves
- Generate classification reports
- Compare model performance
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (confusion_matrix, classification_report, roc_curve, 
                              auc, roc_auc_score, precision_recall_curve)
import joblib
import os
import warnings
warnings.filterwarnings('ignore')

print("="*70)
print("TASK 6: MODEL EVALUATION")
print("="*70)

# Load test data
print("\n1. Loading test data...")
X_test = pd.read_csv('X_test.csv')
y_test = pd.read_csv('y_test.csv').values.ravel()
print(f"   ✓ Test samples: {len(X_test):,}")

# Create output directory for evaluation plots
if not os.path.exists('evaluation_plots'):
    os.makedirs('evaluation_plots')
    print("   ✓ Created 'evaluation_plots' directory")

print("\n2. Loading trained models...")

# Load all trained models
model_files = [
    'model_logistic_regression.pkl',
    'model_decision_tree.pkl',
    'model_random_forest.pkl',
    'model_gradient_boosting.pkl',
    'model_xgboost.pkl',
    'model_k-nearest_neighbors.pkl',
    'model_support_vector_machine.pkl'
]

models = {}
model_names = {
    'model_logistic_regression.pkl': 'Logistic Regression',
    'model_decision_tree.pkl': 'Decision Tree',
    'model_random_forest.pkl': 'Random Forest',
    'model_gradient_boosting.pkl': 'Gradient Boosting',
    'model_xgboost.pkl': 'XGBoost',
    'model_k-nearest_neighbors.pkl': 'K-Nearest Neighbors',
    'model_support_vector_machine.pkl': 'Support Vector Machine'
}

for model_file in model_files:
    if os.path.exists(model_file):
        model = joblib.load(model_file)
        models[model_names[model_file]] = model
        print(f"   ✓ Loaded {model_names[model_file]}")

print(f"\n   Total models loaded: {len(models)}")

print("\n3. Generating Confusion Matrices...")

# Create confusion matrices for all models
fig, axes = plt.subplots(2, 4, figsize=(20, 10))
axes = axes.ravel()

for idx, (name, model) in enumerate(models.items()):
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[idx], 
                xticklabels=['No Churn', 'Churn'], 
                yticklabels=['No Churn', 'Churn'])
    axes[idx].set_title(f'{name}', fontsize=12, fontweight='bold')
    axes[idx].set_ylabel('Actual')
    axes[idx].set_xlabel('Predicted')

# Hide the last subplot if we have fewer than 8 models
if len(models) < 8:
    axes[7].axis('off')

plt.tight_layout()
plt.savefig('evaluation_plots/1_confusion_matrices.png', dpi=300, bbox_inches='tight')
print("   ✓ Confusion matrices saved")
plt.close()

print("\n4. Generating ROC Curves...")

# Plot ROC curves
plt.figure(figsize=(12, 8))

roc_auc_scores = {}

for name, model in models.items():
    # Get probability predictions
    if hasattr(model, "predict_proba"):
        y_pred_proba = model.predict_proba(X_test)[:, 1]
    else:
        y_pred_proba = model.decision_function(X_test)
    
    # Calculate ROC curve
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    roc_auc = auc(fpr, tpr)
    roc_auc_scores[name] = roc_auc
    
    # Plot
    plt.plot(fpr, tpr, linewidth=2, label=f'{name} (AUC = {roc_auc:.3f})')

plt.plot([0, 1], [0, 1], 'k--', linewidth=2, label='Random Classifier')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate', fontsize=12)
plt.ylabel('True Positive Rate', fontsize=12)
plt.title('ROC Curves - Model Comparison', fontsize=14, fontweight='bold')
plt.legend(loc='lower right', fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('evaluation_plots/2_roc_curves.png', dpi=300, bbox_inches='tight')
print("   ✓ ROC curves saved")
plt.close()

print("\n5. Generating Precision-Recall Curves...")

plt.figure(figsize=(12, 8))

for name, model in models.items():
    # Get probability predictions
    if hasattr(model, "predict_proba"):
        y_pred_proba = model.predict_proba(X_test)[:, 1]
    else:
        y_pred_proba = model.decision_function(X_test)
    
    # Calculate precision-recall curve
    precision, recall, _ = precision_recall_curve(y_test, y_pred_proba)
    
    # Plot
    plt.plot(recall, precision, linewidth=2, label=f'{name}')

plt.xlabel('Recall', fontsize=12)
plt.ylabel('Precision', fontsize=12)
plt.title('Precision-Recall Curves - Model Comparison', fontsize=14, fontweight='bold')
plt.legend(loc='best', fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('evaluation_plots/3_precision_recall_curves.png', dpi=300, bbox_inches='tight')
print("   ✓ Precision-recall curves saved")
plt.close()

print("\n6. Generating Detailed Classification Reports...")

# Create classification reports for all models
reports = {}

for name, model in models.items():
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, target_names=['No Churn', 'Churn'], 
                                    output_dict=True)
    reports[name] = report
    
    print(f"\n   {name}:")
    print(f"   {'-'*60}")
    print(classification_report(y_test, y_pred, target_names=['No Churn', 'Churn']))

# Save detailed reports to file
with open('detailed_classification_reports.txt', 'w') as f:
    f.write("DETAILED CLASSIFICATION REPORTS\n")
    f.write("="*70 + "\n\n")
    
    for name, model in models.items():
        y_pred = model.predict(X_test)
        f.write(f"{name}\n")
        f.write("-"*70 + "\n")
        f.write(classification_report(y_test, y_pred, target_names=['No Churn', 'Churn']))
        f.write("\n" + "="*70 + "\n\n")

print("\n   ✓ Detailed reports saved to 'detailed_classification_reports.txt'")

print("\n7. Model Performance Comparison...")

# Load previous training results
training_results = pd.read_csv('model_training_results.csv')

# Add ROC-AUC scores
training_results['ROC_AUC'] = training_results['Model'].map(roc_auc_scores)

# Create performance comparison plot
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Plot 1: Accuracy comparison
ax1 = axes[0, 0]
training_results.sort_values('Test_Accuracy', ascending=True).plot(
    x='Model', y='Test_Accuracy', kind='barh', ax=ax1, color='skyblue', legend=False)
ax1.set_title('Model Accuracy Comparison', fontsize=12, fontweight='bold')
ax1.set_xlabel('Accuracy')
ax1.set_ylabel('')

# Plot 2: F1-Score comparison
ax2 = axes[0, 1]
training_results.sort_values('F1_Score', ascending=True).plot(
    x='Model', y='F1_Score', kind='barh', ax=ax2, color='lightcoral', legend=False)
ax2.set_title('Model F1-Score Comparison', fontsize=12, fontweight='bold')
ax2.set_xlabel('F1-Score')
ax2.set_ylabel('')

# Plot 3: ROC-AUC comparison
ax3 = axes[1, 0]
training_results.sort_values('ROC_AUC', ascending=True).plot(
    x='Model', y='ROC_AUC', kind='barh', ax=ax3, color='lightgreen', legend=False)
ax3.set_title('Model ROC-AUC Comparison', fontsize=12, fontweight='bold')
ax3.set_xlabel('ROC-AUC Score')
ax3.set_ylabel('')

# Plot 4: Precision vs Recall
ax4 = axes[1, 1]
ax4.scatter(training_results['Recall'], training_results['Precision'], s=100, alpha=0.6)
for idx, row in training_results.iterrows():
    ax4.annotate(row['Model'], (row['Recall'], row['Precision']), 
                fontsize=8, ha='right')
ax4.set_xlabel('Recall', fontsize=12)
ax4.set_ylabel('Precision', fontsize=12)
ax4.set_title('Precision vs Recall', fontsize=12, fontweight='bold')
ax4.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('evaluation_plots/4_performance_comparison.png', dpi=300, bbox_inches='tight')
print("   ✓ Performance comparison plot saved")
plt.close()

# Save updated results
training_results.to_csv('final_model_evaluation_results.csv', index=False)
print("   ✓ Final results saved to 'final_model_evaluation_results.csv'")

print("\n8. Final Model Ranking:")
print("\n   " + "="*70)

# Rank models by different metrics
print("\n   a) By Test Accuracy:")
top_accuracy = training_results.nlargest(3, 'Test_Accuracy')
for idx, row in top_accuracy.iterrows():
    print(f"      {row['Model']:30s}: {row['Test_Accuracy']:.4f}")

print("\n   b) By F1-Score:")
top_f1 = training_results.nlargest(3, 'F1_Score')
for idx, row in top_f1.iterrows():
    print(f"      {row['Model']:30s}: {row['F1_Score']:.4f}")

print("\n   c) By ROC-AUC:")
top_auc = training_results.nlargest(3, 'ROC_AUC')
for idx, row in top_auc.iterrows():
    print(f"      {row['Model']:30s}: {row['ROC_AUC']:.4f}")

# Overall best model
print("\n9. Recommended Model:")
best_model = training_results.iloc[training_results['F1_Score'].idxmax()]
print(f"\n   {best_model['Model']}")
print(f"   {'='*50}")
print(f"   Test Accuracy:  {best_model['Test_Accuracy']:.4f}")
print(f"   Precision:      {best_model['Precision']:.4f}")
print(f"   Recall:         {best_model['Recall']:.4f}")
print(f"   F1-Score:       {best_model['F1_Score']:.4f}")
print(f"   ROC-AUC:        {best_model['ROC_AUC']:.4f}")

print("\n" + "="*70)
print("TASK 6 COMPLETED SUCCESSFULLY!")
print("="*70)
print(f"\nKey Achievements:")
print(f"✓ Generated confusion matrices for all models")
print(f"✓ Created ROC and Precision-Recall curves")
print(f"✓ Comprehensive performance comparison completed")
print(f"✓ Recommended model: {best_model['Model']}")
print(f"\nGenerated {len(os.listdir('evaluation_plots'))} evaluation plots")
print("\nNext Step: Run 7_insights_and_recommendations.py")
