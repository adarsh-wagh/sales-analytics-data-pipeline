from database.connection import connect_engine
from database.loader import load_dataframe
from extract.bronze_reader import read_table

from transform import (
    crm_customer,
    crm_product,
    crm_sales,
    erp_customer,
    erp_location,
    erp_category,
)

from utils.logging_config import logger


def main():

    logger.info("Starting Silver layer load")

    engine = connect_engine()

    tables = [
        ("cust_info", "cust_info", crm_customer),
        ("prd_info", "prd_info", crm_product),
        ("sales_details", "sales_details", crm_sales),
        ("cust_az12", "cust_az12", erp_customer),
        ("loc_a101", "loc_a101", erp_location),
        ("px_cat_g1v2", "px_cat_g1v2", erp_category),
    ]

    try:

        for bronze_table, silver_table, transformer in tables:

            logger.info(f"Processing {bronze_table}")

            with engine.begin() as conn:

                df = read_table(bronze_table, conn)

                df = transformer.transform(df)

                load_dataframe(df, silver_table, conn, "silver")

                logger.info(f"Finished {silver_table}")

        logger.info("Silver layer loaded successfully.")

    except Exception as e:

        logger.error(f"Silver load failed: {e}")

        raise


if __name__ == "__main__":
    main()