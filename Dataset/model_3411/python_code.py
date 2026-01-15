from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Gender(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


############################################
# Definition of Classes
############################################

class people_Universe:

    pass
class people_Person:

    def __init__(self, gender: str, name: str, Person: "people_Person" = None, parents: set["people_Person"] = None, Person4: "people_Person" = None, children: set["people_Person"] = None, people_Person: "people_Universe" = None):
        self.gender = gender
        self.name = name
        self.Person = Person
        self.parents = parents if parents is not None else set()
        self.Person4 = Person4
        self.children = children if children is not None else set()
        self.people_Person = people_Person
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def Person4(self):
        return self.__Person4

    @Person4.setter
    def Person4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_people_Person__Person4", None)
        self.__Person4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                if opp_val is None:
                    setattr(value, "children", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_people_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parents"):
                opp_val = getattr(old_value, "parents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parents"):
                opp_val = getattr(value, "parents", None)
                if opp_val is None:
                    setattr(value, "parents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def people_Person(self):
        return self.__people_Person

    @people_Person.setter
    def people_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_people_Person__people_Person", None)
        self.__people_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "people_Universe"):
                opp_val = getattr(old_value, "people_Universe", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "people_Universe"):
                opp_val = getattr(value, "people_Universe", None)
                if opp_val is None:
                    setattr(value, "people_Universe", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parents(self):
        return self.__parents

    @parents.setter
    def parents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_people_Person__parents", None)
        self.__parents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    if opp_val == self:
                        setattr(item, "Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    setattr(item, "Person", self)
                    

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_people_Person__children", None)
        self.__children = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person4"):
                    opp_val = getattr(item, "Person4", None)
                    
                    if opp_val == self:
                        setattr(item, "Person4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person4"):
                    opp_val = getattr(item, "Person4", None)
                    
                    setattr(item, "Person4", self)
                    
