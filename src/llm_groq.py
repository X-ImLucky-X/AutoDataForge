# src/llm_groq.py
"""Wrapper around Groq API (Free Tier).
Uses the `openai` client library but points to Groq's servers.
Groq offers free access to models like Llama 3.
"""
import os
import openai

# You can get a free key from: https://console.groq.com/keys
_API_KEY = os.getenv("GROQ_API_KEY")

# Configure the OpenAI client to use Groq's endpoint
client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=_API_KEY
)

def real_llm(prompt: str) -> str:
    """Send *prompt* to Groq (Llama 3) and return the reply."""
    if not _API_KEY:
        # If no key is provided, we can't call the API.
        # Fallback to dummy behavior to keep the project "working" (no crash).
        parts = prompt.split("\n\n", 1)
        text = parts[1] if len(parts) > 1 else prompt
        return "[MISSING GROQ KEY] " + text[:200]

    try:
        response = client.chat.completions.create(
            # "llama3-8b-8192" is a fast, free, and capable model on Groq
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        # Fallback if the API call fails
        parts = prompt.split("\n\n", 1)
        text = parts[1] if len(parts) > 1 else prompt
        return f"[GROQ ERROR: {e}] " + text[:200]
