import pandas as pd
import numpy as np
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv"
df = pd.read_csv(url)

df['human_auth_required'] = np.where((df['smoker'] == 'yes') & (df['bmi'] > 30), 'Yes', 'No')
np.random.seed(42)
df['model_confidence_score'] = np.random.uniform(0.4, 0.99, len(df))
df['model_auth_prediction'] = df['human_auth_required']

error_mask = np.random.rand(len(df)) > 0.86
df.loc[error_mask, 'model_auth_prediction'] = np.where(df.loc[error_mask, 'human_auth_required'] == 'Yes', 'No', 'Yes')
conn = sqlite3.connect(':memory:')
df.to_sql('claims_data', conn, index=False)

query = """
SELECT 
    region,
    COUNT(*) as total_claims,
    SUM(CASE WHEN model_auth_prediction = human_auth_required THEN 1 ELSE 0 END) * 100.0 / COUNT(*) as model_accuracy,
    AVG(charges) as avg_claim_cost
FROM claims_data
GROUP BY region
ORDER BY model_accuracy DESC;
"""
sql_results = pd.read_sql_query(query, conn)
print(sql_results.to_string())

# 4. SEABORN: STAKEHOLDER VISUALIZATIONS
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Chart 1: Is the LLM struggling with high-cost claims? (Risk Analysis)
sns.boxplot(data=df, x='model_auth_prediction', y='charges', hue='human_auth_required', ax=axes[0], palette="Set2")
axes[0].set_title('Financial Risk: Model Predictions vs Actual Ground Truth')
axes[0].set_xlabel('Model Predicted "Requires Auth"')
axes[0].set_ylabel('Claim Cost ($)')

# Chart 2: LLM Confidence Distribution (Explainability & Trust)
sns.histplot(data=df, x='model_confidence_score', hue='model_auth_prediction', multiple="stack", bins=20, ax=axes[1])
axes[1].set_title('Model Agent Confidence Scores by Prediction')
axes[1].set_xlabel('Confidence Score (0.0 to 1.0)')
axes[1].axvline(x=0.7, color='red', linestyle='--', label='Suggested Human Review Threshold')
axes[1].legend()

plt.tight_layout()
plt.show()