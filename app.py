import streamlit as st
import openai

# Make sure to set your API key as an environment variable before running:
# export OPENAI_API_KEY="your_api_key"

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("Super Translator 🔤")
st.write("Type an English word/phrase and get its definition, synonyms, and Russian translation.")

word = st.text_input("Enter an English word/phrase:")

if word:
    prompt = f"""
    For the word/phrase "{word}", provide:
    1. A clear English definition (1-2 sentences).
    2. 3-5 synonyms in English.
    3. The Russian translation.
    Format your answer as:
    Definition: ...
    Synonyms: ...
    Translation (RU): ...
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    answer = response["choices"][0]["message"]["content"]

    st.text_area("Result:", answer, height=200)

