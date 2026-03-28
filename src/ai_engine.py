from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def fix_bug(code):
    try:
        prompt = f"""
You are an expert software engineer.

Analyze the following code:
{code}

1. Identify the bug or issue
2. Explain why it occurs
3. Provide corrected code

Keep response clean and structured.
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ ERROR: {str(e)}"
