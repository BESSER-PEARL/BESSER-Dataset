from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AbstractState:

    pass
class y2fsm_Region(AbstractState):

    def __init__(self, name: str, y2fsm_Region: set["y2fsm_AbstractState"] = None, y2fsm_Region2: set["y2fsm_Foo"] = None):
        self.name = name
        self.y2fsm_Region = y2fsm_Region if y2fsm_Region is not None else set()
        self.y2fsm_Region2 = y2fsm_Region2 if y2fsm_Region2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def y2fsm_Region(self):
        return self.__y2fsm_Region

    @y2fsm_Region.setter
    def y2fsm_Region(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_y2fsm_Region__y2fsm_Region", None)
        self.__y2fsm_Region = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "y2fsm_AbstractState"):
                    opp_val = getattr(item, "y2fsm_AbstractState", None)
                    
                    if opp_val == self:
                        setattr(item, "y2fsm_AbstractState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "y2fsm_AbstractState"):
                    opp_val = getattr(item, "y2fsm_AbstractState", None)
                    
                    setattr(item, "y2fsm_AbstractState", self)
                    

    @property
    def y2fsm_Region2(self):
        return self.__y2fsm_Region2

    @y2fsm_Region2.setter
    def y2fsm_Region2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_y2fsm_Region__y2fsm_Region2", None)
        self.__y2fsm_Region2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "y2fsm_Foo"):
                    opp_val = getattr(item, "y2fsm_Foo", None)
                    
                    if opp_val == self:
                        setattr(item, "y2fsm_Foo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "y2fsm_Foo"):
                    opp_val = getattr(item, "y2fsm_Foo", None)
                    
                    setattr(item, "y2fsm_Foo", self)
                    

class y2fsm_Foo:

    def __init__(self, id: str, y2fsm_Foo: "y2fsm_Region" = None, y2fsm_Foo5: "y2fsm_AbstractState" = None):
        self.id = id
        self.y2fsm_Foo = y2fsm_Foo
        self.y2fsm_Foo5 = y2fsm_Foo5
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def y2fsm_Foo5(self):
        return self.__y2fsm_Foo5

    @y2fsm_Foo5.setter
    def y2fsm_Foo5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_y2fsm_Foo__y2fsm_Foo5", None)
        self.__y2fsm_Foo5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "y2fsm_AbstractState4"):
                opp_val = getattr(old_value, "y2fsm_AbstractState4", None)
                if opp_val == self:
                    setattr(old_value, "y2fsm_AbstractState4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "y2fsm_AbstractState4"):
                opp_val = getattr(value, "y2fsm_AbstractState4", None)
                setattr(value, "y2fsm_AbstractState4", self)

    @property
    def y2fsm_Foo(self):
        return self.__y2fsm_Foo

    @y2fsm_Foo.setter
    def y2fsm_Foo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_y2fsm_Foo__y2fsm_Foo", None)
        self.__y2fsm_Foo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "y2fsm_Region2"):
                opp_val = getattr(old_value, "y2fsm_Region2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "y2fsm_Region2"):
                opp_val = getattr(value, "y2fsm_Region2", None)
                if opp_val is None:
                    setattr(value, "y2fsm_Region2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class y2fsm_AbstractState(ABC):

    def __init__(self, id: str, y2fsm_AbstractState: "y2fsm_Region" = None, y2fsm_AbstractState4: "y2fsm_Foo" = None):
        self.id = id
        self.y2fsm_AbstractState = y2fsm_AbstractState
        self.y2fsm_AbstractState4 = y2fsm_AbstractState4
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def y2fsm_AbstractState(self):
        return self.__y2fsm_AbstractState

    @y2fsm_AbstractState.setter
    def y2fsm_AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_y2fsm_AbstractState__y2fsm_AbstractState", None)
        self.__y2fsm_AbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "y2fsm_Region"):
                opp_val = getattr(old_value, "y2fsm_Region", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "y2fsm_Region"):
                opp_val = getattr(value, "y2fsm_Region", None)
                if opp_val is None:
                    setattr(value, "y2fsm_Region", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def y2fsm_AbstractState4(self):
        return self.__y2fsm_AbstractState4

    @y2fsm_AbstractState4.setter
    def y2fsm_AbstractState4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_y2fsm_AbstractState__y2fsm_AbstractState4", None)
        self.__y2fsm_AbstractState4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "y2fsm_Foo5"):
                opp_val = getattr(old_value, "y2fsm_Foo5", None)
                if opp_val == self:
                    setattr(old_value, "y2fsm_Foo5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "y2fsm_Foo5"):
                opp_val = getattr(value, "y2fsm_Foo5", None)
                setattr(value, "y2fsm_Foo5", self)
