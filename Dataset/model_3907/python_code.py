from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class PrimitiveTypeEnum(Enum):
    DOUBLE = "DOUBLE"
    CHAR = "CHAR"
    BYTE = "BYTE"
    LONG = "LONG"
    INT = "INT"
    STRING = "STRING"
    BOOL = "BOOL"
class VariableCharacterisationType(Enum):
    STRUCTURE = "STRUCTURE"
    NUMBER_OF_ELEMENTS = "NUMBER_OF_ELEMENTS"
    VALUE = "VALUE"
    BYTESIZE = "BYTESIZE"
    TYPE = "TYPE"
class ComponentType(Enum):
    BUSINESS_COMPONENT = "BUSINESS_COMPONENT"
    INFRASTRUCTURE_COMPONENT = "INFRASTRUCTURE_COMPONENT"
class ParameterModifier(Enum):
    none = "none"
    in = "in"
    out = "out"
    inout = "inout"


############################################
# Definition of Classes
############################################

class ParametricResourceDemand:

    pass
class pcm_av_completions_av_NetworkDemandParametricResourceDemand(ParametricResourceDemand):

    pass
class ExternalCallAction:

    pass
class pcm_av_completions_av_DelegatingExternalCallAction(ExternalCallAction):

    pass
class Allocation:

    pass
class Completion:

    pass
class pcm_av_completions_av_CompletionRepository:

    pass
class repository_av_RepositoryComponent:

    pass
class AllocationContext:

    pass
class LinkingResource:

    pass
class ResourceEnvironment:

    pass
class ResourceContainer:

    pass
class ExternalFailureOccurrenceDescription:

    pass
class System:

    pass
class SpecifiedExecutionTime:

    pass
class pcm_av_qos_performance_av_ComponentSpecifiedExecutionTime(SpecifiedExecutionTime):

    pass
class pcm_av_qos_performance_av_SystemSpecifiedExecutionTime(SpecifiedExecutionTime):

    def __init__(self):
        
    def SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem method
        pass

class pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction:

    pass
class SpecifiedQoSAnnotation:

    pass
class pcm_av_qos_performance_av_SpecifiedExecutionTime(SpecifiedQoSAnnotation):

    pass
class pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation(SpecifiedQoSAnnotation):

    def __init__(self, ExternalFailureOccurrenceDescription: set["ExternalFailureOccurrenceDescription"] = None, qosannotations_av606: "pcm_av_qosannotations_av_QoSAnnotations"):
        self.ExternalFailureOccurrenceDescription = ExternalFailureOccurrenceDescription if ExternalFailureOccurrenceDescription is not None else set()
        
    @property
    def ExternalFailureOccurrenceDescription(self):
        return self.__ExternalFailureOccurrenceDescription

    @ExternalFailureOccurrenceDescription.setter
    def ExternalFailureOccurrenceDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription", None)
        self.__ExternalFailureOccurrenceDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reliability_av624"):
                    opp_val = getattr(item, "reliability_av624", None)
                    
                    if opp_val == self:
                        setattr(item, "reliability_av624", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reliability_av624"):
                    opp_val = getattr(item, "reliability_av624", None)
                    
                    setattr(item, "reliability_av624", self)
                    

    def MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed method
        pass

    def SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem method
        pass

    def SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1 method
        pass

class seff_reliability_av_RecoveryActionBehaviour:

    pass
class QoSAnnotations:

    pass
class pcm_av_qosannotations_av_SpecifiedQoSAnnotation:

    pass
class seff_reliability_av_RecoveryAction:

    pass
class pcm_av_seff_performance_av_ParametricResourceDemand:

    def __init__(self, PCMRandomVariable578: "PCMRandomVariable" = None, pcm_av_seff_performance_av_ParametricResourceDemand: "ProcessingResourceType" = None, AbstractInternalControlFlowAction583: "AbstractInternalControlFlowAction" = None):
        self.PCMRandomVariable578 = PCMRandomVariable578
        self.pcm_av_seff_performance_av_ParametricResourceDemand = pcm_av_seff_performance_av_ParametricResourceDemand
        self.AbstractInternalControlFlowAction583 = AbstractInternalControlFlowAction583
        
    @property
    def pcm_av_seff_performance_av_ParametricResourceDemand(self):
        return self.__pcm_av_seff_performance_av_ParametricResourceDemand

    @pcm_av_seff_performance_av_ParametricResourceDemand.setter
    def pcm_av_seff_performance_av_ParametricResourceDemand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_performance_av_ParametricResourceDemand__pcm_av_seff_performance_av_ParametricResourceDemand", None)
        self.__pcm_av_seff_performance_av_ParametricResourceDemand = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcessingResourceType581"):
                opp_val = getattr(old_value, "ProcessingResourceType581", None)
                if opp_val == self:
                    setattr(old_value, "ProcessingResourceType581", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessingResourceType581"):
                opp_val = getattr(value, "ProcessingResourceType581", None)
                setattr(value, "ProcessingResourceType581", self)

    @property
    def AbstractInternalControlFlowAction583(self):
        return self.__AbstractInternalControlFlowAction583

    @AbstractInternalControlFlowAction583.setter
    def AbstractInternalControlFlowAction583(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_performance_av_ParametricResourceDemand__AbstractInternalControlFlowAction583", None)
        self.__AbstractInternalControlFlowAction583 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av584"):
                opp_val = getattr(old_value, "seff_av584", None)
                if opp_val == self:
                    setattr(old_value, "seff_av584", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av584"):
                opp_val = getattr(value, "seff_av584", None)
                setattr(value, "seff_av584", self)

    @property
    def PCMRandomVariable578(self):
        return self.__PCMRandomVariable578

    @PCMRandomVariable578.setter
    def PCMRandomVariable578(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_performance_av_ParametricResourceDemand__PCMRandomVariable578", None)
        self.__PCMRandomVariable578 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av579"):
                opp_val = getattr(old_value, "core_av579", None)
                if opp_val == self:
                    setattr(old_value, "core_av579", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av579"):
                opp_val = getattr(value, "core_av579", None)
                setattr(value, "core_av579", self)

    def DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

class seff_av_AbstractInternalControlFlowAction:

    pass
class seff_av_CallAction:

    pass
class pcm_av_seff_av_InternalCallAction(seff_av_AbstractInternalControlFlowAction, seff_av_CallAction):

    pass
class ResourceDemandingSEFF:

    pass
class ResourceDemandingInternalBehaviour:

    pass
class seff_reliability_av_FailureHandlingEntity:

    pass
class seff_av_CallReturnAction:

    pass
class seff_av_AbstractAction:

    pass
class pcm_av_seff_av_EmitEventAction(seff_av_AbstractAction, seff_av_CallAction):

    pass
class pcm_av_seff_av_ExternalCallAction(seff_av_CallReturnAction, seff_reliability_av_FailureHandlingEntity, seff_av_AbstractAction):

    def __init__(self, retryCount: int, pcm_av_seff_av_ExternalCallAction: "OperationSignature" = None, pcm_av_seff_av_ExternalCallAction531: "OperationRequiredRole" = None):
        self.retryCount = retryCount
        self.pcm_av_seff_av_ExternalCallAction = pcm_av_seff_av_ExternalCallAction
        self.pcm_av_seff_av_ExternalCallAction531 = pcm_av_seff_av_ExternalCallAction531
        
    @property
    def retryCount(self) -> int:
        return self.__retryCount

    @retryCount.setter
    def retryCount(self, retryCount: int):
        self.__retryCount = retryCount

    @property
    def pcm_av_seff_av_ExternalCallAction531(self):
        return self.__pcm_av_seff_av_ExternalCallAction531

    @pcm_av_seff_av_ExternalCallAction531.setter
    def pcm_av_seff_av_ExternalCallAction531(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_av_ExternalCallAction__pcm_av_seff_av_ExternalCallAction531", None)
        self.__pcm_av_seff_av_ExternalCallAction531 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationRequiredRole532"):
                opp_val = getattr(old_value, "OperationRequiredRole532", None)
                if opp_val == self:
                    setattr(old_value, "OperationRequiredRole532", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationRequiredRole532"):
                opp_val = getattr(value, "OperationRequiredRole532", None)
                setattr(value, "OperationRequiredRole532", self)

    @property
    def pcm_av_seff_av_ExternalCallAction(self):
        return self.__pcm_av_seff_av_ExternalCallAction

    @pcm_av_seff_av_ExternalCallAction.setter
    def pcm_av_seff_av_ExternalCallAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_av_ExternalCallAction__pcm_av_seff_av_ExternalCallAction", None)
        self.__pcm_av_seff_av_ExternalCallAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationSignature529"):
                opp_val = getattr(old_value, "OperationSignature529", None)
                if opp_val == self:
                    setattr(old_value, "OperationSignature529", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationSignature529"):
                opp_val = getattr(value, "OperationSignature529", None)
                setattr(value, "OperationSignature529", self)

    def SignatureBelongsToRole(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SignatureBelongsToRole method
        pass

    def OperationRequiredRoleMustBeReferencedByContainer(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement OperationRequiredRoleMustBeReferencedByContainer method
        pass

class pcm_av_seff_av_SynchronisationPoint:

    pass
class ForkAction:

    pass
class ForkedBehaviour:

    pass
class seff_av_ResourceDemandingBehaviour:

    pass
class pcm_av_seff_reliability_av_RecoveryActionBehaviour(seff_av_ResourceDemandingBehaviour, seff_reliability_av_FailureHandlingEntity):

    def __init__(self, seff_reliability_av: "seff_reliability_av_RecoveryAction" = None, pcm_av_seff_reliability_av_RecoveryActionBehaviour: set["seff_reliability_av_RecoveryActionBehaviour"] = None):
        self.seff_reliability_av = seff_reliability_av
        self.pcm_av_seff_reliability_av_RecoveryActionBehaviour = pcm_av_seff_reliability_av_RecoveryActionBehaviour if pcm_av_seff_reliability_av_RecoveryActionBehaviour is not None else set()
        
    @property
    def pcm_av_seff_reliability_av_RecoveryActionBehaviour(self):
        return self.__pcm_av_seff_reliability_av_RecoveryActionBehaviour

    @pcm_av_seff_reliability_av_RecoveryActionBehaviour.setter
    def pcm_av_seff_reliability_av_RecoveryActionBehaviour(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_reliability_av_RecoveryActionBehaviour__pcm_av_seff_reliability_av_RecoveryActionBehaviour", None)
        self.__pcm_av_seff_reliability_av_RecoveryActionBehaviour = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_reliability_av_RecoveryActionBehaviour"):
                    opp_val = getattr(item, "seff_reliability_av_RecoveryActionBehaviour", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_reliability_av_RecoveryActionBehaviour", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_reliability_av_RecoveryActionBehaviour"):
                    opp_val = getattr(item, "seff_reliability_av_RecoveryActionBehaviour", None)
                    
                    setattr(item, "seff_reliability_av_RecoveryActionBehaviour", self)
                    

    @property
    def seff_reliability_av(self):
        return self.__seff_reliability_av

    @seff_reliability_av.setter
    def seff_reliability_av(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_reliability_av_RecoveryActionBehaviour__seff_reliability_av", None)
        self.__seff_reliability_av = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av587"):
                opp_val = getattr(old_value, "seff_av587", None)
                if opp_val == self:
                    setattr(old_value, "seff_av587", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av587"):
                opp_val = getattr(value, "seff_av587", None)
                setattr(value, "seff_av587", self)

    def RecoveryActionBehaviourIsNotSuccessorOfItself(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement RecoveryActionBehaviourIsNotSuccessorOfItself method
        pass

    def SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes method
        pass

    def RecoveryActionBehaviourHasOnlyOnePredecessor(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement RecoveryActionBehaviourHasOnlyOnePredecessor method
        pass

class seff_av_ServiceEffectSpecification:

    pass
class pcm_av_seff_av_ServiceEffectSpecification:

    def __init__(self, seffTypeID: str, pcm_av_seff_av_ServiceEffectSpecification: "Signature" = None, BasicComponent498: "BasicComponent" = None):
        self.seffTypeID = seffTypeID
        self.pcm_av_seff_av_ServiceEffectSpecification = pcm_av_seff_av_ServiceEffectSpecification
        self.BasicComponent498 = BasicComponent498
        
    @property
    def seffTypeID(self) -> str:
        return self.__seffTypeID

    @seffTypeID.setter
    def seffTypeID(self, seffTypeID: str):
        self.__seffTypeID = seffTypeID

    @property
    def BasicComponent498(self):
        return self.__BasicComponent498

    @BasicComponent498.setter
    def BasicComponent498(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_av_ServiceEffectSpecification__BasicComponent498", None)
        self.__BasicComponent498 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av499"):
                opp_val = getattr(old_value, "repository_av499", None)
                if opp_val == self:
                    setattr(old_value, "repository_av499", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av499"):
                opp_val = getattr(value, "repository_av499", None)
                setattr(value, "repository_av499", self)

    @property
    def pcm_av_seff_av_ServiceEffectSpecification(self):
        return self.__pcm_av_seff_av_ServiceEffectSpecification

    @pcm_av_seff_av_ServiceEffectSpecification.setter
    def pcm_av_seff_av_ServiceEffectSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_av_ServiceEffectSpecification__pcm_av_seff_av_ServiceEffectSpecification", None)
        self.__pcm_av_seff_av_ServiceEffectSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Signature"):
                opp_val = getattr(old_value, "Signature", None)
                if opp_val == self:
                    setattr(old_value, "Signature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Signature"):
                opp_val = getattr(value, "Signature", None)
                setattr(value, "Signature", self)

    def ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole method
        pass

class pcm_av_seff_av_CallAction:

    pass
class ResourceDemandingBehaviour:

    pass
class pcm_av_seff_av_ForkedBehaviour(ResourceDemandingBehaviour):

    pass
class pcm_av_seff_av_ResourceDemandingInternalBehaviour(ResourceDemandingBehaviour):

    pass
class BranchAction:

    pass
class AbstractBranchTransition:

    pass
class pcm_av_seff_av_GuardedBranchTransition(AbstractBranchTransition):

    pass
class pcm_av_seff_av_ProbabilisticBranchTransition(AbstractBranchTransition):

    def __init__(self, branchProbability: float, seff_av492: "pcm_av_seff_av_BranchAction", seff_av478: "pcm_av_seff_av_ResourceDemandingBehaviour"):
        self.branchProbability = branchProbability
        
    @property
    def branchProbability(self) -> float:
        return self.__branchProbability

    @branchProbability.setter
    def branchProbability(self, branchProbability: float):
        self.__branchProbability = branchProbability

class AbstractLoopAction:

    pass
class pcm_av_seff_av_LoopAction(AbstractLoopAction):

    pass
class pcm_av_seff_av_CollectionIteratorAction(AbstractLoopAction):

    pass
class CommunicationLinkResourceType:

    pass
class AbstractAction:

    pass
class pcm_av_seff_av_AbstractInternalControlFlowAction(AbstractAction):

    pass
class AbstractInternalControlFlowAction:

    pass
class pcm_av_seff_av_SetVariableAction(AbstractInternalControlFlowAction):

    pass
class pcm_av_seff_av_AbstractLoopAction(AbstractInternalControlFlowAction):

    pass
class pcm_av_seff_av_AcquireAction(AbstractInternalControlFlowAction):

    def __init__(self, timeout: bool, timeoutValue: float, pcm_av_seff_av_AcquireAction: "PassiveResource" = None, seff_av562: "pcm_av_seff_performance_av_InfrastructureCall", seff_av568: "pcm_av_seff_performance_av_ResourceCall", seff_av584: "pcm_av_seff_performance_av_ParametricResourceDemand"):
        self.timeout = timeout
        self.timeoutValue = timeoutValue
        self.pcm_av_seff_av_AcquireAction = pcm_av_seff_av_AcquireAction
        
    @property
    def timeout(self) -> bool:
        return self.__timeout

    @timeout.setter
    def timeout(self, timeout: bool):
        self.__timeout = timeout

    @property
    def timeoutValue(self) -> float:
        return self.__timeoutValue

    @timeoutValue.setter
    def timeoutValue(self, timeoutValue: float):
        self.__timeoutValue = timeoutValue

    @property
    def pcm_av_seff_av_AcquireAction(self):
        return self.__pcm_av_seff_av_AcquireAction

    @pcm_av_seff_av_AcquireAction.setter
    def pcm_av_seff_av_AcquireAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_av_AcquireAction__pcm_av_seff_av_AcquireAction", None)
        self.__pcm_av_seff_av_AcquireAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PassiveResource537"):
                opp_val = getattr(old_value, "PassiveResource537", None)
                if opp_val == self:
                    setattr(old_value, "PassiveResource537", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PassiveResource537"):
                opp_val = getattr(value, "PassiveResource537", None)
                setattr(value, "PassiveResource537", self)

    def TimeoutValueOfAcquireActionMustNotBeNegative(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement TimeoutValueOfAcquireActionMustNotBeNegative method
        pass

class pcm_av_seff_av_ForkAction(AbstractInternalControlFlowAction):

    pass
class pcm_av_seff_av_BranchAction(AbstractInternalControlFlowAction):

    def __init__(self, AbstractBranchTransition491: set["AbstractBranchTransition"] = None, seff_av562: "pcm_av_seff_performance_av_InfrastructureCall", seff_av568: "pcm_av_seff_performance_av_ResourceCall", seff_av584: "pcm_av_seff_performance_av_ParametricResourceDemand"):
        self.AbstractBranchTransition491 = AbstractBranchTransition491 if AbstractBranchTransition491 is not None else set()
        
    @property
    def AbstractBranchTransition491(self):
        return self.__AbstractBranchTransition491

    @AbstractBranchTransition491.setter
    def AbstractBranchTransition491(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_av_BranchAction__AbstractBranchTransition491", None)
        self.__AbstractBranchTransition491 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_av492"):
                    opp_val = getattr(item, "seff_av492", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_av492", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_av492"):
                    opp_val = getattr(item, "seff_av492", None)
                    
                    setattr(item, "seff_av492", self)
                    

    def EitherGuardedBranchesOrProbabilisiticBranchTransitions(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EitherGuardedBranchesOrProbabilisiticBranchTransitions method
        pass

    def AllProbabilisticBranchProbabilitiesMustSumUpTo1(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AllProbabilisticBranchProbabilitiesMustSumUpTo1 method
        pass

class pcm_av_seff_av_InternalAction(AbstractInternalControlFlowAction):

    def __init__(self, InternalFailureOccurrenceDescription554: set["InternalFailureOccurrenceDescription"] = None, seff_av562: "pcm_av_seff_performance_av_InfrastructureCall", seff_av568: "pcm_av_seff_performance_av_ResourceCall", seff_av584: "pcm_av_seff_performance_av_ParametricResourceDemand"):
        self.InternalFailureOccurrenceDescription554 = InternalFailureOccurrenceDescription554 if InternalFailureOccurrenceDescription554 is not None else set()
        
    @property
    def InternalFailureOccurrenceDescription554(self):
        return self.__InternalFailureOccurrenceDescription554

    @InternalFailureOccurrenceDescription554.setter
    def InternalFailureOccurrenceDescription554(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_av_InternalAction__InternalFailureOccurrenceDescription554", None)
        self.__InternalFailureOccurrenceDescription554 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reliability_av555"):
                    opp_val = getattr(item, "reliability_av555", None)
                    
                    if opp_val == self:
                        setattr(item, "reliability_av555", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reliability_av555"):
                    opp_val = getattr(item, "reliability_av555", None)
                    
                    setattr(item, "reliability_av555", self)
                    

    def MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed method
        pass

    def SumOfInternalActionFailureProbabilitiesMustNotExceed1(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SumOfInternalActionFailureProbabilitiesMustNotExceed1 method
        pass

class pcm_av_seff_av_ReleaseAction(AbstractInternalControlFlowAction):

    pass
class pcm_av_seff_av_StartAction(AbstractInternalControlFlowAction):

    def __init__(self, seff_av562: "pcm_av_seff_performance_av_InfrastructureCall", seff_av568: "pcm_av_seff_performance_av_ResourceCall", seff_av584: "pcm_av_seff_performance_av_ParametricResourceDemand"):
        
    def StartActionPredecessorMustNotBeDefined(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement StartActionPredecessorMustNotBeDefined method
        pass

class pcm_av_seff_reliability_av_RecoveryAction(AbstractInternalControlFlowAction):

    def __init__(self, pcm_av_seff_reliability_av_RecoveryAction: "seff_reliability_av_RecoveryActionBehaviour" = None, seff_reliability_av591: set["seff_reliability_av_RecoveryActionBehaviour"] = None, seff_av562: "pcm_av_seff_performance_av_InfrastructureCall", seff_av568: "pcm_av_seff_performance_av_ResourceCall", seff_av584: "pcm_av_seff_performance_av_ParametricResourceDemand"):
        self.pcm_av_seff_reliability_av_RecoveryAction = pcm_av_seff_reliability_av_RecoveryAction
        self.seff_reliability_av591 = seff_reliability_av591 if seff_reliability_av591 is not None else set()
        
    @property
    def pcm_av_seff_reliability_av_RecoveryAction(self):
        return self.__pcm_av_seff_reliability_av_RecoveryAction

    @pcm_av_seff_reliability_av_RecoveryAction.setter
    def pcm_av_seff_reliability_av_RecoveryAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_reliability_av_RecoveryAction__pcm_av_seff_reliability_av_RecoveryAction", None)
        self.__pcm_av_seff_reliability_av_RecoveryAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_reliability_av_RecoveryActionBehaviour589"):
                opp_val = getattr(old_value, "seff_reliability_av_RecoveryActionBehaviour589", None)
                if opp_val == self:
                    setattr(old_value, "seff_reliability_av_RecoveryActionBehaviour589", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_reliability_av_RecoveryActionBehaviour589"):
                opp_val = getattr(value, "seff_reliability_av_RecoveryActionBehaviour589", None)
                setattr(value, "seff_reliability_av_RecoveryActionBehaviour589", self)

    @property
    def seff_reliability_av591(self):
        return self.__seff_reliability_av591

    @seff_reliability_av591.setter
    def seff_reliability_av591(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_reliability_av_RecoveryAction__seff_reliability_av591", None)
        self.__seff_reliability_av591 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_av592"):
                    opp_val = getattr(item, "seff_av592", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_av592", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_av592"):
                    opp_val = getattr(item, "seff_av592", None)
                    
                    setattr(item, "seff_av592", self)
                    

    def PrimaryBehaviourOfRecoveryActionMustBeSet(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement PrimaryBehaviourOfRecoveryActionMustBeSet method
        pass

class pcm_av_seff_av_StopAction(AbstractInternalControlFlowAction):

    def __init__(self, seff_av562: "pcm_av_seff_performance_av_InfrastructureCall", seff_av568: "pcm_av_seff_performance_av_ResourceCall", seff_av584: "pcm_av_seff_performance_av_ParametricResourceDemand"):
        
    def StopActionSuccessorMustNotBeDefined(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement StopActionSuccessorMustNotBeDefined method
        pass

class qos_reliability_av_SpecifiedReliabilityAnnotation:

    pass
class SoftwareInducedFailureType:

    pass
class pcm_av_reliability_av_ResourceTimeoutFailureType(SoftwareInducedFailureType):

    pass
class InternalAction:

    pass
class FailureOccurrenceDescription:

    pass
class pcm_av_reliability_av_ExternalFailureOccurrenceDescription(FailureOccurrenceDescription):

    def __init__(self, qos_reliability_av: "qos_reliability_av_SpecifiedReliabilityAnnotation" = None, pcm_av_reliability_av_ExternalFailureOccurrenceDescription: "FailureType" = None):
        self.qos_reliability_av = qos_reliability_av
        self.pcm_av_reliability_av_ExternalFailureOccurrenceDescription = pcm_av_reliability_av_ExternalFailureOccurrenceDescription
        
    @property
    def qos_reliability_av(self):
        return self.__qos_reliability_av

    @qos_reliability_av.setter
    def qos_reliability_av(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_reliability_av_ExternalFailureOccurrenceDescription__qos_reliability_av", None)
        self.__qos_reliability_av = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qosannotations_av450"):
                opp_val = getattr(old_value, "qosannotations_av450", None)
                if opp_val == self:
                    setattr(old_value, "qosannotations_av450", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qosannotations_av450"):
                opp_val = getattr(value, "qosannotations_av450", None)
                setattr(value, "qosannotations_av450", self)

    @property
    def pcm_av_reliability_av_ExternalFailureOccurrenceDescription(self):
        return self.__pcm_av_reliability_av_ExternalFailureOccurrenceDescription

    @pcm_av_reliability_av_ExternalFailureOccurrenceDescription.setter
    def pcm_av_reliability_av_ExternalFailureOccurrenceDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_reliability_av_ExternalFailureOccurrenceDescription__pcm_av_reliability_av_ExternalFailureOccurrenceDescription", None)
        self.__pcm_av_reliability_av_ExternalFailureOccurrenceDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FailureType452"):
                opp_val = getattr(old_value, "FailureType452", None)
                if opp_val == self:
                    setattr(old_value, "FailureType452", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FailureType452"):
                opp_val = getattr(value, "FailureType452", None)
                setattr(value, "FailureType452", self)

    def NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription method
        pass

class pcm_av_reliability_av_InternalFailureOccurrenceDescription(FailureOccurrenceDescription):

    def __init__(self, InternalAction: "InternalAction" = None, SoftwareInducedFailureType: "SoftwareInducedFailureType" = None):
        self.InternalAction = InternalAction
        self.SoftwareInducedFailureType = SoftwareInducedFailureType
        
    @property
    def InternalAction(self):
        return self.__InternalAction

    @InternalAction.setter
    def InternalAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_reliability_av_InternalFailureOccurrenceDescription__InternalAction", None)
        self.__InternalAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av444"):
                opp_val = getattr(old_value, "seff_av444", None)
                if opp_val == self:
                    setattr(old_value, "seff_av444", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av444"):
                opp_val = getattr(value, "seff_av444", None)
                setattr(value, "seff_av444", self)

    @property
    def SoftwareInducedFailureType(self):
        return self.__SoftwareInducedFailureType

    @SoftwareInducedFailureType.setter
    def SoftwareInducedFailureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_reliability_av_InternalFailureOccurrenceDescription__SoftwareInducedFailureType", None)
        self.__SoftwareInducedFailureType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reliability_av446"):
                opp_val = getattr(old_value, "reliability_av446", None)
                if opp_val == self:
                    setattr(old_value, "reliability_av446", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reliability_av446"):
                opp_val = getattr(value, "reliability_av446", None)
                setattr(value, "reliability_av446", self)

    def NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription method
        pass

class InternalFailureOccurrenceDescription:

    pass
class ProcessingResourceType:

    pass
class SetVariableAction:

    pass
class CallReturnAction:

    pass
class SynchronisationPoint:

    pass
class CallAction:

    pass
class pcm_av_seff_av_CallReturnAction(CallAction):

    pass
class pcm_av_seff_performance_av_InfrastructureCall(CallAction):

    def __init__(self, pcm_av_seff_performance_av_InfrastructureCall: "InfrastructureSignature" = None, PCMRandomVariable559: "PCMRandomVariable" = None, AbstractInternalControlFlowAction: "AbstractInternalControlFlowAction" = None, pcm_av_seff_performance_av_InfrastructureCall564: "InfrastructureRequiredRole" = None, seff_av415: "pcm_av_parameter_av_VariableUsage"):
        self.pcm_av_seff_performance_av_InfrastructureCall = pcm_av_seff_performance_av_InfrastructureCall
        self.PCMRandomVariable559 = PCMRandomVariable559
        self.AbstractInternalControlFlowAction = AbstractInternalControlFlowAction
        self.pcm_av_seff_performance_av_InfrastructureCall564 = pcm_av_seff_performance_av_InfrastructureCall564
        
    @property
    def pcm_av_seff_performance_av_InfrastructureCall(self):
        return self.__pcm_av_seff_performance_av_InfrastructureCall

    @pcm_av_seff_performance_av_InfrastructureCall.setter
    def pcm_av_seff_performance_av_InfrastructureCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_performance_av_InfrastructureCall__pcm_av_seff_performance_av_InfrastructureCall", None)
        self.__pcm_av_seff_performance_av_InfrastructureCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InfrastructureSignature557"):
                opp_val = getattr(old_value, "InfrastructureSignature557", None)
                if opp_val == self:
                    setattr(old_value, "InfrastructureSignature557", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InfrastructureSignature557"):
                opp_val = getattr(value, "InfrastructureSignature557", None)
                setattr(value, "InfrastructureSignature557", self)

    @property
    def PCMRandomVariable559(self):
        return self.__PCMRandomVariable559

    @PCMRandomVariable559.setter
    def PCMRandomVariable559(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_performance_av_InfrastructureCall__PCMRandomVariable559", None)
        self.__PCMRandomVariable559 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av560"):
                opp_val = getattr(old_value, "core_av560", None)
                if opp_val == self:
                    setattr(old_value, "core_av560", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av560"):
                opp_val = getattr(value, "core_av560", None)
                setattr(value, "core_av560", self)

    @property
    def AbstractInternalControlFlowAction(self):
        return self.__AbstractInternalControlFlowAction

    @AbstractInternalControlFlowAction.setter
    def AbstractInternalControlFlowAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_performance_av_InfrastructureCall__AbstractInternalControlFlowAction", None)
        self.__AbstractInternalControlFlowAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av562"):
                opp_val = getattr(old_value, "seff_av562", None)
                if opp_val == self:
                    setattr(old_value, "seff_av562", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av562"):
                opp_val = getattr(value, "seff_av562", None)
                setattr(value, "seff_av562", self)

    @property
    def pcm_av_seff_performance_av_InfrastructureCall564(self):
        return self.__pcm_av_seff_performance_av_InfrastructureCall564

    @pcm_av_seff_performance_av_InfrastructureCall564.setter
    def pcm_av_seff_performance_av_InfrastructureCall564(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_performance_av_InfrastructureCall__pcm_av_seff_performance_av_InfrastructureCall564", None)
        self.__pcm_av_seff_performance_av_InfrastructureCall564 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InfrastructureRequiredRole565"):
                opp_val = getattr(old_value, "InfrastructureRequiredRole565", None)
                if opp_val == self:
                    setattr(old_value, "InfrastructureRequiredRole565", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InfrastructureRequiredRole565"):
                opp_val = getattr(value, "InfrastructureRequiredRole565", None)
                setattr(value, "InfrastructureRequiredRole565", self)

    def ReferencedRequiredRoleMustBeRequiredByComponent(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ReferencedRequiredRoleMustBeRequiredByComponent method
        pass

    def SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

    def SignatureMustBelongToUsedRequiredRole(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SignatureMustBelongToUsedRequiredRole method
        pass

class pcm_av_seff_performance_av_ResourceCall(CallAction):

    def __init__(self, AbstractInternalControlFlowAction567: "AbstractInternalControlFlowAction" = None, pcm_av_seff_performance_av_ResourceCall: "entity_av_ResourceRequiredRole" = None, pcm_av_seff_performance_av_ResourceCall572: "ResourceSignature" = None, PCMRandomVariable575: "PCMRandomVariable" = None, seff_av415: "pcm_av_parameter_av_VariableUsage"):
        self.AbstractInternalControlFlowAction567 = AbstractInternalControlFlowAction567
        self.pcm_av_seff_performance_av_ResourceCall = pcm_av_seff_performance_av_ResourceCall
        self.pcm_av_seff_performance_av_ResourceCall572 = pcm_av_seff_performance_av_ResourceCall572
        self.PCMRandomVariable575 = PCMRandomVariable575
        
    @property
    def pcm_av_seff_performance_av_ResourceCall572(self):
        return self.__pcm_av_seff_performance_av_ResourceCall572

    @pcm_av_seff_performance_av_ResourceCall572.setter
    def pcm_av_seff_performance_av_ResourceCall572(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_performance_av_ResourceCall__pcm_av_seff_performance_av_ResourceCall572", None)
        self.__pcm_av_seff_performance_av_ResourceCall572 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceSignature573"):
                opp_val = getattr(old_value, "ResourceSignature573", None)
                if opp_val == self:
                    setattr(old_value, "ResourceSignature573", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceSignature573"):
                opp_val = getattr(value, "ResourceSignature573", None)
                setattr(value, "ResourceSignature573", self)

    @property
    def pcm_av_seff_performance_av_ResourceCall(self):
        return self.__pcm_av_seff_performance_av_ResourceCall

    @pcm_av_seff_performance_av_ResourceCall.setter
    def pcm_av_seff_performance_av_ResourceCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_performance_av_ResourceCall__pcm_av_seff_performance_av_ResourceCall", None)
        self.__pcm_av_seff_performance_av_ResourceCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entity_av_ResourceRequiredRole570"):
                opp_val = getattr(old_value, "entity_av_ResourceRequiredRole570", None)
                if opp_val == self:
                    setattr(old_value, "entity_av_ResourceRequiredRole570", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entity_av_ResourceRequiredRole570"):
                opp_val = getattr(value, "entity_av_ResourceRequiredRole570", None)
                setattr(value, "entity_av_ResourceRequiredRole570", self)

    @property
    def PCMRandomVariable575(self):
        return self.__PCMRandomVariable575

    @PCMRandomVariable575.setter
    def PCMRandomVariable575(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_performance_av_ResourceCall__PCMRandomVariable575", None)
        self.__PCMRandomVariable575 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av576"):
                opp_val = getattr(old_value, "core_av576", None)
                if opp_val == self:
                    setattr(old_value, "core_av576", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av576"):
                opp_val = getattr(value, "core_av576", None)
                setattr(value, "core_av576", self)

    @property
    def AbstractInternalControlFlowAction567(self):
        return self.__AbstractInternalControlFlowAction567

    @AbstractInternalControlFlowAction567.setter
    def AbstractInternalControlFlowAction567(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_performance_av_ResourceCall__AbstractInternalControlFlowAction567", None)
        self.__AbstractInternalControlFlowAction567 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av568"):
                opp_val = getattr(old_value, "seff_av568", None)
                if opp_val == self:
                    setattr(old_value, "seff_av568", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av568"):
                opp_val = getattr(value, "seff_av568", None)
                setattr(value, "seff_av568", self)

    def ResourceRequiredRoleMustBeReferencedByComponent(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ResourceRequiredRoleMustBeReferencedByComponent method
        pass

    def ResourceSignatureBelongsToResourceRequiredRole(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ResourceSignatureBelongsToResourceRequiredRole method
        pass

    def SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

class pcm_av_reliability_av_FailureOccurrenceDescription:

    def __init__(self, failureProbability: float):
        self.failureProbability = failureProbability
        
    @property
    def failureProbability(self) -> float:
        return self.__failureProbability

    @failureProbability.setter
    def failureProbability(self, failureProbability: float):
        self.__failureProbability = failureProbability

    def EnsureValidFailureProbabilityRange(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EnsureValidFailureProbabilityRange method
        pass

class Variable:

    pass
class pcm_av_parameter_av_CharacterisedVariable(Variable):

    def __init__(self, characterisationType: str):
        self.characterisationType = characterisationType
        
    @property
    def characterisationType(self) -> str:
        return self.__characterisationType

    @characterisationType.setter
    def characterisationType(self, characterisationType: str):
        self.__characterisationType = characterisationType

class pcm_av_parameter_av_VariableCharacterisation:

    def __init__(self, type: str, PCMRandomVariable434: "PCMRandomVariable" = None, VariableUsage437: "VariableUsage" = None):
        self.type = type
        self.PCMRandomVariable434 = PCMRandomVariable434
        self.VariableUsage437 = VariableUsage437
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def PCMRandomVariable434(self):
        return self.__PCMRandomVariable434

    @PCMRandomVariable434.setter
    def PCMRandomVariable434(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_parameter_av_VariableCharacterisation__PCMRandomVariable434", None)
        self.__PCMRandomVariable434 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av435"):
                opp_val = getattr(old_value, "core_av435", None)
                if opp_val == self:
                    setattr(old_value, "core_av435", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av435"):
                opp_val = getattr(value, "core_av435", None)
                setattr(value, "core_av435", self)

    @property
    def VariableUsage437(self):
        return self.__VariableUsage437

    @VariableUsage437.setter
    def VariableUsage437(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_parameter_av_VariableCharacterisation__VariableUsage437", None)
        self.__VariableUsage437 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameter_av438"):
                opp_val = getattr(old_value, "parameter_av438", None)
                if opp_val == self:
                    setattr(old_value, "parameter_av438", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameter_av438"):
                opp_val = getattr(value, "parameter_av438", None)
                setattr(value, "parameter_av438", self)

class parameter_av_pcm_av_AbstractNamedReference:

    pass
class EntryLevelSystemCall:

    pass
class SpecifiedOutputParameterAbstraction:

    pass
class UnitCarryingElement:

    pass
class HardwareInducedFailureType:

    pass
class ResourceType:

    pass
class pcm_av_resourcetype_av_ProcessingResourceType(ResourceType):

    pass
class pcm_av_parameter_av_VariableUsage:

    pass
class pcm_av_protocol_av_Protocol:

    def __init__(self, protocolTypeID: str):
        self.protocolTypeID = protocolTypeID
        
    @property
    def protocolTypeID(self) -> str:
        return self.__protocolTypeID

    @protocolTypeID.setter
    def protocolTypeID(self, protocolTypeID: str):
        self.__protocolTypeID = protocolTypeID

class NetworkInducedFailureType:

    pass
class pcm_av_resourcetype_av_CommunicationLinkResourceType(ResourceType):

    pass
class SchedulingPolicy:

    pass
class pcm_av_resourcetype_av_ResourceRepository:

    pass
class ResourceRepository:

    pass
class NamedElement:

    pass
class pcm_av_resourceenvironment_av_ResourceEnvironment(NamedElement):

    pass
class pcm_av_repository_av_InnerDeclaration(NamedElement):

    pass
class InnerDeclaration:

    pass
class CompositeDataType:

    pass
class repository_av_DataType:

    pass
class repository_av_ImplementationComponentType:

    pass
class entity_av_ComposedProvidingRequiringEntity:

    pass
class pcm_av_completions_av_Completion(repository_av_ImplementationComponentType, entity_av_ComposedProvidingRequiringEntity):

    pass
class pcm_av_subsystem_av_SubSystem(repository_av_RepositoryComponent, entity_av_ComposedProvidingRequiringEntity):

    pass
class pcm_av_repository_av_CompositeComponent(repository_av_ImplementationComponentType, entity_av_ComposedProvidingRequiringEntity):

    def __init__(self):
        
    def RequireSameInterfaces(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RequireSameInterfaces method
        pass

    def ProvideSameInterfaces(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ProvideSameInterfaces method
        pass

class ProvidesComponentType:

    pass
class OperationInterface:

    pass
class Signature:

    pass
class pcm_av_repository_av_OperationSignature(Signature):

    def __init__(self, OperationInterface: "OperationInterface" = None, Parameter352: set["Parameter"] = None, pcm_av_repository_av_OperationSignature: "DataType" = None, Signature596: "pcm_av_qosannotations_av_SpecifiedQoSAnnotation", Signature608: "pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction", Signature: "pcm_av_seff_av_ServiceEffectSpecification"):
        self.OperationInterface = OperationInterface
        self.Parameter352 = Parameter352 if Parameter352 is not None else set()
        self.pcm_av_repository_av_OperationSignature = pcm_av_repository_av_OperationSignature
        
    @property
    def OperationInterface(self):
        return self.__OperationInterface

    @OperationInterface.setter
    def OperationInterface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_OperationSignature__OperationInterface", None)
        self.__OperationInterface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av350"):
                opp_val = getattr(old_value, "repository_av350", None)
                if opp_val == self:
                    setattr(old_value, "repository_av350", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av350"):
                opp_val = getattr(value, "repository_av350", None)
                setattr(value, "repository_av350", self)

    @property
    def Parameter352(self):
        return self.__Parameter352

    @Parameter352.setter
    def Parameter352(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_OperationSignature__Parameter352", None)
        self.__Parameter352 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_av353"):
                    opp_val = getattr(item, "repository_av353", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_av353", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_av353"):
                    opp_val = getattr(item, "repository_av353", None)
                    
                    setattr(item, "repository_av353", self)
                    

    @property
    def pcm_av_repository_av_OperationSignature(self):
        return self.__pcm_av_repository_av_OperationSignature

    @pcm_av_repository_av_OperationSignature.setter
    def pcm_av_repository_av_OperationSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_OperationSignature__pcm_av_repository_av_OperationSignature", None)
        self.__pcm_av_repository_av_OperationSignature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType355"):
                opp_val = getattr(old_value, "DataType355", None)
                if opp_val == self:
                    setattr(old_value, "DataType355", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType355"):
                opp_val = getattr(value, "DataType355", None)
                setattr(value, "DataType355", self)

    def ParameterNamesHaveToBeUniqueForASignature(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ParameterNamesHaveToBeUniqueForASignature method
        pass

class pcm_av_repository_av_EventType(Signature):

    pass
class InfrastructureInterface:

    pass
class pcm_av_repository_av_InfrastructureSignature(Signature):

    pass
class pcm_av_repository_av_ExceptionType:

    def __init__(self, exceptionName: str, exceptionMessage: str):
        self.exceptionName = exceptionName
        self.exceptionMessage = exceptionMessage
        
    @property
    def exceptionName(self) -> str:
        return self.__exceptionName

    @exceptionName.setter
    def exceptionName(self, exceptionName: str):
        self.__exceptionName = exceptionName

    @property
    def exceptionMessage(self) -> str:
        return self.__exceptionMessage

    @exceptionMessage.setter
    def exceptionMessage(self, exceptionMessage: str):
        self.__exceptionMessage = exceptionMessage

class ExceptionType:

    pass
class Parameter:

    pass
class pcm_av_repository_av_RequiredCharacterisation:

    def __init__(self, type: str, pcm_av_repository_av_RequiredCharacterisation: "Parameter" = None, Interface321: "Interface" = None):
        self.type = type
        self.pcm_av_repository_av_RequiredCharacterisation = pcm_av_repository_av_RequiredCharacterisation
        self.Interface321 = Interface321
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def Interface321(self):
        return self.__Interface321

    @Interface321.setter
    def Interface321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_RequiredCharacterisation__Interface321", None)
        self.__Interface321 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av322"):
                opp_val = getattr(old_value, "repository_av322", None)
                if opp_val == self:
                    setattr(old_value, "repository_av322", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av322"):
                opp_val = getattr(value, "repository_av322", None)
                setattr(value, "repository_av322", self)

    @property
    def pcm_av_repository_av_RequiredCharacterisation(self):
        return self.__pcm_av_repository_av_RequiredCharacterisation

    @pcm_av_repository_av_RequiredCharacterisation.setter
    def pcm_av_repository_av_RequiredCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_RequiredCharacterisation__pcm_av_repository_av_RequiredCharacterisation", None)
        self.__pcm_av_repository_av_RequiredCharacterisation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Parameter"):
                opp_val = getattr(old_value, "Parameter", None)
                if opp_val == self:
                    setattr(old_value, "Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Parameter"):
                opp_val = getattr(value, "Parameter", None)
                setattr(value, "Parameter", self)

class RequiredCharacterisation:

    pass
class Protocol:

    pass
class InfrastructureSignature:

    pass
class DataType:

    pass
class pcm_av_repository_av_PrimitiveDataType(DataType):

    def __init__(self, type: str, DataType371: "pcm_av_repository_av_CollectionDataType", DataType355: "pcm_av_repository_av_OperationSignature", DataType: "pcm_av_repository_av_Parameter", repository_av309: "pcm_av_repository_av_Repository", DataType376: "pcm_av_repository_av_InnerDeclaration"):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class pcm_av_repository_av_Parameter:

    def __init__(self, parameterName: str, modifier__Parameter: str, OperationSignature292: "OperationSignature" = None, EventType: "EventType" = None, ResourceSignature: "ResourceSignature" = None, pcm_av_repository_av_Parameter: "DataType" = None, InfrastructureSignature: "InfrastructureSignature" = None):
        self.parameterName = parameterName
        self.modifier__Parameter = modifier__Parameter
        self.OperationSignature292 = OperationSignature292
        self.EventType = EventType
        self.ResourceSignature = ResourceSignature
        self.pcm_av_repository_av_Parameter = pcm_av_repository_av_Parameter
        self.InfrastructureSignature = InfrastructureSignature
        
    @property
    def parameterName(self) -> str:
        return self.__parameterName

    @parameterName.setter
    def parameterName(self, parameterName: str):
        self.__parameterName = parameterName

    @property
    def modifier__Parameter(self) -> str:
        return self.__modifier__Parameter

    @modifier__Parameter.setter
    def modifier__Parameter(self, modifier__Parameter: str):
        self.__modifier__Parameter = modifier__Parameter

    @property
    def OperationSignature292(self):
        return self.__OperationSignature292

    @OperationSignature292.setter
    def OperationSignature292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_Parameter__OperationSignature292", None)
        self.__OperationSignature292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av293"):
                opp_val = getattr(old_value, "repository_av293", None)
                if opp_val == self:
                    setattr(old_value, "repository_av293", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av293"):
                opp_val = getattr(value, "repository_av293", None)
                setattr(value, "repository_av293", self)

    @property
    def ResourceSignature(self):
        return self.__ResourceSignature

    @ResourceSignature.setter
    def ResourceSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_Parameter__ResourceSignature", None)
        self.__ResourceSignature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcetype_av"):
                opp_val = getattr(old_value, "resourcetype_av", None)
                if opp_val == self:
                    setattr(old_value, "resourcetype_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcetype_av"):
                opp_val = getattr(value, "resourcetype_av", None)
                setattr(value, "resourcetype_av", self)

    @property
    def InfrastructureSignature(self):
        return self.__InfrastructureSignature

    @InfrastructureSignature.setter
    def InfrastructureSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_Parameter__InfrastructureSignature", None)
        self.__InfrastructureSignature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av290"):
                opp_val = getattr(old_value, "repository_av290", None)
                if opp_val == self:
                    setattr(old_value, "repository_av290", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av290"):
                opp_val = getattr(value, "repository_av290", None)
                setattr(value, "repository_av290", self)

    @property
    def EventType(self):
        return self.__EventType

    @EventType.setter
    def EventType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_Parameter__EventType", None)
        self.__EventType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av295"):
                opp_val = getattr(old_value, "repository_av295", None)
                if opp_val == self:
                    setattr(old_value, "repository_av295", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av295"):
                opp_val = getattr(value, "repository_av295", None)
                setattr(value, "repository_av295", self)

    @property
    def pcm_av_repository_av_Parameter(self):
        return self.__pcm_av_repository_av_Parameter

    @pcm_av_repository_av_Parameter.setter
    def pcm_av_repository_av_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_Parameter__pcm_av_repository_av_Parameter", None)
        self.__pcm_av_repository_av_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType"):
                opp_val = getattr(old_value, "DataType", None)
                if opp_val == self:
                    setattr(old_value, "DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType"):
                opp_val = getattr(value, "DataType", None)
                setattr(value, "DataType", self)

class FailureType:

    pass
class pcm_av_reliability_av_HardwareInducedFailureType(FailureType):

    def __init__(self, ProcessingResourceType: "ProcessingResourceType" = None, FailureType594: "pcm_av_seff_reliability_av_FailureHandlingEntity", reliability_av306: "pcm_av_repository_av_Repository", FailureType335: "pcm_av_repository_av_Signature", FailureType452: "pcm_av_reliability_av_ExternalFailureOccurrenceDescription"):
        self.ProcessingResourceType = ProcessingResourceType
        
    @property
    def ProcessingResourceType(self):
        return self.__ProcessingResourceType

    @ProcessingResourceType.setter
    def ProcessingResourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_reliability_av_HardwareInducedFailureType__ProcessingResourceType", None)
        self.__ProcessingResourceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcetype_av440"):
                opp_val = getattr(old_value, "resourcetype_av440", None)
                if opp_val == self:
                    setattr(old_value, "resourcetype_av440", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcetype_av440"):
                opp_val = getattr(value, "resourcetype_av440", None)
                setattr(value, "resourcetype_av440", self)

    def HardwareInducedFailureTypeHasProcessingResourceType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement HardwareInducedFailureTypeHasProcessingResourceType method
        pass

class pcm_av_reliability_av_NetworkInducedFailureType(FailureType):

    def __init__(self, CommunicationLinkResourceType: "CommunicationLinkResourceType" = None, FailureType594: "pcm_av_seff_reliability_av_FailureHandlingEntity", reliability_av306: "pcm_av_repository_av_Repository", FailureType335: "pcm_av_repository_av_Signature", FailureType452: "pcm_av_reliability_av_ExternalFailureOccurrenceDescription"):
        self.CommunicationLinkResourceType = CommunicationLinkResourceType
        
    @property
    def CommunicationLinkResourceType(self):
        return self.__CommunicationLinkResourceType

    @CommunicationLinkResourceType.setter
    def CommunicationLinkResourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_reliability_av_NetworkInducedFailureType__CommunicationLinkResourceType", None)
        self.__CommunicationLinkResourceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcetype_av448"):
                opp_val = getattr(old_value, "resourcetype_av448", None)
                if opp_val == self:
                    setattr(old_value, "resourcetype_av448", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcetype_av448"):
                opp_val = getattr(value, "resourcetype_av448", None)
                setattr(value, "resourcetype_av448", self)

    def NetworkInducedFailureTypeHasCommunicationLinkResourceType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement NetworkInducedFailureTypeHasCommunicationLinkResourceType method
        pass

class pcm_av_reliability_av_SoftwareInducedFailureType(FailureType):

    pass
class Interface:

    pass
class pcm_av_repository_av_EventGroup(Interface):

    pass
class pcm_av_repository_av_InfrastructureInterface(Interface):

    pass
class pcm_av_repository_av_OperationInterface(Interface):

    def __init__(self, OperationSignature357: set["OperationSignature"] = None, repository_av304: "pcm_av_repository_av_Repository", repository_av322: "pcm_av_repository_av_RequiredCharacterisation", Interface311: "pcm_av_repository_av_Interface"):
        self.OperationSignature357 = OperationSignature357 if OperationSignature357 is not None else set()
        
    @property
    def OperationSignature357(self):
        return self.__OperationSignature357

    @OperationSignature357.setter
    def OperationSignature357(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_OperationInterface__OperationSignature357", None)
        self.__OperationSignature357 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_av358"):
                    opp_val = getattr(item, "repository_av358", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_av358", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_av358"):
                    opp_val = getattr(item, "repository_av358", None)
                    
                    setattr(item, "repository_av358", self)
                    

    def SignaturesHaveToBeUniqueForAnInterface(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SignaturesHaveToBeUniqueForAnInterface method
        pass

class pcm_av_repository_av_DataType:

    pass
class ResourceSignature:

    pass
class EventType:

    pass
class Repository:

    pass
class InterfaceProvidingRequiringEntity:

    pass
class pcm_av_repository_av_RepositoryComponent(InterfaceProvidingRequiringEntity):

    pass
class CompleteComponentType:

    pass
class ServiceEffectSpecification:

    pass
class ImplementationComponentType:

    pass
class pcm_av_repository_av_BasicComponent(ImplementationComponentType):

    def __init__(self, ServiceEffectSpecification: set["ServiceEffectSpecification"] = None, PassiveResource277: set["PassiveResource"] = None):
        self.ServiceEffectSpecification = ServiceEffectSpecification if ServiceEffectSpecification is not None else set()
        self.PassiveResource277 = PassiveResource277 if PassiveResource277 is not None else set()
        
    @property
    def PassiveResource277(self):
        return self.__PassiveResource277

    @PassiveResource277.setter
    def PassiveResource277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_BasicComponent__PassiveResource277", None)
        self.__PassiveResource277 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_av278"):
                    opp_val = getattr(item, "repository_av278", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_av278", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_av278"):
                    opp_val = getattr(item, "repository_av278", None)
                    
                    setattr(item, "repository_av278", self)
                    

    @property
    def ServiceEffectSpecification(self):
        return self.__ServiceEffectSpecification

    @ServiceEffectSpecification.setter
    def ServiceEffectSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_BasicComponent__ServiceEffectSpecification", None)
        self.__ServiceEffectSpecification = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_av275"):
                    opp_val = getattr(item, "seff_av275", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_av275", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_av275"):
                    opp_val = getattr(item, "seff_av275", None)
                    
                    setattr(item, "seff_av275", self)
                    

    def NoSeffTypeUsedTwice(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NoSeffTypeUsedTwice method
        pass

    def RequireSameInterfacesAsImplementationType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RequireSameInterfacesAsImplementationType method
        pass

    def ProvideSameInterfacesAsImplementationType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ProvideSameInterfacesAsImplementationType method
        pass

class ResourceTimeoutFailureType:

    pass
class BasicComponent:

    pass
class Branch:

    pass
class pcm_av_usagemodel_av_BranchTransition:

    def __init__(self, branchProbability: float, Branch: "Branch" = None, ScenarioBehaviour248: "ScenarioBehaviour" = None):
        self.branchProbability = branchProbability
        self.Branch = Branch
        self.ScenarioBehaviour248 = ScenarioBehaviour248
        
    @property
    def branchProbability(self) -> float:
        return self.__branchProbability

    @branchProbability.setter
    def branchProbability(self, branchProbability: float):
        self.__branchProbability = branchProbability

    @property
    def ScenarioBehaviour248(self):
        return self.__ScenarioBehaviour248

    @ScenarioBehaviour248.setter
    def ScenarioBehaviour248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_usagemodel_av_BranchTransition__ScenarioBehaviour248", None)
        self.__ScenarioBehaviour248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av249"):
                opp_val = getattr(old_value, "usagemodel_av249", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av249", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av249"):
                opp_val = getattr(value, "usagemodel_av249", None)
                setattr(value, "usagemodel_av249", self)

    @property
    def Branch(self):
        return self.__Branch

    @Branch.setter
    def Branch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_usagemodel_av_BranchTransition__Branch", None)
        self.__Branch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av246"):
                opp_val = getattr(old_value, "usagemodel_av246", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av246", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av246"):
                opp_val = getattr(value, "usagemodel_av246", None)
                setattr(value, "usagemodel_av246", self)

class BranchTransition:

    pass
class AbstractUserAction:

    pass
class pcm_av_usagemodel_av_Branch(AbstractUserAction):

    def __init__(self, BranchTransition251: set["BranchTransition"] = None, usagemodel_av230: "pcm_av_usagemodel_av_AbstractUserAction", usagemodel_av227: "pcm_av_usagemodel_av_AbstractUserAction", usagemodel_av244: "pcm_av_usagemodel_av_ScenarioBehaviour"):
        self.BranchTransition251 = BranchTransition251 if BranchTransition251 is not None else set()
        
    @property
    def BranchTransition251(self):
        return self.__BranchTransition251

    @BranchTransition251.setter
    def BranchTransition251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_usagemodel_av_Branch__BranchTransition251", None)
        self.__BranchTransition251 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "usagemodel_av252"):
                    opp_val = getattr(item, "usagemodel_av252", None)
                    
                    if opp_val == self:
                        setattr(item, "usagemodel_av252", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "usagemodel_av252"):
                    opp_val = getattr(item, "usagemodel_av252", None)
                    
                    setattr(item, "usagemodel_av252", self)
                    

    def AllBranchProbabilitiesMustSumUpTo1(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AllBranchProbabilitiesMustSumUpTo1 method
        pass

class pcm_av_usagemodel_av_Delay(AbstractUserAction):

    pass
class pcm_av_usagemodel_av_Stop(AbstractUserAction):

    def __init__(self, usagemodel_av230: "pcm_av_usagemodel_av_AbstractUserAction", usagemodel_av227: "pcm_av_usagemodel_av_AbstractUserAction", usagemodel_av244: "pcm_av_usagemodel_av_ScenarioBehaviour"):
        
    def StopHasNoSuccessor(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement StopHasNoSuccessor method
        pass

class pcm_av_usagemodel_av_Start(AbstractUserAction):

    def __init__(self, usagemodel_av230: "pcm_av_usagemodel_av_AbstractUserAction", usagemodel_av227: "pcm_av_usagemodel_av_AbstractUserAction", usagemodel_av244: "pcm_av_usagemodel_av_ScenarioBehaviour"):
        
    def StartHasNoPredecessor(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement StartHasNoPredecessor method
        pass

class pcm_av_usagemodel_av_Loop(AbstractUserAction):

    pass
class pcm_av_usagemodel_av_EntryLevelSystemCall(AbstractUserAction):

    def __init__(self, priority: int, pcm_av_usagemodel_av_EntryLevelSystemCall: "OperationProvidedRole" = None, pcm_av_usagemodel_av_EntryLevelSystemCall219: "OperationSignature" = None, VariableUsage221: set["VariableUsage"] = None, VariableUsage224: set["VariableUsage"] = None, usagemodel_av230: "pcm_av_usagemodel_av_AbstractUserAction", usagemodel_av227: "pcm_av_usagemodel_av_AbstractUserAction", usagemodel_av244: "pcm_av_usagemodel_av_ScenarioBehaviour"):
        self.priority = priority
        self.pcm_av_usagemodel_av_EntryLevelSystemCall = pcm_av_usagemodel_av_EntryLevelSystemCall
        self.pcm_av_usagemodel_av_EntryLevelSystemCall219 = pcm_av_usagemodel_av_EntryLevelSystemCall219
        self.VariableUsage221 = VariableUsage221 if VariableUsage221 is not None else set()
        self.VariableUsage224 = VariableUsage224 if VariableUsage224 is not None else set()
        
    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def VariableUsage221(self):
        return self.__VariableUsage221

    @VariableUsage221.setter
    def VariableUsage221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_usagemodel_av_EntryLevelSystemCall__VariableUsage221", None)
        self.__VariableUsage221 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "parameter_av222"):
                    opp_val = getattr(item, "parameter_av222", None)
                    
                    if opp_val == self:
                        setattr(item, "parameter_av222", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "parameter_av222"):
                    opp_val = getattr(item, "parameter_av222", None)
                    
                    setattr(item, "parameter_av222", self)
                    

    @property
    def pcm_av_usagemodel_av_EntryLevelSystemCall(self):
        return self.__pcm_av_usagemodel_av_EntryLevelSystemCall

    @pcm_av_usagemodel_av_EntryLevelSystemCall.setter
    def pcm_av_usagemodel_av_EntryLevelSystemCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_usagemodel_av_EntryLevelSystemCall__pcm_av_usagemodel_av_EntryLevelSystemCall", None)
        self.__pcm_av_usagemodel_av_EntryLevelSystemCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationProvidedRole217"):
                opp_val = getattr(old_value, "OperationProvidedRole217", None)
                if opp_val == self:
                    setattr(old_value, "OperationProvidedRole217", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationProvidedRole217"):
                opp_val = getattr(value, "OperationProvidedRole217", None)
                setattr(value, "OperationProvidedRole217", self)

    @property
    def pcm_av_usagemodel_av_EntryLevelSystemCall219(self):
        return self.__pcm_av_usagemodel_av_EntryLevelSystemCall219

    @pcm_av_usagemodel_av_EntryLevelSystemCall219.setter
    def pcm_av_usagemodel_av_EntryLevelSystemCall219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_usagemodel_av_EntryLevelSystemCall__pcm_av_usagemodel_av_EntryLevelSystemCall219", None)
        self.__pcm_av_usagemodel_av_EntryLevelSystemCall219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationSignature"):
                opp_val = getattr(old_value, "OperationSignature", None)
                if opp_val == self:
                    setattr(old_value, "OperationSignature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationSignature"):
                opp_val = getattr(value, "OperationSignature", None)
                setattr(value, "OperationSignature", self)

    @property
    def VariableUsage224(self):
        return self.__VariableUsage224

    @VariableUsage224.setter
    def VariableUsage224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_usagemodel_av_EntryLevelSystemCall__VariableUsage224", None)
        self.__VariableUsage224 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "parameter_av225"):
                    opp_val = getattr(item, "parameter_av225", None)
                    
                    if opp_val == self:
                        setattr(item, "parameter_av225", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "parameter_av225"):
                    opp_val = getattr(item, "parameter_av225", None)
                    
                    setattr(item, "parameter_av225", self)
                    

    def EntryLevelSystemCallMustReferenceProvidedRoleOfASystem(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement EntryLevelSystemCallMustReferenceProvidedRoleOfASystem method
        pass

    def EntryLevelSystemCallSignatureMustMatchItsProvidedRole(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EntryLevelSystemCallSignatureMustMatchItsProvidedRole method
        pass

class OperationSignature:

    pass
class VariableUsage:

    pass
class RepositoryComponent:

    pass
class pcm_av_repository_av_ImplementationComponentType(RepositoryComponent):

    def __init__(self, componentType: str, pcm_av_repository_av_ImplementationComponentType: set["CompleteComponentType"] = None, pcm_av_repository_av_ImplementationComponentType281: set["VariableUsage"] = None, RepositoryComponent: "pcm_av_composition_av_AssemblyContext", repository_av302: "pcm_av_repository_av_Repository"):
        self.componentType = componentType
        self.pcm_av_repository_av_ImplementationComponentType = pcm_av_repository_av_ImplementationComponentType if pcm_av_repository_av_ImplementationComponentType is not None else set()
        self.pcm_av_repository_av_ImplementationComponentType281 = pcm_av_repository_av_ImplementationComponentType281 if pcm_av_repository_av_ImplementationComponentType281 is not None else set()
        
    @property
    def componentType(self) -> str:
        return self.__componentType

    @componentType.setter
    def componentType(self, componentType: str):
        self.__componentType = componentType

    @property
    def pcm_av_repository_av_ImplementationComponentType(self):
        return self.__pcm_av_repository_av_ImplementationComponentType

    @pcm_av_repository_av_ImplementationComponentType.setter
    def pcm_av_repository_av_ImplementationComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_ImplementationComponentType__pcm_av_repository_av_ImplementationComponentType", None)
        self.__pcm_av_repository_av_ImplementationComponentType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteComponentType"):
                    opp_val = getattr(item, "CompleteComponentType", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteComponentType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteComponentType"):
                    opp_val = getattr(item, "CompleteComponentType", None)
                    
                    setattr(item, "CompleteComponentType", self)
                    

    @property
    def pcm_av_repository_av_ImplementationComponentType281(self):
        return self.__pcm_av_repository_av_ImplementationComponentType281

    @pcm_av_repository_av_ImplementationComponentType281.setter
    def pcm_av_repository_av_ImplementationComponentType281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_ImplementationComponentType__pcm_av_repository_av_ImplementationComponentType281", None)
        self.__pcm_av_repository_av_ImplementationComponentType281 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableUsage282"):
                    opp_val = getattr(item, "VariableUsage282", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableUsage282", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableUsage282"):
                    opp_val = getattr(item, "VariableUsage282", None)
                    
                    setattr(item, "VariableUsage282", self)
                    

    def RequiredInterfacesHaveToConformToCompleteType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RequiredInterfacesHaveToConformToCompleteType method
        pass

    def providedInterfacesHaveToConformToCompleteType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement providedInterfacesHaveToConformToCompleteType method
        pass

    def ProvidedInterfaceHaveToConformToComponentType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ProvidedInterfaceHaveToConformToComponentType method
        pass

class pcm_av_repository_av_ProvidesComponentType(RepositoryComponent):

    def __init__(self, RepositoryComponent: "pcm_av_composition_av_AssemblyContext", repository_av302: "pcm_av_repository_av_Repository"):
        
    def AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType method
        pass

class pcm_av_repository_av_CompleteComponentType(RepositoryComponent):

    def __init__(self, pcm_av_repository_av_CompleteComponentType: set["ProvidesComponentType"] = None, RepositoryComponent: "pcm_av_composition_av_AssemblyContext", repository_av302: "pcm_av_repository_av_Repository"):
        self.pcm_av_repository_av_CompleteComponentType = pcm_av_repository_av_CompleteComponentType if pcm_av_repository_av_CompleteComponentType is not None else set()
        
    @property
    def pcm_av_repository_av_CompleteComponentType(self):
        return self.__pcm_av_repository_av_CompleteComponentType

    @pcm_av_repository_av_CompleteComponentType.setter
    def pcm_av_repository_av_CompleteComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_CompleteComponentType__pcm_av_repository_av_CompleteComponentType", None)
        self.__pcm_av_repository_av_CompleteComponentType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProvidesComponentType"):
                    opp_val = getattr(item, "ProvidesComponentType", None)
                    
                    if opp_val == self:
                        setattr(item, "ProvidesComponentType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProvidesComponentType"):
                    opp_val = getattr(item, "ProvidesComponentType", None)
                    
                    setattr(item, "ProvidesComponentType", self)
                    

    def providedInterfacesHaveToConformToProvidedType2(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement providedInterfacesHaveToConformToProvidedType2 method
        pass

    def AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType method
        pass

class UserData:

    pass
class pcm_av_usagemodel_av_UsageModel:

    pass
class pcm_av_usagemodel_av_UserData:

    pass
class Workload:

    pass
class pcm_av_usagemodel_av_OpenWorkload(Workload):

    def __init__(self, PCMRandomVariable260: "PCMRandomVariable" = None, usagemodel_av202: "pcm_av_usagemodel_av_UsageScenario"):
        self.PCMRandomVariable260 = PCMRandomVariable260
        
    @property
    def PCMRandomVariable260(self):
        return self.__PCMRandomVariable260

    @PCMRandomVariable260.setter
    def PCMRandomVariable260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_usagemodel_av_OpenWorkload__PCMRandomVariable260", None)
        self.__PCMRandomVariable260 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av261"):
                opp_val = getattr(old_value, "core_av261", None)
                if opp_val == self:
                    setattr(old_value, "core_av261", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av261"):
                opp_val = getattr(value, "core_av261", None)
                setattr(value, "core_av261", self)

    def InterArrivalTimeInOpenWorkloadNeedsToBeSpecified(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement InterArrivalTimeInOpenWorkloadNeedsToBeSpecified method
        pass

class pcm_av_usagemodel_av_ClosedWorkload(Workload):

    def __init__(self, population: int, PCMRandomVariable266: "PCMRandomVariable" = None, usagemodel_av202: "pcm_av_usagemodel_av_UsageScenario"):
        self.population = population
        self.PCMRandomVariable266 = PCMRandomVariable266
        
    @property
    def population(self) -> int:
        return self.__population

    @population.setter
    def population(self, population: int):
        self.__population = population

    @property
    def PCMRandomVariable266(self):
        return self.__PCMRandomVariable266

    @PCMRandomVariable266.setter
    def PCMRandomVariable266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_usagemodel_av_ClosedWorkload__PCMRandomVariable266", None)
        self.__PCMRandomVariable266 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av267"):
                opp_val = getattr(old_value, "core_av267", None)
                if opp_val == self:
                    setattr(old_value, "core_av267", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av267"):
                opp_val = getattr(value, "core_av267", None)
                setattr(value, "core_av267", self)

    def PopulationInClosedWorkloadNeedsToBeSpecified(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement PopulationInClosedWorkloadNeedsToBeSpecified method
        pass

    def ThinkTimeInClosedWorkloadNeedsToBeSpecified(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ThinkTimeInClosedWorkloadNeedsToBeSpecified method
        pass

class ScenarioBehaviour:

    pass
class UsageModel:

    pass
class UsageScenario:

    pass
class pcm_av_usagemodel_av_Workload:

    pass
class InfrastructureRequiredRole:

    pass
class InfrastructureProvidedRole:

    pass
class OperationRequiredRole:

    pass
class composition_av_Connector:

    pass
class OperationProvidedRole:

    pass
class composition_av_EventChannel:

    pass
class DelegationConnector:

    pass
class pcm_av_composition_av_RequiredDelegationConnector(DelegationConnector):

    def __init__(self, pcm_av_composition_av_RequiredDelegationConnector: "OperationRequiredRole" = None, pcm_av_composition_av_RequiredDelegationConnector110: "OperationRequiredRole" = None, pcm_av_composition_av_RequiredDelegationConnector113: "composition_av_AssemblyContext" = None):
        self.pcm_av_composition_av_RequiredDelegationConnector = pcm_av_composition_av_RequiredDelegationConnector
        self.pcm_av_composition_av_RequiredDelegationConnector110 = pcm_av_composition_av_RequiredDelegationConnector110
        self.pcm_av_composition_av_RequiredDelegationConnector113 = pcm_av_composition_av_RequiredDelegationConnector113
        
    @property
    def pcm_av_composition_av_RequiredDelegationConnector113(self):
        return self.__pcm_av_composition_av_RequiredDelegationConnector113

    @pcm_av_composition_av_RequiredDelegationConnector113.setter
    def pcm_av_composition_av_RequiredDelegationConnector113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_composition_av_RequiredDelegationConnector__pcm_av_composition_av_RequiredDelegationConnector113", None)
        self.__pcm_av_composition_av_RequiredDelegationConnector113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_AssemblyContext114"):
                opp_val = getattr(old_value, "composition_av_AssemblyContext114", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_AssemblyContext114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_AssemblyContext114"):
                opp_val = getattr(value, "composition_av_AssemblyContext114", None)
                setattr(value, "composition_av_AssemblyContext114", self)

    @property
    def pcm_av_composition_av_RequiredDelegationConnector110(self):
        return self.__pcm_av_composition_av_RequiredDelegationConnector110

    @pcm_av_composition_av_RequiredDelegationConnector110.setter
    def pcm_av_composition_av_RequiredDelegationConnector110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_composition_av_RequiredDelegationConnector__pcm_av_composition_av_RequiredDelegationConnector110", None)
        self.__pcm_av_composition_av_RequiredDelegationConnector110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationRequiredRole111"):
                opp_val = getattr(old_value, "OperationRequiredRole111", None)
                if opp_val == self:
                    setattr(old_value, "OperationRequiredRole111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationRequiredRole111"):
                opp_val = getattr(value, "OperationRequiredRole111", None)
                setattr(value, "OperationRequiredRole111", self)

    @property
    def pcm_av_composition_av_RequiredDelegationConnector(self):
        return self.__pcm_av_composition_av_RequiredDelegationConnector

    @pcm_av_composition_av_RequiredDelegationConnector.setter
    def pcm_av_composition_av_RequiredDelegationConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_composition_av_RequiredDelegationConnector__pcm_av_composition_av_RequiredDelegationConnector", None)
        self.__pcm_av_composition_av_RequiredDelegationConnector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationRequiredRole"):
                opp_val = getattr(old_value, "OperationRequiredRole", None)
                if opp_val == self:
                    setattr(old_value, "OperationRequiredRole", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationRequiredRole"):
                opp_val = getattr(value, "OperationRequiredRole", None)
                setattr(value, "OperationRequiredRole", self)

    def RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector method
        pass

    def ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame method
        pass

    def RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

class pcm_av_composition_av_RequiredInfrastructureDelegationConnector(DelegationConnector):

    pass
class pcm_av_composition_av_SinkDelegationConnector(DelegationConnector):

    pass
class pcm_av_composition_av_RequiredResourceDelegationConnector(DelegationConnector):

    pass
class pcm_av_composition_av_SourceDelegationConnector(DelegationConnector):

    pass
class pcm_av_composition_av_ProvidedInfrastructureDelegationConnector(DelegationConnector):

    pass
class pcm_av_composition_av_ProvidedDelegationConnector(DelegationConnector):

    def __init__(self, pcm_av_composition_av_ProvidedDelegationConnector: "OperationProvidedRole" = None, pcm_av_composition_av_ProvidedDelegationConnector103: "OperationProvidedRole" = None, pcm_av_composition_av_ProvidedDelegationConnector106: "composition_av_AssemblyContext" = None):
        self.pcm_av_composition_av_ProvidedDelegationConnector = pcm_av_composition_av_ProvidedDelegationConnector
        self.pcm_av_composition_av_ProvidedDelegationConnector103 = pcm_av_composition_av_ProvidedDelegationConnector103
        self.pcm_av_composition_av_ProvidedDelegationConnector106 = pcm_av_composition_av_ProvidedDelegationConnector106
        
    @property
    def pcm_av_composition_av_ProvidedDelegationConnector(self):
        return self.__pcm_av_composition_av_ProvidedDelegationConnector

    @pcm_av_composition_av_ProvidedDelegationConnector.setter
    def pcm_av_composition_av_ProvidedDelegationConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_composition_av_ProvidedDelegationConnector__pcm_av_composition_av_ProvidedDelegationConnector", None)
        self.__pcm_av_composition_av_ProvidedDelegationConnector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationProvidedRole"):
                opp_val = getattr(old_value, "OperationProvidedRole", None)
                if opp_val == self:
                    setattr(old_value, "OperationProvidedRole", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationProvidedRole"):
                opp_val = getattr(value, "OperationProvidedRole", None)
                setattr(value, "OperationProvidedRole", self)

    @property
    def pcm_av_composition_av_ProvidedDelegationConnector103(self):
        return self.__pcm_av_composition_av_ProvidedDelegationConnector103

    @pcm_av_composition_av_ProvidedDelegationConnector103.setter
    def pcm_av_composition_av_ProvidedDelegationConnector103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_composition_av_ProvidedDelegationConnector__pcm_av_composition_av_ProvidedDelegationConnector103", None)
        self.__pcm_av_composition_av_ProvidedDelegationConnector103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationProvidedRole104"):
                opp_val = getattr(old_value, "OperationProvidedRole104", None)
                if opp_val == self:
                    setattr(old_value, "OperationProvidedRole104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationProvidedRole104"):
                opp_val = getattr(value, "OperationProvidedRole104", None)
                setattr(value, "OperationProvidedRole104", self)

    @property
    def pcm_av_composition_av_ProvidedDelegationConnector106(self):
        return self.__pcm_av_composition_av_ProvidedDelegationConnector106

    @pcm_av_composition_av_ProvidedDelegationConnector106.setter
    def pcm_av_composition_av_ProvidedDelegationConnector106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_composition_av_ProvidedDelegationConnector__pcm_av_composition_av_ProvidedDelegationConnector106", None)
        self.__pcm_av_composition_av_ProvidedDelegationConnector106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_AssemblyContext107"):
                opp_val = getattr(old_value, "composition_av_AssemblyContext107", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_AssemblyContext107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_AssemblyContext107"):
                opp_val = getattr(value, "composition_av_AssemblyContext107", None)
                setattr(value, "composition_av_AssemblyContext107", self)

    def ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

    def ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame method
        pass

class PCMRandomVariable:

    pass
class SinkRole:

    pass
class SourceRole:

    pass
class composition_av_EventChannelSourceConnector:

    pass
class EventGroup:

    pass
class pcm_av_composition_av_ResourceRequiredDelegationConnector:

    pass
class entity_av_InterfaceProvidingRequiringEntity:

    pass
class composition_av_ComposedStructure:

    pass
class pcm_av_entity_av_ComposedProvidingRequiringEntity(composition_av_ComposedStructure, entity_av_InterfaceProvidingRequiringEntity):

    def __init__(self, core_av75: "pcm_av_composition_av_ResourceRequiredDelegationConnector", core_av56: "pcm_av_composition_av_Connector", core_av191: "pcm_av_composition_av_AssemblyContext", core_av85: "pcm_av_composition_av_EventChannel"):
        
    def ProvidedRolesMustBeBound(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ProvidedRolesMustBeBound method
        pass

class entity_av_ResourceProvidedRole:

    pass
class composition_av_ResourceRequiredDelegationConnector:

    pass
class composition_av_AssemblyContext:

    pass
class Connector:

    pass
class pcm_av_composition_av_AssemblyConnector(Connector):

    def __init__(self, pcm_av_composition_av_AssemblyConnector: "composition_av_AssemblyContext" = None, pcm_av_composition_av_AssemblyConnector118: "composition_av_AssemblyContext" = None, pcm_av_composition_av_AssemblyConnector121: "OperationProvidedRole" = None, pcm_av_composition_av_AssemblyConnector124: "OperationRequiredRole" = None):
        self.pcm_av_composition_av_AssemblyConnector = pcm_av_composition_av_AssemblyConnector
        self.pcm_av_composition_av_AssemblyConnector118 = pcm_av_composition_av_AssemblyConnector118
        self.pcm_av_composition_av_AssemblyConnector121 = pcm_av_composition_av_AssemblyConnector121
        self.pcm_av_composition_av_AssemblyConnector124 = pcm_av_composition_av_AssemblyConnector124
        
    @property
    def pcm_av_composition_av_AssemblyConnector(self):
        return self.__pcm_av_composition_av_AssemblyConnector

    @pcm_av_composition_av_AssemblyConnector.setter
    def pcm_av_composition_av_AssemblyConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_composition_av_AssemblyConnector__pcm_av_composition_av_AssemblyConnector", None)
        self.__pcm_av_composition_av_AssemblyConnector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_AssemblyContext116"):
                opp_val = getattr(old_value, "composition_av_AssemblyContext116", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_AssemblyContext116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_AssemblyContext116"):
                opp_val = getattr(value, "composition_av_AssemblyContext116", None)
                setattr(value, "composition_av_AssemblyContext116", self)

    @property
    def pcm_av_composition_av_AssemblyConnector124(self):
        return self.__pcm_av_composition_av_AssemblyConnector124

    @pcm_av_composition_av_AssemblyConnector124.setter
    def pcm_av_composition_av_AssemblyConnector124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_composition_av_AssemblyConnector__pcm_av_composition_av_AssemblyConnector124", None)
        self.__pcm_av_composition_av_AssemblyConnector124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationRequiredRole125"):
                opp_val = getattr(old_value, "OperationRequiredRole125", None)
                if opp_val == self:
                    setattr(old_value, "OperationRequiredRole125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationRequiredRole125"):
                opp_val = getattr(value, "OperationRequiredRole125", None)
                setattr(value, "OperationRequiredRole125", self)

    @property
    def pcm_av_composition_av_AssemblyConnector118(self):
        return self.__pcm_av_composition_av_AssemblyConnector118

    @pcm_av_composition_av_AssemblyConnector118.setter
    def pcm_av_composition_av_AssemblyConnector118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_composition_av_AssemblyConnector__pcm_av_composition_av_AssemblyConnector118", None)
        self.__pcm_av_composition_av_AssemblyConnector118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_AssemblyContext119"):
                opp_val = getattr(old_value, "composition_av_AssemblyContext119", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_AssemblyContext119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_AssemblyContext119"):
                opp_val = getattr(value, "composition_av_AssemblyContext119", None)
                setattr(value, "composition_av_AssemblyContext119", self)

    @property
    def pcm_av_composition_av_AssemblyConnector121(self):
        return self.__pcm_av_composition_av_AssemblyConnector121

    @pcm_av_composition_av_AssemblyConnector121.setter
    def pcm_av_composition_av_AssemblyConnector121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_composition_av_AssemblyConnector__pcm_av_composition_av_AssemblyConnector121", None)
        self.__pcm_av_composition_av_AssemblyConnector121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationProvidedRole122"):
                opp_val = getattr(old_value, "OperationProvidedRole122", None)
                if opp_val == self:
                    setattr(old_value, "OperationProvidedRole122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationProvidedRole122"):
                opp_val = getattr(value, "OperationProvidedRole122", None)
                setattr(value, "OperationProvidedRole122", self)

    def AssemblyConnectorsReferencedInterfacesMustMatch(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AssemblyConnectorsReferencedInterfacesMustMatch method
        pass

    def AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch method
        pass

    def AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch method
        pass

class pcm_av_composition_av_EventChannelSourceConnector(Connector):

    pass
class pcm_av_composition_av_AssemblyEventConnector(Connector):

    pass
class pcm_av_composition_av_EventChannelSinkConnector(Connector):

    pass
class pcm_av_composition_av_AssemblyInfrastructureConnector(Connector):

    pass
class pcm_av_composition_av_DelegationConnector(Connector):

    pass
class entity_av_NamedElement:

    pass
class Identifier:

    pass
class pcm_av_resourceenvironment_av_ProcessingResourceSpecification(Identifier):

    def __init__(self, MTTR: float, MTTF: float, requiredByContainer: bool, numberOfReplicas: int, pcm_av_resourceenvironment_av_ProcessingResourceSpecification: "SchedulingPolicy" = None, pcm_av_resourceenvironment_av_ProcessingResourceSpecification654: "ProcessingResourceType" = None, PCMRandomVariable657: "PCMRandomVariable" = None, ResourceContainer660: "ResourceContainer" = None):
        self.MTTR = MTTR
        self.MTTF = MTTF
        self.requiredByContainer = requiredByContainer
        self.numberOfReplicas = numberOfReplicas
        self.pcm_av_resourceenvironment_av_ProcessingResourceSpecification = pcm_av_resourceenvironment_av_ProcessingResourceSpecification
        self.pcm_av_resourceenvironment_av_ProcessingResourceSpecification654 = pcm_av_resourceenvironment_av_ProcessingResourceSpecification654
        self.PCMRandomVariable657 = PCMRandomVariable657
        self.ResourceContainer660 = ResourceContainer660
        
    @property
    def MTTR(self) -> float:
        return self.__MTTR

    @MTTR.setter
    def MTTR(self, MTTR: float):
        self.__MTTR = MTTR

    @property
    def requiredByContainer(self) -> bool:
        return self.__requiredByContainer

    @requiredByContainer.setter
    def requiredByContainer(self, requiredByContainer: bool):
        self.__requiredByContainer = requiredByContainer

    @property
    def numberOfReplicas(self) -> int:
        return self.__numberOfReplicas

    @numberOfReplicas.setter
    def numberOfReplicas(self, numberOfReplicas: int):
        self.__numberOfReplicas = numberOfReplicas

    @property
    def MTTF(self) -> float:
        return self.__MTTF

    @MTTF.setter
    def MTTF(self, MTTF: float):
        self.__MTTF = MTTF

    @property
    def PCMRandomVariable657(self):
        return self.__PCMRandomVariable657

    @PCMRandomVariable657.setter
    def PCMRandomVariable657(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_resourceenvironment_av_ProcessingResourceSpecification__PCMRandomVariable657", None)
        self.__PCMRandomVariable657 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av658"):
                opp_val = getattr(old_value, "core_av658", None)
                if opp_val == self:
                    setattr(old_value, "core_av658", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av658"):
                opp_val = getattr(value, "core_av658", None)
                setattr(value, "core_av658", self)

    @property
    def pcm_av_resourceenvironment_av_ProcessingResourceSpecification(self):
        return self.__pcm_av_resourceenvironment_av_ProcessingResourceSpecification

    @pcm_av_resourceenvironment_av_ProcessingResourceSpecification.setter
    def pcm_av_resourceenvironment_av_ProcessingResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_resourceenvironment_av_ProcessingResourceSpecification__pcm_av_resourceenvironment_av_ProcessingResourceSpecification", None)
        self.__pcm_av_resourceenvironment_av_ProcessingResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SchedulingPolicy652"):
                opp_val = getattr(old_value, "SchedulingPolicy652", None)
                if opp_val == self:
                    setattr(old_value, "SchedulingPolicy652", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SchedulingPolicy652"):
                opp_val = getattr(value, "SchedulingPolicy652", None)
                setattr(value, "SchedulingPolicy652", self)

    @property
    def pcm_av_resourceenvironment_av_ProcessingResourceSpecification654(self):
        return self.__pcm_av_resourceenvironment_av_ProcessingResourceSpecification654

    @pcm_av_resourceenvironment_av_ProcessingResourceSpecification654.setter
    def pcm_av_resourceenvironment_av_ProcessingResourceSpecification654(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_resourceenvironment_av_ProcessingResourceSpecification__pcm_av_resourceenvironment_av_ProcessingResourceSpecification654", None)
        self.__pcm_av_resourceenvironment_av_ProcessingResourceSpecification654 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcessingResourceType655"):
                opp_val = getattr(old_value, "ProcessingResourceType655", None)
                if opp_val == self:
                    setattr(old_value, "ProcessingResourceType655", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessingResourceType655"):
                opp_val = getattr(value, "ProcessingResourceType655", None)
                setattr(value, "ProcessingResourceType655", self)

    @property
    def ResourceContainer660(self):
        return self.__ResourceContainer660

    @ResourceContainer660.setter
    def ResourceContainer660(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_resourceenvironment_av_ProcessingResourceSpecification__ResourceContainer660", None)
        self.__ResourceContainer660 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_av661"):
                opp_val = getattr(old_value, "resourceenvironment_av661", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_av661", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_av661"):
                opp_val = getattr(value, "resourceenvironment_av661", None)
                setattr(value, "resourceenvironment_av661", self)

class pcm_av_seff_av_ResourceDemandingBehaviour(Identifier):

    def __init__(self, AbstractLoopAction: "AbstractLoopAction" = None, AbstractBranchTransition: "AbstractBranchTransition" = None, AbstractAction480: set["AbstractAction"] = None):
        self.AbstractLoopAction = AbstractLoopAction
        self.AbstractBranchTransition = AbstractBranchTransition
        self.AbstractAction480 = AbstractAction480 if AbstractAction480 is not None else set()
        
    @property
    def AbstractAction480(self):
        return self.__AbstractAction480

    @AbstractAction480.setter
    def AbstractAction480(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_av_ResourceDemandingBehaviour__AbstractAction480", None)
        self.__AbstractAction480 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_av481"):
                    opp_val = getattr(item, "seff_av481", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_av481", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_av481"):
                    opp_val = getattr(item, "seff_av481", None)
                    
                    setattr(item, "seff_av481", self)
                    

    @property
    def AbstractLoopAction(self):
        return self.__AbstractLoopAction

    @AbstractLoopAction.setter
    def AbstractLoopAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_av_ResourceDemandingBehaviour__AbstractLoopAction", None)
        self.__AbstractLoopAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av476"):
                opp_val = getattr(old_value, "seff_av476", None)
                if opp_val == self:
                    setattr(old_value, "seff_av476", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av476"):
                opp_val = getattr(value, "seff_av476", None)
                setattr(value, "seff_av476", self)

    @property
    def AbstractBranchTransition(self):
        return self.__AbstractBranchTransition

    @AbstractBranchTransition.setter
    def AbstractBranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_av_ResourceDemandingBehaviour__AbstractBranchTransition", None)
        self.__AbstractBranchTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av478"):
                opp_val = getattr(old_value, "seff_av478", None)
                if opp_val == self:
                    setattr(old_value, "seff_av478", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av478"):
                opp_val = getattr(value, "seff_av478", None)
                setattr(value, "seff_av478", self)

    def ExactlyOneStopAction(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ExactlyOneStopAction method
        pass

    def EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor method
        pass

    def ExactlyOneStartAction(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ExactlyOneStartAction method
        pass

class pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification(Identifier):

    def __init__(self, failureProbability: float, LinkingResource663: "LinkingResource" = None, pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification: "CommunicationLinkResourceType" = None, PCMRandomVariable668: "PCMRandomVariable" = None, PCMRandomVariable671: "PCMRandomVariable" = None):
        self.failureProbability = failureProbability
        self.LinkingResource663 = LinkingResource663
        self.pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification = pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification
        self.PCMRandomVariable668 = PCMRandomVariable668
        self.PCMRandomVariable671 = PCMRandomVariable671
        
    @property
    def failureProbability(self) -> float:
        return self.__failureProbability

    @failureProbability.setter
    def failureProbability(self, failureProbability: float):
        self.__failureProbability = failureProbability

    @property
    def PCMRandomVariable668(self):
        return self.__PCMRandomVariable668

    @PCMRandomVariable668.setter
    def PCMRandomVariable668(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification__PCMRandomVariable668", None)
        self.__PCMRandomVariable668 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av669"):
                opp_val = getattr(old_value, "core_av669", None)
                if opp_val == self:
                    setattr(old_value, "core_av669", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av669"):
                opp_val = getattr(value, "core_av669", None)
                setattr(value, "core_av669", self)

    @property
    def LinkingResource663(self):
        return self.__LinkingResource663

    @LinkingResource663.setter
    def LinkingResource663(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification__LinkingResource663", None)
        self.__LinkingResource663 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_av664"):
                opp_val = getattr(old_value, "resourceenvironment_av664", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_av664", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_av664"):
                opp_val = getattr(value, "resourceenvironment_av664", None)
                setattr(value, "resourceenvironment_av664", self)

    @property
    def pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification(self):
        return self.__pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification

    @pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification.setter
    def pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification__pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification", None)
        self.__pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CommunicationLinkResourceType666"):
                opp_val = getattr(old_value, "CommunicationLinkResourceType666", None)
                if opp_val == self:
                    setattr(old_value, "CommunicationLinkResourceType666", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CommunicationLinkResourceType666"):
                opp_val = getattr(value, "CommunicationLinkResourceType666", None)
                setattr(value, "CommunicationLinkResourceType666", self)

    @property
    def PCMRandomVariable671(self):
        return self.__PCMRandomVariable671

    @PCMRandomVariable671.setter
    def PCMRandomVariable671(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification__PCMRandomVariable671", None)
        self.__PCMRandomVariable671 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av672"):
                opp_val = getattr(old_value, "core_av672", None)
                if opp_val == self:
                    setattr(old_value, "core_av672", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av672"):
                opp_val = getattr(value, "core_av672", None)
                setattr(value, "core_av672", self)

class pcm_av_seff_av_ResourceDemandingSEFF(seff_av_ServiceEffectSpecification, Identifier, seff_av_ResourceDemandingBehaviour):

    pass
class pcm_av_entity_av_Entity(Identifier, entity_av_NamedElement):

    pass
class pcm_av_entity_av_NamedElement:

    def __init__(self, entityName: str):
        self.entityName = entityName
        
    @property
    def entityName(self) -> str:
        return self.__entityName

    @entityName.setter
    def entityName(self, entityName: str):
        self.__entityName = entityName

class Loop:

    pass
class composition_av_AssemblyEventConnector:

    pass
class entity_av_ResourceRequiredRole:

    pass
class RequiredRole:

    pass
class pcm_av_repository_av_OperationRequiredRole(RequiredRole):

    pass
class pcm_av_repository_av_SourceRole(RequiredRole):

    pass
class pcm_av_repository_av_InfrastructureRequiredRole(RequiredRole):

    pass
class entity_av_ResourceInterfaceRequiringEntity:

    pass
class entity_av_Entity:

    pass
class pcm_av_system_av_System(entity_av_Entity, entity_av_ComposedProvidingRequiringEntity):

    def __init__(self, QoSAnnotations626: set["QoSAnnotations"] = None):
        self.QoSAnnotations626 = QoSAnnotations626 if QoSAnnotations626 is not None else set()
        
    @property
    def QoSAnnotations626(self):
        return self.__QoSAnnotations626

    @QoSAnnotations626.setter
    def QoSAnnotations626(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_system_av_System__QoSAnnotations626", None)
        self.__QoSAnnotations626 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qosannotations_av627"):
                    opp_val = getattr(item, "qosannotations_av627", None)
                    
                    if opp_val == self:
                        setattr(item, "qosannotations_av627", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qosannotations_av627"):
                    opp_val = getattr(item, "qosannotations_av627", None)
                    
                    setattr(item, "qosannotations_av627", self)
                    

    def SystemMustHaveAtLeastOneProvidedRole(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SystemMustHaveAtLeastOneProvidedRole method
        pass

class pcm_av_repository_av_CompositeDataType(entity_av_Entity, repository_av_DataType):

    pass
class pcm_av_repository_av_CollectionDataType(entity_av_Entity, repository_av_DataType):

    pass
class pcm_av_entity_av_InterfaceRequiringEntity(entity_av_Entity, entity_av_ResourceInterfaceRequiringEntity):

    pass
class ProvidedRole:

    pass
class pcm_av_repository_av_InfrastructureProvidedRole(ProvidedRole):

    pass
class pcm_av_repository_av_OperationProvidedRole(ProvidedRole):

    pass
class pcm_av_repository_av_SinkRole(ProvidedRole):

    pass
class Entity:

    pass
class pcm_av_resourcetype_av_ResourceInterface(Entity):

    pass
class pcm_av_repository_av_Interface(Entity):

    def __init__(self, pcm_av_repository_av_Interface: set["Interface"] = None, pcm_av_repository_av_Interface313: set["Protocol"] = None, RequiredCharacterisation: set["RequiredCharacterisation"] = None, Repository317: "Repository" = None):
        self.pcm_av_repository_av_Interface = pcm_av_repository_av_Interface if pcm_av_repository_av_Interface is not None else set()
        self.pcm_av_repository_av_Interface313 = pcm_av_repository_av_Interface313 if pcm_av_repository_av_Interface313 is not None else set()
        self.RequiredCharacterisation = RequiredCharacterisation if RequiredCharacterisation is not None else set()
        self.Repository317 = Repository317
        
    @property
    def pcm_av_repository_av_Interface(self):
        return self.__pcm_av_repository_av_Interface

    @pcm_av_repository_av_Interface.setter
    def pcm_av_repository_av_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_Interface__pcm_av_repository_av_Interface", None)
        self.__pcm_av_repository_av_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Interface311"):
                    opp_val = getattr(item, "Interface311", None)
                    
                    if opp_val == self:
                        setattr(item, "Interface311", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Interface311"):
                    opp_val = getattr(item, "Interface311", None)
                    
                    setattr(item, "Interface311", self)
                    

    @property
    def RequiredCharacterisation(self):
        return self.__RequiredCharacterisation

    @RequiredCharacterisation.setter
    def RequiredCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_Interface__RequiredCharacterisation", None)
        self.__RequiredCharacterisation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_av315"):
                    opp_val = getattr(item, "repository_av315", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_av315", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_av315"):
                    opp_val = getattr(item, "repository_av315", None)
                    
                    setattr(item, "repository_av315", self)
                    

    @property
    def pcm_av_repository_av_Interface313(self):
        return self.__pcm_av_repository_av_Interface313

    @pcm_av_repository_av_Interface313.setter
    def pcm_av_repository_av_Interface313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_Interface__pcm_av_repository_av_Interface313", None)
        self.__pcm_av_repository_av_Interface313 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Protocol"):
                    opp_val = getattr(item, "Protocol", None)
                    
                    if opp_val == self:
                        setattr(item, "Protocol", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Protocol"):
                    opp_val = getattr(item, "Protocol", None)
                    
                    setattr(item, "Protocol", self)
                    

    @property
    def Repository317(self):
        return self.__Repository317

    @Repository317.setter
    def Repository317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_Interface__Repository317", None)
        self.__Repository317 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av318"):
                opp_val = getattr(old_value, "repository_av318", None)
                if opp_val == self:
                    setattr(old_value, "repository_av318", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av318"):
                opp_val = getattr(value, "repository_av318", None)
                setattr(value, "repository_av318", self)

    def NoProtocolTypeIDUsedTwice(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NoProtocolTypeIDUsedTwice method
        pass

class pcm_av_usagemodel_av_AbstractUserAction(Entity):

    pass
class pcm_av_resourcetype_av_ResourceSignature(Entity):

    def __init__(self, resourceServiceId: int, Parameter381: "Parameter" = None, ResourceInterface384: "ResourceInterface" = None):
        self.resourceServiceId = resourceServiceId
        self.Parameter381 = Parameter381
        self.ResourceInterface384 = ResourceInterface384
        
    @property
    def resourceServiceId(self) -> int:
        return self.__resourceServiceId

    @resourceServiceId.setter
    def resourceServiceId(self, resourceServiceId: int):
        self.__resourceServiceId = resourceServiceId

    @property
    def ResourceInterface384(self):
        return self.__ResourceInterface384

    @ResourceInterface384.setter
    def ResourceInterface384(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_resourcetype_av_ResourceSignature__ResourceInterface384", None)
        self.__ResourceInterface384 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcetype_av385"):
                opp_val = getattr(old_value, "resourcetype_av385", None)
                if opp_val == self:
                    setattr(old_value, "resourcetype_av385", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcetype_av385"):
                opp_val = getattr(value, "resourcetype_av385", None)
                setattr(value, "resourcetype_av385", self)

    @property
    def Parameter381(self):
        return self.__Parameter381

    @Parameter381.setter
    def Parameter381(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_resourcetype_av_ResourceSignature__Parameter381", None)
        self.__Parameter381 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av382"):
                opp_val = getattr(old_value, "repository_av382", None)
                if opp_val == self:
                    setattr(old_value, "repository_av382", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av382"):
                opp_val = getattr(value, "repository_av382", None)
                setattr(value, "repository_av382", self)

class pcm_av_resourceenvironment_av_ResourceContainer(Entity):

    pass
class pcm_av_seff_av_AbstractBranchTransition(Entity):

    pass
class pcm_av_repository_av_PassiveResource(Entity):

    pass
class pcm_av_resourcetype_av_SchedulingPolicy(Entity):

    pass
class pcm_av_repository_av_Signature(Entity):

    pass
class pcm_av_entity_av_ResourceInterfaceProvidingEntity(Entity):

    pass
class pcm_av_seff_av_AbstractAction(Entity):

    pass
class pcm_av_resourceenvironment_av_LinkingResource(Entity):

    pass
class pcm_av_repository_av_Role(Entity):

    pass
class pcm_av_composition_av_EventChannel(Entity):

    pass
class pcm_av_seff_reliability_av_FailureHandlingEntity(Entity):

    pass
class pcm_av_usagemodel_av_UsageScenario(Entity):

    pass
class pcm_av_repository_av_Repository(Entity):

    def __init__(self, repositoryDescription: str, RepositoryComponent301: set["RepositoryComponent"] = None, Interface: set["Interface"] = None, FailureType: set["FailureType"] = None, DataType308: set["DataType"] = None):
        self.repositoryDescription = repositoryDescription
        self.RepositoryComponent301 = RepositoryComponent301 if RepositoryComponent301 is not None else set()
        self.Interface = Interface if Interface is not None else set()
        self.FailureType = FailureType if FailureType is not None else set()
        self.DataType308 = DataType308 if DataType308 is not None else set()
        
    @property
    def repositoryDescription(self) -> str:
        return self.__repositoryDescription

    @repositoryDescription.setter
    def repositoryDescription(self, repositoryDescription: str):
        self.__repositoryDescription = repositoryDescription

    @property
    def Interface(self):
        return self.__Interface

    @Interface.setter
    def Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_Repository__Interface", None)
        self.__Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_av304"):
                    opp_val = getattr(item, "repository_av304", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_av304", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_av304"):
                    opp_val = getattr(item, "repository_av304", None)
                    
                    setattr(item, "repository_av304", self)
                    

    @property
    def RepositoryComponent301(self):
        return self.__RepositoryComponent301

    @RepositoryComponent301.setter
    def RepositoryComponent301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_Repository__RepositoryComponent301", None)
        self.__RepositoryComponent301 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_av302"):
                    opp_val = getattr(item, "repository_av302", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_av302", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_av302"):
                    opp_val = getattr(item, "repository_av302", None)
                    
                    setattr(item, "repository_av302", self)
                    

    @property
    def DataType308(self):
        return self.__DataType308

    @DataType308.setter
    def DataType308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_Repository__DataType308", None)
        self.__DataType308 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_av309"):
                    opp_val = getattr(item, "repository_av309", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_av309", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_av309"):
                    opp_val = getattr(item, "repository_av309", None)
                    
                    setattr(item, "repository_av309", self)
                    

    @property
    def FailureType(self):
        return self.__FailureType

    @FailureType.setter
    def FailureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_Repository__FailureType", None)
        self.__FailureType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reliability_av306"):
                    opp_val = getattr(item, "reliability_av306", None)
                    
                    if opp_val == self:
                        setattr(item, "reliability_av306", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reliability_av306"):
                    opp_val = getattr(item, "reliability_av306", None)
                    
                    setattr(item, "reliability_av306", self)
                    

class pcm_av_allocation_av_AllocationContext(Entity):

    def __init__(self, pcm_av_allocation_av_AllocationContext: "ResourceContainer" = None, pcm_av_allocation_av_AllocationContext676: "composition_av_AssemblyContext" = None, pcm_av_allocation_av_AllocationContext680: "composition_av_EventChannel" = None, Allocation: "Allocation" = None):
        self.pcm_av_allocation_av_AllocationContext = pcm_av_allocation_av_AllocationContext
        self.pcm_av_allocation_av_AllocationContext676 = pcm_av_allocation_av_AllocationContext676
        self.pcm_av_allocation_av_AllocationContext680 = pcm_av_allocation_av_AllocationContext680
        self.Allocation = Allocation
        
    @property
    def pcm_av_allocation_av_AllocationContext680(self):
        return self.__pcm_av_allocation_av_AllocationContext680

    @pcm_av_allocation_av_AllocationContext680.setter
    def pcm_av_allocation_av_AllocationContext680(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_allocation_av_AllocationContext__pcm_av_allocation_av_AllocationContext680", None)
        self.__pcm_av_allocation_av_AllocationContext680 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_EventChannel"):
                opp_val = getattr(old_value, "composition_av_EventChannel", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_EventChannel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_EventChannel"):
                opp_val = getattr(value, "composition_av_EventChannel", None)
                setattr(value, "composition_av_EventChannel", self)

    @property
    def Allocation(self):
        return self.__Allocation

    @Allocation.setter
    def Allocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_allocation_av_AllocationContext__Allocation", None)
        self.__Allocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "allocation_av"):
                opp_val = getattr(old_value, "allocation_av", None)
                if opp_val == self:
                    setattr(old_value, "allocation_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "allocation_av"):
                opp_val = getattr(value, "allocation_av", None)
                setattr(value, "allocation_av", self)

    @property
    def pcm_av_allocation_av_AllocationContext(self):
        return self.__pcm_av_allocation_av_AllocationContext

    @pcm_av_allocation_av_AllocationContext.setter
    def pcm_av_allocation_av_AllocationContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_allocation_av_AllocationContext__pcm_av_allocation_av_AllocationContext", None)
        self.__pcm_av_allocation_av_AllocationContext = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceContainer674"):
                opp_val = getattr(old_value, "ResourceContainer674", None)
                if opp_val == self:
                    setattr(old_value, "ResourceContainer674", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceContainer674"):
                opp_val = getattr(value, "ResourceContainer674", None)
                setattr(value, "ResourceContainer674", self)

    @property
    def pcm_av_allocation_av_AllocationContext676(self):
        return self.__pcm_av_allocation_av_AllocationContext676

    @pcm_av_allocation_av_AllocationContext676.setter
    def pcm_av_allocation_av_AllocationContext676(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_allocation_av_AllocationContext__pcm_av_allocation_av_AllocationContext676", None)
        self.__pcm_av_allocation_av_AllocationContext676 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_AssemblyContext677"):
                opp_val = getattr(old_value, "composition_av_AssemblyContext677", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_AssemblyContext677", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_AssemblyContext677"):
                opp_val = getattr(value, "composition_av_AssemblyContext677", None)
                setattr(value, "composition_av_AssemblyContext677", self)

    def OneAssemblyContextOrOneEventChannelShouldBeReferred(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement OneAssemblyContextOrOneEventChannelShouldBeReferred method
        pass

class pcm_av_allocation_av_Allocation(Entity):

    def __init__(self, pcm_av_allocation_av_Allocation: "ResourceEnvironment" = None, pcm_av_allocation_av_Allocation684: "System" = None, AllocationContext: set["AllocationContext"] = None):
        self.pcm_av_allocation_av_Allocation = pcm_av_allocation_av_Allocation
        self.pcm_av_allocation_av_Allocation684 = pcm_av_allocation_av_Allocation684
        self.AllocationContext = AllocationContext if AllocationContext is not None else set()
        
    @property
    def pcm_av_allocation_av_Allocation684(self):
        return self.__pcm_av_allocation_av_Allocation684

    @pcm_av_allocation_av_Allocation684.setter
    def pcm_av_allocation_av_Allocation684(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_allocation_av_Allocation__pcm_av_allocation_av_Allocation684", None)
        self.__pcm_av_allocation_av_Allocation684 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "System685"):
                opp_val = getattr(old_value, "System685", None)
                if opp_val == self:
                    setattr(old_value, "System685", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "System685"):
                opp_val = getattr(value, "System685", None)
                setattr(value, "System685", self)

    @property
    def pcm_av_allocation_av_Allocation(self):
        return self.__pcm_av_allocation_av_Allocation

    @pcm_av_allocation_av_Allocation.setter
    def pcm_av_allocation_av_Allocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_allocation_av_Allocation__pcm_av_allocation_av_Allocation", None)
        self.__pcm_av_allocation_av_Allocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceEnvironment682"):
                opp_val = getattr(old_value, "ResourceEnvironment682", None)
                if opp_val == self:
                    setattr(old_value, "ResourceEnvironment682", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceEnvironment682"):
                opp_val = getattr(value, "ResourceEnvironment682", None)
                setattr(value, "ResourceEnvironment682", self)

    @property
    def AllocationContext(self):
        return self.__AllocationContext

    @AllocationContext.setter
    def AllocationContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_allocation_av_Allocation__AllocationContext", None)
        self.__AllocationContext = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "allocation_av687"):
                    opp_val = getattr(item, "allocation_av687", None)
                    
                    if opp_val == self:
                        setattr(item, "allocation_av687", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "allocation_av687"):
                    opp_val = getattr(item, "allocation_av687", None)
                    
                    setattr(item, "allocation_av687", self)
                    

    def EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce method
        pass

    def CommunicatingServersHaveToBeConnectedByLinkingResource(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement CommunicatingServersHaveToBeConnectedByLinkingResource method
        pass

class pcm_av_composition_av_ComposedStructure(Entity):

    def __init__(self, composition_av58: set["composition_av_AssemblyContext"] = None, composition_av61: set["composition_av_ResourceRequiredDelegationConnector"] = None, composition_av67: set["composition_av_Connector"] = None, composition_av64: set["composition_av_EventChannel"] = None):
        self.composition_av58 = composition_av58 if composition_av58 is not None else set()
        self.composition_av61 = composition_av61 if composition_av61 is not None else set()
        self.composition_av67 = composition_av67 if composition_av67 is not None else set()
        self.composition_av64 = composition_av64 if composition_av64 is not None else set()
        
    @property
    def composition_av64(self):
        return self.__composition_av64

    @composition_av64.setter
    def composition_av64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_composition_av_ComposedStructure__composition_av64", None)
        self.__composition_av64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_av65"):
                    opp_val = getattr(item, "core_av65", None)
                    
                    if opp_val == self:
                        setattr(item, "core_av65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_av65"):
                    opp_val = getattr(item, "core_av65", None)
                    
                    setattr(item, "core_av65", self)
                    

    @property
    def composition_av67(self):
        return self.__composition_av67

    @composition_av67.setter
    def composition_av67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_composition_av_ComposedStructure__composition_av67", None)
        self.__composition_av67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_av68"):
                    opp_val = getattr(item, "core_av68", None)
                    
                    if opp_val == self:
                        setattr(item, "core_av68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_av68"):
                    opp_val = getattr(item, "core_av68", None)
                    
                    setattr(item, "core_av68", self)
                    

    @property
    def composition_av58(self):
        return self.__composition_av58

    @composition_av58.setter
    def composition_av58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_composition_av_ComposedStructure__composition_av58", None)
        self.__composition_av58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_av59"):
                    opp_val = getattr(item, "core_av59", None)
                    
                    if opp_val == self:
                        setattr(item, "core_av59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_av59"):
                    opp_val = getattr(item, "core_av59", None)
                    
                    setattr(item, "core_av59", self)
                    

    @property
    def composition_av61(self):
        return self.__composition_av61

    @composition_av61.setter
    def composition_av61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_composition_av_ComposedStructure__composition_av61", None)
        self.__composition_av61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_av62"):
                    opp_val = getattr(item, "core_av62", None)
                    
                    if opp_val == self:
                        setattr(item, "core_av62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_av62"):
                    opp_val = getattr(item, "core_av62", None)
                    
                    setattr(item, "core_av62", self)
                    

    def MultipleConnectorsConstraintForAssemblyConnectors(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MultipleConnectorsConstraintForAssemblyConnectors method
        pass

    def MultipleConnectorsConstraint(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MultipleConnectorsConstraint method
        pass

class pcm_av_qosannotations_av_QoSAnnotations(Entity):

    def __init__(self, System: "System" = None, SpecifiedQoSAnnotation: set["SpecifiedQoSAnnotation"] = None, SpecifiedOutputParameterAbstraction602: set["SpecifiedOutputParameterAbstraction"] = None):
        self.System = System
        self.SpecifiedQoSAnnotation = SpecifiedQoSAnnotation if SpecifiedQoSAnnotation is not None else set()
        self.SpecifiedOutputParameterAbstraction602 = SpecifiedOutputParameterAbstraction602 if SpecifiedOutputParameterAbstraction602 is not None else set()
        
    @property
    def System(self):
        return self.__System

    @System.setter
    def System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_qosannotations_av_QoSAnnotations__System", None)
        self.__System = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system_av"):
                opp_val = getattr(old_value, "system_av", None)
                if opp_val == self:
                    setattr(old_value, "system_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system_av"):
                opp_val = getattr(value, "system_av", None)
                setattr(value, "system_av", self)

    @property
    def SpecifiedOutputParameterAbstraction602(self):
        return self.__SpecifiedOutputParameterAbstraction602

    @SpecifiedOutputParameterAbstraction602.setter
    def SpecifiedOutputParameterAbstraction602(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_qosannotations_av_QoSAnnotations__SpecifiedOutputParameterAbstraction602", None)
        self.__SpecifiedOutputParameterAbstraction602 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qosannotations_av603"):
                    opp_val = getattr(item, "qosannotations_av603", None)
                    
                    if opp_val == self:
                        setattr(item, "qosannotations_av603", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qosannotations_av603"):
                    opp_val = getattr(item, "qosannotations_av603", None)
                    
                    setattr(item, "qosannotations_av603", self)
                    

    @property
    def SpecifiedQoSAnnotation(self):
        return self.__SpecifiedQoSAnnotation

    @SpecifiedQoSAnnotation.setter
    def SpecifiedQoSAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_qosannotations_av_QoSAnnotations__SpecifiedQoSAnnotation", None)
        self.__SpecifiedQoSAnnotation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qosannotations_av606"):
                    opp_val = getattr(item, "qosannotations_av606", None)
                    
                    if opp_val == self:
                        setattr(item, "qosannotations_av606", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qosannotations_av606"):
                    opp_val = getattr(item, "qosannotations_av606", None)
                    
                    setattr(item, "qosannotations_av606", self)
                    

    def MultipleReliabilityAnnotationsPerExternalCallNotAllowed(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MultipleReliabilityAnnotationsPerExternalCallNotAllowed method
        pass

class pcm_av_composition_av_Connector(Entity):

    pass
class pcm_av_reliability_av_FailureType(Entity):

    pass
class pcm_av_usagemodel_av_ScenarioBehaviour(Entity):

    def __init__(self, UsageScenario235: "UsageScenario" = None, BranchTransition: "BranchTransition" = None, Loop240: "Loop" = None, AbstractUserAction243: set["AbstractUserAction"] = None):
        self.UsageScenario235 = UsageScenario235
        self.BranchTransition = BranchTransition
        self.Loop240 = Loop240
        self.AbstractUserAction243 = AbstractUserAction243 if AbstractUserAction243 is not None else set()
        
    @property
    def BranchTransition(self):
        return self.__BranchTransition

    @BranchTransition.setter
    def BranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_usagemodel_av_ScenarioBehaviour__BranchTransition", None)
        self.__BranchTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av238"):
                opp_val = getattr(old_value, "usagemodel_av238", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av238", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av238"):
                opp_val = getattr(value, "usagemodel_av238", None)
                setattr(value, "usagemodel_av238", self)

    @property
    def Loop240(self):
        return self.__Loop240

    @Loop240.setter
    def Loop240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_usagemodel_av_ScenarioBehaviour__Loop240", None)
        self.__Loop240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av241"):
                opp_val = getattr(old_value, "usagemodel_av241", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av241", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av241"):
                opp_val = getattr(value, "usagemodel_av241", None)
                setattr(value, "usagemodel_av241", self)

    @property
    def AbstractUserAction243(self):
        return self.__AbstractUserAction243

    @AbstractUserAction243.setter
    def AbstractUserAction243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_usagemodel_av_ScenarioBehaviour__AbstractUserAction243", None)
        self.__AbstractUserAction243 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "usagemodel_av244"):
                    opp_val = getattr(item, "usagemodel_av244", None)
                    
                    if opp_val == self:
                        setattr(item, "usagemodel_av244", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "usagemodel_av244"):
                    opp_val = getattr(item, "usagemodel_av244", None)
                    
                    setattr(item, "usagemodel_av244", self)
                    

    @property
    def UsageScenario235(self):
        return self.__UsageScenario235

    @UsageScenario235.setter
    def UsageScenario235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_usagemodel_av_ScenarioBehaviour__UsageScenario235", None)
        self.__UsageScenario235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av236"):
                opp_val = getattr(old_value, "usagemodel_av236", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av236", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av236"):
                opp_val = getattr(value, "usagemodel_av236", None)
                setattr(value, "usagemodel_av236", self)

    def Exactlyonestart(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement Exactlyonestart method
        pass

    def EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor method
        pass

    def Exactlyonestop(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement Exactlyonestop method
        pass

class pcm_av_entity_av_ResourceInterfaceRequiringEntity(Entity):

    pass
class pcm_av_composition_av_AssemblyContext(Entity):

    pass
class pcm_av_entity_av_InterfaceProvidingEntity(Entity):

    pass
class entity_av_InterfaceRequiringEntity:

    pass
class entity_av_InterfaceProvidingEntity:

    pass
class pcm_av_entity_av_InterfaceProvidingRequiringEntity(entity_av_InterfaceRequiringEntity, entity_av_InterfaceProvidingEntity):

    pass
class ResourceInterface:

    pass
class entity_av_ResourceInterfaceProvidingEntity:

    pass
class pcm_av_entity_av_ResourceInterfaceProvidingRequiringEntity(entity_av_ResourceInterfaceRequiringEntity, entity_av_ResourceInterfaceProvidingEntity):

    pass
class pcm_av_resourcetype_av_ResourceType(entity_av_Entity, entity_av_ResourceInterfaceProvidingEntity, UnitCarryingElement):

    pass
class Role:

    pass
class pcm_av_repository_av_ProvidedRole(Role):

    pass
class pcm_av_repository_av_RequiredRole(Role):

    pass
class pcm_av_entity_av_ResourceRequiredRole(Role):

    pass
class pcm_av_entity_av_ResourceProvidedRole(Role):

    pass
class ProcessingResourceSpecification:

    pass
class CommunicationLinkResourceSpecification:

    pass
class Delay:

    pass
class OpenWorkload:

    pass
class composition_av_EventChannelSinkConnector:

    pass
class qos_performance_av_SpecifiedExecutionTime:

    pass
class GuardedBranchTransition:

    pass
class LoopAction:

    pass
class seff_performance_av_ParametricResourceDemand:

    pass
class seff_performance_av_ResourceCall:

    pass
class seff_performance_av_InfrastructureCall:

    pass
class VariableCharacterisation:

    pass
class PassiveResource:

    pass
class ClosedWorkload:

    pass
class RandomVariable:

    pass
class pcm_av_core_av_PCMRandomVariable(RandomVariable):

    def __init__(self, ClosedWorkload: "ClosedWorkload" = None, PassiveResource: "PassiveResource" = None, VariableCharacterisation: "VariableCharacterisation" = None, seff_performance_av: "seff_performance_av_InfrastructureCall" = None, seff_performance_av10: "seff_performance_av_ResourceCall" = None, seff_performance_av13: "seff_performance_av_ParametricResourceDemand" = None, LoopAction: "LoopAction" = None, GuardedBranchTransition: "GuardedBranchTransition" = None, qos_performance_av: "qos_performance_av_SpecifiedExecutionTime" = None, composition_av: "composition_av_EventChannelSinkConnector" = None, OpenWorkload: "OpenWorkload" = None, Delay: "Delay" = None, CommunicationLinkResourceSpecification: "CommunicationLinkResourceSpecification" = None, ProcessingResourceSpecification: "ProcessingResourceSpecification" = None, CommunicationLinkResourceSpecification34: "CommunicationLinkResourceSpecification" = None, composition_av22: "composition_av_AssemblyEventConnector" = None, Loop: "Loop" = None):
        self.ClosedWorkload = ClosedWorkload
        self.PassiveResource = PassiveResource
        self.VariableCharacterisation = VariableCharacterisation
        self.seff_performance_av = seff_performance_av
        self.seff_performance_av10 = seff_performance_av10
        self.seff_performance_av13 = seff_performance_av13
        self.LoopAction = LoopAction
        self.GuardedBranchTransition = GuardedBranchTransition
        self.qos_performance_av = qos_performance_av
        self.composition_av = composition_av
        self.OpenWorkload = OpenWorkload
        self.Delay = Delay
        self.CommunicationLinkResourceSpecification = CommunicationLinkResourceSpecification
        self.ProcessingResourceSpecification = ProcessingResourceSpecification
        self.CommunicationLinkResourceSpecification34 = CommunicationLinkResourceSpecification34
        self.composition_av22 = composition_av22
        self.Loop = Loop
        
    @property
    def Loop(self):
        return self.__Loop

    @Loop.setter
    def Loop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__Loop", None)
        self.__Loop = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av25"):
                opp_val = getattr(old_value, "usagemodel_av25", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av25"):
                opp_val = getattr(value, "usagemodel_av25", None)
                setattr(value, "usagemodel_av25", self)

    @property
    def qos_performance_av(self):
        return self.__qos_performance_av

    @qos_performance_av.setter
    def qos_performance_av(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__qos_performance_av", None)
        self.__qos_performance_av = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qosannotations_av"):
                opp_val = getattr(old_value, "qosannotations_av", None)
                if opp_val == self:
                    setattr(old_value, "qosannotations_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qosannotations_av"):
                opp_val = getattr(value, "qosannotations_av", None)
                setattr(value, "qosannotations_av", self)

    @property
    def composition_av22(self):
        return self.__composition_av22

    @composition_av22.setter
    def composition_av22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__composition_av22", None)
        self.__composition_av22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av23"):
                opp_val = getattr(old_value, "core_av23", None)
                if opp_val == self:
                    setattr(old_value, "core_av23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av23"):
                opp_val = getattr(value, "core_av23", None)
                setattr(value, "core_av23", self)

    @property
    def CommunicationLinkResourceSpecification(self):
        return self.__CommunicationLinkResourceSpecification

    @CommunicationLinkResourceSpecification.setter
    def CommunicationLinkResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__CommunicationLinkResourceSpecification", None)
        self.__CommunicationLinkResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_av"):
                opp_val = getattr(old_value, "resourceenvironment_av", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_av"):
                opp_val = getattr(value, "resourceenvironment_av", None)
                setattr(value, "resourceenvironment_av", self)

    @property
    def composition_av(self):
        return self.__composition_av

    @composition_av.setter
    def composition_av(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__composition_av", None)
        self.__composition_av = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av"):
                opp_val = getattr(old_value, "core_av", None)
                if opp_val == self:
                    setattr(old_value, "core_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av"):
                opp_val = getattr(value, "core_av", None)
                setattr(value, "core_av", self)

    @property
    def seff_performance_av(self):
        return self.__seff_performance_av

    @seff_performance_av.setter
    def seff_performance_av(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__seff_performance_av", None)
        self.__seff_performance_av = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av"):
                opp_val = getattr(old_value, "seff_av", None)
                if opp_val == self:
                    setattr(old_value, "seff_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av"):
                opp_val = getattr(value, "seff_av", None)
                setattr(value, "seff_av", self)

    @property
    def GuardedBranchTransition(self):
        return self.__GuardedBranchTransition

    @GuardedBranchTransition.setter
    def GuardedBranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__GuardedBranchTransition", None)
        self.__GuardedBranchTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av18"):
                opp_val = getattr(old_value, "seff_av18", None)
                if opp_val == self:
                    setattr(old_value, "seff_av18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av18"):
                opp_val = getattr(value, "seff_av18", None)
                setattr(value, "seff_av18", self)

    @property
    def seff_performance_av13(self):
        return self.__seff_performance_av13

    @seff_performance_av13.setter
    def seff_performance_av13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__seff_performance_av13", None)
        self.__seff_performance_av13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av14"):
                opp_val = getattr(old_value, "seff_av14", None)
                if opp_val == self:
                    setattr(old_value, "seff_av14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av14"):
                opp_val = getattr(value, "seff_av14", None)
                setattr(value, "seff_av14", self)

    @property
    def PassiveResource(self):
        return self.__PassiveResource

    @PassiveResource.setter
    def PassiveResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__PassiveResource", None)
        self.__PassiveResource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av"):
                opp_val = getattr(old_value, "repository_av", None)
                if opp_val == self:
                    setattr(old_value, "repository_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av"):
                opp_val = getattr(value, "repository_av", None)
                setattr(value, "repository_av", self)

    @property
    def VariableCharacterisation(self):
        return self.__VariableCharacterisation

    @VariableCharacterisation.setter
    def VariableCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__VariableCharacterisation", None)
        self.__VariableCharacterisation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameter_av"):
                opp_val = getattr(old_value, "parameter_av", None)
                if opp_val == self:
                    setattr(old_value, "parameter_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameter_av"):
                opp_val = getattr(value, "parameter_av", None)
                setattr(value, "parameter_av", self)

    @property
    def LoopAction(self):
        return self.__LoopAction

    @LoopAction.setter
    def LoopAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__LoopAction", None)
        self.__LoopAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av16"):
                opp_val = getattr(old_value, "seff_av16", None)
                if opp_val == self:
                    setattr(old_value, "seff_av16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av16"):
                opp_val = getattr(value, "seff_av16", None)
                setattr(value, "seff_av16", self)

    @property
    def ProcessingResourceSpecification(self):
        return self.__ProcessingResourceSpecification

    @ProcessingResourceSpecification.setter
    def ProcessingResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__ProcessingResourceSpecification", None)
        self.__ProcessingResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_av32"):
                opp_val = getattr(old_value, "resourceenvironment_av32", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_av32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_av32"):
                opp_val = getattr(value, "resourceenvironment_av32", None)
                setattr(value, "resourceenvironment_av32", self)

    @property
    def seff_performance_av10(self):
        return self.__seff_performance_av10

    @seff_performance_av10.setter
    def seff_performance_av10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__seff_performance_av10", None)
        self.__seff_performance_av10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av11"):
                opp_val = getattr(old_value, "seff_av11", None)
                if opp_val == self:
                    setattr(old_value, "seff_av11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av11"):
                opp_val = getattr(value, "seff_av11", None)
                setattr(value, "seff_av11", self)

    @property
    def Delay(self):
        return self.__Delay

    @Delay.setter
    def Delay(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__Delay", None)
        self.__Delay = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av29"):
                opp_val = getattr(old_value, "usagemodel_av29", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av29"):
                opp_val = getattr(value, "usagemodel_av29", None)
                setattr(value, "usagemodel_av29", self)

    @property
    def ClosedWorkload(self):
        return self.__ClosedWorkload

    @ClosedWorkload.setter
    def ClosedWorkload(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__ClosedWorkload", None)
        self.__ClosedWorkload = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av"):
                opp_val = getattr(old_value, "usagemodel_av", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av"):
                opp_val = getattr(value, "usagemodel_av", None)
                setattr(value, "usagemodel_av", self)

    @property
    def CommunicationLinkResourceSpecification34(self):
        return self.__CommunicationLinkResourceSpecification34

    @CommunicationLinkResourceSpecification34.setter
    def CommunicationLinkResourceSpecification34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__CommunicationLinkResourceSpecification34", None)
        self.__CommunicationLinkResourceSpecification34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_av35"):
                opp_val = getattr(old_value, "resourceenvironment_av35", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_av35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_av35"):
                opp_val = getattr(value, "resourceenvironment_av35", None)
                setattr(value, "resourceenvironment_av35", self)

    @property
    def OpenWorkload(self):
        return self.__OpenWorkload

    @OpenWorkload.setter
    def OpenWorkload(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__OpenWorkload", None)
        self.__OpenWorkload = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av27"):
                opp_val = getattr(old_value, "usagemodel_av27", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av27"):
                opp_val = getattr(value, "usagemodel_av27", None)
                setattr(value, "usagemodel_av27", self)

    def SpecificationMustNotBeNULL(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SpecificationMustNotBeNULL method
        pass

class pcm_av_PerJoinPointScope:

    pass
class pcm_av_GlobalScope:

    pass
class pcm_av_EObject:

    pass
class pcm_av_Advice:

    pass
class pcm_av_DummyClass:

    pass