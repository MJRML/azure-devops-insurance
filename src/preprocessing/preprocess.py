import os
import pandas as pd


# Resolve project root directory

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "insurance.csv")
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "insurance_processed.csv")

# Load raw dataset

print(f" Loading dataset from: {RAW_DATA_PATH}")
df = pd.read_csv(RAW_DATA_PATH)

# Preprocessing example 

# Convert categorical variables using one-hot encoding
df_processed = pd.get_dummies(df, drop_first=True)

# Ensure output directory exists
os.makedirs(os.path.join(BASE_DIR, "data", "processed"), exist_ok=True)

# Save processed data
df_processed.to_csv(PROCESSED_DATA_PATH, index=False)
print(f" Processed dataset saved to: {PROCESSED_DATA_PATH}")

