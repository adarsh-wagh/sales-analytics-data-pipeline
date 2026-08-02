from utils.logging_config import logger
import pandas as pd

def load_dataframe(df, filename, conn, schemas):

	try:

		logger.info(f"Loading {filename} into the database")

		df.to_sql(
			filename,
			con=conn,
			schema=schemas,
			if_exists="delete_rows",
			index=False,
			chunksize=10000
		)

		logger.info(f"Loaded {len(df)} rows into table '{filename}'")

	except Exception as e:

		logger.error(f"failed to load {filename} into the database: {e}")

		raise
