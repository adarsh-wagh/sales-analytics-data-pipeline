import pandas as pd
import numpy as np


def clean_dates(df):

    date_columns = [
        "sls_order_dt",
        "sls_ship_dt",
        "sls_due_dt"
    ]

    for col in date_columns:

        df[col] = df[col].astype("string")

        df[col] = np.where(
            (df[col].str.len() != 8),
            None,
            df[col]
        )

        df[col] = pd.to_datetime(
            df[col],
            format="%Y%m%d",
            errors="coerce"
        )

    return df


def recalculate_sales(df):

    invalid_sales = (
        df["sls_sales"].isna()
        | (df["sls_sales"] <= 0)
        | (
            df["sls_sales"]
            != df["sls_quantity"] * df["sls_price"].abs()
        )
    )

    df.loc[
        invalid_sales,
        "sls_sales"
    ] = (
        df["sls_quantity"]
        * df["sls_price"].abs()
    )

    return df


def recalculate_price(df):

    invalid_price = (
        df["sls_price"].isna()
        | (df["sls_price"] <= 0)
    )

    df.loc[
        invalid_price,
        "sls_price"
    ] = (
        df["sls_sales"]
        / df["sls_quantity"].replace(0, np.nan)
    )

    return df


def transform(df):

    df = clean_dates(df)
    df = recalculate_sales(df)
    df = recalculate_price(df)

    return df