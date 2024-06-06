class SearchColumn:
    def __init__(self, column_label: str, column_value: str):
        self.label = column_label
        self.value = column_value

    def __repr__(self) -> str:
        return f"{self.label} - {self.value}"

    def __eq__(self, other) -> bool:
        return self.label == other.label and self.value == other.value


class SearchColumns:
    ID = SearchColumn("Номер справи", "id")
    FIRST_NAME = SearchColumn("Імʼя", "firstname")
    LAST_NAME = SearchColumn("Прізвище", "lastname")
    SUR_NAME = SearchColumn("По-батькові", "surname")
    ADDRESS = SearchColumn("Адреса", "address")
    GROUP = SearchColumn("Група", "group")

    ALL_OPTIONS = [ID, FIRST_NAME, LAST_NAME, SUR_NAME, ADDRESS, GROUP]



class SearchBy:
    def __init__(self, search_column: SearchColumn, search_value):
        self.search_column = search_column
        self.search_value = search_value

    def __repr__(self) -> str:
        return f"Col: {self.search_column}, Val: {self.search_value}"
