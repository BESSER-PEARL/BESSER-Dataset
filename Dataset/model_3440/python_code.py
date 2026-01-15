from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Student:

    pass
class SourceModel_BachelorStudent(Student):

    pass
class SourceModel_MasterStudent(Student):

    pass
class Person:

    pass
class SourceModel_Professor(Person):

    pass
class SourceModel_Student(Person):

    pass
class SourceModel_Person:

    def __init__(self, age: str, SourceModel_Person: "SourceModel_Container" = None, SourceModel_Person3: "SourceModel_Person" = None, SourceModel_Person1: "SourceModel_Person" = None):
        self.age = age
        self.SourceModel_Person = SourceModel_Person
        self.SourceModel_Person3 = SourceModel_Person3
        self.SourceModel_Person1 = SourceModel_Person1
        
    @property
    def age(self) -> str:
        return self.__age

    @age.setter
    def age(self, age: str):
        self.__age = age

    @property
    def SourceModel_Person1(self):
        return self.__SourceModel_Person1

    @SourceModel_Person1.setter
    def SourceModel_Person1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SourceModel_Person__SourceModel_Person1", None)
        self.__SourceModel_Person1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SourceModel_Person3"):
                opp_val = getattr(old_value, "SourceModel_Person3", None)
                if opp_val == self:
                    setattr(old_value, "SourceModel_Person3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SourceModel_Person3"):
                opp_val = getattr(value, "SourceModel_Person3", None)
                setattr(value, "SourceModel_Person3", self)

    @property
    def SourceModel_Person3(self):
        return self.__SourceModel_Person3

    @SourceModel_Person3.setter
    def SourceModel_Person3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SourceModel_Person__SourceModel_Person3", None)
        self.__SourceModel_Person3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SourceModel_Person1"):
                opp_val = getattr(old_value, "SourceModel_Person1", None)
                if opp_val == self:
                    setattr(old_value, "SourceModel_Person1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SourceModel_Person1"):
                opp_val = getattr(value, "SourceModel_Person1", None)
                setattr(value, "SourceModel_Person1", self)

    @property
    def SourceModel_Person(self):
        return self.__SourceModel_Person

    @SourceModel_Person.setter
    def SourceModel_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SourceModel_Person__SourceModel_Person", None)
        self.__SourceModel_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SourceModel_Container"):
                opp_val = getattr(old_value, "SourceModel_Container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SourceModel_Container"):
                opp_val = getattr(value, "SourceModel_Container", None)
                if opp_val is None:
                    setattr(value, "SourceModel_Container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SourceModel_Container:

    pass