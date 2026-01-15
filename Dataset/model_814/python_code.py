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

    def __init__(self, fsm_State7: "fsm_StateMachine" = None, 9: "fsm_StateMachine" = None, 12: set["fsm_Transition"] = None, 15: set["fsm_Transition"] = None, 19: "fsm_Transition" = None, 22: "fsm_Transition" = None, 1: "fsm_StateMachine" = None, fsm_State: "fsm_StateMachine" = None):
        self.fsm_State7 = fsm_State7
        self.9 = 9
        self.12 = 12 if 12 is not None else set()
        self.15 = 15 if 15 is not None else set()
        self.19 = 19
        self.22 = 22
        self.1 = 1
        self.fsm_State = fsm_State
        
    @property
    def 19(self):
        return self.__19

    @19.setter
    def 19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__19", None)
        self.__19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "18"):
                opp_val = getattr(old_value, "18", None)
                if opp_val == self:
                    setattr(old_value, "18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "18"):
                opp_val = getattr(value, "18", None)
                setattr(value, "18", self)

    @property
    def 22(self):
        return self.__22

    @22.setter
    def 22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__22", None)
        self.__22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "21"):
                opp_val = getattr(old_value, "21", None)
                if opp_val == self:
                    setattr(old_value, "21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "21"):
                opp_val = getattr(value, "21", None)
                setattr(value, "21", self)

    @property
    def fsm_State7(self):
        return self.__fsm_State7

    @fsm_State7.setter
    def fsm_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State7", None)
        self.__fsm_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_StateMachine6"):
                opp_val = getattr(old_value, "fsm_StateMachine6", None)
                if opp_val == self:
                    setattr(old_value, "fsm_StateMachine6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_StateMachine6"):
                opp_val = getattr(value, "fsm_StateMachine6", None)
                setattr(value, "fsm_StateMachine6", self)

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
            if hasattr(old_value, "fsm_StateMachine"):
                opp_val = getattr(old_value, "fsm_StateMachine", None)
                if opp_val == self:
                    setattr(old_value, "fsm_StateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_StateMachine"):
                opp_val = getattr(value, "fsm_StateMachine", None)
                setattr(value, "fsm_StateMachine", self)

    @property
    def 9(self):
        return self.__9

    @9.setter
    def 9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__9", None)
        self.__9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "10"):
                opp_val = getattr(old_value, "10", None)
                if opp_val == self:
                    setattr(old_value, "10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "10"):
                opp_val = getattr(value, "10", None)
                setattr(value, "10", self)

    @property
    def 12(self):
        return self.__12

    @12.setter
    def 12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__12", None)
        self.__12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "13"):
                    opp_val = getattr(item, "13", None)
                    
                    if opp_val == self:
                        setattr(item, "13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "13"):
                    opp_val = getattr(item, "13", None)
                    
                    setattr(item, "13", self)
                    

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

    @property
    def 15(self):
        return self.__15

    @15.setter
    def 15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__15", None)
        self.__15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "16"):
                    opp_val = getattr(item, "16", None)
                    
                    if opp_val == self:
                        setattr(item, "16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "16"):
                    opp_val = getattr(item, "16", None)
                    
                    setattr(item, "16", self)
                    

    def step(self, inputString: str):
        # TODO: Implement step method
        pass

class fsm_FSMSystem(NamedElement):

    def __init__(self, fsm_FSMSystem: set["fsm_StateMachine"] = None, fsm_FSMSystem26: set["fsm_Buffer"] = None):
        self.fsm_FSMSystem = fsm_FSMSystem if fsm_FSMSystem is not None else set()
        self.fsm_FSMSystem26 = fsm_FSMSystem26 if fsm_FSMSystem26 is not None else set()
        
    @property
    def fsm_FSMSystem26(self):
        return self.__fsm_FSMSystem26

    @fsm_FSMSystem26.setter
    def fsm_FSMSystem26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSMSystem__fsm_FSMSystem26", None)
        self.__fsm_FSMSystem26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_Buffer"):
                    opp_val = getattr(item, "fsm_Buffer", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_Buffer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_Buffer"):
                    opp_val = getattr(item, "fsm_Buffer", None)
                    
                    setattr(item, "fsm_Buffer", self)
                    

    @property
    def fsm_FSMSystem(self):
        return self.__fsm_FSMSystem

    @fsm_FSMSystem.setter
    def fsm_FSMSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSMSystem__fsm_FSMSystem", None)
        self.__fsm_FSMSystem = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_StateMachine24"):
                    opp_val = getattr(item, "fsm_StateMachine24", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_StateMachine24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_StateMachine24"):
                    opp_val = getattr(item, "fsm_StateMachine24", None)
                    
                    setattr(item, "fsm_StateMachine24", self)
                    

    def initialize(self, args: str):
        # TODO: Implement initialize method
        pass

    def main(self):
        # TODO: Implement main method
        pass

class fsm_Buffer(NamedElement):

    def __init__(self, initialValue: str, currentValues: str, fsm_Buffer: "fsm_FSMSystem" = None, fsm_Buffer28: set["fsm_StateMachine"] = None, fsm_Buffer31: set["fsm_StateMachine"] = None):
        self.initialValue = initialValue
        self.currentValues = currentValues
        self.fsm_Buffer = fsm_Buffer
        self.fsm_Buffer28 = fsm_Buffer28 if fsm_Buffer28 is not None else set()
        self.fsm_Buffer31 = fsm_Buffer31 if fsm_Buffer31 is not None else set()
        
    @property
    def currentValues(self) -> str:
        return self.__currentValues

    @currentValues.setter
    def currentValues(self, currentValues: str):
        self.__currentValues = currentValues

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
    def fsm_Buffer31(self):
        return self.__fsm_Buffer31

    @fsm_Buffer31.setter
    def fsm_Buffer31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Buffer__fsm_Buffer31", None)
        self.__fsm_Buffer31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_StateMachine32"):
                    opp_val = getattr(item, "fsm_StateMachine32", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_StateMachine32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_StateMachine32"):
                    opp_val = getattr(item, "fsm_StateMachine32", None)
                    
                    setattr(item, "fsm_StateMachine32", self)
                    

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
            if hasattr(old_value, "fsm_FSMSystem26"):
                opp_val = getattr(old_value, "fsm_FSMSystem26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSMSystem26"):
                opp_val = getattr(value, "fsm_FSMSystem26", None)
                if opp_val is None:
                    setattr(value, "fsm_FSMSystem26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def dequeue(self):
        # TODO: Implement dequeue method
        pass

    def initialize(self):
        # TODO: Implement initialize method
        pass

    def enqueue(self, v: str):
        # TODO: Implement enqueue method
        pass

class fsm_Transition(NamedElement):

    def __init__(self, input: str, output: str, fsm_Transition: "fsm_StateMachine" = None, 13: "fsm_State" = None, 16: "fsm_State" = None, 18: "fsm_State" = None, 21: "fsm_State" = None):
        self.input = input
        self.output = output
        self.fsm_Transition = fsm_Transition
        self.13 = 13
        self.16 = 16
        self.18 = 18
        self.21 = 21
        
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
    def 21(self):
        return self.__21

    @21.setter
    def 21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__21", None)
        self.__21 = value
        
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
            if hasattr(old_value, "15"):
                opp_val = getattr(old_value, "15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "15"):
                opp_val = getattr(value, "15", None)
                if opp_val is None:
                    setattr(value, "15", set([self]))
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

    def fire(self):
        # TODO: Implement fire method
        pass

class fsm_StateMachine(NamedElement):

    def __init__(self, unprocessedString: str, consummedString: str, producedString: str, fsm_StateMachine4: set["fsm_Transition"] = None, fsm_StateMachine6: "fsm_State" = None, 10: "fsm_State" = None, : set["fsm_State"] = None, fsm_StateMachine: "fsm_State" = None, fsm_StateMachine24: "fsm_FSMSystem" = None, fsm_StateMachine29: "fsm_Buffer" = None, fsm_StateMachine32: "fsm_Buffer" = None):
        self.unprocessedString = unprocessedString
        self.consummedString = consummedString
        self.producedString = producedString
        self.fsm_StateMachine4 = fsm_StateMachine4 if fsm_StateMachine4 is not None else set()
        self.fsm_StateMachine6 = fsm_StateMachine6
        self.10 = 10
        self. =  if  is not None else set()
        self.fsm_StateMachine = fsm_StateMachine
        self.fsm_StateMachine24 = fsm_StateMachine24
        self.fsm_StateMachine29 = fsm_StateMachine29
        self.fsm_StateMachine32 = fsm_StateMachine32
        
    @property
    def unprocessedString(self) -> str:
        return self.__unprocessedString

    @unprocessedString.setter
    def unprocessedString(self, unprocessedString: str):
        self.__unprocessedString = unprocessedString

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
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__", None)
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
    def fsm_StateMachine6(self):
        return self.__fsm_StateMachine6

    @fsm_StateMachine6.setter
    def fsm_StateMachine6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__fsm_StateMachine6", None)
        self.__fsm_StateMachine6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State7"):
                opp_val = getattr(old_value, "fsm_State7", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State7"):
                opp_val = getattr(value, "fsm_State7", None)
                setattr(value, "fsm_State7", self)

    @property
    def 10(self):
        return self.__10

    @10.setter
    def 10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__10", None)
        self.__10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "9"):
                opp_val = getattr(old_value, "9", None)
                if opp_val == self:
                    setattr(old_value, "9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "9"):
                opp_val = getattr(value, "9", None)
                setattr(value, "9", self)

    @property
    def fsm_StateMachine4(self):
        return self.__fsm_StateMachine4

    @fsm_StateMachine4.setter
    def fsm_StateMachine4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__fsm_StateMachine4", None)
        self.__fsm_StateMachine4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_Transition"):
                    opp_val = getattr(item, "fsm_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_Transition"):
                    opp_val = getattr(item, "fsm_Transition", None)
                    
                    setattr(item, "fsm_Transition", self)
                    

    @property
    def fsm_StateMachine29(self):
        return self.__fsm_StateMachine29

    @fsm_StateMachine29.setter
    def fsm_StateMachine29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__fsm_StateMachine29", None)
        self.__fsm_StateMachine29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Buffer28"):
                opp_val = getattr(old_value, "fsm_Buffer28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Buffer28"):
                opp_val = getattr(value, "fsm_Buffer28", None)
                if opp_val is None:
                    setattr(value, "fsm_Buffer28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_StateMachine24(self):
        return self.__fsm_StateMachine24

    @fsm_StateMachine24.setter
    def fsm_StateMachine24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__fsm_StateMachine24", None)
        self.__fsm_StateMachine24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_FSMSystem"):
                opp_val = getattr(old_value, "fsm_FSMSystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSMSystem"):
                opp_val = getattr(value, "fsm_FSMSystem", None)
                if opp_val is None:
                    setattr(value, "fsm_FSMSystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_StateMachine32(self):
        return self.__fsm_StateMachine32

    @fsm_StateMachine32.setter
    def fsm_StateMachine32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__fsm_StateMachine32", None)
        self.__fsm_StateMachine32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Buffer31"):
                opp_val = getattr(old_value, "fsm_Buffer31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Buffer31"):
                opp_val = getattr(value, "fsm_Buffer31", None)
                if opp_val is None:
                    setattr(value, "fsm_Buffer31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_StateMachine(self):
        return self.__fsm_StateMachine

    @fsm_StateMachine.setter
    def fsm_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__fsm_StateMachine", None)
        self.__fsm_StateMachine = value
        
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

    def initializeModel(self):
        # TODO: Implement initializeModel method
        pass

    def run(self):
        # TODO: Implement run method
        pass
