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
class AdHocOrdering(Enum):
    parallel = "parallel"
    sequential = "sequential"
class RelationshipDirection(Enum):
    none = "none"
    forward = "forward"
    backward = "backward"
    both = "both"
class ItemKind(Enum):
    physical = "physical"
    information = "information"
class ProcessType(Enum):
    none = "none"
    public = "public"
    private = "private"
class GatewayDirection(Enum):
    unspecified = "unspecified"
    converging = "converging"
    diverging = "diverging"
    mixed = "mixed"
class MultiInstanceBehavior(Enum):
    none = "none"
    one = "one"
    all = "all"
    complex = "complex"
class EventBasedGatewayType(Enum):
    exclusive = "exclusive"
    parallel = "parallel"


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

    def __init__(self, behavior: str, isSequential: str, BPMNProfile_MultiInstanceLoopCharacteristics670: "BPMNProfile_ItemAwareElement" = None, BPMNProfile_MultiInstanceLoopCharacteristics673: "BPMNProfile_ItemAwareElement" = None, BPMNProfile_MultiInstanceLoopCharacteristics676: "BPMNProfile_DataOutput" = None, BPMNProfile_MultiInstanceLoopCharacteristics679: "BPMNProfile_DataInput" = None, BPMNProfile_MultiInstanceLoopCharacteristics682: "BPMNProfile_EventDefinition" = None, BPMNProfile_MultiInstanceLoopCharacteristics685: "BPMNProfile_EventDefinition" = None, BPMNProfile_MultiInstanceLoopCharacteristics688: set["BPMNProfile_ComplexBehaviorDefinition"] = None, BPMNProfile_MultiInstanceLoopCharacteristics: "BPMNProfile_BPMNExpression" = None, BPMNProfile_MultiInstanceLoopCharacteristics665: "BPMNProfile_BPMNExpression" = None, BPMNProfile_MultiInstanceLoopCharacteristics668: "BPMNProfile_ExpansionRegion" = None):
        self.behavior = behavior
        self.isSequential = isSequential
        self.BPMNProfile_MultiInstanceLoopCharacteristics670 = BPMNProfile_MultiInstanceLoopCharacteristics670
        self.BPMNProfile_MultiInstanceLoopCharacteristics673 = BPMNProfile_MultiInstanceLoopCharacteristics673
        self.BPMNProfile_MultiInstanceLoopCharacteristics676 = BPMNProfile_MultiInstanceLoopCharacteristics676
        self.BPMNProfile_MultiInstanceLoopCharacteristics679 = BPMNProfile_MultiInstanceLoopCharacteristics679
        self.BPMNProfile_MultiInstanceLoopCharacteristics682 = BPMNProfile_MultiInstanceLoopCharacteristics682
        self.BPMNProfile_MultiInstanceLoopCharacteristics685 = BPMNProfile_MultiInstanceLoopCharacteristics685
        self.BPMNProfile_MultiInstanceLoopCharacteristics688 = BPMNProfile_MultiInstanceLoopCharacteristics688 if BPMNProfile_MultiInstanceLoopCharacteristics688 is not None else set()
        self.BPMNProfile_MultiInstanceLoopCharacteristics = BPMNProfile_MultiInstanceLoopCharacteristics
        self.BPMNProfile_MultiInstanceLoopCharacteristics665 = BPMNProfile_MultiInstanceLoopCharacteristics665
        self.BPMNProfile_MultiInstanceLoopCharacteristics668 = BPMNProfile_MultiInstanceLoopCharacteristics668
        
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
    def BPMNProfile_MultiInstanceLoopCharacteristics673(self):
        return self.__BPMNProfile_MultiInstanceLoopCharacteristics673

    @BPMNProfile_MultiInstanceLoopCharacteristics673.setter
    def BPMNProfile_MultiInstanceLoopCharacteristics673(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MultiInstanceLoopCharacteristics__BPMNProfile_MultiInstanceLoopCharacteristics673", None)
        self.__BPMNProfile_MultiInstanceLoopCharacteristics673 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ItemAwareElement674"):
                opp_val = getattr(old_value, "BPMNProfile_ItemAwareElement674", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ItemAwareElement674", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ItemAwareElement674"):
                opp_val = getattr(value, "BPMNProfile_ItemAwareElement674", None)
                setattr(value, "BPMNProfile_ItemAwareElement674", self)

    @property
    def BPMNProfile_MultiInstanceLoopCharacteristics685(self):
        return self.__BPMNProfile_MultiInstanceLoopCharacteristics685

    @BPMNProfile_MultiInstanceLoopCharacteristics685.setter
    def BPMNProfile_MultiInstanceLoopCharacteristics685(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MultiInstanceLoopCharacteristics__BPMNProfile_MultiInstanceLoopCharacteristics685", None)
        self.__BPMNProfile_MultiInstanceLoopCharacteristics685 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_EventDefinition686"):
                opp_val = getattr(old_value, "BPMNProfile_EventDefinition686", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_EventDefinition686", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_EventDefinition686"):
                opp_val = getattr(value, "BPMNProfile_EventDefinition686", None)
                setattr(value, "BPMNProfile_EventDefinition686", self)

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
            if hasattr(old_value, "BPMNProfile_ItemAwareElement671"):
                opp_val = getattr(old_value, "BPMNProfile_ItemAwareElement671", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ItemAwareElement671", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ItemAwareElement671"):
                opp_val = getattr(value, "BPMNProfile_ItemAwareElement671", None)
                setattr(value, "BPMNProfile_ItemAwareElement671", self)

    @property
    def BPMNProfile_MultiInstanceLoopCharacteristics682(self):
        return self.__BPMNProfile_MultiInstanceLoopCharacteristics682

    @BPMNProfile_MultiInstanceLoopCharacteristics682.setter
    def BPMNProfile_MultiInstanceLoopCharacteristics682(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MultiInstanceLoopCharacteristics__BPMNProfile_MultiInstanceLoopCharacteristics682", None)
        self.__BPMNProfile_MultiInstanceLoopCharacteristics682 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_EventDefinition683"):
                opp_val = getattr(old_value, "BPMNProfile_EventDefinition683", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_EventDefinition683", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_EventDefinition683"):
                opp_val = getattr(value, "BPMNProfile_EventDefinition683", None)
                setattr(value, "BPMNProfile_EventDefinition683", self)

    @property
    def BPMNProfile_MultiInstanceLoopCharacteristics668(self):
        return self.__BPMNProfile_MultiInstanceLoopCharacteristics668

    @BPMNProfile_MultiInstanceLoopCharacteristics668.setter
    def BPMNProfile_MultiInstanceLoopCharacteristics668(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MultiInstanceLoopCharacteristics__BPMNProfile_MultiInstanceLoopCharacteristics668", None)
        self.__BPMNProfile_MultiInstanceLoopCharacteristics668 = value
        
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
    def BPMNProfile_MultiInstanceLoopCharacteristics665(self):
        return self.__BPMNProfile_MultiInstanceLoopCharacteristics665

    @BPMNProfile_MultiInstanceLoopCharacteristics665.setter
    def BPMNProfile_MultiInstanceLoopCharacteristics665(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MultiInstanceLoopCharacteristics__BPMNProfile_MultiInstanceLoopCharacteristics665", None)
        self.__BPMNProfile_MultiInstanceLoopCharacteristics665 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNExpression666"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNExpression666", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNExpression666", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNExpression666"):
                opp_val = getattr(value, "BPMNProfile_BPMNExpression666", None)
                setattr(value, "BPMNProfile_BPMNExpression666", self)

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
            if hasattr(old_value, "BPMNProfile_DataInput680"):
                opp_val = getattr(old_value, "BPMNProfile_DataInput680", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_DataInput680", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_DataInput680"):
                opp_val = getattr(value, "BPMNProfile_DataInput680", None)
                setattr(value, "BPMNProfile_DataInput680", self)

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
            if hasattr(old_value, "BPMNProfile_BPMNExpression663"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNExpression663", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNExpression663", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNExpression663"):
                opp_val = getattr(value, "BPMNProfile_BPMNExpression663", None)
                setattr(value, "BPMNProfile_BPMNExpression663", self)

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
            if hasattr(old_value, "BPMNProfile_DataOutput677"):
                opp_val = getattr(old_value, "BPMNProfile_DataOutput677", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_DataOutput677", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_DataOutput677"):
                opp_val = getattr(value, "BPMNProfile_DataOutput677", None)
                setattr(value, "BPMNProfile_DataOutput677", self)

    @property
    def BPMNProfile_MultiInstanceLoopCharacteristics688(self):
        return self.__BPMNProfile_MultiInstanceLoopCharacteristics688

    @BPMNProfile_MultiInstanceLoopCharacteristics688.setter
    def BPMNProfile_MultiInstanceLoopCharacteristics688(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MultiInstanceLoopCharacteristics__BPMNProfile_MultiInstanceLoopCharacteristics688", None)
        self.__BPMNProfile_MultiInstanceLoopCharacteristics688 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_ComplexBehaviorDefinition689"):
                    opp_val = getattr(item, "BPMNProfile_ComplexBehaviorDefinition689", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_ComplexBehaviorDefinition689", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_ComplexBehaviorDefinition689"):
                    opp_val = getattr(item, "BPMNProfile_ComplexBehaviorDefinition689", None)
                    
                    setattr(item, "BPMNProfile_ComplexBehaviorDefinition689", self)
                    

    def MultiinstanceLoopCharacteristicstarget(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MultiinstanceLoopCharacteristicstarget method
        pass

class BPMNProfile_StandardLoopCharacteristics(LoopCharacteristics):

    def __init__(self, loopMaximum: str, testBefore: str, BPMNProfile_StandardLoopCharacteristics: "BPMNProfile_LoopNode" = None, BPMNProfile_StandardLoopCharacteristics647: "BPMNProfile_BPMNExpression" = None):
        self.loopMaximum = loopMaximum
        self.testBefore = testBefore
        self.BPMNProfile_StandardLoopCharacteristics = BPMNProfile_StandardLoopCharacteristics
        self.BPMNProfile_StandardLoopCharacteristics647 = BPMNProfile_StandardLoopCharacteristics647
        
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
    def BPMNProfile_StandardLoopCharacteristics647(self):
        return self.__BPMNProfile_StandardLoopCharacteristics647

    @BPMNProfile_StandardLoopCharacteristics647.setter
    def BPMNProfile_StandardLoopCharacteristics647(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_StandardLoopCharacteristics__BPMNProfile_StandardLoopCharacteristics647", None)
        self.__BPMNProfile_StandardLoopCharacteristics647 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNExpression648"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNExpression648", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNExpression648", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNExpression648"):
                opp_val = getattr(value, "BPMNProfile_BPMNExpression648", None)
                setattr(value, "BPMNProfile_BPMNExpression648", self)

    def StandardLoopCharacteristicsloopCondition(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement StandardLoopCharacteristicsloopCondition method
        pass

    def StandardLoopCharacteristicstestBefore(self, diagnostics: str, context: str) -> bool:
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
            if hasattr(old_value, "BPMNProfile_BPMNExpression634"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNExpression634", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNExpression634", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNExpression634"):
                opp_val = getattr(value, "BPMNProfile_BPMNExpression634", None)
                setattr(value, "BPMNProfile_BPMNExpression634", self)

    def AdHocSubProcesscancelRemainingInstances(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AdHocSubProcesscancelRemainingInstances method
        pass

class BPMNProfile_CallBehaviorAction:

    pass
class ConversationNode:

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
                if hasattr(item, "BPMNProfile_ConversationNode607"):
                    opp_val = getattr(item, "BPMNProfile_ConversationNode607", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_ConversationNode607", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_ConversationNode607"):
                    opp_val = getattr(item, "BPMNProfile_ConversationNode607", None)
                    
                    setattr(item, "BPMNProfile_ConversationNode607", self)
                    

    def SubConversationconnectedelements(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SubConversationconnectedelements method
        pass

class HumanPerformer:

    pass
class BPMNProfile_CollaborationUse:

    pass
class BPMNProfile_CallConversation(ConversationNode):

    def __init__(self, BPMNProfile_CallConversation: "BPMNProfile_CollaborationUse" = None, BPMNProfile_CallConversation610: "BPMNProfile_BPMNCollaboration" = None, BPMNProfile_CallConversation613: set["BPMNProfile_ParticipantAssociation"] = None):
        self.BPMNProfile_CallConversation = BPMNProfile_CallConversation
        self.BPMNProfile_CallConversation610 = BPMNProfile_CallConversation610
        self.BPMNProfile_CallConversation613 = BPMNProfile_CallConversation613 if BPMNProfile_CallConversation613 is not None else set()
        
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
    def BPMNProfile_CallConversation613(self):
        return self.__BPMNProfile_CallConversation613

    @BPMNProfile_CallConversation613.setter
    def BPMNProfile_CallConversation613(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CallConversation__BPMNProfile_CallConversation613", None)
        self.__BPMNProfile_CallConversation613 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_ParticipantAssociation614"):
                    opp_val = getattr(item, "BPMNProfile_ParticipantAssociation614", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_ParticipantAssociation614", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_ParticipantAssociation614"):
                    opp_val = getattr(item, "BPMNProfile_ParticipantAssociation614", None)
                    
                    setattr(item, "BPMNProfile_ParticipantAssociation614", self)
                    

    @property
    def BPMNProfile_CallConversation610(self):
        return self.__BPMNProfile_CallConversation610

    @BPMNProfile_CallConversation610.setter
    def BPMNProfile_CallConversation610(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CallConversation__BPMNProfile_CallConversation610", None)
        self.__BPMNProfile_CallConversation610 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNCollaboration611"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNCollaboration611", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNCollaboration611", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNCollaboration611"):
                opp_val = getattr(value, "BPMNProfile_BPMNCollaboration611", None)
                setattr(value, "BPMNProfile_BPMNCollaboration611", self)

    def CallConversationparticipantAssociations(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement CallConversationparticipantAssociations method
        pass

    def CallConversationcalledCollaborationRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement CallConversationcalledCollaborationRef method
        pass

class BPMNCollaboration:

    pass
class BPMNProfile_GlobalConversation(BPMNCollaboration):

    def __init__(self):
        
    def GlobalConversationcontainedelements(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement GlobalConversationcontainedelements method
        pass

class BPMNProfile_PotentialOwner(HumanPerformer):

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

    def __init__(self, BPMNProfile_CallActivity: "BPMNProfile_CallBehaviorAction" = None, BPMNProfile_CallActivity622: "BPMNProfile_CallableElement" = None):
        self.BPMNProfile_CallActivity = BPMNProfile_CallActivity
        self.BPMNProfile_CallActivity622 = BPMNProfile_CallActivity622
        
    @property
    def BPMNProfile_CallActivity622(self):
        return self.__BPMNProfile_CallActivity622

    @BPMNProfile_CallActivity622.setter
    def BPMNProfile_CallActivity622(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CallActivity__BPMNProfile_CallActivity622", None)
        self.__BPMNProfile_CallActivity622 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CallableElement623"):
                opp_val = getattr(old_value, "BPMNProfile_CallableElement623", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_CallableElement623", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CallableElement623"):
                opp_val = getattr(value, "BPMNProfile_CallableElement623", None)
                setattr(value, "BPMNProfile_CallableElement623", self)

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

    def CallActivitycalledElementRefvalues(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement CallActivitycalledElementRefvalues method
        pass

class BPMNProfile_Task(BPMNActivity):

    pass
class BPMNProfile_OpaqueAction:

    pass
class Task:

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
            if hasattr(old_value, "BPMNProfile_OpaqueAction636"):
                opp_val = getattr(old_value, "BPMNProfile_OpaqueAction636", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_OpaqueAction636", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_OpaqueAction636"):
                opp_val = getattr(value, "BPMNProfile_OpaqueAction636", None)
                setattr(value, "BPMNProfile_OpaqueAction636", self)

    def ScriptTaskscript(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ScriptTaskscript method
        pass

    def ScriptTaskscriptFormat(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ScriptTaskscriptFormat method
        pass

class BPMNProfile_SendTask(Task):

    def __init__(self, implementation: str, BPMNProfile_SendTask: "BPMNProfile_BPMNMessage" = None, BPMNProfile_SendTask640: "BPMNProfile_CallOperationAction" = None, BPMNProfile_SendTask643: "BPMNProfile_BPMNOperation" = None):
        self.implementation = implementation
        self.BPMNProfile_SendTask = BPMNProfile_SendTask
        self.BPMNProfile_SendTask640 = BPMNProfile_SendTask640
        self.BPMNProfile_SendTask643 = BPMNProfile_SendTask643
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def BPMNProfile_SendTask640(self):
        return self.__BPMNProfile_SendTask640

    @BPMNProfile_SendTask640.setter
    def BPMNProfile_SendTask640(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_SendTask__BPMNProfile_SendTask640", None)
        self.__BPMNProfile_SendTask640 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CallOperationAction641"):
                opp_val = getattr(old_value, "BPMNProfile_CallOperationAction641", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_CallOperationAction641", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CallOperationAction641"):
                opp_val = getattr(value, "BPMNProfile_CallOperationAction641", None)
                setattr(value, "BPMNProfile_CallOperationAction641", self)

    @property
    def BPMNProfile_SendTask643(self):
        return self.__BPMNProfile_SendTask643

    @BPMNProfile_SendTask643.setter
    def BPMNProfile_SendTask643(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_SendTask__BPMNProfile_SendTask643", None)
        self.__BPMNProfile_SendTask643 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNOperation644"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNOperation644", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNOperation644", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNOperation644"):
                opp_val = getattr(value, "BPMNProfile_BPMNOperation644", None)
                setattr(value, "BPMNProfile_BPMNOperation644", self)

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
            if hasattr(old_value, "BPMNProfile_BPMNMessage638"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNMessage638", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNMessage638", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNMessage638"):
                opp_val = getattr(value, "BPMNProfile_BPMNMessage638", None)
                setattr(value, "BPMNProfile_BPMNMessage638", self)

    def SendTaskoperationRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SendTaskoperationRef method
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
            if hasattr(old_value, "BPMNProfile_OpaqueAction625"):
                opp_val = getattr(old_value, "BPMNProfile_OpaqueAction625", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_OpaqueAction625", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_OpaqueAction625"):
                opp_val = getattr(value, "BPMNProfile_OpaqueAction625", None)
                setattr(value, "BPMNProfile_OpaqueAction625", self)

    def BusinessRuleTaskimplementation(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement BusinessRuleTaskimplementation method
        pass

class BPMNProfile_ManualTask(Task):

    pass
class BPMNProfile_ReceiveTask(Task):

    def __init__(self, implementation: str, instantiate: str, BPMNProfile_ReceiveTask: "BPMNProfile_BPMNMessage" = None, BPMNProfile_ReceiveTask652: "BPMNProfile_AcceptEventAction" = None, BPMNProfile_ReceiveTask655: "BPMNProfile_BPMNOperation" = None):
        self.implementation = implementation
        self.instantiate = instantiate
        self.BPMNProfile_ReceiveTask = BPMNProfile_ReceiveTask
        self.BPMNProfile_ReceiveTask652 = BPMNProfile_ReceiveTask652
        self.BPMNProfile_ReceiveTask655 = BPMNProfile_ReceiveTask655
        
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
    def BPMNProfile_ReceiveTask652(self):
        return self.__BPMNProfile_ReceiveTask652

    @BPMNProfile_ReceiveTask652.setter
    def BPMNProfile_ReceiveTask652(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ReceiveTask__BPMNProfile_ReceiveTask652", None)
        self.__BPMNProfile_ReceiveTask652 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_AcceptEventAction653"):
                opp_val = getattr(old_value, "BPMNProfile_AcceptEventAction653", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_AcceptEventAction653", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_AcceptEventAction653"):
                opp_val = getattr(value, "BPMNProfile_AcceptEventAction653", None)
                setattr(value, "BPMNProfile_AcceptEventAction653", self)

    @property
    def BPMNProfile_ReceiveTask655(self):
        return self.__BPMNProfile_ReceiveTask655

    @BPMNProfile_ReceiveTask655.setter
    def BPMNProfile_ReceiveTask655(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ReceiveTask__BPMNProfile_ReceiveTask655", None)
        self.__BPMNProfile_ReceiveTask655 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNOperation656"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNOperation656", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNOperation656", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNOperation656"):
                opp_val = getattr(value, "BPMNProfile_BPMNOperation656", None)
                setattr(value, "BPMNProfile_BPMNOperation656", self)

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
            if hasattr(old_value, "BPMNProfile_BPMNMessage650"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNMessage650", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNMessage650", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNMessage650"):
                opp_val = getattr(value, "BPMNProfile_BPMNMessage650", None)
                setattr(value, "BPMNProfile_BPMNMessage650", self)

    def ReceiveTaskoperationRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ReceiveTaskoperationRef method
        pass

class BPMNProfile_ServiceTask(Task):

    def __init__(self, implementation: str, BPMNProfile_ServiceTask: "BPMNProfile_CallOperationAction" = None, BPMNProfile_ServiceTask660: "BPMNProfile_BPMNOperation" = None):
        self.implementation = implementation
        self.BPMNProfile_ServiceTask = BPMNProfile_ServiceTask
        self.BPMNProfile_ServiceTask660 = BPMNProfile_ServiceTask660
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def BPMNProfile_ServiceTask660(self):
        return self.__BPMNProfile_ServiceTask660

    @BPMNProfile_ServiceTask660.setter
    def BPMNProfile_ServiceTask660(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ServiceTask__BPMNProfile_ServiceTask660", None)
        self.__BPMNProfile_ServiceTask660 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNOperation661"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNOperation661", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNOperation661", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNOperation661"):
                opp_val = getattr(value, "BPMNProfile_BPMNOperation661", None)
                setattr(value, "BPMNProfile_BPMNOperation661", self)

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
            if hasattr(old_value, "BPMNProfile_CallOperationAction658"):
                opp_val = getattr(old_value, "BPMNProfile_CallOperationAction658", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_CallOperationAction658", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CallOperationAction658"):
                opp_val = getattr(value, "BPMNProfile_CallOperationAction658", None)
                setattr(value, "BPMNProfile_CallOperationAction658", self)

    def ServiceTaskinputSet(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ServiceTaskinputSet method
        pass

    def ServiceTaskoutputSet(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ServiceTaskoutputSet method
        pass

    def ServiceTaskoperationRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ServiceTaskoperationRef method
        pass

class BPMNProfile_UserTask(Task):

    def __init__(self, implementation: str, BPMNProfile_UserTask: "BPMNProfile_OpaqueAction" = None, BPMNProfile_UserTask597: set["BPMNProfile_Rendering"] = None):
        self.implementation = implementation
        self.BPMNProfile_UserTask = BPMNProfile_UserTask
        self.BPMNProfile_UserTask597 = BPMNProfile_UserTask597 if BPMNProfile_UserTask597 is not None else set()
        
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
    def BPMNProfile_UserTask597(self):
        return self.__BPMNProfile_UserTask597

    @BPMNProfile_UserTask597.setter
    def BPMNProfile_UserTask597(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_UserTask__BPMNProfile_UserTask597", None)
        self.__BPMNProfile_UserTask597 = value if value is not None else set()
        
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
                    

    def UserTaskimplementation(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement UserTaskimplementation method
        pass

    def UserTaskrenderings(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement UserTaskrenderings method
        pass

class BPMNProfile_Enumeration:

    pass
class BPMNProfile_SendObjectAction:

    pass
class BPMNProfile_FlowFinalNode:

    pass
class BPMNProfile_CallOperationAction:

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
class BPMNProfile_ChangeEvent:

    pass
class BPMNProfile_ObjectFlow:

    pass
class DataAssociation:

    pass
class BPMNProfile_InitialNode:

    pass
class BPMNProfile_AcceptEventAction:

    pass
class BPMNEvent:

    pass
class BPMNProfile_ThrowEvent(BPMNEvent):

    def __init__(self, BPMNProfile_ThrowEvent: "BPMNProfile_CallOperationAction" = None, BPMNProfile_ThrowEvent533: "BPMNProfile_FlowFinalNode" = None, BPMNProfile_ThrowEvent535: set["BPMNProfile_DataInputAssociation"] = None):
        self.BPMNProfile_ThrowEvent = BPMNProfile_ThrowEvent
        self.BPMNProfile_ThrowEvent533 = BPMNProfile_ThrowEvent533
        self.BPMNProfile_ThrowEvent535 = BPMNProfile_ThrowEvent535 if BPMNProfile_ThrowEvent535 is not None else set()
        
    @property
    def BPMNProfile_ThrowEvent535(self):
        return self.__BPMNProfile_ThrowEvent535

    @BPMNProfile_ThrowEvent535.setter
    def BPMNProfile_ThrowEvent535(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ThrowEvent__BPMNProfile_ThrowEvent535", None)
        self.__BPMNProfile_ThrowEvent535 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_DataInputAssociation536"):
                    opp_val = getattr(item, "BPMNProfile_DataInputAssociation536", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_DataInputAssociation536", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_DataInputAssociation536"):
                    opp_val = getattr(item, "BPMNProfile_DataInputAssociation536", None)
                    
                    setattr(item, "BPMNProfile_DataInputAssociation536", self)
                    

    @property
    def BPMNProfile_ThrowEvent533(self):
        return self.__BPMNProfile_ThrowEvent533

    @BPMNProfile_ThrowEvent533.setter
    def BPMNProfile_ThrowEvent533(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ThrowEvent__BPMNProfile_ThrowEvent533", None)
        self.__BPMNProfile_ThrowEvent533 = value
        
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

    def ThrowEventeventDefinitionRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ThrowEventeventDefinitionRefs method
        pass

class BPMNProfile_CatchEvent(BPMNEvent):

    def __init__(self, parallelMultiple: str, BPMNProfile_CatchEvent: "BPMNProfile_AcceptEventAction" = None, BPMNProfile_CatchEvent473: "BPMNProfile_InitialNode" = None, BPMNProfile_CatchEvent475: set["BPMNProfile_DataOutputAssociation"] = None):
        self.parallelMultiple = parallelMultiple
        self.BPMNProfile_CatchEvent = BPMNProfile_CatchEvent
        self.BPMNProfile_CatchEvent473 = BPMNProfile_CatchEvent473
        self.BPMNProfile_CatchEvent475 = BPMNProfile_CatchEvent475 if BPMNProfile_CatchEvent475 is not None else set()
        
    @property
    def parallelMultiple(self) -> str:
        return self.__parallelMultiple

    @parallelMultiple.setter
    def parallelMultiple(self, parallelMultiple: str):
        self.__parallelMultiple = parallelMultiple

    @property
    def BPMNProfile_CatchEvent475(self):
        return self.__BPMNProfile_CatchEvent475

    @BPMNProfile_CatchEvent475.setter
    def BPMNProfile_CatchEvent475(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CatchEvent__BPMNProfile_CatchEvent475", None)
        self.__BPMNProfile_CatchEvent475 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_DataOutputAssociation476"):
                    opp_val = getattr(item, "BPMNProfile_DataOutputAssociation476", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_DataOutputAssociation476", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_DataOutputAssociation476"):
                    opp_val = getattr(item, "BPMNProfile_DataOutputAssociation476", None)
                    
                    setattr(item, "BPMNProfile_DataOutputAssociation476", self)
                    

    @property
    def BPMNProfile_CatchEvent473(self):
        return self.__BPMNProfile_CatchEvent473

    @BPMNProfile_CatchEvent473.setter
    def BPMNProfile_CatchEvent473(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CatchEvent__BPMNProfile_CatchEvent473", None)
        self.__BPMNProfile_CatchEvent473 = value
        
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

    def catchEventeventDefinitionsRefs(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement catchEventeventDefinitionsRefs method
        pass

class CatchEvent:

    pass
class BPMNProfile_IntermediateCatchEvent(CatchEvent):

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

class BPMNProfile_DataOutputAssociation(DataAssociation):

    def __init__(self, BPMNProfile_DataOutputAssociation: "BPMNProfile_BPMNActivity" = None, BPMNProfile_DataOutputAssociation476: "BPMNProfile_CatchEvent" = None):
        self.BPMNProfile_DataOutputAssociation = BPMNProfile_DataOutputAssociation
        self.BPMNProfile_DataOutputAssociation476 = BPMNProfile_DataOutputAssociation476
        
    @property
    def BPMNProfile_DataOutputAssociation476(self):
        return self.__BPMNProfile_DataOutputAssociation476

    @BPMNProfile_DataOutputAssociation476.setter
    def BPMNProfile_DataOutputAssociation476(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataOutputAssociation__BPMNProfile_DataOutputAssociation476", None)
        self.__BPMNProfile_DataOutputAssociation476 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CatchEvent475"):
                opp_val = getattr(old_value, "BPMNProfile_CatchEvent475", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CatchEvent475"):
                opp_val = getattr(value, "BPMNProfile_CatchEvent475", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_CatchEvent475", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "BPMNProfile_BPMNActivity462"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNActivity462", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNActivity462"):
                opp_val = getattr(value, "BPMNProfile_BPMNActivity462", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNActivity462", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def dataOutputAssociationtarget(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement dataOutputAssociationtarget method
        pass

    def dataOutputAssociationsource(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement dataOutputAssociationsource method
        pass

class BPMNProfile_DataInputAssociation(DataAssociation):

    def __init__(self, BPMNProfile_DataInputAssociation: "BPMNProfile_BPMNActivity" = None, BPMNProfile_DataInputAssociation536: "BPMNProfile_ThrowEvent" = None):
        self.BPMNProfile_DataInputAssociation = BPMNProfile_DataInputAssociation
        self.BPMNProfile_DataInputAssociation536 = BPMNProfile_DataInputAssociation536
        
    @property
    def BPMNProfile_DataInputAssociation536(self):
        return self.__BPMNProfile_DataInputAssociation536

    @BPMNProfile_DataInputAssociation536.setter
    def BPMNProfile_DataInputAssociation536(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataInputAssociation__BPMNProfile_DataInputAssociation536", None)
        self.__BPMNProfile_DataInputAssociation536 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ThrowEvent535"):
                opp_val = getattr(old_value, "BPMNProfile_ThrowEvent535", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ThrowEvent535"):
                opp_val = getattr(value, "BPMNProfile_ThrowEvent535", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_ThrowEvent535", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

    def dataInputAssociationsource(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement dataInputAssociationsource method
        pass

    def dataInputAssociationtarget(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement dataInputAssociationtarget method
        pass

class BPMNProfile_BoundaryEvent(CatchEvent):

    def __init__(self, cancelActivity: str, BPMNProfile_BoundaryEvent: "BPMNProfile_BPMNActivity" = None, BPMNProfile_BoundaryEvent469: "BPMNProfile_BPMNActivity" = None):
        self.cancelActivity = cancelActivity
        self.BPMNProfile_BoundaryEvent = BPMNProfile_BoundaryEvent
        self.BPMNProfile_BoundaryEvent469 = BPMNProfile_BoundaryEvent469
        
    @property
    def cancelActivity(self) -> str:
        return self.__cancelActivity

    @cancelActivity.setter
    def cancelActivity(self, cancelActivity: str):
        self.__cancelActivity = cancelActivity

    @property
    def BPMNProfile_BoundaryEvent469(self):
        return self.__BPMNProfile_BoundaryEvent469

    @BPMNProfile_BoundaryEvent469.setter
    def BPMNProfile_BoundaryEvent469(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BoundaryEvent__BPMNProfile_BoundaryEvent469", None)
        self.__BPMNProfile_BoundaryEvent469 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNActivity470"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNActivity470", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNActivity470", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNActivity470"):
                opp_val = getattr(value, "BPMNProfile_BPMNActivity470", None)
                setattr(value, "BPMNProfile_BPMNActivity470", self)

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
            if hasattr(old_value, "BPMNProfile_BPMNActivity458"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNActivity458", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNActivity458"):
                opp_val = getattr(value, "BPMNProfile_BPMNActivity458", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNActivity458", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def boundaryEventattachedToRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement boundaryEventattachedToRef method
        pass

class BPMNProfile_Event:

    pass
class BPMNProfile_CallEvent:

    pass
class EventDefinition:

    pass
class BPMNProfile_SignalEventDefinition(EventDefinition):

    pass
class BPMNProfile_CancelEventDefinition(EventDefinition):

    pass
class BPMNProfile_TerminateEventDefinition(EventDefinition):

    pass
class BPMNProfile_ErrorEventDefinition(EventDefinition):

    pass
class BPMNProfile_TimerEventDefinition(EventDefinition):

    pass
class BPMNProfile_MessageEventDefinition(EventDefinition):

    pass
class BPMNProfile_LinkEventDefinition(EventDefinition):

    pass
class BPMNProfile_EscalationEventDefinition(EventDefinition):

    pass
class BPMNProfile_ConditionalEventDefinition(EventDefinition):

    def __init__(self, BPMNProfile_ConditionalEventDefinition: "BPMNProfile_ChangeEvent" = None, BPMNProfile_ConditionalEventDefinition548: "BPMNProfile_BPMNExpression" = None):
        self.BPMNProfile_ConditionalEventDefinition = BPMNProfile_ConditionalEventDefinition
        self.BPMNProfile_ConditionalEventDefinition548 = BPMNProfile_ConditionalEventDefinition548
        
    @property
    def BPMNProfile_ConditionalEventDefinition548(self):
        return self.__BPMNProfile_ConditionalEventDefinition548

    @BPMNProfile_ConditionalEventDefinition548.setter
    def BPMNProfile_ConditionalEventDefinition548(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ConditionalEventDefinition__BPMNProfile_ConditionalEventDefinition548", None)
        self.__BPMNProfile_ConditionalEventDefinition548 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNExpression549"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNExpression549", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNExpression549", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNExpression549"):
                opp_val = getattr(value, "BPMNProfile_BPMNExpression549", None)
                setattr(value, "BPMNProfile_BPMNExpression549", self)

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
            if hasattr(old_value, "BPMNProfile_ChangeEvent546"):
                opp_val = getattr(old_value, "BPMNProfile_ChangeEvent546", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ChangeEvent546", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ChangeEvent546"):
                opp_val = getattr(value, "BPMNProfile_ChangeEvent546", None)
                setattr(value, "BPMNProfile_ChangeEvent546", self)

    def conditionalEventDefinitioncondition(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement conditionalEventDefinitioncondition method
        pass

class BPMNProfile_CompensateEventDefinition(EventDefinition):

    def __init__(self, waitForCompletion: str, BPMNProfile_CompensateEventDefinition: "BPMNProfile_BPMNActivity" = None, BPMNProfile_CompensateEventDefinition443: "BPMNProfile_CallEvent" = None):
        self.waitForCompletion = waitForCompletion
        self.BPMNProfile_CompensateEventDefinition = BPMNProfile_CompensateEventDefinition
        self.BPMNProfile_CompensateEventDefinition443 = BPMNProfile_CompensateEventDefinition443
        
    @property
    def waitForCompletion(self) -> str:
        return self.__waitForCompletion

    @waitForCompletion.setter
    def waitForCompletion(self, waitForCompletion: str):
        self.__waitForCompletion = waitForCompletion

    @property
    def BPMNProfile_CompensateEventDefinition443(self):
        return self.__BPMNProfile_CompensateEventDefinition443

    @BPMNProfile_CompensateEventDefinition443.setter
    def BPMNProfile_CompensateEventDefinition443(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CompensateEventDefinition__BPMNProfile_CompensateEventDefinition443", None)
        self.__BPMNProfile_CompensateEventDefinition443 = value
        
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
class BPMNProfile_GlobalManualTask(GlobalTask):

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
                if hasattr(item, "BPMNProfile_Rendering603"):
                    opp_val = getattr(item, "BPMNProfile_Rendering603", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_Rendering603", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_Rendering603"):
                    opp_val = getattr(item, "BPMNProfile_Rendering603", None)
                    
                    setattr(item, "BPMNProfile_Rendering603", self)
                    

    def GlobalUserTaskimplementation(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement GlobalUserTaskimplementation method
        pass

    def GlobalUserTaskrenderings(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement GlobalUserTaskrenderings method
        pass

class BPMNProfile_GlobalScriptTask(GlobalTask):

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

    def GlobalScriptTaskscript(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement GlobalScriptTaskscript method
        pass

    def GlobalScriptTaskscriptFormat(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement GlobalScriptTaskscriptFormat method
        pass

class BPMNProfile_DataStoreNode:

    pass
class BPMNExpression:

    pass
class BPMNProfile_ResourceAssignmentExpression(BPMNExpression):

    def __init__(self, BPMNProfile_ResourceAssignmentExpression: "BPMNProfile_ResourceRole" = None, BPMNProfile_ResourceAssignmentExpression418: "BPMNProfile_BPMNExpression" = None):
        self.BPMNProfile_ResourceAssignmentExpression = BPMNProfile_ResourceAssignmentExpression
        self.BPMNProfile_ResourceAssignmentExpression418 = BPMNProfile_ResourceAssignmentExpression418
        
    @property
    def BPMNProfile_ResourceAssignmentExpression418(self):
        return self.__BPMNProfile_ResourceAssignmentExpression418

    @BPMNProfile_ResourceAssignmentExpression418.setter
    def BPMNProfile_ResourceAssignmentExpression418(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceAssignmentExpression__BPMNProfile_ResourceAssignmentExpression418", None)
        self.__BPMNProfile_ResourceAssignmentExpression418 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNExpression419"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNExpression419", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNExpression419", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNExpression419"):
                opp_val = getattr(value, "BPMNProfile_BPMNExpression419", None)
                setattr(value, "BPMNProfile_BPMNExpression419", self)

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
            if hasattr(old_value, "BPMNProfile_ResourceRole411"):
                opp_val = getattr(old_value, "BPMNProfile_ResourceRole411", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ResourceRole411", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ResourceRole411"):
                opp_val = getattr(value, "BPMNProfile_ResourceRole411", None)
                setattr(value, "BPMNProfile_ResourceRole411", self)

    def ResourceAssignmentExpressionexpression(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceAssignmentExpressionexpression method
        pass

class BPMNProfile_FormalExpression(BPMNExpression):

    def __init__(self, BPMNProfile_FormalExpression: "BPMNProfile_CorrelationPropertyRetrievalExpression" = None, BPMNProfile_FormalExpression384: "BPMNProfile_ItemDefinition" = None, BPMNProfile_FormalExpression399: "BPMNProfile_CorrelationPropertyBinding" = None, BPMNProfile_FormalExpression497: "BPMNProfile_DataAssociation" = None, BPMNProfile_FormalExpression627: "BPMNProfile_ComplexBehaviorDefinition" = None):
        self.BPMNProfile_FormalExpression = BPMNProfile_FormalExpression
        self.BPMNProfile_FormalExpression384 = BPMNProfile_FormalExpression384
        self.BPMNProfile_FormalExpression399 = BPMNProfile_FormalExpression399
        self.BPMNProfile_FormalExpression497 = BPMNProfile_FormalExpression497
        self.BPMNProfile_FormalExpression627 = BPMNProfile_FormalExpression627
        
    @property
    def BPMNProfile_FormalExpression384(self):
        return self.__BPMNProfile_FormalExpression384

    @BPMNProfile_FormalExpression384.setter
    def BPMNProfile_FormalExpression384(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_FormalExpression__BPMNProfile_FormalExpression384", None)
        self.__BPMNProfile_FormalExpression384 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ItemDefinition385"):
                opp_val = getattr(old_value, "BPMNProfile_ItemDefinition385", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ItemDefinition385", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ItemDefinition385"):
                opp_val = getattr(value, "BPMNProfile_ItemDefinition385", None)
                setattr(value, "BPMNProfile_ItemDefinition385", self)

    @property
    def BPMNProfile_FormalExpression399(self):
        return self.__BPMNProfile_FormalExpression399

    @BPMNProfile_FormalExpression399.setter
    def BPMNProfile_FormalExpression399(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_FormalExpression__BPMNProfile_FormalExpression399", None)
        self.__BPMNProfile_FormalExpression399 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CorrelationPropertyBinding398"):
                opp_val = getattr(old_value, "BPMNProfile_CorrelationPropertyBinding398", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_CorrelationPropertyBinding398", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CorrelationPropertyBinding398"):
                opp_val = getattr(value, "BPMNProfile_CorrelationPropertyBinding398", None)
                setattr(value, "BPMNProfile_CorrelationPropertyBinding398", self)

    @property
    def BPMNProfile_FormalExpression627(self):
        return self.__BPMNProfile_FormalExpression627

    @BPMNProfile_FormalExpression627.setter
    def BPMNProfile_FormalExpression627(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_FormalExpression__BPMNProfile_FormalExpression627", None)
        self.__BPMNProfile_FormalExpression627 = value
        
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
    def BPMNProfile_FormalExpression(self):
        return self.__BPMNProfile_FormalExpression

    @BPMNProfile_FormalExpression.setter
    def BPMNProfile_FormalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_FormalExpression__BPMNProfile_FormalExpression", None)
        self.__BPMNProfile_FormalExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CorrelationPropertyRetrievalExpression382"):
                opp_val = getattr(old_value, "BPMNProfile_CorrelationPropertyRetrievalExpression382", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_CorrelationPropertyRetrievalExpression382", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CorrelationPropertyRetrievalExpression382"):
                opp_val = getattr(value, "BPMNProfile_CorrelationPropertyRetrievalExpression382", None)
                setattr(value, "BPMNProfile_CorrelationPropertyRetrievalExpression382", self)

    @property
    def BPMNProfile_FormalExpression497(self):
        return self.__BPMNProfile_FormalExpression497

    @BPMNProfile_FormalExpression497.setter
    def BPMNProfile_FormalExpression497(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_FormalExpression__BPMNProfile_FormalExpression497", None)
        self.__BPMNProfile_FormalExpression497 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_DataAssociation496"):
                opp_val = getattr(old_value, "BPMNProfile_DataAssociation496", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_DataAssociation496", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_DataAssociation496"):
                opp_val = getattr(value, "BPMNProfile_DataAssociation496", None)
                setattr(value, "BPMNProfile_DataAssociation496", self)

    def FormalExpressionevaluatesToTypeRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement FormalExpressionevaluatesToTypeRef method
        pass

class BPMNProfile_InformationFlow:

    pass
class BPMNProfile_InstanceSpecification:

    pass
class BPMNProfile_MultiplicityElement:

    pass
class BPMNProfile_InteractionNode(ABC):

    pass
class InteractionNode:

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

class BPMNProfile_Resource(ItemDefinition):

    def __init__(self, BPMNProfile_Resource: "BPMNProfile_ResourceRole" = None, BPMNProfile_Resource421: set["BPMNProfile_ResourceParameter"] = None):
        self.BPMNProfile_Resource = BPMNProfile_Resource
        self.BPMNProfile_Resource421 = BPMNProfile_Resource421 if BPMNProfile_Resource421 is not None else set()
        
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
            if hasattr(old_value, "BPMNProfile_ResourceRole413"):
                opp_val = getattr(old_value, "BPMNProfile_ResourceRole413", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ResourceRole413", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ResourceRole413"):
                opp_val = getattr(value, "BPMNProfile_ResourceRole413", None)
                setattr(value, "BPMNProfile_ResourceRole413", self)

    @property
    def BPMNProfile_Resource421(self):
        return self.__BPMNProfile_Resource421

    @BPMNProfile_Resource421.setter
    def BPMNProfile_Resource421(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Resource__BPMNProfile_Resource421", None)
        self.__BPMNProfile_Resource421 = value if value is not None else set()
        
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
                    

    def ResourceresourceParameters(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ResourceresourceParameters method
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

    def BPMNSignalstructureRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BPMNSignalstructureRef method
        pass

class BPMNProfile_Error(ItemDefinition):

    def __init__(self, errorCode: str, BPMNProfile_Error: "BPMNProfile_BPMNOperation" = None, BPMNProfile_Error558: "BPMNProfile_ErrorEventDefinition" = None):
        self.errorCode = errorCode
        self.BPMNProfile_Error = BPMNProfile_Error
        self.BPMNProfile_Error558 = BPMNProfile_Error558
        
    @property
    def errorCode(self) -> str:
        return self.__errorCode

    @errorCode.setter
    def errorCode(self, errorCode: str):
        self.__errorCode = errorCode

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
            if hasattr(old_value, "BPMNProfile_BPMNOperation254"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNOperation254", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNOperation254"):
                opp_val = getattr(value, "BPMNProfile_BPMNOperation254", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNOperation254", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_Error558(self):
        return self.__BPMNProfile_Error558

    @BPMNProfile_Error558.setter
    def BPMNProfile_Error558(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Error__BPMNProfile_Error558", None)
        self.__BPMNProfile_Error558 = value
        
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

class BPMNProfile_Collaboration:

    pass
class BPMNProfile_BPMNMessage(ItemDefinition):

    def __init__(self, BPMNProfile_BPMNMessage: "BPMNProfile_BPMNOperation" = None, BPMNProfile_BPMNMessage256: "BPMNProfile_ItemDefinition" = None, BPMNProfile_BPMNMessage252: "BPMNProfile_BPMNOperation" = None, BPMNProfile_BPMNMessage349: "BPMNProfile_MessageFlow" = None, BPMNProfile_BPMNMessage380: "BPMNProfile_CorrelationPropertyRetrievalExpression" = None, BPMNProfile_BPMNMessage538: "BPMNProfile_MessageEventDefinition" = None, BPMNProfile_BPMNMessage638: "BPMNProfile_SendTask" = None, BPMNProfile_BPMNMessage650: "BPMNProfile_ReceiveTask" = None):
        self.BPMNProfile_BPMNMessage = BPMNProfile_BPMNMessage
        self.BPMNProfile_BPMNMessage256 = BPMNProfile_BPMNMessage256
        self.BPMNProfile_BPMNMessage252 = BPMNProfile_BPMNMessage252
        self.BPMNProfile_BPMNMessage349 = BPMNProfile_BPMNMessage349
        self.BPMNProfile_BPMNMessage380 = BPMNProfile_BPMNMessage380
        self.BPMNProfile_BPMNMessage538 = BPMNProfile_BPMNMessage538
        self.BPMNProfile_BPMNMessage638 = BPMNProfile_BPMNMessage638
        self.BPMNProfile_BPMNMessage650 = BPMNProfile_BPMNMessage650
        
    @property
    def BPMNProfile_BPMNMessage252(self):
        return self.__BPMNProfile_BPMNMessage252

    @BPMNProfile_BPMNMessage252.setter
    def BPMNProfile_BPMNMessage252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNMessage__BPMNProfile_BPMNMessage252", None)
        self.__BPMNProfile_BPMNMessage252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNOperation251"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNOperation251", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNOperation251", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNOperation251"):
                opp_val = getattr(value, "BPMNProfile_BPMNOperation251", None)
                setattr(value, "BPMNProfile_BPMNOperation251", self)

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
            if hasattr(old_value, "BPMNProfile_BPMNOperation249"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNOperation249", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNOperation249", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNOperation249"):
                opp_val = getattr(value, "BPMNProfile_BPMNOperation249", None)
                setattr(value, "BPMNProfile_BPMNOperation249", self)

    @property
    def BPMNProfile_BPMNMessage538(self):
        return self.__BPMNProfile_BPMNMessage538

    @BPMNProfile_BPMNMessage538.setter
    def BPMNProfile_BPMNMessage538(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNMessage__BPMNProfile_BPMNMessage538", None)
        self.__BPMNProfile_BPMNMessage538 = value
        
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
    def BPMNProfile_BPMNMessage650(self):
        return self.__BPMNProfile_BPMNMessage650

    @BPMNProfile_BPMNMessage650.setter
    def BPMNProfile_BPMNMessage650(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNMessage__BPMNProfile_BPMNMessage650", None)
        self.__BPMNProfile_BPMNMessage650 = value
        
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
    def BPMNProfile_BPMNMessage349(self):
        return self.__BPMNProfile_BPMNMessage349

    @BPMNProfile_BPMNMessage349.setter
    def BPMNProfile_BPMNMessage349(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNMessage__BPMNProfile_BPMNMessage349", None)
        self.__BPMNProfile_BPMNMessage349 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_MessageFlow348"):
                opp_val = getattr(old_value, "BPMNProfile_MessageFlow348", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_MessageFlow348", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_MessageFlow348"):
                opp_val = getattr(value, "BPMNProfile_MessageFlow348", None)
                setattr(value, "BPMNProfile_MessageFlow348", self)

    @property
    def BPMNProfile_BPMNMessage638(self):
        return self.__BPMNProfile_BPMNMessage638

    @BPMNProfile_BPMNMessage638.setter
    def BPMNProfile_BPMNMessage638(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNMessage__BPMNProfile_BPMNMessage638", None)
        self.__BPMNProfile_BPMNMessage638 = value
        
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

    @property
    def BPMNProfile_BPMNMessage380(self):
        return self.__BPMNProfile_BPMNMessage380

    @BPMNProfile_BPMNMessage380.setter
    def BPMNProfile_BPMNMessage380(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNMessage__BPMNProfile_BPMNMessage380", None)
        self.__BPMNProfile_BPMNMessage380 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CorrelationPropertyRetrievalExpression379"):
                opp_val = getattr(old_value, "BPMNProfile_CorrelationPropertyRetrievalExpression379", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_CorrelationPropertyRetrievalExpression379", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CorrelationPropertyRetrievalExpression379"):
                opp_val = getattr(value, "BPMNProfile_CorrelationPropertyRetrievalExpression379", None)
                setattr(value, "BPMNProfile_CorrelationPropertyRetrievalExpression379", self)

    @property
    def BPMNProfile_BPMNMessage256(self):
        return self.__BPMNProfile_BPMNMessage256

    @BPMNProfile_BPMNMessage256.setter
    def BPMNProfile_BPMNMessage256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNMessage__BPMNProfile_BPMNMessage256", None)
        self.__BPMNProfile_BPMNMessage256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ItemDefinition257"):
                opp_val = getattr(old_value, "BPMNProfile_ItemDefinition257", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ItemDefinition257", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ItemDefinition257"):
                opp_val = getattr(value, "BPMNProfile_ItemDefinition257", None)
                setattr(value, "BPMNProfile_ItemDefinition257", self)

    def MessageitemRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MessageitemRef method
        pass

class BPMNProfile_Operation:

    pass
class BPMNProfile_Interface:

    pass
class BPMNProfile_OutputPin:

    pass
class BPMNProfile_ParameterSet:

    pass
class BPMNProfile_InputPin:

    pass
class BPMNProfile_State:

    pass
class BPMNProfile_TypedElement:

    pass
class BPMNProfile_ActivityParameterNode:

    pass
class BPMNProfile_Parameter:

    pass
class RootElement:

    pass
class BPMNProfile_DataStore(RootElement):

    def __init__(self, capacity: str, isUnlimited: str, BPMNProfile_DataStore: "BPMNProfile_Class" = None, BPMNProfile_DataStore588: "BPMNProfile_ItemDefinition" = None, BPMNProfile_DataStore591: "BPMNProfile_DataStoreReference" = None):
        self.capacity = capacity
        self.isUnlimited = isUnlimited
        self.BPMNProfile_DataStore = BPMNProfile_DataStore
        self.BPMNProfile_DataStore588 = BPMNProfile_DataStore588
        self.BPMNProfile_DataStore591 = BPMNProfile_DataStore591
        
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
            if hasattr(old_value, "BPMNProfile_Class586"):
                opp_val = getattr(old_value, "BPMNProfile_Class586", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Class586", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Class586"):
                opp_val = getattr(value, "BPMNProfile_Class586", None)
                setattr(value, "BPMNProfile_Class586", self)

    @property
    def BPMNProfile_DataStore588(self):
        return self.__BPMNProfile_DataStore588

    @BPMNProfile_DataStore588.setter
    def BPMNProfile_DataStore588(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataStore__BPMNProfile_DataStore588", None)
        self.__BPMNProfile_DataStore588 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ItemDefinition589"):
                opp_val = getattr(old_value, "BPMNProfile_ItemDefinition589", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ItemDefinition589", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ItemDefinition589"):
                opp_val = getattr(value, "BPMNProfile_ItemDefinition589", None)
                setattr(value, "BPMNProfile_ItemDefinition589", self)

    @property
    def BPMNProfile_DataStore591(self):
        return self.__BPMNProfile_DataStore591

    @BPMNProfile_DataStore591.setter
    def BPMNProfile_DataStore591(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataStore__BPMNProfile_DataStore591", None)
        self.__BPMNProfile_DataStore591 = value
        
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

    def __init__(self, itemKind: str, isCollection: str, BPMNProfile_ItemDefinition: "BPMNProfile_ItemAwareElement" = None, BPMNProfile_ItemDefinition193: "BPMNProfile_Class" = None, BPMNProfile_ItemDefinition196: "BPMNProfile_Element" = None, BPMNProfile_ItemDefinition199: "BPMNProfile_Import" = None, BPMNProfile_ItemDefinition257: "BPMNProfile_BPMNMessage" = None, BPMNProfile_ItemDefinition372: "BPMNProfile_CorrelationProperty" = None, BPMNProfile_ItemDefinition385: "BPMNProfile_FormalExpression" = None, BPMNProfile_ItemDefinition427: "BPMNProfile_ResourceParameter" = None, BPMNProfile_ItemDefinition589: "BPMNProfile_DataStore" = None):
        self.itemKind = itemKind
        self.isCollection = isCollection
        self.BPMNProfile_ItemDefinition = BPMNProfile_ItemDefinition
        self.BPMNProfile_ItemDefinition193 = BPMNProfile_ItemDefinition193
        self.BPMNProfile_ItemDefinition196 = BPMNProfile_ItemDefinition196
        self.BPMNProfile_ItemDefinition199 = BPMNProfile_ItemDefinition199
        self.BPMNProfile_ItemDefinition257 = BPMNProfile_ItemDefinition257
        self.BPMNProfile_ItemDefinition372 = BPMNProfile_ItemDefinition372
        self.BPMNProfile_ItemDefinition385 = BPMNProfile_ItemDefinition385
        self.BPMNProfile_ItemDefinition427 = BPMNProfile_ItemDefinition427
        self.BPMNProfile_ItemDefinition589 = BPMNProfile_ItemDefinition589
        
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
    def BPMNProfile_ItemDefinition199(self):
        return self.__BPMNProfile_ItemDefinition199

    @BPMNProfile_ItemDefinition199.setter
    def BPMNProfile_ItemDefinition199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemDefinition__BPMNProfile_ItemDefinition199", None)
        self.__BPMNProfile_ItemDefinition199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Import200"):
                opp_val = getattr(old_value, "BPMNProfile_Import200", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Import200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Import200"):
                opp_val = getattr(value, "BPMNProfile_Import200", None)
                setattr(value, "BPMNProfile_Import200", self)

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
            if hasattr(old_value, "BPMNProfile_ItemAwareElement189"):
                opp_val = getattr(old_value, "BPMNProfile_ItemAwareElement189", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ItemAwareElement189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ItemAwareElement189"):
                opp_val = getattr(value, "BPMNProfile_ItemAwareElement189", None)
                setattr(value, "BPMNProfile_ItemAwareElement189", self)

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
            if hasattr(old_value, "BPMNProfile_Class194"):
                opp_val = getattr(old_value, "BPMNProfile_Class194", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Class194", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Class194"):
                opp_val = getattr(value, "BPMNProfile_Class194", None)
                setattr(value, "BPMNProfile_Class194", self)

    @property
    def BPMNProfile_ItemDefinition589(self):
        return self.__BPMNProfile_ItemDefinition589

    @BPMNProfile_ItemDefinition589.setter
    def BPMNProfile_ItemDefinition589(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemDefinition__BPMNProfile_ItemDefinition589", None)
        self.__BPMNProfile_ItemDefinition589 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_DataStore588"):
                opp_val = getattr(old_value, "BPMNProfile_DataStore588", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_DataStore588", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_DataStore588"):
                opp_val = getattr(value, "BPMNProfile_DataStore588", None)
                setattr(value, "BPMNProfile_DataStore588", self)

    @property
    def BPMNProfile_ItemDefinition257(self):
        return self.__BPMNProfile_ItemDefinition257

    @BPMNProfile_ItemDefinition257.setter
    def BPMNProfile_ItemDefinition257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemDefinition__BPMNProfile_ItemDefinition257", None)
        self.__BPMNProfile_ItemDefinition257 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNMessage256"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNMessage256", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNMessage256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNMessage256"):
                opp_val = getattr(value, "BPMNProfile_BPMNMessage256", None)
                setattr(value, "BPMNProfile_BPMNMessage256", self)

    @property
    def BPMNProfile_ItemDefinition427(self):
        return self.__BPMNProfile_ItemDefinition427

    @BPMNProfile_ItemDefinition427.setter
    def BPMNProfile_ItemDefinition427(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemDefinition__BPMNProfile_ItemDefinition427", None)
        self.__BPMNProfile_ItemDefinition427 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ResourceParameter426"):
                opp_val = getattr(old_value, "BPMNProfile_ResourceParameter426", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ResourceParameter426", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ResourceParameter426"):
                opp_val = getattr(value, "BPMNProfile_ResourceParameter426", None)
                setattr(value, "BPMNProfile_ResourceParameter426", self)

    @property
    def BPMNProfile_ItemDefinition385(self):
        return self.__BPMNProfile_ItemDefinition385

    @BPMNProfile_ItemDefinition385.setter
    def BPMNProfile_ItemDefinition385(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemDefinition__BPMNProfile_ItemDefinition385", None)
        self.__BPMNProfile_ItemDefinition385 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_FormalExpression384"):
                opp_val = getattr(old_value, "BPMNProfile_FormalExpression384", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_FormalExpression384", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_FormalExpression384"):
                opp_val = getattr(value, "BPMNProfile_FormalExpression384", None)
                setattr(value, "BPMNProfile_FormalExpression384", self)

    @property
    def BPMNProfile_ItemDefinition196(self):
        return self.__BPMNProfile_ItemDefinition196

    @BPMNProfile_ItemDefinition196.setter
    def BPMNProfile_ItemDefinition196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemDefinition__BPMNProfile_ItemDefinition196", None)
        self.__BPMNProfile_ItemDefinition196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Element197"):
                opp_val = getattr(old_value, "BPMNProfile_Element197", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Element197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Element197"):
                opp_val = getattr(value, "BPMNProfile_Element197", None)
                setattr(value, "BPMNProfile_Element197", self)

    @property
    def BPMNProfile_ItemDefinition372(self):
        return self.__BPMNProfile_ItemDefinition372

    @BPMNProfile_ItemDefinition372.setter
    def BPMNProfile_ItemDefinition372(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemDefinition__BPMNProfile_ItemDefinition372", None)
        self.__BPMNProfile_ItemDefinition372 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CorrelationProperty371"):
                opp_val = getattr(old_value, "BPMNProfile_CorrelationProperty371", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_CorrelationProperty371", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CorrelationProperty371"):
                opp_val = getattr(value, "BPMNProfile_CorrelationProperty371", None)
                setattr(value, "BPMNProfile_CorrelationProperty371", self)

    def ItemDefinitionstructureRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ItemDefinitionstructureRef method
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
                if hasattr(item, "Participant329"):
                    opp_val = getattr(item, "Participant329", None)
                    
                    if opp_val == self:
                        setattr(item, "Participant329", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Participant329"):
                    opp_val = getattr(item, "Participant329", None)
                    
                    setattr(item, "Participant329", self)
                    

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
            if hasattr(old_value, "participantRef304"):
                opp_val = getattr(old_value, "participantRef304", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "participantRef304"):
                opp_val = getattr(value, "participantRef304", None)
                if opp_val is None:
                    setattr(value, "participantRef304", set([self]))
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
            if hasattr(old_value, "BPMNProfile_Class327"):
                opp_val = getattr(old_value, "BPMNProfile_Class327", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Class327", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Class327"):
                opp_val = getattr(value, "BPMNProfile_Class327", None)
                setattr(value, "BPMNProfile_Class327", self)

    def PartnerRoleparticipantRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement PartnerRoleparticipantRef method
        pass

class BPMNProfile_PartnerEntity(RootElement):

    def __init__(self, PartnerEntity: "BPMNProfile_Participant" = None, BPMNProfile_PartnerEntity: "BPMNProfile_InstanceSpecification" = None, partnerEntityRef: set["BPMNProfile_Participant"] = None):
        self.PartnerEntity = PartnerEntity
        self.BPMNProfile_PartnerEntity = BPMNProfile_PartnerEntity
        self.partnerEntityRef = partnerEntityRef if partnerEntityRef is not None else set()
        
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

class BPMNProfile_Category(RootElement):

    pass
class BPMNProfile_CallableElement(RootElement):

    def __init__(self, BPMNProfile_CallableElement: "BPMNProfile_Behavior" = None, BPMNProfile_CallableElement156: "BPMNProfile_InputOutputSpecification" = None, BPMNProfile_CallableElement158: set["BPMNProfile_BPMNInterface"] = None, BPMNProfile_CallableElement160: set["BPMNProfile_InputOutputBinding"] = None, BPMNProfile_CallableElement242: "BPMNProfile_BPMNInterface" = None, BPMNProfile_CallableElement623: "BPMNProfile_CallActivity" = None):
        self.BPMNProfile_CallableElement = BPMNProfile_CallableElement
        self.BPMNProfile_CallableElement156 = BPMNProfile_CallableElement156
        self.BPMNProfile_CallableElement158 = BPMNProfile_CallableElement158 if BPMNProfile_CallableElement158 is not None else set()
        self.BPMNProfile_CallableElement160 = BPMNProfile_CallableElement160 if BPMNProfile_CallableElement160 is not None else set()
        self.BPMNProfile_CallableElement242 = BPMNProfile_CallableElement242
        self.BPMNProfile_CallableElement623 = BPMNProfile_CallableElement623
        
    @property
    def BPMNProfile_CallableElement156(self):
        return self.__BPMNProfile_CallableElement156

    @BPMNProfile_CallableElement156.setter
    def BPMNProfile_CallableElement156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CallableElement__BPMNProfile_CallableElement156", None)
        self.__BPMNProfile_CallableElement156 = value
        
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
    def BPMNProfile_CallableElement158(self):
        return self.__BPMNProfile_CallableElement158

    @BPMNProfile_CallableElement158.setter
    def BPMNProfile_CallableElement158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CallableElement__BPMNProfile_CallableElement158", None)
        self.__BPMNProfile_CallableElement158 = value if value is not None else set()
        
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
    def BPMNProfile_CallableElement160(self):
        return self.__BPMNProfile_CallableElement160

    @BPMNProfile_CallableElement160.setter
    def BPMNProfile_CallableElement160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CallableElement__BPMNProfile_CallableElement160", None)
        self.__BPMNProfile_CallableElement160 = value if value is not None else set()
        
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
                    

    @property
    def BPMNProfile_CallableElement623(self):
        return self.__BPMNProfile_CallableElement623

    @BPMNProfile_CallableElement623.setter
    def BPMNProfile_CallableElement623(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CallableElement__BPMNProfile_CallableElement623", None)
        self.__BPMNProfile_CallableElement623 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CallActivity622"):
                opp_val = getattr(old_value, "BPMNProfile_CallActivity622", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_CallActivity622", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CallActivity622"):
                opp_val = getattr(value, "BPMNProfile_CallActivity622", None)
                setattr(value, "BPMNProfile_CallActivity622", self)

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
    def BPMNProfile_CallableElement242(self):
        return self.__BPMNProfile_CallableElement242

    @BPMNProfile_CallableElement242.setter
    def BPMNProfile_CallableElement242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_CallableElement__BPMNProfile_CallableElement242", None)
        self.__BPMNProfile_CallableElement242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNInterface241"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNInterface241", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNInterface241"):
                opp_val = getattr(value, "BPMNProfile_BPMNInterface241", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNInterface241", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def CallableEelementsupportedInterfaceRefs(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement CallableEelementsupportedInterfaceRefs method
        pass

    def CallableElementresources(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement CallableElementresources method
        pass

class ItemAwareElement:

    pass
class BPMNProfile_BPMNProperty(ItemAwareElement):

    def __init__(self, BPMNProfile_BPMNProperty: "BPMNProfile_BPMNProcess" = None, BPMNProfile_BPMNProperty404: "BPMNProfile_DataStoreNode" = None, BPMNProfile_BPMNProperty406: "BPMNProfile_Property" = None, BPMNProfile_BPMNProperty453: "BPMNProfile_BPMNActivity" = None, BPMNProfile_BPMNProperty484: "BPMNProfile_BPMNEvent" = None):
        self.BPMNProfile_BPMNProperty = BPMNProfile_BPMNProperty
        self.BPMNProfile_BPMNProperty404 = BPMNProfile_BPMNProperty404
        self.BPMNProfile_BPMNProperty406 = BPMNProfile_BPMNProperty406
        self.BPMNProfile_BPMNProperty453 = BPMNProfile_BPMNProperty453
        self.BPMNProfile_BPMNProperty484 = BPMNProfile_BPMNProperty484
        
    @property
    def BPMNProfile_BPMNProperty404(self):
        return self.__BPMNProfile_BPMNProperty404

    @BPMNProfile_BPMNProperty404.setter
    def BPMNProfile_BPMNProperty404(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProperty__BPMNProfile_BPMNProperty404", None)
        self.__BPMNProfile_BPMNProperty404 = value
        
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
    def BPMNProfile_BPMNProperty453(self):
        return self.__BPMNProfile_BPMNProperty453

    @BPMNProfile_BPMNProperty453.setter
    def BPMNProfile_BPMNProperty453(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProperty__BPMNProfile_BPMNProperty453", None)
        self.__BPMNProfile_BPMNProperty453 = value
        
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
            if hasattr(old_value, "BPMNProfile_BPMNProcess152"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNProcess152", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNProcess152"):
                opp_val = getattr(value, "BPMNProfile_BPMNProcess152", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNProcess152", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_BPMNProperty484(self):
        return self.__BPMNProfile_BPMNProperty484

    @BPMNProfile_BPMNProperty484.setter
    def BPMNProfile_BPMNProperty484(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProperty__BPMNProfile_BPMNProperty484", None)
        self.__BPMNProfile_BPMNProperty484 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNEvent483"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNEvent483", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNEvent483"):
                opp_val = getattr(value, "BPMNProfile_BPMNEvent483", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNEvent483", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_BPMNProperty406(self):
        return self.__BPMNProfile_BPMNProperty406

    @BPMNProfile_BPMNProperty406.setter
    def BPMNProfile_BPMNProperty406(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProperty__BPMNProfile_BPMNProperty406", None)
        self.__BPMNProfile_BPMNProperty406 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Property407"):
                opp_val = getattr(old_value, "BPMNProfile_Property407", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Property407", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Property407"):
                opp_val = getattr(value, "BPMNProfile_Property407", None)
                setattr(value, "BPMNProfile_Property407", self)

    def Propertynotation(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement Propertynotation method
        pass

    def BPMNPropertyapply(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement BPMNPropertyapply method
        pass

class BPMNProfile_DataOutput(ItemAwareElement):

    def __init__(self, isCollection: str, BPMNProfile_DataOutput: "BPMNProfile_InputOutputSpecification" = None, BPMNProfile_DataOutput214: "BPMNProfile_ActivityParameterNode" = None, dataOutputRefs: set["BPMNProfile_OutputSet"] = None, BPMNProfile_DataOutput218: set["BPMNProfile_OutputSet"] = None, BPMNProfile_DataOutput221: set["BPMNProfile_OutputSet"] = None, BPMNProfile_DataOutput228: "BPMNProfile_OutputSet" = None, BPMNProfile_DataOutput231: "BPMNProfile_OutputSet" = None, DataOutput: "BPMNProfile_OutputSet" = None, BPMNProfile_DataOutput209: "BPMNProfile_OutputPin" = None, BPMNProfile_DataOutput211: "BPMNProfile_Parameter" = None, BPMNProfile_DataOutput677: "BPMNProfile_MultiInstanceLoopCharacteristics" = None):
        self.isCollection = isCollection
        self.BPMNProfile_DataOutput = BPMNProfile_DataOutput
        self.BPMNProfile_DataOutput214 = BPMNProfile_DataOutput214
        self.dataOutputRefs = dataOutputRefs if dataOutputRefs is not None else set()
        self.BPMNProfile_DataOutput218 = BPMNProfile_DataOutput218 if BPMNProfile_DataOutput218 is not None else set()
        self.BPMNProfile_DataOutput221 = BPMNProfile_DataOutput221 if BPMNProfile_DataOutput221 is not None else set()
        self.BPMNProfile_DataOutput228 = BPMNProfile_DataOutput228
        self.BPMNProfile_DataOutput231 = BPMNProfile_DataOutput231
        self.DataOutput = DataOutput
        self.BPMNProfile_DataOutput209 = BPMNProfile_DataOutput209
        self.BPMNProfile_DataOutput211 = BPMNProfile_DataOutput211
        self.BPMNProfile_DataOutput677 = BPMNProfile_DataOutput677
        
    @property
    def isCollection(self) -> str:
        return self.__isCollection

    @isCollection.setter
    def isCollection(self, isCollection: str):
        self.__isCollection = isCollection

    @property
    def BPMNProfile_DataOutput218(self):
        return self.__BPMNProfile_DataOutput218

    @BPMNProfile_DataOutput218.setter
    def BPMNProfile_DataOutput218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataOutput__BPMNProfile_DataOutput218", None)
        self.__BPMNProfile_DataOutput218 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_OutputSet219"):
                    opp_val = getattr(item, "BPMNProfile_OutputSet219", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_OutputSet219", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_OutputSet219"):
                    opp_val = getattr(item, "BPMNProfile_OutputSet219", None)
                    
                    setattr(item, "BPMNProfile_OutputSet219", self)
                    

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
            if hasattr(old_value, "BPMNProfile_InputOutputSpecification169"):
                opp_val = getattr(old_value, "BPMNProfile_InputOutputSpecification169", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_InputOutputSpecification169"):
                opp_val = getattr(value, "BPMNProfile_InputOutputSpecification169", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_InputOutputSpecification169", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def BPMNProfile_DataOutput209(self):
        return self.__BPMNProfile_DataOutput209

    @BPMNProfile_DataOutput209.setter
    def BPMNProfile_DataOutput209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataOutput__BPMNProfile_DataOutput209", None)
        self.__BPMNProfile_DataOutput209 = value
        
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
    def BPMNProfile_DataOutput221(self):
        return self.__BPMNProfile_DataOutput221

    @BPMNProfile_DataOutput221.setter
    def BPMNProfile_DataOutput221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataOutput__BPMNProfile_DataOutput221", None)
        self.__BPMNProfile_DataOutput221 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_OutputSet222"):
                    opp_val = getattr(item, "BPMNProfile_OutputSet222", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_OutputSet222", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_OutputSet222"):
                    opp_val = getattr(item, "BPMNProfile_OutputSet222", None)
                    
                    setattr(item, "BPMNProfile_OutputSet222", self)
                    

    @property
    def BPMNProfile_DataOutput211(self):
        return self.__BPMNProfile_DataOutput211

    @BPMNProfile_DataOutput211.setter
    def BPMNProfile_DataOutput211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataOutput__BPMNProfile_DataOutput211", None)
        self.__BPMNProfile_DataOutput211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Parameter212"):
                opp_val = getattr(old_value, "BPMNProfile_Parameter212", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Parameter212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Parameter212"):
                opp_val = getattr(value, "BPMNProfile_Parameter212", None)
                setattr(value, "BPMNProfile_Parameter212", self)

    @property
    def BPMNProfile_DataOutput231(self):
        return self.__BPMNProfile_DataOutput231

    @BPMNProfile_DataOutput231.setter
    def BPMNProfile_DataOutput231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataOutput__BPMNProfile_DataOutput231", None)
        self.__BPMNProfile_DataOutput231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_OutputSet230"):
                opp_val = getattr(old_value, "BPMNProfile_OutputSet230", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_OutputSet230"):
                opp_val = getattr(value, "BPMNProfile_OutputSet230", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_OutputSet230", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_DataOutput228(self):
        return self.__BPMNProfile_DataOutput228

    @BPMNProfile_DataOutput228.setter
    def BPMNProfile_DataOutput228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataOutput__BPMNProfile_DataOutput228", None)
        self.__BPMNProfile_DataOutput228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_OutputSet227"):
                opp_val = getattr(old_value, "BPMNProfile_OutputSet227", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_OutputSet227"):
                opp_val = getattr(value, "BPMNProfile_OutputSet227", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_OutputSet227", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_DataOutput214(self):
        return self.__BPMNProfile_DataOutput214

    @BPMNProfile_DataOutput214.setter
    def BPMNProfile_DataOutput214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataOutput__BPMNProfile_DataOutput214", None)
        self.__BPMNProfile_DataOutput214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ActivityParameterNode215"):
                opp_val = getattr(old_value, "BPMNProfile_ActivityParameterNode215", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ActivityParameterNode215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ActivityParameterNode215"):
                opp_val = getattr(value, "BPMNProfile_ActivityParameterNode215", None)
                setattr(value, "BPMNProfile_ActivityParameterNode215", self)

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
    def BPMNProfile_DataOutput677(self):
        return self.__BPMNProfile_DataOutput677

    @BPMNProfile_DataOutput677.setter
    def BPMNProfile_DataOutput677(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataOutput__BPMNProfile_DataOutput677", None)
        self.__BPMNProfile_DataOutput677 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_MultiInstanceLoopCharacteristics676"):
                opp_val = getattr(old_value, "BPMNProfile_MultiInstanceLoopCharacteristics676", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_MultiInstanceLoopCharacteristics676", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_MultiInstanceLoopCharacteristics676"):
                opp_val = getattr(value, "BPMNProfile_MultiInstanceLoopCharacteristics676", None)
                setattr(value, "BPMNProfile_MultiInstanceLoopCharacteristics676", self)

    def DataOutputnotation(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement DataOutputnotation method
        pass

    def DataOutputitemSubjectRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement DataOutputitemSubjectRef method
        pass

class BPMNProfile_DataInput(ItemAwareElement):

    def __init__(self, isCollection: str, BPMNProfile_DataInput: "BPMNProfile_InputOutputSpecification" = None, BPMNProfile_DataInput175: "BPMNProfile_InputPin" = None, BPMNProfile_DataInput177: "BPMNProfile_Parameter" = None, BPMNProfile_DataInput179: "BPMNProfile_ActivityParameterNode" = None, dataInputRefs: set["BPMNProfile_InputSet"] = None, optionalInputRefs: set["BPMNProfile_InputSet"] = None, whileExecutingInputRefs: set["BPMNProfile_InputSet"] = None, DataInput: "BPMNProfile_InputSet" = None, DataInput205: "BPMNProfile_InputSet" = None, DataInput207: "BPMNProfile_InputSet" = None, BPMNProfile_DataInput680: "BPMNProfile_MultiInstanceLoopCharacteristics" = None):
        self.isCollection = isCollection
        self.BPMNProfile_DataInput = BPMNProfile_DataInput
        self.BPMNProfile_DataInput175 = BPMNProfile_DataInput175
        self.BPMNProfile_DataInput177 = BPMNProfile_DataInput177
        self.BPMNProfile_DataInput179 = BPMNProfile_DataInput179
        self.dataInputRefs = dataInputRefs if dataInputRefs is not None else set()
        self.optionalInputRefs = optionalInputRefs if optionalInputRefs is not None else set()
        self.whileExecutingInputRefs = whileExecutingInputRefs if whileExecutingInputRefs is not None else set()
        self.DataInput = DataInput
        self.DataInput205 = DataInput205
        self.DataInput207 = DataInput207
        self.BPMNProfile_DataInput680 = BPMNProfile_DataInput680
        
    @property
    def isCollection(self) -> str:
        return self.__isCollection

    @isCollection.setter
    def isCollection(self, isCollection: str):
        self.__isCollection = isCollection

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
    def BPMNProfile_DataInput179(self):
        return self.__BPMNProfile_DataInput179

    @BPMNProfile_DataInput179.setter
    def BPMNProfile_DataInput179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataInput__BPMNProfile_DataInput179", None)
        self.__BPMNProfile_DataInput179 = value
        
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
                    

    @property
    def DataInput207(self):
        return self.__DataInput207

    @DataInput207.setter
    def DataInput207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataInput__DataInput207", None)
        self.__DataInput207 = value
        
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
    def DataInput205(self):
        return self.__DataInput205

    @DataInput205.setter
    def DataInput205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataInput__DataInput205", None)
        self.__DataInput205 = value
        
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
                if hasattr(item, "InputSet184"):
                    opp_val = getattr(item, "InputSet184", None)
                    
                    if opp_val == self:
                        setattr(item, "InputSet184", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputSet184"):
                    opp_val = getattr(item, "InputSet184", None)
                    
                    setattr(item, "InputSet184", self)
                    

    @property
    def BPMNProfile_DataInput680(self):
        return self.__BPMNProfile_DataInput680

    @BPMNProfile_DataInput680.setter
    def BPMNProfile_DataInput680(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataInput__BPMNProfile_DataInput680", None)
        self.__BPMNProfile_DataInput680 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_MultiInstanceLoopCharacteristics679"):
                opp_val = getattr(old_value, "BPMNProfile_MultiInstanceLoopCharacteristics679", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_MultiInstanceLoopCharacteristics679", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_MultiInstanceLoopCharacteristics679"):
                opp_val = getattr(value, "BPMNProfile_MultiInstanceLoopCharacteristics679", None)
                setattr(value, "BPMNProfile_MultiInstanceLoopCharacteristics679", self)

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
                if hasattr(item, "InputSet182"):
                    opp_val = getattr(item, "InputSet182", None)
                    
                    if opp_val == self:
                        setattr(item, "InputSet182", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputSet182"):
                    opp_val = getattr(item, "InputSet182", None)
                    
                    setattr(item, "InputSet182", self)
                    

    @property
    def BPMNProfile_DataInput175(self):
        return self.__BPMNProfile_DataInput175

    @BPMNProfile_DataInput175.setter
    def BPMNProfile_DataInput175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataInput__BPMNProfile_DataInput175", None)
        self.__BPMNProfile_DataInput175 = value
        
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
    def BPMNProfile_DataInput177(self):
        return self.__BPMNProfile_DataInput177

    @BPMNProfile_DataInput177.setter
    def BPMNProfile_DataInput177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataInput__BPMNProfile_DataInput177", None)
        self.__BPMNProfile_DataInput177 = value
        
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

    def DataInputAssociation(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement DataInputAssociation method
        pass

    def DataInputnotation(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement DataInputnotation method
        pass

    def DataInputitemSubjectRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement DataInputitemSubjectRef method
        pass

class BPMNProfile_Action:

    pass
class BPMNProfile_BPMNInterface(RootElement):

    def __init__(self, BPMNProfile_BPMNInterface: "BPMNProfile_CallableElement" = None, BPMNProfile_BPMNInterface234: "BPMNProfile_Interface" = None, BPMNProfile_BPMNInterface236: "BPMNProfile_Element" = None, BPMNProfile_BPMNInterface239: set["BPMNProfile_BPMNOperation"] = None, BPMNProfile_BPMNInterface241: set["BPMNProfile_CallableElement"] = None, BPMNProfile_BPMNInterface307: "BPMNProfile_Participant" = None):
        self.BPMNProfile_BPMNInterface = BPMNProfile_BPMNInterface
        self.BPMNProfile_BPMNInterface234 = BPMNProfile_BPMNInterface234
        self.BPMNProfile_BPMNInterface236 = BPMNProfile_BPMNInterface236
        self.BPMNProfile_BPMNInterface239 = BPMNProfile_BPMNInterface239 if BPMNProfile_BPMNInterface239 is not None else set()
        self.BPMNProfile_BPMNInterface241 = BPMNProfile_BPMNInterface241 if BPMNProfile_BPMNInterface241 is not None else set()
        self.BPMNProfile_BPMNInterface307 = BPMNProfile_BPMNInterface307
        
    @property
    def BPMNProfile_BPMNInterface241(self):
        return self.__BPMNProfile_BPMNInterface241

    @BPMNProfile_BPMNInterface241.setter
    def BPMNProfile_BPMNInterface241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNInterface__BPMNProfile_BPMNInterface241", None)
        self.__BPMNProfile_BPMNInterface241 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_CallableElement242"):
                    opp_val = getattr(item, "BPMNProfile_CallableElement242", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_CallableElement242", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_CallableElement242"):
                    opp_val = getattr(item, "BPMNProfile_CallableElement242", None)
                    
                    setattr(item, "BPMNProfile_CallableElement242", self)
                    

    @property
    def BPMNProfile_BPMNInterface307(self):
        return self.__BPMNProfile_BPMNInterface307

    @BPMNProfile_BPMNInterface307.setter
    def BPMNProfile_BPMNInterface307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNInterface__BPMNProfile_BPMNInterface307", None)
        self.__BPMNProfile_BPMNInterface307 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Participant306"):
                opp_val = getattr(old_value, "BPMNProfile_Participant306", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Participant306"):
                opp_val = getattr(value, "BPMNProfile_Participant306", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_Participant306", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_BPMNInterface239(self):
        return self.__BPMNProfile_BPMNInterface239

    @BPMNProfile_BPMNInterface239.setter
    def BPMNProfile_BPMNInterface239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNInterface__BPMNProfile_BPMNInterface239", None)
        self.__BPMNProfile_BPMNInterface239 = value if value is not None else set()
        
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
    def BPMNProfile_BPMNInterface234(self):
        return self.__BPMNProfile_BPMNInterface234

    @BPMNProfile_BPMNInterface234.setter
    def BPMNProfile_BPMNInterface234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNInterface__BPMNProfile_BPMNInterface234", None)
        self.__BPMNProfile_BPMNInterface234 = value
        
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
            if hasattr(old_value, "BPMNProfile_CallableElement158"):
                opp_val = getattr(old_value, "BPMNProfile_CallableElement158", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CallableElement158"):
                opp_val = getattr(value, "BPMNProfile_CallableElement158", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_CallableElement158", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_BPMNInterface236(self):
        return self.__BPMNProfile_BPMNInterface236

    @BPMNProfile_BPMNInterface236.setter
    def BPMNProfile_BPMNInterface236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNInterface__BPMNProfile_BPMNInterface236", None)
        self.__BPMNProfile_BPMNInterface236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Element237"):
                opp_val = getattr(old_value, "BPMNProfile_Element237", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Element237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Element237"):
                opp_val = getattr(value, "BPMNProfile_Element237", None)
                setattr(value, "BPMNProfile_Element237", self)

    def BPMNInterfacecallableElements(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BPMNInterfacecallableElements method
        pass

    def InterfaceownedOperation(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement InterfaceownedOperation method
        pass

    def Interfaceoperationmultiplicity(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement Interfaceoperationmultiplicity method
        pass

    def BPMNInterfaceoperations(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement BPMNInterfaceoperations method
        pass

class BPMNProfile_Behavior:

    pass
class BPMNProfile_Constraint:

    pass
class BPMNProfile_Activity:

    pass
class BPMNProfile_BPMNCollaboration(RootElement):

    def __init__(self, isClosed: str, BPMNProfile_BPMNCollaboration: "BPMNProfile_BPMNProcess" = None, BPMNProfile_BPMNCollaboration271: set["BPMNProfile_ParticipantAssociation"] = None, collaboration: set["BPMNProfile_ConversationLink"] = None, BPMNProfile_BPMNCollaboration274: set["BPMNProfile_MessageFlowAssociation"] = None, BPMNProfile_BPMNCollaboration276: set["BPMNProfile_MessageFlow"] = None, BPMNProfile_BPMNCollaboration278: "BPMNProfile_Collaboration" = None, BPMNProfile_BPMNCollaboration280: set["BPMNProfile_ConversationNode"] = None, BPMNProfile_BPMNCollaboration282: set["BPMNProfile_CorrelationKey"] = None, BPMNProfile_BPMNCollaboration284: set["BPMNProfile_Participant"] = None, BPMNCollaboration: "BPMNProfile_ConversationLink" = None, BPMNProfile_BPMNCollaboration611: "BPMNProfile_CallConversation" = None):
        self.isClosed = isClosed
        self.BPMNProfile_BPMNCollaboration = BPMNProfile_BPMNCollaboration
        self.BPMNProfile_BPMNCollaboration271 = BPMNProfile_BPMNCollaboration271 if BPMNProfile_BPMNCollaboration271 is not None else set()
        self.collaboration = collaboration if collaboration is not None else set()
        self.BPMNProfile_BPMNCollaboration274 = BPMNProfile_BPMNCollaboration274 if BPMNProfile_BPMNCollaboration274 is not None else set()
        self.BPMNProfile_BPMNCollaboration276 = BPMNProfile_BPMNCollaboration276 if BPMNProfile_BPMNCollaboration276 is not None else set()
        self.BPMNProfile_BPMNCollaboration278 = BPMNProfile_BPMNCollaboration278
        self.BPMNProfile_BPMNCollaboration280 = BPMNProfile_BPMNCollaboration280 if BPMNProfile_BPMNCollaboration280 is not None else set()
        self.BPMNProfile_BPMNCollaboration282 = BPMNProfile_BPMNCollaboration282 if BPMNProfile_BPMNCollaboration282 is not None else set()
        self.BPMNProfile_BPMNCollaboration284 = BPMNProfile_BPMNCollaboration284 if BPMNProfile_BPMNCollaboration284 is not None else set()
        self.BPMNCollaboration = BPMNCollaboration
        self.BPMNProfile_BPMNCollaboration611 = BPMNProfile_BPMNCollaboration611
        
    @property
    def isClosed(self) -> str:
        return self.__isClosed

    @isClosed.setter
    def isClosed(self, isClosed: str):
        self.__isClosed = isClosed

    @property
    def BPMNProfile_BPMNCollaboration284(self):
        return self.__BPMNProfile_BPMNCollaboration284

    @BPMNProfile_BPMNCollaboration284.setter
    def BPMNProfile_BPMNCollaboration284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNCollaboration__BPMNProfile_BPMNCollaboration284", None)
        self.__BPMNProfile_BPMNCollaboration284 = value if value is not None else set()
        
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
    def BPMNProfile_BPMNCollaboration282(self):
        return self.__BPMNProfile_BPMNCollaboration282

    @BPMNProfile_BPMNCollaboration282.setter
    def BPMNProfile_BPMNCollaboration282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNCollaboration__BPMNProfile_BPMNCollaboration282", None)
        self.__BPMNProfile_BPMNCollaboration282 = value if value is not None else set()
        
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
    def BPMNProfile_BPMNCollaboration278(self):
        return self.__BPMNProfile_BPMNCollaboration278

    @BPMNProfile_BPMNCollaboration278.setter
    def BPMNProfile_BPMNCollaboration278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNCollaboration__BPMNProfile_BPMNCollaboration278", None)
        self.__BPMNProfile_BPMNCollaboration278 = value
        
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
    def BPMNProfile_BPMNCollaboration280(self):
        return self.__BPMNProfile_BPMNCollaboration280

    @BPMNProfile_BPMNCollaboration280.setter
    def BPMNProfile_BPMNCollaboration280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNCollaboration__BPMNProfile_BPMNCollaboration280", None)
        self.__BPMNProfile_BPMNCollaboration280 = value if value is not None else set()
        
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
    def BPMNProfile_BPMNCollaboration271(self):
        return self.__BPMNProfile_BPMNCollaboration271

    @BPMNProfile_BPMNCollaboration271.setter
    def BPMNProfile_BPMNCollaboration271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNCollaboration__BPMNProfile_BPMNCollaboration271", None)
        self.__BPMNProfile_BPMNCollaboration271 = value if value is not None else set()
        
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
    def BPMNProfile_BPMNCollaboration(self):
        return self.__BPMNProfile_BPMNCollaboration

    @BPMNProfile_BPMNCollaboration.setter
    def BPMNProfile_BPMNCollaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNCollaboration__BPMNProfile_BPMNCollaboration", None)
        self.__BPMNProfile_BPMNCollaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNProcess140"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNProcess140", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNProcess140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNProcess140"):
                opp_val = getattr(value, "BPMNProfile_BPMNProcess140", None)
                setattr(value, "BPMNProfile_BPMNProcess140", self)

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
    def BPMNProfile_BPMNCollaboration611(self):
        return self.__BPMNProfile_BPMNCollaboration611

    @BPMNProfile_BPMNCollaboration611.setter
    def BPMNProfile_BPMNCollaboration611(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNCollaboration__BPMNProfile_BPMNCollaboration611", None)
        self.__BPMNProfile_BPMNCollaboration611 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CallConversation610"):
                opp_val = getattr(old_value, "BPMNProfile_CallConversation610", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_CallConversation610", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CallConversation610"):
                opp_val = getattr(value, "BPMNProfile_CallConversation610", None)
                setattr(value, "BPMNProfile_CallConversation610", self)

    def Collaborationparticipants(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement Collaborationparticipants method
        pass

class FlowElementsContainer:

    pass
class BPMNProfile_SubProcess(FlowElementsContainer, BPMNActivity):

    def __init__(self, triggeredByEvent: str, BPMNProfile_SubProcess: "BPMNProfile_StructuredActivityNode" = None, BPMNProfile_SubProcess618: set["BPMNProfile_LaneSet"] = None):
        self.triggeredByEvent = triggeredByEvent
        self.BPMNProfile_SubProcess = BPMNProfile_SubProcess
        self.BPMNProfile_SubProcess618 = BPMNProfile_SubProcess618 if BPMNProfile_SubProcess618 is not None else set()
        
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
            if hasattr(old_value, "BPMNProfile_StructuredActivityNode616"):
                opp_val = getattr(old_value, "BPMNProfile_StructuredActivityNode616", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_StructuredActivityNode616", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_StructuredActivityNode616"):
                opp_val = getattr(value, "BPMNProfile_StructuredActivityNode616", None)
                setattr(value, "BPMNProfile_StructuredActivityNode616", self)

    @property
    def BPMNProfile_SubProcess618(self):
        return self.__BPMNProfile_SubProcess618

    @BPMNProfile_SubProcess618.setter
    def BPMNProfile_SubProcess618(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_SubProcess__BPMNProfile_SubProcess618", None)
        self.__BPMNProfile_SubProcess618 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_LaneSet619"):
                    opp_val = getattr(item, "BPMNProfile_LaneSet619", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_LaneSet619", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_LaneSet619"):
                    opp_val = getattr(item, "BPMNProfile_LaneSet619", None)
                    
                    setattr(item, "BPMNProfile_LaneSet619", self)
                    

    def SubProcesstriggeredByEvent(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SubProcesstriggeredByEvent method
        pass

class CallableElement:

    pass
class BPMNProfile_GlobalTask(CallableElement):

    def __init__(self, BPMNProfile_GlobalTask: "BPMNProfile_OpaqueBehavior" = None, BPMNProfile_GlobalTask439: set["BPMNProfile_ResourceRole"] = None):
        self.BPMNProfile_GlobalTask = BPMNProfile_GlobalTask
        self.BPMNProfile_GlobalTask439 = BPMNProfile_GlobalTask439 if BPMNProfile_GlobalTask439 is not None else set()
        
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

    @property
    def BPMNProfile_GlobalTask439(self):
        return self.__BPMNProfile_GlobalTask439

    @BPMNProfile_GlobalTask439.setter
    def BPMNProfile_GlobalTask439(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_GlobalTask__BPMNProfile_GlobalTask439", None)
        self.__BPMNProfile_GlobalTask439 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_ResourceRole440"):
                    opp_val = getattr(item, "BPMNProfile_ResourceRole440", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_ResourceRole440", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_ResourceRole440"):
                    opp_val = getattr(item, "BPMNProfile_ResourceRole440", None)
                    
                    setattr(item, "BPMNProfile_ResourceRole440", self)
                    

    def GlobalTasksupportedInterfaceRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement GlobalTasksupportedInterfaceRefs method
        pass

class BPMNProfile_BPMNProcess(FlowElementsContainer, CallableElement):

    def __init__(self, processType: str, isClosed: str, isExecutable: str, BPMNProfile_BPMNProcess: "BPMNProfile_Auditing" = None, BPMNProfile_BPMNProcess140: "BPMNProfile_BPMNCollaboration" = None, BPMNProfile_BPMNProcess142: "BPMNProfile_Activity" = None, BPMNProfile_BPMNProcess144: set["BPMNProfile_CorrelationSubscription"] = None, BPMNProfile_BPMNProcess146: "BPMNProfile_Monitoring" = None, BPMNProfile_BPMNProcess150: "BPMNProfile_BPMNProcess" = None, BPMNProfile_BPMNProcess148: "BPMNProfile_BPMNProcess" = None, BPMNProfile_BPMNProcess152: set["BPMNProfile_BPMNProperty"] = None, process: set["BPMNProfile_ResourceRole"] = None, BPMNProfile_BPMNProcess299: "BPMNProfile_Participant" = None, BPMNProcess: "BPMNProfile_ResourceRole" = None):
        self.processType = processType
        self.isClosed = isClosed
        self.isExecutable = isExecutable
        self.BPMNProfile_BPMNProcess = BPMNProfile_BPMNProcess
        self.BPMNProfile_BPMNProcess140 = BPMNProfile_BPMNProcess140
        self.BPMNProfile_BPMNProcess142 = BPMNProfile_BPMNProcess142
        self.BPMNProfile_BPMNProcess144 = BPMNProfile_BPMNProcess144 if BPMNProfile_BPMNProcess144 is not None else set()
        self.BPMNProfile_BPMNProcess146 = BPMNProfile_BPMNProcess146
        self.BPMNProfile_BPMNProcess150 = BPMNProfile_BPMNProcess150
        self.BPMNProfile_BPMNProcess148 = BPMNProfile_BPMNProcess148
        self.BPMNProfile_BPMNProcess152 = BPMNProfile_BPMNProcess152 if BPMNProfile_BPMNProcess152 is not None else set()
        self.process = process if process is not None else set()
        self.BPMNProfile_BPMNProcess299 = BPMNProfile_BPMNProcess299
        self.BPMNProcess = BPMNProcess
        
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
    def isExecutable(self) -> str:
        return self.__isExecutable

    @isExecutable.setter
    def isExecutable(self, isExecutable: str):
        self.__isExecutable = isExecutable

    @property
    def BPMNProfile_BPMNProcess152(self):
        return self.__BPMNProfile_BPMNProcess152

    @BPMNProfile_BPMNProcess152.setter
    def BPMNProfile_BPMNProcess152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProcess__BPMNProfile_BPMNProcess152", None)
        self.__BPMNProfile_BPMNProcess152 = value if value is not None else set()
        
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
    def BPMNProfile_BPMNProcess(self):
        return self.__BPMNProfile_BPMNProcess

    @BPMNProfile_BPMNProcess.setter
    def BPMNProfile_BPMNProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProcess__BPMNProfile_BPMNProcess", None)
        self.__BPMNProfile_BPMNProcess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Auditing138"):
                opp_val = getattr(old_value, "BPMNProfile_Auditing138", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Auditing138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Auditing138"):
                opp_val = getattr(value, "BPMNProfile_Auditing138", None)
                setattr(value, "BPMNProfile_Auditing138", self)

    @property
    def BPMNProfile_BPMNProcess146(self):
        return self.__BPMNProfile_BPMNProcess146

    @BPMNProfile_BPMNProcess146.setter
    def BPMNProfile_BPMNProcess146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProcess__BPMNProfile_BPMNProcess146", None)
        self.__BPMNProfile_BPMNProcess146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Monitoring147"):
                opp_val = getattr(old_value, "BPMNProfile_Monitoring147", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Monitoring147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Monitoring147"):
                opp_val = getattr(value, "BPMNProfile_Monitoring147", None)
                setattr(value, "BPMNProfile_Monitoring147", self)

    @property
    def BPMNProfile_BPMNProcess150(self):
        return self.__BPMNProfile_BPMNProcess150

    @BPMNProfile_BPMNProcess150.setter
    def BPMNProfile_BPMNProcess150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProcess__BPMNProfile_BPMNProcess150", None)
        self.__BPMNProfile_BPMNProcess150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNProcess148"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNProcess148", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNProcess148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNProcess148"):
                opp_val = getattr(value, "BPMNProfile_BPMNProcess148", None)
                setattr(value, "BPMNProfile_BPMNProcess148", self)

    @property
    def BPMNProfile_BPMNProcess299(self):
        return self.__BPMNProfile_BPMNProcess299

    @BPMNProfile_BPMNProcess299.setter
    def BPMNProfile_BPMNProcess299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProcess__BPMNProfile_BPMNProcess299", None)
        self.__BPMNProfile_BPMNProcess299 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Participant298"):
                opp_val = getattr(old_value, "BPMNProfile_Participant298", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Participant298", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Participant298"):
                opp_val = getattr(value, "BPMNProfile_Participant298", None)
                setattr(value, "BPMNProfile_Participant298", self)

    @property
    def BPMNProfile_BPMNProcess148(self):
        return self.__BPMNProfile_BPMNProcess148

    @BPMNProfile_BPMNProcess148.setter
    def BPMNProfile_BPMNProcess148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProcess__BPMNProfile_BPMNProcess148", None)
        self.__BPMNProfile_BPMNProcess148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNProcess150"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNProcess150", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNProcess150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNProcess150"):
                opp_val = getattr(value, "BPMNProfile_BPMNProcess150", None)
                setattr(value, "BPMNProfile_BPMNProcess150", self)

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
    def BPMNProfile_BPMNProcess142(self):
        return self.__BPMNProfile_BPMNProcess142

    @BPMNProfile_BPMNProcess142.setter
    def BPMNProfile_BPMNProcess142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProcess__BPMNProfile_BPMNProcess142", None)
        self.__BPMNProfile_BPMNProcess142 = value
        
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
    def BPMNProfile_BPMNProcess144(self):
        return self.__BPMNProfile_BPMNProcess144

    @BPMNProfile_BPMNProcess144.setter
    def BPMNProfile_BPMNProcess144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNProcess__BPMNProfile_BPMNProcess144", None)
        self.__BPMNProfile_BPMNProcess144 = value if value is not None else set()
        
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
                    

    def ProcesslaneSets(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ProcesslaneSets method
        pass

    def ProcesssupportedInterfaceRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ProcesssupportedInterfaceRefs method
        pass

    def ProcessflowElements(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ProcessflowElements method
        pass

    def Processproperties(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement Processproperties method
        pass

    def Processsupports(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement Processsupports method
        pass

class BPMNProfile_DecisionNode:

    pass
class BPMNProfile_PackageImport:

    pass
class BPMNProfile_Import:

    def __init__(self, importType: str, location: str, namespace: str, BPMNProfile_Import: "BPMNProfile_Definitions" = None, BPMNProfile_Import122: "BPMNProfile_PackageImport" = None, BPMNProfile_Import124: "BPMNProfile_Definitions" = None, BPMNProfile_Import200: "BPMNProfile_ItemDefinition" = None):
        self.importType = importType
        self.location = location
        self.namespace = namespace
        self.BPMNProfile_Import = BPMNProfile_Import
        self.BPMNProfile_Import122 = BPMNProfile_Import122
        self.BPMNProfile_Import124 = BPMNProfile_Import124
        self.BPMNProfile_Import200 = BPMNProfile_Import200
        
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
    def importType(self) -> str:
        return self.__importType

    @importType.setter
    def importType(self, importType: str):
        self.__importType = importType

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
            if hasattr(old_value, "BPMNProfile_Definitions111"):
                opp_val = getattr(old_value, "BPMNProfile_Definitions111", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Definitions111"):
                opp_val = getattr(value, "BPMNProfile_Definitions111", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_Definitions111", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_Import124(self):
        return self.__BPMNProfile_Import124

    @BPMNProfile_Import124.setter
    def BPMNProfile_Import124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Import__BPMNProfile_Import124", None)
        self.__BPMNProfile_Import124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Definitions125"):
                opp_val = getattr(old_value, "BPMNProfile_Definitions125", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Definitions125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Definitions125"):
                opp_val = getattr(value, "BPMNProfile_Definitions125", None)
                setattr(value, "BPMNProfile_Definitions125", self)

    @property
    def BPMNProfile_Import122(self):
        return self.__BPMNProfile_Import122

    @BPMNProfile_Import122.setter
    def BPMNProfile_Import122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Import__BPMNProfile_Import122", None)
        self.__BPMNProfile_Import122 = value
        
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

    @property
    def BPMNProfile_Import200(self):
        return self.__BPMNProfile_Import200

    @BPMNProfile_Import200.setter
    def BPMNProfile_Import200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Import__BPMNProfile_Import200", None)
        self.__BPMNProfile_Import200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ItemDefinition199"):
                opp_val = getattr(old_value, "BPMNProfile_ItemDefinition199", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ItemDefinition199", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ItemDefinition199"):
                opp_val = getattr(value, "BPMNProfile_ItemDefinition199", None)
                setattr(value, "BPMNProfile_ItemDefinition199", self)

class BPMNProfile_BPMNExtension:

    def __init__(self, mustUnderstand: str, BPMNProfile_BPMNExtension: "BPMNProfile_Definitions" = None, BPMNProfile_BPMNExtension116: "BPMNProfile_Stereotype" = None, BPMNProfile_BPMNExtension119: "BPMNProfile_ExtensionDefinition" = None):
        self.mustUnderstand = mustUnderstand
        self.BPMNProfile_BPMNExtension = BPMNProfile_BPMNExtension
        self.BPMNProfile_BPMNExtension116 = BPMNProfile_BPMNExtension116
        self.BPMNProfile_BPMNExtension119 = BPMNProfile_BPMNExtension119
        
    @property
    def mustUnderstand(self) -> str:
        return self.__mustUnderstand

    @mustUnderstand.setter
    def mustUnderstand(self, mustUnderstand: str):
        self.__mustUnderstand = mustUnderstand

    @property
    def BPMNProfile_BPMNExtension119(self):
        return self.__BPMNProfile_BPMNExtension119

    @BPMNProfile_BPMNExtension119.setter
    def BPMNProfile_BPMNExtension119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNExtension__BPMNProfile_BPMNExtension119", None)
        self.__BPMNProfile_BPMNExtension119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ExtensionDefinition120"):
                opp_val = getattr(old_value, "BPMNProfile_ExtensionDefinition120", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ExtensionDefinition120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ExtensionDefinition120"):
                opp_val = getattr(value, "BPMNProfile_ExtensionDefinition120", None)
                setattr(value, "BPMNProfile_ExtensionDefinition120", self)

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
            if hasattr(old_value, "BPMNProfile_Definitions109"):
                opp_val = getattr(old_value, "BPMNProfile_Definitions109", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Definitions109"):
                opp_val = getattr(value, "BPMNProfile_Definitions109", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_Definitions109", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_BPMNExtension116(self):
        return self.__BPMNProfile_BPMNExtension116

    @BPMNProfile_BPMNExtension116.setter
    def BPMNProfile_BPMNExtension116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNExtension__BPMNProfile_BPMNExtension116", None)
        self.__BPMNProfile_BPMNExtension116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Stereotype117"):
                opp_val = getattr(old_value, "BPMNProfile_Stereotype117", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Stereotype117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Stereotype117"):
                opp_val = getattr(value, "BPMNProfile_Stereotype117", None)
                setattr(value, "BPMNProfile_Stereotype117", self)

class BPMNProfile_Package:

    pass
class BPMNProfile_PackageableElement:

    pass
class BPMNProfile_MergeNode:

    pass
class BPMNProfile_ControlFlow:

    pass
class BPMNProfile_InterruptibleActivityRegion:

    pass
class BPMNProfile_StructuredActivityNode:

    pass
class BPMNProfile_OpaqueExpression:

    pass
class BPMNProfile_EnumerationLiteral:

    pass
class BPMNProfile_ActivityPartition:

    pass
class BPMNProfile_ExtensionAttributeDefinition:

    def __init__(self, type: str, isReference: str, BPMNProfile_ExtensionAttributeDefinition31: "BPMNProfile_Property" = None, BPMNProfile_ExtensionAttributeDefinition38: "BPMNProfile_ExtensionDefinition" = None, BPMNProfile_ExtensionAttributeDefinition: "BPMNProfile_ExtensionAttributeValue" = None):
        self.type = type
        self.isReference = isReference
        self.BPMNProfile_ExtensionAttributeDefinition31 = BPMNProfile_ExtensionAttributeDefinition31
        self.BPMNProfile_ExtensionAttributeDefinition38 = BPMNProfile_ExtensionAttributeDefinition38
        self.BPMNProfile_ExtensionAttributeDefinition = BPMNProfile_ExtensionAttributeDefinition
        
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

class BPMNProfile_Slot:

    pass
class BPMNProfile_Class:

    pass
class BPMNProfile_Dependency:

    pass
class BPMNArtifact:

    pass
class BPMNProfile_TextAnnotation(BPMNArtifact):

    def __init__(self, textFormat: str, text: str, BPMNProfile_TextAnnotation: "BPMNProfile_Comment" = None):
        self.textFormat = textFormat
        self.text = text
        self.BPMNProfile_TextAnnotation = BPMNProfile_TextAnnotation
        
    @property
    def textFormat(self) -> str:
        return self.__textFormat

    @textFormat.setter
    def textFormat(self, textFormat: str):
        self.__textFormat = textFormat

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

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
            if hasattr(old_value, "BPMNProfile_Comment568"):
                opp_val = getattr(old_value, "BPMNProfile_Comment568", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Comment568", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Comment568"):
                opp_val = getattr(value, "BPMNProfile_Comment568", None)
                setattr(value, "BPMNProfile_Comment568", self)

class BPMNProfile_Group(BPMNArtifact):

    pass
class BPMNProfile_Stereotype:

    pass
class BPMNProfile_Comment:

    pass
class BPMNProfile_Property:

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

    def AssociationEnd(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AssociationEnd method
        pass

class BPMNProfile_ExtensionDefinition:

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
                    

class BaseElement:

    pass
class BPMNProfile_ParticipantAssociation(BaseElement):

    def __init__(self, BPMNProfile_ParticipantAssociation: "BPMNProfile_BPMNCollaboration" = None, BPMNProfile_ParticipantAssociation286: "BPMNProfile_Dependency" = None, BPMNProfile_ParticipantAssociation289: "BPMNProfile_Participant" = None, BPMNProfile_ParticipantAssociation292: "BPMNProfile_Participant" = None, BPMNProfile_ParticipantAssociation614: "BPMNProfile_CallConversation" = None):
        self.BPMNProfile_ParticipantAssociation = BPMNProfile_ParticipantAssociation
        self.BPMNProfile_ParticipantAssociation286 = BPMNProfile_ParticipantAssociation286
        self.BPMNProfile_ParticipantAssociation289 = BPMNProfile_ParticipantAssociation289
        self.BPMNProfile_ParticipantAssociation292 = BPMNProfile_ParticipantAssociation292
        self.BPMNProfile_ParticipantAssociation614 = BPMNProfile_ParticipantAssociation614
        
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
            if hasattr(old_value, "BPMNProfile_BPMNCollaboration271"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNCollaboration271", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNCollaboration271"):
                opp_val = getattr(value, "BPMNProfile_BPMNCollaboration271", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNCollaboration271", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_ParticipantAssociation289(self):
        return self.__BPMNProfile_ParticipantAssociation289

    @BPMNProfile_ParticipantAssociation289.setter
    def BPMNProfile_ParticipantAssociation289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ParticipantAssociation__BPMNProfile_ParticipantAssociation289", None)
        self.__BPMNProfile_ParticipantAssociation289 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Participant290"):
                opp_val = getattr(old_value, "BPMNProfile_Participant290", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Participant290", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Participant290"):
                opp_val = getattr(value, "BPMNProfile_Participant290", None)
                setattr(value, "BPMNProfile_Participant290", self)

    @property
    def BPMNProfile_ParticipantAssociation614(self):
        return self.__BPMNProfile_ParticipantAssociation614

    @BPMNProfile_ParticipantAssociation614.setter
    def BPMNProfile_ParticipantAssociation614(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ParticipantAssociation__BPMNProfile_ParticipantAssociation614", None)
        self.__BPMNProfile_ParticipantAssociation614 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_CallConversation613"):
                opp_val = getattr(old_value, "BPMNProfile_CallConversation613", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_CallConversation613"):
                opp_val = getattr(value, "BPMNProfile_CallConversation613", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_CallConversation613", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_ParticipantAssociation292(self):
        return self.__BPMNProfile_ParticipantAssociation292

    @BPMNProfile_ParticipantAssociation292.setter
    def BPMNProfile_ParticipantAssociation292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ParticipantAssociation__BPMNProfile_ParticipantAssociation292", None)
        self.__BPMNProfile_ParticipantAssociation292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Participant293"):
                opp_val = getattr(old_value, "BPMNProfile_Participant293", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Participant293", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Participant293"):
                opp_val = getattr(value, "BPMNProfile_Participant293", None)
                setattr(value, "BPMNProfile_Participant293", self)

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
            if hasattr(old_value, "BPMNProfile_Dependency287"):
                opp_val = getattr(old_value, "BPMNProfile_Dependency287", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Dependency287", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Dependency287"):
                opp_val = getattr(value, "BPMNProfile_Dependency287", None)
                setattr(value, "BPMNProfile_Dependency287", self)

    def ParticipantAssociationouterParticipantRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ParticipantAssociationouterParticipantRef method
        pass

    def ParticipantAssociationinnerParticipantRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ParticipantAssociationinnerParticipantRef method
        pass

class BPMNProfile_DataAssociation(BaseElement):

    def __init__(self, BPMNProfile_DataAssociation: "BPMNProfile_ObjectFlow" = None, BPMNProfile_DataAssociation490: "BPMNProfile_ItemAwareElement" = None, BPMNProfile_DataAssociation493: "BPMNProfile_ItemAwareElement" = None, BPMNProfile_DataAssociation496: "BPMNProfile_FormalExpression" = None, BPMNProfile_DataAssociation499: set["BPMNProfile_Assignment"] = None):
        self.BPMNProfile_DataAssociation = BPMNProfile_DataAssociation
        self.BPMNProfile_DataAssociation490 = BPMNProfile_DataAssociation490
        self.BPMNProfile_DataAssociation493 = BPMNProfile_DataAssociation493
        self.BPMNProfile_DataAssociation496 = BPMNProfile_DataAssociation496
        self.BPMNProfile_DataAssociation499 = BPMNProfile_DataAssociation499 if BPMNProfile_DataAssociation499 is not None else set()
        
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
            if hasattr(old_value, "BPMNProfile_ItemAwareElement491"):
                opp_val = getattr(old_value, "BPMNProfile_ItemAwareElement491", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ItemAwareElement491", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ItemAwareElement491"):
                opp_val = getattr(value, "BPMNProfile_ItemAwareElement491", None)
                setattr(value, "BPMNProfile_ItemAwareElement491", self)

    @property
    def BPMNProfile_DataAssociation496(self):
        return self.__BPMNProfile_DataAssociation496

    @BPMNProfile_DataAssociation496.setter
    def BPMNProfile_DataAssociation496(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataAssociation__BPMNProfile_DataAssociation496", None)
        self.__BPMNProfile_DataAssociation496 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_FormalExpression497"):
                opp_val = getattr(old_value, "BPMNProfile_FormalExpression497", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_FormalExpression497", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_FormalExpression497"):
                opp_val = getattr(value, "BPMNProfile_FormalExpression497", None)
                setattr(value, "BPMNProfile_FormalExpression497", self)

    @property
    def BPMNProfile_DataAssociation499(self):
        return self.__BPMNProfile_DataAssociation499

    @BPMNProfile_DataAssociation499.setter
    def BPMNProfile_DataAssociation499(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataAssociation__BPMNProfile_DataAssociation499", None)
        self.__BPMNProfile_DataAssociation499 = value if value is not None else set()
        
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
    def BPMNProfile_DataAssociation493(self):
        return self.__BPMNProfile_DataAssociation493

    @BPMNProfile_DataAssociation493.setter
    def BPMNProfile_DataAssociation493(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataAssociation__BPMNProfile_DataAssociation493", None)
        self.__BPMNProfile_DataAssociation493 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ItemAwareElement494"):
                opp_val = getattr(old_value, "BPMNProfile_ItemAwareElement494", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ItemAwareElement494", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ItemAwareElement494"):
                opp_val = getattr(value, "BPMNProfile_ItemAwareElement494", None)
                setattr(value, "BPMNProfile_ItemAwareElement494", self)

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

    def DataAssociationtarget(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement DataAssociationtarget method
        pass

    def DataAssociationtransformation(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement DataAssociationtransformation method
        pass

    def DataAssociationsource(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement DataAssociationsource method
        pass

class BPMNProfile_CorrelationPropertyRetrievalExpression(BaseElement):

    pass
class BPMNProfile_CorrelationKey(BaseElement):

    pass
class BPMNProfile_Lane(BaseElement):

    def __init__(self, Lane: "BPMNProfile_LaneSet" = None, BPMNProfile_Lane: "BPMNProfile_LaneSet" = None, BPMNProfile_Lane60: "BPMNProfile_ActivityPartition" = None, BPMNProfile_Lane63: "BPMNProfile_Element" = None, BPMNProfile_Lane66: set["BPMNProfile_FlowNode"] = None, BPMNProfile_Lane69: "BPMNProfile_BaseElement" = None, BPMNProfile_Lane72: "BPMNProfile_LaneSet" = None, lanes: "BPMNProfile_LaneSet" = None):
        self.Lane = Lane
        self.BPMNProfile_Lane = BPMNProfile_Lane
        self.BPMNProfile_Lane60 = BPMNProfile_Lane60
        self.BPMNProfile_Lane63 = BPMNProfile_Lane63
        self.BPMNProfile_Lane66 = BPMNProfile_Lane66 if BPMNProfile_Lane66 is not None else set()
        self.BPMNProfile_Lane69 = BPMNProfile_Lane69
        self.BPMNProfile_Lane72 = BPMNProfile_Lane72
        self.lanes = lanes
        
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

    def LanelaneSet(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement LanelaneSet method
        pass

    def LaneflowNodeRefs(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement LaneflowNodeRefs method
        pass

    def LanepartitionElementRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement LanepartitionElementRef method
        pass

    def LanechildLaneSet(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement LanechildLaneSet method
        pass

class BPMNProfile_ConversationNode(InteractionNode, BaseElement):

    def __init__(self, BPMNProfile_ConversationNode: "BPMNProfile_BPMNCollaboration" = None, BPMNProfile_ConversationNode351: "BPMNProfile_InformationFlow" = None, BPMNProfile_ConversationNode354: set["BPMNProfile_MessageFlow"] = None, BPMNProfile_ConversationNode357: set["BPMNProfile_CorrelationKey"] = None, BPMNProfile_ConversationNode360: set["BPMNProfile_Participant"] = None, BPMNProfile_ConversationNode607: "BPMNProfile_SubConversation" = None):
        self.BPMNProfile_ConversationNode = BPMNProfile_ConversationNode
        self.BPMNProfile_ConversationNode351 = BPMNProfile_ConversationNode351
        self.BPMNProfile_ConversationNode354 = BPMNProfile_ConversationNode354 if BPMNProfile_ConversationNode354 is not None else set()
        self.BPMNProfile_ConversationNode357 = BPMNProfile_ConversationNode357 if BPMNProfile_ConversationNode357 is not None else set()
        self.BPMNProfile_ConversationNode360 = BPMNProfile_ConversationNode360 if BPMNProfile_ConversationNode360 is not None else set()
        self.BPMNProfile_ConversationNode607 = BPMNProfile_ConversationNode607
        
    @property
    def BPMNProfile_ConversationNode607(self):
        return self.__BPMNProfile_ConversationNode607

    @BPMNProfile_ConversationNode607.setter
    def BPMNProfile_ConversationNode607(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ConversationNode__BPMNProfile_ConversationNode607", None)
        self.__BPMNProfile_ConversationNode607 = value
        
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
    def BPMNProfile_ConversationNode351(self):
        return self.__BPMNProfile_ConversationNode351

    @BPMNProfile_ConversationNode351.setter
    def BPMNProfile_ConversationNode351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ConversationNode__BPMNProfile_ConversationNode351", None)
        self.__BPMNProfile_ConversationNode351 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_InformationFlow352"):
                opp_val = getattr(old_value, "BPMNProfile_InformationFlow352", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_InformationFlow352", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_InformationFlow352"):
                opp_val = getattr(value, "BPMNProfile_InformationFlow352", None)
                setattr(value, "BPMNProfile_InformationFlow352", self)

    @property
    def BPMNProfile_ConversationNode357(self):
        return self.__BPMNProfile_ConversationNode357

    @BPMNProfile_ConversationNode357.setter
    def BPMNProfile_ConversationNode357(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ConversationNode__BPMNProfile_ConversationNode357", None)
        self.__BPMNProfile_ConversationNode357 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_CorrelationKey358"):
                    opp_val = getattr(item, "BPMNProfile_CorrelationKey358", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_CorrelationKey358", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_CorrelationKey358"):
                    opp_val = getattr(item, "BPMNProfile_CorrelationKey358", None)
                    
                    setattr(item, "BPMNProfile_CorrelationKey358", self)
                    

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
                if hasattr(item, "BPMNProfile_MessageFlow355"):
                    opp_val = getattr(item, "BPMNProfile_MessageFlow355", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_MessageFlow355", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_MessageFlow355"):
                    opp_val = getattr(item, "BPMNProfile_MessageFlow355", None)
                    
                    setattr(item, "BPMNProfile_MessageFlow355", self)
                    

    @property
    def BPMNProfile_ConversationNode360(self):
        return self.__BPMNProfile_ConversationNode360

    @BPMNProfile_ConversationNode360.setter
    def BPMNProfile_ConversationNode360(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ConversationNode__BPMNProfile_ConversationNode360", None)
        self.__BPMNProfile_ConversationNode360 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_Participant361"):
                    opp_val = getattr(item, "BPMNProfile_Participant361", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_Participant361", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_Participant361"):
                    opp_val = getattr(item, "BPMNProfile_Participant361", None)
                    
                    setattr(item, "BPMNProfile_Participant361", self)
                    

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
            if hasattr(old_value, "BPMNProfile_BPMNCollaboration280"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNCollaboration280", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNCollaboration280"):
                opp_val = getattr(value, "BPMNProfile_BPMNCollaboration280", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNCollaboration280", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def ConversationNodeparticipantRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ConversationNodeparticipantRefs method
        pass

class BPMNProfile_RootElement(BaseElement):

    pass
class BPMNProfile_BPMNRelationship(BaseElement):

    def __init__(self, type: str, direction: str, BPMNProfile_BPMNRelationship: "BPMNProfile_Definitions" = None, BPMNProfile_BPMNRelationship135: "BPMNProfile_Definitions" = None, BPMNProfile_BPMNRelationship127: "BPMNProfile_Constraint" = None, BPMNProfile_BPMNRelationship129: set["BPMNProfile_Element"] = None, BPMNProfile_BPMNRelationship132: set["BPMNProfile_Element"] = None):
        self.type = type
        self.direction = direction
        self.BPMNProfile_BPMNRelationship = BPMNProfile_BPMNRelationship
        self.BPMNProfile_BPMNRelationship135 = BPMNProfile_BPMNRelationship135
        self.BPMNProfile_BPMNRelationship127 = BPMNProfile_BPMNRelationship127
        self.BPMNProfile_BPMNRelationship129 = BPMNProfile_BPMNRelationship129 if BPMNProfile_BPMNRelationship129 is not None else set()
        self.BPMNProfile_BPMNRelationship132 = BPMNProfile_BPMNRelationship132 if BPMNProfile_BPMNRelationship132 is not None else set()
        
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
    def BPMNProfile_BPMNRelationship135(self):
        return self.__BPMNProfile_BPMNRelationship135

    @BPMNProfile_BPMNRelationship135.setter
    def BPMNProfile_BPMNRelationship135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNRelationship__BPMNProfile_BPMNRelationship135", None)
        self.__BPMNProfile_BPMNRelationship135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Definitions136"):
                opp_val = getattr(old_value, "BPMNProfile_Definitions136", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Definitions136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Definitions136"):
                opp_val = getattr(value, "BPMNProfile_Definitions136", None)
                setattr(value, "BPMNProfile_Definitions136", self)

    @property
    def BPMNProfile_BPMNRelationship127(self):
        return self.__BPMNProfile_BPMNRelationship127

    @BPMNProfile_BPMNRelationship127.setter
    def BPMNProfile_BPMNRelationship127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNRelationship__BPMNProfile_BPMNRelationship127", None)
        self.__BPMNProfile_BPMNRelationship127 = value
        
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
    def BPMNProfile_BPMNRelationship129(self):
        return self.__BPMNProfile_BPMNRelationship129

    @BPMNProfile_BPMNRelationship129.setter
    def BPMNProfile_BPMNRelationship129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNRelationship__BPMNProfile_BPMNRelationship129", None)
        self.__BPMNProfile_BPMNRelationship129 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_Element130"):
                    opp_val = getattr(item, "BPMNProfile_Element130", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_Element130", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_Element130"):
                    opp_val = getattr(item, "BPMNProfile_Element130", None)
                    
                    setattr(item, "BPMNProfile_Element130", self)
                    

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
            if hasattr(old_value, "BPMNProfile_Definitions113"):
                opp_val = getattr(old_value, "BPMNProfile_Definitions113", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Definitions113"):
                opp_val = getattr(value, "BPMNProfile_Definitions113", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_Definitions113", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_BPMNRelationship132(self):
        return self.__BPMNProfile_BPMNRelationship132

    @BPMNProfile_BPMNRelationship132.setter
    def BPMNProfile_BPMNRelationship132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNRelationship__BPMNProfile_BPMNRelationship132", None)
        self.__BPMNProfile_BPMNRelationship132 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_Element133"):
                    opp_val = getattr(item, "BPMNProfile_Element133", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_Element133", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_Element133"):
                    opp_val = getattr(item, "BPMNProfile_Element133", None)
                    
                    setattr(item, "BPMNProfile_Element133", self)
                    

class BPMNProfile_FlowElementsContainer(BaseElement):

    pass
class BPMNProfile_ResourceParameter(BaseElement):

    def __init__(self, isRequired: str, BPMNProfile_ResourceParameter: "BPMNProfile_Resource" = None, BPMNProfile_ResourceParameter423: "BPMNProfile_Property" = None, BPMNProfile_ResourceParameter426: "BPMNProfile_ItemDefinition" = None, BPMNProfile_ResourceParameter433: "BPMNProfile_ResourceParameterBinding" = None):
        self.isRequired = isRequired
        self.BPMNProfile_ResourceParameter = BPMNProfile_ResourceParameter
        self.BPMNProfile_ResourceParameter423 = BPMNProfile_ResourceParameter423
        self.BPMNProfile_ResourceParameter426 = BPMNProfile_ResourceParameter426
        self.BPMNProfile_ResourceParameter433 = BPMNProfile_ResourceParameter433
        
    @property
    def isRequired(self) -> str:
        return self.__isRequired

    @isRequired.setter
    def isRequired(self, isRequired: str):
        self.__isRequired = isRequired

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
            if hasattr(old_value, "BPMNProfile_Resource421"):
                opp_val = getattr(old_value, "BPMNProfile_Resource421", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Resource421"):
                opp_val = getattr(value, "BPMNProfile_Resource421", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_Resource421", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_ResourceParameter433(self):
        return self.__BPMNProfile_ResourceParameter433

    @BPMNProfile_ResourceParameter433.setter
    def BPMNProfile_ResourceParameter433(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceParameter__BPMNProfile_ResourceParameter433", None)
        self.__BPMNProfile_ResourceParameter433 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ResourceParameterBinding432"):
                opp_val = getattr(old_value, "BPMNProfile_ResourceParameterBinding432", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ResourceParameterBinding432", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ResourceParameterBinding432"):
                opp_val = getattr(value, "BPMNProfile_ResourceParameterBinding432", None)
                setattr(value, "BPMNProfile_ResourceParameterBinding432", self)

    @property
    def BPMNProfile_ResourceParameter426(self):
        return self.__BPMNProfile_ResourceParameter426

    @BPMNProfile_ResourceParameter426.setter
    def BPMNProfile_ResourceParameter426(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceParameter__BPMNProfile_ResourceParameter426", None)
        self.__BPMNProfile_ResourceParameter426 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ItemDefinition427"):
                opp_val = getattr(old_value, "BPMNProfile_ItemDefinition427", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ItemDefinition427", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ItemDefinition427"):
                opp_val = getattr(value, "BPMNProfile_ItemDefinition427", None)
                setattr(value, "BPMNProfile_ItemDefinition427", self)

    @property
    def BPMNProfile_ResourceParameter423(self):
        return self.__BPMNProfile_ResourceParameter423

    @BPMNProfile_ResourceParameter423.setter
    def BPMNProfile_ResourceParameter423(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceParameter__BPMNProfile_ResourceParameter423", None)
        self.__BPMNProfile_ResourceParameter423 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Property424"):
                opp_val = getattr(old_value, "BPMNProfile_Property424", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Property424", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Property424"):
                opp_val = getattr(value, "BPMNProfile_Property424", None)
                setattr(value, "BPMNProfile_Property424", self)

    def ResourceParameterowner(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceParameterowner method
        pass

    def ResourceParameterisRequired(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ResourceParameterisRequired method
        pass

    def ResourceParametertype(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ResourceParametertype method
        pass

class BPMNProfile_ParticipantMultiplicity(BaseElement):

    def __init__(self, minimum: str, maximum: str, BPMNProfile_ParticipantMultiplicity: "BPMNProfile_Participant" = None, BPMNProfile_ParticipantMultiplicity323: "BPMNProfile_MultiplicityElement" = None):
        self.minimum = minimum
        self.maximum = maximum
        self.BPMNProfile_ParticipantMultiplicity = BPMNProfile_ParticipantMultiplicity
        self.BPMNProfile_ParticipantMultiplicity323 = BPMNProfile_ParticipantMultiplicity323
        
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
    def BPMNProfile_ParticipantMultiplicity323(self):
        return self.__BPMNProfile_ParticipantMultiplicity323

    @BPMNProfile_ParticipantMultiplicity323.setter
    def BPMNProfile_ParticipantMultiplicity323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ParticipantMultiplicity__BPMNProfile_ParticipantMultiplicity323", None)
        self.__BPMNProfile_ParticipantMultiplicity323 = value
        
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
            if hasattr(old_value, "BPMNProfile_Participant301"):
                opp_val = getattr(old_value, "BPMNProfile_Participant301", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Participant301", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Participant301"):
                opp_val = getattr(value, "BPMNProfile_Participant301", None)
                setattr(value, "BPMNProfile_Participant301", self)

class BPMNProfile_BPMNExpression(BaseElement):

    pass
class BPMNProfile_Assignment(BaseElement):

    pass
class BPMNProfile_Monitoring(BaseElement):

    pass
class BPMNProfile_ResourceRole(BaseElement):

    def __init__(self, ResourceRole: "BPMNProfile_BPMNProcess" = None, BPMNProfile_ResourceRole: "BPMNProfile_Property" = None, BPMNProfile_ResourceRole411: "BPMNProfile_ResourceAssignmentExpression" = None, BPMNProfile_ResourceRole413: "BPMNProfile_Resource" = None, BPMNProfile_ResourceRole415: set["BPMNProfile_ResourceParameterBinding"] = None, resources: "BPMNProfile_BPMNProcess" = None, BPMNProfile_ResourceRole440: "BPMNProfile_GlobalTask" = None, BPMNProfile_ResourceRole467: "BPMNProfile_BPMNActivity" = None):
        self.ResourceRole = ResourceRole
        self.BPMNProfile_ResourceRole = BPMNProfile_ResourceRole
        self.BPMNProfile_ResourceRole411 = BPMNProfile_ResourceRole411
        self.BPMNProfile_ResourceRole413 = BPMNProfile_ResourceRole413
        self.BPMNProfile_ResourceRole415 = BPMNProfile_ResourceRole415 if BPMNProfile_ResourceRole415 is not None else set()
        self.resources = resources
        self.BPMNProfile_ResourceRole440 = BPMNProfile_ResourceRole440
        self.BPMNProfile_ResourceRole467 = BPMNProfile_ResourceRole467
        
    @property
    def BPMNProfile_ResourceRole467(self):
        return self.__BPMNProfile_ResourceRole467

    @BPMNProfile_ResourceRole467.setter
    def BPMNProfile_ResourceRole467(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceRole__BPMNProfile_ResourceRole467", None)
        self.__BPMNProfile_ResourceRole467 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNActivity466"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNActivity466", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNActivity466"):
                opp_val = getattr(value, "BPMNProfile_BPMNActivity466", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNActivity466", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_ResourceRole440(self):
        return self.__BPMNProfile_ResourceRole440

    @BPMNProfile_ResourceRole440.setter
    def BPMNProfile_ResourceRole440(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceRole__BPMNProfile_ResourceRole440", None)
        self.__BPMNProfile_ResourceRole440 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_GlobalTask439"):
                opp_val = getattr(old_value, "BPMNProfile_GlobalTask439", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_GlobalTask439"):
                opp_val = getattr(value, "BPMNProfile_GlobalTask439", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_GlobalTask439", set([self]))
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
    def BPMNProfile_ResourceRole413(self):
        return self.__BPMNProfile_ResourceRole413

    @BPMNProfile_ResourceRole413.setter
    def BPMNProfile_ResourceRole413(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceRole__BPMNProfile_ResourceRole413", None)
        self.__BPMNProfile_ResourceRole413 = value
        
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
    def BPMNProfile_ResourceRole415(self):
        return self.__BPMNProfile_ResourceRole415

    @BPMNProfile_ResourceRole415.setter
    def BPMNProfile_ResourceRole415(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceRole__BPMNProfile_ResourceRole415", None)
        self.__BPMNProfile_ResourceRole415 = value if value is not None else set()
        
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
                    

    @property
    def BPMNProfile_ResourceRole411(self):
        return self.__BPMNProfile_ResourceRole411

    @BPMNProfile_ResourceRole411.setter
    def BPMNProfile_ResourceRole411(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceRole__BPMNProfile_ResourceRole411", None)
        self.__BPMNProfile_ResourceRole411 = value
        
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
            if hasattr(old_value, "BPMNProfile_Property409"):
                opp_val = getattr(old_value, "BPMNProfile_Property409", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Property409", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Property409"):
                opp_val = getattr(value, "BPMNProfile_Property409", None)
                setattr(value, "BPMNProfile_Property409", self)

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

    def ResourceRoleprocess(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceRoleprocess method
        pass

    def ResourceRoleresourceRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ResourceRoleresourceRef method
        pass

    def ResourceRoleowner(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ResourceRoleowner method
        pass

    def ResourceRoleisRequired(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ResourceRoleisRequired method
        pass

    def ResourceRoleresourceParameterBindings(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ResourceRoleresourceParameterBindings method
        pass

class BPMNProfile_CorrelationSubscription(BaseElement):

    pass
class BPMNProfile_Rendering(BaseElement):

    pass
class BPMNProfile_InputOutputBinding(BaseElement):

    pass
class BPMNProfile_InputOutputSpecification(BaseElement):

    pass
class BPMNProfile_ComplexBehaviorDefinition(BaseElement):

    pass
class BPMNProfile_LaneSet(BaseElement):

    def __init__(self, LaneSet: "BPMNProfile_FlowElementsContainer" = None, BPMNProfile_LaneSet: "BPMNProfile_ActivityPartition" = None, laneSet: set["BPMNProfile_Lane"] = None, BPMNProfile_LaneSet56: set["BPMNProfile_Lane"] = None, laneSets: "BPMNProfile_FlowElementsContainer" = None, BPMNProfile_LaneSet73: "BPMNProfile_Lane" = None, LaneSet75: "BPMNProfile_Lane" = None, BPMNProfile_LaneSet619: "BPMNProfile_SubProcess" = None):
        self.LaneSet = LaneSet
        self.BPMNProfile_LaneSet = BPMNProfile_LaneSet
        self.laneSet = laneSet if laneSet is not None else set()
        self.BPMNProfile_LaneSet56 = BPMNProfile_LaneSet56 if BPMNProfile_LaneSet56 is not None else set()
        self.laneSets = laneSets
        self.BPMNProfile_LaneSet73 = BPMNProfile_LaneSet73
        self.LaneSet75 = LaneSet75
        self.BPMNProfile_LaneSet619 = BPMNProfile_LaneSet619
        
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

    @property
    def BPMNProfile_LaneSet619(self):
        return self.__BPMNProfile_LaneSet619

    @BPMNProfile_LaneSet619.setter
    def BPMNProfile_LaneSet619(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_LaneSet__BPMNProfile_LaneSet619", None)
        self.__BPMNProfile_LaneSet619 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_SubProcess618"):
                opp_val = getattr(old_value, "BPMNProfile_SubProcess618", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_SubProcess618"):
                opp_val = getattr(value, "BPMNProfile_SubProcess618", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_SubProcess618", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

    def LaneSetlanes(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement LaneSetlanes method
        pass

    def LaneSet(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement LaneSet method
        pass

    def LaneSetparentLane(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement LaneSetparentLane method
        pass

    def LaneSetflowElementsContainer(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement LaneSetflowElementsContainer method
        pass

class BPMNProfile_ResourceParameterBinding(BaseElement):

    def __init__(self, BPMNProfile_ResourceParameterBinding: "BPMNProfile_ResourceRole" = None, BPMNProfile_ResourceParameterBinding429: "BPMNProfile_Slot" = None, BPMNProfile_ResourceParameterBinding432: "BPMNProfile_ResourceParameter" = None, BPMNProfile_ResourceParameterBinding435: "BPMNProfile_BPMNExpression" = None):
        self.BPMNProfile_ResourceParameterBinding = BPMNProfile_ResourceParameterBinding
        self.BPMNProfile_ResourceParameterBinding429 = BPMNProfile_ResourceParameterBinding429
        self.BPMNProfile_ResourceParameterBinding432 = BPMNProfile_ResourceParameterBinding432
        self.BPMNProfile_ResourceParameterBinding435 = BPMNProfile_ResourceParameterBinding435
        
    @property
    def BPMNProfile_ResourceParameterBinding435(self):
        return self.__BPMNProfile_ResourceParameterBinding435

    @BPMNProfile_ResourceParameterBinding435.setter
    def BPMNProfile_ResourceParameterBinding435(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceParameterBinding__BPMNProfile_ResourceParameterBinding435", None)
        self.__BPMNProfile_ResourceParameterBinding435 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNExpression436"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNExpression436", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNExpression436", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNExpression436"):
                opp_val = getattr(value, "BPMNProfile_BPMNExpression436", None)
                setattr(value, "BPMNProfile_BPMNExpression436", self)

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
            if hasattr(old_value, "BPMNProfile_ResourceRole415"):
                opp_val = getattr(old_value, "BPMNProfile_ResourceRole415", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ResourceRole415"):
                opp_val = getattr(value, "BPMNProfile_ResourceRole415", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_ResourceRole415", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_ResourceParameterBinding432(self):
        return self.__BPMNProfile_ResourceParameterBinding432

    @BPMNProfile_ResourceParameterBinding432.setter
    def BPMNProfile_ResourceParameterBinding432(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ResourceParameterBinding__BPMNProfile_ResourceParameterBinding432", None)
        self.__BPMNProfile_ResourceParameterBinding432 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ResourceParameter433"):
                opp_val = getattr(old_value, "BPMNProfile_ResourceParameter433", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ResourceParameter433", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ResourceParameter433"):
                opp_val = getattr(value, "BPMNProfile_ResourceParameter433", None)
                setattr(value, "BPMNProfile_ResourceParameter433", self)

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
            if hasattr(old_value, "BPMNProfile_Slot430"):
                opp_val = getattr(old_value, "BPMNProfile_Slot430", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Slot430", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Slot430"):
                opp_val = getattr(value, "BPMNProfile_Slot430", None)
                setattr(value, "BPMNProfile_Slot430", self)

    def ResourceParameterBindingexpression(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ResourceParameterBindingexpression method
        pass

    def ResourceParameterBindingparameterRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceParameterBindingparameterRef method
        pass

class BPMNProfile_Participant(InteractionNode, BaseElement):

    def __init__(self, BPMNProfile_Participant290: "BPMNProfile_ParticipantAssociation" = None, BPMNProfile_Participant293: "BPMNProfile_ParticipantAssociation" = None, BPMNProfile_Participant: "BPMNProfile_BPMNCollaboration" = None, BPMNProfile_Participant295: "BPMNProfile_Property" = None, BPMNProfile_Participant298: "BPMNProfile_BPMNProcess" = None, BPMNProfile_Participant301: "BPMNProfile_ParticipantMultiplicity" = None, participantRef: set["BPMNProfile_PartnerEntity"] = None, participantRef304: set["BPMNProfile_PartnerRole"] = None, BPMNProfile_Participant306: set["BPMNProfile_BPMNInterface"] = None, Participant: "BPMNProfile_PartnerEntity" = None, Participant329: "BPMNProfile_PartnerRole" = None, BPMNProfile_Participant361: "BPMNProfile_ConversationNode" = None):
        self.BPMNProfile_Participant290 = BPMNProfile_Participant290
        self.BPMNProfile_Participant293 = BPMNProfile_Participant293
        self.BPMNProfile_Participant = BPMNProfile_Participant
        self.BPMNProfile_Participant295 = BPMNProfile_Participant295
        self.BPMNProfile_Participant298 = BPMNProfile_Participant298
        self.BPMNProfile_Participant301 = BPMNProfile_Participant301
        self.participantRef = participantRef if participantRef is not None else set()
        self.participantRef304 = participantRef304 if participantRef304 is not None else set()
        self.BPMNProfile_Participant306 = BPMNProfile_Participant306 if BPMNProfile_Participant306 is not None else set()
        self.Participant = Participant
        self.Participant329 = Participant329
        self.BPMNProfile_Participant361 = BPMNProfile_Participant361
        
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
            if hasattr(old_value, "BPMNProfile_Property296"):
                opp_val = getattr(old_value, "BPMNProfile_Property296", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Property296", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Property296"):
                opp_val = getattr(value, "BPMNProfile_Property296", None)
                setattr(value, "BPMNProfile_Property296", self)

    @property
    def BPMNProfile_Participant306(self):
        return self.__BPMNProfile_Participant306

    @BPMNProfile_Participant306.setter
    def BPMNProfile_Participant306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Participant__BPMNProfile_Participant306", None)
        self.__BPMNProfile_Participant306 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_BPMNInterface307"):
                    opp_val = getattr(item, "BPMNProfile_BPMNInterface307", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_BPMNInterface307", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_BPMNInterface307"):
                    opp_val = getattr(item, "BPMNProfile_BPMNInterface307", None)
                    
                    setattr(item, "BPMNProfile_BPMNInterface307", self)
                    

    @property
    def Participant329(self):
        return self.__Participant329

    @Participant329.setter
    def Participant329(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Participant__Participant329", None)
        self.__Participant329 = value
        
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
    def BPMNProfile_Participant361(self):
        return self.__BPMNProfile_Participant361

    @BPMNProfile_Participant361.setter
    def BPMNProfile_Participant361(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Participant__BPMNProfile_Participant361", None)
        self.__BPMNProfile_Participant361 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ConversationNode360"):
                opp_val = getattr(old_value, "BPMNProfile_ConversationNode360", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ConversationNode360"):
                opp_val = getattr(value, "BPMNProfile_ConversationNode360", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_ConversationNode360", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "BPMNProfile_BPMNCollaboration284"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNCollaboration284", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNCollaboration284"):
                opp_val = getattr(value, "BPMNProfile_BPMNCollaboration284", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNCollaboration284", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_Participant301(self):
        return self.__BPMNProfile_Participant301

    @BPMNProfile_Participant301.setter
    def BPMNProfile_Participant301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Participant__BPMNProfile_Participant301", None)
        self.__BPMNProfile_Participant301 = value
        
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

    @property
    def participantRef304(self):
        return self.__participantRef304

    @participantRef304.setter
    def participantRef304(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Participant__participantRef304", None)
        self.__participantRef304 = value if value is not None else set()
        
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
    def BPMNProfile_Participant293(self):
        return self.__BPMNProfile_Participant293

    @BPMNProfile_Participant293.setter
    def BPMNProfile_Participant293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Participant__BPMNProfile_Participant293", None)
        self.__BPMNProfile_Participant293 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ParticipantAssociation292"):
                opp_val = getattr(old_value, "BPMNProfile_ParticipantAssociation292", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ParticipantAssociation292", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ParticipantAssociation292"):
                opp_val = getattr(value, "BPMNProfile_ParticipantAssociation292", None)
                setattr(value, "BPMNProfile_ParticipantAssociation292", self)

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
    def BPMNProfile_Participant298(self):
        return self.__BPMNProfile_Participant298

    @BPMNProfile_Participant298.setter
    def BPMNProfile_Participant298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Participant__BPMNProfile_Participant298", None)
        self.__BPMNProfile_Participant298 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNProcess299"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNProcess299", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNProcess299", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNProcess299"):
                opp_val = getattr(value, "BPMNProfile_BPMNProcess299", None)
                setattr(value, "BPMNProfile_BPMNProcess299", self)

    @property
    def BPMNProfile_Participant290(self):
        return self.__BPMNProfile_Participant290

    @BPMNProfile_Participant290.setter
    def BPMNProfile_Participant290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Participant__BPMNProfile_Participant290", None)
        self.__BPMNProfile_Participant290 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ParticipantAssociation289"):
                opp_val = getattr(old_value, "BPMNProfile_ParticipantAssociation289", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ParticipantAssociation289", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ParticipantAssociation289"):
                opp_val = getattr(value, "BPMNProfile_ParticipantAssociation289", None)
                setattr(value, "BPMNProfile_ParticipantAssociation289", self)

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

    def participantpartnerEntityRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement participantpartnerEntityRef method
        pass

    def Participantrealizationsupplier(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement Participantrealizationsupplier method
        pass

    def Participantownership(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement Participantownership method
        pass

    def ParticipantinterfaceRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ParticipantinterfaceRefs method
        pass

    def ParticipantmultiplicityMaximum(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ParticipantmultiplicityMaximum method
        pass

    def Participanttype(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement Participanttype method
        pass

    def participantpartnerRoleRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement participantpartnerRoleRef method
        pass

    def ParticipantmultiplicityMinimum(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ParticipantmultiplicityMinimum method
        pass

    def ParticipantprocessRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ParticipantprocessRef method
        pass

class BPMNProfile_Auditing(BaseElement):

    pass
class BPMNProfile_BPMNOperation(BaseElement):

    def __init__(self, BPMNProfile_BPMNOperation: "BPMNProfile_BPMNInterface" = None, BPMNProfile_BPMNOperation244: "BPMNProfile_Operation" = None, BPMNProfile_BPMNOperation246: "BPMNProfile_Element" = None, BPMNProfile_BPMNOperation249: "BPMNProfile_BPMNMessage" = None, BPMNProfile_BPMNOperation266: "BPMNProfile_InputOutputBinding" = None, BPMNProfile_BPMNOperation251: "BPMNProfile_BPMNMessage" = None, BPMNProfile_BPMNOperation254: set["BPMNProfile_Error"] = None, BPMNProfile_BPMNOperation541: "BPMNProfile_MessageEventDefinition" = None, BPMNProfile_BPMNOperation644: "BPMNProfile_SendTask" = None, BPMNProfile_BPMNOperation656: "BPMNProfile_ReceiveTask" = None, BPMNProfile_BPMNOperation661: "BPMNProfile_ServiceTask" = None):
        self.BPMNProfile_BPMNOperation = BPMNProfile_BPMNOperation
        self.BPMNProfile_BPMNOperation244 = BPMNProfile_BPMNOperation244
        self.BPMNProfile_BPMNOperation246 = BPMNProfile_BPMNOperation246
        self.BPMNProfile_BPMNOperation249 = BPMNProfile_BPMNOperation249
        self.BPMNProfile_BPMNOperation266 = BPMNProfile_BPMNOperation266
        self.BPMNProfile_BPMNOperation251 = BPMNProfile_BPMNOperation251
        self.BPMNProfile_BPMNOperation254 = BPMNProfile_BPMNOperation254 if BPMNProfile_BPMNOperation254 is not None else set()
        self.BPMNProfile_BPMNOperation541 = BPMNProfile_BPMNOperation541
        self.BPMNProfile_BPMNOperation644 = BPMNProfile_BPMNOperation644
        self.BPMNProfile_BPMNOperation656 = BPMNProfile_BPMNOperation656
        self.BPMNProfile_BPMNOperation661 = BPMNProfile_BPMNOperation661
        
    @property
    def BPMNProfile_BPMNOperation644(self):
        return self.__BPMNProfile_BPMNOperation644

    @BPMNProfile_BPMNOperation644.setter
    def BPMNProfile_BPMNOperation644(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNOperation__BPMNProfile_BPMNOperation644", None)
        self.__BPMNProfile_BPMNOperation644 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_SendTask643"):
                opp_val = getattr(old_value, "BPMNProfile_SendTask643", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_SendTask643", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_SendTask643"):
                opp_val = getattr(value, "BPMNProfile_SendTask643", None)
                setattr(value, "BPMNProfile_SendTask643", self)

    @property
    def BPMNProfile_BPMNOperation244(self):
        return self.__BPMNProfile_BPMNOperation244

    @BPMNProfile_BPMNOperation244.setter
    def BPMNProfile_BPMNOperation244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNOperation__BPMNProfile_BPMNOperation244", None)
        self.__BPMNProfile_BPMNOperation244 = value
        
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
    def BPMNProfile_BPMNOperation254(self):
        return self.__BPMNProfile_BPMNOperation254

    @BPMNProfile_BPMNOperation254.setter
    def BPMNProfile_BPMNOperation254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNOperation__BPMNProfile_BPMNOperation254", None)
        self.__BPMNProfile_BPMNOperation254 = value if value is not None else set()
        
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
    def BPMNProfile_BPMNOperation249(self):
        return self.__BPMNProfile_BPMNOperation249

    @BPMNProfile_BPMNOperation249.setter
    def BPMNProfile_BPMNOperation249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNOperation__BPMNProfile_BPMNOperation249", None)
        self.__BPMNProfile_BPMNOperation249 = value
        
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
    def BPMNProfile_BPMNOperation661(self):
        return self.__BPMNProfile_BPMNOperation661

    @BPMNProfile_BPMNOperation661.setter
    def BPMNProfile_BPMNOperation661(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNOperation__BPMNProfile_BPMNOperation661", None)
        self.__BPMNProfile_BPMNOperation661 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ServiceTask660"):
                opp_val = getattr(old_value, "BPMNProfile_ServiceTask660", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ServiceTask660", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ServiceTask660"):
                opp_val = getattr(value, "BPMNProfile_ServiceTask660", None)
                setattr(value, "BPMNProfile_ServiceTask660", self)

    @property
    def BPMNProfile_BPMNOperation656(self):
        return self.__BPMNProfile_BPMNOperation656

    @BPMNProfile_BPMNOperation656.setter
    def BPMNProfile_BPMNOperation656(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNOperation__BPMNProfile_BPMNOperation656", None)
        self.__BPMNProfile_BPMNOperation656 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ReceiveTask655"):
                opp_val = getattr(old_value, "BPMNProfile_ReceiveTask655", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ReceiveTask655", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ReceiveTask655"):
                opp_val = getattr(value, "BPMNProfile_ReceiveTask655", None)
                setattr(value, "BPMNProfile_ReceiveTask655", self)

    @property
    def BPMNProfile_BPMNOperation541(self):
        return self.__BPMNProfile_BPMNOperation541

    @BPMNProfile_BPMNOperation541.setter
    def BPMNProfile_BPMNOperation541(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNOperation__BPMNProfile_BPMNOperation541", None)
        self.__BPMNProfile_BPMNOperation541 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_MessageEventDefinition540"):
                opp_val = getattr(old_value, "BPMNProfile_MessageEventDefinition540", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_MessageEventDefinition540", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_MessageEventDefinition540"):
                opp_val = getattr(value, "BPMNProfile_MessageEventDefinition540", None)
                setattr(value, "BPMNProfile_MessageEventDefinition540", self)

    @property
    def BPMNProfile_BPMNOperation251(self):
        return self.__BPMNProfile_BPMNOperation251

    @BPMNProfile_BPMNOperation251.setter
    def BPMNProfile_BPMNOperation251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNOperation__BPMNProfile_BPMNOperation251", None)
        self.__BPMNProfile_BPMNOperation251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNMessage252"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNMessage252", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNMessage252", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNMessage252"):
                opp_val = getattr(value, "BPMNProfile_BPMNMessage252", None)
                setattr(value, "BPMNProfile_BPMNMessage252", self)

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
            if hasattr(old_value, "BPMNProfile_BPMNInterface239"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNInterface239", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNInterface239"):
                opp_val = getattr(value, "BPMNProfile_BPMNInterface239", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNInterface239", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_BPMNOperation246(self):
        return self.__BPMNProfile_BPMNOperation246

    @BPMNProfile_BPMNOperation246.setter
    def BPMNProfile_BPMNOperation246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNOperation__BPMNProfile_BPMNOperation246", None)
        self.__BPMNProfile_BPMNOperation246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Element247"):
                opp_val = getattr(old_value, "BPMNProfile_Element247", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Element247", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Element247"):
                opp_val = getattr(value, "BPMNProfile_Element247", None)
                setattr(value, "BPMNProfile_Element247", self)

    @property
    def BPMNProfile_BPMNOperation266(self):
        return self.__BPMNProfile_BPMNOperation266

    @BPMNProfile_BPMNOperation266.setter
    def BPMNProfile_BPMNOperation266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNOperation__BPMNProfile_BPMNOperation266", None)
        self.__BPMNProfile_BPMNOperation266 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_InputOutputBinding265"):
                opp_val = getattr(old_value, "BPMNProfile_InputOutputBinding265", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_InputOutputBinding265", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_InputOutputBinding265"):
                opp_val = getattr(value, "BPMNProfile_InputOutputBinding265", None)
                setattr(value, "BPMNProfile_InputOutputBinding265", self)

    def BPMNOperationinMessageRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement BPMNOperationinMessageRef method
        pass

    def BPMNOperationowner(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement BPMNOperationowner method
        pass

    def BPMNOperationerrorRefs(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BPMNOperationerrorRefs method
        pass

    def BPMNOperationoutMessageRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BPMNOperationoutMessageRef method
        pass

class BPMNProfile_LoopCharacteristics(BaseElement):

    pass
class BPMNProfile_CategoryValue(BaseElement):

    pass
class BPMNProfile_CorrelationProperty(BaseElement):

    pass
class BPMNProfile_ItemAwareElement(BaseElement):

    def __init__(self, BPMNProfile_ItemAwareElement: set["BPMNProfile_DataState"] = None, BPMNProfile_ItemAwareElement187: "BPMNProfile_TypedElement" = None, BPMNProfile_ItemAwareElement189: "BPMNProfile_ItemDefinition" = None, BPMNProfile_ItemAwareElement491: "BPMNProfile_DataAssociation" = None, BPMNProfile_ItemAwareElement494: "BPMNProfile_DataAssociation" = None, BPMNProfile_ItemAwareElement671: "BPMNProfile_MultiInstanceLoopCharacteristics" = None, BPMNProfile_ItemAwareElement674: "BPMNProfile_MultiInstanceLoopCharacteristics" = None):
        self.BPMNProfile_ItemAwareElement = BPMNProfile_ItemAwareElement if BPMNProfile_ItemAwareElement is not None else set()
        self.BPMNProfile_ItemAwareElement187 = BPMNProfile_ItemAwareElement187
        self.BPMNProfile_ItemAwareElement189 = BPMNProfile_ItemAwareElement189
        self.BPMNProfile_ItemAwareElement491 = BPMNProfile_ItemAwareElement491
        self.BPMNProfile_ItemAwareElement494 = BPMNProfile_ItemAwareElement494
        self.BPMNProfile_ItemAwareElement671 = BPMNProfile_ItemAwareElement671
        self.BPMNProfile_ItemAwareElement674 = BPMNProfile_ItemAwareElement674
        
    @property
    def BPMNProfile_ItemAwareElement671(self):
        return self.__BPMNProfile_ItemAwareElement671

    @BPMNProfile_ItemAwareElement671.setter
    def BPMNProfile_ItemAwareElement671(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemAwareElement__BPMNProfile_ItemAwareElement671", None)
        self.__BPMNProfile_ItemAwareElement671 = value
        
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
    def BPMNProfile_ItemAwareElement491(self):
        return self.__BPMNProfile_ItemAwareElement491

    @BPMNProfile_ItemAwareElement491.setter
    def BPMNProfile_ItemAwareElement491(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemAwareElement__BPMNProfile_ItemAwareElement491", None)
        self.__BPMNProfile_ItemAwareElement491 = value
        
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
    def BPMNProfile_ItemAwareElement494(self):
        return self.__BPMNProfile_ItemAwareElement494

    @BPMNProfile_ItemAwareElement494.setter
    def BPMNProfile_ItemAwareElement494(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemAwareElement__BPMNProfile_ItemAwareElement494", None)
        self.__BPMNProfile_ItemAwareElement494 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_DataAssociation493"):
                opp_val = getattr(old_value, "BPMNProfile_DataAssociation493", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_DataAssociation493", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_DataAssociation493"):
                opp_val = getattr(value, "BPMNProfile_DataAssociation493", None)
                setattr(value, "BPMNProfile_DataAssociation493", self)

    @property
    def BPMNProfile_ItemAwareElement189(self):
        return self.__BPMNProfile_ItemAwareElement189

    @BPMNProfile_ItemAwareElement189.setter
    def BPMNProfile_ItemAwareElement189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemAwareElement__BPMNProfile_ItemAwareElement189", None)
        self.__BPMNProfile_ItemAwareElement189 = value
        
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
    def BPMNProfile_ItemAwareElement187(self):
        return self.__BPMNProfile_ItemAwareElement187

    @BPMNProfile_ItemAwareElement187.setter
    def BPMNProfile_ItemAwareElement187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemAwareElement__BPMNProfile_ItemAwareElement187", None)
        self.__BPMNProfile_ItemAwareElement187 = value
        
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
    def BPMNProfile_ItemAwareElement674(self):
        return self.__BPMNProfile_ItemAwareElement674

    @BPMNProfile_ItemAwareElement674.setter
    def BPMNProfile_ItemAwareElement674(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ItemAwareElement__BPMNProfile_ItemAwareElement674", None)
        self.__BPMNProfile_ItemAwareElement674 = value
        
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

    def ItemAwareElementdataState(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ItemAwareElementdataState method
        pass

class BPMNProfile_Definitions(BaseElement):

    def __init__(self, targetNamespace: str, expressionLanguage: str, typeLanguage: str, exporter: str, exporterVersion: str, Definitions: "BPMNProfile_RootElement" = None, BPMNProfile_Definitions: "BPMNProfile_Package" = None, BPMNProfile_Definitions109: set["BPMNProfile_BPMNExtension"] = None, BPMNProfile_Definitions111: set["BPMNProfile_Import"] = None, BPMNProfile_Definitions113: set["BPMNProfile_BPMNRelationship"] = None, definition: set["BPMNProfile_RootElement"] = None, BPMNProfile_Definitions125: "BPMNProfile_Import" = None, BPMNProfile_Definitions136: "BPMNProfile_BPMNRelationship" = None):
        self.targetNamespace = targetNamespace
        self.expressionLanguage = expressionLanguage
        self.typeLanguage = typeLanguage
        self.exporter = exporter
        self.exporterVersion = exporterVersion
        self.Definitions = Definitions
        self.BPMNProfile_Definitions = BPMNProfile_Definitions
        self.BPMNProfile_Definitions109 = BPMNProfile_Definitions109 if BPMNProfile_Definitions109 is not None else set()
        self.BPMNProfile_Definitions111 = BPMNProfile_Definitions111 if BPMNProfile_Definitions111 is not None else set()
        self.BPMNProfile_Definitions113 = BPMNProfile_Definitions113 if BPMNProfile_Definitions113 is not None else set()
        self.definition = definition if definition is not None else set()
        self.BPMNProfile_Definitions125 = BPMNProfile_Definitions125
        self.BPMNProfile_Definitions136 = BPMNProfile_Definitions136
        
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
    def expressionLanguage(self) -> str:
        return self.__expressionLanguage

    @expressionLanguage.setter
    def expressionLanguage(self, expressionLanguage: str):
        self.__expressionLanguage = expressionLanguage

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
    def BPMNProfile_Definitions113(self):
        return self.__BPMNProfile_Definitions113

    @BPMNProfile_Definitions113.setter
    def BPMNProfile_Definitions113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Definitions__BPMNProfile_Definitions113", None)
        self.__BPMNProfile_Definitions113 = value if value is not None else set()
        
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
    def BPMNProfile_Definitions111(self):
        return self.__BPMNProfile_Definitions111

    @BPMNProfile_Definitions111.setter
    def BPMNProfile_Definitions111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Definitions__BPMNProfile_Definitions111", None)
        self.__BPMNProfile_Definitions111 = value if value is not None else set()
        
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
    def BPMNProfile_Definitions109(self):
        return self.__BPMNProfile_Definitions109

    @BPMNProfile_Definitions109.setter
    def BPMNProfile_Definitions109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Definitions__BPMNProfile_Definitions109", None)
        self.__BPMNProfile_Definitions109 = value if value is not None else set()
        
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
                    

    @property
    def BPMNProfile_Definitions136(self):
        return self.__BPMNProfile_Definitions136

    @BPMNProfile_Definitions136.setter
    def BPMNProfile_Definitions136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Definitions__BPMNProfile_Definitions136", None)
        self.__BPMNProfile_Definitions136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNRelationship135"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNRelationship135", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNRelationship135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNRelationship135"):
                opp_val = getattr(value, "BPMNProfile_BPMNRelationship135", None)
                setattr(value, "BPMNProfile_BPMNRelationship135", self)

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
    def BPMNProfile_Definitions125(self):
        return self.__BPMNProfile_Definitions125

    @BPMNProfile_Definitions125.setter
    def BPMNProfile_Definitions125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_Definitions__BPMNProfile_Definitions125", None)
        self.__BPMNProfile_Definitions125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Import124"):
                opp_val = getattr(old_value, "BPMNProfile_Import124", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Import124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Import124"):
                opp_val = getattr(value, "BPMNProfile_Import124", None)
                setattr(value, "BPMNProfile_Import124", self)

class BPMNProfile_Documentation(BaseElement):

    def __init__(self, textFormat: str, text: str, BPMNProfile_Documentation: "BPMNProfile_BaseElement" = None, BPMNProfile_Documentation33: "BPMNProfile_Comment" = None):
        self.textFormat = textFormat
        self.text = text
        self.BPMNProfile_Documentation = BPMNProfile_Documentation
        self.BPMNProfile_Documentation33 = BPMNProfile_Documentation33
        
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

class BPMNProfile_InputSet(BaseElement):

    def __init__(self, BPMNProfile_InputSet: "BPMNProfile_InputOutputSpecification" = None, InputSet: "BPMNProfile_DataInput" = None, InputSet182: "BPMNProfile_DataInput" = None, InputSet184: "BPMNProfile_DataInput" = None, BPMNProfile_InputSet202: "BPMNProfile_ParameterSet" = None, inputSetWithOptional: set["BPMNProfile_DataInput"] = None, inputSetWithWhileExecuting: set["BPMNProfile_DataInput"] = None, inputSetRefs: set["BPMNProfile_DataInput"] = None, BPMNProfile_InputSet260: "BPMNProfile_InputOutputBinding" = None):
        self.BPMNProfile_InputSet = BPMNProfile_InputSet
        self.InputSet = InputSet
        self.InputSet182 = InputSet182
        self.InputSet184 = InputSet184
        self.BPMNProfile_InputSet202 = BPMNProfile_InputSet202
        self.inputSetWithOptional = inputSetWithOptional if inputSetWithOptional is not None else set()
        self.inputSetWithWhileExecuting = inputSetWithWhileExecuting if inputSetWithWhileExecuting is not None else set()
        self.inputSetRefs = inputSetRefs if inputSetRefs is not None else set()
        self.BPMNProfile_InputSet260 = BPMNProfile_InputSet260
        
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
                if hasattr(item, "DataInput207"):
                    opp_val = getattr(item, "DataInput207", None)
                    
                    if opp_val == self:
                        setattr(item, "DataInput207", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataInput207"):
                    opp_val = getattr(item, "DataInput207", None)
                    
                    setattr(item, "DataInput207", self)
                    

    @property
    def BPMNProfile_InputSet260(self):
        return self.__BPMNProfile_InputSet260

    @BPMNProfile_InputSet260.setter
    def BPMNProfile_InputSet260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_InputSet__BPMNProfile_InputSet260", None)
        self.__BPMNProfile_InputSet260 = value
        
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
    def BPMNProfile_InputSet202(self):
        return self.__BPMNProfile_InputSet202

    @BPMNProfile_InputSet202.setter
    def BPMNProfile_InputSet202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_InputSet__BPMNProfile_InputSet202", None)
        self.__BPMNProfile_InputSet202 = value
        
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
    def BPMNProfile_InputSet(self):
        return self.__BPMNProfile_InputSet

    @BPMNProfile_InputSet.setter
    def BPMNProfile_InputSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_InputSet__BPMNProfile_InputSet", None)
        self.__BPMNProfile_InputSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_InputOutputSpecification171"):
                opp_val = getattr(old_value, "BPMNProfile_InputOutputSpecification171", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_InputOutputSpecification171"):
                opp_val = getattr(value, "BPMNProfile_InputOutputSpecification171", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_InputOutputSpecification171", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def InputSet182(self):
        return self.__InputSet182

    @InputSet182.setter
    def InputSet182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_InputSet__InputSet182", None)
        self.__InputSet182 = value
        
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
                if hasattr(item, "DataInput205"):
                    opp_val = getattr(item, "DataInput205", None)
                    
                    if opp_val == self:
                        setattr(item, "DataInput205", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataInput205"):
                    opp_val = getattr(item, "DataInput205", None)
                    
                    setattr(item, "DataInput205", self)
                    

    @property
    def InputSet184(self):
        return self.__InputSet184

    @InputSet184.setter
    def InputSet184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_InputSet__InputSet184", None)
        self.__InputSet184 = value
        
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

    def InputSetdataInputRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement InputSetdataInputRefs method
        pass

    def InputSetwhileExecutingInputRefs(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement InputSetwhileExecutingInputRefs method
        pass

    def InputSetoptionalInputRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement InputSetoptionalInputRefs method
        pass

class BPMNProfile_MessageFlowAssociation(BaseElement):

    def __init__(self, BPMNProfile_MessageFlowAssociation: "BPMNProfile_BPMNCollaboration" = None, BPMNProfile_MessageFlowAssociation331: "BPMNProfile_Dependency" = None, BPMNProfile_MessageFlowAssociation334: "BPMNProfile_MessageFlow" = None, BPMNProfile_MessageFlowAssociation337: "BPMNProfile_MessageFlow" = None):
        self.BPMNProfile_MessageFlowAssociation = BPMNProfile_MessageFlowAssociation
        self.BPMNProfile_MessageFlowAssociation331 = BPMNProfile_MessageFlowAssociation331
        self.BPMNProfile_MessageFlowAssociation334 = BPMNProfile_MessageFlowAssociation334
        self.BPMNProfile_MessageFlowAssociation337 = BPMNProfile_MessageFlowAssociation337
        
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
    def BPMNProfile_MessageFlowAssociation331(self):
        return self.__BPMNProfile_MessageFlowAssociation331

    @BPMNProfile_MessageFlowAssociation331.setter
    def BPMNProfile_MessageFlowAssociation331(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MessageFlowAssociation__BPMNProfile_MessageFlowAssociation331", None)
        self.__BPMNProfile_MessageFlowAssociation331 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Dependency332"):
                opp_val = getattr(old_value, "BPMNProfile_Dependency332", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Dependency332", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Dependency332"):
                opp_val = getattr(value, "BPMNProfile_Dependency332", None)
                setattr(value, "BPMNProfile_Dependency332", self)

    @property
    def BPMNProfile_MessageFlowAssociation334(self):
        return self.__BPMNProfile_MessageFlowAssociation334

    @BPMNProfile_MessageFlowAssociation334.setter
    def BPMNProfile_MessageFlowAssociation334(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MessageFlowAssociation__BPMNProfile_MessageFlowAssociation334", None)
        self.__BPMNProfile_MessageFlowAssociation334 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_MessageFlow335"):
                opp_val = getattr(old_value, "BPMNProfile_MessageFlow335", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_MessageFlow335", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_MessageFlow335"):
                opp_val = getattr(value, "BPMNProfile_MessageFlow335", None)
                setattr(value, "BPMNProfile_MessageFlow335", self)

    @property
    def BPMNProfile_MessageFlowAssociation337(self):
        return self.__BPMNProfile_MessageFlowAssociation337

    @BPMNProfile_MessageFlowAssociation337.setter
    def BPMNProfile_MessageFlowAssociation337(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MessageFlowAssociation__BPMNProfile_MessageFlowAssociation337", None)
        self.__BPMNProfile_MessageFlowAssociation337 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_MessageFlow338"):
                opp_val = getattr(old_value, "BPMNProfile_MessageFlow338", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_MessageFlow338", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_MessageFlow338"):
                opp_val = getattr(value, "BPMNProfile_MessageFlow338", None)
                setattr(value, "BPMNProfile_MessageFlow338", self)

    def MessageFlowAssociationouterMessageFlowRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MessageFlowAssociationouterMessageFlowRef method
        pass

    def MessageFlowAssociationinnerMessageFlowRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MessageFlowAssociationinnerMessageFlowRef method
        pass

class BPMNProfile_BPMNArtifact(BaseElement):

    pass
class BPMNProfile_DataState(BaseElement):

    pass
class BPMNProfile_CorrelationPropertyBinding(BaseElement):

    pass
class BPMNProfile_OutputSet(BaseElement):

    def __init__(self, BPMNProfile_OutputSet: "BPMNProfile_InputOutputSpecification" = None, OutputSet: "BPMNProfile_DataOutput" = None, BPMNProfile_OutputSet219: "BPMNProfile_DataOutput" = None, BPMNProfile_OutputSet222: "BPMNProfile_DataOutput" = None, BPMNProfile_OutputSet224: "BPMNProfile_ParameterSet" = None, BPMNProfile_OutputSet227: set["BPMNProfile_DataOutput"] = None, BPMNProfile_OutputSet230: set["BPMNProfile_DataOutput"] = None, outputSetRefs: set["BPMNProfile_DataOutput"] = None, BPMNProfile_OutputSet263: "BPMNProfile_InputOutputBinding" = None):
        self.BPMNProfile_OutputSet = BPMNProfile_OutputSet
        self.OutputSet = OutputSet
        self.BPMNProfile_OutputSet219 = BPMNProfile_OutputSet219
        self.BPMNProfile_OutputSet222 = BPMNProfile_OutputSet222
        self.BPMNProfile_OutputSet224 = BPMNProfile_OutputSet224
        self.BPMNProfile_OutputSet227 = BPMNProfile_OutputSet227 if BPMNProfile_OutputSet227 is not None else set()
        self.BPMNProfile_OutputSet230 = BPMNProfile_OutputSet230 if BPMNProfile_OutputSet230 is not None else set()
        self.outputSetRefs = outputSetRefs if outputSetRefs is not None else set()
        self.BPMNProfile_OutputSet263 = BPMNProfile_OutputSet263
        
    @property
    def BPMNProfile_OutputSet227(self):
        return self.__BPMNProfile_OutputSet227

    @BPMNProfile_OutputSet227.setter
    def BPMNProfile_OutputSet227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_OutputSet__BPMNProfile_OutputSet227", None)
        self.__BPMNProfile_OutputSet227 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_DataOutput228"):
                    opp_val = getattr(item, "BPMNProfile_DataOutput228", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_DataOutput228", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_DataOutput228"):
                    opp_val = getattr(item, "BPMNProfile_DataOutput228", None)
                    
                    setattr(item, "BPMNProfile_DataOutput228", self)
                    

    @property
    def BPMNProfile_OutputSet219(self):
        return self.__BPMNProfile_OutputSet219

    @BPMNProfile_OutputSet219.setter
    def BPMNProfile_OutputSet219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_OutputSet__BPMNProfile_OutputSet219", None)
        self.__BPMNProfile_OutputSet219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_DataOutput218"):
                opp_val = getattr(old_value, "BPMNProfile_DataOutput218", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_DataOutput218"):
                opp_val = getattr(value, "BPMNProfile_DataOutput218", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_DataOutput218", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_OutputSet222(self):
        return self.__BPMNProfile_OutputSet222

    @BPMNProfile_OutputSet222.setter
    def BPMNProfile_OutputSet222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_OutputSet__BPMNProfile_OutputSet222", None)
        self.__BPMNProfile_OutputSet222 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_DataOutput221"):
                opp_val = getattr(old_value, "BPMNProfile_DataOutput221", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_DataOutput221"):
                opp_val = getattr(value, "BPMNProfile_DataOutput221", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_DataOutput221", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "BPMNProfile_InputOutputSpecification173"):
                opp_val = getattr(old_value, "BPMNProfile_InputOutputSpecification173", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_InputOutputSpecification173"):
                opp_val = getattr(value, "BPMNProfile_InputOutputSpecification173", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_InputOutputSpecification173", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_OutputSet263(self):
        return self.__BPMNProfile_OutputSet263

    @BPMNProfile_OutputSet263.setter
    def BPMNProfile_OutputSet263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_OutputSet__BPMNProfile_OutputSet263", None)
        self.__BPMNProfile_OutputSet263 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_InputOutputBinding262"):
                opp_val = getattr(old_value, "BPMNProfile_InputOutputBinding262", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_InputOutputBinding262", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_InputOutputBinding262"):
                opp_val = getattr(value, "BPMNProfile_InputOutputBinding262", None)
                setattr(value, "BPMNProfile_InputOutputBinding262", self)

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
    def BPMNProfile_OutputSet230(self):
        return self.__BPMNProfile_OutputSet230

    @BPMNProfile_OutputSet230.setter
    def BPMNProfile_OutputSet230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_OutputSet__BPMNProfile_OutputSet230", None)
        self.__BPMNProfile_OutputSet230 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_DataOutput231"):
                    opp_val = getattr(item, "BPMNProfile_DataOutput231", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_DataOutput231", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_DataOutput231"):
                    opp_val = getattr(item, "BPMNProfile_DataOutput231", None)
                    
                    setattr(item, "BPMNProfile_DataOutput231", self)
                    

    @property
    def BPMNProfile_OutputSet224(self):
        return self.__BPMNProfile_OutputSet224

    @BPMNProfile_OutputSet224.setter
    def BPMNProfile_OutputSet224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_OutputSet__BPMNProfile_OutputSet224", None)
        self.__BPMNProfile_OutputSet224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ParameterSet225"):
                opp_val = getattr(old_value, "BPMNProfile_ParameterSet225", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ParameterSet225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ParameterSet225"):
                opp_val = getattr(value, "BPMNProfile_ParameterSet225", None)
                setattr(value, "BPMNProfile_ParameterSet225", self)

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
                    

    def OutputSetoptionalOutputRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement OutputSetoptionalOutputRefs method
        pass

    def OutputSetdataOutputRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement OutputSetdataOutputRefs method
        pass

    def OutputSetwhileExecutingOutputRefs(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement OutputSetwhileExecutingOutputRefs method
        pass

class BPMNProfile_ConversationLink(BaseElement):

    pass
class BPMNProfile_MessageFlow(BaseElement):

    def __init__(self, BPMNProfile_MessageFlow: "BPMNProfile_BPMNCollaboration" = None, BPMNProfile_MessageFlow335: "BPMNProfile_MessageFlowAssociation" = None, BPMNProfile_MessageFlow338: "BPMNProfile_MessageFlowAssociation" = None, BPMNProfile_MessageFlow340: "BPMNProfile_InformationFlow" = None, BPMNProfile_MessageFlow342: "BPMNProfile_InteractionNode" = None, BPMNProfile_MessageFlow345: "BPMNProfile_InteractionNode" = None, BPMNProfile_MessageFlow348: "BPMNProfile_BPMNMessage" = None, BPMNProfile_MessageFlow355: "BPMNProfile_ConversationNode" = None):
        self.BPMNProfile_MessageFlow = BPMNProfile_MessageFlow
        self.BPMNProfile_MessageFlow335 = BPMNProfile_MessageFlow335
        self.BPMNProfile_MessageFlow338 = BPMNProfile_MessageFlow338
        self.BPMNProfile_MessageFlow340 = BPMNProfile_MessageFlow340
        self.BPMNProfile_MessageFlow342 = BPMNProfile_MessageFlow342
        self.BPMNProfile_MessageFlow345 = BPMNProfile_MessageFlow345
        self.BPMNProfile_MessageFlow348 = BPMNProfile_MessageFlow348
        self.BPMNProfile_MessageFlow355 = BPMNProfile_MessageFlow355
        
    @property
    def BPMNProfile_MessageFlow345(self):
        return self.__BPMNProfile_MessageFlow345

    @BPMNProfile_MessageFlow345.setter
    def BPMNProfile_MessageFlow345(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MessageFlow__BPMNProfile_MessageFlow345", None)
        self.__BPMNProfile_MessageFlow345 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_InteractionNode346"):
                opp_val = getattr(old_value, "BPMNProfile_InteractionNode346", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_InteractionNode346", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_InteractionNode346"):
                opp_val = getattr(value, "BPMNProfile_InteractionNode346", None)
                setattr(value, "BPMNProfile_InteractionNode346", self)

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
            if hasattr(old_value, "BPMNProfile_BPMNCollaboration276"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNCollaboration276", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNCollaboration276"):
                opp_val = getattr(value, "BPMNProfile_BPMNCollaboration276", None)
                if opp_val is None:
                    setattr(value, "BPMNProfile_BPMNCollaboration276", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMNProfile_MessageFlow355(self):
        return self.__BPMNProfile_MessageFlow355

    @BPMNProfile_MessageFlow355.setter
    def BPMNProfile_MessageFlow355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MessageFlow__BPMNProfile_MessageFlow355", None)
        self.__BPMNProfile_MessageFlow355 = value
        
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
    def BPMNProfile_MessageFlow342(self):
        return self.__BPMNProfile_MessageFlow342

    @BPMNProfile_MessageFlow342.setter
    def BPMNProfile_MessageFlow342(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MessageFlow__BPMNProfile_MessageFlow342", None)
        self.__BPMNProfile_MessageFlow342 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_InteractionNode343"):
                opp_val = getattr(old_value, "BPMNProfile_InteractionNode343", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_InteractionNode343", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_InteractionNode343"):
                opp_val = getattr(value, "BPMNProfile_InteractionNode343", None)
                setattr(value, "BPMNProfile_InteractionNode343", self)

    @property
    def BPMNProfile_MessageFlow335(self):
        return self.__BPMNProfile_MessageFlow335

    @BPMNProfile_MessageFlow335.setter
    def BPMNProfile_MessageFlow335(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MessageFlow__BPMNProfile_MessageFlow335", None)
        self.__BPMNProfile_MessageFlow335 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_MessageFlowAssociation334"):
                opp_val = getattr(old_value, "BPMNProfile_MessageFlowAssociation334", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_MessageFlowAssociation334", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_MessageFlowAssociation334"):
                opp_val = getattr(value, "BPMNProfile_MessageFlowAssociation334", None)
                setattr(value, "BPMNProfile_MessageFlowAssociation334", self)

    @property
    def BPMNProfile_MessageFlow340(self):
        return self.__BPMNProfile_MessageFlow340

    @BPMNProfile_MessageFlow340.setter
    def BPMNProfile_MessageFlow340(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MessageFlow__BPMNProfile_MessageFlow340", None)
        self.__BPMNProfile_MessageFlow340 = value
        
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
    def BPMNProfile_MessageFlow338(self):
        return self.__BPMNProfile_MessageFlow338

    @BPMNProfile_MessageFlow338.setter
    def BPMNProfile_MessageFlow338(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MessageFlow__BPMNProfile_MessageFlow338", None)
        self.__BPMNProfile_MessageFlow338 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_MessageFlowAssociation337"):
                opp_val = getattr(old_value, "BPMNProfile_MessageFlowAssociation337", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_MessageFlowAssociation337", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_MessageFlowAssociation337"):
                opp_val = getattr(value, "BPMNProfile_MessageFlowAssociation337", None)
                setattr(value, "BPMNProfile_MessageFlowAssociation337", self)

    @property
    def BPMNProfile_MessageFlow348(self):
        return self.__BPMNProfile_MessageFlow348

    @BPMNProfile_MessageFlow348.setter
    def BPMNProfile_MessageFlow348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_MessageFlow__BPMNProfile_MessageFlow348", None)
        self.__BPMNProfile_MessageFlow348 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNMessage349"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNMessage349", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNMessage349", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNMessage349"):
                opp_val = getattr(value, "BPMNProfile_BPMNMessage349", None)
                setattr(value, "BPMNProfile_BPMNMessage349", self)

    def MessageFlowmessageRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MessageFlowmessageRef method
        pass

    def MessageFlowsourceRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MessageFlowsourceRef method
        pass

    def MessageFlowtargetRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MessageFlowtargetRef method
        pass

class BPMNProfile_FlowElement(BaseElement):

    pass
class BPMNProfile_ActivityNode:

    pass
class FlowElement:

    pass
class BPMNProfile_DataObject(FlowElement, ItemAwareElement):

    def __init__(self, isCollection: str, BPMNProfile_DataObject: "BPMNProfile_DataObjectReference" = None, BPMNProfile_DataObject583: "BPMNProfile_DataStoreNode" = None):
        self.isCollection = isCollection
        self.BPMNProfile_DataObject = BPMNProfile_DataObject
        self.BPMNProfile_DataObject583 = BPMNProfile_DataObject583
        
    @property
    def isCollection(self) -> str:
        return self.__isCollection

    @isCollection.setter
    def isCollection(self, isCollection: str):
        self.__isCollection = isCollection

    @property
    def BPMNProfile_DataObject583(self):
        return self.__BPMNProfile_DataObject583

    @BPMNProfile_DataObject583.setter
    def BPMNProfile_DataObject583(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataObject__BPMNProfile_DataObject583", None)
        self.__BPMNProfile_DataObject583 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_DataStoreNode584"):
                opp_val = getattr(old_value, "BPMNProfile_DataStoreNode584", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_DataStoreNode584", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_DataStoreNode584"):
                opp_val = getattr(value, "BPMNProfile_DataStoreNode584", None)
                setattr(value, "BPMNProfile_DataStoreNode584", self)

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

    def DataObjectdataState(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement DataObjectdataState method
        pass

class BPMNProfile_DataStoreReference(FlowElement, ItemAwareElement):

    pass
class BPMNProfile_DataObjectReference(FlowElement, ItemAwareElement):

    def __init__(self, BPMNProfile_DataObjectReference580: "BPMNProfile_DataStoreNode" = None, BPMNProfile_DataObjectReference: "BPMNProfile_DataObject" = None):
        self.BPMNProfile_DataObjectReference580 = BPMNProfile_DataObjectReference580
        self.BPMNProfile_DataObjectReference = BPMNProfile_DataObjectReference
        
    @property
    def BPMNProfile_DataObjectReference580(self):
        return self.__BPMNProfile_DataObjectReference580

    @BPMNProfile_DataObjectReference580.setter
    def BPMNProfile_DataObjectReference580(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_DataObjectReference__BPMNProfile_DataObjectReference580", None)
        self.__BPMNProfile_DataObjectReference580 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_DataStoreNode581"):
                opp_val = getattr(old_value, "BPMNProfile_DataStoreNode581", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_DataStoreNode581", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_DataStoreNode581"):
                opp_val = getattr(value, "BPMNProfile_DataStoreNode581", None)
                setattr(value, "BPMNProfile_DataStoreNode581", self)

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

    def DataObjectRefdataState(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement DataObjectRefdataState method
        pass

    def DataObjectRefsourcetarget(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement DataObjectRefsourcetarget method
        pass

class BPMNProfile_FlowNode(FlowElement):

    pass
class BPMNProfile_ActivityGroup:

    pass
class BPMNProfile_ControlNode:

    pass
class FlowNode:

    pass
class BPMNProfile_BPMNActivity(InteractionNode, FlowNode):

    def __init__(self, isForCompensation: str, startQuantity: str, completionQuantity: str, BPMNProfile_BPMNActivity: "BPMNProfile_CompensateEventDefinition" = None, BPMNProfile_BPMNActivity446: "BPMNProfile_Action" = None, BPMNProfile_BPMNActivity449: "BPMNProfile_Class" = None, BPMNProfile_BPMNActivity452: set["BPMNProfile_BPMNProperty"] = None, BPMNProfile_BPMNActivity455: "BPMNProfile_SequenceFlow" = None, BPMNProfile_BPMNActivity458: set["BPMNProfile_BoundaryEvent"] = None, BPMNProfile_BPMNActivity460: set["BPMNProfile_DataInputAssociation"] = None, BPMNProfile_BPMNActivity462: set["BPMNProfile_DataOutputAssociation"] = None, BPMNProfile_BPMNActivity464: "BPMNProfile_LoopCharacteristics" = None, BPMNProfile_BPMNActivity466: set["BPMNProfile_ResourceRole"] = None, BPMNProfile_BPMNActivity470: "BPMNProfile_BoundaryEvent" = None):
        self.isForCompensation = isForCompensation
        self.startQuantity = startQuantity
        self.completionQuantity = completionQuantity
        self.BPMNProfile_BPMNActivity = BPMNProfile_BPMNActivity
        self.BPMNProfile_BPMNActivity446 = BPMNProfile_BPMNActivity446
        self.BPMNProfile_BPMNActivity449 = BPMNProfile_BPMNActivity449
        self.BPMNProfile_BPMNActivity452 = BPMNProfile_BPMNActivity452 if BPMNProfile_BPMNActivity452 is not None else set()
        self.BPMNProfile_BPMNActivity455 = BPMNProfile_BPMNActivity455
        self.BPMNProfile_BPMNActivity458 = BPMNProfile_BPMNActivity458 if BPMNProfile_BPMNActivity458 is not None else set()
        self.BPMNProfile_BPMNActivity460 = BPMNProfile_BPMNActivity460 if BPMNProfile_BPMNActivity460 is not None else set()
        self.BPMNProfile_BPMNActivity462 = BPMNProfile_BPMNActivity462 if BPMNProfile_BPMNActivity462 is not None else set()
        self.BPMNProfile_BPMNActivity464 = BPMNProfile_BPMNActivity464
        self.BPMNProfile_BPMNActivity466 = BPMNProfile_BPMNActivity466 if BPMNProfile_BPMNActivity466 is not None else set()
        self.BPMNProfile_BPMNActivity470 = BPMNProfile_BPMNActivity470
        
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
    def BPMNProfile_BPMNActivity470(self):
        return self.__BPMNProfile_BPMNActivity470

    @BPMNProfile_BPMNActivity470.setter
    def BPMNProfile_BPMNActivity470(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNActivity__BPMNProfile_BPMNActivity470", None)
        self.__BPMNProfile_BPMNActivity470 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BoundaryEvent469"):
                opp_val = getattr(old_value, "BPMNProfile_BoundaryEvent469", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BoundaryEvent469", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BoundaryEvent469"):
                opp_val = getattr(value, "BPMNProfile_BoundaryEvent469", None)
                setattr(value, "BPMNProfile_BoundaryEvent469", self)

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
            if hasattr(old_value, "BPMNProfile_Class450"):
                opp_val = getattr(old_value, "BPMNProfile_Class450", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Class450", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Class450"):
                opp_val = getattr(value, "BPMNProfile_Class450", None)
                setattr(value, "BPMNProfile_Class450", self)

    @property
    def BPMNProfile_BPMNActivity466(self):
        return self.__BPMNProfile_BPMNActivity466

    @BPMNProfile_BPMNActivity466.setter
    def BPMNProfile_BPMNActivity466(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNActivity__BPMNProfile_BPMNActivity466", None)
        self.__BPMNProfile_BPMNActivity466 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMNProfile_ResourceRole467"):
                    opp_val = getattr(item, "BPMNProfile_ResourceRole467", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_ResourceRole467", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_ResourceRole467"):
                    opp_val = getattr(item, "BPMNProfile_ResourceRole467", None)
                    
                    setattr(item, "BPMNProfile_ResourceRole467", self)
                    

    @property
    def BPMNProfile_BPMNActivity446(self):
        return self.__BPMNProfile_BPMNActivity446

    @BPMNProfile_BPMNActivity446.setter
    def BPMNProfile_BPMNActivity446(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNActivity__BPMNProfile_BPMNActivity446", None)
        self.__BPMNProfile_BPMNActivity446 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_Action447"):
                opp_val = getattr(old_value, "BPMNProfile_Action447", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_Action447", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_Action447"):
                opp_val = getattr(value, "BPMNProfile_Action447", None)
                setattr(value, "BPMNProfile_Action447", self)

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
            if hasattr(old_value, "BPMNProfile_LoopCharacteristics"):
                opp_val = getattr(old_value, "BPMNProfile_LoopCharacteristics", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_LoopCharacteristics", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_LoopCharacteristics"):
                opp_val = getattr(value, "BPMNProfile_LoopCharacteristics", None)
                setattr(value, "BPMNProfile_LoopCharacteristics", self)

    @property
    def BPMNProfile_BPMNActivity462(self):
        return self.__BPMNProfile_BPMNActivity462

    @BPMNProfile_BPMNActivity462.setter
    def BPMNProfile_BPMNActivity462(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNActivity__BPMNProfile_BPMNActivity462", None)
        self.__BPMNProfile_BPMNActivity462 = value if value is not None else set()
        
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
    def BPMNProfile_BPMNActivity455(self):
        return self.__BPMNProfile_BPMNActivity455

    @BPMNProfile_BPMNActivity455.setter
    def BPMNProfile_BPMNActivity455(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNActivity__BPMNProfile_BPMNActivity455", None)
        self.__BPMNProfile_BPMNActivity455 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_SequenceFlow456"):
                opp_val = getattr(old_value, "BPMNProfile_SequenceFlow456", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_SequenceFlow456", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_SequenceFlow456"):
                opp_val = getattr(value, "BPMNProfile_SequenceFlow456", None)
                setattr(value, "BPMNProfile_SequenceFlow456", self)

    @property
    def BPMNProfile_BPMNActivity458(self):
        return self.__BPMNProfile_BPMNActivity458

    @BPMNProfile_BPMNActivity458.setter
    def BPMNProfile_BPMNActivity458(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_BPMNActivity__BPMNProfile_BPMNActivity458", None)
        self.__BPMNProfile_BPMNActivity458 = value if value is not None else set()
        
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
                if hasattr(item, "BPMNProfile_BPMNProperty453"):
                    opp_val = getattr(item, "BPMNProfile_BPMNProperty453", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMNProfile_BPMNProperty453", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMNProfile_BPMNProperty453"):
                    opp_val = getattr(item, "BPMNProfile_BPMNProperty453", None)
                    
                    setattr(item, "BPMNProfile_BPMNProperty453", self)
                    

    def BPMNActivityloopCharacteristics(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BPMNActivityloopCharacteristics method
        pass

    def BPMNActivityproperties(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BPMNActivityproperties method
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

    def BPMNActivitycontainer(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement BPMNActivitycontainer method
        pass

class BPMNProfile_BPMNEvent(InteractionNode, FlowNode):

    pass
class BPMNProfile_Gateway(FlowNode):

    pass
class BPMNProfile_ForkNode:

    pass
class BPMNProfile_JoinNode:

    pass
class Gateway:

    pass
class BPMNProfile_EventBasedGateway(Gateway):

    def __init__(self, instantiate: str, eventGatewayType: str, BPMNProfile_EventBasedGateway: "BPMNProfile_ForkNode" = None, BPMNProfile_EventBasedGateway91: "BPMNProfile_StructuredActivityNode" = None, BPMNProfile_EventBasedGateway93: "BPMNProfile_InterruptibleActivityRegion" = None):
        self.instantiate = instantiate
        self.eventGatewayType = eventGatewayType
        self.BPMNProfile_EventBasedGateway = BPMNProfile_EventBasedGateway
        self.BPMNProfile_EventBasedGateway91 = BPMNProfile_EventBasedGateway91
        self.BPMNProfile_EventBasedGateway93 = BPMNProfile_EventBasedGateway93
        
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
    def BPMNProfile_EventBasedGateway93(self):
        return self.__BPMNProfile_EventBasedGateway93

    @BPMNProfile_EventBasedGateway93.setter
    def BPMNProfile_EventBasedGateway93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_EventBasedGateway__BPMNProfile_EventBasedGateway93", None)
        self.__BPMNProfile_EventBasedGateway93 = value
        
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
    def BPMNProfile_EventBasedGateway91(self):
        return self.__BPMNProfile_EventBasedGateway91

    @BPMNProfile_EventBasedGateway91.setter
    def BPMNProfile_EventBasedGateway91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_EventBasedGateway__BPMNProfile_EventBasedGateway91", None)
        self.__BPMNProfile_EventBasedGateway91 = value
        
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
            if hasattr(old_value, "BPMNProfile_ForkNode89"):
                opp_val = getattr(old_value, "BPMNProfile_ForkNode89", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ForkNode89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ForkNode89"):
                opp_val = getattr(value, "BPMNProfile_ForkNode89", None)
                setattr(value, "BPMNProfile_ForkNode89", self)

class BPMNProfile_ExclusiveGateway(Gateway):

    def __init__(self, BPMNProfile_ExclusiveGateway101: "BPMNProfile_MergeNode" = None, BPMNProfile_ExclusiveGateway103: "BPMNProfile_SequenceFlow" = None, BPMNProfile_ExclusiveGateway: "BPMNProfile_DecisionNode" = None):
        self.BPMNProfile_ExclusiveGateway101 = BPMNProfile_ExclusiveGateway101
        self.BPMNProfile_ExclusiveGateway103 = BPMNProfile_ExclusiveGateway103
        self.BPMNProfile_ExclusiveGateway = BPMNProfile_ExclusiveGateway
        
    @property
    def BPMNProfile_ExclusiveGateway101(self):
        return self.__BPMNProfile_ExclusiveGateway101

    @BPMNProfile_ExclusiveGateway101.setter
    def BPMNProfile_ExclusiveGateway101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ExclusiveGateway__BPMNProfile_ExclusiveGateway101", None)
        self.__BPMNProfile_ExclusiveGateway101 = value
        
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
    def BPMNProfile_ExclusiveGateway103(self):
        return self.__BPMNProfile_ExclusiveGateway103

    @BPMNProfile_ExclusiveGateway103.setter
    def BPMNProfile_ExclusiveGateway103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ExclusiveGateway__BPMNProfile_ExclusiveGateway103", None)
        self.__BPMNProfile_ExclusiveGateway103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_SequenceFlow104"):
                opp_val = getattr(old_value, "BPMNProfile_SequenceFlow104", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_SequenceFlow104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_SequenceFlow104"):
                opp_val = getattr(value, "BPMNProfile_SequenceFlow104", None)
                setattr(value, "BPMNProfile_SequenceFlow104", self)

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

    def exclusiveGatewaydefault(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement exclusiveGatewaydefault method
        pass

class BPMNProfile_NonExclusiveGateway(Gateway):

    pass
class BPMNProfile_SequenceFlow(FlowElement):

    def __init__(self, isImmediate: str, BPMNProfile_SequenceFlow: "BPMNProfile_InclusiveGateway" = None, BPMNProfile_SequenceFlow81: "BPMNProfile_FlowNode" = None, BPMNProfile_SequenceFlow84: "BPMNProfile_FlowNode" = None, BPMNProfile_SequenceFlow95: "BPMNProfile_ComplexGateway" = None, BPMNProfile_SequenceFlow77: "BPMNProfile_ControlFlow" = None, BPMNProfile_SequenceFlow79: "BPMNProfile_BPMNExpression" = None, BPMNProfile_SequenceFlow104: "BPMNProfile_ExclusiveGateway" = None, BPMNProfile_SequenceFlow456: "BPMNProfile_BPMNActivity" = None):
        self.isImmediate = isImmediate
        self.BPMNProfile_SequenceFlow = BPMNProfile_SequenceFlow
        self.BPMNProfile_SequenceFlow81 = BPMNProfile_SequenceFlow81
        self.BPMNProfile_SequenceFlow84 = BPMNProfile_SequenceFlow84
        self.BPMNProfile_SequenceFlow95 = BPMNProfile_SequenceFlow95
        self.BPMNProfile_SequenceFlow77 = BPMNProfile_SequenceFlow77
        self.BPMNProfile_SequenceFlow79 = BPMNProfile_SequenceFlow79
        self.BPMNProfile_SequenceFlow104 = BPMNProfile_SequenceFlow104
        self.BPMNProfile_SequenceFlow456 = BPMNProfile_SequenceFlow456
        
    @property
    def isImmediate(self) -> str:
        return self.__isImmediate

    @isImmediate.setter
    def isImmediate(self, isImmediate: str):
        self.__isImmediate = isImmediate

    @property
    def BPMNProfile_SequenceFlow456(self):
        return self.__BPMNProfile_SequenceFlow456

    @BPMNProfile_SequenceFlow456.setter
    def BPMNProfile_SequenceFlow456(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_SequenceFlow__BPMNProfile_SequenceFlow456", None)
        self.__BPMNProfile_SequenceFlow456 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNActivity455"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNActivity455", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNActivity455", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNActivity455"):
                opp_val = getattr(value, "BPMNProfile_BPMNActivity455", None)
                setattr(value, "BPMNProfile_BPMNActivity455", self)

    @property
    def BPMNProfile_SequenceFlow104(self):
        return self.__BPMNProfile_SequenceFlow104

    @BPMNProfile_SequenceFlow104.setter
    def BPMNProfile_SequenceFlow104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_SequenceFlow__BPMNProfile_SequenceFlow104", None)
        self.__BPMNProfile_SequenceFlow104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_ExclusiveGateway103"):
                opp_val = getattr(old_value, "BPMNProfile_ExclusiveGateway103", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_ExclusiveGateway103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_ExclusiveGateway103"):
                opp_val = getattr(value, "BPMNProfile_ExclusiveGateway103", None)
                setattr(value, "BPMNProfile_ExclusiveGateway103", self)

    @property
    def BPMNProfile_SequenceFlow95(self):
        return self.__BPMNProfile_SequenceFlow95

    @BPMNProfile_SequenceFlow95.setter
    def BPMNProfile_SequenceFlow95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_SequenceFlow__BPMNProfile_SequenceFlow95", None)
        self.__BPMNProfile_SequenceFlow95 = value
        
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
    def BPMNProfile_SequenceFlow81(self):
        return self.__BPMNProfile_SequenceFlow81

    @BPMNProfile_SequenceFlow81.setter
    def BPMNProfile_SequenceFlow81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_SequenceFlow__BPMNProfile_SequenceFlow81", None)
        self.__BPMNProfile_SequenceFlow81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_FlowNode82"):
                opp_val = getattr(old_value, "BPMNProfile_FlowNode82", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_FlowNode82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_FlowNode82"):
                opp_val = getattr(value, "BPMNProfile_FlowNode82", None)
                setattr(value, "BPMNProfile_FlowNode82", self)

    @property
    def BPMNProfile_SequenceFlow84(self):
        return self.__BPMNProfile_SequenceFlow84

    @BPMNProfile_SequenceFlow84.setter
    def BPMNProfile_SequenceFlow84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_SequenceFlow__BPMNProfile_SequenceFlow84", None)
        self.__BPMNProfile_SequenceFlow84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_FlowNode85"):
                opp_val = getattr(old_value, "BPMNProfile_FlowNode85", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_FlowNode85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_FlowNode85"):
                opp_val = getattr(value, "BPMNProfile_FlowNode85", None)
                setattr(value, "BPMNProfile_FlowNode85", self)

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

    def SequenceFlowsourceRef(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SequenceFlowsourceRef method
        pass

    def SequenceFlowconditionExpression(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SequenceFlowconditionExpression method
        pass

    def SequenceFlowtargetRef(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SequenceFlowtargetRef method
        pass

class NonExclusiveGateway:

    pass
class BPMNProfile_ComplexGateway(NonExclusiveGateway):

    def __init__(self, BPMNProfile_ComplexGateway: "BPMNProfile_SequenceFlow" = None, BPMNProfile_ComplexGateway97: "BPMNProfile_BPMNExpression" = None):
        self.BPMNProfile_ComplexGateway = BPMNProfile_ComplexGateway
        self.BPMNProfile_ComplexGateway97 = BPMNProfile_ComplexGateway97
        
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
            if hasattr(old_value, "BPMNProfile_SequenceFlow95"):
                opp_val = getattr(old_value, "BPMNProfile_SequenceFlow95", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_SequenceFlow95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_SequenceFlow95"):
                opp_val = getattr(value, "BPMNProfile_SequenceFlow95", None)
                setattr(value, "BPMNProfile_SequenceFlow95", self)

    @property
    def BPMNProfile_ComplexGateway97(self):
        return self.__BPMNProfile_ComplexGateway97

    @BPMNProfile_ComplexGateway97.setter
    def BPMNProfile_ComplexGateway97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMNProfile_ComplexGateway__BPMNProfile_ComplexGateway97", None)
        self.__BPMNProfile_ComplexGateway97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMNProfile_BPMNExpression98"):
                opp_val = getattr(old_value, "BPMNProfile_BPMNExpression98", None)
                if opp_val == self:
                    setattr(old_value, "BPMNProfile_BPMNExpression98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMNProfile_BPMNExpression98"):
                opp_val = getattr(value, "BPMNProfile_BPMNExpression98", None)
                setattr(value, "BPMNProfile_BPMNExpression98", self)

    def complexGatewayjoinSpec(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement complexGatewayjoinSpec method
        pass

    def complexGatewayactivationCondition(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement complexGatewayactivationCondition method
        pass

    def complexGatewaydefault(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement complexGatewaydefault method
        pass

class BPMNProfile_ParallelGateway(NonExclusiveGateway):

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
