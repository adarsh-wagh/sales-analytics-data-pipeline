from utils.logging_config import logger
from database.connection import connect_engine
from database.loader import load_dataframe
from utils.file_utils import validate_file
from extract.s3_reader import get_object_body, get_s3_client, list_bucket_objects
from extract.file_reader import read_csv
from pathlib import Path
from dotenv import load_dotenv
import os


def main():

    try:

        load_dotenv()

        source = os.getenv("SOURCE")

        logger.info(f"Starting Bronze layer load from {source}")

        loaded_tables = 0

        engine = connect_engine()

        if source == "local":

            raw_folder = os.getenv("RAW_FOLDER")
            if not raw_folder:
                raise ValueError("RAW_FOLDER not found in .env")

            filepath = Path(raw_folder)
            if not filepath.exists():
                raise FileNotFoundError(f"{filepath} does not exist.")

            for file in filepath.rglob("*.csv"):

                filename = file.stem
                validate_file(file)
                df = read_csv(file, filename)

                with engine.begin() as conn:

                    load_dataframe(df, filename, conn, "bronze")
                    loaded_tables += 1

        elif source == "s3":

            s3_client = get_s3_client()

            bucket = os.getenv("BUCKET")

            obj = list_bucket_objects(s3_client, bucket)

            for item in obj["Contents"]:

                if item["Key"].endswith(".csv"):

                    key = item["Key"]
                    filename = Path(key).stem

                    body = get_object_body(s3_client, bucket, key)

                    df = read_csv(body, filename)

                    with engine.begin() as conn:

                        load_dataframe(df, filename, conn, "bronze")
                        loaded_tables += 1

        else:
            raise ValueError(
                "Invalid SOURCE value in .env. Must be 's3' or 'local'.")
        
        logger.info(f"Bronze layer loaded successfully ({loaded_tables} tables)")

    except Exception as e:

        logger.error(f"failed to load Bronze: {e}")

        raise


if __name__ == "__main__":
    main()
