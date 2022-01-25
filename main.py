import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(layout="wide")
dosya=pd.read_csv("fortune.csv")
st.title("Fortune 500")
dosya=dosya.drop(columns=["hqstate","permalink"])
yearst=st.number_input("Select Year",min_value=min(dosya["year"]),max_value=max(dosya["year"]),value=2021)
if yearst:
    dosya=dosya[dosya["year"]==yearst]
st.dataframe(dosya)
columns1=["sector","industry"]
columns2=["revenues","revchange","profits","prftchange","assets","employees"]
col1,col2=st.columns(2)
with col1:
    columnst1=st.selectbox("Select Column",columns1,index=columns1.index("sector"))
dosya=dosya.set_index(columnst1)
with col2:
    columnst2=st.selectbox("Select Second Column",columns2,index=columns2.index("revenues"))
dosya=dosya.reset_index()
dosya=dosya[[columnst1,columnst2]]
radiost=st.radio("Select Graph",["GraphBar","GraphPie"])
if radiost=="GraphBar":
    fig=px.bar(dosya,x=columnst1,y=columnst2)
    st.plotly_chart(fig,use_container_width=True)
if radiost=="GraphPie":
    fig=px.pie(dosya,values=columnst2,names=columnst1,height=700)
    st.plotly_chart(fig, use_container_width=True)
st.write("Can Begen")
st.write("86180008")
st.write("Bilgi Görsellestirmesi")
