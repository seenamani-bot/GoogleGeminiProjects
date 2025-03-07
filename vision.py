
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## fuction to load Gemini promodel and get response
model=genai.GenerativeModel("gemini-1.5-pro")
def get_gemini_response(input,image):
    if input !="":
     response=model.generate_content([input,image])
    else:
     response=model.generate_content(image)
     return response.text
    
st.set_page_config(page_title="Gemini Image Response Demo")
st.header("Gemini LLM Image Application")
input=st.text_input("Input what do you want from me: ",key="input")
uploaded_file=st.file_uploader("Upload an image",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
   image=Image.open(uploaded_file)
   st.image(image,caption="Uploaded Image",use_container_width=True)
submit=st.button("Tell me")

if submit:
    response=get_gemini_response(input,image)
    st.subheader("The response is")
    st.write(response)
