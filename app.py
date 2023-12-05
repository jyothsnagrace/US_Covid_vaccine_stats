import streamlit as st
import pandas as pd
import altair as alt


def load_data():
    df = pd.read_csv("COVID-19_Case_Surveillance_Public_Use_Data_with_Geography.csv")
    df = df.rename(columns={'sex': 'gender'})
    df = df.apply(lambda x: x.replace({'Missing|Unknown|NA':'Other'}, regex=True))

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
race = st.sidebar.multiselect("Pick your Race", df["race"].unique())
ethnicity = st.sidebar.multiselect("Pick your Ethnicity", df["ethnicity"].unique())



AgeGender_count = df2.groupby(['age_group','gender'])['gender'].count().reset_index(name='count')
race_ethnicity_ct = df2.groupby(['race','ethnicity'])['ethnicity'].count().reset_index(name='count')


with col1:
    st.subheader(f"Vaccination status of {state} by Age Group by gender")
    bar = alt.Chart(AgeGender_count).mark_bar(
        cornerRadiusTopLeft=5,
        cornerRadiusTopRight=7).encode(
            # x='age_group:O',
            # y='count:Q',
            alt.X('age_group:O').axis().title('Age Group'),
            alt.Y('count:Q').axis().title('count'),
            color='gender:N'
            
    )
    st.altair_chart(bar, use_container_width=True, theme="streamlit")

with col2:
    st.subheader("Vaccination status by Race by Ethnicity")
    barh = alt.Chart(race_ethnicity_ct).mark_bar().encode(
        # x='race:O',
        alt.X('count').stack("normalize"),
        alt.Y('race:O').axis().title('Race'),
        color='ethnicity:N'
    )
    st.altair_chart(barh, use_container_width=True, theme="streamlit")