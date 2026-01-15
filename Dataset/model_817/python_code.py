from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsmSample_State:

    def __init__(self, name: str, fsmSample_State14: set["fsmSample_Transition"] = None, fsmSample_State16: set["fsmSample_Transition"] = None, fsmSample_State20: "fsmSample_Transition" = None, fsmSample_State23: "fsmSample_Transition" = None, fsmSample_State: "fsmSample_FSM" = None, fsmSample_State3: "fsmSample_FSM" = None, fsmSample_State6: "fsmSample_FSM" = None, fsmSample_State9: "fsmSample_FSM" = None, fsmSample_State11: "fsmSample_FSM" = None):
        self.name = name
        self.fsmSample_State14 = fsmSample_State14 if fsmSample_State14 is not None else set()
        self.fsmSample_State16 = fsmSample_State16 if fsmSample_State16 is not None else set()
        self.fsmSample_State20 = fsmSample_State20
        self.fsmSample_State23 = fsmSample_State23
        self.fsmSample_State = fsmSample_State
        self.fsmSample_State3 = fsmSample_State3
        self.fsmSample_State6 = fsmSample_State6
        self.fsmSample_State9 = fsmSample_State9
        self.fsmSample_State11 = fsmSample_State11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsmSample_State9(self):
        return self.__fsmSample_State9

    @fsmSample_State9.setter
    def fsmSample_State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_State__fsmSample_State9", None)
        self.__fsmSample_State9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmSample_FSM8"):
                opp_val = getattr(old_value, "fsmSample_FSM8", None)
                if opp_val == self:
                    setattr(old_value, "fsmSample_FSM8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmSample_FSM8"):
                opp_val = getattr(value, "fsmSample_FSM8", None)
                setattr(value, "fsmSample_FSM8", self)

    @property
    def fsmSample_State3(self):
        return self.__fsmSample_State3

    @fsmSample_State3.setter
    def fsmSample_State3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_State__fsmSample_State3", None)
        self.__fsmSample_State3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmSample_FSM2"):
                opp_val = getattr(old_value, "fsmSample_FSM2", None)
                if opp_val == self:
                    setattr(old_value, "fsmSample_FSM2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmSample_FSM2"):
                opp_val = getattr(value, "fsmSample_FSM2", None)
                setattr(value, "fsmSample_FSM2", self)

    @property
    def fsmSample_State20(self):
        return self.__fsmSample_State20

    @fsmSample_State20.setter
    def fsmSample_State20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_State__fsmSample_State20", None)
        self.__fsmSample_State20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmSample_Transition19"):
                opp_val = getattr(old_value, "fsmSample_Transition19", None)
                if opp_val == self:
                    setattr(old_value, "fsmSample_Transition19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmSample_Transition19"):
                opp_val = getattr(value, "fsmSample_Transition19", None)
                setattr(value, "fsmSample_Transition19", self)

    @property
    def fsmSample_State14(self):
        return self.__fsmSample_State14

    @fsmSample_State14.setter
    def fsmSample_State14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_State__fsmSample_State14", None)
        self.__fsmSample_State14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsmSample_Transition"):
                    opp_val = getattr(item, "fsmSample_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "fsmSample_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsmSample_Transition"):
                    opp_val = getattr(item, "fsmSample_Transition", None)
                    
                    setattr(item, "fsmSample_Transition", self)
                    

    @property
    def fsmSample_State6(self):
        return self.__fsmSample_State6

    @fsmSample_State6.setter
    def fsmSample_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_State__fsmSample_State6", None)
        self.__fsmSample_State6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmSample_FSM5"):
                opp_val = getattr(old_value, "fsmSample_FSM5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmSample_FSM5"):
                opp_val = getattr(value, "fsmSample_FSM5", None)
                if opp_val is None:
                    setattr(value, "fsmSample_FSM5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsmSample_State16(self):
        return self.__fsmSample_State16

    @fsmSample_State16.setter
    def fsmSample_State16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_State__fsmSample_State16", None)
        self.__fsmSample_State16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsmSample_Transition17"):
                    opp_val = getattr(item, "fsmSample_Transition17", None)
                    
                    if opp_val == self:
                        setattr(item, "fsmSample_Transition17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsmSample_Transition17"):
                    opp_val = getattr(item, "fsmSample_Transition17", None)
                    
                    setattr(item, "fsmSample_Transition17", self)
                    

    @property
    def fsmSample_State(self):
        return self.__fsmSample_State

    @fsmSample_State.setter
    def fsmSample_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_State__fsmSample_State", None)
        self.__fsmSample_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmSample_FSM"):
                opp_val = getattr(old_value, "fsmSample_FSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmSample_FSM"):
                opp_val = getattr(value, "fsmSample_FSM", None)
                if opp_val is None:
                    setattr(value, "fsmSample_FSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsmSample_State11(self):
        return self.__fsmSample_State11

    @fsmSample_State11.setter
    def fsmSample_State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_State__fsmSample_State11", None)
        self.__fsmSample_State11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmSample_FSM12"):
                opp_val = getattr(old_value, "fsmSample_FSM12", None)
                if opp_val == self:
                    setattr(old_value, "fsmSample_FSM12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmSample_FSM12"):
                opp_val = getattr(value, "fsmSample_FSM12", None)
                setattr(value, "fsmSample_FSM12", self)

    @property
    def fsmSample_State23(self):
        return self.__fsmSample_State23

    @fsmSample_State23.setter
    def fsmSample_State23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_State__fsmSample_State23", None)
        self.__fsmSample_State23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmSample_Transition22"):
                opp_val = getattr(old_value, "fsmSample_Transition22", None)
                if opp_val == self:
                    setattr(old_value, "fsmSample_Transition22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmSample_Transition22"):
                opp_val = getattr(value, "fsmSample_Transition22", None)
                setattr(value, "fsmSample_Transition22", self)

class fsmSample_FSM:

    def __init__(self, name: str, fsmSample_FSM: set["fsmSample_State"] = None, fsmSample_FSM2: "fsmSample_State" = None, fsmSample_FSM5: set["fsmSample_State"] = None, fsmSample_FSM8: "fsmSample_State" = None, fsmSample_FSM12: "fsmSample_State" = None):
        self.name = name
        self.fsmSample_FSM = fsmSample_FSM if fsmSample_FSM is not None else set()
        self.fsmSample_FSM2 = fsmSample_FSM2
        self.fsmSample_FSM5 = fsmSample_FSM5 if fsmSample_FSM5 is not None else set()
        self.fsmSample_FSM8 = fsmSample_FSM8
        self.fsmSample_FSM12 = fsmSample_FSM12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsmSample_FSM2(self):
        return self.__fsmSample_FSM2

    @fsmSample_FSM2.setter
    def fsmSample_FSM2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_FSM__fsmSample_FSM2", None)
        self.__fsmSample_FSM2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmSample_State3"):
                opp_val = getattr(old_value, "fsmSample_State3", None)
                if opp_val == self:
                    setattr(old_value, "fsmSample_State3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmSample_State3"):
                opp_val = getattr(value, "fsmSample_State3", None)
                setattr(value, "fsmSample_State3", self)

    @property
    def fsmSample_FSM12(self):
        return self.__fsmSample_FSM12

    @fsmSample_FSM12.setter
    def fsmSample_FSM12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_FSM__fsmSample_FSM12", None)
        self.__fsmSample_FSM12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmSample_State11"):
                opp_val = getattr(old_value, "fsmSample_State11", None)
                if opp_val == self:
                    setattr(old_value, "fsmSample_State11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmSample_State11"):
                opp_val = getattr(value, "fsmSample_State11", None)
                setattr(value, "fsmSample_State11", self)

    @property
    def fsmSample_FSM5(self):
        return self.__fsmSample_FSM5

    @fsmSample_FSM5.setter
    def fsmSample_FSM5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_FSM__fsmSample_FSM5", None)
        self.__fsmSample_FSM5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsmSample_State6"):
                    opp_val = getattr(item, "fsmSample_State6", None)
                    
                    if opp_val == self:
                        setattr(item, "fsmSample_State6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsmSample_State6"):
                    opp_val = getattr(item, "fsmSample_State6", None)
                    
                    setattr(item, "fsmSample_State6", self)
                    

    @property
    def fsmSample_FSM(self):
        return self.__fsmSample_FSM

    @fsmSample_FSM.setter
    def fsmSample_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_FSM__fsmSample_FSM", None)
        self.__fsmSample_FSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsmSample_State"):
                    opp_val = getattr(item, "fsmSample_State", None)
                    
                    if opp_val == self:
                        setattr(item, "fsmSample_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsmSample_State"):
                    opp_val = getattr(item, "fsmSample_State", None)
                    
                    setattr(item, "fsmSample_State", self)
                    

    @property
    def fsmSample_FSM8(self):
        return self.__fsmSample_FSM8

    @fsmSample_FSM8.setter
    def fsmSample_FSM8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_FSM__fsmSample_FSM8", None)
        self.__fsmSample_FSM8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmSample_State9"):
                opp_val = getattr(old_value, "fsmSample_State9", None)
                if opp_val == self:
                    setattr(old_value, "fsmSample_State9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmSample_State9"):
                opp_val = getattr(value, "fsmSample_State9", None)
                setattr(value, "fsmSample_State9", self)

class fsmSample_Action:

    def __init__(self, name: str, fsmSample_Action: "fsmSample_Transition" = None):
        self.name = name
        self.fsmSample_Action = fsmSample_Action
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsmSample_Action(self):
        return self.__fsmSample_Action

    @fsmSample_Action.setter
    def fsmSample_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_Action__fsmSample_Action", None)
        self.__fsmSample_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmSample_Transition25"):
                opp_val = getattr(old_value, "fsmSample_Transition25", None)
                if opp_val == self:
                    setattr(old_value, "fsmSample_Transition25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmSample_Transition25"):
                opp_val = getattr(value, "fsmSample_Transition25", None)
                setattr(value, "fsmSample_Transition25", self)

class fsmSample_Transition:

    def __init__(self, input: str, output: str, fsmSample_Transition: "fsmSample_State" = None, fsmSample_Transition17: "fsmSample_State" = None, fsmSample_Transition19: "fsmSample_State" = None, fsmSample_Transition22: "fsmSample_State" = None, fsmSample_Transition25: "fsmSample_Action" = None):
        self.input = input
        self.output = output
        self.fsmSample_Transition = fsmSample_Transition
        self.fsmSample_Transition17 = fsmSample_Transition17
        self.fsmSample_Transition19 = fsmSample_Transition19
        self.fsmSample_Transition22 = fsmSample_Transition22
        self.fsmSample_Transition25 = fsmSample_Transition25
        
    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

    @property
    def output(self) -> str:
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output

    @property
    def fsmSample_Transition(self):
        return self.__fsmSample_Transition

    @fsmSample_Transition.setter
    def fsmSample_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_Transition__fsmSample_Transition", None)
        self.__fsmSample_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmSample_State14"):
                opp_val = getattr(old_value, "fsmSample_State14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmSample_State14"):
                opp_val = getattr(value, "fsmSample_State14", None)
                if opp_val is None:
                    setattr(value, "fsmSample_State14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsmSample_Transition19(self):
        return self.__fsmSample_Transition19

    @fsmSample_Transition19.setter
    def fsmSample_Transition19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_Transition__fsmSample_Transition19", None)
        self.__fsmSample_Transition19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmSample_State20"):
                opp_val = getattr(old_value, "fsmSample_State20", None)
                if opp_val == self:
                    setattr(old_value, "fsmSample_State20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmSample_State20"):
                opp_val = getattr(value, "fsmSample_State20", None)
                setattr(value, "fsmSample_State20", self)

    @property
    def fsmSample_Transition25(self):
        return self.__fsmSample_Transition25

    @fsmSample_Transition25.setter
    def fsmSample_Transition25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_Transition__fsmSample_Transition25", None)
        self.__fsmSample_Transition25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmSample_Action"):
                opp_val = getattr(old_value, "fsmSample_Action", None)
                if opp_val == self:
                    setattr(old_value, "fsmSample_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmSample_Action"):
                opp_val = getattr(value, "fsmSample_Action", None)
                setattr(value, "fsmSample_Action", self)

    @property
    def fsmSample_Transition22(self):
        return self.__fsmSample_Transition22

    @fsmSample_Transition22.setter
    def fsmSample_Transition22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_Transition__fsmSample_Transition22", None)
        self.__fsmSample_Transition22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmSample_State23"):
                opp_val = getattr(old_value, "fsmSample_State23", None)
                if opp_val == self:
                    setattr(old_value, "fsmSample_State23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmSample_State23"):
                opp_val = getattr(value, "fsmSample_State23", None)
                setattr(value, "fsmSample_State23", self)

    @property
    def fsmSample_Transition17(self):
        return self.__fsmSample_Transition17

    @fsmSample_Transition17.setter
    def fsmSample_Transition17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_Transition__fsmSample_Transition17", None)
        self.__fsmSample_Transition17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmSample_State16"):
                opp_val = getattr(old_value, "fsmSample_State16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmSample_State16"):
                opp_val = getattr(value, "fsmSample_State16", None)
                if opp_val is None:
                    setattr(value, "fsmSample_State16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
