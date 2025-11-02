# import pandas as pd
# from sklearn.preprocessing import OneHotEncoder
# import os

# # Load raw data
# df = pd.read_csv("../../data/raw/insurance.csv")

# # One-hot encode categorical columns
# categorical_cols = ["sex", "smoker", "region"]
# df = pd.get_dummies(df, columns=categorical_cols, drop_first=False)

# # Save processed data
# os.makedirs("../../data/processed", exist_ok=True)
# df.to_csv("../../data/processed/insurance_processed.csv", index=False)

# print(" Preprocessing completed. Processed data saved to data/processed/insurance_processed.csv")

import os
import pandas as pd

# -------------------------------
# Resolve project root directory
# -------------------------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "insurance.csv")
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "insurance_processed.csv")

# -------------------------------
# Load raw dataset
# -------------------------------
print(f" Loading dataset from: {RAW_DATA_PATH}")
df = pd.read_csv(RAW_DATA_PATH)

# -------------------------------
# Preprocessing example (modify as needed)
# -------------------------------
# Convert categorical variables using one-hot encoding
df_processed = pd.get_dummies(df, drop_first=True)

# Ensure output directory exists
os.makedirs(os.path.join(BASE_DIR, "data", "processed"), exist_ok=True)

# Save processed data
df_processed.to_csv(PROCESSED_DATA_PATH, index=False)
print(f" Processed dataset saved to: {PROCESSED_DATA_PATH}")

