# Interview Notes

## Explain the project in one minute

I built an AdventureWorks data engineering pipeline on Azure. ADLS Gen2 is used as the data lake, and Azure Data Factory performs Git-based dynamic ingestion into the Bronze layer. The dynamic pipeline uses Lookup, ForEach and Dynamic Copy activities with parameterized datasets so the same logic can process multiple files. Azure Databricks Serverless and PySpark are then used for transformations, with Unity Catalog and managed identity providing governed access to ADLS. The processed data is written to the Silver layer, with Gold and Synapse used for downstream analytics. The Gold and Synapse stages are completed in the project.

## Why Lookup?

Lookup retrieves metadata or the collection of items that drives the pipeline.

## Why ForEach?

ForEach repeats the same processing logic for every item returned by Lookup.

## Why Dynamic Copy?

Dynamic Copy allows the source file/path and destination to be determined at runtime.

## Why parameterized datasets?

They make datasets reusable instead of hard-coding one file or folder into each dataset.

## Why Bronze?

Bronze preserves source data in a raw landing layer so the original input remains available for downstream processing.
