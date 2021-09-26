from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.operators.email_operator import EmailOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime as dt
from datetime import timedelta


default_args = {
    'owner': 'berket',
    'depends_on_past': False,
    'email': ['bekakibru2@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'start_date': dt(2021, 9, 13),
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'dbt_dag',
    default_args=default_args,
    description='An Airflow DAG to test simple dbt',
    schedule_interval=timedelta(days=1),
)
dbt_debug = BashOperator(
    task_id='dbt_debug',
    bash_command=' cd ../../dbt && dbt debug',
    dag=dag
)

dbt_run = BashOperator(
    task_id='dbt_run',
    bash_command=' cd ../../dbt && dbt run',
    dag=dag
)

dbt_test = BashOperator(
    task_id='dbt_test',
    bash_command='cd ../../dbt && dbt test',
    dag=dag
)
dbt_doc = BashOperator(
    task_id='dbt_doc',
    bash_command=' cd ../../dbt && dbt docs generate',
    dag=dag
)

dbt_run >> dbt_test >> dbt_doc
