import typing

import streamlit as st


class UiHelper:

    @staticmethod
    @st.experimental_dialog("Поки що не підтримується")
    def not_implemented_yet() -> None:
        st.divider()
        st.write("Схоже, що цей функцонал, поки що, не підтримується")
        st.write("Вибачте за тимчасові незручності")
        if st.button("Вибачаю!!!"):
            st.session_state.vote = None
            st.rerun()

    @staticmethod
    def breadcrumb(inner: typing.Literal["students", "sql"]) -> None:
        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
        with col1:
            st.page_link("start.py", label="Головна  /", icon="🏠")
        with col2:
            if inner == "students":
                st.page_link("pages/students.py", label="Студенти", icon="🎓")
            if inner == "sql":
                st.page_link("pages/sql.py", label="SQL", icon="⛄")
