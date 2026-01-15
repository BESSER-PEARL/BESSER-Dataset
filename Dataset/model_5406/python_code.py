from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ProbabalisticEvent:

    pass
class faultTree_UndevelopedEvent(ProbabalisticEvent):

    pass
class faultTree_ExternalEvent(ProbabalisticEvent):

    pass
class faultTree_BasicEvent(ProbabalisticEvent):

    pass
class Event:

    pass
class faultTree_ProbabalisticEvent(Event):

    def __init__(self, probability: float):
        self.probability = probability
        
    @property
    def probability(self) -> float:
        return self.__probability

    @probability.setter
    def probability(self, probability: float):
        self.__probability = probability

class Gate:

    pass
class faultTree_OR_Gate(Gate):

    pass
class faultTree_AND_Gate(Gate):

    pass
class faultTree_IntermediateEvent(Event):

    pass
class FTElement:

    pass
class faultTree_Event(FTElement):

    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class faultTree_Gate(FTElement):

    pass
class faultTree_FaultTree(FTElement):

    pass
class faultTree_Connector(FTElement):

    pass
class faultTree_FTElement(ABC):

    pass