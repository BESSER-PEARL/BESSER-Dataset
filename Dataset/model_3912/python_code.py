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
    INT = "INT"
    STRING = "STRING"
    BOOL = "BOOL"
    DOUBLE = "DOUBLE"
    CHAR = "CHAR"
    BYTE = "BYTE"
    LONG = "LONG"


############################################
# Definition of Classes
############################################

class repository_av_pc_RepositoryComponent:

    pass
class AllocationContext:

    pass
class ParametricResourceDemand:

    pass
class pcm_av_pc_completions_av_pc_NetworkDemandParametricResourceDemand(ParametricResourceDemand):

    pass
class ExternalCallAction:

    pass
class pcm_av_pc_completions_av_pc_DelegatingExternalCallAction(ExternalCallAction):

    pass
class Completion:

    pass
class pcm_av_pc_completions_av_pc_CompletionRepository:

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
class pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction:

    pass
class SpecifiedExecutionTime:

    pass
class pcm_av_pc_qos_performance_av_pc_ComponentSpecifiedExecutionTime(SpecifiedExecutionTime):

    pass
class pcm_av_pc_qos_performance_av_pc_SystemSpecifiedExecutionTime(SpecifiedExecutionTime):

    def __init__(self):
        
    def SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem method
        pass

class seff_reliability_av_pc_RecoveryAction:

    pass
class seff_reliability_av_pc_RecoveryActionBehaviour:

    pass
class SpecifiedQoSAnnotation:

    pass
class pcm_av_pc_qos_performance_av_pc_SpecifiedExecutionTime(SpecifiedQoSAnnotation):

    pass
class pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation(SpecifiedQoSAnnotation):

    def __init__(self, ExternalFailureOccurrenceDescription: set["ExternalFailureOccurrenceDescription"] = None, qosannotations_av_pc608: "pcm_av_pc_qosannotations_av_pc_QoSAnnotations"):
        self.ExternalFailureOccurrenceDescription = ExternalFailureOccurrenceDescription if ExternalFailureOccurrenceDescription is not None else set()
        
    @property
    def ExternalFailureOccurrenceDescription(self):
        return self.__ExternalFailureOccurrenceDescription

    @ExternalFailureOccurrenceDescription.setter
    def ExternalFailureOccurrenceDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription", None)
        self.__ExternalFailureOccurrenceDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reliability_av_pc626"):
                    opp_val = getattr(item, "reliability_av_pc626", None)
                    
                    if opp_val == self:
                        setattr(item, "reliability_av_pc626", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reliability_av_pc626"):
                    opp_val = getattr(item, "reliability_av_pc626", None)
                    
                    setattr(item, "reliability_av_pc626", self)
                    

    def SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1 method
        pass

    def SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem method
        pass

    def MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed method
        pass

class System:

    pass
class QoSAnnotations:

    pass
class pcm_av_pc_qosannotations_av_pc_SpecifiedQoSAnnotation:

    pass
class pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand:

    def __init__(self, PCMRandomVariable580: "PCMRandomVariable" = None, pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand: "ProcessingResourceType" = None, AbstractInternalControlFlowAction585: "AbstractInternalControlFlowAction" = None):
        self.PCMRandomVariable580 = PCMRandomVariable580
        self.pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand = pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand
        self.AbstractInternalControlFlowAction585 = AbstractInternalControlFlowAction585
        
    @property
    def pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand(self):
        return self.__pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand

    @pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand.setter
    def pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand__pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand", None)
        self.__pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand = value
        
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
        old_value = getattr(self, f"_pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand__AbstractInternalControlFlowAction585", None)
        self.__AbstractInternalControlFlowAction585 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av_pc586"):
                opp_val = getattr(old_value, "seff_av_pc586", None)
                if opp_val == self:
                    setattr(old_value, "seff_av_pc586", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av_pc586"):
                opp_val = getattr(value, "seff_av_pc586", None)
                setattr(value, "seff_av_pc586", self)

    @property
    def PCMRandomVariable580(self):
        return self.__PCMRandomVariable580

    @PCMRandomVariable580.setter
    def PCMRandomVariable580(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand__PCMRandomVariable580", None)
        self.__PCMRandomVariable580 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av_pc581"):
                opp_val = getattr(old_value, "core_av_pc581", None)
                if opp_val == self:
                    setattr(old_value, "core_av_pc581", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av_pc581"):
                opp_val = getattr(value, "core_av_pc581", None)
                setattr(value, "core_av_pc581", self)

    def DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

class seff_av_pc_AbstractInternalControlFlowAction:

    pass
class seff_av_pc_CallAction:

    pass
class pcm_av_pc_seff_av_pc_InternalCallAction(seff_av_pc_CallAction, seff_av_pc_AbstractInternalControlFlowAction):

    pass
class seff_reliability_av_pc_FailureHandlingEntity:

    pass
class seff_av_pc_CallReturnAction:

    pass
class seff_av_pc_AbstractAction:

    pass
class pcm_av_pc_seff_av_pc_EmitEventAction(seff_av_pc_CallAction, seff_av_pc_AbstractAction):

    pass
class pcm_av_pc_seff_av_pc_ExternalCallAction(seff_av_pc_CallReturnAction, seff_reliability_av_pc_FailureHandlingEntity, seff_av_pc_AbstractAction):

    def __init__(self, retryCount: int, pcm_av_pc_seff_av_pc_ExternalCallAction: "OperationSignature" = None, pcm_av_pc_seff_av_pc_ExternalCallAction533: "OperationRequiredRole" = None):
        self.retryCount = retryCount
        self.pcm_av_pc_seff_av_pc_ExternalCallAction = pcm_av_pc_seff_av_pc_ExternalCallAction
        self.pcm_av_pc_seff_av_pc_ExternalCallAction533 = pcm_av_pc_seff_av_pc_ExternalCallAction533
        
    @property
    def retryCount(self) -> int:
        return self.__retryCount

    @retryCount.setter
    def retryCount(self, retryCount: int):
        self.__retryCount = retryCount

    @property
    def pcm_av_pc_seff_av_pc_ExternalCallAction(self):
        return self.__pcm_av_pc_seff_av_pc_ExternalCallAction

    @pcm_av_pc_seff_av_pc_ExternalCallAction.setter
    def pcm_av_pc_seff_av_pc_ExternalCallAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_av_pc_ExternalCallAction__pcm_av_pc_seff_av_pc_ExternalCallAction", None)
        self.__pcm_av_pc_seff_av_pc_ExternalCallAction = value
        
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

    @property
    def pcm_av_pc_seff_av_pc_ExternalCallAction533(self):
        return self.__pcm_av_pc_seff_av_pc_ExternalCallAction533

    @pcm_av_pc_seff_av_pc_ExternalCallAction533.setter
    def pcm_av_pc_seff_av_pc_ExternalCallAction533(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_av_pc_ExternalCallAction__pcm_av_pc_seff_av_pc_ExternalCallAction533", None)
        self.__pcm_av_pc_seff_av_pc_ExternalCallAction533 = value
        
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

    def OperationRequiredRoleMustBeReferencedByContainer(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement OperationRequiredRoleMustBeReferencedByContainer method
        pass

    def SignatureBelongsToRole(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SignatureBelongsToRole method
        pass

class pcm_av_pc_seff_av_pc_SynchronisationPoint:

    pass
class ForkAction:

    pass
class ForkedBehaviour:

    pass
class pcm_av_pc_seff_av_pc_CallAction:

    pass
class ResourceDemandingSEFF:

    pass
class ResourceDemandingInternalBehaviour:

    pass
class seff_av_pc_ResourceDemandingBehaviour:

    pass
class pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour(seff_av_pc_ResourceDemandingBehaviour, seff_reliability_av_pc_FailureHandlingEntity):

    def __init__(self, pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour: set["seff_reliability_av_pc_RecoveryActionBehaviour"] = None, seff_reliability_av_pc: "seff_reliability_av_pc_RecoveryAction" = None):
        self.pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour = pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour if pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour is not None else set()
        self.seff_reliability_av_pc = seff_reliability_av_pc
        
    @property
    def pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour(self):
        return self.__pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour

    @pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour.setter
    def pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour__pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour", None)
        self.__pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_reliability_av_pc_RecoveryActionBehaviour"):
                    opp_val = getattr(item, "seff_reliability_av_pc_RecoveryActionBehaviour", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_reliability_av_pc_RecoveryActionBehaviour", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_reliability_av_pc_RecoveryActionBehaviour"):
                    opp_val = getattr(item, "seff_reliability_av_pc_RecoveryActionBehaviour", None)
                    
                    setattr(item, "seff_reliability_av_pc_RecoveryActionBehaviour", self)
                    

    @property
    def seff_reliability_av_pc(self):
        return self.__seff_reliability_av_pc

    @seff_reliability_av_pc.setter
    def seff_reliability_av_pc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour__seff_reliability_av_pc", None)
        self.__seff_reliability_av_pc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av_pc589"):
                opp_val = getattr(old_value, "seff_av_pc589", None)
                if opp_val == self:
                    setattr(old_value, "seff_av_pc589", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av_pc589"):
                opp_val = getattr(value, "seff_av_pc589", None)
                setattr(value, "seff_av_pc589", self)

    def RecoveryActionBehaviourHasOnlyOnePredecessor(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RecoveryActionBehaviourHasOnlyOnePredecessor method
        pass

    def RecoveryActionBehaviourIsNotSuccessorOfItself(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement RecoveryActionBehaviourIsNotSuccessorOfItself method
        pass

    def SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes method
        pass

class seff_av_pc_ServiceEffectSpecification:

    pass
class pcm_av_pc_seff_av_pc_ServiceEffectSpecification:

    def __init__(self, seffTypeID: str, pcm_av_pc_seff_av_pc_ServiceEffectSpecification: "Signature" = None, BasicComponent500: "BasicComponent" = None):
        self.seffTypeID = seffTypeID
        self.pcm_av_pc_seff_av_pc_ServiceEffectSpecification = pcm_av_pc_seff_av_pc_ServiceEffectSpecification
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
        old_value = getattr(self, f"_pcm_av_pc_seff_av_pc_ServiceEffectSpecification__BasicComponent500", None)
        self.__BasicComponent500 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av_pc501"):
                opp_val = getattr(old_value, "repository_av_pc501", None)
                if opp_val == self:
                    setattr(old_value, "repository_av_pc501", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av_pc501"):
                opp_val = getattr(value, "repository_av_pc501", None)
                setattr(value, "repository_av_pc501", self)

    @property
    def pcm_av_pc_seff_av_pc_ServiceEffectSpecification(self):
        return self.__pcm_av_pc_seff_av_pc_ServiceEffectSpecification

    @pcm_av_pc_seff_av_pc_ServiceEffectSpecification.setter
    def pcm_av_pc_seff_av_pc_ServiceEffectSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_av_pc_ServiceEffectSpecification__pcm_av_pc_seff_av_pc_ServiceEffectSpecification", None)
        self.__pcm_av_pc_seff_av_pc_ServiceEffectSpecification = value
        
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

    def ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole method
        pass

class BranchAction:

    pass
class AbstractBranchTransition:

    pass
class pcm_av_pc_seff_av_pc_GuardedBranchTransition(AbstractBranchTransition):

    pass
class pcm_av_pc_seff_av_pc_ProbabilisticBranchTransition(AbstractBranchTransition):

    def __init__(self, branchProbability: float, seff_av_pc480: "pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour", seff_av_pc494: "pcm_av_pc_seff_av_pc_BranchAction"):
        self.branchProbability = branchProbability
        
    @property
    def branchProbability(self) -> float:
        return self.__branchProbability

    @branchProbability.setter
    def branchProbability(self, branchProbability: float):
        self.__branchProbability = branchProbability

class AbstractLoopAction:

    pass
class pcm_av_pc_seff_av_pc_LoopAction(AbstractLoopAction):

    pass
class pcm_av_pc_seff_av_pc_CollectionIteratorAction(AbstractLoopAction):

    pass
class AbstractInternalControlFlowAction:

    pass
class pcm_av_pc_seff_av_pc_AcquireAction(AbstractInternalControlFlowAction):

    def __init__(self, timeout: bool, timeoutValue: float, pcm_av_pc_seff_av_pc_AcquireAction: "PassiveResource" = None, seff_av_pc570: "pcm_av_pc_seff_performance_av_pc_ResourceCall", seff_av_pc564: "pcm_av_pc_seff_performance_av_pc_InfrastructureCall", seff_av_pc586: "pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand"):
        self.timeout = timeout
        self.timeoutValue = timeoutValue
        self.pcm_av_pc_seff_av_pc_AcquireAction = pcm_av_pc_seff_av_pc_AcquireAction
        
    @property
    def timeoutValue(self) -> float:
        return self.__timeoutValue

    @timeoutValue.setter
    def timeoutValue(self, timeoutValue: float):
        self.__timeoutValue = timeoutValue

    @property
    def timeout(self) -> bool:
        return self.__timeout

    @timeout.setter
    def timeout(self, timeout: bool):
        self.__timeout = timeout

    @property
    def pcm_av_pc_seff_av_pc_AcquireAction(self):
        return self.__pcm_av_pc_seff_av_pc_AcquireAction

    @pcm_av_pc_seff_av_pc_AcquireAction.setter
    def pcm_av_pc_seff_av_pc_AcquireAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_av_pc_AcquireAction__pcm_av_pc_seff_av_pc_AcquireAction", None)
        self.__pcm_av_pc_seff_av_pc_AcquireAction = value
        
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

class pcm_av_pc_seff_av_pc_StartAction(AbstractInternalControlFlowAction):

    def __init__(self, seff_av_pc570: "pcm_av_pc_seff_performance_av_pc_ResourceCall", seff_av_pc564: "pcm_av_pc_seff_performance_av_pc_InfrastructureCall", seff_av_pc586: "pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand"):
        
    def StartActionPredecessorMustNotBeDefined(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement StartActionPredecessorMustNotBeDefined method
        pass

class pcm_av_pc_seff_av_pc_BranchAction(AbstractInternalControlFlowAction):

    def __init__(self, AbstractBranchTransition493: set["AbstractBranchTransition"] = None, seff_av_pc570: "pcm_av_pc_seff_performance_av_pc_ResourceCall", seff_av_pc564: "pcm_av_pc_seff_performance_av_pc_InfrastructureCall", seff_av_pc586: "pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand"):
        self.AbstractBranchTransition493 = AbstractBranchTransition493 if AbstractBranchTransition493 is not None else set()
        
    @property
    def AbstractBranchTransition493(self):
        return self.__AbstractBranchTransition493

    @AbstractBranchTransition493.setter
    def AbstractBranchTransition493(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_av_pc_BranchAction__AbstractBranchTransition493", None)
        self.__AbstractBranchTransition493 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_av_pc494"):
                    opp_val = getattr(item, "seff_av_pc494", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_av_pc494", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_av_pc494"):
                    opp_val = getattr(item, "seff_av_pc494", None)
                    
                    setattr(item, "seff_av_pc494", self)
                    

    def AllProbabilisticBranchProbabilitiesMustSumUpTo1(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AllProbabilisticBranchProbabilitiesMustSumUpTo1 method
        pass

    def EitherGuardedBranchesOrProbabilisiticBranchTransitions(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EitherGuardedBranchesOrProbabilisiticBranchTransitions method
        pass

class pcm_av_pc_seff_reliability_av_pc_RecoveryAction(AbstractInternalControlFlowAction):

    def __init__(self, pcm_av_pc_seff_reliability_av_pc_RecoveryAction: "seff_reliability_av_pc_RecoveryActionBehaviour" = None, seff_reliability_av_pc593: set["seff_reliability_av_pc_RecoveryActionBehaviour"] = None, seff_av_pc570: "pcm_av_pc_seff_performance_av_pc_ResourceCall", seff_av_pc564: "pcm_av_pc_seff_performance_av_pc_InfrastructureCall", seff_av_pc586: "pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand"):
        self.pcm_av_pc_seff_reliability_av_pc_RecoveryAction = pcm_av_pc_seff_reliability_av_pc_RecoveryAction
        self.seff_reliability_av_pc593 = seff_reliability_av_pc593 if seff_reliability_av_pc593 is not None else set()
        
    @property
    def seff_reliability_av_pc593(self):
        return self.__seff_reliability_av_pc593

    @seff_reliability_av_pc593.setter
    def seff_reliability_av_pc593(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_reliability_av_pc_RecoveryAction__seff_reliability_av_pc593", None)
        self.__seff_reliability_av_pc593 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_av_pc594"):
                    opp_val = getattr(item, "seff_av_pc594", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_av_pc594", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_av_pc594"):
                    opp_val = getattr(item, "seff_av_pc594", None)
                    
                    setattr(item, "seff_av_pc594", self)
                    

    @property
    def pcm_av_pc_seff_reliability_av_pc_RecoveryAction(self):
        return self.__pcm_av_pc_seff_reliability_av_pc_RecoveryAction

    @pcm_av_pc_seff_reliability_av_pc_RecoveryAction.setter
    def pcm_av_pc_seff_reliability_av_pc_RecoveryAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_reliability_av_pc_RecoveryAction__pcm_av_pc_seff_reliability_av_pc_RecoveryAction", None)
        self.__pcm_av_pc_seff_reliability_av_pc_RecoveryAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_reliability_av_pc_RecoveryActionBehaviour591"):
                opp_val = getattr(old_value, "seff_reliability_av_pc_RecoveryActionBehaviour591", None)
                if opp_val == self:
                    setattr(old_value, "seff_reliability_av_pc_RecoveryActionBehaviour591", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_reliability_av_pc_RecoveryActionBehaviour591"):
                opp_val = getattr(value, "seff_reliability_av_pc_RecoveryActionBehaviour591", None)
                setattr(value, "seff_reliability_av_pc_RecoveryActionBehaviour591", self)

    def PrimaryBehaviourOfRecoveryActionMustBeSet(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement PrimaryBehaviourOfRecoveryActionMustBeSet method
        pass

class pcm_av_pc_seff_av_pc_InternalAction(AbstractInternalControlFlowAction):

    def __init__(self, InternalFailureOccurrenceDescription556: set["InternalFailureOccurrenceDescription"] = None, seff_av_pc570: "pcm_av_pc_seff_performance_av_pc_ResourceCall", seff_av_pc564: "pcm_av_pc_seff_performance_av_pc_InfrastructureCall", seff_av_pc586: "pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand"):
        self.InternalFailureOccurrenceDescription556 = InternalFailureOccurrenceDescription556 if InternalFailureOccurrenceDescription556 is not None else set()
        
    @property
    def InternalFailureOccurrenceDescription556(self):
        return self.__InternalFailureOccurrenceDescription556

    @InternalFailureOccurrenceDescription556.setter
    def InternalFailureOccurrenceDescription556(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_av_pc_InternalAction__InternalFailureOccurrenceDescription556", None)
        self.__InternalFailureOccurrenceDescription556 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reliability_av_pc557"):
                    opp_val = getattr(item, "reliability_av_pc557", None)
                    
                    if opp_val == self:
                        setattr(item, "reliability_av_pc557", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reliability_av_pc557"):
                    opp_val = getattr(item, "reliability_av_pc557", None)
                    
                    setattr(item, "reliability_av_pc557", self)
                    

    def MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed method
        pass

    def SumOfInternalActionFailureProbabilitiesMustNotExceed1(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SumOfInternalActionFailureProbabilitiesMustNotExceed1 method
        pass

class pcm_av_pc_seff_av_pc_SetVariableAction(AbstractInternalControlFlowAction):

    pass
class pcm_av_pc_seff_av_pc_ForkAction(AbstractInternalControlFlowAction):

    pass
class pcm_av_pc_seff_av_pc_ReleaseAction(AbstractInternalControlFlowAction):

    pass
class pcm_av_pc_seff_av_pc_AbstractLoopAction(AbstractInternalControlFlowAction):

    pass
class pcm_av_pc_seff_av_pc_StopAction(AbstractInternalControlFlowAction):

    def __init__(self, seff_av_pc570: "pcm_av_pc_seff_performance_av_pc_ResourceCall", seff_av_pc564: "pcm_av_pc_seff_performance_av_pc_InfrastructureCall", seff_av_pc586: "pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand"):
        
    def StopActionSuccessorMustNotBeDefined(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement StopActionSuccessorMustNotBeDefined method
        pass

class ResourceDemandingBehaviour:

    pass
class pcm_av_pc_seff_av_pc_ForkedBehaviour(ResourceDemandingBehaviour):

    pass
class pcm_av_pc_seff_av_pc_ResourceDemandingInternalBehaviour(ResourceDemandingBehaviour):

    pass
class AbstractAction:

    pass
class pcm_av_pc_seff_av_pc_AbstractInternalControlFlowAction(AbstractAction):

    pass
class FailureOccurrenceDescription:

    pass
class pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription(FailureOccurrenceDescription):

    def __init__(self, InternalAction: "InternalAction" = None, SoftwareInducedFailureType: "SoftwareInducedFailureType" = None):
        self.InternalAction = InternalAction
        self.SoftwareInducedFailureType = SoftwareInducedFailureType
        
    @property
    def InternalAction(self):
        return self.__InternalAction

    @InternalAction.setter
    def InternalAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription__InternalAction", None)
        self.__InternalAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av_pc446"):
                opp_val = getattr(old_value, "seff_av_pc446", None)
                if opp_val == self:
                    setattr(old_value, "seff_av_pc446", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av_pc446"):
                opp_val = getattr(value, "seff_av_pc446", None)
                setattr(value, "seff_av_pc446", self)

    @property
    def SoftwareInducedFailureType(self):
        return self.__SoftwareInducedFailureType

    @SoftwareInducedFailureType.setter
    def SoftwareInducedFailureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription__SoftwareInducedFailureType", None)
        self.__SoftwareInducedFailureType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reliability_av_pc448"):
                opp_val = getattr(old_value, "reliability_av_pc448", None)
                if opp_val == self:
                    setattr(old_value, "reliability_av_pc448", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reliability_av_pc448"):
                opp_val = getattr(value, "reliability_av_pc448", None)
                setattr(value, "reliability_av_pc448", self)

    def NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription method
        pass

class InternalFailureOccurrenceDescription:

    pass
class ProcessingResourceType:

    pass
class qos_reliability_av_pc_SpecifiedReliabilityAnnotation:

    pass
class pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription(FailureOccurrenceDescription):

    def __init__(self, qos_reliability_av_pc: "qos_reliability_av_pc_SpecifiedReliabilityAnnotation" = None, pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription: "FailureType" = None):
        self.qos_reliability_av_pc = qos_reliability_av_pc
        self.pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription = pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription
        
    @property
    def pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription(self):
        return self.__pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription

    @pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription.setter
    def pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription__pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription", None)
        self.__pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription = value
        
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

    @property
    def qos_reliability_av_pc(self):
        return self.__qos_reliability_av_pc

    @qos_reliability_av_pc.setter
    def qos_reliability_av_pc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription__qos_reliability_av_pc", None)
        self.__qos_reliability_av_pc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qosannotations_av_pc452"):
                opp_val = getattr(old_value, "qosannotations_av_pc452", None)
                if opp_val == self:
                    setattr(old_value, "qosannotations_av_pc452", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qosannotations_av_pc452"):
                opp_val = getattr(value, "qosannotations_av_pc452", None)
                setattr(value, "qosannotations_av_pc452", self)

    def NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription method
        pass

class CommunicationLinkResourceType:

    pass
class SoftwareInducedFailureType:

    pass
class pcm_av_pc_reliability_av_pc_ResourceTimeoutFailureType(SoftwareInducedFailureType):

    pass
class InternalAction:

    pass
class pcm_av_pc_parameter_av_pc_VariableCharacterisation:

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
    def PCMRandomVariable436(self):
        return self.__PCMRandomVariable436

    @PCMRandomVariable436.setter
    def PCMRandomVariable436(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_parameter_av_pc_VariableCharacterisation__PCMRandomVariable436", None)
        self.__PCMRandomVariable436 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av_pc437"):
                opp_val = getattr(old_value, "core_av_pc437", None)
                if opp_val == self:
                    setattr(old_value, "core_av_pc437", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av_pc437"):
                opp_val = getattr(value, "core_av_pc437", None)
                setattr(value, "core_av_pc437", self)

    @property
    def VariableUsage439(self):
        return self.__VariableUsage439

    @VariableUsage439.setter
    def VariableUsage439(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_parameter_av_pc_VariableCharacterisation__VariableUsage439", None)
        self.__VariableUsage439 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameter_av_pc440"):
                opp_val = getattr(old_value, "parameter_av_pc440", None)
                if opp_val == self:
                    setattr(old_value, "parameter_av_pc440", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameter_av_pc440"):
                opp_val = getattr(value, "parameter_av_pc440", None)
                setattr(value, "parameter_av_pc440", self)

class parameter_av_pc_pcm_av_pc_AbstractNamedReference:

    pass
class EntryLevelSystemCall:

    pass
class pcm_av_pc_reliability_av_pc_FailureOccurrenceDescription:

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
class pcm_av_pc_parameter_av_pc_CharacterisedVariable(Variable):

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
class pcm_av_pc_seff_performance_av_pc_ResourceCall(CallAction):

    def __init__(self, AbstractInternalControlFlowAction569: "AbstractInternalControlFlowAction" = None, pcm_av_pc_seff_performance_av_pc_ResourceCall: "entity_av_pc_ResourceRequiredRole" = None, pcm_av_pc_seff_performance_av_pc_ResourceCall574: "ResourceSignature" = None, PCMRandomVariable577: "PCMRandomVariable" = None, seff_av_pc417: "pcm_av_pc_parameter_av_pc_VariableUsage"):
        self.AbstractInternalControlFlowAction569 = AbstractInternalControlFlowAction569
        self.pcm_av_pc_seff_performance_av_pc_ResourceCall = pcm_av_pc_seff_performance_av_pc_ResourceCall
        self.pcm_av_pc_seff_performance_av_pc_ResourceCall574 = pcm_av_pc_seff_performance_av_pc_ResourceCall574
        self.PCMRandomVariable577 = PCMRandomVariable577
        
    @property
    def pcm_av_pc_seff_performance_av_pc_ResourceCall(self):
        return self.__pcm_av_pc_seff_performance_av_pc_ResourceCall

    @pcm_av_pc_seff_performance_av_pc_ResourceCall.setter
    def pcm_av_pc_seff_performance_av_pc_ResourceCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_performance_av_pc_ResourceCall__pcm_av_pc_seff_performance_av_pc_ResourceCall", None)
        self.__pcm_av_pc_seff_performance_av_pc_ResourceCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entity_av_pc_ResourceRequiredRole572"):
                opp_val = getattr(old_value, "entity_av_pc_ResourceRequiredRole572", None)
                if opp_val == self:
                    setattr(old_value, "entity_av_pc_ResourceRequiredRole572", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entity_av_pc_ResourceRequiredRole572"):
                opp_val = getattr(value, "entity_av_pc_ResourceRequiredRole572", None)
                setattr(value, "entity_av_pc_ResourceRequiredRole572", self)

    @property
    def AbstractInternalControlFlowAction569(self):
        return self.__AbstractInternalControlFlowAction569

    @AbstractInternalControlFlowAction569.setter
    def AbstractInternalControlFlowAction569(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_performance_av_pc_ResourceCall__AbstractInternalControlFlowAction569", None)
        self.__AbstractInternalControlFlowAction569 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av_pc570"):
                opp_val = getattr(old_value, "seff_av_pc570", None)
                if opp_val == self:
                    setattr(old_value, "seff_av_pc570", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av_pc570"):
                opp_val = getattr(value, "seff_av_pc570", None)
                setattr(value, "seff_av_pc570", self)

    @property
    def pcm_av_pc_seff_performance_av_pc_ResourceCall574(self):
        return self.__pcm_av_pc_seff_performance_av_pc_ResourceCall574

    @pcm_av_pc_seff_performance_av_pc_ResourceCall574.setter
    def pcm_av_pc_seff_performance_av_pc_ResourceCall574(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_performance_av_pc_ResourceCall__pcm_av_pc_seff_performance_av_pc_ResourceCall574", None)
        self.__pcm_av_pc_seff_performance_av_pc_ResourceCall574 = value
        
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
    def PCMRandomVariable577(self):
        return self.__PCMRandomVariable577

    @PCMRandomVariable577.setter
    def PCMRandomVariable577(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_performance_av_pc_ResourceCall__PCMRandomVariable577", None)
        self.__PCMRandomVariable577 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av_pc578"):
                opp_val = getattr(old_value, "core_av_pc578", None)
                if opp_val == self:
                    setattr(old_value, "core_av_pc578", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av_pc578"):
                opp_val = getattr(value, "core_av_pc578", None)
                setattr(value, "core_av_pc578", self)

    def ResourceRequiredRoleMustBeReferencedByComponent(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ResourceRequiredRoleMustBeReferencedByComponent method
        pass

    def ResourceSignatureBelongsToResourceRequiredRole(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceSignatureBelongsToResourceRequiredRole method
        pass

    def SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

class pcm_av_pc_seff_av_pc_CallReturnAction(CallAction):

    pass
class pcm_av_pc_seff_performance_av_pc_InfrastructureCall(CallAction):

    def __init__(self, pcm_av_pc_seff_performance_av_pc_InfrastructureCall: "InfrastructureSignature" = None, PCMRandomVariable561: "PCMRandomVariable" = None, AbstractInternalControlFlowAction: "AbstractInternalControlFlowAction" = None, pcm_av_pc_seff_performance_av_pc_InfrastructureCall566: "InfrastructureRequiredRole" = None, seff_av_pc417: "pcm_av_pc_parameter_av_pc_VariableUsage"):
        self.pcm_av_pc_seff_performance_av_pc_InfrastructureCall = pcm_av_pc_seff_performance_av_pc_InfrastructureCall
        self.PCMRandomVariable561 = PCMRandomVariable561
        self.AbstractInternalControlFlowAction = AbstractInternalControlFlowAction
        self.pcm_av_pc_seff_performance_av_pc_InfrastructureCall566 = pcm_av_pc_seff_performance_av_pc_InfrastructureCall566
        
    @property
    def AbstractInternalControlFlowAction(self):
        return self.__AbstractInternalControlFlowAction

    @AbstractInternalControlFlowAction.setter
    def AbstractInternalControlFlowAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_performance_av_pc_InfrastructureCall__AbstractInternalControlFlowAction", None)
        self.__AbstractInternalControlFlowAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av_pc564"):
                opp_val = getattr(old_value, "seff_av_pc564", None)
                if opp_val == self:
                    setattr(old_value, "seff_av_pc564", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av_pc564"):
                opp_val = getattr(value, "seff_av_pc564", None)
                setattr(value, "seff_av_pc564", self)

    @property
    def pcm_av_pc_seff_performance_av_pc_InfrastructureCall(self):
        return self.__pcm_av_pc_seff_performance_av_pc_InfrastructureCall

    @pcm_av_pc_seff_performance_av_pc_InfrastructureCall.setter
    def pcm_av_pc_seff_performance_av_pc_InfrastructureCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_performance_av_pc_InfrastructureCall__pcm_av_pc_seff_performance_av_pc_InfrastructureCall", None)
        self.__pcm_av_pc_seff_performance_av_pc_InfrastructureCall = value
        
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
    def pcm_av_pc_seff_performance_av_pc_InfrastructureCall566(self):
        return self.__pcm_av_pc_seff_performance_av_pc_InfrastructureCall566

    @pcm_av_pc_seff_performance_av_pc_InfrastructureCall566.setter
    def pcm_av_pc_seff_performance_av_pc_InfrastructureCall566(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_performance_av_pc_InfrastructureCall__pcm_av_pc_seff_performance_av_pc_InfrastructureCall566", None)
        self.__pcm_av_pc_seff_performance_av_pc_InfrastructureCall566 = value
        
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
    def PCMRandomVariable561(self):
        return self.__PCMRandomVariable561

    @PCMRandomVariable561.setter
    def PCMRandomVariable561(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_performance_av_pc_InfrastructureCall__PCMRandomVariable561", None)
        self.__PCMRandomVariable561 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av_pc562"):
                opp_val = getattr(old_value, "core_av_pc562", None)
                if opp_val == self:
                    setattr(old_value, "core_av_pc562", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av_pc562"):
                opp_val = getattr(value, "core_av_pc562", None)
                setattr(value, "core_av_pc562", self)

    def SignatureMustBelongToUsedRequiredRole(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SignatureMustBelongToUsedRequiredRole method
        pass

    def SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

    def ReferencedRequiredRoleMustBeRequiredByComponent(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ReferencedRequiredRoleMustBeRequiredByComponent method
        pass

class pcm_av_pc_parameter_av_pc_VariableUsage:

    pass
class pcm_av_pc_protocol_av_pc_Protocol:

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
class CompositeDataType:

    pass
class pcm_av_pc_resourcetype_av_pc_ResourceRepository:

    pass
class ResourceRepository:

    pass
class UnitCarryingElement:

    pass
class HardwareInducedFailureType:

    pass
class ResourceType:

    pass
class pcm_av_pc_resourcetype_av_pc_CommunicationLinkResourceType(ResourceType):

    pass
class pcm_av_pc_resourcetype_av_pc_ProcessingResourceType(ResourceType):

    pass
class NamedElement:

    pass
class pcm_av_pc_resourceenvironment_av_pc_ResourceEnvironment(NamedElement):

    pass
class pcm_av_pc_repository_av_pc_InnerDeclaration(NamedElement):

    pass
class InnerDeclaration:

    pass
class repository_av_pc_DataType:

    pass
class repository_av_pc_ImplementationComponentType:

    pass
class entity_av_pc_ComposedProvidingRequiringEntity:

    pass
class pcm_av_pc_completions_av_pc_Completion(entity_av_pc_ComposedProvidingRequiringEntity, repository_av_pc_ImplementationComponentType):

    pass
class pcm_av_pc_subsystem_av_pc_SubSystem(entity_av_pc_ComposedProvidingRequiringEntity, repository_av_pc_RepositoryComponent):

    pass
class pcm_av_pc_repository_av_pc_CompositeComponent(repository_av_pc_ImplementationComponentType, entity_av_pc_ComposedProvidingRequiringEntity):

    def __init__(self):
        
    def RequireSameInterfaces(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement RequireSameInterfaces method
        pass

    def ProvideSameInterfaces(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ProvideSameInterfaces method
        pass

class ProvidesComponentType:

    pass
class OperationInterface:

    pass
class InfrastructureInterface:

    pass
class pcm_av_pc_repository_av_pc_ExceptionType:

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
class pcm_av_pc_repository_av_pc_InfrastructureSignature(Signature):

    pass
class pcm_av_pc_repository_av_pc_EventType(Signature):

    pass
class Protocol:

    pass
class Parameter:

    pass
class pcm_av_pc_repository_av_pc_OperationSignature(Signature):

    def __init__(self, pcm_av_pc_repository_av_pc_OperationSignature: "DataType" = None, OperationInterface: "OperationInterface" = None, Parameter354: set["Parameter"] = None, Signature598: "pcm_av_pc_qosannotations_av_pc_SpecifiedQoSAnnotation", Signature610: "pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction", Signature: "pcm_av_pc_seff_av_pc_ServiceEffectSpecification"):
        self.pcm_av_pc_repository_av_pc_OperationSignature = pcm_av_pc_repository_av_pc_OperationSignature
        self.OperationInterface = OperationInterface
        self.Parameter354 = Parameter354 if Parameter354 is not None else set()
        
    @property
    def OperationInterface(self):
        return self.__OperationInterface

    @OperationInterface.setter
    def OperationInterface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_OperationSignature__OperationInterface", None)
        self.__OperationInterface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av_pc352"):
                opp_val = getattr(old_value, "repository_av_pc352", None)
                if opp_val == self:
                    setattr(old_value, "repository_av_pc352", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av_pc352"):
                opp_val = getattr(value, "repository_av_pc352", None)
                setattr(value, "repository_av_pc352", self)

    @property
    def Parameter354(self):
        return self.__Parameter354

    @Parameter354.setter
    def Parameter354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_OperationSignature__Parameter354", None)
        self.__Parameter354 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_av_pc355"):
                    opp_val = getattr(item, "repository_av_pc355", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_av_pc355", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_av_pc355"):
                    opp_val = getattr(item, "repository_av_pc355", None)
                    
                    setattr(item, "repository_av_pc355", self)
                    

    @property
    def pcm_av_pc_repository_av_pc_OperationSignature(self):
        return self.__pcm_av_pc_repository_av_pc_OperationSignature

    @pcm_av_pc_repository_av_pc_OperationSignature.setter
    def pcm_av_pc_repository_av_pc_OperationSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_OperationSignature__pcm_av_pc_repository_av_pc_OperationSignature", None)
        self.__pcm_av_pc_repository_av_pc_OperationSignature = value
        
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

    def ParameterNamesHaveToBeUniqueForASignature(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ParameterNamesHaveToBeUniqueForASignature method
        pass

class pcm_av_pc_repository_av_pc_RequiredCharacterisation:

    def __init__(self, type: str, pcm_av_pc_repository_av_pc_RequiredCharacterisation: "Parameter" = None, Interface323: "Interface" = None):
        self.type = type
        self.pcm_av_pc_repository_av_pc_RequiredCharacterisation = pcm_av_pc_repository_av_pc_RequiredCharacterisation
        self.Interface323 = Interface323
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def pcm_av_pc_repository_av_pc_RequiredCharacterisation(self):
        return self.__pcm_av_pc_repository_av_pc_RequiredCharacterisation

    @pcm_av_pc_repository_av_pc_RequiredCharacterisation.setter
    def pcm_av_pc_repository_av_pc_RequiredCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_RequiredCharacterisation__pcm_av_pc_repository_av_pc_RequiredCharacterisation", None)
        self.__pcm_av_pc_repository_av_pc_RequiredCharacterisation = value
        
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
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_RequiredCharacterisation__Interface323", None)
        self.__Interface323 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av_pc324"):
                opp_val = getattr(old_value, "repository_av_pc324", None)
                if opp_val == self:
                    setattr(old_value, "repository_av_pc324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av_pc324"):
                opp_val = getattr(value, "repository_av_pc324", None)
                setattr(value, "repository_av_pc324", self)

class RequiredCharacterisation:

    pass
class EventType:

    pass
class InfrastructureSignature:

    pass
class DataType:

    pass
class pcm_av_pc_repository_av_pc_PrimitiveDataType(DataType):

    def __init__(self, type: str, DataType: "pcm_av_pc_repository_av_pc_Parameter", DataType378: "pcm_av_pc_repository_av_pc_InnerDeclaration", repository_av_pc311: "pcm_av_pc_repository_av_pc_Repository", DataType357: "pcm_av_pc_repository_av_pc_OperationSignature", DataType373: "pcm_av_pc_repository_av_pc_CollectionDataType"):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class pcm_av_pc_repository_av_pc_Parameter:

    def __init__(self, parameterName: str, modifier__Parameter: str, ResourceSignature: "ResourceSignature" = None, pcm_av_pc_repository_av_pc_Parameter: "DataType" = None, InfrastructureSignature: "InfrastructureSignature" = None, OperationSignature294: "OperationSignature" = None, EventType: "EventType" = None):
        self.parameterName = parameterName
        self.modifier__Parameter = modifier__Parameter
        self.ResourceSignature = ResourceSignature
        self.pcm_av_pc_repository_av_pc_Parameter = pcm_av_pc_repository_av_pc_Parameter
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
    def EventType(self):
        return self.__EventType

    @EventType.setter
    def EventType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_Parameter__EventType", None)
        self.__EventType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av_pc297"):
                opp_val = getattr(old_value, "repository_av_pc297", None)
                if opp_val == self:
                    setattr(old_value, "repository_av_pc297", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av_pc297"):
                opp_val = getattr(value, "repository_av_pc297", None)
                setattr(value, "repository_av_pc297", self)

    @property
    def InfrastructureSignature(self):
        return self.__InfrastructureSignature

    @InfrastructureSignature.setter
    def InfrastructureSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_Parameter__InfrastructureSignature", None)
        self.__InfrastructureSignature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av_pc292"):
                opp_val = getattr(old_value, "repository_av_pc292", None)
                if opp_val == self:
                    setattr(old_value, "repository_av_pc292", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av_pc292"):
                opp_val = getattr(value, "repository_av_pc292", None)
                setattr(value, "repository_av_pc292", self)

    @property
    def pcm_av_pc_repository_av_pc_Parameter(self):
        return self.__pcm_av_pc_repository_av_pc_Parameter

    @pcm_av_pc_repository_av_pc_Parameter.setter
    def pcm_av_pc_repository_av_pc_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_Parameter__pcm_av_pc_repository_av_pc_Parameter", None)
        self.__pcm_av_pc_repository_av_pc_Parameter = value
        
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
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_Parameter__OperationSignature294", None)
        self.__OperationSignature294 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av_pc295"):
                opp_val = getattr(old_value, "repository_av_pc295", None)
                if opp_val == self:
                    setattr(old_value, "repository_av_pc295", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av_pc295"):
                opp_val = getattr(value, "repository_av_pc295", None)
                setattr(value, "repository_av_pc295", self)

    @property
    def ResourceSignature(self):
        return self.__ResourceSignature

    @ResourceSignature.setter
    def ResourceSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_Parameter__ResourceSignature", None)
        self.__ResourceSignature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcetype_av_pc"):
                opp_val = getattr(old_value, "resourcetype_av_pc", None)
                if opp_val == self:
                    setattr(old_value, "resourcetype_av_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcetype_av_pc"):
                opp_val = getattr(value, "resourcetype_av_pc", None)
                setattr(value, "resourcetype_av_pc", self)

class Repository:

    pass
class InterfaceProvidingRequiringEntity:

    pass
class pcm_av_pc_repository_av_pc_RepositoryComponent(InterfaceProvidingRequiringEntity):

    pass
class FailureType:

    pass
class pcm_av_pc_reliability_av_pc_NetworkInducedFailureType(FailureType):

    def __init__(self, CommunicationLinkResourceType: "CommunicationLinkResourceType" = None, FailureType596: "pcm_av_pc_seff_reliability_av_pc_FailureHandlingEntity", FailureType337: "pcm_av_pc_repository_av_pc_Signature", reliability_av_pc308: "pcm_av_pc_repository_av_pc_Repository", FailureType454: "pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription"):
        self.CommunicationLinkResourceType = CommunicationLinkResourceType
        
    @property
    def CommunicationLinkResourceType(self):
        return self.__CommunicationLinkResourceType

    @CommunicationLinkResourceType.setter
    def CommunicationLinkResourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_reliability_av_pc_NetworkInducedFailureType__CommunicationLinkResourceType", None)
        self.__CommunicationLinkResourceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcetype_av_pc450"):
                opp_val = getattr(old_value, "resourcetype_av_pc450", None)
                if opp_val == self:
                    setattr(old_value, "resourcetype_av_pc450", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcetype_av_pc450"):
                opp_val = getattr(value, "resourcetype_av_pc450", None)
                setattr(value, "resourcetype_av_pc450", self)

    def NetworkInducedFailureTypeHasCommunicationLinkResourceType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NetworkInducedFailureTypeHasCommunicationLinkResourceType method
        pass

class pcm_av_pc_reliability_av_pc_HardwareInducedFailureType(FailureType):

    def __init__(self, ProcessingResourceType: "ProcessingResourceType" = None, FailureType596: "pcm_av_pc_seff_reliability_av_pc_FailureHandlingEntity", FailureType337: "pcm_av_pc_repository_av_pc_Signature", reliability_av_pc308: "pcm_av_pc_repository_av_pc_Repository", FailureType454: "pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription"):
        self.ProcessingResourceType = ProcessingResourceType
        
    @property
    def ProcessingResourceType(self):
        return self.__ProcessingResourceType

    @ProcessingResourceType.setter
    def ProcessingResourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_reliability_av_pc_HardwareInducedFailureType__ProcessingResourceType", None)
        self.__ProcessingResourceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcetype_av_pc442"):
                opp_val = getattr(old_value, "resourcetype_av_pc442", None)
                if opp_val == self:
                    setattr(old_value, "resourcetype_av_pc442", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcetype_av_pc442"):
                opp_val = getattr(value, "resourcetype_av_pc442", None)
                setattr(value, "resourcetype_av_pc442", self)

    def HardwareInducedFailureTypeHasProcessingResourceType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement HardwareInducedFailureTypeHasProcessingResourceType method
        pass

class pcm_av_pc_reliability_av_pc_SoftwareInducedFailureType(FailureType):

    pass
class Interface:

    pass
class pcm_av_pc_repository_av_pc_InfrastructureInterface(Interface):

    pass
class pcm_av_pc_repository_av_pc_EventGroup(Interface):

    pass
class pcm_av_pc_repository_av_pc_OperationInterface(Interface):

    def __init__(self, OperationSignature359: set["OperationSignature"] = None, repository_av_pc324: "pcm_av_pc_repository_av_pc_RequiredCharacterisation", repository_av_pc306: "pcm_av_pc_repository_av_pc_Repository", Interface313: "pcm_av_pc_repository_av_pc_Interface"):
        self.OperationSignature359 = OperationSignature359 if OperationSignature359 is not None else set()
        
    @property
    def OperationSignature359(self):
        return self.__OperationSignature359

    @OperationSignature359.setter
    def OperationSignature359(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_OperationInterface__OperationSignature359", None)
        self.__OperationSignature359 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_av_pc360"):
                    opp_val = getattr(item, "repository_av_pc360", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_av_pc360", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_av_pc360"):
                    opp_val = getattr(item, "repository_av_pc360", None)
                    
                    setattr(item, "repository_av_pc360", self)
                    

    def SignaturesHaveToBeUniqueForAnInterface(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SignaturesHaveToBeUniqueForAnInterface method
        pass

class pcm_av_pc_repository_av_pc_DataType:

    pass
class ResourceSignature:

    pass
class ServiceEffectSpecification:

    pass
class CompleteComponentType:

    pass
class ImplementationComponentType:

    pass
class pcm_av_pc_repository_av_pc_BasicComponent(ImplementationComponentType):

    def __init__(self, ServiceEffectSpecification: set["ServiceEffectSpecification"] = None, PassiveResource279: set["PassiveResource"] = None):
        self.ServiceEffectSpecification = ServiceEffectSpecification if ServiceEffectSpecification is not None else set()
        self.PassiveResource279 = PassiveResource279 if PassiveResource279 is not None else set()
        
    @property
    def ServiceEffectSpecification(self):
        return self.__ServiceEffectSpecification

    @ServiceEffectSpecification.setter
    def ServiceEffectSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_BasicComponent__ServiceEffectSpecification", None)
        self.__ServiceEffectSpecification = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_av_pc277"):
                    opp_val = getattr(item, "seff_av_pc277", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_av_pc277", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_av_pc277"):
                    opp_val = getattr(item, "seff_av_pc277", None)
                    
                    setattr(item, "seff_av_pc277", self)
                    

    @property
    def PassiveResource279(self):
        return self.__PassiveResource279

    @PassiveResource279.setter
    def PassiveResource279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_BasicComponent__PassiveResource279", None)
        self.__PassiveResource279 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_av_pc280"):
                    opp_val = getattr(item, "repository_av_pc280", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_av_pc280", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_av_pc280"):
                    opp_val = getattr(item, "repository_av_pc280", None)
                    
                    setattr(item, "repository_av_pc280", self)
                    

    def RequireSameInterfacesAsImplementationType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RequireSameInterfacesAsImplementationType method
        pass

    def NoSeffTypeUsedTwice(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement NoSeffTypeUsedTwice method
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
class pcm_av_pc_usagemodel_av_pc_BranchTransition:

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
    def Branch(self):
        return self.__Branch

    @Branch.setter
    def Branch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_BranchTransition__Branch", None)
        self.__Branch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av_pc248"):
                opp_val = getattr(old_value, "usagemodel_av_pc248", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av_pc248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av_pc248"):
                opp_val = getattr(value, "usagemodel_av_pc248", None)
                setattr(value, "usagemodel_av_pc248", self)

    @property
    def ScenarioBehaviour250(self):
        return self.__ScenarioBehaviour250

    @ScenarioBehaviour250.setter
    def ScenarioBehaviour250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_BranchTransition__ScenarioBehaviour250", None)
        self.__ScenarioBehaviour250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av_pc251"):
                opp_val = getattr(old_value, "usagemodel_av_pc251", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av_pc251", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av_pc251"):
                opp_val = getattr(value, "usagemodel_av_pc251", None)
                setattr(value, "usagemodel_av_pc251", self)

class BranchTransition:

    pass
class AbstractUserAction:

    pass
class pcm_av_pc_usagemodel_av_pc_Stop(AbstractUserAction):

    def __init__(self, usagemodel_av_pc229: "pcm_av_pc_usagemodel_av_pc_AbstractUserAction", usagemodel_av_pc232: "pcm_av_pc_usagemodel_av_pc_AbstractUserAction", usagemodel_av_pc246: "pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour"):
        
    def StopHasNoSuccessor(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement StopHasNoSuccessor method
        pass

class pcm_av_pc_usagemodel_av_pc_Delay(AbstractUserAction):

    pass
class pcm_av_pc_usagemodel_av_pc_Start(AbstractUserAction):

    def __init__(self, usagemodel_av_pc229: "pcm_av_pc_usagemodel_av_pc_AbstractUserAction", usagemodel_av_pc232: "pcm_av_pc_usagemodel_av_pc_AbstractUserAction", usagemodel_av_pc246: "pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour"):
        
    def StartHasNoPredecessor(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement StartHasNoPredecessor method
        pass

class pcm_av_pc_usagemodel_av_pc_Loop(AbstractUserAction):

    pass
class pcm_av_pc_usagemodel_av_pc_Branch(AbstractUserAction):

    def __init__(self, BranchTransition253: set["BranchTransition"] = None, usagemodel_av_pc229: "pcm_av_pc_usagemodel_av_pc_AbstractUserAction", usagemodel_av_pc232: "pcm_av_pc_usagemodel_av_pc_AbstractUserAction", usagemodel_av_pc246: "pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour"):
        self.BranchTransition253 = BranchTransition253 if BranchTransition253 is not None else set()
        
    @property
    def BranchTransition253(self):
        return self.__BranchTransition253

    @BranchTransition253.setter
    def BranchTransition253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_Branch__BranchTransition253", None)
        self.__BranchTransition253 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "usagemodel_av_pc254"):
                    opp_val = getattr(item, "usagemodel_av_pc254", None)
                    
                    if opp_val == self:
                        setattr(item, "usagemodel_av_pc254", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "usagemodel_av_pc254"):
                    opp_val = getattr(item, "usagemodel_av_pc254", None)
                    
                    setattr(item, "usagemodel_av_pc254", self)
                    

    def AllBranchProbabilitiesMustSumUpTo1(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AllBranchProbabilitiesMustSumUpTo1 method
        pass

class pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall(AbstractUserAction):

    def __init__(self, priority: int, pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall: "OperationProvidedRole" = None, pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall221: "OperationSignature" = None, VariableUsage223: set["VariableUsage"] = None, VariableUsage226: set["VariableUsage"] = None, usagemodel_av_pc229: "pcm_av_pc_usagemodel_av_pc_AbstractUserAction", usagemodel_av_pc232: "pcm_av_pc_usagemodel_av_pc_AbstractUserAction", usagemodel_av_pc246: "pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour"):
        self.priority = priority
        self.pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall = pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall
        self.pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall221 = pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall221
        self.VariableUsage223 = VariableUsage223 if VariableUsage223 is not None else set()
        self.VariableUsage226 = VariableUsage226 if VariableUsage226 is not None else set()
        
    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall(self):
        return self.__pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall

    @pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall.setter
    def pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall__pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall", None)
        self.__pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall = value
        
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
    def VariableUsage223(self):
        return self.__VariableUsage223

    @VariableUsage223.setter
    def VariableUsage223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall__VariableUsage223", None)
        self.__VariableUsage223 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "parameter_av_pc224"):
                    opp_val = getattr(item, "parameter_av_pc224", None)
                    
                    if opp_val == self:
                        setattr(item, "parameter_av_pc224", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "parameter_av_pc224"):
                    opp_val = getattr(item, "parameter_av_pc224", None)
                    
                    setattr(item, "parameter_av_pc224", self)
                    

    @property
    def VariableUsage226(self):
        return self.__VariableUsage226

    @VariableUsage226.setter
    def VariableUsage226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall__VariableUsage226", None)
        self.__VariableUsage226 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "parameter_av_pc227"):
                    opp_val = getattr(item, "parameter_av_pc227", None)
                    
                    if opp_val == self:
                        setattr(item, "parameter_av_pc227", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "parameter_av_pc227"):
                    opp_val = getattr(item, "parameter_av_pc227", None)
                    
                    setattr(item, "parameter_av_pc227", self)
                    

    @property
    def pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall221(self):
        return self.__pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall221

    @pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall221.setter
    def pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall__pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall221", None)
        self.__pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall221 = value
        
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

    def EntryLevelSystemCallMustReferenceProvidedRoleOfASystem(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement EntryLevelSystemCallMustReferenceProvidedRoleOfASystem method
        pass

    def EntryLevelSystemCallSignatureMustMatchItsProvidedRole(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement EntryLevelSystemCallSignatureMustMatchItsProvidedRole method
        pass

class UserData:

    pass
class pcm_av_pc_usagemodel_av_pc_UsageModel:

    pass
class pcm_av_pc_usagemodel_av_pc_UserData:

    pass
class Workload:

    pass
class pcm_av_pc_usagemodel_av_pc_OpenWorkload(Workload):

    def __init__(self, PCMRandomVariable262: "PCMRandomVariable" = None, usagemodel_av_pc204: "pcm_av_pc_usagemodel_av_pc_UsageScenario"):
        self.PCMRandomVariable262 = PCMRandomVariable262
        
    @property
    def PCMRandomVariable262(self):
        return self.__PCMRandomVariable262

    @PCMRandomVariable262.setter
    def PCMRandomVariable262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_OpenWorkload__PCMRandomVariable262", None)
        self.__PCMRandomVariable262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av_pc263"):
                opp_val = getattr(old_value, "core_av_pc263", None)
                if opp_val == self:
                    setattr(old_value, "core_av_pc263", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av_pc263"):
                opp_val = getattr(value, "core_av_pc263", None)
                setattr(value, "core_av_pc263", self)

    def InterArrivalTimeInOpenWorkloadNeedsToBeSpecified(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement InterArrivalTimeInOpenWorkloadNeedsToBeSpecified method
        pass

class pcm_av_pc_usagemodel_av_pc_ClosedWorkload(Workload):

    def __init__(self, population: int, PCMRandomVariable268: "PCMRandomVariable" = None, usagemodel_av_pc204: "pcm_av_pc_usagemodel_av_pc_UsageScenario"):
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
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_ClosedWorkload__PCMRandomVariable268", None)
        self.__PCMRandomVariable268 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av_pc269"):
                opp_val = getattr(old_value, "core_av_pc269", None)
                if opp_val == self:
                    setattr(old_value, "core_av_pc269", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av_pc269"):
                opp_val = getattr(value, "core_av_pc269", None)
                setattr(value, "core_av_pc269", self)

    def PopulationInClosedWorkloadNeedsToBeSpecified(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement PopulationInClosedWorkloadNeedsToBeSpecified method
        pass

    def ThinkTimeInClosedWorkloadNeedsToBeSpecified(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ThinkTimeInClosedWorkloadNeedsToBeSpecified method
        pass

class ScenarioBehaviour:

    pass
class UsageModel:

    pass
class UsageScenario:

    pass
class pcm_av_pc_usagemodel_av_pc_Workload:

    pass
class OperationSignature:

    pass
class InfrastructureRequiredRole:

    pass
class InfrastructureProvidedRole:

    pass
class VariableUsage:

    pass
class RepositoryComponent:

    pass
class pcm_av_pc_repository_av_pc_CompleteComponentType(RepositoryComponent):

    def __init__(self, pcm_av_pc_repository_av_pc_CompleteComponentType: set["ProvidesComponentType"] = None, RepositoryComponent: "pcm_av_pc_composition_av_pc_AssemblyContext", repository_av_pc304: "pcm_av_pc_repository_av_pc_Repository"):
        self.pcm_av_pc_repository_av_pc_CompleteComponentType = pcm_av_pc_repository_av_pc_CompleteComponentType if pcm_av_pc_repository_av_pc_CompleteComponentType is not None else set()
        
    @property
    def pcm_av_pc_repository_av_pc_CompleteComponentType(self):
        return self.__pcm_av_pc_repository_av_pc_CompleteComponentType

    @pcm_av_pc_repository_av_pc_CompleteComponentType.setter
    def pcm_av_pc_repository_av_pc_CompleteComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_CompleteComponentType__pcm_av_pc_repository_av_pc_CompleteComponentType", None)
        self.__pcm_av_pc_repository_av_pc_CompleteComponentType = value if value is not None else set()
        
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

    def AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType method
        pass

class pcm_av_pc_repository_av_pc_ImplementationComponentType(RepositoryComponent):

    def __init__(self, componentType: str, pcm_av_pc_repository_av_pc_ImplementationComponentType: set["CompleteComponentType"] = None, pcm_av_pc_repository_av_pc_ImplementationComponentType283: set["VariableUsage"] = None, RepositoryComponent: "pcm_av_pc_composition_av_pc_AssemblyContext", repository_av_pc304: "pcm_av_pc_repository_av_pc_Repository"):
        self.componentType = componentType
        self.pcm_av_pc_repository_av_pc_ImplementationComponentType = pcm_av_pc_repository_av_pc_ImplementationComponentType if pcm_av_pc_repository_av_pc_ImplementationComponentType is not None else set()
        self.pcm_av_pc_repository_av_pc_ImplementationComponentType283 = pcm_av_pc_repository_av_pc_ImplementationComponentType283 if pcm_av_pc_repository_av_pc_ImplementationComponentType283 is not None else set()
        
    @property
    def componentType(self) -> str:
        return self.__componentType

    @componentType.setter
    def componentType(self, componentType: str):
        self.__componentType = componentType

    @property
    def pcm_av_pc_repository_av_pc_ImplementationComponentType283(self):
        return self.__pcm_av_pc_repository_av_pc_ImplementationComponentType283

    @pcm_av_pc_repository_av_pc_ImplementationComponentType283.setter
    def pcm_av_pc_repository_av_pc_ImplementationComponentType283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_ImplementationComponentType__pcm_av_pc_repository_av_pc_ImplementationComponentType283", None)
        self.__pcm_av_pc_repository_av_pc_ImplementationComponentType283 = value if value is not None else set()
        
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
                    

    @property
    def pcm_av_pc_repository_av_pc_ImplementationComponentType(self):
        return self.__pcm_av_pc_repository_av_pc_ImplementationComponentType

    @pcm_av_pc_repository_av_pc_ImplementationComponentType.setter
    def pcm_av_pc_repository_av_pc_ImplementationComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_ImplementationComponentType__pcm_av_pc_repository_av_pc_ImplementationComponentType", None)
        self.__pcm_av_pc_repository_av_pc_ImplementationComponentType = value if value is not None else set()
        
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
                    

    def ProvidedInterfaceHaveToConformToComponentType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ProvidedInterfaceHaveToConformToComponentType method
        pass

    def providedInterfacesHaveToConformToCompleteType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement providedInterfacesHaveToConformToCompleteType method
        pass

    def RequiredInterfacesHaveToConformToCompleteType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement RequiredInterfacesHaveToConformToCompleteType method
        pass

class pcm_av_pc_repository_av_pc_ProvidesComponentType(RepositoryComponent):

    def __init__(self, RepositoryComponent: "pcm_av_pc_composition_av_pc_AssemblyContext", repository_av_pc304: "pcm_av_pc_repository_av_pc_Repository"):
        
    def AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType method
        pass

class OperationProvidedRole:

    pass
class OperationRequiredRole:

    pass
class composition_av_pc_EventChannelSourceConnector:

    pass
class EventGroup:

    pass
class pcm_av_pc_composition_av_pc_ResourceRequiredDelegationConnector:

    pass
class DelegationConnector:

    pass
class pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector(DelegationConnector):

    pass
class pcm_av_pc_composition_av_pc_RequiredDelegationConnector(DelegationConnector):

    def __init__(self, pcm_av_pc_composition_av_pc_RequiredDelegationConnector: "OperationRequiredRole" = None, pcm_av_pc_composition_av_pc_RequiredDelegationConnector112: "OperationRequiredRole" = None, pcm_av_pc_composition_av_pc_RequiredDelegationConnector115: "composition_av_pc_AssemblyContext" = None):
        self.pcm_av_pc_composition_av_pc_RequiredDelegationConnector = pcm_av_pc_composition_av_pc_RequiredDelegationConnector
        self.pcm_av_pc_composition_av_pc_RequiredDelegationConnector112 = pcm_av_pc_composition_av_pc_RequiredDelegationConnector112
        self.pcm_av_pc_composition_av_pc_RequiredDelegationConnector115 = pcm_av_pc_composition_av_pc_RequiredDelegationConnector115
        
    @property
    def pcm_av_pc_composition_av_pc_RequiredDelegationConnector115(self):
        return self.__pcm_av_pc_composition_av_pc_RequiredDelegationConnector115

    @pcm_av_pc_composition_av_pc_RequiredDelegationConnector115.setter
    def pcm_av_pc_composition_av_pc_RequiredDelegationConnector115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_composition_av_pc_RequiredDelegationConnector__pcm_av_pc_composition_av_pc_RequiredDelegationConnector115", None)
        self.__pcm_av_pc_composition_av_pc_RequiredDelegationConnector115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_pc_AssemblyContext116"):
                opp_val = getattr(old_value, "composition_av_pc_AssemblyContext116", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_pc_AssemblyContext116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_pc_AssemblyContext116"):
                opp_val = getattr(value, "composition_av_pc_AssemblyContext116", None)
                setattr(value, "composition_av_pc_AssemblyContext116", self)

    @property
    def pcm_av_pc_composition_av_pc_RequiredDelegationConnector112(self):
        return self.__pcm_av_pc_composition_av_pc_RequiredDelegationConnector112

    @pcm_av_pc_composition_av_pc_RequiredDelegationConnector112.setter
    def pcm_av_pc_composition_av_pc_RequiredDelegationConnector112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_composition_av_pc_RequiredDelegationConnector__pcm_av_pc_composition_av_pc_RequiredDelegationConnector112", None)
        self.__pcm_av_pc_composition_av_pc_RequiredDelegationConnector112 = value
        
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

    @property
    def pcm_av_pc_composition_av_pc_RequiredDelegationConnector(self):
        return self.__pcm_av_pc_composition_av_pc_RequiredDelegationConnector

    @pcm_av_pc_composition_av_pc_RequiredDelegationConnector.setter
    def pcm_av_pc_composition_av_pc_RequiredDelegationConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_composition_av_pc_RequiredDelegationConnector__pcm_av_pc_composition_av_pc_RequiredDelegationConnector", None)
        self.__pcm_av_pc_composition_av_pc_RequiredDelegationConnector = value
        
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

    def RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

    def ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame method
        pass

class pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector(DelegationConnector):

    pass
class pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector(DelegationConnector):

    pass
class pcm_av_pc_composition_av_pc_SinkDelegationConnector(DelegationConnector):

    pass
class pcm_av_pc_composition_av_pc_SourceDelegationConnector(DelegationConnector):

    pass
class pcm_av_pc_composition_av_pc_ProvidedDelegationConnector(DelegationConnector):

    def __init__(self, pcm_av_pc_composition_av_pc_ProvidedDelegationConnector: "OperationProvidedRole" = None, pcm_av_pc_composition_av_pc_ProvidedDelegationConnector105: "OperationProvidedRole" = None, pcm_av_pc_composition_av_pc_ProvidedDelegationConnector108: "composition_av_pc_AssemblyContext" = None):
        self.pcm_av_pc_composition_av_pc_ProvidedDelegationConnector = pcm_av_pc_composition_av_pc_ProvidedDelegationConnector
        self.pcm_av_pc_composition_av_pc_ProvidedDelegationConnector105 = pcm_av_pc_composition_av_pc_ProvidedDelegationConnector105
        self.pcm_av_pc_composition_av_pc_ProvidedDelegationConnector108 = pcm_av_pc_composition_av_pc_ProvidedDelegationConnector108
        
    @property
    def pcm_av_pc_composition_av_pc_ProvidedDelegationConnector105(self):
        return self.__pcm_av_pc_composition_av_pc_ProvidedDelegationConnector105

    @pcm_av_pc_composition_av_pc_ProvidedDelegationConnector105.setter
    def pcm_av_pc_composition_av_pc_ProvidedDelegationConnector105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_composition_av_pc_ProvidedDelegationConnector__pcm_av_pc_composition_av_pc_ProvidedDelegationConnector105", None)
        self.__pcm_av_pc_composition_av_pc_ProvidedDelegationConnector105 = value
        
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
    def pcm_av_pc_composition_av_pc_ProvidedDelegationConnector(self):
        return self.__pcm_av_pc_composition_av_pc_ProvidedDelegationConnector

    @pcm_av_pc_composition_av_pc_ProvidedDelegationConnector.setter
    def pcm_av_pc_composition_av_pc_ProvidedDelegationConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_composition_av_pc_ProvidedDelegationConnector__pcm_av_pc_composition_av_pc_ProvidedDelegationConnector", None)
        self.__pcm_av_pc_composition_av_pc_ProvidedDelegationConnector = value
        
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
    def pcm_av_pc_composition_av_pc_ProvidedDelegationConnector108(self):
        return self.__pcm_av_pc_composition_av_pc_ProvidedDelegationConnector108

    @pcm_av_pc_composition_av_pc_ProvidedDelegationConnector108.setter
    def pcm_av_pc_composition_av_pc_ProvidedDelegationConnector108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_composition_av_pc_ProvidedDelegationConnector__pcm_av_pc_composition_av_pc_ProvidedDelegationConnector108", None)
        self.__pcm_av_pc_composition_av_pc_ProvidedDelegationConnector108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_pc_AssemblyContext109"):
                opp_val = getattr(old_value, "composition_av_pc_AssemblyContext109", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_pc_AssemblyContext109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_pc_AssemblyContext109"):
                opp_val = getattr(value, "composition_av_pc_AssemblyContext109", None)
                setattr(value, "composition_av_pc_AssemblyContext109", self)

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
class SourceRole:

    pass
class Connector:

    pass
class pcm_av_pc_composition_av_pc_EventChannelSinkConnector(Connector):

    pass
class pcm_av_pc_composition_av_pc_EventChannelSourceConnector(Connector):

    pass
class pcm_av_pc_composition_av_pc_AssemblyConnector(Connector):

    def __init__(self, pcm_av_pc_composition_av_pc_AssemblyConnector126: "OperationRequiredRole" = None, pcm_av_pc_composition_av_pc_AssemblyConnector: "composition_av_pc_AssemblyContext" = None, pcm_av_pc_composition_av_pc_AssemblyConnector120: "composition_av_pc_AssemblyContext" = None, pcm_av_pc_composition_av_pc_AssemblyConnector123: "OperationProvidedRole" = None):
        self.pcm_av_pc_composition_av_pc_AssemblyConnector126 = pcm_av_pc_composition_av_pc_AssemblyConnector126
        self.pcm_av_pc_composition_av_pc_AssemblyConnector = pcm_av_pc_composition_av_pc_AssemblyConnector
        self.pcm_av_pc_composition_av_pc_AssemblyConnector120 = pcm_av_pc_composition_av_pc_AssemblyConnector120
        self.pcm_av_pc_composition_av_pc_AssemblyConnector123 = pcm_av_pc_composition_av_pc_AssemblyConnector123
        
    @property
    def pcm_av_pc_composition_av_pc_AssemblyConnector126(self):
        return self.__pcm_av_pc_composition_av_pc_AssemblyConnector126

    @pcm_av_pc_composition_av_pc_AssemblyConnector126.setter
    def pcm_av_pc_composition_av_pc_AssemblyConnector126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_composition_av_pc_AssemblyConnector__pcm_av_pc_composition_av_pc_AssemblyConnector126", None)
        self.__pcm_av_pc_composition_av_pc_AssemblyConnector126 = value
        
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

    @property
    def pcm_av_pc_composition_av_pc_AssemblyConnector120(self):
        return self.__pcm_av_pc_composition_av_pc_AssemblyConnector120

    @pcm_av_pc_composition_av_pc_AssemblyConnector120.setter
    def pcm_av_pc_composition_av_pc_AssemblyConnector120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_composition_av_pc_AssemblyConnector__pcm_av_pc_composition_av_pc_AssemblyConnector120", None)
        self.__pcm_av_pc_composition_av_pc_AssemblyConnector120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_pc_AssemblyContext121"):
                opp_val = getattr(old_value, "composition_av_pc_AssemblyContext121", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_pc_AssemblyContext121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_pc_AssemblyContext121"):
                opp_val = getattr(value, "composition_av_pc_AssemblyContext121", None)
                setattr(value, "composition_av_pc_AssemblyContext121", self)

    @property
    def pcm_av_pc_composition_av_pc_AssemblyConnector(self):
        return self.__pcm_av_pc_composition_av_pc_AssemblyConnector

    @pcm_av_pc_composition_av_pc_AssemblyConnector.setter
    def pcm_av_pc_composition_av_pc_AssemblyConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_composition_av_pc_AssemblyConnector__pcm_av_pc_composition_av_pc_AssemblyConnector", None)
        self.__pcm_av_pc_composition_av_pc_AssemblyConnector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_pc_AssemblyContext118"):
                opp_val = getattr(old_value, "composition_av_pc_AssemblyContext118", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_pc_AssemblyContext118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_pc_AssemblyContext118"):
                opp_val = getattr(value, "composition_av_pc_AssemblyContext118", None)
                setattr(value, "composition_av_pc_AssemblyContext118", self)

    @property
    def pcm_av_pc_composition_av_pc_AssemblyConnector123(self):
        return self.__pcm_av_pc_composition_av_pc_AssemblyConnector123

    @pcm_av_pc_composition_av_pc_AssemblyConnector123.setter
    def pcm_av_pc_composition_av_pc_AssemblyConnector123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_composition_av_pc_AssemblyConnector__pcm_av_pc_composition_av_pc_AssemblyConnector123", None)
        self.__pcm_av_pc_composition_av_pc_AssemblyConnector123 = value
        
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

    def AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch method
        pass

    def AssemblyConnectorsReferencedInterfacesMustMatch(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AssemblyConnectorsReferencedInterfacesMustMatch method
        pass

    def AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch method
        pass

class pcm_av_pc_composition_av_pc_AssemblyEventConnector(Connector):

    pass
class pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector(Connector):

    pass
class pcm_av_pc_composition_av_pc_DelegationConnector(Connector):

    pass
class entity_av_pc_NamedElement:

    pass
class Identifier:

    pass
class pcm_av_pc_seff_av_pc_ResourceDemandingSEFF(seff_av_pc_ResourceDemandingBehaviour, Identifier, seff_av_pc_ServiceEffectSpecification):

    pass
class pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification(Identifier):

    def __init__(self, MTTR: float, MTTF: float, requiredByContainer: bool, numberOfReplicas: int, pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification: "SchedulingPolicy" = None, pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification656: "ProcessingResourceType" = None, PCMRandomVariable659: "PCMRandomVariable" = None, ResourceContainer662: "ResourceContainer" = None):
        self.MTTR = MTTR
        self.MTTF = MTTF
        self.requiredByContainer = requiredByContainer
        self.numberOfReplicas = numberOfReplicas
        self.pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification = pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification
        self.pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification656 = pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification656
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
    def pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification656(self):
        return self.__pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification656

    @pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification656.setter
    def pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification656(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification__pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification656", None)
        self.__pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification656 = value
        
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
    def pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification(self):
        return self.__pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification

    @pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification.setter
    def pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification__pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification", None)
        self.__pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification = value
        
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
    def PCMRandomVariable659(self):
        return self.__PCMRandomVariable659

    @PCMRandomVariable659.setter
    def PCMRandomVariable659(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification__PCMRandomVariable659", None)
        self.__PCMRandomVariable659 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av_pc660"):
                opp_val = getattr(old_value, "core_av_pc660", None)
                if opp_val == self:
                    setattr(old_value, "core_av_pc660", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av_pc660"):
                opp_val = getattr(value, "core_av_pc660", None)
                setattr(value, "core_av_pc660", self)

    @property
    def ResourceContainer662(self):
        return self.__ResourceContainer662

    @ResourceContainer662.setter
    def ResourceContainer662(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification__ResourceContainer662", None)
        self.__ResourceContainer662 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_av_pc663"):
                opp_val = getattr(old_value, "resourceenvironment_av_pc663", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_av_pc663", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_av_pc663"):
                opp_val = getattr(value, "resourceenvironment_av_pc663", None)
                setattr(value, "resourceenvironment_av_pc663", self)

class pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour(Identifier):

    def __init__(self, AbstractLoopAction: "AbstractLoopAction" = None, AbstractBranchTransition: "AbstractBranchTransition" = None, AbstractAction482: set["AbstractAction"] = None):
        self.AbstractLoopAction = AbstractLoopAction
        self.AbstractBranchTransition = AbstractBranchTransition
        self.AbstractAction482 = AbstractAction482 if AbstractAction482 is not None else set()
        
    @property
    def AbstractAction482(self):
        return self.__AbstractAction482

    @AbstractAction482.setter
    def AbstractAction482(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour__AbstractAction482", None)
        self.__AbstractAction482 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_av_pc483"):
                    opp_val = getattr(item, "seff_av_pc483", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_av_pc483", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_av_pc483"):
                    opp_val = getattr(item, "seff_av_pc483", None)
                    
                    setattr(item, "seff_av_pc483", self)
                    

    @property
    def AbstractBranchTransition(self):
        return self.__AbstractBranchTransition

    @AbstractBranchTransition.setter
    def AbstractBranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour__AbstractBranchTransition", None)
        self.__AbstractBranchTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av_pc480"):
                opp_val = getattr(old_value, "seff_av_pc480", None)
                if opp_val == self:
                    setattr(old_value, "seff_av_pc480", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av_pc480"):
                opp_val = getattr(value, "seff_av_pc480", None)
                setattr(value, "seff_av_pc480", self)

    @property
    def AbstractLoopAction(self):
        return self.__AbstractLoopAction

    @AbstractLoopAction.setter
    def AbstractLoopAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour__AbstractLoopAction", None)
        self.__AbstractLoopAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av_pc478"):
                opp_val = getattr(old_value, "seff_av_pc478", None)
                if opp_val == self:
                    setattr(old_value, "seff_av_pc478", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av_pc478"):
                opp_val = getattr(value, "seff_av_pc478", None)
                setattr(value, "seff_av_pc478", self)

    def EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor method
        pass

    def ExactlyOneStopAction(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ExactlyOneStopAction method
        pass

    def ExactlyOneStartAction(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ExactlyOneStartAction method
        pass

class pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification(Identifier):

    def __init__(self, failureProbability: float, LinkingResource665: "LinkingResource" = None, pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification: "CommunicationLinkResourceType" = None, PCMRandomVariable670: "PCMRandomVariable" = None, PCMRandomVariable673: "PCMRandomVariable" = None):
        self.failureProbability = failureProbability
        self.LinkingResource665 = LinkingResource665
        self.pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification = pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification
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
        old_value = getattr(self, f"_pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification__PCMRandomVariable670", None)
        self.__PCMRandomVariable670 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av_pc671"):
                opp_val = getattr(old_value, "core_av_pc671", None)
                if opp_val == self:
                    setattr(old_value, "core_av_pc671", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av_pc671"):
                opp_val = getattr(value, "core_av_pc671", None)
                setattr(value, "core_av_pc671", self)

    @property
    def LinkingResource665(self):
        return self.__LinkingResource665

    @LinkingResource665.setter
    def LinkingResource665(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification__LinkingResource665", None)
        self.__LinkingResource665 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_av_pc666"):
                opp_val = getattr(old_value, "resourceenvironment_av_pc666", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_av_pc666", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_av_pc666"):
                opp_val = getattr(value, "resourceenvironment_av_pc666", None)
                setattr(value, "resourceenvironment_av_pc666", self)

    @property
    def pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification(self):
        return self.__pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification

    @pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification.setter
    def pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification__pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification", None)
        self.__pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification = value
        
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

    @property
    def PCMRandomVariable673(self):
        return self.__PCMRandomVariable673

    @PCMRandomVariable673.setter
    def PCMRandomVariable673(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification__PCMRandomVariable673", None)
        self.__PCMRandomVariable673 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av_pc674"):
                opp_val = getattr(old_value, "core_av_pc674", None)
                if opp_val == self:
                    setattr(old_value, "core_av_pc674", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av_pc674"):
                opp_val = getattr(value, "core_av_pc674", None)
                setattr(value, "core_av_pc674", self)

class pcm_av_pc_entity_av_pc_Entity(Identifier, entity_av_pc_NamedElement):

    pass
class pcm_av_pc_entity_av_pc_NamedElement:

    def __init__(self, entityName: str):
        self.entityName = entityName
        
    @property
    def entityName(self) -> str:
        return self.__entityName

    @entityName.setter
    def entityName(self, entityName: str):
        self.__entityName = entityName

class composition_av_pc_Connector:

    pass
class composition_av_pc_EventChannel:

    pass
class entity_av_pc_InterfaceProvidingRequiringEntity:

    pass
class composition_av_pc_ComposedStructure:

    pass
class pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity(composition_av_pc_ComposedStructure, entity_av_pc_InterfaceProvidingRequiringEntity):

    def __init__(self, core_av_pc77: "pcm_av_pc_composition_av_pc_ResourceRequiredDelegationConnector", core_av_pc58: "pcm_av_pc_composition_av_pc_Connector", core_av_pc193: "pcm_av_pc_composition_av_pc_AssemblyContext", core_av_pc87: "pcm_av_pc_composition_av_pc_EventChannel"):
        
    def ProvidedRolesMustBeBound(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ProvidedRolesMustBeBound method
        pass

class composition_av_pc_ResourceRequiredDelegationConnector:

    pass
class composition_av_pc_AssemblyContext:

    pass
class RequiredRole:

    pass
class pcm_av_pc_repository_av_pc_InfrastructureRequiredRole(RequiredRole):

    pass
class pcm_av_pc_repository_av_pc_OperationRequiredRole(RequiredRole):

    pass
class pcm_av_pc_repository_av_pc_SourceRole(RequiredRole):

    pass
class seff_performance_av_pc_InfrastructureCall:

    pass
class entity_av_pc_ResourceInterfaceRequiringEntity:

    pass
class entity_av_pc_Entity:

    pass
class pcm_av_pc_repository_av_pc_CollectionDataType(entity_av_pc_Entity, repository_av_pc_DataType):

    pass
class pcm_av_pc_repository_av_pc_CompositeDataType(entity_av_pc_Entity, repository_av_pc_DataType):

    pass
class pcm_av_pc_system_av_pc_System(entity_av_pc_ComposedProvidingRequiringEntity, entity_av_pc_Entity):

    def __init__(self, QoSAnnotations628: set["QoSAnnotations"] = None):
        self.QoSAnnotations628 = QoSAnnotations628 if QoSAnnotations628 is not None else set()
        
    @property
    def QoSAnnotations628(self):
        return self.__QoSAnnotations628

    @QoSAnnotations628.setter
    def QoSAnnotations628(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_system_av_pc_System__QoSAnnotations628", None)
        self.__QoSAnnotations628 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qosannotations_av_pc629"):
                    opp_val = getattr(item, "qosannotations_av_pc629", None)
                    
                    if opp_val == self:
                        setattr(item, "qosannotations_av_pc629", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qosannotations_av_pc629"):
                    opp_val = getattr(item, "qosannotations_av_pc629", None)
                    
                    setattr(item, "qosannotations_av_pc629", self)
                    

    def SystemMustHaveAtLeastOneProvidedRole(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SystemMustHaveAtLeastOneProvidedRole method
        pass

class pcm_av_pc_entity_av_pc_InterfaceRequiringEntity(entity_av_pc_ResourceInterfaceRequiringEntity, entity_av_pc_Entity):

    pass
class VariableCharacterisation:

    pass
class ProvidedRole:

    pass
class pcm_av_pc_repository_av_pc_SinkRole(ProvidedRole):

    pass
class pcm_av_pc_repository_av_pc_OperationProvidedRole(ProvidedRole):

    pass
class pcm_av_pc_repository_av_pc_InfrastructureProvidedRole(ProvidedRole):

    pass
class PassiveResource:

    pass
class Entity:

    pass
class pcm_av_pc_repository_av_pc_PassiveResource(Entity):

    pass
class pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour(Entity):

    def __init__(self, UsageScenario237: "UsageScenario" = None, BranchTransition: "BranchTransition" = None, Loop242: "Loop" = None, AbstractUserAction245: set["AbstractUserAction"] = None):
        self.UsageScenario237 = UsageScenario237
        self.BranchTransition = BranchTransition
        self.Loop242 = Loop242
        self.AbstractUserAction245 = AbstractUserAction245 if AbstractUserAction245 is not None else set()
        
    @property
    def AbstractUserAction245(self):
        return self.__AbstractUserAction245

    @AbstractUserAction245.setter
    def AbstractUserAction245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour__AbstractUserAction245", None)
        self.__AbstractUserAction245 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "usagemodel_av_pc246"):
                    opp_val = getattr(item, "usagemodel_av_pc246", None)
                    
                    if opp_val == self:
                        setattr(item, "usagemodel_av_pc246", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "usagemodel_av_pc246"):
                    opp_val = getattr(item, "usagemodel_av_pc246", None)
                    
                    setattr(item, "usagemodel_av_pc246", self)
                    

    @property
    def Loop242(self):
        return self.__Loop242

    @Loop242.setter
    def Loop242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour__Loop242", None)
        self.__Loop242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av_pc243"):
                opp_val = getattr(old_value, "usagemodel_av_pc243", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av_pc243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av_pc243"):
                opp_val = getattr(value, "usagemodel_av_pc243", None)
                setattr(value, "usagemodel_av_pc243", self)

    @property
    def BranchTransition(self):
        return self.__BranchTransition

    @BranchTransition.setter
    def BranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour__BranchTransition", None)
        self.__BranchTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av_pc240"):
                opp_val = getattr(old_value, "usagemodel_av_pc240", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av_pc240", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av_pc240"):
                opp_val = getattr(value, "usagemodel_av_pc240", None)
                setattr(value, "usagemodel_av_pc240", self)

    @property
    def UsageScenario237(self):
        return self.__UsageScenario237

    @UsageScenario237.setter
    def UsageScenario237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour__UsageScenario237", None)
        self.__UsageScenario237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av_pc238"):
                opp_val = getattr(old_value, "usagemodel_av_pc238", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av_pc238", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av_pc238"):
                opp_val = getattr(value, "usagemodel_av_pc238", None)
                setattr(value, "usagemodel_av_pc238", self)

    def Exactlyonestop(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement Exactlyonestop method
        pass

    def Exactlyonestart(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement Exactlyonestart method
        pass

    def EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor method
        pass

class pcm_av_pc_usagemodel_av_pc_UsageScenario(Entity):

    pass
class pcm_av_pc_repository_av_pc_Repository(Entity):

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
    def DataType310(self):
        return self.__DataType310

    @DataType310.setter
    def DataType310(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_Repository__DataType310", None)
        self.__DataType310 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_av_pc311"):
                    opp_val = getattr(item, "repository_av_pc311", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_av_pc311", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_av_pc311"):
                    opp_val = getattr(item, "repository_av_pc311", None)
                    
                    setattr(item, "repository_av_pc311", self)
                    

    @property
    def Interface(self):
        return self.__Interface

    @Interface.setter
    def Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_Repository__Interface", None)
        self.__Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_av_pc306"):
                    opp_val = getattr(item, "repository_av_pc306", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_av_pc306", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_av_pc306"):
                    opp_val = getattr(item, "repository_av_pc306", None)
                    
                    setattr(item, "repository_av_pc306", self)
                    

    @property
    def RepositoryComponent303(self):
        return self.__RepositoryComponent303

    @RepositoryComponent303.setter
    def RepositoryComponent303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_Repository__RepositoryComponent303", None)
        self.__RepositoryComponent303 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_av_pc304"):
                    opp_val = getattr(item, "repository_av_pc304", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_av_pc304", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_av_pc304"):
                    opp_val = getattr(item, "repository_av_pc304", None)
                    
                    setattr(item, "repository_av_pc304", self)
                    

    @property
    def FailureType(self):
        return self.__FailureType

    @FailureType.setter
    def FailureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_Repository__FailureType", None)
        self.__FailureType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reliability_av_pc308"):
                    opp_val = getattr(item, "reliability_av_pc308", None)
                    
                    if opp_val == self:
                        setattr(item, "reliability_av_pc308", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reliability_av_pc308"):
                    opp_val = getattr(item, "reliability_av_pc308", None)
                    
                    setattr(item, "reliability_av_pc308", self)
                    

class pcm_av_pc_repository_av_pc_Interface(Entity):

    def __init__(self, pcm_av_pc_repository_av_pc_Interface315: set["Protocol"] = None, RequiredCharacterisation: set["RequiredCharacterisation"] = None, Repository319: "Repository" = None, pcm_av_pc_repository_av_pc_Interface: set["Interface"] = None):
        self.pcm_av_pc_repository_av_pc_Interface315 = pcm_av_pc_repository_av_pc_Interface315 if pcm_av_pc_repository_av_pc_Interface315 is not None else set()
        self.RequiredCharacterisation = RequiredCharacterisation if RequiredCharacterisation is not None else set()
        self.Repository319 = Repository319
        self.pcm_av_pc_repository_av_pc_Interface = pcm_av_pc_repository_av_pc_Interface if pcm_av_pc_repository_av_pc_Interface is not None else set()
        
    @property
    def Repository319(self):
        return self.__Repository319

    @Repository319.setter
    def Repository319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_Interface__Repository319", None)
        self.__Repository319 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av_pc320"):
                opp_val = getattr(old_value, "repository_av_pc320", None)
                if opp_val == self:
                    setattr(old_value, "repository_av_pc320", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av_pc320"):
                opp_val = getattr(value, "repository_av_pc320", None)
                setattr(value, "repository_av_pc320", self)

    @property
    def RequiredCharacterisation(self):
        return self.__RequiredCharacterisation

    @RequiredCharacterisation.setter
    def RequiredCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_Interface__RequiredCharacterisation", None)
        self.__RequiredCharacterisation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_av_pc317"):
                    opp_val = getattr(item, "repository_av_pc317", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_av_pc317", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_av_pc317"):
                    opp_val = getattr(item, "repository_av_pc317", None)
                    
                    setattr(item, "repository_av_pc317", self)
                    

    @property
    def pcm_av_pc_repository_av_pc_Interface(self):
        return self.__pcm_av_pc_repository_av_pc_Interface

    @pcm_av_pc_repository_av_pc_Interface.setter
    def pcm_av_pc_repository_av_pc_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_Interface__pcm_av_pc_repository_av_pc_Interface", None)
        self.__pcm_av_pc_repository_av_pc_Interface = value if value is not None else set()
        
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
    def pcm_av_pc_repository_av_pc_Interface315(self):
        return self.__pcm_av_pc_repository_av_pc_Interface315

    @pcm_av_pc_repository_av_pc_Interface315.setter
    def pcm_av_pc_repository_av_pc_Interface315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_Interface__pcm_av_pc_repository_av_pc_Interface315", None)
        self.__pcm_av_pc_repository_av_pc_Interface315 = value if value is not None else set()
        
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
                    

    def NoProtocolTypeIDUsedTwice(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NoProtocolTypeIDUsedTwice method
        pass

class pcm_av_pc_seff_av_pc_AbstractAction(Entity):

    pass
class pcm_av_pc_seff_reliability_av_pc_FailureHandlingEntity(Entity):

    pass
class pcm_av_pc_seff_av_pc_AbstractBranchTransition(Entity):

    pass
class pcm_av_pc_resourcetype_av_pc_SchedulingPolicy(Entity):

    pass
class pcm_av_pc_composition_av_pc_ComposedStructure(Entity):

    def __init__(self, composition_av_pc60: set["composition_av_pc_AssemblyContext"] = None, composition_av_pc63: set["composition_av_pc_ResourceRequiredDelegationConnector"] = None, composition_av_pc66: set["composition_av_pc_EventChannel"] = None, composition_av_pc69: set["composition_av_pc_Connector"] = None):
        self.composition_av_pc60 = composition_av_pc60 if composition_av_pc60 is not None else set()
        self.composition_av_pc63 = composition_av_pc63 if composition_av_pc63 is not None else set()
        self.composition_av_pc66 = composition_av_pc66 if composition_av_pc66 is not None else set()
        self.composition_av_pc69 = composition_av_pc69 if composition_av_pc69 is not None else set()
        
    @property
    def composition_av_pc66(self):
        return self.__composition_av_pc66

    @composition_av_pc66.setter
    def composition_av_pc66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_composition_av_pc_ComposedStructure__composition_av_pc66", None)
        self.__composition_av_pc66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_av_pc67"):
                    opp_val = getattr(item, "core_av_pc67", None)
                    
                    if opp_val == self:
                        setattr(item, "core_av_pc67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_av_pc67"):
                    opp_val = getattr(item, "core_av_pc67", None)
                    
                    setattr(item, "core_av_pc67", self)
                    

    @property
    def composition_av_pc63(self):
        return self.__composition_av_pc63

    @composition_av_pc63.setter
    def composition_av_pc63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_composition_av_pc_ComposedStructure__composition_av_pc63", None)
        self.__composition_av_pc63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_av_pc64"):
                    opp_val = getattr(item, "core_av_pc64", None)
                    
                    if opp_val == self:
                        setattr(item, "core_av_pc64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_av_pc64"):
                    opp_val = getattr(item, "core_av_pc64", None)
                    
                    setattr(item, "core_av_pc64", self)
                    

    @property
    def composition_av_pc69(self):
        return self.__composition_av_pc69

    @composition_av_pc69.setter
    def composition_av_pc69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_composition_av_pc_ComposedStructure__composition_av_pc69", None)
        self.__composition_av_pc69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_av_pc70"):
                    opp_val = getattr(item, "core_av_pc70", None)
                    
                    if opp_val == self:
                        setattr(item, "core_av_pc70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_av_pc70"):
                    opp_val = getattr(item, "core_av_pc70", None)
                    
                    setattr(item, "core_av_pc70", self)
                    

    @property
    def composition_av_pc60(self):
        return self.__composition_av_pc60

    @composition_av_pc60.setter
    def composition_av_pc60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_composition_av_pc_ComposedStructure__composition_av_pc60", None)
        self.__composition_av_pc60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_av_pc61"):
                    opp_val = getattr(item, "core_av_pc61", None)
                    
                    if opp_val == self:
                        setattr(item, "core_av_pc61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_av_pc61"):
                    opp_val = getattr(item, "core_av_pc61", None)
                    
                    setattr(item, "core_av_pc61", self)
                    

    def MultipleConnectorsConstraint(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MultipleConnectorsConstraint method
        pass

    def MultipleConnectorsConstraintForAssemblyConnectors(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MultipleConnectorsConstraintForAssemblyConnectors method
        pass

class pcm_av_pc_composition_av_pc_AssemblyContext(Entity):

    pass
class pcm_av_pc_qosannotations_av_pc_QoSAnnotations(Entity):

    def __init__(self, SpecifiedOutputParameterAbstraction604: set["SpecifiedOutputParameterAbstraction"] = None, System: "System" = None, SpecifiedQoSAnnotation: set["SpecifiedQoSAnnotation"] = None):
        self.SpecifiedOutputParameterAbstraction604 = SpecifiedOutputParameterAbstraction604 if SpecifiedOutputParameterAbstraction604 is not None else set()
        self.System = System
        self.SpecifiedQoSAnnotation = SpecifiedQoSAnnotation if SpecifiedQoSAnnotation is not None else set()
        
    @property
    def SpecifiedOutputParameterAbstraction604(self):
        return self.__SpecifiedOutputParameterAbstraction604

    @SpecifiedOutputParameterAbstraction604.setter
    def SpecifiedOutputParameterAbstraction604(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_qosannotations_av_pc_QoSAnnotations__SpecifiedOutputParameterAbstraction604", None)
        self.__SpecifiedOutputParameterAbstraction604 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qosannotations_av_pc605"):
                    opp_val = getattr(item, "qosannotations_av_pc605", None)
                    
                    if opp_val == self:
                        setattr(item, "qosannotations_av_pc605", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qosannotations_av_pc605"):
                    opp_val = getattr(item, "qosannotations_av_pc605", None)
                    
                    setattr(item, "qosannotations_av_pc605", self)
                    

    @property
    def System(self):
        return self.__System

    @System.setter
    def System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_qosannotations_av_pc_QoSAnnotations__System", None)
        self.__System = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system_av_pc"):
                opp_val = getattr(old_value, "system_av_pc", None)
                if opp_val == self:
                    setattr(old_value, "system_av_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system_av_pc"):
                opp_val = getattr(value, "system_av_pc", None)
                setattr(value, "system_av_pc", self)

    @property
    def SpecifiedQoSAnnotation(self):
        return self.__SpecifiedQoSAnnotation

    @SpecifiedQoSAnnotation.setter
    def SpecifiedQoSAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_qosannotations_av_pc_QoSAnnotations__SpecifiedQoSAnnotation", None)
        self.__SpecifiedQoSAnnotation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qosannotations_av_pc608"):
                    opp_val = getattr(item, "qosannotations_av_pc608", None)
                    
                    if opp_val == self:
                        setattr(item, "qosannotations_av_pc608", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qosannotations_av_pc608"):
                    opp_val = getattr(item, "qosannotations_av_pc608", None)
                    
                    setattr(item, "qosannotations_av_pc608", self)
                    

    def MultipleReliabilityAnnotationsPerExternalCallNotAllowed(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MultipleReliabilityAnnotationsPerExternalCallNotAllowed method
        pass

class pcm_av_pc_resourceenvironment_av_pc_LinkingResource(Entity):

    pass
class pcm_av_pc_resourcetype_av_pc_ResourceSignature(Entity):

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
        old_value = getattr(self, f"_pcm_av_pc_resourcetype_av_pc_ResourceSignature__Parameter383", None)
        self.__Parameter383 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av_pc384"):
                opp_val = getattr(old_value, "repository_av_pc384", None)
                if opp_val == self:
                    setattr(old_value, "repository_av_pc384", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av_pc384"):
                opp_val = getattr(value, "repository_av_pc384", None)
                setattr(value, "repository_av_pc384", self)

    @property
    def ResourceInterface386(self):
        return self.__ResourceInterface386

    @ResourceInterface386.setter
    def ResourceInterface386(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_resourcetype_av_pc_ResourceSignature__ResourceInterface386", None)
        self.__ResourceInterface386 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcetype_av_pc387"):
                opp_val = getattr(old_value, "resourcetype_av_pc387", None)
                if opp_val == self:
                    setattr(old_value, "resourcetype_av_pc387", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcetype_av_pc387"):
                opp_val = getattr(value, "resourcetype_av_pc387", None)
                setattr(value, "resourcetype_av_pc387", self)

class pcm_av_pc_usagemodel_av_pc_AbstractUserAction(Entity):

    pass
class pcm_av_pc_reliability_av_pc_FailureType(Entity):

    pass
class pcm_av_pc_resourcetype_av_pc_ResourceInterface(Entity):

    pass
class pcm_av_pc_allocation_av_pc_AllocationContext(Entity):

    def __init__(self, pcm_av_pc_allocation_av_pc_AllocationContext: "ResourceContainer" = None, pcm_av_pc_allocation_av_pc_AllocationContext678: "composition_av_pc_AssemblyContext" = None, Allocation: "Allocation" = None, pcm_av_pc_allocation_av_pc_AllocationContext682: "composition_av_pc_EventChannel" = None):
        self.pcm_av_pc_allocation_av_pc_AllocationContext = pcm_av_pc_allocation_av_pc_AllocationContext
        self.pcm_av_pc_allocation_av_pc_AllocationContext678 = pcm_av_pc_allocation_av_pc_AllocationContext678
        self.Allocation = Allocation
        self.pcm_av_pc_allocation_av_pc_AllocationContext682 = pcm_av_pc_allocation_av_pc_AllocationContext682
        
    @property
    def pcm_av_pc_allocation_av_pc_AllocationContext678(self):
        return self.__pcm_av_pc_allocation_av_pc_AllocationContext678

    @pcm_av_pc_allocation_av_pc_AllocationContext678.setter
    def pcm_av_pc_allocation_av_pc_AllocationContext678(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_allocation_av_pc_AllocationContext__pcm_av_pc_allocation_av_pc_AllocationContext678", None)
        self.__pcm_av_pc_allocation_av_pc_AllocationContext678 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_pc_AssemblyContext679"):
                opp_val = getattr(old_value, "composition_av_pc_AssemblyContext679", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_pc_AssemblyContext679", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_pc_AssemblyContext679"):
                opp_val = getattr(value, "composition_av_pc_AssemblyContext679", None)
                setattr(value, "composition_av_pc_AssemblyContext679", self)

    @property
    def pcm_av_pc_allocation_av_pc_AllocationContext682(self):
        return self.__pcm_av_pc_allocation_av_pc_AllocationContext682

    @pcm_av_pc_allocation_av_pc_AllocationContext682.setter
    def pcm_av_pc_allocation_av_pc_AllocationContext682(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_allocation_av_pc_AllocationContext__pcm_av_pc_allocation_av_pc_AllocationContext682", None)
        self.__pcm_av_pc_allocation_av_pc_AllocationContext682 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_pc_EventChannel"):
                opp_val = getattr(old_value, "composition_av_pc_EventChannel", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_pc_EventChannel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_pc_EventChannel"):
                opp_val = getattr(value, "composition_av_pc_EventChannel", None)
                setattr(value, "composition_av_pc_EventChannel", self)

    @property
    def pcm_av_pc_allocation_av_pc_AllocationContext(self):
        return self.__pcm_av_pc_allocation_av_pc_AllocationContext

    @pcm_av_pc_allocation_av_pc_AllocationContext.setter
    def pcm_av_pc_allocation_av_pc_AllocationContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_allocation_av_pc_AllocationContext__pcm_av_pc_allocation_av_pc_AllocationContext", None)
        self.__pcm_av_pc_allocation_av_pc_AllocationContext = value
        
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
    def Allocation(self):
        return self.__Allocation

    @Allocation.setter
    def Allocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_allocation_av_pc_AllocationContext__Allocation", None)
        self.__Allocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "allocation_av_pc"):
                opp_val = getattr(old_value, "allocation_av_pc", None)
                if opp_val == self:
                    setattr(old_value, "allocation_av_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "allocation_av_pc"):
                opp_val = getattr(value, "allocation_av_pc", None)
                setattr(value, "allocation_av_pc", self)

    def OneAssemblyContextOrOneEventChannelShouldBeReferred(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement OneAssemblyContextOrOneEventChannelShouldBeReferred method
        pass

class pcm_av_pc_allocation_av_pc_Allocation(Entity):

    def __init__(self, pcm_av_pc_allocation_av_pc_Allocation: "ResourceEnvironment" = None, pcm_av_pc_allocation_av_pc_Allocation686: "System" = None, AllocationContext: set["AllocationContext"] = None):
        self.pcm_av_pc_allocation_av_pc_Allocation = pcm_av_pc_allocation_av_pc_Allocation
        self.pcm_av_pc_allocation_av_pc_Allocation686 = pcm_av_pc_allocation_av_pc_Allocation686
        self.AllocationContext = AllocationContext if AllocationContext is not None else set()
        
    @property
    def pcm_av_pc_allocation_av_pc_Allocation(self):
        return self.__pcm_av_pc_allocation_av_pc_Allocation

    @pcm_av_pc_allocation_av_pc_Allocation.setter
    def pcm_av_pc_allocation_av_pc_Allocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_allocation_av_pc_Allocation__pcm_av_pc_allocation_av_pc_Allocation", None)
        self.__pcm_av_pc_allocation_av_pc_Allocation = value
        
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

    @property
    def pcm_av_pc_allocation_av_pc_Allocation686(self):
        return self.__pcm_av_pc_allocation_av_pc_Allocation686

    @pcm_av_pc_allocation_av_pc_Allocation686.setter
    def pcm_av_pc_allocation_av_pc_Allocation686(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_allocation_av_pc_Allocation__pcm_av_pc_allocation_av_pc_Allocation686", None)
        self.__pcm_av_pc_allocation_av_pc_Allocation686 = value
        
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
        old_value = getattr(self, f"_pcm_av_pc_allocation_av_pc_Allocation__AllocationContext", None)
        self.__AllocationContext = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "allocation_av_pc689"):
                    opp_val = getattr(item, "allocation_av_pc689", None)
                    
                    if opp_val == self:
                        setattr(item, "allocation_av_pc689", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "allocation_av_pc689"):
                    opp_val = getattr(item, "allocation_av_pc689", None)
                    
                    setattr(item, "allocation_av_pc689", self)
                    

    def EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce method
        pass

    def CommunicatingServersHaveToBeConnectedByLinkingResource(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement CommunicatingServersHaveToBeConnectedByLinkingResource method
        pass

class pcm_av_pc_composition_av_pc_EventChannel(Entity):

    pass
class pcm_av_pc_repository_av_pc_Signature(Entity):

    pass
class pcm_av_pc_composition_av_pc_Connector(Entity):

    pass
class pcm_av_pc_resourceenvironment_av_pc_ResourceContainer(Entity):

    pass
class pcm_av_pc_repository_av_pc_Role(Entity):

    pass
class pcm_av_pc_entity_av_pc_InterfaceProvidingEntity(Entity):

    pass
class ClosedWorkload:

    pass
class entity_av_pc_InterfaceRequiringEntity:

    pass
class entity_av_pc_InterfaceProvidingEntity:

    pass
class pcm_av_pc_entity_av_pc_InterfaceProvidingRequiringEntity(entity_av_pc_InterfaceProvidingEntity, entity_av_pc_InterfaceRequiringEntity):

    pass
class ResourceInterface:

    pass
class entity_av_pc_ResourceInterfaceProvidingEntity:

    pass
class pcm_av_pc_resourcetype_av_pc_ResourceType(entity_av_pc_Entity, entity_av_pc_ResourceInterfaceProvidingEntity, UnitCarryingElement):

    pass
class pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingRequiringEntity(entity_av_pc_ResourceInterfaceRequiringEntity, entity_av_pc_ResourceInterfaceProvidingEntity):

    pass
class Role:

    pass
class pcm_av_pc_repository_av_pc_ProvidedRole(Role):

    pass
class pcm_av_pc_repository_av_pc_RequiredRole(Role):

    pass
class pcm_av_pc_entity_av_pc_ResourceProvidedRole(Role):

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
class composition_av_pc_AssemblyEventConnector:

    pass
class composition_av_pc_EventChannelSinkConnector:

    pass
class entity_av_pc_ResourceProvidedRole:

    pass
class qos_performance_av_pc_SpecifiedExecutionTime:

    pass
class pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingEntity(Entity):

    pass
class GuardedBranchTransition:

    pass
class LoopAction:

    pass
class seff_performance_av_pc_ParametricResourceDemand:

    pass
class pcm_av_pc_entity_av_pc_ResourceRequiredRole(Role):

    pass
class entity_av_pc_ResourceRequiredRole:

    pass
class seff_performance_av_pc_ResourceCall:

    pass
class pcm_av_pc_entity_av_pc_ResourceInterfaceRequiringEntity(Entity):

    pass
class RandomVariable:

    pass
class pcm_av_pc_core_av_pc_PCMRandomVariable(RandomVariable):

    def __init__(self, seff_performance_av_pc12: "seff_performance_av_pc_ResourceCall" = None, seff_performance_av_pc15: "seff_performance_av_pc_ParametricResourceDemand" = None, LoopAction: "LoopAction" = None, GuardedBranchTransition: "GuardedBranchTransition" = None, qos_performance_av_pc: "qos_performance_av_pc_SpecifiedExecutionTime" = None, composition_av_pc: "composition_av_pc_EventChannelSinkConnector" = None, composition_av_pc24: "composition_av_pc_AssemblyEventConnector" = None, Loop: "Loop" = None, OpenWorkload: "OpenWorkload" = None, Delay: "Delay" = None, CommunicationLinkResourceSpecification: "CommunicationLinkResourceSpecification" = None, ProcessingResourceSpecification: "ProcessingResourceSpecification" = None, CommunicationLinkResourceSpecification36: "CommunicationLinkResourceSpecification" = None, ClosedWorkload: "ClosedWorkload" = None, PassiveResource: "PassiveResource" = None, VariableCharacterisation: "VariableCharacterisation" = None, seff_performance_av_pc: "seff_performance_av_pc_InfrastructureCall" = None):
        self.seff_performance_av_pc12 = seff_performance_av_pc12
        self.seff_performance_av_pc15 = seff_performance_av_pc15
        self.LoopAction = LoopAction
        self.GuardedBranchTransition = GuardedBranchTransition
        self.qos_performance_av_pc = qos_performance_av_pc
        self.composition_av_pc = composition_av_pc
        self.composition_av_pc24 = composition_av_pc24
        self.Loop = Loop
        self.OpenWorkload = OpenWorkload
        self.Delay = Delay
        self.CommunicationLinkResourceSpecification = CommunicationLinkResourceSpecification
        self.ProcessingResourceSpecification = ProcessingResourceSpecification
        self.CommunicationLinkResourceSpecification36 = CommunicationLinkResourceSpecification36
        self.ClosedWorkload = ClosedWorkload
        self.PassiveResource = PassiveResource
        self.VariableCharacterisation = VariableCharacterisation
        self.seff_performance_av_pc = seff_performance_av_pc
        
    @property
    def composition_av_pc24(self):
        return self.__composition_av_pc24

    @composition_av_pc24.setter
    def composition_av_pc24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__composition_av_pc24", None)
        self.__composition_av_pc24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av_pc25"):
                opp_val = getattr(old_value, "core_av_pc25", None)
                if opp_val == self:
                    setattr(old_value, "core_av_pc25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av_pc25"):
                opp_val = getattr(value, "core_av_pc25", None)
                setattr(value, "core_av_pc25", self)

    @property
    def LoopAction(self):
        return self.__LoopAction

    @LoopAction.setter
    def LoopAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__LoopAction", None)
        self.__LoopAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av_pc18"):
                opp_val = getattr(old_value, "seff_av_pc18", None)
                if opp_val == self:
                    setattr(old_value, "seff_av_pc18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av_pc18"):
                opp_val = getattr(value, "seff_av_pc18", None)
                setattr(value, "seff_av_pc18", self)

    @property
    def PassiveResource(self):
        return self.__PassiveResource

    @PassiveResource.setter
    def PassiveResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__PassiveResource", None)
        self.__PassiveResource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_av_pc"):
                opp_val = getattr(old_value, "repository_av_pc", None)
                if opp_val == self:
                    setattr(old_value, "repository_av_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_av_pc"):
                opp_val = getattr(value, "repository_av_pc", None)
                setattr(value, "repository_av_pc", self)

    @property
    def seff_performance_av_pc(self):
        return self.__seff_performance_av_pc

    @seff_performance_av_pc.setter
    def seff_performance_av_pc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__seff_performance_av_pc", None)
        self.__seff_performance_av_pc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av_pc"):
                opp_val = getattr(old_value, "seff_av_pc", None)
                if opp_val == self:
                    setattr(old_value, "seff_av_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av_pc"):
                opp_val = getattr(value, "seff_av_pc", None)
                setattr(value, "seff_av_pc", self)

    @property
    def CommunicationLinkResourceSpecification36(self):
        return self.__CommunicationLinkResourceSpecification36

    @CommunicationLinkResourceSpecification36.setter
    def CommunicationLinkResourceSpecification36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__CommunicationLinkResourceSpecification36", None)
        self.__CommunicationLinkResourceSpecification36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_av_pc37"):
                opp_val = getattr(old_value, "resourceenvironment_av_pc37", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_av_pc37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_av_pc37"):
                opp_val = getattr(value, "resourceenvironment_av_pc37", None)
                setattr(value, "resourceenvironment_av_pc37", self)

    @property
    def GuardedBranchTransition(self):
        return self.__GuardedBranchTransition

    @GuardedBranchTransition.setter
    def GuardedBranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__GuardedBranchTransition", None)
        self.__GuardedBranchTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av_pc20"):
                opp_val = getattr(old_value, "seff_av_pc20", None)
                if opp_val == self:
                    setattr(old_value, "seff_av_pc20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av_pc20"):
                opp_val = getattr(value, "seff_av_pc20", None)
                setattr(value, "seff_av_pc20", self)

    @property
    def seff_performance_av_pc12(self):
        return self.__seff_performance_av_pc12

    @seff_performance_av_pc12.setter
    def seff_performance_av_pc12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__seff_performance_av_pc12", None)
        self.__seff_performance_av_pc12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av_pc13"):
                opp_val = getattr(old_value, "seff_av_pc13", None)
                if opp_val == self:
                    setattr(old_value, "seff_av_pc13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av_pc13"):
                opp_val = getattr(value, "seff_av_pc13", None)
                setattr(value, "seff_av_pc13", self)

    @property
    def CommunicationLinkResourceSpecification(self):
        return self.__CommunicationLinkResourceSpecification

    @CommunicationLinkResourceSpecification.setter
    def CommunicationLinkResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__CommunicationLinkResourceSpecification", None)
        self.__CommunicationLinkResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_av_pc"):
                opp_val = getattr(old_value, "resourceenvironment_av_pc", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_av_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_av_pc"):
                opp_val = getattr(value, "resourceenvironment_av_pc", None)
                setattr(value, "resourceenvironment_av_pc", self)

    @property
    def qos_performance_av_pc(self):
        return self.__qos_performance_av_pc

    @qos_performance_av_pc.setter
    def qos_performance_av_pc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__qos_performance_av_pc", None)
        self.__qos_performance_av_pc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qosannotations_av_pc"):
                opp_val = getattr(old_value, "qosannotations_av_pc", None)
                if opp_val == self:
                    setattr(old_value, "qosannotations_av_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qosannotations_av_pc"):
                opp_val = getattr(value, "qosannotations_av_pc", None)
                setattr(value, "qosannotations_av_pc", self)

    @property
    def composition_av_pc(self):
        return self.__composition_av_pc

    @composition_av_pc.setter
    def composition_av_pc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__composition_av_pc", None)
        self.__composition_av_pc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_av_pc"):
                opp_val = getattr(old_value, "core_av_pc", None)
                if opp_val == self:
                    setattr(old_value, "core_av_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_av_pc"):
                opp_val = getattr(value, "core_av_pc", None)
                setattr(value, "core_av_pc", self)

    @property
    def Loop(self):
        return self.__Loop

    @Loop.setter
    def Loop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__Loop", None)
        self.__Loop = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av_pc27"):
                opp_val = getattr(old_value, "usagemodel_av_pc27", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av_pc27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av_pc27"):
                opp_val = getattr(value, "usagemodel_av_pc27", None)
                setattr(value, "usagemodel_av_pc27", self)

    @property
    def Delay(self):
        return self.__Delay

    @Delay.setter
    def Delay(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__Delay", None)
        self.__Delay = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av_pc31"):
                opp_val = getattr(old_value, "usagemodel_av_pc31", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av_pc31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av_pc31"):
                opp_val = getattr(value, "usagemodel_av_pc31", None)
                setattr(value, "usagemodel_av_pc31", self)

    @property
    def OpenWorkload(self):
        return self.__OpenWorkload

    @OpenWorkload.setter
    def OpenWorkload(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__OpenWorkload", None)
        self.__OpenWorkload = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av_pc29"):
                opp_val = getattr(old_value, "usagemodel_av_pc29", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av_pc29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av_pc29"):
                opp_val = getattr(value, "usagemodel_av_pc29", None)
                setattr(value, "usagemodel_av_pc29", self)

    @property
    def ClosedWorkload(self):
        return self.__ClosedWorkload

    @ClosedWorkload.setter
    def ClosedWorkload(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__ClosedWorkload", None)
        self.__ClosedWorkload = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_av_pc"):
                opp_val = getattr(old_value, "usagemodel_av_pc", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_av_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_av_pc"):
                opp_val = getattr(value, "usagemodel_av_pc", None)
                setattr(value, "usagemodel_av_pc", self)

    @property
    def VariableCharacterisation(self):
        return self.__VariableCharacterisation

    @VariableCharacterisation.setter
    def VariableCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__VariableCharacterisation", None)
        self.__VariableCharacterisation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameter_av_pc"):
                opp_val = getattr(old_value, "parameter_av_pc", None)
                if opp_val == self:
                    setattr(old_value, "parameter_av_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameter_av_pc"):
                opp_val = getattr(value, "parameter_av_pc", None)
                setattr(value, "parameter_av_pc", self)

    @property
    def seff_performance_av_pc15(self):
        return self.__seff_performance_av_pc15

    @seff_performance_av_pc15.setter
    def seff_performance_av_pc15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__seff_performance_av_pc15", None)
        self.__seff_performance_av_pc15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_av_pc16"):
                opp_val = getattr(old_value, "seff_av_pc16", None)
                if opp_val == self:
                    setattr(old_value, "seff_av_pc16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_av_pc16"):
                opp_val = getattr(value, "seff_av_pc16", None)
                setattr(value, "seff_av_pc16", self)

    @property
    def ProcessingResourceSpecification(self):
        return self.__ProcessingResourceSpecification

    @ProcessingResourceSpecification.setter
    def ProcessingResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__ProcessingResourceSpecification", None)
        self.__ProcessingResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_av_pc34"):
                opp_val = getattr(old_value, "resourceenvironment_av_pc34", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_av_pc34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_av_pc34"):
                opp_val = getattr(value, "resourceenvironment_av_pc34", None)
                setattr(value, "resourceenvironment_av_pc34", self)

    def SpecificationMustNotBeNULL(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SpecificationMustNotBeNULL method
        pass

class pcm_av_pc_Pointcut:

    pass
class pcm_av_pc_PerJoinPointScope:

    pass
class pcm_av_pc_GlobalScope:

    pass
class pcm_av_pc_EObject:

    pass
class pcm_av_pc_Advice:

    pass
class pcm_av_pc_DummyClass:

    pass