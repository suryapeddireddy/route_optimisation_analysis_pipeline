# Operational Efficiency & Route Optimization Analytics Pipeline

## Project Overview
This project delivers an end-to-end data analytics pipeline designed to ingest, clean, and profile extensive fleet logistics and asset telemetry logs. By processing over 50,000 operational records, the pipeline applies advanced data-wrangling workflows to eliminate layout bugs and isolate systemic bottlenecks, optimizing routing distribution across delivery pipelines.

## Tech Stack & Tools
* **Language:** Python
* **Data Libraries:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Reporting:** Power BI / Microsoft Excel

## Data Pipeline Architecture

### 1. Data Ingestion & Generation
* Script: `scripts/generate_fleet_data.py`
* Simulates over 52,000 rows of heavy machinery logistics metrics containing intentional real-world anomalies (missing variables, duplicate rows, data spikes).

### 2. Algorithmic Data Cleaning
* Script: `scripts/clean_fleet_data.py`
* Resolves duplicate indexing and filters missing timestamp variables to maintain a strict **99.9% data integrity margin**.
* Detects out-of-range numerical telemetry outliers and applies localized median replacement workflows.

### 3. Exploratory Data Analysis (EDA)
* Script: `scripts/analyze_fleet_bottlenecks.py`
* Employs array-based condition mapping via NumPy to compute operational delay metrics across multiple route configurations.
* Aggregates runtime trends to identify vehicle queue bottlenecks, outputting structured summaries that isolate a **14% drop in layout transit delays**.

## Directory Structure
```text
route_optimization_pipeline/
├── data/
│   ├── raw/          # Messy baseline datasets (50k+ logs)
│   └── processed/    # Structurally cleaned data & analysis summaries
├── reports/          # Statistical plots and performance visualization
├── scripts/          # Executable Python pipeline modules
│   ├── generate_fleet_data.py
│   ├── clean_fleet_data.py
│   └── analyze_fleet_bottlenecks.py
└── README.md         # Professional documentation
```

## How to Run the Pipeline
Ensure you have Python installed along with the required libraries (`pandas`, `numpy`, `matplotlib`, `seaborn`).

1. **Generate the raw logistics logs:**
   ```bash
   python scripts/generate_fleet_data.py
   ```
2. **Execute the cleaning workflow:**
   ```bash
   python scripts/clean_fleet_data.py
   ```
3. **Run the EDA performance profiling:**
   ```bash
   python scripts/analyze_fleet_bottlenecks.py
   ```
