from sklearn.ensemble import RandomForestRegressor
from statistics import mean
import matplotlib.pyplot as plt
import unipath
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
from function import *
from unipath import *

BASE_DIR = Path(__file__).parent.replace("\\", "/")

df = read_excel(f"{BASE_DIR}/SSC.xlsx")


def predict_KPI_with_date(df, day, month, year):
    # Supprimer les lignes en double et les valeurs manquantes
    df.drop_duplicates().dropna()

    inputdate = datetime(int(year), int(month), int(day)).strftime('%d.%m.%Y').__str__()
    # Convertir les dates en nombres entiers
    y = df
    X = df[["MOIS"]]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)

    # Normaliser les données
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    # Entraîner un modèle Regression Linéaire
    model = LinearRegression()
    model.fit(X_train, y_train)
    # r2 = 0
    # Prédiction des KPI après un entrainement de train
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    # r2 = accuracy_score(y_test, y_pred_test)
    my_pred = model.predict([[int(ReverseExcelConvertDate(inputdate))]])
    print(ReverseExcelConvertDate(inputdate))
    List = []
    for x in my_pred[0]:
        List.append(x)

    return List


