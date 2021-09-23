FROM python:3.7
RUN pip install 'apache-airflow[postgres]==1.10.14' && pip install dbt==0.15
RUN pip install SQLAlchemy==1.3.23
RUN pip install apache-airflow-providers-postgres
RUN pip install apache-airflow-providers-mysql
RUN pip install dbt-mysql
RUN pip install mysql-connector-python
RUN mkdir /project
COPY scripts_airflow/ /project/scripts/
COPY dbt/profiles.yml /root/.dbt/profiles.yml
RUN chmod +x /project/scripts/init.sh
ENTRYPOINT [ "/project/scripts/init.sh" ]