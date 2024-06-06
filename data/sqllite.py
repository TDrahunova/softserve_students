import math

import pandas
import streamlit as st

from model import Default, SearchColumns
from model import SearchBy as SearchFilter

conn = st.connection('student_db', type='sql')


class SQL:

    @staticmethod
    def group_names() -> list[str]:
        return conn.query('select group_name from std_group').get('group_name').values

    @staticmethod
    def get_all_students(
    ) -> pandas.DataFrame:
        students_data = conn.query(
            f'select s.id,s.first_name,s.last_name,s.sur_name,s.address,std_group.group_name from students as s join std_group on std_group.id=s.group_id')
        return students_data

    @staticmethod
    def get_page_students(
        page_number: int = Default.START_PAGE_NUMBER,
        per_page: int = Default.PER_PAGE_COUNT
    ) -> pandas.DataFrame:
        students_data = conn.query(
            f'select s.id,s.first_name,s.last_name,s.sur_name,s.address,std_group.group_name from students as s join std_group on std_group.id=s.group_id limit {per_page} OFFSET {page_number - 1 * per_page}')
        return students_data

    @staticmethod
    def get_filtered_students(
        search_filter: SearchFilter | None = None,
    ) -> pandas.DataFrame:

        if search_filter is None:
            return SQL.get_all_students()
        if search_filter.search_column == SearchColumns.ID:
            filter = "s.id"
        if search_filter.search_column == SearchColumns.FIRST_NAME:
            filter = "s.first_name"
        if search_filter.search_column == SearchColumns.LAST_NAME:
            filter = "s.last_name"
        if search_filter.search_column == SearchColumns.SUR_NAME:
            # TODO: BUG HERE
            filter = "s.last_name"
        if search_filter.search_column == SearchColumns.ADDRESS:
            filter = "s.address"
        if search_filter.search_column == SearchColumns.GROUP:
            filter = "std_group.group_name"

        select = 'select s.id,s.first_name,s.last_name,s.sur_name,s.address,std_group.group_name from students as s join std_group on std_group.id=s.group_id'
        where = f"where {filter} like '%{search_filter.search_value}%'"
        st.write(f"{select} {where}")
        return conn.query(f"{select} {where}")

    @staticmethod
    def get_paged_filtered_students(
        page_number: int = Default.START_PAGE_NUMBER,
        per_page: int = Default.PER_PAGE_COUNT,
        search_filter: SearchFilter | None = None,
    ) -> pandas.DataFrame:

        if search_filter is None:
            return SQL.get_all_students()
        if search_filter.search_column == SearchColumns.ID:
            filter = "s.id"
        if search_filter.search_column == SearchColumns.FIRST_NAME:
            filter = "s.first_name"
        if search_filter.search_column == SearchColumns.LAST_NAME:
            filter = "s.last_name"
        if search_filter.search_column == SearchColumns.SUR_NAME:
            # TODO: BUG HERE
            filter = "s.last_name"
        if search_filter.search_column == SearchColumns.ADDRESS:
            filter = "s.address"
        if search_filter.search_column == SearchColumns.GROUP:
            filter = "std_group.group_name"
        assert filter, f"Can not create filter for search: {search_filter}"

        select = 'select s.id,s.first_name,s.last_name,s.sur_name,s.address,std_group.group_name from students as s'
        join = 'join std_group on std_group.id=s.group_id'
        where = f"where {filter} like '%{search_filter.search_value}%'"
        offset = f"limit {per_page} OFFSET {page_number - 1 * per_page}"
        return conn.query(f"{select} {join} {where} {offset}")

    @staticmethod
    def get_students_count() -> pandas.DataFrame:
        count = conn.query('select count(id) as c from students').get('c').values[0]
        return count

    @staticmethod
    def get_count_of_pages(filtered_students: pandas.DataFrame | None = None,
                           entity_per_page: int = Default.PER_PAGE_COUNT
                           ) -> int:
        count_of_students = SQL.get_students_count() if filtered_students is None else filtered_students.count()
        return math.ceil(count_of_students / entity_per_page)

    @staticmethod
    def run_sql(sql: str) -> pandas.DataFrame:
        return conn.query(sql)
