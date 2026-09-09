# Architecture

The project follows a layered cloud data architecture.

```text
                 ┌──────────────────────┐
                 │     Git Source       │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Azure Data Factory    │
                 │ Lookup / ForEach /    │
                 │ Dynamic Copy          │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ ADLS Gen2 Bronze     │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Azure Databricks      │
                 │ Serverless + PySpark │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Unity Catalog        │
                 │ Governance           │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ ADLS Gen2 Silver     │
                 └──────────┬───────────┘
                            │
                            ▼
                       Gold / Synapse
```
