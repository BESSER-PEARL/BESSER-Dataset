from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Person:

    pass
class PersonsOne_Student(Person):

    def __init__(self, grade: str):
        self.grade = grade
        
    @property
    def grade(self) -> str:
        return self.__grade

    @grade.setter
    def grade(self, grade: str):
        self.__grade = grade

class PersonsOne_Person:

    def __init__(self, name: str, age: int, PersonsOne_Person: "PersonsOne_Group" = None):
        self.name = name
        self.age = age
        self.PersonsOne_Person = PersonsOne_Person
        
    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PersonsOne_Person(self):
        return self.__PersonsOne_Person

    @PersonsOne_Person.setter
    def PersonsOne_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonsOne_Person__PersonsOne_Person", None)
        self.__PersonsOne_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PersonsOne_Group"):
                opp_val = getattr(old_value, "PersonsOne_Group", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PersonsOne_Group"):
                opp_val = getattr(value, "PersonsOne_Group", None)
                if opp_val is None:
                    setattr(value, "PersonsOne_Group", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PersonsOne_Group:

    def __init__(self, name: str, PersonsOne_Group: set["PersonsOne_Person"] = None):
        self.name = name
        self.PersonsOne_Group = PersonsOne_Group if PersonsOne_Group is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PersonsOne_Group(self):
        return self.__PersonsOne_Group

    @PersonsOne_Group.setter
    def PersonsOne_Group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonsOne_Group__PersonsOne_Group", None)
        self.__PersonsOne_Group = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PersonsOne_Person"):
                    opp_val = getattr(item, "PersonsOne_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "PersonsOne_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PersonsOne_Person"):
                    opp_val = getattr(item, "PersonsOne_Person", None)
                    
                    setattr(item, "PersonsOne_Person", self)
                    
