from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class incomeLevel(Enum):
    UnderGrad = "UnderGrad"
    PreDoc = "PreDoc"
    PostDoc = "PostDoc"
    Professor = "Professor"
class Grade(Enum):
    None = "None"
    BSC = "BSC"
    MSC = "MSC"
    PHD = "PHD"
    Professor = "Professor"
class EEnum0(Enum):


############################################
# Definition of Classes
############################################

class test_University:

    def __init__(self, name: str, test_University: set["test_Person"] = None):
        self.name = name
        self.test_University = test_University if test_University is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def test_University(self):
        return self.__test_University

    @test_University.setter
    def test_University(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_University__test_University", None)
        self.__test_University = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test_Person6"):
                    opp_val = getattr(item, "test_Person6", None)
                    
                    if opp_val == self:
                        setattr(item, "test_Person6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test_Person6"):
                    opp_val = getattr(item, "test_Person6", None)
                    
                    setattr(item, "test_Person6", self)
                    

class test_Person:

    def __init__(self, lastname: str, firstame: str, Grade: str, test_Person: "test_Person" = None, test_Person0: "test_Person" = None, test_Person4: "test_Person" = None, test_Person2: set["test_Person"] = None, test_Person6: "test_University" = None):
        self.lastname = lastname
        self.firstame = firstame
        self.Grade = Grade
        self.test_Person = test_Person
        self.test_Person0 = test_Person0
        self.test_Person4 = test_Person4
        self.test_Person2 = test_Person2 if test_Person2 is not None else set()
        self.test_Person6 = test_Person6
        
    @property
    def firstame(self) -> str:
        return self.__firstame

    @firstame.setter
    def firstame(self, firstame: str):
        self.__firstame = firstame

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def Grade(self) -> str:
        return self.__Grade

    @Grade.setter
    def Grade(self, Grade: str):
        self.__Grade = Grade

    @property
    def test_Person6(self):
        return self.__test_Person6

    @test_Person6.setter
    def test_Person6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Person__test_Person6", None)
        self.__test_Person6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_University"):
                opp_val = getattr(old_value, "test_University", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_University"):
                opp_val = getattr(value, "test_University", None)
                if opp_val is None:
                    setattr(value, "test_University", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def test_Person(self):
        return self.__test_Person

    @test_Person.setter
    def test_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Person__test_Person", None)
        self.__test_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_Person0"):
                opp_val = getattr(old_value, "test_Person0", None)
                if opp_val == self:
                    setattr(old_value, "test_Person0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_Person0"):
                opp_val = getattr(value, "test_Person0", None)
                setattr(value, "test_Person0", self)

    @property
    def test_Person2(self):
        return self.__test_Person2

    @test_Person2.setter
    def test_Person2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Person__test_Person2", None)
        self.__test_Person2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test_Person4"):
                    opp_val = getattr(item, "test_Person4", None)
                    
                    if opp_val == self:
                        setattr(item, "test_Person4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test_Person4"):
                    opp_val = getattr(item, "test_Person4", None)
                    
                    setattr(item, "test_Person4", self)
                    

    @property
    def test_Person0(self):
        return self.__test_Person0

    @test_Person0.setter
    def test_Person0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Person__test_Person0", None)
        self.__test_Person0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_Person"):
                opp_val = getattr(old_value, "test_Person", None)
                if opp_val == self:
                    setattr(old_value, "test_Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_Person"):
                opp_val = getattr(value, "test_Person", None)
                setattr(value, "test_Person", self)

    @property
    def test_Person4(self):
        return self.__test_Person4

    @test_Person4.setter
    def test_Person4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Person__test_Person4", None)
        self.__test_Person4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_Person2"):
                opp_val = getattr(old_value, "test_Person2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_Person2"):
                opp_val = getattr(value, "test_Person2", None)
                if opp_val is None:
                    setattr(value, "test_Person2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Person:

    pass
class test_Employee(Person):

    def __init__(self, incomeLevel: str):
        self.incomeLevel = incomeLevel
        
    @property
    def incomeLevel(self) -> str:
        return self.__incomeLevel

    @incomeLevel.setter
    def incomeLevel(self, incomeLevel: str):
        self.__incomeLevel = incomeLevel

class test_Student(Person):

    def __init__(self, regNo: str):
        self.regNo = regNo
        
    @property
    def regNo(self) -> str:
        return self.__regNo

    @regNo.setter
    def regNo(self, regNo: str):
        self.__regNo = regNo
