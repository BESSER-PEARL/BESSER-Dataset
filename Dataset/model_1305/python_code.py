from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Operator(Enum):
    add = "add"
    sub = "sub"
    eq = "eq"
    mul = "mul"
    gt = "gt"
    lt = "lt"
    lte = "lte"
    gte = "gte"
    div = "div"
    and = "and"
    neq = "neq"
    or = "or"
    not = "not"


############################################
# Definition of Classes
############################################

class SimplStateMachine_Assignment:

    def __init__(self, _name: str, SimplStateMachine_Assignment: "SimplStateMachine_Operation" = None, SimplStateMachine_Assignment33: "SimplStateMachine_ExpressionElement" = None, SimplStateMachine_Assignment36: "SimplStateMachine_Variable" = None):
        self._name = _name
        self.SimplStateMachine_Assignment = SimplStateMachine_Assignment
        self.SimplStateMachine_Assignment33 = SimplStateMachine_Assignment33
        self.SimplStateMachine_Assignment36 = SimplStateMachine_Assignment36
        
    @property
    def _name(self) -> str:
        return self.___name

    @_name.setter
    def _name(self, _name: str):
        self.___name = _name

    @property
    def SimplStateMachine_Assignment33(self):
        return self.__SimplStateMachine_Assignment33

    @SimplStateMachine_Assignment33.setter
    def SimplStateMachine_Assignment33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachine_Assignment__SimplStateMachine_Assignment33", None)
        self.__SimplStateMachine_Assignment33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplStateMachine_ExpressionElement34"):
                opp_val = getattr(old_value, "SimplStateMachine_ExpressionElement34", None)
                if opp_val == self:
                    setattr(old_value, "SimplStateMachine_ExpressionElement34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplStateMachine_ExpressionElement34"):
                opp_val = getattr(value, "SimplStateMachine_ExpressionElement34", None)
                setattr(value, "SimplStateMachine_ExpressionElement34", self)

    @property
    def SimplStateMachine_Assignment(self):
        return self.__SimplStateMachine_Assignment

    @SimplStateMachine_Assignment.setter
    def SimplStateMachine_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachine_Assignment__SimplStateMachine_Assignment", None)
        self.__SimplStateMachine_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplStateMachine_Operation31"):
                opp_val = getattr(old_value, "SimplStateMachine_Operation31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplStateMachine_Operation31"):
                opp_val = getattr(value, "SimplStateMachine_Operation31", None)
                if opp_val is None:
                    setattr(value, "SimplStateMachine_Operation31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SimplStateMachine_Assignment36(self):
        return self.__SimplStateMachine_Assignment36

    @SimplStateMachine_Assignment36.setter
    def SimplStateMachine_Assignment36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachine_Assignment__SimplStateMachine_Assignment36", None)
        self.__SimplStateMachine_Assignment36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplStateMachine_Variable37"):
                opp_val = getattr(old_value, "SimplStateMachine_Variable37", None)
                if opp_val == self:
                    setattr(old_value, "SimplStateMachine_Variable37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplStateMachine_Variable37"):
                opp_val = getattr(value, "SimplStateMachine_Variable37", None)
                setattr(value, "SimplStateMachine_Variable37", self)

class Variable:

    pass
class SimplStateMachine_IntegerVariable(Variable):

    pass
class Data:

    pass
class SimplStateMachine_IntegerData(Data):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class SimplStateMachine_BooleanData(Data):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class ExpressionElement:

    pass
class SimplStateMachine_Data(ExpressionElement):

    pass
class SimplStateMachine_VariableReference(ExpressionElement):

    def __init__(self, _name: str, SimplStateMachine_VariableReference: "SimplStateMachine_Variable" = None):
        self._name = _name
        self.SimplStateMachine_VariableReference = SimplStateMachine_VariableReference
        
    @property
    def _name(self) -> str:
        return self.___name

    @_name.setter
    def _name(self, _name: str):
        self.___name = _name

    @property
    def SimplStateMachine_VariableReference(self):
        return self.__SimplStateMachine_VariableReference

    @SimplStateMachine_VariableReference.setter
    def SimplStateMachine_VariableReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachine_VariableReference__SimplStateMachine_VariableReference", None)
        self.__SimplStateMachine_VariableReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplStateMachine_Variable39"):
                opp_val = getattr(old_value, "SimplStateMachine_Variable39", None)
                if opp_val == self:
                    setattr(old_value, "SimplStateMachine_Variable39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplStateMachine_Variable39"):
                opp_val = getattr(value, "SimplStateMachine_Variable39", None)
                setattr(value, "SimplStateMachine_Variable39", self)

class SimplStateMachine_ExpressionElement(ABC):

    pass
class SimplStateMachine_Expression(ExpressionElement):

    def __init__(self, operator: str, _name: str, SimplStateMachine_Expression: "SimplStateMachine_Transition" = None, SimplStateMachine_Expression24: "SimplStateMachine_ExpressionElement" = None, SimplStateMachine_Expression26: "SimplStateMachine_ExpressionElement" = None):
        self.operator = operator
        self._name = _name
        self.SimplStateMachine_Expression = SimplStateMachine_Expression
        self.SimplStateMachine_Expression24 = SimplStateMachine_Expression24
        self.SimplStateMachine_Expression26 = SimplStateMachine_Expression26
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def _name(self) -> str:
        return self.___name

    @_name.setter
    def _name(self, _name: str):
        self.___name = _name

    @property
    def SimplStateMachine_Expression26(self):
        return self.__SimplStateMachine_Expression26

    @SimplStateMachine_Expression26.setter
    def SimplStateMachine_Expression26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachine_Expression__SimplStateMachine_Expression26", None)
        self.__SimplStateMachine_Expression26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplStateMachine_ExpressionElement27"):
                opp_val = getattr(old_value, "SimplStateMachine_ExpressionElement27", None)
                if opp_val == self:
                    setattr(old_value, "SimplStateMachine_ExpressionElement27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplStateMachine_ExpressionElement27"):
                opp_val = getattr(value, "SimplStateMachine_ExpressionElement27", None)
                setattr(value, "SimplStateMachine_ExpressionElement27", self)

    @property
    def SimplStateMachine_Expression(self):
        return self.__SimplStateMachine_Expression

    @SimplStateMachine_Expression.setter
    def SimplStateMachine_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachine_Expression__SimplStateMachine_Expression", None)
        self.__SimplStateMachine_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplStateMachine_Transition22"):
                opp_val = getattr(old_value, "SimplStateMachine_Transition22", None)
                if opp_val == self:
                    setattr(old_value, "SimplStateMachine_Transition22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplStateMachine_Transition22"):
                opp_val = getattr(value, "SimplStateMachine_Transition22", None)
                setattr(value, "SimplStateMachine_Transition22", self)

    @property
    def SimplStateMachine_Expression24(self):
        return self.__SimplStateMachine_Expression24

    @SimplStateMachine_Expression24.setter
    def SimplStateMachine_Expression24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachine_Expression__SimplStateMachine_Expression24", None)
        self.__SimplStateMachine_Expression24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplStateMachine_ExpressionElement"):
                opp_val = getattr(old_value, "SimplStateMachine_ExpressionElement", None)
                if opp_val == self:
                    setattr(old_value, "SimplStateMachine_ExpressionElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplStateMachine_ExpressionElement"):
                opp_val = getattr(value, "SimplStateMachine_ExpressionElement", None)
                setattr(value, "SimplStateMachine_ExpressionElement", self)

class SimplStateMachine_BooleanVariable(Variable):

    pass
class SimplStateMachine_InitialState:

    pass
class State:

    pass
class SimplStateMachine_Operation:

    pass
class SimplStateMachine_CompositeState(State):

    def __init__(self, CompositeState: "SimplStateMachine_State" = None, container: set["SimplStateMachine_State"] = None, SimplStateMachine_CompositeState: "SimplStateMachine_InitialState" = None):
        self.CompositeState = CompositeState
        self.container = container if container is not None else set()
        self.SimplStateMachine_CompositeState = SimplStateMachine_CompositeState
        
    @property
    def container(self):
        return self.__container

    @container.setter
    def container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachine_CompositeState__container", None)
        self.__container = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    if opp_val == self:
                        setattr(item, "State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    setattr(item, "State", self)
                    

    @property
    def SimplStateMachine_CompositeState(self):
        return self.__SimplStateMachine_CompositeState

    @SimplStateMachine_CompositeState.setter
    def SimplStateMachine_CompositeState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachine_CompositeState__SimplStateMachine_CompositeState", None)
        self.__SimplStateMachine_CompositeState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplStateMachine_InitialState"):
                opp_val = getattr(old_value, "SimplStateMachine_InitialState", None)
                if opp_val == self:
                    setattr(old_value, "SimplStateMachine_InitialState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplStateMachine_InitialState"):
                opp_val = getattr(value, "SimplStateMachine_InitialState", None)
                setattr(value, "SimplStateMachine_InitialState", self)

    @property
    def CompositeState(self):
        return self.__CompositeState

    @CompositeState.setter
    def CompositeState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachine_CompositeState__CompositeState", None)
        self.__CompositeState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "states"):
                opp_val = getattr(old_value, "states", None)
                if opp_val == self:
                    setattr(old_value, "states", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "states"):
                opp_val = getattr(value, "states", None)
                setattr(value, "states", self)

    def unactiveSubTree(self) -> bool:
        # TODO: Implement unactiveSubTree method
        pass

    def activeSubTree(self) -> bool:
        # TODO: Implement activeSubTree method
        pass

class SimplStateMachine_State:

    def __init__(self, name: str, isActive: bool, SimplStateMachine_State14: "SimplStateMachine_Transition" = None, SimplStateMachine_State17: "SimplStateMachine_Transition" = None, states: "SimplStateMachine_CompositeState" = None, SimplStateMachine_State: "SimplStateMachine_Operation" = None, State: "SimplStateMachine_CompositeState" = None, SimplStateMachine_State11: "SimplStateMachine_InitialState" = None):
        self.name = name
        self.isActive = isActive
        self.SimplStateMachine_State14 = SimplStateMachine_State14
        self.SimplStateMachine_State17 = SimplStateMachine_State17
        self.states = states
        self.SimplStateMachine_State = SimplStateMachine_State
        self.State = State
        self.SimplStateMachine_State11 = SimplStateMachine_State11
        
    @property
    def isActive(self) -> bool:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: bool):
        self.__isActive = isActive

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SimplStateMachine_State11(self):
        return self.__SimplStateMachine_State11

    @SimplStateMachine_State11.setter
    def SimplStateMachine_State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachine_State__SimplStateMachine_State11", None)
        self.__SimplStateMachine_State11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplStateMachine_InitialState10"):
                opp_val = getattr(old_value, "SimplStateMachine_InitialState10", None)
                if opp_val == self:
                    setattr(old_value, "SimplStateMachine_InitialState10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplStateMachine_InitialState10"):
                opp_val = getattr(value, "SimplStateMachine_InitialState10", None)
                setattr(value, "SimplStateMachine_InitialState10", self)

    @property
    def SimplStateMachine_State14(self):
        return self.__SimplStateMachine_State14

    @SimplStateMachine_State14.setter
    def SimplStateMachine_State14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachine_State__SimplStateMachine_State14", None)
        self.__SimplStateMachine_State14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplStateMachine_Transition13"):
                opp_val = getattr(old_value, "SimplStateMachine_Transition13", None)
                if opp_val == self:
                    setattr(old_value, "SimplStateMachine_Transition13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplStateMachine_Transition13"):
                opp_val = getattr(value, "SimplStateMachine_Transition13", None)
                setattr(value, "SimplStateMachine_Transition13", self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachine_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "container"):
                opp_val = getattr(old_value, "container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "container"):
                opp_val = getattr(value, "container", None)
                if opp_val is None:
                    setattr(value, "container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SimplStateMachine_State17(self):
        return self.__SimplStateMachine_State17

    @SimplStateMachine_State17.setter
    def SimplStateMachine_State17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachine_State__SimplStateMachine_State17", None)
        self.__SimplStateMachine_State17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplStateMachine_Transition16"):
                opp_val = getattr(old_value, "SimplStateMachine_Transition16", None)
                if opp_val == self:
                    setattr(old_value, "SimplStateMachine_Transition16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplStateMachine_Transition16"):
                opp_val = getattr(value, "SimplStateMachine_Transition16", None)
                setattr(value, "SimplStateMachine_Transition16", self)

    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachine_State__states", None)
        self.__states = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompositeState"):
                opp_val = getattr(old_value, "CompositeState", None)
                if opp_val == self:
                    setattr(old_value, "CompositeState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompositeState"):
                opp_val = getattr(value, "CompositeState", None)
                setattr(value, "CompositeState", self)

    @property
    def SimplStateMachine_State(self):
        return self.__SimplStateMachine_State

    @SimplStateMachine_State.setter
    def SimplStateMachine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachine_State__SimplStateMachine_State", None)
        self.__SimplStateMachine_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplStateMachine_Operation"):
                opp_val = getattr(old_value, "SimplStateMachine_Operation", None)
                if opp_val == self:
                    setattr(old_value, "SimplStateMachine_Operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplStateMachine_Operation"):
                opp_val = getattr(value, "SimplStateMachine_Operation", None)
                setattr(value, "SimplStateMachine_Operation", self)

class SimplStateMachine_Variable(ABC):

    def __init__(self, name: str, SimplStateMachine_Variable: "SimplStateMachine_StateMachine" = None, SimplStateMachine_Variable29: "SimplStateMachine_Data" = None, SimplStateMachine_Variable37: "SimplStateMachine_Assignment" = None, SimplStateMachine_Variable39: "SimplStateMachine_VariableReference" = None):
        self.name = name
        self.SimplStateMachine_Variable = SimplStateMachine_Variable
        self.SimplStateMachine_Variable29 = SimplStateMachine_Variable29
        self.SimplStateMachine_Variable37 = SimplStateMachine_Variable37
        self.SimplStateMachine_Variable39 = SimplStateMachine_Variable39
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SimplStateMachine_Variable39(self):
        return self.__SimplStateMachine_Variable39

    @SimplStateMachine_Variable39.setter
    def SimplStateMachine_Variable39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachine_Variable__SimplStateMachine_Variable39", None)
        self.__SimplStateMachine_Variable39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplStateMachine_VariableReference"):
                opp_val = getattr(old_value, "SimplStateMachine_VariableReference", None)
                if opp_val == self:
                    setattr(old_value, "SimplStateMachine_VariableReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplStateMachine_VariableReference"):
                opp_val = getattr(value, "SimplStateMachine_VariableReference", None)
                setattr(value, "SimplStateMachine_VariableReference", self)

    @property
    def SimplStateMachine_Variable37(self):
        return self.__SimplStateMachine_Variable37

    @SimplStateMachine_Variable37.setter
    def SimplStateMachine_Variable37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachine_Variable__SimplStateMachine_Variable37", None)
        self.__SimplStateMachine_Variable37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplStateMachine_Assignment36"):
                opp_val = getattr(old_value, "SimplStateMachine_Assignment36", None)
                if opp_val == self:
                    setattr(old_value, "SimplStateMachine_Assignment36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplStateMachine_Assignment36"):
                opp_val = getattr(value, "SimplStateMachine_Assignment36", None)
                setattr(value, "SimplStateMachine_Assignment36", self)

    @property
    def SimplStateMachine_Variable(self):
        return self.__SimplStateMachine_Variable

    @SimplStateMachine_Variable.setter
    def SimplStateMachine_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachine_Variable__SimplStateMachine_Variable", None)
        self.__SimplStateMachine_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplStateMachine_StateMachine4"):
                opp_val = getattr(old_value, "SimplStateMachine_StateMachine4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplStateMachine_StateMachine4"):
                opp_val = getattr(value, "SimplStateMachine_StateMachine4", None)
                if opp_val is None:
                    setattr(value, "SimplStateMachine_StateMachine4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SimplStateMachine_Variable29(self):
        return self.__SimplStateMachine_Variable29

    @SimplStateMachine_Variable29.setter
    def SimplStateMachine_Variable29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachine_Variable__SimplStateMachine_Variable29", None)
        self.__SimplStateMachine_Variable29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplStateMachine_Data"):
                opp_val = getattr(old_value, "SimplStateMachine_Data", None)
                if opp_val == self:
                    setattr(old_value, "SimplStateMachine_Data", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplStateMachine_Data"):
                opp_val = getattr(value, "SimplStateMachine_Data", None)
                setattr(value, "SimplStateMachine_Data", self)

class CompositeState:

    pass
class SimplStateMachine_StateMachine(CompositeState):

    pass
class SimplStateMachine_Event:

    def __init__(self, name: str, SimplStateMachine_Event: "SimplStateMachine_StateMachine" = None, SimplStateMachine_Event20: "SimplStateMachine_Transition" = None):
        self.name = name
        self.SimplStateMachine_Event = SimplStateMachine_Event
        self.SimplStateMachine_Event20 = SimplStateMachine_Event20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SimplStateMachine_Event(self):
        return self.__SimplStateMachine_Event

    @SimplStateMachine_Event.setter
    def SimplStateMachine_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachine_Event__SimplStateMachine_Event", None)
        self.__SimplStateMachine_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplStateMachine_StateMachine2"):
                opp_val = getattr(old_value, "SimplStateMachine_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplStateMachine_StateMachine2"):
                opp_val = getattr(value, "SimplStateMachine_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "SimplStateMachine_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SimplStateMachine_Event20(self):
        return self.__SimplStateMachine_Event20

    @SimplStateMachine_Event20.setter
    def SimplStateMachine_Event20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachine_Event__SimplStateMachine_Event20", None)
        self.__SimplStateMachine_Event20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplStateMachine_Transition19"):
                opp_val = getattr(old_value, "SimplStateMachine_Transition19", None)
                if opp_val == self:
                    setattr(old_value, "SimplStateMachine_Transition19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplStateMachine_Transition19"):
                opp_val = getattr(value, "SimplStateMachine_Transition19", None)
                setattr(value, "SimplStateMachine_Transition19", self)

class SimplStateMachine_Transition:

    pass