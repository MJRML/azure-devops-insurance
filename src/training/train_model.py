import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib


# Resolve project root directory
--
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "insurance_processed.csv")
MODEL_DIR = os.path.join(BASE_DIR, "models")
MODEL_PATH = os.path.join(MODEL_DIR, "insurance_model.pkl")

---
# Load processed dataset

print(f" Loading processed dataset from: {PROCESSED_DATA_PATH}")
df = pd.read_csv(PROCESSED_DATA_PATH)

# Prepare features and target

X = df.drop("charges", axis=1)
y = df["charges"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Train model

print(" Training RandomForestRegressor model...")
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n Model trained successfully!")
print(f" Mean Absolute Error: {mae:.2f}")
print(f" Mean Squared Error: {mse:.2f}")
print(f" R² Score: {r2:.2f}")


# Save model

os.makedirs(MODEL_DIR, exist_ok=True)
joblib.dump(model, MODEL_PATH)

print(f"\n Model saved to: {MODEL_PATH}")
