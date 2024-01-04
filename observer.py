from abc import ABC, abstractmethod
from typing import List

# We have a store named Ramesh General Store which is trying to modernize and automate for growth
# We take phone numbers of all the customers that visit our store and keep them in a DB
# so that we can send the notification
# about all the new schemes and marketting about the new products. 
# The customers have the option to add or remove them from the list of people being notified.

# FUN FACT - Pub Sub model works on observer design pattern

class Customer(ABC):

    @abstractmethod
    def get_notifications(self) -> None:
        ...
    
    @abstractmethod
    def stop_notifications(self) -> None:
        ...

    @abstractmethod
    def update(self, notice: str) -> None:
        ...


class RealCustomer(Customer):
    def __init__(self, name: str) -> None:
        self.name = name
        self.notification_flag: bool = False
    
    def get_notifications(self) -> None:
        self.notification_flag = True
    
    def stop_notifications(self) -> None:
        self.notification_flag = False

    def update(self, notice: str) -> None:
        print(notice)


class Store(ABC):
    @abstractmethod
    def subscribe(self, customer: Customer) -> None:
        ...
    @abstractmethod
    def unsubscribe(self, customer: Customer) -> None:
        ...
    @abstractmethod
    def notify(self) -> None:
        ...


class RameshGeneralStore(Store):

    def __init__(self) -> None:
        self.notification_customers: List[Customer] = []

    def subscribe(self, customer: Customer):
        if customer.notification_flag:
            self.notification_customers.append(customer)

    def unsubscribe(self, customer: Customer):
        if not customer.notification_flag:
            self.notification_customers.remove(customer)

    def notify(self):
        for customer in self.notification_customers:
            customer.update(
                notice=f"Hey {customer.name},\n this new product is osssum. consooooooom"
            )

    
if __name__ == "__main__":
    cus1 = RealCustomer(name="Ram Singh")
    cus2 = RealCustomer(name="Ram Charan")
    cus3 = RealCustomer(name="Ram Sharan")

    cus1.get_notifications()
    cus2.get_notifications()
    # cus3.get_notifications()

    store1 = RameshGeneralStore()

    store1.subscribe(customer=cus1)
    store1.subscribe(customer=cus2)
    store1.subscribe(customer=cus3)

    store1.notify()



