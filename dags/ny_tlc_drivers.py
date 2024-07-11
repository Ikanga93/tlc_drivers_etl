# Import libraries
from extract import extract_data
from transform import transform_data
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime
from airflow.operators.bash import BashOperator



# Define the Dag
with DAG(dag_id="ny_tlc_drivers_app", start_date=datetime(2024, 1, 1),
        schedule_interval="@daily", catchup=False) as dag:

        extract_task = PythonOperator(
                task_id="extract_data",
                python_callable=extract_data,
        )

        transform_task = PythonOperator(
                task_id="transform_data",
                python_callable=transform_data,
                op_kwargs={"data": "{{ ti.xcom_pull(task_ids='extract') }}"}
        )

        extract_task >> transform_task
'''
        load_task = PostgresOperator(
                task_id="load_data",
                postgres_conn_id='postgres_conn' ,

                op_args=['{{ ti.xcom_pull(task_ids="transform_task") }}']
        )

        postgres_task_create = PostgresOperator(
                task_id="create_postgre_table",
                postgres_conn_id="postgres_conn",
                sql="""
                        create table if not exists tlc_drivers (
                        app_no INT,
                        type VARCHAR,
                        application_date DATE, 
                        status VARCHAR,
                        other_requirements VARCHAR,
                        last_update TIMESTAMP)
                        primary key app_no
                """
        )
'''
