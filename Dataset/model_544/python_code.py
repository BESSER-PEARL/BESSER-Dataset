from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Person:

    pass
class ExtendedFamilies_Female(Person):

    pass
class ExtendedFamilies_Male(Person):

    pass
class ExtendedFamilies_Person(ABC):

    def __init__(self, firstName: str, Person: "ExtendedFamilies_Family" = None, members: "ExtendedFamilies_Family" = None, Person4: "ExtendedFamilies_Person" = None, parents: set["ExtendedFamilies_Person"] = None, Person7: "ExtendedFamilies_Person" = None, children: set["ExtendedFamilies_Person"] = None):
        self.firstName = firstName
        self.Person = Person
        self.members = members
        self.Person4 = Person4
        self.parents = parents if parents is not None else set()
        self.Person7 = Person7
        self.children = children if children is not None else set()
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def parents(self):
        return self.__parents

    @parents.setter
    def parents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ExtendedFamilies_Person__parents", None)
        self.__parents = value if value is not None else set()
        
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
                    

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ExtendedFamilies_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family"):
                opp_val = getattr(old_value, "family", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family"):
                opp_val = getattr(value, "family", None)
                if opp_val is None:
                    setattr(value, "family", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Person4(self):
        return self.__Person4

    @Person4.setter
    def Person4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ExtendedFamilies_Person__Person4", None)
        self.__Person4 = value
        
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
    def Person7(self):
        return self.__Person7

    @Person7.setter
    def Person7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ExtendedFamilies_Person__Person7", None)
        self.__Person7 = value
        
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
    def members(self):
        return self.__members

    @members.setter
    def members(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ExtendedFamilies_Person__members", None)
        self.__members = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family"):
                opp_val = getattr(old_value, "Family", None)
                if opp_val == self:
                    setattr(old_value, "Family", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family"):
                opp_val = getattr(value, "Family", None)
                setattr(value, "Family", self)

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ExtendedFamilies_Person__children", None)
        self.__children = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person7"):
                    opp_val = getattr(item, "Person7", None)
                    
                    if opp_val == self:
                        setattr(item, "Person7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person7"):
                    opp_val = getattr(item, "Person7", None)
                    
                    setattr(item, "Person7", self)
                    

class ExtendedFamilies_Family:

    def __init__(self, noOfChildren: int, lastName: str, isSingleParent: bool, family: set["ExtendedFamilies_Person"] = None, Family: "ExtendedFamilies_Person" = None):
        self.noOfChildren = noOfChildren
        self.lastName = lastName
        self.isSingleParent = isSingleParent
        self.family = family if family is not None else set()
        self.Family = Family
        
    @property
    def noOfChildren(self) -> int:
        return self.__noOfChildren

    @noOfChildren.setter
    def noOfChildren(self, noOfChildren: int):
        self.__noOfChildren = noOfChildren

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def isSingleParent(self) -> bool:
        return self.__isSingleParent

    @isSingleParent.setter
    def isSingleParent(self, isSingleParent: bool):
        self.__isSingleParent = isSingleParent

    @property
    def Family(self):
        return self.__Family

    @Family.setter
    def Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ExtendedFamilies_Family__Family", None)
        self.__Family = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "members"):
                opp_val = getattr(old_value, "members", None)
                if opp_val == self:
                    setattr(old_value, "members", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "members"):
                opp_val = getattr(value, "members", None)
                setattr(value, "members", self)

    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ExtendedFamilies_Family__family", None)
        self.__family = value if value is not None else set()
        
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
                    
