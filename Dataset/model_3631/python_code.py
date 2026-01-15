from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class EventProcessingContext(Enum):
    STRICT_IMMEDIATE = "STRICT_IMMEDIATE"
    CHRONICLE = "CHRONICLE"
    RECENT = "RECENT"
    UNRESTRICTED = "UNRESTRICTED"
    IMMEDIATE = "IMMEDIATE"
class NumericCompareOperator(Enum):
    MORE_THAN = "MORE_THAN"
    LESS_THAN = "LESS_THAN"
    LESS_OR_EQUALS = "LESS_OR_EQUALS"
    EQUALS = "EQUALS"
    MORE_OR_EQUALS = "MORE_OR_EQUALS"
class TimeConstraintType(Enum):
    START = "START"
    STOP = "STOP"
    CHECK = "CHECK"


############################################
# Definition of Classes
############################################

class internalsm_TimeConstraintSpecification:

    def __init__(self, id: str, expectedLength: str, startTimestamp: str, stopTimestamp: str, internalsm_TimeConstraintSpecification: "internalsm_TimeConstraint" = None):
        self.id = id
        self.expectedLength = expectedLength
        self.startTimestamp = startTimestamp
        self.stopTimestamp = stopTimestamp
        self.internalsm_TimeConstraintSpecification = internalsm_TimeConstraintSpecification
        
    @property
    def expectedLength(self) -> str:
        return self.__expectedLength

    @expectedLength.setter
    def expectedLength(self, expectedLength: str):
        self.__expectedLength = expectedLength

    @property
    def stopTimestamp(self) -> str:
        return self.__stopTimestamp

    @stopTimestamp.setter
    def stopTimestamp(self, stopTimestamp: str):
        self.__stopTimestamp = stopTimestamp

    @property
    def startTimestamp(self) -> str:
        return self.__startTimestamp

    @startTimestamp.setter
    def startTimestamp(self, startTimestamp: str):
        self.__startTimestamp = startTimestamp

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def internalsm_TimeConstraintSpecification(self):
        return self.__internalsm_TimeConstraintSpecification

    @internalsm_TimeConstraintSpecification.setter
    def internalsm_TimeConstraintSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_internalsm_TimeConstraintSpecification__internalsm_TimeConstraintSpecification", None)
        self.__internalsm_TimeConstraintSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "internalsm_TimeConstraint29"):
                opp_val = getattr(old_value, "internalsm_TimeConstraint29", None)
                if opp_val == self:
                    setattr(old_value, "internalsm_TimeConstraint29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "internalsm_TimeConstraint29"):
                opp_val = getattr(value, "internalsm_TimeConstraint29", None)
                setattr(value, "internalsm_TimeConstraint29", self)

    def handleTimeConstraint(self):
        # TODO: Implement handleTimeConstraint method
        pass

class internalsm_InternalExecutionModel:

    def __init__(self, context: str, internalsm_InternalExecutionModel: set["internalsm_StateMachine"] = None, internalsm_InternalExecutionModel19: "internalsm_Event" = None, internalsm_InternalExecutionModel22: set["internalsm_EventToken"] = None):
        self.context = context
        self.internalsm_InternalExecutionModel = internalsm_InternalExecutionModel if internalsm_InternalExecutionModel is not None else set()
        self.internalsm_InternalExecutionModel19 = internalsm_InternalExecutionModel19
        self.internalsm_InternalExecutionModel22 = internalsm_InternalExecutionModel22 if internalsm_InternalExecutionModel22 is not None else set()
        
    @property
    def context(self) -> str:
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context

    @property
    def internalsm_InternalExecutionModel22(self):
        return self.__internalsm_InternalExecutionModel22

    @internalsm_InternalExecutionModel22.setter
    def internalsm_InternalExecutionModel22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_internalsm_InternalExecutionModel__internalsm_InternalExecutionModel22", None)
        self.__internalsm_InternalExecutionModel22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "internalsm_EventToken"):
                    opp_val = getattr(item, "internalsm_EventToken", None)
                    
                    if opp_val == self:
                        setattr(item, "internalsm_EventToken", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "internalsm_EventToken"):
                    opp_val = getattr(item, "internalsm_EventToken", None)
                    
                    setattr(item, "internalsm_EventToken", self)
                    

    @property
    def internalsm_InternalExecutionModel19(self):
        return self.__internalsm_InternalExecutionModel19

    @internalsm_InternalExecutionModel19.setter
    def internalsm_InternalExecutionModel19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_internalsm_InternalExecutionModel__internalsm_InternalExecutionModel19", None)
        self.__internalsm_InternalExecutionModel19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "internalsm_Event20"):
                opp_val = getattr(old_value, "internalsm_Event20", None)
                if opp_val == self:
                    setattr(old_value, "internalsm_Event20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "internalsm_Event20"):
                opp_val = getattr(value, "internalsm_Event20", None)
                setattr(value, "internalsm_Event20", self)

    @property
    def internalsm_InternalExecutionModel(self):
        return self.__internalsm_InternalExecutionModel

    @internalsm_InternalExecutionModel.setter
    def internalsm_InternalExecutionModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_internalsm_InternalExecutionModel__internalsm_InternalExecutionModel", None)
        self.__internalsm_InternalExecutionModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "internalsm_StateMachine17"):
                    opp_val = getattr(item, "internalsm_StateMachine17", None)
                    
                    if opp_val == self:
                        setattr(item, "internalsm_StateMachine17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "internalsm_StateMachine17"):
                    opp_val = getattr(item, "internalsm_StateMachine17", None)
                    
                    setattr(item, "internalsm_StateMachine17", self)
                    

class internalsm_EventPattern:

    pass
class internalsm_StateMachine:

    def __init__(self, priority: int, context: str, internalsm_StateMachine17: "internalsm_InternalExecutionModel" = None, internalsm_StateMachine: set["internalsm_State"] = None, stateMachine: "internalsm_EventPattern" = None):
        self.priority = priority
        self.context = context
        self.internalsm_StateMachine17 = internalsm_StateMachine17
        self.internalsm_StateMachine = internalsm_StateMachine if internalsm_StateMachine is not None else set()
        self.stateMachine = stateMachine
        
    @property
    def context(self) -> str:
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context

    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def internalsm_StateMachine17(self):
        return self.__internalsm_StateMachine17

    @internalsm_StateMachine17.setter
    def internalsm_StateMachine17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_internalsm_StateMachine__internalsm_StateMachine17", None)
        self.__internalsm_StateMachine17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "internalsm_InternalExecutionModel"):
                opp_val = getattr(old_value, "internalsm_InternalExecutionModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "internalsm_InternalExecutionModel"):
                opp_val = getattr(value, "internalsm_InternalExecutionModel", None)
                if opp_val is None:
                    setattr(value, "internalsm_InternalExecutionModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def internalsm_StateMachine(self):
        return self.__internalsm_StateMachine

    @internalsm_StateMachine.setter
    def internalsm_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_internalsm_StateMachine__internalsm_StateMachine", None)
        self.__internalsm_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "internalsm_State14"):
                    opp_val = getattr(item, "internalsm_State14", None)
                    
                    if opp_val == self:
                        setattr(item, "internalsm_State14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "internalsm_State14"):
                    opp_val = getattr(item, "internalsm_State14", None)
                    
                    setattr(item, "internalsm_State14", self)
                    

    @property
    def stateMachine(self):
        return self.__stateMachine

    @stateMachine.setter
    def stateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_internalsm_StateMachine__stateMachine", None)
        self.__stateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CEPMeta.ecoreEventPattern"):
                opp_val = getattr(old_value, "CEPMeta.ecoreEventPattern", None)
                if opp_val == self:
                    setattr(old_value, "CEPMeta.ecoreEventPattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CEPMeta.ecoreEventPattern"):
                opp_val = getattr(value, "CEPMeta.ecoreEventPattern", None)
                setattr(value, "CEPMeta.ecoreEventPattern", self)

class State:

    pass
class internalsm_InitState(State):

    pass
class internalsm_FinalState(State):

    pass
class internalsm_AtomicEventPattern:

    pass
class internalsm_TrapState(State):

    pass
class internalsm_Guard:

    pass
class internalsm_Event:

    pass
class internalsm_TimeConstraint:

    def __init__(self, type: str, internalsm_TimeConstraint: "internalsm_State" = None, internalsm_TimeConstraint29: "internalsm_TimeConstraintSpecification" = None):
        self.type = type
        self.internalsm_TimeConstraint = internalsm_TimeConstraint
        self.internalsm_TimeConstraint29 = internalsm_TimeConstraint29
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def internalsm_TimeConstraint29(self):
        return self.__internalsm_TimeConstraint29

    @internalsm_TimeConstraint29.setter
    def internalsm_TimeConstraint29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_internalsm_TimeConstraint__internalsm_TimeConstraint29", None)
        self.__internalsm_TimeConstraint29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "internalsm_TimeConstraintSpecification"):
                opp_val = getattr(old_value, "internalsm_TimeConstraintSpecification", None)
                if opp_val == self:
                    setattr(old_value, "internalsm_TimeConstraintSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "internalsm_TimeConstraintSpecification"):
                opp_val = getattr(value, "internalsm_TimeConstraintSpecification", None)
                setattr(value, "internalsm_TimeConstraintSpecification", self)

    @property
    def internalsm_TimeConstraint(self):
        return self.__internalsm_TimeConstraint

    @internalsm_TimeConstraint.setter
    def internalsm_TimeConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_internalsm_TimeConstraint__internalsm_TimeConstraint", None)
        self.__internalsm_TimeConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "internalsm_State"):
                opp_val = getattr(old_value, "internalsm_State", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "internalsm_State"):
                opp_val = getattr(value, "internalsm_State", None)
                if opp_val is None:
                    setattr(value, "internalsm_State", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class internalsm_Transition:

    pass
class internalsm_EventToken:

    pass
class internalsm_State:

    def __init__(self, label: str, currentState: set["internalsm_EventToken"] = None, preState: set["internalsm_Transition"] = None, postState: set["internalsm_Transition"] = None, State10: "internalsm_Transition" = None, internalsm_State: set["internalsm_TimeConstraint"] = None, internalsm_State6: "internalsm_Event" = None, State: "internalsm_Transition" = None, internalsm_State14: "internalsm_StateMachine" = None, State24: "internalsm_EventToken" = None):
        self.label = label
        self.currentState = currentState if currentState is not None else set()
        self.preState = preState if preState is not None else set()
        self.postState = postState if postState is not None else set()
        self.State10 = State10
        self.internalsm_State = internalsm_State if internalsm_State is not None else set()
        self.internalsm_State6 = internalsm_State6
        self.State = State
        self.internalsm_State14 = internalsm_State14
        self.State24 = State24
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def State10(self):
        return self.__State10

    @State10.setter
    def State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_internalsm_State__State10", None)
        self.__State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inTransitions"):
                opp_val = getattr(old_value, "inTransitions", None)
                if opp_val == self:
                    setattr(old_value, "inTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inTransitions"):
                opp_val = getattr(value, "inTransitions", None)
                setattr(value, "inTransitions", self)

    @property
    def internalsm_State14(self):
        return self.__internalsm_State14

    @internalsm_State14.setter
    def internalsm_State14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_internalsm_State__internalsm_State14", None)
        self.__internalsm_State14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "internalsm_StateMachine"):
                opp_val = getattr(old_value, "internalsm_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "internalsm_StateMachine"):
                opp_val = getattr(value, "internalsm_StateMachine", None)
                if opp_val is None:
                    setattr(value, "internalsm_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def internalsm_State(self):
        return self.__internalsm_State

    @internalsm_State.setter
    def internalsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_internalsm_State__internalsm_State", None)
        self.__internalsm_State = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "internalsm_TimeConstraint"):
                    opp_val = getattr(item, "internalsm_TimeConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "internalsm_TimeConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "internalsm_TimeConstraint"):
                    opp_val = getattr(item, "internalsm_TimeConstraint", None)
                    
                    setattr(item, "internalsm_TimeConstraint", self)
                    

    @property
    def State24(self):
        return self.__State24

    @State24.setter
    def State24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_internalsm_State__State24", None)
        self.__State24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eventTokens"):
                opp_val = getattr(old_value, "eventTokens", None)
                if opp_val == self:
                    setattr(old_value, "eventTokens", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eventTokens"):
                opp_val = getattr(value, "eventTokens", None)
                setattr(value, "eventTokens", self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_internalsm_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outTransitions"):
                opp_val = getattr(old_value, "outTransitions", None)
                if opp_val == self:
                    setattr(old_value, "outTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outTransitions"):
                opp_val = getattr(value, "outTransitions", None)
                setattr(value, "outTransitions", self)

    @property
    def postState(self):
        return self.__postState

    @postState.setter
    def postState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_internalsm_State__postState", None)
        self.__postState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition2"):
                    opp_val = getattr(item, "Transition2", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition2"):
                    opp_val = getattr(item, "Transition2", None)
                    
                    setattr(item, "Transition2", self)
                    

    @property
    def preState(self):
        return self.__preState

    @preState.setter
    def preState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_internalsm_State__preState", None)
        self.__preState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

    @property
    def currentState(self):
        return self.__currentState

    @currentState.setter
    def currentState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_internalsm_State__currentState", None)
        self.__currentState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EventToken"):
                    opp_val = getattr(item, "EventToken", None)
                    
                    if opp_val == self:
                        setattr(item, "EventToken", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EventToken"):
                    opp_val = getattr(item, "EventToken", None)
                    
                    setattr(item, "EventToken", self)
                    

    @property
    def internalsm_State6(self):
        return self.__internalsm_State6

    @internalsm_State6.setter
    def internalsm_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_internalsm_State__internalsm_State6", None)
        self.__internalsm_State6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "internalsm_Event"):
                opp_val = getattr(old_value, "internalsm_Event", None)
                if opp_val == self:
                    setattr(old_value, "internalsm_Event", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "internalsm_Event"):
                opp_val = getattr(value, "internalsm_Event", None)
                setattr(value, "internalsm_Event", self)
