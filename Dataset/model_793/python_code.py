from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class timedfsm_Transition:

    def __init__(self, input: str, output: str, waitingTime: int, 11: "timedfsm_State" = None, 14: "timedfsm_State" = None, 16: "timedfsm_State" = None, 19: "timedfsm_State" = None):
        self.input = input
        self.output = output
        self.waitingTime = waitingTime
        self.11 = 11
        self.14 = 14
        self.16 = 16
        self.19 = 19
        
    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

    @property
    def waitingTime(self) -> int:
        return self.__waitingTime

    @waitingTime.setter
    def waitingTime(self, waitingTime: int):
        self.__waitingTime = waitingTime

    @property
    def output(self) -> str:
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output

    @property
    def 16(self):
        return self.__16

    @16.setter
    def 16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedfsm_Transition__16", None)
        self.__16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "17"):
                opp_val = getattr(old_value, "17", None)
                if opp_val == self:
                    setattr(old_value, "17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "17"):
                opp_val = getattr(value, "17", None)
                setattr(value, "17", self)

    @property
    def 19(self):
        return self.__19

    @19.setter
    def 19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedfsm_Transition__19", None)
        self.__19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "20"):
                opp_val = getattr(old_value, "20", None)
                if opp_val == self:
                    setattr(old_value, "20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "20"):
                opp_val = getattr(value, "20", None)
                setattr(value, "20", self)

    @property
    def 14(self):
        return self.__14

    @14.setter
    def 14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedfsm_Transition__14", None)
        self.__14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "13"):
                opp_val = getattr(old_value, "13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "13"):
                opp_val = getattr(value, "13", None)
                if opp_val is None:
                    setattr(value, "13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 11(self):
        return self.__11

    @11.setter
    def 11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedfsm_Transition__11", None)
        self.__11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "10"):
                opp_val = getattr(old_value, "10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "10"):
                opp_val = getattr(value, "10", None)
                if opp_val is None:
                    setattr(value, "10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class timedfsm_State:

    def __init__(self, name: str, waitingTime: int, 1: "timedfsm_FSM" = None, timedfsm_State: "timedfsm_FSM" = None, timedfsm_State5: "timedfsm_FSM" = None, 7: "timedfsm_FSM" = None, 10: set["timedfsm_Transition"] = None, 13: set["timedfsm_Transition"] = None, 17: "timedfsm_Transition" = None, 20: "timedfsm_Transition" = None):
        self.name = name
        self.waitingTime = waitingTime
        self.1 = 1
        self.timedfsm_State = timedfsm_State
        self.timedfsm_State5 = timedfsm_State5
        self.7 = 7
        self.10 = 10 if 10 is not None else set()
        self.13 = 13 if 13 is not None else set()
        self.17 = 17
        self.20 = 20
        
    @property
    def waitingTime(self) -> int:
        return self.__waitingTime

    @waitingTime.setter
    def waitingTime(self, waitingTime: int):
        self.__waitingTime = waitingTime

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 17(self):
        return self.__17

    @17.setter
    def 17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedfsm_State__17", None)
        self.__17 = value
        
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
    def 13(self):
        return self.__13

    @13.setter
    def 13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedfsm_State__13", None)
        self.__13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "14"):
                    opp_val = getattr(item, "14", None)
                    
                    if opp_val == self:
                        setattr(item, "14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "14"):
                    opp_val = getattr(item, "14", None)
                    
                    setattr(item, "14", self)
                    

    @property
    def timedfsm_State(self):
        return self.__timedfsm_State

    @timedfsm_State.setter
    def timedfsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedfsm_State__timedfsm_State", None)
        self.__timedfsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "timedfsm_FSM"):
                opp_val = getattr(old_value, "timedfsm_FSM", None)
                if opp_val == self:
                    setattr(old_value, "timedfsm_FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "timedfsm_FSM"):
                opp_val = getattr(value, "timedfsm_FSM", None)
                setattr(value, "timedfsm_FSM", self)

    @property
    def 7(self):
        return self.__7

    @7.setter
    def 7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedfsm_State__7", None)
        self.__7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "8"):
                opp_val = getattr(old_value, "8", None)
                if opp_val == self:
                    setattr(old_value, "8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "8"):
                opp_val = getattr(value, "8", None)
                setattr(value, "8", self)

    @property
    def timedfsm_State5(self):
        return self.__timedfsm_State5

    @timedfsm_State5.setter
    def timedfsm_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedfsm_State__timedfsm_State5", None)
        self.__timedfsm_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "timedfsm_FSM4"):
                opp_val = getattr(old_value, "timedfsm_FSM4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "timedfsm_FSM4"):
                opp_val = getattr(value, "timedfsm_FSM4", None)
                if opp_val is None:
                    setattr(value, "timedfsm_FSM4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 10(self):
        return self.__10

    @10.setter
    def 10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedfsm_State__10", None)
        self.__10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "11"):
                    opp_val = getattr(item, "11", None)
                    
                    if opp_val == self:
                        setattr(item, "11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "11"):
                    opp_val = getattr(item, "11", None)
                    
                    setattr(item, "11", self)
                    

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedfsm_State__1", None)
        self.__1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                if opp_val is None:
                    setattr(value, "", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 20(self):
        return self.__20

    @20.setter
    def 20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedfsm_State__20", None)
        self.__20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "19"):
                opp_val = getattr(old_value, "19", None)
                if opp_val == self:
                    setattr(old_value, "19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "19"):
                opp_val = getattr(value, "19", None)
                setattr(value, "19", self)

class timedfsm_FSM:

    pass