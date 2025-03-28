#Yamilette

import streamlit as st
import os
import vertexai
from vertexai.generative_models import GenerativeModel

from dotenv import load_dotenv

load_dotenv()

vertexai.init(project=os.environ.get("my-ai-shoe-starter"), location="us-central1")

model = GenerativeModel("gemini-1.5-flash-002")

st.title("Find your neighboring states")

users_state = st.text_input("Enter your state")


# Section A: Add in your Vertex AI API call below
response = model.generate_content(
    "What are the neighboring states to " + users_state + "?"
)

# End of Section A


st.write(response.text)

# Section B:  Output the results to the user below


# End of Section B




