from utils.logging_config import logger
import boto3

def get_s3_client():

	try:
		logger.info("Initializing Amazon S3 client")
		
		s3_client = boto3.client("s3")

		logger.info("Amazon S3 client initialized successfully")
		
		return s3_client

	except Exception as e:

		logger.error(f"Failed to initialize Amazon S3 client: {e}")
		
		raise

def list_bucket_objects(s3_client,bucket):

	try:

		logger.info(f"Listing objects in bucket '{bucket}'")
    
		response = s3_client.list_objects_v2(
    		Bucket=bucket,
    		)


		logger.info(f"Retrieved {response.get('KeyCount', 0)} objects from '{bucket}'")

		return response

	except Exception as e:

		logger.error(f"Failed to list objects in bucket '{bucket}': {e}")

		raise

def get_object_body(s3_client,bucket,key):

	try:

		logger.info(f"Downloading '{key}' from bucket '{bucket}'")

		response = s3_client.get_object(
			Bucket=bucket,
			Key=key
			)

		body = response["Body"]

		logger.info(f"Successfully downloaded '{key}'")
	
		return body

	except Exception as e:

		logger.error(f"Failed to download '{key}' from '{bucket}': {e}")

		raise