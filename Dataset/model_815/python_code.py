from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsm_Transition:

    def __init__(self, input: str, output: str, 8: "fsm_State" = None, 11: "fsm_State" = None, 16: "fsm_State" = None, 4: "fsm_FSM" = None, 19: "fsm_State" = None, 22: "fsm_FSM" = None):
        self.input = input
        self.output = output
        self.8 = 8
        self.11 = 11
        self.16 = 16
        self.4 = 4
        self.19 = 19
        self.22 = 22
        
    @property
    def output(self) -> str:
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output

    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

    @property
    def 19(self):
        return self.__19

    @19.setter
    def 19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__19", None)
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
    def 4(self):
        return self.__4

    @4.setter
    def 4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__4", None)
        self.__4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "3"):
                opp_val = getattr(old_value, "3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "3"):
                opp_val = getattr(value, "3", None)
                if opp_val is None:
                    setattr(value, "3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 11(self):
        return self.__11

    @11.setter
    def 11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__11", None)
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

    @property
    def 16(self):
        return self.__16

    @16.setter
    def 16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__16", None)
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
    def 8(self):
        return self.__8

    @8.setter
    def 8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__8", None)
        self.__8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "7"):
                opp_val = getattr(old_value, "7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "7"):
                opp_val = getattr(value, "7", None)
                if opp_val is None:
                    setattr(value, "7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 22(self):
        return self.__22

    @22.setter
    def 22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__22", None)
        self.__22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "23"):
                opp_val = getattr(old_value, "23", None)
                if opp_val == self:
                    setattr(old_value, "23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "23"):
                opp_val = getattr(value, "23", None)
                setattr(value, "23", self)

class fsm_State:

    def __init__(self, name: str, fsm_State: "fsm_FSM" = None, 7: set["fsm_Transition"] = None, 10: set["fsm_Transition"] = None, 13: "fsm_FSM" = None, 17: "fsm_Transition" = None, 1: "fsm_FSM" = None, 20: "fsm_Transition" = None):
        self.name = name
        self.fsm_State = fsm_State
        self.7 = 7 if 7 is not None else set()
        self.10 = 10 if 10 is not None else set()
        self.13 = 13
        self.17 = 17
        self.1 = 1
        self.20 = 20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 10(self):
        return self.__10

    @10.setter
    def 10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__10", None)
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
    def 13(self):
        return self.__13

    @13.setter
    def 13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__13", None)
        self.__13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "14"):
                opp_val = getattr(old_value, "14", None)
                if opp_val == self:
                    setattr(old_value, "14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "14"):
                opp_val = getattr(value, "14", None)
                setattr(value, "14", self)

    @property
    def 20(self):
        return self.__20

    @20.setter
    def 20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__20", None)
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

    @property
    def fsm_State(self):
        return self.__fsm_State

    @fsm_State.setter
    def fsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State", None)
        self.__fsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_FSM"):
                opp_val = getattr(old_value, "fsm_FSM", None)
                if opp_val == self:
                    setattr(old_value, "fsm_FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSM"):
                opp_val = getattr(value, "fsm_FSM", None)
                setattr(value, "fsm_FSM", self)

    @property
    def 17(self):
        return self.__17

    @17.setter
    def 17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__17", None)
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
    def 7(self):
        return self.__7

    @7.setter
    def 7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__7", None)
        self.__7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "8"):
                    opp_val = getattr(item, "8", None)
                    
                    if opp_val == self:
                        setattr(item, "8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "8"):
                    opp_val = getattr(item, "8", None)
                    
                    setattr(item, "8", self)
                    

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__1", None)
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

class fsm_FSM:

    def __init__(self, name: str, fsm_FSM: "fsm_State" = None, 14: "fsm_State" = None, : set["fsm_State"] = None, 3: set["fsm_Transition"] = None, 23: "fsm_Transition" = None):
        self.name = name
        self.fsm_FSM = fsm_FSM
        self.14 = 14
        self. =  if  is not None else set()
        self.3 = 3 if 3 is not None else set()
        self.23 = 23
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 14(self):
        return self.__14

    @14.setter
    def 14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__14", None)
        self.__14 = value
        
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
    def 3(self):
        return self.__3

    @3.setter
    def 3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__3", None)
        self.__3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "4"):
                    opp_val = getattr(item, "4", None)
                    
                    if opp_val == self:
                        setattr(item, "4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "4"):
                    opp_val = getattr(item, "4", None)
                    
                    setattr(item, "4", self)
                    

    @property
    def fsm_FSM(self):
        return self.__fsm_FSM

    @fsm_FSM.setter
    def fsm_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm_FSM", None)
        self.__fsm_FSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State"):
                opp_val = getattr(old_value, "fsm_State", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State"):
                opp_val = getattr(value, "fsm_State", None)
                setattr(value, "fsm_State", self)

    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__", None)
        self.__ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "1"):
                    opp_val = getattr(item, "1", None)
                    
                    if opp_val == self:
                        setattr(item, "1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "1"):
                    opp_val = getattr(item, "1", None)
                    
                    setattr(item, "1", self)
                    

    @property
    def 23(self):
        return self.__23

    @23.setter
    def 23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__23", None)
        self.__23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "22"):
                opp_val = getattr(old_value, "22", None)
                if opp_val == self:
                    setattr(old_value, "22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "22"):
                opp_val = getattr(value, "22", None)
                setattr(value, "22", self)
