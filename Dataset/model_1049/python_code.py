from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class efsm_Param:

    def __init__(self, argName: str, argType: str, efsm_Param: "efsm_Event" = None):
        self.argName = argName
        self.argType = argType
        self.efsm_Param = efsm_Param
        
    @property
    def argName(self) -> str:
        return self.__argName

    @argName.setter
    def argName(self, argName: str):
        self.__argName = argName

    @property
    def argType(self) -> str:
        return self.__argType

    @argType.setter
    def argType(self, argType: str):
        self.__argType = argType

    @property
    def efsm_Param(self):
        return self.__efsm_Param

    @efsm_Param.setter
    def efsm_Param(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_efsm_Param__efsm_Param", None)
        self.__efsm_Param = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "efsm_Event19"):
                opp_val = getattr(old_value, "efsm_Event19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "efsm_Event19"):
                opp_val = getattr(value, "efsm_Event19", None)
                if opp_val is None:
                    setattr(value, "efsm_Event19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class efsm_Variable:

    def __init__(self, name: str, type: str, class: str, efsm_Variable: "efsm_Input" = None):
        self.name = name
        self.type = type
        self.class = class
        self.efsm_Variable = efsm_Variable
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def efsm_Variable(self):
        return self.__efsm_Variable

    @efsm_Variable.setter
    def efsm_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_efsm_Variable__efsm_Variable", None)
        self.__efsm_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "efsm_Input17"):
                opp_val = getattr(old_value, "efsm_Input17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "efsm_Input17"):
                opp_val = getattr(value, "efsm_Input17", None)
                if opp_val is None:
                    setattr(value, "efsm_Input17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractState:

    pass
class efsm_Event:

    def __init__(self, name: str, return: str, class: str, efsm_Event: "efsm_Transition" = None, efsm_Event19: set["efsm_Param"] = None):
        self.name = name
        self.return = return
        self.class = class
        self.efsm_Event = efsm_Event
        self.efsm_Event19 = efsm_Event19 if efsm_Event19 is not None else set()
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def return(self) -> str:
        return self.__return

    @return.setter
    def return(self, return: str):
        self.__return = return

    @property
    def efsm_Event19(self):
        return self.__efsm_Event19

    @efsm_Event19.setter
    def efsm_Event19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_efsm_Event__efsm_Event19", None)
        self.__efsm_Event19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "efsm_Param"):
                    opp_val = getattr(item, "efsm_Param", None)
                    
                    if opp_val == self:
                        setattr(item, "efsm_Param", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "efsm_Param"):
                    opp_val = getattr(item, "efsm_Param", None)
                    
                    setattr(item, "efsm_Param", self)
                    

    @property
    def efsm_Event(self):
        return self.__efsm_Event

    @efsm_Event.setter
    def efsm_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_efsm_Event__efsm_Event", None)
        self.__efsm_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "efsm_Transition15"):
                opp_val = getattr(old_value, "efsm_Transition15", None)
                if opp_val == self:
                    setattr(old_value, "efsm_Transition15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "efsm_Transition15"):
                opp_val = getattr(value, "efsm_Transition15", None)
                setattr(value, "efsm_Transition15", self)

class efsm_Input:

    def __init__(self, name: str, efsm_Input: "efsm_Transition" = None, efsm_Input17: set["efsm_Variable"] = None):
        self.name = name
        self.efsm_Input = efsm_Input
        self.efsm_Input17 = efsm_Input17 if efsm_Input17 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def efsm_Input(self):
        return self.__efsm_Input

    @efsm_Input.setter
    def efsm_Input(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_efsm_Input__efsm_Input", None)
        self.__efsm_Input = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "efsm_Transition13"):
                opp_val = getattr(old_value, "efsm_Transition13", None)
                if opp_val == self:
                    setattr(old_value, "efsm_Transition13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "efsm_Transition13"):
                opp_val = getattr(value, "efsm_Transition13", None)
                setattr(value, "efsm_Transition13", self)

    @property
    def efsm_Input17(self):
        return self.__efsm_Input17

    @efsm_Input17.setter
    def efsm_Input17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_efsm_Input__efsm_Input17", None)
        self.__efsm_Input17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "efsm_Variable"):
                    opp_val = getattr(item, "efsm_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "efsm_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "efsm_Variable"):
                    opp_val = getattr(item, "efsm_Variable", None)
                    
                    setattr(item, "efsm_Variable", self)
                    

class efsm_EFSM:

    def __init__(self, name: str, efsm_EFSM: set["efsm_Transition"] = None, efsm_EFSM2: "efsm_InitialState" = None, efsm_EFSM4: set["efsm_State"] = None, efsm_EFSM6: set["efsm_ContextVariable"] = None):
        self.name = name
        self.efsm_EFSM = efsm_EFSM if efsm_EFSM is not None else set()
        self.efsm_EFSM2 = efsm_EFSM2
        self.efsm_EFSM4 = efsm_EFSM4 if efsm_EFSM4 is not None else set()
        self.efsm_EFSM6 = efsm_EFSM6 if efsm_EFSM6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def efsm_EFSM6(self):
        return self.__efsm_EFSM6

    @efsm_EFSM6.setter
    def efsm_EFSM6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_efsm_EFSM__efsm_EFSM6", None)
        self.__efsm_EFSM6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "efsm_ContextVariable"):
                    opp_val = getattr(item, "efsm_ContextVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "efsm_ContextVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "efsm_ContextVariable"):
                    opp_val = getattr(item, "efsm_ContextVariable", None)
                    
                    setattr(item, "efsm_ContextVariable", self)
                    

    @property
    def efsm_EFSM2(self):
        return self.__efsm_EFSM2

    @efsm_EFSM2.setter
    def efsm_EFSM2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_efsm_EFSM__efsm_EFSM2", None)
        self.__efsm_EFSM2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "efsm_InitialState"):
                opp_val = getattr(old_value, "efsm_InitialState", None)
                if opp_val == self:
                    setattr(old_value, "efsm_InitialState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "efsm_InitialState"):
                opp_val = getattr(value, "efsm_InitialState", None)
                setattr(value, "efsm_InitialState", self)

    @property
    def efsm_EFSM(self):
        return self.__efsm_EFSM

    @efsm_EFSM.setter
    def efsm_EFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_efsm_EFSM__efsm_EFSM", None)
        self.__efsm_EFSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "efsm_Transition"):
                    opp_val = getattr(item, "efsm_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "efsm_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "efsm_Transition"):
                    opp_val = getattr(item, "efsm_Transition", None)
                    
                    setattr(item, "efsm_Transition", self)
                    

    @property
    def efsm_EFSM4(self):
        return self.__efsm_EFSM4

    @efsm_EFSM4.setter
    def efsm_EFSM4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_efsm_EFSM__efsm_EFSM4", None)
        self.__efsm_EFSM4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "efsm_State"):
                    opp_val = getattr(item, "efsm_State", None)
                    
                    if opp_val == self:
                        setattr(item, "efsm_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "efsm_State"):
                    opp_val = getattr(item, "efsm_State", None)
                    
                    setattr(item, "efsm_State", self)
                    

class efsm_AbstractState(ABC):

    def __init__(self, name: str, efsm_AbstractState: "efsm_Transition" = None, efsm_AbstractState11: "efsm_Transition" = None):
        self.name = name
        self.efsm_AbstractState = efsm_AbstractState
        self.efsm_AbstractState11 = efsm_AbstractState11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def efsm_AbstractState(self):
        return self.__efsm_AbstractState

    @efsm_AbstractState.setter
    def efsm_AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_efsm_AbstractState__efsm_AbstractState", None)
        self.__efsm_AbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "efsm_Transition8"):
                opp_val = getattr(old_value, "efsm_Transition8", None)
                if opp_val == self:
                    setattr(old_value, "efsm_Transition8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "efsm_Transition8"):
                opp_val = getattr(value, "efsm_Transition8", None)
                setattr(value, "efsm_Transition8", self)

    @property
    def efsm_AbstractState11(self):
        return self.__efsm_AbstractState11

    @efsm_AbstractState11.setter
    def efsm_AbstractState11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_efsm_AbstractState__efsm_AbstractState11", None)
        self.__efsm_AbstractState11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "efsm_Transition10"):
                opp_val = getattr(old_value, "efsm_Transition10", None)
                if opp_val == self:
                    setattr(old_value, "efsm_Transition10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "efsm_Transition10"):
                opp_val = getattr(value, "efsm_Transition10", None)
                setattr(value, "efsm_Transition10", self)

class efsm_ContextVariable:

    def __init__(self, name: str, type: str, efsm_ContextVariable: "efsm_EFSM" = None):
        self.name = name
        self.type = type
        self.efsm_ContextVariable = efsm_ContextVariable
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def efsm_ContextVariable(self):
        return self.__efsm_ContextVariable

    @efsm_ContextVariable.setter
    def efsm_ContextVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_efsm_ContextVariable__efsm_ContextVariable", None)
        self.__efsm_ContextVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "efsm_EFSM6"):
                opp_val = getattr(old_value, "efsm_EFSM6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "efsm_EFSM6"):
                opp_val = getattr(value, "efsm_EFSM6", None)
                if opp_val is None:
                    setattr(value, "efsm_EFSM6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class efsm_State(AbstractState):

    pass
class efsm_InitialState(AbstractState):

    pass
class efsm_Transition:

    def __init__(self, name: str, output: str, guard: str, action: str, efsm_Transition: "efsm_EFSM" = None, efsm_Transition8: "efsm_AbstractState" = None, efsm_Transition10: "efsm_AbstractState" = None, efsm_Transition13: "efsm_Input" = None, efsm_Transition15: "efsm_Event" = None):
        self.name = name
        self.output = output
        self.guard = guard
        self.action = action
        self.efsm_Transition = efsm_Transition
        self.efsm_Transition8 = efsm_Transition8
        self.efsm_Transition10 = efsm_Transition10
        self.efsm_Transition13 = efsm_Transition13
        self.efsm_Transition15 = efsm_Transition15
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def guard(self) -> str:
        return self.__guard

    @guard.setter
    def guard(self, guard: str):
        self.__guard = guard

    @property
    def output(self) -> str:
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output

    @property
    def efsm_Transition8(self):
        return self.__efsm_Transition8

    @efsm_Transition8.setter
    def efsm_Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_efsm_Transition__efsm_Transition8", None)
        self.__efsm_Transition8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "efsm_AbstractState"):
                opp_val = getattr(old_value, "efsm_AbstractState", None)
                if opp_val == self:
                    setattr(old_value, "efsm_AbstractState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "efsm_AbstractState"):
                opp_val = getattr(value, "efsm_AbstractState", None)
                setattr(value, "efsm_AbstractState", self)

    @property
    def efsm_Transition10(self):
        return self.__efsm_Transition10

    @efsm_Transition10.setter
    def efsm_Transition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_efsm_Transition__efsm_Transition10", None)
        self.__efsm_Transition10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "efsm_AbstractState11"):
                opp_val = getattr(old_value, "efsm_AbstractState11", None)
                if opp_val == self:
                    setattr(old_value, "efsm_AbstractState11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "efsm_AbstractState11"):
                opp_val = getattr(value, "efsm_AbstractState11", None)
                setattr(value, "efsm_AbstractState11", self)

    @property
    def efsm_Transition13(self):
        return self.__efsm_Transition13

    @efsm_Transition13.setter
    def efsm_Transition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_efsm_Transition__efsm_Transition13", None)
        self.__efsm_Transition13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "efsm_Input"):
                opp_val = getattr(old_value, "efsm_Input", None)
                if opp_val == self:
                    setattr(old_value, "efsm_Input", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "efsm_Input"):
                opp_val = getattr(value, "efsm_Input", None)
                setattr(value, "efsm_Input", self)

    @property
    def efsm_Transition15(self):
        return self.__efsm_Transition15

    @efsm_Transition15.setter
    def efsm_Transition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_efsm_Transition__efsm_Transition15", None)
        self.__efsm_Transition15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "efsm_Event"):
                opp_val = getattr(old_value, "efsm_Event", None)
                if opp_val == self:
                    setattr(old_value, "efsm_Event", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "efsm_Event"):
                opp_val = getattr(value, "efsm_Event", None)
                setattr(value, "efsm_Event", self)

    @property
    def efsm_Transition(self):
        return self.__efsm_Transition

    @efsm_Transition.setter
    def efsm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_efsm_Transition__efsm_Transition", None)
        self.__efsm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "efsm_EFSM"):
                opp_val = getattr(old_value, "efsm_EFSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "efsm_EFSM"):
                opp_val = getattr(value, "efsm_EFSM", None)
                if opp_val is None:
                    setattr(value, "efsm_EFSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
