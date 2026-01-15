from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RelationshipStatus(Enum):
    Single = "Single"
    Widowed = "Widowed"
    Divorced = "Divorced"
    Liaised = "Liaised"
    Married = "Married"


############################################
# Definition of Classes
############################################

class familytree_Person(ABC):

    def __init__(self, firstName: str, secondName: str, dayOfBirth: date, nameOfBirth: str, relationshipStatus: str, died: bool, dayOfDeath: date, locationOfBirth: str, imagePaths: str, familytree_Person: "familytree_FamilyTree" = None, Person: "familytree_Person" = None, parents: set["familytree_Person"] = None, Person4: "familytree_Person" = None, children: set["familytree_Person"] = None, Person7: "familytree_Person" = None, inRelationTo: "familytree_Person" = None, Person10: "familytree_Person" = None, inRelationWith: "familytree_Person" = None):
        self.firstName = firstName
        self.secondName = secondName
        self.dayOfBirth = dayOfBirth
        self.nameOfBirth = nameOfBirth
        self.relationshipStatus = relationshipStatus
        self.died = died
        self.dayOfDeath = dayOfDeath
        self.locationOfBirth = locationOfBirth
        self.imagePaths = imagePaths
        self.familytree_Person = familytree_Person
        self.Person = Person
        self.parents = parents if parents is not None else set()
        self.Person4 = Person4
        self.children = children if children is not None else set()
        self.Person7 = Person7
        self.inRelationTo = inRelationTo
        self.Person10 = Person10
        self.inRelationWith = inRelationWith
        
    @property
    def nameOfBirth(self) -> str:
        return self.__nameOfBirth

    @nameOfBirth.setter
    def nameOfBirth(self, nameOfBirth: str):
        self.__nameOfBirth = nameOfBirth

    @property
    def relationshipStatus(self) -> str:
        return self.__relationshipStatus

    @relationshipStatus.setter
    def relationshipStatus(self, relationshipStatus: str):
        self.__relationshipStatus = relationshipStatus

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def secondName(self) -> str:
        return self.__secondName

    @secondName.setter
    def secondName(self, secondName: str):
        self.__secondName = secondName

    @property
    def dayOfBirth(self) -> date:
        return self.__dayOfBirth

    @dayOfBirth.setter
    def dayOfBirth(self, dayOfBirth: date):
        self.__dayOfBirth = dayOfBirth

    @property
    def imagePaths(self) -> str:
        return self.__imagePaths

    @imagePaths.setter
    def imagePaths(self, imagePaths: str):
        self.__imagePaths = imagePaths

    @property
    def dayOfDeath(self) -> date:
        return self.__dayOfDeath

    @dayOfDeath.setter
    def dayOfDeath(self, dayOfDeath: date):
        self.__dayOfDeath = dayOfDeath

    @property
    def locationOfBirth(self) -> str:
        return self.__locationOfBirth

    @locationOfBirth.setter
    def locationOfBirth(self, locationOfBirth: str):
        self.__locationOfBirth = locationOfBirth

    @property
    def died(self) -> bool:
        return self.__died

    @died.setter
    def died(self, died: bool):
        self.__died = died

    @property
    def parents(self):
        return self.__parents

    @parents.setter
    def parents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familytree_Person__parents", None)
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
    def Person7(self):
        return self.__Person7

    @Person7.setter
    def Person7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familytree_Person__Person7", None)
        self.__Person7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inRelationTo"):
                opp_val = getattr(old_value, "inRelationTo", None)
                if opp_val == self:
                    setattr(old_value, "inRelationTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inRelationTo"):
                opp_val = getattr(value, "inRelationTo", None)
                setattr(value, "inRelationTo", self)

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familytree_Person__children", None)
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
                    

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familytree_Person__Person", None)
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
    def Person10(self):
        return self.__Person10

    @Person10.setter
    def Person10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familytree_Person__Person10", None)
        self.__Person10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inRelationWith"):
                opp_val = getattr(old_value, "inRelationWith", None)
                if opp_val == self:
                    setattr(old_value, "inRelationWith", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inRelationWith"):
                opp_val = getattr(value, "inRelationWith", None)
                setattr(value, "inRelationWith", self)

    @property
    def inRelationWith(self):
        return self.__inRelationWith

    @inRelationWith.setter
    def inRelationWith(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familytree_Person__inRelationWith", None)
        self.__inRelationWith = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Person10"):
                opp_val = getattr(old_value, "Person10", None)
                if opp_val == self:
                    setattr(old_value, "Person10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Person10"):
                opp_val = getattr(value, "Person10", None)
                setattr(value, "Person10", self)

    @property
    def inRelationTo(self):
        return self.__inRelationTo

    @inRelationTo.setter
    def inRelationTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familytree_Person__inRelationTo", None)
        self.__inRelationTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Person7"):
                opp_val = getattr(old_value, "Person7", None)
                if opp_val == self:
                    setattr(old_value, "Person7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Person7"):
                opp_val = getattr(value, "Person7", None)
                setattr(value, "Person7", self)

    @property
    def familytree_Person(self):
        return self.__familytree_Person

    @familytree_Person.setter
    def familytree_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familytree_Person__familytree_Person", None)
        self.__familytree_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "familytree_FamilyTree"):
                opp_val = getattr(old_value, "familytree_FamilyTree", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "familytree_FamilyTree"):
                opp_val = getattr(value, "familytree_FamilyTree", None)
                if opp_val is None:
                    setattr(value, "familytree_FamilyTree", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Person4(self):
        return self.__Person4

    @Person4.setter
    def Person4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familytree_Person__Person4", None)
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

class Person:

    pass
class familytree_Man(Person):

    pass
class familytree_Woman(Person):

    pass
class familytree_FamilyTree:

    pass