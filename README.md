📊 **[Click here to view the Interactive Tableau Dashboard](https://public.tableau.com/authoring/TUI_Analytics_Project/Dashboard1#1)**
# TUI Analytics Showcase: Hotel Booking Demand Pipeline ✈️🏖️

## 📌 Project Overview
This project was built to demonstrate an end-to-end data pipeline and analytics workflow, specifically tailored to the travel and hospitality industry. It extracts raw hotel booking data, cleans it, processes it into a SQL database, and generates business insights. The workflow is designed to be automated using Apache Airflow.

## 🎯 Agile Framework
Following agile methodologies, this project was guided by the following criteria:

* **User Story:** As a Marketing Manager at TUI, I want to understand the relationship between booking lead times, customer origins, and cancellation rates, so that we can optimize our targeted marketing campaigns and pricing strategies.
* **Acceptance Criteria:**
  - Raw data is successfully extracted and cleaned using Python (Pandas).
  - Data is loaded into a relational database.
  - SQL queries successfully identify cancellation rates and average lead times by country.
  - The pipeline architecture is structured for daily automation.

## 🛠️ Tech Stack
* **Python (Pandas, NumPy):** Data extraction, transformation, and cleaning.
* **SQL (SQLite):** Data modeling, aggregation, and querying.
* **Apache Airflow:** Orchestration and pipeline automation (DAG structure provided).
* **Git/GitHub:** Version control and documentation.

## 📊 Key Business Insights Discovered
By querying the processed data, I uncovered the following insights relevant to resource planning and marketing:

1. **Cancellation Discrepancy:** - City Hotels experience a significantly higher cancellation rate (**41.79%**) compared to Resort Hotels (**27.77%**). 
   - *Recommendation:* Introduce stricter deposit policies for City Hotel bookings during peak seasons.
2. **Lead Time by Market:**
   - The German market (DEU) books the furthest in advance, averaging **139 days** prior to arrival.
   - The British market (GBR) follows closely with **126 days**.
   - *Recommendation:* Early-bird marketing campaigns for summer holidays should target Germany and the UK 4-5 months in advance, while domestic or short-haul markets can be targeted closer to the date.

## 🚀 Pipeline Architecture (Automation)
To eliminate manual data tasks, the pipeline is structured in `dags/tui_booking_pipeline.py` using **Apache Airflow**. 
- The DAG is scheduled `@daily`.
- It executes `cleaning.py` to handle missing values and create essential calculated columns (e.g., `total_guests`).
- Upon successful cleaning, it triggers `sql_analysis.py` to aggregate the data for dashboard consumption.
