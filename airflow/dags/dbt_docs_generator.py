from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime as dt
from datetime import timedelta

default_args = {
    'owner': 'bereket',
    'depends_on_past': False,
    'email': ['bekakibru2@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'start_date': dt(2021, 9, 13),
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'dbt_docs_generator_dag',
    default_args=default_args,
    description='An Airflow DAG to invoke simple dbt commands',
    schedule_interval='@once',
)


generate_docs = BashOperator(
    task_id='generate_docs',
    bash_command='cd ../../dbt && dbt docs generate',
    dag=dag
)

generate_docs
