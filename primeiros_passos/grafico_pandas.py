#%%
import pandas as pd
import matplotlib.pyplot as plt

# %%
air_quality = pd.read_csv("../data/air_quality_no2.csv", index_col=0,
                          parse_dates=True)
air_quality.head()
# A utilização dos parâmetros index_col serve para definir a coluna
# selecionada como índice e parse_dates converte as datas das colunas
# em timestamp

# %%
# Quero uma verificação visual rápida dos dados
air_quality.plot() # no df, o pandas, por padrão cria um gráfico de linha
plt.show() 

#%%
# Quero plotar apenas as colunas da tabela de dados com os dados de Paris
air_quality["station_paris"].plot() # logo funciona tbm com Series
plt.show()

#%%
# Quero comparar visualmente o NO2 valores medidos de Londres
# versus Paris
air_quality.plot.scatter(x="station_london", y="station_paris",
                         alpha=0.5)
plt.show()

#%%
# Visão geral dos métodos disponíveis de plotagem
[
    method_name
    for method_name in dir(air_quality.plot)
    if not method_name.startswith("_")
]

#%%
air_quality.plot.box()
plt.show()

#%%
# Quero cada uma das colunas em uma subtrama separada
axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
plt.show()

#%%
# Quero personalizar, estender ou salvar ainda mais o gráfico resultante
fig, axs = plt.subplots(figsize=(12, 4))

air_quality.plot.area(ax=axs)

axs.set_ylabel("NO$_2$ concentration")

fig.savefig("no2_concentration.png")

plt.show()

#%%
