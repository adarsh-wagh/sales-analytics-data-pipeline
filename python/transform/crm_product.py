import pandas as pd
import numpy as np

def extract_product_key(df):

	df[['cat_id','prd_key']] = df['prd_key'].str.extract(r'([A-Z]+-[A-Z]+)-(.+)')

	df['cat_id'] = df['cat_id'].str.replace('-', '_', regex=False)

	df = df[
        [
            "prd_id",
            "cat_id",
            "prd_key",
            "prd_nm",
            "prd_cost",
            "prd_line",
            "prd_start_dt",
            "prd_end_dt",
        ]
    ]

	return df

def handle_missing_cost(df):

    df["prd_cost"] = df["prd_cost"].fillna(0)

    return df

def standardize_product_line(df):

    df["prd_line"] = (
        df["prd_line"]
        .str.strip()
        .str.upper()
    )

    conditions = [
        df["prd_line"] == "S",
        df["prd_line"] == "M",
        df["prd_line"] == "R",
        df["prd_line"] == "T"
    ]

    values = [
        "Other Sales",
        "Mountain",
        "Road",
        "Touring"
    ]

    df["prd_line"] = np.select(
        conditions,
        values,
        default="Unknown"
    )

    return df

def calculate_end_date(df):

	df['prd_start_dt'] = pd.to_datetime(df['prd_start_dt'])

	df = df.sort_values(by=["prd_key", "prd_start_dt"])

	next_start_date  = df.groupby('prd_key')['prd_start_dt'].shift(-1)

	df["prd_end_dt"] = next_start_date - pd.Timedelta(days=1)

	return df

def transform(df):

    df = extract_product_key(df)
    df = handle_missing_cost(df)
    df = standardize_product_line(df)
    df = calculate_end_date(df)

    return df