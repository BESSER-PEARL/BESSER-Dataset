from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Tristate(Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"
    UNDEFINED = "UNDEFINED"


############################################
# Definition of Classes
############################################

class sample_SampleClassInterface(ABC):

    def __init__(self):
        
        pass
    def doSomething(self, sample_input) :
        # TODO: Implement doSomething method
        pass

class SampleClassInterface:

    pass
class sample_SampleClassA(SampleClassInterface):

    def __init__(self, sampleAttribute: str, sample_SampleClassA: "sample_SampleClassC" = None):
        self.sampleAttribute = sampleAttribute
        self.sample_SampleClassA = sample_SampleClassA
        
        pass
    @property
    def sampleAttribute(self):
        return self.__sampleAttribute

    @sampleAttribute.setter
    def sampleAttribute(self, sampleAttribute: str):
        self.__sampleAttribute = sampleAttribute


    @property
    def sample_SampleClassA(self):
        return self.__sample_SampleClassA

    @sample_SampleClassA.setter
    def sample_SampleClassA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_SampleClassA__sample_SampleClassA", None)
        self.__sample_SampleClassA = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_SampleClassC"):
                opp_val = getattr(old_value, "sample_SampleClassC", None)
                if opp_val == self:
                    setattr(old_value, "sample_SampleClassC", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_SampleClassC"):
                opp_val = getattr(value, "sample_SampleClassC", None)
                setattr(value, "sample_SampleClassC", self)

class sample_SampleClassB:

    pass
class sample_SampleClassC:

    pass