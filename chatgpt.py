import os
import openai
import streamlit as st
import os.path
from dotenv import load_dotenv
import json

# do this twice to get top level directory
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
load_dotenv(os.path.join(basedir, ".env"))
openai.api_key = os.environ.get("OPENAI_API_KEY")

st.title("CHATGPT Prompt")

response = ""

input_text = st.text_area("Input Text", label_visibility="visible", height=400)

# contact OpenAI
if st.button("Submit"):
    with st.spinner("Wait for it..."):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=input_text,
            temperature=0.8,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
        )

if response:
    output_text = st.text_area(
        "Output Text",
        label_visibility="visible",
        disabled=True,
        height=400,
        value=response.choices[0].text,
    )
    st.json(json.dumps(response.to_dict()))
else:
    output_text = st.text_area(
        "Output Text", label_visibility="visible", disabled=True, height=400
    )