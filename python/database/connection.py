from sqlalchemy import create_engine
from dotenv import load_dotenv
from utils.logging_config import logger
import os

def connect_engine():

	try:
		logger.info("Starting Connection")

		load_dotenv()
	
		connection_string = os.getenv("CONNECTION_STRING")
	
		engine = create_engine(connection_string)

		logger.info("Database engine initialized")

		return engine

	except Exception as e:

		logger.error(f"Connection failed: {e}")
		
		raise

