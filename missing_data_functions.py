import numpy as np
import pandas as pd

def add_nans_to_df(df,col_prob=0.05):
    '''
    Input: df, a df to randomly insert nans into
    Input: col_prob, the per numeric col % of nans to add in 0<x<1
    Output: df_nans, a df of the same size - just with nans added

    Note: Doesn't change df passed in
    '''
    df_nans = df.copy()
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    for col in numeric_cols:
        df_nans[col] = df[col].sample(frac=1-col_prob)
    return df_nans
