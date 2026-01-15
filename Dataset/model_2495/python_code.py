from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class y5fsm_Bar:

    def __init__(self, baz: str, y5fsm_Bar: "y5fsm_State" = None):
        self.baz = baz
        self.y5fsm_Bar = y5fsm_Bar
        
    @property
    def baz(self) -> str:
        return self.__baz

    @baz.setter
    def baz(self, baz: str):
        self.__baz = baz

    @property
    def y5fsm_Bar(self):
        return self.__y5fsm_Bar

    @y5fsm_Bar.setter
    def y5fsm_Bar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_y5fsm_Bar__y5fsm_Bar", None)
        self.__y5fsm_Bar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "y5fsm_State4"):
                opp_val = getattr(old_value, "y5fsm_State4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "y5fsm_State4"):
                opp_val = getattr(value, "y5fsm_State4", None)
                if opp_val is None:
                    setattr(value, "y5fsm_State4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class y5fsm_Foo:

    def __init__(self, zoo: str, y5fsm_Foo: "y5fsm_State" = None):
        self.zoo = zoo
        self.y5fsm_Foo = y5fsm_Foo
        
    @property
    def zoo(self) -> str:
        return self.__zoo

    @zoo.setter
    def zoo(self, zoo: str):
        self.__zoo = zoo

    @property
    def y5fsm_Foo(self):
        return self.__y5fsm_Foo

    @y5fsm_Foo.setter
    def y5fsm_Foo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_y5fsm_Foo__y5fsm_Foo", None)
        self.__y5fsm_Foo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "y5fsm_State2"):
                opp_val = getattr(old_value, "y5fsm_State2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "y5fsm_State2"):
                opp_val = getattr(value, "y5fsm_State2", None)
                if opp_val is None:
                    setattr(value, "y5fsm_State2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class y5fsm_State:

    def __init__(self, id: str, y5fsm_State: "y5fsm_Region" = None, y5fsm_State2: set["y5fsm_Foo"] = None, y5fsm_State4: set["y5fsm_Bar"] = None):
        self.id = id
        self.y5fsm_State = y5fsm_State
        self.y5fsm_State2 = y5fsm_State2 if y5fsm_State2 is not None else set()
        self.y5fsm_State4 = y5fsm_State4 if y5fsm_State4 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def y5fsm_State2(self):
        return self.__y5fsm_State2

    @y5fsm_State2.setter
    def y5fsm_State2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_y5fsm_State__y5fsm_State2", None)
        self.__y5fsm_State2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "y5fsm_Foo"):
                    opp_val = getattr(item, "y5fsm_Foo", None)
                    
                    if opp_val == self:
                        setattr(item, "y5fsm_Foo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "y5fsm_Foo"):
                    opp_val = getattr(item, "y5fsm_Foo", None)
                    
                    setattr(item, "y5fsm_Foo", self)
                    

    @property
    def y5fsm_State4(self):
        return self.__y5fsm_State4

    @y5fsm_State4.setter
    def y5fsm_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_y5fsm_State__y5fsm_State4", None)
        self.__y5fsm_State4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "y5fsm_Bar"):
                    opp_val = getattr(item, "y5fsm_Bar", None)
                    
                    if opp_val == self:
                        setattr(item, "y5fsm_Bar", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "y5fsm_Bar"):
                    opp_val = getattr(item, "y5fsm_Bar", None)
                    
                    setattr(item, "y5fsm_Bar", self)
                    

    @property
    def y5fsm_State(self):
        return self.__y5fsm_State

    @y5fsm_State.setter
    def y5fsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_y5fsm_State__y5fsm_State", None)
        self.__y5fsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "y5fsm_Region"):
                opp_val = getattr(old_value, "y5fsm_Region", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "y5fsm_Region"):
                opp_val = getattr(value, "y5fsm_Region", None)
                if opp_val is None:
                    setattr(value, "y5fsm_Region", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class y5fsm_Region:

    pass