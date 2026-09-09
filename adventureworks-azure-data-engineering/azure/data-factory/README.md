# Azure Data Factory

**Factory:** `adf-aw-project-an`

## Pipelines

- `GitToRaw`
- `DynamicGitToRaw`

The dynamic pipeline is the main portfolio example.

```text
LookupGit
   ↓
ForEachGit
   ↓
DynamicCopy
   ↓
ADLS Gen2 Bronze
```

A documented execution completed successfully with 12 processed items.
