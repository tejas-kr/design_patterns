from abc import ABC, abstractmethod
from typing import AnyStr, List

# In this example, we became Bob the builder. We undertook a contract of building houses of our friends.
# So... bob the builder kar ke dikhayenge ha bhai ha

class House: 
    def __init__(
        self, 
        house_type: str = "appartment",
        windows: int = 2,
        doors: int = 2,
        building_material: str = "wood"
    ) -> None:
        self.house_type = house_type
        self.windows = windows
        self.doors = doors
        self.building_material = building_material

    def create_house(self):
        return (
            f"this is a nice house of {self.house_type} type."
            f"it has {self.doors} doors and {self.windows} windows."
            f"it is made up of {self.building_material} material."
        )
    

class IHouseBuilder(ABC):

    @abstractmethod
    def set_house_type(self, house_type: str):
        ...

    @abstractmethod
    def set_windows(self, windows: int):
        ...

    @abstractmethod
    def set_doors(self, doors: int):
        ...

    @abstractmethod
    def set_building_material(self, building_material: str):
        ...

    @abstractmethod
    def get_house(self):
        ...


class HouseBuilder(IHouseBuilder):

    def __init__(self) -> None:
        self.house = House()

    def set_house_type(self, house_type: str):
        self.house.house_type = house_type
        # return self

    def set_windows(self, windows: int):
        self.house.windows = windows
        # return self

    def set_doors(self, doors: int):
        self.house.doors = doors
        # return self
    
    def set_building_material(self, building_material: str):
        self.house.building_material = building_material
        # return self

    def get_house(self):
        return self.house


class HouseBuildDirector:
    @staticmethod
    def construct():
        # return HouseBuilder()\
        #         .set_building_material("wood")\
        #         .set_windows(2)\
        #         .set_doors(1)\
        #         .set_house_type("own")\
        #         .get_house()
        house_builder = HouseBuilder()
        house_builder.set_building_material("wood")
        house_builder.set_doors(1)
        house_builder.set_windows(2)
        house_builder.set_house_type("appartment")
        return house_builder.get_house()


if __name__ == "__main__":
    house = HouseBuildDirector.construct()
    print(house.create_house())

