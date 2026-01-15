from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class family_Family:

    pass
class family_Person:

    def __init__(self, firstname: str, lastname: str, birthdate: date, family_Person: "family_Family" = None):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.family_Person = family_Person
        
    @property
    def birthdate(self) -> date:
        return self.__birthdate

    @birthdate.setter
    def birthdate(self, birthdate: date):
        self.__birthdate = birthdate

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def family_Person(self):
        return self.__family_Person

    @family_Person.setter
    def family_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Person__family_Person", None)
        self.__family_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Family"):
                opp_val = getattr(old_value, "family_Family", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Family"):
                opp_val = getattr(value, "family_Family", None)
                if opp_val is None:
                    setattr(value, "family_Family", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Parent:

    pass
class family_Father(Parent):

    pass
class family_Mother(Parent):

    pass
class Person:

    pass
class family_Child(Person):

    pass
class family_Parent(Person):

    pass