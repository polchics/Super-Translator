import streamlit as st
from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

st.title("English → Definition, Synonyms & Russian Translator")

# User input
word = st.text_input("Enter an English word or phrase:")

if word:
    with st.spinner("Thinking..."):
        # Prompt to get definition, synonyms, and Russian translation
        prompt = f"""
        Provide the following for the English word/phrase: "{word}"
        1. Definition in English
        2. Synonyms
        3. Translation to Russian
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        answer = response.choices[0].message.content

    st.subheader("Result:")
    st.write(answer)
