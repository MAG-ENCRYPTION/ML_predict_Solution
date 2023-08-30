from sklearn.ensemble import RandomForestRegressor
from statistics import mean
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from datetime import *
from sklearn.neural_network import *
from pandas import read_excel
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from unipath import Path
from function import *

from function import sortDate, predictionAnnuelle

BASE_DIR = Path(__file__).parent.replace("\\", "/")

df = read_excel(f"{BASE_DIR}/SSC.xlsx")
# Supprimer les lignes en double et les valeurs manquantes
df = df.drop_duplicates().dropna()

# Convertir les dates en nombres entiers
y = df[["TONNE CANNES", "TONNE SUCRE", "RENDEMENT APPARENT USINE",
        "PERTES TOTALES", "PERTES BAGASSE", "PERTES ECUMES",
        "PERTES INDETERMINEES"]]

X = df[["MOIS"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)


# Normaliser les données
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Entraîner un modèle ANN
model = RandomForestRegressor(n_estimators=500, max_depth=100)
model.fit(X_train, y_train)

# Prédiction
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)
my_pred = model.predict([[int(ReverseExcelConvertDate("01.11.2010"))]])

"""print(X_test, X_train, y_train, y_test)

print(y_pred_test, y_pred_train)"""
print(ReverseExcelConvertDate("01.11.2010"))
print(my_pred[0][0], my_pred[0][1], my_pred[0][2], my_pred[0][3], my_pred[0][4], my_pred[0][5], my_pred[0][5])

