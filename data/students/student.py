import enum


class Group:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name


class State(str, enum.Enum):
    KYIV = "Київська"
    POLTAVA = "Полтавська"
    LVIV = "Львівська"
    KYROVOGRAD = "Кіровоградська"
    SUMI = "Сумська"
    ZAPORIZHZYA = "Запорізька"
    ODESA = "Одеська"


class City(str, enum.Enum):
    KYIV = "Київ"
    POLTAVA = "Полтава"
    LVIV = "Львів"
    KYROVOGRAD = "Кіровоград"
    SUMI = "Суми"
    ZAPORIZHZYA = "Запоріжжя"
    ODESA = "Одеса"


class Address:
    def __init__(self,
                 zip: str,
                 state: State,
                 city: City,
                 street: str,
                 building: str,
                 ):
        self.zip = zip
        self.state = state
        self.city = city
        self.street = street
        self.building = building

    def __repr__(self):
        return f"{self.zip}, {self.state.value} область, місто {self.city.value}, {self.street}, {self.building}"


class Student:
    def __init__(
            self,
            id: int,
            first_name: str,
            last_name: str,
            sur_name: str,
            address: Address,
            group: Group,
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.sur_name = sur_name
        self.address = address
        self.group = group

    def __repr__(self):
        return f"id: {self.id}, first_name={self.first_name}, last_name={self.last_name}, sur_name={self.sur_name}, address={self.address.__repr__()}, group_name={self.group.name}"
