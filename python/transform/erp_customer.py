import numpy as np
import pandas as pd


def clean_customer_id(df):

    df["cid"] = df["cid"].str.replace(
        "^NAS",
        "",
        regex=True
    )

    return df


def remove_future_birthdays(df):

    df["bdate"] = pd.to_datetime(
        df["bdate"],
        errors="coerce"
    )

    today = pd.Timestamp.today().normalize()

    df.loc[
        df["bdate"] > today,
        "bdate"
    ] = pd.NaT

    return df


def standardize_gender(df):

    df["gen"] = (
        df["gen"]
        .str.strip()
        .str.upper()
    )

    conditions = [
        df["gen"].isin(["M", "MALE"]),
        df["gen"].isin(["F", "FEMALE"])
    ]

    values = [
        "Male",
        "Female"
    ]

    df["gen"] = np.select(
        conditions,
        values,
        default="Unknown"
    )

    return df


def transform(df):

    df = clean_customer_id(df)
    df = remove_future_birthdays(df)
    df = standardize_gender(df)

    return df