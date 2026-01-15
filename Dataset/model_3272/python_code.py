from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class sm_Transition:

    def __init__(self, name: str, sm_Transition16: "sm_State" = None, sm_Transition: "sm_StateMachine" = None, sm_Transition13: "sm_State" = None):
        self.name = name
        self.sm_Transition16 = sm_Transition16
        self.sm_Transition = sm_Transition
        self.sm_Transition13 = sm_Transition13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "sm_StateMachine8"):
                opp_val = getattr(old_value, "sm_StateMachine8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_StateMachine8"):
                opp_val = getattr(value, "sm_StateMachine8", None)
                if opp_val is None:
                    setattr(value, "sm_StateMachine8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sm_Transition13(self):
        return self.__sm_Transition13

    @sm_Transition13.setter
    def sm_Transition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Transition__sm_Transition13", None)
        self.__sm_Transition13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_State14"):
                opp_val = getattr(old_value, "sm_State14", None)
                if opp_val == self:
                    setattr(old_value, "sm_State14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_State14"):
                opp_val = getattr(value, "sm_State14", None)
                setattr(value, "sm_State14", self)

    @property
    def sm_Transition16(self):
        return self.__sm_Transition16

    @sm_Transition16.setter
    def sm_Transition16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Transition__sm_Transition16", None)
        self.__sm_Transition16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_State17"):
                opp_val = getattr(old_value, "sm_State17", None)
                if opp_val == self:
                    setattr(old_value, "sm_State17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_State17"):
                opp_val = getattr(value, "sm_State17", None)
                setattr(value, "sm_State17", self)

class sm_State:

    def __init__(self, name: str, sm_State17: "sm_Transition" = None, sm_State: "sm_StateMachine" = None, sm_State3: "sm_StateMachine" = None, sm_State6: "sm_StateMachine" = None, sm_State10: set["sm_StateMachine"] = None, sm_State14: "sm_Transition" = None):
        self.name = name
        self.sm_State17 = sm_State17
        self.sm_State = sm_State
        self.sm_State3 = sm_State3
        self.sm_State6 = sm_State6
        self.sm_State10 = sm_State10 if sm_State10 is not None else set()
        self.sm_State14 = sm_State14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sm_State6(self):
        return self.__sm_State6

    @sm_State6.setter
    def sm_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__sm_State6", None)
        self.__sm_State6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_StateMachine5"):
                opp_val = getattr(old_value, "sm_StateMachine5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_StateMachine5"):
                opp_val = getattr(value, "sm_StateMachine5", None)
                if opp_val is None:
                    setattr(value, "sm_StateMachine5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sm_State3(self):
        return self.__sm_State3

    @sm_State3.setter
    def sm_State3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__sm_State3", None)
        self.__sm_State3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_StateMachine2"):
                opp_val = getattr(old_value, "sm_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_StateMachine2"):
                opp_val = getattr(value, "sm_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "sm_StateMachine2", set([self]))
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
    def sm_State10(self):
        return self.__sm_State10

    @sm_State10.setter
    def sm_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__sm_State10", None)
        self.__sm_State10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sm_StateMachine11"):
                    opp_val = getattr(item, "sm_StateMachine11", None)
                    
                    if opp_val == self:
                        setattr(item, "sm_StateMachine11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sm_StateMachine11"):
                    opp_val = getattr(item, "sm_StateMachine11", None)
                    
                    setattr(item, "sm_StateMachine11", self)
                    

    @property
    def sm_State14(self):
        return self.__sm_State14

    @sm_State14.setter
    def sm_State14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__sm_State14", None)
        self.__sm_State14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_Transition13"):
                opp_val = getattr(old_value, "sm_Transition13", None)
                if opp_val == self:
                    setattr(old_value, "sm_Transition13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_Transition13"):
                opp_val = getattr(value, "sm_Transition13", None)
                setattr(value, "sm_Transition13", self)

    @property
    def sm_State17(self):
        return self.__sm_State17

    @sm_State17.setter
    def sm_State17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__sm_State17", None)
        self.__sm_State17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_Transition16"):
                opp_val = getattr(old_value, "sm_Transition16", None)
                if opp_val == self:
                    setattr(old_value, "sm_Transition16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_Transition16"):
                opp_val = getattr(value, "sm_Transition16", None)
                setattr(value, "sm_Transition16", self)

class sm_StateMachine:

    def __init__(self, name: str, sm_StateMachine: "sm_State" = None, sm_StateMachine2: set["sm_State"] = None, sm_StateMachine5: set["sm_State"] = None, sm_StateMachine8: set["sm_Transition"] = None, sm_StateMachine11: "sm_State" = None):
        self.name = name
        self.sm_StateMachine = sm_StateMachine
        self.sm_StateMachine2 = sm_StateMachine2 if sm_StateMachine2 is not None else set()
        self.sm_StateMachine5 = sm_StateMachine5 if sm_StateMachine5 is not None else set()
        self.sm_StateMachine8 = sm_StateMachine8 if sm_StateMachine8 is not None else set()
        self.sm_StateMachine11 = sm_StateMachine11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sm_StateMachine2(self):
        return self.__sm_StateMachine2

    @sm_StateMachine2.setter
    def sm_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__sm_StateMachine2", None)
        self.__sm_StateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sm_State3"):
                    opp_val = getattr(item, "sm_State3", None)
                    
                    if opp_val == self:
                        setattr(item, "sm_State3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sm_State3"):
                    opp_val = getattr(item, "sm_State3", None)
                    
                    setattr(item, "sm_State3", self)
                    

    @property
    def sm_StateMachine8(self):
        return self.__sm_StateMachine8

    @sm_StateMachine8.setter
    def sm_StateMachine8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__sm_StateMachine8", None)
        self.__sm_StateMachine8 = value if value is not None else set()
        
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
    def sm_StateMachine11(self):
        return self.__sm_StateMachine11

    @sm_StateMachine11.setter
    def sm_StateMachine11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__sm_StateMachine11", None)
        self.__sm_StateMachine11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_State10"):
                opp_val = getattr(old_value, "sm_State10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_State10"):
                opp_val = getattr(value, "sm_State10", None)
                if opp_val is None:
                    setattr(value, "sm_State10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sm_StateMachine5(self):
        return self.__sm_StateMachine5

    @sm_StateMachine5.setter
    def sm_StateMachine5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__sm_StateMachine5", None)
        self.__sm_StateMachine5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sm_State6"):
                    opp_val = getattr(item, "sm_State6", None)
                    
                    if opp_val == self:
                        setattr(item, "sm_State6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sm_State6"):
                    opp_val = getattr(item, "sm_State6", None)
                    
                    setattr(item, "sm_State6", self)
                    

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
