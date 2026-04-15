# =========================
# 📊 TRAIN MODEL ASSURANCE PRO
# =========================

from sklearn.ensemble import RandomForestClassifier
import numpy as np
import joblib

# =========================
# DATASET PLUS RICHE
# =========================

# [âge, revenu, couverture]
X = np.array([

    # bons profils
    [25, 300000, 1000000],
    [30, 400000, 2000000],
    [35, 600000, 3000000],
    [40, 800000, 5000000],
    [45, 1000000, 7000000],

    # profils moyens
    [50, 300000, 4000000],
    [55, 250000, 3500000],
    [60, 200000, 3000000],

    # profils risqués
    [65, 150000, 4000000],
    [70, 100000, 3000000],
    [75, 80000, 2000000],

    # cas variés
    [28, 500000, 6000000],
    [33, 450000, 5500000],
    [48, 350000, 2500000],
    [52, 200000, 1000000],
])

# 1 = bon client, 0 = risque
y = np.array([
    1,1,1,1,1,
    1,0,0,
    0,0,0,
    1,1,1,0
])

# =========================
# TRAIN MODEL
# =========================

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=5,
    random_state=42
)

model.fit(X, y)

# =========================
# SAVE MODEL
# =========================

joblib.dump(model, "model.pkl")

print("✅ Modèle Assurance PRO généré avec succès !")