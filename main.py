import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(layout="wide")
dosya=pd.read_csv("fortune.csv")
st.title("Dunyadaki En Degerli 500 Sirket")
dosya=dosya.drop(columns=["hqstate","permalink"])
yearlist=list(dosya["year"].unique())
yearlist.insert(0,"All Years")
yearst=st.selectbox("Yıl Sec",yearlist)
st.write("Burdan Yılları Seçerek Datayı Filtreleyebilirsiniz")
if yearst!="All Years":
    dosya=dosya[dosya["year"]==yearst]
st.dataframe(dosya)

col1,col2=st.columns(2)
with col1:
    columns3=["sector","industry"]
    columnst3=st.selectbox("X Degerini Sec",columns3)
    st.write("Burdan Asagidaki Grafik icin X Degerini secebilirsiniz")
with col2:
    columns4 = ["revenues", "revchange", "profits", "prftchange", "assets", "employees"]
    columnst4=st.selectbox("Y Degerini Sec",columns4)
    st.write("Burdan Asagidaki Grafik icin Y Degerini Secebilirsiniz")
dosya=dosya[[columnst3,columnst4]]
dosya=dosya.groupby(columnst3)[columnst4].mean()
dosya=dosya.reset_index()
dosya=dosya.sort_values(by=[columnst4],ascending=False)
graphslist=["Bar Graph","Pie Graph"]
defaultx=graphslist.index("Pie Graph")
graphst=st.selectbox("Grafik Tipini Sec",graphslist,index=defaultx)
st.write("Grafik Tipini Secebilirsiniz")
if graphst=="Bar Graph":
    fig=px.bar(dosya,x=columnst3,y=columnst4,title=columnst3,height=800)
if graphst=="Pie Graph":
    fig=px.pie(dosya,values=columnst4,names=columnst3,title=columnst3,height=700)
st.plotly_chart(fig,use_container_width=True)
st.write("Sag Taraftaki Legend Kısmından cift tıklayarak 1 veya 1'den fazla olcak sekilde spesifik secimler yapabilirsiniz")
#st.dataframe(dosya)
st.write("  ")
st.write("  ")
st.write("Can Begen")
st.write("86180008")
st.write("Bilgi Görsellestirmesi")
