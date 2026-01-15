from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Person:

    pass
class familyTree_Female(Person):

    pass
class familyTree_Male(Person):

    pass
class familyTree_Person(ABC):

    def __init__(self, name: str, lastName: str, Person: "familyTree_FamilyTree" = None, children: "familyTree_Male" = None, children3: "familyTree_Female" = None, Person8: "familyTree_Male" = None, leaves: "familyTree_FamilyTree" = None, Person12: "familyTree_Female" = None):
        self.name = name
        self.lastName = lastName
        self.Person = Person
        self.children = children
        self.children3 = children3
        self.Person8 = Person8
        self.leaves = leaves
        self.Person12 = Person12
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def leaves(self):
        return self.__leaves

    @leaves.setter
    def leaves(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyTree_Person__leaves", None)
        self.__leaves = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FamilyTree"):
                opp_val = getattr(old_value, "FamilyTree", None)
                if opp_val == self:
                    setattr(old_value, "FamilyTree", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FamilyTree"):
                opp_val = getattr(value, "FamilyTree", None)
                setattr(value, "FamilyTree", self)

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyTree_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tree"):
                opp_val = getattr(old_value, "tree", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tree"):
                opp_val = getattr(value, "tree", None)
                if opp_val is None:
                    setattr(value, "tree", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Person12(self):
        return self.__Person12

    @Person12.setter
    def Person12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyTree_Person__Person12", None)
        self.__Person12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mother"):
                opp_val = getattr(old_value, "mother", None)
                if opp_val == self:
                    setattr(old_value, "mother", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mother"):
                opp_val = getattr(value, "mother", None)
                setattr(value, "mother", self)

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyTree_Person__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Male"):
                opp_val = getattr(old_value, "Male", None)
                if opp_val == self:
                    setattr(old_value, "Male", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Male"):
                opp_val = getattr(value, "Male", None)
                setattr(value, "Male", self)

    @property
    def children3(self):
        return self.__children3

    @children3.setter
    def children3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyTree_Person__children3", None)
        self.__children3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Female"):
                opp_val = getattr(old_value, "Female", None)
                if opp_val == self:
                    setattr(old_value, "Female", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Female"):
                opp_val = getattr(value, "Female", None)
                setattr(value, "Female", self)

    @property
    def Person8(self):
        return self.__Person8

    @Person8.setter
    def Person8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyTree_Person__Person8", None)
        self.__Person8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "father"):
                opp_val = getattr(old_value, "father", None)
                if opp_val == self:
                    setattr(old_value, "father", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "father"):
                opp_val = getattr(value, "father", None)
                setattr(value, "father", self)

class familyTree_FamilyTree:

    pass