from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Trace:

    pass
class sexec_TraceReactionWillFire(Trace):

    pass
class sexec_ReactionFired(Trace):

    pass
class sexec_TraceStateExited(Trace):

    pass
class sexec_TraceStateEntered(Trace):

    pass
class sexec_TraceNodeExecuted(Trace):

    pass
class sexec_TraceEndRunCycle(Trace):

    pass
class sexec_TraceBeginRunCycle(Trace):

    pass
class sexec_StateCase:

    pass
class Check:

    pass
class sexec_CheckRef(Check):

    pass
class sexec_Expression:

    pass
class Step:

    pass
class sexec_EnterState(Step):

    pass
class sexec_StateSwitch(Step):

    def __init__(self, stateConfigurationIdx: int, sexec_StateSwitch: set["sexec_StateCase"] = None, sexec_StateSwitch49: "sexec_ExecutionRegion" = None):
        self.stateConfigurationIdx = stateConfigurationIdx
        self.sexec_StateSwitch = sexec_StateSwitch if sexec_StateSwitch is not None else set()
        self.sexec_StateSwitch49 = sexec_StateSwitch49
        
    @property
    def stateConfigurationIdx(self) -> int:
        return self.__stateConfigurationIdx

    @stateConfigurationIdx.setter
    def stateConfigurationIdx(self, stateConfigurationIdx: int):
        self.__stateConfigurationIdx = stateConfigurationIdx

    @property
    def sexec_StateSwitch(self):
        return self.__sexec_StateSwitch

    @sexec_StateSwitch.setter
    def sexec_StateSwitch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_StateSwitch__sexec_StateSwitch", None)
        self.__sexec_StateSwitch = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sexec_StateCase"):
                    opp_val = getattr(item, "sexec_StateCase", None)
                    
                    if opp_val == self:
                        setattr(item, "sexec_StateCase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sexec_StateCase"):
                    opp_val = getattr(item, "sexec_StateCase", None)
                    
                    setattr(item, "sexec_StateCase", self)
                    

    @property
    def sexec_StateSwitch49(self):
        return self.__sexec_StateSwitch49

    @sexec_StateSwitch49.setter
    def sexec_StateSwitch49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_StateSwitch__sexec_StateSwitch49", None)
        self.__sexec_StateSwitch49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_ExecutionRegion50"):
                opp_val = getattr(old_value, "sexec_ExecutionRegion50", None)
                if opp_val == self:
                    setattr(old_value, "sexec_ExecutionRegion50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_ExecutionRegion50"):
                opp_val = getattr(value, "sexec_ExecutionRegion50", None)
                setattr(value, "sexec_ExecutionRegion50", self)

class sexec_SaveHistory(Step):

    def __init__(self, deep: bool, sexec_SaveHistory: "sexec_ExecutionRegion" = None):
        self.deep = deep
        self.sexec_SaveHistory = sexec_SaveHistory
        
    @property
    def deep(self) -> bool:
        return self.__deep

    @deep.setter
    def deep(self, deep: bool):
        self.__deep = deep

    @property
    def sexec_SaveHistory(self):
        return self.__sexec_SaveHistory

    @sexec_SaveHistory.setter
    def sexec_SaveHistory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_SaveHistory__sexec_SaveHistory", None)
        self.__sexec_SaveHistory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_ExecutionRegion58"):
                opp_val = getattr(old_value, "sexec_ExecutionRegion58", None)
                if opp_val == self:
                    setattr(old_value, "sexec_ExecutionRegion58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_ExecutionRegion58"):
                opp_val = getattr(value, "sexec_ExecutionRegion58", None)
                setattr(value, "sexec_ExecutionRegion58", self)

class sexec_Trace(Step):

    pass
class sexec_Call(Step):

    pass
class sexec_ExitState(Step):

    pass
class sexec_HistoryEntry(Step):

    def __init__(self, deep: bool, sexec_HistoryEntry65: "sexec_Step" = None, sexec_HistoryEntry: "sexec_Step" = None, sexec_HistoryEntry62: "sexec_ExecutionRegion" = None):
        self.deep = deep
        self.sexec_HistoryEntry65 = sexec_HistoryEntry65
        self.sexec_HistoryEntry = sexec_HistoryEntry
        self.sexec_HistoryEntry62 = sexec_HistoryEntry62
        
    @property
    def deep(self) -> bool:
        return self.__deep

    @deep.setter
    def deep(self, deep: bool):
        self.__deep = deep

    @property
    def sexec_HistoryEntry62(self):
        return self.__sexec_HistoryEntry62

    @sexec_HistoryEntry62.setter
    def sexec_HistoryEntry62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_HistoryEntry__sexec_HistoryEntry62", None)
        self.__sexec_HistoryEntry62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_ExecutionRegion63"):
                opp_val = getattr(old_value, "sexec_ExecutionRegion63", None)
                if opp_val == self:
                    setattr(old_value, "sexec_ExecutionRegion63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_ExecutionRegion63"):
                opp_val = getattr(value, "sexec_ExecutionRegion63", None)
                setattr(value, "sexec_ExecutionRegion63", self)

    @property
    def sexec_HistoryEntry(self):
        return self.__sexec_HistoryEntry

    @sexec_HistoryEntry.setter
    def sexec_HistoryEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_HistoryEntry__sexec_HistoryEntry", None)
        self.__sexec_HistoryEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_Step60"):
                opp_val = getattr(old_value, "sexec_Step60", None)
                if opp_val == self:
                    setattr(old_value, "sexec_Step60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_Step60"):
                opp_val = getattr(value, "sexec_Step60", None)
                setattr(value, "sexec_Step60", self)

    @property
    def sexec_HistoryEntry65(self):
        return self.__sexec_HistoryEntry65

    @sexec_HistoryEntry65.setter
    def sexec_HistoryEntry65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_HistoryEntry__sexec_HistoryEntry65", None)
        self.__sexec_HistoryEntry65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_Step66"):
                opp_val = getattr(old_value, "sexec_Step66", None)
                if opp_val == self:
                    setattr(old_value, "sexec_Step66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_Step66"):
                opp_val = getattr(value, "sexec_Step66", None)
                setattr(value, "sexec_Step66", self)

class sexec_ScheduleTimeEvent(Step):

    pass
class sexec_UnscheduleTimeEvent(Step):

    pass
class sexec_Check(Step):

    pass
class Event:

    pass
class sexec_TimeEvent(Event):

    def __init__(self, periodic: bool, sexec_TimeEvent: "sexec_ScheduleTimeEvent" = None, sexec_TimeEvent46: "sexec_UnscheduleTimeEvent" = None):
        self.periodic = periodic
        self.sexec_TimeEvent = sexec_TimeEvent
        self.sexec_TimeEvent46 = sexec_TimeEvent46
        
    @property
    def periodic(self) -> bool:
        return self.__periodic

    @periodic.setter
    def periodic(self, periodic: bool):
        self.__periodic = periodic

    @property
    def sexec_TimeEvent(self):
        return self.__sexec_TimeEvent

    @sexec_TimeEvent.setter
    def sexec_TimeEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_TimeEvent__sexec_TimeEvent", None)
        self.__sexec_TimeEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_ScheduleTimeEvent"):
                opp_val = getattr(old_value, "sexec_ScheduleTimeEvent", None)
                if opp_val == self:
                    setattr(old_value, "sexec_ScheduleTimeEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_ScheduleTimeEvent"):
                opp_val = getattr(value, "sexec_ScheduleTimeEvent", None)
                setattr(value, "sexec_ScheduleTimeEvent", self)

    @property
    def sexec_TimeEvent46(self):
        return self.__sexec_TimeEvent46

    @sexec_TimeEvent46.setter
    def sexec_TimeEvent46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_TimeEvent__sexec_TimeEvent46", None)
        self.__sexec_TimeEvent46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_UnscheduleTimeEvent"):
                opp_val = getattr(old_value, "sexec_UnscheduleTimeEvent", None)
                if opp_val == self:
                    setattr(old_value, "sexec_UnscheduleTimeEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_UnscheduleTimeEvent"):
                opp_val = getattr(value, "sexec_UnscheduleTimeEvent", None)
                setattr(value, "sexec_UnscheduleTimeEvent", self)

class sexec_Execution(Step):

    pass
class NamedElement:

    pass
class MappedElement:

    pass
class sexec_ExecutionScope(NamedElement, MappedElement):

    pass
class sexec_Step(NamedElement):

    def __init__(self, comment: str, sexec_Step: "sexec_ExecutionFlow" = None, sexec_Step12: "sexec_ExecutionFlow" = None, sexec_Step15: "sexec_ExecutionState" = None, sexec_Step18: "sexec_ExecutionState" = None, sexec_Step66: "sexec_HistoryEntry" = None, sexec_Step56: "sexec_StateCase" = None, sexec_Step60: "sexec_HistoryEntry" = None):
        self.comment = comment
        self.sexec_Step = sexec_Step
        self.sexec_Step12 = sexec_Step12
        self.sexec_Step15 = sexec_Step15
        self.sexec_Step18 = sexec_Step18
        self.sexec_Step66 = sexec_Step66
        self.sexec_Step56 = sexec_Step56
        self.sexec_Step60 = sexec_Step60
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def sexec_Step66(self):
        return self.__sexec_Step66

    @sexec_Step66.setter
    def sexec_Step66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_Step__sexec_Step66", None)
        self.__sexec_Step66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_HistoryEntry65"):
                opp_val = getattr(old_value, "sexec_HistoryEntry65", None)
                if opp_val == self:
                    setattr(old_value, "sexec_HistoryEntry65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_HistoryEntry65"):
                opp_val = getattr(value, "sexec_HistoryEntry65", None)
                setattr(value, "sexec_HistoryEntry65", self)

    @property
    def sexec_Step12(self):
        return self.__sexec_Step12

    @sexec_Step12.setter
    def sexec_Step12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_Step__sexec_Step12", None)
        self.__sexec_Step12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_ExecutionFlow11"):
                opp_val = getattr(old_value, "sexec_ExecutionFlow11", None)
                if opp_val == self:
                    setattr(old_value, "sexec_ExecutionFlow11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_ExecutionFlow11"):
                opp_val = getattr(value, "sexec_ExecutionFlow11", None)
                setattr(value, "sexec_ExecutionFlow11", self)

    @property
    def sexec_Step(self):
        return self.__sexec_Step

    @sexec_Step.setter
    def sexec_Step(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_Step__sexec_Step", None)
        self.__sexec_Step = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_ExecutionFlow9"):
                opp_val = getattr(old_value, "sexec_ExecutionFlow9", None)
                if opp_val == self:
                    setattr(old_value, "sexec_ExecutionFlow9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_ExecutionFlow9"):
                opp_val = getattr(value, "sexec_ExecutionFlow9", None)
                setattr(value, "sexec_ExecutionFlow9", self)

    @property
    def sexec_Step56(self):
        return self.__sexec_Step56

    @sexec_Step56.setter
    def sexec_Step56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_Step__sexec_Step56", None)
        self.__sexec_Step56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_StateCase55"):
                opp_val = getattr(old_value, "sexec_StateCase55", None)
                if opp_val == self:
                    setattr(old_value, "sexec_StateCase55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_StateCase55"):
                opp_val = getattr(value, "sexec_StateCase55", None)
                setattr(value, "sexec_StateCase55", self)

    @property
    def sexec_Step60(self):
        return self.__sexec_Step60

    @sexec_Step60.setter
    def sexec_Step60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_Step__sexec_Step60", None)
        self.__sexec_Step60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_HistoryEntry"):
                opp_val = getattr(old_value, "sexec_HistoryEntry", None)
                if opp_val == self:
                    setattr(old_value, "sexec_HistoryEntry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_HistoryEntry"):
                opp_val = getattr(value, "sexec_HistoryEntry", None)
                setattr(value, "sexec_HistoryEntry", self)

    @property
    def sexec_Step15(self):
        return self.__sexec_Step15

    @sexec_Step15.setter
    def sexec_Step15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_Step__sexec_Step15", None)
        self.__sexec_Step15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_ExecutionState14"):
                opp_val = getattr(old_value, "sexec_ExecutionState14", None)
                if opp_val == self:
                    setattr(old_value, "sexec_ExecutionState14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_ExecutionState14"):
                opp_val = getattr(value, "sexec_ExecutionState14", None)
                setattr(value, "sexec_ExecutionState14", self)

    @property
    def sexec_Step18(self):
        return self.__sexec_Step18

    @sexec_Step18.setter
    def sexec_Step18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_Step__sexec_Step18", None)
        self.__sexec_Step18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_ExecutionState17"):
                opp_val = getattr(old_value, "sexec_ExecutionState17", None)
                if opp_val == self:
                    setattr(old_value, "sexec_ExecutionState17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_ExecutionState17"):
                opp_val = getattr(value, "sexec_ExecutionState17", None)
                setattr(value, "sexec_ExecutionState17", self)

class sexec_StateVector:

    def __init__(self, size: int, offset: int, sexec_StateVector: "sexec_ExecutionFlow" = None, sexec_StateVector20: "sexec_ExecutionScope" = None, sexec_StateVector28: "sexec_ExecutionRegion" = None):
        self.size = size
        self.offset = offset
        self.sexec_StateVector = sexec_StateVector
        self.sexec_StateVector20 = sexec_StateVector20
        self.sexec_StateVector28 = sexec_StateVector28
        
    @property
    def offset(self) -> int:
        return self.__offset

    @offset.setter
    def offset(self, offset: int):
        self.__offset = offset

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def sexec_StateVector20(self):
        return self.__sexec_StateVector20

    @sexec_StateVector20.setter
    def sexec_StateVector20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_StateVector__sexec_StateVector20", None)
        self.__sexec_StateVector20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_ExecutionScope"):
                opp_val = getattr(old_value, "sexec_ExecutionScope", None)
                if opp_val == self:
                    setattr(old_value, "sexec_ExecutionScope", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_ExecutionScope"):
                opp_val = getattr(value, "sexec_ExecutionScope", None)
                setattr(value, "sexec_ExecutionScope", self)

    @property
    def sexec_StateVector28(self):
        return self.__sexec_StateVector28

    @sexec_StateVector28.setter
    def sexec_StateVector28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_StateVector__sexec_StateVector28", None)
        self.__sexec_StateVector28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_ExecutionRegion27"):
                opp_val = getattr(old_value, "sexec_ExecutionRegion27", None)
                if opp_val == self:
                    setattr(old_value, "sexec_ExecutionRegion27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_ExecutionRegion27"):
                opp_val = getattr(value, "sexec_ExecutionRegion27", None)
                setattr(value, "sexec_ExecutionRegion27", self)

    @property
    def sexec_StateVector(self):
        return self.__sexec_StateVector

    @sexec_StateVector.setter
    def sexec_StateVector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_StateVector__sexec_StateVector", None)
        self.__sexec_StateVector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_ExecutionFlow7"):
                opp_val = getattr(old_value, "sexec_ExecutionFlow7", None)
                if opp_val == self:
                    setattr(old_value, "sexec_ExecutionFlow7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_ExecutionFlow7"):
                opp_val = getattr(value, "sexec_ExecutionFlow7", None)
                setattr(value, "sexec_ExecutionFlow7", self)

class sexec_ExecutionNode(NamedElement, MappedElement):

    def __init__(self, simpleName: str, sexec_ExecutionNode: "sexec_ExecutionFlow" = None, sexec_ExecutionNode31: "sexec_ExecutionRegion" = None, sexec_ExecutionNode68: "sexec_TraceNodeExecuted" = None):
        self.simpleName = simpleName
        self.sexec_ExecutionNode = sexec_ExecutionNode
        self.sexec_ExecutionNode31 = sexec_ExecutionNode31
        self.sexec_ExecutionNode68 = sexec_ExecutionNode68
        
    @property
    def simpleName(self) -> str:
        return self.__simpleName

    @simpleName.setter
    def simpleName(self, simpleName: str):
        self.__simpleName = simpleName

    @property
    def sexec_ExecutionNode31(self):
        return self.__sexec_ExecutionNode31

    @sexec_ExecutionNode31.setter
    def sexec_ExecutionNode31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_ExecutionNode__sexec_ExecutionNode31", None)
        self.__sexec_ExecutionNode31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_ExecutionRegion30"):
                opp_val = getattr(old_value, "sexec_ExecutionRegion30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_ExecutionRegion30"):
                opp_val = getattr(value, "sexec_ExecutionRegion30", None)
                if opp_val is None:
                    setattr(value, "sexec_ExecutionRegion30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sexec_ExecutionNode68(self):
        return self.__sexec_ExecutionNode68

    @sexec_ExecutionNode68.setter
    def sexec_ExecutionNode68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_ExecutionNode__sexec_ExecutionNode68", None)
        self.__sexec_ExecutionNode68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_TraceNodeExecuted"):
                opp_val = getattr(old_value, "sexec_TraceNodeExecuted", None)
                if opp_val == self:
                    setattr(old_value, "sexec_TraceNodeExecuted", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_TraceNodeExecuted"):
                opp_val = getattr(value, "sexec_TraceNodeExecuted", None)
                setattr(value, "sexec_TraceNodeExecuted", self)

    @property
    def sexec_ExecutionNode(self):
        return self.__sexec_ExecutionNode

    @sexec_ExecutionNode.setter
    def sexec_ExecutionNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_ExecutionNode__sexec_ExecutionNode", None)
        self.__sexec_ExecutionNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_ExecutionFlow3"):
                opp_val = getattr(old_value, "sexec_ExecutionFlow3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_ExecutionFlow3"):
                opp_val = getattr(value, "sexec_ExecutionFlow3", None)
                if opp_val is None:
                    setattr(value, "sexec_ExecutionFlow3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ExecutionScope:

    pass
class sexec_ExecutionRegion(ExecutionScope):

    pass
class ScopedElement:

    pass
class sexec_EObject:

    pass
class sexec_MappedElement:

    pass
class ExecutionNode:

    pass
class sexec_ExecutionExit(ExecutionNode):

    pass
class sexec_ExecutionFlow(ExecutionScope, ExecutionNode, ScopedElement):

    pass
class sexec_ExecutionSynchronization(ExecutionNode):

    pass
class sexec_ExecutionChoice(ExecutionNode):

    pass
class sexec_ExecutionEntry(ExecutionNode):

    pass
class sexec_ExecutionState(ExecutionScope, ExecutionNode):

    def __init__(self, leaf: bool, sexec_ExecutionState: "sexec_ExecutionFlow" = None, sexec_ExecutionState14: "sexec_Step" = None, sexec_ExecutionState17: "sexec_Step" = None, sexec_ExecutionState38: "sexec_EnterState" = None, sexec_ExecutionState40: "sexec_ExitState" = None, sexec_ExecutionState53: "sexec_StateCase" = None, sexec_ExecutionState70: "sexec_TraceStateEntered" = None, sexec_ExecutionState72: "sexec_TraceStateExited" = None):
        self.leaf = leaf
        self.sexec_ExecutionState = sexec_ExecutionState
        self.sexec_ExecutionState14 = sexec_ExecutionState14
        self.sexec_ExecutionState17 = sexec_ExecutionState17
        self.sexec_ExecutionState38 = sexec_ExecutionState38
        self.sexec_ExecutionState40 = sexec_ExecutionState40
        self.sexec_ExecutionState53 = sexec_ExecutionState53
        self.sexec_ExecutionState70 = sexec_ExecutionState70
        self.sexec_ExecutionState72 = sexec_ExecutionState72
        
    @property
    def leaf(self) -> bool:
        return self.__leaf

    @leaf.setter
    def leaf(self, leaf: bool):
        self.__leaf = leaf

    @property
    def sexec_ExecutionState(self):
        return self.__sexec_ExecutionState

    @sexec_ExecutionState.setter
    def sexec_ExecutionState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_ExecutionState__sexec_ExecutionState", None)
        self.__sexec_ExecutionState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_ExecutionFlow"):
                opp_val = getattr(old_value, "sexec_ExecutionFlow", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_ExecutionFlow"):
                opp_val = getattr(value, "sexec_ExecutionFlow", None)
                if opp_val is None:
                    setattr(value, "sexec_ExecutionFlow", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sexec_ExecutionState14(self):
        return self.__sexec_ExecutionState14

    @sexec_ExecutionState14.setter
    def sexec_ExecutionState14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_ExecutionState__sexec_ExecutionState14", None)
        self.__sexec_ExecutionState14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_Step15"):
                opp_val = getattr(old_value, "sexec_Step15", None)
                if opp_val == self:
                    setattr(old_value, "sexec_Step15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_Step15"):
                opp_val = getattr(value, "sexec_Step15", None)
                setattr(value, "sexec_Step15", self)

    @property
    def sexec_ExecutionState17(self):
        return self.__sexec_ExecutionState17

    @sexec_ExecutionState17.setter
    def sexec_ExecutionState17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_ExecutionState__sexec_ExecutionState17", None)
        self.__sexec_ExecutionState17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_Step18"):
                opp_val = getattr(old_value, "sexec_Step18", None)
                if opp_val == self:
                    setattr(old_value, "sexec_Step18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_Step18"):
                opp_val = getattr(value, "sexec_Step18", None)
                setattr(value, "sexec_Step18", self)

    @property
    def sexec_ExecutionState72(self):
        return self.__sexec_ExecutionState72

    @sexec_ExecutionState72.setter
    def sexec_ExecutionState72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_ExecutionState__sexec_ExecutionState72", None)
        self.__sexec_ExecutionState72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_TraceStateExited"):
                opp_val = getattr(old_value, "sexec_TraceStateExited", None)
                if opp_val == self:
                    setattr(old_value, "sexec_TraceStateExited", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_TraceStateExited"):
                opp_val = getattr(value, "sexec_TraceStateExited", None)
                setattr(value, "sexec_TraceStateExited", self)

    @property
    def sexec_ExecutionState70(self):
        return self.__sexec_ExecutionState70

    @sexec_ExecutionState70.setter
    def sexec_ExecutionState70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_ExecutionState__sexec_ExecutionState70", None)
        self.__sexec_ExecutionState70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_TraceStateEntered"):
                opp_val = getattr(old_value, "sexec_TraceStateEntered", None)
                if opp_val == self:
                    setattr(old_value, "sexec_TraceStateEntered", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_TraceStateEntered"):
                opp_val = getattr(value, "sexec_TraceStateEntered", None)
                setattr(value, "sexec_TraceStateEntered", self)

    @property
    def sexec_ExecutionState40(self):
        return self.__sexec_ExecutionState40

    @sexec_ExecutionState40.setter
    def sexec_ExecutionState40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_ExecutionState__sexec_ExecutionState40", None)
        self.__sexec_ExecutionState40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_ExitState"):
                opp_val = getattr(old_value, "sexec_ExitState", None)
                if opp_val == self:
                    setattr(old_value, "sexec_ExitState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_ExitState"):
                opp_val = getattr(value, "sexec_ExitState", None)
                setattr(value, "sexec_ExitState", self)

    @property
    def sexec_ExecutionState53(self):
        return self.__sexec_ExecutionState53

    @sexec_ExecutionState53.setter
    def sexec_ExecutionState53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_ExecutionState__sexec_ExecutionState53", None)
        self.__sexec_ExecutionState53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_StateCase52"):
                opp_val = getattr(old_value, "sexec_StateCase52", None)
                if opp_val == self:
                    setattr(old_value, "sexec_StateCase52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_StateCase52"):
                opp_val = getattr(value, "sexec_StateCase52", None)
                setattr(value, "sexec_StateCase52", self)

    @property
    def sexec_ExecutionState38(self):
        return self.__sexec_ExecutionState38

    @sexec_ExecutionState38.setter
    def sexec_ExecutionState38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sexec_ExecutionState__sexec_ExecutionState38", None)
        self.__sexec_ExecutionState38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sexec_EnterState"):
                opp_val = getattr(old_value, "sexec_EnterState", None)
                if opp_val == self:
                    setattr(old_value, "sexec_EnterState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sexec_EnterState"):
                opp_val = getattr(value, "sexec_EnterState", None)
                setattr(value, "sexec_EnterState", self)
