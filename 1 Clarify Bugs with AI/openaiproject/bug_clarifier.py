# /root/openaiproject/bug_clarifier.py

import os
from openai import OpenAI

# Initialize OpenAI client using environment variables
client = OpenAI(
    api_key=os.environ.get("API_KEY"),
    base_url=os.environ.get("BASE_URL")
)


def clarify_bug(description: str) -> str:
    """
    Converts an informal bug description into a clear,
    structured, and professional issue summary.
    """

    prompt = f"""
You are a professional QA engineer.

Rewrite the following informal bug report into a clear,
structured, and professional bug summary.

Bug Report:
"{description}"

Provide:
1. Bug Summary
2. Steps to Reproduce
3. Expected Behavior
4. Actual Behavior
"""

    response = client.chat.completions.create(
        model="openai/gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=100,
        temperature=0.0
    )

    return response.choices[0].message.content.strip()


# Input bug report
bug_description = "App keeps crashing when I click save."

# Store AI response in variable named response
response = clarify_bug(bug_description)

# Print clarified bug summary
print(response)