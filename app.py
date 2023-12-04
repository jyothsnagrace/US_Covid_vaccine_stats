import streamlit as st
import pandas as pd


def load_data():
    df = pd.read_csv("COVID-19_Case_Surveillance_Public_Use_Data_with_Geography.csv")
    return df


df = load_data()

df
df.shape

