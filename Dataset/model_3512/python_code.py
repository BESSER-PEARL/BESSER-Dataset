from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class EnumA(Enum):
    CASE1 = "CASE1"
    CASE2 = "CASE2"


############################################
# Definition of Classes
############################################

class Parent:

    pass
class testoperationbody_ChildA(Parent):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class testoperationbody_ChildB(Parent):

    pass
class testoperationbody_Parent(ABC):

    pass
class testoperationbody_ConceptA:

    pass
class testoperationbody_Main:

    def __init__(self, listint: int, singlebool: bool, testoperationbody_Main: set["testoperationbody_ConceptA"] = None, testoperationbody_Main2: "testoperationbody_ConceptA" = None, testoperationbody_Main5: set["testoperationbody_Parent"] = None):
        self.listint = listint
        self.singlebool = singlebool
        self.testoperationbody_Main = testoperationbody_Main if testoperationbody_Main is not None else set()
        self.testoperationbody_Main2 = testoperationbody_Main2
        self.testoperationbody_Main5 = testoperationbody_Main5 if testoperationbody_Main5 is not None else set()
        
    @property
    def listint(self) -> int:
        return self.__listint

    @listint.setter
    def listint(self, listint: int):
        self.__listint = listint

    @property
    def singlebool(self) -> bool:
        return self.__singlebool

    @singlebool.setter
    def singlebool(self, singlebool: bool):
        self.__singlebool = singlebool

    @property
    def testoperationbody_Main5(self):
        return self.__testoperationbody_Main5

    @testoperationbody_Main5.setter
    def testoperationbody_Main5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testoperationbody_Main__testoperationbody_Main5", None)
        self.__testoperationbody_Main5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testoperationbody_Parent"):
                    opp_val = getattr(item, "testoperationbody_Parent", None)
                    
                    if opp_val == self:
                        setattr(item, "testoperationbody_Parent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testoperationbody_Parent"):
                    opp_val = getattr(item, "testoperationbody_Parent", None)
                    
                    setattr(item, "testoperationbody_Parent", self)
                    

    @property
    def testoperationbody_Main(self):
        return self.__testoperationbody_Main

    @testoperationbody_Main.setter
    def testoperationbody_Main(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testoperationbody_Main__testoperationbody_Main", None)
        self.__testoperationbody_Main = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testoperationbody_ConceptA"):
                    opp_val = getattr(item, "testoperationbody_ConceptA", None)
                    
                    if opp_val == self:
                        setattr(item, "testoperationbody_ConceptA", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testoperationbody_ConceptA"):
                    opp_val = getattr(item, "testoperationbody_ConceptA", None)
                    
                    setattr(item, "testoperationbody_ConceptA", self)
                    

    @property
    def testoperationbody_Main2(self):
        return self.__testoperationbody_Main2

    @testoperationbody_Main2.setter
    def testoperationbody_Main2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testoperationbody_Main__testoperationbody_Main2", None)
        self.__testoperationbody_Main2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testoperationbody_ConceptA3"):
                opp_val = getattr(old_value, "testoperationbody_ConceptA3", None)
                if opp_val == self:
                    setattr(old_value, "testoperationbody_ConceptA3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testoperationbody_ConceptA3"):
                opp_val = getattr(value, "testoperationbody_ConceptA3", None)
                setattr(value, "testoperationbody_ConceptA3", self)
