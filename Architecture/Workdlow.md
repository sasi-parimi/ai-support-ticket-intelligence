# Workflow

## End-to-End Pipeline

Customer Tickets (Amazon S3 CSV)
↓
PySpark on AWS EMR
↓
Distributed Processing using mapPartitions()
↓
Amazon Bedrock Classification (Claude 3 Sonnet)
↓
Generate:
- summary
- sentiment
- priority
- department
↓
Amazon Bedrock Knowledge Base (RAG)
↓
Retrieve enterprise support docs
↓
Generate grounded solution recommendation
↓
Final enriched ticket dataset
↓
Stored back in Amazon S3 / Support Dashboard
