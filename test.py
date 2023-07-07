from pandas import *

df = read_excel('C:/Users/MBO/PycharmProjects/NewFastAPI/data.xlsx')
a2_value = df.loc[1, 'ID FILIERE']
r = str(a2_value)
ID = []
DEBOUCHE = [0]
TAILLE = int(df.size / df.columns.size)
for i in range(TAILLE):
    ID.append(df.loc[i, 'ID FILIERE'])
    DEBOUCHE.append(df.loc[i,'DEBOUCHE'])
print(ID)
print(DEBOUCHE)
print(len(DEBOUCHE))

# Afficher la valeur de la cellule A2
