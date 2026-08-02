import numpy as np


def clean_customer_id(df):

    df["cid"] = (
        df["cid"]
        .str.replace("-", "", regex=False)
    )

    return df


def standardize_country(df):

    df["cntry"] = (
        df["cntry"]
        .fillna("")
        .str.strip()
    )

    conditions = [
        df["cntry"] == "DE",
        df["cntry"].isin(["US", "USA"]),
        df["cntry"] == ""
    ]

    values = [
        "Germany",
        "United States",
        "Unknown"
    ]

    df["cntry"] = np.select(
        conditions,
        values,
        default=df["cntry"]
    )

    return df


def transform(df):

    df = clean_customer_id(df)
    df = standardize_country(df)

    return df