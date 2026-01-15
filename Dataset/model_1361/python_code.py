from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class State:

    pass
class statemachine_InitialState(State):

    pass
class statemachine_FinalState(State):

    pass
class statemachine_NormalState(State):

    pass
class statemachine_Action:

    def __init__(self, actionLabel: str, actionStatement: str, statemachine_Action: "statemachine_NormalState" = None):
        self.actionLabel = actionLabel
        self.actionStatement = actionStatement
        self.statemachine_Action = statemachine_Action
        
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
    def statemachine_Action(self):
        return self.__statemachine_Action

    @statemachine_Action.setter
    def statemachine_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Action__statemachine_Action", None)
        self.__statemachine_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_NormalState"):
                opp_val = getattr(old_value, "statemachine_NormalState", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_NormalState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_NormalState"):
                opp_val = getattr(value, "statemachine_NormalState", None)
                setattr(value, "statemachine_NormalState", self)

class Declaration:

    pass
class statemachine_State(Declaration):

    def __init__(self, label: str, id: int, statemachine_State: "statemachine_Transition" = None, statemachine_State6: "statemachine_Transition" = None, statemachine_State9: "statemachine_State" = None, statemachine_State7: set["statemachine_State"] = None, statemachine_State12: "statemachine_State" = None, statemachine_State10: set["statemachine_State"] = None, statemachine_State14: set["statemachine_Transition"] = None):
        self.label = label
        self.id = id
        self.statemachine_State = statemachine_State
        self.statemachine_State6 = statemachine_State6
        self.statemachine_State9 = statemachine_State9
        self.statemachine_State7 = statemachine_State7 if statemachine_State7 is not None else set()
        self.statemachine_State12 = statemachine_State12
        self.statemachine_State10 = statemachine_State10 if statemachine_State10 is not None else set()
        self.statemachine_State14 = statemachine_State14 if statemachine_State14 is not None else set()
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def statemachine_State10(self):
        return self.__statemachine_State10

    @statemachine_State10.setter
    def statemachine_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State10", None)
        self.__statemachine_State10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_State12"):
                    opp_val = getattr(item, "statemachine_State12", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_State12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_State12"):
                    opp_val = getattr(item, "statemachine_State12", None)
                    
                    setattr(item, "statemachine_State12", self)
                    

    @property
    def statemachine_State7(self):
        return self.__statemachine_State7

    @statemachine_State7.setter
    def statemachine_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State7", None)
        self.__statemachine_State7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_State9"):
                    opp_val = getattr(item, "statemachine_State9", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_State9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_State9"):
                    opp_val = getattr(item, "statemachine_State9", None)
                    
                    setattr(item, "statemachine_State9", self)
                    

    @property
    def statemachine_State(self):
        return self.__statemachine_State

    @statemachine_State.setter
    def statemachine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State", None)
        self.__statemachine_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition"):
                opp_val = getattr(old_value, "statemachine_Transition", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition"):
                opp_val = getattr(value, "statemachine_Transition", None)
                setattr(value, "statemachine_Transition", self)

    @property
    def statemachine_State6(self):
        return self.__statemachine_State6

    @statemachine_State6.setter
    def statemachine_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State6", None)
        self.__statemachine_State6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition5"):
                opp_val = getattr(old_value, "statemachine_Transition5", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition5"):
                opp_val = getattr(value, "statemachine_Transition5", None)
                setattr(value, "statemachine_Transition5", self)

    @property
    def statemachine_State9(self):
        return self.__statemachine_State9

    @statemachine_State9.setter
    def statemachine_State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State9", None)
        self.__statemachine_State9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State7"):
                opp_val = getattr(old_value, "statemachine_State7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State7"):
                opp_val = getattr(value, "statemachine_State7", None)
                if opp_val is None:
                    setattr(value, "statemachine_State7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_State14(self):
        return self.__statemachine_State14

    @statemachine_State14.setter
    def statemachine_State14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State14", None)
        self.__statemachine_State14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Transition15"):
                    opp_val = getattr(item, "statemachine_Transition15", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Transition15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Transition15"):
                    opp_val = getattr(item, "statemachine_Transition15", None)
                    
                    setattr(item, "statemachine_Transition15", self)
                    

    @property
    def statemachine_State12(self):
        return self.__statemachine_State12

    @statemachine_State12.setter
    def statemachine_State12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State12", None)
        self.__statemachine_State12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State10"):
                opp_val = getattr(old_value, "statemachine_State10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State10"):
                opp_val = getattr(value, "statemachine_State10", None)
                if opp_val is None:
                    setattr(value, "statemachine_State10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def printReachable(self):
        # TODO: Implement printReachable method
        pass

class statemachine_Transition(Declaration):

    def __init__(self, label: str, sourceLabel: str, targetLabel: str, guardLabel: str, actionLabel: str, guardExpression: str, actionStatement: str, statemachine_Transition: "statemachine_State" = None, statemachine_Transition5: "statemachine_State" = None, statemachine_Transition15: "statemachine_State" = None):
        self.label = label
        self.sourceLabel = sourceLabel
        self.targetLabel = targetLabel
        self.guardLabel = guardLabel
        self.actionLabel = actionLabel
        self.guardExpression = guardExpression
        self.actionStatement = actionStatement
        self.statemachine_Transition = statemachine_Transition
        self.statemachine_Transition5 = statemachine_Transition5
        self.statemachine_Transition15 = statemachine_Transition15
        
    @property
    def guardExpression(self) -> str:
        return self.__guardExpression

    @guardExpression.setter
    def guardExpression(self, guardExpression: str):
        self.__guardExpression = guardExpression

    @property
    def actionStatement(self) -> str:
        return self.__actionStatement

    @actionStatement.setter
    def actionStatement(self, actionStatement: str):
        self.__actionStatement = actionStatement

    @property
    def guardLabel(self) -> str:
        return self.__guardLabel

    @guardLabel.setter
    def guardLabel(self, guardLabel: str):
        self.__guardLabel = guardLabel

    @property
    def targetLabel(self) -> str:
        return self.__targetLabel

    @targetLabel.setter
    def targetLabel(self, targetLabel: str):
        self.__targetLabel = targetLabel

    @property
    def actionLabel(self) -> str:
        return self.__actionLabel

    @actionLabel.setter
    def actionLabel(self, actionLabel: str):
        self.__actionLabel = actionLabel

    @property
    def sourceLabel(self) -> str:
        return self.__sourceLabel

    @sourceLabel.setter
    def sourceLabel(self, sourceLabel: str):
        self.__sourceLabel = sourceLabel

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def statemachine_Transition(self):
        return self.__statemachine_Transition

    @statemachine_Transition.setter
    def statemachine_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition", None)
        self.__statemachine_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State"):
                opp_val = getattr(old_value, "statemachine_State", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State"):
                opp_val = getattr(value, "statemachine_State", None)
                setattr(value, "statemachine_State", self)

    @property
    def statemachine_Transition5(self):
        return self.__statemachine_Transition5

    @statemachine_Transition5.setter
    def statemachine_Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition5", None)
        self.__statemachine_Transition5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State6"):
                opp_val = getattr(old_value, "statemachine_State6", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_State6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State6"):
                opp_val = getattr(value, "statemachine_State6", None)
                setattr(value, "statemachine_State6", self)

    @property
    def statemachine_Transition15(self):
        return self.__statemachine_Transition15

    @statemachine_Transition15.setter
    def statemachine_Transition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition15", None)
        self.__statemachine_Transition15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State14"):
                opp_val = getattr(old_value, "statemachine_State14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State14"):
                opp_val = getattr(value, "statemachine_State14", None)
                if opp_val is None:
                    setattr(value, "statemachine_State14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemachine_StateMachineVariable:

    def __init__(self, type: str, name: str, statemachine_StateMachineVariable: "statemachine_StateMachine" = None):
        self.type = type
        self.name = name
        self.statemachine_StateMachineVariable = statemachine_StateMachineVariable
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statemachine_StateMachineVariable(self):
        return self.__statemachine_StateMachineVariable

    @statemachine_StateMachineVariable.setter
    def statemachine_StateMachineVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_StateMachineVariable__statemachine_StateMachineVariable", None)
        self.__statemachine_StateMachineVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_StateMachine2"):
                opp_val = getattr(old_value, "statemachine_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_StateMachine2"):
                opp_val = getattr(value, "statemachine_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "statemachine_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemachine_Declaration(ABC):

    def __init__(self, statemachine_Declaration: "statemachine_StateMachine" = None):
        self.statemachine_Declaration = statemachine_Declaration
        
    @property
    def statemachine_Declaration(self):
        return self.__statemachine_Declaration

    @statemachine_Declaration.setter
    def statemachine_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Declaration__statemachine_Declaration", None)
        self.__statemachine_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_StateMachine"):
                opp_val = getattr(old_value, "statemachine_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_StateMachine"):
                opp_val = getattr(value, "statemachine_StateMachine", None)
                if opp_val is None:
                    setattr(value, "statemachine_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def printReachable(self):
        # TODO: Implement printReachable method
        pass

class statemachine_StateMachine:

    def __init__(self, statemachine_StateMachine: set["statemachine_Declaration"] = None, statemachine_StateMachine2: set["statemachine_StateMachineVariable"] = None):
        self.statemachine_StateMachine = statemachine_StateMachine if statemachine_StateMachine is not None else set()
        self.statemachine_StateMachine2 = statemachine_StateMachine2 if statemachine_StateMachine2 is not None else set()
        
    @property
    def statemachine_StateMachine2(self):
        return self.__statemachine_StateMachine2

    @statemachine_StateMachine2.setter
    def statemachine_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_StateMachine__statemachine_StateMachine2", None)
        self.__statemachine_StateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_StateMachineVariable"):
                    opp_val = getattr(item, "statemachine_StateMachineVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_StateMachineVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_StateMachineVariable"):
                    opp_val = getattr(item, "statemachine_StateMachineVariable", None)
                    
                    setattr(item, "statemachine_StateMachineVariable", self)
                    

    @property
    def statemachine_StateMachine(self):
        return self.__statemachine_StateMachine

    @statemachine_StateMachine.setter
    def statemachine_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_StateMachine__statemachine_StateMachine", None)
        self.__statemachine_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Declaration"):
                    opp_val = getattr(item, "statemachine_Declaration", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Declaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Declaration"):
                    opp_val = getattr(item, "statemachine_Declaration", None)
                    
                    setattr(item, "statemachine_Declaration", self)
                    

    def printReachable(self):
        # TODO: Implement printReachable method
        pass
