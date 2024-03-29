from statistics import mean
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from datetime import *
from pandas import read_excel
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from unipath import Path

from function import sortDate, predictionAnnuelle

BASE_DIR = Path(__file__).parent.replace("\\", "/")

df = read_excel(f"{BASE_DIR}/data.xlsx")
# Supprimer les lignes en double et les valeurs manquantes
df = df.drop_duplicates().dropna()

# Convertir les dates en nombres entiers
y = [datetime.strptime(date_str, '%d.%m.%Y').toordinal() for date_str in df["Date"]]

X = df[["Machine", "Repère", "Equipement", "Nature intervention"]]

# Encoder les variables catégorielles
encoder = OneHotEncoder(handle_unknown="ignore")
X_encoded = encoder.fit_transform(X).toarray()

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=4)


# Normaliser les données
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X_encoded)

# Entraîner un modèle d'arbre de décision
model = DecisionTreeRegressor(max_depth=4)
model.fit(X_train, y_train)

# Prédictions et évaluation
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)
mse_train = mean_squared_error(y_train, y_pred_train)
mse_test = mean_squared_error(y_test, y_pred_test)
r2_train = r2_score(y_train, y_pred_train)
r2_test = r2_score(y_test, y_pred_test)
print(f"MSE train: {mse_train:.2f}   MSE test: {mse_test:.2f}")
print(f"R² train: {r2_train:.2f}   R² test: {r2_test:.2f}")

# Définir la date de début des prédictions
start_date = datetime.now().date()
X_new = [["Turboréducteur n°1", "11.17.BY10", "RÉGULATEUR DE VITESSE", "335947"]]
end_date = predictionAnnuelle(X_new, 10, model, encoder)
print(end_date)

# Convertir les prédictions en dates
y_pred_train_dates = sortDate([datetime.fromordinal(int(date)).strftime('%d.%m.%Y') for date in y_pred_train])
y_pred_test_dates = sortDate([datetime.fromordinal(int(date)).strftime('%d.%m.%Y') for date in y_pred_test])

X_train_decode = encoder.inverse_transform(X_train)
print(f"La prediction de la date est : {y_pred_train_dates} (train) et {X_train_decode[0][1]} ")

# Tracer la relation entre la date prédite et le repère
plt.figure(figsize=(12, 12))
plt.scatter(X_train_decode[100:151, 0], y_pred_train_dates[100:151])
plt.xlabel('Machine')
plt.ylabel('Date prédite')
plt.xticks(rotation=90)
plt.title('Relation entre la machine et la date prédite pour la panne')
plt.show()
