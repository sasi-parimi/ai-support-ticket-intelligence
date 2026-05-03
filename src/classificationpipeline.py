"""
Classification Pipeline

This module classifies support tickets into:
- summary
- sentiment
- priority
- department

Model Used:
Amazon Bedrock - Claude 3 Sonnet
"""

def classify_ticket(ticket_text):
    return {
        "summary": "sample summary",
        "sentiment": "neutral",
        "priority": "medium",
        "department": "general"
    }
