from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class fsm_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class NamedElement:

    pass
class fsm_Buffer(NamedElement):

    def __init__(self, initialValue: str, fsm_Buffer: "fsm_FSMSystem" = None, fsm_Buffer17: set["fsm_StateMachine"] = None, fsm_Buffer20: set["fsm_StateMachine"] = None):
        self.initialValue = initialValue
        self.fsm_Buffer = fsm_Buffer
        self.fsm_Buffer17 = fsm_Buffer17 if fsm_Buffer17 is not None else set()
        self.fsm_Buffer20 = fsm_Buffer20 if fsm_Buffer20 is not None else set()
        
        pass
    @property
    def initialValue(self):
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: str):
        self.__initialValue = initialValue


    @property
    def fsm_Buffer17(self):
        return self.__fsm_Buffer17

    @fsm_Buffer17.setter
    def fsm_Buffer17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Buffer__fsm_Buffer17", None)
        self.__fsm_Buffer17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_StateMachine18"):
                    opp_val = getattr(item, "fsm_StateMachine18", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_StateMachine18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_StateMachine18"):
                    opp_val = getattr(item, "fsm_StateMachine18", None)
                    
                    setattr(item, "fsm_StateMachine18", self)
                    

    @property
    def fsm_Buffer20(self):
        return self.__fsm_Buffer20

    @fsm_Buffer20.setter
    def fsm_Buffer20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Buffer__fsm_Buffer20", None)
        self.__fsm_Buffer20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_StateMachine21"):
                    opp_val = getattr(item, "fsm_StateMachine21", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_StateMachine21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_StateMachine21"):
                    opp_val = getattr(item, "fsm_StateMachine21", None)
                    
                    setattr(item, "fsm_StateMachine21", self)
                    

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
            if hasattr(old_value, "fsm_FSMSystem15"):
                opp_val = getattr(old_value, "fsm_FSMSystem15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSMSystem15"):
                opp_val = getattr(value, "fsm_FSMSystem15", None)
                if opp_val is None:
                    setattr(value, "fsm_FSMSystem15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fsm_Transition(NamedElement):

    def __init__(self, input: str, output: str, fsm_Transition: "fsm_StateMachine" = None, Transition: "fsm_State" = None, Transition7: "fsm_State" = None, outgoingTransitions: "fsm_State" = None, incomingTransitions: "fsm_State" = None):
        self.input = input
        self.output = output
        self.fsm_Transition = fsm_Transition
        self.Transition = Transition
        self.Transition7 = Transition7
        self.outgoingTransitions = outgoingTransitions
        self.incomingTransitions = incomingTransitions
        
        pass
    @property
    def input(self):
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input


    @property
    def output(self):
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output


    @property
    def Transition7(self):
        return self.__Transition7

    @Transition7.setter
    def Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__Transition7", None)
        self.__Transition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoingTransitions(self):
        return self.__outgoingTransitions

    @outgoingTransitions.setter
    def outgoingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__outgoingTransitions", None)
        self.__outgoingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State9"):
                opp_val = getattr(old_value, "State9", None)
                if opp_val == self:
                    setattr(old_value, "State9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State9"):
                opp_val = getattr(value, "State9", None)
                setattr(value, "State9", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incomingTransitions(self):
        return self.__incomingTransitions

    @incomingTransitions.setter
    def incomingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__incomingTransitions", None)
        self.__incomingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State11"):
                opp_val = getattr(old_value, "State11", None)
                if opp_val == self:
                    setattr(old_value, "State11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State11"):
                opp_val = getattr(value, "State11", None)
                setattr(value, "State11", self)

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
            if hasattr(old_value, "fsm_StateMachine3"):
                opp_val = getattr(old_value, "fsm_StateMachine3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_StateMachine3"):
                opp_val = getattr(value, "fsm_StateMachine3", None)
                if opp_val is None:
                    setattr(value, "fsm_StateMachine3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fsm_State(NamedElement):

    pass
class fsm_FSMSystem(NamedElement):

    pass
class fsm_StateMachine(NamedElement):

    pass