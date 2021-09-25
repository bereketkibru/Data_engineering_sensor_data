from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.operators.email_operator import EmailOperator
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
    'create_tables',
    default_args=default_args,
    description='An Airflow DAG to create tables',
    schedule_interval=timedelta(days=1),
)

create_table = MySqlOperator(
    task_id='create_table_mysql_external_file',
    mysql_conn_id='mysql_conn_id',
    sql='I80_davis_schema.sql',
    dag=dag,
)

create_table1 = MySqlOperator(
    task_id='create_table_mysql_external_file2',
    mysql_conn_id='mysql_conn_id',
    sql='I80_stations_schema.sql',
    dag=dag,
)

email = EmailOperator(task_id='send_email',
                      to='bekakibru2@gmail.com',
                      subject='Daily report generated',
                      html_content=""" <h1>Congratulations! Your store reports are ready.</h1> """,
                      dag=dag,
                      )

create_table >> create_table1 >> email
