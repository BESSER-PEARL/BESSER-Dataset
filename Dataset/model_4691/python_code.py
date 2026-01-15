from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Person:

    pass
class basicfamily_Man(Person):

    pass
class basicfamily_Woman(Person):

    pass
class basicfamily_Person(ABC):

    def __init__(self, name: str, basicfamily_Person: "basicfamily_Family" = None, Person: "basicfamily_Person" = None, children: set["basicfamily_Person"] = None, Person5: "basicfamily_Person" = None, parents: set["basicfamily_Person"] = None, basicfamily_Person7: "basicfamily_Woman" = None, basicfamily_Person9: "basicfamily_Man" = None):
        self.name = name
        self.basicfamily_Person = basicfamily_Person
        self.Person = Person
        self.children = children if children is not None else set()
        self.Person5 = Person5
        self.parents = parents if parents is not None else set()
        self.basicfamily_Person7 = basicfamily_Person7
        self.basicfamily_Person9 = basicfamily_Person9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def basicfamily_Person9(self):
        return self.__basicfamily_Person9

    @basicfamily_Person9.setter
    def basicfamily_Person9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfamily_Person__basicfamily_Person9", None)
        self.__basicfamily_Person9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicfamily_Man"):
                opp_val = getattr(old_value, "basicfamily_Man", None)
                if opp_val == self:
                    setattr(old_value, "basicfamily_Man", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicfamily_Man"):
                opp_val = getattr(value, "basicfamily_Man", None)
                setattr(value, "basicfamily_Man", self)

    @property
    def basicfamily_Person7(self):
        return self.__basicfamily_Person7

    @basicfamily_Person7.setter
    def basicfamily_Person7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfamily_Person__basicfamily_Person7", None)
        self.__basicfamily_Person7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicfamily_Woman"):
                opp_val = getattr(old_value, "basicfamily_Woman", None)
                if opp_val == self:
                    setattr(old_value, "basicfamily_Woman", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicfamily_Woman"):
                opp_val = getattr(value, "basicfamily_Woman", None)
                setattr(value, "basicfamily_Woman", self)

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfamily_Person__Person", None)
        self.__Person = value
        
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
        old_value = getattr(self, f"_basicfamily_Person__parents", None)
        self.__parents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person5"):
                    opp_val = getattr(item, "Person5", None)
                    
                    if opp_val == self:
                        setattr(item, "Person5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person5"):
                    opp_val = getattr(item, "Person5", None)
                    
                    setattr(item, "Person5", self)
                    

    @property
    def Person5(self):
        return self.__Person5

    @Person5.setter
    def Person5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfamily_Person__Person5", None)
        self.__Person5 = value
        
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
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfamily_Person__children", None)
        self.__children = value if value is not None else set()
        
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
    def basicfamily_Person(self):
        return self.__basicfamily_Person

    @basicfamily_Person.setter
    def basicfamily_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfamily_Person__basicfamily_Person", None)
        self.__basicfamily_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicfamily_Family"):
                opp_val = getattr(old_value, "basicfamily_Family", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicfamily_Family"):
                opp_val = getattr(value, "basicfamily_Family", None)
                if opp_val is None:
                    setattr(value, "basicfamily_Family", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class basicfamily_Family:

    def __init__(self, name: str, basicfamily_Family: set["basicfamily_Person"] = None):
        self.name = name
        self.basicfamily_Family = basicfamily_Family if basicfamily_Family is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def basicfamily_Family(self):
        return self.__basicfamily_Family

    @basicfamily_Family.setter
    def basicfamily_Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfamily_Family__basicfamily_Family", None)
        self.__basicfamily_Family = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basicfamily_Person"):
                    opp_val = getattr(item, "basicfamily_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "basicfamily_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basicfamily_Person"):
                    opp_val = getattr(item, "basicfamily_Person", None)
                    
                    setattr(item, "basicfamily_Person", self)
                    
