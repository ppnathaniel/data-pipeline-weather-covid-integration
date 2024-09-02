# Global Weather and COVID-19 Impact Analysis

## Project Overview

This project demonstrates a complete data pipeline that collects, processes, and analyzes data from multiple sources. The focus is on analyzing the impact of weather conditions on COVID-19 cases by leveraging various open-source tools.

### Key Components
- **Data Collection:** Gather weather data from OpenWeatherMap API and COVID-19 data from the COVID-19 Data API.
- **Data Ingestion:** Ingest the collected data into Apache Kafka.
- **Data Storage:** Store the data in a data lake (Apache Hudi) and a data warehouse (Apache Hive).
- **Data Processing:** Use Apache Spark for batch and stream processing.
- **Data Consumption:** Analyze and visualize the data using Jupyter Notebooks.
- **Deployment:** Deploy the project infrastructure on AWS using Terraform.

## Project Structure

