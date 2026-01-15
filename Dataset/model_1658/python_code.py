from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class hello123_Alias:

    def __init__(self, id: str, hello123_Alias: "hello123_NamedElement" = None):
        self.id = id
        self.hello123_Alias = hello123_Alias
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def hello123_Alias(self):
        return self.__hello123_Alias

    @hello123_Alias.setter
    def hello123_Alias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello123_Alias__hello123_Alias", None)
        self.__hello123_Alias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello123_NamedElement"):
                opp_val = getattr(old_value, "hello123_NamedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello123_NamedElement"):
                opp_val = getattr(value, "hello123_NamedElement", None)
                if opp_val is None:
                    setattr(value, "hello123_NamedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class hello123_NamedElement(ABC):

    def __init__(self, name: str, hello123_NamedElement: set["hello123_Alias"] = None):
        self.name = name
        self.hello123_NamedElement = hello123_NamedElement if hello123_NamedElement is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hello123_NamedElement(self):
        return self.__hello123_NamedElement

    @hello123_NamedElement.setter
    def hello123_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello123_NamedElement__hello123_NamedElement", None)
        self.__hello123_NamedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hello123_Alias"):
                    opp_val = getattr(item, "hello123_Alias", None)
                    
                    if opp_val == self:
                        setattr(item, "hello123_Alias", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hello123_Alias"):
                    opp_val = getattr(item, "hello123_Alias", None)
                    
                    setattr(item, "hello123_Alias", self)
                    

class hello123_Bar:

    def __init__(self, id: str, hello123_Bar: "hello123_Thing" = None):
        self.id = id
        self.hello123_Bar = hello123_Bar
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def hello123_Bar(self):
        return self.__hello123_Bar

    @hello123_Bar.setter
    def hello123_Bar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello123_Bar__hello123_Bar", None)
        self.__hello123_Bar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello123_Thing7"):
                opp_val = getattr(old_value, "hello123_Thing7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello123_Thing7"):
                opp_val = getattr(value, "hello123_Thing7", None)
                if opp_val is None:
                    setattr(value, "hello123_Thing7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class hello123_World:

    pass
class hello123_Foo:

    def __init__(self, id: str, hello123_Foo: "hello123_Thing" = None):
        self.id = id
        self.hello123_Foo = hello123_Foo
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def hello123_Foo(self):
        return self.__hello123_Foo

    @hello123_Foo.setter
    def hello123_Foo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello123_Foo__hello123_Foo", None)
        self.__hello123_Foo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello123_Thing5"):
                opp_val = getattr(old_value, "hello123_Thing5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello123_Thing5"):
                opp_val = getattr(value, "hello123_Thing5", None)
                if opp_val is None:
                    setattr(value, "hello123_Thing5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class hello123_Property:

    def __init__(self, name: str, value: str, hello123_Property: "hello123_Thing" = None):
        self.name = name
        self.value = value
        self.hello123_Property = hello123_Property
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def hello123_Property(self):
        return self.__hello123_Property

    @hello123_Property.setter
    def hello123_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello123_Property__hello123_Property", None)
        self.__hello123_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello123_Thing3"):
                opp_val = getattr(old_value, "hello123_Thing3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello123_Thing3"):
                opp_val = getattr(value, "hello123_Thing3", None)
                if opp_val is None:
                    setattr(value, "hello123_Thing3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedElement:

    pass
class hello123_RelatedTo(NamedElement):

    def __init__(self, since: str, RelatedTo: "hello123_Thing" = None, relations: "hello123_Thing" = None, hello123_RelatedTo: "hello123_Thing" = None):
        self.since = since
        self.RelatedTo = RelatedTo
        self.relations = relations
        self.hello123_RelatedTo = hello123_RelatedTo
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def relations(self):
        return self.__relations

    @relations.setter
    def relations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello123_RelatedTo__relations", None)
        self.__relations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Thing"):
                opp_val = getattr(old_value, "Thing", None)
                if opp_val == self:
                    setattr(old_value, "Thing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Thing"):
                opp_val = getattr(value, "Thing", None)
                setattr(value, "Thing", self)

    @property
    def hello123_RelatedTo(self):
        return self.__hello123_RelatedTo

    @hello123_RelatedTo.setter
    def hello123_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello123_RelatedTo__hello123_RelatedTo", None)
        self.__hello123_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello123_Thing11"):
                opp_val = getattr(old_value, "hello123_Thing11", None)
                if opp_val == self:
                    setattr(old_value, "hello123_Thing11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello123_Thing11"):
                opp_val = getattr(value, "hello123_Thing11", None)
                setattr(value, "hello123_Thing11", self)

    @property
    def RelatedTo(self):
        return self.__RelatedTo

    @RelatedTo.setter
    def RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello123_RelatedTo__RelatedTo", None)
        self.__RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fromThing"):
                opp_val = getattr(old_value, "fromThing", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fromThing"):
                opp_val = getattr(value, "fromThing", None)
                if opp_val is None:
                    setattr(value, "fromThing", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class hello123_Thing(NamedElement):

    def __init__(self, id: int, hello123_Thing: "hello123_World" = None, fromThing: set["hello123_RelatedTo"] = None, hello123_Thing3: set["hello123_Property"] = None, hello123_Thing5: set["hello123_Foo"] = None, hello123_Thing7: set["hello123_Bar"] = None, Thing: "hello123_RelatedTo" = None, hello123_Thing11: "hello123_RelatedTo" = None):
        self.id = id
        self.hello123_Thing = hello123_Thing
        self.fromThing = fromThing if fromThing is not None else set()
        self.hello123_Thing3 = hello123_Thing3 if hello123_Thing3 is not None else set()
        self.hello123_Thing5 = hello123_Thing5 if hello123_Thing5 is not None else set()
        self.hello123_Thing7 = hello123_Thing7 if hello123_Thing7 is not None else set()
        self.Thing = Thing
        self.hello123_Thing11 = hello123_Thing11
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def hello123_Thing11(self):
        return self.__hello123_Thing11

    @hello123_Thing11.setter
    def hello123_Thing11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello123_Thing__hello123_Thing11", None)
        self.__hello123_Thing11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello123_RelatedTo"):
                opp_val = getattr(old_value, "hello123_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "hello123_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello123_RelatedTo"):
                opp_val = getattr(value, "hello123_RelatedTo", None)
                setattr(value, "hello123_RelatedTo", self)

    @property
    def hello123_Thing7(self):
        return self.__hello123_Thing7

    @hello123_Thing7.setter
    def hello123_Thing7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello123_Thing__hello123_Thing7", None)
        self.__hello123_Thing7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hello123_Bar"):
                    opp_val = getattr(item, "hello123_Bar", None)
                    
                    if opp_val == self:
                        setattr(item, "hello123_Bar", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hello123_Bar"):
                    opp_val = getattr(item, "hello123_Bar", None)
                    
                    setattr(item, "hello123_Bar", self)
                    

    @property
    def hello123_Thing(self):
        return self.__hello123_Thing

    @hello123_Thing.setter
    def hello123_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello123_Thing__hello123_Thing", None)
        self.__hello123_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello123_World"):
                opp_val = getattr(old_value, "hello123_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello123_World"):
                opp_val = getattr(value, "hello123_World", None)
                if opp_val is None:
                    setattr(value, "hello123_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Thing(self):
        return self.__Thing

    @Thing.setter
    def Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello123_Thing__Thing", None)
        self.__Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relations"):
                opp_val = getattr(old_value, "relations", None)
                if opp_val == self:
                    setattr(old_value, "relations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relations"):
                opp_val = getattr(value, "relations", None)
                setattr(value, "relations", self)

    @property
    def fromThing(self):
        return self.__fromThing

    @fromThing.setter
    def fromThing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello123_Thing__fromThing", None)
        self.__fromThing = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RelatedTo"):
                    opp_val = getattr(item, "RelatedTo", None)
                    
                    if opp_val == self:
                        setattr(item, "RelatedTo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RelatedTo"):
                    opp_val = getattr(item, "RelatedTo", None)
                    
                    setattr(item, "RelatedTo", self)
                    

    @property
    def hello123_Thing3(self):
        return self.__hello123_Thing3

    @hello123_Thing3.setter
    def hello123_Thing3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello123_Thing__hello123_Thing3", None)
        self.__hello123_Thing3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hello123_Property"):
                    opp_val = getattr(item, "hello123_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "hello123_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hello123_Property"):
                    opp_val = getattr(item, "hello123_Property", None)
                    
                    setattr(item, "hello123_Property", self)
                    

    @property
    def hello123_Thing5(self):
        return self.__hello123_Thing5

    @hello123_Thing5.setter
    def hello123_Thing5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello123_Thing__hello123_Thing5", None)
        self.__hello123_Thing5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hello123_Foo"):
                    opp_val = getattr(item, "hello123_Foo", None)
                    
                    if opp_val == self:
                        setattr(item, "hello123_Foo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hello123_Foo"):
                    opp_val = getattr(item, "hello123_Foo", None)
                    
                    setattr(item, "hello123_Foo", self)
                    
