# Import libraries
from tasks import extract, transform, load
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime
from airflow.operators.bash import BashOperator



# Define the Dag
with DAG(dag_id="ny_tlc_drivers_app", start_date=datetime(2024, 1, 1),
        schedule_interval="@daily", catchup=False) as dag:

        extract_task_01 = PythonOperator(
                task_id="extract_task",
                python_callable=extract.extract_data
                # op_args={api_url}
        )

        transform_task_01 = PythonOperator(
                task_id="transform_task",
                python_callable=transform.transform_data,
                op_args=['{{ ti.xcom_pull(task_ids="extract_task") }}']
        )

        load_task_01 = PythonOperator(
                task_id="load_task_01",
                python_callable=load.load_data,
                op_args=['{{ ti.xcom_pull(task_ids="transform_task") }}']
        )

        postgres_task_01 = PostgresOperator(
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

        postgres_task_02 = PostgresOperator(
                task_id="Insert_into_table",
                
        )

        extract_task_01 >> transform_task_01 >> load_task_01

