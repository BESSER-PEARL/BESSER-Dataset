from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class simpleworld101_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class simpleworld101_Person:

    def __init__(self, name: str, foreName: str, simpleworld101_Person: set["simpleworld101_Relations"] = None, simpleworld101_Person2: set["simpleworld101_Element"] = None, simpleworld101_Person4: "simpleworld101_Thing" = None, persons: set["simpleworld101_Thing"] = None, simpleworld101_Person16: "simpleworld101_World" = None, Person: "simpleworld101_Thing" = None):
        self.name = name
        self.foreName = foreName
        self.simpleworld101_Person = simpleworld101_Person if simpleworld101_Person is not None else set()
        self.simpleworld101_Person2 = simpleworld101_Person2 if simpleworld101_Person2 is not None else set()
        self.simpleworld101_Person4 = simpleworld101_Person4
        self.persons = persons if persons is not None else set()
        self.simpleworld101_Person16 = simpleworld101_Person16
        self.Person = Person
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def foreName(self) -> str:
        return self.__foreName

    @foreName.setter
    def foreName(self, foreName: str):
        self.__foreName = foreName

    @property
    def simpleworld101_Person4(self):
        return self.__simpleworld101_Person4

    @simpleworld101_Person4.setter
    def simpleworld101_Person4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld101_Person__simpleworld101_Person4", None)
        self.__simpleworld101_Person4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleworld101_Thing"):
                opp_val = getattr(old_value, "simpleworld101_Thing", None)
                if opp_val == self:
                    setattr(old_value, "simpleworld101_Thing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleworld101_Thing"):
                opp_val = getattr(value, "simpleworld101_Thing", None)
                setattr(value, "simpleworld101_Thing", self)

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld101_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "things"):
                opp_val = getattr(old_value, "things", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "things"):
                opp_val = getattr(value, "things", None)
                if opp_val is None:
                    setattr(value, "things", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleworld101_Person2(self):
        return self.__simpleworld101_Person2

    @simpleworld101_Person2.setter
    def simpleworld101_Person2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld101_Person__simpleworld101_Person2", None)
        self.__simpleworld101_Person2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleworld101_Element"):
                    opp_val = getattr(item, "simpleworld101_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleworld101_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleworld101_Element"):
                    opp_val = getattr(item, "simpleworld101_Element", None)
                    
                    setattr(item, "simpleworld101_Element", self)
                    

    @property
    def persons(self):
        return self.__persons

    @persons.setter
    def persons(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld101_Person__persons", None)
        self.__persons = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Thing"):
                    opp_val = getattr(item, "Thing", None)
                    
                    if opp_val == self:
                        setattr(item, "Thing", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Thing"):
                    opp_val = getattr(item, "Thing", None)
                    
                    setattr(item, "Thing", self)
                    

    @property
    def simpleworld101_Person16(self):
        return self.__simpleworld101_Person16

    @simpleworld101_Person16.setter
    def simpleworld101_Person16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld101_Person__simpleworld101_Person16", None)
        self.__simpleworld101_Person16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleworld101_World"):
                opp_val = getattr(old_value, "simpleworld101_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleworld101_World"):
                opp_val = getattr(value, "simpleworld101_World", None)
                if opp_val is None:
                    setattr(value, "simpleworld101_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleworld101_Person(self):
        return self.__simpleworld101_Person

    @simpleworld101_Person.setter
    def simpleworld101_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld101_Person__simpleworld101_Person", None)
        self.__simpleworld101_Person = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleworld101_Relations"):
                    opp_val = getattr(item, "simpleworld101_Relations", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleworld101_Relations", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleworld101_Relations"):
                    opp_val = getattr(item, "simpleworld101_Relations", None)
                    
                    setattr(item, "simpleworld101_Relations", self)
                    

class Named:

    pass
class simpleworld101_World(Named):

    pass
class simpleworld101_Part(Named):

    def __init__(self, content: str, id: int, simpleworld101_Part14: "simpleworld101_Relations" = None, simpleworld101_Part: "simpleworld101_Thing" = None):
        self.content = content
        self.id = id
        self.simpleworld101_Part14 = simpleworld101_Part14
        self.simpleworld101_Part = simpleworld101_Part
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def simpleworld101_Part(self):
        return self.__simpleworld101_Part

    @simpleworld101_Part.setter
    def simpleworld101_Part(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld101_Part__simpleworld101_Part", None)
        self.__simpleworld101_Part = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleworld101_Thing7"):
                opp_val = getattr(old_value, "simpleworld101_Thing7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleworld101_Thing7"):
                opp_val = getattr(value, "simpleworld101_Thing7", None)
                if opp_val is None:
                    setattr(value, "simpleworld101_Thing7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleworld101_Part14(self):
        return self.__simpleworld101_Part14

    @simpleworld101_Part14.setter
    def simpleworld101_Part14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld101_Part__simpleworld101_Part14", None)
        self.__simpleworld101_Part14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleworld101_Relations13"):
                opp_val = getattr(old_value, "simpleworld101_Relations13", None)
                if opp_val == self:
                    setattr(old_value, "simpleworld101_Relations13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleworld101_Relations13"):
                opp_val = getattr(value, "simpleworld101_Relations13", None)
                setattr(value, "simpleworld101_Relations13", self)

class simpleworld101_Thing(Named):

    pass
class simpleworld101_Element:

    def __init__(self, description: str, simpleworld101_Element: "simpleworld101_Person" = None):
        self.description = description
        self.simpleworld101_Element = simpleworld101_Element
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def simpleworld101_Element(self):
        return self.__simpleworld101_Element

    @simpleworld101_Element.setter
    def simpleworld101_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld101_Element__simpleworld101_Element", None)
        self.__simpleworld101_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleworld101_Person2"):
                opp_val = getattr(old_value, "simpleworld101_Person2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleworld101_Person2"):
                opp_val = getattr(value, "simpleworld101_Person2", None)
                if opp_val is None:
                    setattr(value, "simpleworld101_Person2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simpleworld101_Relations:

    def __init__(self, since: int, simpleworld101_Relations: "simpleworld101_Person" = None, simpleworld101_Relations13: "simpleworld101_Part" = None):
        self.since = since
        self.simpleworld101_Relations = simpleworld101_Relations
        self.simpleworld101_Relations13 = simpleworld101_Relations13
        
    @property
    def since(self) -> int:
        return self.__since

    @since.setter
    def since(self, since: int):
        self.__since = since

    @property
    def simpleworld101_Relations13(self):
        return self.__simpleworld101_Relations13

    @simpleworld101_Relations13.setter
    def simpleworld101_Relations13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld101_Relations__simpleworld101_Relations13", None)
        self.__simpleworld101_Relations13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleworld101_Part14"):
                opp_val = getattr(old_value, "simpleworld101_Part14", None)
                if opp_val == self:
                    setattr(old_value, "simpleworld101_Part14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleworld101_Part14"):
                opp_val = getattr(value, "simpleworld101_Part14", None)
                setattr(value, "simpleworld101_Part14", self)

    @property
    def simpleworld101_Relations(self):
        return self.__simpleworld101_Relations

    @simpleworld101_Relations.setter
    def simpleworld101_Relations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld101_Relations__simpleworld101_Relations", None)
        self.__simpleworld101_Relations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleworld101_Person"):
                opp_val = getattr(old_value, "simpleworld101_Person", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleworld101_Person"):
                opp_val = getattr(value, "simpleworld101_Person", None)
                if opp_val is None:
                    setattr(value, "simpleworld101_Person", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
