
            # BLOCO 1
import pandas as pd

df = pd.read_csv("/content/data.csv")
df

            # BLOCO 2
df.isnull().sum()
df.info()


            # BLOCO 3
colunas_deletadas = ["id","Unnamed: 32"]
dfwork = df.drop(colunas_deletadas,axis=1)
dfwork

            # BLOCO 4
dfwork["area_worst"].value_counts()


            # BLOCO 5
colunas = ['id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean',
       'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
       'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
       'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
       'fractal_dimension_se', 'radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst', 'smoothness_worst',
       'compactness_worst', 'concavity_worst', 'concave points_worst',
       'symmetry_worst', 'fractal_dimension_worst', 'Unnamed: 32']
for coluna in colunas:
  print(coluna)


            # BLOCO 6
dfwork["diagnosis"] = dfwork["diagnosis"].replace("M",0)
dfwork["diagnosis"] = dfwork["diagnosis"].replace("B",1)
dfwork

            # BLOCO 7
x = dfwork["diagnosis"] # label
x

            # BLOCO 8
y = dfwork.drop("diagnosis",axis=1) #features
y

            # BLOCO 9
from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split (x, y , test_size = 0.3)
x_train


            # BLOCO 10
from sklearn.ensemble import ExtraTreesClassifier

model = ExtraTreesClassifier (n_estimators=100)


            # BLOCO 11
model.fit(y_train, x_train) #primeiro parametro é sempre y (features)
result = model.score(y_test , x_test) #primeiro parâmetro é sempre y (features)
print(result)

            # BLOCO 12
x_test.shape

            # BLOCO 13
previsao = model.predict(y_test[100:110])
for tipo in previsao:
  if tipo==0:
    print("O tipo de cancer é MALIGNO")
  else:
    print("O tipo de cancer é BENIGNO")

            # BLOCO 14
x_test[100:110]
