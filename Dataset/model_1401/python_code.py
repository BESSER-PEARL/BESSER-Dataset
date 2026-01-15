from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class State:

    pass
class HSM_CompositeState(State):

    pass
class HSM_StateMachine:

    def __init__(self, HSM_StateMachine: set["HSM_State"] = None, HSM_StateMachine2: set["HSM_Transition"] = None):
        self.HSM_StateMachine = HSM_StateMachine if HSM_StateMachine is not None else set()
        self.HSM_StateMachine2 = HSM_StateMachine2 if HSM_StateMachine2 is not None else set()
        
    @property
    def HSM_StateMachine2(self):
        return self.__HSM_StateMachine2

    @HSM_StateMachine2.setter
    def HSM_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_StateMachine__HSM_StateMachine2", None)
        self.__HSM_StateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HSM_Transition"):
                    opp_val = getattr(item, "HSM_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "HSM_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HSM_Transition"):
                    opp_val = getattr(item, "HSM_Transition", None)
                    
                    setattr(item, "HSM_Transition", self)
                    

    @property
    def HSM_StateMachine(self):
        return self.__HSM_StateMachine

    @HSM_StateMachine.setter
    def HSM_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_StateMachine__HSM_StateMachine", None)
        self.__HSM_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HSM_State"):
                    opp_val = getattr(item, "HSM_State", None)
                    
                    if opp_val == self:
                        setattr(item, "HSM_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HSM_State"):
                    opp_val = getattr(item, "HSM_State", None)
                    
                    setattr(item, "HSM_State", self)
                    

    def addTransition(self, trg: str, src: str):
        # TODO: Implement addTransition method
        pass

class HSM_Transition:

    pass
class HSM_State:

    def __init__(self, name: str, HSM_State: "HSM_StateMachine" = None, HSM_State4: "HSM_CompositeState" = None, HSM_State7: "HSM_Transition" = None, HSM_State10: "HSM_Transition" = None):
        self.name = name
        self.HSM_State = HSM_State
        self.HSM_State4 = HSM_State4
        self.HSM_State7 = HSM_State7
        self.HSM_State10 = HSM_State10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def HSM_State10(self):
        return self.__HSM_State10

    @HSM_State10.setter
    def HSM_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_State__HSM_State10", None)
        self.__HSM_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HSM_Transition9"):
                opp_val = getattr(old_value, "HSM_Transition9", None)
                if opp_val == self:
                    setattr(old_value, "HSM_Transition9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HSM_Transition9"):
                opp_val = getattr(value, "HSM_Transition9", None)
                setattr(value, "HSM_Transition9", self)

    @property
    def HSM_State7(self):
        return self.__HSM_State7

    @HSM_State7.setter
    def HSM_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_State__HSM_State7", None)
        self.__HSM_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HSM_Transition6"):
                opp_val = getattr(old_value, "HSM_Transition6", None)
                if opp_val == self:
                    setattr(old_value, "HSM_Transition6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HSM_Transition6"):
                opp_val = getattr(value, "HSM_Transition6", None)
                setattr(value, "HSM_Transition6", self)

    @property
    def HSM_State4(self):
        return self.__HSM_State4

    @HSM_State4.setter
    def HSM_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_State__HSM_State4", None)
        self.__HSM_State4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HSM_CompositeState"):
                opp_val = getattr(old_value, "HSM_CompositeState", None)
                if opp_val == self:
                    setattr(old_value, "HSM_CompositeState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HSM_CompositeState"):
                opp_val = getattr(value, "HSM_CompositeState", None)
                setattr(value, "HSM_CompositeState", self)

    @property
    def HSM_State(self):
        return self.__HSM_State

    @HSM_State.setter
    def HSM_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_State__HSM_State", None)
        self.__HSM_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HSM_StateMachine"):
                opp_val = getattr(old_value, "HSM_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HSM_StateMachine"):
                opp_val = getattr(value, "HSM_StateMachine", None)
                if opp_val is None:
                    setattr(value, "HSM_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
