def calculaRatio(df, col1, col2):
    ratio = df[col1] / df[col2]
    if (ratio > 1).any():
        raise ValueError("Error: existe al menos un valor del ratio mayor que 1.")
    nueva_col = f"{col1}_ratio_{col2}"
    df[nueva_col] = ratio
    
    return df