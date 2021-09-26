from airflow import DAG
from datetime import timedelta
from datetime import datetime as dt
from airflow.operators.bash_operator import BashOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.operators.email_operator import EmailOperator

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
    'populate_data',
    default_args=default_args,
    description='An Airflow DAG to populate data',
    schedule_interval=timedelta(days=1),
)

check_file = BashOperator(
    task_id="check_file",
    bash_command="shasum ../../data/I80_stations.csv",
    retries=2,
    retry_delay=timedelta(seconds=15),
    dag=dag
)

insert = MySqlOperator(
    task_id='insert_I80_stations',
    mysql_conn_id="mysql_conn_id",
    sql="LOAD DATA INFILE '/var/lib/mysql-files/I80_stations.csv' INTO TABLE I80Stations FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS (ID,Fwy,Dir,District,County,City,@vState_PM,Abs_PM,Latitude,Longitude,@vLength,Type,Lanes,Name,User_ID_1,User_ID_2,User_ID_3,User_ID_4) SET State_PM = NULLIF( @vState_PM, ''),Length = NULLIF( @vLength, '');",
    dag=dag
)

email = EmailOperator(task_id='send_email',
                      to='bekakibru2@gmail.com',
                      subject='Daily report generated',
                      html_content=""" <h1>Congratulations! Your store reports are ready.</h1> """,
                      dag=dag
                      )

check_file >> insert >> email
