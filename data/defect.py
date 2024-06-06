import pandas
import streamlit as st

DEFECT_COLUMN_CONFIG = {
    "n": st.column_config.NumberColumn("N"),
    "step": st.column_config.TextColumn("Step to reproduce"),
    "data": st.column_config.TextColumn("Test Data"),
}


class DefectStep:
    def __init__(self, n: int, step: str, test_data: str):
        self.n = n
        self.step = step
        self.test_data = test_data


class Defect:
    def __init__(self, steps: list[DefectStep]):
        self.steps = {}
        self.latest_step: int = 0
        for step in steps:
            self.latest_step += 1
            self.steps[self.latest_step] = step

    def to_data_frame(self) -> pandas.DataFrame:
        result = {}
        result["n"] = [step.n for step in self.steps.values()]
        result["step"] = [step.step for step in self.steps.values()]
        result["data"] = [step.test_data for step in self.steps.values()]
        return pandas.DataFrame(result)


DEFECT_1 = Defect([
    DefectStep(1, "Зайти на сторінку https://softserve-variant6.streamlit.app/", ""),
    DefectStep(2, "Перейти на сторінку СТУДЕНТИ", ""),
    DefectStep(3, "У полі 'Пошук по' вибрати категорію 'По-батькові'", ""),
    DefectStep(4, "у полі “Значення для пошуку” ввести відповідні дані ", "Петрівна"),
])

DEFECT_2 = Defect([
    DefectStep(1, "Зайти на сторінку https://softserve-variant6.streamlit.app/", ""),
    DefectStep(2, "Перейти на сторінку СТУДЕНТИ", ""),
    DefectStep(3, "перевірити, що у колонках з 'Прізвище' та 'Ім'я' знаходиться відповідно прізвище та ім'я студентів ", ""),
])

DEFECT_3 = Defect([
    DefectStep(1, "Зайти на сторінку https://softserve-variant6.streamlit.app/", ""),
    DefectStep(2, "Перейти на сторінку СТУДЕНТИ", ""),
    DefectStep(3, "Перевірити  напис 'Кількість показаних записів'", ""),
])
