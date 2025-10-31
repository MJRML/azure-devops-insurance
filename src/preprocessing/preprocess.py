import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import os

# Load raw data
df = pd.read_csv("../../data/raw/insurance.csv")

# One-hot encode categorical columns
categorical_cols = ["sex", "smoker", "region"]
df = pd.get_dummies(df, columns=categorical_cols, drop_first=False)

# Save processed data
os.makedirs("../../data/processed", exist_ok=True)
df.to_csv("../../data/processed/insurance_processed.csv", index=False)

print("✅ Preprocessing completed. Processed data saved to data/processed/insurance_processed.csv")
