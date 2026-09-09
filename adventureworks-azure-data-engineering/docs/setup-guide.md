# Setup Guide

## 1. Resource group

Create/use:

`AWSPROJECT`

## 2. ADLS Gen2

Create/use:

`dlawstorage`

Enable hierarchical namespace when creating the storage account.

Create:

- `bronze`
- `silver`

## 3. Azure Data Factory

Create/use:

`adf-aw-project-an`

Configure source and destination linked services securely in ADF.

## 4. Git-based ingestion

Configure the Git/HTTP source in ADF.

The dynamic pipeline should use:

```text
LookupGit → ForEachGit → DynamicCopy
```

## 5. Datasets

Configure the five datasets documented in `azure/data-factory/datasets/`.

## 6. Databricks

Use:

`adb-aw-project0`

Run notebooks with Serverless Notebook Compute.

## 7. Unity Catalog

Use:

`adb-aw-metastore0`

Configure the storage credential and external locations documented under `databricks/unity-catalog/`.

## 8. Security

Do not place credentials in source code or GitHub.
