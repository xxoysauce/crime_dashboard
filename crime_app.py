import streamlit as st
import pandas as pd
import plotly.express as px

st.title("형법 범죄 통계 대시보드 (2012~2023)")

# 데이터
data = pd.DataFrame({
    "연도":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023],
    "전체 형법범죄":[2069,2098,2003,2054,1964,1867,1916,2012,2015,1773,1943,1986],
    "살인":[2.0,1.9,1.8,1.9,1.9,1.7,1.6,1.6,1.6,1.3,1.4,1.5],
    "강도":[5.3,4.0,3.2,2.9,2.3,1.9,1.6,1.6,1.3,1.0,1.0,1.2],
    "성폭력(강간 포함)":[42.5,53.4,58.8,60.9,57.3,63.9,62.2,61.9,58.1,63.5,80.2,74.8],
    "폭행":[255.2,250.9,288.9,316.8,336.0,322.2,318.9,312.8,277.0,230.9,250.2,238.1],
    "절도":[583.8,576.7,525.7,483.0,397.5,358.9,344.0,362.5,347.4,322.2,353.6,367.3]
})


st.sidebar.header("⚙️ 옵션 선택")


crimes = ["살인","강도","성폭력(강간 포함)","폭행","절도"]
selected_crimes = st.sidebar.multiselect("보고 싶은 범죄를 선택하세요", crimes, default=crimes)

year = st.sidebar.slider("연도를 선택하세요", 2012, 2023, 2023)


st.subheader("📊 원본 데이터")
st.dataframe(data)


st.subheader("📈 전체 형법범죄 추이")
fig1 = px.line(data, x="연도", y="전체 형법범죄", markers=True, title="전체 형법범죄 추이")
st.plotly_chart(fig1, use_container_width=True)


st.subheader("📉 주요 범죄 추이")
if selected_crimes:
    fig2 = px.line(data, x="연도", y=selected_crimes, markers=True, title="주요 범죄 추이")
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.info("사이드바에서 범죄 유형을 선택하세요!")


st.subheader(f"📌 {year}년 범죄 분포")
row = data[data["연도"] == year].melt(id_vars=["연도"], value_vars=crimes, var_name="범죄", value_name="발생 건수")
fig3 = px.bar(row, x="범죄", y="발생 건수", color="범죄", text="발생 건수", title=f"{year}년 범죄 분포")
st.plotly_chart(fig3, use_container_width=True)


fig4 = px.pie(row, names="범죄", values="발생 건수", title=f"{year}년 범죄 비중", hole=0.3)
st.plotly_chart(fig4, use_container_width=True)
