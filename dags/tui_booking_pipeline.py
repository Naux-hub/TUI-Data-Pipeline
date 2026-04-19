from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

# 1. Definiera standardinställningar för vår DAG
# TUI uppskattar "system reliability", så vi lägger in automatiska retries.
default_args = {
    'owner': 'samuel_montelius',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# 2. Skapa själva DAGen
# Denna är inställd på att köra en gång per dag (schedule_interval='@daily')
with DAG(
    'tui_daily_booking_analysis',
    default_args=default_args,
    description='Automated pipeline for extracting, cleaning, and analyzing TUI booking data',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
    tags=['tui', 'analytics', 'automation'],
) as dag:

    # 3. Definiera våra Tasks (Uppgifter)
    # I en riktig miljö skulle vi använda PythonOperator, men BashOperator 
    # är ett snyggt sätt att visa hur vi anropar våra fristående skript.

    task_clean_data = BashOperator(
        task_id='clean_raw_booking_data',
        # Peka på det första skriptet du skrev
        bash_command='python /path/to/TUI_Analytics_Project/cleaning.py', 
    )

    task_run_sql_analysis = BashOperator(
        task_id='run_sql_business_analysis',
        # Peka på det andra skriptet du skrev
        bash_command='python /path/to/TUI_Analytics_Project/sql_analysis.py',
    )

    # 4. Sätt upp beroenden (Dependencies)
    # Datatvätten MÅSTE köras innan analysen kan påbörjas.
    task_clean_data >> task_run_sql_analysis