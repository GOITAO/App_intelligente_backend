import joblib
import numpy as np

# Charger le modèle
try:
    model = joblib.load('model.pkl')
    print("✅ Modèle chargé avec succès.")
except FileNotFoundError:
    print("❌ Fichier du modèle non trouvé.")
    exit()

# Exemple de nouvelles données à prédire
# 🧠 Remplacez ceci selon vos vrais features
# Ici, le modèle attend 2 features comme à l'entraînement
new_data = np.array([[6, 7]])

# Prédiction
try:
    prediction = model.predict(new_data)
    print(f"🎯 Prédiction : {prediction}")

    # Si le modèle est de classification, on peut aussi voir la probabilité :
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(new_data)
        print(f"📊 Probabilités : {proba}")
except Exception as e:
    print(f"❌ Erreur lors de la prédiction : {e}")
