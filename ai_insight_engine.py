# ===== File: ai_insight_engine.py =====
import openai
import os

# Load your OpenAI key from environment or Streamlit secrets
overlay_key = os.getenv("OPENAI_API_KEY") or st.secrets["OPENAI_API_KEY"]
openai.api_key = overlay_key

def generate_insight(context: dict) -> str:
    """
    Generates a short insight based on the selected section.
    Context contains at least 'section' key; can be extended with data point details.
    """
    prompt = f"You are an expert educational analyst. Provide a concise insight for the section: {context['section']}."
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content": prompt}],
        max_tokens=100,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()
