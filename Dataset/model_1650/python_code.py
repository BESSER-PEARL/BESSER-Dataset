from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class simpleworld102_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Named:

    pass
class simpleworld102_Part(Named):

    def __init__(self, content: str, id: int, simpleworld102_Part: "simpleworld102_Thing" = None, simpleworld102_Part14: "simpleworld102_Relations" = None):
        self.content = content
        self.id = id
        self.simpleworld102_Part = simpleworld102_Part
        self.simpleworld102_Part14 = simpleworld102_Part14
        
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
    def simpleworld102_Part(self):
        return self.__simpleworld102_Part

    @simpleworld102_Part.setter
    def simpleworld102_Part(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld102_Part__simpleworld102_Part", None)
        self.__simpleworld102_Part = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleworld102_Thing7"):
                opp_val = getattr(old_value, "simpleworld102_Thing7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleworld102_Thing7"):
                opp_val = getattr(value, "simpleworld102_Thing7", None)
                if opp_val is None:
                    setattr(value, "simpleworld102_Thing7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleworld102_Part14(self):
        return self.__simpleworld102_Part14

    @simpleworld102_Part14.setter
    def simpleworld102_Part14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld102_Part__simpleworld102_Part14", None)
        self.__simpleworld102_Part14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleworld102_Relations13"):
                opp_val = getattr(old_value, "simpleworld102_Relations13", None)
                if opp_val == self:
                    setattr(old_value, "simpleworld102_Relations13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleworld102_Relations13"):
                opp_val = getattr(value, "simpleworld102_Relations13", None)
                setattr(value, "simpleworld102_Relations13", self)

class simpleworld102_World(Named):

    pass
class simpleworld102_Thing(Named):

    pass
class simpleworld102_Element:

    def __init__(self, description: str, simpleworld102_Element: "simpleworld102_Person" = None):
        self.description = description
        self.simpleworld102_Element = simpleworld102_Element
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def simpleworld102_Element(self):
        return self.__simpleworld102_Element

    @simpleworld102_Element.setter
    def simpleworld102_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld102_Element__simpleworld102_Element", None)
        self.__simpleworld102_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleworld102_Person2"):
                opp_val = getattr(old_value, "simpleworld102_Person2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleworld102_Person2"):
                opp_val = getattr(value, "simpleworld102_Person2", None)
                if opp_val is None:
                    setattr(value, "simpleworld102_Person2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simpleworld102_Relations:

    def __init__(self, since: int, simpleworld102_Relations: "simpleworld102_Person" = None, simpleworld102_Relations13: "simpleworld102_Part" = None):
        self.since = since
        self.simpleworld102_Relations = simpleworld102_Relations
        self.simpleworld102_Relations13 = simpleworld102_Relations13
        
    @property
    def since(self) -> int:
        return self.__since

    @since.setter
    def since(self, since: int):
        self.__since = since

    @property
    def simpleworld102_Relations(self):
        return self.__simpleworld102_Relations

    @simpleworld102_Relations.setter
    def simpleworld102_Relations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld102_Relations__simpleworld102_Relations", None)
        self.__simpleworld102_Relations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleworld102_Person"):
                opp_val = getattr(old_value, "simpleworld102_Person", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleworld102_Person"):
                opp_val = getattr(value, "simpleworld102_Person", None)
                if opp_val is None:
                    setattr(value, "simpleworld102_Person", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleworld102_Relations13(self):
        return self.__simpleworld102_Relations13

    @simpleworld102_Relations13.setter
    def simpleworld102_Relations13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld102_Relations__simpleworld102_Relations13", None)
        self.__simpleworld102_Relations13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleworld102_Part14"):
                opp_val = getattr(old_value, "simpleworld102_Part14", None)
                if opp_val == self:
                    setattr(old_value, "simpleworld102_Part14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleworld102_Part14"):
                opp_val = getattr(value, "simpleworld102_Part14", None)
                setattr(value, "simpleworld102_Part14", self)

class simpleworld102_Person:

    def __init__(self, name: str, foreName: str, Person: "simpleworld102_Thing" = None, simpleworld102_Person: set["simpleworld102_Relations"] = None, simpleworld102_Person2: set["simpleworld102_Element"] = None, simpleworld102_Person4: "simpleworld102_Thing" = None, persons: set["simpleworld102_Thing"] = None, simpleworld102_Person16: "simpleworld102_World" = None):
        self.name = name
        self.foreName = foreName
        self.Person = Person
        self.simpleworld102_Person = simpleworld102_Person if simpleworld102_Person is not None else set()
        self.simpleworld102_Person2 = simpleworld102_Person2 if simpleworld102_Person2 is not None else set()
        self.simpleworld102_Person4 = simpleworld102_Person4
        self.persons = persons if persons is not None else set()
        self.simpleworld102_Person16 = simpleworld102_Person16
        
    @property
    def foreName(self) -> str:
        return self.__foreName

    @foreName.setter
    def foreName(self, foreName: str):
        self.__foreName = foreName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simpleworld102_Person2(self):
        return self.__simpleworld102_Person2

    @simpleworld102_Person2.setter
    def simpleworld102_Person2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld102_Person__simpleworld102_Person2", None)
        self.__simpleworld102_Person2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleworld102_Element"):
                    opp_val = getattr(item, "simpleworld102_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleworld102_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleworld102_Element"):
                    opp_val = getattr(item, "simpleworld102_Element", None)
                    
                    setattr(item, "simpleworld102_Element", self)
                    

    @property
    def simpleworld102_Person16(self):
        return self.__simpleworld102_Person16

    @simpleworld102_Person16.setter
    def simpleworld102_Person16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld102_Person__simpleworld102_Person16", None)
        self.__simpleworld102_Person16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleworld102_World"):
                opp_val = getattr(old_value, "simpleworld102_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleworld102_World"):
                opp_val = getattr(value, "simpleworld102_World", None)
                if opp_val is None:
                    setattr(value, "simpleworld102_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleworld102_Person4(self):
        return self.__simpleworld102_Person4

    @simpleworld102_Person4.setter
    def simpleworld102_Person4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld102_Person__simpleworld102_Person4", None)
        self.__simpleworld102_Person4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleworld102_Thing"):
                opp_val = getattr(old_value, "simpleworld102_Thing", None)
                if opp_val == self:
                    setattr(old_value, "simpleworld102_Thing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleworld102_Thing"):
                opp_val = getattr(value, "simpleworld102_Thing", None)
                setattr(value, "simpleworld102_Thing", self)

    @property
    def persons(self):
        return self.__persons

    @persons.setter
    def persons(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld102_Person__persons", None)
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
    def simpleworld102_Person(self):
        return self.__simpleworld102_Person

    @simpleworld102_Person.setter
    def simpleworld102_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld102_Person__simpleworld102_Person", None)
        self.__simpleworld102_Person = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleworld102_Relations"):
                    opp_val = getattr(item, "simpleworld102_Relations", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleworld102_Relations", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleworld102_Relations"):
                    opp_val = getattr(item, "simpleworld102_Relations", None)
                    
                    setattr(item, "simpleworld102_Relations", self)
                    

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld102_Person__Person", None)
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
