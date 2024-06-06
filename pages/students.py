import pandas
import streamlit
import streamlit as st
from data import DatabaseStudents
from model import Key
from model import Default
from model import SearchColumns as Column
from model import SearchBy as SearchFilter

db = DatabaseStudents()


@st.experimental_dialog("Поки що не підтримується")
def not_implemented_yet() -> None:
    st.divider()
    st.write("Схоже, що цей функцонал, поки що, не підтримується")
    st.write("Вибачте за тимчасові незручності")
    if st.button("Вибачаю!!!"):
        st.session_state.vote = None
        st.rerun()


col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col1:
    st.page_link("start.py", label="Головна  /", icon="🏠")
with col2:
    st.page_link("pages/students.py", label="Студенти", icon="🎓")

st.title('Студенти')
if st.button("Новий запис"):
    not_implemented_yet()

page = st.session_state.get(Key.PAGE_NUMBER, Default.START_PAGE_NUMBER)
search_filter = None
search_col_1, search_col_2, search_col_3, search_col_4 = st.columns(4)
with search_col_1:
    search_column = st.selectbox("Пошук по", Column.ALL_OPTIONS, format_func=lambda x: x.label)
with search_col_2:
    search_value = st.text_input("Значення для пошуку")
with search_col_3:
    if st.button("Пошук"):
        search_filter = SearchFilter(search_column, search_value)
with search_col_4:
    if st.button("Очистити пошуковий фільтр"):
        page = Default.START_PAGE_NUMBER
        search_filter = None
        st.rerun()
filtered_students = db.get_filtered_students(search_filter)
per_page = Default.PER_PAGE_COUNT

found_students = filtered_students if search_filter else None

page = page or st.session_state.get(Key.PAGE_NUMBER, default=Default.START_PAGE_NUMBER)
last_page = db.get_count_of_pages(filtered_students)
is_last_page = page >= last_page
is_first_page = page <= 1
per_page = st.session_state.get(key=Key.STUDENTS_PER_PAGE, default=Default.PER_PAGE_COUNT)

start_records = (page - 1) * per_page + 1
end_records = page * per_page if not is_last_page else len(filtered_students) % per_page or page * per_page
if search_filter:
    st.write(
        f"Показані {start_records}-{end_records} із {len(filtered_students)} записів"
    )
else:
    st.write(
        "Показані 1-10 з 7 записів"
    )

config = {
    Column.ID.value: st.column_config.NumberColumn(Column.ID.label, width='small', required=True),
    Column.FIRST_NAME.value: st.column_config.TextColumn(Column.LAST_NAME.label, width='small', required=True),
    Column.LAST_NAME.value: st.column_config.TextColumn(Column.FIRST_NAME.label, width='small', required=True),
    Column.SUR_NAME.value: st.column_config.TextColumn(Column.SUR_NAME.label, width='small', required=True),
    Column.ADDRESS.value: st.column_config.TextColumn(Column.ADDRESS.label, width='large', required=True),
    Column.GROUP.value: st.column_config.SelectboxColumn(Column.GROUP.label, options=db.group_names())
}
students_data = db.students_to_dataframe(page, per_page, filtered_students)
st.dataframe(data=students_data, column_config=config, hide_index=True)

c1, c2, c3, c4, c5, c6, c7, c8 = st.columns(8)

with c1:
    if st.button('1 <<', disabled=is_first_page):
        st.session_state.__setattr__(Key.PAGE_NUMBER, Default.START_PAGE_NUMBER)
        st.rerun()

with c2:
    if st.button(f'{page - 1 if page > 2 else 1}<', disabled=is_first_page):
        st.session_state.__setattr__(Key.PAGE_NUMBER, page - 1)
        st.rerun()

with c3:
    st.button(label=str(page), disabled=True)

with c4:
    if st.button(label=f"{page + 1} > ", disabled=is_last_page):
        st.session_state.__setattr__(Key.PAGE_NUMBER, page + 1)
        st.rerun()

with c5:
    if st.button(label=f'{last_page} >>', disabled=is_last_page):
        st.session_state.__setattr__(Key.PAGE_NUMBER, db.get_count_of_pages())
        st.rerun()
