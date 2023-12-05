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


col1, col2 = st.columns(2)
df["case_month"] = pd.to_datetime(df["case_month"])

startDate = pd.to_datetime(df["case_month"]).min()
endDate = pd.to_datetime(df["case_month"]).max()

with col1:
    date1 = pd.to_datetime(st.date_input("Start Date", startDate))
with col2:
    date2 = pd.to_datetime(st.date_input("End Date", endDate))

df = df[(df["case_month"] >= date1) & (df["case_month"] <= date2)].copy()



st.sidebar.header("Choose your filter:")
state = st.sidebar.multiselect("Pick your State", df["res_state"].unique())

if not state:
    df2 = df.copy()
else:
    df2 = df[df["res_state"].isin(state)]

df2
df2.shape

