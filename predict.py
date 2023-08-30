from statistics import mean
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from datetime import *
from pandas import read_excel
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


df = read_excel("C:/Users/MBO/PycharmProjects/Maint_API_AI/data.xlsx")
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
model = DecisionTreeRegressor(max_depth=100)
model.fit(X_train, y_train)

# Prédictions et évaluation
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)
accuracy_train = accuracy_score(y_train, y_pred_train.round())
accuracy_test = accuracy_score(y_test, y_pred_test.round())

# Convertir les prédictions en dates
y_pred_train_dates = [datetime.fromordinal(int(date)).strftime('%d.%m.%Y') for date in y_pred_train]
y_pred_test_dates = [datetime.fromordinal(int(date)).strftime('%d.%m.%Y') for date in y_pred_test]

X_train_decode = encoder.inverse_transform(X_train)
print(f"Accuracy train: {accuracy_train}   Accuracy test: {accuracy_test}")
print(f"La prediction de la date est : {y_pred_train_dates} (train) et {X_train_decode[0][1]} ")

# Tracer la relation entre la date prédite et le repère
plt.scatter(X_train_decode[1:10, 1], y_pred_train_dates[1:10])
plt.xlabel('Machine')
plt.ylabel('Date prédite')
plt.title('Relation entre le repère et la date prédite')
plt.show()
