from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DecompositionType(Enum):
    EXCLUSIVE_OR = "EXCLUSIVE_OR"
    PARALLEL_AND = "PARALLEL_AND"


############################################
# Definition of Classes
############################################

class Reference:

    pass
class simulink_ModelReference(Reference):

    def __init__(self, modelName: str):
        self.modelName = modelName
        
    @property
    def modelName(self) -> str:
        return self.__modelName

    @modelName.setter
    def modelName(self, modelName: str):
        self.__modelName = modelName

class simulink_BlockReference(Reference):

    pass
class OutPort:

    pass
class InPort:

    pass
class Data:

    pass
class simulink_OutputData(OutPort, Data):

    pass
class simulink_LocalData(Data):

    def __init__(self, dataType: str):
        self.dataType = dataType
        
    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

class simulink_InputData(InPort, Data):

    pass
class TruthTable:

    pass
class simulink_DecisionEntry:

    def __init__(self, conditionOutcome: str, simulink_DecisionEntry: "simulink_Decision" = None, simulink_DecisionEntry58: "simulink_Condition" = None):
        self.conditionOutcome = conditionOutcome
        self.simulink_DecisionEntry = simulink_DecisionEntry
        self.simulink_DecisionEntry58 = simulink_DecisionEntry58
        
    @property
    def conditionOutcome(self) -> str:
        return self.__conditionOutcome

    @conditionOutcome.setter
    def conditionOutcome(self, conditionOutcome: str):
        self.__conditionOutcome = conditionOutcome

    @property
    def simulink_DecisionEntry58(self):
        return self.__simulink_DecisionEntry58

    @simulink_DecisionEntry58.setter
    def simulink_DecisionEntry58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_DecisionEntry__simulink_DecisionEntry58", None)
        self.__simulink_DecisionEntry58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_Condition59"):
                opp_val = getattr(old_value, "simulink_Condition59", None)
                if opp_val == self:
                    setattr(old_value, "simulink_Condition59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_Condition59"):
                opp_val = getattr(value, "simulink_Condition59", None)
                setattr(value, "simulink_Condition59", self)

    @property
    def simulink_DecisionEntry(self):
        return self.__simulink_DecisionEntry

    @simulink_DecisionEntry.setter
    def simulink_DecisionEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_DecisionEntry__simulink_DecisionEntry", None)
        self.__simulink_DecisionEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_Decision56"):
                opp_val = getattr(old_value, "simulink_Decision56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_Decision56"):
                opp_val = getattr(value, "simulink_Decision56", None)
                if opp_val is None:
                    setattr(value, "simulink_Decision56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simulink_ActionEntry:

    def __init__(self, actionReference: str, description: str, actionStatement: str, simulink_ActionEntry: "simulink_ActionTable" = None):
        self.actionReference = actionReference
        self.description = description
        self.actionStatement = actionStatement
        self.simulink_ActionEntry = simulink_ActionEntry
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def actionReference(self) -> str:
        return self.__actionReference

    @actionReference.setter
    def actionReference(self, actionReference: str):
        self.__actionReference = actionReference

    @property
    def actionStatement(self) -> str:
        return self.__actionStatement

    @actionStatement.setter
    def actionStatement(self, actionStatement: str):
        self.__actionStatement = actionStatement

    @property
    def simulink_ActionEntry(self):
        return self.__simulink_ActionEntry

    @simulink_ActionEntry.setter
    def simulink_ActionEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_ActionEntry__simulink_ActionEntry", None)
        self.__simulink_ActionEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_ActionTable54"):
                opp_val = getattr(old_value, "simulink_ActionTable54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_ActionTable54"):
                opp_val = getattr(value, "simulink_ActionTable54", None)
                if opp_val is None:
                    setattr(value, "simulink_ActionTable54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simulink_Condition:

    def __init__(self, description: str, statement: str, simulink_Condition: "simulink_ConditionTable" = None, simulink_Condition59: "simulink_DecisionEntry" = None):
        self.description = description
        self.statement = statement
        self.simulink_Condition = simulink_Condition
        self.simulink_Condition59 = simulink_Condition59
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def statement(self) -> str:
        return self.__statement

    @statement.setter
    def statement(self, statement: str):
        self.__statement = statement

    @property
    def simulink_Condition59(self):
        return self.__simulink_Condition59

    @simulink_Condition59.setter
    def simulink_Condition59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Condition__simulink_Condition59", None)
        self.__simulink_Condition59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_DecisionEntry58"):
                opp_val = getattr(old_value, "simulink_DecisionEntry58", None)
                if opp_val == self:
                    setattr(old_value, "simulink_DecisionEntry58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_DecisionEntry58"):
                opp_val = getattr(value, "simulink_DecisionEntry58", None)
                setattr(value, "simulink_DecisionEntry58", self)

    @property
    def simulink_Condition(self):
        return self.__simulink_Condition

    @simulink_Condition.setter
    def simulink_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Condition__simulink_Condition", None)
        self.__simulink_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_ConditionTable52"):
                opp_val = getattr(old_value, "simulink_ConditionTable52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_ConditionTable52"):
                opp_val = getattr(value, "simulink_ConditionTable52", None)
                if opp_val is None:
                    setattr(value, "simulink_ConditionTable52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simulink_Decision:

    def __init__(self, actionReference: str, id: int, simulink_Decision: "simulink_ConditionTable" = None, simulink_Decision56: set["simulink_DecisionEntry"] = None):
        self.actionReference = actionReference
        self.id = id
        self.simulink_Decision = simulink_Decision
        self.simulink_Decision56 = simulink_Decision56 if simulink_Decision56 is not None else set()
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def actionReference(self) -> str:
        return self.__actionReference

    @actionReference.setter
    def actionReference(self, actionReference: str):
        self.__actionReference = actionReference

    @property
    def simulink_Decision(self):
        return self.__simulink_Decision

    @simulink_Decision.setter
    def simulink_Decision(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Decision__simulink_Decision", None)
        self.__simulink_Decision = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_ConditionTable50"):
                opp_val = getattr(old_value, "simulink_ConditionTable50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_ConditionTable50"):
                opp_val = getattr(value, "simulink_ConditionTable50", None)
                if opp_val is None:
                    setattr(value, "simulink_ConditionTable50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simulink_Decision56(self):
        return self.__simulink_Decision56

    @simulink_Decision56.setter
    def simulink_Decision56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Decision__simulink_Decision56", None)
        self.__simulink_Decision56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simulink_DecisionEntry"):
                    opp_val = getattr(item, "simulink_DecisionEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "simulink_DecisionEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simulink_DecisionEntry"):
                    opp_val = getattr(item, "simulink_DecisionEntry", None)
                    
                    setattr(item, "simulink_DecisionEntry", self)
                    

class simulink_ActionTable:

    pass
class simulink_ConditionTable:

    pass
class StateflowElement:

    pass
class simulink_TruthTable(StateflowElement):

    pass
class simulink_ContainableStateflowElement(StateflowElement):

    pass
class simulink_CompositeStateflowElement(StateflowElement):

    pass
class simulink_SFWTrigger:

    def __init__(self, statement: str, SFWTrigger: "simulink_Transition" = None, trigger: "simulink_Transition" = None):
        self.statement = statement
        self.SFWTrigger = SFWTrigger
        self.trigger = trigger
        
    @property
    def statement(self) -> str:
        return self.__statement

    @statement.setter
    def statement(self, statement: str):
        self.__statement = statement

    @property
    def SFWTrigger(self):
        return self.__SFWTrigger

    @SFWTrigger.setter
    def SFWTrigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_SFWTrigger__SFWTrigger", None)
        self.__SFWTrigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transition31"):
                opp_val = getattr(old_value, "transition31", None)
                if opp_val == self:
                    setattr(old_value, "transition31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transition31"):
                opp_val = getattr(value, "transition31", None)
                setattr(value, "transition31", self)

    @property
    def trigger(self):
        return self.__trigger

    @trigger.setter
    def trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_SFWTrigger__trigger", None)
        self.__trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transition61"):
                opp_val = getattr(old_value, "Transition61", None)
                if opp_val == self:
                    setattr(old_value, "Transition61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transition61"):
                opp_val = getattr(value, "Transition61", None)
                setattr(value, "Transition61", self)

class simulink_SFWGuard:

    def __init__(self, statement: str, SFWGuard: "simulink_Transition" = None, guard: "simulink_Transition" = None):
        self.statement = statement
        self.SFWGuard = SFWGuard
        self.guard = guard
        
    @property
    def statement(self) -> str:
        return self.__statement

    @statement.setter
    def statement(self, statement: str):
        self.__statement = statement

    @property
    def SFWGuard(self):
        return self.__SFWGuard

    @SFWGuard.setter
    def SFWGuard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_SFWGuard__SFWGuard", None)
        self.__SFWGuard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transition"):
                opp_val = getattr(old_value, "transition", None)
                if opp_val == self:
                    setattr(old_value, "transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transition"):
                opp_val = getattr(value, "transition", None)
                setattr(value, "transition", self)

    @property
    def guard(self):
        return self.__guard

    @guard.setter
    def guard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_SFWGuard__guard", None)
        self.__guard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transition33"):
                opp_val = getattr(old_value, "Transition33", None)
                if opp_val == self:
                    setattr(old_value, "Transition33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transition33"):
                opp_val = getattr(value, "Transition33", None)
                setattr(value, "Transition33", self)

class simulink_Action:

    def __init__(self, statement: str, Action: "simulink_State" = None, Action20: "simulink_State" = None, Action22: "simulink_State" = None, Action29: "simulink_Transition" = None, triggeredActions: "simulink_Transition" = None, entryActions: "simulink_State" = None, duringActions: "simulink_State" = None, exitActions: "simulink_State" = None):
        self.statement = statement
        self.Action = Action
        self.Action20 = Action20
        self.Action22 = Action22
        self.Action29 = Action29
        self.triggeredActions = triggeredActions
        self.entryActions = entryActions
        self.duringActions = duringActions
        self.exitActions = exitActions
        
    @property
    def statement(self) -> str:
        return self.__statement

    @statement.setter
    def statement(self, statement: str):
        self.__statement = statement

    @property
    def Action(self):
        return self.__Action

    @Action.setter
    def Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Action__Action", None)
        self.__Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateEntry"):
                opp_val = getattr(old_value, "stateEntry", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateEntry"):
                opp_val = getattr(value, "stateEntry", None)
                if opp_val is None:
                    setattr(value, "stateEntry", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def entryActions(self):
        return self.__entryActions

    @entryActions.setter
    def entryActions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Action__entryActions", None)
        self.__entryActions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State"):
                opp_val = getattr(old_value, "State", None)
                if opp_val == self:
                    setattr(old_value, "State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State"):
                opp_val = getattr(value, "State", None)
                setattr(value, "State", self)

    @property
    def duringActions(self):
        return self.__duringActions

    @duringActions.setter
    def duringActions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Action__duringActions", None)
        self.__duringActions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State38"):
                opp_val = getattr(old_value, "State38", None)
                if opp_val == self:
                    setattr(old_value, "State38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State38"):
                opp_val = getattr(value, "State38", None)
                setattr(value, "State38", self)

    @property
    def Action29(self):
        return self.__Action29

    @Action29.setter
    def Action29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Action__Action29", None)
        self.__Action29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transition28"):
                opp_val = getattr(old_value, "transition28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transition28"):
                opp_val = getattr(value, "transition28", None)
                if opp_val is None:
                    setattr(value, "transition28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Action20(self):
        return self.__Action20

    @Action20.setter
    def Action20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Action__Action20", None)
        self.__Action20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateDuring"):
                opp_val = getattr(old_value, "stateDuring", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateDuring"):
                opp_val = getattr(value, "stateDuring", None)
                if opp_val is None:
                    setattr(value, "stateDuring", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Action22(self):
        return self.__Action22

    @Action22.setter
    def Action22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Action__Action22", None)
        self.__Action22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateExit"):
                opp_val = getattr(old_value, "stateExit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateExit"):
                opp_val = getattr(value, "stateExit", None)
                if opp_val is None:
                    setattr(value, "stateExit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def exitActions(self):
        return self.__exitActions

    @exitActions.setter
    def exitActions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Action__exitActions", None)
        self.__exitActions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State40"):
                opp_val = getattr(old_value, "State40", None)
                if opp_val == self:
                    setattr(old_value, "State40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State40"):
                opp_val = getattr(value, "State40", None)
                setattr(value, "State40", self)

    @property
    def triggeredActions(self):
        return self.__triggeredActions

    @triggeredActions.setter
    def triggeredActions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Action__triggeredActions", None)
        self.__triggeredActions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transition35"):
                opp_val = getattr(old_value, "Transition35", None)
                if opp_val == self:
                    setattr(old_value, "Transition35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transition35"):
                opp_val = getattr(value, "Transition35", None)
                setattr(value, "Transition35", self)

class Vertex:

    pass
class simulink_Junction(Vertex):

    pass
class ContainableStateflowElement:

    pass
class simulink_ContainableTruthTable(TruthTable, ContainableStateflowElement):

    pass
class simulink_Transition(ContainableStateflowElement):

    def __init__(self, isDefaultTransition: bool, executionOrder: int, Transition: "simulink_Vertex" = None, Transition17: "simulink_Vertex" = None, outgoingTransitions: "simulink_Vertex" = None, incomingTransitions: "simulink_Vertex" = None, transition: "simulink_SFWGuard" = None, transition28: set["simulink_Action"] = None, transition31: "simulink_SFWTrigger" = None, Transition33: "simulink_SFWGuard" = None, Transition35: "simulink_Action" = None, Transition61: "simulink_SFWTrigger" = None):
        self.isDefaultTransition = isDefaultTransition
        self.executionOrder = executionOrder
        self.Transition = Transition
        self.Transition17 = Transition17
        self.outgoingTransitions = outgoingTransitions
        self.incomingTransitions = incomingTransitions
        self.transition = transition
        self.transition28 = transition28 if transition28 is not None else set()
        self.transition31 = transition31
        self.Transition33 = Transition33
        self.Transition35 = Transition35
        self.Transition61 = Transition61
        
    @property
    def isDefaultTransition(self) -> bool:
        return self.__isDefaultTransition

    @isDefaultTransition.setter
    def isDefaultTransition(self, isDefaultTransition: bool):
        self.__isDefaultTransition = isDefaultTransition

    @property
    def executionOrder(self) -> int:
        return self.__executionOrder

    @executionOrder.setter
    def executionOrder(self, executionOrder: int):
        self.__executionOrder = executionOrder

    @property
    def Transition35(self):
        return self.__Transition35

    @Transition35.setter
    def Transition35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Transition__Transition35", None)
        self.__Transition35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "triggeredActions"):
                opp_val = getattr(old_value, "triggeredActions", None)
                if opp_val == self:
                    setattr(old_value, "triggeredActions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "triggeredActions"):
                opp_val = getattr(value, "triggeredActions", None)
                setattr(value, "triggeredActions", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "destination"):
                opp_val = getattr(old_value, "destination", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "destination"):
                opp_val = getattr(value, "destination", None)
                if opp_val is None:
                    setattr(value, "destination", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoingTransitions(self):
        return self.__outgoingTransitions

    @outgoingTransitions.setter
    def outgoingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Transition__outgoingTransitions", None)
        self.__outgoingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex"):
                opp_val = getattr(old_value, "Vertex", None)
                if opp_val == self:
                    setattr(old_value, "Vertex", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex"):
                opp_val = getattr(value, "Vertex", None)
                setattr(value, "Vertex", self)

    @property
    def transition28(self):
        return self.__transition28

    @transition28.setter
    def transition28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Transition__transition28", None)
        self.__transition28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Action29"):
                    opp_val = getattr(item, "Action29", None)
                    
                    if opp_val == self:
                        setattr(item, "Action29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Action29"):
                    opp_val = getattr(item, "Action29", None)
                    
                    setattr(item, "Action29", self)
                    

    @property
    def incomingTransitions(self):
        return self.__incomingTransitions

    @incomingTransitions.setter
    def incomingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Transition__incomingTransitions", None)
        self.__incomingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex25"):
                opp_val = getattr(old_value, "Vertex25", None)
                if opp_val == self:
                    setattr(old_value, "Vertex25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex25"):
                opp_val = getattr(value, "Vertex25", None)
                setattr(value, "Vertex25", self)

    @property
    def Transition17(self):
        return self.__Transition17

    @Transition17.setter
    def Transition17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Transition__Transition17", None)
        self.__Transition17 = value
        
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
    def Transition33(self):
        return self.__Transition33

    @Transition33.setter
    def Transition33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Transition__Transition33", None)
        self.__Transition33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "guard"):
                opp_val = getattr(old_value, "guard", None)
                if opp_val == self:
                    setattr(old_value, "guard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "guard"):
                opp_val = getattr(value, "guard", None)
                setattr(value, "guard", self)

    @property
    def transition(self):
        return self.__transition

    @transition.setter
    def transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Transition__transition", None)
        self.__transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SFWGuard"):
                opp_val = getattr(old_value, "SFWGuard", None)
                if opp_val == self:
                    setattr(old_value, "SFWGuard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SFWGuard"):
                opp_val = getattr(value, "SFWGuard", None)
                setattr(value, "SFWGuard", self)

    @property
    def Transition61(self):
        return self.__Transition61

    @Transition61.setter
    def Transition61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Transition__Transition61", None)
        self.__Transition61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trigger"):
                opp_val = getattr(old_value, "trigger", None)
                if opp_val == self:
                    setattr(old_value, "trigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trigger"):
                opp_val = getattr(value, "trigger", None)
                setattr(value, "trigger", self)

    @property
    def transition31(self):
        return self.__transition31

    @transition31.setter
    def transition31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Transition__transition31", None)
        self.__transition31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SFWTrigger"):
                opp_val = getattr(old_value, "SFWTrigger", None)
                if opp_val == self:
                    setattr(old_value, "SFWTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SFWTrigger"):
                opp_val = getattr(value, "SFWTrigger", None)
                setattr(value, "SFWTrigger", self)

class simulink_Data(ContainableStateflowElement):

    pass
class simulink_Vertex(ContainableStateflowElement):

    pass
class CompositeStateflowElement:

    pass
class simulink_Function(ContainableStateflowElement, CompositeStateflowElement):

    def __init__(self, signature: str):
        self.signature = signature
        
    @property
    def signature(self) -> str:
        return self.__signature

    @signature.setter
    def signature(self, signature: str):
        self.__signature = signature

class simulink_State(Vertex, CompositeStateflowElement):

    def __init__(self, decomposition: str, executionOrder: int, stateEntry: set["simulink_Action"] = None, stateDuring: set["simulink_Action"] = None, stateExit: set["simulink_Action"] = None, State: "simulink_Action" = None, State38: "simulink_Action" = None, State40: "simulink_Action" = None):
        self.decomposition = decomposition
        self.executionOrder = executionOrder
        self.stateEntry = stateEntry if stateEntry is not None else set()
        self.stateDuring = stateDuring if stateDuring is not None else set()
        self.stateExit = stateExit if stateExit is not None else set()
        self.State = State
        self.State38 = State38
        self.State40 = State40
        
    @property
    def executionOrder(self) -> int:
        return self.__executionOrder

    @executionOrder.setter
    def executionOrder(self, executionOrder: int):
        self.__executionOrder = executionOrder

    @property
    def decomposition(self) -> str:
        return self.__decomposition

    @decomposition.setter
    def decomposition(self, decomposition: str):
        self.__decomposition = decomposition

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entryActions"):
                opp_val = getattr(old_value, "entryActions", None)
                if opp_val == self:
                    setattr(old_value, "entryActions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entryActions"):
                opp_val = getattr(value, "entryActions", None)
                setattr(value, "entryActions", self)

    @property
    def stateExit(self):
        return self.__stateExit

    @stateExit.setter
    def stateExit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_State__stateExit", None)
        self.__stateExit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Action22"):
                    opp_val = getattr(item, "Action22", None)
                    
                    if opp_val == self:
                        setattr(item, "Action22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Action22"):
                    opp_val = getattr(item, "Action22", None)
                    
                    setattr(item, "Action22", self)
                    

    @property
    def State38(self):
        return self.__State38

    @State38.setter
    def State38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_State__State38", None)
        self.__State38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "duringActions"):
                opp_val = getattr(old_value, "duringActions", None)
                if opp_val == self:
                    setattr(old_value, "duringActions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "duringActions"):
                opp_val = getattr(value, "duringActions", None)
                setattr(value, "duringActions", self)

    @property
    def stateDuring(self):
        return self.__stateDuring

    @stateDuring.setter
    def stateDuring(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_State__stateDuring", None)
        self.__stateDuring = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Action20"):
                    opp_val = getattr(item, "Action20", None)
                    
                    if opp_val == self:
                        setattr(item, "Action20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Action20"):
                    opp_val = getattr(item, "Action20", None)
                    
                    setattr(item, "Action20", self)
                    

    @property
    def State40(self):
        return self.__State40

    @State40.setter
    def State40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_State__State40", None)
        self.__State40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exitActions"):
                opp_val = getattr(old_value, "exitActions", None)
                if opp_val == self:
                    setattr(old_value, "exitActions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exitActions"):
                opp_val = getattr(value, "exitActions", None)
                setattr(value, "exitActions", self)

    @property
    def stateEntry(self):
        return self.__stateEntry

    @stateEntry.setter
    def stateEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_State__stateEntry", None)
        self.__stateEntry = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Action"):
                    opp_val = getattr(item, "Action", None)
                    
                    if opp_val == self:
                        setattr(item, "Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Action"):
                    opp_val = getattr(item, "Action", None)
                    
                    setattr(item, "Action", self)
                    

class PortBlock:

    pass
class simulink_OutPortBlock(PortBlock):

    pass
class simulink_InPortBlock(PortBlock):

    pass
class Block:

    pass
class simulink_TruthTableChart(Block, TruthTable):

    pass
class simulink_Chart(Block, CompositeStateflowElement):

    def __init__(self, decomposition: str):
        self.decomposition = decomposition
        
    @property
    def decomposition(self) -> str:
        return self.__decomposition

    @decomposition.setter
    def decomposition(self, decomposition: str):
        self.__decomposition = decomposition

class Port:

    pass
class simulink_OutPort(Port):

    pass
class simulink_InPort(Port):

    pass
class simulink_PortBlock(Block):

    def __init__(self, portNumber: int, PortBlock: "simulink_Port" = None, portBlock: "simulink_Port" = None):
        self.portNumber = portNumber
        self.PortBlock = PortBlock
        self.portBlock = portBlock
        
    @property
    def portNumber(self) -> int:
        return self.__portNumber

    @portNumber.setter
    def portNumber(self, portNumber: int):
        self.__portNumber = portNumber

    @property
    def PortBlock(self):
        return self.__PortBlock

    @PortBlock.setter
    def PortBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_PortBlock__PortBlock", None)
        self.__PortBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "port"):
                opp_val = getattr(old_value, "port", None)
                if opp_val == self:
                    setattr(old_value, "port", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "port"):
                opp_val = getattr(value, "port", None)
                setattr(value, "port", self)

    @property
    def portBlock(self):
        return self.__portBlock

    @portBlock.setter
    def portBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_PortBlock__portBlock", None)
        self.__portBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Port11"):
                opp_val = getattr(old_value, "Port11", None)
                if opp_val == self:
                    setattr(old_value, "Port11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Port11"):
                opp_val = getattr(value, "Port11", None)
                setattr(value, "Port11", self)

class simulink_SubSystem(Block):

    pass
class SimulinkElement:

    pass
class simulink_StateflowElement(SimulinkElement):

    def __init__(self, path: str, id: int):
        self.path = path
        self.id = id
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class simulink_Port(SimulinkElement):

    def __init__(self, dataType: str, portNumber: int, Port: "simulink_Block" = None, ownedPorts: "simulink_Block" = None, port: "simulink_PortBlock" = None, Port11: "simulink_PortBlock" = None):
        self.dataType = dataType
        self.portNumber = portNumber
        self.Port = Port
        self.ownedPorts = ownedPorts
        self.port = port
        self.Port11 = Port11
        
    @property
    def portNumber(self) -> int:
        return self.__portNumber

    @portNumber.setter
    def portNumber(self, portNumber: int):
        self.__portNumber = portNumber

    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

    @property
    def ownedPorts(self):
        return self.__ownedPorts

    @ownedPorts.setter
    def ownedPorts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Port__ownedPorts", None)
        self.__ownedPorts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Block"):
                opp_val = getattr(old_value, "Block", None)
                if opp_val == self:
                    setattr(old_value, "Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Block"):
                opp_val = getattr(value, "Block", None)
                setattr(value, "Block", self)

    @property
    def Port(self):
        return self.__Port

    @Port.setter
    def Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Port__Port", None)
        self.__Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "block"):
                opp_val = getattr(old_value, "block", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "block"):
                opp_val = getattr(value, "block", None)
                if opp_val is None:
                    setattr(value, "block", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Port11(self):
        return self.__Port11

    @Port11.setter
    def Port11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Port__Port11", None)
        self.__Port11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "portBlock"):
                opp_val = getattr(old_value, "portBlock", None)
                if opp_val == self:
                    setattr(old_value, "portBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "portBlock"):
                opp_val = getattr(value, "portBlock", None)
                setattr(value, "portBlock", self)

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Port__port", None)
        self.__port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PortBlock"):
                opp_val = getattr(old_value, "PortBlock", None)
                if opp_val == self:
                    setattr(old_value, "PortBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PortBlock"):
                opp_val = getattr(value, "PortBlock", None)
                setattr(value, "PortBlock", self)

class simulink_Connection(SimulinkElement):

    pass
class simulink_Block(SimulinkElement):

    pass
class simulink_SimulinkElement(ABC):

    def __init__(self, name: str, handle: str):
        self.name = name
        self.handle = handle
        
    @property
    def handle(self) -> str:
        return self.__handle

    @handle.setter
    def handle(self, handle: str):
        self.__handle = handle

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class SubSystem:

    pass
class simulink_Reference(SubSystem):

    pass
class simulink_SimulinkModel(SubSystem):

    def __init__(self, file: str, isLibrary: bool):
        self.file = file
        self.isLibrary = isLibrary
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def isLibrary(self) -> bool:
        return self.__isLibrary

    @isLibrary.setter
    def isLibrary(self, isLibrary: bool):
        self.__isLibrary = isLibrary
