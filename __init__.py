import os

from dotenv import load_dotenv
from openai import OpenAI


# Load .env file
load_dotenv()


# Get OpenRouter API key
api_key = os.getenv("OPENROUTER_API_KEY")


if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env file")


# OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)


def analyze_email(email_text):

    prompt = f"""
You are an AI Email Security System.

Analyze the following email.

Classify it into exactly one category:

SPAM
NOT SPAM
PHISHING

Also provide:

1. Risk level: LOW, MEDIUM, HIGH, or CRITICAL
2. Confidence score from 0 to 100
3. Short reason
4. Suspicious keywords if any

Email:

{email_text}

Return the result in this format:

Classification: SPAM/NOT SPAM/PHISHING
Risk Level: LOW/MEDIUM/HIGH/CRITICAL
Confidence: XX%
Reason: ...
Suspicious Keywords: ...
"""


    response = client.chat.completions.create(

        model="openai/gpt-4o-mini",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0
    )


    return response.choices[0].message.content