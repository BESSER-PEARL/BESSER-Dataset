from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class GatewayDirection(Enum):
    mixed = "mixed"
    unspecified = "unspecified"
    converging = "converging"
    diverging = "diverging"
class ProcessType(Enum):
    none = "none"
    public = "public"
    private = "private"
class AssociationDirection(Enum):
    none = "none"
    one = "one"
    both = "both"
class ItemKind(Enum):
    physical = "physical"
    information = "information"
class MultiInstanceBehavior(Enum):
    none = "none"
    one = "one"
    all = "all"
    complex = "complex"
class EventBasedGatewayType(Enum):
    exclusive = "exclusive"
    parallel = "parallel"
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

class bpmnprof_ExpansionRegion:

    pass
class bpmnprof_LoopNode:

    pass
class LoopCharacteristics:

    pass
class bpmnprof_MultiInstanceLoopCharacteristics(LoopCharacteristics):

    def __init__(self, isSequential: str, behavior: str, bpmnprof_MultiInstanceLoopCharacteristics662: "bpmnprof_ExpansionRegion" = None, bpmnprof_MultiInstanceLoopCharacteristics664: "bpmnprof_ItemAwareElement" = None, bpmnprof_MultiInstanceLoopCharacteristics667: "bpmnprof_ItemAwareElement" = None, bpmnprof_MultiInstanceLoopCharacteristics: "bpmnprof_BPMNExpression" = None, bpmnprof_MultiInstanceLoopCharacteristics659: "bpmnprof_BPMNExpression" = None, bpmnprof_MultiInstanceLoopCharacteristics670: "bpmnprof_DataOutput" = None, bpmnprof_MultiInstanceLoopCharacteristics673: "bpmnprof_DataInput" = None, bpmnprof_MultiInstanceLoopCharacteristics676: "bpmnprof_EventDefinition" = None, bpmnprof_MultiInstanceLoopCharacteristics679: "bpmnprof_EventDefinition" = None, bpmnprof_MultiInstanceLoopCharacteristics682: set["bpmnprof_ComplexBehaviorDefinition"] = None):
        self.isSequential = isSequential
        self.behavior = behavior
        self.bpmnprof_MultiInstanceLoopCharacteristics662 = bpmnprof_MultiInstanceLoopCharacteristics662
        self.bpmnprof_MultiInstanceLoopCharacteristics664 = bpmnprof_MultiInstanceLoopCharacteristics664
        self.bpmnprof_MultiInstanceLoopCharacteristics667 = bpmnprof_MultiInstanceLoopCharacteristics667
        self.bpmnprof_MultiInstanceLoopCharacteristics = bpmnprof_MultiInstanceLoopCharacteristics
        self.bpmnprof_MultiInstanceLoopCharacteristics659 = bpmnprof_MultiInstanceLoopCharacteristics659
        self.bpmnprof_MultiInstanceLoopCharacteristics670 = bpmnprof_MultiInstanceLoopCharacteristics670
        self.bpmnprof_MultiInstanceLoopCharacteristics673 = bpmnprof_MultiInstanceLoopCharacteristics673
        self.bpmnprof_MultiInstanceLoopCharacteristics676 = bpmnprof_MultiInstanceLoopCharacteristics676
        self.bpmnprof_MultiInstanceLoopCharacteristics679 = bpmnprof_MultiInstanceLoopCharacteristics679
        self.bpmnprof_MultiInstanceLoopCharacteristics682 = bpmnprof_MultiInstanceLoopCharacteristics682 if bpmnprof_MultiInstanceLoopCharacteristics682 is not None else set()
        
    @property
    def behavior(self) -> str:
        return self.__behavior

    @behavior.setter
    def behavior(self, behavior: str):
        self.__behavior = behavior

    @property
    def isSequential(self) -> str:
        return self.__isSequential

    @isSequential.setter
    def isSequential(self, isSequential: str):
        self.__isSequential = isSequential

    @property
    def bpmnprof_MultiInstanceLoopCharacteristics667(self):
        return self.__bpmnprof_MultiInstanceLoopCharacteristics667

    @bpmnprof_MultiInstanceLoopCharacteristics667.setter
    def bpmnprof_MultiInstanceLoopCharacteristics667(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_MultiInstanceLoopCharacteristics__bpmnprof_MultiInstanceLoopCharacteristics667", None)
        self.__bpmnprof_MultiInstanceLoopCharacteristics667 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ItemAwareElement668"):
                opp_val = getattr(old_value, "bpmnprof_ItemAwareElement668", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ItemAwareElement668", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ItemAwareElement668"):
                opp_val = getattr(value, "bpmnprof_ItemAwareElement668", None)
                setattr(value, "bpmnprof_ItemAwareElement668", self)

    @property
    def bpmnprof_MultiInstanceLoopCharacteristics673(self):
        return self.__bpmnprof_MultiInstanceLoopCharacteristics673

    @bpmnprof_MultiInstanceLoopCharacteristics673.setter
    def bpmnprof_MultiInstanceLoopCharacteristics673(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_MultiInstanceLoopCharacteristics__bpmnprof_MultiInstanceLoopCharacteristics673", None)
        self.__bpmnprof_MultiInstanceLoopCharacteristics673 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_DataInput674"):
                opp_val = getattr(old_value, "bpmnprof_DataInput674", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_DataInput674", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_DataInput674"):
                opp_val = getattr(value, "bpmnprof_DataInput674", None)
                setattr(value, "bpmnprof_DataInput674", self)

    @property
    def bpmnprof_MultiInstanceLoopCharacteristics679(self):
        return self.__bpmnprof_MultiInstanceLoopCharacteristics679

    @bpmnprof_MultiInstanceLoopCharacteristics679.setter
    def bpmnprof_MultiInstanceLoopCharacteristics679(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_MultiInstanceLoopCharacteristics__bpmnprof_MultiInstanceLoopCharacteristics679", None)
        self.__bpmnprof_MultiInstanceLoopCharacteristics679 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_EventDefinition680"):
                opp_val = getattr(old_value, "bpmnprof_EventDefinition680", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_EventDefinition680", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_EventDefinition680"):
                opp_val = getattr(value, "bpmnprof_EventDefinition680", None)
                setattr(value, "bpmnprof_EventDefinition680", self)

    @property
    def bpmnprof_MultiInstanceLoopCharacteristics659(self):
        return self.__bpmnprof_MultiInstanceLoopCharacteristics659

    @bpmnprof_MultiInstanceLoopCharacteristics659.setter
    def bpmnprof_MultiInstanceLoopCharacteristics659(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_MultiInstanceLoopCharacteristics__bpmnprof_MultiInstanceLoopCharacteristics659", None)
        self.__bpmnprof_MultiInstanceLoopCharacteristics659 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNExpression660"):
                opp_val = getattr(old_value, "bpmnprof_BPMNExpression660", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNExpression660", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNExpression660"):
                opp_val = getattr(value, "bpmnprof_BPMNExpression660", None)
                setattr(value, "bpmnprof_BPMNExpression660", self)

    @property
    def bpmnprof_MultiInstanceLoopCharacteristics(self):
        return self.__bpmnprof_MultiInstanceLoopCharacteristics

    @bpmnprof_MultiInstanceLoopCharacteristics.setter
    def bpmnprof_MultiInstanceLoopCharacteristics(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_MultiInstanceLoopCharacteristics__bpmnprof_MultiInstanceLoopCharacteristics", None)
        self.__bpmnprof_MultiInstanceLoopCharacteristics = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNExpression657"):
                opp_val = getattr(old_value, "bpmnprof_BPMNExpression657", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNExpression657", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNExpression657"):
                opp_val = getattr(value, "bpmnprof_BPMNExpression657", None)
                setattr(value, "bpmnprof_BPMNExpression657", self)

    @property
    def bpmnprof_MultiInstanceLoopCharacteristics662(self):
        return self.__bpmnprof_MultiInstanceLoopCharacteristics662

    @bpmnprof_MultiInstanceLoopCharacteristics662.setter
    def bpmnprof_MultiInstanceLoopCharacteristics662(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_MultiInstanceLoopCharacteristics__bpmnprof_MultiInstanceLoopCharacteristics662", None)
        self.__bpmnprof_MultiInstanceLoopCharacteristics662 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ExpansionRegion"):
                opp_val = getattr(old_value, "bpmnprof_ExpansionRegion", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ExpansionRegion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ExpansionRegion"):
                opp_val = getattr(value, "bpmnprof_ExpansionRegion", None)
                setattr(value, "bpmnprof_ExpansionRegion", self)

    @property
    def bpmnprof_MultiInstanceLoopCharacteristics664(self):
        return self.__bpmnprof_MultiInstanceLoopCharacteristics664

    @bpmnprof_MultiInstanceLoopCharacteristics664.setter
    def bpmnprof_MultiInstanceLoopCharacteristics664(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_MultiInstanceLoopCharacteristics__bpmnprof_MultiInstanceLoopCharacteristics664", None)
        self.__bpmnprof_MultiInstanceLoopCharacteristics664 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ItemAwareElement665"):
                opp_val = getattr(old_value, "bpmnprof_ItemAwareElement665", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ItemAwareElement665", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ItemAwareElement665"):
                opp_val = getattr(value, "bpmnprof_ItemAwareElement665", None)
                setattr(value, "bpmnprof_ItemAwareElement665", self)

    @property
    def bpmnprof_MultiInstanceLoopCharacteristics676(self):
        return self.__bpmnprof_MultiInstanceLoopCharacteristics676

    @bpmnprof_MultiInstanceLoopCharacteristics676.setter
    def bpmnprof_MultiInstanceLoopCharacteristics676(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_MultiInstanceLoopCharacteristics__bpmnprof_MultiInstanceLoopCharacteristics676", None)
        self.__bpmnprof_MultiInstanceLoopCharacteristics676 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_EventDefinition677"):
                opp_val = getattr(old_value, "bpmnprof_EventDefinition677", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_EventDefinition677", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_EventDefinition677"):
                opp_val = getattr(value, "bpmnprof_EventDefinition677", None)
                setattr(value, "bpmnprof_EventDefinition677", self)

    @property
    def bpmnprof_MultiInstanceLoopCharacteristics682(self):
        return self.__bpmnprof_MultiInstanceLoopCharacteristics682

    @bpmnprof_MultiInstanceLoopCharacteristics682.setter
    def bpmnprof_MultiInstanceLoopCharacteristics682(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_MultiInstanceLoopCharacteristics__bpmnprof_MultiInstanceLoopCharacteristics682", None)
        self.__bpmnprof_MultiInstanceLoopCharacteristics682 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_ComplexBehaviorDefinition683"):
                    opp_val = getattr(item, "bpmnprof_ComplexBehaviorDefinition683", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_ComplexBehaviorDefinition683", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_ComplexBehaviorDefinition683"):
                    opp_val = getattr(item, "bpmnprof_ComplexBehaviorDefinition683", None)
                    
                    setattr(item, "bpmnprof_ComplexBehaviorDefinition683", self)
                    

    @property
    def bpmnprof_MultiInstanceLoopCharacteristics670(self):
        return self.__bpmnprof_MultiInstanceLoopCharacteristics670

    @bpmnprof_MultiInstanceLoopCharacteristics670.setter
    def bpmnprof_MultiInstanceLoopCharacteristics670(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_MultiInstanceLoopCharacteristics__bpmnprof_MultiInstanceLoopCharacteristics670", None)
        self.__bpmnprof_MultiInstanceLoopCharacteristics670 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_DataOutput671"):
                opp_val = getattr(old_value, "bpmnprof_DataOutput671", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_DataOutput671", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_DataOutput671"):
                opp_val = getattr(value, "bpmnprof_DataOutput671", None)
                setattr(value, "bpmnprof_DataOutput671", self)

    def MultiinstanceLoopCharacteristicstarget(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MultiinstanceLoopCharacteristicstarget method
        pass

class bpmnprof_StandardLoopCharacteristics(LoopCharacteristics):

    def __init__(self, loopMaximum: str, testBefore: str, bpmnprof_StandardLoopCharacteristics: "bpmnprof_LoopNode" = None, bpmnprof_StandardLoopCharacteristics641: "bpmnprof_BPMNExpression" = None):
        self.loopMaximum = loopMaximum
        self.testBefore = testBefore
        self.bpmnprof_StandardLoopCharacteristics = bpmnprof_StandardLoopCharacteristics
        self.bpmnprof_StandardLoopCharacteristics641 = bpmnprof_StandardLoopCharacteristics641
        
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
    def bpmnprof_StandardLoopCharacteristics(self):
        return self.__bpmnprof_StandardLoopCharacteristics

    @bpmnprof_StandardLoopCharacteristics.setter
    def bpmnprof_StandardLoopCharacteristics(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_StandardLoopCharacteristics__bpmnprof_StandardLoopCharacteristics", None)
        self.__bpmnprof_StandardLoopCharacteristics = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_LoopNode"):
                opp_val = getattr(old_value, "bpmnprof_LoopNode", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_LoopNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_LoopNode"):
                opp_val = getattr(value, "bpmnprof_LoopNode", None)
                setattr(value, "bpmnprof_LoopNode", self)

    @property
    def bpmnprof_StandardLoopCharacteristics641(self):
        return self.__bpmnprof_StandardLoopCharacteristics641

    @bpmnprof_StandardLoopCharacteristics641.setter
    def bpmnprof_StandardLoopCharacteristics641(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_StandardLoopCharacteristics__bpmnprof_StandardLoopCharacteristics641", None)
        self.__bpmnprof_StandardLoopCharacteristics641 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNExpression642"):
                opp_val = getattr(old_value, "bpmnprof_BPMNExpression642", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNExpression642", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNExpression642"):
                opp_val = getattr(value, "bpmnprof_BPMNExpression642", None)
                setattr(value, "bpmnprof_BPMNExpression642", self)

    def StandardLoopCharacteristicstestBefore(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement StandardLoopCharacteristicstestBefore method
        pass

    def StandardLoopCharacteristicsloopCondition(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement StandardLoopCharacteristicsloopCondition method
        pass

class SubProcess:

    pass
class bpmnprof_AdHocSubProcess(SubProcess):

    def __init__(self, ordering: str, cancelRemainingInstances: str, bpmnprof_AdHocSubProcess: "bpmnprof_BPMNExpression" = None):
        self.ordering = ordering
        self.cancelRemainingInstances = cancelRemainingInstances
        self.bpmnprof_AdHocSubProcess = bpmnprof_AdHocSubProcess
        
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
    def bpmnprof_AdHocSubProcess(self):
        return self.__bpmnprof_AdHocSubProcess

    @bpmnprof_AdHocSubProcess.setter
    def bpmnprof_AdHocSubProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_AdHocSubProcess__bpmnprof_AdHocSubProcess", None)
        self.__bpmnprof_AdHocSubProcess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNExpression628"):
                opp_val = getattr(old_value, "bpmnprof_BPMNExpression628", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNExpression628", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNExpression628"):
                opp_val = getattr(value, "bpmnprof_BPMNExpression628", None)
                setattr(value, "bpmnprof_BPMNExpression628", self)

    def AdHocSubProcesscancelRemainingInstances(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AdHocSubProcesscancelRemainingInstances method
        pass

class bpmnprof_Transaction(SubProcess):

    def __init__(self, method: str):
        self.method = method
        
    @property
    def method(self) -> str:
        return self.__method

    @method.setter
    def method(self, method: str):
        self.__method = method

class bpmnprof_CallBehaviorAction:

    pass
class bpmnprof_CollaborationUse:

    pass
class BPMNCollaboration:

    pass
class bpmnprof_GlobalConversation(BPMNCollaboration):

    def __init__(self):
        
    def GlobalConversationcontainedelements(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement GlobalConversationcontainedelements method
        pass

class ResourceRole:

    pass
class bpmnprof_Performer(ResourceRole):

    pass
class Performer:

    pass
class bpmnprof_HumanPerformer(Performer):

    pass
class bpmnprof_Image:

    pass
class ConversationNode:

    pass
class bpmnprof_CallConversation(ConversationNode):

    def __init__(self, bpmnprof_CallConversation: "bpmnprof_CollaborationUse" = None, bpmnprof_CallConversation604: "bpmnprof_BPMNCollaboration" = None, bpmnprof_CallConversation607: set["bpmnprof_ParticipantAssociation"] = None):
        self.bpmnprof_CallConversation = bpmnprof_CallConversation
        self.bpmnprof_CallConversation604 = bpmnprof_CallConversation604
        self.bpmnprof_CallConversation607 = bpmnprof_CallConversation607 if bpmnprof_CallConversation607 is not None else set()
        
    @property
    def bpmnprof_CallConversation(self):
        return self.__bpmnprof_CallConversation

    @bpmnprof_CallConversation.setter
    def bpmnprof_CallConversation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_CallConversation__bpmnprof_CallConversation", None)
        self.__bpmnprof_CallConversation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_CollaborationUse"):
                opp_val = getattr(old_value, "bpmnprof_CollaborationUse", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_CollaborationUse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_CollaborationUse"):
                opp_val = getattr(value, "bpmnprof_CollaborationUse", None)
                setattr(value, "bpmnprof_CollaborationUse", self)

    @property
    def bpmnprof_CallConversation607(self):
        return self.__bpmnprof_CallConversation607

    @bpmnprof_CallConversation607.setter
    def bpmnprof_CallConversation607(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_CallConversation__bpmnprof_CallConversation607", None)
        self.__bpmnprof_CallConversation607 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_ParticipantAssociation608"):
                    opp_val = getattr(item, "bpmnprof_ParticipantAssociation608", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_ParticipantAssociation608", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_ParticipantAssociation608"):
                    opp_val = getattr(item, "bpmnprof_ParticipantAssociation608", None)
                    
                    setattr(item, "bpmnprof_ParticipantAssociation608", self)
                    

    @property
    def bpmnprof_CallConversation604(self):
        return self.__bpmnprof_CallConversation604

    @bpmnprof_CallConversation604.setter
    def bpmnprof_CallConversation604(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_CallConversation__bpmnprof_CallConversation604", None)
        self.__bpmnprof_CallConversation604 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNCollaboration605"):
                opp_val = getattr(old_value, "bpmnprof_BPMNCollaboration605", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNCollaboration605", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNCollaboration605"):
                opp_val = getattr(value, "bpmnprof_BPMNCollaboration605", None)
                setattr(value, "bpmnprof_BPMNCollaboration605", self)

    def CallConversationparticipantAssociations(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement CallConversationparticipantAssociations method
        pass

    def CallConversationcalledCollaborationRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement CallConversationcalledCollaborationRef method
        pass

class bpmnprof_Conversation(ConversationNode):

    pass
class bpmnprof_SubConversation(ConversationNode):

    def __init__(self, bpmnprof_SubConversation: set["bpmnprof_ConversationNode"] = None):
        self.bpmnprof_SubConversation = bpmnprof_SubConversation if bpmnprof_SubConversation is not None else set()
        
    @property
    def bpmnprof_SubConversation(self):
        return self.__bpmnprof_SubConversation

    @bpmnprof_SubConversation.setter
    def bpmnprof_SubConversation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_SubConversation__bpmnprof_SubConversation", None)
        self.__bpmnprof_SubConversation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_ConversationNode601"):
                    opp_val = getattr(item, "bpmnprof_ConversationNode601", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_ConversationNode601", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_ConversationNode601"):
                    opp_val = getattr(item, "bpmnprof_ConversationNode601", None)
                    
                    setattr(item, "bpmnprof_ConversationNode601", self)
                    

    def SubConversationconnectedelements(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SubConversationconnectedelements method
        pass

class HumanPerformer:

    pass
class bpmnprof_PotentialOwner(HumanPerformer):

    pass
class bpmnprof_OpaqueAction:

    pass
class Task:

    pass
class bpmnprof_ReceiveTask(Task):

    def __init__(self, implementation: str, instantiate: str, bpmnprof_ReceiveTask646: "bpmnprof_AcceptEventAction" = None, bpmnprof_ReceiveTask649: "bpmnprof_BPMNOperation" = None, bpmnprof_ReceiveTask: "bpmnprof_BPMNMessage" = None):
        self.implementation = implementation
        self.instantiate = instantiate
        self.bpmnprof_ReceiveTask646 = bpmnprof_ReceiveTask646
        self.bpmnprof_ReceiveTask649 = bpmnprof_ReceiveTask649
        self.bpmnprof_ReceiveTask = bpmnprof_ReceiveTask
        
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
    def bpmnprof_ReceiveTask646(self):
        return self.__bpmnprof_ReceiveTask646

    @bpmnprof_ReceiveTask646.setter
    def bpmnprof_ReceiveTask646(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ReceiveTask__bpmnprof_ReceiveTask646", None)
        self.__bpmnprof_ReceiveTask646 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_AcceptEventAction647"):
                opp_val = getattr(old_value, "bpmnprof_AcceptEventAction647", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_AcceptEventAction647", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_AcceptEventAction647"):
                opp_val = getattr(value, "bpmnprof_AcceptEventAction647", None)
                setattr(value, "bpmnprof_AcceptEventAction647", self)

    @property
    def bpmnprof_ReceiveTask649(self):
        return self.__bpmnprof_ReceiveTask649

    @bpmnprof_ReceiveTask649.setter
    def bpmnprof_ReceiveTask649(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ReceiveTask__bpmnprof_ReceiveTask649", None)
        self.__bpmnprof_ReceiveTask649 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNOperation650"):
                opp_val = getattr(old_value, "bpmnprof_BPMNOperation650", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNOperation650", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNOperation650"):
                opp_val = getattr(value, "bpmnprof_BPMNOperation650", None)
                setattr(value, "bpmnprof_BPMNOperation650", self)

    @property
    def bpmnprof_ReceiveTask(self):
        return self.__bpmnprof_ReceiveTask

    @bpmnprof_ReceiveTask.setter
    def bpmnprof_ReceiveTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ReceiveTask__bpmnprof_ReceiveTask", None)
        self.__bpmnprof_ReceiveTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNMessage644"):
                opp_val = getattr(old_value, "bpmnprof_BPMNMessage644", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNMessage644", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNMessage644"):
                opp_val = getattr(value, "bpmnprof_BPMNMessage644", None)
                setattr(value, "bpmnprof_BPMNMessage644", self)

    def ReceiveTaskoperationRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ReceiveTaskoperationRef method
        pass

class bpmnprof_SendTask(Task):

    def __init__(self, implementation: str, bpmnprof_SendTask: "bpmnprof_BPMNMessage" = None, bpmnprof_SendTask634: "bpmnprof_CallOperationAction" = None, bpmnprof_SendTask637: "bpmnprof_BPMNOperation" = None):
        self.implementation = implementation
        self.bpmnprof_SendTask = bpmnprof_SendTask
        self.bpmnprof_SendTask634 = bpmnprof_SendTask634
        self.bpmnprof_SendTask637 = bpmnprof_SendTask637
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def bpmnprof_SendTask634(self):
        return self.__bpmnprof_SendTask634

    @bpmnprof_SendTask634.setter
    def bpmnprof_SendTask634(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_SendTask__bpmnprof_SendTask634", None)
        self.__bpmnprof_SendTask634 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_CallOperationAction635"):
                opp_val = getattr(old_value, "bpmnprof_CallOperationAction635", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_CallOperationAction635", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_CallOperationAction635"):
                opp_val = getattr(value, "bpmnprof_CallOperationAction635", None)
                setattr(value, "bpmnprof_CallOperationAction635", self)

    @property
    def bpmnprof_SendTask(self):
        return self.__bpmnprof_SendTask

    @bpmnprof_SendTask.setter
    def bpmnprof_SendTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_SendTask__bpmnprof_SendTask", None)
        self.__bpmnprof_SendTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNMessage632"):
                opp_val = getattr(old_value, "bpmnprof_BPMNMessage632", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNMessage632", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNMessage632"):
                opp_val = getattr(value, "bpmnprof_BPMNMessage632", None)
                setattr(value, "bpmnprof_BPMNMessage632", self)

    @property
    def bpmnprof_SendTask637(self):
        return self.__bpmnprof_SendTask637

    @bpmnprof_SendTask637.setter
    def bpmnprof_SendTask637(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_SendTask__bpmnprof_SendTask637", None)
        self.__bpmnprof_SendTask637 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNOperation638"):
                opp_val = getattr(old_value, "bpmnprof_BPMNOperation638", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNOperation638", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNOperation638"):
                opp_val = getattr(value, "bpmnprof_BPMNOperation638", None)
                setattr(value, "bpmnprof_BPMNOperation638", self)

    def SendTaskoperationRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SendTaskoperationRef method
        pass

class bpmnprof_ScriptTask(Task):

    def __init__(self, scriptFormat: str, script: str, bpmnprof_ScriptTask: "bpmnprof_OpaqueAction" = None):
        self.scriptFormat = scriptFormat
        self.script = script
        self.bpmnprof_ScriptTask = bpmnprof_ScriptTask
        
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

    @property
    def bpmnprof_ScriptTask(self):
        return self.__bpmnprof_ScriptTask

    @bpmnprof_ScriptTask.setter
    def bpmnprof_ScriptTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ScriptTask__bpmnprof_ScriptTask", None)
        self.__bpmnprof_ScriptTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_OpaqueAction630"):
                opp_val = getattr(old_value, "bpmnprof_OpaqueAction630", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_OpaqueAction630", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_OpaqueAction630"):
                opp_val = getattr(value, "bpmnprof_OpaqueAction630", None)
                setattr(value, "bpmnprof_OpaqueAction630", self)

    def ScriptTaskscript(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ScriptTaskscript method
        pass

    def ScriptTaskscriptFormat(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ScriptTaskscriptFormat method
        pass

class bpmnprof_ManualTask(Task):

    pass
class bpmnprof_ServiceTask(Task):

    def __init__(self, implementation: str, bpmnprof_ServiceTask: "bpmnprof_CallOperationAction" = None, bpmnprof_ServiceTask654: "bpmnprof_BPMNOperation" = None):
        self.implementation = implementation
        self.bpmnprof_ServiceTask = bpmnprof_ServiceTask
        self.bpmnprof_ServiceTask654 = bpmnprof_ServiceTask654
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def bpmnprof_ServiceTask(self):
        return self.__bpmnprof_ServiceTask

    @bpmnprof_ServiceTask.setter
    def bpmnprof_ServiceTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ServiceTask__bpmnprof_ServiceTask", None)
        self.__bpmnprof_ServiceTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_CallOperationAction652"):
                opp_val = getattr(old_value, "bpmnprof_CallOperationAction652", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_CallOperationAction652", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_CallOperationAction652"):
                opp_val = getattr(value, "bpmnprof_CallOperationAction652", None)
                setattr(value, "bpmnprof_CallOperationAction652", self)

    @property
    def bpmnprof_ServiceTask654(self):
        return self.__bpmnprof_ServiceTask654

    @bpmnprof_ServiceTask654.setter
    def bpmnprof_ServiceTask654(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ServiceTask__bpmnprof_ServiceTask654", None)
        self.__bpmnprof_ServiceTask654 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNOperation655"):
                opp_val = getattr(old_value, "bpmnprof_BPMNOperation655", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNOperation655", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNOperation655"):
                opp_val = getattr(value, "bpmnprof_BPMNOperation655", None)
                setattr(value, "bpmnprof_BPMNOperation655", self)

    def ServiceTaskinputSet(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ServiceTaskinputSet method
        pass

    def ServiceTaskoperationRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ServiceTaskoperationRef method
        pass

    def ServiceTaskoutputSet(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ServiceTaskoutputSet method
        pass

class bpmnprof_BusinessRuleTask(Task):

    def __init__(self, implementation: str, bpmnprof_BusinessRuleTask: "bpmnprof_OpaqueAction" = None):
        self.implementation = implementation
        self.bpmnprof_BusinessRuleTask = bpmnprof_BusinessRuleTask
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def bpmnprof_BusinessRuleTask(self):
        return self.__bpmnprof_BusinessRuleTask

    @bpmnprof_BusinessRuleTask.setter
    def bpmnprof_BusinessRuleTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BusinessRuleTask__bpmnprof_BusinessRuleTask", None)
        self.__bpmnprof_BusinessRuleTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_OpaqueAction619"):
                opp_val = getattr(old_value, "bpmnprof_OpaqueAction619", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_OpaqueAction619", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_OpaqueAction619"):
                opp_val = getattr(value, "bpmnprof_OpaqueAction619", None)
                setattr(value, "bpmnprof_OpaqueAction619", self)

    def BusinessRuleTaskimplementation(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BusinessRuleTaskimplementation method
        pass

class bpmnprof_UserTask(Task):

    def __init__(self, implementation: str, bpmnprof_UserTask591: set["bpmnprof_Rendering"] = None, bpmnprof_UserTask: "bpmnprof_OpaqueAction" = None):
        self.implementation = implementation
        self.bpmnprof_UserTask591 = bpmnprof_UserTask591 if bpmnprof_UserTask591 is not None else set()
        self.bpmnprof_UserTask = bpmnprof_UserTask
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def bpmnprof_UserTask(self):
        return self.__bpmnprof_UserTask

    @bpmnprof_UserTask.setter
    def bpmnprof_UserTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_UserTask__bpmnprof_UserTask", None)
        self.__bpmnprof_UserTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_OpaqueAction"):
                opp_val = getattr(old_value, "bpmnprof_OpaqueAction", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_OpaqueAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_OpaqueAction"):
                opp_val = getattr(value, "bpmnprof_OpaqueAction", None)
                setattr(value, "bpmnprof_OpaqueAction", self)

    @property
    def bpmnprof_UserTask591(self):
        return self.__bpmnprof_UserTask591

    @bpmnprof_UserTask591.setter
    def bpmnprof_UserTask591(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_UserTask__bpmnprof_UserTask591", None)
        self.__bpmnprof_UserTask591 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_Rendering"):
                    opp_val = getattr(item, "bpmnprof_Rendering", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_Rendering", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_Rendering"):
                    opp_val = getattr(item, "bpmnprof_Rendering", None)
                    
                    setattr(item, "bpmnprof_Rendering", self)
                    

    def UserTaskrenderings(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement UserTaskrenderings method
        pass

    def UserTaskimplementation(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement UserTaskimplementation method
        pass

class BPMNActivity:

    pass
class bpmnprof_CallActivity(BPMNActivity):

    def __init__(self, bpmnprof_CallActivity: "bpmnprof_CallBehaviorAction" = None, bpmnprof_CallActivity616: "bpmnprof_CallableElement" = None):
        self.bpmnprof_CallActivity = bpmnprof_CallActivity
        self.bpmnprof_CallActivity616 = bpmnprof_CallActivity616
        
    @property
    def bpmnprof_CallActivity(self):
        return self.__bpmnprof_CallActivity

    @bpmnprof_CallActivity.setter
    def bpmnprof_CallActivity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_CallActivity__bpmnprof_CallActivity", None)
        self.__bpmnprof_CallActivity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_CallBehaviorAction"):
                opp_val = getattr(old_value, "bpmnprof_CallBehaviorAction", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_CallBehaviorAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_CallBehaviorAction"):
                opp_val = getattr(value, "bpmnprof_CallBehaviorAction", None)
                setattr(value, "bpmnprof_CallBehaviorAction", self)

    @property
    def bpmnprof_CallActivity616(self):
        return self.__bpmnprof_CallActivity616

    @bpmnprof_CallActivity616.setter
    def bpmnprof_CallActivity616(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_CallActivity__bpmnprof_CallActivity616", None)
        self.__bpmnprof_CallActivity616 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_CallableElement617"):
                opp_val = getattr(old_value, "bpmnprof_CallableElement617", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_CallableElement617", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_CallableElement617"):
                opp_val = getattr(value, "bpmnprof_CallableElement617", None)
                setattr(value, "bpmnprof_CallableElement617", self)

    def CallActivitycalledElementRefvalues(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement CallActivitycalledElementRefvalues method
        pass

class bpmnprof_Task(BPMNActivity):

    pass
class bpmnprof_SendObjectAction:

    pass
class bpmnprof_Enumeration:

    pass
class bpmnprof_FlowFinalNode:

    pass
class bpmnprof_CallOperationAction:

    pass
class bpmnprof_ChangeEvent:

    pass
class bpmnprof_FinalNode:

    pass
class ThrowEvent:

    pass
class bpmnprof_IntermediateThrowEvent(ThrowEvent):

    pass
class bpmnprof_ImplicitThrowEvent(ThrowEvent):

    pass
class bpmnprof_EndEvent(ThrowEvent):

    pass
class DataAssociation:

    pass
class bpmnprof_ObjectFlow:

    pass
class bpmnprof_InitialNode:

    pass
class bpmnprof_AcceptEventAction:

    pass
class BPMNEvent:

    pass
class bpmnprof_ThrowEvent(BPMNEvent):

    def __init__(self, bpmnprof_ThrowEvent: "bpmnprof_CallOperationAction" = None, bpmnprof_ThrowEvent527: "bpmnprof_FlowFinalNode" = None, bpmnprof_ThrowEvent529: set["bpmnprof_DataInputAssociation"] = None):
        self.bpmnprof_ThrowEvent = bpmnprof_ThrowEvent
        self.bpmnprof_ThrowEvent527 = bpmnprof_ThrowEvent527
        self.bpmnprof_ThrowEvent529 = bpmnprof_ThrowEvent529 if bpmnprof_ThrowEvent529 is not None else set()
        
    @property
    def bpmnprof_ThrowEvent527(self):
        return self.__bpmnprof_ThrowEvent527

    @bpmnprof_ThrowEvent527.setter
    def bpmnprof_ThrowEvent527(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ThrowEvent__bpmnprof_ThrowEvent527", None)
        self.__bpmnprof_ThrowEvent527 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_FlowFinalNode"):
                opp_val = getattr(old_value, "bpmnprof_FlowFinalNode", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_FlowFinalNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_FlowFinalNode"):
                opp_val = getattr(value, "bpmnprof_FlowFinalNode", None)
                setattr(value, "bpmnprof_FlowFinalNode", self)

    @property
    def bpmnprof_ThrowEvent529(self):
        return self.__bpmnprof_ThrowEvent529

    @bpmnprof_ThrowEvent529.setter
    def bpmnprof_ThrowEvent529(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ThrowEvent__bpmnprof_ThrowEvent529", None)
        self.__bpmnprof_ThrowEvent529 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_DataInputAssociation530"):
                    opp_val = getattr(item, "bpmnprof_DataInputAssociation530", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_DataInputAssociation530", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_DataInputAssociation530"):
                    opp_val = getattr(item, "bpmnprof_DataInputAssociation530", None)
                    
                    setattr(item, "bpmnprof_DataInputAssociation530", self)
                    

    @property
    def bpmnprof_ThrowEvent(self):
        return self.__bpmnprof_ThrowEvent

    @bpmnprof_ThrowEvent.setter
    def bpmnprof_ThrowEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ThrowEvent__bpmnprof_ThrowEvent", None)
        self.__bpmnprof_ThrowEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_CallOperationAction"):
                opp_val = getattr(old_value, "bpmnprof_CallOperationAction", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_CallOperationAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_CallOperationAction"):
                opp_val = getattr(value, "bpmnprof_CallOperationAction", None)
                setattr(value, "bpmnprof_CallOperationAction", self)

    def ThrowEventeventDefinitionRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ThrowEventeventDefinitionRefs method
        pass

class bpmnprof_CatchEvent(BPMNEvent):

    def __init__(self, parallelMultiple: str, bpmnprof_CatchEvent: "bpmnprof_AcceptEventAction" = None, bpmnprof_CatchEvent467: "bpmnprof_InitialNode" = None, bpmnprof_CatchEvent469: set["bpmnprof_DataOutputAssociation"] = None):
        self.parallelMultiple = parallelMultiple
        self.bpmnprof_CatchEvent = bpmnprof_CatchEvent
        self.bpmnprof_CatchEvent467 = bpmnprof_CatchEvent467
        self.bpmnprof_CatchEvent469 = bpmnprof_CatchEvent469 if bpmnprof_CatchEvent469 is not None else set()
        
    @property
    def parallelMultiple(self) -> str:
        return self.__parallelMultiple

    @parallelMultiple.setter
    def parallelMultiple(self, parallelMultiple: str):
        self.__parallelMultiple = parallelMultiple

    @property
    def bpmnprof_CatchEvent(self):
        return self.__bpmnprof_CatchEvent

    @bpmnprof_CatchEvent.setter
    def bpmnprof_CatchEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_CatchEvent__bpmnprof_CatchEvent", None)
        self.__bpmnprof_CatchEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_AcceptEventAction"):
                opp_val = getattr(old_value, "bpmnprof_AcceptEventAction", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_AcceptEventAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_AcceptEventAction"):
                opp_val = getattr(value, "bpmnprof_AcceptEventAction", None)
                setattr(value, "bpmnprof_AcceptEventAction", self)

    @property
    def bpmnprof_CatchEvent467(self):
        return self.__bpmnprof_CatchEvent467

    @bpmnprof_CatchEvent467.setter
    def bpmnprof_CatchEvent467(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_CatchEvent__bpmnprof_CatchEvent467", None)
        self.__bpmnprof_CatchEvent467 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_InitialNode"):
                opp_val = getattr(old_value, "bpmnprof_InitialNode", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_InitialNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_InitialNode"):
                opp_val = getattr(value, "bpmnprof_InitialNode", None)
                setattr(value, "bpmnprof_InitialNode", self)

    @property
    def bpmnprof_CatchEvent469(self):
        return self.__bpmnprof_CatchEvent469

    @bpmnprof_CatchEvent469.setter
    def bpmnprof_CatchEvent469(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_CatchEvent__bpmnprof_CatchEvent469", None)
        self.__bpmnprof_CatchEvent469 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_DataOutputAssociation470"):
                    opp_val = getattr(item, "bpmnprof_DataOutputAssociation470", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_DataOutputAssociation470", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_DataOutputAssociation470"):
                    opp_val = getattr(item, "bpmnprof_DataOutputAssociation470", None)
                    
                    setattr(item, "bpmnprof_DataOutputAssociation470", self)
                    

    def catchEventeventDefinitionsRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement catchEventeventDefinitionsRefs method
        pass

class CatchEvent:

    pass
class bpmnprof_IntermediateCatchEvent(CatchEvent):

    pass
class bpmnprof_StartEvent(CatchEvent):

    def __init__(self, isInterrupting: str):
        self.isInterrupting = isInterrupting
        
    @property
    def isInterrupting(self) -> str:
        return self.__isInterrupting

    @isInterrupting.setter
    def isInterrupting(self, isInterrupting: str):
        self.__isInterrupting = isInterrupting

class bpmnprof_BoundaryEvent(CatchEvent):

    def __init__(self, cancelActivity: str, bpmnprof_BoundaryEvent: "bpmnprof_BPMNActivity" = None, bpmnprof_BoundaryEvent463: "bpmnprof_BPMNActivity" = None):
        self.cancelActivity = cancelActivity
        self.bpmnprof_BoundaryEvent = bpmnprof_BoundaryEvent
        self.bpmnprof_BoundaryEvent463 = bpmnprof_BoundaryEvent463
        
    @property
    def cancelActivity(self) -> str:
        return self.__cancelActivity

    @cancelActivity.setter
    def cancelActivity(self, cancelActivity: str):
        self.__cancelActivity = cancelActivity

    @property
    def bpmnprof_BoundaryEvent(self):
        return self.__bpmnprof_BoundaryEvent

    @bpmnprof_BoundaryEvent.setter
    def bpmnprof_BoundaryEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BoundaryEvent__bpmnprof_BoundaryEvent", None)
        self.__bpmnprof_BoundaryEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNActivity452"):
                opp_val = getattr(old_value, "bpmnprof_BPMNActivity452", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNActivity452"):
                opp_val = getattr(value, "bpmnprof_BPMNActivity452", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_BPMNActivity452", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_BoundaryEvent463(self):
        return self.__bpmnprof_BoundaryEvent463

    @bpmnprof_BoundaryEvent463.setter
    def bpmnprof_BoundaryEvent463(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BoundaryEvent__bpmnprof_BoundaryEvent463", None)
        self.__bpmnprof_BoundaryEvent463 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNActivity464"):
                opp_val = getattr(old_value, "bpmnprof_BPMNActivity464", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNActivity464", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNActivity464"):
                opp_val = getattr(value, "bpmnprof_BPMNActivity464", None)
                setattr(value, "bpmnprof_BPMNActivity464", self)

    def boundaryEventattachedToRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement boundaryEventattachedToRef method
        pass

class bpmnprof_DataOutputAssociation(DataAssociation):

    def __init__(self, bpmnprof_DataOutputAssociation: "bpmnprof_BPMNActivity" = None, bpmnprof_DataOutputAssociation470: "bpmnprof_CatchEvent" = None):
        self.bpmnprof_DataOutputAssociation = bpmnprof_DataOutputAssociation
        self.bpmnprof_DataOutputAssociation470 = bpmnprof_DataOutputAssociation470
        
    @property
    def bpmnprof_DataOutputAssociation(self):
        return self.__bpmnprof_DataOutputAssociation

    @bpmnprof_DataOutputAssociation.setter
    def bpmnprof_DataOutputAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataOutputAssociation__bpmnprof_DataOutputAssociation", None)
        self.__bpmnprof_DataOutputAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNActivity456"):
                opp_val = getattr(old_value, "bpmnprof_BPMNActivity456", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNActivity456"):
                opp_val = getattr(value, "bpmnprof_BPMNActivity456", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_BPMNActivity456", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_DataOutputAssociation470(self):
        return self.__bpmnprof_DataOutputAssociation470

    @bpmnprof_DataOutputAssociation470.setter
    def bpmnprof_DataOutputAssociation470(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataOutputAssociation__bpmnprof_DataOutputAssociation470", None)
        self.__bpmnprof_DataOutputAssociation470 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_CatchEvent469"):
                opp_val = getattr(old_value, "bpmnprof_CatchEvent469", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_CatchEvent469"):
                opp_val = getattr(value, "bpmnprof_CatchEvent469", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_CatchEvent469", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def dataOutputAssociationtarget(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement dataOutputAssociationtarget method
        pass

    def dataOutputAssociationsource(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement dataOutputAssociationsource method
        pass

class bpmnprof_DataInputAssociation(DataAssociation):

    def __init__(self, bpmnprof_DataInputAssociation: "bpmnprof_BPMNActivity" = None, bpmnprof_DataInputAssociation530: "bpmnprof_ThrowEvent" = None):
        self.bpmnprof_DataInputAssociation = bpmnprof_DataInputAssociation
        self.bpmnprof_DataInputAssociation530 = bpmnprof_DataInputAssociation530
        
    @property
    def bpmnprof_DataInputAssociation530(self):
        return self.__bpmnprof_DataInputAssociation530

    @bpmnprof_DataInputAssociation530.setter
    def bpmnprof_DataInputAssociation530(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataInputAssociation__bpmnprof_DataInputAssociation530", None)
        self.__bpmnprof_DataInputAssociation530 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ThrowEvent529"):
                opp_val = getattr(old_value, "bpmnprof_ThrowEvent529", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ThrowEvent529"):
                opp_val = getattr(value, "bpmnprof_ThrowEvent529", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_ThrowEvent529", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_DataInputAssociation(self):
        return self.__bpmnprof_DataInputAssociation

    @bpmnprof_DataInputAssociation.setter
    def bpmnprof_DataInputAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataInputAssociation__bpmnprof_DataInputAssociation", None)
        self.__bpmnprof_DataInputAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNActivity454"):
                opp_val = getattr(old_value, "bpmnprof_BPMNActivity454", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNActivity454"):
                opp_val = getattr(value, "bpmnprof_BPMNActivity454", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_BPMNActivity454", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def dataInputAssociationtarget(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement dataInputAssociationtarget method
        pass

    def dataInputAssociationsource(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement dataInputAssociationsource method
        pass

class bpmnprof_Event:

    pass
class bpmnprof_CallEvent:

    pass
class EventDefinition:

    pass
class bpmnprof_EscalationEventDefinition(EventDefinition):

    pass
class bpmnprof_MessageEventDefinition(EventDefinition):

    pass
class bpmnprof_ErrorEventDefinition(EventDefinition):

    pass
class bpmnprof_TimerEventDefinition(EventDefinition):

    pass
class bpmnprof_ConditionalEventDefinition(EventDefinition):

    def __init__(self, bpmnprof_ConditionalEventDefinition: "bpmnprof_ChangeEvent" = None, bpmnprof_ConditionalEventDefinition542: "bpmnprof_BPMNExpression" = None):
        self.bpmnprof_ConditionalEventDefinition = bpmnprof_ConditionalEventDefinition
        self.bpmnprof_ConditionalEventDefinition542 = bpmnprof_ConditionalEventDefinition542
        
    @property
    def bpmnprof_ConditionalEventDefinition(self):
        return self.__bpmnprof_ConditionalEventDefinition

    @bpmnprof_ConditionalEventDefinition.setter
    def bpmnprof_ConditionalEventDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ConditionalEventDefinition__bpmnprof_ConditionalEventDefinition", None)
        self.__bpmnprof_ConditionalEventDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ChangeEvent540"):
                opp_val = getattr(old_value, "bpmnprof_ChangeEvent540", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ChangeEvent540", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ChangeEvent540"):
                opp_val = getattr(value, "bpmnprof_ChangeEvent540", None)
                setattr(value, "bpmnprof_ChangeEvent540", self)

    @property
    def bpmnprof_ConditionalEventDefinition542(self):
        return self.__bpmnprof_ConditionalEventDefinition542

    @bpmnprof_ConditionalEventDefinition542.setter
    def bpmnprof_ConditionalEventDefinition542(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ConditionalEventDefinition__bpmnprof_ConditionalEventDefinition542", None)
        self.__bpmnprof_ConditionalEventDefinition542 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNExpression543"):
                opp_val = getattr(old_value, "bpmnprof_BPMNExpression543", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNExpression543", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNExpression543"):
                opp_val = getattr(value, "bpmnprof_BPMNExpression543", None)
                setattr(value, "bpmnprof_BPMNExpression543", self)

    def conditionalEventDefinitioncondition(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement conditionalEventDefinitioncondition method
        pass

class bpmnprof_SignalEventDefinition(EventDefinition):

    pass
class bpmnprof_CancelEventDefinition(EventDefinition):

    pass
class bpmnprof_TerminateEventDefinition(EventDefinition):

    pass
class bpmnprof_LinkEventDefinition(EventDefinition):

    pass
class bpmnprof_CompensateEventDefinition(EventDefinition):

    def __init__(self, waitForCompletion: str, bpmnprof_CompensateEventDefinition: "bpmnprof_BPMNActivity" = None, bpmnprof_CompensateEventDefinition437: "bpmnprof_CallEvent" = None):
        self.waitForCompletion = waitForCompletion
        self.bpmnprof_CompensateEventDefinition = bpmnprof_CompensateEventDefinition
        self.bpmnprof_CompensateEventDefinition437 = bpmnprof_CompensateEventDefinition437
        
    @property
    def waitForCompletion(self) -> str:
        return self.__waitForCompletion

    @waitForCompletion.setter
    def waitForCompletion(self, waitForCompletion: str):
        self.__waitForCompletion = waitForCompletion

    @property
    def bpmnprof_CompensateEventDefinition(self):
        return self.__bpmnprof_CompensateEventDefinition

    @bpmnprof_CompensateEventDefinition.setter
    def bpmnprof_CompensateEventDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_CompensateEventDefinition__bpmnprof_CompensateEventDefinition", None)
        self.__bpmnprof_CompensateEventDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNActivity"):
                opp_val = getattr(old_value, "bpmnprof_BPMNActivity", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNActivity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNActivity"):
                opp_val = getattr(value, "bpmnprof_BPMNActivity", None)
                setattr(value, "bpmnprof_BPMNActivity", self)

    @property
    def bpmnprof_CompensateEventDefinition437(self):
        return self.__bpmnprof_CompensateEventDefinition437

    @bpmnprof_CompensateEventDefinition437.setter
    def bpmnprof_CompensateEventDefinition437(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_CompensateEventDefinition__bpmnprof_CompensateEventDefinition437", None)
        self.__bpmnprof_CompensateEventDefinition437 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_CallEvent"):
                opp_val = getattr(old_value, "bpmnprof_CallEvent", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_CallEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_CallEvent"):
                opp_val = getattr(value, "bpmnprof_CallEvent", None)
                setattr(value, "bpmnprof_CallEvent", self)

class GlobalTask:

    pass
class bpmnprof_GlobalManualTask(GlobalTask):

    pass
class bpmnprof_GlobalUserTask(GlobalTask):

    def __init__(self, implementation: str, bpmnprof_GlobalUserTask: set["bpmnprof_Rendering"] = None):
        self.implementation = implementation
        self.bpmnprof_GlobalUserTask = bpmnprof_GlobalUserTask if bpmnprof_GlobalUserTask is not None else set()
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def bpmnprof_GlobalUserTask(self):
        return self.__bpmnprof_GlobalUserTask

    @bpmnprof_GlobalUserTask.setter
    def bpmnprof_GlobalUserTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_GlobalUserTask__bpmnprof_GlobalUserTask", None)
        self.__bpmnprof_GlobalUserTask = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_Rendering597"):
                    opp_val = getattr(item, "bpmnprof_Rendering597", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_Rendering597", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_Rendering597"):
                    opp_val = getattr(item, "bpmnprof_Rendering597", None)
                    
                    setattr(item, "bpmnprof_Rendering597", self)
                    

    def GlobalUserTaskrenderings(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement GlobalUserTaskrenderings method
        pass

    def GlobalUserTaskimplementation(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement GlobalUserTaskimplementation method
        pass

class bpmnprof_GlobalBusinessRuleTask(GlobalTask):

    def __init__(self, implementation: str):
        self.implementation = implementation
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    def GlobalBusinessRuleTaskimplementation(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement GlobalBusinessRuleTaskimplementation method
        pass

class bpmnprof_GlobalScriptTask(GlobalTask):

    def __init__(self, script: str, scriptFormat: str):
        self.script = script
        self.scriptFormat = scriptFormat
        
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

    def GlobalScriptTaskscriptFormat(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement GlobalScriptTaskscriptFormat method
        pass

    def GlobalScriptTaskscript(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement GlobalScriptTaskscript method
        pass

class bpmnprof_OpaqueBehavior:

    pass
class bpmnprof_DataStoreNode:

    pass
class BPMNExpression:

    pass
class bpmnprof_ResourceAssignmentExpression(BPMNExpression):

    def __init__(self, bpmnprof_ResourceAssignmentExpression: "bpmnprof_ResourceRole" = None, bpmnprof_ResourceAssignmentExpression412: "bpmnprof_BPMNExpression" = None):
        self.bpmnprof_ResourceAssignmentExpression = bpmnprof_ResourceAssignmentExpression
        self.bpmnprof_ResourceAssignmentExpression412 = bpmnprof_ResourceAssignmentExpression412
        
    @property
    def bpmnprof_ResourceAssignmentExpression412(self):
        return self.__bpmnprof_ResourceAssignmentExpression412

    @bpmnprof_ResourceAssignmentExpression412.setter
    def bpmnprof_ResourceAssignmentExpression412(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ResourceAssignmentExpression__bpmnprof_ResourceAssignmentExpression412", None)
        self.__bpmnprof_ResourceAssignmentExpression412 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNExpression413"):
                opp_val = getattr(old_value, "bpmnprof_BPMNExpression413", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNExpression413", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNExpression413"):
                opp_val = getattr(value, "bpmnprof_BPMNExpression413", None)
                setattr(value, "bpmnprof_BPMNExpression413", self)

    @property
    def bpmnprof_ResourceAssignmentExpression(self):
        return self.__bpmnprof_ResourceAssignmentExpression

    @bpmnprof_ResourceAssignmentExpression.setter
    def bpmnprof_ResourceAssignmentExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ResourceAssignmentExpression__bpmnprof_ResourceAssignmentExpression", None)
        self.__bpmnprof_ResourceAssignmentExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ResourceRole405"):
                opp_val = getattr(old_value, "bpmnprof_ResourceRole405", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ResourceRole405", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ResourceRole405"):
                opp_val = getattr(value, "bpmnprof_ResourceRole405", None)
                setattr(value, "bpmnprof_ResourceRole405", self)

    def ResourceAssignmentExpressionexpression(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceAssignmentExpressionexpression method
        pass

class bpmnprof_FormalExpression(BPMNExpression):

    def __init__(self, bpmnprof_FormalExpression: "bpmnprof_CorrelationPropertyRetrievalExpression" = None, bpmnprof_FormalExpression393: "bpmnprof_CorrelationPropertyBinding" = None, bpmnprof_FormalExpression378: "bpmnprof_ItemDefinition" = None, bpmnprof_FormalExpression491: "bpmnprof_DataAssociation" = None, bpmnprof_FormalExpression621: "bpmnprof_ComplexBehaviorDefinition" = None):
        self.bpmnprof_FormalExpression = bpmnprof_FormalExpression
        self.bpmnprof_FormalExpression393 = bpmnprof_FormalExpression393
        self.bpmnprof_FormalExpression378 = bpmnprof_FormalExpression378
        self.bpmnprof_FormalExpression491 = bpmnprof_FormalExpression491
        self.bpmnprof_FormalExpression621 = bpmnprof_FormalExpression621
        
    @property
    def bpmnprof_FormalExpression491(self):
        return self.__bpmnprof_FormalExpression491

    @bpmnprof_FormalExpression491.setter
    def bpmnprof_FormalExpression491(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_FormalExpression__bpmnprof_FormalExpression491", None)
        self.__bpmnprof_FormalExpression491 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_DataAssociation490"):
                opp_val = getattr(old_value, "bpmnprof_DataAssociation490", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_DataAssociation490", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_DataAssociation490"):
                opp_val = getattr(value, "bpmnprof_DataAssociation490", None)
                setattr(value, "bpmnprof_DataAssociation490", self)

    @property
    def bpmnprof_FormalExpression378(self):
        return self.__bpmnprof_FormalExpression378

    @bpmnprof_FormalExpression378.setter
    def bpmnprof_FormalExpression378(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_FormalExpression__bpmnprof_FormalExpression378", None)
        self.__bpmnprof_FormalExpression378 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ItemDefinition379"):
                opp_val = getattr(old_value, "bpmnprof_ItemDefinition379", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ItemDefinition379", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ItemDefinition379"):
                opp_val = getattr(value, "bpmnprof_ItemDefinition379", None)
                setattr(value, "bpmnprof_ItemDefinition379", self)

    @property
    def bpmnprof_FormalExpression(self):
        return self.__bpmnprof_FormalExpression

    @bpmnprof_FormalExpression.setter
    def bpmnprof_FormalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_FormalExpression__bpmnprof_FormalExpression", None)
        self.__bpmnprof_FormalExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_CorrelationPropertyRetrievalExpression376"):
                opp_val = getattr(old_value, "bpmnprof_CorrelationPropertyRetrievalExpression376", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_CorrelationPropertyRetrievalExpression376", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_CorrelationPropertyRetrievalExpression376"):
                opp_val = getattr(value, "bpmnprof_CorrelationPropertyRetrievalExpression376", None)
                setattr(value, "bpmnprof_CorrelationPropertyRetrievalExpression376", self)

    @property
    def bpmnprof_FormalExpression621(self):
        return self.__bpmnprof_FormalExpression621

    @bpmnprof_FormalExpression621.setter
    def bpmnprof_FormalExpression621(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_FormalExpression__bpmnprof_FormalExpression621", None)
        self.__bpmnprof_FormalExpression621 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ComplexBehaviorDefinition"):
                opp_val = getattr(old_value, "bpmnprof_ComplexBehaviorDefinition", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ComplexBehaviorDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ComplexBehaviorDefinition"):
                opp_val = getattr(value, "bpmnprof_ComplexBehaviorDefinition", None)
                setattr(value, "bpmnprof_ComplexBehaviorDefinition", self)

    @property
    def bpmnprof_FormalExpression393(self):
        return self.__bpmnprof_FormalExpression393

    @bpmnprof_FormalExpression393.setter
    def bpmnprof_FormalExpression393(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_FormalExpression__bpmnprof_FormalExpression393", None)
        self.__bpmnprof_FormalExpression393 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_CorrelationPropertyBinding392"):
                opp_val = getattr(old_value, "bpmnprof_CorrelationPropertyBinding392", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_CorrelationPropertyBinding392", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_CorrelationPropertyBinding392"):
                opp_val = getattr(value, "bpmnprof_CorrelationPropertyBinding392", None)
                setattr(value, "bpmnprof_CorrelationPropertyBinding392", self)

    def FormalExpressionevaluatesToTypeRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement FormalExpressionevaluatesToTypeRef method
        pass

class InteractionNode:

    pass
class bpmnprof_InformationFlow:

    pass
class bpmnprof_InstanceSpecification:

    pass
class bpmnprof_InteractionNode(ABC):

    pass
class bpmnprof_MultiplicityElement:

    pass
class bpmnprof_ConversationNode(InteractionNode):

    def __init__(self, bpmnprof_ConversationNode: "bpmnprof_BPMNCollaboration" = None, bpmnprof_ConversationNode345: "bpmnprof_InformationFlow" = None, bpmnprof_ConversationNode348: set["bpmnprof_MessageFlow"] = None, bpmnprof_ConversationNode351: set["bpmnprof_CorrelationKey"] = None, bpmnprof_ConversationNode354: set["bpmnprof_Participant"] = None, bpmnprof_ConversationNode601: "bpmnprof_SubConversation" = None):
        self.bpmnprof_ConversationNode = bpmnprof_ConversationNode
        self.bpmnprof_ConversationNode345 = bpmnprof_ConversationNode345
        self.bpmnprof_ConversationNode348 = bpmnprof_ConversationNode348 if bpmnprof_ConversationNode348 is not None else set()
        self.bpmnprof_ConversationNode351 = bpmnprof_ConversationNode351 if bpmnprof_ConversationNode351 is not None else set()
        self.bpmnprof_ConversationNode354 = bpmnprof_ConversationNode354 if bpmnprof_ConversationNode354 is not None else set()
        self.bpmnprof_ConversationNode601 = bpmnprof_ConversationNode601
        
    @property
    def bpmnprof_ConversationNode(self):
        return self.__bpmnprof_ConversationNode

    @bpmnprof_ConversationNode.setter
    def bpmnprof_ConversationNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ConversationNode__bpmnprof_ConversationNode", None)
        self.__bpmnprof_ConversationNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNCollaboration274"):
                opp_val = getattr(old_value, "bpmnprof_BPMNCollaboration274", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNCollaboration274"):
                opp_val = getattr(value, "bpmnprof_BPMNCollaboration274", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_BPMNCollaboration274", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_ConversationNode351(self):
        return self.__bpmnprof_ConversationNode351

    @bpmnprof_ConversationNode351.setter
    def bpmnprof_ConversationNode351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ConversationNode__bpmnprof_ConversationNode351", None)
        self.__bpmnprof_ConversationNode351 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_CorrelationKey352"):
                    opp_val = getattr(item, "bpmnprof_CorrelationKey352", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_CorrelationKey352", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_CorrelationKey352"):
                    opp_val = getattr(item, "bpmnprof_CorrelationKey352", None)
                    
                    setattr(item, "bpmnprof_CorrelationKey352", self)
                    

    @property
    def bpmnprof_ConversationNode345(self):
        return self.__bpmnprof_ConversationNode345

    @bpmnprof_ConversationNode345.setter
    def bpmnprof_ConversationNode345(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ConversationNode__bpmnprof_ConversationNode345", None)
        self.__bpmnprof_ConversationNode345 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_InformationFlow346"):
                opp_val = getattr(old_value, "bpmnprof_InformationFlow346", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_InformationFlow346", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_InformationFlow346"):
                opp_val = getattr(value, "bpmnprof_InformationFlow346", None)
                setattr(value, "bpmnprof_InformationFlow346", self)

    @property
    def bpmnprof_ConversationNode354(self):
        return self.__bpmnprof_ConversationNode354

    @bpmnprof_ConversationNode354.setter
    def bpmnprof_ConversationNode354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ConversationNode__bpmnprof_ConversationNode354", None)
        self.__bpmnprof_ConversationNode354 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_Participant355"):
                    opp_val = getattr(item, "bpmnprof_Participant355", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_Participant355", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_Participant355"):
                    opp_val = getattr(item, "bpmnprof_Participant355", None)
                    
                    setattr(item, "bpmnprof_Participant355", self)
                    

    @property
    def bpmnprof_ConversationNode601(self):
        return self.__bpmnprof_ConversationNode601

    @bpmnprof_ConversationNode601.setter
    def bpmnprof_ConversationNode601(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ConversationNode__bpmnprof_ConversationNode601", None)
        self.__bpmnprof_ConversationNode601 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_SubConversation"):
                opp_val = getattr(old_value, "bpmnprof_SubConversation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_SubConversation"):
                opp_val = getattr(value, "bpmnprof_SubConversation", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_SubConversation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_ConversationNode348(self):
        return self.__bpmnprof_ConversationNode348

    @bpmnprof_ConversationNode348.setter
    def bpmnprof_ConversationNode348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ConversationNode__bpmnprof_ConversationNode348", None)
        self.__bpmnprof_ConversationNode348 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_MessageFlow349"):
                    opp_val = getattr(item, "bpmnprof_MessageFlow349", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_MessageFlow349", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_MessageFlow349"):
                    opp_val = getattr(item, "bpmnprof_MessageFlow349", None)
                    
                    setattr(item, "bpmnprof_MessageFlow349", self)
                    

    def ConversationNodeparticipantRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ConversationNodeparticipantRefs method
        pass

class bpmnprof_Collaboration:

    pass
class bpmnprof_Operation:

    pass
class ItemDefinition:

    pass
class bpmnprof_BPMNMessage(ItemDefinition):

    def __init__(self, bpmnprof_BPMNMessage246: "bpmnprof_BPMNOperation" = None, bpmnprof_BPMNMessage250: "bpmnprof_ItemDefinition" = None, bpmnprof_BPMNMessage: "bpmnprof_BPMNOperation" = None, bpmnprof_BPMNMessage343: "bpmnprof_MessageFlow" = None, bpmnprof_BPMNMessage374: "bpmnprof_CorrelationPropertyRetrievalExpression" = None, bpmnprof_BPMNMessage532: "bpmnprof_MessageEventDefinition" = None, bpmnprof_BPMNMessage632: "bpmnprof_SendTask" = None, bpmnprof_BPMNMessage644: "bpmnprof_ReceiveTask" = None):
        self.bpmnprof_BPMNMessage246 = bpmnprof_BPMNMessage246
        self.bpmnprof_BPMNMessage250 = bpmnprof_BPMNMessage250
        self.bpmnprof_BPMNMessage = bpmnprof_BPMNMessage
        self.bpmnprof_BPMNMessage343 = bpmnprof_BPMNMessage343
        self.bpmnprof_BPMNMessage374 = bpmnprof_BPMNMessage374
        self.bpmnprof_BPMNMessage532 = bpmnprof_BPMNMessage532
        self.bpmnprof_BPMNMessage632 = bpmnprof_BPMNMessage632
        self.bpmnprof_BPMNMessage644 = bpmnprof_BPMNMessage644
        
    @property
    def bpmnprof_BPMNMessage632(self):
        return self.__bpmnprof_BPMNMessage632

    @bpmnprof_BPMNMessage632.setter
    def bpmnprof_BPMNMessage632(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNMessage__bpmnprof_BPMNMessage632", None)
        self.__bpmnprof_BPMNMessage632 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_SendTask"):
                opp_val = getattr(old_value, "bpmnprof_SendTask", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_SendTask", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_SendTask"):
                opp_val = getattr(value, "bpmnprof_SendTask", None)
                setattr(value, "bpmnprof_SendTask", self)

    @property
    def bpmnprof_BPMNMessage374(self):
        return self.__bpmnprof_BPMNMessage374

    @bpmnprof_BPMNMessage374.setter
    def bpmnprof_BPMNMessage374(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNMessage__bpmnprof_BPMNMessage374", None)
        self.__bpmnprof_BPMNMessage374 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_CorrelationPropertyRetrievalExpression373"):
                opp_val = getattr(old_value, "bpmnprof_CorrelationPropertyRetrievalExpression373", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_CorrelationPropertyRetrievalExpression373", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_CorrelationPropertyRetrievalExpression373"):
                opp_val = getattr(value, "bpmnprof_CorrelationPropertyRetrievalExpression373", None)
                setattr(value, "bpmnprof_CorrelationPropertyRetrievalExpression373", self)

    @property
    def bpmnprof_BPMNMessage532(self):
        return self.__bpmnprof_BPMNMessage532

    @bpmnprof_BPMNMessage532.setter
    def bpmnprof_BPMNMessage532(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNMessage__bpmnprof_BPMNMessage532", None)
        self.__bpmnprof_BPMNMessage532 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_MessageEventDefinition"):
                opp_val = getattr(old_value, "bpmnprof_MessageEventDefinition", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_MessageEventDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_MessageEventDefinition"):
                opp_val = getattr(value, "bpmnprof_MessageEventDefinition", None)
                setattr(value, "bpmnprof_MessageEventDefinition", self)

    @property
    def bpmnprof_BPMNMessage(self):
        return self.__bpmnprof_BPMNMessage

    @bpmnprof_BPMNMessage.setter
    def bpmnprof_BPMNMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNMessage__bpmnprof_BPMNMessage", None)
        self.__bpmnprof_BPMNMessage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNOperation243"):
                opp_val = getattr(old_value, "bpmnprof_BPMNOperation243", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNOperation243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNOperation243"):
                opp_val = getattr(value, "bpmnprof_BPMNOperation243", None)
                setattr(value, "bpmnprof_BPMNOperation243", self)

    @property
    def bpmnprof_BPMNMessage250(self):
        return self.__bpmnprof_BPMNMessage250

    @bpmnprof_BPMNMessage250.setter
    def bpmnprof_BPMNMessage250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNMessage__bpmnprof_BPMNMessage250", None)
        self.__bpmnprof_BPMNMessage250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ItemDefinition251"):
                opp_val = getattr(old_value, "bpmnprof_ItemDefinition251", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ItemDefinition251", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ItemDefinition251"):
                opp_val = getattr(value, "bpmnprof_ItemDefinition251", None)
                setattr(value, "bpmnprof_ItemDefinition251", self)

    @property
    def bpmnprof_BPMNMessage246(self):
        return self.__bpmnprof_BPMNMessage246

    @bpmnprof_BPMNMessage246.setter
    def bpmnprof_BPMNMessage246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNMessage__bpmnprof_BPMNMessage246", None)
        self.__bpmnprof_BPMNMessage246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNOperation245"):
                opp_val = getattr(old_value, "bpmnprof_BPMNOperation245", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNOperation245", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNOperation245"):
                opp_val = getattr(value, "bpmnprof_BPMNOperation245", None)
                setattr(value, "bpmnprof_BPMNOperation245", self)

    @property
    def bpmnprof_BPMNMessage343(self):
        return self.__bpmnprof_BPMNMessage343

    @bpmnprof_BPMNMessage343.setter
    def bpmnprof_BPMNMessage343(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNMessage__bpmnprof_BPMNMessage343", None)
        self.__bpmnprof_BPMNMessage343 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_MessageFlow342"):
                opp_val = getattr(old_value, "bpmnprof_MessageFlow342", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_MessageFlow342", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_MessageFlow342"):
                opp_val = getattr(value, "bpmnprof_MessageFlow342", None)
                setattr(value, "bpmnprof_MessageFlow342", self)

    @property
    def bpmnprof_BPMNMessage644(self):
        return self.__bpmnprof_BPMNMessage644

    @bpmnprof_BPMNMessage644.setter
    def bpmnprof_BPMNMessage644(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNMessage__bpmnprof_BPMNMessage644", None)
        self.__bpmnprof_BPMNMessage644 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ReceiveTask"):
                opp_val = getattr(old_value, "bpmnprof_ReceiveTask", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ReceiveTask", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ReceiveTask"):
                opp_val = getattr(value, "bpmnprof_ReceiveTask", None)
                setattr(value, "bpmnprof_ReceiveTask", self)

    def MessageitemRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MessageitemRef method
        pass

class bpmnprof_Resource(ItemDefinition):

    def __init__(self, bpmnprof_Resource: "bpmnprof_ResourceRole" = None, bpmnprof_Resource415: set["bpmnprof_ResourceParameter"] = None):
        self.bpmnprof_Resource = bpmnprof_Resource
        self.bpmnprof_Resource415 = bpmnprof_Resource415 if bpmnprof_Resource415 is not None else set()
        
    @property
    def bpmnprof_Resource415(self):
        return self.__bpmnprof_Resource415

    @bpmnprof_Resource415.setter
    def bpmnprof_Resource415(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Resource__bpmnprof_Resource415", None)
        self.__bpmnprof_Resource415 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_ResourceParameter"):
                    opp_val = getattr(item, "bpmnprof_ResourceParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_ResourceParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_ResourceParameter"):
                    opp_val = getattr(item, "bpmnprof_ResourceParameter", None)
                    
                    setattr(item, "bpmnprof_ResourceParameter", self)
                    

    @property
    def bpmnprof_Resource(self):
        return self.__bpmnprof_Resource

    @bpmnprof_Resource.setter
    def bpmnprof_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Resource__bpmnprof_Resource", None)
        self.__bpmnprof_Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ResourceRole407"):
                opp_val = getattr(old_value, "bpmnprof_ResourceRole407", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ResourceRole407", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ResourceRole407"):
                opp_val = getattr(value, "bpmnprof_ResourceRole407", None)
                setattr(value, "bpmnprof_ResourceRole407", self)

    def ResourceresourceParameters(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceresourceParameters method
        pass

class bpmnprof_Escalation(ItemDefinition):

    def __init__(self, escalationCode: str, bpmnprof_Escalation: "bpmnprof_EscalationEventDefinition" = None):
        self.escalationCode = escalationCode
        self.bpmnprof_Escalation = bpmnprof_Escalation
        
    @property
    def escalationCode(self) -> str:
        return self.__escalationCode

    @escalationCode.setter
    def escalationCode(self, escalationCode: str):
        self.__escalationCode = escalationCode

    @property
    def bpmnprof_Escalation(self):
        return self.__bpmnprof_Escalation

    @bpmnprof_Escalation.setter
    def bpmnprof_Escalation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Escalation__bpmnprof_Escalation", None)
        self.__bpmnprof_Escalation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_EscalationEventDefinition"):
                opp_val = getattr(old_value, "bpmnprof_EscalationEventDefinition", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_EscalationEventDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_EscalationEventDefinition"):
                opp_val = getattr(value, "bpmnprof_EscalationEventDefinition", None)
                setattr(value, "bpmnprof_EscalationEventDefinition", self)

    def EscalationstructureRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement EscalationstructureRef method
        pass

class bpmnprof_BPMNSignal(ItemDefinition):

    def __init__(self, bpmnprof_BPMNSignal: "bpmnprof_SignalEventDefinition" = None):
        self.bpmnprof_BPMNSignal = bpmnprof_BPMNSignal
        
    @property
    def bpmnprof_BPMNSignal(self):
        return self.__bpmnprof_BPMNSignal

    @bpmnprof_BPMNSignal.setter
    def bpmnprof_BPMNSignal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNSignal__bpmnprof_BPMNSignal", None)
        self.__bpmnprof_BPMNSignal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_SignalEventDefinition"):
                opp_val = getattr(old_value, "bpmnprof_SignalEventDefinition", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_SignalEventDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_SignalEventDefinition"):
                opp_val = getattr(value, "bpmnprof_SignalEventDefinition", None)
                setattr(value, "bpmnprof_SignalEventDefinition", self)

    def BPMNSignalstructureRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BPMNSignalstructureRef method
        pass

class bpmnprof_Error(ItemDefinition):

    def __init__(self, errorCode: str, bpmnprof_Error: "bpmnprof_BPMNOperation" = None, bpmnprof_Error552: "bpmnprof_ErrorEventDefinition" = None):
        self.errorCode = errorCode
        self.bpmnprof_Error = bpmnprof_Error
        self.bpmnprof_Error552 = bpmnprof_Error552
        
    @property
    def errorCode(self) -> str:
        return self.__errorCode

    @errorCode.setter
    def errorCode(self, errorCode: str):
        self.__errorCode = errorCode

    @property
    def bpmnprof_Error(self):
        return self.__bpmnprof_Error

    @bpmnprof_Error.setter
    def bpmnprof_Error(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Error__bpmnprof_Error", None)
        self.__bpmnprof_Error = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNOperation248"):
                opp_val = getattr(old_value, "bpmnprof_BPMNOperation248", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNOperation248"):
                opp_val = getattr(value, "bpmnprof_BPMNOperation248", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_BPMNOperation248", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_Error552(self):
        return self.__bpmnprof_Error552

    @bpmnprof_Error552.setter
    def bpmnprof_Error552(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Error__bpmnprof_Error552", None)
        self.__bpmnprof_Error552 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ErrorEventDefinition"):
                opp_val = getattr(old_value, "bpmnprof_ErrorEventDefinition", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ErrorEventDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ErrorEventDefinition"):
                opp_val = getattr(value, "bpmnprof_ErrorEventDefinition", None)
                setattr(value, "bpmnprof_ErrorEventDefinition", self)

class bpmnprof_Interface:

    pass
class bpmnprof_ParameterSet:

    pass
class bpmnprof_OutputPin:

    pass
class bpmnprof_State:

    pass
class bpmnprof_TypedElement:

    pass
class bpmnprof_InputPin:

    pass
class bpmnprof_ActivityParameterNode:

    pass
class bpmnprof_Parameter:

    pass
class bpmnprof_Behavior:

    pass
class RootElement:

    pass
class bpmnprof_PartnerEntity(RootElement):

    def __init__(self, PartnerEntity: "bpmnprof_Participant" = None, bpmnprof_PartnerEntity: "bpmnprof_InstanceSpecification" = None, partnerEntityRef: set["bpmnprof_Participant"] = None):
        self.PartnerEntity = PartnerEntity
        self.bpmnprof_PartnerEntity = bpmnprof_PartnerEntity
        self.partnerEntityRef = partnerEntityRef if partnerEntityRef is not None else set()
        
    @property
    def bpmnprof_PartnerEntity(self):
        return self.__bpmnprof_PartnerEntity

    @bpmnprof_PartnerEntity.setter
    def bpmnprof_PartnerEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_PartnerEntity__bpmnprof_PartnerEntity", None)
        self.__bpmnprof_PartnerEntity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_InstanceSpecification"):
                opp_val = getattr(old_value, "bpmnprof_InstanceSpecification", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_InstanceSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_InstanceSpecification"):
                opp_val = getattr(value, "bpmnprof_InstanceSpecification", None)
                setattr(value, "bpmnprof_InstanceSpecification", self)

    @property
    def PartnerEntity(self):
        return self.__PartnerEntity

    @PartnerEntity.setter
    def PartnerEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_PartnerEntity__PartnerEntity", None)
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
    def partnerEntityRef(self):
        return self.__partnerEntityRef

    @partnerEntityRef.setter
    def partnerEntityRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_PartnerEntity__partnerEntityRef", None)
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
                    

    def PartnerEntityparticipantRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement PartnerEntityparticipantRef method
        pass

class bpmnprof_Category(RootElement):

    pass
class bpmnprof_DataStore(RootElement):

    def __init__(self, capacity: str, isUnlimited: str, bpmnprof_DataStore: "bpmnprof_Class" = None, bpmnprof_DataStore582: "bpmnprof_ItemDefinition" = None, bpmnprof_DataStore585: "bpmnprof_DataStoreReference" = None):
        self.capacity = capacity
        self.isUnlimited = isUnlimited
        self.bpmnprof_DataStore = bpmnprof_DataStore
        self.bpmnprof_DataStore582 = bpmnprof_DataStore582
        self.bpmnprof_DataStore585 = bpmnprof_DataStore585
        
    @property
    def capacity(self) -> str:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: str):
        self.__capacity = capacity

    @property
    def isUnlimited(self) -> str:
        return self.__isUnlimited

    @isUnlimited.setter
    def isUnlimited(self, isUnlimited: str):
        self.__isUnlimited = isUnlimited

    @property
    def bpmnprof_DataStore582(self):
        return self.__bpmnprof_DataStore582

    @bpmnprof_DataStore582.setter
    def bpmnprof_DataStore582(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataStore__bpmnprof_DataStore582", None)
        self.__bpmnprof_DataStore582 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ItemDefinition583"):
                opp_val = getattr(old_value, "bpmnprof_ItemDefinition583", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ItemDefinition583", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ItemDefinition583"):
                opp_val = getattr(value, "bpmnprof_ItemDefinition583", None)
                setattr(value, "bpmnprof_ItemDefinition583", self)

    @property
    def bpmnprof_DataStore585(self):
        return self.__bpmnprof_DataStore585

    @bpmnprof_DataStore585.setter
    def bpmnprof_DataStore585(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataStore__bpmnprof_DataStore585", None)
        self.__bpmnprof_DataStore585 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_DataStoreReference"):
                opp_val = getattr(old_value, "bpmnprof_DataStoreReference", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_DataStoreReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_DataStoreReference"):
                opp_val = getattr(value, "bpmnprof_DataStoreReference", None)
                setattr(value, "bpmnprof_DataStoreReference", self)

    @property
    def bpmnprof_DataStore(self):
        return self.__bpmnprof_DataStore

    @bpmnprof_DataStore.setter
    def bpmnprof_DataStore(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataStore__bpmnprof_DataStore", None)
        self.__bpmnprof_DataStore = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Class580"):
                opp_val = getattr(old_value, "bpmnprof_Class580", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Class580", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Class580"):
                opp_val = getattr(value, "bpmnprof_Class580", None)
                setattr(value, "bpmnprof_Class580", self)

class bpmnprof_EventDefinition(RootElement):

    pass
class bpmnprof_BPMNInterface(RootElement):

    def __init__(self, bpmnprof_BPMNInterface: "bpmnprof_CallableElement" = None, bpmnprof_BPMNInterface228: "bpmnprof_Interface" = None, bpmnprof_BPMNInterface230: "bpmnprof_Element" = None, bpmnprof_BPMNInterface233: set["bpmnprof_BPMNOperation"] = None, bpmnprof_BPMNInterface235: set["bpmnprof_CallableElement"] = None, bpmnprof_BPMNInterface301: "bpmnprof_Participant" = None):
        self.bpmnprof_BPMNInterface = bpmnprof_BPMNInterface
        self.bpmnprof_BPMNInterface228 = bpmnprof_BPMNInterface228
        self.bpmnprof_BPMNInterface230 = bpmnprof_BPMNInterface230
        self.bpmnprof_BPMNInterface233 = bpmnprof_BPMNInterface233 if bpmnprof_BPMNInterface233 is not None else set()
        self.bpmnprof_BPMNInterface235 = bpmnprof_BPMNInterface235 if bpmnprof_BPMNInterface235 is not None else set()
        self.bpmnprof_BPMNInterface301 = bpmnprof_BPMNInterface301
        
    @property
    def bpmnprof_BPMNInterface228(self):
        return self.__bpmnprof_BPMNInterface228

    @bpmnprof_BPMNInterface228.setter
    def bpmnprof_BPMNInterface228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNInterface__bpmnprof_BPMNInterface228", None)
        self.__bpmnprof_BPMNInterface228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Interface"):
                opp_val = getattr(old_value, "bpmnprof_Interface", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Interface", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Interface"):
                opp_val = getattr(value, "bpmnprof_Interface", None)
                setattr(value, "bpmnprof_Interface", self)

    @property
    def bpmnprof_BPMNInterface230(self):
        return self.__bpmnprof_BPMNInterface230

    @bpmnprof_BPMNInterface230.setter
    def bpmnprof_BPMNInterface230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNInterface__bpmnprof_BPMNInterface230", None)
        self.__bpmnprof_BPMNInterface230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Element231"):
                opp_val = getattr(old_value, "bpmnprof_Element231", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Element231", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Element231"):
                opp_val = getattr(value, "bpmnprof_Element231", None)
                setattr(value, "bpmnprof_Element231", self)

    @property
    def bpmnprof_BPMNInterface233(self):
        return self.__bpmnprof_BPMNInterface233

    @bpmnprof_BPMNInterface233.setter
    def bpmnprof_BPMNInterface233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNInterface__bpmnprof_BPMNInterface233", None)
        self.__bpmnprof_BPMNInterface233 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_BPMNOperation"):
                    opp_val = getattr(item, "bpmnprof_BPMNOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_BPMNOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_BPMNOperation"):
                    opp_val = getattr(item, "bpmnprof_BPMNOperation", None)
                    
                    setattr(item, "bpmnprof_BPMNOperation", self)
                    

    @property
    def bpmnprof_BPMNInterface(self):
        return self.__bpmnprof_BPMNInterface

    @bpmnprof_BPMNInterface.setter
    def bpmnprof_BPMNInterface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNInterface__bpmnprof_BPMNInterface", None)
        self.__bpmnprof_BPMNInterface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_CallableElement152"):
                opp_val = getattr(old_value, "bpmnprof_CallableElement152", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_CallableElement152"):
                opp_val = getattr(value, "bpmnprof_CallableElement152", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_CallableElement152", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_BPMNInterface235(self):
        return self.__bpmnprof_BPMNInterface235

    @bpmnprof_BPMNInterface235.setter
    def bpmnprof_BPMNInterface235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNInterface__bpmnprof_BPMNInterface235", None)
        self.__bpmnprof_BPMNInterface235 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_CallableElement236"):
                    opp_val = getattr(item, "bpmnprof_CallableElement236", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_CallableElement236", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_CallableElement236"):
                    opp_val = getattr(item, "bpmnprof_CallableElement236", None)
                    
                    setattr(item, "bpmnprof_CallableElement236", self)
                    

    @property
    def bpmnprof_BPMNInterface301(self):
        return self.__bpmnprof_BPMNInterface301

    @bpmnprof_BPMNInterface301.setter
    def bpmnprof_BPMNInterface301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNInterface__bpmnprof_BPMNInterface301", None)
        self.__bpmnprof_BPMNInterface301 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Participant300"):
                opp_val = getattr(old_value, "bpmnprof_Participant300", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Participant300"):
                opp_val = getattr(value, "bpmnprof_Participant300", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_Participant300", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def Interfaceoperationmultiplicity(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement Interfaceoperationmultiplicity method
        pass

    def BPMNInterfaceoperations(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement BPMNInterfaceoperations method
        pass

    def InterfaceownedOperation(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement InterfaceownedOperation method
        pass

    def BPMNInterfacecallableElements(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BPMNInterfacecallableElements method
        pass

class bpmnprof_PartnerRole(RootElement):

    def __init__(self, PartnerRole: "bpmnprof_Participant" = None, bpmnprof_PartnerRole: "bpmnprof_Class" = None, partnerRoleRef: set["bpmnprof_Participant"] = None):
        self.PartnerRole = PartnerRole
        self.bpmnprof_PartnerRole = bpmnprof_PartnerRole
        self.partnerRoleRef = partnerRoleRef if partnerRoleRef is not None else set()
        
    @property
    def bpmnprof_PartnerRole(self):
        return self.__bpmnprof_PartnerRole

    @bpmnprof_PartnerRole.setter
    def bpmnprof_PartnerRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_PartnerRole__bpmnprof_PartnerRole", None)
        self.__bpmnprof_PartnerRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Class321"):
                opp_val = getattr(old_value, "bpmnprof_Class321", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Class321", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Class321"):
                opp_val = getattr(value, "bpmnprof_Class321", None)
                setattr(value, "bpmnprof_Class321", self)

    @property
    def partnerRoleRef(self):
        return self.__partnerRoleRef

    @partnerRoleRef.setter
    def partnerRoleRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_PartnerRole__partnerRoleRef", None)
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
        old_value = getattr(self, f"_bpmnprof_PartnerRole__PartnerRole", None)
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

    def PartnerRoleparticipantRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement PartnerRoleparticipantRef method
        pass

class bpmnprof_ItemDefinition(RootElement):

    def __init__(self, isCollection: str, itemKind: str, bpmnprof_ItemDefinition187: "bpmnprof_Class" = None, bpmnprof_ItemDefinition190: "bpmnprof_Element" = None, bpmnprof_ItemDefinition193: "bpmnprof_Import" = None, bpmnprof_ItemDefinition: "bpmnprof_ItemAwareElement" = None, bpmnprof_ItemDefinition251: "bpmnprof_BPMNMessage" = None, bpmnprof_ItemDefinition366: "bpmnprof_CorrelationProperty" = None, bpmnprof_ItemDefinition379: "bpmnprof_FormalExpression" = None, bpmnprof_ItemDefinition421: "bpmnprof_ResourceParameter" = None, bpmnprof_ItemDefinition583: "bpmnprof_DataStore" = None):
        self.isCollection = isCollection
        self.itemKind = itemKind
        self.bpmnprof_ItemDefinition187 = bpmnprof_ItemDefinition187
        self.bpmnprof_ItemDefinition190 = bpmnprof_ItemDefinition190
        self.bpmnprof_ItemDefinition193 = bpmnprof_ItemDefinition193
        self.bpmnprof_ItemDefinition = bpmnprof_ItemDefinition
        self.bpmnprof_ItemDefinition251 = bpmnprof_ItemDefinition251
        self.bpmnprof_ItemDefinition366 = bpmnprof_ItemDefinition366
        self.bpmnprof_ItemDefinition379 = bpmnprof_ItemDefinition379
        self.bpmnprof_ItemDefinition421 = bpmnprof_ItemDefinition421
        self.bpmnprof_ItemDefinition583 = bpmnprof_ItemDefinition583
        
    @property
    def itemKind(self) -> str:
        return self.__itemKind

    @itemKind.setter
    def itemKind(self, itemKind: str):
        self.__itemKind = itemKind

    @property
    def isCollection(self) -> str:
        return self.__isCollection

    @isCollection.setter
    def isCollection(self, isCollection: str):
        self.__isCollection = isCollection

    @property
    def bpmnprof_ItemDefinition583(self):
        return self.__bpmnprof_ItemDefinition583

    @bpmnprof_ItemDefinition583.setter
    def bpmnprof_ItemDefinition583(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ItemDefinition__bpmnprof_ItemDefinition583", None)
        self.__bpmnprof_ItemDefinition583 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_DataStore582"):
                opp_val = getattr(old_value, "bpmnprof_DataStore582", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_DataStore582", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_DataStore582"):
                opp_val = getattr(value, "bpmnprof_DataStore582", None)
                setattr(value, "bpmnprof_DataStore582", self)

    @property
    def bpmnprof_ItemDefinition193(self):
        return self.__bpmnprof_ItemDefinition193

    @bpmnprof_ItemDefinition193.setter
    def bpmnprof_ItemDefinition193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ItemDefinition__bpmnprof_ItemDefinition193", None)
        self.__bpmnprof_ItemDefinition193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Import194"):
                opp_val = getattr(old_value, "bpmnprof_Import194", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Import194", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Import194"):
                opp_val = getattr(value, "bpmnprof_Import194", None)
                setattr(value, "bpmnprof_Import194", self)

    @property
    def bpmnprof_ItemDefinition(self):
        return self.__bpmnprof_ItemDefinition

    @bpmnprof_ItemDefinition.setter
    def bpmnprof_ItemDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ItemDefinition__bpmnprof_ItemDefinition", None)
        self.__bpmnprof_ItemDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ItemAwareElement183"):
                opp_val = getattr(old_value, "bpmnprof_ItemAwareElement183", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ItemAwareElement183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ItemAwareElement183"):
                opp_val = getattr(value, "bpmnprof_ItemAwareElement183", None)
                setattr(value, "bpmnprof_ItemAwareElement183", self)

    @property
    def bpmnprof_ItemDefinition190(self):
        return self.__bpmnprof_ItemDefinition190

    @bpmnprof_ItemDefinition190.setter
    def bpmnprof_ItemDefinition190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ItemDefinition__bpmnprof_ItemDefinition190", None)
        self.__bpmnprof_ItemDefinition190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Element191"):
                opp_val = getattr(old_value, "bpmnprof_Element191", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Element191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Element191"):
                opp_val = getattr(value, "bpmnprof_Element191", None)
                setattr(value, "bpmnprof_Element191", self)

    @property
    def bpmnprof_ItemDefinition251(self):
        return self.__bpmnprof_ItemDefinition251

    @bpmnprof_ItemDefinition251.setter
    def bpmnprof_ItemDefinition251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ItemDefinition__bpmnprof_ItemDefinition251", None)
        self.__bpmnprof_ItemDefinition251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNMessage250"):
                opp_val = getattr(old_value, "bpmnprof_BPMNMessage250", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNMessage250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNMessage250"):
                opp_val = getattr(value, "bpmnprof_BPMNMessage250", None)
                setattr(value, "bpmnprof_BPMNMessage250", self)

    @property
    def bpmnprof_ItemDefinition187(self):
        return self.__bpmnprof_ItemDefinition187

    @bpmnprof_ItemDefinition187.setter
    def bpmnprof_ItemDefinition187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ItemDefinition__bpmnprof_ItemDefinition187", None)
        self.__bpmnprof_ItemDefinition187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Class188"):
                opp_val = getattr(old_value, "bpmnprof_Class188", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Class188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Class188"):
                opp_val = getattr(value, "bpmnprof_Class188", None)
                setattr(value, "bpmnprof_Class188", self)

    @property
    def bpmnprof_ItemDefinition366(self):
        return self.__bpmnprof_ItemDefinition366

    @bpmnprof_ItemDefinition366.setter
    def bpmnprof_ItemDefinition366(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ItemDefinition__bpmnprof_ItemDefinition366", None)
        self.__bpmnprof_ItemDefinition366 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_CorrelationProperty365"):
                opp_val = getattr(old_value, "bpmnprof_CorrelationProperty365", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_CorrelationProperty365", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_CorrelationProperty365"):
                opp_val = getattr(value, "bpmnprof_CorrelationProperty365", None)
                setattr(value, "bpmnprof_CorrelationProperty365", self)

    @property
    def bpmnprof_ItemDefinition421(self):
        return self.__bpmnprof_ItemDefinition421

    @bpmnprof_ItemDefinition421.setter
    def bpmnprof_ItemDefinition421(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ItemDefinition__bpmnprof_ItemDefinition421", None)
        self.__bpmnprof_ItemDefinition421 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ResourceParameter420"):
                opp_val = getattr(old_value, "bpmnprof_ResourceParameter420", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ResourceParameter420", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ResourceParameter420"):
                opp_val = getattr(value, "bpmnprof_ResourceParameter420", None)
                setattr(value, "bpmnprof_ResourceParameter420", self)

    @property
    def bpmnprof_ItemDefinition379(self):
        return self.__bpmnprof_ItemDefinition379

    @bpmnprof_ItemDefinition379.setter
    def bpmnprof_ItemDefinition379(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ItemDefinition__bpmnprof_ItemDefinition379", None)
        self.__bpmnprof_ItemDefinition379 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_FormalExpression378"):
                opp_val = getattr(old_value, "bpmnprof_FormalExpression378", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_FormalExpression378", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_FormalExpression378"):
                opp_val = getattr(value, "bpmnprof_FormalExpression378", None)
                setattr(value, "bpmnprof_FormalExpression378", self)

    def ItemDefinitionstructureRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ItemDefinitionstructureRef method
        pass

class bpmnprof_CallableElement(RootElement):

    def __init__(self, bpmnprof_CallableElement: "bpmnprof_Behavior" = None, bpmnprof_CallableElement150: "bpmnprof_InputOutputSpecification" = None, bpmnprof_CallableElement152: set["bpmnprof_BPMNInterface"] = None, bpmnprof_CallableElement154: set["bpmnprof_InputOutputBinding"] = None, bpmnprof_CallableElement236: "bpmnprof_BPMNInterface" = None, bpmnprof_CallableElement617: "bpmnprof_CallActivity" = None):
        self.bpmnprof_CallableElement = bpmnprof_CallableElement
        self.bpmnprof_CallableElement150 = bpmnprof_CallableElement150
        self.bpmnprof_CallableElement152 = bpmnprof_CallableElement152 if bpmnprof_CallableElement152 is not None else set()
        self.bpmnprof_CallableElement154 = bpmnprof_CallableElement154 if bpmnprof_CallableElement154 is not None else set()
        self.bpmnprof_CallableElement236 = bpmnprof_CallableElement236
        self.bpmnprof_CallableElement617 = bpmnprof_CallableElement617
        
    @property
    def bpmnprof_CallableElement236(self):
        return self.__bpmnprof_CallableElement236

    @bpmnprof_CallableElement236.setter
    def bpmnprof_CallableElement236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_CallableElement__bpmnprof_CallableElement236", None)
        self.__bpmnprof_CallableElement236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNInterface235"):
                opp_val = getattr(old_value, "bpmnprof_BPMNInterface235", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNInterface235"):
                opp_val = getattr(value, "bpmnprof_BPMNInterface235", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_BPMNInterface235", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_CallableElement152(self):
        return self.__bpmnprof_CallableElement152

    @bpmnprof_CallableElement152.setter
    def bpmnprof_CallableElement152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_CallableElement__bpmnprof_CallableElement152", None)
        self.__bpmnprof_CallableElement152 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_BPMNInterface"):
                    opp_val = getattr(item, "bpmnprof_BPMNInterface", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_BPMNInterface", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_BPMNInterface"):
                    opp_val = getattr(item, "bpmnprof_BPMNInterface", None)
                    
                    setattr(item, "bpmnprof_BPMNInterface", self)
                    

    @property
    def bpmnprof_CallableElement617(self):
        return self.__bpmnprof_CallableElement617

    @bpmnprof_CallableElement617.setter
    def bpmnprof_CallableElement617(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_CallableElement__bpmnprof_CallableElement617", None)
        self.__bpmnprof_CallableElement617 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_CallActivity616"):
                opp_val = getattr(old_value, "bpmnprof_CallActivity616", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_CallActivity616", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_CallActivity616"):
                opp_val = getattr(value, "bpmnprof_CallActivity616", None)
                setattr(value, "bpmnprof_CallActivity616", self)

    @property
    def bpmnprof_CallableElement(self):
        return self.__bpmnprof_CallableElement

    @bpmnprof_CallableElement.setter
    def bpmnprof_CallableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_CallableElement__bpmnprof_CallableElement", None)
        self.__bpmnprof_CallableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Behavior"):
                opp_val = getattr(old_value, "bpmnprof_Behavior", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Behavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Behavior"):
                opp_val = getattr(value, "bpmnprof_Behavior", None)
                setattr(value, "bpmnprof_Behavior", self)

    @property
    def bpmnprof_CallableElement154(self):
        return self.__bpmnprof_CallableElement154

    @bpmnprof_CallableElement154.setter
    def bpmnprof_CallableElement154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_CallableElement__bpmnprof_CallableElement154", None)
        self.__bpmnprof_CallableElement154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_InputOutputBinding"):
                    opp_val = getattr(item, "bpmnprof_InputOutputBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_InputOutputBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_InputOutputBinding"):
                    opp_val = getattr(item, "bpmnprof_InputOutputBinding", None)
                    
                    setattr(item, "bpmnprof_InputOutputBinding", self)
                    

    @property
    def bpmnprof_CallableElement150(self):
        return self.__bpmnprof_CallableElement150

    @bpmnprof_CallableElement150.setter
    def bpmnprof_CallableElement150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_CallableElement__bpmnprof_CallableElement150", None)
        self.__bpmnprof_CallableElement150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_InputOutputSpecification"):
                opp_val = getattr(old_value, "bpmnprof_InputOutputSpecification", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_InputOutputSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_InputOutputSpecification"):
                opp_val = getattr(value, "bpmnprof_InputOutputSpecification", None)
                setattr(value, "bpmnprof_InputOutputSpecification", self)

    def CallableEelementsupportedInterfaceRefs(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement CallableEelementsupportedInterfaceRefs method
        pass

    def CallableElementresources(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement CallableElementresources method
        pass

class ItemAwareElement:

    pass
class bpmnprof_DataOutput(ItemAwareElement):

    def __init__(self, isCollection: str, bpmnprof_DataOutput: "bpmnprof_InputOutputSpecification" = None, bpmnprof_DataOutput203: "bpmnprof_OutputPin" = None, bpmnprof_DataOutput205: "bpmnprof_Parameter" = None, bpmnprof_DataOutput208: "bpmnprof_ActivityParameterNode" = None, dataOutputRefs: set["bpmnprof_OutputSet"] = None, bpmnprof_DataOutput222: "bpmnprof_OutputSet" = None, bpmnprof_DataOutput225: "bpmnprof_OutputSet" = None, DataOutput: "bpmnprof_OutputSet" = None, bpmnprof_DataOutput212: set["bpmnprof_OutputSet"] = None, bpmnprof_DataOutput215: set["bpmnprof_OutputSet"] = None, bpmnprof_DataOutput671: "bpmnprof_MultiInstanceLoopCharacteristics" = None):
        self.isCollection = isCollection
        self.bpmnprof_DataOutput = bpmnprof_DataOutput
        self.bpmnprof_DataOutput203 = bpmnprof_DataOutput203
        self.bpmnprof_DataOutput205 = bpmnprof_DataOutput205
        self.bpmnprof_DataOutput208 = bpmnprof_DataOutput208
        self.dataOutputRefs = dataOutputRefs if dataOutputRefs is not None else set()
        self.bpmnprof_DataOutput222 = bpmnprof_DataOutput222
        self.bpmnprof_DataOutput225 = bpmnprof_DataOutput225
        self.DataOutput = DataOutput
        self.bpmnprof_DataOutput212 = bpmnprof_DataOutput212 if bpmnprof_DataOutput212 is not None else set()
        self.bpmnprof_DataOutput215 = bpmnprof_DataOutput215 if bpmnprof_DataOutput215 is not None else set()
        self.bpmnprof_DataOutput671 = bpmnprof_DataOutput671
        
    @property
    def isCollection(self) -> str:
        return self.__isCollection

    @isCollection.setter
    def isCollection(self, isCollection: str):
        self.__isCollection = isCollection

    @property
    def bpmnprof_DataOutput203(self):
        return self.__bpmnprof_DataOutput203

    @bpmnprof_DataOutput203.setter
    def bpmnprof_DataOutput203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataOutput__bpmnprof_DataOutput203", None)
        self.__bpmnprof_DataOutput203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_OutputPin"):
                opp_val = getattr(old_value, "bpmnprof_OutputPin", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_OutputPin", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_OutputPin"):
                opp_val = getattr(value, "bpmnprof_OutputPin", None)
                setattr(value, "bpmnprof_OutputPin", self)

    @property
    def bpmnprof_DataOutput671(self):
        return self.__bpmnprof_DataOutput671

    @bpmnprof_DataOutput671.setter
    def bpmnprof_DataOutput671(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataOutput__bpmnprof_DataOutput671", None)
        self.__bpmnprof_DataOutput671 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_MultiInstanceLoopCharacteristics670"):
                opp_val = getattr(old_value, "bpmnprof_MultiInstanceLoopCharacteristics670", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_MultiInstanceLoopCharacteristics670", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_MultiInstanceLoopCharacteristics670"):
                opp_val = getattr(value, "bpmnprof_MultiInstanceLoopCharacteristics670", None)
                setattr(value, "bpmnprof_MultiInstanceLoopCharacteristics670", self)

    @property
    def dataOutputRefs(self):
        return self.__dataOutputRefs

    @dataOutputRefs.setter
    def dataOutputRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataOutput__dataOutputRefs", None)
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
    def bpmnprof_DataOutput205(self):
        return self.__bpmnprof_DataOutput205

    @bpmnprof_DataOutput205.setter
    def bpmnprof_DataOutput205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataOutput__bpmnprof_DataOutput205", None)
        self.__bpmnprof_DataOutput205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Parameter206"):
                opp_val = getattr(old_value, "bpmnprof_Parameter206", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Parameter206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Parameter206"):
                opp_val = getattr(value, "bpmnprof_Parameter206", None)
                setattr(value, "bpmnprof_Parameter206", self)

    @property
    def bpmnprof_DataOutput208(self):
        return self.__bpmnprof_DataOutput208

    @bpmnprof_DataOutput208.setter
    def bpmnprof_DataOutput208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataOutput__bpmnprof_DataOutput208", None)
        self.__bpmnprof_DataOutput208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ActivityParameterNode209"):
                opp_val = getattr(old_value, "bpmnprof_ActivityParameterNode209", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ActivityParameterNode209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ActivityParameterNode209"):
                opp_val = getattr(value, "bpmnprof_ActivityParameterNode209", None)
                setattr(value, "bpmnprof_ActivityParameterNode209", self)

    @property
    def bpmnprof_DataOutput222(self):
        return self.__bpmnprof_DataOutput222

    @bpmnprof_DataOutput222.setter
    def bpmnprof_DataOutput222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataOutput__bpmnprof_DataOutput222", None)
        self.__bpmnprof_DataOutput222 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_OutputSet221"):
                opp_val = getattr(old_value, "bpmnprof_OutputSet221", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_OutputSet221"):
                opp_val = getattr(value, "bpmnprof_OutputSet221", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_OutputSet221", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DataOutput(self):
        return self.__DataOutput

    @DataOutput.setter
    def DataOutput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataOutput__DataOutput", None)
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
    def bpmnprof_DataOutput212(self):
        return self.__bpmnprof_DataOutput212

    @bpmnprof_DataOutput212.setter
    def bpmnprof_DataOutput212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataOutput__bpmnprof_DataOutput212", None)
        self.__bpmnprof_DataOutput212 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_OutputSet213"):
                    opp_val = getattr(item, "bpmnprof_OutputSet213", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_OutputSet213", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_OutputSet213"):
                    opp_val = getattr(item, "bpmnprof_OutputSet213", None)
                    
                    setattr(item, "bpmnprof_OutputSet213", self)
                    

    @property
    def bpmnprof_DataOutput(self):
        return self.__bpmnprof_DataOutput

    @bpmnprof_DataOutput.setter
    def bpmnprof_DataOutput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataOutput__bpmnprof_DataOutput", None)
        self.__bpmnprof_DataOutput = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_InputOutputSpecification163"):
                opp_val = getattr(old_value, "bpmnprof_InputOutputSpecification163", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_InputOutputSpecification163"):
                opp_val = getattr(value, "bpmnprof_InputOutputSpecification163", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_InputOutputSpecification163", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_DataOutput225(self):
        return self.__bpmnprof_DataOutput225

    @bpmnprof_DataOutput225.setter
    def bpmnprof_DataOutput225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataOutput__bpmnprof_DataOutput225", None)
        self.__bpmnprof_DataOutput225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_OutputSet224"):
                opp_val = getattr(old_value, "bpmnprof_OutputSet224", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_OutputSet224"):
                opp_val = getattr(value, "bpmnprof_OutputSet224", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_OutputSet224", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_DataOutput215(self):
        return self.__bpmnprof_DataOutput215

    @bpmnprof_DataOutput215.setter
    def bpmnprof_DataOutput215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataOutput__bpmnprof_DataOutput215", None)
        self.__bpmnprof_DataOutput215 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_OutputSet216"):
                    opp_val = getattr(item, "bpmnprof_OutputSet216", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_OutputSet216", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_OutputSet216"):
                    opp_val = getattr(item, "bpmnprof_OutputSet216", None)
                    
                    setattr(item, "bpmnprof_OutputSet216", self)
                    

    def DataOutputitemSubjectRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement DataOutputitemSubjectRef method
        pass

    def DataOutputnotation(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement DataOutputnotation method
        pass

class bpmnprof_DataInput(ItemAwareElement):

    def __init__(self, isCollection: str, bpmnprof_DataInput: "bpmnprof_InputOutputSpecification" = None, bpmnprof_DataInput171: "bpmnprof_Parameter" = None, bpmnprof_DataInput173: "bpmnprof_ActivityParameterNode" = None, dataInputRefs: set["bpmnprof_InputSet"] = None, optionalInputRefs: set["bpmnprof_InputSet"] = None, whileExecutingInputRefs: set["bpmnprof_InputSet"] = None, bpmnprof_DataInput169: "bpmnprof_InputPin" = None, DataInput: "bpmnprof_InputSet" = None, DataInput199: "bpmnprof_InputSet" = None, DataInput201: "bpmnprof_InputSet" = None, bpmnprof_DataInput674: "bpmnprof_MultiInstanceLoopCharacteristics" = None):
        self.isCollection = isCollection
        self.bpmnprof_DataInput = bpmnprof_DataInput
        self.bpmnprof_DataInput171 = bpmnprof_DataInput171
        self.bpmnprof_DataInput173 = bpmnprof_DataInput173
        self.dataInputRefs = dataInputRefs if dataInputRefs is not None else set()
        self.optionalInputRefs = optionalInputRefs if optionalInputRefs is not None else set()
        self.whileExecutingInputRefs = whileExecutingInputRefs if whileExecutingInputRefs is not None else set()
        self.bpmnprof_DataInput169 = bpmnprof_DataInput169
        self.DataInput = DataInput
        self.DataInput199 = DataInput199
        self.DataInput201 = DataInput201
        self.bpmnprof_DataInput674 = bpmnprof_DataInput674
        
    @property
    def isCollection(self) -> str:
        return self.__isCollection

    @isCollection.setter
    def isCollection(self, isCollection: str):
        self.__isCollection = isCollection

    @property
    def bpmnprof_DataInput171(self):
        return self.__bpmnprof_DataInput171

    @bpmnprof_DataInput171.setter
    def bpmnprof_DataInput171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataInput__bpmnprof_DataInput171", None)
        self.__bpmnprof_DataInput171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Parameter"):
                opp_val = getattr(old_value, "bpmnprof_Parameter", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Parameter"):
                opp_val = getattr(value, "bpmnprof_Parameter", None)
                setattr(value, "bpmnprof_Parameter", self)

    @property
    def bpmnprof_DataInput(self):
        return self.__bpmnprof_DataInput

    @bpmnprof_DataInput.setter
    def bpmnprof_DataInput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataInput__bpmnprof_DataInput", None)
        self.__bpmnprof_DataInput = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_InputOutputSpecification161"):
                opp_val = getattr(old_value, "bpmnprof_InputOutputSpecification161", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_InputOutputSpecification161"):
                opp_val = getattr(value, "bpmnprof_InputOutputSpecification161", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_InputOutputSpecification161", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_DataInput173(self):
        return self.__bpmnprof_DataInput173

    @bpmnprof_DataInput173.setter
    def bpmnprof_DataInput173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataInput__bpmnprof_DataInput173", None)
        self.__bpmnprof_DataInput173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ActivityParameterNode"):
                opp_val = getattr(old_value, "bpmnprof_ActivityParameterNode", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ActivityParameterNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ActivityParameterNode"):
                opp_val = getattr(value, "bpmnprof_ActivityParameterNode", None)
                setattr(value, "bpmnprof_ActivityParameterNode", self)

    @property
    def bpmnprof_DataInput169(self):
        return self.__bpmnprof_DataInput169

    @bpmnprof_DataInput169.setter
    def bpmnprof_DataInput169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataInput__bpmnprof_DataInput169", None)
        self.__bpmnprof_DataInput169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_InputPin"):
                opp_val = getattr(old_value, "bpmnprof_InputPin", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_InputPin", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_InputPin"):
                opp_val = getattr(value, "bpmnprof_InputPin", None)
                setattr(value, "bpmnprof_InputPin", self)

    @property
    def DataInput199(self):
        return self.__DataInput199

    @DataInput199.setter
    def DataInput199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataInput__DataInput199", None)
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
    def whileExecutingInputRefs(self):
        return self.__whileExecutingInputRefs

    @whileExecutingInputRefs.setter
    def whileExecutingInputRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataInput__whileExecutingInputRefs", None)
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
        old_value = getattr(self, f"_bpmnprof_DataInput__dataInputRefs", None)
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
                    

    @property
    def bpmnprof_DataInput674(self):
        return self.__bpmnprof_DataInput674

    @bpmnprof_DataInput674.setter
    def bpmnprof_DataInput674(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataInput__bpmnprof_DataInput674", None)
        self.__bpmnprof_DataInput674 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_MultiInstanceLoopCharacteristics673"):
                opp_val = getattr(old_value, "bpmnprof_MultiInstanceLoopCharacteristics673", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_MultiInstanceLoopCharacteristics673", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_MultiInstanceLoopCharacteristics673"):
                opp_val = getattr(value, "bpmnprof_MultiInstanceLoopCharacteristics673", None)
                setattr(value, "bpmnprof_MultiInstanceLoopCharacteristics673", self)

    @property
    def optionalInputRefs(self):
        return self.__optionalInputRefs

    @optionalInputRefs.setter
    def optionalInputRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataInput__optionalInputRefs", None)
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
    def DataInput201(self):
        return self.__DataInput201

    @DataInput201.setter
    def DataInput201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataInput__DataInput201", None)
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
    def DataInput(self):
        return self.__DataInput

    @DataInput.setter
    def DataInput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataInput__DataInput", None)
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

    def DataInputAssociation(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement DataInputAssociation method
        pass

    def DataInputnotation(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement DataInputnotation method
        pass

    def DataInputitemSubjectRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement DataInputitemSubjectRef method
        pass

class bpmnprof_Action:

    pass
class bpmnprof_BPMNProperty(ItemAwareElement):

    def __init__(self, bpmnprof_BPMNProperty: "bpmnprof_BPMNProcess" = None, bpmnprof_BPMNProperty398: "bpmnprof_DataStoreNode" = None, bpmnprof_BPMNProperty400: "bpmnprof_Property" = None, bpmnprof_BPMNProperty447: "bpmnprof_BPMNActivity" = None, bpmnprof_BPMNProperty478: "bpmnprof_BPMNEvent" = None):
        self.bpmnprof_BPMNProperty = bpmnprof_BPMNProperty
        self.bpmnprof_BPMNProperty398 = bpmnprof_BPMNProperty398
        self.bpmnprof_BPMNProperty400 = bpmnprof_BPMNProperty400
        self.bpmnprof_BPMNProperty447 = bpmnprof_BPMNProperty447
        self.bpmnprof_BPMNProperty478 = bpmnprof_BPMNProperty478
        
    @property
    def bpmnprof_BPMNProperty(self):
        return self.__bpmnprof_BPMNProperty

    @bpmnprof_BPMNProperty.setter
    def bpmnprof_BPMNProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNProperty__bpmnprof_BPMNProperty", None)
        self.__bpmnprof_BPMNProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNProcess146"):
                opp_val = getattr(old_value, "bpmnprof_BPMNProcess146", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNProcess146"):
                opp_val = getattr(value, "bpmnprof_BPMNProcess146", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_BPMNProcess146", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_BPMNProperty400(self):
        return self.__bpmnprof_BPMNProperty400

    @bpmnprof_BPMNProperty400.setter
    def bpmnprof_BPMNProperty400(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNProperty__bpmnprof_BPMNProperty400", None)
        self.__bpmnprof_BPMNProperty400 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Property401"):
                opp_val = getattr(old_value, "bpmnprof_Property401", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Property401", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Property401"):
                opp_val = getattr(value, "bpmnprof_Property401", None)
                setattr(value, "bpmnprof_Property401", self)

    @property
    def bpmnprof_BPMNProperty447(self):
        return self.__bpmnprof_BPMNProperty447

    @bpmnprof_BPMNProperty447.setter
    def bpmnprof_BPMNProperty447(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNProperty__bpmnprof_BPMNProperty447", None)
        self.__bpmnprof_BPMNProperty447 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNActivity446"):
                opp_val = getattr(old_value, "bpmnprof_BPMNActivity446", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNActivity446"):
                opp_val = getattr(value, "bpmnprof_BPMNActivity446", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_BPMNActivity446", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_BPMNProperty478(self):
        return self.__bpmnprof_BPMNProperty478

    @bpmnprof_BPMNProperty478.setter
    def bpmnprof_BPMNProperty478(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNProperty__bpmnprof_BPMNProperty478", None)
        self.__bpmnprof_BPMNProperty478 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNEvent477"):
                opp_val = getattr(old_value, "bpmnprof_BPMNEvent477", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNEvent477"):
                opp_val = getattr(value, "bpmnprof_BPMNEvent477", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_BPMNEvent477", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_BPMNProperty398(self):
        return self.__bpmnprof_BPMNProperty398

    @bpmnprof_BPMNProperty398.setter
    def bpmnprof_BPMNProperty398(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNProperty__bpmnprof_BPMNProperty398", None)
        self.__bpmnprof_BPMNProperty398 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_DataStoreNode"):
                opp_val = getattr(old_value, "bpmnprof_DataStoreNode", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_DataStoreNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_DataStoreNode"):
                opp_val = getattr(value, "bpmnprof_DataStoreNode", None)
                setattr(value, "bpmnprof_DataStoreNode", self)

    def Propertynotation(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement Propertynotation method
        pass

    def BPMNPropertyapply(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BPMNPropertyapply method
        pass

class bpmnprof_Activity:

    pass
class bpmnprof_BPMNCollaboration(RootElement):

    def __init__(self, isClosed: str, bpmnprof_BPMNCollaboration: "bpmnprof_BPMNProcess" = None, collaboration: set["bpmnprof_ConversationLink"] = None, bpmnprof_BPMNCollaboration268: set["bpmnprof_MessageFlowAssociation"] = None, bpmnprof_BPMNCollaboration265: set["bpmnprof_ParticipantAssociation"] = None, bpmnprof_BPMNCollaboration270: set["bpmnprof_MessageFlow"] = None, bpmnprof_BPMNCollaboration272: "bpmnprof_Collaboration" = None, bpmnprof_BPMNCollaboration274: set["bpmnprof_ConversationNode"] = None, bpmnprof_BPMNCollaboration276: set["bpmnprof_CorrelationKey"] = None, bpmnprof_BPMNCollaboration278: set["bpmnprof_Participant"] = None, BPMNCollaboration: "bpmnprof_ConversationLink" = None, bpmnprof_BPMNCollaboration605: "bpmnprof_CallConversation" = None):
        self.isClosed = isClosed
        self.bpmnprof_BPMNCollaboration = bpmnprof_BPMNCollaboration
        self.collaboration = collaboration if collaboration is not None else set()
        self.bpmnprof_BPMNCollaboration268 = bpmnprof_BPMNCollaboration268 if bpmnprof_BPMNCollaboration268 is not None else set()
        self.bpmnprof_BPMNCollaboration265 = bpmnprof_BPMNCollaboration265 if bpmnprof_BPMNCollaboration265 is not None else set()
        self.bpmnprof_BPMNCollaboration270 = bpmnprof_BPMNCollaboration270 if bpmnprof_BPMNCollaboration270 is not None else set()
        self.bpmnprof_BPMNCollaboration272 = bpmnprof_BPMNCollaboration272
        self.bpmnprof_BPMNCollaboration274 = bpmnprof_BPMNCollaboration274 if bpmnprof_BPMNCollaboration274 is not None else set()
        self.bpmnprof_BPMNCollaboration276 = bpmnprof_BPMNCollaboration276 if bpmnprof_BPMNCollaboration276 is not None else set()
        self.bpmnprof_BPMNCollaboration278 = bpmnprof_BPMNCollaboration278 if bpmnprof_BPMNCollaboration278 is not None else set()
        self.BPMNCollaboration = BPMNCollaboration
        self.bpmnprof_BPMNCollaboration605 = bpmnprof_BPMNCollaboration605
        
    @property
    def isClosed(self) -> str:
        return self.__isClosed

    @isClosed.setter
    def isClosed(self, isClosed: str):
        self.__isClosed = isClosed

    @property
    def bpmnprof_BPMNCollaboration(self):
        return self.__bpmnprof_BPMNCollaboration

    @bpmnprof_BPMNCollaboration.setter
    def bpmnprof_BPMNCollaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNCollaboration__bpmnprof_BPMNCollaboration", None)
        self.__bpmnprof_BPMNCollaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNProcess134"):
                opp_val = getattr(old_value, "bpmnprof_BPMNProcess134", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNProcess134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNProcess134"):
                opp_val = getattr(value, "bpmnprof_BPMNProcess134", None)
                setattr(value, "bpmnprof_BPMNProcess134", self)

    @property
    def bpmnprof_BPMNCollaboration605(self):
        return self.__bpmnprof_BPMNCollaboration605

    @bpmnprof_BPMNCollaboration605.setter
    def bpmnprof_BPMNCollaboration605(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNCollaboration__bpmnprof_BPMNCollaboration605", None)
        self.__bpmnprof_BPMNCollaboration605 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_CallConversation604"):
                opp_val = getattr(old_value, "bpmnprof_CallConversation604", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_CallConversation604", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_CallConversation604"):
                opp_val = getattr(value, "bpmnprof_CallConversation604", None)
                setattr(value, "bpmnprof_CallConversation604", self)

    @property
    def bpmnprof_BPMNCollaboration265(self):
        return self.__bpmnprof_BPMNCollaboration265

    @bpmnprof_BPMNCollaboration265.setter
    def bpmnprof_BPMNCollaboration265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNCollaboration__bpmnprof_BPMNCollaboration265", None)
        self.__bpmnprof_BPMNCollaboration265 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_ParticipantAssociation"):
                    opp_val = getattr(item, "bpmnprof_ParticipantAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_ParticipantAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_ParticipantAssociation"):
                    opp_val = getattr(item, "bpmnprof_ParticipantAssociation", None)
                    
                    setattr(item, "bpmnprof_ParticipantAssociation", self)
                    

    @property
    def bpmnprof_BPMNCollaboration272(self):
        return self.__bpmnprof_BPMNCollaboration272

    @bpmnprof_BPMNCollaboration272.setter
    def bpmnprof_BPMNCollaboration272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNCollaboration__bpmnprof_BPMNCollaboration272", None)
        self.__bpmnprof_BPMNCollaboration272 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Collaboration"):
                opp_val = getattr(old_value, "bpmnprof_Collaboration", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Collaboration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Collaboration"):
                opp_val = getattr(value, "bpmnprof_Collaboration", None)
                setattr(value, "bpmnprof_Collaboration", self)

    @property
    def bpmnprof_BPMNCollaboration270(self):
        return self.__bpmnprof_BPMNCollaboration270

    @bpmnprof_BPMNCollaboration270.setter
    def bpmnprof_BPMNCollaboration270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNCollaboration__bpmnprof_BPMNCollaboration270", None)
        self.__bpmnprof_BPMNCollaboration270 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_MessageFlow"):
                    opp_val = getattr(item, "bpmnprof_MessageFlow", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_MessageFlow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_MessageFlow"):
                    opp_val = getattr(item, "bpmnprof_MessageFlow", None)
                    
                    setattr(item, "bpmnprof_MessageFlow", self)
                    

    @property
    def bpmnprof_BPMNCollaboration276(self):
        return self.__bpmnprof_BPMNCollaboration276

    @bpmnprof_BPMNCollaboration276.setter
    def bpmnprof_BPMNCollaboration276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNCollaboration__bpmnprof_BPMNCollaboration276", None)
        self.__bpmnprof_BPMNCollaboration276 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_CorrelationKey"):
                    opp_val = getattr(item, "bpmnprof_CorrelationKey", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_CorrelationKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_CorrelationKey"):
                    opp_val = getattr(item, "bpmnprof_CorrelationKey", None)
                    
                    setattr(item, "bpmnprof_CorrelationKey", self)
                    

    @property
    def collaboration(self):
        return self.__collaboration

    @collaboration.setter
    def collaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNCollaboration__collaboration", None)
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
    def BPMNCollaboration(self):
        return self.__BPMNCollaboration

    @BPMNCollaboration.setter
    def BPMNCollaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNCollaboration__BPMNCollaboration", None)
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
    def bpmnprof_BPMNCollaboration274(self):
        return self.__bpmnprof_BPMNCollaboration274

    @bpmnprof_BPMNCollaboration274.setter
    def bpmnprof_BPMNCollaboration274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNCollaboration__bpmnprof_BPMNCollaboration274", None)
        self.__bpmnprof_BPMNCollaboration274 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_ConversationNode"):
                    opp_val = getattr(item, "bpmnprof_ConversationNode", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_ConversationNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_ConversationNode"):
                    opp_val = getattr(item, "bpmnprof_ConversationNode", None)
                    
                    setattr(item, "bpmnprof_ConversationNode", self)
                    

    @property
    def bpmnprof_BPMNCollaboration268(self):
        return self.__bpmnprof_BPMNCollaboration268

    @bpmnprof_BPMNCollaboration268.setter
    def bpmnprof_BPMNCollaboration268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNCollaboration__bpmnprof_BPMNCollaboration268", None)
        self.__bpmnprof_BPMNCollaboration268 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_MessageFlowAssociation"):
                    opp_val = getattr(item, "bpmnprof_MessageFlowAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_MessageFlowAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_MessageFlowAssociation"):
                    opp_val = getattr(item, "bpmnprof_MessageFlowAssociation", None)
                    
                    setattr(item, "bpmnprof_MessageFlowAssociation", self)
                    

    @property
    def bpmnprof_BPMNCollaboration278(self):
        return self.__bpmnprof_BPMNCollaboration278

    @bpmnprof_BPMNCollaboration278.setter
    def bpmnprof_BPMNCollaboration278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNCollaboration__bpmnprof_BPMNCollaboration278", None)
        self.__bpmnprof_BPMNCollaboration278 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_Participant"):
                    opp_val = getattr(item, "bpmnprof_Participant", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_Participant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_Participant"):
                    opp_val = getattr(item, "bpmnprof_Participant", None)
                    
                    setattr(item, "bpmnprof_Participant", self)
                    

    def Collaborationparticipants(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement Collaborationparticipants method
        pass

class bpmnprof_Constraint:

    pass
class bpmnprof_PackageImport:

    pass
class FlowElementsContainer:

    pass
class bpmnprof_SubProcess(FlowElementsContainer, BPMNActivity):

    def __init__(self, triggeredByEvent: str, bpmnprof_SubProcess: "bpmnprof_StructuredActivityNode" = None, bpmnprof_SubProcess612: set["bpmnprof_LaneSet"] = None):
        self.triggeredByEvent = triggeredByEvent
        self.bpmnprof_SubProcess = bpmnprof_SubProcess
        self.bpmnprof_SubProcess612 = bpmnprof_SubProcess612 if bpmnprof_SubProcess612 is not None else set()
        
    @property
    def triggeredByEvent(self) -> str:
        return self.__triggeredByEvent

    @triggeredByEvent.setter
    def triggeredByEvent(self, triggeredByEvent: str):
        self.__triggeredByEvent = triggeredByEvent

    @property
    def bpmnprof_SubProcess(self):
        return self.__bpmnprof_SubProcess

    @bpmnprof_SubProcess.setter
    def bpmnprof_SubProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_SubProcess__bpmnprof_SubProcess", None)
        self.__bpmnprof_SubProcess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_StructuredActivityNode610"):
                opp_val = getattr(old_value, "bpmnprof_StructuredActivityNode610", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_StructuredActivityNode610", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_StructuredActivityNode610"):
                opp_val = getattr(value, "bpmnprof_StructuredActivityNode610", None)
                setattr(value, "bpmnprof_StructuredActivityNode610", self)

    @property
    def bpmnprof_SubProcess612(self):
        return self.__bpmnprof_SubProcess612

    @bpmnprof_SubProcess612.setter
    def bpmnprof_SubProcess612(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_SubProcess__bpmnprof_SubProcess612", None)
        self.__bpmnprof_SubProcess612 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_LaneSet613"):
                    opp_val = getattr(item, "bpmnprof_LaneSet613", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_LaneSet613", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_LaneSet613"):
                    opp_val = getattr(item, "bpmnprof_LaneSet613", None)
                    
                    setattr(item, "bpmnprof_LaneSet613", self)
                    

    def SubProcesstriggeredByEvent(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SubProcesstriggeredByEvent method
        pass

class CallableElement:

    pass
class bpmnprof_GlobalTask(CallableElement):

    def __init__(self, bpmnprof_GlobalTask: "bpmnprof_OpaqueBehavior" = None, bpmnprof_GlobalTask433: set["bpmnprof_ResourceRole"] = None):
        self.bpmnprof_GlobalTask = bpmnprof_GlobalTask
        self.bpmnprof_GlobalTask433 = bpmnprof_GlobalTask433 if bpmnprof_GlobalTask433 is not None else set()
        
    @property
    def bpmnprof_GlobalTask(self):
        return self.__bpmnprof_GlobalTask

    @bpmnprof_GlobalTask.setter
    def bpmnprof_GlobalTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_GlobalTask__bpmnprof_GlobalTask", None)
        self.__bpmnprof_GlobalTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_OpaqueBehavior"):
                opp_val = getattr(old_value, "bpmnprof_OpaqueBehavior", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_OpaqueBehavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_OpaqueBehavior"):
                opp_val = getattr(value, "bpmnprof_OpaqueBehavior", None)
                setattr(value, "bpmnprof_OpaqueBehavior", self)

    @property
    def bpmnprof_GlobalTask433(self):
        return self.__bpmnprof_GlobalTask433

    @bpmnprof_GlobalTask433.setter
    def bpmnprof_GlobalTask433(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_GlobalTask__bpmnprof_GlobalTask433", None)
        self.__bpmnprof_GlobalTask433 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_ResourceRole434"):
                    opp_val = getattr(item, "bpmnprof_ResourceRole434", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_ResourceRole434", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_ResourceRole434"):
                    opp_val = getattr(item, "bpmnprof_ResourceRole434", None)
                    
                    setattr(item, "bpmnprof_ResourceRole434", self)
                    

    def GlobalTasksupportedInterfaceRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement GlobalTasksupportedInterfaceRefs method
        pass

class bpmnprof_BPMNProcess(FlowElementsContainer, CallableElement):

    def __init__(self, isExecutable: str, processType: str, isClosed: str, bpmnprof_BPMNProcess134: "bpmnprof_BPMNCollaboration" = None, bpmnprof_BPMNProcess136: "bpmnprof_Activity" = None, bpmnprof_BPMNProcess138: set["bpmnprof_CorrelationSubscription"] = None, bpmnprof_BPMNProcess140: "bpmnprof_Monitoring" = None, bpmnprof_BPMNProcess144: "bpmnprof_BPMNProcess" = None, bpmnprof_BPMNProcess142: "bpmnprof_BPMNProcess" = None, bpmnprof_BPMNProcess146: set["bpmnprof_BPMNProperty"] = None, bpmnprof_BPMNProcess: "bpmnprof_Auditing" = None, process: set["bpmnprof_ResourceRole"] = None, bpmnprof_BPMNProcess293: "bpmnprof_Participant" = None, BPMNProcess: "bpmnprof_ResourceRole" = None):
        self.isExecutable = isExecutable
        self.processType = processType
        self.isClosed = isClosed
        self.bpmnprof_BPMNProcess134 = bpmnprof_BPMNProcess134
        self.bpmnprof_BPMNProcess136 = bpmnprof_BPMNProcess136
        self.bpmnprof_BPMNProcess138 = bpmnprof_BPMNProcess138 if bpmnprof_BPMNProcess138 is not None else set()
        self.bpmnprof_BPMNProcess140 = bpmnprof_BPMNProcess140
        self.bpmnprof_BPMNProcess144 = bpmnprof_BPMNProcess144
        self.bpmnprof_BPMNProcess142 = bpmnprof_BPMNProcess142
        self.bpmnprof_BPMNProcess146 = bpmnprof_BPMNProcess146 if bpmnprof_BPMNProcess146 is not None else set()
        self.bpmnprof_BPMNProcess = bpmnprof_BPMNProcess
        self.process = process if process is not None else set()
        self.bpmnprof_BPMNProcess293 = bpmnprof_BPMNProcess293
        self.BPMNProcess = BPMNProcess
        
    @property
    def isClosed(self) -> str:
        return self.__isClosed

    @isClosed.setter
    def isClosed(self, isClosed: str):
        self.__isClosed = isClosed

    @property
    def processType(self) -> str:
        return self.__processType

    @processType.setter
    def processType(self, processType: str):
        self.__processType = processType

    @property
    def isExecutable(self) -> str:
        return self.__isExecutable

    @isExecutable.setter
    def isExecutable(self, isExecutable: str):
        self.__isExecutable = isExecutable

    @property
    def bpmnprof_BPMNProcess(self):
        return self.__bpmnprof_BPMNProcess

    @bpmnprof_BPMNProcess.setter
    def bpmnprof_BPMNProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNProcess__bpmnprof_BPMNProcess", None)
        self.__bpmnprof_BPMNProcess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Auditing132"):
                opp_val = getattr(old_value, "bpmnprof_Auditing132", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Auditing132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Auditing132"):
                opp_val = getattr(value, "bpmnprof_Auditing132", None)
                setattr(value, "bpmnprof_Auditing132", self)

    @property
    def bpmnprof_BPMNProcess136(self):
        return self.__bpmnprof_BPMNProcess136

    @bpmnprof_BPMNProcess136.setter
    def bpmnprof_BPMNProcess136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNProcess__bpmnprof_BPMNProcess136", None)
        self.__bpmnprof_BPMNProcess136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Activity"):
                opp_val = getattr(old_value, "bpmnprof_Activity", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Activity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Activity"):
                opp_val = getattr(value, "bpmnprof_Activity", None)
                setattr(value, "bpmnprof_Activity", self)

    @property
    def bpmnprof_BPMNProcess142(self):
        return self.__bpmnprof_BPMNProcess142

    @bpmnprof_BPMNProcess142.setter
    def bpmnprof_BPMNProcess142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNProcess__bpmnprof_BPMNProcess142", None)
        self.__bpmnprof_BPMNProcess142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNProcess144"):
                opp_val = getattr(old_value, "bpmnprof_BPMNProcess144", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNProcess144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNProcess144"):
                opp_val = getattr(value, "bpmnprof_BPMNProcess144", None)
                setattr(value, "bpmnprof_BPMNProcess144", self)

    @property
    def bpmnprof_BPMNProcess140(self):
        return self.__bpmnprof_BPMNProcess140

    @bpmnprof_BPMNProcess140.setter
    def bpmnprof_BPMNProcess140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNProcess__bpmnprof_BPMNProcess140", None)
        self.__bpmnprof_BPMNProcess140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Monitoring141"):
                opp_val = getattr(old_value, "bpmnprof_Monitoring141", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Monitoring141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Monitoring141"):
                opp_val = getattr(value, "bpmnprof_Monitoring141", None)
                setattr(value, "bpmnprof_Monitoring141", self)

    @property
    def bpmnprof_BPMNProcess144(self):
        return self.__bpmnprof_BPMNProcess144

    @bpmnprof_BPMNProcess144.setter
    def bpmnprof_BPMNProcess144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNProcess__bpmnprof_BPMNProcess144", None)
        self.__bpmnprof_BPMNProcess144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNProcess142"):
                opp_val = getattr(old_value, "bpmnprof_BPMNProcess142", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNProcess142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNProcess142"):
                opp_val = getattr(value, "bpmnprof_BPMNProcess142", None)
                setattr(value, "bpmnprof_BPMNProcess142", self)

    @property
    def process(self):
        return self.__process

    @process.setter
    def process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNProcess__process", None)
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
    def bpmnprof_BPMNProcess134(self):
        return self.__bpmnprof_BPMNProcess134

    @bpmnprof_BPMNProcess134.setter
    def bpmnprof_BPMNProcess134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNProcess__bpmnprof_BPMNProcess134", None)
        self.__bpmnprof_BPMNProcess134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNCollaboration"):
                opp_val = getattr(old_value, "bpmnprof_BPMNCollaboration", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNCollaboration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNCollaboration"):
                opp_val = getattr(value, "bpmnprof_BPMNCollaboration", None)
                setattr(value, "bpmnprof_BPMNCollaboration", self)

    @property
    def bpmnprof_BPMNProcess138(self):
        return self.__bpmnprof_BPMNProcess138

    @bpmnprof_BPMNProcess138.setter
    def bpmnprof_BPMNProcess138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNProcess__bpmnprof_BPMNProcess138", None)
        self.__bpmnprof_BPMNProcess138 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_CorrelationSubscription"):
                    opp_val = getattr(item, "bpmnprof_CorrelationSubscription", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_CorrelationSubscription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_CorrelationSubscription"):
                    opp_val = getattr(item, "bpmnprof_CorrelationSubscription", None)
                    
                    setattr(item, "bpmnprof_CorrelationSubscription", self)
                    

    @property
    def bpmnprof_BPMNProcess146(self):
        return self.__bpmnprof_BPMNProcess146

    @bpmnprof_BPMNProcess146.setter
    def bpmnprof_BPMNProcess146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNProcess__bpmnprof_BPMNProcess146", None)
        self.__bpmnprof_BPMNProcess146 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_BPMNProperty"):
                    opp_val = getattr(item, "bpmnprof_BPMNProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_BPMNProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_BPMNProperty"):
                    opp_val = getattr(item, "bpmnprof_BPMNProperty", None)
                    
                    setattr(item, "bpmnprof_BPMNProperty", self)
                    

    @property
    def bpmnprof_BPMNProcess293(self):
        return self.__bpmnprof_BPMNProcess293

    @bpmnprof_BPMNProcess293.setter
    def bpmnprof_BPMNProcess293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNProcess__bpmnprof_BPMNProcess293", None)
        self.__bpmnprof_BPMNProcess293 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Participant292"):
                opp_val = getattr(old_value, "bpmnprof_Participant292", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Participant292", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Participant292"):
                opp_val = getattr(value, "bpmnprof_Participant292", None)
                setattr(value, "bpmnprof_Participant292", self)

    @property
    def BPMNProcess(self):
        return self.__BPMNProcess

    @BPMNProcess.setter
    def BPMNProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNProcess__BPMNProcess", None)
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

    def ProcesssupportedInterfaceRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ProcesssupportedInterfaceRefs method
        pass

    def Processproperties(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement Processproperties method
        pass

    def Processsupports(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement Processsupports method
        pass

    def ProcessflowElements(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ProcessflowElements method
        pass

    def ProcesslaneSets(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ProcesslaneSets method
        pass

class bpmnprof_PackageableElement:

    pass
class bpmnprof_MergeNode:

    pass
class bpmnprof_DecisionNode:

    pass
class bpmnprof_Import:

    def __init__(self, importType: str, location: str, namespace: str, bpmnprof_Import: "bpmnprof_Definitions" = None, bpmnprof_Import116: "bpmnprof_PackageImport" = None, bpmnprof_Import118: "bpmnprof_Definitions" = None, bpmnprof_Import194: "bpmnprof_ItemDefinition" = None):
        self.importType = importType
        self.location = location
        self.namespace = namespace
        self.bpmnprof_Import = bpmnprof_Import
        self.bpmnprof_Import116 = bpmnprof_Import116
        self.bpmnprof_Import118 = bpmnprof_Import118
        self.bpmnprof_Import194 = bpmnprof_Import194
        
    @property
    def importType(self) -> str:
        return self.__importType

    @importType.setter
    def importType(self, importType: str):
        self.__importType = importType

    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def bpmnprof_Import(self):
        return self.__bpmnprof_Import

    @bpmnprof_Import.setter
    def bpmnprof_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Import__bpmnprof_Import", None)
        self.__bpmnprof_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Definitions105"):
                opp_val = getattr(old_value, "bpmnprof_Definitions105", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Definitions105"):
                opp_val = getattr(value, "bpmnprof_Definitions105", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_Definitions105", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_Import118(self):
        return self.__bpmnprof_Import118

    @bpmnprof_Import118.setter
    def bpmnprof_Import118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Import__bpmnprof_Import118", None)
        self.__bpmnprof_Import118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Definitions119"):
                opp_val = getattr(old_value, "bpmnprof_Definitions119", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Definitions119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Definitions119"):
                opp_val = getattr(value, "bpmnprof_Definitions119", None)
                setattr(value, "bpmnprof_Definitions119", self)

    @property
    def bpmnprof_Import194(self):
        return self.__bpmnprof_Import194

    @bpmnprof_Import194.setter
    def bpmnprof_Import194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Import__bpmnprof_Import194", None)
        self.__bpmnprof_Import194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ItemDefinition193"):
                opp_val = getattr(old_value, "bpmnprof_ItemDefinition193", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ItemDefinition193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ItemDefinition193"):
                opp_val = getattr(value, "bpmnprof_ItemDefinition193", None)
                setattr(value, "bpmnprof_ItemDefinition193", self)

    @property
    def bpmnprof_Import116(self):
        return self.__bpmnprof_Import116

    @bpmnprof_Import116.setter
    def bpmnprof_Import116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Import__bpmnprof_Import116", None)
        self.__bpmnprof_Import116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_PackageImport"):
                opp_val = getattr(old_value, "bpmnprof_PackageImport", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_PackageImport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_PackageImport"):
                opp_val = getattr(value, "bpmnprof_PackageImport", None)
                setattr(value, "bpmnprof_PackageImport", self)

class bpmnprof_BPMNExtension:

    def __init__(self, mustUnderstand: str, bpmnprof_BPMNExtension: "bpmnprof_Definitions" = None, bpmnprof_BPMNExtension110: "bpmnprof_Stereotype" = None, bpmnprof_BPMNExtension113: "bpmnprof_ExtensionDefinition" = None):
        self.mustUnderstand = mustUnderstand
        self.bpmnprof_BPMNExtension = bpmnprof_BPMNExtension
        self.bpmnprof_BPMNExtension110 = bpmnprof_BPMNExtension110
        self.bpmnprof_BPMNExtension113 = bpmnprof_BPMNExtension113
        
    @property
    def mustUnderstand(self) -> str:
        return self.__mustUnderstand

    @mustUnderstand.setter
    def mustUnderstand(self, mustUnderstand: str):
        self.__mustUnderstand = mustUnderstand

    @property
    def bpmnprof_BPMNExtension113(self):
        return self.__bpmnprof_BPMNExtension113

    @bpmnprof_BPMNExtension113.setter
    def bpmnprof_BPMNExtension113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNExtension__bpmnprof_BPMNExtension113", None)
        self.__bpmnprof_BPMNExtension113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ExtensionDefinition114"):
                opp_val = getattr(old_value, "bpmnprof_ExtensionDefinition114", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ExtensionDefinition114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ExtensionDefinition114"):
                opp_val = getattr(value, "bpmnprof_ExtensionDefinition114", None)
                setattr(value, "bpmnprof_ExtensionDefinition114", self)

    @property
    def bpmnprof_BPMNExtension110(self):
        return self.__bpmnprof_BPMNExtension110

    @bpmnprof_BPMNExtension110.setter
    def bpmnprof_BPMNExtension110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNExtension__bpmnprof_BPMNExtension110", None)
        self.__bpmnprof_BPMNExtension110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Stereotype111"):
                opp_val = getattr(old_value, "bpmnprof_Stereotype111", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Stereotype111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Stereotype111"):
                opp_val = getattr(value, "bpmnprof_Stereotype111", None)
                setattr(value, "bpmnprof_Stereotype111", self)

    @property
    def bpmnprof_BPMNExtension(self):
        return self.__bpmnprof_BPMNExtension

    @bpmnprof_BPMNExtension.setter
    def bpmnprof_BPMNExtension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNExtension__bpmnprof_BPMNExtension", None)
        self.__bpmnprof_BPMNExtension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Definitions103"):
                opp_val = getattr(old_value, "bpmnprof_Definitions103", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Definitions103"):
                opp_val = getattr(value, "bpmnprof_Definitions103", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_Definitions103", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmnprof_Package:

    pass
class bpmnprof_InterruptibleActivityRegion:

    pass
class bpmnprof_StructuredActivityNode:

    pass
class bpmnprof_OpaqueExpression:

    pass
class bpmnprof_ControlFlow:

    pass
class bpmnprof_ActivityPartition:

    pass
class bpmnprof_Class:

    pass
class bpmnprof_Dependency:

    pass
class bpmnprof_EnumerationLiteral:

    pass
class bpmnprof_Property:

    pass
class bpmnprof_ExtensionAttributeDefinition:

    def __init__(self, type: str, isReference: str, bpmnprof_ExtensionAttributeDefinition38: "bpmnprof_ExtensionDefinition" = None, bpmnprof_ExtensionAttributeDefinition: "bpmnprof_ExtensionAttributeValue" = None, bpmnprof_ExtensionAttributeDefinition31: "bpmnprof_Property" = None):
        self.type = type
        self.isReference = isReference
        self.bpmnprof_ExtensionAttributeDefinition38 = bpmnprof_ExtensionAttributeDefinition38
        self.bpmnprof_ExtensionAttributeDefinition = bpmnprof_ExtensionAttributeDefinition
        self.bpmnprof_ExtensionAttributeDefinition31 = bpmnprof_ExtensionAttributeDefinition31
        
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
    def bpmnprof_ExtensionAttributeDefinition31(self):
        return self.__bpmnprof_ExtensionAttributeDefinition31

    @bpmnprof_ExtensionAttributeDefinition31.setter
    def bpmnprof_ExtensionAttributeDefinition31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ExtensionAttributeDefinition__bpmnprof_ExtensionAttributeDefinition31", None)
        self.__bpmnprof_ExtensionAttributeDefinition31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Property"):
                opp_val = getattr(old_value, "bpmnprof_Property", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Property", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Property"):
                opp_val = getattr(value, "bpmnprof_Property", None)
                setattr(value, "bpmnprof_Property", self)

    @property
    def bpmnprof_ExtensionAttributeDefinition(self):
        return self.__bpmnprof_ExtensionAttributeDefinition

    @bpmnprof_ExtensionAttributeDefinition.setter
    def bpmnprof_ExtensionAttributeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ExtensionAttributeDefinition__bpmnprof_ExtensionAttributeDefinition", None)
        self.__bpmnprof_ExtensionAttributeDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ExtensionAttributeValue29"):
                opp_val = getattr(old_value, "bpmnprof_ExtensionAttributeValue29", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ExtensionAttributeValue29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ExtensionAttributeValue29"):
                opp_val = getattr(value, "bpmnprof_ExtensionAttributeValue29", None)
                setattr(value, "bpmnprof_ExtensionAttributeValue29", self)

    @property
    def bpmnprof_ExtensionAttributeDefinition38(self):
        return self.__bpmnprof_ExtensionAttributeDefinition38

    @bpmnprof_ExtensionAttributeDefinition38.setter
    def bpmnprof_ExtensionAttributeDefinition38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ExtensionAttributeDefinition__bpmnprof_ExtensionAttributeDefinition38", None)
        self.__bpmnprof_ExtensionAttributeDefinition38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ExtensionDefinition37"):
                opp_val = getattr(old_value, "bpmnprof_ExtensionDefinition37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ExtensionDefinition37"):
                opp_val = getattr(value, "bpmnprof_ExtensionDefinition37", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_ExtensionDefinition37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmnprof_Slot:

    pass
class bpmnprof_ExtensionDefinition:

    pass
class bpmnprof_Element:

    pass
class bpmnprof_ExtensionAttributeValue:

    pass
class BPMNArtifact:

    pass
class bpmnprof_TextAnnotation(BPMNArtifact):

    def __init__(self, textFormat: str, text: str, bpmnprof_TextAnnotation: "bpmnprof_Comment" = None):
        self.textFormat = textFormat
        self.text = text
        self.bpmnprof_TextAnnotation = bpmnprof_TextAnnotation
        
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
    def bpmnprof_TextAnnotation(self):
        return self.__bpmnprof_TextAnnotation

    @bpmnprof_TextAnnotation.setter
    def bpmnprof_TextAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_TextAnnotation__bpmnprof_TextAnnotation", None)
        self.__bpmnprof_TextAnnotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Comment562"):
                opp_val = getattr(old_value, "bpmnprof_Comment562", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Comment562", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Comment562"):
                opp_val = getattr(value, "bpmnprof_Comment562", None)
                setattr(value, "bpmnprof_Comment562", self)

class bpmnprof_BPMNAssociation(BPMNArtifact):

    def __init__(self, associationDirection: str, BPMNAssociation: "bpmnprof_BaseElement" = None, BPMNAssociation22: "bpmnprof_BaseElement" = None, bpmnprof_BPMNAssociation: "bpmnprof_Dependency" = None, incoming: "bpmnprof_BaseElement" = None, outgoing: "bpmnprof_BaseElement" = None):
        self.associationDirection = associationDirection
        self.BPMNAssociation = BPMNAssociation
        self.BPMNAssociation22 = BPMNAssociation22
        self.bpmnprof_BPMNAssociation = bpmnprof_BPMNAssociation
        self.incoming = incoming
        self.outgoing = outgoing
        
    @property
    def associationDirection(self) -> str:
        return self.__associationDirection

    @associationDirection.setter
    def associationDirection(self, associationDirection: str):
        self.__associationDirection = associationDirection

    @property
    def bpmnprof_BPMNAssociation(self):
        return self.__bpmnprof_BPMNAssociation

    @bpmnprof_BPMNAssociation.setter
    def bpmnprof_BPMNAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNAssociation__bpmnprof_BPMNAssociation", None)
        self.__bpmnprof_BPMNAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Dependency"):
                opp_val = getattr(old_value, "bpmnprof_Dependency", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Dependency", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Dependency"):
                opp_val = getattr(value, "bpmnprof_Dependency", None)
                setattr(value, "bpmnprof_Dependency", self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNAssociation__outgoing", None)
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

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNAssociation__incoming", None)
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
        old_value = getattr(self, f"_bpmnprof_BPMNAssociation__BPMNAssociation22", None)
        self.__BPMNAssociation22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "targetRef"):
                opp_val = getattr(old_value, "targetRef", None)
                if opp_val == self:
                    setattr(old_value, "targetRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "targetRef"):
                opp_val = getattr(value, "targetRef", None)
                setattr(value, "targetRef", self)

    @property
    def BPMNAssociation(self):
        return self.__BPMNAssociation

    @BPMNAssociation.setter
    def BPMNAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNAssociation__BPMNAssociation", None)
        self.__BPMNAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourceRef"):
                opp_val = getattr(old_value, "sourceRef", None)
                if opp_val == self:
                    setattr(old_value, "sourceRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourceRef"):
                opp_val = getattr(value, "sourceRef", None)
                setattr(value, "sourceRef", self)

    def AssociationEnd(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AssociationEnd method
        pass

class bpmnprof_Group(BPMNArtifact):

    pass
class bpmnprof_Stereotype:

    pass
class bpmnprof_Comment:

    pass
class FlowElement:

    pass
class bpmnprof_DataObjectReference(ItemAwareElement, FlowElement):

    def __init__(self, bpmnprof_DataObjectReference: "bpmnprof_DataObject" = None, bpmnprof_DataObjectReference574: "bpmnprof_DataStoreNode" = None):
        self.bpmnprof_DataObjectReference = bpmnprof_DataObjectReference
        self.bpmnprof_DataObjectReference574 = bpmnprof_DataObjectReference574
        
    @property
    def bpmnprof_DataObjectReference574(self):
        return self.__bpmnprof_DataObjectReference574

    @bpmnprof_DataObjectReference574.setter
    def bpmnprof_DataObjectReference574(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataObjectReference__bpmnprof_DataObjectReference574", None)
        self.__bpmnprof_DataObjectReference574 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_DataStoreNode575"):
                opp_val = getattr(old_value, "bpmnprof_DataStoreNode575", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_DataStoreNode575", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_DataStoreNode575"):
                opp_val = getattr(value, "bpmnprof_DataStoreNode575", None)
                setattr(value, "bpmnprof_DataStoreNode575", self)

    @property
    def bpmnprof_DataObjectReference(self):
        return self.__bpmnprof_DataObjectReference

    @bpmnprof_DataObjectReference.setter
    def bpmnprof_DataObjectReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataObjectReference__bpmnprof_DataObjectReference", None)
        self.__bpmnprof_DataObjectReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_DataObject"):
                opp_val = getattr(old_value, "bpmnprof_DataObject", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_DataObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_DataObject"):
                opp_val = getattr(value, "bpmnprof_DataObject", None)
                setattr(value, "bpmnprof_DataObject", self)

    def DataObjectRefdataState(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement DataObjectRefdataState method
        pass

    def DataObjectRefsourcetarget(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement DataObjectRefsourcetarget method
        pass

class bpmnprof_DataStoreReference(ItemAwareElement, FlowElement):

    pass
class bpmnprof_DataObject(ItemAwareElement, FlowElement):

    def __init__(self, isCollection: str, bpmnprof_DataObject577: "bpmnprof_DataStoreNode" = None, bpmnprof_DataObject: "bpmnprof_DataObjectReference" = None):
        self.isCollection = isCollection
        self.bpmnprof_DataObject577 = bpmnprof_DataObject577
        self.bpmnprof_DataObject = bpmnprof_DataObject
        
    @property
    def isCollection(self) -> str:
        return self.__isCollection

    @isCollection.setter
    def isCollection(self, isCollection: str):
        self.__isCollection = isCollection

    @property
    def bpmnprof_DataObject(self):
        return self.__bpmnprof_DataObject

    @bpmnprof_DataObject.setter
    def bpmnprof_DataObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataObject__bpmnprof_DataObject", None)
        self.__bpmnprof_DataObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_DataObjectReference"):
                opp_val = getattr(old_value, "bpmnprof_DataObjectReference", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_DataObjectReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_DataObjectReference"):
                opp_val = getattr(value, "bpmnprof_DataObjectReference", None)
                setattr(value, "bpmnprof_DataObjectReference", self)

    @property
    def bpmnprof_DataObject577(self):
        return self.__bpmnprof_DataObject577

    @bpmnprof_DataObject577.setter
    def bpmnprof_DataObject577(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataObject__bpmnprof_DataObject577", None)
        self.__bpmnprof_DataObject577 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_DataStoreNode578"):
                opp_val = getattr(old_value, "bpmnprof_DataStoreNode578", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_DataStoreNode578", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_DataStoreNode578"):
                opp_val = getattr(value, "bpmnprof_DataStoreNode578", None)
                setattr(value, "bpmnprof_DataStoreNode578", self)

    def DataObjectdataState(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement DataObjectdataState method
        pass

class bpmnprof_FlowNode(FlowElement):

    pass
class bpmnprof_ActivityGroup:

    pass
class bpmnprof_ControlNode:

    pass
class FlowNode:

    pass
class bpmnprof_BPMNActivity(FlowNode):

    def __init__(self, isForCompensation: str, startQuantity: str, completionQuantity: str, bpmnprof_BPMNActivity: "bpmnprof_CompensateEventDefinition" = None, bpmnprof_BPMNActivity454: set["bpmnprof_DataInputAssociation"] = None, bpmnprof_BPMNActivity456: set["bpmnprof_DataOutputAssociation"] = None, bpmnprof_BPMNActivity458: "bpmnprof_LoopCharacteristics" = None, bpmnprof_BPMNActivity440: "bpmnprof_Action" = None, bpmnprof_BPMNActivity443: "bpmnprof_Class" = None, bpmnprof_BPMNActivity446: set["bpmnprof_BPMNProperty"] = None, bpmnprof_BPMNActivity449: "bpmnprof_SequenceFlow" = None, bpmnprof_BPMNActivity452: set["bpmnprof_BoundaryEvent"] = None, bpmnprof_BPMNActivity460: set["bpmnprof_ResourceRole"] = None, bpmnprof_BPMNActivity464: "bpmnprof_BoundaryEvent" = None):
        self.isForCompensation = isForCompensation
        self.startQuantity = startQuantity
        self.completionQuantity = completionQuantity
        self.bpmnprof_BPMNActivity = bpmnprof_BPMNActivity
        self.bpmnprof_BPMNActivity454 = bpmnprof_BPMNActivity454 if bpmnprof_BPMNActivity454 is not None else set()
        self.bpmnprof_BPMNActivity456 = bpmnprof_BPMNActivity456 if bpmnprof_BPMNActivity456 is not None else set()
        self.bpmnprof_BPMNActivity458 = bpmnprof_BPMNActivity458
        self.bpmnprof_BPMNActivity440 = bpmnprof_BPMNActivity440
        self.bpmnprof_BPMNActivity443 = bpmnprof_BPMNActivity443
        self.bpmnprof_BPMNActivity446 = bpmnprof_BPMNActivity446 if bpmnprof_BPMNActivity446 is not None else set()
        self.bpmnprof_BPMNActivity449 = bpmnprof_BPMNActivity449
        self.bpmnprof_BPMNActivity452 = bpmnprof_BPMNActivity452 if bpmnprof_BPMNActivity452 is not None else set()
        self.bpmnprof_BPMNActivity460 = bpmnprof_BPMNActivity460 if bpmnprof_BPMNActivity460 is not None else set()
        self.bpmnprof_BPMNActivity464 = bpmnprof_BPMNActivity464
        
    @property
    def completionQuantity(self) -> str:
        return self.__completionQuantity

    @completionQuantity.setter
    def completionQuantity(self, completionQuantity: str):
        self.__completionQuantity = completionQuantity

    @property
    def startQuantity(self) -> str:
        return self.__startQuantity

    @startQuantity.setter
    def startQuantity(self, startQuantity: str):
        self.__startQuantity = startQuantity

    @property
    def isForCompensation(self) -> str:
        return self.__isForCompensation

    @isForCompensation.setter
    def isForCompensation(self, isForCompensation: str):
        self.__isForCompensation = isForCompensation

    @property
    def bpmnprof_BPMNActivity449(self):
        return self.__bpmnprof_BPMNActivity449

    @bpmnprof_BPMNActivity449.setter
    def bpmnprof_BPMNActivity449(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNActivity__bpmnprof_BPMNActivity449", None)
        self.__bpmnprof_BPMNActivity449 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_SequenceFlow450"):
                opp_val = getattr(old_value, "bpmnprof_SequenceFlow450", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_SequenceFlow450", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_SequenceFlow450"):
                opp_val = getattr(value, "bpmnprof_SequenceFlow450", None)
                setattr(value, "bpmnprof_SequenceFlow450", self)

    @property
    def bpmnprof_BPMNActivity464(self):
        return self.__bpmnprof_BPMNActivity464

    @bpmnprof_BPMNActivity464.setter
    def bpmnprof_BPMNActivity464(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNActivity__bpmnprof_BPMNActivity464", None)
        self.__bpmnprof_BPMNActivity464 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BoundaryEvent463"):
                opp_val = getattr(old_value, "bpmnprof_BoundaryEvent463", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BoundaryEvent463", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BoundaryEvent463"):
                opp_val = getattr(value, "bpmnprof_BoundaryEvent463", None)
                setattr(value, "bpmnprof_BoundaryEvent463", self)

    @property
    def bpmnprof_BPMNActivity454(self):
        return self.__bpmnprof_BPMNActivity454

    @bpmnprof_BPMNActivity454.setter
    def bpmnprof_BPMNActivity454(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNActivity__bpmnprof_BPMNActivity454", None)
        self.__bpmnprof_BPMNActivity454 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_DataInputAssociation"):
                    opp_val = getattr(item, "bpmnprof_DataInputAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_DataInputAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_DataInputAssociation"):
                    opp_val = getattr(item, "bpmnprof_DataInputAssociation", None)
                    
                    setattr(item, "bpmnprof_DataInputAssociation", self)
                    

    @property
    def bpmnprof_BPMNActivity456(self):
        return self.__bpmnprof_BPMNActivity456

    @bpmnprof_BPMNActivity456.setter
    def bpmnprof_BPMNActivity456(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNActivity__bpmnprof_BPMNActivity456", None)
        self.__bpmnprof_BPMNActivity456 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_DataOutputAssociation"):
                    opp_val = getattr(item, "bpmnprof_DataOutputAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_DataOutputAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_DataOutputAssociation"):
                    opp_val = getattr(item, "bpmnprof_DataOutputAssociation", None)
                    
                    setattr(item, "bpmnprof_DataOutputAssociation", self)
                    

    @property
    def bpmnprof_BPMNActivity446(self):
        return self.__bpmnprof_BPMNActivity446

    @bpmnprof_BPMNActivity446.setter
    def bpmnprof_BPMNActivity446(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNActivity__bpmnprof_BPMNActivity446", None)
        self.__bpmnprof_BPMNActivity446 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_BPMNProperty447"):
                    opp_val = getattr(item, "bpmnprof_BPMNProperty447", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_BPMNProperty447", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_BPMNProperty447"):
                    opp_val = getattr(item, "bpmnprof_BPMNProperty447", None)
                    
                    setattr(item, "bpmnprof_BPMNProperty447", self)
                    

    @property
    def bpmnprof_BPMNActivity458(self):
        return self.__bpmnprof_BPMNActivity458

    @bpmnprof_BPMNActivity458.setter
    def bpmnprof_BPMNActivity458(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNActivity__bpmnprof_BPMNActivity458", None)
        self.__bpmnprof_BPMNActivity458 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_LoopCharacteristics"):
                opp_val = getattr(old_value, "bpmnprof_LoopCharacteristics", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_LoopCharacteristics", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_LoopCharacteristics"):
                opp_val = getattr(value, "bpmnprof_LoopCharacteristics", None)
                setattr(value, "bpmnprof_LoopCharacteristics", self)

    @property
    def bpmnprof_BPMNActivity440(self):
        return self.__bpmnprof_BPMNActivity440

    @bpmnprof_BPMNActivity440.setter
    def bpmnprof_BPMNActivity440(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNActivity__bpmnprof_BPMNActivity440", None)
        self.__bpmnprof_BPMNActivity440 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Action441"):
                opp_val = getattr(old_value, "bpmnprof_Action441", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Action441", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Action441"):
                opp_val = getattr(value, "bpmnprof_Action441", None)
                setattr(value, "bpmnprof_Action441", self)

    @property
    def bpmnprof_BPMNActivity460(self):
        return self.__bpmnprof_BPMNActivity460

    @bpmnprof_BPMNActivity460.setter
    def bpmnprof_BPMNActivity460(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNActivity__bpmnprof_BPMNActivity460", None)
        self.__bpmnprof_BPMNActivity460 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_ResourceRole461"):
                    opp_val = getattr(item, "bpmnprof_ResourceRole461", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_ResourceRole461", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_ResourceRole461"):
                    opp_val = getattr(item, "bpmnprof_ResourceRole461", None)
                    
                    setattr(item, "bpmnprof_ResourceRole461", self)
                    

    @property
    def bpmnprof_BPMNActivity(self):
        return self.__bpmnprof_BPMNActivity

    @bpmnprof_BPMNActivity.setter
    def bpmnprof_BPMNActivity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNActivity__bpmnprof_BPMNActivity", None)
        self.__bpmnprof_BPMNActivity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_CompensateEventDefinition"):
                opp_val = getattr(old_value, "bpmnprof_CompensateEventDefinition", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_CompensateEventDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_CompensateEventDefinition"):
                opp_val = getattr(value, "bpmnprof_CompensateEventDefinition", None)
                setattr(value, "bpmnprof_CompensateEventDefinition", self)

    @property
    def bpmnprof_BPMNActivity443(self):
        return self.__bpmnprof_BPMNActivity443

    @bpmnprof_BPMNActivity443.setter
    def bpmnprof_BPMNActivity443(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNActivity__bpmnprof_BPMNActivity443", None)
        self.__bpmnprof_BPMNActivity443 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Class444"):
                opp_val = getattr(old_value, "bpmnprof_Class444", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Class444", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Class444"):
                opp_val = getattr(value, "bpmnprof_Class444", None)
                setattr(value, "bpmnprof_Class444", self)

    @property
    def bpmnprof_BPMNActivity452(self):
        return self.__bpmnprof_BPMNActivity452

    @bpmnprof_BPMNActivity452.setter
    def bpmnprof_BPMNActivity452(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNActivity__bpmnprof_BPMNActivity452", None)
        self.__bpmnprof_BPMNActivity452 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_BoundaryEvent"):
                    opp_val = getattr(item, "bpmnprof_BoundaryEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_BoundaryEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_BoundaryEvent"):
                    opp_val = getattr(item, "bpmnprof_BoundaryEvent", None)
                    
                    setattr(item, "bpmnprof_BoundaryEvent", self)
                    

    def BPMNActivityproperties(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement BPMNActivityproperties method
        pass

    def BPMNActivitycontainer(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement BPMNActivitycontainer method
        pass

    def BPMNActivityloopCharacteristics(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BPMNActivityloopCharacteristics method
        pass

    def BPMNActivityboundaryEventsRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement BPMNActivityboundaryEventsRefs method
        pass

    def BPMNActivityresources(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BPMNActivityresources method
        pass

    def BPMNActivitydefault(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BPMNActivitydefault method
        pass

class bpmnprof_BPMNEvent(FlowNode):

    pass
class bpmnprof_Gateway(FlowNode):

    pass
class bpmnprof_ForkNode:

    pass
class bpmnprof_JoinNode:

    pass
class Gateway:

    pass
class bpmnprof_EventBasedGateway(Gateway):

    def __init__(self, instantiate: str, eventGatewayType: str, bpmnprof_EventBasedGateway: "bpmnprof_ForkNode" = None, bpmnprof_EventBasedGateway85: "bpmnprof_StructuredActivityNode" = None, bpmnprof_EventBasedGateway87: "bpmnprof_InterruptibleActivityRegion" = None):
        self.instantiate = instantiate
        self.eventGatewayType = eventGatewayType
        self.bpmnprof_EventBasedGateway = bpmnprof_EventBasedGateway
        self.bpmnprof_EventBasedGateway85 = bpmnprof_EventBasedGateway85
        self.bpmnprof_EventBasedGateway87 = bpmnprof_EventBasedGateway87
        
    @property
    def eventGatewayType(self) -> str:
        return self.__eventGatewayType

    @eventGatewayType.setter
    def eventGatewayType(self, eventGatewayType: str):
        self.__eventGatewayType = eventGatewayType

    @property
    def instantiate(self) -> str:
        return self.__instantiate

    @instantiate.setter
    def instantiate(self, instantiate: str):
        self.__instantiate = instantiate

    @property
    def bpmnprof_EventBasedGateway(self):
        return self.__bpmnprof_EventBasedGateway

    @bpmnprof_EventBasedGateway.setter
    def bpmnprof_EventBasedGateway(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_EventBasedGateway__bpmnprof_EventBasedGateway", None)
        self.__bpmnprof_EventBasedGateway = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ForkNode83"):
                opp_val = getattr(old_value, "bpmnprof_ForkNode83", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ForkNode83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ForkNode83"):
                opp_val = getattr(value, "bpmnprof_ForkNode83", None)
                setattr(value, "bpmnprof_ForkNode83", self)

    @property
    def bpmnprof_EventBasedGateway85(self):
        return self.__bpmnprof_EventBasedGateway85

    @bpmnprof_EventBasedGateway85.setter
    def bpmnprof_EventBasedGateway85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_EventBasedGateway__bpmnprof_EventBasedGateway85", None)
        self.__bpmnprof_EventBasedGateway85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_StructuredActivityNode"):
                opp_val = getattr(old_value, "bpmnprof_StructuredActivityNode", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_StructuredActivityNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_StructuredActivityNode"):
                opp_val = getattr(value, "bpmnprof_StructuredActivityNode", None)
                setattr(value, "bpmnprof_StructuredActivityNode", self)

    @property
    def bpmnprof_EventBasedGateway87(self):
        return self.__bpmnprof_EventBasedGateway87

    @bpmnprof_EventBasedGateway87.setter
    def bpmnprof_EventBasedGateway87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_EventBasedGateway__bpmnprof_EventBasedGateway87", None)
        self.__bpmnprof_EventBasedGateway87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_InterruptibleActivityRegion"):
                opp_val = getattr(old_value, "bpmnprof_InterruptibleActivityRegion", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_InterruptibleActivityRegion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_InterruptibleActivityRegion"):
                opp_val = getattr(value, "bpmnprof_InterruptibleActivityRegion", None)
                setattr(value, "bpmnprof_InterruptibleActivityRegion", self)

class bpmnprof_ExclusiveGateway(Gateway):

    def __init__(self, bpmnprof_ExclusiveGateway: "bpmnprof_DecisionNode" = None, bpmnprof_ExclusiveGateway95: "bpmnprof_MergeNode" = None, bpmnprof_ExclusiveGateway97: "bpmnprof_SequenceFlow" = None):
        self.bpmnprof_ExclusiveGateway = bpmnprof_ExclusiveGateway
        self.bpmnprof_ExclusiveGateway95 = bpmnprof_ExclusiveGateway95
        self.bpmnprof_ExclusiveGateway97 = bpmnprof_ExclusiveGateway97
        
    @property
    def bpmnprof_ExclusiveGateway97(self):
        return self.__bpmnprof_ExclusiveGateway97

    @bpmnprof_ExclusiveGateway97.setter
    def bpmnprof_ExclusiveGateway97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ExclusiveGateway__bpmnprof_ExclusiveGateway97", None)
        self.__bpmnprof_ExclusiveGateway97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_SequenceFlow98"):
                opp_val = getattr(old_value, "bpmnprof_SequenceFlow98", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_SequenceFlow98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_SequenceFlow98"):
                opp_val = getattr(value, "bpmnprof_SequenceFlow98", None)
                setattr(value, "bpmnprof_SequenceFlow98", self)

    @property
    def bpmnprof_ExclusiveGateway(self):
        return self.__bpmnprof_ExclusiveGateway

    @bpmnprof_ExclusiveGateway.setter
    def bpmnprof_ExclusiveGateway(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ExclusiveGateway__bpmnprof_ExclusiveGateway", None)
        self.__bpmnprof_ExclusiveGateway = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_DecisionNode"):
                opp_val = getattr(old_value, "bpmnprof_DecisionNode", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_DecisionNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_DecisionNode"):
                opp_val = getattr(value, "bpmnprof_DecisionNode", None)
                setattr(value, "bpmnprof_DecisionNode", self)

    @property
    def bpmnprof_ExclusiveGateway95(self):
        return self.__bpmnprof_ExclusiveGateway95

    @bpmnprof_ExclusiveGateway95.setter
    def bpmnprof_ExclusiveGateway95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ExclusiveGateway__bpmnprof_ExclusiveGateway95", None)
        self.__bpmnprof_ExclusiveGateway95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_MergeNode"):
                opp_val = getattr(old_value, "bpmnprof_MergeNode", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_MergeNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_MergeNode"):
                opp_val = getattr(value, "bpmnprof_MergeNode", None)
                setattr(value, "bpmnprof_MergeNode", self)

    def exclusiveGatewaydefault(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement exclusiveGatewaydefault method
        pass

class bpmnprof_NonExclusiveGateway(Gateway):

    pass
class bpmnprof_SequenceFlow(FlowElement):

    def __init__(self, isImmediate: str, bpmnprof_SequenceFlow: "bpmnprof_InclusiveGateway" = None, bpmnprof_SequenceFlow77: "bpmnprof_ControlFlow" = None, bpmnprof_SequenceFlow89: "bpmnprof_ComplexGateway" = None, bpmnprof_SequenceFlow79: "bpmnprof_BPMNExpression" = None, bpmnprof_SequenceFlow98: "bpmnprof_ExclusiveGateway" = None, bpmnprof_SequenceFlow450: "bpmnprof_BPMNActivity" = None):
        self.isImmediate = isImmediate
        self.bpmnprof_SequenceFlow = bpmnprof_SequenceFlow
        self.bpmnprof_SequenceFlow77 = bpmnprof_SequenceFlow77
        self.bpmnprof_SequenceFlow89 = bpmnprof_SequenceFlow89
        self.bpmnprof_SequenceFlow79 = bpmnprof_SequenceFlow79
        self.bpmnprof_SequenceFlow98 = bpmnprof_SequenceFlow98
        self.bpmnprof_SequenceFlow450 = bpmnprof_SequenceFlow450
        
    @property
    def isImmediate(self) -> str:
        return self.__isImmediate

    @isImmediate.setter
    def isImmediate(self, isImmediate: str):
        self.__isImmediate = isImmediate

    @property
    def bpmnprof_SequenceFlow(self):
        return self.__bpmnprof_SequenceFlow

    @bpmnprof_SequenceFlow.setter
    def bpmnprof_SequenceFlow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_SequenceFlow__bpmnprof_SequenceFlow", None)
        self.__bpmnprof_SequenceFlow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_InclusiveGateway"):
                opp_val = getattr(old_value, "bpmnprof_InclusiveGateway", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_InclusiveGateway", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_InclusiveGateway"):
                opp_val = getattr(value, "bpmnprof_InclusiveGateway", None)
                setattr(value, "bpmnprof_InclusiveGateway", self)

    @property
    def bpmnprof_SequenceFlow450(self):
        return self.__bpmnprof_SequenceFlow450

    @bpmnprof_SequenceFlow450.setter
    def bpmnprof_SequenceFlow450(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_SequenceFlow__bpmnprof_SequenceFlow450", None)
        self.__bpmnprof_SequenceFlow450 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNActivity449"):
                opp_val = getattr(old_value, "bpmnprof_BPMNActivity449", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNActivity449", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNActivity449"):
                opp_val = getattr(value, "bpmnprof_BPMNActivity449", None)
                setattr(value, "bpmnprof_BPMNActivity449", self)

    @property
    def bpmnprof_SequenceFlow98(self):
        return self.__bpmnprof_SequenceFlow98

    @bpmnprof_SequenceFlow98.setter
    def bpmnprof_SequenceFlow98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_SequenceFlow__bpmnprof_SequenceFlow98", None)
        self.__bpmnprof_SequenceFlow98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ExclusiveGateway97"):
                opp_val = getattr(old_value, "bpmnprof_ExclusiveGateway97", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ExclusiveGateway97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ExclusiveGateway97"):
                opp_val = getattr(value, "bpmnprof_ExclusiveGateway97", None)
                setattr(value, "bpmnprof_ExclusiveGateway97", self)

    @property
    def bpmnprof_SequenceFlow79(self):
        return self.__bpmnprof_SequenceFlow79

    @bpmnprof_SequenceFlow79.setter
    def bpmnprof_SequenceFlow79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_SequenceFlow__bpmnprof_SequenceFlow79", None)
        self.__bpmnprof_SequenceFlow79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNExpression"):
                opp_val = getattr(old_value, "bpmnprof_BPMNExpression", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNExpression"):
                opp_val = getattr(value, "bpmnprof_BPMNExpression", None)
                setattr(value, "bpmnprof_BPMNExpression", self)

    @property
    def bpmnprof_SequenceFlow89(self):
        return self.__bpmnprof_SequenceFlow89

    @bpmnprof_SequenceFlow89.setter
    def bpmnprof_SequenceFlow89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_SequenceFlow__bpmnprof_SequenceFlow89", None)
        self.__bpmnprof_SequenceFlow89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ComplexGateway"):
                opp_val = getattr(old_value, "bpmnprof_ComplexGateway", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ComplexGateway", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ComplexGateway"):
                opp_val = getattr(value, "bpmnprof_ComplexGateway", None)
                setattr(value, "bpmnprof_ComplexGateway", self)

    @property
    def bpmnprof_SequenceFlow77(self):
        return self.__bpmnprof_SequenceFlow77

    @bpmnprof_SequenceFlow77.setter
    def bpmnprof_SequenceFlow77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_SequenceFlow__bpmnprof_SequenceFlow77", None)
        self.__bpmnprof_SequenceFlow77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ControlFlow"):
                opp_val = getattr(old_value, "bpmnprof_ControlFlow", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ControlFlow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ControlFlow"):
                opp_val = getattr(value, "bpmnprof_ControlFlow", None)
                setattr(value, "bpmnprof_ControlFlow", self)

    def SequenceFlowsourceRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SequenceFlowsourceRef method
        pass

    def SequenceFlowconditionExpression(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SequenceFlowconditionExpression method
        pass

    def SequenceFlowtargetRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SequenceFlowtargetRef method
        pass

class bpmnprof_BaseElement(ABC):

    def __init__(self, id: str, bpmnprof_BaseElement: set["bpmnprof_ExtensionAttributeValue"] = None, bpmnprof_BaseElement15: "bpmnprof_Element" = None, bpmnprof_BaseElement17: set["bpmnprof_Documentation"] = None, bpmnprof_BaseElement19: set["bpmnprof_ExtensionDefinition"] = None, sourceRef: "bpmnprof_BPMNAssociation" = None, targetRef: "bpmnprof_BPMNAssociation" = None, BaseElement: "bpmnprof_BPMNAssociation" = None, BaseElement42: "bpmnprof_BPMNAssociation" = None, bpmnprof_BaseElement70: "bpmnprof_Lane" = None):
        self.id = id
        self.bpmnprof_BaseElement = bpmnprof_BaseElement if bpmnprof_BaseElement is not None else set()
        self.bpmnprof_BaseElement15 = bpmnprof_BaseElement15
        self.bpmnprof_BaseElement17 = bpmnprof_BaseElement17 if bpmnprof_BaseElement17 is not None else set()
        self.bpmnprof_BaseElement19 = bpmnprof_BaseElement19 if bpmnprof_BaseElement19 is not None else set()
        self.sourceRef = sourceRef
        self.targetRef = targetRef
        self.BaseElement = BaseElement
        self.BaseElement42 = BaseElement42
        self.bpmnprof_BaseElement70 = bpmnprof_BaseElement70
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def bpmnprof_BaseElement15(self):
        return self.__bpmnprof_BaseElement15

    @bpmnprof_BaseElement15.setter
    def bpmnprof_BaseElement15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BaseElement__bpmnprof_BaseElement15", None)
        self.__bpmnprof_BaseElement15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Element"):
                opp_val = getattr(old_value, "bpmnprof_Element", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Element", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Element"):
                opp_val = getattr(value, "bpmnprof_Element", None)
                setattr(value, "bpmnprof_Element", self)

    @property
    def sourceRef(self):
        return self.__sourceRef

    @sourceRef.setter
    def sourceRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BaseElement__sourceRef", None)
        self.__sourceRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNAssociation"):
                opp_val = getattr(old_value, "BPMNAssociation", None)
                if opp_val == self:
                    setattr(old_value, "BPMNAssociation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNAssociation"):
                opp_val = getattr(value, "BPMNAssociation", None)
                setattr(value, "BPMNAssociation", self)

    @property
    def bpmnprof_BaseElement70(self):
        return self.__bpmnprof_BaseElement70

    @bpmnprof_BaseElement70.setter
    def bpmnprof_BaseElement70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BaseElement__bpmnprof_BaseElement70", None)
        self.__bpmnprof_BaseElement70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Lane69"):
                opp_val = getattr(old_value, "bpmnprof_Lane69", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Lane69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Lane69"):
                opp_val = getattr(value, "bpmnprof_Lane69", None)
                setattr(value, "bpmnprof_Lane69", self)

    @property
    def BaseElement42(self):
        return self.__BaseElement42

    @BaseElement42.setter
    def BaseElement42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BaseElement__BaseElement42", None)
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
    def bpmnprof_BaseElement(self):
        return self.__bpmnprof_BaseElement

    @bpmnprof_BaseElement.setter
    def bpmnprof_BaseElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BaseElement__bpmnprof_BaseElement", None)
        self.__bpmnprof_BaseElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_ExtensionAttributeValue"):
                    opp_val = getattr(item, "bpmnprof_ExtensionAttributeValue", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_ExtensionAttributeValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_ExtensionAttributeValue"):
                    opp_val = getattr(item, "bpmnprof_ExtensionAttributeValue", None)
                    
                    setattr(item, "bpmnprof_ExtensionAttributeValue", self)
                    

    @property
    def bpmnprof_BaseElement19(self):
        return self.__bpmnprof_BaseElement19

    @bpmnprof_BaseElement19.setter
    def bpmnprof_BaseElement19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BaseElement__bpmnprof_BaseElement19", None)
        self.__bpmnprof_BaseElement19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_ExtensionDefinition"):
                    opp_val = getattr(item, "bpmnprof_ExtensionDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_ExtensionDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_ExtensionDefinition"):
                    opp_val = getattr(item, "bpmnprof_ExtensionDefinition", None)
                    
                    setattr(item, "bpmnprof_ExtensionDefinition", self)
                    

    @property
    def BaseElement(self):
        return self.__BaseElement

    @BaseElement.setter
    def BaseElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BaseElement__BaseElement", None)
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

    @property
    def bpmnprof_BaseElement17(self):
        return self.__bpmnprof_BaseElement17

    @bpmnprof_BaseElement17.setter
    def bpmnprof_BaseElement17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BaseElement__bpmnprof_BaseElement17", None)
        self.__bpmnprof_BaseElement17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_Documentation"):
                    opp_val = getattr(item, "bpmnprof_Documentation", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_Documentation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_Documentation"):
                    opp_val = getattr(item, "bpmnprof_Documentation", None)
                    
                    setattr(item, "bpmnprof_Documentation", self)
                    

    @property
    def targetRef(self):
        return self.__targetRef

    @targetRef.setter
    def targetRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BaseElement__targetRef", None)
        self.__targetRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNAssociation22"):
                opp_val = getattr(old_value, "BPMNAssociation22", None)
                if opp_val == self:
                    setattr(old_value, "BPMNAssociation22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNAssociation22"):
                opp_val = getattr(value, "BPMNAssociation22", None)
                setattr(value, "BPMNAssociation22", self)

class BaseElement:

    pass
class bpmnprof_InputOutputSpecification(BaseElement):

    pass
class bpmnprof_RootElement(BaseElement):

    pass
class bpmnprof_Assignment(BaseElement):

    pass
class bpmnprof_ResourceParameterBinding(BaseElement):

    def __init__(self, bpmnprof_ResourceParameterBinding: "bpmnprof_ResourceRole" = None, bpmnprof_ResourceParameterBinding423: "bpmnprof_Slot" = None, bpmnprof_ResourceParameterBinding426: "bpmnprof_ResourceParameter" = None, bpmnprof_ResourceParameterBinding429: "bpmnprof_BPMNExpression" = None):
        self.bpmnprof_ResourceParameterBinding = bpmnprof_ResourceParameterBinding
        self.bpmnprof_ResourceParameterBinding423 = bpmnprof_ResourceParameterBinding423
        self.bpmnprof_ResourceParameterBinding426 = bpmnprof_ResourceParameterBinding426
        self.bpmnprof_ResourceParameterBinding429 = bpmnprof_ResourceParameterBinding429
        
    @property
    def bpmnprof_ResourceParameterBinding426(self):
        return self.__bpmnprof_ResourceParameterBinding426

    @bpmnprof_ResourceParameterBinding426.setter
    def bpmnprof_ResourceParameterBinding426(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ResourceParameterBinding__bpmnprof_ResourceParameterBinding426", None)
        self.__bpmnprof_ResourceParameterBinding426 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ResourceParameter427"):
                opp_val = getattr(old_value, "bpmnprof_ResourceParameter427", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ResourceParameter427", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ResourceParameter427"):
                opp_val = getattr(value, "bpmnprof_ResourceParameter427", None)
                setattr(value, "bpmnprof_ResourceParameter427", self)

    @property
    def bpmnprof_ResourceParameterBinding423(self):
        return self.__bpmnprof_ResourceParameterBinding423

    @bpmnprof_ResourceParameterBinding423.setter
    def bpmnprof_ResourceParameterBinding423(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ResourceParameterBinding__bpmnprof_ResourceParameterBinding423", None)
        self.__bpmnprof_ResourceParameterBinding423 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Slot424"):
                opp_val = getattr(old_value, "bpmnprof_Slot424", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Slot424", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Slot424"):
                opp_val = getattr(value, "bpmnprof_Slot424", None)
                setattr(value, "bpmnprof_Slot424", self)

    @property
    def bpmnprof_ResourceParameterBinding(self):
        return self.__bpmnprof_ResourceParameterBinding

    @bpmnprof_ResourceParameterBinding.setter
    def bpmnprof_ResourceParameterBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ResourceParameterBinding__bpmnprof_ResourceParameterBinding", None)
        self.__bpmnprof_ResourceParameterBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ResourceRole409"):
                opp_val = getattr(old_value, "bpmnprof_ResourceRole409", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ResourceRole409"):
                opp_val = getattr(value, "bpmnprof_ResourceRole409", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_ResourceRole409", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_ResourceParameterBinding429(self):
        return self.__bpmnprof_ResourceParameterBinding429

    @bpmnprof_ResourceParameterBinding429.setter
    def bpmnprof_ResourceParameterBinding429(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ResourceParameterBinding__bpmnprof_ResourceParameterBinding429", None)
        self.__bpmnprof_ResourceParameterBinding429 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNExpression430"):
                opp_val = getattr(old_value, "bpmnprof_BPMNExpression430", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNExpression430", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNExpression430"):
                opp_val = getattr(value, "bpmnprof_BPMNExpression430", None)
                setattr(value, "bpmnprof_BPMNExpression430", self)

    def ResourceParameterBindingexpression(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceParameterBindingexpression method
        pass

    def ResourceParameterBindingparameterRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceParameterBindingparameterRef method
        pass

class bpmnprof_CorrelationKey(BaseElement):

    pass
class bpmnprof_ConversationLink(BaseElement):

    pass
class bpmnprof_MessageFlow(BaseElement):

    def __init__(self, bpmnprof_MessageFlow: "bpmnprof_BPMNCollaboration" = None, bpmnprof_MessageFlow334: "bpmnprof_InformationFlow" = None, bpmnprof_MessageFlow336: "bpmnprof_InteractionNode" = None, bpmnprof_MessageFlow339: "bpmnprof_InteractionNode" = None, bpmnprof_MessageFlow342: "bpmnprof_BPMNMessage" = None, bpmnprof_MessageFlow329: "bpmnprof_MessageFlowAssociation" = None, bpmnprof_MessageFlow332: "bpmnprof_MessageFlowAssociation" = None, bpmnprof_MessageFlow349: "bpmnprof_ConversationNode" = None):
        self.bpmnprof_MessageFlow = bpmnprof_MessageFlow
        self.bpmnprof_MessageFlow334 = bpmnprof_MessageFlow334
        self.bpmnprof_MessageFlow336 = bpmnprof_MessageFlow336
        self.bpmnprof_MessageFlow339 = bpmnprof_MessageFlow339
        self.bpmnprof_MessageFlow342 = bpmnprof_MessageFlow342
        self.bpmnprof_MessageFlow329 = bpmnprof_MessageFlow329
        self.bpmnprof_MessageFlow332 = bpmnprof_MessageFlow332
        self.bpmnprof_MessageFlow349 = bpmnprof_MessageFlow349
        
    @property
    def bpmnprof_MessageFlow(self):
        return self.__bpmnprof_MessageFlow

    @bpmnprof_MessageFlow.setter
    def bpmnprof_MessageFlow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_MessageFlow__bpmnprof_MessageFlow", None)
        self.__bpmnprof_MessageFlow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNCollaboration270"):
                opp_val = getattr(old_value, "bpmnprof_BPMNCollaboration270", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNCollaboration270"):
                opp_val = getattr(value, "bpmnprof_BPMNCollaboration270", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_BPMNCollaboration270", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_MessageFlow336(self):
        return self.__bpmnprof_MessageFlow336

    @bpmnprof_MessageFlow336.setter
    def bpmnprof_MessageFlow336(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_MessageFlow__bpmnprof_MessageFlow336", None)
        self.__bpmnprof_MessageFlow336 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_InteractionNode337"):
                opp_val = getattr(old_value, "bpmnprof_InteractionNode337", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_InteractionNode337", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_InteractionNode337"):
                opp_val = getattr(value, "bpmnprof_InteractionNode337", None)
                setattr(value, "bpmnprof_InteractionNode337", self)

    @property
    def bpmnprof_MessageFlow342(self):
        return self.__bpmnprof_MessageFlow342

    @bpmnprof_MessageFlow342.setter
    def bpmnprof_MessageFlow342(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_MessageFlow__bpmnprof_MessageFlow342", None)
        self.__bpmnprof_MessageFlow342 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNMessage343"):
                opp_val = getattr(old_value, "bpmnprof_BPMNMessage343", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNMessage343", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNMessage343"):
                opp_val = getattr(value, "bpmnprof_BPMNMessage343", None)
                setattr(value, "bpmnprof_BPMNMessage343", self)

    @property
    def bpmnprof_MessageFlow334(self):
        return self.__bpmnprof_MessageFlow334

    @bpmnprof_MessageFlow334.setter
    def bpmnprof_MessageFlow334(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_MessageFlow__bpmnprof_MessageFlow334", None)
        self.__bpmnprof_MessageFlow334 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_InformationFlow"):
                opp_val = getattr(old_value, "bpmnprof_InformationFlow", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_InformationFlow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_InformationFlow"):
                opp_val = getattr(value, "bpmnprof_InformationFlow", None)
                setattr(value, "bpmnprof_InformationFlow", self)

    @property
    def bpmnprof_MessageFlow339(self):
        return self.__bpmnprof_MessageFlow339

    @bpmnprof_MessageFlow339.setter
    def bpmnprof_MessageFlow339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_MessageFlow__bpmnprof_MessageFlow339", None)
        self.__bpmnprof_MessageFlow339 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_InteractionNode340"):
                opp_val = getattr(old_value, "bpmnprof_InteractionNode340", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_InteractionNode340", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_InteractionNode340"):
                opp_val = getattr(value, "bpmnprof_InteractionNode340", None)
                setattr(value, "bpmnprof_InteractionNode340", self)

    @property
    def bpmnprof_MessageFlow332(self):
        return self.__bpmnprof_MessageFlow332

    @bpmnprof_MessageFlow332.setter
    def bpmnprof_MessageFlow332(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_MessageFlow__bpmnprof_MessageFlow332", None)
        self.__bpmnprof_MessageFlow332 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_MessageFlowAssociation331"):
                opp_val = getattr(old_value, "bpmnprof_MessageFlowAssociation331", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_MessageFlowAssociation331", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_MessageFlowAssociation331"):
                opp_val = getattr(value, "bpmnprof_MessageFlowAssociation331", None)
                setattr(value, "bpmnprof_MessageFlowAssociation331", self)

    @property
    def bpmnprof_MessageFlow329(self):
        return self.__bpmnprof_MessageFlow329

    @bpmnprof_MessageFlow329.setter
    def bpmnprof_MessageFlow329(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_MessageFlow__bpmnprof_MessageFlow329", None)
        self.__bpmnprof_MessageFlow329 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_MessageFlowAssociation328"):
                opp_val = getattr(old_value, "bpmnprof_MessageFlowAssociation328", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_MessageFlowAssociation328", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_MessageFlowAssociation328"):
                opp_val = getattr(value, "bpmnprof_MessageFlowAssociation328", None)
                setattr(value, "bpmnprof_MessageFlowAssociation328", self)

    @property
    def bpmnprof_MessageFlow349(self):
        return self.__bpmnprof_MessageFlow349

    @bpmnprof_MessageFlow349.setter
    def bpmnprof_MessageFlow349(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_MessageFlow__bpmnprof_MessageFlow349", None)
        self.__bpmnprof_MessageFlow349 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ConversationNode348"):
                opp_val = getattr(old_value, "bpmnprof_ConversationNode348", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ConversationNode348"):
                opp_val = getattr(value, "bpmnprof_ConversationNode348", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_ConversationNode348", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def MessageFlowsourceRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MessageFlowsourceRef method
        pass

    def MessageFlowtargetRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MessageFlowtargetRef method
        pass

    def MessageFlowmessageRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MessageFlowmessageRef method
        pass

class bpmnprof_ResourceRole(BaseElement):

    def __init__(self, ResourceRole: "bpmnprof_BPMNProcess" = None, bpmnprof_ResourceRole: "bpmnprof_Property" = None, bpmnprof_ResourceRole405: "bpmnprof_ResourceAssignmentExpression" = None, bpmnprof_ResourceRole407: "bpmnprof_Resource" = None, bpmnprof_ResourceRole409: set["bpmnprof_ResourceParameterBinding"] = None, resources: "bpmnprof_BPMNProcess" = None, bpmnprof_ResourceRole434: "bpmnprof_GlobalTask" = None, bpmnprof_ResourceRole461: "bpmnprof_BPMNActivity" = None):
        self.ResourceRole = ResourceRole
        self.bpmnprof_ResourceRole = bpmnprof_ResourceRole
        self.bpmnprof_ResourceRole405 = bpmnprof_ResourceRole405
        self.bpmnprof_ResourceRole407 = bpmnprof_ResourceRole407
        self.bpmnprof_ResourceRole409 = bpmnprof_ResourceRole409 if bpmnprof_ResourceRole409 is not None else set()
        self.resources = resources
        self.bpmnprof_ResourceRole434 = bpmnprof_ResourceRole434
        self.bpmnprof_ResourceRole461 = bpmnprof_ResourceRole461
        
    @property
    def bpmnprof_ResourceRole405(self):
        return self.__bpmnprof_ResourceRole405

    @bpmnprof_ResourceRole405.setter
    def bpmnprof_ResourceRole405(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ResourceRole__bpmnprof_ResourceRole405", None)
        self.__bpmnprof_ResourceRole405 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ResourceAssignmentExpression"):
                opp_val = getattr(old_value, "bpmnprof_ResourceAssignmentExpression", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ResourceAssignmentExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ResourceAssignmentExpression"):
                opp_val = getattr(value, "bpmnprof_ResourceAssignmentExpression", None)
                setattr(value, "bpmnprof_ResourceAssignmentExpression", self)

    @property
    def bpmnprof_ResourceRole409(self):
        return self.__bpmnprof_ResourceRole409

    @bpmnprof_ResourceRole409.setter
    def bpmnprof_ResourceRole409(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ResourceRole__bpmnprof_ResourceRole409", None)
        self.__bpmnprof_ResourceRole409 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_ResourceParameterBinding"):
                    opp_val = getattr(item, "bpmnprof_ResourceParameterBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_ResourceParameterBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_ResourceParameterBinding"):
                    opp_val = getattr(item, "bpmnprof_ResourceParameterBinding", None)
                    
                    setattr(item, "bpmnprof_ResourceParameterBinding", self)
                    

    @property
    def ResourceRole(self):
        return self.__ResourceRole

    @ResourceRole.setter
    def ResourceRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ResourceRole__ResourceRole", None)
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
    def bpmnprof_ResourceRole407(self):
        return self.__bpmnprof_ResourceRole407

    @bpmnprof_ResourceRole407.setter
    def bpmnprof_ResourceRole407(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ResourceRole__bpmnprof_ResourceRole407", None)
        self.__bpmnprof_ResourceRole407 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Resource"):
                opp_val = getattr(old_value, "bpmnprof_Resource", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Resource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Resource"):
                opp_val = getattr(value, "bpmnprof_Resource", None)
                setattr(value, "bpmnprof_Resource", self)

    @property
    def bpmnprof_ResourceRole461(self):
        return self.__bpmnprof_ResourceRole461

    @bpmnprof_ResourceRole461.setter
    def bpmnprof_ResourceRole461(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ResourceRole__bpmnprof_ResourceRole461", None)
        self.__bpmnprof_ResourceRole461 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNActivity460"):
                opp_val = getattr(old_value, "bpmnprof_BPMNActivity460", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNActivity460"):
                opp_val = getattr(value, "bpmnprof_BPMNActivity460", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_BPMNActivity460", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def resources(self):
        return self.__resources

    @resources.setter
    def resources(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ResourceRole__resources", None)
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
    def bpmnprof_ResourceRole(self):
        return self.__bpmnprof_ResourceRole

    @bpmnprof_ResourceRole.setter
    def bpmnprof_ResourceRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ResourceRole__bpmnprof_ResourceRole", None)
        self.__bpmnprof_ResourceRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Property403"):
                opp_val = getattr(old_value, "bpmnprof_Property403", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Property403", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Property403"):
                opp_val = getattr(value, "bpmnprof_Property403", None)
                setattr(value, "bpmnprof_Property403", self)

    @property
    def bpmnprof_ResourceRole434(self):
        return self.__bpmnprof_ResourceRole434

    @bpmnprof_ResourceRole434.setter
    def bpmnprof_ResourceRole434(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ResourceRole__bpmnprof_ResourceRole434", None)
        self.__bpmnprof_ResourceRole434 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_GlobalTask433"):
                opp_val = getattr(old_value, "bpmnprof_GlobalTask433", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_GlobalTask433"):
                opp_val = getattr(value, "bpmnprof_GlobalTask433", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_GlobalTask433", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def ResourceRoleowner(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ResourceRoleowner method
        pass

    def ResourceRoleresourceParameterBindings(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ResourceRoleresourceParameterBindings method
        pass

    def ResourceRoleprocess(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ResourceRoleprocess method
        pass

    def ResourceRoleisRequired(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceRoleisRequired method
        pass

    def ResourceRoleresourceRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ResourceRoleresourceRef method
        pass

class bpmnprof_ResourceParameter(BaseElement):

    def __init__(self, isRequired: str, bpmnprof_ResourceParameter: "bpmnprof_Resource" = None, bpmnprof_ResourceParameter417: "bpmnprof_Property" = None, bpmnprof_ResourceParameter420: "bpmnprof_ItemDefinition" = None, bpmnprof_ResourceParameter427: "bpmnprof_ResourceParameterBinding" = None):
        self.isRequired = isRequired
        self.bpmnprof_ResourceParameter = bpmnprof_ResourceParameter
        self.bpmnprof_ResourceParameter417 = bpmnprof_ResourceParameter417
        self.bpmnprof_ResourceParameter420 = bpmnprof_ResourceParameter420
        self.bpmnprof_ResourceParameter427 = bpmnprof_ResourceParameter427
        
    @property
    def isRequired(self) -> str:
        return self.__isRequired

    @isRequired.setter
    def isRequired(self, isRequired: str):
        self.__isRequired = isRequired

    @property
    def bpmnprof_ResourceParameter417(self):
        return self.__bpmnprof_ResourceParameter417

    @bpmnprof_ResourceParameter417.setter
    def bpmnprof_ResourceParameter417(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ResourceParameter__bpmnprof_ResourceParameter417", None)
        self.__bpmnprof_ResourceParameter417 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Property418"):
                opp_val = getattr(old_value, "bpmnprof_Property418", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Property418", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Property418"):
                opp_val = getattr(value, "bpmnprof_Property418", None)
                setattr(value, "bpmnprof_Property418", self)

    @property
    def bpmnprof_ResourceParameter420(self):
        return self.__bpmnprof_ResourceParameter420

    @bpmnprof_ResourceParameter420.setter
    def bpmnprof_ResourceParameter420(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ResourceParameter__bpmnprof_ResourceParameter420", None)
        self.__bpmnprof_ResourceParameter420 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ItemDefinition421"):
                opp_val = getattr(old_value, "bpmnprof_ItemDefinition421", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ItemDefinition421", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ItemDefinition421"):
                opp_val = getattr(value, "bpmnprof_ItemDefinition421", None)
                setattr(value, "bpmnprof_ItemDefinition421", self)

    @property
    def bpmnprof_ResourceParameter(self):
        return self.__bpmnprof_ResourceParameter

    @bpmnprof_ResourceParameter.setter
    def bpmnprof_ResourceParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ResourceParameter__bpmnprof_ResourceParameter", None)
        self.__bpmnprof_ResourceParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Resource415"):
                opp_val = getattr(old_value, "bpmnprof_Resource415", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Resource415"):
                opp_val = getattr(value, "bpmnprof_Resource415", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_Resource415", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_ResourceParameter427(self):
        return self.__bpmnprof_ResourceParameter427

    @bpmnprof_ResourceParameter427.setter
    def bpmnprof_ResourceParameter427(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ResourceParameter__bpmnprof_ResourceParameter427", None)
        self.__bpmnprof_ResourceParameter427 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ResourceParameterBinding426"):
                opp_val = getattr(old_value, "bpmnprof_ResourceParameterBinding426", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ResourceParameterBinding426", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ResourceParameterBinding426"):
                opp_val = getattr(value, "bpmnprof_ResourceParameterBinding426", None)
                setattr(value, "bpmnprof_ResourceParameterBinding426", self)

    def ResourceParameterisRequired(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceParameterisRequired method
        pass

    def ResourceParametertype(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceParametertype method
        pass

    def ResourceParameterowner(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceParameterowner method
        pass

class bpmnprof_CorrelationPropertyRetrievalExpression(BaseElement):

    pass
class bpmnprof_Monitoring(BaseElement):

    pass
class bpmnprof_Rendering(BaseElement):

    pass
class bpmnprof_CorrelationPropertyBinding(BaseElement):

    pass
class bpmnprof_InputOutputBinding(BaseElement):

    pass
class bpmnprof_ParticipantAssociation(BaseElement):

    def __init__(self, bpmnprof_ParticipantAssociation: "bpmnprof_BPMNCollaboration" = None, bpmnprof_ParticipantAssociation280: "bpmnprof_Dependency" = None, bpmnprof_ParticipantAssociation283: "bpmnprof_Participant" = None, bpmnprof_ParticipantAssociation286: "bpmnprof_Participant" = None, bpmnprof_ParticipantAssociation608: "bpmnprof_CallConversation" = None):
        self.bpmnprof_ParticipantAssociation = bpmnprof_ParticipantAssociation
        self.bpmnprof_ParticipantAssociation280 = bpmnprof_ParticipantAssociation280
        self.bpmnprof_ParticipantAssociation283 = bpmnprof_ParticipantAssociation283
        self.bpmnprof_ParticipantAssociation286 = bpmnprof_ParticipantAssociation286
        self.bpmnprof_ParticipantAssociation608 = bpmnprof_ParticipantAssociation608
        
    @property
    def bpmnprof_ParticipantAssociation283(self):
        return self.__bpmnprof_ParticipantAssociation283

    @bpmnprof_ParticipantAssociation283.setter
    def bpmnprof_ParticipantAssociation283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ParticipantAssociation__bpmnprof_ParticipantAssociation283", None)
        self.__bpmnprof_ParticipantAssociation283 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Participant284"):
                opp_val = getattr(old_value, "bpmnprof_Participant284", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Participant284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Participant284"):
                opp_val = getattr(value, "bpmnprof_Participant284", None)
                setattr(value, "bpmnprof_Participant284", self)

    @property
    def bpmnprof_ParticipantAssociation(self):
        return self.__bpmnprof_ParticipantAssociation

    @bpmnprof_ParticipantAssociation.setter
    def bpmnprof_ParticipantAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ParticipantAssociation__bpmnprof_ParticipantAssociation", None)
        self.__bpmnprof_ParticipantAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNCollaboration265"):
                opp_val = getattr(old_value, "bpmnprof_BPMNCollaboration265", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNCollaboration265"):
                opp_val = getattr(value, "bpmnprof_BPMNCollaboration265", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_BPMNCollaboration265", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_ParticipantAssociation280(self):
        return self.__bpmnprof_ParticipantAssociation280

    @bpmnprof_ParticipantAssociation280.setter
    def bpmnprof_ParticipantAssociation280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ParticipantAssociation__bpmnprof_ParticipantAssociation280", None)
        self.__bpmnprof_ParticipantAssociation280 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Dependency281"):
                opp_val = getattr(old_value, "bpmnprof_Dependency281", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Dependency281", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Dependency281"):
                opp_val = getattr(value, "bpmnprof_Dependency281", None)
                setattr(value, "bpmnprof_Dependency281", self)

    @property
    def bpmnprof_ParticipantAssociation608(self):
        return self.__bpmnprof_ParticipantAssociation608

    @bpmnprof_ParticipantAssociation608.setter
    def bpmnprof_ParticipantAssociation608(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ParticipantAssociation__bpmnprof_ParticipantAssociation608", None)
        self.__bpmnprof_ParticipantAssociation608 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_CallConversation607"):
                opp_val = getattr(old_value, "bpmnprof_CallConversation607", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_CallConversation607"):
                opp_val = getattr(value, "bpmnprof_CallConversation607", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_CallConversation607", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_ParticipantAssociation286(self):
        return self.__bpmnprof_ParticipantAssociation286

    @bpmnprof_ParticipantAssociation286.setter
    def bpmnprof_ParticipantAssociation286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ParticipantAssociation__bpmnprof_ParticipantAssociation286", None)
        self.__bpmnprof_ParticipantAssociation286 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Participant287"):
                opp_val = getattr(old_value, "bpmnprof_Participant287", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Participant287", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Participant287"):
                opp_val = getattr(value, "bpmnprof_Participant287", None)
                setattr(value, "bpmnprof_Participant287", self)

    def ParticipantAssociationouterParticipantRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ParticipantAssociationouterParticipantRef method
        pass

    def ParticipantAssociationinnerParticipantRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ParticipantAssociationinnerParticipantRef method
        pass

class bpmnprof_Auditing(BaseElement):

    pass
class bpmnprof_BPMNOperation(BaseElement):

    def __init__(self, bpmnprof_BPMNOperation: "bpmnprof_BPMNInterface" = None, bpmnprof_BPMNOperation245: "bpmnprof_BPMNMessage" = None, bpmnprof_BPMNOperation248: set["bpmnprof_Error"] = None, bpmnprof_BPMNOperation238: "bpmnprof_Operation" = None, bpmnprof_BPMNOperation240: "bpmnprof_Element" = None, bpmnprof_BPMNOperation243: "bpmnprof_BPMNMessage" = None, bpmnprof_BPMNOperation260: "bpmnprof_InputOutputBinding" = None, bpmnprof_BPMNOperation535: "bpmnprof_MessageEventDefinition" = None, bpmnprof_BPMNOperation638: "bpmnprof_SendTask" = None, bpmnprof_BPMNOperation650: "bpmnprof_ReceiveTask" = None, bpmnprof_BPMNOperation655: "bpmnprof_ServiceTask" = None):
        self.bpmnprof_BPMNOperation = bpmnprof_BPMNOperation
        self.bpmnprof_BPMNOperation245 = bpmnprof_BPMNOperation245
        self.bpmnprof_BPMNOperation248 = bpmnprof_BPMNOperation248 if bpmnprof_BPMNOperation248 is not None else set()
        self.bpmnprof_BPMNOperation238 = bpmnprof_BPMNOperation238
        self.bpmnprof_BPMNOperation240 = bpmnprof_BPMNOperation240
        self.bpmnprof_BPMNOperation243 = bpmnprof_BPMNOperation243
        self.bpmnprof_BPMNOperation260 = bpmnprof_BPMNOperation260
        self.bpmnprof_BPMNOperation535 = bpmnprof_BPMNOperation535
        self.bpmnprof_BPMNOperation638 = bpmnprof_BPMNOperation638
        self.bpmnprof_BPMNOperation650 = bpmnprof_BPMNOperation650
        self.bpmnprof_BPMNOperation655 = bpmnprof_BPMNOperation655
        
    @property
    def bpmnprof_BPMNOperation655(self):
        return self.__bpmnprof_BPMNOperation655

    @bpmnprof_BPMNOperation655.setter
    def bpmnprof_BPMNOperation655(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNOperation__bpmnprof_BPMNOperation655", None)
        self.__bpmnprof_BPMNOperation655 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ServiceTask654"):
                opp_val = getattr(old_value, "bpmnprof_ServiceTask654", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ServiceTask654", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ServiceTask654"):
                opp_val = getattr(value, "bpmnprof_ServiceTask654", None)
                setattr(value, "bpmnprof_ServiceTask654", self)

    @property
    def bpmnprof_BPMNOperation260(self):
        return self.__bpmnprof_BPMNOperation260

    @bpmnprof_BPMNOperation260.setter
    def bpmnprof_BPMNOperation260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNOperation__bpmnprof_BPMNOperation260", None)
        self.__bpmnprof_BPMNOperation260 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_InputOutputBinding259"):
                opp_val = getattr(old_value, "bpmnprof_InputOutputBinding259", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_InputOutputBinding259", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_InputOutputBinding259"):
                opp_val = getattr(value, "bpmnprof_InputOutputBinding259", None)
                setattr(value, "bpmnprof_InputOutputBinding259", self)

    @property
    def bpmnprof_BPMNOperation248(self):
        return self.__bpmnprof_BPMNOperation248

    @bpmnprof_BPMNOperation248.setter
    def bpmnprof_BPMNOperation248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNOperation__bpmnprof_BPMNOperation248", None)
        self.__bpmnprof_BPMNOperation248 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_Error"):
                    opp_val = getattr(item, "bpmnprof_Error", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_Error", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_Error"):
                    opp_val = getattr(item, "bpmnprof_Error", None)
                    
                    setattr(item, "bpmnprof_Error", self)
                    

    @property
    def bpmnprof_BPMNOperation535(self):
        return self.__bpmnprof_BPMNOperation535

    @bpmnprof_BPMNOperation535.setter
    def bpmnprof_BPMNOperation535(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNOperation__bpmnprof_BPMNOperation535", None)
        self.__bpmnprof_BPMNOperation535 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_MessageEventDefinition534"):
                opp_val = getattr(old_value, "bpmnprof_MessageEventDefinition534", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_MessageEventDefinition534", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_MessageEventDefinition534"):
                opp_val = getattr(value, "bpmnprof_MessageEventDefinition534", None)
                setattr(value, "bpmnprof_MessageEventDefinition534", self)

    @property
    def bpmnprof_BPMNOperation(self):
        return self.__bpmnprof_BPMNOperation

    @bpmnprof_BPMNOperation.setter
    def bpmnprof_BPMNOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNOperation__bpmnprof_BPMNOperation", None)
        self.__bpmnprof_BPMNOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNInterface233"):
                opp_val = getattr(old_value, "bpmnprof_BPMNInterface233", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNInterface233"):
                opp_val = getattr(value, "bpmnprof_BPMNInterface233", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_BPMNInterface233", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_BPMNOperation240(self):
        return self.__bpmnprof_BPMNOperation240

    @bpmnprof_BPMNOperation240.setter
    def bpmnprof_BPMNOperation240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNOperation__bpmnprof_BPMNOperation240", None)
        self.__bpmnprof_BPMNOperation240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Element241"):
                opp_val = getattr(old_value, "bpmnprof_Element241", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Element241", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Element241"):
                opp_val = getattr(value, "bpmnprof_Element241", None)
                setattr(value, "bpmnprof_Element241", self)

    @property
    def bpmnprof_BPMNOperation650(self):
        return self.__bpmnprof_BPMNOperation650

    @bpmnprof_BPMNOperation650.setter
    def bpmnprof_BPMNOperation650(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNOperation__bpmnprof_BPMNOperation650", None)
        self.__bpmnprof_BPMNOperation650 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ReceiveTask649"):
                opp_val = getattr(old_value, "bpmnprof_ReceiveTask649", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ReceiveTask649", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ReceiveTask649"):
                opp_val = getattr(value, "bpmnprof_ReceiveTask649", None)
                setattr(value, "bpmnprof_ReceiveTask649", self)

    @property
    def bpmnprof_BPMNOperation638(self):
        return self.__bpmnprof_BPMNOperation638

    @bpmnprof_BPMNOperation638.setter
    def bpmnprof_BPMNOperation638(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNOperation__bpmnprof_BPMNOperation638", None)
        self.__bpmnprof_BPMNOperation638 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_SendTask637"):
                opp_val = getattr(old_value, "bpmnprof_SendTask637", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_SendTask637", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_SendTask637"):
                opp_val = getattr(value, "bpmnprof_SendTask637", None)
                setattr(value, "bpmnprof_SendTask637", self)

    @property
    def bpmnprof_BPMNOperation245(self):
        return self.__bpmnprof_BPMNOperation245

    @bpmnprof_BPMNOperation245.setter
    def bpmnprof_BPMNOperation245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNOperation__bpmnprof_BPMNOperation245", None)
        self.__bpmnprof_BPMNOperation245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNMessage246"):
                opp_val = getattr(old_value, "bpmnprof_BPMNMessage246", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNMessage246", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNMessage246"):
                opp_val = getattr(value, "bpmnprof_BPMNMessage246", None)
                setattr(value, "bpmnprof_BPMNMessage246", self)

    @property
    def bpmnprof_BPMNOperation243(self):
        return self.__bpmnprof_BPMNOperation243

    @bpmnprof_BPMNOperation243.setter
    def bpmnprof_BPMNOperation243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNOperation__bpmnprof_BPMNOperation243", None)
        self.__bpmnprof_BPMNOperation243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNMessage"):
                opp_val = getattr(old_value, "bpmnprof_BPMNMessage", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNMessage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNMessage"):
                opp_val = getattr(value, "bpmnprof_BPMNMessage", None)
                setattr(value, "bpmnprof_BPMNMessage", self)

    @property
    def bpmnprof_BPMNOperation238(self):
        return self.__bpmnprof_BPMNOperation238

    @bpmnprof_BPMNOperation238.setter
    def bpmnprof_BPMNOperation238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNOperation__bpmnprof_BPMNOperation238", None)
        self.__bpmnprof_BPMNOperation238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Operation"):
                opp_val = getattr(old_value, "bpmnprof_Operation", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Operation"):
                opp_val = getattr(value, "bpmnprof_Operation", None)
                setattr(value, "bpmnprof_Operation", self)

    def BPMNOperationinMessageRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BPMNOperationinMessageRef method
        pass

    def BPMNOperationoutMessageRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BPMNOperationoutMessageRef method
        pass

    def BPMNOperationowner(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BPMNOperationowner method
        pass

    def BPMNOperationerrorRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement BPMNOperationerrorRefs method
        pass

class bpmnprof_BPMNArtifact(BaseElement):

    pass
class bpmnprof_MessageFlowAssociation(BaseElement):

    def __init__(self, bpmnprof_MessageFlowAssociation: "bpmnprof_BPMNCollaboration" = None, bpmnprof_MessageFlowAssociation325: "bpmnprof_Dependency" = None, bpmnprof_MessageFlowAssociation328: "bpmnprof_MessageFlow" = None, bpmnprof_MessageFlowAssociation331: "bpmnprof_MessageFlow" = None):
        self.bpmnprof_MessageFlowAssociation = bpmnprof_MessageFlowAssociation
        self.bpmnprof_MessageFlowAssociation325 = bpmnprof_MessageFlowAssociation325
        self.bpmnprof_MessageFlowAssociation328 = bpmnprof_MessageFlowAssociation328
        self.bpmnprof_MessageFlowAssociation331 = bpmnprof_MessageFlowAssociation331
        
    @property
    def bpmnprof_MessageFlowAssociation328(self):
        return self.__bpmnprof_MessageFlowAssociation328

    @bpmnprof_MessageFlowAssociation328.setter
    def bpmnprof_MessageFlowAssociation328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_MessageFlowAssociation__bpmnprof_MessageFlowAssociation328", None)
        self.__bpmnprof_MessageFlowAssociation328 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_MessageFlow329"):
                opp_val = getattr(old_value, "bpmnprof_MessageFlow329", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_MessageFlow329", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_MessageFlow329"):
                opp_val = getattr(value, "bpmnprof_MessageFlow329", None)
                setattr(value, "bpmnprof_MessageFlow329", self)

    @property
    def bpmnprof_MessageFlowAssociation(self):
        return self.__bpmnprof_MessageFlowAssociation

    @bpmnprof_MessageFlowAssociation.setter
    def bpmnprof_MessageFlowAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_MessageFlowAssociation__bpmnprof_MessageFlowAssociation", None)
        self.__bpmnprof_MessageFlowAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNCollaboration268"):
                opp_val = getattr(old_value, "bpmnprof_BPMNCollaboration268", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNCollaboration268"):
                opp_val = getattr(value, "bpmnprof_BPMNCollaboration268", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_BPMNCollaboration268", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_MessageFlowAssociation331(self):
        return self.__bpmnprof_MessageFlowAssociation331

    @bpmnprof_MessageFlowAssociation331.setter
    def bpmnprof_MessageFlowAssociation331(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_MessageFlowAssociation__bpmnprof_MessageFlowAssociation331", None)
        self.__bpmnprof_MessageFlowAssociation331 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_MessageFlow332"):
                opp_val = getattr(old_value, "bpmnprof_MessageFlow332", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_MessageFlow332", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_MessageFlow332"):
                opp_val = getattr(value, "bpmnprof_MessageFlow332", None)
                setattr(value, "bpmnprof_MessageFlow332", self)

    @property
    def bpmnprof_MessageFlowAssociation325(self):
        return self.__bpmnprof_MessageFlowAssociation325

    @bpmnprof_MessageFlowAssociation325.setter
    def bpmnprof_MessageFlowAssociation325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_MessageFlowAssociation__bpmnprof_MessageFlowAssociation325", None)
        self.__bpmnprof_MessageFlowAssociation325 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Dependency326"):
                opp_val = getattr(old_value, "bpmnprof_Dependency326", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Dependency326", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Dependency326"):
                opp_val = getattr(value, "bpmnprof_Dependency326", None)
                setattr(value, "bpmnprof_Dependency326", self)

    def MessageFlowAssociationouterMessageFlowRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MessageFlowAssociationouterMessageFlowRef method
        pass

    def MessageFlowAssociationinnerMessageFlowRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MessageFlowAssociationinnerMessageFlowRef method
        pass

class bpmnprof_OutputSet(BaseElement):

    def __init__(self, bpmnprof_OutputSet: "bpmnprof_InputOutputSpecification" = None, OutputSet: "bpmnprof_DataOutput" = None, bpmnprof_OutputSet218: "bpmnprof_ParameterSet" = None, bpmnprof_OutputSet221: set["bpmnprof_DataOutput"] = None, bpmnprof_OutputSet224: set["bpmnprof_DataOutput"] = None, outputSetRefs: set["bpmnprof_DataOutput"] = None, bpmnprof_OutputSet213: "bpmnprof_DataOutput" = None, bpmnprof_OutputSet216: "bpmnprof_DataOutput" = None, bpmnprof_OutputSet257: "bpmnprof_InputOutputBinding" = None):
        self.bpmnprof_OutputSet = bpmnprof_OutputSet
        self.OutputSet = OutputSet
        self.bpmnprof_OutputSet218 = bpmnprof_OutputSet218
        self.bpmnprof_OutputSet221 = bpmnprof_OutputSet221 if bpmnprof_OutputSet221 is not None else set()
        self.bpmnprof_OutputSet224 = bpmnprof_OutputSet224 if bpmnprof_OutputSet224 is not None else set()
        self.outputSetRefs = outputSetRefs if outputSetRefs is not None else set()
        self.bpmnprof_OutputSet213 = bpmnprof_OutputSet213
        self.bpmnprof_OutputSet216 = bpmnprof_OutputSet216
        self.bpmnprof_OutputSet257 = bpmnprof_OutputSet257
        
    @property
    def bpmnprof_OutputSet218(self):
        return self.__bpmnprof_OutputSet218

    @bpmnprof_OutputSet218.setter
    def bpmnprof_OutputSet218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_OutputSet__bpmnprof_OutputSet218", None)
        self.__bpmnprof_OutputSet218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ParameterSet219"):
                opp_val = getattr(old_value, "bpmnprof_ParameterSet219", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ParameterSet219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ParameterSet219"):
                opp_val = getattr(value, "bpmnprof_ParameterSet219", None)
                setattr(value, "bpmnprof_ParameterSet219", self)

    @property
    def outputSetRefs(self):
        return self.__outputSetRefs

    @outputSetRefs.setter
    def outputSetRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_OutputSet__outputSetRefs", None)
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
    def OutputSet(self):
        return self.__OutputSet

    @OutputSet.setter
    def OutputSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_OutputSet__OutputSet", None)
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
    def bpmnprof_OutputSet(self):
        return self.__bpmnprof_OutputSet

    @bpmnprof_OutputSet.setter
    def bpmnprof_OutputSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_OutputSet__bpmnprof_OutputSet", None)
        self.__bpmnprof_OutputSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_InputOutputSpecification167"):
                opp_val = getattr(old_value, "bpmnprof_InputOutputSpecification167", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_InputOutputSpecification167"):
                opp_val = getattr(value, "bpmnprof_InputOutputSpecification167", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_InputOutputSpecification167", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_OutputSet216(self):
        return self.__bpmnprof_OutputSet216

    @bpmnprof_OutputSet216.setter
    def bpmnprof_OutputSet216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_OutputSet__bpmnprof_OutputSet216", None)
        self.__bpmnprof_OutputSet216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_DataOutput215"):
                opp_val = getattr(old_value, "bpmnprof_DataOutput215", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_DataOutput215"):
                opp_val = getattr(value, "bpmnprof_DataOutput215", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_DataOutput215", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_OutputSet257(self):
        return self.__bpmnprof_OutputSet257

    @bpmnprof_OutputSet257.setter
    def bpmnprof_OutputSet257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_OutputSet__bpmnprof_OutputSet257", None)
        self.__bpmnprof_OutputSet257 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_InputOutputBinding256"):
                opp_val = getattr(old_value, "bpmnprof_InputOutputBinding256", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_InputOutputBinding256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_InputOutputBinding256"):
                opp_val = getattr(value, "bpmnprof_InputOutputBinding256", None)
                setattr(value, "bpmnprof_InputOutputBinding256", self)

    @property
    def bpmnprof_OutputSet224(self):
        return self.__bpmnprof_OutputSet224

    @bpmnprof_OutputSet224.setter
    def bpmnprof_OutputSet224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_OutputSet__bpmnprof_OutputSet224", None)
        self.__bpmnprof_OutputSet224 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_DataOutput225"):
                    opp_val = getattr(item, "bpmnprof_DataOutput225", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_DataOutput225", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_DataOutput225"):
                    opp_val = getattr(item, "bpmnprof_DataOutput225", None)
                    
                    setattr(item, "bpmnprof_DataOutput225", self)
                    

    @property
    def bpmnprof_OutputSet221(self):
        return self.__bpmnprof_OutputSet221

    @bpmnprof_OutputSet221.setter
    def bpmnprof_OutputSet221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_OutputSet__bpmnprof_OutputSet221", None)
        self.__bpmnprof_OutputSet221 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_DataOutput222"):
                    opp_val = getattr(item, "bpmnprof_DataOutput222", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_DataOutput222", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_DataOutput222"):
                    opp_val = getattr(item, "bpmnprof_DataOutput222", None)
                    
                    setattr(item, "bpmnprof_DataOutput222", self)
                    

    @property
    def bpmnprof_OutputSet213(self):
        return self.__bpmnprof_OutputSet213

    @bpmnprof_OutputSet213.setter
    def bpmnprof_OutputSet213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_OutputSet__bpmnprof_OutputSet213", None)
        self.__bpmnprof_OutputSet213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_DataOutput212"):
                opp_val = getattr(old_value, "bpmnprof_DataOutput212", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_DataOutput212"):
                opp_val = getattr(value, "bpmnprof_DataOutput212", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_DataOutput212", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def OutputSetoptionalOutputRefs(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement OutputSetoptionalOutputRefs method
        pass

    def OutputSetdataOutputRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement OutputSetdataOutputRefs method
        pass

    def OutputSetwhileExecutingOutputRefs(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement OutputSetwhileExecutingOutputRefs method
        pass

class bpmnprof_BPMNExpression(BaseElement):

    pass
class bpmnprof_CorrelationProperty(BaseElement):

    pass
class bpmnprof_InputSet(BaseElement):

    def __init__(self, bpmnprof_InputSet: "bpmnprof_InputOutputSpecification" = None, InputSet: "bpmnprof_DataInput" = None, InputSet176: "bpmnprof_DataInput" = None, InputSet178: "bpmnprof_DataInput" = None, bpmnprof_InputSet196: "bpmnprof_ParameterSet" = None, inputSetWithOptional: set["bpmnprof_DataInput"] = None, inputSetWithWhileExecuting: set["bpmnprof_DataInput"] = None, inputSetRefs: set["bpmnprof_DataInput"] = None, bpmnprof_InputSet254: "bpmnprof_InputOutputBinding" = None):
        self.bpmnprof_InputSet = bpmnprof_InputSet
        self.InputSet = InputSet
        self.InputSet176 = InputSet176
        self.InputSet178 = InputSet178
        self.bpmnprof_InputSet196 = bpmnprof_InputSet196
        self.inputSetWithOptional = inputSetWithOptional if inputSetWithOptional is not None else set()
        self.inputSetWithWhileExecuting = inputSetWithWhileExecuting if inputSetWithWhileExecuting is not None else set()
        self.inputSetRefs = inputSetRefs if inputSetRefs is not None else set()
        self.bpmnprof_InputSet254 = bpmnprof_InputSet254
        
    @property
    def inputSetRefs(self):
        return self.__inputSetRefs

    @inputSetRefs.setter
    def inputSetRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_InputSet__inputSetRefs", None)
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
    def InputSet178(self):
        return self.__InputSet178

    @InputSet178.setter
    def InputSet178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_InputSet__InputSet178", None)
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
        old_value = getattr(self, f"_bpmnprof_InputSet__inputSetWithOptional", None)
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
                    

    @property
    def bpmnprof_InputSet254(self):
        return self.__bpmnprof_InputSet254

    @bpmnprof_InputSet254.setter
    def bpmnprof_InputSet254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_InputSet__bpmnprof_InputSet254", None)
        self.__bpmnprof_InputSet254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_InputOutputBinding253"):
                opp_val = getattr(old_value, "bpmnprof_InputOutputBinding253", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_InputOutputBinding253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_InputOutputBinding253"):
                opp_val = getattr(value, "bpmnprof_InputOutputBinding253", None)
                setattr(value, "bpmnprof_InputOutputBinding253", self)

    @property
    def InputSet(self):
        return self.__InputSet

    @InputSet.setter
    def InputSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_InputSet__InputSet", None)
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
    def InputSet176(self):
        return self.__InputSet176

    @InputSet176.setter
    def InputSet176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_InputSet__InputSet176", None)
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
    def bpmnprof_InputSet196(self):
        return self.__bpmnprof_InputSet196

    @bpmnprof_InputSet196.setter
    def bpmnprof_InputSet196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_InputSet__bpmnprof_InputSet196", None)
        self.__bpmnprof_InputSet196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ParameterSet"):
                opp_val = getattr(old_value, "bpmnprof_ParameterSet", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ParameterSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ParameterSet"):
                opp_val = getattr(value, "bpmnprof_ParameterSet", None)
                setattr(value, "bpmnprof_ParameterSet", self)

    @property
    def inputSetWithWhileExecuting(self):
        return self.__inputSetWithWhileExecuting

    @inputSetWithWhileExecuting.setter
    def inputSetWithWhileExecuting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_InputSet__inputSetWithWhileExecuting", None)
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
    def bpmnprof_InputSet(self):
        return self.__bpmnprof_InputSet

    @bpmnprof_InputSet.setter
    def bpmnprof_InputSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_InputSet__bpmnprof_InputSet", None)
        self.__bpmnprof_InputSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_InputOutputSpecification165"):
                opp_val = getattr(old_value, "bpmnprof_InputOutputSpecification165", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_InputOutputSpecification165"):
                opp_val = getattr(value, "bpmnprof_InputOutputSpecification165", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_InputOutputSpecification165", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def InputSetoptionalInputRefs(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement InputSetoptionalInputRefs method
        pass

    def InputSetdataInputRefs(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement InputSetdataInputRefs method
        pass

    def InputSetwhileExecutingInputRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement InputSetwhileExecutingInputRefs method
        pass

class bpmnprof_CorrelationSubscription(BaseElement):

    pass
class bpmnprof_ComplexBehaviorDefinition(BaseElement):

    pass
class bpmnprof_LaneSet(BaseElement):

    def __init__(self, LaneSet: "bpmnprof_FlowElementsContainer" = None, laneSets: "bpmnprof_FlowElementsContainer" = None, bpmnprof_LaneSet: "bpmnprof_ActivityPartition" = None, laneSet: set["bpmnprof_Lane"] = None, bpmnprof_LaneSet56: set["bpmnprof_Lane"] = None, bpmnprof_LaneSet73: "bpmnprof_Lane" = None, LaneSet75: "bpmnprof_Lane" = None, bpmnprof_LaneSet613: "bpmnprof_SubProcess" = None):
        self.LaneSet = LaneSet
        self.laneSets = laneSets
        self.bpmnprof_LaneSet = bpmnprof_LaneSet
        self.laneSet = laneSet if laneSet is not None else set()
        self.bpmnprof_LaneSet56 = bpmnprof_LaneSet56 if bpmnprof_LaneSet56 is not None else set()
        self.bpmnprof_LaneSet73 = bpmnprof_LaneSet73
        self.LaneSet75 = LaneSet75
        self.bpmnprof_LaneSet613 = bpmnprof_LaneSet613
        
    @property
    def bpmnprof_LaneSet(self):
        return self.__bpmnprof_LaneSet

    @bpmnprof_LaneSet.setter
    def bpmnprof_LaneSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_LaneSet__bpmnprof_LaneSet", None)
        self.__bpmnprof_LaneSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ActivityPartition"):
                opp_val = getattr(old_value, "bpmnprof_ActivityPartition", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ActivityPartition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ActivityPartition"):
                opp_val = getattr(value, "bpmnprof_ActivityPartition", None)
                setattr(value, "bpmnprof_ActivityPartition", self)

    @property
    def bpmnprof_LaneSet56(self):
        return self.__bpmnprof_LaneSet56

    @bpmnprof_LaneSet56.setter
    def bpmnprof_LaneSet56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_LaneSet__bpmnprof_LaneSet56", None)
        self.__bpmnprof_LaneSet56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_Lane"):
                    opp_val = getattr(item, "bpmnprof_Lane", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_Lane", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_Lane"):
                    opp_val = getattr(item, "bpmnprof_Lane", None)
                    
                    setattr(item, "bpmnprof_Lane", self)
                    

    @property
    def LaneSet75(self):
        return self.__LaneSet75

    @LaneSet75.setter
    def LaneSet75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_LaneSet__LaneSet75", None)
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
    def LaneSet(self):
        return self.__LaneSet

    @LaneSet.setter
    def LaneSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_LaneSet__LaneSet", None)
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
    def laneSets(self):
        return self.__laneSets

    @laneSets.setter
    def laneSets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_LaneSet__laneSets", None)
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

    @property
    def bpmnprof_LaneSet613(self):
        return self.__bpmnprof_LaneSet613

    @bpmnprof_LaneSet613.setter
    def bpmnprof_LaneSet613(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_LaneSet__bpmnprof_LaneSet613", None)
        self.__bpmnprof_LaneSet613 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_SubProcess612"):
                opp_val = getattr(old_value, "bpmnprof_SubProcess612", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_SubProcess612"):
                opp_val = getattr(value, "bpmnprof_SubProcess612", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_SubProcess612", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_LaneSet73(self):
        return self.__bpmnprof_LaneSet73

    @bpmnprof_LaneSet73.setter
    def bpmnprof_LaneSet73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_LaneSet__bpmnprof_LaneSet73", None)
        self.__bpmnprof_LaneSet73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Lane72"):
                opp_val = getattr(old_value, "bpmnprof_Lane72", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Lane72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Lane72"):
                opp_val = getattr(value, "bpmnprof_Lane72", None)
                setattr(value, "bpmnprof_Lane72", self)

    @property
    def laneSet(self):
        return self.__laneSet

    @laneSet.setter
    def laneSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_LaneSet__laneSet", None)
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
                    

    def LaneSetlanes(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement LaneSetlanes method
        pass

    def LaneSetparentLane(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement LaneSetparentLane method
        pass

    def LaneSetflowElementsContainer(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement LaneSetflowElementsContainer method
        pass

    def LaneSet(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement LaneSet method
        pass

class bpmnprof_DataAssociation(BaseElement):

    def __init__(self, bpmnprof_DataAssociation: "bpmnprof_ObjectFlow" = None, bpmnprof_DataAssociation484: "bpmnprof_ItemAwareElement" = None, bpmnprof_DataAssociation487: "bpmnprof_ItemAwareElement" = None, bpmnprof_DataAssociation490: "bpmnprof_FormalExpression" = None, bpmnprof_DataAssociation493: set["bpmnprof_Assignment"] = None):
        self.bpmnprof_DataAssociation = bpmnprof_DataAssociation
        self.bpmnprof_DataAssociation484 = bpmnprof_DataAssociation484
        self.bpmnprof_DataAssociation487 = bpmnprof_DataAssociation487
        self.bpmnprof_DataAssociation490 = bpmnprof_DataAssociation490
        self.bpmnprof_DataAssociation493 = bpmnprof_DataAssociation493 if bpmnprof_DataAssociation493 is not None else set()
        
    @property
    def bpmnprof_DataAssociation493(self):
        return self.__bpmnprof_DataAssociation493

    @bpmnprof_DataAssociation493.setter
    def bpmnprof_DataAssociation493(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataAssociation__bpmnprof_DataAssociation493", None)
        self.__bpmnprof_DataAssociation493 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_Assignment"):
                    opp_val = getattr(item, "bpmnprof_Assignment", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_Assignment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_Assignment"):
                    opp_val = getattr(item, "bpmnprof_Assignment", None)
                    
                    setattr(item, "bpmnprof_Assignment", self)
                    

    @property
    def bpmnprof_DataAssociation484(self):
        return self.__bpmnprof_DataAssociation484

    @bpmnprof_DataAssociation484.setter
    def bpmnprof_DataAssociation484(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataAssociation__bpmnprof_DataAssociation484", None)
        self.__bpmnprof_DataAssociation484 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ItemAwareElement485"):
                opp_val = getattr(old_value, "bpmnprof_ItemAwareElement485", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ItemAwareElement485", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ItemAwareElement485"):
                opp_val = getattr(value, "bpmnprof_ItemAwareElement485", None)
                setattr(value, "bpmnprof_ItemAwareElement485", self)

    @property
    def bpmnprof_DataAssociation(self):
        return self.__bpmnprof_DataAssociation

    @bpmnprof_DataAssociation.setter
    def bpmnprof_DataAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataAssociation__bpmnprof_DataAssociation", None)
        self.__bpmnprof_DataAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ObjectFlow"):
                opp_val = getattr(old_value, "bpmnprof_ObjectFlow", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ObjectFlow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ObjectFlow"):
                opp_val = getattr(value, "bpmnprof_ObjectFlow", None)
                setattr(value, "bpmnprof_ObjectFlow", self)

    @property
    def bpmnprof_DataAssociation487(self):
        return self.__bpmnprof_DataAssociation487

    @bpmnprof_DataAssociation487.setter
    def bpmnprof_DataAssociation487(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataAssociation__bpmnprof_DataAssociation487", None)
        self.__bpmnprof_DataAssociation487 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ItemAwareElement488"):
                opp_val = getattr(old_value, "bpmnprof_ItemAwareElement488", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ItemAwareElement488", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ItemAwareElement488"):
                opp_val = getattr(value, "bpmnprof_ItemAwareElement488", None)
                setattr(value, "bpmnprof_ItemAwareElement488", self)

    @property
    def bpmnprof_DataAssociation490(self):
        return self.__bpmnprof_DataAssociation490

    @bpmnprof_DataAssociation490.setter
    def bpmnprof_DataAssociation490(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_DataAssociation__bpmnprof_DataAssociation490", None)
        self.__bpmnprof_DataAssociation490 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_FormalExpression491"):
                opp_val = getattr(old_value, "bpmnprof_FormalExpression491", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_FormalExpression491", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_FormalExpression491"):
                opp_val = getattr(value, "bpmnprof_FormalExpression491", None)
                setattr(value, "bpmnprof_FormalExpression491", self)

    def DataAssociationtransformation(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement DataAssociationtransformation method
        pass

    def DataAssociationtarget(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement DataAssociationtarget method
        pass

    def DataAssociationsource(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement DataAssociationsource method
        pass

class bpmnprof_DataState(BaseElement):

    pass
class bpmnprof_Definitions(BaseElement):

    def __init__(self, targetNamespace: str, expressionLanguage: str, typeLanguage: str, exporter: str, exporterVersion: str, bpmnprof_Definitions: "bpmnprof_Package" = None, bpmnprof_Definitions103: set["bpmnprof_BPMNExtension"] = None, bpmnprof_Definitions105: set["bpmnprof_Import"] = None, bpmnprof_Definitions107: set["bpmnprof_BPMNRelationship"] = None, Definitions: "bpmnprof_RootElement" = None, bpmnprof_Definitions130: "bpmnprof_BPMNRelationship" = None, definition: set["bpmnprof_RootElement"] = None, bpmnprof_Definitions119: "bpmnprof_Import" = None):
        self.targetNamespace = targetNamespace
        self.expressionLanguage = expressionLanguage
        self.typeLanguage = typeLanguage
        self.exporter = exporter
        self.exporterVersion = exporterVersion
        self.bpmnprof_Definitions = bpmnprof_Definitions
        self.bpmnprof_Definitions103 = bpmnprof_Definitions103 if bpmnprof_Definitions103 is not None else set()
        self.bpmnprof_Definitions105 = bpmnprof_Definitions105 if bpmnprof_Definitions105 is not None else set()
        self.bpmnprof_Definitions107 = bpmnprof_Definitions107 if bpmnprof_Definitions107 is not None else set()
        self.Definitions = Definitions
        self.bpmnprof_Definitions130 = bpmnprof_Definitions130
        self.definition = definition if definition is not None else set()
        self.bpmnprof_Definitions119 = bpmnprof_Definitions119
        
    @property
    def exporter(self) -> str:
        return self.__exporter

    @exporter.setter
    def exporter(self, exporter: str):
        self.__exporter = exporter

    @property
    def targetNamespace(self) -> str:
        return self.__targetNamespace

    @targetNamespace.setter
    def targetNamespace(self, targetNamespace: str):
        self.__targetNamespace = targetNamespace

    @property
    def expressionLanguage(self) -> str:
        return self.__expressionLanguage

    @expressionLanguage.setter
    def expressionLanguage(self, expressionLanguage: str):
        self.__expressionLanguage = expressionLanguage

    @property
    def exporterVersion(self) -> str:
        return self.__exporterVersion

    @exporterVersion.setter
    def exporterVersion(self, exporterVersion: str):
        self.__exporterVersion = exporterVersion

    @property
    def typeLanguage(self) -> str:
        return self.__typeLanguage

    @typeLanguage.setter
    def typeLanguage(self, typeLanguage: str):
        self.__typeLanguage = typeLanguage

    @property
    def bpmnprof_Definitions130(self):
        return self.__bpmnprof_Definitions130

    @bpmnprof_Definitions130.setter
    def bpmnprof_Definitions130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Definitions__bpmnprof_Definitions130", None)
        self.__bpmnprof_Definitions130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNRelationship129"):
                opp_val = getattr(old_value, "bpmnprof_BPMNRelationship129", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNRelationship129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNRelationship129"):
                opp_val = getattr(value, "bpmnprof_BPMNRelationship129", None)
                setattr(value, "bpmnprof_BPMNRelationship129", self)

    @property
    def bpmnprof_Definitions(self):
        return self.__bpmnprof_Definitions

    @bpmnprof_Definitions.setter
    def bpmnprof_Definitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Definitions__bpmnprof_Definitions", None)
        self.__bpmnprof_Definitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Package"):
                opp_val = getattr(old_value, "bpmnprof_Package", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Package"):
                opp_val = getattr(value, "bpmnprof_Package", None)
                setattr(value, "bpmnprof_Package", self)

    @property
    def Definitions(self):
        return self.__Definitions

    @Definitions.setter
    def Definitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Definitions__Definitions", None)
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
        old_value = getattr(self, f"_bpmnprof_Definitions__definition", None)
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
    def bpmnprof_Definitions119(self):
        return self.__bpmnprof_Definitions119

    @bpmnprof_Definitions119.setter
    def bpmnprof_Definitions119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Definitions__bpmnprof_Definitions119", None)
        self.__bpmnprof_Definitions119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Import118"):
                opp_val = getattr(old_value, "bpmnprof_Import118", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Import118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Import118"):
                opp_val = getattr(value, "bpmnprof_Import118", None)
                setattr(value, "bpmnprof_Import118", self)

    @property
    def bpmnprof_Definitions103(self):
        return self.__bpmnprof_Definitions103

    @bpmnprof_Definitions103.setter
    def bpmnprof_Definitions103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Definitions__bpmnprof_Definitions103", None)
        self.__bpmnprof_Definitions103 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_BPMNExtension"):
                    opp_val = getattr(item, "bpmnprof_BPMNExtension", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_BPMNExtension", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_BPMNExtension"):
                    opp_val = getattr(item, "bpmnprof_BPMNExtension", None)
                    
                    setattr(item, "bpmnprof_BPMNExtension", self)
                    

    @property
    def bpmnprof_Definitions107(self):
        return self.__bpmnprof_Definitions107

    @bpmnprof_Definitions107.setter
    def bpmnprof_Definitions107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Definitions__bpmnprof_Definitions107", None)
        self.__bpmnprof_Definitions107 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_BPMNRelationship"):
                    opp_val = getattr(item, "bpmnprof_BPMNRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_BPMNRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_BPMNRelationship"):
                    opp_val = getattr(item, "bpmnprof_BPMNRelationship", None)
                    
                    setattr(item, "bpmnprof_BPMNRelationship", self)
                    

    @property
    def bpmnprof_Definitions105(self):
        return self.__bpmnprof_Definitions105

    @bpmnprof_Definitions105.setter
    def bpmnprof_Definitions105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Definitions__bpmnprof_Definitions105", None)
        self.__bpmnprof_Definitions105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_Import"):
                    opp_val = getattr(item, "bpmnprof_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_Import"):
                    opp_val = getattr(item, "bpmnprof_Import", None)
                    
                    setattr(item, "bpmnprof_Import", self)
                    

class bpmnprof_ParticipantMultiplicity(BaseElement):

    def __init__(self, minimum: str, maximum: str, bpmnprof_ParticipantMultiplicity317: "bpmnprof_MultiplicityElement" = None, bpmnprof_ParticipantMultiplicity: "bpmnprof_Participant" = None):
        self.minimum = minimum
        self.maximum = maximum
        self.bpmnprof_ParticipantMultiplicity317 = bpmnprof_ParticipantMultiplicity317
        self.bpmnprof_ParticipantMultiplicity = bpmnprof_ParticipantMultiplicity
        
    @property
    def minimum(self) -> str:
        return self.__minimum

    @minimum.setter
    def minimum(self, minimum: str):
        self.__minimum = minimum

    @property
    def maximum(self) -> str:
        return self.__maximum

    @maximum.setter
    def maximum(self, maximum: str):
        self.__maximum = maximum

    @property
    def bpmnprof_ParticipantMultiplicity317(self):
        return self.__bpmnprof_ParticipantMultiplicity317

    @bpmnprof_ParticipantMultiplicity317.setter
    def bpmnprof_ParticipantMultiplicity317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ParticipantMultiplicity__bpmnprof_ParticipantMultiplicity317", None)
        self.__bpmnprof_ParticipantMultiplicity317 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_MultiplicityElement"):
                opp_val = getattr(old_value, "bpmnprof_MultiplicityElement", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_MultiplicityElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_MultiplicityElement"):
                opp_val = getattr(value, "bpmnprof_MultiplicityElement", None)
                setattr(value, "bpmnprof_MultiplicityElement", self)

    @property
    def bpmnprof_ParticipantMultiplicity(self):
        return self.__bpmnprof_ParticipantMultiplicity

    @bpmnprof_ParticipantMultiplicity.setter
    def bpmnprof_ParticipantMultiplicity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ParticipantMultiplicity__bpmnprof_ParticipantMultiplicity", None)
        self.__bpmnprof_ParticipantMultiplicity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Participant295"):
                opp_val = getattr(old_value, "bpmnprof_Participant295", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Participant295", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Participant295"):
                opp_val = getattr(value, "bpmnprof_Participant295", None)
                setattr(value, "bpmnprof_Participant295", self)

class bpmnprof_LoopCharacteristics(BaseElement):

    pass
class bpmnprof_BPMNRelationship(BaseElement):

    def __init__(self, type: str, direction: str, bpmnprof_BPMNRelationship: "bpmnprof_Definitions" = None, bpmnprof_BPMNRelationship123: set["bpmnprof_Element"] = None, bpmnprof_BPMNRelationship126: set["bpmnprof_Element"] = None, bpmnprof_BPMNRelationship129: "bpmnprof_Definitions" = None, bpmnprof_BPMNRelationship121: "bpmnprof_Constraint" = None):
        self.type = type
        self.direction = direction
        self.bpmnprof_BPMNRelationship = bpmnprof_BPMNRelationship
        self.bpmnprof_BPMNRelationship123 = bpmnprof_BPMNRelationship123 if bpmnprof_BPMNRelationship123 is not None else set()
        self.bpmnprof_BPMNRelationship126 = bpmnprof_BPMNRelationship126 if bpmnprof_BPMNRelationship126 is not None else set()
        self.bpmnprof_BPMNRelationship129 = bpmnprof_BPMNRelationship129
        self.bpmnprof_BPMNRelationship121 = bpmnprof_BPMNRelationship121
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def bpmnprof_BPMNRelationship126(self):
        return self.__bpmnprof_BPMNRelationship126

    @bpmnprof_BPMNRelationship126.setter
    def bpmnprof_BPMNRelationship126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNRelationship__bpmnprof_BPMNRelationship126", None)
        self.__bpmnprof_BPMNRelationship126 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_Element127"):
                    opp_val = getattr(item, "bpmnprof_Element127", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_Element127", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_Element127"):
                    opp_val = getattr(item, "bpmnprof_Element127", None)
                    
                    setattr(item, "bpmnprof_Element127", self)
                    

    @property
    def bpmnprof_BPMNRelationship129(self):
        return self.__bpmnprof_BPMNRelationship129

    @bpmnprof_BPMNRelationship129.setter
    def bpmnprof_BPMNRelationship129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNRelationship__bpmnprof_BPMNRelationship129", None)
        self.__bpmnprof_BPMNRelationship129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Definitions130"):
                opp_val = getattr(old_value, "bpmnprof_Definitions130", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Definitions130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Definitions130"):
                opp_val = getattr(value, "bpmnprof_Definitions130", None)
                setattr(value, "bpmnprof_Definitions130", self)

    @property
    def bpmnprof_BPMNRelationship123(self):
        return self.__bpmnprof_BPMNRelationship123

    @bpmnprof_BPMNRelationship123.setter
    def bpmnprof_BPMNRelationship123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNRelationship__bpmnprof_BPMNRelationship123", None)
        self.__bpmnprof_BPMNRelationship123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_Element124"):
                    opp_val = getattr(item, "bpmnprof_Element124", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_Element124", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_Element124"):
                    opp_val = getattr(item, "bpmnprof_Element124", None)
                    
                    setattr(item, "bpmnprof_Element124", self)
                    

    @property
    def bpmnprof_BPMNRelationship121(self):
        return self.__bpmnprof_BPMNRelationship121

    @bpmnprof_BPMNRelationship121.setter
    def bpmnprof_BPMNRelationship121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNRelationship__bpmnprof_BPMNRelationship121", None)
        self.__bpmnprof_BPMNRelationship121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Constraint"):
                opp_val = getattr(old_value, "bpmnprof_Constraint", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Constraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Constraint"):
                opp_val = getattr(value, "bpmnprof_Constraint", None)
                setattr(value, "bpmnprof_Constraint", self)

    @property
    def bpmnprof_BPMNRelationship(self):
        return self.__bpmnprof_BPMNRelationship

    @bpmnprof_BPMNRelationship.setter
    def bpmnprof_BPMNRelationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_BPMNRelationship__bpmnprof_BPMNRelationship", None)
        self.__bpmnprof_BPMNRelationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Definitions107"):
                opp_val = getattr(old_value, "bpmnprof_Definitions107", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Definitions107"):
                opp_val = getattr(value, "bpmnprof_Definitions107", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_Definitions107", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmnprof_FlowElementsContainer(BaseElement):

    pass
class bpmnprof_Participant(BaseElement):

    def __init__(self, bpmnprof_Participant284: "bpmnprof_ParticipantAssociation" = None, bpmnprof_Participant287: "bpmnprof_ParticipantAssociation" = None, bpmnprof_Participant: "bpmnprof_BPMNCollaboration" = None, bpmnprof_Participant289: "bpmnprof_Property" = None, bpmnprof_Participant292: "bpmnprof_BPMNProcess" = None, bpmnprof_Participant295: "bpmnprof_ParticipantMultiplicity" = None, participantRef: set["bpmnprof_PartnerEntity"] = None, participantRef298: set["bpmnprof_PartnerRole"] = None, bpmnprof_Participant300: set["bpmnprof_BPMNInterface"] = None, Participant323: "bpmnprof_PartnerRole" = None, Participant: "bpmnprof_PartnerEntity" = None, bpmnprof_Participant355: "bpmnprof_ConversationNode" = None):
        self.bpmnprof_Participant284 = bpmnprof_Participant284
        self.bpmnprof_Participant287 = bpmnprof_Participant287
        self.bpmnprof_Participant = bpmnprof_Participant
        self.bpmnprof_Participant289 = bpmnprof_Participant289
        self.bpmnprof_Participant292 = bpmnprof_Participant292
        self.bpmnprof_Participant295 = bpmnprof_Participant295
        self.participantRef = participantRef if participantRef is not None else set()
        self.participantRef298 = participantRef298 if participantRef298 is not None else set()
        self.bpmnprof_Participant300 = bpmnprof_Participant300 if bpmnprof_Participant300 is not None else set()
        self.Participant323 = Participant323
        self.Participant = Participant
        self.bpmnprof_Participant355 = bpmnprof_Participant355
        
    @property
    def bpmnprof_Participant292(self):
        return self.__bpmnprof_Participant292

    @bpmnprof_Participant292.setter
    def bpmnprof_Participant292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Participant__bpmnprof_Participant292", None)
        self.__bpmnprof_Participant292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNProcess293"):
                opp_val = getattr(old_value, "bpmnprof_BPMNProcess293", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNProcess293", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNProcess293"):
                opp_val = getattr(value, "bpmnprof_BPMNProcess293", None)
                setattr(value, "bpmnprof_BPMNProcess293", self)

    @property
    def bpmnprof_Participant(self):
        return self.__bpmnprof_Participant

    @bpmnprof_Participant.setter
    def bpmnprof_Participant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Participant__bpmnprof_Participant", None)
        self.__bpmnprof_Participant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNCollaboration278"):
                opp_val = getattr(old_value, "bpmnprof_BPMNCollaboration278", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNCollaboration278"):
                opp_val = getattr(value, "bpmnprof_BPMNCollaboration278", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_BPMNCollaboration278", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmnprof_Participant289(self):
        return self.__bpmnprof_Participant289

    @bpmnprof_Participant289.setter
    def bpmnprof_Participant289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Participant__bpmnprof_Participant289", None)
        self.__bpmnprof_Participant289 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Property290"):
                opp_val = getattr(old_value, "bpmnprof_Property290", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Property290", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Property290"):
                opp_val = getattr(value, "bpmnprof_Property290", None)
                setattr(value, "bpmnprof_Property290", self)

    @property
    def bpmnprof_Participant355(self):
        return self.__bpmnprof_Participant355

    @bpmnprof_Participant355.setter
    def bpmnprof_Participant355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Participant__bpmnprof_Participant355", None)
        self.__bpmnprof_Participant355 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ConversationNode354"):
                opp_val = getattr(old_value, "bpmnprof_ConversationNode354", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ConversationNode354"):
                opp_val = getattr(value, "bpmnprof_ConversationNode354", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_ConversationNode354", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def participantRef298(self):
        return self.__participantRef298

    @participantRef298.setter
    def participantRef298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Participant__participantRef298", None)
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
    def bpmnprof_Participant287(self):
        return self.__bpmnprof_Participant287

    @bpmnprof_Participant287.setter
    def bpmnprof_Participant287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Participant__bpmnprof_Participant287", None)
        self.__bpmnprof_Participant287 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ParticipantAssociation286"):
                opp_val = getattr(old_value, "bpmnprof_ParticipantAssociation286", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ParticipantAssociation286", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ParticipantAssociation286"):
                opp_val = getattr(value, "bpmnprof_ParticipantAssociation286", None)
                setattr(value, "bpmnprof_ParticipantAssociation286", self)

    @property
    def Participant323(self):
        return self.__Participant323

    @Participant323.setter
    def Participant323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Participant__Participant323", None)
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
    def Participant(self):
        return self.__Participant

    @Participant.setter
    def Participant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Participant__Participant", None)
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
    def bpmnprof_Participant284(self):
        return self.__bpmnprof_Participant284

    @bpmnprof_Participant284.setter
    def bpmnprof_Participant284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Participant__bpmnprof_Participant284", None)
        self.__bpmnprof_Participant284 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ParticipantAssociation283"):
                opp_val = getattr(old_value, "bpmnprof_ParticipantAssociation283", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ParticipantAssociation283", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ParticipantAssociation283"):
                opp_val = getattr(value, "bpmnprof_ParticipantAssociation283", None)
                setattr(value, "bpmnprof_ParticipantAssociation283", self)

    @property
    def bpmnprof_Participant300(self):
        return self.__bpmnprof_Participant300

    @bpmnprof_Participant300.setter
    def bpmnprof_Participant300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Participant__bpmnprof_Participant300", None)
        self.__bpmnprof_Participant300 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_BPMNInterface301"):
                    opp_val = getattr(item, "bpmnprof_BPMNInterface301", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_BPMNInterface301", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_BPMNInterface301"):
                    opp_val = getattr(item, "bpmnprof_BPMNInterface301", None)
                    
                    setattr(item, "bpmnprof_BPMNInterface301", self)
                    

    @property
    def bpmnprof_Participant295(self):
        return self.__bpmnprof_Participant295

    @bpmnprof_Participant295.setter
    def bpmnprof_Participant295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Participant__bpmnprof_Participant295", None)
        self.__bpmnprof_Participant295 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ParticipantMultiplicity"):
                opp_val = getattr(old_value, "bpmnprof_ParticipantMultiplicity", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ParticipantMultiplicity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ParticipantMultiplicity"):
                opp_val = getattr(value, "bpmnprof_ParticipantMultiplicity", None)
                setattr(value, "bpmnprof_ParticipantMultiplicity", self)

    @property
    def participantRef(self):
        return self.__participantRef

    @participantRef.setter
    def participantRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Participant__participantRef", None)
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
                    

    def participantpartnerEntityRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement participantpartnerEntityRef method
        pass

    def Participantownership(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement Participantownership method
        pass

    def Participantrealizationsupplier(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement Participantrealizationsupplier method
        pass

    def ParticipantinterfaceRefs(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ParticipantinterfaceRefs method
        pass

    def ParticipantmultiplicityMinimum(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ParticipantmultiplicityMinimum method
        pass

    def ParticipantprocessRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ParticipantprocessRef method
        pass

    def ParticipantmultiplicityMaximum(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ParticipantmultiplicityMaximum method
        pass

    def Participanttype(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement Participanttype method
        pass

    def participantpartnerRoleRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement participantpartnerRoleRef method
        pass

class bpmnprof_CategoryValue(BaseElement):

    pass
class bpmnprof_Documentation(BaseElement):

    def __init__(self, textFormat: str, text: str, bpmnprof_Documentation33: "bpmnprof_Comment" = None, bpmnprof_Documentation: "bpmnprof_BaseElement" = None):
        self.textFormat = textFormat
        self.text = text
        self.bpmnprof_Documentation33 = bpmnprof_Documentation33
        self.bpmnprof_Documentation = bpmnprof_Documentation
        
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
    def bpmnprof_Documentation33(self):
        return self.__bpmnprof_Documentation33

    @bpmnprof_Documentation33.setter
    def bpmnprof_Documentation33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Documentation__bpmnprof_Documentation33", None)
        self.__bpmnprof_Documentation33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Comment"):
                opp_val = getattr(old_value, "bpmnprof_Comment", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Comment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Comment"):
                opp_val = getattr(value, "bpmnprof_Comment", None)
                setattr(value, "bpmnprof_Comment", self)

    @property
    def bpmnprof_Documentation(self):
        return self.__bpmnprof_Documentation

    @bpmnprof_Documentation.setter
    def bpmnprof_Documentation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Documentation__bpmnprof_Documentation", None)
        self.__bpmnprof_Documentation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BaseElement17"):
                opp_val = getattr(old_value, "bpmnprof_BaseElement17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BaseElement17"):
                opp_val = getattr(value, "bpmnprof_BaseElement17", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_BaseElement17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmnprof_ItemAwareElement(BaseElement):

    def __init__(self, bpmnprof_ItemAwareElement: set["bpmnprof_DataState"] = None, bpmnprof_ItemAwareElement181: "bpmnprof_TypedElement" = None, bpmnprof_ItemAwareElement183: "bpmnprof_ItemDefinition" = None, bpmnprof_ItemAwareElement485: "bpmnprof_DataAssociation" = None, bpmnprof_ItemAwareElement488: "bpmnprof_DataAssociation" = None, bpmnprof_ItemAwareElement665: "bpmnprof_MultiInstanceLoopCharacteristics" = None, bpmnprof_ItemAwareElement668: "bpmnprof_MultiInstanceLoopCharacteristics" = None):
        self.bpmnprof_ItemAwareElement = bpmnprof_ItemAwareElement if bpmnprof_ItemAwareElement is not None else set()
        self.bpmnprof_ItemAwareElement181 = bpmnprof_ItemAwareElement181
        self.bpmnprof_ItemAwareElement183 = bpmnprof_ItemAwareElement183
        self.bpmnprof_ItemAwareElement485 = bpmnprof_ItemAwareElement485
        self.bpmnprof_ItemAwareElement488 = bpmnprof_ItemAwareElement488
        self.bpmnprof_ItemAwareElement665 = bpmnprof_ItemAwareElement665
        self.bpmnprof_ItemAwareElement668 = bpmnprof_ItemAwareElement668
        
    @property
    def bpmnprof_ItemAwareElement488(self):
        return self.__bpmnprof_ItemAwareElement488

    @bpmnprof_ItemAwareElement488.setter
    def bpmnprof_ItemAwareElement488(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ItemAwareElement__bpmnprof_ItemAwareElement488", None)
        self.__bpmnprof_ItemAwareElement488 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_DataAssociation487"):
                opp_val = getattr(old_value, "bpmnprof_DataAssociation487", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_DataAssociation487", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_DataAssociation487"):
                opp_val = getattr(value, "bpmnprof_DataAssociation487", None)
                setattr(value, "bpmnprof_DataAssociation487", self)

    @property
    def bpmnprof_ItemAwareElement183(self):
        return self.__bpmnprof_ItemAwareElement183

    @bpmnprof_ItemAwareElement183.setter
    def bpmnprof_ItemAwareElement183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ItemAwareElement__bpmnprof_ItemAwareElement183", None)
        self.__bpmnprof_ItemAwareElement183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ItemDefinition"):
                opp_val = getattr(old_value, "bpmnprof_ItemDefinition", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ItemDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ItemDefinition"):
                opp_val = getattr(value, "bpmnprof_ItemDefinition", None)
                setattr(value, "bpmnprof_ItemDefinition", self)

    @property
    def bpmnprof_ItemAwareElement668(self):
        return self.__bpmnprof_ItemAwareElement668

    @bpmnprof_ItemAwareElement668.setter
    def bpmnprof_ItemAwareElement668(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ItemAwareElement__bpmnprof_ItemAwareElement668", None)
        self.__bpmnprof_ItemAwareElement668 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_MultiInstanceLoopCharacteristics667"):
                opp_val = getattr(old_value, "bpmnprof_MultiInstanceLoopCharacteristics667", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_MultiInstanceLoopCharacteristics667", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_MultiInstanceLoopCharacteristics667"):
                opp_val = getattr(value, "bpmnprof_MultiInstanceLoopCharacteristics667", None)
                setattr(value, "bpmnprof_MultiInstanceLoopCharacteristics667", self)

    @property
    def bpmnprof_ItemAwareElement665(self):
        return self.__bpmnprof_ItemAwareElement665

    @bpmnprof_ItemAwareElement665.setter
    def bpmnprof_ItemAwareElement665(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ItemAwareElement__bpmnprof_ItemAwareElement665", None)
        self.__bpmnprof_ItemAwareElement665 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_MultiInstanceLoopCharacteristics664"):
                opp_val = getattr(old_value, "bpmnprof_MultiInstanceLoopCharacteristics664", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_MultiInstanceLoopCharacteristics664", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_MultiInstanceLoopCharacteristics664"):
                opp_val = getattr(value, "bpmnprof_MultiInstanceLoopCharacteristics664", None)
                setattr(value, "bpmnprof_MultiInstanceLoopCharacteristics664", self)

    @property
    def bpmnprof_ItemAwareElement485(self):
        return self.__bpmnprof_ItemAwareElement485

    @bpmnprof_ItemAwareElement485.setter
    def bpmnprof_ItemAwareElement485(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ItemAwareElement__bpmnprof_ItemAwareElement485", None)
        self.__bpmnprof_ItemAwareElement485 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_DataAssociation484"):
                opp_val = getattr(old_value, "bpmnprof_DataAssociation484", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_DataAssociation484", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_DataAssociation484"):
                opp_val = getattr(value, "bpmnprof_DataAssociation484", None)
                setattr(value, "bpmnprof_DataAssociation484", self)

    @property
    def bpmnprof_ItemAwareElement(self):
        return self.__bpmnprof_ItemAwareElement

    @bpmnprof_ItemAwareElement.setter
    def bpmnprof_ItemAwareElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ItemAwareElement__bpmnprof_ItemAwareElement", None)
        self.__bpmnprof_ItemAwareElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_DataState"):
                    opp_val = getattr(item, "bpmnprof_DataState", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_DataState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_DataState"):
                    opp_val = getattr(item, "bpmnprof_DataState", None)
                    
                    setattr(item, "bpmnprof_DataState", self)
                    

    @property
    def bpmnprof_ItemAwareElement181(self):
        return self.__bpmnprof_ItemAwareElement181

    @bpmnprof_ItemAwareElement181.setter
    def bpmnprof_ItemAwareElement181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ItemAwareElement__bpmnprof_ItemAwareElement181", None)
        self.__bpmnprof_ItemAwareElement181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_TypedElement"):
                opp_val = getattr(old_value, "bpmnprof_TypedElement", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_TypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_TypedElement"):
                opp_val = getattr(value, "bpmnprof_TypedElement", None)
                setattr(value, "bpmnprof_TypedElement", self)

    def ItemAwareElementdataState(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ItemAwareElementdataState method
        pass

class bpmnprof_Lane(BaseElement):

    def __init__(self, Lane: "bpmnprof_LaneSet" = None, bpmnprof_Lane: "bpmnprof_LaneSet" = None, bpmnprof_Lane60: "bpmnprof_ActivityPartition" = None, bpmnprof_Lane63: "bpmnprof_Element" = None, bpmnprof_Lane66: set["bpmnprof_FlowNode"] = None, bpmnprof_Lane69: "bpmnprof_BaseElement" = None, bpmnprof_Lane72: "bpmnprof_LaneSet" = None, lanes: "bpmnprof_LaneSet" = None):
        self.Lane = Lane
        self.bpmnprof_Lane = bpmnprof_Lane
        self.bpmnprof_Lane60 = bpmnprof_Lane60
        self.bpmnprof_Lane63 = bpmnprof_Lane63
        self.bpmnprof_Lane66 = bpmnprof_Lane66 if bpmnprof_Lane66 is not None else set()
        self.bpmnprof_Lane69 = bpmnprof_Lane69
        self.bpmnprof_Lane72 = bpmnprof_Lane72
        self.lanes = lanes
        
    @property
    def bpmnprof_Lane63(self):
        return self.__bpmnprof_Lane63

    @bpmnprof_Lane63.setter
    def bpmnprof_Lane63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Lane__bpmnprof_Lane63", None)
        self.__bpmnprof_Lane63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_Element64"):
                opp_val = getattr(old_value, "bpmnprof_Element64", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_Element64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_Element64"):
                opp_val = getattr(value, "bpmnprof_Element64", None)
                setattr(value, "bpmnprof_Element64", self)

    @property
    def lanes(self):
        return self.__lanes

    @lanes.setter
    def lanes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Lane__lanes", None)
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

    @property
    def bpmnprof_Lane72(self):
        return self.__bpmnprof_Lane72

    @bpmnprof_Lane72.setter
    def bpmnprof_Lane72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Lane__bpmnprof_Lane72", None)
        self.__bpmnprof_Lane72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_LaneSet73"):
                opp_val = getattr(old_value, "bpmnprof_LaneSet73", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_LaneSet73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_LaneSet73"):
                opp_val = getattr(value, "bpmnprof_LaneSet73", None)
                setattr(value, "bpmnprof_LaneSet73", self)

    @property
    def bpmnprof_Lane66(self):
        return self.__bpmnprof_Lane66

    @bpmnprof_Lane66.setter
    def bpmnprof_Lane66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Lane__bpmnprof_Lane66", None)
        self.__bpmnprof_Lane66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmnprof_FlowNode67"):
                    opp_val = getattr(item, "bpmnprof_FlowNode67", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmnprof_FlowNode67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmnprof_FlowNode67"):
                    opp_val = getattr(item, "bpmnprof_FlowNode67", None)
                    
                    setattr(item, "bpmnprof_FlowNode67", self)
                    

    @property
    def bpmnprof_Lane69(self):
        return self.__bpmnprof_Lane69

    @bpmnprof_Lane69.setter
    def bpmnprof_Lane69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Lane__bpmnprof_Lane69", None)
        self.__bpmnprof_Lane69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BaseElement70"):
                opp_val = getattr(old_value, "bpmnprof_BaseElement70", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BaseElement70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BaseElement70"):
                opp_val = getattr(value, "bpmnprof_BaseElement70", None)
                setattr(value, "bpmnprof_BaseElement70", self)

    @property
    def bpmnprof_Lane(self):
        return self.__bpmnprof_Lane

    @bpmnprof_Lane.setter
    def bpmnprof_Lane(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Lane__bpmnprof_Lane", None)
        self.__bpmnprof_Lane = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_LaneSet56"):
                opp_val = getattr(old_value, "bpmnprof_LaneSet56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_LaneSet56"):
                opp_val = getattr(value, "bpmnprof_LaneSet56", None)
                if opp_val is None:
                    setattr(value, "bpmnprof_LaneSet56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Lane(self):
        return self.__Lane

    @Lane.setter
    def Lane(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Lane__Lane", None)
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
    def bpmnprof_Lane60(self):
        return self.__bpmnprof_Lane60

    @bpmnprof_Lane60.setter
    def bpmnprof_Lane60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_Lane__bpmnprof_Lane60", None)
        self.__bpmnprof_Lane60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_ActivityPartition61"):
                opp_val = getattr(old_value, "bpmnprof_ActivityPartition61", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_ActivityPartition61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_ActivityPartition61"):
                opp_val = getattr(value, "bpmnprof_ActivityPartition61", None)
                setattr(value, "bpmnprof_ActivityPartition61", self)

    def LanelaneSet(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement LanelaneSet method
        pass

    def LaneflowNodeRefs(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement LaneflowNodeRefs method
        pass

    def LanechildLaneSet(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement LanechildLaneSet method
        pass

    def LanepartitionElementRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement LanepartitionElementRef method
        pass

class bpmnprof_FlowElement(BaseElement):

    pass
class bpmnprof_ActivityNode:

    pass
class NonExclusiveGateway:

    pass
class bpmnprof_ComplexGateway(NonExclusiveGateway):

    def __init__(self, bpmnprof_ComplexGateway: "bpmnprof_SequenceFlow" = None, bpmnprof_ComplexGateway91: "bpmnprof_BPMNExpression" = None):
        self.bpmnprof_ComplexGateway = bpmnprof_ComplexGateway
        self.bpmnprof_ComplexGateway91 = bpmnprof_ComplexGateway91
        
    @property
    def bpmnprof_ComplexGateway(self):
        return self.__bpmnprof_ComplexGateway

    @bpmnprof_ComplexGateway.setter
    def bpmnprof_ComplexGateway(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ComplexGateway__bpmnprof_ComplexGateway", None)
        self.__bpmnprof_ComplexGateway = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_SequenceFlow89"):
                opp_val = getattr(old_value, "bpmnprof_SequenceFlow89", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_SequenceFlow89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_SequenceFlow89"):
                opp_val = getattr(value, "bpmnprof_SequenceFlow89", None)
                setattr(value, "bpmnprof_SequenceFlow89", self)

    @property
    def bpmnprof_ComplexGateway91(self):
        return self.__bpmnprof_ComplexGateway91

    @bpmnprof_ComplexGateway91.setter
    def bpmnprof_ComplexGateway91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_ComplexGateway__bpmnprof_ComplexGateway91", None)
        self.__bpmnprof_ComplexGateway91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_BPMNExpression92"):
                opp_val = getattr(old_value, "bpmnprof_BPMNExpression92", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_BPMNExpression92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_BPMNExpression92"):
                opp_val = getattr(value, "bpmnprof_BPMNExpression92", None)
                setattr(value, "bpmnprof_BPMNExpression92", self)

    def complexGatewayactivationCondition(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement complexGatewayactivationCondition method
        pass

    def complexGatewaydefault(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement complexGatewaydefault method
        pass

    def complexGatewayjoinSpec(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement complexGatewayjoinSpec method
        pass

class bpmnprof_ParallelGateway(NonExclusiveGateway):

    pass
class bpmnprof_InclusiveGateway(NonExclusiveGateway):

    def __init__(self, bpmnprof_InclusiveGateway: "bpmnprof_SequenceFlow" = None):
        self.bpmnprof_InclusiveGateway = bpmnprof_InclusiveGateway
        
    @property
    def bpmnprof_InclusiveGateway(self):
        return self.__bpmnprof_InclusiveGateway

    @bpmnprof_InclusiveGateway.setter
    def bpmnprof_InclusiveGateway(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmnprof_InclusiveGateway__bpmnprof_InclusiveGateway", None)
        self.__bpmnprof_InclusiveGateway = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmnprof_SequenceFlow"):
                opp_val = getattr(old_value, "bpmnprof_SequenceFlow", None)
                if opp_val == self:
                    setattr(old_value, "bpmnprof_SequenceFlow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmnprof_SequenceFlow"):
                opp_val = getattr(value, "bpmnprof_SequenceFlow", None)
                setattr(value, "bpmnprof_SequenceFlow", self)

    def inclusiveGatewaydefault(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement inclusiveGatewaydefault method
        pass
