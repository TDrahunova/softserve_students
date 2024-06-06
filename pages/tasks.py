import pandas
import streamlit as st
from data import TEST_CASE_1, TEST_CASE_2, TEST_CASE_3, TEST_COLUMN_CONFIG, SQL
from data import DEFECT_COLUMN_CONFIG, DEFECT_1, DEFECT_2, DEFECT_3
from ui import UiHelper

st.title('Завдання')
UiHelper.breadcrumb("tasks")

test_case_tab, bug_tab, sql_tab = st.tabs(["Тест кейси", "Дефект репорти", "SQL querry"])


def pretty_print(dframe: pandas.DataFrame):
    # st.dataframe(df, column_config=TEST_COLUMN_CONFIG, hide_index=True)
    return display(HTML(dframe.to_html().replace("\\n", "<br>")))


with test_case_tab:
    st.markdown("#### Task: Write 1 functional and 1 UI test case to test this page")
    st.divider()
    st.markdown("#### Functional test cases")
    st.markdown("**Test case ID:** 1")
    st.markdown("**Summary:** Перевірка коректного відображення таблиці зі списком студентів")
    st.markdown("**Test case type:** Functional")
    st.markdown("**Priority(high, medium, low):** high")
    st.markdown("**Precondition:** Зайти на сторінку https://softserve-variant6.streamlit.app/")
    st.markdown("##### Test steps:")

    st.dataframe(TEST_CASE_1.to_data_frame(), column_config=TEST_COLUMN_CONFIG, hide_index=True)
    st.markdown("**Post-condition:** Log out")
    st.markdown("**Author/Designer:** Drahunova Tetiana")
    st.markdown("**Status:** in-progress")
    st.markdown("**Created Date:** 06-06-2024")
    st.divider()

    st.markdown("**Test case ID:** 2")
    st.markdown("**Summary:** Перевірка сортування списку студентів у таблиці на сторінці СТУДЕНТИ")
    st.markdown("**Test case type:** Functional")
    st.markdown("**Priority(high, medium, low):** medium")
    st.markdown("**Precondition:** Зайти на сторінку https://softserve-variant6.streamlit.app/")
    st.markdown("##### Test steps:")

    st.dataframe(TEST_CASE_2.to_data_frame(), column_config=TEST_COLUMN_CONFIG, hide_index=True)
    st.markdown("**Post-condition:** Log out")
    st.markdown("**Author/Designer:** Drahunova Tetiana")
    st.markdown("**Status:** in-progress")
    st.markdown("**Created Date:** 06-06-2024")
    st.divider()

    st.markdown("#### UI test cases")

    st.markdown("**Test case ID:** 3")
    st.markdown("**Summary:** Перевірка положення UI елементів на сторінці СТУДЕНТИ")
    st.markdown("**Test case type:** UI")
    st.markdown("**Priority(high, medium, low):** low")
    st.markdown("**Precondition:** Зайти на сторінку https://softserve-variant6.streamlit.app/")
    st.markdown("##### Test steps:")

    st.dataframe(TEST_CASE_3.to_data_frame(), column_config=TEST_COLUMN_CONFIG, hide_index=True)
    st.markdown("**Post-condition:** Log out")
    st.markdown("**Author/Designer:** Drahunova Tetiana")
    st.markdown("**Status:** in-progress")
    st.markdown("**Created Date:** 06-06-2024")
    st.divider()

with bug_tab:
    st.markdown("#### Task: Find (or invent) and report 1 functional and more then 2 non-functional defects.")
    st.divider()
    st.markdown("**Defect ID:** 1")
    st.markdown("**Summary:** Некоректно відображені назви колонок в таблиці списку студентів на сторінці СТУДЕНТИ")
    st.markdown("**Defect type:** Functional")
    st.markdown("**Priority(high, medium, low):** low")
    st.markdown("**Severity(high, medium, low):** medium")
    st.markdown("**Environment:**")
    st.markdown("- MacOS 14.1.1 (23B81)")
    st.markdown("+ Google Chrome v123.0.6312.107")
    st.markdown("##### Steps to reproduce:")
    st.dataframe(DEFECT_1.to_data_frame(), column_config=DEFECT_COLUMN_CONFIG, hide_index=True)
    st.markdown("**Actual result:** Пошук студентів відбувається за Ім'ям")
    st.markdown("**Expected result:** Знайдено студентів по відповідним даним")
    st.divider()

    st.markdown("**Defect ID:** 2")
    st.markdown("**Summary:** Некоректно відбувається пошук студентів по-батькові на сторінці СТУДЕНТИ")
    st.markdown("**Defect type:** Non Functional")
    st.markdown("**Priority(high, medium, low):** medium")
    st.markdown("**Severity(high, medium, low):** low")
    st.markdown("**Environment:**")
    st.markdown("- MacOS 14.1.1 (23B81)")
    st.markdown("+ Google Chrome v123.0.6312.107")
    st.markdown("##### Steps to reproduce:")
    st.dataframe(DEFECT_2.to_data_frame(), column_config=DEFECT_COLUMN_CONFIG, hide_index=True)
    st.markdown(
        "**Actual result:** У колонці 'Прізвище' знаходиться ім'я студентів, у колонці 'Ім'я' знаходиться прізвище студентів")
    st.markdown(
        "**Expected result:** У колонці 'Прізвище' знаходиться прізвище студентів, у колонці 'Ім'я' знаходиться ім'я студентів")
    st.divider()

    st.markdown("**Defect ID:** 3")
    st.markdown("**Summary:** Некоректно відображена напис 'Кількість показаних  записів'")
    st.markdown("**Defect type:** Non Functional")
    st.markdown("**Priority(high, medium, low):** low")
    st.markdown("**Severity(high, medium, low):** medium")
    st.markdown("**Environment:**")
    st.markdown("- MacOS 14.1.1 (23B81)")
    st.markdown("+ Google Chrome v123.0.6312.107")
    st.markdown("##### Steps to reproduce:")
    st.dataframe(DEFECT_3.to_data_frame(), column_config=DEFECT_COLUMN_CONFIG, hide_index=True)
    st.markdown("**Actual result:** Показані 1-10 з :red-background[7] записів")
    st.markdown("**Expected result:** Показані 1-10 з :red-background[17] записів")
    st.divider()

with sql_tab:
    st.markdown(
        "#### Task: Write a sql-query that would receive information about all subjects (Subject) in which the student (Surname) and Score is above 90.")
    st.markdown("##### Table 'students':")
    st.dataframe(SQL.run_sql("select * from students limit 5"), hide_index=True)
    st.write("##### Table 'scores'")
    st.dataframe(SQL.run_sql("select * from scores limit 5"), hide_index=True)
    st.divider()
    sql_query = """select subject from scores 
    join students 
    on students.id = scores.id_stud 
    where students.sur_name = 'Петрівна' and scores.score > 90"""
    query=st.text_area("SQL query", value=sql_query)

    if st.button("Перевірити"):
        st.write("Результат:")
        st.dataframe(SQL.run_sql(query), hide_index=True)
