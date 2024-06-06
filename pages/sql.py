import streamlit as st

from data import SQL
from ui import UiHelper

UiHelper.breadcrumb("sql")

st.title("SQL Editor")
st.divider()
sql = st.text_area("SQL Editor")
if st.button("Run sql script"):
    data = SQL.run_sql(sql)
    st.write("#### SQL результат")
    st.dataframe(data, hide_index=True)
    st.divider()

st.write("### Table 'students'")
st.dataframe(SQL.run_sql("select * from students"), hide_index=True)
st.divider()

st.write("### Table 'std_group'")
st.dataframe(SQL.run_sql("select * from std_group"), hide_index=True)
st.divider()

st.write("### Table 'scores'")
st.dataframe(SQL.run_sql("select * from scores"), hide_index=True)
st.divider()
