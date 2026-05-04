# AWS GenAI Ticket Resolution Pipeline

> AI-powered support ticket classification and intelligent resolution generation using AWS EMR, PySpark, Amazon Bedrock, Claude 3 Sonnet, and Retrieval-Augmented Generation (RAG).

---

## Project Overview

This project builds an **AI-driven customer support automation pipeline** for e-commerce ticket handling.

It processes unstructured customer complaints and converts them into **actionable support intelligence** by automatically generating:

- Ticket Summary
- Sentiment Analysis
- Priority Level
- Department Routing
- Resolution Recommendation (via RAG)

This reduces manual triaging effort and improves customer support response time.

---

## Business Problem

Support teams receive thousands of tickets such as:

> **"Payment deducted but order failed"**

Manual processing creates:

- Slow routing  
- Inconsistent prioritization  
- Delayed resolution  
- Higher operational cost  

This pipeline automates the entire process.

---

## Architecture

```text
Customer Tickets (Amazon S3)
        ↓
PySpark on AWS EMR
        ↓
Distributed Processing using mapPartitions()
        ↓
Amazon Bedrock (Claude 3 Sonnet)
        ↓
Classification:
 • Summary
 • Sentiment
 • Priority
 • Department
        ↓
Amazon Bedrock Knowledge Base (RAG)
        ↓
Retrieve enterprise support documentation
        ↓
Generate grounded resolution recommendation
        ↓
Final enriched support dataset
```

---

## Sample Input

```csv
ticket_id,issue_text
101,Unable to download invoice
102,OTP not received during login
103,Payment deducted but order failed
104,App crashes during checkout
```

---

## Sample Output

```csv
ticket_id,summary,sentiment,priority,department,solution
101,Invoice issue,neutral,low,billing,Retry invoice download after settlement
102,OTP issue,neutral,medium,auth,Wait 2 minutes and retry OTP
103,Payment failure,negative,high,payments,Verify transaction and initiate refund workflow
104,Checkout app crash,negative,high,app,Clear cache and retry checkout process
```

---

## Tech Stack

- AWS EMR
- Apache Spark (PySpark)
- Amazon Bedrock
- Claude 3 Sonnet
- Retrieval-Augmented Generation (RAG)
- Amazon S3
- Python

---

## Repository Structure

```text
architecture/
outputs/
sample_data/
screenshots/
src/
README.md
```

---

## Key Engineering Concepts Used

- Distributed Data Processing using Spark partitions
- LLM-based classification pipeline
- Prompt engineering
- JSON structured response parsing
- Retrieval-Augmented Generation
- Knowledge Base grounding
- Cloud-scale ticket enrichment workflow

---

## Business Impact

- Faster ticket triaging  
- Automated department routing  
- Improved support productivity  
- Faster issue resolution  
- Better analytics visibility  
- Reduced manual operational effort  

---

## Future Improvements

- Batch inference optimization for Bedrock calls  
- Dashboard integration using BI tools  
- Real-time streaming ticket processing  
- Feedback loop for response quality improvement  
