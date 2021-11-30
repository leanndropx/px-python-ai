# primeiro, vamos entender o que são:



1. **Label**: é a coluna no dataframe que irá classificar o restante do conjunto de informações, ou seja, ela tipifica. No caso deste projeto é a coluna "Style" que especifica se o vinho é Vermelho ou Branco. 
2. **Features**: são todas as outras colunas do dataframe com informações que serão responsáveis por caracterizar o tipo contido na coluna Label, no caso deste projeto, são as colunas com informações que formam o conjunto de dados que ira caracterizar o vinho em Vermelho ou Branco, como as colunas 



# agora, vamos detalhar as linhas de código: 



1. carreguei os dados e encontrei a label, neste caso, a label é a coluna "diagnosis" que classifica o tipo de cancer em maligno (M) ou benigno (B). Todas as outras colunas são features com dados que caracterizam o tipo de cancer em um destes dois que acabamos de mencionar
   - importa pandas
   - carrega arquivo csv
   - visualiza os dados e encontra a Label de classificação

```
import pandas as pd

df = pd.read_csv("/content/data.csv")
df
```



2. verifiquei a quantidade de valores nulos por coluna e a necessidade de deletá-los. Neste caso, constatei que as colunas:

   1. **Unnamed: 32**: estava inteiramente preenchida com valores nulos, por isso a coluna inteira foi deletada
   2. **id**: esta coluna possui dados de identificação pessoal que não contribuem para a classificação do tipo de cancer e que, assim sendo, poderiam atrapalhar a acurácia do modelo, por isso esta coluna também foi deletada 

   

```
df.isnull().sum()
df.info()
```



3. deletei as duas colunas mencionadas acima e guardei na variável colunas_deletadas, em seguida, guardei o novo dataframe sem as colunas deletadas em uma nova variável que eu decidi chamar de **dfwork**. Este é o dataframe pronto e já formatado que foi usado durante o restante da construção do código.

```
colunas_deletadas = ["id","Unnamed: 32"]
dfwork = df.drop(colunas_deletadas,axis=1)
dfwork
```



4. Fiz uma última análise na coluna label para verificar se havia algum valor diferente de **M** ou **B** , constatei que não, logo, aqui nenhuma linha precisaria ser deletada. 

```
dfwork["diagnosis"].value_counts()
```



5. fiz uma simulação de listagem de todas as colunas para ter uma visão geral do dataframe. Esta ação não é necessária, fiz apenas como teste. 

```
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
```



6. Substitui a string **M** por **0** (zero) e a string **B** por 1 (um)

```
dfwork["diagnosis"] = dfwork["diagnosis"].replace("M",0)
dfwork["diagnosis"] = dfwork["diagnosis"].replace("B",1)
dfwork
```



7. guardei a label(coluna) **Diagnosis** na variável x

```
x = dfwork["diagnosis"] # label
x
```



8. deletei a label **Diagnosis** do dataframe e guardei o restante dos dados (features) na variável y

```
y = dfwork.drop("diagnosis",axis=1) #features
y
```



9. importei a função train_test_split a biblioteca sklearn e a usei para distruir os dados em 4 variáveis distintas, duas para treino da label, e duas para teste da feature

```
from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split (x, y , test_size = 0.3)
x_train
```



10. importei a função ExtraTreesClassifier (árvore de classificação) da biblioteca sklearn e a estanciei dentro da variável **model**

```
from sklearn.ensemble import ExtraTreesClassifier

model = ExtraTreesClassifier (n_estimators=100)
```



11. usei os métodos **FIT** para treinar os dados, em seguida, fiz o teste com o método **SCORE** e guardei o resultado dentro da variável **result**

```
model.fit(y_train, x_train) #primeiro parametro é sempre y (features)
result = model.score(y_test , x_test) #primeiro parâmetro é sempre y (features)
print(result)
```



12. Imprimi no console a quantidade de linhas da variável teste, para que pudesse escolher algumas linhas para serem testadas na previsão. Constatei uma quantidade de 171 linhas, logo, usaria alguma linha entre essa quantidade para realizar a previsão

```
x_test.shape
```

13. usei o método predict para prever o modelo, escolhi as linhas de dados de 100 a 110 do dataframe de teste. Fiz um loop na variável previsao, que recebeu como retorno da função predict uma lista. No loop, criei a condicional que substitui o valor 0 por "Maligno"e 1 por "Benigno"e em seguida imprime na tela o resultado das análises. 

```
previsao = model.predict(y_test[100:110])
for tipo in previsao:
  if tipo==0:
    print("O tipo de cancer é MALIGNO")
  else:
    print("O tipo de cancer é BENIGNO")
```



14. imprimi na tela as mesmas linhas dos dados usados na previsão para realizar a comparação e verificar a assertividade do modelo. 

```
x_test[100:110]
```

