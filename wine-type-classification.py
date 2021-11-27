

        # 1 - carregar os dados e econtrar a label

import pandas as pd
df = pd.read_csv("/content/wine_dataset.csv")

        # 2 - substitui valore string red / white por 0 / 1

df["style"] = df["style"].replace("red",0)
df["style"] = df["style"].replace("white",1)

        # 3 - separa coluna classificatoria red /white do restante dos dados

rw = df["style"]
dados = df.drop("style",axis=1)

        # 4 - separa dados de treino de dados de teste em 4 variaveis diferentes

from sklearn.model_selection import train_test_split

rw_train , rw_test , dados_train , dados_test = train_test_split(rw, dados , test_size = 0.3)
rw_test[400:420]

        # 5 - estancia modelo com função arvore classificatoria, treina os dados dde treino, testa com dados de teste

from sklearn.ensemble import ExtraTreesClassifier

modelo = ExtraTreesClassifier(n_estimators=100)
modelo.fit(dados_train, rw_train)
resultado = modelo.score(dados_test, rw_test)
print(resultado)


        # 6 - cria previsão

previsao = modelo.predict(dados_test[400:420])
print(previsao)

        # 7 - compara a previsão pra ver se acertou
        
rw_test[400:420]
