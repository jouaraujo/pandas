#%%
import pandas as pd

# %%
titanic = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")

titanic.head()

#%%
# Como selecionar um subconjunto de um df
# Estou interessado na idade dos passageiros do Titanic
ages = titanic["Age"]

ages.head()

#%%
type(titanic["Age"]) # é series a saída

#%%
# Retorna nrows,ncols
titanic["Age"].shape

#%%
# Interessado na idade e no sexo dos passageiros do Titanic
age_sex = titanic[["Age", "Sex"]]
# Os colchetes internos definem uma lista python com nomes de colunas,
# enquanto os colchetes externos são usados para selecionar os dados de
# um df

age_sex.head()

#%%
# O tipo de dados retornado é um df
type(titanic[["Age", "Sex"]])

#%%
titanic[["Age", "Sex"]].shape

#%%
# Como filtrar linhas específicas  de um arquivo df

## estou interessado em passageiros com mais de 35 anos
above_35 = titanic[titanic["Age"] > 35] # filtrar só usar o condicional entre colchetes
above_35.head()

#%%
titanic["Age"] > 35

#%%
# linhas e colunas do filtro
above_35.shape

#%%
# Estou interessado nos passageiros do Titanic das classes de cabine 2 e 3.
class_23 = titanic[titanic["Pclass"].isin([2, 3])]
class_23.head()

#%%
# maneira sem isin
class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
class_23.head()
# ao combinar múltiplas instruções condicionais, cada condição deve estar
# entre parênteses. Além disso não se deve usar or/and e sim |/&

#%%
# Quero trabalhar com dados de passageiros cuja idade seja conhecida
age_no_na = titanic[titanic["Age"].notna()]
age_no_na.head()

#%%
# Verificando o shape 
age_no_na.shape

#%% 
# Como seleciono linhas e colunas específicas de um arquivo df
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
adult_names.head()
# ao usar loc/iloc, a parte antes da vírgula são as linhas que você deseja
# e a parte depois da vírgula são as colunas que você deseja selecionar

#%%
# Estou interessado nas linhas 10 a 25 e nas colunas 3 a 5.
titanic.iloc[9:25, 2:5]

#%%
# Novos valores podem ser atribuídos aos dados selecionados. 
# Por exemplo, para atribuir o nome anonymousaos 
# primeiros 3 elementos da quarta coluna:

titanic.iloc[0:3, 3] = "Anonymous"
titanic.head()