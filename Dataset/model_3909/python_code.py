from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ComponentType(Enum):
    BUSINESS_COMPONENT = "BUSINESS_COMPONENT"
    INFRASTRUCTURE_COMPONENT = "INFRASTRUCTURE_COMPONENT"
class ParameterModifier(Enum):
    none = "none"
    in = "in"
    out = "out"
    inout = "inout"
class VariableCharacterisationType(Enum):
    STRUCTURE = "STRUCTURE"
    NUMBER_OF_ELEMENTS = "NUMBER_OF_ELEMENTS"
    VALUE = "VALUE"
    BYTESIZE = "BYTESIZE"
    TYPE = "TYPE"
class PrimitiveTypeEnum(Enum):
    CHAR = "CHAR"
    BYTE = "BYTE"
    LONG = "LONG"
    INT = "INT"
    STRING = "STRING"
    BOOL = "BOOL"
    DOUBLE = "DOUBLE"


############################################
# Definition of Classes
############################################

class ParametricResourceDemand:

    pass
class pcm_pc_av_completions_pc_av_NetworkDemandParametricResourceDemand(ParametricResourceDemand):

    pass
class ExternalCallAction:

    pass
class pcm_pc_av_completions_pc_av_DelegatingExternalCallAction(ExternalCallAction):

    pass
class Completion:

    pass
class pcm_pc_av_completions_pc_av_CompletionRepository:

    pass
class repository_pc_av_RepositoryComponent:

    pass
class AllocationContext:

    pass
class Allocation:

    pass
class ResourceEnvironment:

    pass
class ResourceContainer:

    pass
class LinkingResource:

    pass
class ExternalFailureOccurrenceDescription:

    pass
class pcm_pc_av_qosannotations_pc_av_SpecifiedOutputParameterAbstraction:

    pass
class SpecifiedExecutionTime:

    pass
class pcm_pc_av_qos_performance_pc_av_ComponentSpecifiedExecutionTime(SpecifiedExecutionTime):

    pass
class pcm_pc_av_qos_performance_pc_av_SystemSpecifiedExecutionTime(SpecifiedExecutionTime):

    def __init__(self):
        
    def SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem method
        pass

class QoSAnnotations:

    pass
class SpecifiedQoSAnnotation:

    pass
class pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation(SpecifiedQoSAnnotation):

    def __init__(self, ExternalFailureOccurrenceDescription: set["ExternalFailureOccurrenceDescription"] = None, qosannotations_pc_av608: "pcm_pc_av_qosannotations_pc_av_QoSAnnotations"):
        self.ExternalFailureOccurrenceDescription = ExternalFailureOccurrenceDescription if ExternalFailureOccurrenceDescription is not None else set()
        
    @property
    def ExternalFailureOccurrenceDescription(self):
        return self.__ExternalFailureOccurrenceDescription

    @ExternalFailureOccurrenceDescription.setter
    def ExternalFailureOccurrenceDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription", None)
        self.__ExternalFailureOccurrenceDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reliability_pc_av626"):
                    opp_val = getattr(item, "reliability_pc_av626", None)
                    
                    if opp_val == self:
                        setattr(item, "reliability_pc_av626", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reliability_pc_av626"):
                    opp_val = getattr(item, "reliability_pc_av626", None)
                    
                    setattr(item, "reliability_pc_av626", self)
                    

    def SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1 method
        pass

    def MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed method
        pass

    def SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem method
        pass

class pcm_pc_av_qos_performance_pc_av_SpecifiedExecutionTime(SpecifiedQoSAnnotation):

    pass
class System:

    pass
class seff_reliability_pc_av_RecoveryAction:

    pass
class seff_reliability_pc_av_RecoveryActionBehaviour:

    pass
class pcm_pc_av_qosannotations_pc_av_SpecifiedQoSAnnotation:

    pass
class pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand:

    def __init__(self, PCMRandomVariable580: "PCMRandomVariable" = None, pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand: "ProcessingResourceType" = None, AbstractInternalControlFlowAction585: "AbstractInternalControlFlowAction" = None):
        self.PCMRandomVariable580 = PCMRandomVariable580
        self.pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand = pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand
        self.AbstractInternalControlFlowAction585 = AbstractInternalControlFlowAction585
        
    @property
    def PCMRandomVariable580(self):
        return self.__PCMRandomVariable580

    @PCMRandomVariable580.setter
    def PCMRandomVariable580(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand__PCMRandomVariable580", None)
        self.__PCMRandomVariable580 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc_av581"):
                opp_val = getattr(old_value, "core_pc_av581", None)
                if opp_val == self:
                    setattr(old_value, "core_pc_av581", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc_av581"):
                opp_val = getattr(value, "core_pc_av581", None)
                setattr(value, "core_pc_av581", self)

    @property
    def pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand(self):
        return self.__pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand

    @pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand.setter
    def pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand__pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand", None)
        self.__pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcessingResourceType583"):
                opp_val = getattr(old_value, "ProcessingResourceType583", None)
                if opp_val == self:
                    setattr(old_value, "ProcessingResourceType583", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessingResourceType583"):
                opp_val = getattr(value, "ProcessingResourceType583", None)
                setattr(value, "ProcessingResourceType583", self)

    @property
    def AbstractInternalControlFlowAction585(self):
        return self.__AbstractInternalControlFlowAction585

    @AbstractInternalControlFlowAction585.setter
    def AbstractInternalControlFlowAction585(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand__AbstractInternalControlFlowAction585", None)
        self.__AbstractInternalControlFlowAction585 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc_av586"):
                opp_val = getattr(old_value, "seff_pc_av586", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc_av586", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc_av586"):
                opp_val = getattr(value, "seff_pc_av586", None)
                setattr(value, "seff_pc_av586", self)

    def DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

class seff_pc_av_AbstractInternalControlFlowAction:

    pass
class seff_pc_av_CallAction:

    pass
class pcm_pc_av_seff_pc_av_InternalCallAction(seff_pc_av_AbstractInternalControlFlowAction, seff_pc_av_CallAction):

    pass
class seff_reliability_pc_av_FailureHandlingEntity:

    pass
class ResourceDemandingSEFF:

    pass
class seff_pc_av_CallReturnAction:

    pass
class seff_pc_av_AbstractAction:

    pass
class pcm_pc_av_seff_pc_av_EmitEventAction(seff_pc_av_AbstractAction, seff_pc_av_CallAction):

    pass
class pcm_pc_av_seff_pc_av_ExternalCallAction(seff_pc_av_AbstractAction, seff_reliability_pc_av_FailureHandlingEntity, seff_pc_av_CallReturnAction):

    def __init__(self, retryCount: int, pcm_pc_av_seff_pc_av_ExternalCallAction: "OperationSignature" = None, pcm_pc_av_seff_pc_av_ExternalCallAction533: "OperationRequiredRole" = None):
        self.retryCount = retryCount
        self.pcm_pc_av_seff_pc_av_ExternalCallAction = pcm_pc_av_seff_pc_av_ExternalCallAction
        self.pcm_pc_av_seff_pc_av_ExternalCallAction533 = pcm_pc_av_seff_pc_av_ExternalCallAction533
        
    @property
    def retryCount(self) -> int:
        return self.__retryCount

    @retryCount.setter
    def retryCount(self, retryCount: int):
        self.__retryCount = retryCount

    @property
    def pcm_pc_av_seff_pc_av_ExternalCallAction533(self):
        return self.__pcm_pc_av_seff_pc_av_ExternalCallAction533

    @pcm_pc_av_seff_pc_av_ExternalCallAction533.setter
    def pcm_pc_av_seff_pc_av_ExternalCallAction533(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_seff_pc_av_ExternalCallAction__pcm_pc_av_seff_pc_av_ExternalCallAction533", None)
        self.__pcm_pc_av_seff_pc_av_ExternalCallAction533 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationRequiredRole534"):
                opp_val = getattr(old_value, "OperationRequiredRole534", None)
                if opp_val == self:
                    setattr(old_value, "OperationRequiredRole534", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationRequiredRole534"):
                opp_val = getattr(value, "OperationRequiredRole534", None)
                setattr(value, "OperationRequiredRole534", self)

    @property
    def pcm_pc_av_seff_pc_av_ExternalCallAction(self):
        return self.__pcm_pc_av_seff_pc_av_ExternalCallAction

    @pcm_pc_av_seff_pc_av_ExternalCallAction.setter
    def pcm_pc_av_seff_pc_av_ExternalCallAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_seff_pc_av_ExternalCallAction__pcm_pc_av_seff_pc_av_ExternalCallAction", None)
        self.__pcm_pc_av_seff_pc_av_ExternalCallAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationSignature531"):
                opp_val = getattr(old_value, "OperationSignature531", None)
                if opp_val == self:
                    setattr(old_value, "OperationSignature531", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationSignature531"):
                opp_val = getattr(value, "OperationSignature531", None)
                setattr(value, "OperationSignature531", self)

    def SignatureBelongsToRole(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SignatureBelongsToRole method
        pass

    def OperationRequiredRoleMustBeReferencedByContainer(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement OperationRequiredRoleMustBeReferencedByContainer method
        pass

class pcm_pc_av_seff_pc_av_SynchronisationPoint:

    pass
class ForkAction:

    pass
class ForkedBehaviour:

    pass
class ResourceDemandingInternalBehaviour:

    pass
class seff_pc_av_ResourceDemandingBehaviour:

    pass
class pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour(seff_reliability_pc_av_FailureHandlingEntity, seff_pc_av_ResourceDemandingBehaviour):

    def __init__(self, pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour: set["seff_reliability_pc_av_RecoveryActionBehaviour"] = None, seff_reliability_pc_av: "seff_reliability_pc_av_RecoveryAction" = None):
        self.pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour = pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour if pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour is not None else set()
        self.seff_reliability_pc_av = seff_reliability_pc_av
        
    @property
    def pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour(self):
        return self.__pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour

    @pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour.setter
    def pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour__pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour", None)
        self.__pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_reliability_pc_av_RecoveryActionBehaviour"):
                    opp_val = getattr(item, "seff_reliability_pc_av_RecoveryActionBehaviour", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_reliability_pc_av_RecoveryActionBehaviour", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_reliability_pc_av_RecoveryActionBehaviour"):
                    opp_val = getattr(item, "seff_reliability_pc_av_RecoveryActionBehaviour", None)
                    
                    setattr(item, "seff_reliability_pc_av_RecoveryActionBehaviour", self)
                    

    @property
    def seff_reliability_pc_av(self):
        return self.__seff_reliability_pc_av

    @seff_reliability_pc_av.setter
    def seff_reliability_pc_av(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour__seff_reliability_pc_av", None)
        self.__seff_reliability_pc_av = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc_av589"):
                opp_val = getattr(old_value, "seff_pc_av589", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc_av589", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc_av589"):
                opp_val = getattr(value, "seff_pc_av589", None)
                setattr(value, "seff_pc_av589", self)

    def SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes method
        pass

    def RecoveryActionBehaviourIsNotSuccessorOfItself(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement RecoveryActionBehaviourIsNotSuccessorOfItself method
        pass

    def RecoveryActionBehaviourHasOnlyOnePredecessor(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RecoveryActionBehaviourHasOnlyOnePredecessor method
        pass

class seff_pc_av_ServiceEffectSpecification:

    pass
class pcm_pc_av_seff_pc_av_ServiceEffectSpecification:

    def __init__(self, seffTypeID: str, pcm_pc_av_seff_pc_av_ServiceEffectSpecification: "Signature" = None, BasicComponent500: "BasicComponent" = None):
        self.seffTypeID = seffTypeID
        self.pcm_pc_av_seff_pc_av_ServiceEffectSpecification = pcm_pc_av_seff_pc_av_ServiceEffectSpecification
        self.BasicComponent500 = BasicComponent500
        
    @property
    def seffTypeID(self) -> str:
        return self.__seffTypeID

    @seffTypeID.setter
    def seffTypeID(self, seffTypeID: str):
        self.__seffTypeID = seffTypeID

    @property
    def BasicComponent500(self):
        return self.__BasicComponent500

    @BasicComponent500.setter
    def BasicComponent500(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_seff_pc_av_ServiceEffectSpecification__BasicComponent500", None)
        self.__BasicComponent500 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc_av501"):
                opp_val = getattr(old_value, "repository_pc_av501", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc_av501", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc_av501"):
                opp_val = getattr(value, "repository_pc_av501", None)
                setattr(value, "repository_pc_av501", self)

    @property
    def pcm_pc_av_seff_pc_av_ServiceEffectSpecification(self):
        return self.__pcm_pc_av_seff_pc_av_ServiceEffectSpecification

    @pcm_pc_av_seff_pc_av_ServiceEffectSpecification.setter
    def pcm_pc_av_seff_pc_av_ServiceEffectSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_seff_pc_av_ServiceEffectSpecification__pcm_pc_av_seff_pc_av_ServiceEffectSpecification", None)
        self.__pcm_pc_av_seff_pc_av_ServiceEffectSpecification = value
        
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

class AbstractBranchTransition:

    pass
class pcm_pc_av_seff_pc_av_GuardedBranchTransition(AbstractBranchTransition):

    pass
class pcm_pc_av_seff_pc_av_ProbabilisticBranchTransition(AbstractBranchTransition):

    def __init__(self, branchProbability: float, seff_pc_av494: "pcm_pc_av_seff_pc_av_BranchAction", seff_pc_av480: "pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour"):
        self.branchProbability = branchProbability
        
    @property
    def branchProbability(self) -> float:
        return self.__branchProbability

    @branchProbability.setter
    def branchProbability(self, branchProbability: float):
        self.__branchProbability = branchProbability

class pcm_pc_av_seff_pc_av_CallAction:

    pass
class BranchAction:

    pass
class AbstractLoopAction:

    pass
class pcm_pc_av_seff_pc_av_CollectionIteratorAction(AbstractLoopAction):

    pass
class pcm_pc_av_seff_pc_av_LoopAction(AbstractLoopAction):

    pass
class ResourceDemandingBehaviour:

    pass
class pcm_pc_av_seff_pc_av_ResourceDemandingInternalBehaviour(ResourceDemandingBehaviour):

    pass
class pcm_pc_av_seff_pc_av_ForkedBehaviour(ResourceDemandingBehaviour):

    pass
class AbstractAction:

    pass
class pcm_pc_av_seff_pc_av_AbstractInternalControlFlowAction(AbstractAction):

    pass
class AbstractInternalControlFlowAction:

    pass
class pcm_pc_av_seff_pc_av_StartAction(AbstractInternalControlFlowAction):

    def __init__(self, seff_pc_av570: "pcm_pc_av_seff_performance_pc_av_ResourceCall", seff_pc_av586: "pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand", seff_pc_av564: "pcm_pc_av_seff_performance_pc_av_InfrastructureCall"):
        
    def StartActionPredecessorMustNotBeDefined(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement StartActionPredecessorMustNotBeDefined method
        pass

class pcm_pc_av_seff_pc_av_ReleaseAction(AbstractInternalControlFlowAction):

    pass
class pcm_pc_av_seff_pc_av_InternalAction(AbstractInternalControlFlowAction):

    def __init__(self, InternalFailureOccurrenceDescription556: set["InternalFailureOccurrenceDescription"] = None, seff_pc_av570: "pcm_pc_av_seff_performance_pc_av_ResourceCall", seff_pc_av586: "pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand", seff_pc_av564: "pcm_pc_av_seff_performance_pc_av_InfrastructureCall"):
        self.InternalFailureOccurrenceDescription556 = InternalFailureOccurrenceDescription556 if InternalFailureOccurrenceDescription556 is not None else set()
        
    @property
    def InternalFailureOccurrenceDescription556(self):
        return self.__InternalFailureOccurrenceDescription556

    @InternalFailureOccurrenceDescription556.setter
    def InternalFailureOccurrenceDescription556(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_seff_pc_av_InternalAction__InternalFailureOccurrenceDescription556", None)
        self.__InternalFailureOccurrenceDescription556 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reliability_pc_av557"):
                    opp_val = getattr(item, "reliability_pc_av557", None)
                    
                    if opp_val == self:
                        setattr(item, "reliability_pc_av557", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reliability_pc_av557"):
                    opp_val = getattr(item, "reliability_pc_av557", None)
                    
                    setattr(item, "reliability_pc_av557", self)
                    

    def MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed method
        pass

    def SumOfInternalActionFailureProbabilitiesMustNotExceed1(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SumOfInternalActionFailureProbabilitiesMustNotExceed1 method
        pass

class pcm_pc_av_seff_reliability_pc_av_RecoveryAction(AbstractInternalControlFlowAction):

    def __init__(self, pcm_pc_av_seff_reliability_pc_av_RecoveryAction: "seff_reliability_pc_av_RecoveryActionBehaviour" = None, seff_reliability_pc_av593: set["seff_reliability_pc_av_RecoveryActionBehaviour"] = None, seff_pc_av570: "pcm_pc_av_seff_performance_pc_av_ResourceCall", seff_pc_av586: "pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand", seff_pc_av564: "pcm_pc_av_seff_performance_pc_av_InfrastructureCall"):
        self.pcm_pc_av_seff_reliability_pc_av_RecoveryAction = pcm_pc_av_seff_reliability_pc_av_RecoveryAction
        self.seff_reliability_pc_av593 = seff_reliability_pc_av593 if seff_reliability_pc_av593 is not None else set()
        
    @property
    def seff_reliability_pc_av593(self):
        return self.__seff_reliability_pc_av593

    @seff_reliability_pc_av593.setter
    def seff_reliability_pc_av593(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_seff_reliability_pc_av_RecoveryAction__seff_reliability_pc_av593", None)
        self.__seff_reliability_pc_av593 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_pc_av594"):
                    opp_val = getattr(item, "seff_pc_av594", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_pc_av594", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_pc_av594"):
                    opp_val = getattr(item, "seff_pc_av594", None)
                    
                    setattr(item, "seff_pc_av594", self)
                    

    @property
    def pcm_pc_av_seff_reliability_pc_av_RecoveryAction(self):
        return self.__pcm_pc_av_seff_reliability_pc_av_RecoveryAction

    @pcm_pc_av_seff_reliability_pc_av_RecoveryAction.setter
    def pcm_pc_av_seff_reliability_pc_av_RecoveryAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_seff_reliability_pc_av_RecoveryAction__pcm_pc_av_seff_reliability_pc_av_RecoveryAction", None)
        self.__pcm_pc_av_seff_reliability_pc_av_RecoveryAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_reliability_pc_av_RecoveryActionBehaviour591"):
                opp_val = getattr(old_value, "seff_reliability_pc_av_RecoveryActionBehaviour591", None)
                if opp_val == self:
                    setattr(old_value, "seff_reliability_pc_av_RecoveryActionBehaviour591", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_reliability_pc_av_RecoveryActionBehaviour591"):
                opp_val = getattr(value, "seff_reliability_pc_av_RecoveryActionBehaviour591", None)
                setattr(value, "seff_reliability_pc_av_RecoveryActionBehaviour591", self)

    def PrimaryBehaviourOfRecoveryActionMustBeSet(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement PrimaryBehaviourOfRecoveryActionMustBeSet method
        pass

class pcm_pc_av_seff_pc_av_ForkAction(AbstractInternalControlFlowAction):

    pass
class pcm_pc_av_seff_pc_av_BranchAction(AbstractInternalControlFlowAction):

    def __init__(self, AbstractBranchTransition493: set["AbstractBranchTransition"] = None, seff_pc_av570: "pcm_pc_av_seff_performance_pc_av_ResourceCall", seff_pc_av586: "pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand", seff_pc_av564: "pcm_pc_av_seff_performance_pc_av_InfrastructureCall"):
        self.AbstractBranchTransition493 = AbstractBranchTransition493 if AbstractBranchTransition493 is not None else set()
        
    @property
    def AbstractBranchTransition493(self):
        return self.__AbstractBranchTransition493

    @AbstractBranchTransition493.setter
    def AbstractBranchTransition493(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_seff_pc_av_BranchAction__AbstractBranchTransition493", None)
        self.__AbstractBranchTransition493 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_pc_av494"):
                    opp_val = getattr(item, "seff_pc_av494", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_pc_av494", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_pc_av494"):
                    opp_val = getattr(item, "seff_pc_av494", None)
                    
                    setattr(item, "seff_pc_av494", self)
                    

    def AllProbabilisticBranchProbabilitiesMustSumUpTo1(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AllProbabilisticBranchProbabilitiesMustSumUpTo1 method
        pass

    def EitherGuardedBranchesOrProbabilisiticBranchTransitions(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EitherGuardedBranchesOrProbabilisiticBranchTransitions method
        pass

class pcm_pc_av_seff_pc_av_AbstractLoopAction(AbstractInternalControlFlowAction):

    pass
class pcm_pc_av_seff_pc_av_AcquireAction(AbstractInternalControlFlowAction):

    def __init__(self, timeoutValue: float, timeout: bool, pcm_pc_av_seff_pc_av_AcquireAction: "PassiveResource" = None, seff_pc_av570: "pcm_pc_av_seff_performance_pc_av_ResourceCall", seff_pc_av586: "pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand", seff_pc_av564: "pcm_pc_av_seff_performance_pc_av_InfrastructureCall"):
        self.timeoutValue = timeoutValue
        self.timeout = timeout
        self.pcm_pc_av_seff_pc_av_AcquireAction = pcm_pc_av_seff_pc_av_AcquireAction
        
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
    def pcm_pc_av_seff_pc_av_AcquireAction(self):
        return self.__pcm_pc_av_seff_pc_av_AcquireAction

    @pcm_pc_av_seff_pc_av_AcquireAction.setter
    def pcm_pc_av_seff_pc_av_AcquireAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_seff_pc_av_AcquireAction__pcm_pc_av_seff_pc_av_AcquireAction", None)
        self.__pcm_pc_av_seff_pc_av_AcquireAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PassiveResource539"):
                opp_val = getattr(old_value, "PassiveResource539", None)
                if opp_val == self:
                    setattr(old_value, "PassiveResource539", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PassiveResource539"):
                opp_val = getattr(value, "PassiveResource539", None)
                setattr(value, "PassiveResource539", self)

    def TimeoutValueOfAcquireActionMustNotBeNegative(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement TimeoutValueOfAcquireActionMustNotBeNegative method
        pass

class pcm_pc_av_seff_pc_av_SetVariableAction(AbstractInternalControlFlowAction):

    pass
class pcm_pc_av_seff_pc_av_StopAction(AbstractInternalControlFlowAction):

    def __init__(self, seff_pc_av570: "pcm_pc_av_seff_performance_pc_av_ResourceCall", seff_pc_av586: "pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand", seff_pc_av564: "pcm_pc_av_seff_performance_pc_av_InfrastructureCall"):
        
    def StopActionSuccessorMustNotBeDefined(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement StopActionSuccessorMustNotBeDefined method
        pass

class qos_reliability_pc_av_SpecifiedReliabilityAnnotation:

    pass
class CommunicationLinkResourceType:

    pass
class SoftwareInducedFailureType:

    pass
class pcm_pc_av_reliability_pc_av_ResourceTimeoutFailureType(SoftwareInducedFailureType):

    pass
class InternalAction:

    pass
class FailureOccurrenceDescription:

    pass
class pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription(FailureOccurrenceDescription):

    def __init__(self, qos_reliability_pc_av: "qos_reliability_pc_av_SpecifiedReliabilityAnnotation" = None, pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription: "FailureType" = None):
        self.qos_reliability_pc_av = qos_reliability_pc_av
        self.pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription = pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription
        
    @property
    def qos_reliability_pc_av(self):
        return self.__qos_reliability_pc_av

    @qos_reliability_pc_av.setter
    def qos_reliability_pc_av(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription__qos_reliability_pc_av", None)
        self.__qos_reliability_pc_av = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qosannotations_pc_av452"):
                opp_val = getattr(old_value, "qosannotations_pc_av452", None)
                if opp_val == self:
                    setattr(old_value, "qosannotations_pc_av452", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qosannotations_pc_av452"):
                opp_val = getattr(value, "qosannotations_pc_av452", None)
                setattr(value, "qosannotations_pc_av452", self)

    @property
    def pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription(self):
        return self.__pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription

    @pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription.setter
    def pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription__pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription", None)
        self.__pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FailureType454"):
                opp_val = getattr(old_value, "FailureType454", None)
                if opp_val == self:
                    setattr(old_value, "FailureType454", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FailureType454"):
                opp_val = getattr(value, "FailureType454", None)
                setattr(value, "FailureType454", self)

    def NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription method
        pass

class pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription(FailureOccurrenceDescription):

    def __init__(self, InternalAction: "InternalAction" = None, SoftwareInducedFailureType: "SoftwareInducedFailureType" = None):
        self.InternalAction = InternalAction
        self.SoftwareInducedFailureType = SoftwareInducedFailureType
        
    @property
    def InternalAction(self):
        return self.__InternalAction

    @InternalAction.setter
    def InternalAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription__InternalAction", None)
        self.__InternalAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc_av446"):
                opp_val = getattr(old_value, "seff_pc_av446", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc_av446", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc_av446"):
                opp_val = getattr(value, "seff_pc_av446", None)
                setattr(value, "seff_pc_av446", self)

    @property
    def SoftwareInducedFailureType(self):
        return self.__SoftwareInducedFailureType

    @SoftwareInducedFailureType.setter
    def SoftwareInducedFailureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription__SoftwareInducedFailureType", None)
        self.__SoftwareInducedFailureType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reliability_pc_av448"):
                opp_val = getattr(old_value, "reliability_pc_av448", None)
                if opp_val == self:
                    setattr(old_value, "reliability_pc_av448", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reliability_pc_av448"):
                opp_val = getattr(value, "reliability_pc_av448", None)
                setattr(value, "reliability_pc_av448", self)

    def NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription method
        pass

class InternalFailureOccurrenceDescription:

    pass
class ProcessingResourceType:

    pass
class EntryLevelSystemCall:

    pass
class pcm_pc_av_reliability_pc_av_FailureOccurrenceDescription:

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
class pcm_pc_av_parameter_pc_av_CharacterisedVariable(Variable):

    def __init__(self, characterisationType: str):
        self.characterisationType = characterisationType
        
    @property
    def characterisationType(self) -> str:
        return self.__characterisationType

    @characterisationType.setter
    def characterisationType(self, characterisationType: str):
        self.__characterisationType = characterisationType

class pcm_pc_av_parameter_pc_av_VariableCharacterisation:

    def __init__(self, type: str, PCMRandomVariable436: "PCMRandomVariable" = None, VariableUsage439: "VariableUsage" = None):
        self.type = type
        self.PCMRandomVariable436 = PCMRandomVariable436
        self.VariableUsage439 = VariableUsage439
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def VariableUsage439(self):
        return self.__VariableUsage439

    @VariableUsage439.setter
    def VariableUsage439(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_parameter_pc_av_VariableCharacterisation__VariableUsage439", None)
        self.__VariableUsage439 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameter_pc_av440"):
                opp_val = getattr(old_value, "parameter_pc_av440", None)
                if opp_val == self:
                    setattr(old_value, "parameter_pc_av440", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameter_pc_av440"):
                opp_val = getattr(value, "parameter_pc_av440", None)
                setattr(value, "parameter_pc_av440", self)

    @property
    def PCMRandomVariable436(self):
        return self.__PCMRandomVariable436

    @PCMRandomVariable436.setter
    def PCMRandomVariable436(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_parameter_pc_av_VariableCharacterisation__PCMRandomVariable436", None)
        self.__PCMRandomVariable436 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc_av437"):
                opp_val = getattr(old_value, "core_pc_av437", None)
                if opp_val == self:
                    setattr(old_value, "core_pc_av437", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc_av437"):
                opp_val = getattr(value, "core_pc_av437", None)
                setattr(value, "core_pc_av437", self)

class parameter_pc_av_pcm_pc_av_AbstractNamedReference:

    pass
class SpecifiedOutputParameterAbstraction:

    pass
class SetVariableAction:

    pass
class CallReturnAction:

    pass
class SynchronisationPoint:

    pass
class CallAction:

    pass
class pcm_pc_av_seff_pc_av_CallReturnAction(CallAction):

    pass
class pcm_pc_av_seff_performance_pc_av_ResourceCall(CallAction):

    def __init__(self, pcm_pc_av_seff_performance_pc_av_ResourceCall574: "ResourceSignature" = None, PCMRandomVariable577: "PCMRandomVariable" = None, AbstractInternalControlFlowAction569: "AbstractInternalControlFlowAction" = None, pcm_pc_av_seff_performance_pc_av_ResourceCall: "entity_pc_av_ResourceRequiredRole" = None, seff_pc_av417: "pcm_pc_av_parameter_pc_av_VariableUsage"):
        self.pcm_pc_av_seff_performance_pc_av_ResourceCall574 = pcm_pc_av_seff_performance_pc_av_ResourceCall574
        self.PCMRandomVariable577 = PCMRandomVariable577
        self.AbstractInternalControlFlowAction569 = AbstractInternalControlFlowAction569
        self.pcm_pc_av_seff_performance_pc_av_ResourceCall = pcm_pc_av_seff_performance_pc_av_ResourceCall
        
    @property
    def pcm_pc_av_seff_performance_pc_av_ResourceCall574(self):
        return self.__pcm_pc_av_seff_performance_pc_av_ResourceCall574

    @pcm_pc_av_seff_performance_pc_av_ResourceCall574.setter
    def pcm_pc_av_seff_performance_pc_av_ResourceCall574(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_seff_performance_pc_av_ResourceCall__pcm_pc_av_seff_performance_pc_av_ResourceCall574", None)
        self.__pcm_pc_av_seff_performance_pc_av_ResourceCall574 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceSignature575"):
                opp_val = getattr(old_value, "ResourceSignature575", None)
                if opp_val == self:
                    setattr(old_value, "ResourceSignature575", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceSignature575"):
                opp_val = getattr(value, "ResourceSignature575", None)
                setattr(value, "ResourceSignature575", self)

    @property
    def pcm_pc_av_seff_performance_pc_av_ResourceCall(self):
        return self.__pcm_pc_av_seff_performance_pc_av_ResourceCall

    @pcm_pc_av_seff_performance_pc_av_ResourceCall.setter
    def pcm_pc_av_seff_performance_pc_av_ResourceCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_seff_performance_pc_av_ResourceCall__pcm_pc_av_seff_performance_pc_av_ResourceCall", None)
        self.__pcm_pc_av_seff_performance_pc_av_ResourceCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entity_pc_av_ResourceRequiredRole572"):
                opp_val = getattr(old_value, "entity_pc_av_ResourceRequiredRole572", None)
                if opp_val == self:
                    setattr(old_value, "entity_pc_av_ResourceRequiredRole572", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entity_pc_av_ResourceRequiredRole572"):
                opp_val = getattr(value, "entity_pc_av_ResourceRequiredRole572", None)
                setattr(value, "entity_pc_av_ResourceRequiredRole572", self)

    @property
    def AbstractInternalControlFlowAction569(self):
        return self.__AbstractInternalControlFlowAction569

    @AbstractInternalControlFlowAction569.setter
    def AbstractInternalControlFlowAction569(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_seff_performance_pc_av_ResourceCall__AbstractInternalControlFlowAction569", None)
        self.__AbstractInternalControlFlowAction569 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc_av570"):
                opp_val = getattr(old_value, "seff_pc_av570", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc_av570", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc_av570"):
                opp_val = getattr(value, "seff_pc_av570", None)
                setattr(value, "seff_pc_av570", self)

    @property
    def PCMRandomVariable577(self):
        return self.__PCMRandomVariable577

    @PCMRandomVariable577.setter
    def PCMRandomVariable577(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_seff_performance_pc_av_ResourceCall__PCMRandomVariable577", None)
        self.__PCMRandomVariable577 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc_av578"):
                opp_val = getattr(old_value, "core_pc_av578", None)
                if opp_val == self:
                    setattr(old_value, "core_pc_av578", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc_av578"):
                opp_val = getattr(value, "core_pc_av578", None)
                setattr(value, "core_pc_av578", self)

    def ResourceRequiredRoleMustBeReferencedByComponent(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceRequiredRoleMustBeReferencedByComponent method
        pass

    def ResourceSignatureBelongsToResourceRequiredRole(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ResourceSignatureBelongsToResourceRequiredRole method
        pass

    def SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

class pcm_pc_av_seff_performance_pc_av_InfrastructureCall(CallAction):

    def __init__(self, pcm_pc_av_seff_performance_pc_av_InfrastructureCall: "InfrastructureSignature" = None, PCMRandomVariable561: "PCMRandomVariable" = None, AbstractInternalControlFlowAction: "AbstractInternalControlFlowAction" = None, pcm_pc_av_seff_performance_pc_av_InfrastructureCall566: "InfrastructureRequiredRole" = None, seff_pc_av417: "pcm_pc_av_parameter_pc_av_VariableUsage"):
        self.pcm_pc_av_seff_performance_pc_av_InfrastructureCall = pcm_pc_av_seff_performance_pc_av_InfrastructureCall
        self.PCMRandomVariable561 = PCMRandomVariable561
        self.AbstractInternalControlFlowAction = AbstractInternalControlFlowAction
        self.pcm_pc_av_seff_performance_pc_av_InfrastructureCall566 = pcm_pc_av_seff_performance_pc_av_InfrastructureCall566
        
    @property
    def pcm_pc_av_seff_performance_pc_av_InfrastructureCall566(self):
        return self.__pcm_pc_av_seff_performance_pc_av_InfrastructureCall566

    @pcm_pc_av_seff_performance_pc_av_InfrastructureCall566.setter
    def pcm_pc_av_seff_performance_pc_av_InfrastructureCall566(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_seff_performance_pc_av_InfrastructureCall__pcm_pc_av_seff_performance_pc_av_InfrastructureCall566", None)
        self.__pcm_pc_av_seff_performance_pc_av_InfrastructureCall566 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InfrastructureRequiredRole567"):
                opp_val = getattr(old_value, "InfrastructureRequiredRole567", None)
                if opp_val == self:
                    setattr(old_value, "InfrastructureRequiredRole567", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InfrastructureRequiredRole567"):
                opp_val = getattr(value, "InfrastructureRequiredRole567", None)
                setattr(value, "InfrastructureRequiredRole567", self)

    @property
    def pcm_pc_av_seff_performance_pc_av_InfrastructureCall(self):
        return self.__pcm_pc_av_seff_performance_pc_av_InfrastructureCall

    @pcm_pc_av_seff_performance_pc_av_InfrastructureCall.setter
    def pcm_pc_av_seff_performance_pc_av_InfrastructureCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_seff_performance_pc_av_InfrastructureCall__pcm_pc_av_seff_performance_pc_av_InfrastructureCall", None)
        self.__pcm_pc_av_seff_performance_pc_av_InfrastructureCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InfrastructureSignature559"):
                opp_val = getattr(old_value, "InfrastructureSignature559", None)
                if opp_val == self:
                    setattr(old_value, "InfrastructureSignature559", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InfrastructureSignature559"):
                opp_val = getattr(value, "InfrastructureSignature559", None)
                setattr(value, "InfrastructureSignature559", self)

    @property
    def PCMRandomVariable561(self):
        return self.__PCMRandomVariable561

    @PCMRandomVariable561.setter
    def PCMRandomVariable561(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_seff_performance_pc_av_InfrastructureCall__PCMRandomVariable561", None)
        self.__PCMRandomVariable561 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc_av562"):
                opp_val = getattr(old_value, "core_pc_av562", None)
                if opp_val == self:
                    setattr(old_value, "core_pc_av562", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc_av562"):
                opp_val = getattr(value, "core_pc_av562", None)
                setattr(value, "core_pc_av562", self)

    @property
    def AbstractInternalControlFlowAction(self):
        return self.__AbstractInternalControlFlowAction

    @AbstractInternalControlFlowAction.setter
    def AbstractInternalControlFlowAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_seff_performance_pc_av_InfrastructureCall__AbstractInternalControlFlowAction", None)
        self.__AbstractInternalControlFlowAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc_av564"):
                opp_val = getattr(old_value, "seff_pc_av564", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc_av564", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc_av564"):
                opp_val = getattr(value, "seff_pc_av564", None)
                setattr(value, "seff_pc_av564", self)

    def SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

    def SignatureMustBelongToUsedRequiredRole(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SignatureMustBelongToUsedRequiredRole method
        pass

    def ReferencedRequiredRoleMustBeRequiredByComponent(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ReferencedRequiredRoleMustBeRequiredByComponent method
        pass

class pcm_pc_av_parameter_pc_av_VariableUsage:

    pass
class pcm_pc_av_protocol_pc_av_Protocol:

    def __init__(self, protocolTypeID: str):
        self.protocolTypeID = protocolTypeID
        
    @property
    def protocolTypeID(self) -> str:
        return self.__protocolTypeID

    @protocolTypeID.setter
    def protocolTypeID(self, protocolTypeID: str):
        self.__protocolTypeID = protocolTypeID

class ResourceType:

    pass
class pcm_pc_av_resourcetype_pc_av_ProcessingResourceType(ResourceType):

    pass
class NetworkInducedFailureType:

    pass
class pcm_pc_av_resourcetype_pc_av_CommunicationLinkResourceType(ResourceType):

    pass
class NamedElement:

    pass
class pcm_pc_av_resourceenvironment_pc_av_ResourceEnvironment(NamedElement):

    pass
class pcm_pc_av_repository_pc_av_InnerDeclaration(NamedElement):

    pass
class SchedulingPolicy:

    pass
class pcm_pc_av_resourcetype_pc_av_ResourceRepository:

    pass
class ResourceRepository:

    pass
class UnitCarryingElement:

    pass
class HardwareInducedFailureType:

    pass
class repository_pc_av_ImplementationComponentType:

    pass
class entity_pc_av_ComposedProvidingRequiringEntity:

    pass
class pcm_pc_av_completions_pc_av_Completion(repository_pc_av_ImplementationComponentType, entity_pc_av_ComposedProvidingRequiringEntity):

    pass
class pcm_pc_av_subsystem_pc_av_SubSystem(repository_pc_av_RepositoryComponent, entity_pc_av_ComposedProvidingRequiringEntity):

    pass
class pcm_pc_av_repository_pc_av_CompositeComponent(repository_pc_av_ImplementationComponentType, entity_pc_av_ComposedProvidingRequiringEntity):

    def __init__(self):
        
    def RequireSameInterfaces(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement RequireSameInterfaces method
        pass

    def ProvideSameInterfaces(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ProvideSameInterfaces method
        pass

class InnerDeclaration:

    pass
class CompositeDataType:

    pass
class repository_pc_av_DataType:

    pass
class ProvidesComponentType:

    pass
class OperationInterface:

    pass
class pcm_pc_av_repository_pc_av_ExceptionType:

    def __init__(self, exceptionName: str, exceptionMessage: str):
        self.exceptionName = exceptionName
        self.exceptionMessage = exceptionMessage
        
    @property
    def exceptionMessage(self) -> str:
        return self.__exceptionMessage

    @exceptionMessage.setter
    def exceptionMessage(self, exceptionMessage: str):
        self.__exceptionMessage = exceptionMessage

    @property
    def exceptionName(self) -> str:
        return self.__exceptionName

    @exceptionName.setter
    def exceptionName(self, exceptionName: str):
        self.__exceptionName = exceptionName

class ExceptionType:

    pass
class Signature:

    pass
class pcm_pc_av_repository_pc_av_OperationSignature(Signature):

    def __init__(self, OperationInterface: "OperationInterface" = None, Parameter354: set["Parameter"] = None, pcm_pc_av_repository_pc_av_OperationSignature: "DataType" = None, Signature598: "pcm_pc_av_qosannotations_pc_av_SpecifiedQoSAnnotation", Signature: "pcm_pc_av_seff_pc_av_ServiceEffectSpecification", Signature610: "pcm_pc_av_qosannotations_pc_av_SpecifiedOutputParameterAbstraction"):
        self.OperationInterface = OperationInterface
        self.Parameter354 = Parameter354 if Parameter354 is not None else set()
        self.pcm_pc_av_repository_pc_av_OperationSignature = pcm_pc_av_repository_pc_av_OperationSignature
        
    @property
    def pcm_pc_av_repository_pc_av_OperationSignature(self):
        return self.__pcm_pc_av_repository_pc_av_OperationSignature

    @pcm_pc_av_repository_pc_av_OperationSignature.setter
    def pcm_pc_av_repository_pc_av_OperationSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_repository_pc_av_OperationSignature__pcm_pc_av_repository_pc_av_OperationSignature", None)
        self.__pcm_pc_av_repository_pc_av_OperationSignature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType357"):
                opp_val = getattr(old_value, "DataType357", None)
                if opp_val == self:
                    setattr(old_value, "DataType357", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType357"):
                opp_val = getattr(value, "DataType357", None)
                setattr(value, "DataType357", self)

    @property
    def OperationInterface(self):
        return self.__OperationInterface

    @OperationInterface.setter
    def OperationInterface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_repository_pc_av_OperationSignature__OperationInterface", None)
        self.__OperationInterface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc_av352"):
                opp_val = getattr(old_value, "repository_pc_av352", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc_av352", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc_av352"):
                opp_val = getattr(value, "repository_pc_av352", None)
                setattr(value, "repository_pc_av352", self)

    @property
    def Parameter354(self):
        return self.__Parameter354

    @Parameter354.setter
    def Parameter354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_repository_pc_av_OperationSignature__Parameter354", None)
        self.__Parameter354 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_pc_av355"):
                    opp_val = getattr(item, "repository_pc_av355", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_pc_av355", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_pc_av355"):
                    opp_val = getattr(item, "repository_pc_av355", None)
                    
                    setattr(item, "repository_pc_av355", self)
                    

    def ParameterNamesHaveToBeUniqueForASignature(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ParameterNamesHaveToBeUniqueForASignature method
        pass

class pcm_pc_av_repository_pc_av_EventType(Signature):

    pass
class InfrastructureInterface:

    pass
class pcm_pc_av_repository_pc_av_InfrastructureSignature(Signature):

    pass
class FailureType:

    pass
class pcm_pc_av_reliability_pc_av_HardwareInducedFailureType(FailureType):

    def __init__(self, ProcessingResourceType: "ProcessingResourceType" = None, FailureType596: "pcm_pc_av_seff_reliability_pc_av_FailureHandlingEntity", reliability_pc_av308: "pcm_pc_av_repository_pc_av_Repository", FailureType454: "pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription", FailureType337: "pcm_pc_av_repository_pc_av_Signature"):
        self.ProcessingResourceType = ProcessingResourceType
        
    @property
    def ProcessingResourceType(self):
        return self.__ProcessingResourceType

    @ProcessingResourceType.setter
    def ProcessingResourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_reliability_pc_av_HardwareInducedFailureType__ProcessingResourceType", None)
        self.__ProcessingResourceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcetype_pc_av442"):
                opp_val = getattr(old_value, "resourcetype_pc_av442", None)
                if opp_val == self:
                    setattr(old_value, "resourcetype_pc_av442", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcetype_pc_av442"):
                opp_val = getattr(value, "resourcetype_pc_av442", None)
                setattr(value, "resourcetype_pc_av442", self)

    def HardwareInducedFailureTypeHasProcessingResourceType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement HardwareInducedFailureTypeHasProcessingResourceType method
        pass

class pcm_pc_av_reliability_pc_av_NetworkInducedFailureType(FailureType):

    def __init__(self, CommunicationLinkResourceType: "CommunicationLinkResourceType" = None, FailureType596: "pcm_pc_av_seff_reliability_pc_av_FailureHandlingEntity", reliability_pc_av308: "pcm_pc_av_repository_pc_av_Repository", FailureType454: "pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription", FailureType337: "pcm_pc_av_repository_pc_av_Signature"):
        self.CommunicationLinkResourceType = CommunicationLinkResourceType
        
    @property
    def CommunicationLinkResourceType(self):
        return self.__CommunicationLinkResourceType

    @CommunicationLinkResourceType.setter
    def CommunicationLinkResourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_reliability_pc_av_NetworkInducedFailureType__CommunicationLinkResourceType", None)
        self.__CommunicationLinkResourceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcetype_pc_av450"):
                opp_val = getattr(old_value, "resourcetype_pc_av450", None)
                if opp_val == self:
                    setattr(old_value, "resourcetype_pc_av450", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcetype_pc_av450"):
                opp_val = getattr(value, "resourcetype_pc_av450", None)
                setattr(value, "resourcetype_pc_av450", self)

    def NetworkInducedFailureTypeHasCommunicationLinkResourceType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement NetworkInducedFailureTypeHasCommunicationLinkResourceType method
        pass

class pcm_pc_av_reliability_pc_av_SoftwareInducedFailureType(FailureType):

    pass
class Interface:

    pass
class pcm_pc_av_repository_pc_av_OperationInterface(Interface):

    def __init__(self, OperationSignature359: set["OperationSignature"] = None, repository_pc_av306: "pcm_pc_av_repository_pc_av_Repository", Interface313: "pcm_pc_av_repository_pc_av_Interface", repository_pc_av324: "pcm_pc_av_repository_pc_av_RequiredCharacterisation"):
        self.OperationSignature359 = OperationSignature359 if OperationSignature359 is not None else set()
        
    @property
    def OperationSignature359(self):
        return self.__OperationSignature359

    @OperationSignature359.setter
    def OperationSignature359(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_repository_pc_av_OperationInterface__OperationSignature359", None)
        self.__OperationSignature359 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_pc_av360"):
                    opp_val = getattr(item, "repository_pc_av360", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_pc_av360", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_pc_av360"):
                    opp_val = getattr(item, "repository_pc_av360", None)
                    
                    setattr(item, "repository_pc_av360", self)
                    

    def SignaturesHaveToBeUniqueForAnInterface(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SignaturesHaveToBeUniqueForAnInterface method
        pass

class pcm_pc_av_repository_pc_av_EventGroup(Interface):

    pass
class pcm_pc_av_repository_pc_av_InfrastructureInterface(Interface):

    pass
class Parameter:

    pass
class pcm_pc_av_repository_pc_av_RequiredCharacterisation:

    def __init__(self, type: str, pcm_pc_av_repository_pc_av_RequiredCharacterisation: "Parameter" = None, Interface323: "Interface" = None):
        self.type = type
        self.pcm_pc_av_repository_pc_av_RequiredCharacterisation = pcm_pc_av_repository_pc_av_RequiredCharacterisation
        self.Interface323 = Interface323
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def pcm_pc_av_repository_pc_av_RequiredCharacterisation(self):
        return self.__pcm_pc_av_repository_pc_av_RequiredCharacterisation

    @pcm_pc_av_repository_pc_av_RequiredCharacterisation.setter
    def pcm_pc_av_repository_pc_av_RequiredCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_repository_pc_av_RequiredCharacterisation__pcm_pc_av_repository_pc_av_RequiredCharacterisation", None)
        self.__pcm_pc_av_repository_pc_av_RequiredCharacterisation = value
        
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

    @property
    def Interface323(self):
        return self.__Interface323

    @Interface323.setter
    def Interface323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_repository_pc_av_RequiredCharacterisation__Interface323", None)
        self.__Interface323 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc_av324"):
                opp_val = getattr(old_value, "repository_pc_av324", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc_av324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc_av324"):
                opp_val = getattr(value, "repository_pc_av324", None)
                setattr(value, "repository_pc_av324", self)

class RequiredCharacterisation:

    pass
class Protocol:

    pass
class EventType:

    pass
class InfrastructureSignature:

    pass
class DataType:

    pass
class pcm_pc_av_repository_pc_av_PrimitiveDataType(DataType):

    def __init__(self, type: str, DataType: "pcm_pc_av_repository_pc_av_Parameter", DataType378: "pcm_pc_av_repository_pc_av_InnerDeclaration", DataType357: "pcm_pc_av_repository_pc_av_OperationSignature", repository_pc_av311: "pcm_pc_av_repository_pc_av_Repository", DataType373: "pcm_pc_av_repository_pc_av_CollectionDataType"):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class pcm_pc_av_repository_pc_av_Parameter:

    def __init__(self, modifier__Parameter: str, parameterName: str, ResourceSignature: "ResourceSignature" = None, pcm_pc_av_repository_pc_av_Parameter: "DataType" = None, InfrastructureSignature: "InfrastructureSignature" = None, OperationSignature294: "OperationSignature" = None, EventType: "EventType" = None):
        self.modifier__Parameter = modifier__Parameter
        self.parameterName = parameterName
        self.ResourceSignature = ResourceSignature
        self.pcm_pc_av_repository_pc_av_Parameter = pcm_pc_av_repository_pc_av_Parameter
        self.InfrastructureSignature = InfrastructureSignature
        self.OperationSignature294 = OperationSignature294
        self.EventType = EventType
        
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
    def InfrastructureSignature(self):
        return self.__InfrastructureSignature

    @InfrastructureSignature.setter
    def InfrastructureSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_repository_pc_av_Parameter__InfrastructureSignature", None)
        self.__InfrastructureSignature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc_av292"):
                opp_val = getattr(old_value, "repository_pc_av292", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc_av292", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc_av292"):
                opp_val = getattr(value, "repository_pc_av292", None)
                setattr(value, "repository_pc_av292", self)

    @property
    def EventType(self):
        return self.__EventType

    @EventType.setter
    def EventType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_repository_pc_av_Parameter__EventType", None)
        self.__EventType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc_av297"):
                opp_val = getattr(old_value, "repository_pc_av297", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc_av297", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc_av297"):
                opp_val = getattr(value, "repository_pc_av297", None)
                setattr(value, "repository_pc_av297", self)

    @property
    def ResourceSignature(self):
        return self.__ResourceSignature

    @ResourceSignature.setter
    def ResourceSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_repository_pc_av_Parameter__ResourceSignature", None)
        self.__ResourceSignature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcetype_pc_av"):
                opp_val = getattr(old_value, "resourcetype_pc_av", None)
                if opp_val == self:
                    setattr(old_value, "resourcetype_pc_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcetype_pc_av"):
                opp_val = getattr(value, "resourcetype_pc_av", None)
                setattr(value, "resourcetype_pc_av", self)

    @property
    def pcm_pc_av_repository_pc_av_Parameter(self):
        return self.__pcm_pc_av_repository_pc_av_Parameter

    @pcm_pc_av_repository_pc_av_Parameter.setter
    def pcm_pc_av_repository_pc_av_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_repository_pc_av_Parameter__pcm_pc_av_repository_pc_av_Parameter", None)
        self.__pcm_pc_av_repository_pc_av_Parameter = value
        
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
    def OperationSignature294(self):
        return self.__OperationSignature294

    @OperationSignature294.setter
    def OperationSignature294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_repository_pc_av_Parameter__OperationSignature294", None)
        self.__OperationSignature294 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc_av295"):
                opp_val = getattr(old_value, "repository_pc_av295", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc_av295", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc_av295"):
                opp_val = getattr(value, "repository_pc_av295", None)
                setattr(value, "repository_pc_av295", self)

class Repository:

    pass
class InterfaceProvidingRequiringEntity:

    pass
class pcm_pc_av_repository_pc_av_RepositoryComponent(InterfaceProvidingRequiringEntity):

    pass
class pcm_pc_av_repository_pc_av_DataType:

    pass
class ResourceSignature:

    pass
class ServiceEffectSpecification:

    pass
class CompleteComponentType:

    pass
class ImplementationComponentType:

    pass
class pcm_pc_av_repository_pc_av_BasicComponent(ImplementationComponentType):

    def __init__(self, ServiceEffectSpecification: set["ServiceEffectSpecification"] = None, PassiveResource279: set["PassiveResource"] = None):
        self.ServiceEffectSpecification = ServiceEffectSpecification if ServiceEffectSpecification is not None else set()
        self.PassiveResource279 = PassiveResource279 if PassiveResource279 is not None else set()
        
    @property
    def PassiveResource279(self):
        return self.__PassiveResource279

    @PassiveResource279.setter
    def PassiveResource279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_repository_pc_av_BasicComponent__PassiveResource279", None)
        self.__PassiveResource279 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_pc_av280"):
                    opp_val = getattr(item, "repository_pc_av280", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_pc_av280", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_pc_av280"):
                    opp_val = getattr(item, "repository_pc_av280", None)
                    
                    setattr(item, "repository_pc_av280", self)
                    

    @property
    def ServiceEffectSpecification(self):
        return self.__ServiceEffectSpecification

    @ServiceEffectSpecification.setter
    def ServiceEffectSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_repository_pc_av_BasicComponent__ServiceEffectSpecification", None)
        self.__ServiceEffectSpecification = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_pc_av277"):
                    opp_val = getattr(item, "seff_pc_av277", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_pc_av277", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_pc_av277"):
                    opp_val = getattr(item, "seff_pc_av277", None)
                    
                    setattr(item, "seff_pc_av277", self)
                    

    def NoSeffTypeUsedTwice(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement NoSeffTypeUsedTwice method
        pass

    def RequireSameInterfacesAsImplementationType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RequireSameInterfacesAsImplementationType method
        pass

    def ProvideSameInterfacesAsImplementationType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ProvideSameInterfacesAsImplementationType method
        pass

class ResourceTimeoutFailureType:

    pass
class BasicComponent:

    pass
class Branch:

    pass
class pcm_pc_av_usagemodel_pc_av_BranchTransition:

    def __init__(self, branchProbability: float, Branch: "Branch" = None, ScenarioBehaviour250: "ScenarioBehaviour" = None):
        self.branchProbability = branchProbability
        self.Branch = Branch
        self.ScenarioBehaviour250 = ScenarioBehaviour250
        
    @property
    def branchProbability(self) -> float:
        return self.__branchProbability

    @branchProbability.setter
    def branchProbability(self, branchProbability: float):
        self.__branchProbability = branchProbability

    @property
    def ScenarioBehaviour250(self):
        return self.__ScenarioBehaviour250

    @ScenarioBehaviour250.setter
    def ScenarioBehaviour250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_usagemodel_pc_av_BranchTransition__ScenarioBehaviour250", None)
        self.__ScenarioBehaviour250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc_av251"):
                opp_val = getattr(old_value, "usagemodel_pc_av251", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc_av251", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc_av251"):
                opp_val = getattr(value, "usagemodel_pc_av251", None)
                setattr(value, "usagemodel_pc_av251", self)

    @property
    def Branch(self):
        return self.__Branch

    @Branch.setter
    def Branch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_usagemodel_pc_av_BranchTransition__Branch", None)
        self.__Branch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc_av248"):
                opp_val = getattr(old_value, "usagemodel_pc_av248", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc_av248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc_av248"):
                opp_val = getattr(value, "usagemodel_pc_av248", None)
                setattr(value, "usagemodel_pc_av248", self)

class BranchTransition:

    pass
class AbstractUserAction:

    pass
class pcm_pc_av_usagemodel_pc_av_Loop(AbstractUserAction):

    pass
class pcm_pc_av_usagemodel_pc_av_Start(AbstractUserAction):

    def __init__(self, usagemodel_pc_av229: "pcm_pc_av_usagemodel_pc_av_AbstractUserAction", usagemodel_pc_av232: "pcm_pc_av_usagemodel_pc_av_AbstractUserAction", usagemodel_pc_av246: "pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour"):
        
    def StartHasNoPredecessor(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement StartHasNoPredecessor method
        pass

class pcm_pc_av_usagemodel_pc_av_Delay(AbstractUserAction):

    pass
class pcm_pc_av_usagemodel_pc_av_Branch(AbstractUserAction):

    def __init__(self, BranchTransition253: set["BranchTransition"] = None, usagemodel_pc_av229: "pcm_pc_av_usagemodel_pc_av_AbstractUserAction", usagemodel_pc_av232: "pcm_pc_av_usagemodel_pc_av_AbstractUserAction", usagemodel_pc_av246: "pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour"):
        self.BranchTransition253 = BranchTransition253 if BranchTransition253 is not None else set()
        
    @property
    def BranchTransition253(self):
        return self.__BranchTransition253

    @BranchTransition253.setter
    def BranchTransition253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_usagemodel_pc_av_Branch__BranchTransition253", None)
        self.__BranchTransition253 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "usagemodel_pc_av254"):
                    opp_val = getattr(item, "usagemodel_pc_av254", None)
                    
                    if opp_val == self:
                        setattr(item, "usagemodel_pc_av254", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "usagemodel_pc_av254"):
                    opp_val = getattr(item, "usagemodel_pc_av254", None)
                    
                    setattr(item, "usagemodel_pc_av254", self)
                    

    def AllBranchProbabilitiesMustSumUpTo1(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AllBranchProbabilitiesMustSumUpTo1 method
        pass

class pcm_pc_av_usagemodel_pc_av_Stop(AbstractUserAction):

    def __init__(self, usagemodel_pc_av229: "pcm_pc_av_usagemodel_pc_av_AbstractUserAction", usagemodel_pc_av232: "pcm_pc_av_usagemodel_pc_av_AbstractUserAction", usagemodel_pc_av246: "pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour"):
        
    def StopHasNoSuccessor(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement StopHasNoSuccessor method
        pass

class pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall(AbstractUserAction):

    def __init__(self, priority: int, pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall: "OperationProvidedRole" = None, pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall221: "OperationSignature" = None, VariableUsage223: set["VariableUsage"] = None, VariableUsage226: set["VariableUsage"] = None, usagemodel_pc_av229: "pcm_pc_av_usagemodel_pc_av_AbstractUserAction", usagemodel_pc_av232: "pcm_pc_av_usagemodel_pc_av_AbstractUserAction", usagemodel_pc_av246: "pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour"):
        self.priority = priority
        self.pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall = pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall
        self.pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall221 = pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall221
        self.VariableUsage223 = VariableUsage223 if VariableUsage223 is not None else set()
        self.VariableUsage226 = VariableUsage226 if VariableUsage226 is not None else set()
        
    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall221(self):
        return self.__pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall221

    @pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall221.setter
    def pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall__pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall221", None)
        self.__pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall221 = value
        
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
    def pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall(self):
        return self.__pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall

    @pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall.setter
    def pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall__pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall", None)
        self.__pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationProvidedRole219"):
                opp_val = getattr(old_value, "OperationProvidedRole219", None)
                if opp_val == self:
                    setattr(old_value, "OperationProvidedRole219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationProvidedRole219"):
                opp_val = getattr(value, "OperationProvidedRole219", None)
                setattr(value, "OperationProvidedRole219", self)

    @property
    def VariableUsage226(self):
        return self.__VariableUsage226

    @VariableUsage226.setter
    def VariableUsage226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall__VariableUsage226", None)
        self.__VariableUsage226 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "parameter_pc_av227"):
                    opp_val = getattr(item, "parameter_pc_av227", None)
                    
                    if opp_val == self:
                        setattr(item, "parameter_pc_av227", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "parameter_pc_av227"):
                    opp_val = getattr(item, "parameter_pc_av227", None)
                    
                    setattr(item, "parameter_pc_av227", self)
                    

    @property
    def VariableUsage223(self):
        return self.__VariableUsage223

    @VariableUsage223.setter
    def VariableUsage223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall__VariableUsage223", None)
        self.__VariableUsage223 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "parameter_pc_av224"):
                    opp_val = getattr(item, "parameter_pc_av224", None)
                    
                    if opp_val == self:
                        setattr(item, "parameter_pc_av224", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "parameter_pc_av224"):
                    opp_val = getattr(item, "parameter_pc_av224", None)
                    
                    setattr(item, "parameter_pc_av224", self)
                    

    def EntryLevelSystemCallMustReferenceProvidedRoleOfASystem(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement EntryLevelSystemCallMustReferenceProvidedRoleOfASystem method
        pass

    def EntryLevelSystemCallSignatureMustMatchItsProvidedRole(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement EntryLevelSystemCallSignatureMustMatchItsProvidedRole method
        pass

class UserData:

    pass
class pcm_pc_av_usagemodel_pc_av_UsageModel:

    pass
class pcm_pc_av_usagemodel_pc_av_UserData:

    pass
class Workload:

    pass
class pcm_pc_av_usagemodel_pc_av_OpenWorkload(Workload):

    def __init__(self, PCMRandomVariable262: "PCMRandomVariable" = None, usagemodel_pc_av204: "pcm_pc_av_usagemodel_pc_av_UsageScenario"):
        self.PCMRandomVariable262 = PCMRandomVariable262
        
    @property
    def PCMRandomVariable262(self):
        return self.__PCMRandomVariable262

    @PCMRandomVariable262.setter
    def PCMRandomVariable262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_usagemodel_pc_av_OpenWorkload__PCMRandomVariable262", None)
        self.__PCMRandomVariable262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc_av263"):
                opp_val = getattr(old_value, "core_pc_av263", None)
                if opp_val == self:
                    setattr(old_value, "core_pc_av263", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc_av263"):
                opp_val = getattr(value, "core_pc_av263", None)
                setattr(value, "core_pc_av263", self)

    def InterArrivalTimeInOpenWorkloadNeedsToBeSpecified(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement InterArrivalTimeInOpenWorkloadNeedsToBeSpecified method
        pass

class pcm_pc_av_usagemodel_pc_av_ClosedWorkload(Workload):

    def __init__(self, population: int, PCMRandomVariable268: "PCMRandomVariable" = None, usagemodel_pc_av204: "pcm_pc_av_usagemodel_pc_av_UsageScenario"):
        self.population = population
        self.PCMRandomVariable268 = PCMRandomVariable268
        
    @property
    def population(self) -> int:
        return self.__population

    @population.setter
    def population(self, population: int):
        self.__population = population

    @property
    def PCMRandomVariable268(self):
        return self.__PCMRandomVariable268

    @PCMRandomVariable268.setter
    def PCMRandomVariable268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_usagemodel_pc_av_ClosedWorkload__PCMRandomVariable268", None)
        self.__PCMRandomVariable268 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc_av269"):
                opp_val = getattr(old_value, "core_pc_av269", None)
                if opp_val == self:
                    setattr(old_value, "core_pc_av269", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc_av269"):
                opp_val = getattr(value, "core_pc_av269", None)
                setattr(value, "core_pc_av269", self)

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
class OperationSignature:

    pass
class InfrastructureRequiredRole:

    pass
class InfrastructureProvidedRole:

    pass
class UsageScenario:

    pass
class pcm_pc_av_usagemodel_pc_av_Workload:

    pass
class VariableUsage:

    pass
class RepositoryComponent:

    pass
class pcm_pc_av_repository_pc_av_ImplementationComponentType(RepositoryComponent):

    def __init__(self, componentType: str, pcm_pc_av_repository_pc_av_ImplementationComponentType: set["CompleteComponentType"] = None, pcm_pc_av_repository_pc_av_ImplementationComponentType283: set["VariableUsage"] = None, RepositoryComponent: "pcm_pc_av_composition_pc_av_AssemblyContext", repository_pc_av304: "pcm_pc_av_repository_pc_av_Repository"):
        self.componentType = componentType
        self.pcm_pc_av_repository_pc_av_ImplementationComponentType = pcm_pc_av_repository_pc_av_ImplementationComponentType if pcm_pc_av_repository_pc_av_ImplementationComponentType is not None else set()
        self.pcm_pc_av_repository_pc_av_ImplementationComponentType283 = pcm_pc_av_repository_pc_av_ImplementationComponentType283 if pcm_pc_av_repository_pc_av_ImplementationComponentType283 is not None else set()
        
    @property
    def componentType(self) -> str:
        return self.__componentType

    @componentType.setter
    def componentType(self, componentType: str):
        self.__componentType = componentType

    @property
    def pcm_pc_av_repository_pc_av_ImplementationComponentType(self):
        return self.__pcm_pc_av_repository_pc_av_ImplementationComponentType

    @pcm_pc_av_repository_pc_av_ImplementationComponentType.setter
    def pcm_pc_av_repository_pc_av_ImplementationComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_repository_pc_av_ImplementationComponentType__pcm_pc_av_repository_pc_av_ImplementationComponentType", None)
        self.__pcm_pc_av_repository_pc_av_ImplementationComponentType = value if value is not None else set()
        
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
    def pcm_pc_av_repository_pc_av_ImplementationComponentType283(self):
        return self.__pcm_pc_av_repository_pc_av_ImplementationComponentType283

    @pcm_pc_av_repository_pc_av_ImplementationComponentType283.setter
    def pcm_pc_av_repository_pc_av_ImplementationComponentType283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_repository_pc_av_ImplementationComponentType__pcm_pc_av_repository_pc_av_ImplementationComponentType283", None)
        self.__pcm_pc_av_repository_pc_av_ImplementationComponentType283 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableUsage284"):
                    opp_val = getattr(item, "VariableUsage284", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableUsage284", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableUsage284"):
                    opp_val = getattr(item, "VariableUsage284", None)
                    
                    setattr(item, "VariableUsage284", self)
                    

    def RequiredInterfacesHaveToConformToCompleteType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RequiredInterfacesHaveToConformToCompleteType method
        pass

    def providedInterfacesHaveToConformToCompleteType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement providedInterfacesHaveToConformToCompleteType method
        pass

    def ProvidedInterfaceHaveToConformToComponentType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ProvidedInterfaceHaveToConformToComponentType method
        pass

class pcm_pc_av_repository_pc_av_ProvidesComponentType(RepositoryComponent):

    def __init__(self, RepositoryComponent: "pcm_pc_av_composition_pc_av_AssemblyContext", repository_pc_av304: "pcm_pc_av_repository_pc_av_Repository"):
        
    def AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType method
        pass

class pcm_pc_av_repository_pc_av_CompleteComponentType(RepositoryComponent):

    def __init__(self, pcm_pc_av_repository_pc_av_CompleteComponentType: set["ProvidesComponentType"] = None, RepositoryComponent: "pcm_pc_av_composition_pc_av_AssemblyContext", repository_pc_av304: "pcm_pc_av_repository_pc_av_Repository"):
        self.pcm_pc_av_repository_pc_av_CompleteComponentType = pcm_pc_av_repository_pc_av_CompleteComponentType if pcm_pc_av_repository_pc_av_CompleteComponentType is not None else set()
        
    @property
    def pcm_pc_av_repository_pc_av_CompleteComponentType(self):
        return self.__pcm_pc_av_repository_pc_av_CompleteComponentType

    @pcm_pc_av_repository_pc_av_CompleteComponentType.setter
    def pcm_pc_av_repository_pc_av_CompleteComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_repository_pc_av_CompleteComponentType__pcm_pc_av_repository_pc_av_CompleteComponentType", None)
        self.__pcm_pc_av_repository_pc_av_CompleteComponentType = value if value is not None else set()
        
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
                    

    def AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType method
        pass

    def providedInterfacesHaveToConformToProvidedType2(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement providedInterfacesHaveToConformToProvidedType2 method
        pass

class OperationProvidedRole:

    pass
class OperationRequiredRole:

    pass
class SourceRole:

    pass
class composition_pc_av_EventChannelSourceConnector:

    pass
class EventGroup:

    pass
class pcm_pc_av_composition_pc_av_ResourceRequiredDelegationConnector:

    pass
class composition_pc_av_Connector:

    pass
class DelegationConnector:

    pass
class pcm_pc_av_composition_pc_av_SinkDelegationConnector(DelegationConnector):

    pass
class pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector(DelegationConnector):

    pass
class pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector(DelegationConnector):

    pass
class pcm_pc_av_composition_pc_av_SourceDelegationConnector(DelegationConnector):

    pass
class pcm_pc_av_composition_pc_av_RequiredDelegationConnector(DelegationConnector):

    def __init__(self, pcm_pc_av_composition_pc_av_RequiredDelegationConnector: "OperationRequiredRole" = None, pcm_pc_av_composition_pc_av_RequiredDelegationConnector112: "OperationRequiredRole" = None, pcm_pc_av_composition_pc_av_RequiredDelegationConnector115: "composition_pc_av_AssemblyContext" = None):
        self.pcm_pc_av_composition_pc_av_RequiredDelegationConnector = pcm_pc_av_composition_pc_av_RequiredDelegationConnector
        self.pcm_pc_av_composition_pc_av_RequiredDelegationConnector112 = pcm_pc_av_composition_pc_av_RequiredDelegationConnector112
        self.pcm_pc_av_composition_pc_av_RequiredDelegationConnector115 = pcm_pc_av_composition_pc_av_RequiredDelegationConnector115
        
    @property
    def pcm_pc_av_composition_pc_av_RequiredDelegationConnector(self):
        return self.__pcm_pc_av_composition_pc_av_RequiredDelegationConnector

    @pcm_pc_av_composition_pc_av_RequiredDelegationConnector.setter
    def pcm_pc_av_composition_pc_av_RequiredDelegationConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_composition_pc_av_RequiredDelegationConnector__pcm_pc_av_composition_pc_av_RequiredDelegationConnector", None)
        self.__pcm_pc_av_composition_pc_av_RequiredDelegationConnector = value
        
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
    def pcm_pc_av_composition_pc_av_RequiredDelegationConnector115(self):
        return self.__pcm_pc_av_composition_pc_av_RequiredDelegationConnector115

    @pcm_pc_av_composition_pc_av_RequiredDelegationConnector115.setter
    def pcm_pc_av_composition_pc_av_RequiredDelegationConnector115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_composition_pc_av_RequiredDelegationConnector__pcm_pc_av_composition_pc_av_RequiredDelegationConnector115", None)
        self.__pcm_pc_av_composition_pc_av_RequiredDelegationConnector115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_pc_av_AssemblyContext116"):
                opp_val = getattr(old_value, "composition_pc_av_AssemblyContext116", None)
                if opp_val == self:
                    setattr(old_value, "composition_pc_av_AssemblyContext116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_pc_av_AssemblyContext116"):
                opp_val = getattr(value, "composition_pc_av_AssemblyContext116", None)
                setattr(value, "composition_pc_av_AssemblyContext116", self)

    @property
    def pcm_pc_av_composition_pc_av_RequiredDelegationConnector112(self):
        return self.__pcm_pc_av_composition_pc_av_RequiredDelegationConnector112

    @pcm_pc_av_composition_pc_av_RequiredDelegationConnector112.setter
    def pcm_pc_av_composition_pc_av_RequiredDelegationConnector112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_composition_pc_av_RequiredDelegationConnector__pcm_pc_av_composition_pc_av_RequiredDelegationConnector112", None)
        self.__pcm_pc_av_composition_pc_av_RequiredDelegationConnector112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationRequiredRole113"):
                opp_val = getattr(old_value, "OperationRequiredRole113", None)
                if opp_val == self:
                    setattr(old_value, "OperationRequiredRole113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationRequiredRole113"):
                opp_val = getattr(value, "OperationRequiredRole113", None)
                setattr(value, "OperationRequiredRole113", self)

    def ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame method
        pass

    def RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector method
        pass

    def RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

class pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector(DelegationConnector):

    pass
class pcm_pc_av_composition_pc_av_ProvidedDelegationConnector(DelegationConnector):

    def __init__(self, pcm_pc_av_composition_pc_av_ProvidedDelegationConnector: "OperationProvidedRole" = None, pcm_pc_av_composition_pc_av_ProvidedDelegationConnector105: "OperationProvidedRole" = None, pcm_pc_av_composition_pc_av_ProvidedDelegationConnector108: "composition_pc_av_AssemblyContext" = None):
        self.pcm_pc_av_composition_pc_av_ProvidedDelegationConnector = pcm_pc_av_composition_pc_av_ProvidedDelegationConnector
        self.pcm_pc_av_composition_pc_av_ProvidedDelegationConnector105 = pcm_pc_av_composition_pc_av_ProvidedDelegationConnector105
        self.pcm_pc_av_composition_pc_av_ProvidedDelegationConnector108 = pcm_pc_av_composition_pc_av_ProvidedDelegationConnector108
        
    @property
    def pcm_pc_av_composition_pc_av_ProvidedDelegationConnector105(self):
        return self.__pcm_pc_av_composition_pc_av_ProvidedDelegationConnector105

    @pcm_pc_av_composition_pc_av_ProvidedDelegationConnector105.setter
    def pcm_pc_av_composition_pc_av_ProvidedDelegationConnector105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_composition_pc_av_ProvidedDelegationConnector__pcm_pc_av_composition_pc_av_ProvidedDelegationConnector105", None)
        self.__pcm_pc_av_composition_pc_av_ProvidedDelegationConnector105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationProvidedRole106"):
                opp_val = getattr(old_value, "OperationProvidedRole106", None)
                if opp_val == self:
                    setattr(old_value, "OperationProvidedRole106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationProvidedRole106"):
                opp_val = getattr(value, "OperationProvidedRole106", None)
                setattr(value, "OperationProvidedRole106", self)

    @property
    def pcm_pc_av_composition_pc_av_ProvidedDelegationConnector108(self):
        return self.__pcm_pc_av_composition_pc_av_ProvidedDelegationConnector108

    @pcm_pc_av_composition_pc_av_ProvidedDelegationConnector108.setter
    def pcm_pc_av_composition_pc_av_ProvidedDelegationConnector108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_composition_pc_av_ProvidedDelegationConnector__pcm_pc_av_composition_pc_av_ProvidedDelegationConnector108", None)
        self.__pcm_pc_av_composition_pc_av_ProvidedDelegationConnector108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_pc_av_AssemblyContext109"):
                opp_val = getattr(old_value, "composition_pc_av_AssemblyContext109", None)
                if opp_val == self:
                    setattr(old_value, "composition_pc_av_AssemblyContext109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_pc_av_AssemblyContext109"):
                opp_val = getattr(value, "composition_pc_av_AssemblyContext109", None)
                setattr(value, "composition_pc_av_AssemblyContext109", self)

    @property
    def pcm_pc_av_composition_pc_av_ProvidedDelegationConnector(self):
        return self.__pcm_pc_av_composition_pc_av_ProvidedDelegationConnector

    @pcm_pc_av_composition_pc_av_ProvidedDelegationConnector.setter
    def pcm_pc_av_composition_pc_av_ProvidedDelegationConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_composition_pc_av_ProvidedDelegationConnector__pcm_pc_av_composition_pc_av_ProvidedDelegationConnector", None)
        self.__pcm_pc_av_composition_pc_av_ProvidedDelegationConnector = value
        
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

    def ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame method
        pass

    def ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

class PCMRandomVariable:

    pass
class SinkRole:

    pass
class Connector:

    pass
class pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector(Connector):

    pass
class pcm_pc_av_composition_pc_av_EventChannelSourceConnector(Connector):

    pass
class pcm_pc_av_composition_pc_av_AssemblyEventConnector(Connector):

    pass
class pcm_pc_av_composition_pc_av_EventChannelSinkConnector(Connector):

    pass
class pcm_pc_av_composition_pc_av_AssemblyConnector(Connector):

    def __init__(self, pcm_pc_av_composition_pc_av_AssemblyConnector: "composition_pc_av_AssemblyContext" = None, pcm_pc_av_composition_pc_av_AssemblyConnector120: "composition_pc_av_AssemblyContext" = None, pcm_pc_av_composition_pc_av_AssemblyConnector123: "OperationProvidedRole" = None, pcm_pc_av_composition_pc_av_AssemblyConnector126: "OperationRequiredRole" = None):
        self.pcm_pc_av_composition_pc_av_AssemblyConnector = pcm_pc_av_composition_pc_av_AssemblyConnector
        self.pcm_pc_av_composition_pc_av_AssemblyConnector120 = pcm_pc_av_composition_pc_av_AssemblyConnector120
        self.pcm_pc_av_composition_pc_av_AssemblyConnector123 = pcm_pc_av_composition_pc_av_AssemblyConnector123
        self.pcm_pc_av_composition_pc_av_AssemblyConnector126 = pcm_pc_av_composition_pc_av_AssemblyConnector126
        
    @property
    def pcm_pc_av_composition_pc_av_AssemblyConnector123(self):
        return self.__pcm_pc_av_composition_pc_av_AssemblyConnector123

    @pcm_pc_av_composition_pc_av_AssemblyConnector123.setter
    def pcm_pc_av_composition_pc_av_AssemblyConnector123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_composition_pc_av_AssemblyConnector__pcm_pc_av_composition_pc_av_AssemblyConnector123", None)
        self.__pcm_pc_av_composition_pc_av_AssemblyConnector123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationProvidedRole124"):
                opp_val = getattr(old_value, "OperationProvidedRole124", None)
                if opp_val == self:
                    setattr(old_value, "OperationProvidedRole124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationProvidedRole124"):
                opp_val = getattr(value, "OperationProvidedRole124", None)
                setattr(value, "OperationProvidedRole124", self)

    @property
    def pcm_pc_av_composition_pc_av_AssemblyConnector(self):
        return self.__pcm_pc_av_composition_pc_av_AssemblyConnector

    @pcm_pc_av_composition_pc_av_AssemblyConnector.setter
    def pcm_pc_av_composition_pc_av_AssemblyConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_composition_pc_av_AssemblyConnector__pcm_pc_av_composition_pc_av_AssemblyConnector", None)
        self.__pcm_pc_av_composition_pc_av_AssemblyConnector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_pc_av_AssemblyContext118"):
                opp_val = getattr(old_value, "composition_pc_av_AssemblyContext118", None)
                if opp_val == self:
                    setattr(old_value, "composition_pc_av_AssemblyContext118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_pc_av_AssemblyContext118"):
                opp_val = getattr(value, "composition_pc_av_AssemblyContext118", None)
                setattr(value, "composition_pc_av_AssemblyContext118", self)

    @property
    def pcm_pc_av_composition_pc_av_AssemblyConnector120(self):
        return self.__pcm_pc_av_composition_pc_av_AssemblyConnector120

    @pcm_pc_av_composition_pc_av_AssemblyConnector120.setter
    def pcm_pc_av_composition_pc_av_AssemblyConnector120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_composition_pc_av_AssemblyConnector__pcm_pc_av_composition_pc_av_AssemblyConnector120", None)
        self.__pcm_pc_av_composition_pc_av_AssemblyConnector120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_pc_av_AssemblyContext121"):
                opp_val = getattr(old_value, "composition_pc_av_AssemblyContext121", None)
                if opp_val == self:
                    setattr(old_value, "composition_pc_av_AssemblyContext121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_pc_av_AssemblyContext121"):
                opp_val = getattr(value, "composition_pc_av_AssemblyContext121", None)
                setattr(value, "composition_pc_av_AssemblyContext121", self)

    @property
    def pcm_pc_av_composition_pc_av_AssemblyConnector126(self):
        return self.__pcm_pc_av_composition_pc_av_AssemblyConnector126

    @pcm_pc_av_composition_pc_av_AssemblyConnector126.setter
    def pcm_pc_av_composition_pc_av_AssemblyConnector126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_composition_pc_av_AssemblyConnector__pcm_pc_av_composition_pc_av_AssemblyConnector126", None)
        self.__pcm_pc_av_composition_pc_av_AssemblyConnector126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationRequiredRole127"):
                opp_val = getattr(old_value, "OperationRequiredRole127", None)
                if opp_val == self:
                    setattr(old_value, "OperationRequiredRole127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationRequiredRole127"):
                opp_val = getattr(value, "OperationRequiredRole127", None)
                setattr(value, "OperationRequiredRole127", self)

    def AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch method
        pass

    def AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch method
        pass

    def AssemblyConnectorsReferencedInterfacesMustMatch(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AssemblyConnectorsReferencedInterfacesMustMatch method
        pass

class pcm_pc_av_composition_pc_av_DelegationConnector(Connector):

    pass
class entity_pc_av_NamedElement:

    pass
class Identifier:

    pass
class pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour(Identifier):

    def __init__(self, AbstractLoopAction: "AbstractLoopAction" = None, AbstractAction482: set["AbstractAction"] = None, AbstractBranchTransition: "AbstractBranchTransition" = None):
        self.AbstractLoopAction = AbstractLoopAction
        self.AbstractAction482 = AbstractAction482 if AbstractAction482 is not None else set()
        self.AbstractBranchTransition = AbstractBranchTransition
        
    @property
    def AbstractAction482(self):
        return self.__AbstractAction482

    @AbstractAction482.setter
    def AbstractAction482(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour__AbstractAction482", None)
        self.__AbstractAction482 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_pc_av483"):
                    opp_val = getattr(item, "seff_pc_av483", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_pc_av483", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_pc_av483"):
                    opp_val = getattr(item, "seff_pc_av483", None)
                    
                    setattr(item, "seff_pc_av483", self)
                    

    @property
    def AbstractBranchTransition(self):
        return self.__AbstractBranchTransition

    @AbstractBranchTransition.setter
    def AbstractBranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour__AbstractBranchTransition", None)
        self.__AbstractBranchTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc_av480"):
                opp_val = getattr(old_value, "seff_pc_av480", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc_av480", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc_av480"):
                opp_val = getattr(value, "seff_pc_av480", None)
                setattr(value, "seff_pc_av480", self)

    @property
    def AbstractLoopAction(self):
        return self.__AbstractLoopAction

    @AbstractLoopAction.setter
    def AbstractLoopAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour__AbstractLoopAction", None)
        self.__AbstractLoopAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc_av478"):
                opp_val = getattr(old_value, "seff_pc_av478", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc_av478", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc_av478"):
                opp_val = getattr(value, "seff_pc_av478", None)
                setattr(value, "seff_pc_av478", self)

    def EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor method
        pass

    def ExactlyOneStartAction(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ExactlyOneStartAction method
        pass

    def ExactlyOneStopAction(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ExactlyOneStopAction method
        pass

class pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification(Identifier):

    def __init__(self, failureProbability: float, LinkingResource665: "LinkingResource" = None, pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification: "CommunicationLinkResourceType" = None, PCMRandomVariable670: "PCMRandomVariable" = None, PCMRandomVariable673: "PCMRandomVariable" = None):
        self.failureProbability = failureProbability
        self.LinkingResource665 = LinkingResource665
        self.pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification = pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification
        self.PCMRandomVariable670 = PCMRandomVariable670
        self.PCMRandomVariable673 = PCMRandomVariable673
        
    @property
    def failureProbability(self) -> float:
        return self.__failureProbability

    @failureProbability.setter
    def failureProbability(self, failureProbability: float):
        self.__failureProbability = failureProbability

    @property
    def PCMRandomVariable670(self):
        return self.__PCMRandomVariable670

    @PCMRandomVariable670.setter
    def PCMRandomVariable670(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification__PCMRandomVariable670", None)
        self.__PCMRandomVariable670 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc_av671"):
                opp_val = getattr(old_value, "core_pc_av671", None)
                if opp_val == self:
                    setattr(old_value, "core_pc_av671", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc_av671"):
                opp_val = getattr(value, "core_pc_av671", None)
                setattr(value, "core_pc_av671", self)

    @property
    def PCMRandomVariable673(self):
        return self.__PCMRandomVariable673

    @PCMRandomVariable673.setter
    def PCMRandomVariable673(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification__PCMRandomVariable673", None)
        self.__PCMRandomVariable673 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc_av674"):
                opp_val = getattr(old_value, "core_pc_av674", None)
                if opp_val == self:
                    setattr(old_value, "core_pc_av674", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc_av674"):
                opp_val = getattr(value, "core_pc_av674", None)
                setattr(value, "core_pc_av674", self)

    @property
    def LinkingResource665(self):
        return self.__LinkingResource665

    @LinkingResource665.setter
    def LinkingResource665(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification__LinkingResource665", None)
        self.__LinkingResource665 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_pc_av666"):
                opp_val = getattr(old_value, "resourceenvironment_pc_av666", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_pc_av666", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_pc_av666"):
                opp_val = getattr(value, "resourceenvironment_pc_av666", None)
                setattr(value, "resourceenvironment_pc_av666", self)

    @property
    def pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification(self):
        return self.__pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification

    @pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification.setter
    def pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification__pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification", None)
        self.__pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CommunicationLinkResourceType668"):
                opp_val = getattr(old_value, "CommunicationLinkResourceType668", None)
                if opp_val == self:
                    setattr(old_value, "CommunicationLinkResourceType668", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CommunicationLinkResourceType668"):
                opp_val = getattr(value, "CommunicationLinkResourceType668", None)
                setattr(value, "CommunicationLinkResourceType668", self)

class pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification(Identifier):

    def __init__(self, MTTR: float, MTTF: float, requiredByContainer: bool, numberOfReplicas: int, pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification: "SchedulingPolicy" = None, pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification656: "ProcessingResourceType" = None, PCMRandomVariable659: "PCMRandomVariable" = None, ResourceContainer662: "ResourceContainer" = None):
        self.MTTR = MTTR
        self.MTTF = MTTF
        self.requiredByContainer = requiredByContainer
        self.numberOfReplicas = numberOfReplicas
        self.pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification = pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification
        self.pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification656 = pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification656
        self.PCMRandomVariable659 = PCMRandomVariable659
        self.ResourceContainer662 = ResourceContainer662
        
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
    def numberOfReplicas(self) -> int:
        return self.__numberOfReplicas

    @numberOfReplicas.setter
    def numberOfReplicas(self, numberOfReplicas: int):
        self.__numberOfReplicas = numberOfReplicas

    @property
    def MTTR(self) -> float:
        return self.__MTTR

    @MTTR.setter
    def MTTR(self, MTTR: float):
        self.__MTTR = MTTR

    @property
    def pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification656(self):
        return self.__pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification656

    @pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification656.setter
    def pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification656(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification__pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification656", None)
        self.__pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification656 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcessingResourceType657"):
                opp_val = getattr(old_value, "ProcessingResourceType657", None)
                if opp_val == self:
                    setattr(old_value, "ProcessingResourceType657", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessingResourceType657"):
                opp_val = getattr(value, "ProcessingResourceType657", None)
                setattr(value, "ProcessingResourceType657", self)

    @property
    def pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification(self):
        return self.__pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification

    @pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification.setter
    def pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification__pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification", None)
        self.__pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SchedulingPolicy654"):
                opp_val = getattr(old_value, "SchedulingPolicy654", None)
                if opp_val == self:
                    setattr(old_value, "SchedulingPolicy654", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SchedulingPolicy654"):
                opp_val = getattr(value, "SchedulingPolicy654", None)
                setattr(value, "SchedulingPolicy654", self)

    @property
    def ResourceContainer662(self):
        return self.__ResourceContainer662

    @ResourceContainer662.setter
    def ResourceContainer662(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification__ResourceContainer662", None)
        self.__ResourceContainer662 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_pc_av663"):
                opp_val = getattr(old_value, "resourceenvironment_pc_av663", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_pc_av663", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_pc_av663"):
                opp_val = getattr(value, "resourceenvironment_pc_av663", None)
                setattr(value, "resourceenvironment_pc_av663", self)

    @property
    def PCMRandomVariable659(self):
        return self.__PCMRandomVariable659

    @PCMRandomVariable659.setter
    def PCMRandomVariable659(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification__PCMRandomVariable659", None)
        self.__PCMRandomVariable659 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc_av660"):
                opp_val = getattr(old_value, "core_pc_av660", None)
                if opp_val == self:
                    setattr(old_value, "core_pc_av660", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc_av660"):
                opp_val = getattr(value, "core_pc_av660", None)
                setattr(value, "core_pc_av660", self)

class pcm_pc_av_seff_pc_av_ResourceDemandingSEFF(Identifier, seff_pc_av_ServiceEffectSpecification, seff_pc_av_ResourceDemandingBehaviour):

    pass
class pcm_pc_av_entity_pc_av_Entity(Identifier, entity_pc_av_NamedElement):

    pass
class pcm_pc_av_entity_pc_av_NamedElement:

    def __init__(self, entityName: str):
        self.entityName = entityName
        
    @property
    def entityName(self) -> str:
        return self.__entityName

    @entityName.setter
    def entityName(self, entityName: str):
        self.__entityName = entityName

class composition_pc_av_EventChannel:

    pass
class composition_pc_av_ResourceRequiredDelegationConnector:

    pass
class composition_pc_av_AssemblyContext:

    pass
class entity_pc_av_ResourceRequiredRole:

    pass
class RequiredRole:

    pass
class pcm_pc_av_repository_pc_av_InfrastructureRequiredRole(RequiredRole):

    pass
class pcm_pc_av_repository_pc_av_OperationRequiredRole(RequiredRole):

    pass
class pcm_pc_av_repository_pc_av_SourceRole(RequiredRole):

    pass
class entity_pc_av_ResourceInterfaceRequiringEntity:

    pass
class entity_pc_av_Entity:

    pass
class pcm_pc_av_repository_pc_av_CollectionDataType(repository_pc_av_DataType, entity_pc_av_Entity):

    pass
class pcm_pc_av_repository_pc_av_CompositeDataType(repository_pc_av_DataType, entity_pc_av_Entity):

    pass
class pcm_pc_av_system_pc_av_System(entity_pc_av_Entity, entity_pc_av_ComposedProvidingRequiringEntity):

    def __init__(self, QoSAnnotations628: set["QoSAnnotations"] = None):
        self.QoSAnnotations628 = QoSAnnotations628 if QoSAnnotations628 is not None else set()
        
    @property
    def QoSAnnotations628(self):
        return self.__QoSAnnotations628

    @QoSAnnotations628.setter
    def QoSAnnotations628(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_system_pc_av_System__QoSAnnotations628", None)
        self.__QoSAnnotations628 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qosannotations_pc_av629"):
                    opp_val = getattr(item, "qosannotations_pc_av629", None)
                    
                    if opp_val == self:
                        setattr(item, "qosannotations_pc_av629", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qosannotations_pc_av629"):
                    opp_val = getattr(item, "qosannotations_pc_av629", None)
                    
                    setattr(item, "qosannotations_pc_av629", self)
                    

    def SystemMustHaveAtLeastOneProvidedRole(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SystemMustHaveAtLeastOneProvidedRole method
        pass

class pcm_pc_av_entity_pc_av_InterfaceRequiringEntity(entity_pc_av_ResourceInterfaceRequiringEntity, entity_pc_av_Entity):

    pass
class ProvidedRole:

    pass
class pcm_pc_av_repository_pc_av_SinkRole(ProvidedRole):

    pass
class pcm_pc_av_repository_pc_av_InfrastructureProvidedRole(ProvidedRole):

    pass
class pcm_pc_av_repository_pc_av_OperationProvidedRole(ProvidedRole):

    pass
class Entity:

    pass
class pcm_pc_av_reliability_pc_av_FailureType(Entity):

    pass
class pcm_pc_av_resourcetype_pc_av_ResourceSignature(Entity):

    def __init__(self, resourceServiceId: int, Parameter383: "Parameter" = None, ResourceInterface386: "ResourceInterface" = None):
        self.resourceServiceId = resourceServiceId
        self.Parameter383 = Parameter383
        self.ResourceInterface386 = ResourceInterface386
        
    @property
    def resourceServiceId(self) -> int:
        return self.__resourceServiceId

    @resourceServiceId.setter
    def resourceServiceId(self, resourceServiceId: int):
        self.__resourceServiceId = resourceServiceId

    @property
    def Parameter383(self):
        return self.__Parameter383

    @Parameter383.setter
    def Parameter383(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_resourcetype_pc_av_ResourceSignature__Parameter383", None)
        self.__Parameter383 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc_av384"):
                opp_val = getattr(old_value, "repository_pc_av384", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc_av384", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc_av384"):
                opp_val = getattr(value, "repository_pc_av384", None)
                setattr(value, "repository_pc_av384", self)

    @property
    def ResourceInterface386(self):
        return self.__ResourceInterface386

    @ResourceInterface386.setter
    def ResourceInterface386(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_resourcetype_pc_av_ResourceSignature__ResourceInterface386", None)
        self.__ResourceInterface386 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcetype_pc_av387"):
                opp_val = getattr(old_value, "resourcetype_pc_av387", None)
                if opp_val == self:
                    setattr(old_value, "resourcetype_pc_av387", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcetype_pc_av387"):
                opp_val = getattr(value, "resourcetype_pc_av387", None)
                setattr(value, "resourcetype_pc_av387", self)

class pcm_pc_av_composition_pc_av_AssemblyContext(Entity):

    pass
class pcm_pc_av_seff_pc_av_AbstractAction(Entity):

    pass
class pcm_pc_av_seff_pc_av_AbstractBranchTransition(Entity):

    pass
class pcm_pc_av_usagemodel_pc_av_AbstractUserAction(Entity):

    pass
class pcm_pc_av_resourceenvironment_pc_av_LinkingResource(Entity):

    pass
class pcm_pc_av_repository_pc_av_Role(Entity):

    pass
class pcm_pc_av_entity_pc_av_ResourceInterfaceRequiringEntity(Entity):

    pass
class pcm_pc_av_repository_pc_av_Signature(Entity):

    pass
class pcm_pc_av_composition_pc_av_ComposedStructure(Entity):

    def __init__(self, composition_pc_av60: set["composition_pc_av_AssemblyContext"] = None, composition_pc_av63: set["composition_pc_av_ResourceRequiredDelegationConnector"] = None, composition_pc_av66: set["composition_pc_av_EventChannel"] = None, composition_pc_av69: set["composition_pc_av_Connector"] = None):
        self.composition_pc_av60 = composition_pc_av60 if composition_pc_av60 is not None else set()
        self.composition_pc_av63 = composition_pc_av63 if composition_pc_av63 is not None else set()
        self.composition_pc_av66 = composition_pc_av66 if composition_pc_av66 is not None else set()
        self.composition_pc_av69 = composition_pc_av69 if composition_pc_av69 is not None else set()
        
    @property
    def composition_pc_av69(self):
        return self.__composition_pc_av69

    @composition_pc_av69.setter
    def composition_pc_av69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_composition_pc_av_ComposedStructure__composition_pc_av69", None)
        self.__composition_pc_av69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_pc_av70"):
                    opp_val = getattr(item, "core_pc_av70", None)
                    
                    if opp_val == self:
                        setattr(item, "core_pc_av70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_pc_av70"):
                    opp_val = getattr(item, "core_pc_av70", None)
                    
                    setattr(item, "core_pc_av70", self)
                    

    @property
    def composition_pc_av63(self):
        return self.__composition_pc_av63

    @composition_pc_av63.setter
    def composition_pc_av63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_composition_pc_av_ComposedStructure__composition_pc_av63", None)
        self.__composition_pc_av63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_pc_av64"):
                    opp_val = getattr(item, "core_pc_av64", None)
                    
                    if opp_val == self:
                        setattr(item, "core_pc_av64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_pc_av64"):
                    opp_val = getattr(item, "core_pc_av64", None)
                    
                    setattr(item, "core_pc_av64", self)
                    

    @property
    def composition_pc_av60(self):
        return self.__composition_pc_av60

    @composition_pc_av60.setter
    def composition_pc_av60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_composition_pc_av_ComposedStructure__composition_pc_av60", None)
        self.__composition_pc_av60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_pc_av61"):
                    opp_val = getattr(item, "core_pc_av61", None)
                    
                    if opp_val == self:
                        setattr(item, "core_pc_av61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_pc_av61"):
                    opp_val = getattr(item, "core_pc_av61", None)
                    
                    setattr(item, "core_pc_av61", self)
                    

    @property
    def composition_pc_av66(self):
        return self.__composition_pc_av66

    @composition_pc_av66.setter
    def composition_pc_av66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_composition_pc_av_ComposedStructure__composition_pc_av66", None)
        self.__composition_pc_av66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_pc_av67"):
                    opp_val = getattr(item, "core_pc_av67", None)
                    
                    if opp_val == self:
                        setattr(item, "core_pc_av67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_pc_av67"):
                    opp_val = getattr(item, "core_pc_av67", None)
                    
                    setattr(item, "core_pc_av67", self)
                    

    def MultipleConnectorsConstraint(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MultipleConnectorsConstraint method
        pass

    def MultipleConnectorsConstraintForAssemblyConnectors(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MultipleConnectorsConstraintForAssemblyConnectors method
        pass

class pcm_pc_av_repository_pc_av_PassiveResource(Entity):

    pass
class pcm_pc_av_repository_pc_av_Interface(Entity):

    def __init__(self, pcm_pc_av_repository_pc_av_Interface315: set["Protocol"] = None, RequiredCharacterisation: set["RequiredCharacterisation"] = None, Repository319: "Repository" = None, pcm_pc_av_repository_pc_av_Interface: set["Interface"] = None):
        self.pcm_pc_av_repository_pc_av_Interface315 = pcm_pc_av_repository_pc_av_Interface315 if pcm_pc_av_repository_pc_av_Interface315 is not None else set()
        self.RequiredCharacterisation = RequiredCharacterisation if RequiredCharacterisation is not None else set()
        self.Repository319 = Repository319
        self.pcm_pc_av_repository_pc_av_Interface = pcm_pc_av_repository_pc_av_Interface if pcm_pc_av_repository_pc_av_Interface is not None else set()
        
    @property
    def RequiredCharacterisation(self):
        return self.__RequiredCharacterisation

    @RequiredCharacterisation.setter
    def RequiredCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_repository_pc_av_Interface__RequiredCharacterisation", None)
        self.__RequiredCharacterisation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_pc_av317"):
                    opp_val = getattr(item, "repository_pc_av317", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_pc_av317", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_pc_av317"):
                    opp_val = getattr(item, "repository_pc_av317", None)
                    
                    setattr(item, "repository_pc_av317", self)
                    

    @property
    def pcm_pc_av_repository_pc_av_Interface(self):
        return self.__pcm_pc_av_repository_pc_av_Interface

    @pcm_pc_av_repository_pc_av_Interface.setter
    def pcm_pc_av_repository_pc_av_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_repository_pc_av_Interface__pcm_pc_av_repository_pc_av_Interface", None)
        self.__pcm_pc_av_repository_pc_av_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Interface313"):
                    opp_val = getattr(item, "Interface313", None)
                    
                    if opp_val == self:
                        setattr(item, "Interface313", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Interface313"):
                    opp_val = getattr(item, "Interface313", None)
                    
                    setattr(item, "Interface313", self)
                    

    @property
    def pcm_pc_av_repository_pc_av_Interface315(self):
        return self.__pcm_pc_av_repository_pc_av_Interface315

    @pcm_pc_av_repository_pc_av_Interface315.setter
    def pcm_pc_av_repository_pc_av_Interface315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_repository_pc_av_Interface__pcm_pc_av_repository_pc_av_Interface315", None)
        self.__pcm_pc_av_repository_pc_av_Interface315 = value if value is not None else set()
        
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
    def Repository319(self):
        return self.__Repository319

    @Repository319.setter
    def Repository319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_repository_pc_av_Interface__Repository319", None)
        self.__Repository319 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc_av320"):
                opp_val = getattr(old_value, "repository_pc_av320", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc_av320", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc_av320"):
                opp_val = getattr(value, "repository_pc_av320", None)
                setattr(value, "repository_pc_av320", self)

    def NoProtocolTypeIDUsedTwice(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement NoProtocolTypeIDUsedTwice method
        pass

class pcm_pc_av_repository_pc_av_Repository(Entity):

    def __init__(self, repositoryDescription: str, RepositoryComponent303: set["RepositoryComponent"] = None, Interface: set["Interface"] = None, FailureType: set["FailureType"] = None, DataType310: set["DataType"] = None):
        self.repositoryDescription = repositoryDescription
        self.RepositoryComponent303 = RepositoryComponent303 if RepositoryComponent303 is not None else set()
        self.Interface = Interface if Interface is not None else set()
        self.FailureType = FailureType if FailureType is not None else set()
        self.DataType310 = DataType310 if DataType310 is not None else set()
        
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
        old_value = getattr(self, f"_pcm_pc_av_repository_pc_av_Repository__Interface", None)
        self.__Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_pc_av306"):
                    opp_val = getattr(item, "repository_pc_av306", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_pc_av306", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_pc_av306"):
                    opp_val = getattr(item, "repository_pc_av306", None)
                    
                    setattr(item, "repository_pc_av306", self)
                    

    @property
    def FailureType(self):
        return self.__FailureType

    @FailureType.setter
    def FailureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_repository_pc_av_Repository__FailureType", None)
        self.__FailureType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reliability_pc_av308"):
                    opp_val = getattr(item, "reliability_pc_av308", None)
                    
                    if opp_val == self:
                        setattr(item, "reliability_pc_av308", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reliability_pc_av308"):
                    opp_val = getattr(item, "reliability_pc_av308", None)
                    
                    setattr(item, "reliability_pc_av308", self)
                    

    @property
    def RepositoryComponent303(self):
        return self.__RepositoryComponent303

    @RepositoryComponent303.setter
    def RepositoryComponent303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_repository_pc_av_Repository__RepositoryComponent303", None)
        self.__RepositoryComponent303 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_pc_av304"):
                    opp_val = getattr(item, "repository_pc_av304", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_pc_av304", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_pc_av304"):
                    opp_val = getattr(item, "repository_pc_av304", None)
                    
                    setattr(item, "repository_pc_av304", self)
                    

    @property
    def DataType310(self):
        return self.__DataType310

    @DataType310.setter
    def DataType310(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_repository_pc_av_Repository__DataType310", None)
        self.__DataType310 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_pc_av311"):
                    opp_val = getattr(item, "repository_pc_av311", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_pc_av311", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_pc_av311"):
                    opp_val = getattr(item, "repository_pc_av311", None)
                    
                    setattr(item, "repository_pc_av311", self)
                    

class pcm_pc_av_composition_pc_av_Connector(Entity):

    pass
class pcm_pc_av_allocation_pc_av_Allocation(Entity):

    def __init__(self, pcm_pc_av_allocation_pc_av_Allocation: "ResourceEnvironment" = None, pcm_pc_av_allocation_pc_av_Allocation686: "System" = None, AllocationContext: set["AllocationContext"] = None):
        self.pcm_pc_av_allocation_pc_av_Allocation = pcm_pc_av_allocation_pc_av_Allocation
        self.pcm_pc_av_allocation_pc_av_Allocation686 = pcm_pc_av_allocation_pc_av_Allocation686
        self.AllocationContext = AllocationContext if AllocationContext is not None else set()
        
    @property
    def pcm_pc_av_allocation_pc_av_Allocation686(self):
        return self.__pcm_pc_av_allocation_pc_av_Allocation686

    @pcm_pc_av_allocation_pc_av_Allocation686.setter
    def pcm_pc_av_allocation_pc_av_Allocation686(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_allocation_pc_av_Allocation__pcm_pc_av_allocation_pc_av_Allocation686", None)
        self.__pcm_pc_av_allocation_pc_av_Allocation686 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "System687"):
                opp_val = getattr(old_value, "System687", None)
                if opp_val == self:
                    setattr(old_value, "System687", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "System687"):
                opp_val = getattr(value, "System687", None)
                setattr(value, "System687", self)

    @property
    def AllocationContext(self):
        return self.__AllocationContext

    @AllocationContext.setter
    def AllocationContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_allocation_pc_av_Allocation__AllocationContext", None)
        self.__AllocationContext = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "allocation_pc_av689"):
                    opp_val = getattr(item, "allocation_pc_av689", None)
                    
                    if opp_val == self:
                        setattr(item, "allocation_pc_av689", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "allocation_pc_av689"):
                    opp_val = getattr(item, "allocation_pc_av689", None)
                    
                    setattr(item, "allocation_pc_av689", self)
                    

    @property
    def pcm_pc_av_allocation_pc_av_Allocation(self):
        return self.__pcm_pc_av_allocation_pc_av_Allocation

    @pcm_pc_av_allocation_pc_av_Allocation.setter
    def pcm_pc_av_allocation_pc_av_Allocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_allocation_pc_av_Allocation__pcm_pc_av_allocation_pc_av_Allocation", None)
        self.__pcm_pc_av_allocation_pc_av_Allocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceEnvironment684"):
                opp_val = getattr(old_value, "ResourceEnvironment684", None)
                if opp_val == self:
                    setattr(old_value, "ResourceEnvironment684", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceEnvironment684"):
                opp_val = getattr(value, "ResourceEnvironment684", None)
                setattr(value, "ResourceEnvironment684", self)

    def CommunicatingServersHaveToBeConnectedByLinkingResource(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement CommunicatingServersHaveToBeConnectedByLinkingResource method
        pass

    def EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce method
        pass

class pcm_pc_av_resourceenvironment_pc_av_ResourceContainer(Entity):

    pass
class pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour(Entity):

    def __init__(self, UsageScenario237: "UsageScenario" = None, BranchTransition: "BranchTransition" = None, Loop242: "Loop" = None, AbstractUserAction245: set["AbstractUserAction"] = None):
        self.UsageScenario237 = UsageScenario237
        self.BranchTransition = BranchTransition
        self.Loop242 = Loop242
        self.AbstractUserAction245 = AbstractUserAction245 if AbstractUserAction245 is not None else set()
        
    @property
    def UsageScenario237(self):
        return self.__UsageScenario237

    @UsageScenario237.setter
    def UsageScenario237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour__UsageScenario237", None)
        self.__UsageScenario237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc_av238"):
                opp_val = getattr(old_value, "usagemodel_pc_av238", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc_av238", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc_av238"):
                opp_val = getattr(value, "usagemodel_pc_av238", None)
                setattr(value, "usagemodel_pc_av238", self)

    @property
    def AbstractUserAction245(self):
        return self.__AbstractUserAction245

    @AbstractUserAction245.setter
    def AbstractUserAction245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour__AbstractUserAction245", None)
        self.__AbstractUserAction245 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "usagemodel_pc_av246"):
                    opp_val = getattr(item, "usagemodel_pc_av246", None)
                    
                    if opp_val == self:
                        setattr(item, "usagemodel_pc_av246", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "usagemodel_pc_av246"):
                    opp_val = getattr(item, "usagemodel_pc_av246", None)
                    
                    setattr(item, "usagemodel_pc_av246", self)
                    

    @property
    def BranchTransition(self):
        return self.__BranchTransition

    @BranchTransition.setter
    def BranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour__BranchTransition", None)
        self.__BranchTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc_av240"):
                opp_val = getattr(old_value, "usagemodel_pc_av240", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc_av240", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc_av240"):
                opp_val = getattr(value, "usagemodel_pc_av240", None)
                setattr(value, "usagemodel_pc_av240", self)

    @property
    def Loop242(self):
        return self.__Loop242

    @Loop242.setter
    def Loop242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour__Loop242", None)
        self.__Loop242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc_av243"):
                opp_val = getattr(old_value, "usagemodel_pc_av243", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc_av243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc_av243"):
                opp_val = getattr(value, "usagemodel_pc_av243", None)
                setattr(value, "usagemodel_pc_av243", self)

    def Exactlyonestop(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement Exactlyonestop method
        pass

    def EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor method
        pass

    def Exactlyonestart(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement Exactlyonestart method
        pass

class pcm_pc_av_composition_pc_av_EventChannel(Entity):

    pass
class pcm_pc_av_allocation_pc_av_AllocationContext(Entity):

    def __init__(self, pcm_pc_av_allocation_pc_av_AllocationContext: "ResourceContainer" = None, pcm_pc_av_allocation_pc_av_AllocationContext678: "composition_pc_av_AssemblyContext" = None, Allocation: "Allocation" = None, pcm_pc_av_allocation_pc_av_AllocationContext682: "composition_pc_av_EventChannel" = None):
        self.pcm_pc_av_allocation_pc_av_AllocationContext = pcm_pc_av_allocation_pc_av_AllocationContext
        self.pcm_pc_av_allocation_pc_av_AllocationContext678 = pcm_pc_av_allocation_pc_av_AllocationContext678
        self.Allocation = Allocation
        self.pcm_pc_av_allocation_pc_av_AllocationContext682 = pcm_pc_av_allocation_pc_av_AllocationContext682
        
    @property
    def pcm_pc_av_allocation_pc_av_AllocationContext678(self):
        return self.__pcm_pc_av_allocation_pc_av_AllocationContext678

    @pcm_pc_av_allocation_pc_av_AllocationContext678.setter
    def pcm_pc_av_allocation_pc_av_AllocationContext678(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_allocation_pc_av_AllocationContext__pcm_pc_av_allocation_pc_av_AllocationContext678", None)
        self.__pcm_pc_av_allocation_pc_av_AllocationContext678 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_pc_av_AssemblyContext679"):
                opp_val = getattr(old_value, "composition_pc_av_AssemblyContext679", None)
                if opp_val == self:
                    setattr(old_value, "composition_pc_av_AssemblyContext679", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_pc_av_AssemblyContext679"):
                opp_val = getattr(value, "composition_pc_av_AssemblyContext679", None)
                setattr(value, "composition_pc_av_AssemblyContext679", self)

    @property
    def pcm_pc_av_allocation_pc_av_AllocationContext(self):
        return self.__pcm_pc_av_allocation_pc_av_AllocationContext

    @pcm_pc_av_allocation_pc_av_AllocationContext.setter
    def pcm_pc_av_allocation_pc_av_AllocationContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_allocation_pc_av_AllocationContext__pcm_pc_av_allocation_pc_av_AllocationContext", None)
        self.__pcm_pc_av_allocation_pc_av_AllocationContext = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceContainer676"):
                opp_val = getattr(old_value, "ResourceContainer676", None)
                if opp_val == self:
                    setattr(old_value, "ResourceContainer676", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceContainer676"):
                opp_val = getattr(value, "ResourceContainer676", None)
                setattr(value, "ResourceContainer676", self)

    @property
    def pcm_pc_av_allocation_pc_av_AllocationContext682(self):
        return self.__pcm_pc_av_allocation_pc_av_AllocationContext682

    @pcm_pc_av_allocation_pc_av_AllocationContext682.setter
    def pcm_pc_av_allocation_pc_av_AllocationContext682(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_allocation_pc_av_AllocationContext__pcm_pc_av_allocation_pc_av_AllocationContext682", None)
        self.__pcm_pc_av_allocation_pc_av_AllocationContext682 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_pc_av_EventChannel"):
                opp_val = getattr(old_value, "composition_pc_av_EventChannel", None)
                if opp_val == self:
                    setattr(old_value, "composition_pc_av_EventChannel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_pc_av_EventChannel"):
                opp_val = getattr(value, "composition_pc_av_EventChannel", None)
                setattr(value, "composition_pc_av_EventChannel", self)

    @property
    def Allocation(self):
        return self.__Allocation

    @Allocation.setter
    def Allocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_allocation_pc_av_AllocationContext__Allocation", None)
        self.__Allocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "allocation_pc_av"):
                opp_val = getattr(old_value, "allocation_pc_av", None)
                if opp_val == self:
                    setattr(old_value, "allocation_pc_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "allocation_pc_av"):
                opp_val = getattr(value, "allocation_pc_av", None)
                setattr(value, "allocation_pc_av", self)

    def OneAssemblyContextOrOneEventChannelShouldBeReferred(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement OneAssemblyContextOrOneEventChannelShouldBeReferred method
        pass

class pcm_pc_av_qosannotations_pc_av_QoSAnnotations(Entity):

    def __init__(self, SpecifiedOutputParameterAbstraction604: set["SpecifiedOutputParameterAbstraction"] = None, System: "System" = None, SpecifiedQoSAnnotation: set["SpecifiedQoSAnnotation"] = None):
        self.SpecifiedOutputParameterAbstraction604 = SpecifiedOutputParameterAbstraction604 if SpecifiedOutputParameterAbstraction604 is not None else set()
        self.System = System
        self.SpecifiedQoSAnnotation = SpecifiedQoSAnnotation if SpecifiedQoSAnnotation is not None else set()
        
    @property
    def System(self):
        return self.__System

    @System.setter
    def System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_qosannotations_pc_av_QoSAnnotations__System", None)
        self.__System = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system_pc_av"):
                opp_val = getattr(old_value, "system_pc_av", None)
                if opp_val == self:
                    setattr(old_value, "system_pc_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system_pc_av"):
                opp_val = getattr(value, "system_pc_av", None)
                setattr(value, "system_pc_av", self)

    @property
    def SpecifiedOutputParameterAbstraction604(self):
        return self.__SpecifiedOutputParameterAbstraction604

    @SpecifiedOutputParameterAbstraction604.setter
    def SpecifiedOutputParameterAbstraction604(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_qosannotations_pc_av_QoSAnnotations__SpecifiedOutputParameterAbstraction604", None)
        self.__SpecifiedOutputParameterAbstraction604 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qosannotations_pc_av605"):
                    opp_val = getattr(item, "qosannotations_pc_av605", None)
                    
                    if opp_val == self:
                        setattr(item, "qosannotations_pc_av605", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qosannotations_pc_av605"):
                    opp_val = getattr(item, "qosannotations_pc_av605", None)
                    
                    setattr(item, "qosannotations_pc_av605", self)
                    

    @property
    def SpecifiedQoSAnnotation(self):
        return self.__SpecifiedQoSAnnotation

    @SpecifiedQoSAnnotation.setter
    def SpecifiedQoSAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_qosannotations_pc_av_QoSAnnotations__SpecifiedQoSAnnotation", None)
        self.__SpecifiedQoSAnnotation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qosannotations_pc_av608"):
                    opp_val = getattr(item, "qosannotations_pc_av608", None)
                    
                    if opp_val == self:
                        setattr(item, "qosannotations_pc_av608", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qosannotations_pc_av608"):
                    opp_val = getattr(item, "qosannotations_pc_av608", None)
                    
                    setattr(item, "qosannotations_pc_av608", self)
                    

    def MultipleReliabilityAnnotationsPerExternalCallNotAllowed(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MultipleReliabilityAnnotationsPerExternalCallNotAllowed method
        pass

class pcm_pc_av_seff_reliability_pc_av_FailureHandlingEntity(Entity):

    pass
class pcm_pc_av_usagemodel_pc_av_UsageScenario(Entity):

    pass
class pcm_pc_av_resourcetype_pc_av_ResourceInterface(Entity):

    pass
class pcm_pc_av_resourcetype_pc_av_SchedulingPolicy(Entity):

    pass
class pcm_pc_av_entity_pc_av_InterfaceProvidingEntity(Entity):

    pass
class entity_pc_av_InterfaceRequiringEntity:

    pass
class entity_pc_av_InterfaceProvidingEntity:

    pass
class pcm_pc_av_entity_pc_av_InterfaceProvidingRequiringEntity(entity_pc_av_InterfaceRequiringEntity, entity_pc_av_InterfaceProvidingEntity):

    pass
class ResourceInterface:

    pass
class entity_pc_av_ResourceInterfaceProvidingEntity:

    pass
class pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingRequiringEntity(entity_pc_av_ResourceInterfaceRequiringEntity, entity_pc_av_ResourceInterfaceProvidingEntity):

    pass
class pcm_pc_av_resourcetype_pc_av_ResourceType(entity_pc_av_Entity, entity_pc_av_ResourceInterfaceProvidingEntity, UnitCarryingElement):

    pass
class Role:

    pass
class pcm_pc_av_repository_pc_av_RequiredRole(Role):

    pass
class pcm_pc_av_repository_pc_av_ProvidedRole(Role):

    pass
class pcm_pc_av_entity_pc_av_ResourceRequiredRole(Role):

    pass
class pcm_pc_av_entity_pc_av_ResourceProvidedRole(Role):

    pass
class entity_pc_av_InterfaceProvidingRequiringEntity:

    pass
class composition_pc_av_ComposedStructure:

    pass
class pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity(entity_pc_av_InterfaceProvidingRequiringEntity, composition_pc_av_ComposedStructure):

    def __init__(self, core_pc_av87: "pcm_pc_av_composition_pc_av_EventChannel", core_pc_av193: "pcm_pc_av_composition_pc_av_AssemblyContext", core_pc_av58: "pcm_pc_av_composition_pc_av_Connector", core_pc_av77: "pcm_pc_av_composition_pc_av_ResourceRequiredDelegationConnector"):
        
    def ProvidedRolesMustBeBound(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ProvidedRolesMustBeBound method
        pass

class entity_pc_av_ResourceProvidedRole:

    pass
class pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingEntity(Entity):

    pass
class composition_pc_av_AssemblyEventConnector:

    pass
class composition_pc_av_EventChannelSinkConnector:

    pass
class qos_performance_pc_av_SpecifiedExecutionTime:

    pass
class GuardedBranchTransition:

    pass
class LoopAction:

    pass
class seff_performance_pc_av_ParametricResourceDemand:

    pass
class seff_performance_pc_av_ResourceCall:

    pass
class seff_performance_pc_av_InfrastructureCall:

    pass
class VariableCharacterisation:

    pass
class PassiveResource:

    pass
class ClosedWorkload:

    pass
class ProcessingResourceSpecification:

    pass
class CommunicationLinkResourceSpecification:

    pass
class Delay:

    pass
class OpenWorkload:

    pass
class Loop:

    pass
class pcm_pc_av_GlobalScope:

    pass
class pcm_pc_av_Advice:

    pass
class pcm_pc_av_EObject:

    pass
class pcm_pc_av_Pointcut:

    pass
class pcm_pc_av_DummyClass:

    pass
class RandomVariable:

    pass
class pcm_pc_av_core_pc_av_PCMRandomVariable(RandomVariable):

    def __init__(self, Loop: "Loop" = None, OpenWorkload: "OpenWorkload" = None, Delay: "Delay" = None, CommunicationLinkResourceSpecification: "CommunicationLinkResourceSpecification" = None, ProcessingResourceSpecification: "ProcessingResourceSpecification" = None, CommunicationLinkResourceSpecification36: "CommunicationLinkResourceSpecification" = None, ClosedWorkload: "ClosedWorkload" = None, PassiveResource: "PassiveResource" = None, VariableCharacterisation: "VariableCharacterisation" = None, seff_performance_pc_av: "seff_performance_pc_av_InfrastructureCall" = None, seff_performance_pc_av12: "seff_performance_pc_av_ResourceCall" = None, seff_performance_pc_av15: "seff_performance_pc_av_ParametricResourceDemand" = None, LoopAction: "LoopAction" = None, GuardedBranchTransition: "GuardedBranchTransition" = None, qos_performance_pc_av: "qos_performance_pc_av_SpecifiedExecutionTime" = None, composition_pc_av: "composition_pc_av_EventChannelSinkConnector" = None, composition_pc_av24: "composition_pc_av_AssemblyEventConnector" = None):
        self.Loop = Loop
        self.OpenWorkload = OpenWorkload
        self.Delay = Delay
        self.CommunicationLinkResourceSpecification = CommunicationLinkResourceSpecification
        self.ProcessingResourceSpecification = ProcessingResourceSpecification
        self.CommunicationLinkResourceSpecification36 = CommunicationLinkResourceSpecification36
        self.ClosedWorkload = ClosedWorkload
        self.PassiveResource = PassiveResource
        self.VariableCharacterisation = VariableCharacterisation
        self.seff_performance_pc_av = seff_performance_pc_av
        self.seff_performance_pc_av12 = seff_performance_pc_av12
        self.seff_performance_pc_av15 = seff_performance_pc_av15
        self.LoopAction = LoopAction
        self.GuardedBranchTransition = GuardedBranchTransition
        self.qos_performance_pc_av = qos_performance_pc_av
        self.composition_pc_av = composition_pc_av
        self.composition_pc_av24 = composition_pc_av24
        
    @property
    def PassiveResource(self):
        return self.__PassiveResource

    @PassiveResource.setter
    def PassiveResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_core_pc_av_PCMRandomVariable__PassiveResource", None)
        self.__PassiveResource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc_av"):
                opp_val = getattr(old_value, "repository_pc_av", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc_av"):
                opp_val = getattr(value, "repository_pc_av", None)
                setattr(value, "repository_pc_av", self)

    @property
    def VariableCharacterisation(self):
        return self.__VariableCharacterisation

    @VariableCharacterisation.setter
    def VariableCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_core_pc_av_PCMRandomVariable__VariableCharacterisation", None)
        self.__VariableCharacterisation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameter_pc_av"):
                opp_val = getattr(old_value, "parameter_pc_av", None)
                if opp_val == self:
                    setattr(old_value, "parameter_pc_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameter_pc_av"):
                opp_val = getattr(value, "parameter_pc_av", None)
                setattr(value, "parameter_pc_av", self)

    @property
    def CommunicationLinkResourceSpecification(self):
        return self.__CommunicationLinkResourceSpecification

    @CommunicationLinkResourceSpecification.setter
    def CommunicationLinkResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_core_pc_av_PCMRandomVariable__CommunicationLinkResourceSpecification", None)
        self.__CommunicationLinkResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_pc_av"):
                opp_val = getattr(old_value, "resourceenvironment_pc_av", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_pc_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_pc_av"):
                opp_val = getattr(value, "resourceenvironment_pc_av", None)
                setattr(value, "resourceenvironment_pc_av", self)

    @property
    def seff_performance_pc_av15(self):
        return self.__seff_performance_pc_av15

    @seff_performance_pc_av15.setter
    def seff_performance_pc_av15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_core_pc_av_PCMRandomVariable__seff_performance_pc_av15", None)
        self.__seff_performance_pc_av15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc_av16"):
                opp_val = getattr(old_value, "seff_pc_av16", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc_av16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc_av16"):
                opp_val = getattr(value, "seff_pc_av16", None)
                setattr(value, "seff_pc_av16", self)

    @property
    def qos_performance_pc_av(self):
        return self.__qos_performance_pc_av

    @qos_performance_pc_av.setter
    def qos_performance_pc_av(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_core_pc_av_PCMRandomVariable__qos_performance_pc_av", None)
        self.__qos_performance_pc_av = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qosannotations_pc_av"):
                opp_val = getattr(old_value, "qosannotations_pc_av", None)
                if opp_val == self:
                    setattr(old_value, "qosannotations_pc_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qosannotations_pc_av"):
                opp_val = getattr(value, "qosannotations_pc_av", None)
                setattr(value, "qosannotations_pc_av", self)

    @property
    def Loop(self):
        return self.__Loop

    @Loop.setter
    def Loop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_core_pc_av_PCMRandomVariable__Loop", None)
        self.__Loop = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc_av27"):
                opp_val = getattr(old_value, "usagemodel_pc_av27", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc_av27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc_av27"):
                opp_val = getattr(value, "usagemodel_pc_av27", None)
                setattr(value, "usagemodel_pc_av27", self)

    @property
    def composition_pc_av(self):
        return self.__composition_pc_av

    @composition_pc_av.setter
    def composition_pc_av(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_core_pc_av_PCMRandomVariable__composition_pc_av", None)
        self.__composition_pc_av = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc_av"):
                opp_val = getattr(old_value, "core_pc_av", None)
                if opp_val == self:
                    setattr(old_value, "core_pc_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc_av"):
                opp_val = getattr(value, "core_pc_av", None)
                setattr(value, "core_pc_av", self)

    @property
    def LoopAction(self):
        return self.__LoopAction

    @LoopAction.setter
    def LoopAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_core_pc_av_PCMRandomVariable__LoopAction", None)
        self.__LoopAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc_av18"):
                opp_val = getattr(old_value, "seff_pc_av18", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc_av18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc_av18"):
                opp_val = getattr(value, "seff_pc_av18", None)
                setattr(value, "seff_pc_av18", self)

    @property
    def ProcessingResourceSpecification(self):
        return self.__ProcessingResourceSpecification

    @ProcessingResourceSpecification.setter
    def ProcessingResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_core_pc_av_PCMRandomVariable__ProcessingResourceSpecification", None)
        self.__ProcessingResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_pc_av34"):
                opp_val = getattr(old_value, "resourceenvironment_pc_av34", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_pc_av34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_pc_av34"):
                opp_val = getattr(value, "resourceenvironment_pc_av34", None)
                setattr(value, "resourceenvironment_pc_av34", self)

    @property
    def seff_performance_pc_av12(self):
        return self.__seff_performance_pc_av12

    @seff_performance_pc_av12.setter
    def seff_performance_pc_av12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_core_pc_av_PCMRandomVariable__seff_performance_pc_av12", None)
        self.__seff_performance_pc_av12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc_av13"):
                opp_val = getattr(old_value, "seff_pc_av13", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc_av13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc_av13"):
                opp_val = getattr(value, "seff_pc_av13", None)
                setattr(value, "seff_pc_av13", self)

    @property
    def CommunicationLinkResourceSpecification36(self):
        return self.__CommunicationLinkResourceSpecification36

    @CommunicationLinkResourceSpecification36.setter
    def CommunicationLinkResourceSpecification36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_core_pc_av_PCMRandomVariable__CommunicationLinkResourceSpecification36", None)
        self.__CommunicationLinkResourceSpecification36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_pc_av37"):
                opp_val = getattr(old_value, "resourceenvironment_pc_av37", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_pc_av37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_pc_av37"):
                opp_val = getattr(value, "resourceenvironment_pc_av37", None)
                setattr(value, "resourceenvironment_pc_av37", self)

    @property
    def Delay(self):
        return self.__Delay

    @Delay.setter
    def Delay(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_core_pc_av_PCMRandomVariable__Delay", None)
        self.__Delay = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc_av31"):
                opp_val = getattr(old_value, "usagemodel_pc_av31", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc_av31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc_av31"):
                opp_val = getattr(value, "usagemodel_pc_av31", None)
                setattr(value, "usagemodel_pc_av31", self)

    @property
    def composition_pc_av24(self):
        return self.__composition_pc_av24

    @composition_pc_av24.setter
    def composition_pc_av24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_core_pc_av_PCMRandomVariable__composition_pc_av24", None)
        self.__composition_pc_av24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc_av25"):
                opp_val = getattr(old_value, "core_pc_av25", None)
                if opp_val == self:
                    setattr(old_value, "core_pc_av25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc_av25"):
                opp_val = getattr(value, "core_pc_av25", None)
                setattr(value, "core_pc_av25", self)

    @property
    def ClosedWorkload(self):
        return self.__ClosedWorkload

    @ClosedWorkload.setter
    def ClosedWorkload(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_core_pc_av_PCMRandomVariable__ClosedWorkload", None)
        self.__ClosedWorkload = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc_av"):
                opp_val = getattr(old_value, "usagemodel_pc_av", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc_av"):
                opp_val = getattr(value, "usagemodel_pc_av", None)
                setattr(value, "usagemodel_pc_av", self)

    @property
    def seff_performance_pc_av(self):
        return self.__seff_performance_pc_av

    @seff_performance_pc_av.setter
    def seff_performance_pc_av(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_core_pc_av_PCMRandomVariable__seff_performance_pc_av", None)
        self.__seff_performance_pc_av = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc_av"):
                opp_val = getattr(old_value, "seff_pc_av", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc_av", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc_av"):
                opp_val = getattr(value, "seff_pc_av", None)
                setattr(value, "seff_pc_av", self)

    @property
    def GuardedBranchTransition(self):
        return self.__GuardedBranchTransition

    @GuardedBranchTransition.setter
    def GuardedBranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_core_pc_av_PCMRandomVariable__GuardedBranchTransition", None)
        self.__GuardedBranchTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc_av20"):
                opp_val = getattr(old_value, "seff_pc_av20", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc_av20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc_av20"):
                opp_val = getattr(value, "seff_pc_av20", None)
                setattr(value, "seff_pc_av20", self)

    @property
    def OpenWorkload(self):
        return self.__OpenWorkload

    @OpenWorkload.setter
    def OpenWorkload(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_av_core_pc_av_PCMRandomVariable__OpenWorkload", None)
        self.__OpenWorkload = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc_av29"):
                opp_val = getattr(old_value, "usagemodel_pc_av29", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc_av29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc_av29"):
                opp_val = getattr(value, "usagemodel_pc_av29", None)
                setattr(value, "usagemodel_pc_av29", self)

    def SpecificationMustNotBeNULL(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SpecificationMustNotBeNULL method
        pass

class pcm_pc_av_PerJoinPointScope:

    pass