import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Créer des données d'exemple
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])  # Deux champs (features)
y = np.array([3, 5, 7, 9, 11])  # Variable cible

# Créer un modèle de régression linéaire
model = LinearRegression()

# Entraîner le modèle avec les données
model.fit(X, y)

# Prédire une nouvelle valeur
new_data = np.array([[6, 7]])
prediction = model.predict(new_data)

print(f"Prediction pour les nouvelles données : {prediction}")

# Afficher les coefficients du modèle
print(f"Coefficient d'intersection (intercept): {model.intercept_}")
print(f"Coefficients des features: {model.coef_}")

# Enregistrer le modèle entraîné avec joblib
filename = 'model.joblib'
joblib.dump(model, filename)

print(f"Modèle enregistré dans le fichier : {filename}")
