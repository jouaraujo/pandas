#%%
import pandas as pd

# %%
titanic = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")
titanic.head()

# %%
air_quality = pd.read_csv("../data/air_quality_long.csv", index_col="date.utc",
                          parse_dates=True
)
air_quality.head()

#%%
# Como remodelar o layout das tabelas
## Classificar linhas das tabelas

# %%
# Quero classificar os dados do Titanic de acordo com a idade dos
# passageiros.
titanic.sort_values(by="Age").head()

#%%
# Quero classificar os dados do Titanic de acordo com a classe 
# da cabine e a idade em ordem decrescente
titanic.sort_values(by=["Pclass", "Age"], ascending=False).head()

#%%
# Formato de tabela 
# filter for no2 data only
no2 = air_quality[air_quality["parameter"] == "no2"]

# %%
no2_subset = no2.sort_index().groupby(["location"]).head(2)
no2_subset

#%%
# Quero os valores das três estações como colunas separadas, uma
# ao lado da outra
no2_subset.pivot(columns="location", values="value")

#%%
no2.head()

#%%
no2.pivot(columns="location", values="value").plot()

#%%
# Tabela dinâmica
# Quero as concentrações médias para NO2 e PM2.5 em cada uma das estações
# em forma de tabela

air_quality.pivot_table(
    values="value", index="location", columns="parameter",
    aggfunc="mean"
)
# No caso de pivot(), os dados são apenas reorganizados. 
# Quando vários valores precisam ser agregados (neste caso específico,
# os valores em diferentes intervalos de tempo), 
# pivot_table()podem ser usados, fornecendo uma função de agregação 
# (por exemplo, média) sobre como combinar esses valores.

#%%
air_quality.pivot_table(
    values="value",
    index="location",
    columns="parameter",
    aggfunc="mean",
    margins=True,
)

#%%
# Outra forma
air_quality.groupby(["parameter", "location"])[["value"]].mean()

#%%
# adicionamos um novo índice ao DataFrame com reset_index()
no2_pivoted = (no2.pivot(columns="location", values="value")
                  .reset_index())
no2_pivoted.head()

#%%
# Quero coletar toda a qualidade do ar NO2 medições em uma única
# coluna (formato longo)

no_2 = no2_pivoted.melt(id_vars="date.utc")
no_2.head()
# O pandas.melt()método em a DataFrameconverte a tabela de 
# dados de formato amplo para formato longo. Os cabeçalhos das 
# colunas tornam-se os nomes das variáveis ​​em uma coluna recém-criada.

#%%
no_2 = no2_pivoted.melt(
    id_vars="date.utc",
    value_vars=["BETR801", "FR04014", "London Westminster"],
    value_name="NO_2",
    var_name="id_location",
)
no_2.head()

# value_vars define quais colunas serão fundidas
# value_name fornece um nome de coluna personalizado para a 
## coluna de valores em vez do nome de coluna padrão value
# var_name fornece um nome de coluna personalizado para a 
## coluna que coleta os nomes dos cabeçalhos das colunas. 
## Caso contrário, será necessário o nome do índice ou um
## padrão variable