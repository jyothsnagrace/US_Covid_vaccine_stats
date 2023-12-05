import streamlit as st
import pandas as pd


def load_data():
    df = pd.read_csv("COVID-19_Case_Surveillance_Public_Use_Data_with_Geography.csv")
    return df


st.set_page_config(page_title="Covid 19 Vaccinated Demographics", page_icon=":mask", layout="wide")


st.title(":mask: _United States:_ Covid 19 Vaccinated Demographics :syringe: :mask:")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)


df = load_data()

df
df.shape

