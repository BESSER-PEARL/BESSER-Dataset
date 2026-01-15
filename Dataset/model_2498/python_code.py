from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class y3fsm_Foo:

    def __init__(self, zoo: str, y3fsm_Foo5: "y3fsm_AbstractState" = None, y3fsm_Foo: "y3fsm_AbstractState" = None):
        self.zoo = zoo
        self.y3fsm_Foo5 = y3fsm_Foo5
        self.y3fsm_Foo = y3fsm_Foo
        
    @property
    def zoo(self) -> str:
        return self.__zoo

    @zoo.setter
    def zoo(self, zoo: str):
        self.__zoo = zoo

    @property
    def y3fsm_Foo5(self):
        return self.__y3fsm_Foo5

    @y3fsm_Foo5.setter
    def y3fsm_Foo5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_y3fsm_Foo__y3fsm_Foo5", None)
        self.__y3fsm_Foo5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "y3fsm_AbstractState4"):
                opp_val = getattr(old_value, "y3fsm_AbstractState4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "y3fsm_AbstractState4"):
                opp_val = getattr(value, "y3fsm_AbstractState4", None)
                if opp_val is None:
                    setattr(value, "y3fsm_AbstractState4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def y3fsm_Foo(self):
        return self.__y3fsm_Foo

    @y3fsm_Foo.setter
    def y3fsm_Foo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_y3fsm_Foo__y3fsm_Foo", None)
        self.__y3fsm_Foo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "y3fsm_AbstractState2"):
                opp_val = getattr(old_value, "y3fsm_AbstractState2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "y3fsm_AbstractState2"):
                opp_val = getattr(value, "y3fsm_AbstractState2", None)
                if opp_val is None:
                    setattr(value, "y3fsm_AbstractState2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class y3fsm_AbstractState(ABC):

    def __init__(self, id: str, y3fsm_AbstractState: "y3fsm_Region" = None, y3fsm_AbstractState4: set["y3fsm_Foo"] = None, y3fsm_AbstractState2: set["y3fsm_Foo"] = None):
        self.id = id
        self.y3fsm_AbstractState = y3fsm_AbstractState
        self.y3fsm_AbstractState4 = y3fsm_AbstractState4 if y3fsm_AbstractState4 is not None else set()
        self.y3fsm_AbstractState2 = y3fsm_AbstractState2 if y3fsm_AbstractState2 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def y3fsm_AbstractState4(self):
        return self.__y3fsm_AbstractState4

    @y3fsm_AbstractState4.setter
    def y3fsm_AbstractState4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_y3fsm_AbstractState__y3fsm_AbstractState4", None)
        self.__y3fsm_AbstractState4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "y3fsm_Foo5"):
                    opp_val = getattr(item, "y3fsm_Foo5", None)
                    
                    if opp_val == self:
                        setattr(item, "y3fsm_Foo5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "y3fsm_Foo5"):
                    opp_val = getattr(item, "y3fsm_Foo5", None)
                    
                    setattr(item, "y3fsm_Foo5", self)
                    

    @property
    def y3fsm_AbstractState2(self):
        return self.__y3fsm_AbstractState2

    @y3fsm_AbstractState2.setter
    def y3fsm_AbstractState2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_y3fsm_AbstractState__y3fsm_AbstractState2", None)
        self.__y3fsm_AbstractState2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "y3fsm_Foo"):
                    opp_val = getattr(item, "y3fsm_Foo", None)
                    
                    if opp_val == self:
                        setattr(item, "y3fsm_Foo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "y3fsm_Foo"):
                    opp_val = getattr(item, "y3fsm_Foo", None)
                    
                    setattr(item, "y3fsm_Foo", self)
                    

    @property
    def y3fsm_AbstractState(self):
        return self.__y3fsm_AbstractState

    @y3fsm_AbstractState.setter
    def y3fsm_AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_y3fsm_AbstractState__y3fsm_AbstractState", None)
        self.__y3fsm_AbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "y3fsm_Region"):
                opp_val = getattr(old_value, "y3fsm_Region", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "y3fsm_Region"):
                opp_val = getattr(value, "y3fsm_Region", None)
                if opp_val is None:
                    setattr(value, "y3fsm_Region", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractState:

    pass
class y3fsm_Region(AbstractState):

    def __init__(self, name: str, y3fsm_Region: set["y3fsm_AbstractState"] = None):
        self.name = name
        self.y3fsm_Region = y3fsm_Region if y3fsm_Region is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def y3fsm_Region(self):
        return self.__y3fsm_Region

    @y3fsm_Region.setter
    def y3fsm_Region(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_y3fsm_Region__y3fsm_Region", None)
        self.__y3fsm_Region = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "y3fsm_AbstractState"):
                    opp_val = getattr(item, "y3fsm_AbstractState", None)
                    
                    if opp_val == self:
                        setattr(item, "y3fsm_AbstractState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "y3fsm_AbstractState"):
                    opp_val = getattr(item, "y3fsm_AbstractState", None)
                    
                    setattr(item, "y3fsm_AbstractState", self)
                    
