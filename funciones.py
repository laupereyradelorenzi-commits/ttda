def estandarizar(df,columna):    
    df_estandarizar=df.copy()
    df_estandarizar[columna] =  df_estandarizar[columna].min()