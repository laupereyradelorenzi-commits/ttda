def eliminaDecimales(df, col):
    nueva_col = col + "_sin_decimales"
    df[nueva_col] = df[col].astype(int)
    
    return df