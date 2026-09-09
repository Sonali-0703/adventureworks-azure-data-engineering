# End-to-End Data Flow

```text
Git
  ↓
Azure Data Factory
  ↓
LookupGit
  ↓
ForEachGit
  ↓
DynamicCopy
  ↓
ADLS Gen2 Bronze
  ↓
Azure Databricks Serverless
  ↓
Unity Catalog governed access
  ↓
PySpark transformations
  ↓
ADLS Gen2 Silver
  ↓
Gold / Analytics
  ↓
Synapse
```

The ADF stage is responsible for ingestion. Databricks is responsible for Spark-based transformation.
