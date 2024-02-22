#%% 
import pandas as pd

# %%
# Criando um DF do zero
# Dados de passageiros do Titanic
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. Wiliam Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"]
    }
)

df

#%%
# Estou apenas interessado em trabalhar com os dados da coluna Age
df["Age"] # O resultado é uma series

#%%
# Criando Series do zero
ages = pd.Series([22, 35, 58],name="Age")
ages

#%%
# Saber a idade máxima dos passageiros
df["Age"].max() # Para o Df

#%%
ages.max() # Para a series

#%%
# Algumas estatísticas básicas dos dados numéricos
df.describe()