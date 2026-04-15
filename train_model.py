from sklearn.ensemble import RandomForestClassifier
import numpy as np
import joblib

X = np.array([
    [25, 200000, 1000000, 2, 50000, 0],
    [35, 400000, 3000000, 5, 100000, 20000],
    [45, 600000, 5000000, 10, 150000, 50000],
    [60, 300000, 2000000, 20, 200000, 100000],
    [30, 800000, 7000000, 3, 80000, 0],
])

y = np.array([1, 1, 1, 0, 0])

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("✅ Model PRO généré")