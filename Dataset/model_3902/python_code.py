from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AssociationDirection(Enum):
    none = "none"
    one = "one"
    both = "both"
class MultiInstanceBehavior(Enum):
    none = "none"
    one = "one"
    all = "all"
    complex = "complex"
class GatewayDirection(Enum):
    unspecified = "unspecified"
    converging = "converging"
    diverging = "diverging"
    mixed = "mixed"
class EventBasedGatewayType(Enum):
    exclusive = "exclusive"
    parallel = "parallel"
class ProcessType(Enum):
    private = "private"
    none = "none"
    public = "public"
class ItemKind(Enum):
    physical = "physical"
    information = "information"
class AdHocOrdering(Enum):
    parallel = "parallel"
    sequential = "sequential"
class RelationshipDirection(Enum):
    none = "none"
    forward = "forward"
    backward = "backward"
    both = "both"


############################################
# Definition of Classes
############################################

class BPMNProfile_ExpansionRegion:

    pass
class BPMNProfile_LoopNode:

    pass
class LoopCharacteristics:

    pass
class BPMNProfile_MultiInstanceLoopCharacteristics(LoopCharacteristics):

    def __init__(self, isSequential: str, behavior: str, BPMNProfile_MultiInstanceLoopCharacteristics664: "BPMNProfile_ItemAwareElement" = None, BPMNProfile_MultiInstanceLoopCharacteristics667: "BPMNProfile_ItemAwareElement" = None, BPMNProfile_MultiInstanceLoopCharacteristics670: "BPMNProfile_DataOutput" = None, BPMNProfile_MultiInstanceLoopCharacteristics: "BPMNProfile_BPMNExpression" = None, BPMNProfile_MultiInstanceLoopCharacteristics659: "BPMNProfile_BPMNExpression" = None, BPMNProfile_MultiInstanceLoopCharacteristics662: "BPMNProfile_ExpansionRegion" = None, BPMNProfile_MultiInstanceLoopCharacteristics673: "BPMNProfile_DataInput" = None, BPMNProfile_MultiInstanceLoopCharacteristics676: "BPMNProfile_EventDefinition" = None, BPMNProfile_MultiInstanceLoopCharacteristics679: "BPMNProfile_EventDefinition" = None, BPMNProfile_MultiInstanceLoopCharacteristics682: set["BPMNProfile_ComplexBehaviorDefinition"] = None):
        self.isSequential = isSequential
        self.behavior = behavior
        self.BPMNProfile_MultiInstanceLoopCharacteristics664 = BPMNProfile_MultiInstanceLoopCharacteristics664
        self.BPMNProfile_MultiInstanceLoopCharacteristics667 = BPMNProfile_MultiInstanceLoopCharacteristics667
        self.BPMNProfile_MultiInstanceLoopCharacteristics670 = BPMNProfile_MultiInstanceLoopCharacteristics670
        self.BPMNProfile_MultiInstanceLoopCharacteristics = BPMNProfile_MultiInstanceLoopCharacteristics
        self.BPMNProfile_MultiInstanceLoopCharacteristics659 = BPMNProfile_MultiInstanceLoopCharacteristics659
        self.BPMNProfile_MultiInstanceLoopCharacteristics662 = BPMNProfile_MultiInstanceLoopCharacteristics662
        self.BPMNProfile_MultiInstanceLoopCharacteristics673 = BPMNProfile_MultiInstanceLoopCharacteristics673
        self.BPMNProfile_MultiInstanceLoopCharacteristics676 = BPMNProfile_MultiInstanceLoopCharacteristics676
        self.BPMNProfile_MultiInstanceLoopCharacteristics679 = BPMNProfile_MultiInstanceLoopCharacteristics679
        self.BPMNProfile_MultiInstanceLoopCharacteristics682 = BPMNProfile_MultiInstanceLoopCharacteristics682 if BPMNProfile_MultiInstanceLoopCharacteristics682 is not None else set()
        
    @property
    def isSequential(self) -> str:
        return self.__isSequential

    @isSequential.setter
    def isSequential(self, isSequential: str):
        self.__isSequential = isSequential

    @property
    def behavior(self) -> str:
        return self.__behavior

    @behavior.setter
    def behavior(self, behavior: str):
        self.__behavior = behavior

    @property
    def BPMNProfile_MultiInstanceLoopCharacteristics679(self):
        return self.__BPMNProfile_MultiInstanceLoopCharacteristics679

    @BPMNProfile_MultiInstanceLoopCharacteristics679.setter
    def BPMNProfile_MultiInstanceLoopCharacteristics679(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MultiInstanceLoopCharacteristics__BPMNProfile_MultiInstanceLoopCharacteristics679", None)
        self.__BPMNProfile_MultiInstanceLoopCharacteristics679 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_EventDefinition680"):
                opp_val = getattr(old_value, "BPMNProfile_EventDefinition680", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_EventDefinition680", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_EventDefinition680"):
                opp_val = getattr(value, "BPMNProfile_EventDefinition680", None)
                setattr(value, "BPMNProfile_EventDefinition680", self)

    @property
    def BPMNProfile_MultiInstanceLoopCharacteristics676(self):
        return self.__BPMNProfile_MultiInstanceLoopCharacteristics676

    @BPMNProfile_MultiInstanceLoopCharacteristics676.setter
    def BPMNProfile_MultiInstanceLoopCharacteristics676(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MultiInstanceLoopCharacteristics__BPMNProfile_MultiInstanceLoopCharacteristics676", None)
        self.__BPMNProfile_MultiInstanceLoopCharacteristics676 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_EventDefinition677"):
                opp_val = getattr(old_value, "BPMNProfile_EventDefinition677", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_EventDefinition677", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_EventDefinition677"):
                opp_val = getattr(value, "BPMNProfile_EventDefinition677", None)
                setattr(value, "BPMNProfile_EventDefinition677", self)

    @property
    def BPMNProfile_MultiInstanceLoopCharacteristics(self):
        return self.__BPMNProfile_MultiInstanceLoopCharacteristics

    @BPMNProfile_MultiInstanceLoopCharacteristics.setter
    def BPMNProfile_MultiInstanceLoopCharacteristics(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MultiInstanceLoopCharacteristics__BPMNProfile_MultiInstanceLoopCharacteristics", None)
        self.__BPMNProfile_MultiInstanceLoopCharacteristics = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNExpression657"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNExpression657", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNExpression657", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNExpression657"):
                opp_val = getattr(value, "BPMNProfile_BPMNExpression657", None)
                setattr(value, "BPMNProfile_BPMNExpression657", self)

    @property
    def BPMNProfile_MultiInstanceLoopCharacteristics670(self):
        return self.__BPMNProfile_MultiInstanceLoopCharacteristics670

    @BPMNProfile_MultiInstanceLoopCharacteristics670.setter
    def BPMNProfile_MultiInstanceLoopCharacteristics670(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MultiInstanceLoopCharacteristics__BPMNProfile_MultiInstanceLoopCharacteristics670", None)
        self.__BPMNProfile_MultiInstanceLoopCharacteristics670 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_DataOutput671"):
                opp_val = getattr(old_value, "BPMNProfile_DataOutput671", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_DataOutput671", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_DataOutput671"):
                opp_val = getattr(value, "BPMNProfile_DataOutput671", None)
                setattr(value, "BPMNProfile_DataOutput671", self)

    @property
    def BPMNProfile_MultiInstanceLoopCharacteristics659(self):
        return self.__BPMNProfile_MultiInstanceLoopCharacteristics659

    @BPMNProfile_MultiInstanceLoopCharacteristics659.setter
    def BPMNProfile_MultiInstanceLoopCharacteristics659(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MultiInstanceLoopCharacteristics__BPMNProfile_MultiInstanceLoopCharacteristics659", None)
        self.__BPMNProfile_MultiInstanceLoopCharacteristics659 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNExpression660"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNExpression660", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNExpression660", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNExpression660"):
                opp_val = getattr(value, "BPMNProfile_BPMNExpression660", None)
                setattr(value, "BPMNProfile_BPMNExpression660", self)

    @property
    def BPMNProfile_MultiInstanceLoopCharacteristics662(self):
        return self.__BPMNProfile_MultiInstanceLoopCharacteristics662

    @BPMNProfile_MultiInstanceLoopCharacteristics662.setter
    def BPMNProfile_MultiInstanceLoopCharacteristics662(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MultiInstanceLoopCharacteristics__BPMNProfile_MultiInstanceLoopCharacteristics662", None)
        self.__BPMNProfile_MultiInstanceLoopCharacteristics662 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ExpansionRegion"):
                opp_val = getattr(old_value, "BPMNProfile_ExpansionRegion", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ExpansionRegion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ExpansionRegion"):
                opp_val = getattr(value, "BPMNProfile_ExpansionRegion", None)
                setattr(value, "BPMNProfile_ExpansionRegion", self)

    @property
    def BPMNProfile_MultiInstanceLoopCharacteristics664(self):
        return self.__BPMNProfile_MultiInstanceLoopCharacteristics664

    @BPMNProfile_MultiInstanceLoopCharacteristics664.setter
    def BPMNProfile_MultiInstanceLoopCharacteristics664(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MultiInstanceLoopCharacteristics__BPMNProfile_MultiInstanceLoopCharacteristics664", None)
        self.__BPMNProfile_MultiInstanceLoopCharacteristics664 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ItemAwareElement665"):
                opp_val = getattr(old_value, "BPMNProfile_ItemAwareElement665", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ItemAwareElement665", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ItemAwareElement665"):
                opp_val = getattr(value, "BPMNProfile_ItemAwareElement665", None)
                setattr(value, "BPMNProfile_ItemAwareElement665", self)

    @property
    def BPMNProfile_MultiInstanceLoopCharacteristics667(self):
        return self.__BPMNProfile_MultiInstanceLoopCharacteristics667

    @BPMNProfile_MultiInstanceLoopCharacteristics667.setter
    def BPMNProfile_MultiInstanceLoopCharacteristics667(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MultiInstanceLoopCharacteristics__BPMNProfile_MultiInstanceLoopCharacteristics667", None)
        self.__BPMNProfile_MultiInstanceLoopCharacteristics667 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ItemAwareElement668"):
                opp_val = getattr(old_value, "BPMNProfile_ItemAwareElement668", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ItemAwareElement668", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ItemAwareElement668"):
                opp_val = getattr(value, "BPMNProfile_ItemAwareElement668", None)
                setattr(value, "BPMNProfile_ItemAwareElement668", self)

    @property
    def BPMNProfile_MultiInstanceLoopCharacteristics682(self):
        return self.__BPMNProfile_MultiInstanceLoopCharacteristics682

    @BPMNProfile_MultiInstanceLoopCharacteristics682.setter
    def BPMNProfile_MultiInstanceLoopCharacteristics682(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MultiInstanceLoopCharacteristics__BPMNProfile_MultiInstanceLoopCharacteristics682", None)
        self.__BPMNProfile_MultiInstanceLoopCharacteristics682 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_ComplexBehaviorDefinition683"):
                    opp_val = getattr(item, "BPMNProfile_ComplexBehaviorDefinition683", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_ComplexBehaviorDefinition683", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_ComplexBehaviorDefinition683"):
                    opp_val = getattr(item, "BPMNProfile_ComplexBehaviorDefinition683", None)
                    
                    setattr(item, "BPMNProfile_ComplexBehaviorDefinition683", self)
                    

    @property
    def BPMNProfile_MultiInstanceLoopCharacteristics673(self):
        return self.__BPMNProfile_MultiInstanceLoopCharacteristics673

    @BPMNProfile_MultiInstanceLoopCharacteristics673.setter
    def BPMNProfile_MultiInstanceLoopCharacteristics673(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MultiInstanceLoopCharacteristics__BPMNProfile_MultiInstanceLoopCharacteristics673", None)
        self.__BPMNProfile_MultiInstanceLoopCharacteristics673 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_DataInput674"):
                opp_val = getattr(old_value, "BPMNProfile_DataInput674", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_DataInput674", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_DataInput674"):
                opp_val = getattr(value, "BPMNProfile_DataInput674", None)
                setattr(value, "BPMNProfile_DataInput674", self)

    def MultiinstanceLoopCharacteristicstarget(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MultiinstanceLoopCharacteristicstarget method
        pass

class BPMNProfile_StandardLoopCharacteristics(LoopCharacteristics):

    def __init__(self, loopMaximum: str, testBefore: str, BPMNProfile_StandardLoopCharacteristics: "BPMNProfile_LoopNode" = None, BPMNProfile_StandardLoopCharacteristics641: "BPMNProfile_BPMNExpression" = None):
        self.loopMaximum = loopMaximum
        self.testBefore = testBefore
        self.BPMNProfile_StandardLoopCharacteristics = BPMNProfile_StandardLoopCharacteristics
        self.BPMNProfile_StandardLoopCharacteristics641 = BPMNProfile_StandardLoopCharacteristics641
        
    @property
    def loopMaximum(self) -> str:
        return self.__loopMaximum

    @loopMaximum.setter
    def loopMaximum(self, loopMaximum: str):
        self.__loopMaximum = loopMaximum

    @property
    def testBefore(self) -> str:
        return self.__testBefore

    @testBefore.setter
    def testBefore(self, testBefore: str):
        self.__testBefore = testBefore

    @property
    def BPMNProfile_StandardLoopCharacteristics(self):
        return self.__BPMNProfile_StandardLoopCharacteristics

    @BPMNProfile_StandardLoopCharacteristics.setter
    def BPMNProfile_StandardLoopCharacteristics(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_StandardLoopCharacteristics__BPMNProfile_StandardLoopCharacteristics", None)
        self.__BPMNProfile_StandardLoopCharacteristics = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_LoopNode"):
                opp_val = getattr(old_value, "BPMNProfile_LoopNode", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_LoopNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_LoopNode"):
                opp_val = getattr(value, "BPMNProfile_LoopNode", None)
                setattr(value, "BPMNProfile_LoopNode", self)

    @property
    def BPMNProfile_StandardLoopCharacteristics641(self):
        return self.__BPMNProfile_StandardLoopCharacteristics641

    @BPMNProfile_StandardLoopCharacteristics641.setter
    def BPMNProfile_StandardLoopCharacteristics641(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_StandardLoopCharacteristics__BPMNProfile_StandardLoopCharacteristics641", None)
        self.__BPMNProfile_StandardLoopCharacteristics641 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNExpression642"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNExpression642", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNExpression642", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNExpression642"):
                opp_val = getattr(value, "BPMNProfile_BPMNExpression642", None)
                setattr(value, "BPMNProfile_BPMNExpression642", self)

    def StandardLoopCharacteristicsloopCondition(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement StandardLoopCharacteristicsloopCondition method
        pass

    def StandardLoopCharacteristicstestBefore(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement StandardLoopCharacteristicstestBefore method
        pass

class SubProcess:

    pass
class BPMNProfile_Transaction(SubProcess):

    def __init__(self, method: str):
        self.method = method
        
    @property
    def method(self) -> str:
        return self.__method

    @method.setter
    def method(self, method: str):
        self.__method = method

class BPMNProfile_AdHocSubProcess(SubProcess):

    def __init__(self, ordering: str, cancelRemainingInstances: str, BPMNProfile_AdHocSubProcess: "BPMNProfile_BPMNExpression" = None):
        self.ordering = ordering
        self.cancelRemainingInstances = cancelRemainingInstances
        self.BPMNProfile_AdHocSubProcess = BPMNProfile_AdHocSubProcess
        
    @property
    def ordering(self) -> str:
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering

    @property
    def cancelRemainingInstances(self) -> str:
        return self.__cancelRemainingInstances

    @cancelRemainingInstances.setter
    def cancelRemainingInstances(self, cancelRemainingInstances: str):
        self.__cancelRemainingInstances = cancelRemainingInstances

    @property
    def BPMNProfile_AdHocSubProcess(self):
        return self.__BPMNProfile_AdHocSubProcess

    @BPMNProfile_AdHocSubProcess.setter
    def BPMNProfile_AdHocSubProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_AdHocSubProcess__BPMNProfile_AdHocSubProcess", None)
        self.__BPMNProfile_AdHocSubProcess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNExpression628"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNExpression628", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNExpression628", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNExpression628"):
                opp_val = getattr(value, "BPMNProfile_BPMNExpression628", None)
                setattr(value, "BPMNProfile_BPMNExpression628", self)

    def AdHocSubProcesscancelRemainingInstances(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AdHocSubProcesscancelRemainingInstances method
        pass

class BPMNProfile_CallBehaviorAction:

    pass
class BPMNProfile_CollaborationUse:

    pass
class BPMNCollaboration:

    pass
class BPMNProfile_GlobalConversation(BPMNCollaboration):

    def __init__(self):
        
    def GlobalConversationcontainedelements(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement GlobalConversationcontainedelements method
        pass

class ResourceRole:

    pass
class BPMNProfile_Performer(ResourceRole):

    pass
class Performer:

    pass
class BPMNProfile_HumanPerformer(Performer):

    pass
class BPMNProfile_Image:

    pass
class BPMNActivity:

    pass
class BPMNProfile_CallActivity(BPMNActivity):

    def __init__(self, BPMNProfile_CallActivity: "BPMNProfile_CallBehaviorAction" = None, BPMNProfile_CallActivity616: "BPMNProfile_CallableElement" = None):
        self.BPMNProfile_CallActivity = BPMNProfile_CallActivity
        self.BPMNProfile_CallActivity616 = BPMNProfile_CallActivity616
        
    @property
    def BPMNProfile_CallActivity616(self):
        return self.__BPMNProfile_CallActivity616

    @BPMNProfile_CallActivity616.setter
    def BPMNProfile_CallActivity616(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CallActivity__BPMNProfile_CallActivity616", None)
        self.__BPMNProfile_CallActivity616 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CallableElement617"):
                opp_val = getattr(old_value, "BPMNProfile_CallableElement617", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_CallableElement617", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CallableElement617"):
                opp_val = getattr(value, "BPMNProfile_CallableElement617", None)
                setattr(value, "BPMNProfile_CallableElement617", self)

    @property
    def BPMNProfile_CallActivity(self):
        return self.__BPMNProfile_CallActivity

    @BPMNProfile_CallActivity.setter
    def BPMNProfile_CallActivity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CallActivity__BPMNProfile_CallActivity", None)
        self.__BPMNProfile_CallActivity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CallBehaviorAction"):
                opp_val = getattr(old_value, "BPMNProfile_CallBehaviorAction", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_CallBehaviorAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CallBehaviorAction"):
                opp_val = getattr(value, "BPMNProfile_CallBehaviorAction", None)
                setattr(value, "BPMNProfile_CallBehaviorAction", self)

    def CallActivitycalledElementRefvalues(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement CallActivitycalledElementRefvalues method
        pass

class BPMNProfile_Task(BPMNActivity):

    pass
class BPMNProfile_OpaqueAction:

    pass
class ConversationNode:

    pass
class BPMNProfile_CallConversation(ConversationNode):

    def __init__(self, BPMNProfile_CallConversation607: set["BPMNProfile_ParticipantAssociation"] = None, BPMNProfile_CallConversation: "BPMNProfile_CollaborationUse" = None, BPMNProfile_CallConversation604: "BPMNProfile_BPMNCollaboration" = None):
        self.BPMNProfile_CallConversation607 = BPMNProfile_CallConversation607 if BPMNProfile_CallConversation607 is not None else set()
        self.BPMNProfile_CallConversation = BPMNProfile_CallConversation
        self.BPMNProfile_CallConversation604 = BPMNProfile_CallConversation604
        
    @property
    def BPMNProfile_CallConversation607(self):
        return self.__BPMNProfile_CallConversation607

    @BPMNProfile_CallConversation607.setter
    def BPMNProfile_CallConversation607(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CallConversation__BPMNProfile_CallConversation607", None)
        self.__BPMNProfile_CallConversation607 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_ParticipantAssociation608"):
                    opp_val = getattr(item, "BPMNProfile_ParticipantAssociation608", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_ParticipantAssociation608", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_ParticipantAssociation608"):
                    opp_val = getattr(item, "BPMNProfile_ParticipantAssociation608", None)
                    
                    setattr(item, "BPMNProfile_ParticipantAssociation608", self)
                    

    @property
    def BPMNProfile_CallConversation(self):
        return self.__BPMNProfile_CallConversation

    @BPMNProfile_CallConversation.setter
    def BPMNProfile_CallConversation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CallConversation__BPMNProfile_CallConversation", None)
        self.__BPMNProfile_CallConversation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CollaborationUse"):
                opp_val = getattr(old_value, "BPMNProfile_CollaborationUse", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_CollaborationUse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CollaborationUse"):
                opp_val = getattr(value, "BPMNProfile_CollaborationUse", None)
                setattr(value, "BPMNProfile_CollaborationUse", self)

    @property
    def BPMNProfile_CallConversation604(self):
        return self.__BPMNProfile_CallConversation604

    @BPMNProfile_CallConversation604.setter
    def BPMNProfile_CallConversation604(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CallConversation__BPMNProfile_CallConversation604", None)
        self.__BPMNProfile_CallConversation604 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNCollaboration605"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNCollaboration605", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNCollaboration605", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNCollaboration605"):
                opp_val = getattr(value, "BPMNProfile_BPMNCollaboration605", None)
                setattr(value, "BPMNProfile_BPMNCollaboration605", self)

    def CallConversationparticipantAssociations(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement CallConversationparticipantAssociations method
        pass

    def CallConversationcalledCollaborationRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement CallConversationcalledCollaborationRef method
        pass

class BPMNProfile_Conversation(ConversationNode):

    pass
class BPMNProfile_SubConversation(ConversationNode):

    def __init__(self, BPMNProfile_SubConversation: set["BPMNProfile_ConversationNode"] = None):
        self.BPMNProfile_SubConversation = BPMNProfile_SubConversation if BPMNProfile_SubConversation is not None else set()
        
    @property
    def BPMNProfile_SubConversation(self):
        return self.__BPMNProfile_SubConversation

    @BPMNProfile_SubConversation.setter
    def BPMNProfile_SubConversation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_SubConversation__BPMNProfile_SubConversation", None)
        self.__BPMNProfile_SubConversation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_ConversationNode601"):
                    opp_val = getattr(item, "BPMNProfile_ConversationNode601", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_ConversationNode601", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_ConversationNode601"):
                    opp_val = getattr(item, "BPMNProfile_ConversationNode601", None)
                    
                    setattr(item, "BPMNProfile_ConversationNode601", self)
                    

    def SubConversationconnectedelements(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SubConversationconnectedelements method
        pass

class HumanPerformer:

    pass
class BPMNProfile_PotentialOwner(HumanPerformer):

    pass
class Task:

    pass
class BPMNProfile_ServiceTask(Task):

    def __init__(self, implementation: str, BPMNProfile_ServiceTask: "BPMNProfile_CallOperationAction" = None, BPMNProfile_ServiceTask654: "BPMNProfile_BPMNOperation" = None):
        self.implementation = implementation
        self.BPMNProfile_ServiceTask = BPMNProfile_ServiceTask
        self.BPMNProfile_ServiceTask654 = BPMNProfile_ServiceTask654
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def BPMNProfile_ServiceTask654(self):
        return self.__BPMNProfile_ServiceTask654

    @BPMNProfile_ServiceTask654.setter
    def BPMNProfile_ServiceTask654(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ServiceTask__BPMNProfile_ServiceTask654", None)
        self.__BPMNProfile_ServiceTask654 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNOperation655"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNOperation655", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNOperation655", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNOperation655"):
                opp_val = getattr(value, "BPMNProfile_BPMNOperation655", None)
                setattr(value, "BPMNProfile_BPMNOperation655", self)

    @property
    def BPMNProfile_ServiceTask(self):
        return self.__BPMNProfile_ServiceTask

    @BPMNProfile_ServiceTask.setter
    def BPMNProfile_ServiceTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ServiceTask__BPMNProfile_ServiceTask", None)
        self.__BPMNProfile_ServiceTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CallOperationAction652"):
                opp_val = getattr(old_value, "BPMNProfile_CallOperationAction652", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_CallOperationAction652", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CallOperationAction652"):
                opp_val = getattr(value, "BPMNProfile_CallOperationAction652", None)
                setattr(value, "BPMNProfile_CallOperationAction652", self)

    def ServiceTaskoutputSet(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ServiceTaskoutputSet method
        pass

    def ServiceTaskoperationRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ServiceTaskoperationRef method
        pass

    def ServiceTaskinputSet(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ServiceTaskinputSet method
        pass

class BPMNProfile_BusinessRuleTask(Task):

    def __init__(self, implementation: str, BPMNProfile_BusinessRuleTask: "BPMNProfile_OpaqueAction" = None):
        self.implementation = implementation
        self.BPMNProfile_BusinessRuleTask = BPMNProfile_BusinessRuleTask
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def BPMNProfile_BusinessRuleTask(self):
        return self.__BPMNProfile_BusinessRuleTask

    @BPMNProfile_BusinessRuleTask.setter
    def BPMNProfile_BusinessRuleTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BusinessRuleTask__BPMNProfile_BusinessRuleTask", None)
        self.__BPMNProfile_BusinessRuleTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_OpaqueAction619"):
                opp_val = getattr(old_value, "BPMNProfile_OpaqueAction619", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_OpaqueAction619", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_OpaqueAction619"):
                opp_val = getattr(value, "BPMNProfile_OpaqueAction619", None)
                setattr(value, "BPMNProfile_OpaqueAction619", self)

    def BusinessRuleTaskimplementation(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BusinessRuleTaskimplementation method
        pass

class BPMNProfile_SendTask(Task):

    def __init__(self, implementation: str, BPMNProfile_SendTask: "BPMNProfile_BPMNMessage" = None, BPMNProfile_SendTask634: "BPMNProfile_CallOperationAction" = None, BPMNProfile_SendTask637: "BPMNProfile_BPMNOperation" = None):
        self.implementation = implementation
        self.BPMNProfile_SendTask = BPMNProfile_SendTask
        self.BPMNProfile_SendTask634 = BPMNProfile_SendTask634
        self.BPMNProfile_SendTask637 = BPMNProfile_SendTask637
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def BPMNProfile_SendTask637(self):
        return self.__BPMNProfile_SendTask637

    @BPMNProfile_SendTask637.setter
    def BPMNProfile_SendTask637(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_SendTask__BPMNProfile_SendTask637", None)
        self.__BPMNProfile_SendTask637 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNOperation638"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNOperation638", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNOperation638", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNOperation638"):
                opp_val = getattr(value, "BPMNProfile_BPMNOperation638", None)
                setattr(value, "BPMNProfile_BPMNOperation638", self)

    @property
    def BPMNProfile_SendTask634(self):
        return self.__BPMNProfile_SendTask634

    @BPMNProfile_SendTask634.setter
    def BPMNProfile_SendTask634(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_SendTask__BPMNProfile_SendTask634", None)
        self.__BPMNProfile_SendTask634 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CallOperationAction635"):
                opp_val = getattr(old_value, "BPMNProfile_CallOperationAction635", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_CallOperationAction635", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CallOperationAction635"):
                opp_val = getattr(value, "BPMNProfile_CallOperationAction635", None)
                setattr(value, "BPMNProfile_CallOperationAction635", self)

    @property
    def BPMNProfile_SendTask(self):
        return self.__BPMNProfile_SendTask

    @BPMNProfile_SendTask.setter
    def BPMNProfile_SendTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_SendTask__BPMNProfile_SendTask", None)
        self.__BPMNProfile_SendTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNMessage632"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNMessage632", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNMessage632", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNMessage632"):
                opp_val = getattr(value, "BPMNProfile_BPMNMessage632", None)
                setattr(value, "BPMNProfile_BPMNMessage632", self)

    def SendTaskoperationRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SendTaskoperationRef method
        pass

class BPMNProfile_ManualTask(Task):

    pass
class BPMNProfile_ReceiveTask(Task):

    def __init__(self, implementation: str, instantiate: str, BPMNProfile_ReceiveTask646: "BPMNProfile_AcceptEventAction" = None, BPMNProfile_ReceiveTask649: "BPMNProfile_BPMNOperation" = None, BPMNProfile_ReceiveTask: "BPMNProfile_BPMNMessage" = None):
        self.implementation = implementation
        self.instantiate = instantiate
        self.BPMNProfile_ReceiveTask646 = BPMNProfile_ReceiveTask646
        self.BPMNProfile_ReceiveTask649 = BPMNProfile_ReceiveTask649
        self.BPMNProfile_ReceiveTask = BPMNProfile_ReceiveTask
        
    @property
    def instantiate(self) -> str:
        return self.__instantiate

    @instantiate.setter
    def instantiate(self, instantiate: str):
        self.__instantiate = instantiate

    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def BPMNProfile_ReceiveTask649(self):
        return self.__BPMNProfile_ReceiveTask649

    @BPMNProfile_ReceiveTask649.setter
    def BPMNProfile_ReceiveTask649(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ReceiveTask__BPMNProfile_ReceiveTask649", None)
        self.__BPMNProfile_ReceiveTask649 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNOperation650"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNOperation650", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNOperation650", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNOperation650"):
                opp_val = getattr(value, "BPMNProfile_BPMNOperation650", None)
                setattr(value, "BPMNProfile_BPMNOperation650", self)

    @property
    def BPMNProfile_ReceiveTask(self):
        return self.__BPMNProfile_ReceiveTask

    @BPMNProfile_ReceiveTask.setter
    def BPMNProfile_ReceiveTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ReceiveTask__BPMNProfile_ReceiveTask", None)
        self.__BPMNProfile_ReceiveTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNMessage644"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNMessage644", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNMessage644", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNMessage644"):
                opp_val = getattr(value, "BPMNProfile_BPMNMessage644", None)
                setattr(value, "BPMNProfile_BPMNMessage644", self)

    @property
    def BPMNProfile_ReceiveTask646(self):
        return self.__BPMNProfile_ReceiveTask646

    @BPMNProfile_ReceiveTask646.setter
    def BPMNProfile_ReceiveTask646(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ReceiveTask__BPMNProfile_ReceiveTask646", None)
        self.__BPMNProfile_ReceiveTask646 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_AcceptEventAction647"):
                opp_val = getattr(old_value, "BPMNProfile_AcceptEventAction647", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_AcceptEventAction647", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_AcceptEventAction647"):
                opp_val = getattr(value, "BPMNProfile_AcceptEventAction647", None)
                setattr(value, "BPMNProfile_AcceptEventAction647", self)

    def ReceiveTaskoperationRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ReceiveTaskoperationRef method
        pass

class BPMNProfile_ScriptTask(Task):

    def __init__(self, scriptFormat: str, script: str, BPMNProfile_ScriptTask: "BPMNProfile_OpaqueAction" = None):
        self.scriptFormat = scriptFormat
        self.script = script
        self.BPMNProfile_ScriptTask = BPMNProfile_ScriptTask
        
    @property
    def script(self) -> str:
        return self.__script

    @script.setter
    def script(self, script: str):
        self.__script = script

    @property
    def scriptFormat(self) -> str:
        return self.__scriptFormat

    @scriptFormat.setter
    def scriptFormat(self, scriptFormat: str):
        self.__scriptFormat = scriptFormat

    @property
    def BPMNProfile_ScriptTask(self):
        return self.__BPMNProfile_ScriptTask

    @BPMNProfile_ScriptTask.setter
    def BPMNProfile_ScriptTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ScriptTask__BPMNProfile_ScriptTask", None)
        self.__BPMNProfile_ScriptTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_OpaqueAction630"):
                opp_val = getattr(old_value, "BPMNProfile_OpaqueAction630", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_OpaqueAction630", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_OpaqueAction630"):
                opp_val = getattr(value, "BPMNProfile_OpaqueAction630", None)
                setattr(value, "BPMNProfile_OpaqueAction630", self)

    def ScriptTaskscript(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ScriptTaskscript method
        pass

    def ScriptTaskscriptFormat(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ScriptTaskscriptFormat method
        pass

class BPMNProfile_UserTask(Task):

    def __init__(self, implementation: str, BPMNProfile_UserTask: "BPMNProfile_OpaqueAction" = None, BPMNProfile_UserTask591: set["BPMNProfile_Rendering"] = None):
        self.implementation = implementation
        self.BPMNProfile_UserTask = BPMNProfile_UserTask
        self.BPMNProfile_UserTask591 = BPMNProfile_UserTask591 if BPMNProfile_UserTask591 is not None else set()
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def BPMNProfile_UserTask(self):
        return self.__BPMNProfile_UserTask

    @BPMNProfile_UserTask.setter
    def BPMNProfile_UserTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_UserTask__BPMNProfile_UserTask", None)
        self.__BPMNProfile_UserTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_OpaqueAction"):
                opp_val = getattr(old_value, "BPMNProfile_OpaqueAction", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_OpaqueAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_OpaqueAction"):
                opp_val = getattr(value, "BPMNProfile_OpaqueAction", None)
                setattr(value, "BPMNProfile_OpaqueAction", self)

    @property
    def BPMNProfile_UserTask591(self):
        return self.__BPMNProfile_UserTask591

    @BPMNProfile_UserTask591.setter
    def BPMNProfile_UserTask591(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_UserTask__BPMNProfile_UserTask591", None)
        self.__BPMNProfile_UserTask591 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_Rendering"):
                    opp_val = getattr(item, "BPMNProfile_Rendering", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_Rendering", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_Rendering"):
                    opp_val = getattr(item, "BPMNProfile_Rendering", None)
                    
                    setattr(item, "BPMNProfile_Rendering", self)
                    

    def UserTaskrenderings(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement UserTaskrenderings method
        pass

    def UserTaskimplementation(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement UserTaskimplementation method
        pass

class BPMNProfile_Enumeration:

    pass
class BPMNProfile_SendObjectAction:

    pass
class BPMNProfile_FlowFinalNode:

    pass
class BPMNProfile_CallOperationAction:

    pass
class BPMNProfile_ChangeEvent:

    pass
class BPMNProfile_FinalNode:

    pass
class ThrowEvent:

    pass
class BPMNProfile_ImplicitThrowEvent(ThrowEvent):

    pass
class BPMNProfile_IntermediateThrowEvent(ThrowEvent):

    pass
class BPMNProfile_EndEvent(ThrowEvent):

    pass
class BPMNProfile_ObjectFlow:

    pass
class DataAssociation:

    pass
class BPMNEvent:

    pass
class BPMNProfile_ThrowEvent(BPMNEvent):

    def __init__(self, BPMNProfile_ThrowEvent: "BPMNProfile_CallOperationAction" = None, BPMNProfile_ThrowEvent527: "BPMNProfile_FlowFinalNode" = None, BPMNProfile_ThrowEvent529: set["BPMNProfile_DataInputAssociation"] = None):
        self.BPMNProfile_ThrowEvent = BPMNProfile_ThrowEvent
        self.BPMNProfile_ThrowEvent527 = BPMNProfile_ThrowEvent527
        self.BPMNProfile_ThrowEvent529 = BPMNProfile_ThrowEvent529 if BPMNProfile_ThrowEvent529 is not None else set()
        
    @property
    def BPMNProfile_ThrowEvent527(self):
        return self.__BPMNProfile_ThrowEvent527

    @BPMNProfile_ThrowEvent527.setter
    def BPMNProfile_ThrowEvent527(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ThrowEvent__BPMNProfile_ThrowEvent527", None)
        self.__BPMNProfile_ThrowEvent527 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_FlowFinalNode"):
                opp_val = getattr(old_value, "BPMNProfile_FlowFinalNode", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_FlowFinalNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_FlowFinalNode"):
                opp_val = getattr(value, "BPMNProfile_FlowFinalNode", None)
                setattr(value, "BPMNProfile_FlowFinalNode", self)

    @property
    def BPMNProfile_ThrowEvent529(self):
        return self.__BPMNProfile_ThrowEvent529

    @BPMNProfile_ThrowEvent529.setter
    def BPMNProfile_ThrowEvent529(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ThrowEvent__BPMNProfile_ThrowEvent529", None)
        self.__BPMNProfile_ThrowEvent529 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_DataInputAssociation530"):
                    opp_val = getattr(item, "BPMNProfile_DataInputAssociation530", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_DataInputAssociation530", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_DataInputAssociation530"):
                    opp_val = getattr(item, "BPMNProfile_DataInputAssociation530", None)
                    
                    setattr(item, "BPMNProfile_DataInputAssociation530", self)
                    

    @property
    def BPMNProfile_ThrowEvent(self):
        return self.__BPMNProfile_ThrowEvent

    @BPMNProfile_ThrowEvent.setter
    def BPMNProfile_ThrowEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ThrowEvent__BPMNProfile_ThrowEvent", None)
        self.__BPMNProfile_ThrowEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CallOperationAction"):
                opp_val = getattr(old_value, "BPMNProfile_CallOperationAction", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_CallOperationAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CallOperationAction"):
                opp_val = getattr(value, "BPMNProfile_CallOperationAction", None)
                setattr(value, "BPMNProfile_CallOperationAction", self)

    def ThrowEventeventDefinitionRefs(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ThrowEventeventDefinitionRefs method
        pass

class BPMNProfile_CatchEvent(BPMNEvent):

    def __init__(self, parallelMultiple: str, BPMNProfile_CatchEvent: "BPMNProfile_AcceptEventAction" = None, BPMNProfile_CatchEvent467: "BPMNProfile_InitialNode" = None, BPMNProfile_CatchEvent469: set["BPMNProfile_DataOutputAssociation"] = None):
        self.parallelMultiple = parallelMultiple
        self.BPMNProfile_CatchEvent = BPMNProfile_CatchEvent
        self.BPMNProfile_CatchEvent467 = BPMNProfile_CatchEvent467
        self.BPMNProfile_CatchEvent469 = BPMNProfile_CatchEvent469 if BPMNProfile_CatchEvent469 is not None else set()
        
    @property
    def parallelMultiple(self) -> str:
        return self.__parallelMultiple

    @parallelMultiple.setter
    def parallelMultiple(self, parallelMultiple: str):
        self.__parallelMultiple = parallelMultiple

    @property
    def BPMNProfile_CatchEvent469(self):
        return self.__BPMNProfile_CatchEvent469

    @BPMNProfile_CatchEvent469.setter
    def BPMNProfile_CatchEvent469(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CatchEvent__BPMNProfile_CatchEvent469", None)
        self.__BPMNProfile_CatchEvent469 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_DataOutputAssociation470"):
                    opp_val = getattr(item, "BPMNProfile_DataOutputAssociation470", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_DataOutputAssociation470", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_DataOutputAssociation470"):
                    opp_val = getattr(item, "BPMNProfile_DataOutputAssociation470", None)
                    
                    setattr(item, "BPMNProfile_DataOutputAssociation470", self)
                    

    @property
    def BPMNProfile_CatchEvent467(self):
        return self.__BPMNProfile_CatchEvent467

    @BPMNProfile_CatchEvent467.setter
    def BPMNProfile_CatchEvent467(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CatchEvent__BPMNProfile_CatchEvent467", None)
        self.__BPMNProfile_CatchEvent467 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_InitialNode"):
                opp_val = getattr(old_value, "BPMNProfile_InitialNode", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_InitialNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_InitialNode"):
                opp_val = getattr(value, "BPMNProfile_InitialNode", None)
                setattr(value, "BPMNProfile_InitialNode", self)

    @property
    def BPMNProfile_CatchEvent(self):
        return self.__BPMNProfile_CatchEvent

    @BPMNProfile_CatchEvent.setter
    def BPMNProfile_CatchEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CatchEvent__BPMNProfile_CatchEvent", None)
        self.__BPMNProfile_CatchEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_AcceptEventAction"):
                opp_val = getattr(old_value, "BPMNProfile_AcceptEventAction", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_AcceptEventAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_AcceptEventAction"):
                opp_val = getattr(value, "BPMNProfile_AcceptEventAction", None)
                setattr(value, "BPMNProfile_AcceptEventAction", self)

    def catchEventeventDefinitionsRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement catchEventeventDefinitionsRefs method
        pass

class CatchEvent:

    pass
class BPMNProfile_StartEvent(CatchEvent):

    def __init__(self, isInterrupting: str):
        self.isInterrupting = isInterrupting
        
    @property
    def isInterrupting(self) -> str:
        return self.__isInterrupting

    @isInterrupting.setter
    def isInterrupting(self, isInterrupting: str):
        self.__isInterrupting = isInterrupting

class BPMNProfile_IntermediateCatchEvent(CatchEvent):

    pass
class BPMNProfile_DataOutputAssociation(DataAssociation):

    def __init__(self, BPMNProfile_DataOutputAssociation470: "BPMNProfile_CatchEvent" = None, BPMNProfile_DataOutputAssociation: "BPMNProfile_BPMNActivity" = None):
        self.BPMNProfile_DataOutputAssociation470 = BPMNProfile_DataOutputAssociation470
        self.BPMNProfile_DataOutputAssociation = BPMNProfile_DataOutputAssociation
        
    @property
    def BPMNProfile_DataOutputAssociation(self):
        return self.__BPMNProfile_DataOutputAssociation

    @BPMNProfile_DataOutputAssociation.setter
    def BPMNProfile_DataOutputAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataOutputAssociation__BPMNProfile_DataOutputAssociation", None)
        self.__BPMNProfile_DataOutputAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNActivity456"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNActivity456", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNActivity456"):
                opp_val = getattr(value, "BPMNProfile_BPMNActivity456", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNActivity456", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_DataOutputAssociation470(self):
        return self.__BPMNProfile_DataOutputAssociation470

    @BPMNProfile_DataOutputAssociation470.setter
    def BPMNProfile_DataOutputAssociation470(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataOutputAssociation__BPMNProfile_DataOutputAssociation470", None)
        self.__BPMNProfile_DataOutputAssociation470 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CatchEvent469"):
                opp_val = getattr(old_value, "BPMNProfile_CatchEvent469", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CatchEvent469"):
                opp_val = getattr(value, "BPMNProfile_CatchEvent469", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_CatchEvent469", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def dataOutputAssociationtarget(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement dataOutputAssociationtarget method
        pass

    def dataOutputAssociationsource(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement dataOutputAssociationsource method
        pass

class BPMNProfile_DataInputAssociation(DataAssociation):

    def __init__(self, BPMNProfile_DataInputAssociation: "BPMNProfile_BPMNActivity" = None, BPMNProfile_DataInputAssociation530: "BPMNProfile_ThrowEvent" = None):
        self.BPMNProfile_DataInputAssociation = BPMNProfile_DataInputAssociation
        self.BPMNProfile_DataInputAssociation530 = BPMNProfile_DataInputAssociation530
        
    @property
    def BPMNProfile_DataInputAssociation(self):
        return self.__BPMNProfile_DataInputAssociation

    @BPMNProfile_DataInputAssociation.setter
    def BPMNProfile_DataInputAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataInputAssociation__BPMNProfile_DataInputAssociation", None)
        self.__BPMNProfile_DataInputAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNActivity454"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNActivity454", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNActivity454"):
                opp_val = getattr(value, "BPMNProfile_BPMNActivity454", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNActivity454", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_DataInputAssociation530(self):
        return self.__BPMNProfile_DataInputAssociation530

    @BPMNProfile_DataInputAssociation530.setter
    def BPMNProfile_DataInputAssociation530(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataInputAssociation__BPMNProfile_DataInputAssociation530", None)
        self.__BPMNProfile_DataInputAssociation530 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ThrowEvent529"):
                opp_val = getattr(old_value, "BPMNProfile_ThrowEvent529", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ThrowEvent529"):
                opp_val = getattr(value, "BPMNProfile_ThrowEvent529", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_ThrowEvent529", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def dataInputAssociationtarget(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement dataInputAssociationtarget method
        pass

    def dataInputAssociationsource(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement dataInputAssociationsource method
        pass

class BPMNProfile_BoundaryEvent(CatchEvent):

    def __init__(self, cancelActivity: str, BPMNProfile_BoundaryEvent: "BPMNProfile_BPMNActivity" = None, BPMNProfile_BoundaryEvent463: "BPMNProfile_BPMNActivity" = None):
        self.cancelActivity = cancelActivity
        self.BPMNProfile_BoundaryEvent = BPMNProfile_BoundaryEvent
        self.BPMNProfile_BoundaryEvent463 = BPMNProfile_BoundaryEvent463
        
    @property
    def cancelActivity(self) -> str:
        return self.__cancelActivity

    @cancelActivity.setter
    def cancelActivity(self, cancelActivity: str):
        self.__cancelActivity = cancelActivity

    @property
    def BPMNProfile_BoundaryEvent463(self):
        return self.__BPMNProfile_BoundaryEvent463

    @BPMNProfile_BoundaryEvent463.setter
    def BPMNProfile_BoundaryEvent463(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BoundaryEvent__BPMNProfile_BoundaryEvent463", None)
        self.__BPMNProfile_BoundaryEvent463 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNActivity464"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNActivity464", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNActivity464", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNActivity464"):
                opp_val = getattr(value, "BPMNProfile_BPMNActivity464", None)
                setattr(value, "BPMNProfile_BPMNActivity464", self)

    @property
    def BPMNProfile_BoundaryEvent(self):
        return self.__BPMNProfile_BoundaryEvent

    @BPMNProfile_BoundaryEvent.setter
    def BPMNProfile_BoundaryEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BoundaryEvent__BPMNProfile_BoundaryEvent", None)
        self.__BPMNProfile_BoundaryEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNActivity452"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNActivity452", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNActivity452"):
                opp_val = getattr(value, "BPMNProfile_BPMNActivity452", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNActivity452", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def boundaryEventattachedToRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement boundaryEventattachedToRef method
        pass

class BPMNProfile_InitialNode:

    pass
class BPMNProfile_AcceptEventAction:

    pass
class BPMNProfile_Event:

    pass
class BPMNProfile_CallEvent:

    pass
class EventDefinition:

    pass
class BPMNProfile_SignalEventDefinition(EventDefinition):

    pass
class BPMNProfile_ErrorEventDefinition(EventDefinition):

    pass
class BPMNProfile_EscalationEventDefinition(EventDefinition):

    pass
class BPMNProfile_ConditionalEventDefinition(EventDefinition):

    def __init__(self, BPMNProfile_ConditionalEventDefinition: "BPMNProfile_ChangeEvent" = None, BPMNProfile_ConditionalEventDefinition542: "BPMNProfile_BPMNExpression" = None):
        self.BPMNProfile_ConditionalEventDefinition = BPMNProfile_ConditionalEventDefinition
        self.BPMNProfile_ConditionalEventDefinition542 = BPMNProfile_ConditionalEventDefinition542
        
    @property
    def BPMNProfile_ConditionalEventDefinition542(self):
        return self.__BPMNProfile_ConditionalEventDefinition542

    @BPMNProfile_ConditionalEventDefinition542.setter
    def BPMNProfile_ConditionalEventDefinition542(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ConditionalEventDefinition__BPMNProfile_ConditionalEventDefinition542", None)
        self.__BPMNProfile_ConditionalEventDefinition542 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNExpression543"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNExpression543", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNExpression543", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNExpression543"):
                opp_val = getattr(value, "BPMNProfile_BPMNExpression543", None)
                setattr(value, "BPMNProfile_BPMNExpression543", self)

    @property
    def BPMNProfile_ConditionalEventDefinition(self):
        return self.__BPMNProfile_ConditionalEventDefinition

    @BPMNProfile_ConditionalEventDefinition.setter
    def BPMNProfile_ConditionalEventDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ConditionalEventDefinition__BPMNProfile_ConditionalEventDefinition", None)
        self.__BPMNProfile_ConditionalEventDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ChangeEvent540"):
                opp_val = getattr(old_value, "BPMNProfile_ChangeEvent540", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ChangeEvent540", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ChangeEvent540"):
                opp_val = getattr(value, "BPMNProfile_ChangeEvent540", None)
                setattr(value, "BPMNProfile_ChangeEvent540", self)

    def conditionalEventDefinitioncondition(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement conditionalEventDefinitioncondition method
        pass

class BPMNProfile_TerminateEventDefinition(EventDefinition):

    pass
class BPMNProfile_MessageEventDefinition(EventDefinition):

    pass
class BPMNProfile_CancelEventDefinition(EventDefinition):

    pass
class BPMNProfile_LinkEventDefinition(EventDefinition):

    pass
class BPMNProfile_TimerEventDefinition(EventDefinition):

    pass
class BPMNProfile_CompensateEventDefinition(EventDefinition):

    def __init__(self, waitForCompletion: str, BPMNProfile_CompensateEventDefinition: "BPMNProfile_BPMNActivity" = None, BPMNProfile_CompensateEventDefinition437: "BPMNProfile_CallEvent" = None):
        self.waitForCompletion = waitForCompletion
        self.BPMNProfile_CompensateEventDefinition = BPMNProfile_CompensateEventDefinition
        self.BPMNProfile_CompensateEventDefinition437 = BPMNProfile_CompensateEventDefinition437
        
    @property
    def waitForCompletion(self) -> str:
        return self.__waitForCompletion

    @waitForCompletion.setter
    def waitForCompletion(self, waitForCompletion: str):
        self.__waitForCompletion = waitForCompletion

    @property
    def BPMNProfile_CompensateEventDefinition437(self):
        return self.__BPMNProfile_CompensateEventDefinition437

    @BPMNProfile_CompensateEventDefinition437.setter
    def BPMNProfile_CompensateEventDefinition437(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CompensateEventDefinition__BPMNProfile_CompensateEventDefinition437", None)
        self.__BPMNProfile_CompensateEventDefinition437 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CallEvent"):
                opp_val = getattr(old_value, "BPMNProfile_CallEvent", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_CallEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CallEvent"):
                opp_val = getattr(value, "BPMNProfile_CallEvent", None)
                setattr(value, "BPMNProfile_CallEvent", self)

    @property
    def BPMNProfile_CompensateEventDefinition(self):
        return self.__BPMNProfile_CompensateEventDefinition

    @BPMNProfile_CompensateEventDefinition.setter
    def BPMNProfile_CompensateEventDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CompensateEventDefinition__BPMNProfile_CompensateEventDefinition", None)
        self.__BPMNProfile_CompensateEventDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNActivity"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNActivity", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNActivity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNActivity"):
                opp_val = getattr(value, "BPMNProfile_BPMNActivity", None)
                setattr(value, "BPMNProfile_BPMNActivity", self)

class BPMNProfile_OpaqueBehavior:

    pass
class GlobalTask:

    pass
class BPMNProfile_GlobalUserTask(GlobalTask):

    def __init__(self, implementation: str, BPMNProfile_GlobalUserTask: set["BPMNProfile_Rendering"] = None):
        self.implementation = implementation
        self.BPMNProfile_GlobalUserTask = BPMNProfile_GlobalUserTask if BPMNProfile_GlobalUserTask is not None else set()
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def BPMNProfile_GlobalUserTask(self):
        return self.__BPMNProfile_GlobalUserTask

    @BPMNProfile_GlobalUserTask.setter
    def BPMNProfile_GlobalUserTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_GlobalUserTask__BPMNProfile_GlobalUserTask", None)
        self.__BPMNProfile_GlobalUserTask = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_Rendering597"):
                    opp_val = getattr(item, "BPMNProfile_Rendering597", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_Rendering597", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_Rendering597"):
                    opp_val = getattr(item, "BPMNProfile_Rendering597", None)
                    
                    setattr(item, "BPMNProfile_Rendering597", self)
                    

    def GlobalUserTaskimplementation(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement GlobalUserTaskimplementation method
        pass

    def GlobalUserTaskrenderings(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement GlobalUserTaskrenderings method
        pass

class BPMNProfile_GlobalManualTask(GlobalTask):

    pass
class BPMNProfile_GlobalScriptTask(GlobalTask):

    def __init__(self, script: str, scriptFormat: str):
        self.script = script
        self.scriptFormat = scriptFormat
        
    @property
    def scriptFormat(self) -> str:
        return self.__scriptFormat

    @scriptFormat.setter
    def scriptFormat(self, scriptFormat: str):
        self.__scriptFormat = scriptFormat

    @property
    def script(self) -> str:
        return self.__script

    @script.setter
    def script(self, script: str):
        self.__script = script

    def GlobalScriptTaskscript(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement GlobalScriptTaskscript method
        pass

    def GlobalScriptTaskscriptFormat(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement GlobalScriptTaskscriptFormat method
        pass

class BPMNProfile_GlobalBusinessRuleTask(GlobalTask):

    def __init__(self, implementation: str):
        self.implementation = implementation
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    def GlobalBusinessRuleTaskimplementation(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement GlobalBusinessRuleTaskimplementation method
        pass

class BPMNExpression:

    pass
class BPMNProfile_ResourceAssignmentExpression(BPMNExpression):

    def __init__(self, BPMNProfile_ResourceAssignmentExpression: "BPMNProfile_ResourceRole" = None, BPMNProfile_ResourceAssignmentExpression412: "BPMNProfile_BPMNExpression" = None):
        self.BPMNProfile_ResourceAssignmentExpression = BPMNProfile_ResourceAssignmentExpression
        self.BPMNProfile_ResourceAssignmentExpression412 = BPMNProfile_ResourceAssignmentExpression412
        
    @property
    def BPMNProfile_ResourceAssignmentExpression412(self):
        return self.__BPMNProfile_ResourceAssignmentExpression412

    @BPMNProfile_ResourceAssignmentExpression412.setter
    def BPMNProfile_ResourceAssignmentExpression412(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceAssignmentExpression__BPMNProfile_ResourceAssignmentExpression412", None)
        self.__BPMNProfile_ResourceAssignmentExpression412 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNExpression413"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNExpression413", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNExpression413", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNExpression413"):
                opp_val = getattr(value, "BPMNProfile_BPMNExpression413", None)
                setattr(value, "BPMNProfile_BPMNExpression413", self)

    @property
    def BPMNProfile_ResourceAssignmentExpression(self):
        return self.__BPMNProfile_ResourceAssignmentExpression

    @BPMNProfile_ResourceAssignmentExpression.setter
    def BPMNProfile_ResourceAssignmentExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceAssignmentExpression__BPMNProfile_ResourceAssignmentExpression", None)
        self.__BPMNProfile_ResourceAssignmentExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ResourceRole405"):
                opp_val = getattr(old_value, "BPMNProfile_ResourceRole405", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ResourceRole405", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ResourceRole405"):
                opp_val = getattr(value, "BPMNProfile_ResourceRole405", None)
                setattr(value, "BPMNProfile_ResourceRole405", self)

    def ResourceAssignmentExpressionexpression(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceAssignmentExpressionexpression method
        pass

class BPMNProfile_FormalExpression(BPMNExpression):

    def __init__(self, BPMNProfile_FormalExpression: "BPMNProfile_CorrelationPropertyRetrievalExpression" = None, BPMNProfile_FormalExpression378: "BPMNProfile_ItemDefinition" = None, BPMNProfile_FormalExpression393: "BPMNProfile_CorrelationPropertyBinding" = None, BPMNProfile_FormalExpression491: "BPMNProfile_DataAssociation" = None, BPMNProfile_FormalExpression621: "BPMNProfile_ComplexBehaviorDefinition" = None):
        self.BPMNProfile_FormalExpression = BPMNProfile_FormalExpression
        self.BPMNProfile_FormalExpression378 = BPMNProfile_FormalExpression378
        self.BPMNProfile_FormalExpression393 = BPMNProfile_FormalExpression393
        self.BPMNProfile_FormalExpression491 = BPMNProfile_FormalExpression491
        self.BPMNProfile_FormalExpression621 = BPMNProfile_FormalExpression621
        
    @property
    def BPMNProfile_FormalExpression(self):
        return self.__BPMNProfile_FormalExpression

    @BPMNProfile_FormalExpression.setter
    def BPMNProfile_FormalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_FormalExpression__BPMNProfile_FormalExpression", None)
        self.__BPMNProfile_FormalExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CorrelationPropertyRetrievalExpression376"):
                opp_val = getattr(old_value, "BPMNProfile_CorrelationPropertyRetrievalExpression376", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_CorrelationPropertyRetrievalExpression376", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CorrelationPropertyRetrievalExpression376"):
                opp_val = getattr(value, "BPMNProfile_CorrelationPropertyRetrievalExpression376", None)
                setattr(value, "BPMNProfile_CorrelationPropertyRetrievalExpression376", self)

    @property
    def BPMNProfile_FormalExpression491(self):
        return self.__BPMNProfile_FormalExpression491

    @BPMNProfile_FormalExpression491.setter
    def BPMNProfile_FormalExpression491(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_FormalExpression__BPMNProfile_FormalExpression491", None)
        self.__BPMNProfile_FormalExpression491 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_DataAssociation490"):
                opp_val = getattr(old_value, "BPMNProfile_DataAssociation490", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_DataAssociation490", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_DataAssociation490"):
                opp_val = getattr(value, "BPMNProfile_DataAssociation490", None)
                setattr(value, "BPMNProfile_DataAssociation490", self)

    @property
    def BPMNProfile_FormalExpression621(self):
        return self.__BPMNProfile_FormalExpression621

    @BPMNProfile_FormalExpression621.setter
    def BPMNProfile_FormalExpression621(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_FormalExpression__BPMNProfile_FormalExpression621", None)
        self.__BPMNProfile_FormalExpression621 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ComplexBehaviorDefinition"):
                opp_val = getattr(old_value, "BPMNProfile_ComplexBehaviorDefinition", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ComplexBehaviorDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ComplexBehaviorDefinition"):
                opp_val = getattr(value, "BPMNProfile_ComplexBehaviorDefinition", None)
                setattr(value, "BPMNProfile_ComplexBehaviorDefinition", self)

    @property
    def BPMNProfile_FormalExpression393(self):
        return self.__BPMNProfile_FormalExpression393

    @BPMNProfile_FormalExpression393.setter
    def BPMNProfile_FormalExpression393(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_FormalExpression__BPMNProfile_FormalExpression393", None)
        self.__BPMNProfile_FormalExpression393 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CorrelationPropertyBinding392"):
                opp_val = getattr(old_value, "BPMNProfile_CorrelationPropertyBinding392", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_CorrelationPropertyBinding392", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CorrelationPropertyBinding392"):
                opp_val = getattr(value, "BPMNProfile_CorrelationPropertyBinding392", None)
                setattr(value, "BPMNProfile_CorrelationPropertyBinding392", self)

    @property
    def BPMNProfile_FormalExpression378(self):
        return self.__BPMNProfile_FormalExpression378

    @BPMNProfile_FormalExpression378.setter
    def BPMNProfile_FormalExpression378(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_FormalExpression__BPMNProfile_FormalExpression378", None)
        self.__BPMNProfile_FormalExpression378 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ItemDefinition379"):
                opp_val = getattr(old_value, "BPMNProfile_ItemDefinition379", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ItemDefinition379", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ItemDefinition379"):
                opp_val = getattr(value, "BPMNProfile_ItemDefinition379", None)
                setattr(value, "BPMNProfile_ItemDefinition379", self)

    def FormalExpressionevaluatesToTypeRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement FormalExpressionevaluatesToTypeRef method
        pass

class BPMNProfile_DataStoreNode:

    pass
class InteractionNode:

    pass
class BPMNProfile_InformationFlow:

    pass
class BPMNProfile_MultiplicityElement:

    pass
class BPMNProfile_InteractionNode(ABC):

    pass
class BPMNProfile_InstanceSpecification:

    pass
class BPMNProfile_ConversationNode(InteractionNode):

    def __init__(self, BPMNProfile_ConversationNode: "BPMNProfile_BPMNCollaboration" = None, BPMNProfile_ConversationNode345: "BPMNProfile_InformationFlow" = None, BPMNProfile_ConversationNode348: set["BPMNProfile_MessageFlow"] = None, BPMNProfile_ConversationNode351: set["BPMNProfile_CorrelationKey"] = None, BPMNProfile_ConversationNode354: set["BPMNProfile_Participant"] = None, BPMNProfile_ConversationNode601: "BPMNProfile_SubConversation" = None):
        self.BPMNProfile_ConversationNode = BPMNProfile_ConversationNode
        self.BPMNProfile_ConversationNode345 = BPMNProfile_ConversationNode345
        self.BPMNProfile_ConversationNode348 = BPMNProfile_ConversationNode348 if BPMNProfile_ConversationNode348 is not None else set()
        self.BPMNProfile_ConversationNode351 = BPMNProfile_ConversationNode351 if BPMNProfile_ConversationNode351 is not None else set()
        self.BPMNProfile_ConversationNode354 = BPMNProfile_ConversationNode354 if BPMNProfile_ConversationNode354 is not None else set()
        self.BPMNProfile_ConversationNode601 = BPMNProfile_ConversationNode601
        
    @property
    def BPMNProfile_ConversationNode348(self):
        return self.__BPMNProfile_ConversationNode348

    @BPMNProfile_ConversationNode348.setter
    def BPMNProfile_ConversationNode348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ConversationNode__BPMNProfile_ConversationNode348", None)
        self.__BPMNProfile_ConversationNode348 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_MessageFlow349"):
                    opp_val = getattr(item, "BPMNProfile_MessageFlow349", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_MessageFlow349", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_MessageFlow349"):
                    opp_val = getattr(item, "BPMNProfile_MessageFlow349", None)
                    
                    setattr(item, "BPMNProfile_MessageFlow349", self)
                    

    @property
    def BPMNProfile_ConversationNode601(self):
        return self.__BPMNProfile_ConversationNode601

    @BPMNProfile_ConversationNode601.setter
    def BPMNProfile_ConversationNode601(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ConversationNode__BPMNProfile_ConversationNode601", None)
        self.__BPMNProfile_ConversationNode601 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_SubConversation"):
                opp_val = getattr(old_value, "BPMNProfile_SubConversation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_SubConversation"):
                opp_val = getattr(value, "BPMNProfile_SubConversation", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_SubConversation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_ConversationNode(self):
        return self.__BPMNProfile_ConversationNode

    @BPMNProfile_ConversationNode.setter
    def BPMNProfile_ConversationNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ConversationNode__BPMNProfile_ConversationNode", None)
        self.__BPMNProfile_ConversationNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNCollaboration274"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNCollaboration274", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNCollaboration274"):
                opp_val = getattr(value, "BPMNProfile_BPMNCollaboration274", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNCollaboration274", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_ConversationNode351(self):
        return self.__BPMNProfile_ConversationNode351

    @BPMNProfile_ConversationNode351.setter
    def BPMNProfile_ConversationNode351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ConversationNode__BPMNProfile_ConversationNode351", None)
        self.__BPMNProfile_ConversationNode351 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_CorrelationKey352"):
                    opp_val = getattr(item, "BPMNProfile_CorrelationKey352", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_CorrelationKey352", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_CorrelationKey352"):
                    opp_val = getattr(item, "BPMNProfile_CorrelationKey352", None)
                    
                    setattr(item, "BPMNProfile_CorrelationKey352", self)
                    

    @property
    def BPMNProfile_ConversationNode354(self):
        return self.__BPMNProfile_ConversationNode354

    @BPMNProfile_ConversationNode354.setter
    def BPMNProfile_ConversationNode354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ConversationNode__BPMNProfile_ConversationNode354", None)
        self.__BPMNProfile_ConversationNode354 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_Participant355"):
                    opp_val = getattr(item, "BPMNProfile_Participant355", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_Participant355", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_Participant355"):
                    opp_val = getattr(item, "BPMNProfile_Participant355", None)
                    
                    setattr(item, "BPMNProfile_Participant355", self)
                    

    @property
    def BPMNProfile_ConversationNode345(self):
        return self.__BPMNProfile_ConversationNode345

    @BPMNProfile_ConversationNode345.setter
    def BPMNProfile_ConversationNode345(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ConversationNode__BPMNProfile_ConversationNode345", None)
        self.__BPMNProfile_ConversationNode345 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_InformationFlow346"):
                opp_val = getattr(old_value, "BPMNProfile_InformationFlow346", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_InformationFlow346", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_InformationFlow346"):
                opp_val = getattr(value, "BPMNProfile_InformationFlow346", None)
                setattr(value, "BPMNProfile_InformationFlow346", self)

    def ConversationNodeparticipantRefs(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ConversationNodeparticipantRefs method
        pass

class BPMNProfile_Collaboration:

    pass
class ItemDefinition:

    pass
class BPMNProfile_Escalation(ItemDefinition):

    def __init__(self, escalationCode: str, BPMNProfile_Escalation: "BPMNProfile_EscalationEventDefinition" = None):
        self.escalationCode = escalationCode
        self.BPMNProfile_Escalation = BPMNProfile_Escalation
        
    @property
    def escalationCode(self) -> str:
        return self.__escalationCode

    @escalationCode.setter
    def escalationCode(self, escalationCode: str):
        self.__escalationCode = escalationCode

    @property
    def BPMNProfile_Escalation(self):
        return self.__BPMNProfile_Escalation

    @BPMNProfile_Escalation.setter
    def BPMNProfile_Escalation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Escalation__BPMNProfile_Escalation", None)
        self.__BPMNProfile_Escalation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_EscalationEventDefinition"):
                opp_val = getattr(old_value, "BPMNProfile_EscalationEventDefinition", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_EscalationEventDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_EscalationEventDefinition"):
                opp_val = getattr(value, "BPMNProfile_EscalationEventDefinition", None)
                setattr(value, "BPMNProfile_EscalationEventDefinition", self)

    def EscalationstructureRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement EscalationstructureRef method
        pass

class BPMNProfile_BPMNSignal(ItemDefinition):

    def __init__(self, BPMNProfile_BPMNSignal: "BPMNProfile_SignalEventDefinition" = None):
        self.BPMNProfile_BPMNSignal = BPMNProfile_BPMNSignal
        
    @property
    def BPMNProfile_BPMNSignal(self):
        return self.__BPMNProfile_BPMNSignal

    @BPMNProfile_BPMNSignal.setter
    def BPMNProfile_BPMNSignal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNSignal__BPMNProfile_BPMNSignal", None)
        self.__BPMNProfile_BPMNSignal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_SignalEventDefinition"):
                opp_val = getattr(old_value, "BPMNProfile_SignalEventDefinition", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_SignalEventDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_SignalEventDefinition"):
                opp_val = getattr(value, "BPMNProfile_SignalEventDefinition", None)
                setattr(value, "BPMNProfile_SignalEventDefinition", self)

    def BPMNSignalstructureRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement BPMNSignalstructureRef method
        pass

class BPMNProfile_Resource(ItemDefinition):

    def __init__(self, BPMNProfile_Resource: "BPMNProfile_ResourceRole" = None, BPMNProfile_Resource415: set["BPMNProfile_ResourceParameter"] = None):
        self.BPMNProfile_Resource = BPMNProfile_Resource
        self.BPMNProfile_Resource415 = BPMNProfile_Resource415 if BPMNProfile_Resource415 is not None else set()
        
    @property
    def BPMNProfile_Resource415(self):
        return self.__BPMNProfile_Resource415

    @BPMNProfile_Resource415.setter
    def BPMNProfile_Resource415(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Resource__BPMNProfile_Resource415", None)
        self.__BPMNProfile_Resource415 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_ResourceParameter"):
                    opp_val = getattr(item, "BPMNProfile_ResourceParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_ResourceParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_ResourceParameter"):
                    opp_val = getattr(item, "BPMNProfile_ResourceParameter", None)
                    
                    setattr(item, "BPMNProfile_ResourceParameter", self)
                    

    @property
    def BPMNProfile_Resource(self):
        return self.__BPMNProfile_Resource

    @BPMNProfile_Resource.setter
    def BPMNProfile_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Resource__BPMNProfile_Resource", None)
        self.__BPMNProfile_Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ResourceRole407"):
                opp_val = getattr(old_value, "BPMNProfile_ResourceRole407", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ResourceRole407", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ResourceRole407"):
                opp_val = getattr(value, "BPMNProfile_ResourceRole407", None)
                setattr(value, "BPMNProfile_ResourceRole407", self)

    def ResourceresourceParameters(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ResourceresourceParameters method
        pass

class BPMNProfile_Error(ItemDefinition):

    def __init__(self, errorCode: str, BPMNProfile_Error: "BPMNProfile_BPMNOperation" = None, BPMNProfile_Error552: "BPMNProfile_ErrorEventDefinition" = None):
        self.errorCode = errorCode
        self.BPMNProfile_Error = BPMNProfile_Error
        self.BPMNProfile_Error552 = BPMNProfile_Error552
        
    @property
    def errorCode(self) -> str:
        return self.__errorCode

    @errorCode.setter
    def errorCode(self, errorCode: str):
        self.__errorCode = errorCode

    @property
    def BPMNProfile_Error552(self):
        return self.__BPMNProfile_Error552

    @BPMNProfile_Error552.setter
    def BPMNProfile_Error552(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Error__BPMNProfile_Error552", None)
        self.__BPMNProfile_Error552 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ErrorEventDefinition"):
                opp_val = getattr(old_value, "BPMNProfile_ErrorEventDefinition", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ErrorEventDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ErrorEventDefinition"):
                opp_val = getattr(value, "BPMNProfile_ErrorEventDefinition", None)
                setattr(value, "BPMNProfile_ErrorEventDefinition", self)

    @property
    def BPMNProfile_Error(self):
        return self.__BPMNProfile_Error

    @BPMNProfile_Error.setter
    def BPMNProfile_Error(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Error__BPMNProfile_Error", None)
        self.__BPMNProfile_Error = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNOperation248"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNOperation248", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNOperation248"):
                opp_val = getattr(value, "BPMNProfile_BPMNOperation248", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNOperation248", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMNProfile_BPMNMessage(ItemDefinition):

    def __init__(self, BPMNProfile_BPMNMessage: "BPMNProfile_BPMNOperation" = None, BPMNProfile_BPMNMessage246: "BPMNProfile_BPMNOperation" = None, BPMNProfile_BPMNMessage250: "BPMNProfile_ItemDefinition" = None, BPMNProfile_BPMNMessage374: "BPMNProfile_CorrelationPropertyRetrievalExpression" = None, BPMNProfile_BPMNMessage343: "BPMNProfile_MessageFlow" = None, BPMNProfile_BPMNMessage532: "BPMNProfile_MessageEventDefinition" = None, BPMNProfile_BPMNMessage632: "BPMNProfile_SendTask" = None, BPMNProfile_BPMNMessage644: "BPMNProfile_ReceiveTask" = None):
        self.BPMNProfile_BPMNMessage = BPMNProfile_BPMNMessage
        self.BPMNProfile_BPMNMessage246 = BPMNProfile_BPMNMessage246
        self.BPMNProfile_BPMNMessage250 = BPMNProfile_BPMNMessage250
        self.BPMNProfile_BPMNMessage374 = BPMNProfile_BPMNMessage374
        self.BPMNProfile_BPMNMessage343 = BPMNProfile_BPMNMessage343
        self.BPMNProfile_BPMNMessage532 = BPMNProfile_BPMNMessage532
        self.BPMNProfile_BPMNMessage632 = BPMNProfile_BPMNMessage632
        self.BPMNProfile_BPMNMessage644 = BPMNProfile_BPMNMessage644
        
    @property
    def BPMNProfile_BPMNMessage(self):
        return self.__BPMNProfile_BPMNMessage

    @BPMNProfile_BPMNMessage.setter
    def BPMNProfile_BPMNMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNMessage__BPMNProfile_BPMNMessage", None)
        self.__BPMNProfile_BPMNMessage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNOperation243"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNOperation243", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNOperation243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNOperation243"):
                opp_val = getattr(value, "BPMNProfile_BPMNOperation243", None)
                setattr(value, "BPMNProfile_BPMNOperation243", self)

    @property
    def BPMNProfile_BPMNMessage343(self):
        return self.__BPMNProfile_BPMNMessage343

    @BPMNProfile_BPMNMessage343.setter
    def BPMNProfile_BPMNMessage343(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNMessage__BPMNProfile_BPMNMessage343", None)
        self.__BPMNProfile_BPMNMessage343 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_MessageFlow342"):
                opp_val = getattr(old_value, "BPMNProfile_MessageFlow342", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_MessageFlow342", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_MessageFlow342"):
                opp_val = getattr(value, "BPMNProfile_MessageFlow342", None)
                setattr(value, "BPMNProfile_MessageFlow342", self)

    @property
    def BPMNProfile_BPMNMessage374(self):
        return self.__BPMNProfile_BPMNMessage374

    @BPMNProfile_BPMNMessage374.setter
    def BPMNProfile_BPMNMessage374(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNMessage__BPMNProfile_BPMNMessage374", None)
        self.__BPMNProfile_BPMNMessage374 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CorrelationPropertyRetrievalExpression373"):
                opp_val = getattr(old_value, "BPMNProfile_CorrelationPropertyRetrievalExpression373", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_CorrelationPropertyRetrievalExpression373", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CorrelationPropertyRetrievalExpression373"):
                opp_val = getattr(value, "BPMNProfile_CorrelationPropertyRetrievalExpression373", None)
                setattr(value, "BPMNProfile_CorrelationPropertyRetrievalExpression373", self)

    @property
    def BPMNProfile_BPMNMessage532(self):
        return self.__BPMNProfile_BPMNMessage532

    @BPMNProfile_BPMNMessage532.setter
    def BPMNProfile_BPMNMessage532(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNMessage__BPMNProfile_BPMNMessage532", None)
        self.__BPMNProfile_BPMNMessage532 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_MessageEventDefinition"):
                opp_val = getattr(old_value, "BPMNProfile_MessageEventDefinition", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_MessageEventDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_MessageEventDefinition"):
                opp_val = getattr(value, "BPMNProfile_MessageEventDefinition", None)
                setattr(value, "BPMNProfile_MessageEventDefinition", self)

    @property
    def BPMNProfile_BPMNMessage250(self):
        return self.__BPMNProfile_BPMNMessage250

    @BPMNProfile_BPMNMessage250.setter
    def BPMNProfile_BPMNMessage250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNMessage__BPMNProfile_BPMNMessage250", None)
        self.__BPMNProfile_BPMNMessage250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ItemDefinition251"):
                opp_val = getattr(old_value, "BPMNProfile_ItemDefinition251", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ItemDefinition251", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ItemDefinition251"):
                opp_val = getattr(value, "BPMNProfile_ItemDefinition251", None)
                setattr(value, "BPMNProfile_ItemDefinition251", self)

    @property
    def BPMNProfile_BPMNMessage246(self):
        return self.__BPMNProfile_BPMNMessage246

    @BPMNProfile_BPMNMessage246.setter
    def BPMNProfile_BPMNMessage246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNMessage__BPMNProfile_BPMNMessage246", None)
        self.__BPMNProfile_BPMNMessage246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNOperation245"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNOperation245", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNOperation245", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNOperation245"):
                opp_val = getattr(value, "BPMNProfile_BPMNOperation245", None)
                setattr(value, "BPMNProfile_BPMNOperation245", self)

    @property
    def BPMNProfile_BPMNMessage644(self):
        return self.__BPMNProfile_BPMNMessage644

    @BPMNProfile_BPMNMessage644.setter
    def BPMNProfile_BPMNMessage644(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNMessage__BPMNProfile_BPMNMessage644", None)
        self.__BPMNProfile_BPMNMessage644 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ReceiveTask"):
                opp_val = getattr(old_value, "BPMNProfile_ReceiveTask", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ReceiveTask", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ReceiveTask"):
                opp_val = getattr(value, "BPMNProfile_ReceiveTask", None)
                setattr(value, "BPMNProfile_ReceiveTask", self)

    @property
    def BPMNProfile_BPMNMessage632(self):
        return self.__BPMNProfile_BPMNMessage632

    @BPMNProfile_BPMNMessage632.setter
    def BPMNProfile_BPMNMessage632(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNMessage__BPMNProfile_BPMNMessage632", None)
        self.__BPMNProfile_BPMNMessage632 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_SendTask"):
                opp_val = getattr(old_value, "BPMNProfile_SendTask", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_SendTask", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_SendTask"):
                opp_val = getattr(value, "BPMNProfile_SendTask", None)
                setattr(value, "BPMNProfile_SendTask", self)

    def MessageitemRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MessageitemRef method
        pass

class BPMNProfile_Interface:

    pass
class BPMNProfile_Operation:

    pass
class BPMNProfile_OutputPin:

    pass
class BPMNProfile_ParameterSet:

    pass
class BPMNProfile_TypedElement:

    pass
class BPMNProfile_State:

    pass
class BPMNProfile_ActivityParameterNode:

    pass
class BPMNProfile_Parameter:

    pass
class BPMNProfile_InputPin:

    pass
class ItemAwareElement:

    pass
class BPMNProfile_Action:

    pass
class BPMNProfile_Behavior:

    pass
class RootElement:

    pass
class BPMNProfile_Category(RootElement):

    pass
class BPMNProfile_EventDefinition(RootElement):

    pass
class BPMNProfile_PartnerRole(RootElement):

    def __init__(self, PartnerRole: "BPMNProfile_Participant" = None, BPMNProfile_PartnerRole: "BPMNProfile_Class" = None, partnerRoleRef: set["BPMNProfile_Participant"] = None):
        self.PartnerRole = PartnerRole
        self.BPMNProfile_PartnerRole = BPMNProfile_PartnerRole
        self.partnerRoleRef = partnerRoleRef if partnerRoleRef is not None else set()
        
    @property
    def partnerRoleRef(self):
        return self.__partnerRoleRef

    @partnerRoleRef.setter
    def partnerRoleRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_PartnerRole__partnerRoleRef", None)
        self.__partnerRoleRef = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Participant323"):
                    opp_val = getattr(item, "Participant323", None)
                    
                    if opp_val == self:
                        setattr(item, "Participant323", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Participant323"):
                    opp_val = getattr(item, "Participant323", None)
                    
                    setattr(item, "Participant323", self)
                    

    @property
    def PartnerRole(self):
        return self.__PartnerRole

    @PartnerRole.setter
    def PartnerRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_PartnerRole__PartnerRole", None)
        self.__PartnerRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "participantRef298"):
                opp_val = getattr(old_value, "participantRef298", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "participantRef298"):
                opp_val = getattr(value, "participantRef298", None)
                if opp_val is None:
                    setattr(value, "participantRef298", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_PartnerRole(self):
        return self.__BPMNProfile_PartnerRole

    @BPMNProfile_PartnerRole.setter
    def BPMNProfile_PartnerRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_PartnerRole__BPMNProfile_PartnerRole", None)
        self.__BPMNProfile_PartnerRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Class321"):
                opp_val = getattr(old_value, "BPMNProfile_Class321", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Class321", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Class321"):
                opp_val = getattr(value, "BPMNProfile_Class321", None)
                setattr(value, "BPMNProfile_Class321", self)

    def PartnerRoleparticipantRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement PartnerRoleparticipantRef method
        pass

class BPMNProfile_PartnerEntity(RootElement):

    def __init__(self, BPMNProfile_PartnerEntity: "BPMNProfile_InstanceSpecification" = None, partnerEntityRef: set["BPMNProfile_Participant"] = None, PartnerEntity: "BPMNProfile_Participant" = None):
        self.BPMNProfile_PartnerEntity = BPMNProfile_PartnerEntity
        self.partnerEntityRef = partnerEntityRef if partnerEntityRef is not None else set()
        self.PartnerEntity = PartnerEntity
        
    @property
    def PartnerEntity(self):
        return self.__PartnerEntity

    @PartnerEntity.setter
    def PartnerEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_PartnerEntity__PartnerEntity", None)
        self.__PartnerEntity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "participantRef"):
                opp_val = getattr(old_value, "participantRef", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "participantRef"):
                opp_val = getattr(value, "participantRef", None)
                if opp_val is None:
                    setattr(value, "participantRef", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_PartnerEntity(self):
        return self.__BPMNProfile_PartnerEntity

    @BPMNProfile_PartnerEntity.setter
    def BPMNProfile_PartnerEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_PartnerEntity__BPMNProfile_PartnerEntity", None)
        self.__BPMNProfile_PartnerEntity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_InstanceSpecification"):
                opp_val = getattr(old_value, "BPMNProfile_InstanceSpecification", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_InstanceSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_InstanceSpecification"):
                opp_val = getattr(value, "BPMNProfile_InstanceSpecification", None)
                setattr(value, "BPMNProfile_InstanceSpecification", self)

    @property
    def partnerEntityRef(self):
        return self.__partnerEntityRef

    @partnerEntityRef.setter
    def partnerEntityRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_PartnerEntity__partnerEntityRef", None)
        self.__partnerEntityRef = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Participant"):
                    opp_val = getattr(item, "Participant", None)
                    
                    if opp_val == self:
                        setattr(item, "Participant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Participant"):
                    opp_val = getattr(item, "Participant", None)
                    
                    setattr(item, "Participant", self)
                    

    def PartnerEntityparticipantRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement PartnerEntityparticipantRef method
        pass

class BPMNProfile_DataStore(RootElement):

    def __init__(self, capacity: str, isUnlimited: str, BPMNProfile_DataStore585: "BPMNProfile_DataStoreReference" = None, BPMNProfile_DataStore: "BPMNProfile_Class" = None, BPMNProfile_DataStore582: "BPMNProfile_ItemDefinition" = None):
        self.capacity = capacity
        self.isUnlimited = isUnlimited
        self.BPMNProfile_DataStore585 = BPMNProfile_DataStore585
        self.BPMNProfile_DataStore = BPMNProfile_DataStore
        self.BPMNProfile_DataStore582 = BPMNProfile_DataStore582
        
    @property
    def isUnlimited(self) -> str:
        return self.__isUnlimited

    @isUnlimited.setter
    def isUnlimited(self, isUnlimited: str):
        self.__isUnlimited = isUnlimited

    @property
    def capacity(self) -> str:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: str):
        self.__capacity = capacity

    @property
    def BPMNProfile_DataStore(self):
        return self.__BPMNProfile_DataStore

    @BPMNProfile_DataStore.setter
    def BPMNProfile_DataStore(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataStore__BPMNProfile_DataStore", None)
        self.__BPMNProfile_DataStore = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Class580"):
                opp_val = getattr(old_value, "BPMNProfile_Class580", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Class580", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Class580"):
                opp_val = getattr(value, "BPMNProfile_Class580", None)
                setattr(value, "BPMNProfile_Class580", self)

    @property
    def BPMNProfile_DataStore582(self):
        return self.__BPMNProfile_DataStore582

    @BPMNProfile_DataStore582.setter
    def BPMNProfile_DataStore582(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataStore__BPMNProfile_DataStore582", None)
        self.__BPMNProfile_DataStore582 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ItemDefinition583"):
                opp_val = getattr(old_value, "BPMNProfile_ItemDefinition583", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ItemDefinition583", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ItemDefinition583"):
                opp_val = getattr(value, "BPMNProfile_ItemDefinition583", None)
                setattr(value, "BPMNProfile_ItemDefinition583", self)

    @property
    def BPMNProfile_DataStore585(self):
        return self.__BPMNProfile_DataStore585

    @BPMNProfile_DataStore585.setter
    def BPMNProfile_DataStore585(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataStore__BPMNProfile_DataStore585", None)
        self.__BPMNProfile_DataStore585 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_DataStoreReference"):
                opp_val = getattr(old_value, "BPMNProfile_DataStoreReference", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_DataStoreReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_DataStoreReference"):
                opp_val = getattr(value, "BPMNProfile_DataStoreReference", None)
                setattr(value, "BPMNProfile_DataStoreReference", self)

class BPMNProfile_ItemDefinition(RootElement):

    def __init__(self, itemKind: str, isCollection: str, BPMNProfile_ItemDefinition: "BPMNProfile_ItemAwareElement" = None, BPMNProfile_ItemDefinition187: "BPMNProfile_Class" = None, BPMNProfile_ItemDefinition190: "BPMNProfile_Element" = None, BPMNProfile_ItemDefinition193: "BPMNProfile_Import" = None, BPMNProfile_ItemDefinition251: "BPMNProfile_BPMNMessage" = None, BPMNProfile_ItemDefinition366: "BPMNProfile_CorrelationProperty" = None, BPMNProfile_ItemDefinition379: "BPMNProfile_FormalExpression" = None, BPMNProfile_ItemDefinition421: "BPMNProfile_ResourceParameter" = None, BPMNProfile_ItemDefinition583: "BPMNProfile_DataStore" = None):
        self.itemKind = itemKind
        self.isCollection = isCollection
        self.BPMNProfile_ItemDefinition = BPMNProfile_ItemDefinition
        self.BPMNProfile_ItemDefinition187 = BPMNProfile_ItemDefinition187
        self.BPMNProfile_ItemDefinition190 = BPMNProfile_ItemDefinition190
        self.BPMNProfile_ItemDefinition193 = BPMNProfile_ItemDefinition193
        self.BPMNProfile_ItemDefinition251 = BPMNProfile_ItemDefinition251
        self.BPMNProfile_ItemDefinition366 = BPMNProfile_ItemDefinition366
        self.BPMNProfile_ItemDefinition379 = BPMNProfile_ItemDefinition379
        self.BPMNProfile_ItemDefinition421 = BPMNProfile_ItemDefinition421
        self.BPMNProfile_ItemDefinition583 = BPMNProfile_ItemDefinition583
        
    @property
    def isCollection(self) -> str:
        return self.__isCollection

    @isCollection.setter
    def isCollection(self, isCollection: str):
        self.__isCollection = isCollection

    @property
    def itemKind(self) -> str:
        return self.__itemKind

    @itemKind.setter
    def itemKind(self, itemKind: str):
        self.__itemKind = itemKind

    @property
    def BPMNProfile_ItemDefinition421(self):
        return self.__BPMNProfile_ItemDefinition421

    @BPMNProfile_ItemDefinition421.setter
    def BPMNProfile_ItemDefinition421(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemDefinition__BPMNProfile_ItemDefinition421", None)
        self.__BPMNProfile_ItemDefinition421 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ResourceParameter420"):
                opp_val = getattr(old_value, "BPMNProfile_ResourceParameter420", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ResourceParameter420", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ResourceParameter420"):
                opp_val = getattr(value, "BPMNProfile_ResourceParameter420", None)
                setattr(value, "BPMNProfile_ResourceParameter420", self)

    @property
    def BPMNProfile_ItemDefinition(self):
        return self.__BPMNProfile_ItemDefinition

    @BPMNProfile_ItemDefinition.setter
    def BPMNProfile_ItemDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemDefinition__BPMNProfile_ItemDefinition", None)
        self.__BPMNProfile_ItemDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ItemAwareElement183"):
                opp_val = getattr(old_value, "BPMNProfile_ItemAwareElement183", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ItemAwareElement183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ItemAwareElement183"):
                opp_val = getattr(value, "BPMNProfile_ItemAwareElement183", None)
                setattr(value, "BPMNProfile_ItemAwareElement183", self)

    @property
    def BPMNProfile_ItemDefinition190(self):
        return self.__BPMNProfile_ItemDefinition190

    @BPMNProfile_ItemDefinition190.setter
    def BPMNProfile_ItemDefinition190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemDefinition__BPMNProfile_ItemDefinition190", None)
        self.__BPMNProfile_ItemDefinition190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Element191"):
                opp_val = getattr(old_value, "BPMNProfile_Element191", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Element191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Element191"):
                opp_val = getattr(value, "BPMNProfile_Element191", None)
                setattr(value, "BPMNProfile_Element191", self)

    @property
    def BPMNProfile_ItemDefinition251(self):
        return self.__BPMNProfile_ItemDefinition251

    @BPMNProfile_ItemDefinition251.setter
    def BPMNProfile_ItemDefinition251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemDefinition__BPMNProfile_ItemDefinition251", None)
        self.__BPMNProfile_ItemDefinition251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNMessage250"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNMessage250", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNMessage250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNMessage250"):
                opp_val = getattr(value, "BPMNProfile_BPMNMessage250", None)
                setattr(value, "BPMNProfile_BPMNMessage250", self)

    @property
    def BPMNProfile_ItemDefinition379(self):
        return self.__BPMNProfile_ItemDefinition379

    @BPMNProfile_ItemDefinition379.setter
    def BPMNProfile_ItemDefinition379(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemDefinition__BPMNProfile_ItemDefinition379", None)
        self.__BPMNProfile_ItemDefinition379 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_FormalExpression378"):
                opp_val = getattr(old_value, "BPMNProfile_FormalExpression378", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_FormalExpression378", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_FormalExpression378"):
                opp_val = getattr(value, "BPMNProfile_FormalExpression378", None)
                setattr(value, "BPMNProfile_FormalExpression378", self)

    @property
    def BPMNProfile_ItemDefinition187(self):
        return self.__BPMNProfile_ItemDefinition187

    @BPMNProfile_ItemDefinition187.setter
    def BPMNProfile_ItemDefinition187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemDefinition__BPMNProfile_ItemDefinition187", None)
        self.__BPMNProfile_ItemDefinition187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Class188"):
                opp_val = getattr(old_value, "BPMNProfile_Class188", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Class188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Class188"):
                opp_val = getattr(value, "BPMNProfile_Class188", None)
                setattr(value, "BPMNProfile_Class188", self)

    @property
    def BPMNProfile_ItemDefinition193(self):
        return self.__BPMNProfile_ItemDefinition193

    @BPMNProfile_ItemDefinition193.setter
    def BPMNProfile_ItemDefinition193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemDefinition__BPMNProfile_ItemDefinition193", None)
        self.__BPMNProfile_ItemDefinition193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Import194"):
                opp_val = getattr(old_value, "BPMNProfile_Import194", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Import194", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Import194"):
                opp_val = getattr(value, "BPMNProfile_Import194", None)
                setattr(value, "BPMNProfile_Import194", self)

    @property
    def BPMNProfile_ItemDefinition366(self):
        return self.__BPMNProfile_ItemDefinition366

    @BPMNProfile_ItemDefinition366.setter
    def BPMNProfile_ItemDefinition366(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemDefinition__BPMNProfile_ItemDefinition366", None)
        self.__BPMNProfile_ItemDefinition366 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CorrelationProperty365"):
                opp_val = getattr(old_value, "BPMNProfile_CorrelationProperty365", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_CorrelationProperty365", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CorrelationProperty365"):
                opp_val = getattr(value, "BPMNProfile_CorrelationProperty365", None)
                setattr(value, "BPMNProfile_CorrelationProperty365", self)

    @property
    def BPMNProfile_ItemDefinition583(self):
        return self.__BPMNProfile_ItemDefinition583

    @BPMNProfile_ItemDefinition583.setter
    def BPMNProfile_ItemDefinition583(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemDefinition__BPMNProfile_ItemDefinition583", None)
        self.__BPMNProfile_ItemDefinition583 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_DataStore582"):
                opp_val = getattr(old_value, "BPMNProfile_DataStore582", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_DataStore582", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_DataStore582"):
                opp_val = getattr(value, "BPMNProfile_DataStore582", None)
                setattr(value, "BPMNProfile_DataStore582", self)

    def ItemDefinitionstructureRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ItemDefinitionstructureRef method
        pass

class BPMNProfile_BPMNInterface(RootElement):

    def __init__(self, BPMNProfile_BPMNInterface: "BPMNProfile_CallableElement" = None, BPMNProfile_BPMNInterface228: "BPMNProfile_Interface" = None, BPMNProfile_BPMNInterface230: "BPMNProfile_Element" = None, BPMNProfile_BPMNInterface233: set["BPMNProfile_BPMNOperation"] = None, BPMNProfile_BPMNInterface235: set["BPMNProfile_CallableElement"] = None, BPMNProfile_BPMNInterface301: "BPMNProfile_Participant" = None):
        self.BPMNProfile_BPMNInterface = BPMNProfile_BPMNInterface
        self.BPMNProfile_BPMNInterface228 = BPMNProfile_BPMNInterface228
        self.BPMNProfile_BPMNInterface230 = BPMNProfile_BPMNInterface230
        self.BPMNProfile_BPMNInterface233 = BPMNProfile_BPMNInterface233 if BPMNProfile_BPMNInterface233 is not None else set()
        self.BPMNProfile_BPMNInterface235 = BPMNProfile_BPMNInterface235 if BPMNProfile_BPMNInterface235 is not None else set()
        self.BPMNProfile_BPMNInterface301 = BPMNProfile_BPMNInterface301
        
    @property
    def BPMNProfile_BPMNInterface(self):
        return self.__BPMNProfile_BPMNInterface

    @BPMNProfile_BPMNInterface.setter
    def BPMNProfile_BPMNInterface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNInterface__BPMNProfile_BPMNInterface", None)
        self.__BPMNProfile_BPMNInterface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CallableElement152"):
                opp_val = getattr(old_value, "BPMNProfile_CallableElement152", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CallableElement152"):
                opp_val = getattr(value, "BPMNProfile_CallableElement152", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_CallableElement152", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_BPMNInterface235(self):
        return self.__BPMNProfile_BPMNInterface235

    @BPMNProfile_BPMNInterface235.setter
    def BPMNProfile_BPMNInterface235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNInterface__BPMNProfile_BPMNInterface235", None)
        self.__BPMNProfile_BPMNInterface235 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_CallableElement236"):
                    opp_val = getattr(item, "BPMNProfile_CallableElement236", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_CallableElement236", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_CallableElement236"):
                    opp_val = getattr(item, "BPMNProfile_CallableElement236", None)
                    
                    setattr(item, "BPMNProfile_CallableElement236", self)
                    

    @property
    def BPMNProfile_BPMNInterface301(self):
        return self.__BPMNProfile_BPMNInterface301

    @BPMNProfile_BPMNInterface301.setter
    def BPMNProfile_BPMNInterface301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNInterface__BPMNProfile_BPMNInterface301", None)
        self.__BPMNProfile_BPMNInterface301 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Participant300"):
                opp_val = getattr(old_value, "BPMNProfile_Participant300", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Participant300"):
                opp_val = getattr(value, "BPMNProfile_Participant300", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_Participant300", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_BPMNInterface233(self):
        return self.__BPMNProfile_BPMNInterface233

    @BPMNProfile_BPMNInterface233.setter
    def BPMNProfile_BPMNInterface233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNInterface__BPMNProfile_BPMNInterface233", None)
        self.__BPMNProfile_BPMNInterface233 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_BPMNOperation"):
                    opp_val = getattr(item, "BPMNProfile_BPMNOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_BPMNOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_BPMNOperation"):
                    opp_val = getattr(item, "BPMNProfile_BPMNOperation", None)
                    
                    setattr(item, "BPMNProfile_BPMNOperation", self)
                    

    @property
    def BPMNProfile_BPMNInterface230(self):
        return self.__BPMNProfile_BPMNInterface230

    @BPMNProfile_BPMNInterface230.setter
    def BPMNProfile_BPMNInterface230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNInterface__BPMNProfile_BPMNInterface230", None)
        self.__BPMNProfile_BPMNInterface230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Element231"):
                opp_val = getattr(old_value, "BPMNProfile_Element231", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Element231", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Element231"):
                opp_val = getattr(value, "BPMNProfile_Element231", None)
                setattr(value, "BPMNProfile_Element231", self)

    @property
    def BPMNProfile_BPMNInterface228(self):
        return self.__BPMNProfile_BPMNInterface228

    @BPMNProfile_BPMNInterface228.setter
    def BPMNProfile_BPMNInterface228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNInterface__BPMNProfile_BPMNInterface228", None)
        self.__BPMNProfile_BPMNInterface228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Interface"):
                opp_val = getattr(old_value, "BPMNProfile_Interface", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Interface", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Interface"):
                opp_val = getattr(value, "BPMNProfile_Interface", None)
                setattr(value, "BPMNProfile_Interface", self)

    def BPMNInterfacecallableElements(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BPMNInterfacecallableElements method
        pass

    def BPMNInterfaceoperations(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement BPMNInterfaceoperations method
        pass

    def Interfaceoperationmultiplicity(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement Interfaceoperationmultiplicity method
        pass

    def InterfaceownedOperation(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement InterfaceownedOperation method
        pass

class BPMNProfile_CallableElement(RootElement):

    def __init__(self, BPMNProfile_CallableElement: "BPMNProfile_Behavior" = None, BPMNProfile_CallableElement150: "BPMNProfile_InputOutputSpecification" = None, BPMNProfile_CallableElement152: set["BPMNProfile_BPMNInterface"] = None, BPMNProfile_CallableElement154: set["BPMNProfile_InputOutputBinding"] = None, BPMNProfile_CallableElement236: "BPMNProfile_BPMNInterface" = None, BPMNProfile_CallableElement617: "BPMNProfile_CallActivity" = None):
        self.BPMNProfile_CallableElement = BPMNProfile_CallableElement
        self.BPMNProfile_CallableElement150 = BPMNProfile_CallableElement150
        self.BPMNProfile_CallableElement152 = BPMNProfile_CallableElement152 if BPMNProfile_CallableElement152 is not None else set()
        self.BPMNProfile_CallableElement154 = BPMNProfile_CallableElement154 if BPMNProfile_CallableElement154 is not None else set()
        self.BPMNProfile_CallableElement236 = BPMNProfile_CallableElement236
        self.BPMNProfile_CallableElement617 = BPMNProfile_CallableElement617
        
    @property
    def BPMNProfile_CallableElement236(self):
        return self.__BPMNProfile_CallableElement236

    @BPMNProfile_CallableElement236.setter
    def BPMNProfile_CallableElement236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CallableElement__BPMNProfile_CallableElement236", None)
        self.__BPMNProfile_CallableElement236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNInterface235"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNInterface235", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNInterface235"):
                opp_val = getattr(value, "BPMNProfile_BPMNInterface235", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNInterface235", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_CallableElement617(self):
        return self.__BPMNProfile_CallableElement617

    @BPMNProfile_CallableElement617.setter
    def BPMNProfile_CallableElement617(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CallableElement__BPMNProfile_CallableElement617", None)
        self.__BPMNProfile_CallableElement617 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CallActivity616"):
                opp_val = getattr(old_value, "BPMNProfile_CallActivity616", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_CallActivity616", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CallActivity616"):
                opp_val = getattr(value, "BPMNProfile_CallActivity616", None)
                setattr(value, "BPMNProfile_CallActivity616", self)

    @property
    def BPMNProfile_CallableElement152(self):
        return self.__BPMNProfile_CallableElement152

    @BPMNProfile_CallableElement152.setter
    def BPMNProfile_CallableElement152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CallableElement__BPMNProfile_CallableElement152", None)
        self.__BPMNProfile_CallableElement152 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_BPMNInterface"):
                    opp_val = getattr(item, "BPMNProfile_BPMNInterface", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_BPMNInterface", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_BPMNInterface"):
                    opp_val = getattr(item, "BPMNProfile_BPMNInterface", None)
                    
                    setattr(item, "BPMNProfile_BPMNInterface", self)
                    

    @property
    def BPMNProfile_CallableElement150(self):
        return self.__BPMNProfile_CallableElement150

    @BPMNProfile_CallableElement150.setter
    def BPMNProfile_CallableElement150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CallableElement__BPMNProfile_CallableElement150", None)
        self.__BPMNProfile_CallableElement150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_InputOutputSpecification"):
                opp_val = getattr(old_value, "BPMNProfile_InputOutputSpecification", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_InputOutputSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_InputOutputSpecification"):
                opp_val = getattr(value, "BPMNProfile_InputOutputSpecification", None)
                setattr(value, "BPMNProfile_InputOutputSpecification", self)

    @property
    def BPMNProfile_CallableElement(self):
        return self.__BPMNProfile_CallableElement

    @BPMNProfile_CallableElement.setter
    def BPMNProfile_CallableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CallableElement__BPMNProfile_CallableElement", None)
        self.__BPMNProfile_CallableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Behavior"):
                opp_val = getattr(old_value, "BPMNProfile_Behavior", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Behavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Behavior"):
                opp_val = getattr(value, "BPMNProfile_Behavior", None)
                setattr(value, "BPMNProfile_Behavior", self)

    @property
    def BPMNProfile_CallableElement154(self):
        return self.__BPMNProfile_CallableElement154

    @BPMNProfile_CallableElement154.setter
    def BPMNProfile_CallableElement154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CallableElement__BPMNProfile_CallableElement154", None)
        self.__BPMNProfile_CallableElement154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_InputOutputBinding"):
                    opp_val = getattr(item, "BPMNProfile_InputOutputBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_InputOutputBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_InputOutputBinding"):
                    opp_val = getattr(item, "BPMNProfile_InputOutputBinding", None)
                    
                    setattr(item, "BPMNProfile_InputOutputBinding", self)
                    

    def CallableEelementsupportedInterfaceRefs(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement CallableEelementsupportedInterfaceRefs method
        pass

    def CallableElementresources(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement CallableElementresources method
        pass

class BPMNProfile_BPMNProperty(ItemAwareElement):

    def __init__(self, BPMNProfile_BPMNProperty: "BPMNProfile_BPMNProcess" = None, BPMNProfile_BPMNProperty398: "BPMNProfile_DataStoreNode" = None, BPMNProfile_BPMNProperty400: "BPMNProfile_Property" = None, BPMNProfile_BPMNProperty447: "BPMNProfile_BPMNActivity" = None, BPMNProfile_BPMNProperty478: "BPMNProfile_BPMNEvent" = None):
        self.BPMNProfile_BPMNProperty = BPMNProfile_BPMNProperty
        self.BPMNProfile_BPMNProperty398 = BPMNProfile_BPMNProperty398
        self.BPMNProfile_BPMNProperty400 = BPMNProfile_BPMNProperty400
        self.BPMNProfile_BPMNProperty447 = BPMNProfile_BPMNProperty447
        self.BPMNProfile_BPMNProperty478 = BPMNProfile_BPMNProperty478
        
    @property
    def BPMNProfile_BPMNProperty447(self):
        return self.__BPMNProfile_BPMNProperty447

    @BPMNProfile_BPMNProperty447.setter
    def BPMNProfile_BPMNProperty447(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProperty__BPMNProfile_BPMNProperty447", None)
        self.__BPMNProfile_BPMNProperty447 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNActivity446"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNActivity446", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNActivity446"):
                opp_val = getattr(value, "BPMNProfile_BPMNActivity446", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNActivity446", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_BPMNProperty478(self):
        return self.__BPMNProfile_BPMNProperty478

    @BPMNProfile_BPMNProperty478.setter
    def BPMNProfile_BPMNProperty478(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProperty__BPMNProfile_BPMNProperty478", None)
        self.__BPMNProfile_BPMNProperty478 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNEvent477"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNEvent477", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNEvent477"):
                opp_val = getattr(value, "BPMNProfile_BPMNEvent477", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNEvent477", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_BPMNProperty400(self):
        return self.__BPMNProfile_BPMNProperty400

    @BPMNProfile_BPMNProperty400.setter
    def BPMNProfile_BPMNProperty400(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProperty__BPMNProfile_BPMNProperty400", None)
        self.__BPMNProfile_BPMNProperty400 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Property401"):
                opp_val = getattr(old_value, "BPMNProfile_Property401", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Property401", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Property401"):
                opp_val = getattr(value, "BPMNProfile_Property401", None)
                setattr(value, "BPMNProfile_Property401", self)

    @property
    def BPMNProfile_BPMNProperty398(self):
        return self.__BPMNProfile_BPMNProperty398

    @BPMNProfile_BPMNProperty398.setter
    def BPMNProfile_BPMNProperty398(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProperty__BPMNProfile_BPMNProperty398", None)
        self.__BPMNProfile_BPMNProperty398 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_DataStoreNode"):
                opp_val = getattr(old_value, "BPMNProfile_DataStoreNode", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_DataStoreNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_DataStoreNode"):
                opp_val = getattr(value, "BPMNProfile_DataStoreNode", None)
                setattr(value, "BPMNProfile_DataStoreNode", self)

    @property
    def BPMNProfile_BPMNProperty(self):
        return self.__BPMNProfile_BPMNProperty

    @BPMNProfile_BPMNProperty.setter
    def BPMNProfile_BPMNProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProperty__BPMNProfile_BPMNProperty", None)
        self.__BPMNProfile_BPMNProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNProcess146"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNProcess146", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNProcess146"):
                opp_val = getattr(value, "BPMNProfile_BPMNProcess146", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNProcess146", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def BPMNPropertyapply(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement BPMNPropertyapply method
        pass

    def Propertynotation(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement Propertynotation method
        pass

class BPMNProfile_DataOutput(ItemAwareElement):

    def __init__(self, isCollection: str, BPMNProfile_DataOutput: "BPMNProfile_InputOutputSpecification" = None, BPMNProfile_DataOutput203: "BPMNProfile_OutputPin" = None, BPMNProfile_DataOutput205: "BPMNProfile_Parameter" = None, DataOutput: "BPMNProfile_OutputSet" = None, BPMNProfile_DataOutput208: "BPMNProfile_ActivityParameterNode" = None, dataOutputRefs: set["BPMNProfile_OutputSet"] = None, BPMNProfile_DataOutput212: set["BPMNProfile_OutputSet"] = None, BPMNProfile_DataOutput215: set["BPMNProfile_OutputSet"] = None, BPMNProfile_DataOutput222: "BPMNProfile_OutputSet" = None, BPMNProfile_DataOutput225: "BPMNProfile_OutputSet" = None, BPMNProfile_DataOutput671: "BPMNProfile_MultiInstanceLoopCharacteristics" = None):
        self.isCollection = isCollection
        self.BPMNProfile_DataOutput = BPMNProfile_DataOutput
        self.BPMNProfile_DataOutput203 = BPMNProfile_DataOutput203
        self.BPMNProfile_DataOutput205 = BPMNProfile_DataOutput205
        self.DataOutput = DataOutput
        self.BPMNProfile_DataOutput208 = BPMNProfile_DataOutput208
        self.dataOutputRefs = dataOutputRefs if dataOutputRefs is not None else set()
        self.BPMNProfile_DataOutput212 = BPMNProfile_DataOutput212 if BPMNProfile_DataOutput212 is not None else set()
        self.BPMNProfile_DataOutput215 = BPMNProfile_DataOutput215 if BPMNProfile_DataOutput215 is not None else set()
        self.BPMNProfile_DataOutput222 = BPMNProfile_DataOutput222
        self.BPMNProfile_DataOutput225 = BPMNProfile_DataOutput225
        self.BPMNProfile_DataOutput671 = BPMNProfile_DataOutput671
        
    @property
    def isCollection(self) -> str:
        return self.__isCollection

    @isCollection.setter
    def isCollection(self, isCollection: str):
        self.__isCollection = isCollection

    @property
    def dataOutputRefs(self):
        return self.__dataOutputRefs

    @dataOutputRefs.setter
    def dataOutputRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataOutput__dataOutputRefs", None)
        self.__dataOutputRefs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputSet"):
                    opp_val = getattr(item, "OutputSet", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputSet"):
                    opp_val = getattr(item, "OutputSet", None)
                    
                    setattr(item, "OutputSet", self)
                    

    @property
    def BPMNProfile_DataOutput212(self):
        return self.__BPMNProfile_DataOutput212

    @BPMNProfile_DataOutput212.setter
    def BPMNProfile_DataOutput212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataOutput__BPMNProfile_DataOutput212", None)
        self.__BPMNProfile_DataOutput212 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_OutputSet213"):
                    opp_val = getattr(item, "BPMNProfile_OutputSet213", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_OutputSet213", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_OutputSet213"):
                    opp_val = getattr(item, "BPMNProfile_OutputSet213", None)
                    
                    setattr(item, "BPMNProfile_OutputSet213", self)
                    

    @property
    def BPMNProfile_DataOutput215(self):
        return self.__BPMNProfile_DataOutput215

    @BPMNProfile_DataOutput215.setter
    def BPMNProfile_DataOutput215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataOutput__BPMNProfile_DataOutput215", None)
        self.__BPMNProfile_DataOutput215 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_OutputSet216"):
                    opp_val = getattr(item, "BPMNProfile_OutputSet216", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_OutputSet216", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_OutputSet216"):
                    opp_val = getattr(item, "BPMNProfile_OutputSet216", None)
                    
                    setattr(item, "BPMNProfile_OutputSet216", self)
                    

    @property
    def BPMNProfile_DataOutput(self):
        return self.__BPMNProfile_DataOutput

    @BPMNProfile_DataOutput.setter
    def BPMNProfile_DataOutput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataOutput__BPMNProfile_DataOutput", None)
        self.__BPMNProfile_DataOutput = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_InputOutputSpecification163"):
                opp_val = getattr(old_value, "BPMNProfile_InputOutputSpecification163", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_InputOutputSpecification163"):
                opp_val = getattr(value, "BPMNProfile_InputOutputSpecification163", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_InputOutputSpecification163", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_DataOutput671(self):
        return self.__BPMNProfile_DataOutput671

    @BPMNProfile_DataOutput671.setter
    def BPMNProfile_DataOutput671(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataOutput__BPMNProfile_DataOutput671", None)
        self.__BPMNProfile_DataOutput671 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_MultiInstanceLoopCharacteristics670"):
                opp_val = getattr(old_value, "BPMNProfile_MultiInstanceLoopCharacteristics670", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_MultiInstanceLoopCharacteristics670", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_MultiInstanceLoopCharacteristics670"):
                opp_val = getattr(value, "BPMNProfile_MultiInstanceLoopCharacteristics670", None)
                setattr(value, "BPMNProfile_MultiInstanceLoopCharacteristics670", self)

    @property
    def BPMNProfile_DataOutput203(self):
        return self.__BPMNProfile_DataOutput203

    @BPMNProfile_DataOutput203.setter
    def BPMNProfile_DataOutput203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataOutput__BPMNProfile_DataOutput203", None)
        self.__BPMNProfile_DataOutput203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_OutputPin"):
                opp_val = getattr(old_value, "BPMNProfile_OutputPin", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_OutputPin", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_OutputPin"):
                opp_val = getattr(value, "BPMNProfile_OutputPin", None)
                setattr(value, "BPMNProfile_OutputPin", self)

    @property
    def BPMNProfile_DataOutput222(self):
        return self.__BPMNProfile_DataOutput222

    @BPMNProfile_DataOutput222.setter
    def BPMNProfile_DataOutput222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataOutput__BPMNProfile_DataOutput222", None)
        self.__BPMNProfile_DataOutput222 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_OutputSet221"):
                opp_val = getattr(old_value, "BPMNProfile_OutputSet221", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_OutputSet221"):
                opp_val = getattr(value, "BPMNProfile_OutputSet221", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_OutputSet221", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_DataOutput208(self):
        return self.__BPMNProfile_DataOutput208

    @BPMNProfile_DataOutput208.setter
    def BPMNProfile_DataOutput208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataOutput__BPMNProfile_DataOutput208", None)
        self.__BPMNProfile_DataOutput208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ActivityParameterNode209"):
                opp_val = getattr(old_value, "BPMNProfile_ActivityParameterNode209", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ActivityParameterNode209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ActivityParameterNode209"):
                opp_val = getattr(value, "BPMNProfile_ActivityParameterNode209", None)
                setattr(value, "BPMNProfile_ActivityParameterNode209", self)

    @property
    def BPMNProfile_DataOutput205(self):
        return self.__BPMNProfile_DataOutput205

    @BPMNProfile_DataOutput205.setter
    def BPMNProfile_DataOutput205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataOutput__BPMNProfile_DataOutput205", None)
        self.__BPMNProfile_DataOutput205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Parameter206"):
                opp_val = getattr(old_value, "BPMNProfile_Parameter206", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Parameter206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Parameter206"):
                opp_val = getattr(value, "BPMNProfile_Parameter206", None)
                setattr(value, "BPMNProfile_Parameter206", self)

    @property
    def DataOutput(self):
        return self.__DataOutput

    @DataOutput.setter
    def DataOutput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataOutput__DataOutput", None)
        self.__DataOutput = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outputSetRefs"):
                opp_val = getattr(old_value, "outputSetRefs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outputSetRefs"):
                opp_val = getattr(value, "outputSetRefs", None)
                if opp_val is None:
                    setattr(value, "outputSetRefs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_DataOutput225(self):
        return self.__BPMNProfile_DataOutput225

    @BPMNProfile_DataOutput225.setter
    def BPMNProfile_DataOutput225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataOutput__BPMNProfile_DataOutput225", None)
        self.__BPMNProfile_DataOutput225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_OutputSet224"):
                opp_val = getattr(old_value, "BPMNProfile_OutputSet224", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_OutputSet224"):
                opp_val = getattr(value, "BPMNProfile_OutputSet224", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_OutputSet224", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def DataOutputitemSubjectRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement DataOutputitemSubjectRef method
        pass

    def DataOutputnotation(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement DataOutputnotation method
        pass

class BPMNProfile_DataInput(ItemAwareElement):

    def __init__(self, isCollection: str, BPMNProfile_DataInput: "BPMNProfile_InputOutputSpecification" = None, BPMNProfile_DataInput169: "BPMNProfile_InputPin" = None, BPMNProfile_DataInput171: "BPMNProfile_Parameter" = None, BPMNProfile_DataInput173: "BPMNProfile_ActivityParameterNode" = None, dataInputRefs: set["BPMNProfile_InputSet"] = None, optionalInputRefs: set["BPMNProfile_InputSet"] = None, whileExecutingInputRefs: set["BPMNProfile_InputSet"] = None, DataInput: "BPMNProfile_InputSet" = None, DataInput199: "BPMNProfile_InputSet" = None, DataInput201: "BPMNProfile_InputSet" = None, BPMNProfile_DataInput674: "BPMNProfile_MultiInstanceLoopCharacteristics" = None):
        self.isCollection = isCollection
        self.BPMNProfile_DataInput = BPMNProfile_DataInput
        self.BPMNProfile_DataInput169 = BPMNProfile_DataInput169
        self.BPMNProfile_DataInput171 = BPMNProfile_DataInput171
        self.BPMNProfile_DataInput173 = BPMNProfile_DataInput173
        self.dataInputRefs = dataInputRefs if dataInputRefs is not None else set()
        self.optionalInputRefs = optionalInputRefs if optionalInputRefs is not None else set()
        self.whileExecutingInputRefs = whileExecutingInputRefs if whileExecutingInputRefs is not None else set()
        self.DataInput = DataInput
        self.DataInput199 = DataInput199
        self.DataInput201 = DataInput201
        self.BPMNProfile_DataInput674 = BPMNProfile_DataInput674
        
    @property
    def isCollection(self) -> str:
        return self.__isCollection

    @isCollection.setter
    def isCollection(self, isCollection: str):
        self.__isCollection = isCollection

    @property
    def optionalInputRefs(self):
        return self.__optionalInputRefs

    @optionalInputRefs.setter
    def optionalInputRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataInput__optionalInputRefs", None)
        self.__optionalInputRefs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InputSet176"):
                    opp_val = getattr(item, "InputSet176", None)
                    
                    if opp_val == self:
                        setattr(item, "InputSet176", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputSet176"):
                    opp_val = getattr(item, "InputSet176", None)
                    
                    setattr(item, "InputSet176", self)
                    

    @property
    def BPMNProfile_DataInput171(self):
        return self.__BPMNProfile_DataInput171

    @BPMNProfile_DataInput171.setter
    def BPMNProfile_DataInput171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataInput__BPMNProfile_DataInput171", None)
        self.__BPMNProfile_DataInput171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Parameter"):
                opp_val = getattr(old_value, "BPMNProfile_Parameter", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Parameter"):
                opp_val = getattr(value, "BPMNProfile_Parameter", None)
                setattr(value, "BPMNProfile_Parameter", self)

    @property
    def BPMNProfile_DataInput169(self):
        return self.__BPMNProfile_DataInput169

    @BPMNProfile_DataInput169.setter
    def BPMNProfile_DataInput169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataInput__BPMNProfile_DataInput169", None)
        self.__BPMNProfile_DataInput169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_InputPin"):
                opp_val = getattr(old_value, "BPMNProfile_InputPin", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_InputPin", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_InputPin"):
                opp_val = getattr(value, "BPMNProfile_InputPin", None)
                setattr(value, "BPMNProfile_InputPin", self)

    @property
    def BPMNProfile_DataInput173(self):
        return self.__BPMNProfile_DataInput173

    @BPMNProfile_DataInput173.setter
    def BPMNProfile_DataInput173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataInput__BPMNProfile_DataInput173", None)
        self.__BPMNProfile_DataInput173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ActivityParameterNode"):
                opp_val = getattr(old_value, "BPMNProfile_ActivityParameterNode", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ActivityParameterNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ActivityParameterNode"):
                opp_val = getattr(value, "BPMNProfile_ActivityParameterNode", None)
                setattr(value, "BPMNProfile_ActivityParameterNode", self)

    @property
    def DataInput(self):
        return self.__DataInput

    @DataInput.setter
    def DataInput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataInput__DataInput", None)
        self.__DataInput = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inputSetWithOptional"):
                opp_val = getattr(old_value, "inputSetWithOptional", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inputSetWithOptional"):
                opp_val = getattr(value, "inputSetWithOptional", None)
                if opp_val is None:
                    setattr(value, "inputSetWithOptional", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DataInput201(self):
        return self.__DataInput201

    @DataInput201.setter
    def DataInput201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataInput__DataInput201", None)
        self.__DataInput201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inputSetRefs"):
                opp_val = getattr(old_value, "inputSetRefs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inputSetRefs"):
                opp_val = getattr(value, "inputSetRefs", None)
                if opp_val is None:
                    setattr(value, "inputSetRefs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_DataInput674(self):
        return self.__BPMNProfile_DataInput674

    @BPMNProfile_DataInput674.setter
    def BPMNProfile_DataInput674(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataInput__BPMNProfile_DataInput674", None)
        self.__BPMNProfile_DataInput674 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_MultiInstanceLoopCharacteristics673"):
                opp_val = getattr(old_value, "BPMNProfile_MultiInstanceLoopCharacteristics673", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_MultiInstanceLoopCharacteristics673", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_MultiInstanceLoopCharacteristics673"):
                opp_val = getattr(value, "BPMNProfile_MultiInstanceLoopCharacteristics673", None)
                setattr(value, "BPMNProfile_MultiInstanceLoopCharacteristics673", self)

    @property
    def DataInput199(self):
        return self.__DataInput199

    @DataInput199.setter
    def DataInput199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataInput__DataInput199", None)
        self.__DataInput199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inputSetWithWhileExecuting"):
                opp_val = getattr(old_value, "inputSetWithWhileExecuting", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inputSetWithWhileExecuting"):
                opp_val = getattr(value, "inputSetWithWhileExecuting", None)
                if opp_val is None:
                    setattr(value, "inputSetWithWhileExecuting", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_DataInput(self):
        return self.__BPMNProfile_DataInput

    @BPMNProfile_DataInput.setter
    def BPMNProfile_DataInput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataInput__BPMNProfile_DataInput", None)
        self.__BPMNProfile_DataInput = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_InputOutputSpecification161"):
                opp_val = getattr(old_value, "BPMNProfile_InputOutputSpecification161", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_InputOutputSpecification161"):
                opp_val = getattr(value, "BPMNProfile_InputOutputSpecification161", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_InputOutputSpecification161", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def whileExecutingInputRefs(self):
        return self.__whileExecutingInputRefs

    @whileExecutingInputRefs.setter
    def whileExecutingInputRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataInput__whileExecutingInputRefs", None)
        self.__whileExecutingInputRefs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InputSet178"):
                    opp_val = getattr(item, "InputSet178", None)
                    
                    if opp_val == self:
                        setattr(item, "InputSet178", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputSet178"):
                    opp_val = getattr(item, "InputSet178", None)
                    
                    setattr(item, "InputSet178", self)
                    

    @property
    def dataInputRefs(self):
        return self.__dataInputRefs

    @dataInputRefs.setter
    def dataInputRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataInput__dataInputRefs", None)
        self.__dataInputRefs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InputSet"):
                    opp_val = getattr(item, "InputSet", None)
                    
                    if opp_val == self:
                        setattr(item, "InputSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputSet"):
                    opp_val = getattr(item, "InputSet", None)
                    
                    setattr(item, "InputSet", self)
                    

    def DataInputAssociation(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement DataInputAssociation method
        pass

    def DataInputnotation(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement DataInputnotation method
        pass

    def DataInputitemSubjectRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement DataInputitemSubjectRef method
        pass

class FlowElementsContainer:

    pass
class BPMNProfile_SubProcess(FlowElementsContainer, BPMNActivity):

    def __init__(self, triggeredByEvent: str, BPMNProfile_SubProcess: "BPMNProfile_StructuredActivityNode" = None, BPMNProfile_SubProcess612: set["BPMNProfile_LaneSet"] = None):
        self.triggeredByEvent = triggeredByEvent
        self.BPMNProfile_SubProcess = BPMNProfile_SubProcess
        self.BPMNProfile_SubProcess612 = BPMNProfile_SubProcess612 if BPMNProfile_SubProcess612 is not None else set()
        
    @property
    def triggeredByEvent(self) -> str:
        return self.__triggeredByEvent

    @triggeredByEvent.setter
    def triggeredByEvent(self, triggeredByEvent: str):
        self.__triggeredByEvent = triggeredByEvent

    @property
    def BPMNProfile_SubProcess(self):
        return self.__BPMNProfile_SubProcess

    @BPMNProfile_SubProcess.setter
    def BPMNProfile_SubProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_SubProcess__BPMNProfile_SubProcess", None)
        self.__BPMNProfile_SubProcess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_StructuredActivityNode610"):
                opp_val = getattr(old_value, "BPMNProfile_StructuredActivityNode610", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_StructuredActivityNode610", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_StructuredActivityNode610"):
                opp_val = getattr(value, "BPMNProfile_StructuredActivityNode610", None)
                setattr(value, "BPMNProfile_StructuredActivityNode610", self)

    @property
    def BPMNProfile_SubProcess612(self):
        return self.__BPMNProfile_SubProcess612

    @BPMNProfile_SubProcess612.setter
    def BPMNProfile_SubProcess612(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_SubProcess__BPMNProfile_SubProcess612", None)
        self.__BPMNProfile_SubProcess612 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_LaneSet613"):
                    opp_val = getattr(item, "BPMNProfile_LaneSet613", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_LaneSet613", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_LaneSet613"):
                    opp_val = getattr(item, "BPMNProfile_LaneSet613", None)
                    
                    setattr(item, "BPMNProfile_LaneSet613", self)
                    

    def SubProcesstriggeredByEvent(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SubProcesstriggeredByEvent method
        pass

class CallableElement:

    pass
class BPMNProfile_GlobalTask(CallableElement):

    def __init__(self, BPMNProfile_GlobalTask: "BPMNProfile_OpaqueBehavior" = None, BPMNProfile_GlobalTask433: set["BPMNProfile_ResourceRole"] = None):
        self.BPMNProfile_GlobalTask = BPMNProfile_GlobalTask
        self.BPMNProfile_GlobalTask433 = BPMNProfile_GlobalTask433 if BPMNProfile_GlobalTask433 is not None else set()
        
    @property
    def BPMNProfile_GlobalTask433(self):
        return self.__BPMNProfile_GlobalTask433

    @BPMNProfile_GlobalTask433.setter
    def BPMNProfile_GlobalTask433(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_GlobalTask__BPMNProfile_GlobalTask433", None)
        self.__BPMNProfile_GlobalTask433 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_ResourceRole434"):
                    opp_val = getattr(item, "BPMNProfile_ResourceRole434", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_ResourceRole434", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_ResourceRole434"):
                    opp_val = getattr(item, "BPMNProfile_ResourceRole434", None)
                    
                    setattr(item, "BPMNProfile_ResourceRole434", self)
                    

    @property
    def BPMNProfile_GlobalTask(self):
        return self.__BPMNProfile_GlobalTask

    @BPMNProfile_GlobalTask.setter
    def BPMNProfile_GlobalTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_GlobalTask__BPMNProfile_GlobalTask", None)
        self.__BPMNProfile_GlobalTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_OpaqueBehavior"):
                opp_val = getattr(old_value, "BPMNProfile_OpaqueBehavior", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_OpaqueBehavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_OpaqueBehavior"):
                opp_val = getattr(value, "BPMNProfile_OpaqueBehavior", None)
                setattr(value, "BPMNProfile_OpaqueBehavior", self)

    def GlobalTasksupportedInterfaceRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement GlobalTasksupportedInterfaceRefs method
        pass

class BPMNProfile_BPMNProcess(FlowElementsContainer, CallableElement):

    def __init__(self, isExecutable: str, processType: str, isClosed: str, BPMNProfile_BPMNProcess: "BPMNProfile_Auditing" = None, BPMNProfile_BPMNProcess134: "BPMNProfile_BPMNCollaboration" = None, BPMNProfile_BPMNProcess136: "BPMNProfile_Activity" = None, BPMNProfile_BPMNProcess138: set["BPMNProfile_CorrelationSubscription"] = None, BPMNProfile_BPMNProcess140: "BPMNProfile_Monitoring" = None, BPMNProfile_BPMNProcess144: "BPMNProfile_BPMNProcess" = None, BPMNProfile_BPMNProcess142: "BPMNProfile_BPMNProcess" = None, BPMNProfile_BPMNProcess146: set["BPMNProfile_BPMNProperty"] = None, process: set["BPMNProfile_ResourceRole"] = None, BPMNProfile_BPMNProcess293: "BPMNProfile_Participant" = None, BPMNProcess: "BPMNProfile_ResourceRole" = None):
        self.isExecutable = isExecutable
        self.processType = processType
        self.isClosed = isClosed
        self.BPMNProfile_BPMNProcess = BPMNProfile_BPMNProcess
        self.BPMNProfile_BPMNProcess134 = BPMNProfile_BPMNProcess134
        self.BPMNProfile_BPMNProcess136 = BPMNProfile_BPMNProcess136
        self.BPMNProfile_BPMNProcess138 = BPMNProfile_BPMNProcess138 if BPMNProfile_BPMNProcess138 is not None else set()
        self.BPMNProfile_BPMNProcess140 = BPMNProfile_BPMNProcess140
        self.BPMNProfile_BPMNProcess144 = BPMNProfile_BPMNProcess144
        self.BPMNProfile_BPMNProcess142 = BPMNProfile_BPMNProcess142
        self.BPMNProfile_BPMNProcess146 = BPMNProfile_BPMNProcess146 if BPMNProfile_BPMNProcess146 is not None else set()
        self.process = process if process is not None else set()
        self.BPMNProfile_BPMNProcess293 = BPMNProfile_BPMNProcess293
        self.BPMNProcess = BPMNProcess
        
    @property
    def isExecutable(self) -> str:
        return self.__isExecutable

    @isExecutable.setter
    def isExecutable(self, isExecutable: str):
        self.__isExecutable = isExecutable

    @property
    def processType(self) -> str:
        return self.__processType

    @processType.setter
    def processType(self, processType: str):
        self.__processType = processType

    @property
    def isClosed(self) -> str:
        return self.__isClosed

    @isClosed.setter
    def isClosed(self, isClosed: str):
        self.__isClosed = isClosed

    @property
    def BPMNProfile_BPMNProcess146(self):
        return self.__BPMNProfile_BPMNProcess146

    @BPMNProfile_BPMNProcess146.setter
    def BPMNProfile_BPMNProcess146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProcess__BPMNProfile_BPMNProcess146", None)
        self.__BPMNProfile_BPMNProcess146 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_BPMNProperty"):
                    opp_val = getattr(item, "BPMNProfile_BPMNProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_BPMNProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_BPMNProperty"):
                    opp_val = getattr(item, "BPMNProfile_BPMNProperty", None)
                    
                    setattr(item, "BPMNProfile_BPMNProperty", self)
                    

    @property
    def BPMNProfile_BPMNProcess144(self):
        return self.__BPMNProfile_BPMNProcess144

    @BPMNProfile_BPMNProcess144.setter
    def BPMNProfile_BPMNProcess144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProcess__BPMNProfile_BPMNProcess144", None)
        self.__BPMNProfile_BPMNProcess144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNProcess142"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNProcess142", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNProcess142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNProcess142"):
                opp_val = getattr(value, "BPMNProfile_BPMNProcess142", None)
                setattr(value, "BPMNProfile_BPMNProcess142", self)

    @property
    def BPMNProcess(self):
        return self.__BPMNProcess

    @BPMNProcess.setter
    def BPMNProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProcess__BPMNProcess", None)
        self.__BPMNProcess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resources"):
                opp_val = getattr(old_value, "resources", None)
                if opp_val == self:
                    setattr(old_value, "resources", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resources"):
                opp_val = getattr(value, "resources", None)
                setattr(value, "resources", self)

    @property
    def BPMNProfile_BPMNProcess140(self):
        return self.__BPMNProfile_BPMNProcess140

    @BPMNProfile_BPMNProcess140.setter
    def BPMNProfile_BPMNProcess140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProcess__BPMNProfile_BPMNProcess140", None)
        self.__BPMNProfile_BPMNProcess140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Monitoring141"):
                opp_val = getattr(old_value, "BPMNProfile_Monitoring141", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Monitoring141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Monitoring141"):
                opp_val = getattr(value, "BPMNProfile_Monitoring141", None)
                setattr(value, "BPMNProfile_Monitoring141", self)

    @property
    def BPMNProfile_BPMNProcess138(self):
        return self.__BPMNProfile_BPMNProcess138

    @BPMNProfile_BPMNProcess138.setter
    def BPMNProfile_BPMNProcess138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProcess__BPMNProfile_BPMNProcess138", None)
        self.__BPMNProfile_BPMNProcess138 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_CorrelationSubscription"):
                    opp_val = getattr(item, "BPMNProfile_CorrelationSubscription", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_CorrelationSubscription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_CorrelationSubscription"):
                    opp_val = getattr(item, "BPMNProfile_CorrelationSubscription", None)
                    
                    setattr(item, "BPMNProfile_CorrelationSubscription", self)
                    

    @property
    def process(self):
        return self.__process

    @process.setter
    def process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProcess__process", None)
        self.__process = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ResourceRole"):
                    opp_val = getattr(item, "ResourceRole", None)
                    
                    if opp_val == self:
                        setattr(item, "ResourceRole", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ResourceRole"):
                    opp_val = getattr(item, "ResourceRole", None)
                    
                    setattr(item, "ResourceRole", self)
                    

    @property
    def BPMNProfile_BPMNProcess134(self):
        return self.__BPMNProfile_BPMNProcess134

    @BPMNProfile_BPMNProcess134.setter
    def BPMNProfile_BPMNProcess134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProcess__BPMNProfile_BPMNProcess134", None)
        self.__BPMNProfile_BPMNProcess134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNCollaboration"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNCollaboration", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNCollaboration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNCollaboration"):
                opp_val = getattr(value, "BPMNProfile_BPMNCollaboration", None)
                setattr(value, "BPMNProfile_BPMNCollaboration", self)

    @property
    def BPMNProfile_BPMNProcess142(self):
        return self.__BPMNProfile_BPMNProcess142

    @BPMNProfile_BPMNProcess142.setter
    def BPMNProfile_BPMNProcess142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProcess__BPMNProfile_BPMNProcess142", None)
        self.__BPMNProfile_BPMNProcess142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNProcess144"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNProcess144", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNProcess144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNProcess144"):
                opp_val = getattr(value, "BPMNProfile_BPMNProcess144", None)
                setattr(value, "BPMNProfile_BPMNProcess144", self)

    @property
    def BPMNProfile_BPMNProcess136(self):
        return self.__BPMNProfile_BPMNProcess136

    @BPMNProfile_BPMNProcess136.setter
    def BPMNProfile_BPMNProcess136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProcess__BPMNProfile_BPMNProcess136", None)
        self.__BPMNProfile_BPMNProcess136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Activity"):
                opp_val = getattr(old_value, "BPMNProfile_Activity", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Activity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Activity"):
                opp_val = getattr(value, "BPMNProfile_Activity", None)
                setattr(value, "BPMNProfile_Activity", self)

    @property
    def BPMNProfile_BPMNProcess293(self):
        return self.__BPMNProfile_BPMNProcess293

    @BPMNProfile_BPMNProcess293.setter
    def BPMNProfile_BPMNProcess293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProcess__BPMNProfile_BPMNProcess293", None)
        self.__BPMNProfile_BPMNProcess293 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Participant292"):
                opp_val = getattr(old_value, "BPMNProfile_Participant292", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Participant292", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Participant292"):
                opp_val = getattr(value, "BPMNProfile_Participant292", None)
                setattr(value, "BPMNProfile_Participant292", self)

    @property
    def BPMNProfile_BPMNProcess(self):
        return self.__BPMNProfile_BPMNProcess

    @BPMNProfile_BPMNProcess.setter
    def BPMNProfile_BPMNProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProcess__BPMNProfile_BPMNProcess", None)
        self.__BPMNProfile_BPMNProcess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Auditing132"):
                opp_val = getattr(old_value, "BPMNProfile_Auditing132", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Auditing132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Auditing132"):
                opp_val = getattr(value, "BPMNProfile_Auditing132", None)
                setattr(value, "BPMNProfile_Auditing132", self)

    def ProcessflowElements(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ProcessflowElements method
        pass

    def ProcesssupportedInterfaceRefs(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ProcesssupportedInterfaceRefs method
        pass

    def ProcesslaneSets(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ProcesslaneSets method
        pass

    def Processproperties(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement Processproperties method
        pass

    def Processsupports(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement Processsupports method
        pass

class BPMNProfile_Activity:

    pass
class BPMNProfile_BPMNCollaboration(RootElement):

    def __init__(self, isClosed: str, BPMNProfile_BPMNCollaboration: "BPMNProfile_BPMNProcess" = None, BPMNProfile_BPMNCollaboration265: set["BPMNProfile_ParticipantAssociation"] = None, collaboration: set["BPMNProfile_ConversationLink"] = None, BPMNProfile_BPMNCollaboration268: set["BPMNProfile_MessageFlowAssociation"] = None, BPMNProfile_BPMNCollaboration270: set["BPMNProfile_MessageFlow"] = None, BPMNProfile_BPMNCollaboration272: "BPMNProfile_Collaboration" = None, BPMNProfile_BPMNCollaboration274: set["BPMNProfile_ConversationNode"] = None, BPMNProfile_BPMNCollaboration276: set["BPMNProfile_CorrelationKey"] = None, BPMNProfile_BPMNCollaboration278: set["BPMNProfile_Participant"] = None, BPMNCollaboration: "BPMNProfile_ConversationLink" = None, BPMNProfile_BPMNCollaboration605: "BPMNProfile_CallConversation" = None):
        self.isClosed = isClosed
        self.BPMNProfile_BPMNCollaboration = BPMNProfile_BPMNCollaboration
        self.BPMNProfile_BPMNCollaboration265 = BPMNProfile_BPMNCollaboration265 if BPMNProfile_BPMNCollaboration265 is not None else set()
        self.collaboration = collaboration if collaboration is not None else set()
        self.BPMNProfile_BPMNCollaboration268 = BPMNProfile_BPMNCollaboration268 if BPMNProfile_BPMNCollaboration268 is not None else set()
        self.BPMNProfile_BPMNCollaboration270 = BPMNProfile_BPMNCollaboration270 if BPMNProfile_BPMNCollaboration270 is not None else set()
        self.BPMNProfile_BPMNCollaboration272 = BPMNProfile_BPMNCollaboration272
        self.BPMNProfile_BPMNCollaboration274 = BPMNProfile_BPMNCollaboration274 if BPMNProfile_BPMNCollaboration274 is not None else set()
        self.BPMNProfile_BPMNCollaboration276 = BPMNProfile_BPMNCollaboration276 if BPMNProfile_BPMNCollaboration276 is not None else set()
        self.BPMNProfile_BPMNCollaboration278 = BPMNProfile_BPMNCollaboration278 if BPMNProfile_BPMNCollaboration278 is not None else set()
        self.BPMNCollaboration = BPMNCollaboration
        self.BPMNProfile_BPMNCollaboration605 = BPMNProfile_BPMNCollaboration605
        
    @property
    def isClosed(self) -> str:
        return self.__isClosed

    @isClosed.setter
    def isClosed(self, isClosed: str):
        self.__isClosed = isClosed

    @property
    def collaboration(self):
        return self.__collaboration

    @collaboration.setter
    def collaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNCollaboration__collaboration", None)
        self.__collaboration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConversationLink"):
                    opp_val = getattr(item, "ConversationLink", None)
                    
                    if opp_val == self:
                        setattr(item, "ConversationLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConversationLink"):
                    opp_val = getattr(item, "ConversationLink", None)
                    
                    setattr(item, "ConversationLink", self)
                    

    @property
    def BPMNProfile_BPMNCollaboration276(self):
        return self.__BPMNProfile_BPMNCollaboration276

    @BPMNProfile_BPMNCollaboration276.setter
    def BPMNProfile_BPMNCollaboration276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNCollaboration__BPMNProfile_BPMNCollaboration276", None)
        self.__BPMNProfile_BPMNCollaboration276 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_CorrelationKey"):
                    opp_val = getattr(item, "BPMNProfile_CorrelationKey", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_CorrelationKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_CorrelationKey"):
                    opp_val = getattr(item, "BPMNProfile_CorrelationKey", None)
                    
                    setattr(item, "BPMNProfile_CorrelationKey", self)
                    

    @property
    def BPMNProfile_BPMNCollaboration272(self):
        return self.__BPMNProfile_BPMNCollaboration272

    @BPMNProfile_BPMNCollaboration272.setter
    def BPMNProfile_BPMNCollaboration272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNCollaboration__BPMNProfile_BPMNCollaboration272", None)
        self.__BPMNProfile_BPMNCollaboration272 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Collaboration"):
                opp_val = getattr(old_value, "BPMNProfile_Collaboration", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Collaboration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Collaboration"):
                opp_val = getattr(value, "BPMNProfile_Collaboration", None)
                setattr(value, "BPMNProfile_Collaboration", self)

    @property
    def BPMNProfile_BPMNCollaboration270(self):
        return self.__BPMNProfile_BPMNCollaboration270

    @BPMNProfile_BPMNCollaboration270.setter
    def BPMNProfile_BPMNCollaboration270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNCollaboration__BPMNProfile_BPMNCollaboration270", None)
        self.__BPMNProfile_BPMNCollaboration270 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_MessageFlow"):
                    opp_val = getattr(item, "BPMNProfile_MessageFlow", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_MessageFlow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_MessageFlow"):
                    opp_val = getattr(item, "BPMNProfile_MessageFlow", None)
                    
                    setattr(item, "BPMNProfile_MessageFlow", self)
                    

    @property
    def BPMNProfile_BPMNCollaboration605(self):
        return self.__BPMNProfile_BPMNCollaboration605

    @BPMNProfile_BPMNCollaboration605.setter
    def BPMNProfile_BPMNCollaboration605(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNCollaboration__BPMNProfile_BPMNCollaboration605", None)
        self.__BPMNProfile_BPMNCollaboration605 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CallConversation604"):
                opp_val = getattr(old_value, "BPMNProfile_CallConversation604", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_CallConversation604", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CallConversation604"):
                opp_val = getattr(value, "BPMNProfile_CallConversation604", None)
                setattr(value, "BPMNProfile_CallConversation604", self)

    @property
    def BPMNProfile_BPMNCollaboration278(self):
        return self.__BPMNProfile_BPMNCollaboration278

    @BPMNProfile_BPMNCollaboration278.setter
    def BPMNProfile_BPMNCollaboration278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNCollaboration__BPMNProfile_BPMNCollaboration278", None)
        self.__BPMNProfile_BPMNCollaboration278 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_Participant"):
                    opp_val = getattr(item, "BPMNProfile_Participant", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_Participant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_Participant"):
                    opp_val = getattr(item, "BPMNProfile_Participant", None)
                    
                    setattr(item, "BPMNProfile_Participant", self)
                    

    @property
    def BPMNProfile_BPMNCollaboration(self):
        return self.__BPMNProfile_BPMNCollaboration

    @BPMNProfile_BPMNCollaboration.setter
    def BPMNProfile_BPMNCollaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNCollaboration__BPMNProfile_BPMNCollaboration", None)
        self.__BPMNProfile_BPMNCollaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNProcess134"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNProcess134", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNProcess134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNProcess134"):
                opp_val = getattr(value, "BPMNProfile_BPMNProcess134", None)
                setattr(value, "BPMNProfile_BPMNProcess134", self)

    @property
    def BPMNCollaboration(self):
        return self.__BPMNCollaboration

    @BPMNCollaboration.setter
    def BPMNCollaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNCollaboration__BPMNCollaboration", None)
        self.__BPMNCollaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conversationLinks"):
                opp_val = getattr(old_value, "conversationLinks", None)
                if opp_val == self:
                    setattr(old_value, "conversationLinks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conversationLinks"):
                opp_val = getattr(value, "conversationLinks", None)
                setattr(value, "conversationLinks", self)

    @property
    def BPMNProfile_BPMNCollaboration268(self):
        return self.__BPMNProfile_BPMNCollaboration268

    @BPMNProfile_BPMNCollaboration268.setter
    def BPMNProfile_BPMNCollaboration268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNCollaboration__BPMNProfile_BPMNCollaboration268", None)
        self.__BPMNProfile_BPMNCollaboration268 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_MessageFlowAssociation"):
                    opp_val = getattr(item, "BPMNProfile_MessageFlowAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_MessageFlowAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_MessageFlowAssociation"):
                    opp_val = getattr(item, "BPMNProfile_MessageFlowAssociation", None)
                    
                    setattr(item, "BPMNProfile_MessageFlowAssociation", self)
                    

    @property
    def BPMNProfile_BPMNCollaboration265(self):
        return self.__BPMNProfile_BPMNCollaboration265

    @BPMNProfile_BPMNCollaboration265.setter
    def BPMNProfile_BPMNCollaboration265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNCollaboration__BPMNProfile_BPMNCollaboration265", None)
        self.__BPMNProfile_BPMNCollaboration265 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_ParticipantAssociation"):
                    opp_val = getattr(item, "BPMNProfile_ParticipantAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_ParticipantAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_ParticipantAssociation"):
                    opp_val = getattr(item, "BPMNProfile_ParticipantAssociation", None)
                    
                    setattr(item, "BPMNProfile_ParticipantAssociation", self)
                    

    @property
    def BPMNProfile_BPMNCollaboration274(self):
        return self.__BPMNProfile_BPMNCollaboration274

    @BPMNProfile_BPMNCollaboration274.setter
    def BPMNProfile_BPMNCollaboration274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNCollaboration__BPMNProfile_BPMNCollaboration274", None)
        self.__BPMNProfile_BPMNCollaboration274 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_ConversationNode"):
                    opp_val = getattr(item, "BPMNProfile_ConversationNode", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_ConversationNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_ConversationNode"):
                    opp_val = getattr(item, "BPMNProfile_ConversationNode", None)
                    
                    setattr(item, "BPMNProfile_ConversationNode", self)
                    

    def Collaborationparticipants(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement Collaborationparticipants method
        pass

class BPMNProfile_PackageImport:

    pass
class BPMNProfile_Import:

    def __init__(self, importType: str, location: str, namespace: str, BPMNProfile_Import: "BPMNProfile_Definitions" = None, BPMNProfile_Import116: "BPMNProfile_PackageImport" = None, BPMNProfile_Import118: "BPMNProfile_Definitions" = None, BPMNProfile_Import194: "BPMNProfile_ItemDefinition" = None):
        self.importType = importType
        self.location = location
        self.namespace = namespace
        self.BPMNProfile_Import = BPMNProfile_Import
        self.BPMNProfile_Import116 = BPMNProfile_Import116
        self.BPMNProfile_Import118 = BPMNProfile_Import118
        self.BPMNProfile_Import194 = BPMNProfile_Import194
        
    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def importType(self) -> str:
        return self.__importType

    @importType.setter
    def importType(self, importType: str):
        self.__importType = importType

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def BPMNProfile_Import194(self):
        return self.__BPMNProfile_Import194

    @BPMNProfile_Import194.setter
    def BPMNProfile_Import194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Import__BPMNProfile_Import194", None)
        self.__BPMNProfile_Import194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ItemDefinition193"):
                opp_val = getattr(old_value, "BPMNProfile_ItemDefinition193", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ItemDefinition193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ItemDefinition193"):
                opp_val = getattr(value, "BPMNProfile_ItemDefinition193", None)
                setattr(value, "BPMNProfile_ItemDefinition193", self)

    @property
    def BPMNProfile_Import(self):
        return self.__BPMNProfile_Import

    @BPMNProfile_Import.setter
    def BPMNProfile_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Import__BPMNProfile_Import", None)
        self.__BPMNProfile_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Definitions105"):
                opp_val = getattr(old_value, "BPMNProfile_Definitions105", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Definitions105"):
                opp_val = getattr(value, "BPMNProfile_Definitions105", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_Definitions105", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_Import118(self):
        return self.__BPMNProfile_Import118

    @BPMNProfile_Import118.setter
    def BPMNProfile_Import118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Import__BPMNProfile_Import118", None)
        self.__BPMNProfile_Import118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Definitions119"):
                opp_val = getattr(old_value, "BPMNProfile_Definitions119", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Definitions119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Definitions119"):
                opp_val = getattr(value, "BPMNProfile_Definitions119", None)
                setattr(value, "BPMNProfile_Definitions119", self)

    @property
    def BPMNProfile_Import116(self):
        return self.__BPMNProfile_Import116

    @BPMNProfile_Import116.setter
    def BPMNProfile_Import116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Import__BPMNProfile_Import116", None)
        self.__BPMNProfile_Import116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_PackageImport"):
                opp_val = getattr(old_value, "BPMNProfile_PackageImport", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_PackageImport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_PackageImport"):
                opp_val = getattr(value, "BPMNProfile_PackageImport", None)
                setattr(value, "BPMNProfile_PackageImport", self)

class BPMNProfile_BPMNExtension:

    def __init__(self, mustUnderstand: str, BPMNProfile_BPMNExtension: "BPMNProfile_Definitions" = None, BPMNProfile_BPMNExtension110: "BPMNProfile_Stereotype" = None, BPMNProfile_BPMNExtension113: "BPMNProfile_ExtensionDefinition" = None):
        self.mustUnderstand = mustUnderstand
        self.BPMNProfile_BPMNExtension = BPMNProfile_BPMNExtension
        self.BPMNProfile_BPMNExtension110 = BPMNProfile_BPMNExtension110
        self.BPMNProfile_BPMNExtension113 = BPMNProfile_BPMNExtension113
        
    @property
    def mustUnderstand(self) -> str:
        return self.__mustUnderstand

    @mustUnderstand.setter
    def mustUnderstand(self, mustUnderstand: str):
        self.__mustUnderstand = mustUnderstand

    @property
    def BPMNProfile_BPMNExtension(self):
        return self.__BPMNProfile_BPMNExtension

    @BPMNProfile_BPMNExtension.setter
    def BPMNProfile_BPMNExtension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNExtension__BPMNProfile_BPMNExtension", None)
        self.__BPMNProfile_BPMNExtension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Definitions103"):
                opp_val = getattr(old_value, "BPMNProfile_Definitions103", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Definitions103"):
                opp_val = getattr(value, "BPMNProfile_Definitions103", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_Definitions103", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_BPMNExtension113(self):
        return self.__BPMNProfile_BPMNExtension113

    @BPMNProfile_BPMNExtension113.setter
    def BPMNProfile_BPMNExtension113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNExtension__BPMNProfile_BPMNExtension113", None)
        self.__BPMNProfile_BPMNExtension113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ExtensionDefinition114"):
                opp_val = getattr(old_value, "BPMNProfile_ExtensionDefinition114", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ExtensionDefinition114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ExtensionDefinition114"):
                opp_val = getattr(value, "BPMNProfile_ExtensionDefinition114", None)
                setattr(value, "BPMNProfile_ExtensionDefinition114", self)

    @property
    def BPMNProfile_BPMNExtension110(self):
        return self.__BPMNProfile_BPMNExtension110

    @BPMNProfile_BPMNExtension110.setter
    def BPMNProfile_BPMNExtension110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNExtension__BPMNProfile_BPMNExtension110", None)
        self.__BPMNProfile_BPMNExtension110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Stereotype111"):
                opp_val = getattr(old_value, "BPMNProfile_Stereotype111", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Stereotype111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Stereotype111"):
                opp_val = getattr(value, "BPMNProfile_Stereotype111", None)
                setattr(value, "BPMNProfile_Stereotype111", self)

class BPMNProfile_Package:

    pass
class BPMNProfile_Constraint:

    pass
class BPMNProfile_InterruptibleActivityRegion:

    pass
class BPMNProfile_StructuredActivityNode:

    pass
class BPMNProfile_PackageableElement:

    pass
class BPMNProfile_MergeNode:

    pass
class BPMNProfile_DecisionNode:

    pass
class BPMNProfile_ControlFlow:

    pass
class BPMNProfile_OpaqueExpression:

    pass
class BPMNProfile_ActivityPartition:

    pass
class BPMNProfile_EnumerationLiteral:

    pass
class BPMNProfile_Class:

    pass
class BPMNProfile_Dependency:

    pass
class BPMNArtifact:

    pass
class BPMNProfile_Group(BPMNArtifact):

    pass
class BPMNProfile_TextAnnotation(BPMNArtifact):

    def __init__(self, textFormat: str, text: str, BPMNProfile_TextAnnotation: "BPMNProfile_Comment" = None):
        self.textFormat = textFormat
        self.text = text
        self.BPMNProfile_TextAnnotation = BPMNProfile_TextAnnotation
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def textFormat(self) -> str:
        return self.__textFormat

    @textFormat.setter
    def textFormat(self, textFormat: str):
        self.__textFormat = textFormat

    @property
    def BPMNProfile_TextAnnotation(self):
        return self.__BPMNProfile_TextAnnotation

    @BPMNProfile_TextAnnotation.setter
    def BPMNProfile_TextAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_TextAnnotation__BPMNProfile_TextAnnotation", None)
        self.__BPMNProfile_TextAnnotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Comment562"):
                opp_val = getattr(old_value, "BPMNProfile_Comment562", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Comment562", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Comment562"):
                opp_val = getattr(value, "BPMNProfile_Comment562", None)
                setattr(value, "BPMNProfile_Comment562", self)

class BPMNProfile_Stereotype:

    pass
class Gateway:

    pass
class BPMNProfile_EventBasedGateway(Gateway):

    def __init__(self, instantiate: str, eventGatewayType: str, BPMNProfile_EventBasedGateway: "BPMNProfile_ForkNode" = None, BPMNProfile_EventBasedGateway85: "BPMNProfile_StructuredActivityNode" = None, BPMNProfile_EventBasedGateway87: "BPMNProfile_InterruptibleActivityRegion" = None):
        self.instantiate = instantiate
        self.eventGatewayType = eventGatewayType
        self.BPMNProfile_EventBasedGateway = BPMNProfile_EventBasedGateway
        self.BPMNProfile_EventBasedGateway85 = BPMNProfile_EventBasedGateway85
        self.BPMNProfile_EventBasedGateway87 = BPMNProfile_EventBasedGateway87
        
    @property
    def instantiate(self) -> str:
        return self.__instantiate

    @instantiate.setter
    def instantiate(self, instantiate: str):
        self.__instantiate = instantiate

    @property
    def eventGatewayType(self) -> str:
        return self.__eventGatewayType

    @eventGatewayType.setter
    def eventGatewayType(self, eventGatewayType: str):
        self.__eventGatewayType = eventGatewayType

    @property
    def BPMNProfile_EventBasedGateway87(self):
        return self.__BPMNProfile_EventBasedGateway87

    @BPMNProfile_EventBasedGateway87.setter
    def BPMNProfile_EventBasedGateway87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_EventBasedGateway__BPMNProfile_EventBasedGateway87", None)
        self.__BPMNProfile_EventBasedGateway87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_InterruptibleActivityRegion"):
                opp_val = getattr(old_value, "BPMNProfile_InterruptibleActivityRegion", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_InterruptibleActivityRegion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_InterruptibleActivityRegion"):
                opp_val = getattr(value, "BPMNProfile_InterruptibleActivityRegion", None)
                setattr(value, "BPMNProfile_InterruptibleActivityRegion", self)

    @property
    def BPMNProfile_EventBasedGateway85(self):
        return self.__BPMNProfile_EventBasedGateway85

    @BPMNProfile_EventBasedGateway85.setter
    def BPMNProfile_EventBasedGateway85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_EventBasedGateway__BPMNProfile_EventBasedGateway85", None)
        self.__BPMNProfile_EventBasedGateway85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_StructuredActivityNode"):
                opp_val = getattr(old_value, "BPMNProfile_StructuredActivityNode", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_StructuredActivityNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_StructuredActivityNode"):
                opp_val = getattr(value, "BPMNProfile_StructuredActivityNode", None)
                setattr(value, "BPMNProfile_StructuredActivityNode", self)

    @property
    def BPMNProfile_EventBasedGateway(self):
        return self.__BPMNProfile_EventBasedGateway

    @BPMNProfile_EventBasedGateway.setter
    def BPMNProfile_EventBasedGateway(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_EventBasedGateway__BPMNProfile_EventBasedGateway", None)
        self.__BPMNProfile_EventBasedGateway = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ForkNode83"):
                opp_val = getattr(old_value, "BPMNProfile_ForkNode83", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ForkNode83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ForkNode83"):
                opp_val = getattr(value, "BPMNProfile_ForkNode83", None)
                setattr(value, "BPMNProfile_ForkNode83", self)

class BPMNProfile_ExclusiveGateway(Gateway):

    def __init__(self, BPMNProfile_ExclusiveGateway: "BPMNProfile_DecisionNode" = None, BPMNProfile_ExclusiveGateway95: "BPMNProfile_MergeNode" = None, BPMNProfile_ExclusiveGateway97: "BPMNProfile_SequenceFlow" = None):
        self.BPMNProfile_ExclusiveGateway = BPMNProfile_ExclusiveGateway
        self.BPMNProfile_ExclusiveGateway95 = BPMNProfile_ExclusiveGateway95
        self.BPMNProfile_ExclusiveGateway97 = BPMNProfile_ExclusiveGateway97
        
    @property
    def BPMNProfile_ExclusiveGateway95(self):
        return self.__BPMNProfile_ExclusiveGateway95

    @BPMNProfile_ExclusiveGateway95.setter
    def BPMNProfile_ExclusiveGateway95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ExclusiveGateway__BPMNProfile_ExclusiveGateway95", None)
        self.__BPMNProfile_ExclusiveGateway95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_MergeNode"):
                opp_val = getattr(old_value, "BPMNProfile_MergeNode", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_MergeNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_MergeNode"):
                opp_val = getattr(value, "BPMNProfile_MergeNode", None)
                setattr(value, "BPMNProfile_MergeNode", self)

    @property
    def BPMNProfile_ExclusiveGateway(self):
        return self.__BPMNProfile_ExclusiveGateway

    @BPMNProfile_ExclusiveGateway.setter
    def BPMNProfile_ExclusiveGateway(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ExclusiveGateway__BPMNProfile_ExclusiveGateway", None)
        self.__BPMNProfile_ExclusiveGateway = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_DecisionNode"):
                opp_val = getattr(old_value, "BPMNProfile_DecisionNode", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_DecisionNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_DecisionNode"):
                opp_val = getattr(value, "BPMNProfile_DecisionNode", None)
                setattr(value, "BPMNProfile_DecisionNode", self)

    @property
    def BPMNProfile_ExclusiveGateway97(self):
        return self.__BPMNProfile_ExclusiveGateway97

    @BPMNProfile_ExclusiveGateway97.setter
    def BPMNProfile_ExclusiveGateway97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ExclusiveGateway__BPMNProfile_ExclusiveGateway97", None)
        self.__BPMNProfile_ExclusiveGateway97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_SequenceFlow98"):
                opp_val = getattr(old_value, "BPMNProfile_SequenceFlow98", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_SequenceFlow98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_SequenceFlow98"):
                opp_val = getattr(value, "BPMNProfile_SequenceFlow98", None)
                setattr(value, "BPMNProfile_SequenceFlow98", self)

    def exclusiveGatewaydefault(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement exclusiveGatewaydefault method
        pass

class BPMNProfile_NonExclusiveGateway(Gateway):

    pass
class BPMNProfile_Property:

    pass
class BPMNProfile_ExtensionAttributeDefinition:

    def __init__(self, type: str, isReference: str, BPMNProfile_ExtensionAttributeDefinition: "BPMNProfile_ExtensionAttributeValue" = None, BPMNProfile_ExtensionAttributeDefinition31: "BPMNProfile_Property" = None, BPMNProfile_ExtensionAttributeDefinition38: "BPMNProfile_ExtensionDefinition" = None):
        self.type = type
        self.isReference = isReference
        self.BPMNProfile_ExtensionAttributeDefinition = BPMNProfile_ExtensionAttributeDefinition
        self.BPMNProfile_ExtensionAttributeDefinition31 = BPMNProfile_ExtensionAttributeDefinition31
        self.BPMNProfile_ExtensionAttributeDefinition38 = BPMNProfile_ExtensionAttributeDefinition38
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def isReference(self) -> str:
        return self.__isReference

    @isReference.setter
    def isReference(self, isReference: str):
        self.__isReference = isReference

    @property
    def BPMNProfile_ExtensionAttributeDefinition31(self):
        return self.__BPMNProfile_ExtensionAttributeDefinition31

    @BPMNProfile_ExtensionAttributeDefinition31.setter
    def BPMNProfile_ExtensionAttributeDefinition31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ExtensionAttributeDefinition__BPMNProfile_ExtensionAttributeDefinition31", None)
        self.__BPMNProfile_ExtensionAttributeDefinition31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Property"):
                opp_val = getattr(old_value, "BPMNProfile_Property", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Property", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Property"):
                opp_val = getattr(value, "BPMNProfile_Property", None)
                setattr(value, "BPMNProfile_Property", self)

    @property
    def BPMNProfile_ExtensionAttributeDefinition(self):
        return self.__BPMNProfile_ExtensionAttributeDefinition

    @BPMNProfile_ExtensionAttributeDefinition.setter
    def BPMNProfile_ExtensionAttributeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ExtensionAttributeDefinition__BPMNProfile_ExtensionAttributeDefinition", None)
        self.__BPMNProfile_ExtensionAttributeDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ExtensionAttributeValue29"):
                opp_val = getattr(old_value, "BPMNProfile_ExtensionAttributeValue29", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ExtensionAttributeValue29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ExtensionAttributeValue29"):
                opp_val = getattr(value, "BPMNProfile_ExtensionAttributeValue29", None)
                setattr(value, "BPMNProfile_ExtensionAttributeValue29", self)

    @property
    def BPMNProfile_ExtensionAttributeDefinition38(self):
        return self.__BPMNProfile_ExtensionAttributeDefinition38

    @BPMNProfile_ExtensionAttributeDefinition38.setter
    def BPMNProfile_ExtensionAttributeDefinition38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ExtensionAttributeDefinition__BPMNProfile_ExtensionAttributeDefinition38", None)
        self.__BPMNProfile_ExtensionAttributeDefinition38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ExtensionDefinition37"):
                opp_val = getattr(old_value, "BPMNProfile_ExtensionDefinition37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ExtensionDefinition37"):
                opp_val = getattr(value, "BPMNProfile_ExtensionDefinition37", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_ExtensionDefinition37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMNProfile_Slot:

    pass
class BPMNProfile_BPMNAssociation(BPMNArtifact):

    def __init__(self, associationDirection: str, BPMNAssociation: "BPMNProfile_BaseElement" = None, BPMNAssociation22: "BPMNProfile_BaseElement" = None, BPMNProfile_BPMNAssociation: "BPMNProfile_Dependency" = None, incoming: "BPMNProfile_BaseElement" = None, outgoing: "BPMNProfile_BaseElement" = None):
        self.associationDirection = associationDirection
        self.BPMNAssociation = BPMNAssociation
        self.BPMNAssociation22 = BPMNAssociation22
        self.BPMNProfile_BPMNAssociation = BPMNProfile_BPMNAssociation
        self.incoming = incoming
        self.outgoing = outgoing
        
    @property
    def associationDirection(self) -> str:
        return self.__associationDirection

    @associationDirection.setter
    def associationDirection(self, associationDirection: str):
        self.__associationDirection = associationDirection

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNAssociation__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BaseElement"):
                opp_val = getattr(old_value, "BaseElement", None)
                if opp_val == self:
                    setattr(old_value, "BaseElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BaseElement"):
                opp_val = getattr(value, "BaseElement", None)
                setattr(value, "BaseElement", self)

    @property
    def BPMNAssociation22(self):
        return self.__BPMNAssociation22

    @BPMNAssociation22.setter
    def BPMNAssociation22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNAssociation__BPMNAssociation22", None)
        self.__BPMNAssociation22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "targetRef"):
                opp_val = getattr(old_value, "targetRef", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "targetRef"):
                opp_val = getattr(value, "targetRef", None)
                if opp_val is None:
                    setattr(value, "targetRef", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNAssociation(self):
        return self.__BPMNAssociation

    @BPMNAssociation.setter
    def BPMNAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNAssociation__BPMNAssociation", None)
        self.__BPMNAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourceRef"):
                opp_val = getattr(old_value, "sourceRef", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourceRef"):
                opp_val = getattr(value, "sourceRef", None)
                if opp_val is None:
                    setattr(value, "sourceRef", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_BPMNAssociation(self):
        return self.__BPMNProfile_BPMNAssociation

    @BPMNProfile_BPMNAssociation.setter
    def BPMNProfile_BPMNAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNAssociation__BPMNProfile_BPMNAssociation", None)
        self.__BPMNProfile_BPMNAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Dependency"):
                opp_val = getattr(old_value, "BPMNProfile_Dependency", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Dependency", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Dependency"):
                opp_val = getattr(value, "BPMNProfile_Dependency", None)
                setattr(value, "BPMNProfile_Dependency", self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNAssociation__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BaseElement42"):
                opp_val = getattr(old_value, "BaseElement42", None)
                if opp_val == self:
                    setattr(old_value, "BaseElement42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BaseElement42"):
                opp_val = getattr(value, "BaseElement42", None)
                setattr(value, "BaseElement42", self)

    def AssociationEnd(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AssociationEnd method
        pass

class NonExclusiveGateway:

    pass
class BPMNProfile_ParallelGateway(NonExclusiveGateway):

    pass
class BPMNProfile_ComplexGateway(NonExclusiveGateway):

    def __init__(self, BPMNProfile_ComplexGateway: "BPMNProfile_SequenceFlow" = None, BPMNProfile_ComplexGateway91: "BPMNProfile_BPMNExpression" = None):
        self.BPMNProfile_ComplexGateway = BPMNProfile_ComplexGateway
        self.BPMNProfile_ComplexGateway91 = BPMNProfile_ComplexGateway91
        
    @property
    def BPMNProfile_ComplexGateway(self):
        return self.__BPMNProfile_ComplexGateway

    @BPMNProfile_ComplexGateway.setter
    def BPMNProfile_ComplexGateway(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ComplexGateway__BPMNProfile_ComplexGateway", None)
        self.__BPMNProfile_ComplexGateway = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_SequenceFlow89"):
                opp_val = getattr(old_value, "BPMNProfile_SequenceFlow89", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_SequenceFlow89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_SequenceFlow89"):
                opp_val = getattr(value, "BPMNProfile_SequenceFlow89", None)
                setattr(value, "BPMNProfile_SequenceFlow89", self)

    @property
    def BPMNProfile_ComplexGateway91(self):
        return self.__BPMNProfile_ComplexGateway91

    @BPMNProfile_ComplexGateway91.setter
    def BPMNProfile_ComplexGateway91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ComplexGateway__BPMNProfile_ComplexGateway91", None)
        self.__BPMNProfile_ComplexGateway91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNExpression92"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNExpression92", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNExpression92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNExpression92"):
                opp_val = getattr(value, "BPMNProfile_BPMNExpression92", None)
                setattr(value, "BPMNProfile_BPMNExpression92", self)

    def complexGatewayjoinSpec(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement complexGatewayjoinSpec method
        pass

    def complexGatewaydefault(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement complexGatewaydefault method
        pass

    def complexGatewayactivationCondition(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement complexGatewayactivationCondition method
        pass

class BPMNProfile_ExtensionDefinition:

    pass
class BPMNProfile_InclusiveGateway(NonExclusiveGateway):

    def __init__(self, BPMNProfile_InclusiveGateway: "BPMNProfile_SequenceFlow" = None):
        self.BPMNProfile_InclusiveGateway = BPMNProfile_InclusiveGateway
        
    @property
    def BPMNProfile_InclusiveGateway(self):
        return self.__BPMNProfile_InclusiveGateway

    @BPMNProfile_InclusiveGateway.setter
    def BPMNProfile_InclusiveGateway(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_InclusiveGateway__BPMNProfile_InclusiveGateway", None)
        self.__BPMNProfile_InclusiveGateway = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_SequenceFlow"):
                opp_val = getattr(old_value, "BPMNProfile_SequenceFlow", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_SequenceFlow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_SequenceFlow"):
                opp_val = getattr(value, "BPMNProfile_SequenceFlow", None)
                setattr(value, "BPMNProfile_SequenceFlow", self)

    def inclusiveGatewaydefault(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement inclusiveGatewaydefault method
        pass

class BPMNProfile_Element:

    pass
class BPMNProfile_ExtensionAttributeValue:

    pass
class BPMNProfile_BaseElement(ABC):

    def __init__(self, id: str, BPMNProfile_BaseElement: set["BPMNProfile_ExtensionAttributeValue"] = None, BPMNProfile_BaseElement15: "BPMNProfile_Element" = None, BPMNProfile_BaseElement17: set["BPMNProfile_Documentation"] = None, BPMNProfile_BaseElement19: set["BPMNProfile_ExtensionDefinition"] = None, sourceRef: set["BPMNProfile_BPMNAssociation"] = None, targetRef: set["BPMNProfile_BPMNAssociation"] = None, BaseElement: "BPMNProfile_BPMNAssociation" = None, BaseElement42: "BPMNProfile_BPMNAssociation" = None, BPMNProfile_BaseElement70: "BPMNProfile_Lane" = None):
        self.id = id
        self.BPMNProfile_BaseElement = BPMNProfile_BaseElement if BPMNProfile_BaseElement is not None else set()
        self.BPMNProfile_BaseElement15 = BPMNProfile_BaseElement15
        self.BPMNProfile_BaseElement17 = BPMNProfile_BaseElement17 if BPMNProfile_BaseElement17 is not None else set()
        self.BPMNProfile_BaseElement19 = BPMNProfile_BaseElement19 if BPMNProfile_BaseElement19 is not None else set()
        self.sourceRef = sourceRef if sourceRef is not None else set()
        self.targetRef = targetRef if targetRef is not None else set()
        self.BaseElement = BaseElement
        self.BaseElement42 = BaseElement42
        self.BPMNProfile_BaseElement70 = BPMNProfile_BaseElement70
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def BPMNProfile_BaseElement19(self):
        return self.__BPMNProfile_BaseElement19

    @BPMNProfile_BaseElement19.setter
    def BPMNProfile_BaseElement19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BaseElement__BPMNProfile_BaseElement19", None)
        self.__BPMNProfile_BaseElement19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_ExtensionDefinition"):
                    opp_val = getattr(item, "BPMNProfile_ExtensionDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_ExtensionDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_ExtensionDefinition"):
                    opp_val = getattr(item, "BPMNProfile_ExtensionDefinition", None)
                    
                    setattr(item, "BPMNProfile_ExtensionDefinition", self)
                    

    @property
    def BPMNProfile_BaseElement70(self):
        return self.__BPMNProfile_BaseElement70

    @BPMNProfile_BaseElement70.setter
    def BPMNProfile_BaseElement70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BaseElement__BPMNProfile_BaseElement70", None)
        self.__BPMNProfile_BaseElement70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Lane69"):
                opp_val = getattr(old_value, "BPMNProfile_Lane69", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Lane69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Lane69"):
                opp_val = getattr(value, "BPMNProfile_Lane69", None)
                setattr(value, "BPMNProfile_Lane69", self)

    @property
    def sourceRef(self):
        return self.__sourceRef

    @sourceRef.setter
    def sourceRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BaseElement__sourceRef", None)
        self.__sourceRef = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNAssociation"):
                    opp_val = getattr(item, "BPMNAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNAssociation"):
                    opp_val = getattr(item, "BPMNAssociation", None)
                    
                    setattr(item, "BPMNAssociation", self)
                    

    @property
    def BaseElement42(self):
        return self.__BaseElement42

    @BaseElement42.setter
    def BaseElement42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BaseElement__BaseElement42", None)
        self.__BaseElement42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

    @property
    def targetRef(self):
        return self.__targetRef

    @targetRef.setter
    def targetRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BaseElement__targetRef", None)
        self.__targetRef = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNAssociation22"):
                    opp_val = getattr(item, "BPMNAssociation22", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNAssociation22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNAssociation22"):
                    opp_val = getattr(item, "BPMNAssociation22", None)
                    
                    setattr(item, "BPMNAssociation22", self)
                    

    @property
    def BPMNProfile_BaseElement15(self):
        return self.__BPMNProfile_BaseElement15

    @BPMNProfile_BaseElement15.setter
    def BPMNProfile_BaseElement15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BaseElement__BPMNProfile_BaseElement15", None)
        self.__BPMNProfile_BaseElement15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Element"):
                opp_val = getattr(old_value, "BPMNProfile_Element", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Element", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Element"):
                opp_val = getattr(value, "BPMNProfile_Element", None)
                setattr(value, "BPMNProfile_Element", self)

    @property
    def BPMNProfile_BaseElement(self):
        return self.__BPMNProfile_BaseElement

    @BPMNProfile_BaseElement.setter
    def BPMNProfile_BaseElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BaseElement__BPMNProfile_BaseElement", None)
        self.__BPMNProfile_BaseElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_ExtensionAttributeValue"):
                    opp_val = getattr(item, "BPMNProfile_ExtensionAttributeValue", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_ExtensionAttributeValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_ExtensionAttributeValue"):
                    opp_val = getattr(item, "BPMNProfile_ExtensionAttributeValue", None)
                    
                    setattr(item, "BPMNProfile_ExtensionAttributeValue", self)
                    

    @property
    def BPMNProfile_BaseElement17(self):
        return self.__BPMNProfile_BaseElement17

    @BPMNProfile_BaseElement17.setter
    def BPMNProfile_BaseElement17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BaseElement__BPMNProfile_BaseElement17", None)
        self.__BPMNProfile_BaseElement17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_Documentation"):
                    opp_val = getattr(item, "BPMNProfile_Documentation", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_Documentation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_Documentation"):
                    opp_val = getattr(item, "BPMNProfile_Documentation", None)
                    
                    setattr(item, "BPMNProfile_Documentation", self)
                    

    @property
    def BaseElement(self):
        return self.__BaseElement

    @BaseElement.setter
    def BaseElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BaseElement__BaseElement", None)
        self.__BaseElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if opp_val == self:
                    setattr(old_value, "incoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                setattr(value, "incoming", self)

class BaseElement:

    pass
class BPMNProfile_LaneSet(BaseElement):

    def __init__(self, LaneSet: "BPMNProfile_FlowElementsContainer" = None, BPMNProfile_LaneSet: "BPMNProfile_ActivityPartition" = None, laneSet: set["BPMNProfile_Lane"] = None, BPMNProfile_LaneSet56: set["BPMNProfile_Lane"] = None, laneSets: "BPMNProfile_FlowElementsContainer" = None, BPMNProfile_LaneSet73: "BPMNProfile_Lane" = None, LaneSet75: "BPMNProfile_Lane" = None, BPMNProfile_LaneSet613: "BPMNProfile_SubProcess" = None):
        self.LaneSet = LaneSet
        self.BPMNProfile_LaneSet = BPMNProfile_LaneSet
        self.laneSet = laneSet if laneSet is not None else set()
        self.BPMNProfile_LaneSet56 = BPMNProfile_LaneSet56 if BPMNProfile_LaneSet56 is not None else set()
        self.laneSets = laneSets
        self.BPMNProfile_LaneSet73 = BPMNProfile_LaneSet73
        self.LaneSet75 = LaneSet75
        self.BPMNProfile_LaneSet613 = BPMNProfile_LaneSet613
        
    @property
    def laneSet(self):
        return self.__laneSet

    @laneSet.setter
    def laneSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_LaneSet__laneSet", None)
        self.__laneSet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Lane"):
                    opp_val = getattr(item, "Lane", None)
                    
                    if opp_val == self:
                        setattr(item, "Lane", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Lane"):
                    opp_val = getattr(item, "Lane", None)
                    
                    setattr(item, "Lane", self)
                    

    @property
    def LaneSet(self):
        return self.__LaneSet

    @LaneSet.setter
    def LaneSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_LaneSet__LaneSet", None)
        self.__LaneSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flowElementsContainer"):
                opp_val = getattr(old_value, "flowElementsContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flowElementsContainer"):
                opp_val = getattr(value, "flowElementsContainer", None)
                if opp_val is None:
                    setattr(value, "flowElementsContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_LaneSet73(self):
        return self.__BPMNProfile_LaneSet73

    @BPMNProfile_LaneSet73.setter
    def BPMNProfile_LaneSet73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_LaneSet__BPMNProfile_LaneSet73", None)
        self.__BPMNProfile_LaneSet73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Lane72"):
                opp_val = getattr(old_value, "BPMNProfile_Lane72", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Lane72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Lane72"):
                opp_val = getattr(value, "BPMNProfile_Lane72", None)
                setattr(value, "BPMNProfile_Lane72", self)

    @property
    def BPMNProfile_LaneSet(self):
        return self.__BPMNProfile_LaneSet

    @BPMNProfile_LaneSet.setter
    def BPMNProfile_LaneSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_LaneSet__BPMNProfile_LaneSet", None)
        self.__BPMNProfile_LaneSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ActivityPartition"):
                opp_val = getattr(old_value, "BPMNProfile_ActivityPartition", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ActivityPartition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ActivityPartition"):
                opp_val = getattr(value, "BPMNProfile_ActivityPartition", None)
                setattr(value, "BPMNProfile_ActivityPartition", self)

    @property
    def BPMNProfile_LaneSet613(self):
        return self.__BPMNProfile_LaneSet613

    @BPMNProfile_LaneSet613.setter
    def BPMNProfile_LaneSet613(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_LaneSet__BPMNProfile_LaneSet613", None)
        self.__BPMNProfile_LaneSet613 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_SubProcess612"):
                opp_val = getattr(old_value, "BPMNProfile_SubProcess612", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_SubProcess612"):
                opp_val = getattr(value, "BPMNProfile_SubProcess612", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_SubProcess612", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def LaneSet75(self):
        return self.__LaneSet75

    @LaneSet75.setter
    def LaneSet75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_LaneSet__LaneSet75", None)
        self.__LaneSet75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lanes"):
                opp_val = getattr(old_value, "lanes", None)
                if opp_val == self:
                    setattr(old_value, "lanes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lanes"):
                opp_val = getattr(value, "lanes", None)
                setattr(value, "lanes", self)

    @property
    def BPMNProfile_LaneSet56(self):
        return self.__BPMNProfile_LaneSet56

    @BPMNProfile_LaneSet56.setter
    def BPMNProfile_LaneSet56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_LaneSet__BPMNProfile_LaneSet56", None)
        self.__BPMNProfile_LaneSet56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_Lane"):
                    opp_val = getattr(item, "BPMNProfile_Lane", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_Lane", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_Lane"):
                    opp_val = getattr(item, "BPMNProfile_Lane", None)
                    
                    setattr(item, "BPMNProfile_Lane", self)
                    

    @property
    def laneSets(self):
        return self.__laneSets

    @laneSets.setter
    def laneSets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_LaneSet__laneSets", None)
        self.__laneSets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FlowElementsContainer58"):
                opp_val = getattr(old_value, "FlowElementsContainer58", None)
                if opp_val == self:
                    setattr(old_value, "FlowElementsContainer58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FlowElementsContainer58"):
                opp_val = getattr(value, "FlowElementsContainer58", None)
                setattr(value, "FlowElementsContainer58", self)

    def LaneSet(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement LaneSet method
        pass

    def LaneSetflowElementsContainer(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement LaneSetflowElementsContainer method
        pass

    def LaneSetparentLane(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement LaneSetparentLane method
        pass

    def LaneSetlanes(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement LaneSetlanes method
        pass

class BPMNProfile_ConversationLink(BaseElement):

    pass
class BPMNProfile_BPMNArtifact(BaseElement):

    pass
class BPMNProfile_ResourceParameter(BaseElement):

    def __init__(self, isRequired: str, BPMNProfile_ResourceParameter: "BPMNProfile_Resource" = None, BPMNProfile_ResourceParameter417: "BPMNProfile_Property" = None, BPMNProfile_ResourceParameter420: "BPMNProfile_ItemDefinition" = None, BPMNProfile_ResourceParameter427: "BPMNProfile_ResourceParameterBinding" = None):
        self.isRequired = isRequired
        self.BPMNProfile_ResourceParameter = BPMNProfile_ResourceParameter
        self.BPMNProfile_ResourceParameter417 = BPMNProfile_ResourceParameter417
        self.BPMNProfile_ResourceParameter420 = BPMNProfile_ResourceParameter420
        self.BPMNProfile_ResourceParameter427 = BPMNProfile_ResourceParameter427
        
    @property
    def isRequired(self) -> str:
        return self.__isRequired

    @isRequired.setter
    def isRequired(self, isRequired: str):
        self.__isRequired = isRequired

    @property
    def BPMNProfile_ResourceParameter417(self):
        return self.__BPMNProfile_ResourceParameter417

    @BPMNProfile_ResourceParameter417.setter
    def BPMNProfile_ResourceParameter417(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceParameter__BPMNProfile_ResourceParameter417", None)
        self.__BPMNProfile_ResourceParameter417 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Property418"):
                opp_val = getattr(old_value, "BPMNProfile_Property418", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Property418", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Property418"):
                opp_val = getattr(value, "BPMNProfile_Property418", None)
                setattr(value, "BPMNProfile_Property418", self)

    @property
    def BPMNProfile_ResourceParameter420(self):
        return self.__BPMNProfile_ResourceParameter420

    @BPMNProfile_ResourceParameter420.setter
    def BPMNProfile_ResourceParameter420(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceParameter__BPMNProfile_ResourceParameter420", None)
        self.__BPMNProfile_ResourceParameter420 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ItemDefinition421"):
                opp_val = getattr(old_value, "BPMNProfile_ItemDefinition421", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ItemDefinition421", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ItemDefinition421"):
                opp_val = getattr(value, "BPMNProfile_ItemDefinition421", None)
                setattr(value, "BPMNProfile_ItemDefinition421", self)

    @property
    def BPMNProfile_ResourceParameter(self):
        return self.__BPMNProfile_ResourceParameter

    @BPMNProfile_ResourceParameter.setter
    def BPMNProfile_ResourceParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceParameter__BPMNProfile_ResourceParameter", None)
        self.__BPMNProfile_ResourceParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Resource415"):
                opp_val = getattr(old_value, "BPMNProfile_Resource415", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Resource415"):
                opp_val = getattr(value, "BPMNProfile_Resource415", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_Resource415", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_ResourceParameter427(self):
        return self.__BPMNProfile_ResourceParameter427

    @BPMNProfile_ResourceParameter427.setter
    def BPMNProfile_ResourceParameter427(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceParameter__BPMNProfile_ResourceParameter427", None)
        self.__BPMNProfile_ResourceParameter427 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ResourceParameterBinding426"):
                opp_val = getattr(old_value, "BPMNProfile_ResourceParameterBinding426", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ResourceParameterBinding426", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ResourceParameterBinding426"):
                opp_val = getattr(value, "BPMNProfile_ResourceParameterBinding426", None)
                setattr(value, "BPMNProfile_ResourceParameterBinding426", self)

    def ResourceParametertype(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ResourceParametertype method
        pass

    def ResourceParameterowner(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceParameterowner method
        pass

    def ResourceParameterisRequired(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceParameterisRequired method
        pass

class BPMNProfile_Monitoring(BaseElement):

    pass
class BPMNProfile_LoopCharacteristics(BaseElement):

    pass
class BPMNProfile_BPMNOperation(BaseElement):

    def __init__(self, BPMNProfile_BPMNOperation: "BPMNProfile_BPMNInterface" = None, BPMNProfile_BPMNOperation238: "BPMNProfile_Operation" = None, BPMNProfile_BPMNOperation240: "BPMNProfile_Element" = None, BPMNProfile_BPMNOperation243: "BPMNProfile_BPMNMessage" = None, BPMNProfile_BPMNOperation245: "BPMNProfile_BPMNMessage" = None, BPMNProfile_BPMNOperation248: set["BPMNProfile_Error"] = None, BPMNProfile_BPMNOperation260: "BPMNProfile_InputOutputBinding" = None, BPMNProfile_BPMNOperation535: "BPMNProfile_MessageEventDefinition" = None, BPMNProfile_BPMNOperation650: "BPMNProfile_ReceiveTask" = None, BPMNProfile_BPMNOperation638: "BPMNProfile_SendTask" = None, BPMNProfile_BPMNOperation655: "BPMNProfile_ServiceTask" = None):
        self.BPMNProfile_BPMNOperation = BPMNProfile_BPMNOperation
        self.BPMNProfile_BPMNOperation238 = BPMNProfile_BPMNOperation238
        self.BPMNProfile_BPMNOperation240 = BPMNProfile_BPMNOperation240
        self.BPMNProfile_BPMNOperation243 = BPMNProfile_BPMNOperation243
        self.BPMNProfile_BPMNOperation245 = BPMNProfile_BPMNOperation245
        self.BPMNProfile_BPMNOperation248 = BPMNProfile_BPMNOperation248 if BPMNProfile_BPMNOperation248 is not None else set()
        self.BPMNProfile_BPMNOperation260 = BPMNProfile_BPMNOperation260
        self.BPMNProfile_BPMNOperation535 = BPMNProfile_BPMNOperation535
        self.BPMNProfile_BPMNOperation650 = BPMNProfile_BPMNOperation650
        self.BPMNProfile_BPMNOperation638 = BPMNProfile_BPMNOperation638
        self.BPMNProfile_BPMNOperation655 = BPMNProfile_BPMNOperation655
        
    @property
    def BPMNProfile_BPMNOperation638(self):
        return self.__BPMNProfile_BPMNOperation638

    @BPMNProfile_BPMNOperation638.setter
    def BPMNProfile_BPMNOperation638(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNOperation__BPMNProfile_BPMNOperation638", None)
        self.__BPMNProfile_BPMNOperation638 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_SendTask637"):
                opp_val = getattr(old_value, "BPMNProfile_SendTask637", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_SendTask637", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_SendTask637"):
                opp_val = getattr(value, "BPMNProfile_SendTask637", None)
                setattr(value, "BPMNProfile_SendTask637", self)

    @property
    def BPMNProfile_BPMNOperation248(self):
        return self.__BPMNProfile_BPMNOperation248

    @BPMNProfile_BPMNOperation248.setter
    def BPMNProfile_BPMNOperation248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNOperation__BPMNProfile_BPMNOperation248", None)
        self.__BPMNProfile_BPMNOperation248 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_Error"):
                    opp_val = getattr(item, "BPMNProfile_Error", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_Error", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_Error"):
                    opp_val = getattr(item, "BPMNProfile_Error", None)
                    
                    setattr(item, "BPMNProfile_Error", self)
                    

    @property
    def BPMNProfile_BPMNOperation260(self):
        return self.__BPMNProfile_BPMNOperation260

    @BPMNProfile_BPMNOperation260.setter
    def BPMNProfile_BPMNOperation260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNOperation__BPMNProfile_BPMNOperation260", None)
        self.__BPMNProfile_BPMNOperation260 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_InputOutputBinding259"):
                opp_val = getattr(old_value, "BPMNProfile_InputOutputBinding259", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_InputOutputBinding259", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_InputOutputBinding259"):
                opp_val = getattr(value, "BPMNProfile_InputOutputBinding259", None)
                setattr(value, "BPMNProfile_InputOutputBinding259", self)

    @property
    def BPMNProfile_BPMNOperation243(self):
        return self.__BPMNProfile_BPMNOperation243

    @BPMNProfile_BPMNOperation243.setter
    def BPMNProfile_BPMNOperation243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNOperation__BPMNProfile_BPMNOperation243", None)
        self.__BPMNProfile_BPMNOperation243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNMessage"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNMessage", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNMessage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNMessage"):
                opp_val = getattr(value, "BPMNProfile_BPMNMessage", None)
                setattr(value, "BPMNProfile_BPMNMessage", self)

    @property
    def BPMNProfile_BPMNOperation245(self):
        return self.__BPMNProfile_BPMNOperation245

    @BPMNProfile_BPMNOperation245.setter
    def BPMNProfile_BPMNOperation245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNOperation__BPMNProfile_BPMNOperation245", None)
        self.__BPMNProfile_BPMNOperation245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNMessage246"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNMessage246", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNMessage246", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNMessage246"):
                opp_val = getattr(value, "BPMNProfile_BPMNMessage246", None)
                setattr(value, "BPMNProfile_BPMNMessage246", self)

    @property
    def BPMNProfile_BPMNOperation240(self):
        return self.__BPMNProfile_BPMNOperation240

    @BPMNProfile_BPMNOperation240.setter
    def BPMNProfile_BPMNOperation240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNOperation__BPMNProfile_BPMNOperation240", None)
        self.__BPMNProfile_BPMNOperation240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Element241"):
                opp_val = getattr(old_value, "BPMNProfile_Element241", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Element241", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Element241"):
                opp_val = getattr(value, "BPMNProfile_Element241", None)
                setattr(value, "BPMNProfile_Element241", self)

    @property
    def BPMNProfile_BPMNOperation535(self):
        return self.__BPMNProfile_BPMNOperation535

    @BPMNProfile_BPMNOperation535.setter
    def BPMNProfile_BPMNOperation535(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNOperation__BPMNProfile_BPMNOperation535", None)
        self.__BPMNProfile_BPMNOperation535 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_MessageEventDefinition534"):
                opp_val = getattr(old_value, "BPMNProfile_MessageEventDefinition534", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_MessageEventDefinition534", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_MessageEventDefinition534"):
                opp_val = getattr(value, "BPMNProfile_MessageEventDefinition534", None)
                setattr(value, "BPMNProfile_MessageEventDefinition534", self)

    @property
    def BPMNProfile_BPMNOperation650(self):
        return self.__BPMNProfile_BPMNOperation650

    @BPMNProfile_BPMNOperation650.setter
    def BPMNProfile_BPMNOperation650(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNOperation__BPMNProfile_BPMNOperation650", None)
        self.__BPMNProfile_BPMNOperation650 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ReceiveTask649"):
                opp_val = getattr(old_value, "BPMNProfile_ReceiveTask649", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ReceiveTask649", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ReceiveTask649"):
                opp_val = getattr(value, "BPMNProfile_ReceiveTask649", None)
                setattr(value, "BPMNProfile_ReceiveTask649", self)

    @property
    def BPMNProfile_BPMNOperation655(self):
        return self.__BPMNProfile_BPMNOperation655

    @BPMNProfile_BPMNOperation655.setter
    def BPMNProfile_BPMNOperation655(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNOperation__BPMNProfile_BPMNOperation655", None)
        self.__BPMNProfile_BPMNOperation655 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ServiceTask654"):
                opp_val = getattr(old_value, "BPMNProfile_ServiceTask654", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ServiceTask654", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ServiceTask654"):
                opp_val = getattr(value, "BPMNProfile_ServiceTask654", None)
                setattr(value, "BPMNProfile_ServiceTask654", self)

    @property
    def BPMNProfile_BPMNOperation238(self):
        return self.__BPMNProfile_BPMNOperation238

    @BPMNProfile_BPMNOperation238.setter
    def BPMNProfile_BPMNOperation238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNOperation__BPMNProfile_BPMNOperation238", None)
        self.__BPMNProfile_BPMNOperation238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Operation"):
                opp_val = getattr(old_value, "BPMNProfile_Operation", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Operation"):
                opp_val = getattr(value, "BPMNProfile_Operation", None)
                setattr(value, "BPMNProfile_Operation", self)

    @property
    def BPMNProfile_BPMNOperation(self):
        return self.__BPMNProfile_BPMNOperation

    @BPMNProfile_BPMNOperation.setter
    def BPMNProfile_BPMNOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNOperation__BPMNProfile_BPMNOperation", None)
        self.__BPMNProfile_BPMNOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNInterface233"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNInterface233", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNInterface233"):
                opp_val = getattr(value, "BPMNProfile_BPMNInterface233", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNInterface233", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def BPMNOperationowner(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement BPMNOperationowner method
        pass

    def BPMNOperationoutMessageRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement BPMNOperationoutMessageRef method
        pass

    def BPMNOperationerrorRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement BPMNOperationerrorRefs method
        pass

    def BPMNOperationinMessageRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement BPMNOperationinMessageRef method
        pass

class BPMNProfile_RootElement(BaseElement):

    pass
class BPMNProfile_CorrelationPropertyRetrievalExpression(BaseElement):

    pass
class BPMNProfile_MessageFlow(BaseElement):

    def __init__(self, BPMNProfile_MessageFlow: "BPMNProfile_BPMNCollaboration" = None, BPMNProfile_MessageFlow329: "BPMNProfile_MessageFlowAssociation" = None, BPMNProfile_MessageFlow332: "BPMNProfile_MessageFlowAssociation" = None, BPMNProfile_MessageFlow334: "BPMNProfile_InformationFlow" = None, BPMNProfile_MessageFlow336: "BPMNProfile_InteractionNode" = None, BPMNProfile_MessageFlow339: "BPMNProfile_InteractionNode" = None, BPMNProfile_MessageFlow342: "BPMNProfile_BPMNMessage" = None, BPMNProfile_MessageFlow349: "BPMNProfile_ConversationNode" = None):
        self.BPMNProfile_MessageFlow = BPMNProfile_MessageFlow
        self.BPMNProfile_MessageFlow329 = BPMNProfile_MessageFlow329
        self.BPMNProfile_MessageFlow332 = BPMNProfile_MessageFlow332
        self.BPMNProfile_MessageFlow334 = BPMNProfile_MessageFlow334
        self.BPMNProfile_MessageFlow336 = BPMNProfile_MessageFlow336
        self.BPMNProfile_MessageFlow339 = BPMNProfile_MessageFlow339
        self.BPMNProfile_MessageFlow342 = BPMNProfile_MessageFlow342
        self.BPMNProfile_MessageFlow349 = BPMNProfile_MessageFlow349
        
    @property
    def BPMNProfile_MessageFlow336(self):
        return self.__BPMNProfile_MessageFlow336

    @BPMNProfile_MessageFlow336.setter
    def BPMNProfile_MessageFlow336(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MessageFlow__BPMNProfile_MessageFlow336", None)
        self.__BPMNProfile_MessageFlow336 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_InteractionNode337"):
                opp_val = getattr(old_value, "BPMNProfile_InteractionNode337", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_InteractionNode337", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_InteractionNode337"):
                opp_val = getattr(value, "BPMNProfile_InteractionNode337", None)
                setattr(value, "BPMNProfile_InteractionNode337", self)

    @property
    def BPMNProfile_MessageFlow342(self):
        return self.__BPMNProfile_MessageFlow342

    @BPMNProfile_MessageFlow342.setter
    def BPMNProfile_MessageFlow342(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MessageFlow__BPMNProfile_MessageFlow342", None)
        self.__BPMNProfile_MessageFlow342 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNMessage343"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNMessage343", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNMessage343", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNMessage343"):
                opp_val = getattr(value, "BPMNProfile_BPMNMessage343", None)
                setattr(value, "BPMNProfile_BPMNMessage343", self)

    @property
    def BPMNProfile_MessageFlow(self):
        return self.__BPMNProfile_MessageFlow

    @BPMNProfile_MessageFlow.setter
    def BPMNProfile_MessageFlow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MessageFlow__BPMNProfile_MessageFlow", None)
        self.__BPMNProfile_MessageFlow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNCollaboration270"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNCollaboration270", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNCollaboration270"):
                opp_val = getattr(value, "BPMNProfile_BPMNCollaboration270", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNCollaboration270", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_MessageFlow349(self):
        return self.__BPMNProfile_MessageFlow349

    @BPMNProfile_MessageFlow349.setter
    def BPMNProfile_MessageFlow349(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MessageFlow__BPMNProfile_MessageFlow349", None)
        self.__BPMNProfile_MessageFlow349 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ConversationNode348"):
                opp_val = getattr(old_value, "BPMNProfile_ConversationNode348", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ConversationNode348"):
                opp_val = getattr(value, "BPMNProfile_ConversationNode348", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_ConversationNode348", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_MessageFlow329(self):
        return self.__BPMNProfile_MessageFlow329

    @BPMNProfile_MessageFlow329.setter
    def BPMNProfile_MessageFlow329(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MessageFlow__BPMNProfile_MessageFlow329", None)
        self.__BPMNProfile_MessageFlow329 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_MessageFlowAssociation328"):
                opp_val = getattr(old_value, "BPMNProfile_MessageFlowAssociation328", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_MessageFlowAssociation328", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_MessageFlowAssociation328"):
                opp_val = getattr(value, "BPMNProfile_MessageFlowAssociation328", None)
                setattr(value, "BPMNProfile_MessageFlowAssociation328", self)

    @property
    def BPMNProfile_MessageFlow339(self):
        return self.__BPMNProfile_MessageFlow339

    @BPMNProfile_MessageFlow339.setter
    def BPMNProfile_MessageFlow339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MessageFlow__BPMNProfile_MessageFlow339", None)
        self.__BPMNProfile_MessageFlow339 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_InteractionNode340"):
                opp_val = getattr(old_value, "BPMNProfile_InteractionNode340", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_InteractionNode340", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_InteractionNode340"):
                opp_val = getattr(value, "BPMNProfile_InteractionNode340", None)
                setattr(value, "BPMNProfile_InteractionNode340", self)

    @property
    def BPMNProfile_MessageFlow334(self):
        return self.__BPMNProfile_MessageFlow334

    @BPMNProfile_MessageFlow334.setter
    def BPMNProfile_MessageFlow334(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MessageFlow__BPMNProfile_MessageFlow334", None)
        self.__BPMNProfile_MessageFlow334 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_InformationFlow"):
                opp_val = getattr(old_value, "BPMNProfile_InformationFlow", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_InformationFlow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_InformationFlow"):
                opp_val = getattr(value, "BPMNProfile_InformationFlow", None)
                setattr(value, "BPMNProfile_InformationFlow", self)

    @property
    def BPMNProfile_MessageFlow332(self):
        return self.__BPMNProfile_MessageFlow332

    @BPMNProfile_MessageFlow332.setter
    def BPMNProfile_MessageFlow332(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MessageFlow__BPMNProfile_MessageFlow332", None)
        self.__BPMNProfile_MessageFlow332 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_MessageFlowAssociation331"):
                opp_val = getattr(old_value, "BPMNProfile_MessageFlowAssociation331", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_MessageFlowAssociation331", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_MessageFlowAssociation331"):
                opp_val = getattr(value, "BPMNProfile_MessageFlowAssociation331", None)
                setattr(value, "BPMNProfile_MessageFlowAssociation331", self)

    def MessageFlowmessageRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MessageFlowmessageRef method
        pass

    def MessageFlowtargetRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MessageFlowtargetRef method
        pass

    def MessageFlowsourceRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MessageFlowsourceRef method
        pass

class BPMNProfile_ParticipantAssociation(BaseElement):

    def __init__(self, BPMNProfile_ParticipantAssociation286: "BPMNProfile_Participant" = None, BPMNProfile_ParticipantAssociation: "BPMNProfile_BPMNCollaboration" = None, BPMNProfile_ParticipantAssociation280: "BPMNProfile_Dependency" = None, BPMNProfile_ParticipantAssociation283: "BPMNProfile_Participant" = None, BPMNProfile_ParticipantAssociation608: "BPMNProfile_CallConversation" = None):
        self.BPMNProfile_ParticipantAssociation286 = BPMNProfile_ParticipantAssociation286
        self.BPMNProfile_ParticipantAssociation = BPMNProfile_ParticipantAssociation
        self.BPMNProfile_ParticipantAssociation280 = BPMNProfile_ParticipantAssociation280
        self.BPMNProfile_ParticipantAssociation283 = BPMNProfile_ParticipantAssociation283
        self.BPMNProfile_ParticipantAssociation608 = BPMNProfile_ParticipantAssociation608
        
    @property
    def BPMNProfile_ParticipantAssociation286(self):
        return self.__BPMNProfile_ParticipantAssociation286

    @BPMNProfile_ParticipantAssociation286.setter
    def BPMNProfile_ParticipantAssociation286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ParticipantAssociation__BPMNProfile_ParticipantAssociation286", None)
        self.__BPMNProfile_ParticipantAssociation286 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Participant287"):
                opp_val = getattr(old_value, "BPMNProfile_Participant287", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Participant287", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Participant287"):
                opp_val = getattr(value, "BPMNProfile_Participant287", None)
                setattr(value, "BPMNProfile_Participant287", self)

    @property
    def BPMNProfile_ParticipantAssociation280(self):
        return self.__BPMNProfile_ParticipantAssociation280

    @BPMNProfile_ParticipantAssociation280.setter
    def BPMNProfile_ParticipantAssociation280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ParticipantAssociation__BPMNProfile_ParticipantAssociation280", None)
        self.__BPMNProfile_ParticipantAssociation280 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Dependency281"):
                opp_val = getattr(old_value, "BPMNProfile_Dependency281", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Dependency281", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Dependency281"):
                opp_val = getattr(value, "BPMNProfile_Dependency281", None)
                setattr(value, "BPMNProfile_Dependency281", self)

    @property
    def BPMNProfile_ParticipantAssociation283(self):
        return self.__BPMNProfile_ParticipantAssociation283

    @BPMNProfile_ParticipantAssociation283.setter
    def BPMNProfile_ParticipantAssociation283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ParticipantAssociation__BPMNProfile_ParticipantAssociation283", None)
        self.__BPMNProfile_ParticipantAssociation283 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Participant284"):
                opp_val = getattr(old_value, "BPMNProfile_Participant284", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Participant284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Participant284"):
                opp_val = getattr(value, "BPMNProfile_Participant284", None)
                setattr(value, "BPMNProfile_Participant284", self)

    @property
    def BPMNProfile_ParticipantAssociation608(self):
        return self.__BPMNProfile_ParticipantAssociation608

    @BPMNProfile_ParticipantAssociation608.setter
    def BPMNProfile_ParticipantAssociation608(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ParticipantAssociation__BPMNProfile_ParticipantAssociation608", None)
        self.__BPMNProfile_ParticipantAssociation608 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CallConversation607"):
                opp_val = getattr(old_value, "BPMNProfile_CallConversation607", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CallConversation607"):
                opp_val = getattr(value, "BPMNProfile_CallConversation607", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_CallConversation607", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_ParticipantAssociation(self):
        return self.__BPMNProfile_ParticipantAssociation

    @BPMNProfile_ParticipantAssociation.setter
    def BPMNProfile_ParticipantAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ParticipantAssociation__BPMNProfile_ParticipantAssociation", None)
        self.__BPMNProfile_ParticipantAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNCollaboration265"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNCollaboration265", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNCollaboration265"):
                opp_val = getattr(value, "BPMNProfile_BPMNCollaboration265", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNCollaboration265", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def ParticipantAssociationinnerParticipantRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ParticipantAssociationinnerParticipantRef method
        pass

    def ParticipantAssociationouterParticipantRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ParticipantAssociationouterParticipantRef method
        pass

class BPMNProfile_MessageFlowAssociation(BaseElement):

    def __init__(self, BPMNProfile_MessageFlowAssociation: "BPMNProfile_BPMNCollaboration" = None, BPMNProfile_MessageFlowAssociation325: "BPMNProfile_Dependency" = None, BPMNProfile_MessageFlowAssociation328: "BPMNProfile_MessageFlow" = None, BPMNProfile_MessageFlowAssociation331: "BPMNProfile_MessageFlow" = None):
        self.BPMNProfile_MessageFlowAssociation = BPMNProfile_MessageFlowAssociation
        self.BPMNProfile_MessageFlowAssociation325 = BPMNProfile_MessageFlowAssociation325
        self.BPMNProfile_MessageFlowAssociation328 = BPMNProfile_MessageFlowAssociation328
        self.BPMNProfile_MessageFlowAssociation331 = BPMNProfile_MessageFlowAssociation331
        
    @property
    def BPMNProfile_MessageFlowAssociation328(self):
        return self.__BPMNProfile_MessageFlowAssociation328

    @BPMNProfile_MessageFlowAssociation328.setter
    def BPMNProfile_MessageFlowAssociation328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MessageFlowAssociation__BPMNProfile_MessageFlowAssociation328", None)
        self.__BPMNProfile_MessageFlowAssociation328 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_MessageFlow329"):
                opp_val = getattr(old_value, "BPMNProfile_MessageFlow329", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_MessageFlow329", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_MessageFlow329"):
                opp_val = getattr(value, "BPMNProfile_MessageFlow329", None)
                setattr(value, "BPMNProfile_MessageFlow329", self)

    @property
    def BPMNProfile_MessageFlowAssociation325(self):
        return self.__BPMNProfile_MessageFlowAssociation325

    @BPMNProfile_MessageFlowAssociation325.setter
    def BPMNProfile_MessageFlowAssociation325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MessageFlowAssociation__BPMNProfile_MessageFlowAssociation325", None)
        self.__BPMNProfile_MessageFlowAssociation325 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Dependency326"):
                opp_val = getattr(old_value, "BPMNProfile_Dependency326", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Dependency326", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Dependency326"):
                opp_val = getattr(value, "BPMNProfile_Dependency326", None)
                setattr(value, "BPMNProfile_Dependency326", self)

    @property
    def BPMNProfile_MessageFlowAssociation(self):
        return self.__BPMNProfile_MessageFlowAssociation

    @BPMNProfile_MessageFlowAssociation.setter
    def BPMNProfile_MessageFlowAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MessageFlowAssociation__BPMNProfile_MessageFlowAssociation", None)
        self.__BPMNProfile_MessageFlowAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNCollaboration268"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNCollaboration268", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNCollaboration268"):
                opp_val = getattr(value, "BPMNProfile_BPMNCollaboration268", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNCollaboration268", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_MessageFlowAssociation331(self):
        return self.__BPMNProfile_MessageFlowAssociation331

    @BPMNProfile_MessageFlowAssociation331.setter
    def BPMNProfile_MessageFlowAssociation331(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MessageFlowAssociation__BPMNProfile_MessageFlowAssociation331", None)
        self.__BPMNProfile_MessageFlowAssociation331 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_MessageFlow332"):
                opp_val = getattr(old_value, "BPMNProfile_MessageFlow332", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_MessageFlow332", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_MessageFlow332"):
                opp_val = getattr(value, "BPMNProfile_MessageFlow332", None)
                setattr(value, "BPMNProfile_MessageFlow332", self)

    def MessageFlowAssociationinnerMessageFlowRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MessageFlowAssociationinnerMessageFlowRef method
        pass

    def MessageFlowAssociationouterMessageFlowRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MessageFlowAssociationouterMessageFlowRef method
        pass

class BPMNProfile_ItemAwareElement(BaseElement):

    def __init__(self, BPMNProfile_ItemAwareElement183: "BPMNProfile_ItemDefinition" = None, BPMNProfile_ItemAwareElement: set["BPMNProfile_DataState"] = None, BPMNProfile_ItemAwareElement181: "BPMNProfile_TypedElement" = None, BPMNProfile_ItemAwareElement485: "BPMNProfile_DataAssociation" = None, BPMNProfile_ItemAwareElement488: "BPMNProfile_DataAssociation" = None, BPMNProfile_ItemAwareElement665: "BPMNProfile_MultiInstanceLoopCharacteristics" = None, BPMNProfile_ItemAwareElement668: "BPMNProfile_MultiInstanceLoopCharacteristics" = None):
        self.BPMNProfile_ItemAwareElement183 = BPMNProfile_ItemAwareElement183
        self.BPMNProfile_ItemAwareElement = BPMNProfile_ItemAwareElement if BPMNProfile_ItemAwareElement is not None else set()
        self.BPMNProfile_ItemAwareElement181 = BPMNProfile_ItemAwareElement181
        self.BPMNProfile_ItemAwareElement485 = BPMNProfile_ItemAwareElement485
        self.BPMNProfile_ItemAwareElement488 = BPMNProfile_ItemAwareElement488
        self.BPMNProfile_ItemAwareElement665 = BPMNProfile_ItemAwareElement665
        self.BPMNProfile_ItemAwareElement668 = BPMNProfile_ItemAwareElement668
        
    @property
    def BPMNProfile_ItemAwareElement181(self):
        return self.__BPMNProfile_ItemAwareElement181

    @BPMNProfile_ItemAwareElement181.setter
    def BPMNProfile_ItemAwareElement181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemAwareElement__BPMNProfile_ItemAwareElement181", None)
        self.__BPMNProfile_ItemAwareElement181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_TypedElement"):
                opp_val = getattr(old_value, "BPMNProfile_TypedElement", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_TypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_TypedElement"):
                opp_val = getattr(value, "BPMNProfile_TypedElement", None)
                setattr(value, "BPMNProfile_TypedElement", self)

    @property
    def BPMNProfile_ItemAwareElement183(self):
        return self.__BPMNProfile_ItemAwareElement183

    @BPMNProfile_ItemAwareElement183.setter
    def BPMNProfile_ItemAwareElement183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemAwareElement__BPMNProfile_ItemAwareElement183", None)
        self.__BPMNProfile_ItemAwareElement183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ItemDefinition"):
                opp_val = getattr(old_value, "BPMNProfile_ItemDefinition", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ItemDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ItemDefinition"):
                opp_val = getattr(value, "BPMNProfile_ItemDefinition", None)
                setattr(value, "BPMNProfile_ItemDefinition", self)

    @property
    def BPMNProfile_ItemAwareElement665(self):
        return self.__BPMNProfile_ItemAwareElement665

    @BPMNProfile_ItemAwareElement665.setter
    def BPMNProfile_ItemAwareElement665(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemAwareElement__BPMNProfile_ItemAwareElement665", None)
        self.__BPMNProfile_ItemAwareElement665 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_MultiInstanceLoopCharacteristics664"):
                opp_val = getattr(old_value, "BPMNProfile_MultiInstanceLoopCharacteristics664", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_MultiInstanceLoopCharacteristics664", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_MultiInstanceLoopCharacteristics664"):
                opp_val = getattr(value, "BPMNProfile_MultiInstanceLoopCharacteristics664", None)
                setattr(value, "BPMNProfile_MultiInstanceLoopCharacteristics664", self)

    @property
    def BPMNProfile_ItemAwareElement485(self):
        return self.__BPMNProfile_ItemAwareElement485

    @BPMNProfile_ItemAwareElement485.setter
    def BPMNProfile_ItemAwareElement485(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemAwareElement__BPMNProfile_ItemAwareElement485", None)
        self.__BPMNProfile_ItemAwareElement485 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_DataAssociation484"):
                opp_val = getattr(old_value, "BPMNProfile_DataAssociation484", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_DataAssociation484", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_DataAssociation484"):
                opp_val = getattr(value, "BPMNProfile_DataAssociation484", None)
                setattr(value, "BPMNProfile_DataAssociation484", self)

    @property
    def BPMNProfile_ItemAwareElement488(self):
        return self.__BPMNProfile_ItemAwareElement488

    @BPMNProfile_ItemAwareElement488.setter
    def BPMNProfile_ItemAwareElement488(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemAwareElement__BPMNProfile_ItemAwareElement488", None)
        self.__BPMNProfile_ItemAwareElement488 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_DataAssociation487"):
                opp_val = getattr(old_value, "BPMNProfile_DataAssociation487", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_DataAssociation487", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_DataAssociation487"):
                opp_val = getattr(value, "BPMNProfile_DataAssociation487", None)
                setattr(value, "BPMNProfile_DataAssociation487", self)

    @property
    def BPMNProfile_ItemAwareElement(self):
        return self.__BPMNProfile_ItemAwareElement

    @BPMNProfile_ItemAwareElement.setter
    def BPMNProfile_ItemAwareElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemAwareElement__BPMNProfile_ItemAwareElement", None)
        self.__BPMNProfile_ItemAwareElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_DataState"):
                    opp_val = getattr(item, "BPMNProfile_DataState", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_DataState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_DataState"):
                    opp_val = getattr(item, "BPMNProfile_DataState", None)
                    
                    setattr(item, "BPMNProfile_DataState", self)
                    

    @property
    def BPMNProfile_ItemAwareElement668(self):
        return self.__BPMNProfile_ItemAwareElement668

    @BPMNProfile_ItemAwareElement668.setter
    def BPMNProfile_ItemAwareElement668(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemAwareElement__BPMNProfile_ItemAwareElement668", None)
        self.__BPMNProfile_ItemAwareElement668 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_MultiInstanceLoopCharacteristics667"):
                opp_val = getattr(old_value, "BPMNProfile_MultiInstanceLoopCharacteristics667", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_MultiInstanceLoopCharacteristics667", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_MultiInstanceLoopCharacteristics667"):
                opp_val = getattr(value, "BPMNProfile_MultiInstanceLoopCharacteristics667", None)
                setattr(value, "BPMNProfile_MultiInstanceLoopCharacteristics667", self)

    def ItemAwareElementdataState(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ItemAwareElementdataState method
        pass

class BPMNProfile_InputOutputBinding(BaseElement):

    pass
class BPMNProfile_CorrelationPropertyBinding(BaseElement):

    pass
class BPMNProfile_CorrelationProperty(BaseElement):

    pass
class BPMNProfile_ResourceRole(BaseElement):

    def __init__(self, ResourceRole: "BPMNProfile_BPMNProcess" = None, resources: "BPMNProfile_BPMNProcess" = None, BPMNProfile_ResourceRole: "BPMNProfile_Property" = None, BPMNProfile_ResourceRole405: "BPMNProfile_ResourceAssignmentExpression" = None, BPMNProfile_ResourceRole407: "BPMNProfile_Resource" = None, BPMNProfile_ResourceRole409: set["BPMNProfile_ResourceParameterBinding"] = None, BPMNProfile_ResourceRole434: "BPMNProfile_GlobalTask" = None, BPMNProfile_ResourceRole461: "BPMNProfile_BPMNActivity" = None):
        self.ResourceRole = ResourceRole
        self.resources = resources
        self.BPMNProfile_ResourceRole = BPMNProfile_ResourceRole
        self.BPMNProfile_ResourceRole405 = BPMNProfile_ResourceRole405
        self.BPMNProfile_ResourceRole407 = BPMNProfile_ResourceRole407
        self.BPMNProfile_ResourceRole409 = BPMNProfile_ResourceRole409 if BPMNProfile_ResourceRole409 is not None else set()
        self.BPMNProfile_ResourceRole434 = BPMNProfile_ResourceRole434
        self.BPMNProfile_ResourceRole461 = BPMNProfile_ResourceRole461
        
    @property
    def BPMNProfile_ResourceRole405(self):
        return self.__BPMNProfile_ResourceRole405

    @BPMNProfile_ResourceRole405.setter
    def BPMNProfile_ResourceRole405(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceRole__BPMNProfile_ResourceRole405", None)
        self.__BPMNProfile_ResourceRole405 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ResourceAssignmentExpression"):
                opp_val = getattr(old_value, "BPMNProfile_ResourceAssignmentExpression", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ResourceAssignmentExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ResourceAssignmentExpression"):
                opp_val = getattr(value, "BPMNProfile_ResourceAssignmentExpression", None)
                setattr(value, "BPMNProfile_ResourceAssignmentExpression", self)

    @property
    def BPMNProfile_ResourceRole(self):
        return self.__BPMNProfile_ResourceRole

    @BPMNProfile_ResourceRole.setter
    def BPMNProfile_ResourceRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceRole__BPMNProfile_ResourceRole", None)
        self.__BPMNProfile_ResourceRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Property403"):
                opp_val = getattr(old_value, "BPMNProfile_Property403", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Property403", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Property403"):
                opp_val = getattr(value, "BPMNProfile_Property403", None)
                setattr(value, "BPMNProfile_Property403", self)

    @property
    def BPMNProfile_ResourceRole461(self):
        return self.__BPMNProfile_ResourceRole461

    @BPMNProfile_ResourceRole461.setter
    def BPMNProfile_ResourceRole461(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceRole__BPMNProfile_ResourceRole461", None)
        self.__BPMNProfile_ResourceRole461 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNActivity460"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNActivity460", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNActivity460"):
                opp_val = getattr(value, "BPMNProfile_BPMNActivity460", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNActivity460", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_ResourceRole407(self):
        return self.__BPMNProfile_ResourceRole407

    @BPMNProfile_ResourceRole407.setter
    def BPMNProfile_ResourceRole407(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceRole__BPMNProfile_ResourceRole407", None)
        self.__BPMNProfile_ResourceRole407 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Resource"):
                opp_val = getattr(old_value, "BPMNProfile_Resource", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Resource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Resource"):
                opp_val = getattr(value, "BPMNProfile_Resource", None)
                setattr(value, "BPMNProfile_Resource", self)

    @property
    def BPMNProfile_ResourceRole434(self):
        return self.__BPMNProfile_ResourceRole434

    @BPMNProfile_ResourceRole434.setter
    def BPMNProfile_ResourceRole434(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceRole__BPMNProfile_ResourceRole434", None)
        self.__BPMNProfile_ResourceRole434 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_GlobalTask433"):
                opp_val = getattr(old_value, "BPMNProfile_GlobalTask433", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_GlobalTask433"):
                opp_val = getattr(value, "BPMNProfile_GlobalTask433", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_GlobalTask433", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def resources(self):
        return self.__resources

    @resources.setter
    def resources(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceRole__resources", None)
        self.__resources = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProcess"):
                opp_val = getattr(old_value, "BPMNProcess", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProcess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProcess"):
                opp_val = getattr(value, "BPMNProcess", None)
                setattr(value, "BPMNProcess", self)

    @property
    def ResourceRole(self):
        return self.__ResourceRole

    @ResourceRole.setter
    def ResourceRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceRole__ResourceRole", None)
        self.__ResourceRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "process"):
                opp_val = getattr(old_value, "process", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "process"):
                opp_val = getattr(value, "process", None)
                if opp_val is None:
                    setattr(value, "process", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_ResourceRole409(self):
        return self.__BPMNProfile_ResourceRole409

    @BPMNProfile_ResourceRole409.setter
    def BPMNProfile_ResourceRole409(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceRole__BPMNProfile_ResourceRole409", None)
        self.__BPMNProfile_ResourceRole409 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_ResourceParameterBinding"):
                    opp_val = getattr(item, "BPMNProfile_ResourceParameterBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_ResourceParameterBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_ResourceParameterBinding"):
                    opp_val = getattr(item, "BPMNProfile_ResourceParameterBinding", None)
                    
                    setattr(item, "BPMNProfile_ResourceParameterBinding", self)
                    

    def ResourceRoleisRequired(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceRoleisRequired method
        pass

    def ResourceRoleresourceParameterBindings(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceRoleresourceParameterBindings method
        pass

    def ResourceRoleresourceRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceRoleresourceRef method
        pass

    def ResourceRoleowner(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceRoleowner method
        pass

    def ResourceRoleprocess(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ResourceRoleprocess method
        pass

class BPMNProfile_BPMNExpression(BaseElement):

    pass
class BPMNProfile_DataAssociation(BaseElement):

    def __init__(self, BPMNProfile_DataAssociation: "BPMNProfile_ObjectFlow" = None, BPMNProfile_DataAssociation484: "BPMNProfile_ItemAwareElement" = None, BPMNProfile_DataAssociation487: "BPMNProfile_ItemAwareElement" = None, BPMNProfile_DataAssociation490: "BPMNProfile_FormalExpression" = None, BPMNProfile_DataAssociation493: set["BPMNProfile_Assignment"] = None):
        self.BPMNProfile_DataAssociation = BPMNProfile_DataAssociation
        self.BPMNProfile_DataAssociation484 = BPMNProfile_DataAssociation484
        self.BPMNProfile_DataAssociation487 = BPMNProfile_DataAssociation487
        self.BPMNProfile_DataAssociation490 = BPMNProfile_DataAssociation490
        self.BPMNProfile_DataAssociation493 = BPMNProfile_DataAssociation493 if BPMNProfile_DataAssociation493 is not None else set()
        
    @property
    def BPMNProfile_DataAssociation493(self):
        return self.__BPMNProfile_DataAssociation493

    @BPMNProfile_DataAssociation493.setter
    def BPMNProfile_DataAssociation493(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataAssociation__BPMNProfile_DataAssociation493", None)
        self.__BPMNProfile_DataAssociation493 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_Assignment"):
                    opp_val = getattr(item, "BPMNProfile_Assignment", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_Assignment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_Assignment"):
                    opp_val = getattr(item, "BPMNProfile_Assignment", None)
                    
                    setattr(item, "BPMNProfile_Assignment", self)
                    

    @property
    def BPMNProfile_DataAssociation484(self):
        return self.__BPMNProfile_DataAssociation484

    @BPMNProfile_DataAssociation484.setter
    def BPMNProfile_DataAssociation484(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataAssociation__BPMNProfile_DataAssociation484", None)
        self.__BPMNProfile_DataAssociation484 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ItemAwareElement485"):
                opp_val = getattr(old_value, "BPMNProfile_ItemAwareElement485", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ItemAwareElement485", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ItemAwareElement485"):
                opp_val = getattr(value, "BPMNProfile_ItemAwareElement485", None)
                setattr(value, "BPMNProfile_ItemAwareElement485", self)

    @property
    def BPMNProfile_DataAssociation490(self):
        return self.__BPMNProfile_DataAssociation490

    @BPMNProfile_DataAssociation490.setter
    def BPMNProfile_DataAssociation490(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataAssociation__BPMNProfile_DataAssociation490", None)
        self.__BPMNProfile_DataAssociation490 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_FormalExpression491"):
                opp_val = getattr(old_value, "BPMNProfile_FormalExpression491", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_FormalExpression491", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_FormalExpression491"):
                opp_val = getattr(value, "BPMNProfile_FormalExpression491", None)
                setattr(value, "BPMNProfile_FormalExpression491", self)

    @property
    def BPMNProfile_DataAssociation487(self):
        return self.__BPMNProfile_DataAssociation487

    @BPMNProfile_DataAssociation487.setter
    def BPMNProfile_DataAssociation487(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataAssociation__BPMNProfile_DataAssociation487", None)
        self.__BPMNProfile_DataAssociation487 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ItemAwareElement488"):
                opp_val = getattr(old_value, "BPMNProfile_ItemAwareElement488", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ItemAwareElement488", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ItemAwareElement488"):
                opp_val = getattr(value, "BPMNProfile_ItemAwareElement488", None)
                setattr(value, "BPMNProfile_ItemAwareElement488", self)

    @property
    def BPMNProfile_DataAssociation(self):
        return self.__BPMNProfile_DataAssociation

    @BPMNProfile_DataAssociation.setter
    def BPMNProfile_DataAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataAssociation__BPMNProfile_DataAssociation", None)
        self.__BPMNProfile_DataAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ObjectFlow"):
                opp_val = getattr(old_value, "BPMNProfile_ObjectFlow", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ObjectFlow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ObjectFlow"):
                opp_val = getattr(value, "BPMNProfile_ObjectFlow", None)
                setattr(value, "BPMNProfile_ObjectFlow", self)

    def DataAssociationsource(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement DataAssociationsource method
        pass

    def DataAssociationtransformation(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement DataAssociationtransformation method
        pass

    def DataAssociationtarget(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement DataAssociationtarget method
        pass

class BPMNProfile_Rendering(BaseElement):

    pass
class BPMNProfile_CorrelationKey(BaseElement):

    pass
class BPMNProfile_Participant(BaseElement):

    def __init__(self, BPMNProfile_Participant287: "BPMNProfile_ParticipantAssociation" = None, BPMNProfile_Participant: "BPMNProfile_BPMNCollaboration" = None, BPMNProfile_Participant284: "BPMNProfile_ParticipantAssociation" = None, BPMNProfile_Participant289: "BPMNProfile_Property" = None, BPMNProfile_Participant292: "BPMNProfile_BPMNProcess" = None, BPMNProfile_Participant295: "BPMNProfile_ParticipantMultiplicity" = None, Participant: "BPMNProfile_PartnerEntity" = None, participantRef: set["BPMNProfile_PartnerEntity"] = None, participantRef298: set["BPMNProfile_PartnerRole"] = None, BPMNProfile_Participant300: set["BPMNProfile_BPMNInterface"] = None, Participant323: "BPMNProfile_PartnerRole" = None, BPMNProfile_Participant355: "BPMNProfile_ConversationNode" = None):
        self.BPMNProfile_Participant287 = BPMNProfile_Participant287
        self.BPMNProfile_Participant = BPMNProfile_Participant
        self.BPMNProfile_Participant284 = BPMNProfile_Participant284
        self.BPMNProfile_Participant289 = BPMNProfile_Participant289
        self.BPMNProfile_Participant292 = BPMNProfile_Participant292
        self.BPMNProfile_Participant295 = BPMNProfile_Participant295
        self.Participant = Participant
        self.participantRef = participantRef if participantRef is not None else set()
        self.participantRef298 = participantRef298 if participantRef298 is not None else set()
        self.BPMNProfile_Participant300 = BPMNProfile_Participant300 if BPMNProfile_Participant300 is not None else set()
        self.Participant323 = Participant323
        self.BPMNProfile_Participant355 = BPMNProfile_Participant355
        
    @property
    def participantRef298(self):
        return self.__participantRef298

    @participantRef298.setter
    def participantRef298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Participant__participantRef298", None)
        self.__participantRef298 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PartnerRole"):
                    opp_val = getattr(item, "PartnerRole", None)
                    
                    if opp_val == self:
                        setattr(item, "PartnerRole", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PartnerRole"):
                    opp_val = getattr(item, "PartnerRole", None)
                    
                    setattr(item, "PartnerRole", self)
                    

    @property
    def BPMNProfile_Participant300(self):
        return self.__BPMNProfile_Participant300

    @BPMNProfile_Participant300.setter
    def BPMNProfile_Participant300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Participant__BPMNProfile_Participant300", None)
        self.__BPMNProfile_Participant300 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_BPMNInterface301"):
                    opp_val = getattr(item, "BPMNProfile_BPMNInterface301", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_BPMNInterface301", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_BPMNInterface301"):
                    opp_val = getattr(item, "BPMNProfile_BPMNInterface301", None)
                    
                    setattr(item, "BPMNProfile_BPMNInterface301", self)
                    

    @property
    def BPMNProfile_Participant284(self):
        return self.__BPMNProfile_Participant284

    @BPMNProfile_Participant284.setter
    def BPMNProfile_Participant284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Participant__BPMNProfile_Participant284", None)
        self.__BPMNProfile_Participant284 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ParticipantAssociation283"):
                opp_val = getattr(old_value, "BPMNProfile_ParticipantAssociation283", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ParticipantAssociation283", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ParticipantAssociation283"):
                opp_val = getattr(value, "BPMNProfile_ParticipantAssociation283", None)
                setattr(value, "BPMNProfile_ParticipantAssociation283", self)

    @property
    def BPMNProfile_Participant289(self):
        return self.__BPMNProfile_Participant289

    @BPMNProfile_Participant289.setter
    def BPMNProfile_Participant289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Participant__BPMNProfile_Participant289", None)
        self.__BPMNProfile_Participant289 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Property290"):
                opp_val = getattr(old_value, "BPMNProfile_Property290", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Property290", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Property290"):
                opp_val = getattr(value, "BPMNProfile_Property290", None)
                setattr(value, "BPMNProfile_Property290", self)

    @property
    def BPMNProfile_Participant287(self):
        return self.__BPMNProfile_Participant287

    @BPMNProfile_Participant287.setter
    def BPMNProfile_Participant287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Participant__BPMNProfile_Participant287", None)
        self.__BPMNProfile_Participant287 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ParticipantAssociation286"):
                opp_val = getattr(old_value, "BPMNProfile_ParticipantAssociation286", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ParticipantAssociation286", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ParticipantAssociation286"):
                opp_val = getattr(value, "BPMNProfile_ParticipantAssociation286", None)
                setattr(value, "BPMNProfile_ParticipantAssociation286", self)

    @property
    def BPMNProfile_Participant292(self):
        return self.__BPMNProfile_Participant292

    @BPMNProfile_Participant292.setter
    def BPMNProfile_Participant292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Participant__BPMNProfile_Participant292", None)
        self.__BPMNProfile_Participant292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNProcess293"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNProcess293", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNProcess293", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNProcess293"):
                opp_val = getattr(value, "BPMNProfile_BPMNProcess293", None)
                setattr(value, "BPMNProfile_BPMNProcess293", self)

    @property
    def BPMNProfile_Participant355(self):
        return self.__BPMNProfile_Participant355

    @BPMNProfile_Participant355.setter
    def BPMNProfile_Participant355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Participant__BPMNProfile_Participant355", None)
        self.__BPMNProfile_Participant355 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ConversationNode354"):
                opp_val = getattr(old_value, "BPMNProfile_ConversationNode354", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ConversationNode354"):
                opp_val = getattr(value, "BPMNProfile_ConversationNode354", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_ConversationNode354", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def participantRef(self):
        return self.__participantRef

    @participantRef.setter
    def participantRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Participant__participantRef", None)
        self.__participantRef = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PartnerEntity"):
                    opp_val = getattr(item, "PartnerEntity", None)
                    
                    if opp_val == self:
                        setattr(item, "PartnerEntity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PartnerEntity"):
                    opp_val = getattr(item, "PartnerEntity", None)
                    
                    setattr(item, "PartnerEntity", self)
                    

    @property
    def BPMNProfile_Participant(self):
        return self.__BPMNProfile_Participant

    @BPMNProfile_Participant.setter
    def BPMNProfile_Participant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Participant__BPMNProfile_Participant", None)
        self.__BPMNProfile_Participant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNCollaboration278"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNCollaboration278", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNCollaboration278"):
                opp_val = getattr(value, "BPMNProfile_BPMNCollaboration278", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNCollaboration278", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Participant(self):
        return self.__Participant

    @Participant.setter
    def Participant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Participant__Participant", None)
        self.__Participant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "partnerEntityRef"):
                opp_val = getattr(old_value, "partnerEntityRef", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "partnerEntityRef"):
                opp_val = getattr(value, "partnerEntityRef", None)
                if opp_val is None:
                    setattr(value, "partnerEntityRef", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Participant323(self):
        return self.__Participant323

    @Participant323.setter
    def Participant323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Participant__Participant323", None)
        self.__Participant323 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "partnerRoleRef"):
                opp_val = getattr(old_value, "partnerRoleRef", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "partnerRoleRef"):
                opp_val = getattr(value, "partnerRoleRef", None)
                if opp_val is None:
                    setattr(value, "partnerRoleRef", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_Participant295(self):
        return self.__BPMNProfile_Participant295

    @BPMNProfile_Participant295.setter
    def BPMNProfile_Participant295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Participant__BPMNProfile_Participant295", None)
        self.__BPMNProfile_Participant295 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ParticipantMultiplicity"):
                opp_val = getattr(old_value, "BPMNProfile_ParticipantMultiplicity", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ParticipantMultiplicity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ParticipantMultiplicity"):
                opp_val = getattr(value, "BPMNProfile_ParticipantMultiplicity", None)
                setattr(value, "BPMNProfile_ParticipantMultiplicity", self)

    def ParticipantmultiplicityMinimum(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ParticipantmultiplicityMinimum method
        pass

    def Participanttype(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement Participanttype method
        pass

    def Participantownership(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement Participantownership method
        pass

    def Participantrealizationsupplier(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement Participantrealizationsupplier method
        pass

    def ParticipantmultiplicityMaximum(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ParticipantmultiplicityMaximum method
        pass

    def participantpartnerEntityRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement participantpartnerEntityRef method
        pass

    def ParticipantprocessRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ParticipantprocessRef method
        pass

    def ParticipantinterfaceRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ParticipantinterfaceRefs method
        pass

    def participantpartnerRoleRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement participantpartnerRoleRef method
        pass

class BPMNProfile_OutputSet(BaseElement):

    def __init__(self, BPMNProfile_OutputSet: "BPMNProfile_InputOutputSpecification" = None, outputSetRefs: set["BPMNProfile_DataOutput"] = None, OutputSet: "BPMNProfile_DataOutput" = None, BPMNProfile_OutputSet213: "BPMNProfile_DataOutput" = None, BPMNProfile_OutputSet216: "BPMNProfile_DataOutput" = None, BPMNProfile_OutputSet218: "BPMNProfile_ParameterSet" = None, BPMNProfile_OutputSet221: set["BPMNProfile_DataOutput"] = None, BPMNProfile_OutputSet224: set["BPMNProfile_DataOutput"] = None, BPMNProfile_OutputSet257: "BPMNProfile_InputOutputBinding" = None):
        self.BPMNProfile_OutputSet = BPMNProfile_OutputSet
        self.outputSetRefs = outputSetRefs if outputSetRefs is not None else set()
        self.OutputSet = OutputSet
        self.BPMNProfile_OutputSet213 = BPMNProfile_OutputSet213
        self.BPMNProfile_OutputSet216 = BPMNProfile_OutputSet216
        self.BPMNProfile_OutputSet218 = BPMNProfile_OutputSet218
        self.BPMNProfile_OutputSet221 = BPMNProfile_OutputSet221 if BPMNProfile_OutputSet221 is not None else set()
        self.BPMNProfile_OutputSet224 = BPMNProfile_OutputSet224 if BPMNProfile_OutputSet224 is not None else set()
        self.BPMNProfile_OutputSet257 = BPMNProfile_OutputSet257
        
    @property
    def OutputSet(self):
        return self.__OutputSet

    @OutputSet.setter
    def OutputSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_OutputSet__OutputSet", None)
        self.__OutputSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataOutputRefs"):
                opp_val = getattr(old_value, "dataOutputRefs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataOutputRefs"):
                opp_val = getattr(value, "dataOutputRefs", None)
                if opp_val is None:
                    setattr(value, "dataOutputRefs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_OutputSet216(self):
        return self.__BPMNProfile_OutputSet216

    @BPMNProfile_OutputSet216.setter
    def BPMNProfile_OutputSet216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_OutputSet__BPMNProfile_OutputSet216", None)
        self.__BPMNProfile_OutputSet216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_DataOutput215"):
                opp_val = getattr(old_value, "BPMNProfile_DataOutput215", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_DataOutput215"):
                opp_val = getattr(value, "BPMNProfile_DataOutput215", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_DataOutput215", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_OutputSet221(self):
        return self.__BPMNProfile_OutputSet221

    @BPMNProfile_OutputSet221.setter
    def BPMNProfile_OutputSet221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_OutputSet__BPMNProfile_OutputSet221", None)
        self.__BPMNProfile_OutputSet221 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_DataOutput222"):
                    opp_val = getattr(item, "BPMNProfile_DataOutput222", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_DataOutput222", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_DataOutput222"):
                    opp_val = getattr(item, "BPMNProfile_DataOutput222", None)
                    
                    setattr(item, "BPMNProfile_DataOutput222", self)
                    

    @property
    def outputSetRefs(self):
        return self.__outputSetRefs

    @outputSetRefs.setter
    def outputSetRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_OutputSet__outputSetRefs", None)
        self.__outputSetRefs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataOutput"):
                    opp_val = getattr(item, "DataOutput", None)
                    
                    if opp_val == self:
                        setattr(item, "DataOutput", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataOutput"):
                    opp_val = getattr(item, "DataOutput", None)
                    
                    setattr(item, "DataOutput", self)
                    

    @property
    def BPMNProfile_OutputSet213(self):
        return self.__BPMNProfile_OutputSet213

    @BPMNProfile_OutputSet213.setter
    def BPMNProfile_OutputSet213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_OutputSet__BPMNProfile_OutputSet213", None)
        self.__BPMNProfile_OutputSet213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_DataOutput212"):
                opp_val = getattr(old_value, "BPMNProfile_DataOutput212", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_DataOutput212"):
                opp_val = getattr(value, "BPMNProfile_DataOutput212", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_DataOutput212", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_OutputSet218(self):
        return self.__BPMNProfile_OutputSet218

    @BPMNProfile_OutputSet218.setter
    def BPMNProfile_OutputSet218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_OutputSet__BPMNProfile_OutputSet218", None)
        self.__BPMNProfile_OutputSet218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ParameterSet219"):
                opp_val = getattr(old_value, "BPMNProfile_ParameterSet219", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ParameterSet219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ParameterSet219"):
                opp_val = getattr(value, "BPMNProfile_ParameterSet219", None)
                setattr(value, "BPMNProfile_ParameterSet219", self)

    @property
    def BPMNProfile_OutputSet257(self):
        return self.__BPMNProfile_OutputSet257

    @BPMNProfile_OutputSet257.setter
    def BPMNProfile_OutputSet257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_OutputSet__BPMNProfile_OutputSet257", None)
        self.__BPMNProfile_OutputSet257 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_InputOutputBinding256"):
                opp_val = getattr(old_value, "BPMNProfile_InputOutputBinding256", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_InputOutputBinding256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_InputOutputBinding256"):
                opp_val = getattr(value, "BPMNProfile_InputOutputBinding256", None)
                setattr(value, "BPMNProfile_InputOutputBinding256", self)

    @property
    def BPMNProfile_OutputSet(self):
        return self.__BPMNProfile_OutputSet

    @BPMNProfile_OutputSet.setter
    def BPMNProfile_OutputSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_OutputSet__BPMNProfile_OutputSet", None)
        self.__BPMNProfile_OutputSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_InputOutputSpecification167"):
                opp_val = getattr(old_value, "BPMNProfile_InputOutputSpecification167", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_InputOutputSpecification167"):
                opp_val = getattr(value, "BPMNProfile_InputOutputSpecification167", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_InputOutputSpecification167", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_OutputSet224(self):
        return self.__BPMNProfile_OutputSet224

    @BPMNProfile_OutputSet224.setter
    def BPMNProfile_OutputSet224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_OutputSet__BPMNProfile_OutputSet224", None)
        self.__BPMNProfile_OutputSet224 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_DataOutput225"):
                    opp_val = getattr(item, "BPMNProfile_DataOutput225", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_DataOutput225", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_DataOutput225"):
                    opp_val = getattr(item, "BPMNProfile_DataOutput225", None)
                    
                    setattr(item, "BPMNProfile_DataOutput225", self)
                    

    def OutputSetdataOutputRefs(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement OutputSetdataOutputRefs method
        pass

    def OutputSetwhileExecutingOutputRefs(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement OutputSetwhileExecutingOutputRefs method
        pass

    def OutputSetoptionalOutputRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement OutputSetoptionalOutputRefs method
        pass

class BPMNProfile_ComplexBehaviorDefinition(BaseElement):

    pass
class BPMNProfile_ParticipantMultiplicity(BaseElement):

    def __init__(self, minimum: str, maximum: str, BPMNProfile_ParticipantMultiplicity: "BPMNProfile_Participant" = None, BPMNProfile_ParticipantMultiplicity317: "BPMNProfile_MultiplicityElement" = None):
        self.minimum = minimum
        self.maximum = maximum
        self.BPMNProfile_ParticipantMultiplicity = BPMNProfile_ParticipantMultiplicity
        self.BPMNProfile_ParticipantMultiplicity317 = BPMNProfile_ParticipantMultiplicity317
        
    @property
    def maximum(self) -> str:
        return self.__maximum

    @maximum.setter
    def maximum(self, maximum: str):
        self.__maximum = maximum

    @property
    def minimum(self) -> str:
        return self.__minimum

    @minimum.setter
    def minimum(self, minimum: str):
        self.__minimum = minimum

    @property
    def BPMNProfile_ParticipantMultiplicity(self):
        return self.__BPMNProfile_ParticipantMultiplicity

    @BPMNProfile_ParticipantMultiplicity.setter
    def BPMNProfile_ParticipantMultiplicity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ParticipantMultiplicity__BPMNProfile_ParticipantMultiplicity", None)
        self.__BPMNProfile_ParticipantMultiplicity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Participant295"):
                opp_val = getattr(old_value, "BPMNProfile_Participant295", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Participant295", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Participant295"):
                opp_val = getattr(value, "BPMNProfile_Participant295", None)
                setattr(value, "BPMNProfile_Participant295", self)

    @property
    def BPMNProfile_ParticipantMultiplicity317(self):
        return self.__BPMNProfile_ParticipantMultiplicity317

    @BPMNProfile_ParticipantMultiplicity317.setter
    def BPMNProfile_ParticipantMultiplicity317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ParticipantMultiplicity__BPMNProfile_ParticipantMultiplicity317", None)
        self.__BPMNProfile_ParticipantMultiplicity317 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_MultiplicityElement"):
                opp_val = getattr(old_value, "BPMNProfile_MultiplicityElement", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_MultiplicityElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_MultiplicityElement"):
                opp_val = getattr(value, "BPMNProfile_MultiplicityElement", None)
                setattr(value, "BPMNProfile_MultiplicityElement", self)

class BPMNProfile_InputOutputSpecification(BaseElement):

    pass
class BPMNProfile_DataState(BaseElement):

    pass
class BPMNProfile_BPMNRelationship(BaseElement):

    def __init__(self, type: str, direction: str, BPMNProfile_BPMNRelationship121: "BPMNProfile_Constraint" = None, BPMNProfile_BPMNRelationship123: set["BPMNProfile_Element"] = None, BPMNProfile_BPMNRelationship: "BPMNProfile_Definitions" = None, BPMNProfile_BPMNRelationship126: set["BPMNProfile_Element"] = None, BPMNProfile_BPMNRelationship129: "BPMNProfile_Definitions" = None):
        self.type = type
        self.direction = direction
        self.BPMNProfile_BPMNRelationship121 = BPMNProfile_BPMNRelationship121
        self.BPMNProfile_BPMNRelationship123 = BPMNProfile_BPMNRelationship123 if BPMNProfile_BPMNRelationship123 is not None else set()
        self.BPMNProfile_BPMNRelationship = BPMNProfile_BPMNRelationship
        self.BPMNProfile_BPMNRelationship126 = BPMNProfile_BPMNRelationship126 if BPMNProfile_BPMNRelationship126 is not None else set()
        self.BPMNProfile_BPMNRelationship129 = BPMNProfile_BPMNRelationship129
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def BPMNProfile_BPMNRelationship129(self):
        return self.__BPMNProfile_BPMNRelationship129

    @BPMNProfile_BPMNRelationship129.setter
    def BPMNProfile_BPMNRelationship129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNRelationship__BPMNProfile_BPMNRelationship129", None)
        self.__BPMNProfile_BPMNRelationship129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Definitions130"):
                opp_val = getattr(old_value, "BPMNProfile_Definitions130", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Definitions130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Definitions130"):
                opp_val = getattr(value, "BPMNProfile_Definitions130", None)
                setattr(value, "BPMNProfile_Definitions130", self)

    @property
    def BPMNProfile_BPMNRelationship121(self):
        return self.__BPMNProfile_BPMNRelationship121

    @BPMNProfile_BPMNRelationship121.setter
    def BPMNProfile_BPMNRelationship121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNRelationship__BPMNProfile_BPMNRelationship121", None)
        self.__BPMNProfile_BPMNRelationship121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Constraint"):
                opp_val = getattr(old_value, "BPMNProfile_Constraint", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Constraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Constraint"):
                opp_val = getattr(value, "BPMNProfile_Constraint", None)
                setattr(value, "BPMNProfile_Constraint", self)

    @property
    def BPMNProfile_BPMNRelationship126(self):
        return self.__BPMNProfile_BPMNRelationship126

    @BPMNProfile_BPMNRelationship126.setter
    def BPMNProfile_BPMNRelationship126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNRelationship__BPMNProfile_BPMNRelationship126", None)
        self.__BPMNProfile_BPMNRelationship126 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_Element127"):
                    opp_val = getattr(item, "BPMNProfile_Element127", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_Element127", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_Element127"):
                    opp_val = getattr(item, "BPMNProfile_Element127", None)
                    
                    setattr(item, "BPMNProfile_Element127", self)
                    

    @property
    def BPMNProfile_BPMNRelationship(self):
        return self.__BPMNProfile_BPMNRelationship

    @BPMNProfile_BPMNRelationship.setter
    def BPMNProfile_BPMNRelationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNRelationship__BPMNProfile_BPMNRelationship", None)
        self.__BPMNProfile_BPMNRelationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Definitions107"):
                opp_val = getattr(old_value, "BPMNProfile_Definitions107", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Definitions107"):
                opp_val = getattr(value, "BPMNProfile_Definitions107", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_Definitions107", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_BPMNRelationship123(self):
        return self.__BPMNProfile_BPMNRelationship123

    @BPMNProfile_BPMNRelationship123.setter
    def BPMNProfile_BPMNRelationship123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNRelationship__BPMNProfile_BPMNRelationship123", None)
        self.__BPMNProfile_BPMNRelationship123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_Element124"):
                    opp_val = getattr(item, "BPMNProfile_Element124", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_Element124", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_Element124"):
                    opp_val = getattr(item, "BPMNProfile_Element124", None)
                    
                    setattr(item, "BPMNProfile_Element124", self)
                    

class BPMNProfile_CategoryValue(BaseElement):

    pass
class BPMNProfile_Definitions(BaseElement):

    def __init__(self, targetNamespace: str, expressionLanguage: str, typeLanguage: str, exporter: str, exporterVersion: str, Definitions: "BPMNProfile_RootElement" = None, BPMNProfile_Definitions: "BPMNProfile_Package" = None, BPMNProfile_Definitions103: set["BPMNProfile_BPMNExtension"] = None, BPMNProfile_Definitions105: set["BPMNProfile_Import"] = None, BPMNProfile_Definitions107: set["BPMNProfile_BPMNRelationship"] = None, definition: set["BPMNProfile_RootElement"] = None, BPMNProfile_Definitions119: "BPMNProfile_Import" = None, BPMNProfile_Definitions130: "BPMNProfile_BPMNRelationship" = None):
        self.targetNamespace = targetNamespace
        self.expressionLanguage = expressionLanguage
        self.typeLanguage = typeLanguage
        self.exporter = exporter
        self.exporterVersion = exporterVersion
        self.Definitions = Definitions
        self.BPMNProfile_Definitions = BPMNProfile_Definitions
        self.BPMNProfile_Definitions103 = BPMNProfile_Definitions103 if BPMNProfile_Definitions103 is not None else set()
        self.BPMNProfile_Definitions105 = BPMNProfile_Definitions105 if BPMNProfile_Definitions105 is not None else set()
        self.BPMNProfile_Definitions107 = BPMNProfile_Definitions107 if BPMNProfile_Definitions107 is not None else set()
        self.definition = definition if definition is not None else set()
        self.BPMNProfile_Definitions119 = BPMNProfile_Definitions119
        self.BPMNProfile_Definitions130 = BPMNProfile_Definitions130
        
    @property
    def exporter(self) -> str:
        return self.__exporter

    @exporter.setter
    def exporter(self, exporter: str):
        self.__exporter = exporter

    @property
    def exporterVersion(self) -> str:
        return self.__exporterVersion

    @exporterVersion.setter
    def exporterVersion(self, exporterVersion: str):
        self.__exporterVersion = exporterVersion

    @property
    def targetNamespace(self) -> str:
        return self.__targetNamespace

    @targetNamespace.setter
    def targetNamespace(self, targetNamespace: str):
        self.__targetNamespace = targetNamespace

    @property
    def typeLanguage(self) -> str:
        return self.__typeLanguage

    @typeLanguage.setter
    def typeLanguage(self, typeLanguage: str):
        self.__typeLanguage = typeLanguage

    @property
    def expressionLanguage(self) -> str:
        return self.__expressionLanguage

    @expressionLanguage.setter
    def expressionLanguage(self, expressionLanguage: str):
        self.__expressionLanguage = expressionLanguage

    @property
    def BPMNProfile_Definitions107(self):
        return self.__BPMNProfile_Definitions107

    @BPMNProfile_Definitions107.setter
    def BPMNProfile_Definitions107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Definitions__BPMNProfile_Definitions107", None)
        self.__BPMNProfile_Definitions107 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_BPMNRelationship"):
                    opp_val = getattr(item, "BPMNProfile_BPMNRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_BPMNRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_BPMNRelationship"):
                    opp_val = getattr(item, "BPMNProfile_BPMNRelationship", None)
                    
                    setattr(item, "BPMNProfile_BPMNRelationship", self)
                    

    @property
    def BPMNProfile_Definitions130(self):
        return self.__BPMNProfile_Definitions130

    @BPMNProfile_Definitions130.setter
    def BPMNProfile_Definitions130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Definitions__BPMNProfile_Definitions130", None)
        self.__BPMNProfile_Definitions130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNRelationship129"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNRelationship129", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNRelationship129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNRelationship129"):
                opp_val = getattr(value, "BPMNProfile_BPMNRelationship129", None)
                setattr(value, "BPMNProfile_BPMNRelationship129", self)

    @property
    def BPMNProfile_Definitions(self):
        return self.__BPMNProfile_Definitions

    @BPMNProfile_Definitions.setter
    def BPMNProfile_Definitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Definitions__BPMNProfile_Definitions", None)
        self.__BPMNProfile_Definitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Package"):
                opp_val = getattr(old_value, "BPMNProfile_Package", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Package"):
                opp_val = getattr(value, "BPMNProfile_Package", None)
                setattr(value, "BPMNProfile_Package", self)

    @property
    def BPMNProfile_Definitions105(self):
        return self.__BPMNProfile_Definitions105

    @BPMNProfile_Definitions105.setter
    def BPMNProfile_Definitions105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Definitions__BPMNProfile_Definitions105", None)
        self.__BPMNProfile_Definitions105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_Import"):
                    opp_val = getattr(item, "BPMNProfile_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_Import"):
                    opp_val = getattr(item, "BPMNProfile_Import", None)
                    
                    setattr(item, "BPMNProfile_Import", self)
                    

    @property
    def Definitions(self):
        return self.__Definitions

    @Definitions.setter
    def Definitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Definitions__Definitions", None)
        self.__Definitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rootElements"):
                opp_val = getattr(old_value, "rootElements", None)
                if opp_val == self:
                    setattr(old_value, "rootElements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rootElements"):
                opp_val = getattr(value, "rootElements", None)
                setattr(value, "rootElements", self)

    @property
    def definition(self):
        return self.__definition

    @definition.setter
    def definition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Definitions__definition", None)
        self.__definition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RootElement"):
                    opp_val = getattr(item, "RootElement", None)
                    
                    if opp_val == self:
                        setattr(item, "RootElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RootElement"):
                    opp_val = getattr(item, "RootElement", None)
                    
                    setattr(item, "RootElement", self)
                    

    @property
    def BPMNProfile_Definitions119(self):
        return self.__BPMNProfile_Definitions119

    @BPMNProfile_Definitions119.setter
    def BPMNProfile_Definitions119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Definitions__BPMNProfile_Definitions119", None)
        self.__BPMNProfile_Definitions119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Import118"):
                opp_val = getattr(old_value, "BPMNProfile_Import118", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Import118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Import118"):
                opp_val = getattr(value, "BPMNProfile_Import118", None)
                setattr(value, "BPMNProfile_Import118", self)

    @property
    def BPMNProfile_Definitions103(self):
        return self.__BPMNProfile_Definitions103

    @BPMNProfile_Definitions103.setter
    def BPMNProfile_Definitions103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Definitions__BPMNProfile_Definitions103", None)
        self.__BPMNProfile_Definitions103 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_BPMNExtension"):
                    opp_val = getattr(item, "BPMNProfile_BPMNExtension", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_BPMNExtension", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_BPMNExtension"):
                    opp_val = getattr(item, "BPMNProfile_BPMNExtension", None)
                    
                    setattr(item, "BPMNProfile_BPMNExtension", self)
                    

class BPMNProfile_InputSet(BaseElement):

    def __init__(self, BPMNProfile_InputSet: "BPMNProfile_InputOutputSpecification" = None, InputSet: "BPMNProfile_DataInput" = None, InputSet176: "BPMNProfile_DataInput" = None, InputSet178: "BPMNProfile_DataInput" = None, BPMNProfile_InputSet196: "BPMNProfile_ParameterSet" = None, inputSetWithOptional: set["BPMNProfile_DataInput"] = None, inputSetWithWhileExecuting: set["BPMNProfile_DataInput"] = None, inputSetRefs: set["BPMNProfile_DataInput"] = None, BPMNProfile_InputSet254: "BPMNProfile_InputOutputBinding" = None):
        self.BPMNProfile_InputSet = BPMNProfile_InputSet
        self.InputSet = InputSet
        self.InputSet176 = InputSet176
        self.InputSet178 = InputSet178
        self.BPMNProfile_InputSet196 = BPMNProfile_InputSet196
        self.inputSetWithOptional = inputSetWithOptional if inputSetWithOptional is not None else set()
        self.inputSetWithWhileExecuting = inputSetWithWhileExecuting if inputSetWithWhileExecuting is not None else set()
        self.inputSetRefs = inputSetRefs if inputSetRefs is not None else set()
        self.BPMNProfile_InputSet254 = BPMNProfile_InputSet254
        
    @property
    def inputSetWithWhileExecuting(self):
        return self.__inputSetWithWhileExecuting

    @inputSetWithWhileExecuting.setter
    def inputSetWithWhileExecuting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_InputSet__inputSetWithWhileExecuting", None)
        self.__inputSetWithWhileExecuting = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataInput199"):
                    opp_val = getattr(item, "DataInput199", None)
                    
                    if opp_val == self:
                        setattr(item, "DataInput199", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataInput199"):
                    opp_val = getattr(item, "DataInput199", None)
                    
                    setattr(item, "DataInput199", self)
                    

    @property
    def inputSetRefs(self):
        return self.__inputSetRefs

    @inputSetRefs.setter
    def inputSetRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_InputSet__inputSetRefs", None)
        self.__inputSetRefs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataInput201"):
                    opp_val = getattr(item, "DataInput201", None)
                    
                    if opp_val == self:
                        setattr(item, "DataInput201", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataInput201"):
                    opp_val = getattr(item, "DataInput201", None)
                    
                    setattr(item, "DataInput201", self)
                    

    @property
    def InputSet176(self):
        return self.__InputSet176

    @InputSet176.setter
    def InputSet176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_InputSet__InputSet176", None)
        self.__InputSet176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optionalInputRefs"):
                opp_val = getattr(old_value, "optionalInputRefs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optionalInputRefs"):
                opp_val = getattr(value, "optionalInputRefs", None)
                if opp_val is None:
                    setattr(value, "optionalInputRefs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_InputSet(self):
        return self.__BPMNProfile_InputSet

    @BPMNProfile_InputSet.setter
    def BPMNProfile_InputSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_InputSet__BPMNProfile_InputSet", None)
        self.__BPMNProfile_InputSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_InputOutputSpecification165"):
                opp_val = getattr(old_value, "BPMNProfile_InputOutputSpecification165", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_InputOutputSpecification165"):
                opp_val = getattr(value, "BPMNProfile_InputOutputSpecification165", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_InputOutputSpecification165", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_InputSet254(self):
        return self.__BPMNProfile_InputSet254

    @BPMNProfile_InputSet254.setter
    def BPMNProfile_InputSet254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_InputSet__BPMNProfile_InputSet254", None)
        self.__BPMNProfile_InputSet254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_InputOutputBinding253"):
                opp_val = getattr(old_value, "BPMNProfile_InputOutputBinding253", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_InputOutputBinding253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_InputOutputBinding253"):
                opp_val = getattr(value, "BPMNProfile_InputOutputBinding253", None)
                setattr(value, "BPMNProfile_InputOutputBinding253", self)

    @property
    def InputSet(self):
        return self.__InputSet

    @InputSet.setter
    def InputSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_InputSet__InputSet", None)
        self.__InputSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataInputRefs"):
                opp_val = getattr(old_value, "dataInputRefs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataInputRefs"):
                opp_val = getattr(value, "dataInputRefs", None)
                if opp_val is None:
                    setattr(value, "dataInputRefs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_InputSet196(self):
        return self.__BPMNProfile_InputSet196

    @BPMNProfile_InputSet196.setter
    def BPMNProfile_InputSet196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_InputSet__BPMNProfile_InputSet196", None)
        self.__BPMNProfile_InputSet196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ParameterSet"):
                opp_val = getattr(old_value, "BPMNProfile_ParameterSet", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ParameterSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ParameterSet"):
                opp_val = getattr(value, "BPMNProfile_ParameterSet", None)
                setattr(value, "BPMNProfile_ParameterSet", self)

    @property
    def InputSet178(self):
        return self.__InputSet178

    @InputSet178.setter
    def InputSet178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_InputSet__InputSet178", None)
        self.__InputSet178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileExecutingInputRefs"):
                opp_val = getattr(old_value, "whileExecutingInputRefs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileExecutingInputRefs"):
                opp_val = getattr(value, "whileExecutingInputRefs", None)
                if opp_val is None:
                    setattr(value, "whileExecutingInputRefs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def inputSetWithOptional(self):
        return self.__inputSetWithOptional

    @inputSetWithOptional.setter
    def inputSetWithOptional(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_InputSet__inputSetWithOptional", None)
        self.__inputSetWithOptional = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataInput"):
                    opp_val = getattr(item, "DataInput", None)
                    
                    if opp_val == self:
                        setattr(item, "DataInput", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataInput"):
                    opp_val = getattr(item, "DataInput", None)
                    
                    setattr(item, "DataInput", self)
                    

    def InputSetdataInputRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement InputSetdataInputRefs method
        pass

    def InputSetoptionalInputRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement InputSetoptionalInputRefs method
        pass

    def InputSetwhileExecutingInputRefs(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement InputSetwhileExecutingInputRefs method
        pass

class BPMNProfile_CorrelationSubscription(BaseElement):

    pass
class BPMNProfile_Assignment(BaseElement):

    pass
class BPMNProfile_ResourceParameterBinding(BaseElement):

    def __init__(self, BPMNProfile_ResourceParameterBinding: "BPMNProfile_ResourceRole" = None, BPMNProfile_ResourceParameterBinding423: "BPMNProfile_Slot" = None, BPMNProfile_ResourceParameterBinding426: "BPMNProfile_ResourceParameter" = None, BPMNProfile_ResourceParameterBinding429: "BPMNProfile_BPMNExpression" = None):
        self.BPMNProfile_ResourceParameterBinding = BPMNProfile_ResourceParameterBinding
        self.BPMNProfile_ResourceParameterBinding423 = BPMNProfile_ResourceParameterBinding423
        self.BPMNProfile_ResourceParameterBinding426 = BPMNProfile_ResourceParameterBinding426
        self.BPMNProfile_ResourceParameterBinding429 = BPMNProfile_ResourceParameterBinding429
        
    @property
    def BPMNProfile_ResourceParameterBinding426(self):
        return self.__BPMNProfile_ResourceParameterBinding426

    @BPMNProfile_ResourceParameterBinding426.setter
    def BPMNProfile_ResourceParameterBinding426(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceParameterBinding__BPMNProfile_ResourceParameterBinding426", None)
        self.__BPMNProfile_ResourceParameterBinding426 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ResourceParameter427"):
                opp_val = getattr(old_value, "BPMNProfile_ResourceParameter427", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ResourceParameter427", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ResourceParameter427"):
                opp_val = getattr(value, "BPMNProfile_ResourceParameter427", None)
                setattr(value, "BPMNProfile_ResourceParameter427", self)

    @property
    def BPMNProfile_ResourceParameterBinding429(self):
        return self.__BPMNProfile_ResourceParameterBinding429

    @BPMNProfile_ResourceParameterBinding429.setter
    def BPMNProfile_ResourceParameterBinding429(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceParameterBinding__BPMNProfile_ResourceParameterBinding429", None)
        self.__BPMNProfile_ResourceParameterBinding429 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNExpression430"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNExpression430", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNExpression430", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNExpression430"):
                opp_val = getattr(value, "BPMNProfile_BPMNExpression430", None)
                setattr(value, "BPMNProfile_BPMNExpression430", self)

    @property
    def BPMNProfile_ResourceParameterBinding423(self):
        return self.__BPMNProfile_ResourceParameterBinding423

    @BPMNProfile_ResourceParameterBinding423.setter
    def BPMNProfile_ResourceParameterBinding423(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceParameterBinding__BPMNProfile_ResourceParameterBinding423", None)
        self.__BPMNProfile_ResourceParameterBinding423 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Slot424"):
                opp_val = getattr(old_value, "BPMNProfile_Slot424", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Slot424", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Slot424"):
                opp_val = getattr(value, "BPMNProfile_Slot424", None)
                setattr(value, "BPMNProfile_Slot424", self)

    @property
    def BPMNProfile_ResourceParameterBinding(self):
        return self.__BPMNProfile_ResourceParameterBinding

    @BPMNProfile_ResourceParameterBinding.setter
    def BPMNProfile_ResourceParameterBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceParameterBinding__BPMNProfile_ResourceParameterBinding", None)
        self.__BPMNProfile_ResourceParameterBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ResourceRole409"):
                opp_val = getattr(old_value, "BPMNProfile_ResourceRole409", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ResourceRole409"):
                opp_val = getattr(value, "BPMNProfile_ResourceRole409", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_ResourceRole409", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def ResourceParameterBindingparameterRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceParameterBindingparameterRef method
        pass

    def ResourceParameterBindingexpression(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceParameterBindingexpression method
        pass

class BPMNProfile_Lane(BaseElement):

    def __init__(self, BPMNProfile_Lane60: "BPMNProfile_ActivityPartition" = None, Lane: "BPMNProfile_LaneSet" = None, BPMNProfile_Lane: "BPMNProfile_LaneSet" = None, BPMNProfile_Lane63: "BPMNProfile_Element" = None, BPMNProfile_Lane66: set["BPMNProfile_FlowNode"] = None, BPMNProfile_Lane69: "BPMNProfile_BaseElement" = None, BPMNProfile_Lane72: "BPMNProfile_LaneSet" = None, lanes: "BPMNProfile_LaneSet" = None):
        self.BPMNProfile_Lane60 = BPMNProfile_Lane60
        self.Lane = Lane
        self.BPMNProfile_Lane = BPMNProfile_Lane
        self.BPMNProfile_Lane63 = BPMNProfile_Lane63
        self.BPMNProfile_Lane66 = BPMNProfile_Lane66 if BPMNProfile_Lane66 is not None else set()
        self.BPMNProfile_Lane69 = BPMNProfile_Lane69
        self.BPMNProfile_Lane72 = BPMNProfile_Lane72
        self.lanes = lanes
        
    @property
    def BPMNProfile_Lane69(self):
        return self.__BPMNProfile_Lane69

    @BPMNProfile_Lane69.setter
    def BPMNProfile_Lane69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Lane__BPMNProfile_Lane69", None)
        self.__BPMNProfile_Lane69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BaseElement70"):
                opp_val = getattr(old_value, "BPMNProfile_BaseElement70", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BaseElement70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BaseElement70"):
                opp_val = getattr(value, "BPMNProfile_BaseElement70", None)
                setattr(value, "BPMNProfile_BaseElement70", self)

    @property
    def BPMNProfile_Lane(self):
        return self.__BPMNProfile_Lane

    @BPMNProfile_Lane.setter
    def BPMNProfile_Lane(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Lane__BPMNProfile_Lane", None)
        self.__BPMNProfile_Lane = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_LaneSet56"):
                opp_val = getattr(old_value, "BPMNProfile_LaneSet56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_LaneSet56"):
                opp_val = getattr(value, "BPMNProfile_LaneSet56", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_LaneSet56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_Lane66(self):
        return self.__BPMNProfile_Lane66

    @BPMNProfile_Lane66.setter
    def BPMNProfile_Lane66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Lane__BPMNProfile_Lane66", None)
        self.__BPMNProfile_Lane66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_FlowNode67"):
                    opp_val = getattr(item, "BPMNProfile_FlowNode67", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_FlowNode67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_FlowNode67"):
                    opp_val = getattr(item, "BPMNProfile_FlowNode67", None)
                    
                    setattr(item, "BPMNProfile_FlowNode67", self)
                    

    @property
    def Lane(self):
        return self.__Lane

    @Lane.setter
    def Lane(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Lane__Lane", None)
        self.__Lane = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "laneSet"):
                opp_val = getattr(old_value, "laneSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "laneSet"):
                opp_val = getattr(value, "laneSet", None)
                if opp_val is None:
                    setattr(value, "laneSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_Lane72(self):
        return self.__BPMNProfile_Lane72

    @BPMNProfile_Lane72.setter
    def BPMNProfile_Lane72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Lane__BPMNProfile_Lane72", None)
        self.__BPMNProfile_Lane72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_LaneSet73"):
                opp_val = getattr(old_value, "BPMNProfile_LaneSet73", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_LaneSet73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_LaneSet73"):
                opp_val = getattr(value, "BPMNProfile_LaneSet73", None)
                setattr(value, "BPMNProfile_LaneSet73", self)

    @property
    def BPMNProfile_Lane63(self):
        return self.__BPMNProfile_Lane63

    @BPMNProfile_Lane63.setter
    def BPMNProfile_Lane63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Lane__BPMNProfile_Lane63", None)
        self.__BPMNProfile_Lane63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Element64"):
                opp_val = getattr(old_value, "BPMNProfile_Element64", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Element64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Element64"):
                opp_val = getattr(value, "BPMNProfile_Element64", None)
                setattr(value, "BPMNProfile_Element64", self)

    @property
    def BPMNProfile_Lane60(self):
        return self.__BPMNProfile_Lane60

    @BPMNProfile_Lane60.setter
    def BPMNProfile_Lane60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Lane__BPMNProfile_Lane60", None)
        self.__BPMNProfile_Lane60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ActivityPartition61"):
                opp_val = getattr(old_value, "BPMNProfile_ActivityPartition61", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ActivityPartition61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ActivityPartition61"):
                opp_val = getattr(value, "BPMNProfile_ActivityPartition61", None)
                setattr(value, "BPMNProfile_ActivityPartition61", self)

    @property
    def lanes(self):
        return self.__lanes

    @lanes.setter
    def lanes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Lane__lanes", None)
        self.__lanes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LaneSet75"):
                opp_val = getattr(old_value, "LaneSet75", None)
                if opp_val == self:
                    setattr(old_value, "LaneSet75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LaneSet75"):
                opp_val = getattr(value, "LaneSet75", None)
                setattr(value, "LaneSet75", self)

    def LanelaneSet(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement LanelaneSet method
        pass

    def LanechildLaneSet(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement LanechildLaneSet method
        pass

    def LaneflowNodeRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement LaneflowNodeRefs method
        pass

    def LanepartitionElementRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement LanepartitionElementRef method
        pass

class BPMNProfile_Auditing(BaseElement):

    pass
class BPMNProfile_Documentation(BaseElement):

    def __init__(self, textFormat: str, text: str, BPMNProfile_Documentation33: "BPMNProfile_Comment" = None, BPMNProfile_Documentation: "BPMNProfile_BaseElement" = None):
        self.textFormat = textFormat
        self.text = text
        self.BPMNProfile_Documentation33 = BPMNProfile_Documentation33
        self.BPMNProfile_Documentation = BPMNProfile_Documentation
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def textFormat(self) -> str:
        return self.__textFormat

    @textFormat.setter
    def textFormat(self, textFormat: str):
        self.__textFormat = textFormat

    @property
    def BPMNProfile_Documentation(self):
        return self.__BPMNProfile_Documentation

    @BPMNProfile_Documentation.setter
    def BPMNProfile_Documentation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Documentation__BPMNProfile_Documentation", None)
        self.__BPMNProfile_Documentation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BaseElement17"):
                opp_val = getattr(old_value, "BPMNProfile_BaseElement17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BaseElement17"):
                opp_val = getattr(value, "BPMNProfile_BaseElement17", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BaseElement17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_Documentation33(self):
        return self.__BPMNProfile_Documentation33

    @BPMNProfile_Documentation33.setter
    def BPMNProfile_Documentation33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Documentation__BPMNProfile_Documentation33", None)
        self.__BPMNProfile_Documentation33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Comment"):
                opp_val = getattr(old_value, "BPMNProfile_Comment", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Comment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Comment"):
                opp_val = getattr(value, "BPMNProfile_Comment", None)
                setattr(value, "BPMNProfile_Comment", self)

class BPMNProfile_FlowElementsContainer(BaseElement):

    pass
class BPMNProfile_FlowElement(BaseElement):

    pass
class BPMNProfile_ActivityNode:

    pass
class FlowElement:

    pass
class BPMNProfile_DataObjectReference(ItemAwareElement, FlowElement):

    def __init__(self, BPMNProfile_DataObjectReference: "BPMNProfile_DataObject" = None, BPMNProfile_DataObjectReference574: "BPMNProfile_DataStoreNode" = None):
        self.BPMNProfile_DataObjectReference = BPMNProfile_DataObjectReference
        self.BPMNProfile_DataObjectReference574 = BPMNProfile_DataObjectReference574
        
    @property
    def BPMNProfile_DataObjectReference574(self):
        return self.__BPMNProfile_DataObjectReference574

    @BPMNProfile_DataObjectReference574.setter
    def BPMNProfile_DataObjectReference574(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataObjectReference__BPMNProfile_DataObjectReference574", None)
        self.__BPMNProfile_DataObjectReference574 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_DataStoreNode575"):
                opp_val = getattr(old_value, "BPMNProfile_DataStoreNode575", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_DataStoreNode575", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_DataStoreNode575"):
                opp_val = getattr(value, "BPMNProfile_DataStoreNode575", None)
                setattr(value, "BPMNProfile_DataStoreNode575", self)

    @property
    def BPMNProfile_DataObjectReference(self):
        return self.__BPMNProfile_DataObjectReference

    @BPMNProfile_DataObjectReference.setter
    def BPMNProfile_DataObjectReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataObjectReference__BPMNProfile_DataObjectReference", None)
        self.__BPMNProfile_DataObjectReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_DataObject"):
                opp_val = getattr(old_value, "BPMNProfile_DataObject", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_DataObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_DataObject"):
                opp_val = getattr(value, "BPMNProfile_DataObject", None)
                setattr(value, "BPMNProfile_DataObject", self)

    def DataObjectRefdataState(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement DataObjectRefdataState method
        pass

    def DataObjectRefsourcetarget(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement DataObjectRefsourcetarget method
        pass

class BPMNProfile_SequenceFlow(FlowElement):

    def __init__(self, isImmediate: str, BPMNProfile_SequenceFlow: "BPMNProfile_InclusiveGateway" = None, BPMNProfile_SequenceFlow77: "BPMNProfile_ControlFlow" = None, BPMNProfile_SequenceFlow79: "BPMNProfile_BPMNExpression" = None, BPMNProfile_SequenceFlow98: "BPMNProfile_ExclusiveGateway" = None, BPMNProfile_SequenceFlow89: "BPMNProfile_ComplexGateway" = None, BPMNProfile_SequenceFlow450: "BPMNProfile_BPMNActivity" = None):
        self.isImmediate = isImmediate
        self.BPMNProfile_SequenceFlow = BPMNProfile_SequenceFlow
        self.BPMNProfile_SequenceFlow77 = BPMNProfile_SequenceFlow77
        self.BPMNProfile_SequenceFlow79 = BPMNProfile_SequenceFlow79
        self.BPMNProfile_SequenceFlow98 = BPMNProfile_SequenceFlow98
        self.BPMNProfile_SequenceFlow89 = BPMNProfile_SequenceFlow89
        self.BPMNProfile_SequenceFlow450 = BPMNProfile_SequenceFlow450
        
    @property
    def isImmediate(self) -> str:
        return self.__isImmediate

    @isImmediate.setter
    def isImmediate(self, isImmediate: str):
        self.__isImmediate = isImmediate

    @property
    def BPMNProfile_SequenceFlow77(self):
        return self.__BPMNProfile_SequenceFlow77

    @BPMNProfile_SequenceFlow77.setter
    def BPMNProfile_SequenceFlow77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_SequenceFlow__BPMNProfile_SequenceFlow77", None)
        self.__BPMNProfile_SequenceFlow77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ControlFlow"):
                opp_val = getattr(old_value, "BPMNProfile_ControlFlow", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ControlFlow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ControlFlow"):
                opp_val = getattr(value, "BPMNProfile_ControlFlow", None)
                setattr(value, "BPMNProfile_ControlFlow", self)

    @property
    def BPMNProfile_SequenceFlow89(self):
        return self.__BPMNProfile_SequenceFlow89

    @BPMNProfile_SequenceFlow89.setter
    def BPMNProfile_SequenceFlow89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_SequenceFlow__BPMNProfile_SequenceFlow89", None)
        self.__BPMNProfile_SequenceFlow89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ComplexGateway"):
                opp_val = getattr(old_value, "BPMNProfile_ComplexGateway", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ComplexGateway", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ComplexGateway"):
                opp_val = getattr(value, "BPMNProfile_ComplexGateway", None)
                setattr(value, "BPMNProfile_ComplexGateway", self)

    @property
    def BPMNProfile_SequenceFlow(self):
        return self.__BPMNProfile_SequenceFlow

    @BPMNProfile_SequenceFlow.setter
    def BPMNProfile_SequenceFlow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_SequenceFlow__BPMNProfile_SequenceFlow", None)
        self.__BPMNProfile_SequenceFlow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_InclusiveGateway"):
                opp_val = getattr(old_value, "BPMNProfile_InclusiveGateway", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_InclusiveGateway", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_InclusiveGateway"):
                opp_val = getattr(value, "BPMNProfile_InclusiveGateway", None)
                setattr(value, "BPMNProfile_InclusiveGateway", self)

    @property
    def BPMNProfile_SequenceFlow79(self):
        return self.__BPMNProfile_SequenceFlow79

    @BPMNProfile_SequenceFlow79.setter
    def BPMNProfile_SequenceFlow79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_SequenceFlow__BPMNProfile_SequenceFlow79", None)
        self.__BPMNProfile_SequenceFlow79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNExpression"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNExpression", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNExpression"):
                opp_val = getattr(value, "BPMNProfile_BPMNExpression", None)
                setattr(value, "BPMNProfile_BPMNExpression", self)

    @property
    def BPMNProfile_SequenceFlow98(self):
        return self.__BPMNProfile_SequenceFlow98

    @BPMNProfile_SequenceFlow98.setter
    def BPMNProfile_SequenceFlow98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_SequenceFlow__BPMNProfile_SequenceFlow98", None)
        self.__BPMNProfile_SequenceFlow98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ExclusiveGateway97"):
                opp_val = getattr(old_value, "BPMNProfile_ExclusiveGateway97", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ExclusiveGateway97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ExclusiveGateway97"):
                opp_val = getattr(value, "BPMNProfile_ExclusiveGateway97", None)
                setattr(value, "BPMNProfile_ExclusiveGateway97", self)

    @property
    def BPMNProfile_SequenceFlow450(self):
        return self.__BPMNProfile_SequenceFlow450

    @BPMNProfile_SequenceFlow450.setter
    def BPMNProfile_SequenceFlow450(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_SequenceFlow__BPMNProfile_SequenceFlow450", None)
        self.__BPMNProfile_SequenceFlow450 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNActivity449"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNActivity449", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNActivity449", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNActivity449"):
                opp_val = getattr(value, "BPMNProfile_BPMNActivity449", None)
                setattr(value, "BPMNProfile_BPMNActivity449", self)

    def SequenceFlowtargetRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SequenceFlowtargetRef method
        pass

    def SequenceFlowconditionExpression(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SequenceFlowconditionExpression method
        pass

    def SequenceFlowsourceRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SequenceFlowsourceRef method
        pass

class BPMNProfile_DataStoreReference(ItemAwareElement, FlowElement):

    pass
class BPMNProfile_DataObject(ItemAwareElement, FlowElement):

    def __init__(self, isCollection: str, BPMNProfile_DataObject: "BPMNProfile_DataObjectReference" = None, BPMNProfile_DataObject577: "BPMNProfile_DataStoreNode" = None):
        self.isCollection = isCollection
        self.BPMNProfile_DataObject = BPMNProfile_DataObject
        self.BPMNProfile_DataObject577 = BPMNProfile_DataObject577
        
    @property
    def isCollection(self) -> str:
        return self.__isCollection

    @isCollection.setter
    def isCollection(self, isCollection: str):
        self.__isCollection = isCollection

    @property
    def BPMNProfile_DataObject577(self):
        return self.__BPMNProfile_DataObject577

    @BPMNProfile_DataObject577.setter
    def BPMNProfile_DataObject577(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataObject__BPMNProfile_DataObject577", None)
        self.__BPMNProfile_DataObject577 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_DataStoreNode578"):
                opp_val = getattr(old_value, "BPMNProfile_DataStoreNode578", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_DataStoreNode578", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_DataStoreNode578"):
                opp_val = getattr(value, "BPMNProfile_DataStoreNode578", None)
                setattr(value, "BPMNProfile_DataStoreNode578", self)

    @property
    def BPMNProfile_DataObject(self):
        return self.__BPMNProfile_DataObject

    @BPMNProfile_DataObject.setter
    def BPMNProfile_DataObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataObject__BPMNProfile_DataObject", None)
        self.__BPMNProfile_DataObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_DataObjectReference"):
                opp_val = getattr(old_value, "BPMNProfile_DataObjectReference", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_DataObjectReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_DataObjectReference"):
                opp_val = getattr(value, "BPMNProfile_DataObjectReference", None)
                setattr(value, "BPMNProfile_DataObjectReference", self)

    def DataObjectdataState(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement DataObjectdataState method
        pass

class BPMNProfile_FlowNode(FlowElement):

    pass
class BPMNProfile_ActivityGroup:

    pass
class BPMNProfile_ControlNode:

    pass
class FlowNode:

    pass
class BPMNProfile_BPMNActivity(FlowNode):

    def __init__(self, isForCompensation: str, startQuantity: str, completionQuantity: str, BPMNProfile_BPMNActivity440: "BPMNProfile_Action" = None, BPMNProfile_BPMNActivity: "BPMNProfile_CompensateEventDefinition" = None, BPMNProfile_BPMNActivity443: "BPMNProfile_Class" = None, BPMNProfile_BPMNActivity446: set["BPMNProfile_BPMNProperty"] = None, BPMNProfile_BPMNActivity449: "BPMNProfile_SequenceFlow" = None, BPMNProfile_BPMNActivity452: set["BPMNProfile_BoundaryEvent"] = None, BPMNProfile_BPMNActivity454: set["BPMNProfile_DataInputAssociation"] = None, BPMNProfile_BPMNActivity456: set["BPMNProfile_DataOutputAssociation"] = None, BPMNProfile_BPMNActivity458: "BPMNProfile_LoopCharacteristics" = None, BPMNProfile_BPMNActivity460: set["BPMNProfile_ResourceRole"] = None, BPMNProfile_BPMNActivity464: "BPMNProfile_BoundaryEvent" = None):
        self.isForCompensation = isForCompensation
        self.startQuantity = startQuantity
        self.completionQuantity = completionQuantity
        self.BPMNProfile_BPMNActivity440 = BPMNProfile_BPMNActivity440
        self.BPMNProfile_BPMNActivity = BPMNProfile_BPMNActivity
        self.BPMNProfile_BPMNActivity443 = BPMNProfile_BPMNActivity443
        self.BPMNProfile_BPMNActivity446 = BPMNProfile_BPMNActivity446 if BPMNProfile_BPMNActivity446 is not None else set()
        self.BPMNProfile_BPMNActivity449 = BPMNProfile_BPMNActivity449
        self.BPMNProfile_BPMNActivity452 = BPMNProfile_BPMNActivity452 if BPMNProfile_BPMNActivity452 is not None else set()
        self.BPMNProfile_BPMNActivity454 = BPMNProfile_BPMNActivity454 if BPMNProfile_BPMNActivity454 is not None else set()
        self.BPMNProfile_BPMNActivity456 = BPMNProfile_BPMNActivity456 if BPMNProfile_BPMNActivity456 is not None else set()
        self.BPMNProfile_BPMNActivity458 = BPMNProfile_BPMNActivity458
        self.BPMNProfile_BPMNActivity460 = BPMNProfile_BPMNActivity460 if BPMNProfile_BPMNActivity460 is not None else set()
        self.BPMNProfile_BPMNActivity464 = BPMNProfile_BPMNActivity464
        
    @property
    def isForCompensation(self) -> str:
        return self.__isForCompensation

    @isForCompensation.setter
    def isForCompensation(self, isForCompensation: str):
        self.__isForCompensation = isForCompensation

    @property
    def startQuantity(self) -> str:
        return self.__startQuantity

    @startQuantity.setter
    def startQuantity(self, startQuantity: str):
        self.__startQuantity = startQuantity

    @property
    def completionQuantity(self) -> str:
        return self.__completionQuantity

    @completionQuantity.setter
    def completionQuantity(self, completionQuantity: str):
        self.__completionQuantity = completionQuantity

    @property
    def BPMNProfile_BPMNActivity443(self):
        return self.__BPMNProfile_BPMNActivity443

    @BPMNProfile_BPMNActivity443.setter
    def BPMNProfile_BPMNActivity443(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNActivity__BPMNProfile_BPMNActivity443", None)
        self.__BPMNProfile_BPMNActivity443 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Class444"):
                opp_val = getattr(old_value, "BPMNProfile_Class444", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Class444", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Class444"):
                opp_val = getattr(value, "BPMNProfile_Class444", None)
                setattr(value, "BPMNProfile_Class444", self)

    @property
    def BPMNProfile_BPMNActivity440(self):
        return self.__BPMNProfile_BPMNActivity440

    @BPMNProfile_BPMNActivity440.setter
    def BPMNProfile_BPMNActivity440(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNActivity__BPMNProfile_BPMNActivity440", None)
        self.__BPMNProfile_BPMNActivity440 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Action441"):
                opp_val = getattr(old_value, "BPMNProfile_Action441", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Action441", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Action441"):
                opp_val = getattr(value, "BPMNProfile_Action441", None)
                setattr(value, "BPMNProfile_Action441", self)

    @property
    def BPMNProfile_BPMNActivity454(self):
        return self.__BPMNProfile_BPMNActivity454

    @BPMNProfile_BPMNActivity454.setter
    def BPMNProfile_BPMNActivity454(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNActivity__BPMNProfile_BPMNActivity454", None)
        self.__BPMNProfile_BPMNActivity454 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_DataInputAssociation"):
                    opp_val = getattr(item, "BPMNProfile_DataInputAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_DataInputAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_DataInputAssociation"):
                    opp_val = getattr(item, "BPMNProfile_DataInputAssociation", None)
                    
                    setattr(item, "BPMNProfile_DataInputAssociation", self)
                    

    @property
    def BPMNProfile_BPMNActivity(self):
        return self.__BPMNProfile_BPMNActivity

    @BPMNProfile_BPMNActivity.setter
    def BPMNProfile_BPMNActivity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNActivity__BPMNProfile_BPMNActivity", None)
        self.__BPMNProfile_BPMNActivity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CompensateEventDefinition"):
                opp_val = getattr(old_value, "BPMNProfile_CompensateEventDefinition", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_CompensateEventDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CompensateEventDefinition"):
                opp_val = getattr(value, "BPMNProfile_CompensateEventDefinition", None)
                setattr(value, "BPMNProfile_CompensateEventDefinition", self)

    @property
    def BPMNProfile_BPMNActivity460(self):
        return self.__BPMNProfile_BPMNActivity460

    @BPMNProfile_BPMNActivity460.setter
    def BPMNProfile_BPMNActivity460(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNActivity__BPMNProfile_BPMNActivity460", None)
        self.__BPMNProfile_BPMNActivity460 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_ResourceRole461"):
                    opp_val = getattr(item, "BPMNProfile_ResourceRole461", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_ResourceRole461", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_ResourceRole461"):
                    opp_val = getattr(item, "BPMNProfile_ResourceRole461", None)
                    
                    setattr(item, "BPMNProfile_ResourceRole461", self)
                    

    @property
    def BPMNProfile_BPMNActivity449(self):
        return self.__BPMNProfile_BPMNActivity449

    @BPMNProfile_BPMNActivity449.setter
    def BPMNProfile_BPMNActivity449(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNActivity__BPMNProfile_BPMNActivity449", None)
        self.__BPMNProfile_BPMNActivity449 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_SequenceFlow450"):
                opp_val = getattr(old_value, "BPMNProfile_SequenceFlow450", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_SequenceFlow450", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_SequenceFlow450"):
                opp_val = getattr(value, "BPMNProfile_SequenceFlow450", None)
                setattr(value, "BPMNProfile_SequenceFlow450", self)

    @property
    def BPMNProfile_BPMNActivity464(self):
        return self.__BPMNProfile_BPMNActivity464

    @BPMNProfile_BPMNActivity464.setter
    def BPMNProfile_BPMNActivity464(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNActivity__BPMNProfile_BPMNActivity464", None)
        self.__BPMNProfile_BPMNActivity464 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BoundaryEvent463"):
                opp_val = getattr(old_value, "BPMNProfile_BoundaryEvent463", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BoundaryEvent463", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BoundaryEvent463"):
                opp_val = getattr(value, "BPMNProfile_BoundaryEvent463", None)
                setattr(value, "BPMNProfile_BoundaryEvent463", self)

    @property
    def BPMNProfile_BPMNActivity446(self):
        return self.__BPMNProfile_BPMNActivity446

    @BPMNProfile_BPMNActivity446.setter
    def BPMNProfile_BPMNActivity446(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNActivity__BPMNProfile_BPMNActivity446", None)
        self.__BPMNProfile_BPMNActivity446 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_BPMNProperty447"):
                    opp_val = getattr(item, "BPMNProfile_BPMNProperty447", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_BPMNProperty447", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_BPMNProperty447"):
                    opp_val = getattr(item, "BPMNProfile_BPMNProperty447", None)
                    
                    setattr(item, "BPMNProfile_BPMNProperty447", self)
                    

    @property
    def BPMNProfile_BPMNActivity452(self):
        return self.__BPMNProfile_BPMNActivity452

    @BPMNProfile_BPMNActivity452.setter
    def BPMNProfile_BPMNActivity452(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNActivity__BPMNProfile_BPMNActivity452", None)
        self.__BPMNProfile_BPMNActivity452 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_BoundaryEvent"):
                    opp_val = getattr(item, "BPMNProfile_BoundaryEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_BoundaryEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_BoundaryEvent"):
                    opp_val = getattr(item, "BPMNProfile_BoundaryEvent", None)
                    
                    setattr(item, "BPMNProfile_BoundaryEvent", self)
                    

    @property
    def BPMNProfile_BPMNActivity456(self):
        return self.__BPMNProfile_BPMNActivity456

    @BPMNProfile_BPMNActivity456.setter
    def BPMNProfile_BPMNActivity456(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNActivity__BPMNProfile_BPMNActivity456", None)
        self.__BPMNProfile_BPMNActivity456 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_DataOutputAssociation"):
                    opp_val = getattr(item, "BPMNProfile_DataOutputAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_DataOutputAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_DataOutputAssociation"):
                    opp_val = getattr(item, "BPMNProfile_DataOutputAssociation", None)
                    
                    setattr(item, "BPMNProfile_DataOutputAssociation", self)
                    

    @property
    def BPMNProfile_BPMNActivity458(self):
        return self.__BPMNProfile_BPMNActivity458

    @BPMNProfile_BPMNActivity458.setter
    def BPMNProfile_BPMNActivity458(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNActivity__BPMNProfile_BPMNActivity458", None)
        self.__BPMNProfile_BPMNActivity458 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_LoopCharacteristics"):
                opp_val = getattr(old_value, "BPMNProfile_LoopCharacteristics", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_LoopCharacteristics", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_LoopCharacteristics"):
                opp_val = getattr(value, "BPMNProfile_LoopCharacteristics", None)
                setattr(value, "BPMNProfile_LoopCharacteristics", self)

    def BPMNActivitycontainer(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement BPMNActivitycontainer method
        pass

    def BPMNActivityproperties(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement BPMNActivityproperties method
        pass

    def BPMNActivityboundaryEventsRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement BPMNActivityboundaryEventsRefs method
        pass

    def BPMNActivityloopCharacteristics(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BPMNActivityloopCharacteristics method
        pass

    def BPMNActivitydefault(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BPMNActivitydefault method
        pass

    def BPMNActivityresources(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BPMNActivityresources method
        pass

class BPMNProfile_BPMNEvent(FlowNode):

    pass
class BPMNProfile_Gateway(FlowNode):

    pass
class BPMNProfile_Comment:

    pass
class BPMNProfile_ForkNode:

    pass
class BPMNProfile_JoinNode:

    pass