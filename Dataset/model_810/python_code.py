from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class fsm_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class fsm_State(NamedElement):

    pass
class fsm_Transition(NamedElement):

    def __init__(self, input: str, output: str, fsm_Transition: "fsm_StateMachine" = None, 10: "fsm_State" = None, 13: "fsm_State" = None, 15: "fsm_State" = None, 18: "fsm_State" = None):
        self.input = input
        self.output = output
        self.fsm_Transition = fsm_Transition
        self.10 = 10
        self.13 = 13
        self.15 = 15
        self.18 = 18
        
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
    def 15(self):
        return self.__15

    @15.setter
    def 15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__15", None)
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
    def 10(self):
        return self.__10

    @10.setter
    def 10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__10", None)
        self.__10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "9"):
                opp_val = getattr(old_value, "9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "9"):
                opp_val = getattr(value, "9", None)
                if opp_val is None:
                    setattr(value, "9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 13(self):
        return self.__13

    @13.setter
    def 13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__13", None)
        self.__13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "12"):
                opp_val = getattr(old_value, "12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "12"):
                opp_val = getattr(value, "12", None)
                if opp_val is None:
                    setattr(value, "12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_Transition(self):
        return self.__fsm_Transition

    @fsm_Transition.setter
    def fsm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition", None)
        self.__fsm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_StateMachine4"):
                opp_val = getattr(old_value, "fsm_StateMachine4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_StateMachine4"):
                opp_val = getattr(value, "fsm_StateMachine4", None)
                if opp_val is None:
                    setattr(value, "fsm_StateMachine4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 18(self):
        return self.__18

    @18.setter
    def 18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__18", None)
        self.__18 = value
        
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

class fsm_FSMSystem(NamedElement):

    pass
class fsm_Buffer(NamedElement):

    def __init__(self, initialValue: str, fsm_Buffer: "fsm_FSMSystem" = None, fsm_Buffer25: set["fsm_StateMachine"] = None, fsm_Buffer28: set["fsm_StateMachine"] = None):
        self.initialValue = initialValue
        self.fsm_Buffer = fsm_Buffer
        self.fsm_Buffer25 = fsm_Buffer25 if fsm_Buffer25 is not None else set()
        self.fsm_Buffer28 = fsm_Buffer28 if fsm_Buffer28 is not None else set()
        
    @property
    def initialValue(self) -> str:
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: str):
        self.__initialValue = initialValue

    @property
    def fsm_Buffer28(self):
        return self.__fsm_Buffer28

    @fsm_Buffer28.setter
    def fsm_Buffer28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Buffer__fsm_Buffer28", None)
        self.__fsm_Buffer28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_StateMachine29"):
                    opp_val = getattr(item, "fsm_StateMachine29", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_StateMachine29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_StateMachine29"):
                    opp_val = getattr(item, "fsm_StateMachine29", None)
                    
                    setattr(item, "fsm_StateMachine29", self)
                    

    @property
    def fsm_Buffer25(self):
        return self.__fsm_Buffer25

    @fsm_Buffer25.setter
    def fsm_Buffer25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Buffer__fsm_Buffer25", None)
        self.__fsm_Buffer25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_StateMachine26"):
                    opp_val = getattr(item, "fsm_StateMachine26", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_StateMachine26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_StateMachine26"):
                    opp_val = getattr(item, "fsm_StateMachine26", None)
                    
                    setattr(item, "fsm_StateMachine26", self)
                    

    @property
    def fsm_Buffer(self):
        return self.__fsm_Buffer

    @fsm_Buffer.setter
    def fsm_Buffer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Buffer__fsm_Buffer", None)
        self.__fsm_Buffer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_FSMSystem23"):
                opp_val = getattr(old_value, "fsm_FSMSystem23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSMSystem23"):
                opp_val = getattr(value, "fsm_FSMSystem23", None)
                if opp_val is None:
                    setattr(value, "fsm_FSMSystem23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fsm_StateMachine(NamedElement):

    pass