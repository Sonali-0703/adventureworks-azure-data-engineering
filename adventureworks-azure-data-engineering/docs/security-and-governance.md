# Security and Governance

## Storage access

The project uses Unity Catalog storage credentials and Azure managed identity for governed ADLS access.

## GitHub safety

This repository intentionally excludes:

- storage keys
- SAS tokens
- passwords
- client secrets
- access tokens
- secret-bearing connection strings

## ADF

Linked services should hold credentials securely inside Azure Data Factory or through supported secret-management mechanisms.

## Databricks

Avoid `fs.azure.account.key...` configuration in Serverless notebooks. Use Unity Catalog storage credentials and external locations for governed storage access.
