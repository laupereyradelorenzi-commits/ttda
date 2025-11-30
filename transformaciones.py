def reemplazar_por_media(df, columna):
    df_reempl=df.copy()
    df_reempl['AvgBill'] =df_reempl['AvgBill'].mean()

    return df_reempl

    def crear_columna_ratio(df, num, den):
    df_num_den=df.copy()
    df_reempl['AvgBill'] =df_reempl['AvgBill'].mean()

    return df_reempl