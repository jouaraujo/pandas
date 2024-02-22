#%%
import pandas as pd

# %%
air_quality = pd.read_csv("../data/air_quality_no2.csv", index_col=0,
                          parse_dates=True)
air_quality.head()

#%%
# Eu quero expressar a concentração de NO2 da estação em Londres em mg/m3
air_quality["london_mg_per_cubic"] = air_quality["station_london"] *  1.882

air_quality.head()

#%%
# Quero verificar a proporção dos valores em Paris versus Antuérpia
# e salvar o resultado em uma nova coluna
air_quality["ratio_paris_antwerp"] = (
    air_quality["station_paris"] / air_quality["station_antwerp"]
)
air_quality.head()

#%%
# Quero renomear as colunas de dados para os identificadores de 
# estação correspondentes usados pelo OpenAQ
air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westiminster",
    }
)
air_quality_renamed.head()

#%%
# Conversão para letras minúsculas
air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
air_quality_renamed.head()