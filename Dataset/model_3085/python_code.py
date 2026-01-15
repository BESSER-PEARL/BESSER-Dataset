from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ObjectNodeOrderingKind(Enum):
    FIFO = "FIFO"
    LIFO = "LIFO"
    ordered = "ordered"
    unordered = "unordered"
class ObjectNodeKind(Enum):
    Unspecified = "Unspecified"
    NoBuffer = "NoBuffer"
    Overwrite = "Overwrite"


############################################
# Definition of Classes
############################################

class Pin:

    pass
class ObjectNode:

    pass
class activity_Pin(ObjectNode):

    def __init__(self, isControl: bool):
        self.isControl = isControl
        
    @property
    def isControl(self) -> bool:
        return self.__isControl

    @isControl.setter
    def isControl(self, isControl: bool):
        self.__isControl = isControl

class AbstractAction:

    pass
class activity_AcceptEventAction(AbstractAction):

    def __init__(self, isUnmarshall: bool):
        self.isUnmarshall = isUnmarshall
        
    @property
    def isUnmarshall(self) -> bool:
        return self.__isUnmarshall

    @isUnmarshall.setter
    def isUnmarshall(self, isUnmarshall: bool):
        self.__isUnmarshall = isUnmarshall

class activity_OutputPin(Pin):

    pass
class activity_InputPin(Pin):

    pass
class ActivityNode:

    pass
class activity_AbstractBehavior:

    pass
class activity_IState:

    pass
class AbstractNamedElement:

    pass
class activity_ObjectNode(AbstractNamedElement, ActivityNode):

    def __init__(self, isControlType: bool, kindOfNode: str, ordering: str, activity_ObjectNode: "activity_ValueSpecification" = None, activity_ObjectNode27: set["activity_IState"] = None, activity_ObjectNode29: "activity_AbstractBehavior" = None):
        self.isControlType = isControlType
        self.kindOfNode = kindOfNode
        self.ordering = ordering
        self.activity_ObjectNode = activity_ObjectNode
        self.activity_ObjectNode27 = activity_ObjectNode27 if activity_ObjectNode27 is not None else set()
        self.activity_ObjectNode29 = activity_ObjectNode29
        
    @property
    def isControlType(self) -> bool:
        return self.__isControlType

    @isControlType.setter
    def isControlType(self, isControlType: bool):
        self.__isControlType = isControlType

    @property
    def kindOfNode(self) -> str:
        return self.__kindOfNode

    @kindOfNode.setter
    def kindOfNode(self, kindOfNode: str):
        self.__kindOfNode = kindOfNode

    @property
    def ordering(self) -> str:
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering

    @property
    def activity_ObjectNode29(self):
        return self.__activity_ObjectNode29

    @activity_ObjectNode29.setter
    def activity_ObjectNode29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activity_ObjectNode__activity_ObjectNode29", None)
        self.__activity_ObjectNode29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activity_AbstractBehavior"):
                opp_val = getattr(old_value, "activity_AbstractBehavior", None)
                if opp_val == self:
                    setattr(old_value, "activity_AbstractBehavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activity_AbstractBehavior"):
                opp_val = getattr(value, "activity_AbstractBehavior", None)
                setattr(value, "activity_AbstractBehavior", self)

    @property
    def activity_ObjectNode27(self):
        return self.__activity_ObjectNode27

    @activity_ObjectNode27.setter
    def activity_ObjectNode27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activity_ObjectNode__activity_ObjectNode27", None)
        self.__activity_ObjectNode27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activity_IState"):
                    opp_val = getattr(item, "activity_IState", None)
                    
                    if opp_val == self:
                        setattr(item, "activity_IState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activity_IState"):
                    opp_val = getattr(item, "activity_IState", None)
                    
                    setattr(item, "activity_IState", self)
                    

    @property
    def activity_ObjectNode(self):
        return self.__activity_ObjectNode

    @activity_ObjectNode.setter
    def activity_ObjectNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activity_ObjectNode__activity_ObjectNode", None)
        self.__activity_ObjectNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activity_ValueSpecification25"):
                opp_val = getattr(old_value, "activity_ValueSpecification25", None)
                if opp_val == self:
                    setattr(old_value, "activity_ValueSpecification25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activity_ValueSpecification25"):
                opp_val = getattr(value, "activity_ValueSpecification25", None)
                setattr(value, "activity_ValueSpecification25", self)

class ActivityEdge:

    pass
class activity_ObjectFlow(ActivityEdge):

    def __init__(self, isMulticast: bool, isMultireceive: bool):
        self.isMulticast = isMulticast
        self.isMultireceive = isMultireceive
        
    @property
    def isMulticast(self) -> bool:
        return self.__isMulticast

    @isMulticast.setter
    def isMulticast(self, isMulticast: bool):
        self.__isMulticast = isMulticast

    @property
    def isMultireceive(self) -> bool:
        return self.__isMultireceive

    @isMultireceive.setter
    def isMultireceive(self, isMultireceive: bool):
        self.__isMultireceive = isMultireceive

class activity_AbstractAction(AbstractNamedElement, ActivityNode):

    pass
class ModelElement:

    pass
class activity_ActivityPartition(AbstractNamedElement, ModelElement):

    def __init__(self, isDimension: bool, isExternal: bool):
        self.isDimension = isDimension
        self.isExternal = isExternal
        
    @property
    def isExternal(self) -> bool:
        return self.__isExternal

    @isExternal.setter
    def isExternal(self, isExternal: bool):
        self.__isExternal = isExternal

    @property
    def isDimension(self) -> bool:
        return self.__isDimension

    @isDimension.setter
    def isDimension(self, isDimension: bool):
        self.__isDimension = isDimension

class activity_ActivityEdge(ModelElement):

    def __init__(self, kindOfRate: str, activity_ActivityEdge: "activity_ValueSpecification" = None, activity_ActivityEdge2: "activity_ValueSpecification" = None, activity_ActivityEdge5: "activity_ActivityNode" = None, activity_ActivityEdge7: "activity_ActivityNode" = None, activity_ActivityEdge17: "activity_ActivityNode" = None, activity_ActivityEdge20: "activity_ActivityNode" = None, activity_ActivityEdge10: "activity_ValueSpecification" = None, activity_ActivityEdge13: "activity_ValueSpecification" = None):
        self.kindOfRate = kindOfRate
        self.activity_ActivityEdge = activity_ActivityEdge
        self.activity_ActivityEdge2 = activity_ActivityEdge2
        self.activity_ActivityEdge5 = activity_ActivityEdge5
        self.activity_ActivityEdge7 = activity_ActivityEdge7
        self.activity_ActivityEdge17 = activity_ActivityEdge17
        self.activity_ActivityEdge20 = activity_ActivityEdge20
        self.activity_ActivityEdge10 = activity_ActivityEdge10
        self.activity_ActivityEdge13 = activity_ActivityEdge13
        
    @property
    def kindOfRate(self) -> str:
        return self.__kindOfRate

    @kindOfRate.setter
    def kindOfRate(self, kindOfRate: str):
        self.__kindOfRate = kindOfRate

    @property
    def activity_ActivityEdge13(self):
        return self.__activity_ActivityEdge13

    @activity_ActivityEdge13.setter
    def activity_ActivityEdge13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activity_ActivityEdge__activity_ActivityEdge13", None)
        self.__activity_ActivityEdge13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activity_ValueSpecification14"):
                opp_val = getattr(old_value, "activity_ValueSpecification14", None)
                if opp_val == self:
                    setattr(old_value, "activity_ValueSpecification14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activity_ValueSpecification14"):
                opp_val = getattr(value, "activity_ValueSpecification14", None)
                setattr(value, "activity_ValueSpecification14", self)

    @property
    def activity_ActivityEdge10(self):
        return self.__activity_ActivityEdge10

    @activity_ActivityEdge10.setter
    def activity_ActivityEdge10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activity_ActivityEdge__activity_ActivityEdge10", None)
        self.__activity_ActivityEdge10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activity_ValueSpecification11"):
                opp_val = getattr(old_value, "activity_ValueSpecification11", None)
                if opp_val == self:
                    setattr(old_value, "activity_ValueSpecification11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activity_ValueSpecification11"):
                opp_val = getattr(value, "activity_ValueSpecification11", None)
                setattr(value, "activity_ValueSpecification11", self)

    @property
    def activity_ActivityEdge2(self):
        return self.__activity_ActivityEdge2

    @activity_ActivityEdge2.setter
    def activity_ActivityEdge2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activity_ActivityEdge__activity_ActivityEdge2", None)
        self.__activity_ActivityEdge2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activity_ValueSpecification3"):
                opp_val = getattr(old_value, "activity_ValueSpecification3", None)
                if opp_val == self:
                    setattr(old_value, "activity_ValueSpecification3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activity_ValueSpecification3"):
                opp_val = getattr(value, "activity_ValueSpecification3", None)
                setattr(value, "activity_ValueSpecification3", self)

    @property
    def activity_ActivityEdge17(self):
        return self.__activity_ActivityEdge17

    @activity_ActivityEdge17.setter
    def activity_ActivityEdge17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activity_ActivityEdge__activity_ActivityEdge17", None)
        self.__activity_ActivityEdge17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activity_ActivityNode16"):
                opp_val = getattr(old_value, "activity_ActivityNode16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activity_ActivityNode16"):
                opp_val = getattr(value, "activity_ActivityNode16", None)
                if opp_val is None:
                    setattr(value, "activity_ActivityNode16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activity_ActivityEdge(self):
        return self.__activity_ActivityEdge

    @activity_ActivityEdge.setter
    def activity_ActivityEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activity_ActivityEdge__activity_ActivityEdge", None)
        self.__activity_ActivityEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activity_ValueSpecification"):
                opp_val = getattr(old_value, "activity_ValueSpecification", None)
                if opp_val == self:
                    setattr(old_value, "activity_ValueSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activity_ValueSpecification"):
                opp_val = getattr(value, "activity_ValueSpecification", None)
                setattr(value, "activity_ValueSpecification", self)

    @property
    def activity_ActivityEdge5(self):
        return self.__activity_ActivityEdge5

    @activity_ActivityEdge5.setter
    def activity_ActivityEdge5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activity_ActivityEdge__activity_ActivityEdge5", None)
        self.__activity_ActivityEdge5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activity_ActivityNode"):
                opp_val = getattr(old_value, "activity_ActivityNode", None)
                if opp_val == self:
                    setattr(old_value, "activity_ActivityNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activity_ActivityNode"):
                opp_val = getattr(value, "activity_ActivityNode", None)
                setattr(value, "activity_ActivityNode", self)

    @property
    def activity_ActivityEdge7(self):
        return self.__activity_ActivityEdge7

    @activity_ActivityEdge7.setter
    def activity_ActivityEdge7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activity_ActivityEdge__activity_ActivityEdge7", None)
        self.__activity_ActivityEdge7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activity_ActivityNode8"):
                opp_val = getattr(old_value, "activity_ActivityNode8", None)
                if opp_val == self:
                    setattr(old_value, "activity_ActivityNode8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activity_ActivityNode8"):
                opp_val = getattr(value, "activity_ActivityNode8", None)
                setattr(value, "activity_ActivityNode8", self)

    @property
    def activity_ActivityEdge20(self):
        return self.__activity_ActivityEdge20

    @activity_ActivityEdge20.setter
    def activity_ActivityEdge20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activity_ActivityEdge__activity_ActivityEdge20", None)
        self.__activity_ActivityEdge20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activity_ActivityNode19"):
                opp_val = getattr(old_value, "activity_ActivityNode19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activity_ActivityNode19"):
                opp_val = getattr(value, "activity_ActivityNode19", None)
                if opp_val is None:
                    setattr(value, "activity_ActivityNode19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TraceableElement:

    pass
class AbstractBehavior:

    pass
class activity_AbstractActivity(AbstractBehavior, TraceableElement):

    def __init__(self, isReadOnly: bool, isSingleExecution: bool):
        self.isReadOnly = isReadOnly
        self.isSingleExecution = isSingleExecution
        
    @property
    def isSingleExecution(self) -> bool:
        return self.__isSingleExecution

    @isSingleExecution.setter
    def isSingleExecution(self, isSingleExecution: bool):
        self.__isSingleExecution = isSingleExecution

    @property
    def isReadOnly(self) -> bool:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly

class activity_ActivityNode(AbstractNamedElement):

    pass
class activity_ValueSpecification:

    pass