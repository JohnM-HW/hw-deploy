import pandas as pd
import datetime

def process_data(all_data, prod_data, stg_data, test_data):
    df = pd.DataFrame(all_data)
    df_prod = pd.DataFrame(prod_data)
    df_stg = pd.DataFrame(stg_data)
    df_test = pd.DataFrame(test_data)

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    date_range = pd.date_range(start=df["timestamp"].min(), end=df["timestamp"].max())
    grouped_data = df.groupby("timestamp").size().to_frame(name='RecordCount')
    result = grouped_data.reindex(date_range).fillna(0)

    df_prod["timestamp"] = pd.to_datetime(df_prod["timestamp"])
    df_stg["timestamp"] = pd.to_datetime(df_stg["timestamp"])
    df_test["timestamp"] = pd.to_datetime(df_test["timestamp"])

    return df, df_prod, df_stg, df_test, result

def process_full_data(full_data):
    df = pd.DataFrame(full_data)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    return df