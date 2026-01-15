from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class sm_State:

    def __init__(self, name: str, sm_State4: "sm_StateMachine" = None, sm_State7: "sm_StateMachine" = None, sm_State11: set["sm_StateMachine"] = None, sm_State15: "sm_Transition" = None, sm_State18: "sm_Transition" = None, sm_State: "sm_StateMachine" = None):
        self.name = name
        self.sm_State4 = sm_State4
        self.sm_State7 = sm_State7
        self.sm_State11 = sm_State11 if sm_State11 is not None else set()
        self.sm_State15 = sm_State15
        self.sm_State18 = sm_State18
        self.sm_State = sm_State
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sm_State7(self):
        return self.__sm_State7

    @sm_State7.setter
    def sm_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__sm_State7", None)
        self.__sm_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_StateMachine6"):
                opp_val = getattr(old_value, "sm_StateMachine6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_StateMachine6"):
                opp_val = getattr(value, "sm_StateMachine6", None)
                if opp_val is None:
                    setattr(value, "sm_StateMachine6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sm_State18(self):
        return self.__sm_State18

    @sm_State18.setter
    def sm_State18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__sm_State18", None)
        self.__sm_State18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_Transition17"):
                opp_val = getattr(old_value, "sm_Transition17", None)
                if opp_val == self:
                    setattr(old_value, "sm_Transition17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_Transition17"):
                opp_val = getattr(value, "sm_Transition17", None)
                setattr(value, "sm_Transition17", self)

    @property
    def sm_State11(self):
        return self.__sm_State11

    @sm_State11.setter
    def sm_State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__sm_State11", None)
        self.__sm_State11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sm_StateMachine12"):
                    opp_val = getattr(item, "sm_StateMachine12", None)
                    
                    if opp_val == self:
                        setattr(item, "sm_StateMachine12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sm_StateMachine12"):
                    opp_val = getattr(item, "sm_StateMachine12", None)
                    
                    setattr(item, "sm_StateMachine12", self)
                    

    @property
    def sm_State4(self):
        return self.__sm_State4

    @sm_State4.setter
    def sm_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__sm_State4", None)
        self.__sm_State4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_StateMachine3"):
                opp_val = getattr(old_value, "sm_StateMachine3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_StateMachine3"):
                opp_val = getattr(value, "sm_StateMachine3", None)
                if opp_val is None:
                    setattr(value, "sm_StateMachine3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sm_State(self):
        return self.__sm_State

    @sm_State.setter
    def sm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__sm_State", None)
        self.__sm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_StateMachine"):
                opp_val = getattr(old_value, "sm_StateMachine", None)
                if opp_val == self:
                    setattr(old_value, "sm_StateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_StateMachine"):
                opp_val = getattr(value, "sm_StateMachine", None)
                setattr(value, "sm_StateMachine", self)

    @property
    def sm_State15(self):
        return self.__sm_State15

    @sm_State15.setter
    def sm_State15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__sm_State15", None)
        self.__sm_State15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_Transition14"):
                opp_val = getattr(old_value, "sm_Transition14", None)
                if opp_val == self:
                    setattr(old_value, "sm_Transition14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_Transition14"):
                opp_val = getattr(value, "sm_Transition14", None)
                setattr(value, "sm_Transition14", self)

class sm_StateMachine:

    def __init__(self, name: str, sm_StateMachine3: set["sm_State"] = None, sm_StateMachine6: set["sm_State"] = None, sm_StateMachine9: set["sm_Transition"] = None, sm_StateMachine12: "sm_State" = None, sm_StateMachine: "sm_State" = None):
        self.name = name
        self.sm_StateMachine3 = sm_StateMachine3 if sm_StateMachine3 is not None else set()
        self.sm_StateMachine6 = sm_StateMachine6 if sm_StateMachine6 is not None else set()
        self.sm_StateMachine9 = sm_StateMachine9 if sm_StateMachine9 is not None else set()
        self.sm_StateMachine12 = sm_StateMachine12
        self.sm_StateMachine = sm_StateMachine
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sm_StateMachine12(self):
        return self.__sm_StateMachine12

    @sm_StateMachine12.setter
    def sm_StateMachine12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__sm_StateMachine12", None)
        self.__sm_StateMachine12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_State11"):
                opp_val = getattr(old_value, "sm_State11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_State11"):
                opp_val = getattr(value, "sm_State11", None)
                if opp_val is None:
                    setattr(value, "sm_State11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sm_StateMachine6(self):
        return self.__sm_StateMachine6

    @sm_StateMachine6.setter
    def sm_StateMachine6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__sm_StateMachine6", None)
        self.__sm_StateMachine6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sm_State7"):
                    opp_val = getattr(item, "sm_State7", None)
                    
                    if opp_val == self:
                        setattr(item, "sm_State7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sm_State7"):
                    opp_val = getattr(item, "sm_State7", None)
                    
                    setattr(item, "sm_State7", self)
                    

    @property
    def sm_StateMachine(self):
        return self.__sm_StateMachine

    @sm_StateMachine.setter
    def sm_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__sm_StateMachine", None)
        self.__sm_StateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_State"):
                opp_val = getattr(old_value, "sm_State", None)
                if opp_val == self:
                    setattr(old_value, "sm_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_State"):
                opp_val = getattr(value, "sm_State", None)
                setattr(value, "sm_State", self)

    @property
    def sm_StateMachine9(self):
        return self.__sm_StateMachine9

    @sm_StateMachine9.setter
    def sm_StateMachine9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__sm_StateMachine9", None)
        self.__sm_StateMachine9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sm_Transition"):
                    opp_val = getattr(item, "sm_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "sm_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sm_Transition"):
                    opp_val = getattr(item, "sm_Transition", None)
                    
                    setattr(item, "sm_Transition", self)
                    

    @property
    def sm_StateMachine3(self):
        return self.__sm_StateMachine3

    @sm_StateMachine3.setter
    def sm_StateMachine3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__sm_StateMachine3", None)
        self.__sm_StateMachine3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sm_State4"):
                    opp_val = getattr(item, "sm_State4", None)
                    
                    if opp_val == self:
                        setattr(item, "sm_State4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sm_State4"):
                    opp_val = getattr(item, "sm_State4", None)
                    
                    setattr(item, "sm_State4", self)
                    

class sm_Transition:

    def __init__(self, name: str, sm_Transition: "sm_StateMachine" = None, sm_Transition14: "sm_State" = None, sm_Transition17: "sm_State" = None):
        self.name = name
        self.sm_Transition = sm_Transition
        self.sm_Transition14 = sm_Transition14
        self.sm_Transition17 = sm_Transition17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sm_Transition14(self):
        return self.__sm_Transition14

    @sm_Transition14.setter
    def sm_Transition14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Transition__sm_Transition14", None)
        self.__sm_Transition14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_State15"):
                opp_val = getattr(old_value, "sm_State15", None)
                if opp_val == self:
                    setattr(old_value, "sm_State15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_State15"):
                opp_val = getattr(value, "sm_State15", None)
                setattr(value, "sm_State15", self)

    @property
    def sm_Transition17(self):
        return self.__sm_Transition17

    @sm_Transition17.setter
    def sm_Transition17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Transition__sm_Transition17", None)
        self.__sm_Transition17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_State18"):
                opp_val = getattr(old_value, "sm_State18", None)
                if opp_val == self:
                    setattr(old_value, "sm_State18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_State18"):
                opp_val = getattr(value, "sm_State18", None)
                setattr(value, "sm_State18", self)

    @property
    def sm_Transition(self):
        return self.__sm_Transition

    @sm_Transition.setter
    def sm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Transition__sm_Transition", None)
        self.__sm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_StateMachine9"):
                opp_val = getattr(old_value, "sm_StateMachine9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_StateMachine9"):
                opp_val = getattr(value, "sm_StateMachine9", None)
                if opp_val is None:
                    setattr(value, "sm_StateMachine9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sm_Event:

    def __init__(self, name: str, sm_Event: "sm_sm_Transition" = None):
        self.name = name
        self.sm_Event = sm_Event
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sm_Event(self):
        return self.__sm_Event

    @sm_Event.setter
    def sm_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Event__sm_Event", None)
        self.__sm_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_sm_Transition"):
                opp_val = getattr(old_value, "sm_sm_Transition", None)
                if opp_val == self:
                    setattr(old_value, "sm_sm_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_sm_Transition"):
                opp_val = getattr(value, "sm_sm_Transition", None)
                setattr(value, "sm_sm_Transition", self)

class Transition:

    pass
class sm_sm_Transition(Transition):

    pass
class State:

    pass
class sm_sm_State(State):

    pass
class StateMachine:

    pass
class sm_sm_StateMachine(StateMachine):

    pass