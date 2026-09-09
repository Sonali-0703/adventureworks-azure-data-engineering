# Project Overview

## Objective

Build a reusable Azure data engineering pipeline for AdventureWorks data.

## Main stages

1. Create and organize Azure resources.
2. Store data in ADLS Gen2.
3. Land source files in the Bronze/Raw layer.
4. Build Azure Data Factory ingestion.
5. Connect the ingestion process to Git.
6. Use Lookup + ForEach + Dynamic Copy for reusable ingestion.
7. Use parameterized ADF datasets.
8. Process Bronze data with Databricks and PySpark.
9. Govern storage access with Unity Catalog.
10. Write transformed data to Silver.
11. Prepare Gold analytics and Synapse integration.

## Portfolio principle

Only sanitized configuration and reproducible documentation belong in GitHub.
Secrets remain in Azure.
