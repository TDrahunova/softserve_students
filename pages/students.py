import math

import pandas
import streamlit as st

from data import SQL
from model import Default
from model import Key
from model import SearchBy as SearchFilter
from model import SearchColumns as Column
from ui import UiHelper

all_students = SQL.get_all_students()
all_students_count = SQL.get_students_count()


class PageHelper:
    per_page = st.session_state.get(Key.STUDENTS_PER_PAGE, Default.PER_PAGE_COUNT)

    @property
    def page(self) -> int:
        return st.session_state.get(Key.PAGE_NUMBER, Default.START_PAGE_NUMBER)

    def last_page(self, the_students: pandas.DataFrame | int | None) -> int:
        students_count = the_students if isinstance(the_students, int) else None
        if students_count is None:
            students_count = SQL.get_records_count(the_students) if the_students is not None else all_students_count
        return math.ceil(students_count / self.per_page)

    def is_last_page(self, the_students: int | pandas.DataFrame | None) -> bool:
        return self.page >= self.last_page(the_students)

    @property
    def is_first_page(self) -> bool:
        return self.page <= 1


ph = PageHelper()

UiHelper.breadcrumb("students")

st.title('Студенти')
if st.button("Новий запис"):
    UiHelper.not_implemented_yet()

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

page = ph.page
found_students = SQL.get_filtered_students(search_filter) if search_filter else SQL.get_page_students(ph.page,
                                                                                                      ph.per_page)

start_records = (page - 1) * ph.per_page + 1
records_found = SQL.get_records_count(found_students) if search_filter else all_students_count

end_records = start_records + ph.per_page if records_found % ph.per_page == 0 else page * ph.per_page

if search_filter:
    if records_found:
        st.write(
            f"Показані {start_records}-{end_records} із {len(found_students)} записів"
        )
    else:
        st.write(f"Записів не знайдено")
else:
    st.write(
        "Показані 1-10 з 7 записів"
    )

column_config = {
    Column.ID.value: st.column_config.NumberColumn(Column.ID.label, width='small', required=True),
    Column.FIRST_NAME.value: st.column_config.TextColumn(Column.LAST_NAME.label, width='small', required=True),
    Column.LAST_NAME.value: st.column_config.TextColumn(Column.FIRST_NAME.label, width='small', required=True),
    Column.SUR_NAME.value: st.column_config.TextColumn(Column.SUR_NAME.label, width='small', required=True),
    Column.ADDRESS.value: st.column_config.TextColumn(Column.ADDRESS.label, width='large', required=True),
    Column.GROUP.value: st.column_config.TextColumn(Column.GROUP.label)
}

students_data = SQL.get_paged_filtered_students(page, per_page=ph.per_page, search_filter=search_filter)
if not SQL.get_records_count(students_data):
    err_1,err_2,err3 = st.columns(3)
    st.write(f"### :grey[Студентів за пошуком '{search_filter.search_column.label}' = '{search_filter.search_value}' не знайдено]", )
else:
    st.dataframe(data=students_data, column_config=column_config, hide_index=True)

    c1, c2, c3, c4, c5, c6, c7, c8 = st.columns(8)

    with c1:
        if st.button('1 <<', disabled=ph.is_first_page):
            st.session_state.__setattr__(Key.PAGE_NUMBER, Default.START_PAGE_NUMBER)
            st.rerun()

    with c2:
        if st.button(f'{page - 1 if page > 2 else 1}<', disabled=ph.is_first_page):
            st.session_state.__setattr__(Key.PAGE_NUMBER, page - 1)
            st.rerun()

    with c3:
        st.button(label=str(page), disabled=True)

    with c4:
        if st.button(label=f"{page + 1} > ", disabled=ph.is_last_page(found_students)):
            st.session_state.__setattr__(Key.PAGE_NUMBER, page + 1)
            st.rerun()

    with c5:
        last_page = ph.last_page(found_students)
        if st.button(label=f'{last_page} >>', disabled=ph.is_last_page(found_students)):
            st.session_state.__setattr__(last_page)
            st.rerun()
