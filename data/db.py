import math
import typing

from model import SearchColumns, SearchBy

import pandas
import pandas as pd

from model.const import Default

from .students import Group, Student, Address, State, City

group_41 = Group("КН-4-1")
group_21 = Group("КН-2-1")


class DatabaseStudents:
    BASE_GROUPS = [group_21, group_41]
    BASE_STUDENTS: list[Student] = [
        Student(1, "Василь", "Петренко", "Петрович",
                address=Address("13948", State.LVIV, City.LVIV, "просп. Космонавта Попова", "17"),
                group=group_41),
        Student(2, "Степан", "Майстренко", "Сергійович",
                address=Address("96426", State.ODESA, City.ODESA, "просп. Космонавта Попова", "17"),
                group=group_41),
        Student(3, "Тетяна", "Драгунова", "Петрівна",
                address=Address("03162", State.KYIV, City.KYIV, "б-р. Жуля Верна", "07/А"),
                group=group_21),
        Student(4, "Артур", "Коваленко", "Вікторович",
                address=Address("99349", State.POLTAVA, City.POLTAVA, "пров. Волкова", "08"),
                group=group_41),
        Student(5, "Віктор", "Ларін", "Сергійович",
                address=Address("40241", State.ZAPORIZHZYA, City.ZAPORIZHZYA, "просп. Тараса Шевченка", "09"),
                group=group_41),
        Student(6, "Назар", "Лісогор", "Степанович",
                address=Address("13878", State.ZAPORIZHZYA, City.ZAPORIZHZYA, "пров. Волкова", "66"),
                group=group_41),
        Student(7, "Ксенія", "Мякушко", "Павлівна",
                address=Address("78099", State.SUMI, City.SUMI, "просп. Пацаэва", "88"),
                group=group_41),
        Student(8, "Наталія", "Олійник", "Адріївна",
                address=Address("46975", State.KYROVOGRAD, City.KYROVOGRAD, "пров. Генерала Жадова", "14"),
                group=group_41),
        Student(9, "Максим", "Приходько", "Віталійович",
                address=Address("60000", State.POLTAVA, City.POLTAVA, "пл. Лесі Українки", "64"),
                group=group_41),
        Student(10, "Світлана", "Васильєва", "Петрівна",
                address=Address("96426", State.ODESA, City.ODESA, "пров. Михайла Грушевського", "69"),
                group=group_41),
        Student(11, "Деніс", "Коровін", "Віталійович",
                address=Address("46975", State.KYROVOGRAD, City.KYROVOGRAD, "пров. Генерала Жадова", "14"),
                group=group_41),
        Student(12, "Захар", "Муцько", "Іванович",
                address=Address("55724", State.KYIV, City.KYIV, "б-р. Кольцова", "18"),
                group=group_21),
        Student(13, "Люцифер", "Петренко", "Павлович",
                address=Address("21666", State.KYIV, City.KYIV, "просп. ", "13"),
                group=group_21),
        Student(14, "Мурат", "Кожедуб", "Умерович",
                address=Address("66731", State.LVIV, City.LVIV, "пров. Виноградний", "99"),
                group=group_21),
        Student(15, "Вікторія", "Місюра", "Денісівна",
                address=Address("32987", State.SUMI, City.SUMI, "пров. Січових стрільців", "64"),
                group=group_21),
        Student(16, "Анна-Сніжана-Марія", "Крутько", "Всеволодівна",
                address=Address("99851", State.ODESA, City.ODESA, "просп. Миру", "09"),
                group=group_21),
        Student(17, "Тамара", "Рожкова", "Ігоровна",
                address=Address("22671", State.ZAPORIZHZYA, City.ZAPORIZHZYA, "пров. Політехнічний", "39"),
                group=group_21),
    ]

    students: list[Student] = list(BASE_STUDENTS)
    groups: list[Group] = list(BASE_GROUPS)

    def group_names(self) -> list[str]:
        return [g.name for g in self.groups]

    def get_count_of_pages(self,
                           filtered_students: list[Student] | None = None,
                           entity_per_page: int = Default.PER_PAGE_COUNT) -> int:
        stds = filtered_students if filtered_students is not None else self.students
        return math.ceil(len(stds) / entity_per_page)

    def get_count_of_records(
            self,
            filtered_students: list[Student] | None = None,
            entity_per_page: int = Default.PER_PAGE_COUNT
    ) -> int:
        if filtered_students is None:
            return len(self.students) - entity_per_page
        return len(filtered_students)

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def get_filtered_students(self, search_filter: SearchBy | None = None) -> list[Student]:
        filtered_students = list(self.students)
        if search_filter is not None:
            filter_value = search_filter.search_value
            if search_filter.search_column == SearchColumns.ID:
                filtered_students = [s for s in self.students if filter_value in str(s.id)]
            if search_filter.search_column == SearchColumns.FIRST_NAME:
                filtered_students = [s for s in self.students if filter_value in s.first_name]
            if search_filter.search_column == SearchColumns.LAST_NAME:
                filtered_students = [s for s in self.students if filter_value in s.last_name]
            if search_filter.search_column == SearchColumns.SUR_NAME:
                # TODO: BUG HERE
                filtered_students = [s for s in self.students if filter_value in s.last_name]
            if search_filter.search_column == SearchColumns.ADDRESS:
                filtered_students = [s for s in self.students if filter_value in s.address.__repr__()]
            if search_filter.search_column == SearchColumns.GROUP:
                filtered_students = [s for s in self.students if filter_value in s.group.__repr__()]
        return filtered_students

    def get_page(
            self,
            page_number: int,
            entity_per_page: int = Default.PER_PAGE_COUNT,
            filtered_students: list[Student] | None = None,
    ) -> list[Student]:
        filtered_students = filtered_students if filtered_students is not None else self.students
        if len(filtered_students) < entity_per_page:
            return filtered_students
        start_index = (page_number - 1) * entity_per_page
        end_index = start_index + entity_per_page
        stds = filtered_students[start_index:end_index]
        return stds

    def students_to_dataframe(
            self,
            page_number=Default.START_PAGE_NUMBER,
            per_page=Default.PER_PAGE_COUNT,
            filtered_students: list[Student] = None,
    ) -> dict[str, typing.Any]:
        filtered_students = filtered_students if filtered_students is not None else self.students
        paged_students = self.get_page(page_number, per_page, filtered_students)
        return {
            "id": [s.id for s in paged_students],
            "firstname": [s.first_name for s in paged_students],
            "surname": [s.sur_name for s in paged_students],
            "address": [s.address.__repr__() for s in paged_students],
            "group": [s.group.name for s in paged_students]
        }
