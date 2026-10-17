# E-Commerce End-to-End Data Pipeline & Analytics

An end-to-end data engineering and business intelligence project built on real-world e-commerce data from the Brazilian platform **Olist**.

This project implements an automated ETL pipeline that extracts raw CSV files, performs data cleaning and type transformations, and loads the data into a containerized PostgreSQL relational database. Analytical SQL queries are executed to extract business-critical insights regarding revenue, customer distribution, and payment behavior.

---

## Architecture & Tech Stack

- **Database & Infrastructure:** PostgreSQL 15, Docker & Docker Compose, pgAdmin 4
- **Scripting & ETL:** Python 3, Pandas, SQLAlchemy, Psycopg2
- **Data Modeling & Analytics:** Relational Data Modeling (3NF/Star Schema principles), Advanced SQL (Window Functions, Aggregations, Multi-table JOINs)

---

## Project Structure

```text
├── data/
│   └── raw/               # Raw e-commerce CSV datasets (excluded via .gitignore)
├── sql/
│   ├── schema.sql         # DDL scripts: table schemas and relational constraints (PK/FK)
│   └── analytics.sql      # Analytical SQL queries for business intelligence
├── src/
│   ├── db.py              # Centralized database engine and connection handling
│   └── etl.py             # Automated data cleaning, transformation, and ingestion script
├── docker-compose.yml     # Multi-container orchestration (PostgreSQL & pgAdmin)
├── requirements.txt       # Python project dependencies
└── README.md              # Project documentation

Future Improvements

Automating and scheduling the pipeline using Apache Airflow or Prefect.
Building data warehouse data models (staging / marts) using dbt
```
