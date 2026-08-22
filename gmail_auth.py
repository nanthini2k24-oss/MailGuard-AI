import os
from dotenv import load_dotenv
from openai import OpenAI


# Load .env file
load_dotenv()


# Get OpenRouter API key
api_key = os.getenv("OPENROUTER_API_KEY")


# Check API key
if not api_key:
    raise ValueError(
        "OPENROUTER_API_KEY not found. "
        "Please check your .env file."
    )


# Create OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)


def analyze_email(email_text):

    prompt = f"""
You are an AI Email Security System.

Analyze the following email carefully.

Classify the email into exactly ONE of these categories:

SPAM
NOT SPAM
PHISHING

Also provide:

1. Risk Level: LOW, MEDIUM, HIGH, or CRITICAL
2. Confidence Score: 0 to 100
3. Reason
4. Suspicious Keywords
5. Security Recommendation

Email:

{email_text}

Return the result in this format:

Classification: SPAM / NOT SPAM / PHISHING
Risk Level: LOW / MEDIUM / HIGH / CRITICAL
Confidence: XX%
Reason: ...
Suspicious Keywords: ...
Recommendation: ...
"""

    response = client.chat.completions.create(

        # OpenRouter model
        model="openai/gpt-4o-mini",

        messages=[
            {
                "role": "system",
                "content": "You are an expert email security analyst."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0
    )

    result = response.choices[0].message.content

    return result