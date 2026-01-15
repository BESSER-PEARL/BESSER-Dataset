from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class stuff_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class stuff_Foo:

    def __init__(self, name: str, stuff_Foo: "stuff_Stuff" = None, stuff_Foo8: "stuff_Stuff" = None, stuff_Foo11: "stuff_Thing" = None):
        self.name = name
        self.stuff_Foo = stuff_Foo
        self.stuff_Foo8 = stuff_Foo8
        self.stuff_Foo11 = stuff_Foo11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stuff_Foo(self):
        return self.__stuff_Foo

    @stuff_Foo.setter
    def stuff_Foo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stuff_Foo__stuff_Foo", None)
        self.__stuff_Foo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stuff_Stuff"):
                opp_val = getattr(old_value, "stuff_Stuff", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stuff_Stuff"):
                opp_val = getattr(value, "stuff_Stuff", None)
                if opp_val is None:
                    setattr(value, "stuff_Stuff", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stuff_Foo8(self):
        return self.__stuff_Foo8

    @stuff_Foo8.setter
    def stuff_Foo8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stuff_Foo__stuff_Foo8", None)
        self.__stuff_Foo8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stuff_Stuff9"):
                opp_val = getattr(old_value, "stuff_Stuff9", None)
                if opp_val == self:
                    setattr(old_value, "stuff_Stuff9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stuff_Stuff9"):
                opp_val = getattr(value, "stuff_Stuff9", None)
                setattr(value, "stuff_Stuff9", self)

    @property
    def stuff_Foo11(self):
        return self.__stuff_Foo11

    @stuff_Foo11.setter
    def stuff_Foo11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stuff_Foo__stuff_Foo11", None)
        self.__stuff_Foo11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stuff_Thing12"):
                opp_val = getattr(old_value, "stuff_Thing12", None)
                if opp_val == self:
                    setattr(old_value, "stuff_Thing12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stuff_Thing12"):
                opp_val = getattr(value, "stuff_Thing12", None)
                setattr(value, "stuff_Thing12", self)

class Thing:

    pass
class stuff_Stuff(Thing):

    pass
class NamedElement:

    pass
class stuff_Baz(NamedElement):

    pass
class stuff_Bar(NamedElement):

    pass
class stuff_Thing:

    def __init__(self, id: int, stuff_Thing: "stuff_World" = None, stuff_Thing3: "stuff_Thing" = None, stuff_Thing1: set["stuff_Thing"] = None, stuff_Thing12: "stuff_Foo" = None):
        self.id = id
        self.stuff_Thing = stuff_Thing
        self.stuff_Thing3 = stuff_Thing3
        self.stuff_Thing1 = stuff_Thing1 if stuff_Thing1 is not None else set()
        self.stuff_Thing12 = stuff_Thing12
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def stuff_Thing3(self):
        return self.__stuff_Thing3

    @stuff_Thing3.setter
    def stuff_Thing3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stuff_Thing__stuff_Thing3", None)
        self.__stuff_Thing3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stuff_Thing1"):
                opp_val = getattr(old_value, "stuff_Thing1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stuff_Thing1"):
                opp_val = getattr(value, "stuff_Thing1", None)
                if opp_val is None:
                    setattr(value, "stuff_Thing1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stuff_Thing(self):
        return self.__stuff_Thing

    @stuff_Thing.setter
    def stuff_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stuff_Thing__stuff_Thing", None)
        self.__stuff_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stuff_World"):
                opp_val = getattr(old_value, "stuff_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stuff_World"):
                opp_val = getattr(value, "stuff_World", None)
                if opp_val is None:
                    setattr(value, "stuff_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stuff_Thing1(self):
        return self.__stuff_Thing1

    @stuff_Thing1.setter
    def stuff_Thing1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stuff_Thing__stuff_Thing1", None)
        self.__stuff_Thing1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stuff_Thing3"):
                    opp_val = getattr(item, "stuff_Thing3", None)
                    
                    if opp_val == self:
                        setattr(item, "stuff_Thing3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stuff_Thing3"):
                    opp_val = getattr(item, "stuff_Thing3", None)
                    
                    setattr(item, "stuff_Thing3", self)
                    

    @property
    def stuff_Thing12(self):
        return self.__stuff_Thing12

    @stuff_Thing12.setter
    def stuff_Thing12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stuff_Thing__stuff_Thing12", None)
        self.__stuff_Thing12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stuff_Foo11"):
                opp_val = getattr(old_value, "stuff_Foo11", None)
                if opp_val == self:
                    setattr(old_value, "stuff_Foo11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stuff_Foo11"):
                opp_val = getattr(value, "stuff_Foo11", None)
                setattr(value, "stuff_Foo11", self)

class stuff_World:

    pass