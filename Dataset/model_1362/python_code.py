from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class State:

    pass
class statemachine103_FinalState(State):

    pass
class statemachine103_InitialState(State):

    pass
class statemachine103_NormalState(State):

    pass
class statemachine103_Action:

    def __init__(self, actionLabel: str, actionStatement: str, statemachine103_Action11: "statemachine103_Action" = None, statemachine103_Action9: "statemachine103_Action" = None, statemachine103_Action: "statemachine103_Transition" = None, statemachine103_Action13: "statemachine103_NormalState" = None):
        self.actionLabel = actionLabel
        self.actionStatement = actionStatement
        self.statemachine103_Action11 = statemachine103_Action11
        self.statemachine103_Action9 = statemachine103_Action9
        self.statemachine103_Action = statemachine103_Action
        self.statemachine103_Action13 = statemachine103_Action13
        
    @property
    def actionLabel(self) -> str:
        return self.__actionLabel

    @actionLabel.setter
    def actionLabel(self, actionLabel: str):
        self.__actionLabel = actionLabel

    @property
    def actionStatement(self) -> str:
        return self.__actionStatement

    @actionStatement.setter
    def actionStatement(self, actionStatement: str):
        self.__actionStatement = actionStatement

    @property
    def statemachine103_Action11(self):
        return self.__statemachine103_Action11

    @statemachine103_Action11.setter
    def statemachine103_Action11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine103_Action__statemachine103_Action11", None)
        self.__statemachine103_Action11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine103_Action9"):
                opp_val = getattr(old_value, "statemachine103_Action9", None)
                if opp_val == self:
                    setattr(old_value, "statemachine103_Action9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine103_Action9"):
                opp_val = getattr(value, "statemachine103_Action9", None)
                setattr(value, "statemachine103_Action9", self)

    @property
    def statemachine103_Action(self):
        return self.__statemachine103_Action

    @statemachine103_Action.setter
    def statemachine103_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine103_Action__statemachine103_Action", None)
        self.__statemachine103_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine103_Transition8"):
                opp_val = getattr(old_value, "statemachine103_Transition8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine103_Transition8"):
                opp_val = getattr(value, "statemachine103_Transition8", None)
                if opp_val is None:
                    setattr(value, "statemachine103_Transition8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine103_Action9(self):
        return self.__statemachine103_Action9

    @statemachine103_Action9.setter
    def statemachine103_Action9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine103_Action__statemachine103_Action9", None)
        self.__statemachine103_Action9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine103_Action11"):
                opp_val = getattr(old_value, "statemachine103_Action11", None)
                if opp_val == self:
                    setattr(old_value, "statemachine103_Action11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine103_Action11"):
                opp_val = getattr(value, "statemachine103_Action11", None)
                setattr(value, "statemachine103_Action11", self)

    @property
    def statemachine103_Action13(self):
        return self.__statemachine103_Action13

    @statemachine103_Action13.setter
    def statemachine103_Action13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine103_Action__statemachine103_Action13", None)
        self.__statemachine103_Action13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine103_NormalState"):
                opp_val = getattr(old_value, "statemachine103_NormalState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine103_NormalState"):
                opp_val = getattr(value, "statemachine103_NormalState", None)
                if opp_val is None:
                    setattr(value, "statemachine103_NormalState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class StateMachineObject:

    pass
class statemachine103_Transition(StateMachineObject):

    def __init__(self, guardLabel: str, guardExpression: str, statemachine103_Transition: "statemachine103_State" = None, statemachine103_Transition5: "statemachine103_State" = None, statemachine103_Transition8: set["statemachine103_Action"] = None):
        self.guardLabel = guardLabel
        self.guardExpression = guardExpression
        self.statemachine103_Transition = statemachine103_Transition
        self.statemachine103_Transition5 = statemachine103_Transition5
        self.statemachine103_Transition8 = statemachine103_Transition8 if statemachine103_Transition8 is not None else set()
        
    @property
    def guardLabel(self) -> str:
        return self.__guardLabel

    @guardLabel.setter
    def guardLabel(self, guardLabel: str):
        self.__guardLabel = guardLabel

    @property
    def guardExpression(self) -> str:
        return self.__guardExpression

    @guardExpression.setter
    def guardExpression(self, guardExpression: str):
        self.__guardExpression = guardExpression

    @property
    def statemachine103_Transition5(self):
        return self.__statemachine103_Transition5

    @statemachine103_Transition5.setter
    def statemachine103_Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine103_Transition__statemachine103_Transition5", None)
        self.__statemachine103_Transition5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine103_State6"):
                opp_val = getattr(old_value, "statemachine103_State6", None)
                if opp_val == self:
                    setattr(old_value, "statemachine103_State6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine103_State6"):
                opp_val = getattr(value, "statemachine103_State6", None)
                setattr(value, "statemachine103_State6", self)

    @property
    def statemachine103_Transition(self):
        return self.__statemachine103_Transition

    @statemachine103_Transition.setter
    def statemachine103_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine103_Transition__statemachine103_Transition", None)
        self.__statemachine103_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine103_State"):
                opp_val = getattr(old_value, "statemachine103_State", None)
                if opp_val == self:
                    setattr(old_value, "statemachine103_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine103_State"):
                opp_val = getattr(value, "statemachine103_State", None)
                setattr(value, "statemachine103_State", self)

    @property
    def statemachine103_Transition8(self):
        return self.__statemachine103_Transition8

    @statemachine103_Transition8.setter
    def statemachine103_Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine103_Transition__statemachine103_Transition8", None)
        self.__statemachine103_Transition8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine103_Action"):
                    opp_val = getattr(item, "statemachine103_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine103_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine103_Action"):
                    opp_val = getattr(item, "statemachine103_Action", None)
                    
                    setattr(item, "statemachine103_Action", self)
                    

class statemachine103_StateMachineVariable:

    def __init__(self, type: str, name: str, statemachine103_StateMachineVariable: "statemachine103_StateMachine" = None):
        self.type = type
        self.name = name
        self.statemachine103_StateMachineVariable = statemachine103_StateMachineVariable
        
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
    def statemachine103_StateMachineVariable(self):
        return self.__statemachine103_StateMachineVariable

    @statemachine103_StateMachineVariable.setter
    def statemachine103_StateMachineVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine103_StateMachineVariable__statemachine103_StateMachineVariable", None)
        self.__statemachine103_StateMachineVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine103_StateMachine2"):
                opp_val = getattr(old_value, "statemachine103_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine103_StateMachine2"):
                opp_val = getattr(value, "statemachine103_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "statemachine103_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemachine103_State(StateMachineObject):

    def __init__(self, id: int, statemachine103_State: "statemachine103_Transition" = None, statemachine103_State6: "statemachine103_Transition" = None):
        self.id = id
        self.statemachine103_State = statemachine103_State
        self.statemachine103_State6 = statemachine103_State6
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def statemachine103_State6(self):
        return self.__statemachine103_State6

    @statemachine103_State6.setter
    def statemachine103_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine103_State__statemachine103_State6", None)
        self.__statemachine103_State6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine103_Transition5"):
                opp_val = getattr(old_value, "statemachine103_Transition5", None)
                if opp_val == self:
                    setattr(old_value, "statemachine103_Transition5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine103_Transition5"):
                opp_val = getattr(value, "statemachine103_Transition5", None)
                setattr(value, "statemachine103_Transition5", self)

    @property
    def statemachine103_State(self):
        return self.__statemachine103_State

    @statemachine103_State.setter
    def statemachine103_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine103_State__statemachine103_State", None)
        self.__statemachine103_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine103_Transition"):
                opp_val = getattr(old_value, "statemachine103_Transition", None)
                if opp_val == self:
                    setattr(old_value, "statemachine103_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine103_Transition"):
                opp_val = getattr(value, "statemachine103_Transition", None)
                setattr(value, "statemachine103_Transition", self)

class statemachine103_StateMachineObject(ABC):

    def __init__(self, label: str, statemachine103_StateMachineObject: "statemachine103_StateMachine" = None):
        self.label = label
        self.statemachine103_StateMachineObject = statemachine103_StateMachineObject
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def statemachine103_StateMachineObject(self):
        return self.__statemachine103_StateMachineObject

    @statemachine103_StateMachineObject.setter
    def statemachine103_StateMachineObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine103_StateMachineObject__statemachine103_StateMachineObject", None)
        self.__statemachine103_StateMachineObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine103_StateMachine"):
                opp_val = getattr(old_value, "statemachine103_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine103_StateMachine"):
                opp_val = getattr(value, "statemachine103_StateMachine", None)
                if opp_val is None:
                    setattr(value, "statemachine103_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemachine103_StateMachine:

    def __init__(self, label: str, statemachine103_StateMachine: set["statemachine103_StateMachineObject"] = None, statemachine103_StateMachine2: set["statemachine103_StateMachineVariable"] = None):
        self.label = label
        self.statemachine103_StateMachine = statemachine103_StateMachine if statemachine103_StateMachine is not None else set()
        self.statemachine103_StateMachine2 = statemachine103_StateMachine2 if statemachine103_StateMachine2 is not None else set()
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def statemachine103_StateMachine(self):
        return self.__statemachine103_StateMachine

    @statemachine103_StateMachine.setter
    def statemachine103_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine103_StateMachine__statemachine103_StateMachine", None)
        self.__statemachine103_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine103_StateMachineObject"):
                    opp_val = getattr(item, "statemachine103_StateMachineObject", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine103_StateMachineObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine103_StateMachineObject"):
                    opp_val = getattr(item, "statemachine103_StateMachineObject", None)
                    
                    setattr(item, "statemachine103_StateMachineObject", self)
                    

    @property
    def statemachine103_StateMachine2(self):
        return self.__statemachine103_StateMachine2

    @statemachine103_StateMachine2.setter
    def statemachine103_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine103_StateMachine__statemachine103_StateMachine2", None)
        self.__statemachine103_StateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine103_StateMachineVariable"):
                    opp_val = getattr(item, "statemachine103_StateMachineVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine103_StateMachineVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine103_StateMachineVariable"):
                    opp_val = getattr(item, "statemachine103_StateMachineVariable", None)
                    
                    setattr(item, "statemachine103_StateMachineVariable", self)
                    
