import openai
import streamlit as st
import json


openai.api_key = st.secrets["OPENAI_API_KEY"]

# define models
models = {
    "Davinci": "text-davinci-003",
    "Curie": "text-curie-001",
    "Babbage": "text-babbage-001",
    "Ada": "text-ada-001",
}
st.title("CHATGPT Prompt")

response = ""

input_text = st.text_area("Input Text", label_visibility="visible", height=400)
with st.sidebar:
    model = st.selectbox("ChatGPT model", ("Davinci", "Curie", "Babbage", "Ada"))
    model = models[model]
    # Controls randomness, so a low temperature is less random (deterministic), while a high temperature is more random.
    temperature = st.slider(
        label="Temperature", min_value=0.0, max_value=1.0, value=0.8
    )
    # Specifies the maximum number of tokens that can be generated by the model. Note tokens can be word pieces.
    max_tokens = st.slider(
        label="Maximum Tokens", min_value=50, max_value=300, value=50
    )
    # Computes the cumulative probability distribution, cuts off as soon as that distribution exceeds the value of top_p
    top_p = st.slider(label="Top p", min_value=0.0, max_value=1.0, value=1.0)
    frequency_penalty = st.slider(
        label="Frequency Penalty", min_value=0.0, max_value=1.0, value=0.5
    )
    # Encourages the model to make novel predictions. The presence penalty lowers the probability of a word if it already appeared in the predicted text.
    presence_penalty = st.slider(
        label="Presence Penalty", min_value=0.0, max_value=1.0, value=0.0
    )
# submit prompt to openai
if st.button("Submit"):
    with st.spinner("Wait for it..."):
        response = openai.Completion.create(
            model=model,
            prompt=input_text,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
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

