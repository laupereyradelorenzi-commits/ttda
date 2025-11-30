
def normalizar(df, columna):
    df_normalitzat=df.copy()
    df_normalitzat[columna] =(df_normalitzat[columna] -df_normalitzat[columna].mean()) /df_normalitzat[columna].std

    return df_normalitzat
    
def estandarizar(df,columna):    
    df_estand=df.copy()
    df_estand[columna] = (df_estand[columna] - df_estand[columna].min()) / (df_estand[columna].max() - df_estand[columna].min())

    return df_estand