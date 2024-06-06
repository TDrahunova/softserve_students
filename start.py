import streamlit as st

st.title('Головна')
st.divider()
st.page_link("start.py", label="Головна", icon="🏠")
st.page_link("pages/students.py", label="Студенти", icon="🎓")
st.page_link("pages/tasks.py", label="Завдання", icon="💀")
st.page_link("pages/sql.py", label="SQL", icon="⛄")
