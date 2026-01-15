from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class gemoc_FSM:

    def __init__(self, name: bool, gemoc_FSM: set["gemoc_State"] = None, gemoc_FSM2: set["gemoc_Transition"] = None, gemoc_FSM10: "gemoc_State" = None):
        self.name = name
        self.gemoc_FSM = gemoc_FSM if gemoc_FSM is not None else set()
        self.gemoc_FSM2 = gemoc_FSM2 if gemoc_FSM2 is not None else set()
        self.gemoc_FSM10 = gemoc_FSM10
        
    @property
    def name(self) -> bool:
        return self.__name

    @name.setter
    def name(self, name: bool):
        self.__name = name

    @property
    def gemoc_FSM(self):
        return self.__gemoc_FSM

    @gemoc_FSM.setter
    def gemoc_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_FSM__gemoc_FSM", None)
        self.__gemoc_FSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gemoc_State"):
                    opp_val = getattr(item, "gemoc_State", None)
                    
                    if opp_val == self:
                        setattr(item, "gemoc_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gemoc_State"):
                    opp_val = getattr(item, "gemoc_State", None)
                    
                    setattr(item, "gemoc_State", self)
                    

    @property
    def gemoc_FSM2(self):
        return self.__gemoc_FSM2

    @gemoc_FSM2.setter
    def gemoc_FSM2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_FSM__gemoc_FSM2", None)
        self.__gemoc_FSM2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gemoc_Transition"):
                    opp_val = getattr(item, "gemoc_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "gemoc_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gemoc_Transition"):
                    opp_val = getattr(item, "gemoc_Transition", None)
                    
                    setattr(item, "gemoc_Transition", self)
                    

    @property
    def gemoc_FSM10(self):
        return self.__gemoc_FSM10

    @gemoc_FSM10.setter
    def gemoc_FSM10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_FSM__gemoc_FSM10", None)
        self.__gemoc_FSM10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gemoc_State9"):
                opp_val = getattr(old_value, "gemoc_State9", None)
                if opp_val == self:
                    setattr(old_value, "gemoc_State9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gemoc_State9"):
                opp_val = getattr(value, "gemoc_State9", None)
                setattr(value, "gemoc_State9", self)

    def main(self):
        # TODO: Implement main method
        pass

    def setCurrentState(self, state: str):
        # TODO: Implement setCurrentState method
        pass

    def initialize(self):
        # TODO: Implement initialize method
        pass

    def print(self):
        # TODO: Implement print method
        pass

class gemoc_Transition:

    def __init__(self, name: str, trigger: str, gemoc_Transition: "gemoc_FSM" = None, 4: "gemoc_State" = None, 7: "gemoc_State" = None, 12: "gemoc_State" = None, 15: "gemoc_State" = None):
        self.name = name
        self.trigger = trigger
        self.gemoc_Transition = gemoc_Transition
        self.4 = 4
        self.7 = 7
        self.12 = 12
        self.15 = 15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def trigger(self) -> str:
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger

    @property
    def 7(self):
        return self.__7

    @7.setter
    def 7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_Transition__7", None)
        self.__7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "6"):
                opp_val = getattr(old_value, "6", None)
                if opp_val == self:
                    setattr(old_value, "6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "6"):
                opp_val = getattr(value, "6", None)
                setattr(value, "6", self)

    @property
    def 4(self):
        return self.__4

    @4.setter
    def 4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_Transition__4", None)
        self.__4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if opp_val == self:
                    setattr(old_value, "", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                setattr(value, "", self)

    @property
    def 15(self):
        return self.__15

    @15.setter
    def 15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_Transition__15", None)
        self.__15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "16"):
                opp_val = getattr(old_value, "16", None)
                if opp_val == self:
                    setattr(old_value, "16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "16"):
                opp_val = getattr(value, "16", None)
                setattr(value, "16", self)

    @property
    def 12(self):
        return self.__12

    @12.setter
    def 12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_Transition__12", None)
        self.__12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "13"):
                opp_val = getattr(old_value, "13", None)
                if opp_val == self:
                    setattr(old_value, "13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "13"):
                opp_val = getattr(value, "13", None)
                setattr(value, "13", self)

    @property
    def gemoc_Transition(self):
        return self.__gemoc_Transition

    @gemoc_Transition.setter
    def gemoc_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_Transition__gemoc_Transition", None)
        self.__gemoc_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gemoc_FSM2"):
                opp_val = getattr(old_value, "gemoc_FSM2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gemoc_FSM2"):
                opp_val = getattr(value, "gemoc_FSM2", None)
                if opp_val is None:
                    setattr(value, "gemoc_FSM2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def fire(self):
        # TODO: Implement fire method
        pass

class gemoc_State:

    def __init__(self, name: str, gemoc_State: "gemoc_FSM" = None, : "gemoc_Transition" = None, 6: "gemoc_Transition" = None, gemoc_State9: "gemoc_FSM" = None, 13: "gemoc_Transition" = None, 16: "gemoc_Transition" = None):
        self.name = name
        self.gemoc_State = gemoc_State
        self. = 
        self.6 = 6
        self.gemoc_State9 = gemoc_State9
        self.13 = 13
        self.16 = 16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gemoc_State(self):
        return self.__gemoc_State

    @gemoc_State.setter
    def gemoc_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_State__gemoc_State", None)
        self.__gemoc_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gemoc_FSM"):
                opp_val = getattr(old_value, "gemoc_FSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gemoc_FSM"):
                opp_val = getattr(value, "gemoc_FSM", None)
                if opp_val is None:
                    setattr(value, "gemoc_FSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_State__", None)
        self.__ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "4"):
                opp_val = getattr(old_value, "4", None)
                if opp_val == self:
                    setattr(old_value, "4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "4"):
                opp_val = getattr(value, "4", None)
                setattr(value, "4", self)

    @property
    def 16(self):
        return self.__16

    @16.setter
    def 16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_State__16", None)
        self.__16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "15"):
                opp_val = getattr(old_value, "15", None)
                if opp_val == self:
                    setattr(old_value, "15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "15"):
                opp_val = getattr(value, "15", None)
                setattr(value, "15", self)

    @property
    def gemoc_State9(self):
        return self.__gemoc_State9

    @gemoc_State9.setter
    def gemoc_State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_State__gemoc_State9", None)
        self.__gemoc_State9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gemoc_FSM10"):
                opp_val = getattr(old_value, "gemoc_FSM10", None)
                if opp_val == self:
                    setattr(old_value, "gemoc_FSM10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gemoc_FSM10"):
                opp_val = getattr(value, "gemoc_FSM10", None)
                setattr(value, "gemoc_FSM10", self)

    @property
    def 6(self):
        return self.__6

    @6.setter
    def 6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_State__6", None)
        self.__6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "7"):
                opp_val = getattr(old_value, "7", None)
                if opp_val == self:
                    setattr(old_value, "7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "7"):
                opp_val = getattr(value, "7", None)
                setattr(value, "7", self)

    @property
    def 13(self):
        return self.__13

    @13.setter
    def 13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gemoc_State__13", None)
        self.__13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "12"):
                opp_val = getattr(old_value, "12", None)
                if opp_val == self:
                    setattr(old_value, "12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "12"):
                opp_val = getattr(value, "12", None)
                setattr(value, "12", self)

    def step(self, inputString: str):
        # TODO: Implement step method
        pass

    def isValidTrigger(self, trigger: str):
        # TODO: Implement isValidTrigger method
        pass
