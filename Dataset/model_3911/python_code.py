from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class PrimitiveTypeEnum(Enum):
    INT = "INT"
    STRING = "STRING"
    BOOL = "BOOL"
    DOUBLE = "DOUBLE"
    CHAR = "CHAR"
    BYTE = "BYTE"
    LONG = "LONG"
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
class pcm_av_av_completions_av_av_NetworkDemandParametricResourceDemand(ParametricResourceDemand):

    pass
class ExternalCallAction:

    pass
class pcm_av_av_completions_av_av_DelegatingExternalCallAction(ExternalCallAction):

    pass
class Completion:

    pass
class Allocation:

    pass
class pcm_av_av_completions_av_av_CompletionRepository:

    pass
class repository_av_av_RepositoryComponent:

    pass
class AllocationContext:

    pass
class ResourceEnvironment:

    pass
class ResourceContainer:

    pass
class LinkingResource:

    pass
class ExternalFailureOccurrenceDescription:

    pass
class QoSAnnotations:

    pass
class SpecifiedExecutionTime:

    pass
class pcm_av_av_qos_performance_av_av_ComponentSpecifiedExecutionTime(SpecifiedExecutionTime):

    pass
class pcm_av_av_qos_performance_av_av_SystemSpecifiedExecutionTime(SpecifiedExecutionTime):

    def __init__(self):
        
    def SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem method
        pass

class pcm_av_av_qosannotations_av_av_SpecifiedOutputParameterAbstraction:

    pass
class SpecifiedQoSAnnotation:

    pass
class pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation(SpecifiedQoSAnnotation):

    def __init__(self, ExternalFailureOccurrenceDescription: set["ExternalFailureOccurrenceDescription"] = None, qosannotations_av_av612: "pcm_av_av_qosannotations_av_av_QoSAnnotations"):
        self.ExternalFailureOccurrenceDescription = ExternalFailureOccurrenceDescription if ExternalFailureOccurrenceDescription is not None else set()
        
    @property
    def ExternalFailureOccurrenceDescription(self):
        return self.__ExternalFailureOccurrenceDescription

    @ExternalFailureOccurrenceDescription.setter
    def ExternalFailureOccurrenceDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription", None)
        self.__ExternalFailureOccurrenceDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reliability_av_av630"):
                    opp_val = getattr(item, "reliability_av_av630", None)
                    
                    if opp_val == self:
                        setattr(item, "reliability_av_av630", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reliability_av_av630"):
                    opp_val = getattr(item, "reliability_av_av630", None)
                    
                    setattr(item, "reliability_av_av630", self)
                    

    def SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1 method
        pass

    def MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed method
        pass

    def SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem method
        pass

class pcm_av_av_qos_performance_av_av_SpecifiedExecutionTime(SpecifiedQoSAnnotation):

    pass
class System:

    pass
class pcm_av_av_qosannotations_av_av_SpecifiedQoSAnnotation:

    pass
class seff_reliability_av_av_RecoveryAction:

    pass
class seff_reliability_av_av_RecoveryActionBehaviour:

    pass
class pcm_av_av_seff_performance_av_av_ParametricResourceDemand:

    def __init__(self, PCMRandomVariable584: "PCMRandomVariable" = None, pcm_av_av_seff_performance_av_av_ParametricResourceDemand: "ProcessingResourceType" = None, AbstractInternalControlFlowAction589: "AbstractInternalControlFlowAction" = None):
        self.PCMRandomVariable584 = PCMRandomVariable584
        self.pcm_av_av_seff_performance_av_av_ParametricResourceDemand = pcm_av_av_seff_performance_av_av_ParametricResourceDemand
        self.AbstractInternalControlFlowAction589 = AbstractInternalControlFlowAction589
        
    @property
    def AbstractInternalControlFlowAction589(self):
        return self.__AbstractInternalControlFlowAction589

    @AbstractInternalControlFlowAction589.setter
    def AbstractInternalControlFlowAction589(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_seff_performance_av_av_ParametricResourceDemand__AbstractInternalControlFlowAction589", None)
        self.__AbstractInternalControlFlowAction589 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av_av590"):
                opp_val = getattr(old_value, "seff_av_av590", None)
                if opp_val == self:
                    setattr(old_value, "seff_av_av590", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av_av590"):
                opp_val = getattr(value, "seff_av_av590", None)
                setattr(value, "seff_av_av590", self)

    @property
    def PCMRandomVariable584(self):
        return self.__PCMRandomVariable584

    @PCMRandomVariable584.setter
    def PCMRandomVariable584(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_seff_performance_av_av_ParametricResourceDemand__PCMRandomVariable584", None)
        self.__PCMRandomVariable584 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av_av585"):
                opp_val = getattr(old_value, "core_av_av585", None)
                if opp_val == self:
                    setattr(old_value, "core_av_av585", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av_av585"):
                opp_val = getattr(value, "core_av_av585", None)
                setattr(value, "core_av_av585", self)

    @property
    def pcm_av_av_seff_performance_av_av_ParametricResourceDemand(self):
        return self.__pcm_av_av_seff_performance_av_av_ParametricResourceDemand

    @pcm_av_av_seff_performance_av_av_ParametricResourceDemand.setter
    def pcm_av_av_seff_performance_av_av_ParametricResourceDemand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_seff_performance_av_av_ParametricResourceDemand__pcm_av_av_seff_performance_av_av_ParametricResourceDemand", None)
        self.__pcm_av_av_seff_performance_av_av_ParametricResourceDemand = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcessingResourceType587"):
                opp_val = getattr(old_value, "ProcessingResourceType587", None)
                if opp_val == self:
                    setattr(old_value, "ProcessingResourceType587", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessingResourceType587"):
                opp_val = getattr(value, "ProcessingResourceType587", None)
                setattr(value, "ProcessingResourceType587", self)

    def DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

class seff_av_av_AbstractInternalControlFlowAction:

    pass
class seff_av_av_CallAction:

    pass
class pcm_av_av_seff_av_av_InternalCallAction(seff_av_av_AbstractInternalControlFlowAction, seff_av_av_CallAction):

    pass
class seff_reliability_av_av_FailureHandlingEntity:

    pass
class seff_av_av_CallReturnAction:

    pass
class seff_av_av_AbstractAction:

    pass
class pcm_av_av_seff_av_av_EmitEventAction(seff_av_av_CallAction, seff_av_av_AbstractAction):

    pass
class pcm_av_av_seff_av_av_ExternalCallAction(seff_av_av_CallReturnAction, seff_av_av_AbstractAction, seff_reliability_av_av_FailureHandlingEntity):

    def __init__(self, retryCount: int, pcm_av_av_seff_av_av_ExternalCallAction: "OperationSignature" = None, pcm_av_av_seff_av_av_ExternalCallAction537: "OperationRequiredRole" = None):
        self.retryCount = retryCount
        self.pcm_av_av_seff_av_av_ExternalCallAction = pcm_av_av_seff_av_av_ExternalCallAction
        self.pcm_av_av_seff_av_av_ExternalCallAction537 = pcm_av_av_seff_av_av_ExternalCallAction537
        
    @property
    def retryCount(self) -> int:
        return self.__retryCount

    @retryCount.setter
    def retryCount(self, retryCount: int):
        self.__retryCount = retryCount

    @property
    def pcm_av_av_seff_av_av_ExternalCallAction(self):
        return self.__pcm_av_av_seff_av_av_ExternalCallAction

    @pcm_av_av_seff_av_av_ExternalCallAction.setter
    def pcm_av_av_seff_av_av_ExternalCallAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_seff_av_av_ExternalCallAction__pcm_av_av_seff_av_av_ExternalCallAction", None)
        self.__pcm_av_av_seff_av_av_ExternalCallAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationSignature535"):
                opp_val = getattr(old_value, "OperationSignature535", None)
                if opp_val == self:
                    setattr(old_value, "OperationSignature535", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationSignature535"):
                opp_val = getattr(value, "OperationSignature535", None)
                setattr(value, "OperationSignature535", self)

    @property
    def pcm_av_av_seff_av_av_ExternalCallAction537(self):
        return self.__pcm_av_av_seff_av_av_ExternalCallAction537

    @pcm_av_av_seff_av_av_ExternalCallAction537.setter
    def pcm_av_av_seff_av_av_ExternalCallAction537(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_seff_av_av_ExternalCallAction__pcm_av_av_seff_av_av_ExternalCallAction537", None)
        self.__pcm_av_av_seff_av_av_ExternalCallAction537 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationRequiredRole538"):
                opp_val = getattr(old_value, "OperationRequiredRole538", None)
                if opp_val == self:
                    setattr(old_value, "OperationRequiredRole538", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationRequiredRole538"):
                opp_val = getattr(value, "OperationRequiredRole538", None)
                setattr(value, "OperationRequiredRole538", self)

    def OperationRequiredRoleMustBeReferencedByContainer(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement OperationRequiredRoleMustBeReferencedByContainer method
        pass

    def SignatureBelongsToRole(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SignatureBelongsToRole method
        pass

class ResourceDemandingInternalBehaviour:

    pass
class seff_av_av_ResourceDemandingBehaviour:

    pass
class pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour(seff_av_av_ResourceDemandingBehaviour, seff_reliability_av_av_FailureHandlingEntity):

    def __init__(self, pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour: set["seff_reliability_av_av_RecoveryActionBehaviour"] = None, seff_reliability_av_av: "seff_reliability_av_av_RecoveryAction" = None):
        self.pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour = pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour if pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour is not None else set()
        self.seff_reliability_av_av = seff_reliability_av_av
        
    @property
    def seff_reliability_av_av(self):
        return self.__seff_reliability_av_av

    @seff_reliability_av_av.setter
    def seff_reliability_av_av(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour__seff_reliability_av_av", None)
        self.__seff_reliability_av_av = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av_av593"):
                opp_val = getattr(old_value, "seff_av_av593", None)
                if opp_val == self:
                    setattr(old_value, "seff_av_av593", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av_av593"):
                opp_val = getattr(value, "seff_av_av593", None)
                setattr(value, "seff_av_av593", self)

    @property
    def pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour(self):
        return self.__pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour

    @pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour.setter
    def pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour__pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour", None)
        self.__pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_reliability_av_av_RecoveryActionBehaviour"):
                    opp_val = getattr(item, "seff_reliability_av_av_RecoveryActionBehaviour", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_reliability_av_av_RecoveryActionBehaviour", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_reliability_av_av_RecoveryActionBehaviour"):
                    opp_val = getattr(item, "seff_reliability_av_av_RecoveryActionBehaviour", None)
                    
                    setattr(item, "seff_reliability_av_av_RecoveryActionBehaviour", self)
                    

    def SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes method
        pass

    def RecoveryActionBehaviourIsNotSuccessorOfItself(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RecoveryActionBehaviourIsNotSuccessorOfItself method
        pass

    def RecoveryActionBehaviourHasOnlyOnePredecessor(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RecoveryActionBehaviourHasOnlyOnePredecessor method
        pass

class seff_av_av_ServiceEffectSpecification:

    pass
class pcm_av_av_seff_av_av_SynchronisationPoint:

    pass
class ForkAction:

    pass
class ForkedBehaviour:

    pass
class ResourceDemandingSEFF:

    pass
class BranchAction:

    pass
class pcm_av_av_seff_av_av_ServiceEffectSpecification:

    def __init__(self, seffTypeID: str, pcm_av_av_seff_av_av_ServiceEffectSpecification: "Signature" = None, BasicComponent504: "BasicComponent" = None):
        self.seffTypeID = seffTypeID
        self.pcm_av_av_seff_av_av_ServiceEffectSpecification = pcm_av_av_seff_av_av_ServiceEffectSpecification
        self.BasicComponent504 = BasicComponent504
        
    @property
    def seffTypeID(self) -> str:
        return self.__seffTypeID

    @seffTypeID.setter
    def seffTypeID(self, seffTypeID: str):
        self.__seffTypeID = seffTypeID

    @property
    def pcm_av_av_seff_av_av_ServiceEffectSpecification(self):
        return self.__pcm_av_av_seff_av_av_ServiceEffectSpecification

    @pcm_av_av_seff_av_av_ServiceEffectSpecification.setter
    def pcm_av_av_seff_av_av_ServiceEffectSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_seff_av_av_ServiceEffectSpecification__pcm_av_av_seff_av_av_ServiceEffectSpecification", None)
        self.__pcm_av_av_seff_av_av_ServiceEffectSpecification = value
        
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

    @property
    def BasicComponent504(self):
        return self.__BasicComponent504

    @BasicComponent504.setter
    def BasicComponent504(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_seff_av_av_ServiceEffectSpecification__BasicComponent504", None)
        self.__BasicComponent504 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av_av505"):
                opp_val = getattr(old_value, "repository_av_av505", None)
                if opp_val == self:
                    setattr(old_value, "repository_av_av505", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av_av505"):
                opp_val = getattr(value, "repository_av_av505", None)
                setattr(value, "repository_av_av505", self)

    def ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole method
        pass

class pcm_av_av_seff_av_av_CallAction:

    pass
class AbstractAction:

    pass
class pcm_av_av_seff_av_av_AbstractInternalControlFlowAction(AbstractAction):

    pass
class AbstractBranchTransition:

    pass
class pcm_av_av_seff_av_av_ProbabilisticBranchTransition(AbstractBranchTransition):

    def __init__(self, branchProbability: float, seff_av_av484: "pcm_av_av_seff_av_av_ResourceDemandingBehaviour", seff_av_av498: "pcm_av_av_seff_av_av_BranchAction"):
        self.branchProbability = branchProbability
        
    @property
    def branchProbability(self) -> float:
        return self.__branchProbability

    @branchProbability.setter
    def branchProbability(self, branchProbability: float):
        self.__branchProbability = branchProbability

class pcm_av_av_seff_av_av_GuardedBranchTransition(AbstractBranchTransition):

    pass
class AbstractLoopAction:

    pass
class pcm_av_av_seff_av_av_LoopAction(AbstractLoopAction):

    pass
class pcm_av_av_seff_av_av_CollectionIteratorAction(AbstractLoopAction):

    pass
class ResourceDemandingBehaviour:

    pass
class pcm_av_av_seff_av_av_ResourceDemandingInternalBehaviour(ResourceDemandingBehaviour):

    pass
class pcm_av_av_seff_av_av_ForkedBehaviour(ResourceDemandingBehaviour):

    pass
class CommunicationLinkResourceType:

    pass
class AbstractInternalControlFlowAction:

    pass
class pcm_av_av_seff_av_av_StartAction(AbstractInternalControlFlowAction):

    def __init__(self, seff_av_av574: "pcm_av_av_seff_performance_av_av_ResourceCall", seff_av_av568: "pcm_av_av_seff_performance_av_av_InfrastructureCall", seff_av_av590: "pcm_av_av_seff_performance_av_av_ParametricResourceDemand"):
        
    def StartActionPredecessorMustNotBeDefined(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement StartActionPredecessorMustNotBeDefined method
        pass

class pcm_av_av_seff_av_av_AcquireAction(AbstractInternalControlFlowAction):

    def __init__(self, timeout: bool, timeoutValue: float, pcm_av_av_seff_av_av_AcquireAction: "PassiveResource" = None, seff_av_av574: "pcm_av_av_seff_performance_av_av_ResourceCall", seff_av_av568: "pcm_av_av_seff_performance_av_av_InfrastructureCall", seff_av_av590: "pcm_av_av_seff_performance_av_av_ParametricResourceDemand"):
        self.timeout = timeout
        self.timeoutValue = timeoutValue
        self.pcm_av_av_seff_av_av_AcquireAction = pcm_av_av_seff_av_av_AcquireAction
        
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
    def pcm_av_av_seff_av_av_AcquireAction(self):
        return self.__pcm_av_av_seff_av_av_AcquireAction

    @pcm_av_av_seff_av_av_AcquireAction.setter
    def pcm_av_av_seff_av_av_AcquireAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_seff_av_av_AcquireAction__pcm_av_av_seff_av_av_AcquireAction", None)
        self.__pcm_av_av_seff_av_av_AcquireAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PassiveResource543"):
                opp_val = getattr(old_value, "PassiveResource543", None)
                if opp_val == self:
                    setattr(old_value, "PassiveResource543", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PassiveResource543"):
                opp_val = getattr(value, "PassiveResource543", None)
                setattr(value, "PassiveResource543", self)

    def TimeoutValueOfAcquireActionMustNotBeNegative(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement TimeoutValueOfAcquireActionMustNotBeNegative method
        pass

class pcm_av_av_seff_av_av_ForkAction(AbstractInternalControlFlowAction):

    pass
class pcm_av_av_seff_av_av_BranchAction(AbstractInternalControlFlowAction):

    def __init__(self, AbstractBranchTransition497: set["AbstractBranchTransition"] = None, seff_av_av574: "pcm_av_av_seff_performance_av_av_ResourceCall", seff_av_av568: "pcm_av_av_seff_performance_av_av_InfrastructureCall", seff_av_av590: "pcm_av_av_seff_performance_av_av_ParametricResourceDemand"):
        self.AbstractBranchTransition497 = AbstractBranchTransition497 if AbstractBranchTransition497 is not None else set()
        
    @property
    def AbstractBranchTransition497(self):
        return self.__AbstractBranchTransition497

    @AbstractBranchTransition497.setter
    def AbstractBranchTransition497(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_seff_av_av_BranchAction__AbstractBranchTransition497", None)
        self.__AbstractBranchTransition497 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_av_av498"):
                    opp_val = getattr(item, "seff_av_av498", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_av_av498", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_av_av498"):
                    opp_val = getattr(item, "seff_av_av498", None)
                    
                    setattr(item, "seff_av_av498", self)
                    

    def AllProbabilisticBranchProbabilitiesMustSumUpTo1(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AllProbabilisticBranchProbabilitiesMustSumUpTo1 method
        pass

    def EitherGuardedBranchesOrProbabilisiticBranchTransitions(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EitherGuardedBranchesOrProbabilisiticBranchTransitions method
        pass

class pcm_av_av_seff_reliability_av_av_RecoveryAction(AbstractInternalControlFlowAction):

    def __init__(self, pcm_av_av_seff_reliability_av_av_RecoveryAction: "seff_reliability_av_av_RecoveryActionBehaviour" = None, seff_reliability_av_av597: set["seff_reliability_av_av_RecoveryActionBehaviour"] = None, seff_av_av574: "pcm_av_av_seff_performance_av_av_ResourceCall", seff_av_av568: "pcm_av_av_seff_performance_av_av_InfrastructureCall", seff_av_av590: "pcm_av_av_seff_performance_av_av_ParametricResourceDemand"):
        self.pcm_av_av_seff_reliability_av_av_RecoveryAction = pcm_av_av_seff_reliability_av_av_RecoveryAction
        self.seff_reliability_av_av597 = seff_reliability_av_av597 if seff_reliability_av_av597 is not None else set()
        
    @property
    def pcm_av_av_seff_reliability_av_av_RecoveryAction(self):
        return self.__pcm_av_av_seff_reliability_av_av_RecoveryAction

    @pcm_av_av_seff_reliability_av_av_RecoveryAction.setter
    def pcm_av_av_seff_reliability_av_av_RecoveryAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_seff_reliability_av_av_RecoveryAction__pcm_av_av_seff_reliability_av_av_RecoveryAction", None)
        self.__pcm_av_av_seff_reliability_av_av_RecoveryAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_reliability_av_av_RecoveryActionBehaviour595"):
                opp_val = getattr(old_value, "seff_reliability_av_av_RecoveryActionBehaviour595", None)
                if opp_val == self:
                    setattr(old_value, "seff_reliability_av_av_RecoveryActionBehaviour595", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_reliability_av_av_RecoveryActionBehaviour595"):
                opp_val = getattr(value, "seff_reliability_av_av_RecoveryActionBehaviour595", None)
                setattr(value, "seff_reliability_av_av_RecoveryActionBehaviour595", self)

    @property
    def seff_reliability_av_av597(self):
        return self.__seff_reliability_av_av597

    @seff_reliability_av_av597.setter
    def seff_reliability_av_av597(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_seff_reliability_av_av_RecoveryAction__seff_reliability_av_av597", None)
        self.__seff_reliability_av_av597 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_av_av598"):
                    opp_val = getattr(item, "seff_av_av598", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_av_av598", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_av_av598"):
                    opp_val = getattr(item, "seff_av_av598", None)
                    
                    setattr(item, "seff_av_av598", self)
                    

    def PrimaryBehaviourOfRecoveryActionMustBeSet(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement PrimaryBehaviourOfRecoveryActionMustBeSet method
        pass

class pcm_av_av_seff_av_av_ReleaseAction(AbstractInternalControlFlowAction):

    pass
class pcm_av_av_seff_av_av_InternalAction(AbstractInternalControlFlowAction):

    def __init__(self, InternalFailureOccurrenceDescription560: set["InternalFailureOccurrenceDescription"] = None, seff_av_av574: "pcm_av_av_seff_performance_av_av_ResourceCall", seff_av_av568: "pcm_av_av_seff_performance_av_av_InfrastructureCall", seff_av_av590: "pcm_av_av_seff_performance_av_av_ParametricResourceDemand"):
        self.InternalFailureOccurrenceDescription560 = InternalFailureOccurrenceDescription560 if InternalFailureOccurrenceDescription560 is not None else set()
        
    @property
    def InternalFailureOccurrenceDescription560(self):
        return self.__InternalFailureOccurrenceDescription560

    @InternalFailureOccurrenceDescription560.setter
    def InternalFailureOccurrenceDescription560(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_seff_av_av_InternalAction__InternalFailureOccurrenceDescription560", None)
        self.__InternalFailureOccurrenceDescription560 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reliability_av_av561"):
                    opp_val = getattr(item, "reliability_av_av561", None)
                    
                    if opp_val == self:
                        setattr(item, "reliability_av_av561", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reliability_av_av561"):
                    opp_val = getattr(item, "reliability_av_av561", None)
                    
                    setattr(item, "reliability_av_av561", self)
                    

    def SumOfInternalActionFailureProbabilitiesMustNotExceed1(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SumOfInternalActionFailureProbabilitiesMustNotExceed1 method
        pass

    def MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed method
        pass

class pcm_av_av_seff_av_av_SetVariableAction(AbstractInternalControlFlowAction):

    pass
class pcm_av_av_seff_av_av_AbstractLoopAction(AbstractInternalControlFlowAction):

    pass
class pcm_av_av_seff_av_av_StopAction(AbstractInternalControlFlowAction):

    def __init__(self, seff_av_av574: "pcm_av_av_seff_performance_av_av_ResourceCall", seff_av_av568: "pcm_av_av_seff_performance_av_av_InfrastructureCall", seff_av_av590: "pcm_av_av_seff_performance_av_av_ParametricResourceDemand"):
        
    def StopActionSuccessorMustNotBeDefined(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement StopActionSuccessorMustNotBeDefined method
        pass

class qos_reliability_av_av_SpecifiedReliabilityAnnotation:

    pass
class SoftwareInducedFailureType:

    pass
class pcm_av_av_reliability_av_av_ResourceTimeoutFailureType(SoftwareInducedFailureType):

    pass
class InternalAction:

    pass
class FailureOccurrenceDescription:

    pass
class pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription(FailureOccurrenceDescription):

    def __init__(self, qos_reliability_av_av: "qos_reliability_av_av_SpecifiedReliabilityAnnotation" = None, pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription: "FailureType" = None):
        self.qos_reliability_av_av = qos_reliability_av_av
        self.pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription = pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription
        
    @property
    def qos_reliability_av_av(self):
        return self.__qos_reliability_av_av

    @qos_reliability_av_av.setter
    def qos_reliability_av_av(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription__qos_reliability_av_av", None)
        self.__qos_reliability_av_av = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qosannotations_av_av456"):
                opp_val = getattr(old_value, "qosannotations_av_av456", None)
                if opp_val == self:
                    setattr(old_value, "qosannotations_av_av456", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qosannotations_av_av456"):
                opp_val = getattr(value, "qosannotations_av_av456", None)
                setattr(value, "qosannotations_av_av456", self)

    @property
    def pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription(self):
        return self.__pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription

    @pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription.setter
    def pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription__pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription", None)
        self.__pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FailureType458"):
                opp_val = getattr(old_value, "FailureType458", None)
                if opp_val == self:
                    setattr(old_value, "FailureType458", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FailureType458"):
                opp_val = getattr(value, "FailureType458", None)
                setattr(value, "FailureType458", self)

    def NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription method
        pass

class pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription(FailureOccurrenceDescription):

    def __init__(self, InternalAction: "InternalAction" = None, SoftwareInducedFailureType: "SoftwareInducedFailureType" = None):
        self.InternalAction = InternalAction
        self.SoftwareInducedFailureType = SoftwareInducedFailureType
        
    @property
    def InternalAction(self):
        return self.__InternalAction

    @InternalAction.setter
    def InternalAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription__InternalAction", None)
        self.__InternalAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av_av450"):
                opp_val = getattr(old_value, "seff_av_av450", None)
                if opp_val == self:
                    setattr(old_value, "seff_av_av450", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av_av450"):
                opp_val = getattr(value, "seff_av_av450", None)
                setattr(value, "seff_av_av450", self)

    @property
    def SoftwareInducedFailureType(self):
        return self.__SoftwareInducedFailureType

    @SoftwareInducedFailureType.setter
    def SoftwareInducedFailureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription__SoftwareInducedFailureType", None)
        self.__SoftwareInducedFailureType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reliability_av_av452"):
                opp_val = getattr(old_value, "reliability_av_av452", None)
                if opp_val == self:
                    setattr(old_value, "reliability_av_av452", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reliability_av_av452"):
                opp_val = getattr(value, "reliability_av_av452", None)
                setattr(value, "reliability_av_av452", self)

    def NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription method
        pass

class InternalFailureOccurrenceDescription:

    pass
class ProcessingResourceType:

    pass
class pcm_av_av_parameter_av_av_VariableCharacterisation:

    def __init__(self, type: str, PCMRandomVariable440: "PCMRandomVariable" = None, VariableUsage443: "VariableUsage" = None):
        self.type = type
        self.PCMRandomVariable440 = PCMRandomVariable440
        self.VariableUsage443 = VariableUsage443
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def PCMRandomVariable440(self):
        return self.__PCMRandomVariable440

    @PCMRandomVariable440.setter
    def PCMRandomVariable440(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_parameter_av_av_VariableCharacterisation__PCMRandomVariable440", None)
        self.__PCMRandomVariable440 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av_av441"):
                opp_val = getattr(old_value, "core_av_av441", None)
                if opp_val == self:
                    setattr(old_value, "core_av_av441", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av_av441"):
                opp_val = getattr(value, "core_av_av441", None)
                setattr(value, "core_av_av441", self)

    @property
    def VariableUsage443(self):
        return self.__VariableUsage443

    @VariableUsage443.setter
    def VariableUsage443(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_parameter_av_av_VariableCharacterisation__VariableUsage443", None)
        self.__VariableUsage443 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameter_av_av444"):
                opp_val = getattr(old_value, "parameter_av_av444", None)
                if opp_val == self:
                    setattr(old_value, "parameter_av_av444", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameter_av_av444"):
                opp_val = getattr(value, "parameter_av_av444", None)
                setattr(value, "parameter_av_av444", self)

class parameter_av_av_pcm_av_av_AbstractNamedReference:

    pass
class EntryLevelSystemCall:

    pass
class SpecifiedOutputParameterAbstraction:

    pass
class SetVariableAction:

    pass
class pcm_av_av_reliability_av_av_FailureOccurrenceDescription:

    def __init__(self, failureProbability: float):
        self.failureProbability = failureProbability
        
    @property
    def failureProbability(self) -> float:
        return self.__failureProbability

    @failureProbability.setter
    def failureProbability(self, failureProbability: float):
        self.__failureProbability = failureProbability

    def EnsureValidFailureProbabilityRange(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement EnsureValidFailureProbabilityRange method
        pass

class Variable:

    pass
class pcm_av_av_parameter_av_av_CharacterisedVariable(Variable):

    def __init__(self, characterisationType: str):
        self.characterisationType = characterisationType
        
    @property
    def characterisationType(self) -> str:
        return self.__characterisationType

    @characterisationType.setter
    def characterisationType(self, characterisationType: str):
        self.__characterisationType = characterisationType

class SchedulingPolicy:

    pass
class pcm_av_av_resourcetype_av_av_ResourceRepository:

    pass
class ResourceRepository:

    pass
class CallReturnAction:

    pass
class SynchronisationPoint:

    pass
class CallAction:

    pass
class pcm_av_av_seff_performance_av_av_InfrastructureCall(CallAction):

    def __init__(self, pcm_av_av_seff_performance_av_av_InfrastructureCall: "InfrastructureSignature" = None, PCMRandomVariable565: "PCMRandomVariable" = None, AbstractInternalControlFlowAction: "AbstractInternalControlFlowAction" = None, pcm_av_av_seff_performance_av_av_InfrastructureCall570: "InfrastructureRequiredRole" = None, seff_av_av421: "pcm_av_av_parameter_av_av_VariableUsage"):
        self.pcm_av_av_seff_performance_av_av_InfrastructureCall = pcm_av_av_seff_performance_av_av_InfrastructureCall
        self.PCMRandomVariable565 = PCMRandomVariable565
        self.AbstractInternalControlFlowAction = AbstractInternalControlFlowAction
        self.pcm_av_av_seff_performance_av_av_InfrastructureCall570 = pcm_av_av_seff_performance_av_av_InfrastructureCall570
        
    @property
    def AbstractInternalControlFlowAction(self):
        return self.__AbstractInternalControlFlowAction

    @AbstractInternalControlFlowAction.setter
    def AbstractInternalControlFlowAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_seff_performance_av_av_InfrastructureCall__AbstractInternalControlFlowAction", None)
        self.__AbstractInternalControlFlowAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av_av568"):
                opp_val = getattr(old_value, "seff_av_av568", None)
                if opp_val == self:
                    setattr(old_value, "seff_av_av568", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av_av568"):
                opp_val = getattr(value, "seff_av_av568", None)
                setattr(value, "seff_av_av568", self)

    @property
    def PCMRandomVariable565(self):
        return self.__PCMRandomVariable565

    @PCMRandomVariable565.setter
    def PCMRandomVariable565(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_seff_performance_av_av_InfrastructureCall__PCMRandomVariable565", None)
        self.__PCMRandomVariable565 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av_av566"):
                opp_val = getattr(old_value, "core_av_av566", None)
                if opp_val == self:
                    setattr(old_value, "core_av_av566", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av_av566"):
                opp_val = getattr(value, "core_av_av566", None)
                setattr(value, "core_av_av566", self)

    @property
    def pcm_av_av_seff_performance_av_av_InfrastructureCall(self):
        return self.__pcm_av_av_seff_performance_av_av_InfrastructureCall

    @pcm_av_av_seff_performance_av_av_InfrastructureCall.setter
    def pcm_av_av_seff_performance_av_av_InfrastructureCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_seff_performance_av_av_InfrastructureCall__pcm_av_av_seff_performance_av_av_InfrastructureCall", None)
        self.__pcm_av_av_seff_performance_av_av_InfrastructureCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InfrastructureSignature563"):
                opp_val = getattr(old_value, "InfrastructureSignature563", None)
                if opp_val == self:
                    setattr(old_value, "InfrastructureSignature563", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InfrastructureSignature563"):
                opp_val = getattr(value, "InfrastructureSignature563", None)
                setattr(value, "InfrastructureSignature563", self)

    @property
    def pcm_av_av_seff_performance_av_av_InfrastructureCall570(self):
        return self.__pcm_av_av_seff_performance_av_av_InfrastructureCall570

    @pcm_av_av_seff_performance_av_av_InfrastructureCall570.setter
    def pcm_av_av_seff_performance_av_av_InfrastructureCall570(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_seff_performance_av_av_InfrastructureCall__pcm_av_av_seff_performance_av_av_InfrastructureCall570", None)
        self.__pcm_av_av_seff_performance_av_av_InfrastructureCall570 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InfrastructureRequiredRole571"):
                opp_val = getattr(old_value, "InfrastructureRequiredRole571", None)
                if opp_val == self:
                    setattr(old_value, "InfrastructureRequiredRole571", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InfrastructureRequiredRole571"):
                opp_val = getattr(value, "InfrastructureRequiredRole571", None)
                setattr(value, "InfrastructureRequiredRole571", self)

    def SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

    def ReferencedRequiredRoleMustBeRequiredByComponent(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ReferencedRequiredRoleMustBeRequiredByComponent method
        pass

    def SignatureMustBelongToUsedRequiredRole(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SignatureMustBelongToUsedRequiredRole method
        pass

class pcm_av_av_seff_av_av_CallReturnAction(CallAction):

    pass
class pcm_av_av_seff_performance_av_av_ResourceCall(CallAction):

    def __init__(self, AbstractInternalControlFlowAction573: "AbstractInternalControlFlowAction" = None, pcm_av_av_seff_performance_av_av_ResourceCall: "entity_av_av_ResourceRequiredRole" = None, pcm_av_av_seff_performance_av_av_ResourceCall578: "ResourceSignature" = None, PCMRandomVariable581: "PCMRandomVariable" = None, seff_av_av421: "pcm_av_av_parameter_av_av_VariableUsage"):
        self.AbstractInternalControlFlowAction573 = AbstractInternalControlFlowAction573
        self.pcm_av_av_seff_performance_av_av_ResourceCall = pcm_av_av_seff_performance_av_av_ResourceCall
        self.pcm_av_av_seff_performance_av_av_ResourceCall578 = pcm_av_av_seff_performance_av_av_ResourceCall578
        self.PCMRandomVariable581 = PCMRandomVariable581
        
    @property
    def AbstractInternalControlFlowAction573(self):
        return self.__AbstractInternalControlFlowAction573

    @AbstractInternalControlFlowAction573.setter
    def AbstractInternalControlFlowAction573(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_seff_performance_av_av_ResourceCall__AbstractInternalControlFlowAction573", None)
        self.__AbstractInternalControlFlowAction573 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av_av574"):
                opp_val = getattr(old_value, "seff_av_av574", None)
                if opp_val == self:
                    setattr(old_value, "seff_av_av574", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av_av574"):
                opp_val = getattr(value, "seff_av_av574", None)
                setattr(value, "seff_av_av574", self)

    @property
    def PCMRandomVariable581(self):
        return self.__PCMRandomVariable581

    @PCMRandomVariable581.setter
    def PCMRandomVariable581(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_seff_performance_av_av_ResourceCall__PCMRandomVariable581", None)
        self.__PCMRandomVariable581 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av_av582"):
                opp_val = getattr(old_value, "core_av_av582", None)
                if opp_val == self:
                    setattr(old_value, "core_av_av582", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av_av582"):
                opp_val = getattr(value, "core_av_av582", None)
                setattr(value, "core_av_av582", self)

    @property
    def pcm_av_av_seff_performance_av_av_ResourceCall(self):
        return self.__pcm_av_av_seff_performance_av_av_ResourceCall

    @pcm_av_av_seff_performance_av_av_ResourceCall.setter
    def pcm_av_av_seff_performance_av_av_ResourceCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_seff_performance_av_av_ResourceCall__pcm_av_av_seff_performance_av_av_ResourceCall", None)
        self.__pcm_av_av_seff_performance_av_av_ResourceCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entity_av_av_ResourceRequiredRole576"):
                opp_val = getattr(old_value, "entity_av_av_ResourceRequiredRole576", None)
                if opp_val == self:
                    setattr(old_value, "entity_av_av_ResourceRequiredRole576", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entity_av_av_ResourceRequiredRole576"):
                opp_val = getattr(value, "entity_av_av_ResourceRequiredRole576", None)
                setattr(value, "entity_av_av_ResourceRequiredRole576", self)

    @property
    def pcm_av_av_seff_performance_av_av_ResourceCall578(self):
        return self.__pcm_av_av_seff_performance_av_av_ResourceCall578

    @pcm_av_av_seff_performance_av_av_ResourceCall578.setter
    def pcm_av_av_seff_performance_av_av_ResourceCall578(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_seff_performance_av_av_ResourceCall__pcm_av_av_seff_performance_av_av_ResourceCall578", None)
        self.__pcm_av_av_seff_performance_av_av_ResourceCall578 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceSignature579"):
                opp_val = getattr(old_value, "ResourceSignature579", None)
                if opp_val == self:
                    setattr(old_value, "ResourceSignature579", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceSignature579"):
                opp_val = getattr(value, "ResourceSignature579", None)
                setattr(value, "ResourceSignature579", self)

    def ResourceSignatureBelongsToResourceRequiredRole(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ResourceSignatureBelongsToResourceRequiredRole method
        pass

    def ResourceRequiredRoleMustBeReferencedByComponent(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ResourceRequiredRoleMustBeReferencedByComponent method
        pass

    def SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

class pcm_av_av_parameter_av_av_VariableUsage:

    pass
class pcm_av_av_protocol_av_av_Protocol:

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
class repository_av_av_DataType:

    pass
class UnitCarryingElement:

    pass
class HardwareInducedFailureType:

    pass
class ResourceType:

    pass
class pcm_av_av_resourcetype_av_av_CommunicationLinkResourceType(ResourceType):

    pass
class pcm_av_av_resourcetype_av_av_ProcessingResourceType(ResourceType):

    pass
class NamedElement:

    pass
class pcm_av_av_resourceenvironment_av_av_ResourceEnvironment(NamedElement):

    pass
class pcm_av_av_repository_av_av_InnerDeclaration(NamedElement):

    pass
class InnerDeclaration:

    pass
class CompositeDataType:

    pass
class ProvidesComponentType:

    pass
class repository_av_av_ImplementationComponentType:

    pass
class entity_av_av_ComposedProvidingRequiringEntity:

    pass
class pcm_av_av_subsystem_av_av_SubSystem(entity_av_av_ComposedProvidingRequiringEntity, repository_av_av_RepositoryComponent):

    pass
class pcm_av_av_completions_av_av_Completion(entity_av_av_ComposedProvidingRequiringEntity, repository_av_av_ImplementationComponentType):

    pass
class pcm_av_av_repository_av_av_CompositeComponent(entity_av_av_ComposedProvidingRequiringEntity, repository_av_av_ImplementationComponentType):

    def __init__(self):
        
    def ProvideSameInterfaces(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ProvideSameInterfaces method
        pass

    def RequireSameInterfaces(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement RequireSameInterfaces method
        pass

class InfrastructureInterface:

    pass
class OperationInterface:

    pass
class Parameter:

    pass
class pcm_av_av_repository_av_av_RequiredCharacterisation:

    def __init__(self, type: str, pcm_av_av_repository_av_av_RequiredCharacterisation: "Parameter" = None, Interface327: "Interface" = None):
        self.type = type
        self.pcm_av_av_repository_av_av_RequiredCharacterisation = pcm_av_av_repository_av_av_RequiredCharacterisation
        self.Interface327 = Interface327
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def Interface327(self):
        return self.__Interface327

    @Interface327.setter
    def Interface327(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_repository_av_av_RequiredCharacterisation__Interface327", None)
        self.__Interface327 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av_av328"):
                opp_val = getattr(old_value, "repository_av_av328", None)
                if opp_val == self:
                    setattr(old_value, "repository_av_av328", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av_av328"):
                opp_val = getattr(value, "repository_av_av328", None)
                setattr(value, "repository_av_av328", self)

    @property
    def pcm_av_av_repository_av_av_RequiredCharacterisation(self):
        return self.__pcm_av_av_repository_av_av_RequiredCharacterisation

    @pcm_av_av_repository_av_av_RequiredCharacterisation.setter
    def pcm_av_av_repository_av_av_RequiredCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_repository_av_av_RequiredCharacterisation__pcm_av_av_repository_av_av_RequiredCharacterisation", None)
        self.__pcm_av_av_repository_av_av_RequiredCharacterisation = value
        
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
class pcm_av_av_repository_av_av_ExceptionType:

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
class Signature:

    pass
class pcm_av_av_repository_av_av_OperationSignature(Signature):

    def __init__(self, OperationInterface: "OperationInterface" = None, Parameter358: set["Parameter"] = None, pcm_av_av_repository_av_av_OperationSignature: "DataType" = None, Signature614: "pcm_av_av_qosannotations_av_av_SpecifiedOutputParameterAbstraction", Signature602: "pcm_av_av_qosannotations_av_av_SpecifiedQoSAnnotation", Signature: "pcm_av_av_seff_av_av_ServiceEffectSpecification"):
        self.OperationInterface = OperationInterface
        self.Parameter358 = Parameter358 if Parameter358 is not None else set()
        self.pcm_av_av_repository_av_av_OperationSignature = pcm_av_av_repository_av_av_OperationSignature
        
    @property
    def OperationInterface(self):
        return self.__OperationInterface

    @OperationInterface.setter
    def OperationInterface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_repository_av_av_OperationSignature__OperationInterface", None)
        self.__OperationInterface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av_av356"):
                opp_val = getattr(old_value, "repository_av_av356", None)
                if opp_val == self:
                    setattr(old_value, "repository_av_av356", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av_av356"):
                opp_val = getattr(value, "repository_av_av356", None)
                setattr(value, "repository_av_av356", self)

    @property
    def Parameter358(self):
        return self.__Parameter358

    @Parameter358.setter
    def Parameter358(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_repository_av_av_OperationSignature__Parameter358", None)
        self.__Parameter358 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_av_av359"):
                    opp_val = getattr(item, "repository_av_av359", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_av_av359", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_av_av359"):
                    opp_val = getattr(item, "repository_av_av359", None)
                    
                    setattr(item, "repository_av_av359", self)
                    

    @property
    def pcm_av_av_repository_av_av_OperationSignature(self):
        return self.__pcm_av_av_repository_av_av_OperationSignature

    @pcm_av_av_repository_av_av_OperationSignature.setter
    def pcm_av_av_repository_av_av_OperationSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_repository_av_av_OperationSignature__pcm_av_av_repository_av_av_OperationSignature", None)
        self.__pcm_av_av_repository_av_av_OperationSignature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType361"):
                opp_val = getattr(old_value, "DataType361", None)
                if opp_val == self:
                    setattr(old_value, "DataType361", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType361"):
                opp_val = getattr(value, "DataType361", None)
                setattr(value, "DataType361", self)

    def ParameterNamesHaveToBeUniqueForASignature(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ParameterNamesHaveToBeUniqueForASignature method
        pass

class pcm_av_av_repository_av_av_InfrastructureSignature(Signature):

    pass
class pcm_av_av_repository_av_av_EventType(Signature):

    pass
class FailureType:

    pass
class pcm_av_av_reliability_av_av_NetworkInducedFailureType(FailureType):

    def __init__(self, CommunicationLinkResourceType: "CommunicationLinkResourceType" = None, FailureType458: "pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription", reliability_av_av312: "pcm_av_av_repository_av_av_Repository", FailureType341: "pcm_av_av_repository_av_av_Signature", FailureType600: "pcm_av_av_seff_reliability_av_av_FailureHandlingEntity"):
        self.CommunicationLinkResourceType = CommunicationLinkResourceType
        
    @property
    def CommunicationLinkResourceType(self):
        return self.__CommunicationLinkResourceType

    @CommunicationLinkResourceType.setter
    def CommunicationLinkResourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_reliability_av_av_NetworkInducedFailureType__CommunicationLinkResourceType", None)
        self.__CommunicationLinkResourceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcetype_av_av454"):
                opp_val = getattr(old_value, "resourcetype_av_av454", None)
                if opp_val == self:
                    setattr(old_value, "resourcetype_av_av454", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcetype_av_av454"):
                opp_val = getattr(value, "resourcetype_av_av454", None)
                setattr(value, "resourcetype_av_av454", self)

    def NetworkInducedFailureTypeHasCommunicationLinkResourceType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NetworkInducedFailureTypeHasCommunicationLinkResourceType method
        pass

class pcm_av_av_reliability_av_av_HardwareInducedFailureType(FailureType):

    def __init__(self, ProcessingResourceType: "ProcessingResourceType" = None, FailureType458: "pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription", reliability_av_av312: "pcm_av_av_repository_av_av_Repository", FailureType341: "pcm_av_av_repository_av_av_Signature", FailureType600: "pcm_av_av_seff_reliability_av_av_FailureHandlingEntity"):
        self.ProcessingResourceType = ProcessingResourceType
        
    @property
    def ProcessingResourceType(self):
        return self.__ProcessingResourceType

    @ProcessingResourceType.setter
    def ProcessingResourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_reliability_av_av_HardwareInducedFailureType__ProcessingResourceType", None)
        self.__ProcessingResourceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcetype_av_av446"):
                opp_val = getattr(old_value, "resourcetype_av_av446", None)
                if opp_val == self:
                    setattr(old_value, "resourcetype_av_av446", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcetype_av_av446"):
                opp_val = getattr(value, "resourcetype_av_av446", None)
                setattr(value, "resourcetype_av_av446", self)

    def HardwareInducedFailureTypeHasProcessingResourceType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement HardwareInducedFailureTypeHasProcessingResourceType method
        pass

class pcm_av_av_reliability_av_av_SoftwareInducedFailureType(FailureType):

    pass
class Protocol:

    pass
class DataType:

    pass
class pcm_av_av_repository_av_av_PrimitiveDataType(DataType):

    def __init__(self, type: str, DataType: "pcm_av_av_repository_av_av_Parameter", DataType361: "pcm_av_av_repository_av_av_OperationSignature", repository_av_av315: "pcm_av_av_repository_av_av_Repository", DataType377: "pcm_av_av_repository_av_av_CollectionDataType", DataType382: "pcm_av_av_repository_av_av_InnerDeclaration"):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class pcm_av_av_repository_av_av_Parameter:

    def __init__(self, parameterName: str, modifier__Parameter: str, InfrastructureSignature: "InfrastructureSignature" = None, OperationSignature298: "OperationSignature" = None, EventType: "EventType" = None, ResourceSignature: "ResourceSignature" = None, pcm_av_av_repository_av_av_Parameter: "DataType" = None):
        self.parameterName = parameterName
        self.modifier__Parameter = modifier__Parameter
        self.InfrastructureSignature = InfrastructureSignature
        self.OperationSignature298 = OperationSignature298
        self.EventType = EventType
        self.ResourceSignature = ResourceSignature
        self.pcm_av_av_repository_av_av_Parameter = pcm_av_av_repository_av_av_Parameter
        
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
    def pcm_av_av_repository_av_av_Parameter(self):
        return self.__pcm_av_av_repository_av_av_Parameter

    @pcm_av_av_repository_av_av_Parameter.setter
    def pcm_av_av_repository_av_av_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_repository_av_av_Parameter__pcm_av_av_repository_av_av_Parameter", None)
        self.__pcm_av_av_repository_av_av_Parameter = value
        
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

    @property
    def OperationSignature298(self):
        return self.__OperationSignature298

    @OperationSignature298.setter
    def OperationSignature298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_repository_av_av_Parameter__OperationSignature298", None)
        self.__OperationSignature298 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av_av299"):
                opp_val = getattr(old_value, "repository_av_av299", None)
                if opp_val == self:
                    setattr(old_value, "repository_av_av299", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av_av299"):
                opp_val = getattr(value, "repository_av_av299", None)
                setattr(value, "repository_av_av299", self)

    @property
    def ResourceSignature(self):
        return self.__ResourceSignature

    @ResourceSignature.setter
    def ResourceSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_repository_av_av_Parameter__ResourceSignature", None)
        self.__ResourceSignature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcetype_av_av"):
                opp_val = getattr(old_value, "resourcetype_av_av", None)
                if opp_val == self:
                    setattr(old_value, "resourcetype_av_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcetype_av_av"):
                opp_val = getattr(value, "resourcetype_av_av", None)
                setattr(value, "resourcetype_av_av", self)

    @property
    def InfrastructureSignature(self):
        return self.__InfrastructureSignature

    @InfrastructureSignature.setter
    def InfrastructureSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_repository_av_av_Parameter__InfrastructureSignature", None)
        self.__InfrastructureSignature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av_av296"):
                opp_val = getattr(old_value, "repository_av_av296", None)
                if opp_val == self:
                    setattr(old_value, "repository_av_av296", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av_av296"):
                opp_val = getattr(value, "repository_av_av296", None)
                setattr(value, "repository_av_av296", self)

    @property
    def EventType(self):
        return self.__EventType

    @EventType.setter
    def EventType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_repository_av_av_Parameter__EventType", None)
        self.__EventType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av_av301"):
                opp_val = getattr(old_value, "repository_av_av301", None)
                if opp_val == self:
                    setattr(old_value, "repository_av_av301", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av_av301"):
                opp_val = getattr(value, "repository_av_av301", None)
                setattr(value, "repository_av_av301", self)

class Repository:

    pass
class InterfaceProvidingRequiringEntity:

    pass
class pcm_av_av_repository_av_av_RepositoryComponent(InterfaceProvidingRequiringEntity):

    pass
class Interface:

    pass
class pcm_av_av_repository_av_av_OperationInterface(Interface):

    def __init__(self, OperationSignature363: set["OperationSignature"] = None, Interface317: "pcm_av_av_repository_av_av_Interface", repository_av_av310: "pcm_av_av_repository_av_av_Repository", repository_av_av328: "pcm_av_av_repository_av_av_RequiredCharacterisation"):
        self.OperationSignature363 = OperationSignature363 if OperationSignature363 is not None else set()
        
    @property
    def OperationSignature363(self):
        return self.__OperationSignature363

    @OperationSignature363.setter
    def OperationSignature363(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_repository_av_av_OperationInterface__OperationSignature363", None)
        self.__OperationSignature363 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_av_av364"):
                    opp_val = getattr(item, "repository_av_av364", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_av_av364", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_av_av364"):
                    opp_val = getattr(item, "repository_av_av364", None)
                    
                    setattr(item, "repository_av_av364", self)
                    

    def SignaturesHaveToBeUniqueForAnInterface(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SignaturesHaveToBeUniqueForAnInterface method
        pass

class pcm_av_av_repository_av_av_InfrastructureInterface(Interface):

    pass
class pcm_av_av_repository_av_av_EventGroup(Interface):

    pass
class pcm_av_av_repository_av_av_DataType:

    pass
class ResourceSignature:

    pass
class EventType:

    pass
class InfrastructureSignature:

    pass
class ServiceEffectSpecification:

    pass
class CompleteComponentType:

    pass
class ImplementationComponentType:

    pass
class pcm_av_av_repository_av_av_BasicComponent(ImplementationComponentType):

    def __init__(self, PassiveResource283: set["PassiveResource"] = None, ServiceEffectSpecification: set["ServiceEffectSpecification"] = None):
        self.PassiveResource283 = PassiveResource283 if PassiveResource283 is not None else set()
        self.ServiceEffectSpecification = ServiceEffectSpecification if ServiceEffectSpecification is not None else set()
        
    @property
    def PassiveResource283(self):
        return self.__PassiveResource283

    @PassiveResource283.setter
    def PassiveResource283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_repository_av_av_BasicComponent__PassiveResource283", None)
        self.__PassiveResource283 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_av_av284"):
                    opp_val = getattr(item, "repository_av_av284", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_av_av284", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_av_av284"):
                    opp_val = getattr(item, "repository_av_av284", None)
                    
                    setattr(item, "repository_av_av284", self)
                    

    @property
    def ServiceEffectSpecification(self):
        return self.__ServiceEffectSpecification

    @ServiceEffectSpecification.setter
    def ServiceEffectSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_repository_av_av_BasicComponent__ServiceEffectSpecification", None)
        self.__ServiceEffectSpecification = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_av_av281"):
                    opp_val = getattr(item, "seff_av_av281", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_av_av281", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_av_av281"):
                    opp_val = getattr(item, "seff_av_av281", None)
                    
                    setattr(item, "seff_av_av281", self)
                    

    def NoSeffTypeUsedTwice(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NoSeffTypeUsedTwice method
        pass

    def ProvideSameInterfacesAsImplementationType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ProvideSameInterfacesAsImplementationType method
        pass

    def RequireSameInterfacesAsImplementationType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RequireSameInterfacesAsImplementationType method
        pass

class ResourceTimeoutFailureType:

    pass
class BasicComponent:

    pass
class Branch:

    pass
class pcm_av_av_usagemodel_av_av_BranchTransition:

    def __init__(self, branchProbability: float, Branch: "Branch" = None, ScenarioBehaviour254: "ScenarioBehaviour" = None):
        self.branchProbability = branchProbability
        self.Branch = Branch
        self.ScenarioBehaviour254 = ScenarioBehaviour254
        
    @property
    def branchProbability(self) -> float:
        return self.__branchProbability

    @branchProbability.setter
    def branchProbability(self, branchProbability: float):
        self.__branchProbability = branchProbability

    @property
    def Branch(self):
        return self.__Branch

    @Branch.setter
    def Branch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_usagemodel_av_av_BranchTransition__Branch", None)
        self.__Branch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av_av252"):
                opp_val = getattr(old_value, "usagemodel_av_av252", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av_av252", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av_av252"):
                opp_val = getattr(value, "usagemodel_av_av252", None)
                setattr(value, "usagemodel_av_av252", self)

    @property
    def ScenarioBehaviour254(self):
        return self.__ScenarioBehaviour254

    @ScenarioBehaviour254.setter
    def ScenarioBehaviour254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_usagemodel_av_av_BranchTransition__ScenarioBehaviour254", None)
        self.__ScenarioBehaviour254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av_av255"):
                opp_val = getattr(old_value, "usagemodel_av_av255", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av_av255", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av_av255"):
                opp_val = getattr(value, "usagemodel_av_av255", None)
                setattr(value, "usagemodel_av_av255", self)

class BranchTransition:

    pass
class OperationSignature:

    pass
class AbstractUserAction:

    pass
class pcm_av_av_usagemodel_av_av_Start(AbstractUserAction):

    def __init__(self, usagemodel_av_av233: "pcm_av_av_usagemodel_av_av_AbstractUserAction", usagemodel_av_av250: "pcm_av_av_usagemodel_av_av_ScenarioBehaviour", usagemodel_av_av236: "pcm_av_av_usagemodel_av_av_AbstractUserAction"):
        
    def StartHasNoPredecessor(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement StartHasNoPredecessor method
        pass

class pcm_av_av_usagemodel_av_av_Delay(AbstractUserAction):

    pass
class pcm_av_av_usagemodel_av_av_Loop(AbstractUserAction):

    pass
class pcm_av_av_usagemodel_av_av_Branch(AbstractUserAction):

    def __init__(self, BranchTransition257: set["BranchTransition"] = None, usagemodel_av_av233: "pcm_av_av_usagemodel_av_av_AbstractUserAction", usagemodel_av_av250: "pcm_av_av_usagemodel_av_av_ScenarioBehaviour", usagemodel_av_av236: "pcm_av_av_usagemodel_av_av_AbstractUserAction"):
        self.BranchTransition257 = BranchTransition257 if BranchTransition257 is not None else set()
        
    @property
    def BranchTransition257(self):
        return self.__BranchTransition257

    @BranchTransition257.setter
    def BranchTransition257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_usagemodel_av_av_Branch__BranchTransition257", None)
        self.__BranchTransition257 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "usagemodel_av_av258"):
                    opp_val = getattr(item, "usagemodel_av_av258", None)
                    
                    if opp_val == self:
                        setattr(item, "usagemodel_av_av258", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "usagemodel_av_av258"):
                    opp_val = getattr(item, "usagemodel_av_av258", None)
                    
                    setattr(item, "usagemodel_av_av258", self)
                    

    def AllBranchProbabilitiesMustSumUpTo1(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AllBranchProbabilitiesMustSumUpTo1 method
        pass

class pcm_av_av_usagemodel_av_av_Stop(AbstractUserAction):

    def __init__(self, usagemodel_av_av233: "pcm_av_av_usagemodel_av_av_AbstractUserAction", usagemodel_av_av250: "pcm_av_av_usagemodel_av_av_ScenarioBehaviour", usagemodel_av_av236: "pcm_av_av_usagemodel_av_av_AbstractUserAction"):
        
    def StopHasNoSuccessor(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement StopHasNoSuccessor method
        pass

class pcm_av_av_usagemodel_av_av_EntryLevelSystemCall(AbstractUserAction):

    def __init__(self, priority: int, pcm_av_av_usagemodel_av_av_EntryLevelSystemCall: "OperationProvidedRole" = None, pcm_av_av_usagemodel_av_av_EntryLevelSystemCall225: "OperationSignature" = None, VariableUsage227: set["VariableUsage"] = None, VariableUsage230: set["VariableUsage"] = None, usagemodel_av_av233: "pcm_av_av_usagemodel_av_av_AbstractUserAction", usagemodel_av_av250: "pcm_av_av_usagemodel_av_av_ScenarioBehaviour", usagemodel_av_av236: "pcm_av_av_usagemodel_av_av_AbstractUserAction"):
        self.priority = priority
        self.pcm_av_av_usagemodel_av_av_EntryLevelSystemCall = pcm_av_av_usagemodel_av_av_EntryLevelSystemCall
        self.pcm_av_av_usagemodel_av_av_EntryLevelSystemCall225 = pcm_av_av_usagemodel_av_av_EntryLevelSystemCall225
        self.VariableUsage227 = VariableUsage227 if VariableUsage227 is not None else set()
        self.VariableUsage230 = VariableUsage230 if VariableUsage230 is not None else set()
        
    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def VariableUsage227(self):
        return self.__VariableUsage227

    @VariableUsage227.setter
    def VariableUsage227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_usagemodel_av_av_EntryLevelSystemCall__VariableUsage227", None)
        self.__VariableUsage227 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "parameter_av_av228"):
                    opp_val = getattr(item, "parameter_av_av228", None)
                    
                    if opp_val == self:
                        setattr(item, "parameter_av_av228", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "parameter_av_av228"):
                    opp_val = getattr(item, "parameter_av_av228", None)
                    
                    setattr(item, "parameter_av_av228", self)
                    

    @property
    def VariableUsage230(self):
        return self.__VariableUsage230

    @VariableUsage230.setter
    def VariableUsage230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_usagemodel_av_av_EntryLevelSystemCall__VariableUsage230", None)
        self.__VariableUsage230 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "parameter_av_av231"):
                    opp_val = getattr(item, "parameter_av_av231", None)
                    
                    if opp_val == self:
                        setattr(item, "parameter_av_av231", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "parameter_av_av231"):
                    opp_val = getattr(item, "parameter_av_av231", None)
                    
                    setattr(item, "parameter_av_av231", self)
                    

    @property
    def pcm_av_av_usagemodel_av_av_EntryLevelSystemCall(self):
        return self.__pcm_av_av_usagemodel_av_av_EntryLevelSystemCall

    @pcm_av_av_usagemodel_av_av_EntryLevelSystemCall.setter
    def pcm_av_av_usagemodel_av_av_EntryLevelSystemCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_usagemodel_av_av_EntryLevelSystemCall__pcm_av_av_usagemodel_av_av_EntryLevelSystemCall", None)
        self.__pcm_av_av_usagemodel_av_av_EntryLevelSystemCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationProvidedRole223"):
                opp_val = getattr(old_value, "OperationProvidedRole223", None)
                if opp_val == self:
                    setattr(old_value, "OperationProvidedRole223", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationProvidedRole223"):
                opp_val = getattr(value, "OperationProvidedRole223", None)
                setattr(value, "OperationProvidedRole223", self)

    @property
    def pcm_av_av_usagemodel_av_av_EntryLevelSystemCall225(self):
        return self.__pcm_av_av_usagemodel_av_av_EntryLevelSystemCall225

    @pcm_av_av_usagemodel_av_av_EntryLevelSystemCall225.setter
    def pcm_av_av_usagemodel_av_av_EntryLevelSystemCall225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_usagemodel_av_av_EntryLevelSystemCall__pcm_av_av_usagemodel_av_av_EntryLevelSystemCall225", None)
        self.__pcm_av_av_usagemodel_av_av_EntryLevelSystemCall225 = value
        
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

    def EntryLevelSystemCallMustReferenceProvidedRoleOfASystem(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EntryLevelSystemCallMustReferenceProvidedRoleOfASystem method
        pass

    def EntryLevelSystemCallSignatureMustMatchItsProvidedRole(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EntryLevelSystemCallSignatureMustMatchItsProvidedRole method
        pass

class UserData:

    pass
class RepositoryComponent:

    pass
class pcm_av_av_repository_av_av_CompleteComponentType(RepositoryComponent):

    def __init__(self, pcm_av_av_repository_av_av_CompleteComponentType: set["ProvidesComponentType"] = None, RepositoryComponent: "pcm_av_av_composition_av_av_AssemblyContext", repository_av_av308: "pcm_av_av_repository_av_av_Repository"):
        self.pcm_av_av_repository_av_av_CompleteComponentType = pcm_av_av_repository_av_av_CompleteComponentType if pcm_av_av_repository_av_av_CompleteComponentType is not None else set()
        
    @property
    def pcm_av_av_repository_av_av_CompleteComponentType(self):
        return self.__pcm_av_av_repository_av_av_CompleteComponentType

    @pcm_av_av_repository_av_av_CompleteComponentType.setter
    def pcm_av_av_repository_av_av_CompleteComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_repository_av_av_CompleteComponentType__pcm_av_av_repository_av_av_CompleteComponentType", None)
        self.__pcm_av_av_repository_av_av_CompleteComponentType = value if value is not None else set()
        
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
                    

    def providedInterfacesHaveToConformToProvidedType2(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement providedInterfacesHaveToConformToProvidedType2 method
        pass

    def AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType method
        pass

class pcm_av_av_repository_av_av_ProvidesComponentType(RepositoryComponent):

    def __init__(self, RepositoryComponent: "pcm_av_av_composition_av_av_AssemblyContext", repository_av_av308: "pcm_av_av_repository_av_av_Repository"):
        
    def AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType method
        pass

class pcm_av_av_repository_av_av_ImplementationComponentType(RepositoryComponent):

    def __init__(self, componentType: str, pcm_av_av_repository_av_av_ImplementationComponentType: set["CompleteComponentType"] = None, pcm_av_av_repository_av_av_ImplementationComponentType287: set["VariableUsage"] = None, RepositoryComponent: "pcm_av_av_composition_av_av_AssemblyContext", repository_av_av308: "pcm_av_av_repository_av_av_Repository"):
        self.componentType = componentType
        self.pcm_av_av_repository_av_av_ImplementationComponentType = pcm_av_av_repository_av_av_ImplementationComponentType if pcm_av_av_repository_av_av_ImplementationComponentType is not None else set()
        self.pcm_av_av_repository_av_av_ImplementationComponentType287 = pcm_av_av_repository_av_av_ImplementationComponentType287 if pcm_av_av_repository_av_av_ImplementationComponentType287 is not None else set()
        
    @property
    def componentType(self) -> str:
        return self.__componentType

    @componentType.setter
    def componentType(self, componentType: str):
        self.__componentType = componentType

    @property
    def pcm_av_av_repository_av_av_ImplementationComponentType287(self):
        return self.__pcm_av_av_repository_av_av_ImplementationComponentType287

    @pcm_av_av_repository_av_av_ImplementationComponentType287.setter
    def pcm_av_av_repository_av_av_ImplementationComponentType287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_repository_av_av_ImplementationComponentType__pcm_av_av_repository_av_av_ImplementationComponentType287", None)
        self.__pcm_av_av_repository_av_av_ImplementationComponentType287 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableUsage288"):
                    opp_val = getattr(item, "VariableUsage288", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableUsage288", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableUsage288"):
                    opp_val = getattr(item, "VariableUsage288", None)
                    
                    setattr(item, "VariableUsage288", self)
                    

    @property
    def pcm_av_av_repository_av_av_ImplementationComponentType(self):
        return self.__pcm_av_av_repository_av_av_ImplementationComponentType

    @pcm_av_av_repository_av_av_ImplementationComponentType.setter
    def pcm_av_av_repository_av_av_ImplementationComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_repository_av_av_ImplementationComponentType__pcm_av_av_repository_av_av_ImplementationComponentType", None)
        self.__pcm_av_av_repository_av_av_ImplementationComponentType = value if value is not None else set()
        
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
                    

    def RequiredInterfacesHaveToConformToCompleteType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RequiredInterfacesHaveToConformToCompleteType method
        pass

    def ProvidedInterfaceHaveToConformToComponentType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ProvidedInterfaceHaveToConformToComponentType method
        pass

    def providedInterfacesHaveToConformToCompleteType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement providedInterfacesHaveToConformToCompleteType method
        pass

class pcm_av_av_usagemodel_av_av_UsageModel:

    pass
class pcm_av_av_usagemodel_av_av_UserData:

    pass
class Workload:

    pass
class pcm_av_av_usagemodel_av_av_OpenWorkload(Workload):

    def __init__(self, PCMRandomVariable266: "PCMRandomVariable" = None, usagemodel_av_av208: "pcm_av_av_usagemodel_av_av_UsageScenario"):
        self.PCMRandomVariable266 = PCMRandomVariable266
        
    @property
    def PCMRandomVariable266(self):
        return self.__PCMRandomVariable266

    @PCMRandomVariable266.setter
    def PCMRandomVariable266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_usagemodel_av_av_OpenWorkload__PCMRandomVariable266", None)
        self.__PCMRandomVariable266 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av_av267"):
                opp_val = getattr(old_value, "core_av_av267", None)
                if opp_val == self:
                    setattr(old_value, "core_av_av267", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av_av267"):
                opp_val = getattr(value, "core_av_av267", None)
                setattr(value, "core_av_av267", self)

    def InterArrivalTimeInOpenWorkloadNeedsToBeSpecified(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement InterArrivalTimeInOpenWorkloadNeedsToBeSpecified method
        pass

class pcm_av_av_usagemodel_av_av_ClosedWorkload(Workload):

    def __init__(self, population: int, PCMRandomVariable272: "PCMRandomVariable" = None, usagemodel_av_av208: "pcm_av_av_usagemodel_av_av_UsageScenario"):
        self.population = population
        self.PCMRandomVariable272 = PCMRandomVariable272
        
    @property
    def population(self) -> int:
        return self.__population

    @population.setter
    def population(self, population: int):
        self.__population = population

    @property
    def PCMRandomVariable272(self):
        return self.__PCMRandomVariable272

    @PCMRandomVariable272.setter
    def PCMRandomVariable272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_usagemodel_av_av_ClosedWorkload__PCMRandomVariable272", None)
        self.__PCMRandomVariable272 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av_av273"):
                opp_val = getattr(old_value, "core_av_av273", None)
                if opp_val == self:
                    setattr(old_value, "core_av_av273", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av_av273"):
                opp_val = getattr(value, "core_av_av273", None)
                setattr(value, "core_av_av273", self)

    def PopulationInClosedWorkloadNeedsToBeSpecified(self, context: str, diagnostics: str) -> bool:
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
class pcm_av_av_usagemodel_av_av_Workload:

    pass
class VariableUsage:

    pass
class InfrastructureRequiredRole:

    pass
class InfrastructureProvidedRole:

    pass
class OperationRequiredRole:

    pass
class DelegationConnector:

    pass
class pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector(DelegationConnector):

    pass
class pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector(DelegationConnector):

    pass
class pcm_av_av_composition_av_av_SinkDelegationConnector(DelegationConnector):

    pass
class pcm_av_av_composition_av_av_SourceDelegationConnector(DelegationConnector):

    pass
class pcm_av_av_composition_av_av_RequiredResourceDelegationConnector(DelegationConnector):

    pass
class pcm_av_av_composition_av_av_ProvidedDelegationConnector(DelegationConnector):

    def __init__(self, pcm_av_av_composition_av_av_ProvidedDelegationConnector: "OperationProvidedRole" = None, pcm_av_av_composition_av_av_ProvidedDelegationConnector109: "OperationProvidedRole" = None, pcm_av_av_composition_av_av_ProvidedDelegationConnector112: "composition_av_av_AssemblyContext" = None):
        self.pcm_av_av_composition_av_av_ProvidedDelegationConnector = pcm_av_av_composition_av_av_ProvidedDelegationConnector
        self.pcm_av_av_composition_av_av_ProvidedDelegationConnector109 = pcm_av_av_composition_av_av_ProvidedDelegationConnector109
        self.pcm_av_av_composition_av_av_ProvidedDelegationConnector112 = pcm_av_av_composition_av_av_ProvidedDelegationConnector112
        
    @property
    def pcm_av_av_composition_av_av_ProvidedDelegationConnector109(self):
        return self.__pcm_av_av_composition_av_av_ProvidedDelegationConnector109

    @pcm_av_av_composition_av_av_ProvidedDelegationConnector109.setter
    def pcm_av_av_composition_av_av_ProvidedDelegationConnector109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_composition_av_av_ProvidedDelegationConnector__pcm_av_av_composition_av_av_ProvidedDelegationConnector109", None)
        self.__pcm_av_av_composition_av_av_ProvidedDelegationConnector109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationProvidedRole110"):
                opp_val = getattr(old_value, "OperationProvidedRole110", None)
                if opp_val == self:
                    setattr(old_value, "OperationProvidedRole110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationProvidedRole110"):
                opp_val = getattr(value, "OperationProvidedRole110", None)
                setattr(value, "OperationProvidedRole110", self)

    @property
    def pcm_av_av_composition_av_av_ProvidedDelegationConnector(self):
        return self.__pcm_av_av_composition_av_av_ProvidedDelegationConnector

    @pcm_av_av_composition_av_av_ProvidedDelegationConnector.setter
    def pcm_av_av_composition_av_av_ProvidedDelegationConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_composition_av_av_ProvidedDelegationConnector__pcm_av_av_composition_av_av_ProvidedDelegationConnector", None)
        self.__pcm_av_av_composition_av_av_ProvidedDelegationConnector = value
        
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
    def pcm_av_av_composition_av_av_ProvidedDelegationConnector112(self):
        return self.__pcm_av_av_composition_av_av_ProvidedDelegationConnector112

    @pcm_av_av_composition_av_av_ProvidedDelegationConnector112.setter
    def pcm_av_av_composition_av_av_ProvidedDelegationConnector112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_composition_av_av_ProvidedDelegationConnector__pcm_av_av_composition_av_av_ProvidedDelegationConnector112", None)
        self.__pcm_av_av_composition_av_av_ProvidedDelegationConnector112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_av_AssemblyContext113"):
                opp_val = getattr(old_value, "composition_av_av_AssemblyContext113", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_av_AssemblyContext113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_av_AssemblyContext113"):
                opp_val = getattr(value, "composition_av_av_AssemblyContext113", None)
                setattr(value, "composition_av_av_AssemblyContext113", self)

    def ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame method
        pass

    def ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

class PCMRandomVariable:

    pass
class SinkRole:

    pass
class pcm_av_av_composition_av_av_RequiredDelegationConnector(DelegationConnector):

    def __init__(self, pcm_av_av_composition_av_av_RequiredDelegationConnector: "OperationRequiredRole" = None, pcm_av_av_composition_av_av_RequiredDelegationConnector116: "OperationRequiredRole" = None, pcm_av_av_composition_av_av_RequiredDelegationConnector119: "composition_av_av_AssemblyContext" = None):
        self.pcm_av_av_composition_av_av_RequiredDelegationConnector = pcm_av_av_composition_av_av_RequiredDelegationConnector
        self.pcm_av_av_composition_av_av_RequiredDelegationConnector116 = pcm_av_av_composition_av_av_RequiredDelegationConnector116
        self.pcm_av_av_composition_av_av_RequiredDelegationConnector119 = pcm_av_av_composition_av_av_RequiredDelegationConnector119
        
    @property
    def pcm_av_av_composition_av_av_RequiredDelegationConnector(self):
        return self.__pcm_av_av_composition_av_av_RequiredDelegationConnector

    @pcm_av_av_composition_av_av_RequiredDelegationConnector.setter
    def pcm_av_av_composition_av_av_RequiredDelegationConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_composition_av_av_RequiredDelegationConnector__pcm_av_av_composition_av_av_RequiredDelegationConnector", None)
        self.__pcm_av_av_composition_av_av_RequiredDelegationConnector = value
        
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

    @property
    def pcm_av_av_composition_av_av_RequiredDelegationConnector116(self):
        return self.__pcm_av_av_composition_av_av_RequiredDelegationConnector116

    @pcm_av_av_composition_av_av_RequiredDelegationConnector116.setter
    def pcm_av_av_composition_av_av_RequiredDelegationConnector116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_composition_av_av_RequiredDelegationConnector__pcm_av_av_composition_av_av_RequiredDelegationConnector116", None)
        self.__pcm_av_av_composition_av_av_RequiredDelegationConnector116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationRequiredRole117"):
                opp_val = getattr(old_value, "OperationRequiredRole117", None)
                if opp_val == self:
                    setattr(old_value, "OperationRequiredRole117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationRequiredRole117"):
                opp_val = getattr(value, "OperationRequiredRole117", None)
                setattr(value, "OperationRequiredRole117", self)

    @property
    def pcm_av_av_composition_av_av_RequiredDelegationConnector119(self):
        return self.__pcm_av_av_composition_av_av_RequiredDelegationConnector119

    @pcm_av_av_composition_av_av_RequiredDelegationConnector119.setter
    def pcm_av_av_composition_av_av_RequiredDelegationConnector119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_composition_av_av_RequiredDelegationConnector__pcm_av_av_composition_av_av_RequiredDelegationConnector119", None)
        self.__pcm_av_av_composition_av_av_RequiredDelegationConnector119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_av_AssemblyContext120"):
                opp_val = getattr(old_value, "composition_av_av_AssemblyContext120", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_av_AssemblyContext120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_av_AssemblyContext120"):
                opp_val = getattr(value, "composition_av_av_AssemblyContext120", None)
                setattr(value, "composition_av_av_AssemblyContext120", self)

    def RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

    def RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector method
        pass

    def ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame method
        pass

class OperationProvidedRole:

    pass
class composition_av_av_Connector:

    pass
class SourceRole:

    pass
class composition_av_av_EventChannelSourceConnector:

    pass
class EventGroup:

    pass
class pcm_av_av_composition_av_av_ResourceRequiredDelegationConnector:

    pass
class entity_av_av_NamedElement:

    pass
class Identifier:

    pass
class pcm_av_av_seff_av_av_ResourceDemandingBehaviour(Identifier):

    def __init__(self, AbstractLoopAction: "AbstractLoopAction" = None, AbstractBranchTransition: "AbstractBranchTransition" = None, AbstractAction486: set["AbstractAction"] = None):
        self.AbstractLoopAction = AbstractLoopAction
        self.AbstractBranchTransition = AbstractBranchTransition
        self.AbstractAction486 = AbstractAction486 if AbstractAction486 is not None else set()
        
    @property
    def AbstractAction486(self):
        return self.__AbstractAction486

    @AbstractAction486.setter
    def AbstractAction486(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_seff_av_av_ResourceDemandingBehaviour__AbstractAction486", None)
        self.__AbstractAction486 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_av_av487"):
                    opp_val = getattr(item, "seff_av_av487", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_av_av487", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_av_av487"):
                    opp_val = getattr(item, "seff_av_av487", None)
                    
                    setattr(item, "seff_av_av487", self)
                    

    @property
    def AbstractBranchTransition(self):
        return self.__AbstractBranchTransition

    @AbstractBranchTransition.setter
    def AbstractBranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_seff_av_av_ResourceDemandingBehaviour__AbstractBranchTransition", None)
        self.__AbstractBranchTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av_av484"):
                opp_val = getattr(old_value, "seff_av_av484", None)
                if opp_val == self:
                    setattr(old_value, "seff_av_av484", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av_av484"):
                opp_val = getattr(value, "seff_av_av484", None)
                setattr(value, "seff_av_av484", self)

    @property
    def AbstractLoopAction(self):
        return self.__AbstractLoopAction

    @AbstractLoopAction.setter
    def AbstractLoopAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_seff_av_av_ResourceDemandingBehaviour__AbstractLoopAction", None)
        self.__AbstractLoopAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av_av482"):
                opp_val = getattr(old_value, "seff_av_av482", None)
                if opp_val == self:
                    setattr(old_value, "seff_av_av482", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av_av482"):
                opp_val = getattr(value, "seff_av_av482", None)
                setattr(value, "seff_av_av482", self)

    def EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor method
        pass

    def ExactlyOneStartAction(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ExactlyOneStartAction method
        pass

    def ExactlyOneStopAction(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ExactlyOneStopAction method
        pass

class pcm_av_av_seff_av_av_ResourceDemandingSEFF(Identifier, seff_av_av_ResourceDemandingBehaviour, seff_av_av_ServiceEffectSpecification):

    pass
class pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification(Identifier):

    def __init__(self, MTTR: float, MTTF: float, requiredByContainer: bool, numberOfReplicas: int, ResourceContainer666: "ResourceContainer" = None, pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification: "SchedulingPolicy" = None, pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification660: "ProcessingResourceType" = None, PCMRandomVariable663: "PCMRandomVariable" = None):
        self.MTTR = MTTR
        self.MTTF = MTTF
        self.requiredByContainer = requiredByContainer
        self.numberOfReplicas = numberOfReplicas
        self.ResourceContainer666 = ResourceContainer666
        self.pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification = pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification
        self.pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification660 = pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification660
        self.PCMRandomVariable663 = PCMRandomVariable663
        
    @property
    def MTTR(self) -> float:
        return self.__MTTR

    @MTTR.setter
    def MTTR(self, MTTR: float):
        self.__MTTR = MTTR

    @property
    def numberOfReplicas(self) -> int:
        return self.__numberOfReplicas

    @numberOfReplicas.setter
    def numberOfReplicas(self, numberOfReplicas: int):
        self.__numberOfReplicas = numberOfReplicas

    @property
    def requiredByContainer(self) -> bool:
        return self.__requiredByContainer

    @requiredByContainer.setter
    def requiredByContainer(self, requiredByContainer: bool):
        self.__requiredByContainer = requiredByContainer

    @property
    def MTTF(self) -> float:
        return self.__MTTF

    @MTTF.setter
    def MTTF(self, MTTF: float):
        self.__MTTF = MTTF

    @property
    def PCMRandomVariable663(self):
        return self.__PCMRandomVariable663

    @PCMRandomVariable663.setter
    def PCMRandomVariable663(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification__PCMRandomVariable663", None)
        self.__PCMRandomVariable663 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av_av664"):
                opp_val = getattr(old_value, "core_av_av664", None)
                if opp_val == self:
                    setattr(old_value, "core_av_av664", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av_av664"):
                opp_val = getattr(value, "core_av_av664", None)
                setattr(value, "core_av_av664", self)

    @property
    def ResourceContainer666(self):
        return self.__ResourceContainer666

    @ResourceContainer666.setter
    def ResourceContainer666(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification__ResourceContainer666", None)
        self.__ResourceContainer666 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_av_av667"):
                opp_val = getattr(old_value, "resourceenvironment_av_av667", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_av_av667", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_av_av667"):
                opp_val = getattr(value, "resourceenvironment_av_av667", None)
                setattr(value, "resourceenvironment_av_av667", self)

    @property
    def pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification660(self):
        return self.__pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification660

    @pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification660.setter
    def pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification660(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification__pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification660", None)
        self.__pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification660 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcessingResourceType661"):
                opp_val = getattr(old_value, "ProcessingResourceType661", None)
                if opp_val == self:
                    setattr(old_value, "ProcessingResourceType661", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessingResourceType661"):
                opp_val = getattr(value, "ProcessingResourceType661", None)
                setattr(value, "ProcessingResourceType661", self)

    @property
    def pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification(self):
        return self.__pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification

    @pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification.setter
    def pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification__pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification", None)
        self.__pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SchedulingPolicy658"):
                opp_val = getattr(old_value, "SchedulingPolicy658", None)
                if opp_val == self:
                    setattr(old_value, "SchedulingPolicy658", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SchedulingPolicy658"):
                opp_val = getattr(value, "SchedulingPolicy658", None)
                setattr(value, "SchedulingPolicy658", self)

class pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification(Identifier):

    def __init__(self, failureProbability: float, LinkingResource669: "LinkingResource" = None, pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification: "CommunicationLinkResourceType" = None, PCMRandomVariable674: "PCMRandomVariable" = None, PCMRandomVariable677: "PCMRandomVariable" = None):
        self.failureProbability = failureProbability
        self.LinkingResource669 = LinkingResource669
        self.pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification = pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification
        self.PCMRandomVariable674 = PCMRandomVariable674
        self.PCMRandomVariable677 = PCMRandomVariable677
        
    @property
    def failureProbability(self) -> float:
        return self.__failureProbability

    @failureProbability.setter
    def failureProbability(self, failureProbability: float):
        self.__failureProbability = failureProbability

    @property
    def PCMRandomVariable674(self):
        return self.__PCMRandomVariable674

    @PCMRandomVariable674.setter
    def PCMRandomVariable674(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification__PCMRandomVariable674", None)
        self.__PCMRandomVariable674 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av_av675"):
                opp_val = getattr(old_value, "core_av_av675", None)
                if opp_val == self:
                    setattr(old_value, "core_av_av675", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av_av675"):
                opp_val = getattr(value, "core_av_av675", None)
                setattr(value, "core_av_av675", self)

    @property
    def PCMRandomVariable677(self):
        return self.__PCMRandomVariable677

    @PCMRandomVariable677.setter
    def PCMRandomVariable677(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification__PCMRandomVariable677", None)
        self.__PCMRandomVariable677 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av_av678"):
                opp_val = getattr(old_value, "core_av_av678", None)
                if opp_val == self:
                    setattr(old_value, "core_av_av678", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av_av678"):
                opp_val = getattr(value, "core_av_av678", None)
                setattr(value, "core_av_av678", self)

    @property
    def pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification(self):
        return self.__pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification

    @pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification.setter
    def pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification__pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification", None)
        self.__pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CommunicationLinkResourceType672"):
                opp_val = getattr(old_value, "CommunicationLinkResourceType672", None)
                if opp_val == self:
                    setattr(old_value, "CommunicationLinkResourceType672", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CommunicationLinkResourceType672"):
                opp_val = getattr(value, "CommunicationLinkResourceType672", None)
                setattr(value, "CommunicationLinkResourceType672", self)

    @property
    def LinkingResource669(self):
        return self.__LinkingResource669

    @LinkingResource669.setter
    def LinkingResource669(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification__LinkingResource669", None)
        self.__LinkingResource669 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_av_av670"):
                opp_val = getattr(old_value, "resourceenvironment_av_av670", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_av_av670", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_av_av670"):
                opp_val = getattr(value, "resourceenvironment_av_av670", None)
                setattr(value, "resourceenvironment_av_av670", self)

class pcm_av_av_entity_av_av_Entity(Identifier, entity_av_av_NamedElement):

    pass
class pcm_av_av_entity_av_av_NamedElement:

    def __init__(self, entityName: str):
        self.entityName = entityName
        
    @property
    def entityName(self) -> str:
        return self.__entityName

    @entityName.setter
    def entityName(self, entityName: str):
        self.__entityName = entityName

class entity_av_av_InterfaceProvidingRequiringEntity:

    pass
class composition_av_av_ComposedStructure:

    pass
class pcm_av_av_entity_av_av_ComposedProvidingRequiringEntity(entity_av_av_InterfaceProvidingRequiringEntity, composition_av_av_ComposedStructure):

    def __init__(self, core_av_av91: "pcm_av_av_composition_av_av_EventChannel", core_av_av197: "pcm_av_av_composition_av_av_AssemblyContext", core_av_av81: "pcm_av_av_composition_av_av_ResourceRequiredDelegationConnector", core_av_av62: "pcm_av_av_composition_av_av_Connector"):
        
    def ProvidedRolesMustBeBound(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ProvidedRolesMustBeBound method
        pass

class composition_av_av_EventChannel:

    pass
class composition_av_av_ResourceRequiredDelegationConnector:

    pass
class composition_av_av_AssemblyContext:

    pass
class Connector:

    pass
class pcm_av_av_composition_av_av_EventChannelSourceConnector(Connector):

    pass
class pcm_av_av_composition_av_av_EventChannelSinkConnector(Connector):

    pass
class pcm_av_av_composition_av_av_AssemblyEventConnector(Connector):

    pass
class pcm_av_av_composition_av_av_AssemblyInfrastructureConnector(Connector):

    pass
class pcm_av_av_composition_av_av_AssemblyConnector(Connector):

    def __init__(self, pcm_av_av_composition_av_av_AssemblyConnector: "composition_av_av_AssemblyContext" = None, pcm_av_av_composition_av_av_AssemblyConnector124: "composition_av_av_AssemblyContext" = None, pcm_av_av_composition_av_av_AssemblyConnector127: "OperationProvidedRole" = None, pcm_av_av_composition_av_av_AssemblyConnector130: "OperationRequiredRole" = None):
        self.pcm_av_av_composition_av_av_AssemblyConnector = pcm_av_av_composition_av_av_AssemblyConnector
        self.pcm_av_av_composition_av_av_AssemblyConnector124 = pcm_av_av_composition_av_av_AssemblyConnector124
        self.pcm_av_av_composition_av_av_AssemblyConnector127 = pcm_av_av_composition_av_av_AssemblyConnector127
        self.pcm_av_av_composition_av_av_AssemblyConnector130 = pcm_av_av_composition_av_av_AssemblyConnector130
        
    @property
    def pcm_av_av_composition_av_av_AssemblyConnector127(self):
        return self.__pcm_av_av_composition_av_av_AssemblyConnector127

    @pcm_av_av_composition_av_av_AssemblyConnector127.setter
    def pcm_av_av_composition_av_av_AssemblyConnector127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_composition_av_av_AssemblyConnector__pcm_av_av_composition_av_av_AssemblyConnector127", None)
        self.__pcm_av_av_composition_av_av_AssemblyConnector127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationProvidedRole128"):
                opp_val = getattr(old_value, "OperationProvidedRole128", None)
                if opp_val == self:
                    setattr(old_value, "OperationProvidedRole128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationProvidedRole128"):
                opp_val = getattr(value, "OperationProvidedRole128", None)
                setattr(value, "OperationProvidedRole128", self)

    @property
    def pcm_av_av_composition_av_av_AssemblyConnector130(self):
        return self.__pcm_av_av_composition_av_av_AssemblyConnector130

    @pcm_av_av_composition_av_av_AssemblyConnector130.setter
    def pcm_av_av_composition_av_av_AssemblyConnector130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_composition_av_av_AssemblyConnector__pcm_av_av_composition_av_av_AssemblyConnector130", None)
        self.__pcm_av_av_composition_av_av_AssemblyConnector130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationRequiredRole131"):
                opp_val = getattr(old_value, "OperationRequiredRole131", None)
                if opp_val == self:
                    setattr(old_value, "OperationRequiredRole131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationRequiredRole131"):
                opp_val = getattr(value, "OperationRequiredRole131", None)
                setattr(value, "OperationRequiredRole131", self)

    @property
    def pcm_av_av_composition_av_av_AssemblyConnector(self):
        return self.__pcm_av_av_composition_av_av_AssemblyConnector

    @pcm_av_av_composition_av_av_AssemblyConnector.setter
    def pcm_av_av_composition_av_av_AssemblyConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_composition_av_av_AssemblyConnector__pcm_av_av_composition_av_av_AssemblyConnector", None)
        self.__pcm_av_av_composition_av_av_AssemblyConnector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_av_AssemblyContext122"):
                opp_val = getattr(old_value, "composition_av_av_AssemblyContext122", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_av_AssemblyContext122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_av_AssemblyContext122"):
                opp_val = getattr(value, "composition_av_av_AssemblyContext122", None)
                setattr(value, "composition_av_av_AssemblyContext122", self)

    @property
    def pcm_av_av_composition_av_av_AssemblyConnector124(self):
        return self.__pcm_av_av_composition_av_av_AssemblyConnector124

    @pcm_av_av_composition_av_av_AssemblyConnector124.setter
    def pcm_av_av_composition_av_av_AssemblyConnector124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_composition_av_av_AssemblyConnector__pcm_av_av_composition_av_av_AssemblyConnector124", None)
        self.__pcm_av_av_composition_av_av_AssemblyConnector124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_av_AssemblyContext125"):
                opp_val = getattr(old_value, "composition_av_av_AssemblyContext125", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_av_AssemblyContext125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_av_AssemblyContext125"):
                opp_val = getattr(value, "composition_av_av_AssemblyContext125", None)
                setattr(value, "composition_av_av_AssemblyContext125", self)

    def AssemblyConnectorsReferencedInterfacesMustMatch(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AssemblyConnectorsReferencedInterfacesMustMatch method
        pass

    def AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch method
        pass

    def AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch method
        pass

class pcm_av_av_composition_av_av_DelegationConnector(Connector):

    pass
class entity_av_av_ResourceInterfaceProvidingEntity:

    pass
class Role:

    pass
class pcm_av_av_repository_av_av_ProvidedRole(Role):

    pass
class pcm_av_av_repository_av_av_RequiredRole(Role):

    pass
class pcm_av_av_entity_av_av_ResourceProvidedRole(Role):

    pass
class ProcessingResourceSpecification:

    pass
class CommunicationLinkResourceSpecification:

    pass
class Delay:

    pass
class entity_av_av_ResourceProvidedRole:

    pass
class pcm_av_av_entity_av_av_ResourceRequiredRole(Role):

    pass
class entity_av_av_ResourceRequiredRole:

    pass
class RequiredRole:

    pass
class pcm_av_av_repository_av_av_InfrastructureRequiredRole(RequiredRole):

    pass
class pcm_av_av_repository_av_av_OperationRequiredRole(RequiredRole):

    pass
class pcm_av_av_repository_av_av_SourceRole(RequiredRole):

    pass
class entity_av_av_ResourceInterfaceRequiringEntity:

    pass
class pcm_av_av_entity_av_av_ResourceInterfaceProvidingRequiringEntity(entity_av_av_ResourceInterfaceRequiringEntity, entity_av_av_ResourceInterfaceProvidingEntity):

    pass
class entity_av_av_Entity:

    pass
class pcm_av_av_repository_av_av_CollectionDataType(repository_av_av_DataType, entity_av_av_Entity):

    pass
class pcm_av_av_resourcetype_av_av_ResourceType(entity_av_av_Entity, entity_av_av_ResourceInterfaceProvidingEntity, UnitCarryingElement):

    pass
class pcm_av_av_system_av_av_System(entity_av_av_ComposedProvidingRequiringEntity, entity_av_av_Entity):

    def __init__(self, QoSAnnotations632: set["QoSAnnotations"] = None):
        self.QoSAnnotations632 = QoSAnnotations632 if QoSAnnotations632 is not None else set()
        
    @property
    def QoSAnnotations632(self):
        return self.__QoSAnnotations632

    @QoSAnnotations632.setter
    def QoSAnnotations632(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_system_av_av_System__QoSAnnotations632", None)
        self.__QoSAnnotations632 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qosannotations_av_av633"):
                    opp_val = getattr(item, "qosannotations_av_av633", None)
                    
                    if opp_val == self:
                        setattr(item, "qosannotations_av_av633", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qosannotations_av_av633"):
                    opp_val = getattr(item, "qosannotations_av_av633", None)
                    
                    setattr(item, "qosannotations_av_av633", self)
                    

    def SystemMustHaveAtLeastOneProvidedRole(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SystemMustHaveAtLeastOneProvidedRole method
        pass

class pcm_av_av_repository_av_av_CompositeDataType(repository_av_av_DataType, entity_av_av_Entity):

    pass
class pcm_av_av_entity_av_av_InterfaceRequiringEntity(entity_av_av_ResourceInterfaceRequiringEntity, entity_av_av_Entity):

    pass
class ProvidedRole:

    pass
class pcm_av_av_repository_av_av_SinkRole(ProvidedRole):

    pass
class pcm_av_av_repository_av_av_InfrastructureProvidedRole(ProvidedRole):

    pass
class pcm_av_av_repository_av_av_OperationProvidedRole(ProvidedRole):

    pass
class Entity:

    pass
class pcm_av_av_resourcetype_av_av_SchedulingPolicy(Entity):

    pass
class pcm_av_av_usagemodel_av_av_AbstractUserAction(Entity):

    pass
class pcm_av_av_resourcetype_av_av_ResourceSignature(Entity):

    def __init__(self, resourceServiceId: int, Parameter387: "Parameter" = None, ResourceInterface390: "ResourceInterface" = None):
        self.resourceServiceId = resourceServiceId
        self.Parameter387 = Parameter387
        self.ResourceInterface390 = ResourceInterface390
        
    @property
    def resourceServiceId(self) -> int:
        return self.__resourceServiceId

    @resourceServiceId.setter
    def resourceServiceId(self, resourceServiceId: int):
        self.__resourceServiceId = resourceServiceId

    @property
    def ResourceInterface390(self):
        return self.__ResourceInterface390

    @ResourceInterface390.setter
    def ResourceInterface390(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_resourcetype_av_av_ResourceSignature__ResourceInterface390", None)
        self.__ResourceInterface390 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcetype_av_av391"):
                opp_val = getattr(old_value, "resourcetype_av_av391", None)
                if opp_val == self:
                    setattr(old_value, "resourcetype_av_av391", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcetype_av_av391"):
                opp_val = getattr(value, "resourcetype_av_av391", None)
                setattr(value, "resourcetype_av_av391", self)

    @property
    def Parameter387(self):
        return self.__Parameter387

    @Parameter387.setter
    def Parameter387(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_resourcetype_av_av_ResourceSignature__Parameter387", None)
        self.__Parameter387 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av_av388"):
                opp_val = getattr(old_value, "repository_av_av388", None)
                if opp_val == self:
                    setattr(old_value, "repository_av_av388", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av_av388"):
                opp_val = getattr(value, "repository_av_av388", None)
                setattr(value, "repository_av_av388", self)

class pcm_av_av_entity_av_av_ResourceInterfaceProvidingEntity(Entity):

    pass
class pcm_av_av_allocation_av_av_AllocationContext(Entity):

    def __init__(self, pcm_av_av_allocation_av_av_AllocationContext: "ResourceContainer" = None, pcm_av_av_allocation_av_av_AllocationContext682: "composition_av_av_AssemblyContext" = None, Allocation: "Allocation" = None, pcm_av_av_allocation_av_av_AllocationContext686: "composition_av_av_EventChannel" = None):
        self.pcm_av_av_allocation_av_av_AllocationContext = pcm_av_av_allocation_av_av_AllocationContext
        self.pcm_av_av_allocation_av_av_AllocationContext682 = pcm_av_av_allocation_av_av_AllocationContext682
        self.Allocation = Allocation
        self.pcm_av_av_allocation_av_av_AllocationContext686 = pcm_av_av_allocation_av_av_AllocationContext686
        
    @property
    def pcm_av_av_allocation_av_av_AllocationContext(self):
        return self.__pcm_av_av_allocation_av_av_AllocationContext

    @pcm_av_av_allocation_av_av_AllocationContext.setter
    def pcm_av_av_allocation_av_av_AllocationContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_allocation_av_av_AllocationContext__pcm_av_av_allocation_av_av_AllocationContext", None)
        self.__pcm_av_av_allocation_av_av_AllocationContext = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceContainer680"):
                opp_val = getattr(old_value, "ResourceContainer680", None)
                if opp_val == self:
                    setattr(old_value, "ResourceContainer680", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceContainer680"):
                opp_val = getattr(value, "ResourceContainer680", None)
                setattr(value, "ResourceContainer680", self)

    @property
    def pcm_av_av_allocation_av_av_AllocationContext686(self):
        return self.__pcm_av_av_allocation_av_av_AllocationContext686

    @pcm_av_av_allocation_av_av_AllocationContext686.setter
    def pcm_av_av_allocation_av_av_AllocationContext686(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_allocation_av_av_AllocationContext__pcm_av_av_allocation_av_av_AllocationContext686", None)
        self.__pcm_av_av_allocation_av_av_AllocationContext686 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_av_EventChannel"):
                opp_val = getattr(old_value, "composition_av_av_EventChannel", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_av_EventChannel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_av_EventChannel"):
                opp_val = getattr(value, "composition_av_av_EventChannel", None)
                setattr(value, "composition_av_av_EventChannel", self)

    @property
    def Allocation(self):
        return self.__Allocation

    @Allocation.setter
    def Allocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_allocation_av_av_AllocationContext__Allocation", None)
        self.__Allocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "allocation_av_av"):
                opp_val = getattr(old_value, "allocation_av_av", None)
                if opp_val == self:
                    setattr(old_value, "allocation_av_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "allocation_av_av"):
                opp_val = getattr(value, "allocation_av_av", None)
                setattr(value, "allocation_av_av", self)

    @property
    def pcm_av_av_allocation_av_av_AllocationContext682(self):
        return self.__pcm_av_av_allocation_av_av_AllocationContext682

    @pcm_av_av_allocation_av_av_AllocationContext682.setter
    def pcm_av_av_allocation_av_av_AllocationContext682(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_allocation_av_av_AllocationContext__pcm_av_av_allocation_av_av_AllocationContext682", None)
        self.__pcm_av_av_allocation_av_av_AllocationContext682 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_av_AssemblyContext683"):
                opp_val = getattr(old_value, "composition_av_av_AssemblyContext683", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_av_AssemblyContext683", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_av_AssemblyContext683"):
                opp_val = getattr(value, "composition_av_av_AssemblyContext683", None)
                setattr(value, "composition_av_av_AssemblyContext683", self)

    def OneAssemblyContextOrOneEventChannelShouldBeReferred(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement OneAssemblyContextOrOneEventChannelShouldBeReferred method
        pass

class pcm_av_av_usagemodel_av_av_ScenarioBehaviour(Entity):

    def __init__(self, UsageScenario241: "UsageScenario" = None, BranchTransition: "BranchTransition" = None, Loop246: "Loop" = None, AbstractUserAction249: set["AbstractUserAction"] = None):
        self.UsageScenario241 = UsageScenario241
        self.BranchTransition = BranchTransition
        self.Loop246 = Loop246
        self.AbstractUserAction249 = AbstractUserAction249 if AbstractUserAction249 is not None else set()
        
    @property
    def BranchTransition(self):
        return self.__BranchTransition

    @BranchTransition.setter
    def BranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_usagemodel_av_av_ScenarioBehaviour__BranchTransition", None)
        self.__BranchTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av_av244"):
                opp_val = getattr(old_value, "usagemodel_av_av244", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av_av244", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av_av244"):
                opp_val = getattr(value, "usagemodel_av_av244", None)
                setattr(value, "usagemodel_av_av244", self)

    @property
    def AbstractUserAction249(self):
        return self.__AbstractUserAction249

    @AbstractUserAction249.setter
    def AbstractUserAction249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_usagemodel_av_av_ScenarioBehaviour__AbstractUserAction249", None)
        self.__AbstractUserAction249 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "usagemodel_av_av250"):
                    opp_val = getattr(item, "usagemodel_av_av250", None)
                    
                    if opp_val == self:
                        setattr(item, "usagemodel_av_av250", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "usagemodel_av_av250"):
                    opp_val = getattr(item, "usagemodel_av_av250", None)
                    
                    setattr(item, "usagemodel_av_av250", self)
                    

    @property
    def UsageScenario241(self):
        return self.__UsageScenario241

    @UsageScenario241.setter
    def UsageScenario241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_usagemodel_av_av_ScenarioBehaviour__UsageScenario241", None)
        self.__UsageScenario241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av_av242"):
                opp_val = getattr(old_value, "usagemodel_av_av242", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av_av242", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av_av242"):
                opp_val = getattr(value, "usagemodel_av_av242", None)
                setattr(value, "usagemodel_av_av242", self)

    @property
    def Loop246(self):
        return self.__Loop246

    @Loop246.setter
    def Loop246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_usagemodel_av_av_ScenarioBehaviour__Loop246", None)
        self.__Loop246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av_av247"):
                opp_val = getattr(old_value, "usagemodel_av_av247", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av_av247", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av_av247"):
                opp_val = getattr(value, "usagemodel_av_av247", None)
                setattr(value, "usagemodel_av_av247", self)

    def Exactlyonestop(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement Exactlyonestop method
        pass

    def Exactlyonestart(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement Exactlyonestart method
        pass

    def EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor method
        pass

class pcm_av_av_repository_av_av_PassiveResource(Entity):

    pass
class pcm_av_av_resourceenvironment_av_av_ResourceContainer(Entity):

    pass
class pcm_av_av_composition_av_av_EventChannel(Entity):

    pass
class pcm_av_av_composition_av_av_Connector(Entity):

    pass
class pcm_av_av_seff_av_av_AbstractAction(Entity):

    pass
class pcm_av_av_allocation_av_av_Allocation(Entity):

    def __init__(self, pcm_av_av_allocation_av_av_Allocation: "ResourceEnvironment" = None, pcm_av_av_allocation_av_av_Allocation690: "System" = None, AllocationContext: set["AllocationContext"] = None):
        self.pcm_av_av_allocation_av_av_Allocation = pcm_av_av_allocation_av_av_Allocation
        self.pcm_av_av_allocation_av_av_Allocation690 = pcm_av_av_allocation_av_av_Allocation690
        self.AllocationContext = AllocationContext if AllocationContext is not None else set()
        
    @property
    def pcm_av_av_allocation_av_av_Allocation690(self):
        return self.__pcm_av_av_allocation_av_av_Allocation690

    @pcm_av_av_allocation_av_av_Allocation690.setter
    def pcm_av_av_allocation_av_av_Allocation690(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_allocation_av_av_Allocation__pcm_av_av_allocation_av_av_Allocation690", None)
        self.__pcm_av_av_allocation_av_av_Allocation690 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "System691"):
                opp_val = getattr(old_value, "System691", None)
                if opp_val == self:
                    setattr(old_value, "System691", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "System691"):
                opp_val = getattr(value, "System691", None)
                setattr(value, "System691", self)

    @property
    def AllocationContext(self):
        return self.__AllocationContext

    @AllocationContext.setter
    def AllocationContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_allocation_av_av_Allocation__AllocationContext", None)
        self.__AllocationContext = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "allocation_av_av693"):
                    opp_val = getattr(item, "allocation_av_av693", None)
                    
                    if opp_val == self:
                        setattr(item, "allocation_av_av693", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "allocation_av_av693"):
                    opp_val = getattr(item, "allocation_av_av693", None)
                    
                    setattr(item, "allocation_av_av693", self)
                    

    @property
    def pcm_av_av_allocation_av_av_Allocation(self):
        return self.__pcm_av_av_allocation_av_av_Allocation

    @pcm_av_av_allocation_av_av_Allocation.setter
    def pcm_av_av_allocation_av_av_Allocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_allocation_av_av_Allocation__pcm_av_av_allocation_av_av_Allocation", None)
        self.__pcm_av_av_allocation_av_av_Allocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceEnvironment688"):
                opp_val = getattr(old_value, "ResourceEnvironment688", None)
                if opp_val == self:
                    setattr(old_value, "ResourceEnvironment688", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceEnvironment688"):
                opp_val = getattr(value, "ResourceEnvironment688", None)
                setattr(value, "ResourceEnvironment688", self)

    def EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce method
        pass

    def CommunicatingServersHaveToBeConnectedByLinkingResource(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement CommunicatingServersHaveToBeConnectedByLinkingResource method
        pass

class pcm_av_av_usagemodel_av_av_UsageScenario(Entity):

    pass
class pcm_av_av_composition_av_av_AssemblyContext(Entity):

    pass
class pcm_av_av_composition_av_av_ComposedStructure(Entity):

    def __init__(self, composition_av_av64: set["composition_av_av_AssemblyContext"] = None, composition_av_av67: set["composition_av_av_ResourceRequiredDelegationConnector"] = None, composition_av_av70: set["composition_av_av_EventChannel"] = None, composition_av_av73: set["composition_av_av_Connector"] = None):
        self.composition_av_av64 = composition_av_av64 if composition_av_av64 is not None else set()
        self.composition_av_av67 = composition_av_av67 if composition_av_av67 is not None else set()
        self.composition_av_av70 = composition_av_av70 if composition_av_av70 is not None else set()
        self.composition_av_av73 = composition_av_av73 if composition_av_av73 is not None else set()
        
    @property
    def composition_av_av64(self):
        return self.__composition_av_av64

    @composition_av_av64.setter
    def composition_av_av64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_composition_av_av_ComposedStructure__composition_av_av64", None)
        self.__composition_av_av64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_av_av65"):
                    opp_val = getattr(item, "core_av_av65", None)
                    
                    if opp_val == self:
                        setattr(item, "core_av_av65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_av_av65"):
                    opp_val = getattr(item, "core_av_av65", None)
                    
                    setattr(item, "core_av_av65", self)
                    

    @property
    def composition_av_av67(self):
        return self.__composition_av_av67

    @composition_av_av67.setter
    def composition_av_av67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_composition_av_av_ComposedStructure__composition_av_av67", None)
        self.__composition_av_av67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_av_av68"):
                    opp_val = getattr(item, "core_av_av68", None)
                    
                    if opp_val == self:
                        setattr(item, "core_av_av68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_av_av68"):
                    opp_val = getattr(item, "core_av_av68", None)
                    
                    setattr(item, "core_av_av68", self)
                    

    @property
    def composition_av_av70(self):
        return self.__composition_av_av70

    @composition_av_av70.setter
    def composition_av_av70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_composition_av_av_ComposedStructure__composition_av_av70", None)
        self.__composition_av_av70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_av_av71"):
                    opp_val = getattr(item, "core_av_av71", None)
                    
                    if opp_val == self:
                        setattr(item, "core_av_av71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_av_av71"):
                    opp_val = getattr(item, "core_av_av71", None)
                    
                    setattr(item, "core_av_av71", self)
                    

    @property
    def composition_av_av73(self):
        return self.__composition_av_av73

    @composition_av_av73.setter
    def composition_av_av73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_composition_av_av_ComposedStructure__composition_av_av73", None)
        self.__composition_av_av73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_av_av74"):
                    opp_val = getattr(item, "core_av_av74", None)
                    
                    if opp_val == self:
                        setattr(item, "core_av_av74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_av_av74"):
                    opp_val = getattr(item, "core_av_av74", None)
                    
                    setattr(item, "core_av_av74", self)
                    

    def MultipleConnectorsConstraintForAssemblyConnectors(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MultipleConnectorsConstraintForAssemblyConnectors method
        pass

    def MultipleConnectorsConstraint(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MultipleConnectorsConstraint method
        pass

class pcm_av_av_resourcetype_av_av_ResourceInterface(Entity):

    pass
class pcm_av_av_reliability_av_av_FailureType(Entity):

    pass
class pcm_av_av_repository_av_av_Interface(Entity):

    def __init__(self, pcm_av_av_repository_av_av_Interface: set["Interface"] = None, pcm_av_av_repository_av_av_Interface319: set["Protocol"] = None, RequiredCharacterisation: set["RequiredCharacterisation"] = None, Repository323: "Repository" = None):
        self.pcm_av_av_repository_av_av_Interface = pcm_av_av_repository_av_av_Interface if pcm_av_av_repository_av_av_Interface is not None else set()
        self.pcm_av_av_repository_av_av_Interface319 = pcm_av_av_repository_av_av_Interface319 if pcm_av_av_repository_av_av_Interface319 is not None else set()
        self.RequiredCharacterisation = RequiredCharacterisation if RequiredCharacterisation is not None else set()
        self.Repository323 = Repository323
        
    @property
    def Repository323(self):
        return self.__Repository323

    @Repository323.setter
    def Repository323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_repository_av_av_Interface__Repository323", None)
        self.__Repository323 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av_av324"):
                opp_val = getattr(old_value, "repository_av_av324", None)
                if opp_val == self:
                    setattr(old_value, "repository_av_av324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av_av324"):
                opp_val = getattr(value, "repository_av_av324", None)
                setattr(value, "repository_av_av324", self)

    @property
    def pcm_av_av_repository_av_av_Interface319(self):
        return self.__pcm_av_av_repository_av_av_Interface319

    @pcm_av_av_repository_av_av_Interface319.setter
    def pcm_av_av_repository_av_av_Interface319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_repository_av_av_Interface__pcm_av_av_repository_av_av_Interface319", None)
        self.__pcm_av_av_repository_av_av_Interface319 = value if value is not None else set()
        
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
    def pcm_av_av_repository_av_av_Interface(self):
        return self.__pcm_av_av_repository_av_av_Interface

    @pcm_av_av_repository_av_av_Interface.setter
    def pcm_av_av_repository_av_av_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_repository_av_av_Interface__pcm_av_av_repository_av_av_Interface", None)
        self.__pcm_av_av_repository_av_av_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Interface317"):
                    opp_val = getattr(item, "Interface317", None)
                    
                    if opp_val == self:
                        setattr(item, "Interface317", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Interface317"):
                    opp_val = getattr(item, "Interface317", None)
                    
                    setattr(item, "Interface317", self)
                    

    @property
    def RequiredCharacterisation(self):
        return self.__RequiredCharacterisation

    @RequiredCharacterisation.setter
    def RequiredCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_repository_av_av_Interface__RequiredCharacterisation", None)
        self.__RequiredCharacterisation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_av_av321"):
                    opp_val = getattr(item, "repository_av_av321", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_av_av321", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_av_av321"):
                    opp_val = getattr(item, "repository_av_av321", None)
                    
                    setattr(item, "repository_av_av321", self)
                    

    def NoProtocolTypeIDUsedTwice(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement NoProtocolTypeIDUsedTwice method
        pass

class pcm_av_av_repository_av_av_Repository(Entity):

    def __init__(self, repositoryDescription: str, RepositoryComponent307: set["RepositoryComponent"] = None, Interface: set["Interface"] = None, DataType314: set["DataType"] = None, FailureType: set["FailureType"] = None):
        self.repositoryDescription = repositoryDescription
        self.RepositoryComponent307 = RepositoryComponent307 if RepositoryComponent307 is not None else set()
        self.Interface = Interface if Interface is not None else set()
        self.DataType314 = DataType314 if DataType314 is not None else set()
        self.FailureType = FailureType if FailureType is not None else set()
        
    @property
    def repositoryDescription(self) -> str:
        return self.__repositoryDescription

    @repositoryDescription.setter
    def repositoryDescription(self, repositoryDescription: str):
        self.__repositoryDescription = repositoryDescription

    @property
    def FailureType(self):
        return self.__FailureType

    @FailureType.setter
    def FailureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_repository_av_av_Repository__FailureType", None)
        self.__FailureType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reliability_av_av312"):
                    opp_val = getattr(item, "reliability_av_av312", None)
                    
                    if opp_val == self:
                        setattr(item, "reliability_av_av312", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reliability_av_av312"):
                    opp_val = getattr(item, "reliability_av_av312", None)
                    
                    setattr(item, "reliability_av_av312", self)
                    

    @property
    def DataType314(self):
        return self.__DataType314

    @DataType314.setter
    def DataType314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_repository_av_av_Repository__DataType314", None)
        self.__DataType314 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_av_av315"):
                    opp_val = getattr(item, "repository_av_av315", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_av_av315", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_av_av315"):
                    opp_val = getattr(item, "repository_av_av315", None)
                    
                    setattr(item, "repository_av_av315", self)
                    

    @property
    def Interface(self):
        return self.__Interface

    @Interface.setter
    def Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_repository_av_av_Repository__Interface", None)
        self.__Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_av_av310"):
                    opp_val = getattr(item, "repository_av_av310", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_av_av310", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_av_av310"):
                    opp_val = getattr(item, "repository_av_av310", None)
                    
                    setattr(item, "repository_av_av310", self)
                    

    @property
    def RepositoryComponent307(self):
        return self.__RepositoryComponent307

    @RepositoryComponent307.setter
    def RepositoryComponent307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_repository_av_av_Repository__RepositoryComponent307", None)
        self.__RepositoryComponent307 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_av_av308"):
                    opp_val = getattr(item, "repository_av_av308", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_av_av308", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_av_av308"):
                    opp_val = getattr(item, "repository_av_av308", None)
                    
                    setattr(item, "repository_av_av308", self)
                    

class pcm_av_av_repository_av_av_Role(Entity):

    pass
class pcm_av_av_entity_av_av_ResourceInterfaceRequiringEntity(Entity):

    pass
class pcm_av_av_seff_reliability_av_av_FailureHandlingEntity(Entity):

    pass
class pcm_av_av_qosannotations_av_av_QoSAnnotations(Entity):

    def __init__(self, System: "System" = None, SpecifiedQoSAnnotation: set["SpecifiedQoSAnnotation"] = None, SpecifiedOutputParameterAbstraction608: set["SpecifiedOutputParameterAbstraction"] = None):
        self.System = System
        self.SpecifiedQoSAnnotation = SpecifiedQoSAnnotation if SpecifiedQoSAnnotation is not None else set()
        self.SpecifiedOutputParameterAbstraction608 = SpecifiedOutputParameterAbstraction608 if SpecifiedOutputParameterAbstraction608 is not None else set()
        
    @property
    def SpecifiedOutputParameterAbstraction608(self):
        return self.__SpecifiedOutputParameterAbstraction608

    @SpecifiedOutputParameterAbstraction608.setter
    def SpecifiedOutputParameterAbstraction608(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_qosannotations_av_av_QoSAnnotations__SpecifiedOutputParameterAbstraction608", None)
        self.__SpecifiedOutputParameterAbstraction608 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qosannotations_av_av609"):
                    opp_val = getattr(item, "qosannotations_av_av609", None)
                    
                    if opp_val == self:
                        setattr(item, "qosannotations_av_av609", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qosannotations_av_av609"):
                    opp_val = getattr(item, "qosannotations_av_av609", None)
                    
                    setattr(item, "qosannotations_av_av609", self)
                    

    @property
    def System(self):
        return self.__System

    @System.setter
    def System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_qosannotations_av_av_QoSAnnotations__System", None)
        self.__System = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system_av_av"):
                opp_val = getattr(old_value, "system_av_av", None)
                if opp_val == self:
                    setattr(old_value, "system_av_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system_av_av"):
                opp_val = getattr(value, "system_av_av", None)
                setattr(value, "system_av_av", self)

    @property
    def SpecifiedQoSAnnotation(self):
        return self.__SpecifiedQoSAnnotation

    @SpecifiedQoSAnnotation.setter
    def SpecifiedQoSAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_qosannotations_av_av_QoSAnnotations__SpecifiedQoSAnnotation", None)
        self.__SpecifiedQoSAnnotation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qosannotations_av_av612"):
                    opp_val = getattr(item, "qosannotations_av_av612", None)
                    
                    if opp_val == self:
                        setattr(item, "qosannotations_av_av612", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qosannotations_av_av612"):
                    opp_val = getattr(item, "qosannotations_av_av612", None)
                    
                    setattr(item, "qosannotations_av_av612", self)
                    

    def MultipleReliabilityAnnotationsPerExternalCallNotAllowed(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MultipleReliabilityAnnotationsPerExternalCallNotAllowed method
        pass

class pcm_av_av_repository_av_av_Signature(Entity):

    pass
class pcm_av_av_seff_av_av_AbstractBranchTransition(Entity):

    pass
class pcm_av_av_resourceenvironment_av_av_LinkingResource(Entity):

    pass
class pcm_av_av_entity_av_av_InterfaceProvidingEntity(Entity):

    pass
class entity_av_av_InterfaceRequiringEntity:

    pass
class entity_av_av_InterfaceProvidingEntity:

    pass
class pcm_av_av_entity_av_av_InterfaceProvidingRequiringEntity(entity_av_av_InterfaceRequiringEntity, entity_av_av_InterfaceProvidingEntity):

    pass
class ResourceInterface:

    pass
class RandomVariable:

    pass
class pcm_av_av_core_av_av_PCMRandomVariable(RandomVariable):

    def __init__(self, ClosedWorkload: "ClosedWorkload" = None, PassiveResource: "PassiveResource" = None, VariableCharacterisation: "VariableCharacterisation" = None, seff_performance_av_av: "seff_performance_av_av_InfrastructureCall" = None, seff_performance_av_av16: "seff_performance_av_av_ResourceCall" = None, seff_performance_av_av19: "seff_performance_av_av_ParametricResourceDemand" = None, LoopAction: "LoopAction" = None, GuardedBranchTransition: "GuardedBranchTransition" = None, qos_performance_av_av: "qos_performance_av_av_SpecifiedExecutionTime" = None, composition_av_av: "composition_av_av_EventChannelSinkConnector" = None, composition_av_av28: "composition_av_av_AssemblyEventConnector" = None, Loop: "Loop" = None, OpenWorkload: "OpenWorkload" = None, Delay: "Delay" = None, CommunicationLinkResourceSpecification: "CommunicationLinkResourceSpecification" = None, ProcessingResourceSpecification: "ProcessingResourceSpecification" = None, CommunicationLinkResourceSpecification40: "CommunicationLinkResourceSpecification" = None):
        self.ClosedWorkload = ClosedWorkload
        self.PassiveResource = PassiveResource
        self.VariableCharacterisation = VariableCharacterisation
        self.seff_performance_av_av = seff_performance_av_av
        self.seff_performance_av_av16 = seff_performance_av_av16
        self.seff_performance_av_av19 = seff_performance_av_av19
        self.LoopAction = LoopAction
        self.GuardedBranchTransition = GuardedBranchTransition
        self.qos_performance_av_av = qos_performance_av_av
        self.composition_av_av = composition_av_av
        self.composition_av_av28 = composition_av_av28
        self.Loop = Loop
        self.OpenWorkload = OpenWorkload
        self.Delay = Delay
        self.CommunicationLinkResourceSpecification = CommunicationLinkResourceSpecification
        self.ProcessingResourceSpecification = ProcessingResourceSpecification
        self.CommunicationLinkResourceSpecification40 = CommunicationLinkResourceSpecification40
        
    @property
    def PassiveResource(self):
        return self.__PassiveResource

    @PassiveResource.setter
    def PassiveResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_core_av_av_PCMRandomVariable__PassiveResource", None)
        self.__PassiveResource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av_av"):
                opp_val = getattr(old_value, "repository_av_av", None)
                if opp_val == self:
                    setattr(old_value, "repository_av_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av_av"):
                opp_val = getattr(value, "repository_av_av", None)
                setattr(value, "repository_av_av", self)

    @property
    def CommunicationLinkResourceSpecification(self):
        return self.__CommunicationLinkResourceSpecification

    @CommunicationLinkResourceSpecification.setter
    def CommunicationLinkResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_core_av_av_PCMRandomVariable__CommunicationLinkResourceSpecification", None)
        self.__CommunicationLinkResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_av_av"):
                opp_val = getattr(old_value, "resourceenvironment_av_av", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_av_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_av_av"):
                opp_val = getattr(value, "resourceenvironment_av_av", None)
                setattr(value, "resourceenvironment_av_av", self)

    @property
    def seff_performance_av_av(self):
        return self.__seff_performance_av_av

    @seff_performance_av_av.setter
    def seff_performance_av_av(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_core_av_av_PCMRandomVariable__seff_performance_av_av", None)
        self.__seff_performance_av_av = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av_av"):
                opp_val = getattr(old_value, "seff_av_av", None)
                if opp_val == self:
                    setattr(old_value, "seff_av_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av_av"):
                opp_val = getattr(value, "seff_av_av", None)
                setattr(value, "seff_av_av", self)

    @property
    def VariableCharacterisation(self):
        return self.__VariableCharacterisation

    @VariableCharacterisation.setter
    def VariableCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_core_av_av_PCMRandomVariable__VariableCharacterisation", None)
        self.__VariableCharacterisation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameter_av_av"):
                opp_val = getattr(old_value, "parameter_av_av", None)
                if opp_val == self:
                    setattr(old_value, "parameter_av_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameter_av_av"):
                opp_val = getattr(value, "parameter_av_av", None)
                setattr(value, "parameter_av_av", self)

    @property
    def composition_av_av28(self):
        return self.__composition_av_av28

    @composition_av_av28.setter
    def composition_av_av28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_core_av_av_PCMRandomVariable__composition_av_av28", None)
        self.__composition_av_av28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av_av29"):
                opp_val = getattr(old_value, "core_av_av29", None)
                if opp_val == self:
                    setattr(old_value, "core_av_av29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av_av29"):
                opp_val = getattr(value, "core_av_av29", None)
                setattr(value, "core_av_av29", self)

    @property
    def GuardedBranchTransition(self):
        return self.__GuardedBranchTransition

    @GuardedBranchTransition.setter
    def GuardedBranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_core_av_av_PCMRandomVariable__GuardedBranchTransition", None)
        self.__GuardedBranchTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av_av24"):
                opp_val = getattr(old_value, "seff_av_av24", None)
                if opp_val == self:
                    setattr(old_value, "seff_av_av24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av_av24"):
                opp_val = getattr(value, "seff_av_av24", None)
                setattr(value, "seff_av_av24", self)

    @property
    def qos_performance_av_av(self):
        return self.__qos_performance_av_av

    @qos_performance_av_av.setter
    def qos_performance_av_av(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_core_av_av_PCMRandomVariable__qos_performance_av_av", None)
        self.__qos_performance_av_av = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qosannotations_av_av"):
                opp_val = getattr(old_value, "qosannotations_av_av", None)
                if opp_val == self:
                    setattr(old_value, "qosannotations_av_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qosannotations_av_av"):
                opp_val = getattr(value, "qosannotations_av_av", None)
                setattr(value, "qosannotations_av_av", self)

    @property
    def LoopAction(self):
        return self.__LoopAction

    @LoopAction.setter
    def LoopAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_core_av_av_PCMRandomVariable__LoopAction", None)
        self.__LoopAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av_av22"):
                opp_val = getattr(old_value, "seff_av_av22", None)
                if opp_val == self:
                    setattr(old_value, "seff_av_av22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av_av22"):
                opp_val = getattr(value, "seff_av_av22", None)
                setattr(value, "seff_av_av22", self)

    @property
    def seff_performance_av_av19(self):
        return self.__seff_performance_av_av19

    @seff_performance_av_av19.setter
    def seff_performance_av_av19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_core_av_av_PCMRandomVariable__seff_performance_av_av19", None)
        self.__seff_performance_av_av19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av_av20"):
                opp_val = getattr(old_value, "seff_av_av20", None)
                if opp_val == self:
                    setattr(old_value, "seff_av_av20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av_av20"):
                opp_val = getattr(value, "seff_av_av20", None)
                setattr(value, "seff_av_av20", self)

    @property
    def OpenWorkload(self):
        return self.__OpenWorkload

    @OpenWorkload.setter
    def OpenWorkload(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_core_av_av_PCMRandomVariable__OpenWorkload", None)
        self.__OpenWorkload = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av_av33"):
                opp_val = getattr(old_value, "usagemodel_av_av33", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av_av33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av_av33"):
                opp_val = getattr(value, "usagemodel_av_av33", None)
                setattr(value, "usagemodel_av_av33", self)

    @property
    def composition_av_av(self):
        return self.__composition_av_av

    @composition_av_av.setter
    def composition_av_av(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_core_av_av_PCMRandomVariable__composition_av_av", None)
        self.__composition_av_av = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av_av"):
                opp_val = getattr(old_value, "core_av_av", None)
                if opp_val == self:
                    setattr(old_value, "core_av_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av_av"):
                opp_val = getattr(value, "core_av_av", None)
                setattr(value, "core_av_av", self)

    @property
    def CommunicationLinkResourceSpecification40(self):
        return self.__CommunicationLinkResourceSpecification40

    @CommunicationLinkResourceSpecification40.setter
    def CommunicationLinkResourceSpecification40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_core_av_av_PCMRandomVariable__CommunicationLinkResourceSpecification40", None)
        self.__CommunicationLinkResourceSpecification40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_av_av41"):
                opp_val = getattr(old_value, "resourceenvironment_av_av41", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_av_av41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_av_av41"):
                opp_val = getattr(value, "resourceenvironment_av_av41", None)
                setattr(value, "resourceenvironment_av_av41", self)

    @property
    def Delay(self):
        return self.__Delay

    @Delay.setter
    def Delay(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_core_av_av_PCMRandomVariable__Delay", None)
        self.__Delay = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av_av35"):
                opp_val = getattr(old_value, "usagemodel_av_av35", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av_av35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av_av35"):
                opp_val = getattr(value, "usagemodel_av_av35", None)
                setattr(value, "usagemodel_av_av35", self)

    @property
    def ProcessingResourceSpecification(self):
        return self.__ProcessingResourceSpecification

    @ProcessingResourceSpecification.setter
    def ProcessingResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_core_av_av_PCMRandomVariable__ProcessingResourceSpecification", None)
        self.__ProcessingResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_av_av38"):
                opp_val = getattr(old_value, "resourceenvironment_av_av38", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_av_av38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_av_av38"):
                opp_val = getattr(value, "resourceenvironment_av_av38", None)
                setattr(value, "resourceenvironment_av_av38", self)

    @property
    def ClosedWorkload(self):
        return self.__ClosedWorkload

    @ClosedWorkload.setter
    def ClosedWorkload(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_core_av_av_PCMRandomVariable__ClosedWorkload", None)
        self.__ClosedWorkload = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av_av"):
                opp_val = getattr(old_value, "usagemodel_av_av", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av_av"):
                opp_val = getattr(value, "usagemodel_av_av", None)
                setattr(value, "usagemodel_av_av", self)

    @property
    def Loop(self):
        return self.__Loop

    @Loop.setter
    def Loop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_core_av_av_PCMRandomVariable__Loop", None)
        self.__Loop = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av_av31"):
                opp_val = getattr(old_value, "usagemodel_av_av31", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av_av31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av_av31"):
                opp_val = getattr(value, "usagemodel_av_av31", None)
                setattr(value, "usagemodel_av_av31", self)

    @property
    def seff_performance_av_av16(self):
        return self.__seff_performance_av_av16

    @seff_performance_av_av16.setter
    def seff_performance_av_av16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_av_core_av_av_PCMRandomVariable__seff_performance_av_av16", None)
        self.__seff_performance_av_av16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av_av17"):
                opp_val = getattr(old_value, "seff_av_av17", None)
                if opp_val == self:
                    setattr(old_value, "seff_av_av17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av_av17"):
                opp_val = getattr(value, "seff_av_av17", None)
                setattr(value, "seff_av_av17", self)

    def SpecificationMustNotBeNULL(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SpecificationMustNotBeNULL method
        pass

class pcm_av_av_PerJoinPointScope:

    pass
class pcm_av_av_GlobalScope:

    pass
class OpenWorkload:

    pass
class Loop:

    pass
class composition_av_av_AssemblyEventConnector:

    pass
class composition_av_av_EventChannelSinkConnector:

    pass
class qos_performance_av_av_SpecifiedExecutionTime:

    pass
class GuardedBranchTransition:

    pass
class LoopAction:

    pass
class seff_performance_av_av_ParametricResourceDemand:

    pass
class seff_performance_av_av_ResourceCall:

    pass
class seff_performance_av_av_InfrastructureCall:

    pass
class VariableCharacterisation:

    pass
class PassiveResource:

    pass
class ClosedWorkload:

    pass
class pcm_av_av_Advice:

    pass
class pcm_av_av_PerJoinPointScopePerJoinPointScope:

    pass
class pcm_av_av_GlobalScopeGlobalScope:

    pass
class pcm_av_av_EObject:

    pass
class pcm_av_av_AdviceAdvice:

    pass
class pcm_av_av_DummyClass:

    pass