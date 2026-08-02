from utils.logging_config import logger
import pandas as pd


def read_table(table_name, conn):

    try:

        logger.info(f"Reading bronze.{table_name}")

        query = f"SELECT * FROM bronze.{table_name}"

        df = pd.read_sql(
            query, 
            con = conn
        )
        
        logger.info(
            f"Loaded {len(df)} rows from bronze.{table_name}"
        )

        return df

    except Exception as e:

        logger.error(
            f"Failed reading bronze.{table_name}: {e}"
        )

        raise