from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Person:

    pass
class familytree_Woman(Person):

    pass
class familytree_Man(Person):

    pass
class familytree_Wedding:

    pass
class familytree_Person(ABC):

    def __init__(self, firstName: str, lastName: str, birthYear: int, deathYear: int, familytree_Person: "familytree_FamilyTree" = None, Person: "familytree_Person" = None, parents: set["familytree_Person"] = None, Person7: "familytree_Person" = None, children: set["familytree_Person"] = None):
        self.firstName = firstName
        self.lastName = lastName
        self.birthYear = birthYear
        self.deathYear = deathYear
        self.familytree_Person = familytree_Person
        self.Person = Person
        self.parents = parents if parents is not None else set()
        self.Person7 = Person7
        self.children = children if children is not None else set()
        
    @property
    def birthYear(self) -> int:
        return self.__birthYear

    @birthYear.setter
    def birthYear(self, birthYear: int):
        self.__birthYear = birthYear

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def deathYear(self) -> int:
        return self.__deathYear

    @deathYear.setter
    def deathYear(self, deathYear: int):
        self.__deathYear = deathYear

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

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
    def Person7(self):
        return self.__Person7

    @Person7.setter
    def Person7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familytree_Person__Person7", None)
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
                    

class familytree_FamilyTree:

    def __init__(self, name: str, familytree_FamilyTree: set["familytree_Person"] = None, familytree_FamilyTree2: set["familytree_Wedding"] = None):
        self.name = name
        self.familytree_FamilyTree = familytree_FamilyTree if familytree_FamilyTree is not None else set()
        self.familytree_FamilyTree2 = familytree_FamilyTree2 if familytree_FamilyTree2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def familytree_FamilyTree(self):
        return self.__familytree_FamilyTree

    @familytree_FamilyTree.setter
    def familytree_FamilyTree(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familytree_FamilyTree__familytree_FamilyTree", None)
        self.__familytree_FamilyTree = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "familytree_Person"):
                    opp_val = getattr(item, "familytree_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "familytree_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "familytree_Person"):
                    opp_val = getattr(item, "familytree_Person", None)
                    
                    setattr(item, "familytree_Person", self)
                    

    @property
    def familytree_FamilyTree2(self):
        return self.__familytree_FamilyTree2

    @familytree_FamilyTree2.setter
    def familytree_FamilyTree2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familytree_FamilyTree__familytree_FamilyTree2", None)
        self.__familytree_FamilyTree2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "familytree_Wedding"):
                    opp_val = getattr(item, "familytree_Wedding", None)
                    
                    if opp_val == self:
                        setattr(item, "familytree_Wedding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "familytree_Wedding"):
                    opp_val = getattr(item, "familytree_Wedding", None)
                    
                    setattr(item, "familytree_Wedding", self)
                    
