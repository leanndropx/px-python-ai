# em modelos de classificação, é importante entender  a ideia de:



1. **Label**: é a coluna no dataframe que irá classificar o restante do conjunto de informações, ou seja, ela tipifica. No caso deste projeto é a coluna "Style" que especifica se o vinho é Vermelho ou Branco. 
2. **Features**: são todas as outras colunas do dataframe com que formam um conjunto de dados que caracteriza o o valor contido na coluna Label. Por exemplo, um conunto de dados (features) que pode caracterizar um vinho como Vermelho ou Branco (label), ou conjunto de dados (features) que caracteriza um tipo de cancer como maligno ou benigno (label).



# as etapas em algoritmos de classificação, normalmente podem ser enquadradas em 8 blocos de ações: 



1. Carregar e fazer a formatação dos dados:
   1. verificar e deletar os valores nulos, quando necessário
   2. encontrar e deletar as colunas que não influenciam um padrão para a análise classificatória, como por exemplo colunas de identificação pessoal e datas. 
2. Encontrar a label e substituir os valores da Label de string para valores numéricos
3. separar a label e as features em variáveis diferentes
4. separar todos os dados em dados de treino e dados de teste
5. Estanciar o modelo escolhido importado e treiná-lo com os dados de treino, no caso deste diretório estamos usando o modelo ExtraTreesClassifier, também conhecido como árvore de classificação.
6. Criar a previsão
7. Comparar a previsão com os dados de teste para verificar se o modelo acertou



# comandos úteis por bloco de ação:



| Pandas / Sklearn                                             |                                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |
| **Comando**                                                  | **Função**                                                   |
|                                                              |                                                              |
| **1 - carregar os dados**                                    |                                                              |
| pd.read_csv("caminho do arquivo")                            | carrega arquivo csv e transforma em dataframe                |
| pd.read_excel("caminho do arquivo")                          | carrega arquivo excel e transforma em data frame             |
|                                                              |                                                              |
| **2 - verificar / deletar / trabalhar com valores nulos**    |                                                              |
| df.isnull().sum()                                            | mostra quantidade de valores nulos em cada coluna            |
| df.info()                                                    | mostra quantidade de valores não nulos em cada coluna        |
| df.dropna()                                                  | deleta todos os dados faltantes do dataframe                 |
| df.dropna(subset=["nome da coluna")                          | limpa dados nulos de uma coluna específica                   |
| df.dropna(axis=0)                                            | deleta as linhas que contem dados faltantes                  |
| df.dropna(axis=1)                                            | deleta as colunas que contem dados faltantes                 |
| df.update(df["nome da coluna"].fillna(valor)                 | preenche os campos de valores nulos com outro valor          |
|                                                              |                                                              |
| **3 - visualizar colunas / econtrar a coluna Label**         |                                                              |
| df.columns                                                   | mostra lista com nomes das colunas                           |
| list(df.columns)                                             | mostra nomes das colunas um embaixo do outro                 |
| df.rename(columns={'nome': 'novo_nome'})                     | muda nome da coluna para melhor visualizá-las                |
| df[nome_da_coluna].value_counts()                            | conta frequencia de valores em determinada coluna            |
|                                                              |                                                              |
| **4 - deletar colunas desnecessárias**                       |                                                              |
| df.drop("nome",axis=1)                                       | deleta uma coluna pelo nome                                  |
| df.drop("nome",axis=1,inplace=True)                          | deleta uma coluna pelo nome dentro da variável original      |
| df.drop(df[[0,32]],axis=1)                                   | deleta uma coluna pela posição index                         |
| del df["nome da coluna"]                                     | deleta uma coluna pelo nome                                  |
|                                                              |                                                              |
| **5 - substituir string da coluna label por numero**         |                                                              |
| df["nome da coluna"].replace("valor",0)                      | substitui um valor por outro                                 |
|                                                              |                                                              |
| **6 - dividir em dados de treino e teste**                   |                                                              |
| x_train , x_test , y_train , y_test = train_test_split (x, y , test_size = 0.3) | função divide dados em 4 variáveis de treino e teste         |
|                                                              |                                                              |
| **7 - estanciar função de modelo de aprendizagem**           |                                                              |
| model = ExtraTreesClassifier (n_estimators=100)              | estancia modelo de árvore de decisão                         |
|                                                              |                                                              |
| **8 - treinar modelo com dados de treino**                   |                                                              |
| model.fit(y_train, x_train)                                  | treina modelo com dados de treino                            |
|                                                              |                                                              |
| **9 - testa modelo com dados de teste**                      |                                                              |
| result = model.score(y_test , x_test)                        | testa modelo com dados de teste e mostra acuracia            |
|                                                              |                                                              |
| **10 - faz a previsão**                                      |                                                              |
| previsao = model.predict(y_test[100:110])                    | função faz a previsão de dados selecionados do dataframde de teste |
