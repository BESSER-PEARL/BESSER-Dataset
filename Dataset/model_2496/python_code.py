from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class y4fsm_State(ABC):

    def __init__(self, id: str, y4fsm_State2: set["y4fsm_Foo"] = None, y4fsm_State4: set["y4fsm_Bar"] = None, y4fsm_State: "y4fsm_Region" = None):
        self.id = id
        self.y4fsm_State2 = y4fsm_State2 if y4fsm_State2 is not None else set()
        self.y4fsm_State4 = y4fsm_State4 if y4fsm_State4 is not None else set()
        self.y4fsm_State = y4fsm_State
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def y4fsm_State(self):
        return self.__y4fsm_State

    @y4fsm_State.setter
    def y4fsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_y4fsm_State__y4fsm_State", None)
        self.__y4fsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "y4fsm_Region"):
                opp_val = getattr(old_value, "y4fsm_Region", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "y4fsm_Region"):
                opp_val = getattr(value, "y4fsm_Region", None)
                if opp_val is None:
                    setattr(value, "y4fsm_Region", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def y4fsm_State2(self):
        return self.__y4fsm_State2

    @y4fsm_State2.setter
    def y4fsm_State2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_y4fsm_State__y4fsm_State2", None)
        self.__y4fsm_State2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "y4fsm_Foo"):
                    opp_val = getattr(item, "y4fsm_Foo", None)
                    
                    if opp_val == self:
                        setattr(item, "y4fsm_Foo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "y4fsm_Foo"):
                    opp_val = getattr(item, "y4fsm_Foo", None)
                    
                    setattr(item, "y4fsm_Foo", self)
                    

    @property
    def y4fsm_State4(self):
        return self.__y4fsm_State4

    @y4fsm_State4.setter
    def y4fsm_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_y4fsm_State__y4fsm_State4", None)
        self.__y4fsm_State4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "y4fsm_Bar"):
                    opp_val = getattr(item, "y4fsm_Bar", None)
                    
                    if opp_val == self:
                        setattr(item, "y4fsm_Bar", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "y4fsm_Bar"):
                    opp_val = getattr(item, "y4fsm_Bar", None)
                    
                    setattr(item, "y4fsm_Bar", self)
                    

class y4fsm_Bar:

    def __init__(self, baz: str, y4fsm_Bar: "y4fsm_State" = None):
        self.baz = baz
        self.y4fsm_Bar = y4fsm_Bar
        
    @property
    def baz(self) -> str:
        return self.__baz

    @baz.setter
    def baz(self, baz: str):
        self.__baz = baz

    @property
    def y4fsm_Bar(self):
        return self.__y4fsm_Bar

    @y4fsm_Bar.setter
    def y4fsm_Bar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_y4fsm_Bar__y4fsm_Bar", None)
        self.__y4fsm_Bar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "y4fsm_State4"):
                opp_val = getattr(old_value, "y4fsm_State4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "y4fsm_State4"):
                opp_val = getattr(value, "y4fsm_State4", None)
                if opp_val is None:
                    setattr(value, "y4fsm_State4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class y4fsm_Foo:

    def __init__(self, zoo: str, y4fsm_Foo: "y4fsm_State" = None):
        self.zoo = zoo
        self.y4fsm_Foo = y4fsm_Foo
        
    @property
    def zoo(self) -> str:
        return self.__zoo

    @zoo.setter
    def zoo(self, zoo: str):
        self.__zoo = zoo

    @property
    def y4fsm_Foo(self):
        return self.__y4fsm_Foo

    @y4fsm_Foo.setter
    def y4fsm_Foo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_y4fsm_Foo__y4fsm_Foo", None)
        self.__y4fsm_Foo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "y4fsm_State2"):
                opp_val = getattr(old_value, "y4fsm_State2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "y4fsm_State2"):
                opp_val = getattr(value, "y4fsm_State2", None)
                if opp_val is None:
                    setattr(value, "y4fsm_State2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class State:

    pass
class y4fsm_Region(State):

    def __init__(self, name: str, y4fsm_Region: set["y4fsm_State"] = None):
        self.name = name
        self.y4fsm_Region = y4fsm_Region if y4fsm_Region is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def y4fsm_Region(self):
        return self.__y4fsm_Region

    @y4fsm_Region.setter
    def y4fsm_Region(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_y4fsm_Region__y4fsm_Region", None)
        self.__y4fsm_Region = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "y4fsm_State"):
                    opp_val = getattr(item, "y4fsm_State", None)
                    
                    if opp_val == self:
                        setattr(item, "y4fsm_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "y4fsm_State"):
                    opp_val = getattr(item, "y4fsm_State", None)
                    
                    setattr(item, "y4fsm_State", self)
                    
