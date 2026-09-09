# ADLS Gen2 Storage

**Storage Account:** `dlawstorage`

The data lake uses Azure Data Lake Storage Gen2.

## Containers

- `bronze` — raw ingested data
- `silver` — transformed data

Bronze path:

```text
abfss://bronze@dlawstorage.dfs.core.windows.net/
```

Silver path:

```text
abfss://silver@dlawstorage.dfs.core.windows.net/
```

Hierarchical namespace is required for ADLS Gen2.
