import streamlit as st
import pandas as pd



import certifi, os
certifi.where()
os.environ['SSL_CERT_FILE'] = certifi.where()

# def load_data():
#     url = 'https://data.cdc.gov/resource/n8mc-b4w4.csv?$query=SELECT%0A%20%20%60res_state%60%2C%0A%20%20%60case_month%60%2C%0A%20%20%60age_group%60%2C%0A%20%20%60sex%60%2C%0A%20%20%60ethnicity%60%2C%0A%20%20%60race%60%2C%0A%20%20count(*)%20AS%20%60count%60%0AGROUP%20BY%0A%20%20%60res_state%60%2C%0A%20%20%60case_month%60%2C%0A%20%20%60age_group%60%2C%0A%20%20%60sex%60%2C%0A%20%20%60race%60%2C%0A%20%20%60ethnicity%60'
#     df = pd.read_csv(url)
#     # data = df.rename(columns={'long': 'lon'})
#     # data['month_sold'] = pd.to_datetime(data['date']).dt.month
#     return df


# df = load_data()

# df
# df.shape


df=[]
i=0
while True:
    if i==0:
        offset=""
    else:
        offset=f"%20offset%20{i}00"
    url = 'https://data.cdc.gov/resource/n8mc-b4w4.csv?$query=SELECT%0A%20%20%60res_state%60%2C%0A%20%20%60case_month%60%2C%0A%20%20%60age_group%60%2C%0A%20%20%60sex%60%2C%0A%20%20%60ethnicity%60%2C%0A%20%20%60race%60%2C%0A%20%20count(*)%20AS%20%60count%60%0AGROUP%20BY%0A%20%20%60res_state%60%2C%0A%20%20%60case_month%60%2C%0A%20%20%60age_group%60%2C%0A%20%20%60sex%60%2C%0A%20%20%60race%60%2C%0A%20%20%60ethnicity%60'
    temp=pd.read_csv(requests.get(url).text)
    if temp.shape[0]>0:
        df.append(pd.read_csv(requests.get(url).text))
        i+=1
    else:
        break
df=pd.concat(df)
df
df.shape