import pandas
import streamlit as st

TEST_COLUMN_CONFIG = {
    "n": st.column_config.NumberColumn("N"),
    "step": st.column_config.TextColumn("Test Step"),
    "data": st.column_config.TextColumn("Test Data"),
    "expected": st.column_config.TextColumn("Expected result"),
}


class TestStep:
    def __init__(self, n: int, step: str, test_data: str, expected_result: str):
        self.n = n
        self.step = step
        self.test_data = test_data
        self.expected_result = expected_result


class TestCase:
    def __init__(self, test_steps: list[TestStep]):
        self.test_steps = {}
        self.latest_step: int = 0
        for step in test_steps:
            self.latest_step += 1
            self.test_steps[self.latest_step] = step

    def add_step(self, test_step: TestStep):
        self.latest_step += 1
        self.test_steps[self.latest_step] = test_step

    def to_data_frame(self) -> pandas.DataFrame:
        result = {}
        result["n"] = [step.n for step in self.test_steps.values()]
        result["step"] = [step.step for step in self.test_steps.values()]
        result["data"] = [step.test_data for step in self.test_steps.values()]
        result["expected"] = [step.expected_result for step in self.test_steps.values()]
        return pandas.DataFrame(result)


TEST_CASE_1: TestCase = TestCase([
    TestStep(1, 'Перейти на сторінку СТУДЕНТИ', "", ""),
    TestStep(2, 'Дочекатися поки система оновить дані', "", ""),
    TestStep(3, 'перевірити чи відображається таблиця зі списком  студентів',
             "Перелік полів, що мають бути у таблиці:\nНомер справи,\nПрізвище, Ім'я, По-батькові, Адреса, Група",
             "Відображається таблиця зі списком студентів."),

])

TEST_CASE_2: TestCase = TestCase([
    TestStep(1, "Клікнути по заголовку таблиці 'Номер справи'", "", "Користувачі відсортовані по 'Номер справи' за зростанням"),
    TestStep(2, "Клікнути по заголовку таблиці 'Номер справи'", "", "Користувачі відсортовані по 'Номер справи' за спаданням"),
    TestStep(3, "Клікнути по заголовку таблиці 'Прівзище'", "", "Користувачі відсортовані по 'Прівзище' за зростанням"),
    TestStep(4, "Клікнути по заголовку таблиці 'Прівзище'", "", "Користувачі відсортовані по 'Прівзище' за спаданням"),
    TestStep(5, "Клікнути по заголовку таблиці 'Ім'я'", "", "Користувачі відсортовані по 'Ім'я' за зростанням"),
    TestStep(6, "Клікнути по заголовку таблиці 'Ім'я'", "", "Користувачі відсортовані по 'Ім'я' за спаданням"),
    TestStep(7, "Клікнути по заголовку таблиці 'Адреса'", "", "Користувачі відсортовані по 'Адреса' за зростанням"),
    TestStep(8, "Клікнути по заголовку таблиці 'Адреса'", "", "Користувачі відсортовані по 'Адреса' за спаданням"),
    TestStep(9, "Клікнути по заголовку таблиці 'Група'", "", "Користувачі відсортовані по 'Група' за зростанням"),
    TestStep(10, "Клікнути по заголовку таблиці 'Група'", "", "Користувачі відсортовані по 'Група' за спаданням"),
])

TEST_CASE_3: TestCase = TestCase([
    TestStep(1, 'Перейти на сторінку СТУДЕНТИ', "", ""),
    TestStep(2, "Перевірити положення елементу Breadcrumbs", "Головна / Студенти", "Елемент  Breadcrumbs  знаходиться у верхньому лівому куті сторінки"),
    TestStep(3, "Перевірити положення title 'Студенти'", "", "Елемент “Студенти” знаходиться у верхньому лівому куті сторінки під елементом Breadcrumbs"),
    TestStep(4, "Перевірити наявність і положення кнопки 'Новий запис” ", "", "Кнопка  “Новий запис” знаходиться нижче від title 'Студенти' вирівняний по лівому краю, кнопка має бути активна"),
    TestStep(5, "Перевірити  наявність і положення напису 'Кількість показаних записів”", "", "Напис “Кількість показаних  записів” знаходиться під кнопкою 'Новий запис' та вище таблиці із списком студентів, а також вирівняний по лівому краю сторінки"),
    TestStep(6, "Перевірити наявність і положення таблиці зі списком студентів", "", "Таблиця зі списком студентів має бути розташована нижче напису 'Кількості показаних записів' і має займати 100% доступної ширини"),
    TestStep(7, "Перевірити положення Pagination", "", "Pagination знаходиться нижче від таблиці вирівняна по лівому краю"),
])
