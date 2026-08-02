from datetime import datetime, timedelta

from load.load_bronze import main as bronze_main
from load.load_silver import main as silver_main

from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.operators.email import EmailOperator


default_args = {
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}


with DAG(
    dag_id="sales_etl_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args=default_args,
) as dag:

    load_bronze = PythonOperator(
        task_id="load_bronze",
        python_callable=bronze_main,
    )

    validate_bronze = SQLExecuteQueryOperator(
        task_id="validate_bronze",
        conn_id="postgres_sales",
        sql="sql/validation/validate_bronze.sql",
    )

    load_silver = PythonOperator(
        task_id="load_silver",
        python_callable=silver_main,
    )

    validate_silver = SQLExecuteQueryOperator(
        task_id="validate_silver",
        conn_id="postgres_sales",
        sql="sql/validation/validate_silver.sql",
    )

    success_email = EmailOperator(
        task_id="send_success_email",
        to="abc@email.com",
        subject="Sales Analytics Pipeline - Success",
        html_content="""
        <h3>Sales Analytics Pipeline Completed Successfully</h3>
        <p>The Bronze and Silver ETL pipeline finished without errors.</p>
        """,
    )

    (
        load_bronze
        >> validate_bronze
        >> load_silver
        >> validate_silver
        >> success_email
    )
