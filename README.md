# AWS GenAI Ticket Resolution Pipeline

## Overview
An AI-powered support ticket intelligence pipeline built using:

- AWS EMR
- PySpark
- Amazon Bedrock
- Claude 3 Sonnet
- Retrieval-Augmented Generation (RAG)
- Amazon S3

This project automates customer support ticket classification and generates grounded resolution recommendations using enterprise knowledge retrieval.

---

## Problem Statement
Customer support teams receive thousands of unstructured support tickets like:

> "Payment deducted but order failed"

Manual triaging is slow and inconsistent.

This pipeline automates:

✅ Ticket understanding  
✅ Sentiment analysis  
✅ Priority assignment  
✅ Department routing  
✅ Solution recommendation using RAG

---

## Architecture Flow

Customer Tickets (Amazon S3 CSV)  
↓  
PySpark on AWS EMR  
↓  
Distributed Processing using mapPartitions()  
↓  
Amazon Bedrock Classification (Claude 3 Sonnet)  
↓  
Generate:
- Summary
- Sentiment
- Priority
- Department

↓  
Amazon Bedrock Knowledge Base (RAG)  
↓  
Retrieve enterprise support docs  
↓  
Generate grounded solution recommendation  
↓  
Final enriched ticket dataset

---

## Sample Input

```csv
ticket_id,issue_text
101,Unable to download invoice
102,OTP not received during login
103,Payment deducted but order failed
```

## Sample Output

```csv
ticket_id,summary,sentiment,priority,department,solution
101,Invoice issue,neutral,low,billing,Retry invoice download after settlement
102,OTP issue,neutral,medium,auth,Wait 2 minutes and retry OTP
103,Payment failure,negative,high,payments,Verify transaction and initiate refund workflow
```

---

## Tech Stack
- AWS EMR
- Apache Spark
- Amazon Bedrock
- Claude 3 Sonnet
- Retrieval-Augmented Generation
- Amazon S3
- Python

---

## Project Structure

```text
architecture/
outputs/
sample_data/
screenshots/
src/
README.md
```

---

## Business Impact
- Faster ticket triaging
- Automated routing
- Faster customer resolution
- Improved support productivity
- Better analytics on ticket categories
