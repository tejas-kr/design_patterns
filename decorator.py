from abc import ABC, abstractmethod
from typing import List, AnyStr

# We need to design a subscription model for our news website with some addons.

class Subscription(ABC): 
    @abstractmethod
    def get_cost(self): ...

class MonthlySubscription(Subscription):

    def __init__(self) -> None:
        self.cost = 120

    def get_cost(self):
        return self.cost
    
    
class YearlySubscription(Subscription):

    def __init__(self) -> None:
        self.cost = 1000

    def get_cost(self):
        return self.cost
    
    
class QuaterlySubscription(Subscription):

    def __init__(self) -> None:
        self.cost = 340

    def get_cost(self):
        return self.cost
    

class AddOnDecorator(Subscription):
    ...


class BetterSoundQuality(AddOnDecorator):
    def __init__(self, subscription: Subscription) -> None:
        self.cost = 50
        self.subscription = subscription

    def get_cost(self):
        return self.subscription.get_cost() + self.cost
    

class ExtraControlButtons(AddOnDecorator):
    def __init__(self, subscription: Subscription) -> None:
        self.cost = 100
        self.subscription = subscription

    def get_cost(self):
        return self.subscription.get_cost() + self.cost
    


if __name__ == "__main__": 
    # We want a Monthly subs with better sound quality
    bs_m_subs = BetterSoundQuality(MonthlySubscription())
    
    # Extra control button + better sound + monthly
    ecb_bs_m_subs = ExtraControlButtons(BetterSoundQuality(MonthlySubscription()))

    ecb_q_subs = ExtraControlButtons(QuaterlySubscription())

    print(bs_m_subs.get_cost())
    print(ecb_bs_m_subs.get_cost())
    print(ecb_q_subs.get_cost())
    

