import pandas as pd
import numpy as np

def remove_null_ids(df):

	df = df.dropna(subset=['cst_id'])

	return df

def keep_latest_customer(df):

	df = df.sort_values(
  	  by=["cst_id", "cst_create_date"],
  	  ascending=[True, False]
	)

	df = df.drop_duplicates(
  	  subset=["cst_id"],
  	  keep="first"
	).reset_index(drop=True)

	return df
	
	

def clean_names(df):
	df["cst_firstname"] = (
	    df["cst_firstname"]
	        .str.strip()
	)
	df["cst_lastname"] = (
	    df["cst_lastname"]
 	       .str.strip()
	)

	return df

def standardize_gender(df):

	df["cst_gndr"] = (
	    df["cst_gndr"]
	    .str.strip()
	    .str.upper()
	)

	gender_case = [
	    df["cst_gndr"].isin(["M", "MALE"]),
	    df["cst_gndr"].isin(["F", "FEMALE"]),
	]

	gender_values = [
	    "Male",
	    "Female"
	]

	df["cst_gndr"] = np.select(
    	gender_case,
    	gender_values,
    	default="Unknown"
	)

	return df

def standardize_marital_status(df):

	df["cst_marital_status"] = (
 	   df["cst_marital_status"]
 	   .str.strip()
 	   .str.upper()
	)
	
	marital_case = [
  	  df["cst_marital_status"].isin(["M","MARRIED"]),
	    df["cst_marital_status"].isin(["S","SINGLE"])
	]

	marital_values = [
  	  "Married",
 	   "Single"
	]


	df["cst_marital_status"] = np.select(
 	   marital_case,
 	   marital_values,
 	   default="Unknown"
	)

	return df

def transform(df):

    df = remove_null_ids(df)
    df = keep_latest_customer(df)
    df = clean_names(df)
    df = standardize_gender(df)
    df = standardize_marital_status(df)

    return df