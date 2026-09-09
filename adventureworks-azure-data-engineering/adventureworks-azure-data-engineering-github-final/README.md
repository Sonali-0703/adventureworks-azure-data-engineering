# 🚀 AdventureWorks Azure Data Engineering Project

An end-to-end Azure data engineering portfolio project built around the AdventureWorks dataset.

The project demonstrates a practical cloud data pipeline:

**Azure Resource Group → ADLS Gen2 → ADF Git-based Dynamic Ingestion → Bronze → Databricks/Unity Catalog → Silver → Gold → Synapse/Analytics**

> **Portfolio note:** This repository contains sanitized documentation and examples. No passwords, access keys, SAS tokens, client secrets, tokens, or secret-bearing connection strings are stored here.

---

## 🏗️ Architecture

```text
                         AZURE
                           │
                           ▼
                  ┌─────────────────┐
                  │ Resource Group  │
                  │    AWSPROJECT   │
                  └────────┬────────┘
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
      ┌──────────────┐          ┌──────────────────┐
      │ ADLS Gen2    │          │ Azure Data Factory│
      │ dlawstorage  │◄─────────│ adf-aw-project-an│
      └──────┬───────┘          └────────┬─────────┘
             │                           │
             │                    Git Repository
             │                           │
             │                       LookupGit
             │                           │
             │                       ForEachGit
             │                           │
             │                      DynamicCopy
             │                           │
             ▼                           ▼
        ┌─────────── BRONZE / RAW ◄──────┘
        │
        ▼
 ┌────────────────────┐
 │ Azure Databricks   │
 │ adb-aw-project0    │
 │ Serverless         │
 └─────────┬──────────┘
           │
           ▼
 ┌────────────────────┐
 │ Unity Catalog      │
 │ adb-aw-metastore0  │
 └─────────┬──────────┘
           │
           ▼
      PySpark ETL
           │
           ▼
        SILVER
           │
           ▼
         GOLD
           │
           ▼
 Azure Synapse Analytics
           │
           ▼
      Analytics / BI
```

---

## ☁️ Azure Resource Inventory

| Component | Resource / Name |
|---|---|
| Resource Group | `AWSPROJECT` |
| ADLS Gen2 Storage Account | `dlawstorage` |
| Bronze Container | `bronze` |
| Silver Container | `silver` |
| Azure Data Factory | `adf-aw-project-an` |
| Databricks Workspace | `adb-aw-project0` |
| Unity Catalog Metastore | `adb-aw-metastore0` |
| Storage Credential | `adls-bronze-credential` |
| Bronze External Location | `bronze-location` |
| Silver External Location | `silver-location` |
| Databricks Compute | Serverless Notebook Compute |

---

## 🔄 ADF Dynamic Ingestion

The main dynamic ingestion pipeline is:

```text
Git Source
    │
    ▼
LookupGit
    │
    ▼
ForEachGit
    │
    ▼
DynamicCopy
    │
    ▼
ADLS Gen2 / Bronze
```

The design allows one reusable pipeline to process multiple source items instead of creating one copy activity per file.

The documented ADF run completed successfully and processed **12 items**.

### ADF pipelines

- `DynamicGitToRaw`
- `GitToRaw`

### ADF datasets

- `ds_git_dynamic`
- `ds_git_parameters`
- `ds_https`
- `ds_raw`
- `ds_sink_dynamic`

---

## 🥉 Bronze Layer

Bronze is the raw landing layer.

```text
abfss://bronze@dlawstorage.dfs.core.windows.net/
```

The ingestion layer preserves source data before downstream transformation.

---

## 🧱 Databricks + Unity Catalog

Databricks Serverless is used for PySpark processing.

Unity Catalog is configured with:

- Metastore: `adb-aw-metastore0`
- Storage credential: `adls-bronze-credential`
- External location: `bronze-location`
- External location: `silver-location`

The project uses managed identity-based access rather than embedding storage account keys in notebook code.

---

## 🥈 Silver Transformation

A documented Calendar transformation creates:

- `Month`
- `Year`

Example:

```python
Calendar = Calendar.withColumn("Month", month(col("Date")))                    .withColumn("Year", year(col("Date")))
```

The transformed Calendar dataset is written as Parquet to:

```text
abfss://silver@dlawstorage.dfs.core.windows.net/Adventure_Calendar
```

A Customers transformation example is also documented:

```python
Customers = Customers.withColumn(
    "FullName",
    concat_ws(" ", col("FirstName"), col("LastName"))
)
```

---

## 🥇 Gold & Synapse

The Gold analytics layer and Azure Synapse Analytics stage are completed parts of the project.

Gold contains business-ready analytical datasets and aggregations built from the processed data.

Azure Synapse Analytics is used as the downstream analytics component for querying and serving the prepared data.

---

## 📂 Repository Structure

```text
adventureworks-azure-data-engineering/
│
├── README.md
├── .gitignore
├── LICENSE
├── docs/
├── azure/
├── databricks/
├── sql/
├── config/
├── screenshots/
└── data/
```

See the individual folders for implementation notes.

---

## 🔐 Security

Never commit:

- Azure storage account keys
- SAS tokens
- Passwords
- Client secrets
- Access tokens
- Service-principal secrets
- Secret-bearing connection strings
- `.env` files containing secrets

Use Azure-managed identity, Azure Key Vault, or secret-backed connection mechanisms instead.

---

## 🎯 Skills Demonstrated

- Azure Resource Groups
- ADLS Gen2
- Azure Data Factory
- Git integration
- Dynamic pipelines
- Lookup activity
- ForEach activity
- Dynamic Copy activity
- Parameterized datasets
- Bronze/Silver/Gold architecture
- Azure Databricks
- PySpark
- Unity Catalog
- Managed identity
- External locations
- Azure Synapse Analytics
- Cloud data engineering
