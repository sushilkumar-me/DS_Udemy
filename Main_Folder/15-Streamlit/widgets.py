import streamlit as st 
import pandas as pd
st.title("Streamlit text input")

name = st.text_input("Enter your name")


age = st.slider("select your age ",0,100,25)

st.write(f"Your age is{age}")

options = ["python", "c++", "java", "SQL"]
choice = st.selectbox("Choose your favorite language:", options)
st.write(f"You selected {choice}")


if name: 
    st.write(f"Hello {name}")

data = {
    "Name": ["sushil", "jhon", "venky", "akash"], 
    "Age": [19,23,21,20], 
    "City": ["Bangalore", "kolkata", "Bangalore", "Surat"]
}

df = pd.DataFrame(data) 
df.to_csv("sampledata.csv")
st.write(df)

uploaded_files = st.file_uploader("Choose a CSV file", type = "csv")

if uploaded_files is not None: 
    df= pd.read_csv(uploaded_files)
    st.write(df)

    