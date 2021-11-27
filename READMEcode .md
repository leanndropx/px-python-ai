# Este código foi organizado da seguinte forma: 



A minha linha de raciocícinio para organizar meus algoritmos de **classificação** normalmente é feita em 8 blocos de ações:

1. Carregar os dados e encontrar a label
2. substituir os valores da Label de string para valores numéricos
3. separar a label e as features em variáveis diferentes
4. separar todos os dados em dados de treino e dados de teste
5. Estanciar o modelo escolhido importado e treiná-lo com os dados de treino, neste caso o modelo é ExtraTreesClassifier
6. Cria a previsão
7. Compara a previsão pra ver se acertou



### o que são:

1. **Label**: é a coluna no dataframe que irá classificar o restante do conjunto de informações, ou seja, ela tipifica. No caso deste projeto é a coluna "Style" que especifica se o vinho é Vermelho ou Branco. 
2. **Features**: são todas as outras colunas do dataframe com informações que serão responsáveis por caracterizar o tipo contido na coluna Label, no caso deste projeto, são as colunas com informações que formam o conjunto de dados que ira caracterizar o vinho em Vermelho ou Branco, como as colunas 



# Detalhando as linhas de código: 



1. carregar os dados e encontrar a label
   - importa pandas
   - carrega arquivo csv
   - visualiza os dados e encontra a Label de classificação

```
import pandas as pd

df = pd.read_csv("/content/wine_dataset.csv")
df
```



2. substituir os valores de string da label por valores numéricos

```
df["style"] = df["style"].replace("red",0)
df["style"] = df["style"].replace("white",1)
df
```



3. separar a label das features em variáveis diferentes
   - cria variável **rw** que recebe a coluna **"Style"** com a classificação dos dados em Red /White
   - cria variável **dados** que deleta a coluna  "Style" (label) e armazena todo o restante dos dados (features)

```
rw = df["style"]
dados = df.drop("style",axis=1)
```



4. separar todos os dados em dados de treino e dados de teste
   - importa a função **train_test_split** 
   - cria 4 variáveis que divide label e features em label e features de treino e de teste:
     - rw_train: variávei com dados de treino da Label  
     - rw_test: variável com dados de teste da Label
     - dados_train: variável com dados de treino das Features
     - dados_test: variável com dados de teste das Features
   - as 4 variáveis criadas recebem a função train_test_split com o parâmetro test_size, onde deverá ser especificado a porcetagem dos dados que será utilizada para teste
   - imprime na tela a variável **rw_test** das linhas de 400 a 420, para verificar os dados foram alocados de forma correta nas variáveis pela função.

```
from sklearn.model_selection import train_test_split

rw_train , rw_test , dados_train , dados_test = train_test_split(rw, dados , test_size = 0.3)
rw_test[400:420]
```



5. Estanciar o modelo e treiná-lo
   - importa a função do modelo de árvore de decisão **ExtraTreesClassifier**
   - cria a variável **modelo** e estancia a função
   - usa o método **FIT**  para treinar os dados, e coloca como parâmetro as variáveis de treino das Features e da Label
   - usa o método **SCORE** para testar os dados e encontrar a acurácia do modelo, ou seja, a porcentagem de acerto. Coloca como parâmentro as variáveis de teste criadas para Features e Label
   - imprime a variável resultado com a acurácia do modelo 

```
from sklearn.ensemble import ExtraTreesClassifier

modelo = ExtraTreesClassifier(n_estimators=100)
modelo.fit(dados_train, rw_train)
resultado = modelo.score(dados_test, rw_test)
print(resultado)
```



6. Cria a previsão
   - cria a variável **previsao** que recebe a função estanciada com o método predict
   - nos parâmentros, coloca as linhas dos dados de teste que gostaria de fazer a previão
   - imprime a previsão na tela, os valores serão mostrados em lista com os numeros 0 - Red , ou 1 - White

```
previsao = modelo.predict(dados_test[400:420])
print(previsao)
```



7. Compara a previsão pra ver se acertou
   - imprime na tela as linhas dos dados de teste usados na previsão para ver se o modelo acertou
   - se tiver igual ao trecho de código acima, o modelo está correto

```
rw_test[400:420]

```

