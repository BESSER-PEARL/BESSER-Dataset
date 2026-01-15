from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class k3fsm_Transition:

    def __init__(self, input: str, name: str, output: str, 22: "k3fsm_State" = None, 11: "k3fsm_State" = None, 14: "k3fsm_State" = None, 19: "k3fsm_State" = None):
        self.input = input
        self.name = name
        self.output = output
        self.22 = 22
        self.11 = 11
        self.14 = 14
        self.19 = 19
        
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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 11(self):
        return self.__11

    @11.setter
    def 11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_Transition__11", None)
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
    def 22(self):
        return self.__22

    @22.setter
    def 22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_Transition__22", None)
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

    @property
    def 14(self):
        return self.__14

    @14.setter
    def 14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_Transition__14", None)
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
    def 19(self):
        return self.__19

    @19.setter
    def 19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_Transition__19", None)
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

class k3fsm_State:

    def __init__(self, name: str, 1: "k3fsm_FSM" = None, k3fsm_State: "k3fsm_FSM" = None, k3fsm_State5: "k3fsm_FSM" = None, k3fsm_State8: "k3fsm_FSM" = None, 23: "k3fsm_Transition" = None, 10: set["k3fsm_Transition"] = None, 13: set["k3fsm_Transition"] = None, 16: "k3fsm_FSM" = None, 20: "k3fsm_Transition" = None):
        self.name = name
        self.1 = 1
        self.k3fsm_State = k3fsm_State
        self.k3fsm_State5 = k3fsm_State5
        self.k3fsm_State8 = k3fsm_State8
        self.23 = 23
        self.10 = 10 if 10 is not None else set()
        self.13 = 13 if 13 is not None else set()
        self.16 = 16
        self.20 = 20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 23(self):
        return self.__23

    @23.setter
    def 23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_State__23", None)
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

    @property
    def 20(self):
        return self.__20

    @20.setter
    def 20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_State__20", None)
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
    def k3fsm_State(self):
        return self.__k3fsm_State

    @k3fsm_State.setter
    def k3fsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_State__k3fsm_State", None)
        self.__k3fsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k3fsm_FSM"):
                opp_val = getattr(old_value, "k3fsm_FSM", None)
                if opp_val == self:
                    setattr(old_value, "k3fsm_FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k3fsm_FSM"):
                opp_val = getattr(value, "k3fsm_FSM", None)
                setattr(value, "k3fsm_FSM", self)

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_State__1", None)
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
    def k3fsm_State8(self):
        return self.__k3fsm_State8

    @k3fsm_State8.setter
    def k3fsm_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_State__k3fsm_State8", None)
        self.__k3fsm_State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k3fsm_FSM7"):
                opp_val = getattr(old_value, "k3fsm_FSM7", None)
                if opp_val == self:
                    setattr(old_value, "k3fsm_FSM7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k3fsm_FSM7"):
                opp_val = getattr(value, "k3fsm_FSM7", None)
                setattr(value, "k3fsm_FSM7", self)

    @property
    def 16(self):
        return self.__16

    @16.setter
    def 16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_State__16", None)
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
    def 10(self):
        return self.__10

    @10.setter
    def 10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_State__10", None)
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
        old_value = getattr(self, f"_k3fsm_State__13", None)
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
    def k3fsm_State5(self):
        return self.__k3fsm_State5

    @k3fsm_State5.setter
    def k3fsm_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_State__k3fsm_State5", None)
        self.__k3fsm_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k3fsm_FSM4"):
                opp_val = getattr(old_value, "k3fsm_FSM4", None)
                if opp_val == self:
                    setattr(old_value, "k3fsm_FSM4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k3fsm_FSM4"):
                opp_val = getattr(value, "k3fsm_FSM4", None)
                setattr(value, "k3fsm_FSM4", self)

class k3fsm_FSM:

    def __init__(self, name: str, unprocessedString: str, consummedString: str, producedString: str, : set["k3fsm_State"] = None, k3fsm_FSM: "k3fsm_State" = None, k3fsm_FSM4: "k3fsm_State" = None, k3fsm_FSM7: "k3fsm_State" = None, 17: "k3fsm_State" = None):
        self.name = name
        self.unprocessedString = unprocessedString
        self.consummedString = consummedString
        self.producedString = producedString
        self. =  if  is not None else set()
        self.k3fsm_FSM = k3fsm_FSM
        self.k3fsm_FSM4 = k3fsm_FSM4
        self.k3fsm_FSM7 = k3fsm_FSM7
        self.17 = 17
        
    @property
    def consummedString(self) -> str:
        return self.__consummedString

    @consummedString.setter
    def consummedString(self, consummedString: str):
        self.__consummedString = consummedString

    @property
    def producedString(self) -> str:
        return self.__producedString

    @producedString.setter
    def producedString(self, producedString: str):
        self.__producedString = producedString

    @property
    def unprocessedString(self) -> str:
        return self.__unprocessedString

    @unprocessedString.setter
    def unprocessedString(self, unprocessedString: str):
        self.__unprocessedString = unprocessedString

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def k3fsm_FSM4(self):
        return self.__k3fsm_FSM4

    @k3fsm_FSM4.setter
    def k3fsm_FSM4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_FSM__k3fsm_FSM4", None)
        self.__k3fsm_FSM4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k3fsm_State5"):
                opp_val = getattr(old_value, "k3fsm_State5", None)
                if opp_val == self:
                    setattr(old_value, "k3fsm_State5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k3fsm_State5"):
                opp_val = getattr(value, "k3fsm_State5", None)
                setattr(value, "k3fsm_State5", self)

    @property
    def 17(self):
        return self.__17

    @17.setter
    def 17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_FSM__17", None)
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
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_FSM__", None)
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
    def k3fsm_FSM7(self):
        return self.__k3fsm_FSM7

    @k3fsm_FSM7.setter
    def k3fsm_FSM7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_FSM__k3fsm_FSM7", None)
        self.__k3fsm_FSM7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k3fsm_State8"):
                opp_val = getattr(old_value, "k3fsm_State8", None)
                if opp_val == self:
                    setattr(old_value, "k3fsm_State8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k3fsm_State8"):
                opp_val = getattr(value, "k3fsm_State8", None)
                setattr(value, "k3fsm_State8", self)

    @property
    def k3fsm_FSM(self):
        return self.__k3fsm_FSM

    @k3fsm_FSM.setter
    def k3fsm_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_FSM__k3fsm_FSM", None)
        self.__k3fsm_FSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k3fsm_State"):
                opp_val = getattr(old_value, "k3fsm_State", None)
                if opp_val == self:
                    setattr(old_value, "k3fsm_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k3fsm_State"):
                opp_val = getattr(value, "k3fsm_State", None)
                setattr(value, "k3fsm_State", self)
