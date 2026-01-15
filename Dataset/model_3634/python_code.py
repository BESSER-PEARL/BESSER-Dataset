from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VisibilityKind(Enum):
    public = "public"
    protected = "protected"
    package = "package"


############################################
# Definition of Classes
############################################

class ValueSpecification:

    pass
class umlknes_OpaqueExpression(ValueSpecification):

    pass
class Event:

    pass
class umlknes_DestructionEvent(Event):

    pass
class umlknes_CreationEvent(Event):

    pass
class umlknes_ExecutionEvent(Event):

    pass
class umlknes_Event(ABC):

    pass
class umlknes_NamedElement(ABC):

    def __init__(self, visibility: str):
        self.visibility = visibility
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

class NamedElement:

    pass
class umlknes_RedefinableElement(NamedElement):

    def __init__(self, isLeaf: bool):
        self.isLeaf = isLeaf
        
    @property
    def isLeaf(self) -> bool:
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: bool):
        self.__isLeaf = isLeaf

class umlknes_Trigger(NamedElement):

    pass
class Action:

    pass
class umlknes_AcceptEventAction(Action):

    def __init__(self, isUnMarshall: bool, umlknes_AcceptEventAction: set["umlknes_Trigger"] = None):
        self.isUnMarshall = isUnMarshall
        self.umlknes_AcceptEventAction = umlknes_AcceptEventAction if umlknes_AcceptEventAction is not None else set()
        
    @property
    def isUnMarshall(self) -> bool:
        return self.__isUnMarshall

    @isUnMarshall.setter
    def isUnMarshall(self, isUnMarshall: bool):
        self.__isUnMarshall = isUnMarshall

    @property
    def umlknes_AcceptEventAction(self):
        return self.__umlknes_AcceptEventAction

    @umlknes_AcceptEventAction.setter
    def umlknes_AcceptEventAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlknes_AcceptEventAction__umlknes_AcceptEventAction", None)
        self.__umlknes_AcceptEventAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umlknes_Trigger"):
                    opp_val = getattr(item, "umlknes_Trigger", None)
                    
                    if opp_val == self:
                        setattr(item, "umlknes_Trigger", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umlknes_Trigger"):
                    opp_val = getattr(item, "umlknes_Trigger", None)
                    
                    setattr(item, "umlknes_Trigger", self)
                    

class ActivityEdge:

    pass
class umlknes_ControlFlow(ActivityEdge):

    pass
class umlknes_ValueSpecification(NamedElement):

    pass
class ControlNode:

    pass
class umlknes_InitialNode(ControlNode):

    pass
class umlknes_DecisionNode(ControlNode):

    pass
class umlknes_ActivityFinalNode(ControlNode):

    pass
class ActivityNode:

    pass
class umlknes_Action(ActivityNode):

    pass
class umlknes_ControlNode(ActivityNode):

    pass
class RedefinableElement:

    pass
class umlknes_ActivityEdge(RedefinableElement):

    pass
class umlknes_ActivityNode(RedefinableElement):

    pass
class umlknes_Activity:

    def __init__(self, isReadOnly: bool, isSingleExecution: bool, activity: set["umlknes_ActivityNode"] = None, activity2: set["umlknes_ActivityEdge"] = None, Activity: "umlknes_ActivityNode" = None, Activity15: "umlknes_ActivityEdge" = None):
        self.isReadOnly = isReadOnly
        self.isSingleExecution = isSingleExecution
        self.activity = activity if activity is not None else set()
        self.activity2 = activity2 if activity2 is not None else set()
        self.Activity = Activity
        self.Activity15 = Activity15
        
    @property
    def isReadOnly(self) -> bool:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly

    @property
    def isSingleExecution(self) -> bool:
        return self.__isSingleExecution

    @isSingleExecution.setter
    def isSingleExecution(self, isSingleExecution: bool):
        self.__isSingleExecution = isSingleExecution

    @property
    def Activity15(self):
        return self.__Activity15

    @Activity15.setter
    def Activity15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlknes_Activity__Activity15", None)
        self.__Activity15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edge"):
                opp_val = getattr(old_value, "edge", None)
                if opp_val == self:
                    setattr(old_value, "edge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edge"):
                opp_val = getattr(value, "edge", None)
                setattr(value, "edge", self)

    @property
    def Activity(self):
        return self.__Activity

    @Activity.setter
    def Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlknes_Activity__Activity", None)
        self.__Activity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "node"):
                opp_val = getattr(old_value, "node", None)
                if opp_val == self:
                    setattr(old_value, "node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "node"):
                opp_val = getattr(value, "node", None)
                setattr(value, "node", self)

    @property
    def activity2(self):
        return self.__activity2

    @activity2.setter
    def activity2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlknes_Activity__activity2", None)
        self.__activity2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityEdge"):
                    opp_val = getattr(item, "ActivityEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityEdge"):
                    opp_val = getattr(item, "ActivityEdge", None)
                    
                    setattr(item, "ActivityEdge", self)
                    

    @property
    def activity(self):
        return self.__activity

    @activity.setter
    def activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlknes_Activity__activity", None)
        self.__activity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityNode"):
                    opp_val = getattr(item, "ActivityNode", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityNode"):
                    opp_val = getattr(item, "ActivityNode", None)
                    
                    setattr(item, "ActivityNode", self)
                    
