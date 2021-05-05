import streamlit as st
import time

# from .functions import *

st.title("Talk to someone you lost")
st.header('Covid-19 Mental Health Recovery')
st.subheader("Talk to someone you lost.\n Tell us how they talked to you and this application will talk to you in the same manner")

file = st.file_uploader("Upload your whatsapp chat here")
# print(file)

if file:
    st.text("Received file, training")
    st.progress(1)
    model = train_chat_model(file)
else:
    st.text("Please upload whatsapp chat data")

human_name = st.text_input('What is your Name')
bot_name = st.text_input('Tell us the name of the person you lost')
input_text = st.text_input('Enter the message you want to send to the one you lost', "I miss you")
output_text = " "

if input_text == "I miss you":
    output_text = str(bot_name) + " says:\n "
elif input_text == "":
    output_text == " "
else:
    output_text = "I am in a good place " + "\U0001f970"

# st.text_area(output_text)
st.text(output_text)