# Import libraries
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime
from airflow.operators.bash import BashOperator
from extract import extract_data



# Define the Dag
with DAG("ny_tlc_drivers_app", start_date=datetime(2024, 1, 1),
        schedule_interval="@daily", catchup=False) as dag:

        extract_task_01 = PythonOperator(
                task_id="extract_task_01",
                python_callable=extract_task,
                op_args={api_url}
        )

        transform_task_01 = PythonOperator(
                task_id="transform_task_01",
                python_callable=transform_task,
                op_args=['{{ ti.xcom_pull(task_ids="extract_task_01") }}']
        )

        load_task_01 = PythonOperator(
                task_id="load_task_01",
                python_callable=load_task,
                op_args=['{{ ti.xcom_pull(task_ids="transform_task_01") }}']
        )

        load_postgres = PostgresOperator(
                task_id="create_postgres_table",
                postgres_conn_id="postgres_conn",
                sql="""
                        create table if not exists tlc_driver (
                        app_no INT,
                        type VARCHAR,
                        application_date DATE, 
                        status VARCHAR,
                        other_requirements VARCHAR,
                        last_update TIMESTAMP)
                """
        )

        extract_task_01 >> transform_task_01 >> load_task_01

