#%%
import pandas as pd

# %%
titanic = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")
titanic.head()

#%%
# Como calcular estatísticas resumidas
## Qual é a idade média dos passageiros do Titanic?
titanic["Age"].mean()

#%%
# Qual é a idade média e o preço da passagem dos passageiros do Titanic?
titanic[["Age", "Fare"]].median()

#%%
titanic[["Age", "Fare"]].describe()

#%%
# Estatísticas específicas com .agg()
titanic.agg(
    {
        "Age": ["min", "max", "median", "skew"],
        "Fare": ["min", "max", "median", "mean"],
    }
)

#%%
# Agregando estatísticas agrupadas por categoria
## Qual é a idade média dos passageiros do sexo masculino e feminino
## do Titanic?
titanic[["Sex", "Age"]].groupby("Sex").mean()

#%%
# Agora usando numeric_only=True
titanic.groupby("Sex").mean(numeric_only=True)

#%%
# Outra forma
titanic.groupby("Sex")["Age"].mean() # Retorna uma Series

#%%
#%%
# Qual o preço médio da passagem para cada uma das combinações
# de sexo e classe de cabine?
titanic.groupby(["Sex", "Pclass"])["Fare"].mean()

#%%
# Qual o número de passageiros em cada uma das classes de cabine?
titanic["Pclass"].value_counts() # número de registros p/ categoria

#%%
# Outra forma
titanic.groupby("Pclass")["Pclass"].count()