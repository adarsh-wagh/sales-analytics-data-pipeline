from utils.logging_config import logger

def validate_file(file):

    if not file.exists():

        logger.error(f"{file} does not exist.")

        raise FileNotFoundError(f"{file} does not exist.")
