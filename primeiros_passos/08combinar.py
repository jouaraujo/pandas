#%%
import pandas as pd

# %%
air_quality_no2 = pd.read_csv("../data/air_quality_long.csv",
                              parse_dates=True)

# %%
air_quality_no2 = air_quality_no2[["date.utc", "location",
                                   "parameter", "value"]]
air_quality_no2.head()

#%%
air_quality_pm25 = pd.read_csv("../data/air_quality_pm25_long.csv",
                               parse_dates=True)

# %%
air_quality_pm25 = air_quality_pm25[["date.utc", "location",
                                     "parameter", "value"]]
air_quality_pm25.head()

# %%
# Como combinar dados de várias tabelas
## Quero combinar as medidas de NO2 e PM25, duas tabelas com estrutura semelhante,
## em uma única tabela.
air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
air_quality.head()
# A concat()função executa operações de concatenação de múltiplas 
# tabelas ao longo de um dos eixos (linha ou coluna).

#%%
# Verificando o formato das tabelas originais e concatenadas para verificar o funcionamento
print(f"O tamanho da tabela air_quality_pm25 {air_quality_pm25.shape}")
print(f"O tamanho da tabela air_quality_no2 {air_quality_no2.shape}")
print(f"O tamanho da tabela air_quality {air_quality.shape}")
# Portanto, a tabela resultante tem 3.178 = 1.110 + 2.068 linhas.

# O argumento axis retornará em vários métodos pandas que podem ser 
# aplicados ao longo de um axis . O DataFrametem  tem dois eixos 
# correspondentes: o primeiro correndo verticalmente para baixo nas 
# linhas (eixo 0) e o segundo correndo horizontalmente nas 
# colunas (eixo 1). A maioria das operações como concatenação ou 
# estatísticas resumidas são, por padrão, em linhas (eixo 0), 
# mas também podem ser aplicadas em colunas.

# %%
air_quality = air_quality.sort_values("date.utc")
air_quality.head()

#%%
air_quality = pd.concat([air_quality_pm25, air_quality_no2],
                        keys=["PM25", "NO2"])
air_quality.head()

#%%
