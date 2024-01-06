from abc import ABC, abstractmethod
from typing import AnyStr, List, Union
import requests

# We want to gather data from 2 APIs, both returning in different formats. 
# So we will create an adapter to make data (responce from api) acceptable to the client.
# we are either getting cat facts or dog images

class API(ABC):
    @abstractmethod
    def setup_request(self): ...

    @abstractmethod
    def get_data(self): ...


class DogImageAPI(API):

    req: Union[requests.models.Response, None]

    def __init__(self) -> None:
        self.req = None
        self.url = "https://dog.ceo/api/breeds/image/random"

    def setup_request(self):
        self.req = requests.get(self.url)

    def get_data(self):
        return self.req.json()


class CatFactAPI(API):

    req: Union[requests.models.Response, None]

    def __init__(self) -> None:
        self.req = None
        self.url = "https://catfact.ninja/fact"

    def setup_request(self):
        self.req = requests.get(self.url)

    def get_data(self):
        return self.req.json()


class GetDataAdapter(ABC):
    @abstractmethod
    def get_data(self): ...


class GetData(GetDataAdapter):

    def __init__(self, data_type: str) -> None:
        self.data_type = data_type
        self.api_obj: API
        self.data = None
        self.formated_data = {"type": "", "data": ""}

    def get_data(self):
        if self.data_type.lower() == "dog":
            print("dog")
            self.api_obj = DogImageAPI()
            self.api_obj.setup_request()
            self.data = self.api_obj.get_data()
            print(self.data)
            self.formated_data["type"] = "Dog Image"
            self.formated_data["data"] = self.data["message"] 
        elif self.data_type.lower() == "cat":
            print("cat")
            self.api_obj = CatFactAPI()
            self.api_obj.setup_request()
            self.data = self.api_obj.get_data()
            print(self.data)
            self.formated_data["type"] = "Cat Fact"
            self.formated_data["data"] = self.data["fact"]
        else:
            return {"error": "Api for this ket does not exist"}
            
        return self.formated_data
    

if __name__ == "__main__":
    cat_data_obj = GetData(data_type="cat")
    dog_data_obj = GetData(data_type="dog")
    wrong_data_obj = GetData(data_type="cog")
    
    cat_data = cat_data_obj.get_data()
    dog_data = dog_data_obj.get_data()
    wrong_data = wrong_data_obj.get_data()

    print(cat_data)
    print(dog_data)
    print(wrong_data)





