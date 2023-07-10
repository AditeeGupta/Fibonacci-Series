import openai
import streamlit as st
from streamlit_chat import message
openai.api_key = st.secrets['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']
def generate_response(prompt):
    completions = openai.Completion.create(
    model='davinci:ft-personal-2023-07-08-14-36-57',
    prompt = prompt,
    max_tokens = 1024,
    n = 1,
    stop = None,
    temperature = 0.5
    )
    message = completions.choices[0].text
    return message
st.title("Chatbot")

