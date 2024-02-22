#%% 
import pandas as pd

#%%
# Analisar dados dos passageiros do Titanic, disponíveis em arquivo csv
titanic = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")

#%%
titanic

#%%
# Ver as primeiras 8 linhas do Df
titanic.head(8)

#%%
# Ver as últimas 8 linhas do Df
titanic.tail(8)

#%%
# Verificação de como o Pandas interpretrou cada um dos tipos de dados da coluna
titanic.dtypes

#%%
# Passar para o formato de planilha
titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)

#%%
# A função read_excel recarregará os dados em df
titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")

#%%
titanic.head()

#%%
# Resumo técnico do df
titanic.info()
