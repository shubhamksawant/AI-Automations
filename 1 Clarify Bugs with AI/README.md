# Building an AI Bug Description Clarifier with OpenAI and Python

Modern development teams move fast — but bug reports often don’t.

Developers commonly write issues like:

> “App crashes when saving.”

While short reports are quick to write, they’re usually difficult for QA teams, engineers, or support teams to reproduce and debug effectively.

To solve this, I built a simple **AI Bug Description Clarifier** using Python and the OpenAI API that transforms informal bug reports into structured and professional issue summaries.

---

# Problem Statement

The xFusion AI Engineering team wanted a tool that could:

* Accept informal bug reports
* Rewrite them professionally
* Make them easier to understand and reproduce
* Standardize issue reporting across teams

---

# Tech Stack

* Python
* OpenAI API
* GPT-4.1 Mini
* Virtual Environment (`venv`)

---

# Project Structure

```bash
/root/openaiproject/
├── venv/
└── bug_clarifier.py
```

---

# Step 1 — Create Virtual Environment

First, create and activate a Python virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the OpenAI SDK:

```bash
pip install openai
```

---

# Step 2 — Create the Python Script

Create the file:

```bash
/root/openaiproject/bug_clarifier.py
```

---

# Step 3 — Full Python Code

```python
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
```

---

# Step 4 — Run the Script

```bash
python bug_clarifier.py
```

---

# Example Output

```text
Bug Summary:
The application crashes when the user clicks the save button.

Steps to Reproduce:
1. Open the application
2. Make changes
3. Click the save button

Expected Behavior:
The application should save changes successfully.

Actual Behavior:
The application crashes immediately after clicking save.
```

---

# Understanding the Prompt Engineering

The key part of this project is the **dynamic prompt**.

```python
prompt = f"""
...
Bug Report:
"{description}"
...
"""
```

Instead of hardcoding the bug report, the script dynamically inserts the developer’s input into the AI prompt.

This makes the tool reusable for any bug report.

---

# Why temperature=0.0?

```python
temperature=0.0
```

A low temperature ensures:

* Consistent responses
* Professional formatting
* Less randomness
* More deterministic outputs

Perfect for enterprise workflows and automation.

---

# Why Use GPT-4.1 Mini?

We used:

```python
model="openai/gpt-4.1-mini"
```

Because it provides:

* Fast responses
* Low cost
* High-quality structured outputs
* Great for automation pipelines

---

# Real-World Use Cases

This project can be extended into:

* Jira ticket enhancement
* AI-powered QA assistants
* GitHub issue standardization
* Slack/Discord bug-report bots
* Internal developer tooling

---

# Key Learnings

During this project, I learned:

* How to use the OpenAI Python SDK
* Prompt engineering basics
* Structuring AI outputs
* Using environment variables securely
* Building lightweight AI automation tools

---

# Future Improvements

Possible upgrades:

* Add severity classification
* Detect duplicate bugs
* Generate reproduction scripts
* Export issues to Jira/GitHub
* Add Streamlit UI
* Integrate with CI/CD pipelines

---

# Final Thoughts

AI is becoming incredibly useful for improving developer productivity.

Even a small automation like this can save engineering teams hours of clarification and back-and-forth communication.

This project is a great beginner-friendly introduction to:

* OpenAI APIs
* Prompt engineering
* AI automation with Python

---

# Connect With Me

* YouTube: https://www.youtube.com/@shubuntoo
* Instagram: https://www.instagram.com/shubuntoo
* GitHub: https://github.com/shubhamksawant
* LinkedIn: https://www.linkedin.com/in/shubhamsawant/
