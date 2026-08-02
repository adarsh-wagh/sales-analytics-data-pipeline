from utils.logging_config import logger
import pandas as pd

def read_csv(file, filename):

	try:

		logger.info(f"Reading file {filename}")

		df = pd.read_csv(file)

		df.columns = (
			df.columns
			.str.strip()
			.str.lower()
		)

		logger.info(f"Finished reading {filename} successfully")

		return df

	except Exception as e:

		logger.error(f"Failed to read {filename}: {e}")

		raise