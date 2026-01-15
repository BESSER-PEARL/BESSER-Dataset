from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class VariableCharacterisationType(Enum):
    BYTESIZE = "BYTESIZE"
    TYPE = "TYPE"
    STRUCTURE = "STRUCTURE"
    NUMBER_OF_ELEMENTS = "NUMBER_OF_ELEMENTS"
    VALUE = "VALUE"
class ComponentType(Enum):
    BUSINESS_COMPONENT = "BUSINESS_COMPONENT"
    INFRASTRUCTURE_COMPONENT = "INFRASTRUCTURE_COMPONENT"
class PrimitiveTypeEnum(Enum):
    INT = "INT"
    STRING = "STRING"
    BOOL = "BOOL"
    DOUBLE = "DOUBLE"
    CHAR = "CHAR"
    BYTE = "BYTE"
    LONG = "LONG"
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
class pcm_pc_completions_pc_NetworkDemandParametricResourceDemand(ParametricResourceDemand):

    pass
class ExternalCallAction:

    pass
class pcm_pc_completions_pc_DelegatingExternalCallAction(ExternalCallAction):

    pass
class Completion:

    pass
class pcm_pc_completions_pc_CompletionRepository:

    pass
class Allocation:

    pass
class repository_pc_RepositoryComponent:

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
class pcm_pc_qosannotations_pc_SpecifiedOutputParameterAbstraction:

    pass
class SpecifiedQoSAnnotation:

    pass
class pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation(SpecifiedQoSAnnotation):

    def __init__(self, ExternalFailureOccurrenceDescription: set["ExternalFailureOccurrenceDescription"] = None, qosannotations_pc602: "pcm_pc_qosannotations_pc_QoSAnnotations"):
        self.ExternalFailureOccurrenceDescription = ExternalFailureOccurrenceDescription if ExternalFailureOccurrenceDescription is not None else set()
        
    @property
    def ExternalFailureOccurrenceDescription(self):
        return self.__ExternalFailureOccurrenceDescription

    @ExternalFailureOccurrenceDescription.setter
    def ExternalFailureOccurrenceDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription", None)
        self.__ExternalFailureOccurrenceDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reliability_pc620"):
                    opp_val = getattr(item, "reliability_pc620", None)
                    
                    if opp_val == self:
                        setattr(item, "reliability_pc620", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reliability_pc620"):
                    opp_val = getattr(item, "reliability_pc620", None)
                    
                    setattr(item, "reliability_pc620", self)
                    

    def MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed method
        pass

    def SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1 method
        pass

    def SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem method
        pass

class System:

    pass
class pcm_pc_qos_performance_pc_SpecifiedExecutionTime(SpecifiedQoSAnnotation):

    pass
class SpecifiedExecutionTime:

    pass
class pcm_pc_qos_performance_pc_ComponentSpecifiedExecutionTime(SpecifiedExecutionTime):

    pass
class pcm_pc_qos_performance_pc_SystemSpecifiedExecutionTime(SpecifiedExecutionTime):

    def __init__(self):
        
    def SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem method
        pass

class seff_reliability_pc_RecoveryAction:

    pass
class QoSAnnotations:

    pass
class pcm_pc_qosannotations_pc_SpecifiedQoSAnnotation:

    pass
class seff_reliability_pc_RecoveryActionBehaviour:

    pass
class pcm_pc_seff_performance_pc_ParametricResourceDemand:

    def __init__(self, PCMRandomVariable574: "PCMRandomVariable" = None, pcm_pc_seff_performance_pc_ParametricResourceDemand: "ProcessingResourceType" = None, AbstractInternalControlFlowAction579: "AbstractInternalControlFlowAction" = None):
        self.PCMRandomVariable574 = PCMRandomVariable574
        self.pcm_pc_seff_performance_pc_ParametricResourceDemand = pcm_pc_seff_performance_pc_ParametricResourceDemand
        self.AbstractInternalControlFlowAction579 = AbstractInternalControlFlowAction579
        
    @property
    def pcm_pc_seff_performance_pc_ParametricResourceDemand(self):
        return self.__pcm_pc_seff_performance_pc_ParametricResourceDemand

    @pcm_pc_seff_performance_pc_ParametricResourceDemand.setter
    def pcm_pc_seff_performance_pc_ParametricResourceDemand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_seff_performance_pc_ParametricResourceDemand__pcm_pc_seff_performance_pc_ParametricResourceDemand", None)
        self.__pcm_pc_seff_performance_pc_ParametricResourceDemand = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcessingResourceType577"):
                opp_val = getattr(old_value, "ProcessingResourceType577", None)
                if opp_val == self:
                    setattr(old_value, "ProcessingResourceType577", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessingResourceType577"):
                opp_val = getattr(value, "ProcessingResourceType577", None)
                setattr(value, "ProcessingResourceType577", self)

    @property
    def AbstractInternalControlFlowAction579(self):
        return self.__AbstractInternalControlFlowAction579

    @AbstractInternalControlFlowAction579.setter
    def AbstractInternalControlFlowAction579(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_seff_performance_pc_ParametricResourceDemand__AbstractInternalControlFlowAction579", None)
        self.__AbstractInternalControlFlowAction579 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc580"):
                opp_val = getattr(old_value, "seff_pc580", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc580", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc580"):
                opp_val = getattr(value, "seff_pc580", None)
                setattr(value, "seff_pc580", self)

    @property
    def PCMRandomVariable574(self):
        return self.__PCMRandomVariable574

    @PCMRandomVariable574.setter
    def PCMRandomVariable574(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_seff_performance_pc_ParametricResourceDemand__PCMRandomVariable574", None)
        self.__PCMRandomVariable574 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc575"):
                opp_val = getattr(old_value, "core_pc575", None)
                if opp_val == self:
                    setattr(old_value, "core_pc575", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc575"):
                opp_val = getattr(value, "core_pc575", None)
                setattr(value, "core_pc575", self)

    def DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

class seff_pc_AbstractInternalControlFlowAction:

    pass
class seff_pc_CallAction:

    pass
class pcm_pc_seff_pc_InternalCallAction(seff_pc_CallAction, seff_pc_AbstractInternalControlFlowAction):

    pass
class seff_reliability_pc_FailureHandlingEntity:

    pass
class seff_pc_CallReturnAction:

    pass
class seff_pc_AbstractAction:

    pass
class pcm_pc_seff_pc_EmitEventAction(seff_pc_AbstractAction, seff_pc_CallAction):

    pass
class pcm_pc_seff_pc_ExternalCallAction(seff_pc_AbstractAction, seff_reliability_pc_FailureHandlingEntity, seff_pc_CallReturnAction):

    def __init__(self, retryCount: int, pcm_pc_seff_pc_ExternalCallAction: "OperationSignature" = None, pcm_pc_seff_pc_ExternalCallAction527: "OperationRequiredRole" = None):
        self.retryCount = retryCount
        self.pcm_pc_seff_pc_ExternalCallAction = pcm_pc_seff_pc_ExternalCallAction
        self.pcm_pc_seff_pc_ExternalCallAction527 = pcm_pc_seff_pc_ExternalCallAction527
        
    @property
    def retryCount(self) -> int:
        return self.__retryCount

    @retryCount.setter
    def retryCount(self, retryCount: int):
        self.__retryCount = retryCount

    @property
    def pcm_pc_seff_pc_ExternalCallAction527(self):
        return self.__pcm_pc_seff_pc_ExternalCallAction527

    @pcm_pc_seff_pc_ExternalCallAction527.setter
    def pcm_pc_seff_pc_ExternalCallAction527(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_seff_pc_ExternalCallAction__pcm_pc_seff_pc_ExternalCallAction527", None)
        self.__pcm_pc_seff_pc_ExternalCallAction527 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationRequiredRole528"):
                opp_val = getattr(old_value, "OperationRequiredRole528", None)
                if opp_val == self:
                    setattr(old_value, "OperationRequiredRole528", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationRequiredRole528"):
                opp_val = getattr(value, "OperationRequiredRole528", None)
                setattr(value, "OperationRequiredRole528", self)

    @property
    def pcm_pc_seff_pc_ExternalCallAction(self):
        return self.__pcm_pc_seff_pc_ExternalCallAction

    @pcm_pc_seff_pc_ExternalCallAction.setter
    def pcm_pc_seff_pc_ExternalCallAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_seff_pc_ExternalCallAction__pcm_pc_seff_pc_ExternalCallAction", None)
        self.__pcm_pc_seff_pc_ExternalCallAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationSignature525"):
                opp_val = getattr(old_value, "OperationSignature525", None)
                if opp_val == self:
                    setattr(old_value, "OperationSignature525", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationSignature525"):
                opp_val = getattr(value, "OperationSignature525", None)
                setattr(value, "OperationSignature525", self)

    def SignatureBelongsToRole(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SignatureBelongsToRole method
        pass

    def OperationRequiredRoleMustBeReferencedByContainer(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement OperationRequiredRoleMustBeReferencedByContainer method
        pass

class pcm_pc_seff_pc_SynchronisationPoint:

    pass
class ForkAction:

    pass
class ResourceDemandingInternalBehaviour:

    pass
class ForkedBehaviour:

    pass
class ResourceDemandingSEFF:

    pass
class seff_pc_ResourceDemandingBehaviour:

    pass
class pcm_pc_seff_reliability_pc_RecoveryActionBehaviour(seff_reliability_pc_FailureHandlingEntity, seff_pc_ResourceDemandingBehaviour):

    def __init__(self, pcm_pc_seff_reliability_pc_RecoveryActionBehaviour: set["seff_reliability_pc_RecoveryActionBehaviour"] = None, seff_reliability_pc: "seff_reliability_pc_RecoveryAction" = None):
        self.pcm_pc_seff_reliability_pc_RecoveryActionBehaviour = pcm_pc_seff_reliability_pc_RecoveryActionBehaviour if pcm_pc_seff_reliability_pc_RecoveryActionBehaviour is not None else set()
        self.seff_reliability_pc = seff_reliability_pc
        
    @property
    def pcm_pc_seff_reliability_pc_RecoveryActionBehaviour(self):
        return self.__pcm_pc_seff_reliability_pc_RecoveryActionBehaviour

    @pcm_pc_seff_reliability_pc_RecoveryActionBehaviour.setter
    def pcm_pc_seff_reliability_pc_RecoveryActionBehaviour(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_seff_reliability_pc_RecoveryActionBehaviour__pcm_pc_seff_reliability_pc_RecoveryActionBehaviour", None)
        self.__pcm_pc_seff_reliability_pc_RecoveryActionBehaviour = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_reliability_pc_RecoveryActionBehaviour"):
                    opp_val = getattr(item, "seff_reliability_pc_RecoveryActionBehaviour", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_reliability_pc_RecoveryActionBehaviour", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_reliability_pc_RecoveryActionBehaviour"):
                    opp_val = getattr(item, "seff_reliability_pc_RecoveryActionBehaviour", None)
                    
                    setattr(item, "seff_reliability_pc_RecoveryActionBehaviour", self)
                    

    @property
    def seff_reliability_pc(self):
        return self.__seff_reliability_pc

    @seff_reliability_pc.setter
    def seff_reliability_pc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_seff_reliability_pc_RecoveryActionBehaviour__seff_reliability_pc", None)
        self.__seff_reliability_pc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc583"):
                opp_val = getattr(old_value, "seff_pc583", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc583", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc583"):
                opp_val = getattr(value, "seff_pc583", None)
                setattr(value, "seff_pc583", self)

    def RecoveryActionBehaviourHasOnlyOnePredecessor(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement RecoveryActionBehaviourHasOnlyOnePredecessor method
        pass

    def SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes method
        pass

    def RecoveryActionBehaviourIsNotSuccessorOfItself(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RecoveryActionBehaviourIsNotSuccessorOfItself method
        pass

class seff_pc_ServiceEffectSpecification:

    pass
class pcm_pc_seff_pc_ServiceEffectSpecification:

    def __init__(self, seffTypeID: str, pcm_pc_seff_pc_ServiceEffectSpecification: "Signature" = None, BasicComponent494: "BasicComponent" = None):
        self.seffTypeID = seffTypeID
        self.pcm_pc_seff_pc_ServiceEffectSpecification = pcm_pc_seff_pc_ServiceEffectSpecification
        self.BasicComponent494 = BasicComponent494
        
    @property
    def seffTypeID(self) -> str:
        return self.__seffTypeID

    @seffTypeID.setter
    def seffTypeID(self, seffTypeID: str):
        self.__seffTypeID = seffTypeID

    @property
    def pcm_pc_seff_pc_ServiceEffectSpecification(self):
        return self.__pcm_pc_seff_pc_ServiceEffectSpecification

    @pcm_pc_seff_pc_ServiceEffectSpecification.setter
    def pcm_pc_seff_pc_ServiceEffectSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_seff_pc_ServiceEffectSpecification__pcm_pc_seff_pc_ServiceEffectSpecification", None)
        self.__pcm_pc_seff_pc_ServiceEffectSpecification = value
        
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
    def BasicComponent494(self):
        return self.__BasicComponent494

    @BasicComponent494.setter
    def BasicComponent494(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_seff_pc_ServiceEffectSpecification__BasicComponent494", None)
        self.__BasicComponent494 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc495"):
                opp_val = getattr(old_value, "repository_pc495", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc495", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc495"):
                opp_val = getattr(value, "repository_pc495", None)
                setattr(value, "repository_pc495", self)

    def ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole method
        pass

class pcm_pc_seff_pc_CallAction:

    pass
class ResourceDemandingBehaviour:

    pass
class pcm_pc_seff_pc_ResourceDemandingInternalBehaviour(ResourceDemandingBehaviour):

    pass
class pcm_pc_seff_pc_ForkedBehaviour(ResourceDemandingBehaviour):

    pass
class BranchAction:

    pass
class AbstractBranchTransition:

    pass
class pcm_pc_seff_pc_GuardedBranchTransition(AbstractBranchTransition):

    pass
class pcm_pc_seff_pc_ProbabilisticBranchTransition(AbstractBranchTransition):

    def __init__(self, branchProbability: float, seff_pc474: "pcm_pc_seff_pc_ResourceDemandingBehaviour", seff_pc488: "pcm_pc_seff_pc_BranchAction"):
        self.branchProbability = branchProbability
        
    @property
    def branchProbability(self) -> float:
        return self.__branchProbability

    @branchProbability.setter
    def branchProbability(self, branchProbability: float):
        self.__branchProbability = branchProbability

class AbstractAction:

    pass
class pcm_pc_seff_pc_AbstractInternalControlFlowAction(AbstractAction):

    pass
class AbstractLoopAction:

    pass
class pcm_pc_seff_pc_CollectionIteratorAction(AbstractLoopAction):

    pass
class pcm_pc_seff_pc_LoopAction(AbstractLoopAction):

    pass
class CommunicationLinkResourceType:

    pass
class SoftwareInducedFailureType:

    pass
class AbstractInternalControlFlowAction:

    pass
class pcm_pc_seff_pc_AcquireAction(AbstractInternalControlFlowAction):

    def __init__(self, timeout: bool, timeoutValue: float, pcm_pc_seff_pc_AcquireAction: "PassiveResource" = None, seff_pc580: "pcm_pc_seff_performance_pc_ParametricResourceDemand", seff_pc558: "pcm_pc_seff_performance_pc_InfrastructureCall", seff_pc564: "pcm_pc_seff_performance_pc_ResourceCall"):
        self.timeout = timeout
        self.timeoutValue = timeoutValue
        self.pcm_pc_seff_pc_AcquireAction = pcm_pc_seff_pc_AcquireAction
        
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
    def pcm_pc_seff_pc_AcquireAction(self):
        return self.__pcm_pc_seff_pc_AcquireAction

    @pcm_pc_seff_pc_AcquireAction.setter
    def pcm_pc_seff_pc_AcquireAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_seff_pc_AcquireAction__pcm_pc_seff_pc_AcquireAction", None)
        self.__pcm_pc_seff_pc_AcquireAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PassiveResource533"):
                opp_val = getattr(old_value, "PassiveResource533", None)
                if opp_val == self:
                    setattr(old_value, "PassiveResource533", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PassiveResource533"):
                opp_val = getattr(value, "PassiveResource533", None)
                setattr(value, "PassiveResource533", self)

    def TimeoutValueOfAcquireActionMustNotBeNegative(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement TimeoutValueOfAcquireActionMustNotBeNegative method
        pass

class pcm_pc_seff_pc_InternalAction(AbstractInternalControlFlowAction):

    def __init__(self, InternalFailureOccurrenceDescription550: set["InternalFailureOccurrenceDescription"] = None, seff_pc580: "pcm_pc_seff_performance_pc_ParametricResourceDemand", seff_pc558: "pcm_pc_seff_performance_pc_InfrastructureCall", seff_pc564: "pcm_pc_seff_performance_pc_ResourceCall"):
        self.InternalFailureOccurrenceDescription550 = InternalFailureOccurrenceDescription550 if InternalFailureOccurrenceDescription550 is not None else set()
        
    @property
    def InternalFailureOccurrenceDescription550(self):
        return self.__InternalFailureOccurrenceDescription550

    @InternalFailureOccurrenceDescription550.setter
    def InternalFailureOccurrenceDescription550(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_seff_pc_InternalAction__InternalFailureOccurrenceDescription550", None)
        self.__InternalFailureOccurrenceDescription550 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reliability_pc551"):
                    opp_val = getattr(item, "reliability_pc551", None)
                    
                    if opp_val == self:
                        setattr(item, "reliability_pc551", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reliability_pc551"):
                    opp_val = getattr(item, "reliability_pc551", None)
                    
                    setattr(item, "reliability_pc551", self)
                    

    def MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed method
        pass

    def SumOfInternalActionFailureProbabilitiesMustNotExceed1(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SumOfInternalActionFailureProbabilitiesMustNotExceed1 method
        pass

class pcm_pc_seff_pc_ForkAction(AbstractInternalControlFlowAction):

    pass
class pcm_pc_seff_reliability_pc_RecoveryAction(AbstractInternalControlFlowAction):

    def __init__(self, pcm_pc_seff_reliability_pc_RecoveryAction: "seff_reliability_pc_RecoveryActionBehaviour" = None, seff_reliability_pc587: set["seff_reliability_pc_RecoveryActionBehaviour"] = None, seff_pc580: "pcm_pc_seff_performance_pc_ParametricResourceDemand", seff_pc558: "pcm_pc_seff_performance_pc_InfrastructureCall", seff_pc564: "pcm_pc_seff_performance_pc_ResourceCall"):
        self.pcm_pc_seff_reliability_pc_RecoveryAction = pcm_pc_seff_reliability_pc_RecoveryAction
        self.seff_reliability_pc587 = seff_reliability_pc587 if seff_reliability_pc587 is not None else set()
        
    @property
    def seff_reliability_pc587(self):
        return self.__seff_reliability_pc587

    @seff_reliability_pc587.setter
    def seff_reliability_pc587(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_seff_reliability_pc_RecoveryAction__seff_reliability_pc587", None)
        self.__seff_reliability_pc587 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_pc588"):
                    opp_val = getattr(item, "seff_pc588", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_pc588", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_pc588"):
                    opp_val = getattr(item, "seff_pc588", None)
                    
                    setattr(item, "seff_pc588", self)
                    

    @property
    def pcm_pc_seff_reliability_pc_RecoveryAction(self):
        return self.__pcm_pc_seff_reliability_pc_RecoveryAction

    @pcm_pc_seff_reliability_pc_RecoveryAction.setter
    def pcm_pc_seff_reliability_pc_RecoveryAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_seff_reliability_pc_RecoveryAction__pcm_pc_seff_reliability_pc_RecoveryAction", None)
        self.__pcm_pc_seff_reliability_pc_RecoveryAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_reliability_pc_RecoveryActionBehaviour585"):
                opp_val = getattr(old_value, "seff_reliability_pc_RecoveryActionBehaviour585", None)
                if opp_val == self:
                    setattr(old_value, "seff_reliability_pc_RecoveryActionBehaviour585", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_reliability_pc_RecoveryActionBehaviour585"):
                opp_val = getattr(value, "seff_reliability_pc_RecoveryActionBehaviour585", None)
                setattr(value, "seff_reliability_pc_RecoveryActionBehaviour585", self)

    def PrimaryBehaviourOfRecoveryActionMustBeSet(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement PrimaryBehaviourOfRecoveryActionMustBeSet method
        pass

class pcm_pc_seff_pc_StartAction(AbstractInternalControlFlowAction):

    def __init__(self, seff_pc580: "pcm_pc_seff_performance_pc_ParametricResourceDemand", seff_pc558: "pcm_pc_seff_performance_pc_InfrastructureCall", seff_pc564: "pcm_pc_seff_performance_pc_ResourceCall"):
        
    def StartActionPredecessorMustNotBeDefined(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement StartActionPredecessorMustNotBeDefined method
        pass

class pcm_pc_seff_pc_SetVariableAction(AbstractInternalControlFlowAction):

    pass
class pcm_pc_seff_pc_BranchAction(AbstractInternalControlFlowAction):

    def __init__(self, AbstractBranchTransition487: set["AbstractBranchTransition"] = None, seff_pc580: "pcm_pc_seff_performance_pc_ParametricResourceDemand", seff_pc558: "pcm_pc_seff_performance_pc_InfrastructureCall", seff_pc564: "pcm_pc_seff_performance_pc_ResourceCall"):
        self.AbstractBranchTransition487 = AbstractBranchTransition487 if AbstractBranchTransition487 is not None else set()
        
    @property
    def AbstractBranchTransition487(self):
        return self.__AbstractBranchTransition487

    @AbstractBranchTransition487.setter
    def AbstractBranchTransition487(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_seff_pc_BranchAction__AbstractBranchTransition487", None)
        self.__AbstractBranchTransition487 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_pc488"):
                    opp_val = getattr(item, "seff_pc488", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_pc488", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_pc488"):
                    opp_val = getattr(item, "seff_pc488", None)
                    
                    setattr(item, "seff_pc488", self)
                    

    def EitherGuardedBranchesOrProbabilisiticBranchTransitions(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EitherGuardedBranchesOrProbabilisiticBranchTransitions method
        pass

    def AllProbabilisticBranchProbabilitiesMustSumUpTo1(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AllProbabilisticBranchProbabilitiesMustSumUpTo1 method
        pass

class pcm_pc_seff_pc_AbstractLoopAction(AbstractInternalControlFlowAction):

    pass
class pcm_pc_seff_pc_ReleaseAction(AbstractInternalControlFlowAction):

    pass
class pcm_pc_seff_pc_StopAction(AbstractInternalControlFlowAction):

    def __init__(self, seff_pc580: "pcm_pc_seff_performance_pc_ParametricResourceDemand", seff_pc558: "pcm_pc_seff_performance_pc_InfrastructureCall", seff_pc564: "pcm_pc_seff_performance_pc_ResourceCall"):
        
    def StopActionSuccessorMustNotBeDefined(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement StopActionSuccessorMustNotBeDefined method
        pass

class pcm_pc_reliability_pc_ResourceTimeoutFailureType(SoftwareInducedFailureType):

    pass
class qos_reliability_pc_SpecifiedReliabilityAnnotation:

    pass
class FailureOccurrenceDescription:

    pass
class pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription(FailureOccurrenceDescription):

    def __init__(self, qos_reliability_pc: "qos_reliability_pc_SpecifiedReliabilityAnnotation" = None, pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription: "FailureType" = None):
        self.qos_reliability_pc = qos_reliability_pc
        self.pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription = pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription
        
    @property
    def pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription(self):
        return self.__pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription

    @pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription.setter
    def pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription__pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription", None)
        self.__pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FailureType448"):
                opp_val = getattr(old_value, "FailureType448", None)
                if opp_val == self:
                    setattr(old_value, "FailureType448", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FailureType448"):
                opp_val = getattr(value, "FailureType448", None)
                setattr(value, "FailureType448", self)

    @property
    def qos_reliability_pc(self):
        return self.__qos_reliability_pc

    @qos_reliability_pc.setter
    def qos_reliability_pc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription__qos_reliability_pc", None)
        self.__qos_reliability_pc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qosannotations_pc446"):
                opp_val = getattr(old_value, "qosannotations_pc446", None)
                if opp_val == self:
                    setattr(old_value, "qosannotations_pc446", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qosannotations_pc446"):
                opp_val = getattr(value, "qosannotations_pc446", None)
                setattr(value, "qosannotations_pc446", self)

    def NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription method
        pass

class pcm_pc_reliability_pc_InternalFailureOccurrenceDescription(FailureOccurrenceDescription):

    def __init__(self, InternalAction: "InternalAction" = None, SoftwareInducedFailureType: "SoftwareInducedFailureType" = None):
        self.InternalAction = InternalAction
        self.SoftwareInducedFailureType = SoftwareInducedFailureType
        
    @property
    def InternalAction(self):
        return self.__InternalAction

    @InternalAction.setter
    def InternalAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_reliability_pc_InternalFailureOccurrenceDescription__InternalAction", None)
        self.__InternalAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc440"):
                opp_val = getattr(old_value, "seff_pc440", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc440", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc440"):
                opp_val = getattr(value, "seff_pc440", None)
                setattr(value, "seff_pc440", self)

    @property
    def SoftwareInducedFailureType(self):
        return self.__SoftwareInducedFailureType

    @SoftwareInducedFailureType.setter
    def SoftwareInducedFailureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_reliability_pc_InternalFailureOccurrenceDescription__SoftwareInducedFailureType", None)
        self.__SoftwareInducedFailureType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reliability_pc442"):
                opp_val = getattr(old_value, "reliability_pc442", None)
                if opp_val == self:
                    setattr(old_value, "reliability_pc442", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reliability_pc442"):
                opp_val = getattr(value, "reliability_pc442", None)
                setattr(value, "reliability_pc442", self)

    def NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription method
        pass

class InternalAction:

    pass
class Variable:

    pass
class pcm_pc_parameter_pc_CharacterisedVariable(Variable):

    def __init__(self, characterisationType: str):
        self.characterisationType = characterisationType
        
    @property
    def characterisationType(self) -> str:
        return self.__characterisationType

    @characterisationType.setter
    def characterisationType(self, characterisationType: str):
        self.__characterisationType = characterisationType

class InternalFailureOccurrenceDescription:

    pass
class ProcessingResourceType:

    pass
class pcm_pc_reliability_pc_FailureOccurrenceDescription:

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

class pcm_pc_parameter_pc_VariableUsage:

    pass
class pcm_pc_protocol_pc_Protocol:

    def __init__(self, protocolTypeID: str):
        self.protocolTypeID = protocolTypeID
        
    @property
    def protocolTypeID(self) -> str:
        return self.__protocolTypeID

    @protocolTypeID.setter
    def protocolTypeID(self, protocolTypeID: str):
        self.__protocolTypeID = protocolTypeID

class pcm_pc_parameter_pc_VariableCharacterisation:

    def __init__(self, type: str, PCMRandomVariable430: "PCMRandomVariable" = None, VariableUsage433: "VariableUsage" = None):
        self.type = type
        self.PCMRandomVariable430 = PCMRandomVariable430
        self.VariableUsage433 = VariableUsage433
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def VariableUsage433(self):
        return self.__VariableUsage433

    @VariableUsage433.setter
    def VariableUsage433(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_parameter_pc_VariableCharacterisation__VariableUsage433", None)
        self.__VariableUsage433 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameter_pc434"):
                opp_val = getattr(old_value, "parameter_pc434", None)
                if opp_val == self:
                    setattr(old_value, "parameter_pc434", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameter_pc434"):
                opp_val = getattr(value, "parameter_pc434", None)
                setattr(value, "parameter_pc434", self)

    @property
    def PCMRandomVariable430(self):
        return self.__PCMRandomVariable430

    @PCMRandomVariable430.setter
    def PCMRandomVariable430(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_parameter_pc_VariableCharacterisation__PCMRandomVariable430", None)
        self.__PCMRandomVariable430 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc431"):
                opp_val = getattr(old_value, "core_pc431", None)
                if opp_val == self:
                    setattr(old_value, "core_pc431", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc431"):
                opp_val = getattr(value, "core_pc431", None)
                setattr(value, "core_pc431", self)

class parameter_pc_pcm_pc_AbstractNamedReference:

    pass
class EntryLevelSystemCall:

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
class pcm_pc_seff_performance_pc_InfrastructureCall(CallAction):

    def __init__(self, pcm_pc_seff_performance_pc_InfrastructureCall: "InfrastructureSignature" = None, PCMRandomVariable555: "PCMRandomVariable" = None, AbstractInternalControlFlowAction: "AbstractInternalControlFlowAction" = None, pcm_pc_seff_performance_pc_InfrastructureCall560: "InfrastructureRequiredRole" = None, seff_pc411: "pcm_pc_parameter_pc_VariableUsage"):
        self.pcm_pc_seff_performance_pc_InfrastructureCall = pcm_pc_seff_performance_pc_InfrastructureCall
        self.PCMRandomVariable555 = PCMRandomVariable555
        self.AbstractInternalControlFlowAction = AbstractInternalControlFlowAction
        self.pcm_pc_seff_performance_pc_InfrastructureCall560 = pcm_pc_seff_performance_pc_InfrastructureCall560
        
    @property
    def pcm_pc_seff_performance_pc_InfrastructureCall(self):
        return self.__pcm_pc_seff_performance_pc_InfrastructureCall

    @pcm_pc_seff_performance_pc_InfrastructureCall.setter
    def pcm_pc_seff_performance_pc_InfrastructureCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_seff_performance_pc_InfrastructureCall__pcm_pc_seff_performance_pc_InfrastructureCall", None)
        self.__pcm_pc_seff_performance_pc_InfrastructureCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InfrastructureSignature553"):
                opp_val = getattr(old_value, "InfrastructureSignature553", None)
                if opp_val == self:
                    setattr(old_value, "InfrastructureSignature553", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InfrastructureSignature553"):
                opp_val = getattr(value, "InfrastructureSignature553", None)
                setattr(value, "InfrastructureSignature553", self)

    @property
    def AbstractInternalControlFlowAction(self):
        return self.__AbstractInternalControlFlowAction

    @AbstractInternalControlFlowAction.setter
    def AbstractInternalControlFlowAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_seff_performance_pc_InfrastructureCall__AbstractInternalControlFlowAction", None)
        self.__AbstractInternalControlFlowAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc558"):
                opp_val = getattr(old_value, "seff_pc558", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc558", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc558"):
                opp_val = getattr(value, "seff_pc558", None)
                setattr(value, "seff_pc558", self)

    @property
    def PCMRandomVariable555(self):
        return self.__PCMRandomVariable555

    @PCMRandomVariable555.setter
    def PCMRandomVariable555(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_seff_performance_pc_InfrastructureCall__PCMRandomVariable555", None)
        self.__PCMRandomVariable555 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc556"):
                opp_val = getattr(old_value, "core_pc556", None)
                if opp_val == self:
                    setattr(old_value, "core_pc556", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc556"):
                opp_val = getattr(value, "core_pc556", None)
                setattr(value, "core_pc556", self)

    @property
    def pcm_pc_seff_performance_pc_InfrastructureCall560(self):
        return self.__pcm_pc_seff_performance_pc_InfrastructureCall560

    @pcm_pc_seff_performance_pc_InfrastructureCall560.setter
    def pcm_pc_seff_performance_pc_InfrastructureCall560(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_seff_performance_pc_InfrastructureCall__pcm_pc_seff_performance_pc_InfrastructureCall560", None)
        self.__pcm_pc_seff_performance_pc_InfrastructureCall560 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InfrastructureRequiredRole561"):
                opp_val = getattr(old_value, "InfrastructureRequiredRole561", None)
                if opp_val == self:
                    setattr(old_value, "InfrastructureRequiredRole561", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InfrastructureRequiredRole561"):
                opp_val = getattr(value, "InfrastructureRequiredRole561", None)
                setattr(value, "InfrastructureRequiredRole561", self)

    def ReferencedRequiredRoleMustBeRequiredByComponent(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ReferencedRequiredRoleMustBeRequiredByComponent method
        pass

    def SignatureMustBelongToUsedRequiredRole(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SignatureMustBelongToUsedRequiredRole method
        pass

    def SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

class pcm_pc_seff_pc_CallReturnAction(CallAction):

    pass
class pcm_pc_seff_performance_pc_ResourceCall(CallAction):

    def __init__(self, AbstractInternalControlFlowAction563: "AbstractInternalControlFlowAction" = None, pcm_pc_seff_performance_pc_ResourceCall: "entity_pc_ResourceRequiredRole" = None, pcm_pc_seff_performance_pc_ResourceCall568: "ResourceSignature" = None, PCMRandomVariable571: "PCMRandomVariable" = None, seff_pc411: "pcm_pc_parameter_pc_VariableUsage"):
        self.AbstractInternalControlFlowAction563 = AbstractInternalControlFlowAction563
        self.pcm_pc_seff_performance_pc_ResourceCall = pcm_pc_seff_performance_pc_ResourceCall
        self.pcm_pc_seff_performance_pc_ResourceCall568 = pcm_pc_seff_performance_pc_ResourceCall568
        self.PCMRandomVariable571 = PCMRandomVariable571
        
    @property
    def pcm_pc_seff_performance_pc_ResourceCall(self):
        return self.__pcm_pc_seff_performance_pc_ResourceCall

    @pcm_pc_seff_performance_pc_ResourceCall.setter
    def pcm_pc_seff_performance_pc_ResourceCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_seff_performance_pc_ResourceCall__pcm_pc_seff_performance_pc_ResourceCall", None)
        self.__pcm_pc_seff_performance_pc_ResourceCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entity_pc_ResourceRequiredRole566"):
                opp_val = getattr(old_value, "entity_pc_ResourceRequiredRole566", None)
                if opp_val == self:
                    setattr(old_value, "entity_pc_ResourceRequiredRole566", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entity_pc_ResourceRequiredRole566"):
                opp_val = getattr(value, "entity_pc_ResourceRequiredRole566", None)
                setattr(value, "entity_pc_ResourceRequiredRole566", self)

    @property
    def PCMRandomVariable571(self):
        return self.__PCMRandomVariable571

    @PCMRandomVariable571.setter
    def PCMRandomVariable571(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_seff_performance_pc_ResourceCall__PCMRandomVariable571", None)
        self.__PCMRandomVariable571 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc572"):
                opp_val = getattr(old_value, "core_pc572", None)
                if opp_val == self:
                    setattr(old_value, "core_pc572", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc572"):
                opp_val = getattr(value, "core_pc572", None)
                setattr(value, "core_pc572", self)

    @property
    def AbstractInternalControlFlowAction563(self):
        return self.__AbstractInternalControlFlowAction563

    @AbstractInternalControlFlowAction563.setter
    def AbstractInternalControlFlowAction563(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_seff_performance_pc_ResourceCall__AbstractInternalControlFlowAction563", None)
        self.__AbstractInternalControlFlowAction563 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc564"):
                opp_val = getattr(old_value, "seff_pc564", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc564", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc564"):
                opp_val = getattr(value, "seff_pc564", None)
                setattr(value, "seff_pc564", self)

    @property
    def pcm_pc_seff_performance_pc_ResourceCall568(self):
        return self.__pcm_pc_seff_performance_pc_ResourceCall568

    @pcm_pc_seff_performance_pc_ResourceCall568.setter
    def pcm_pc_seff_performance_pc_ResourceCall568(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_seff_performance_pc_ResourceCall__pcm_pc_seff_performance_pc_ResourceCall568", None)
        self.__pcm_pc_seff_performance_pc_ResourceCall568 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceSignature569"):
                opp_val = getattr(old_value, "ResourceSignature569", None)
                if opp_val == self:
                    setattr(old_value, "ResourceSignature569", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceSignature569"):
                opp_val = getattr(value, "ResourceSignature569", None)
                setattr(value, "ResourceSignature569", self)

    def SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

    def ResourceSignatureBelongsToResourceRequiredRole(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceSignatureBelongsToResourceRequiredRole method
        pass

    def ResourceRequiredRoleMustBeReferencedByComponent(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceRequiredRoleMustBeReferencedByComponent method
        pass

class NetworkInducedFailureType:

    pass
class SchedulingPolicy:

    pass
class pcm_pc_resourcetype_pc_ResourceRepository:

    pass
class ResourceRepository:

    pass
class UnitCarryingElement:

    pass
class HardwareInducedFailureType:

    pass
class ResourceType:

    pass
class pcm_pc_resourcetype_pc_CommunicationLinkResourceType(ResourceType):

    pass
class pcm_pc_resourcetype_pc_ProcessingResourceType(ResourceType):

    pass
class NamedElement:

    pass
class pcm_pc_resourceenvironment_pc_ResourceEnvironment(NamedElement):

    pass
class pcm_pc_repository_pc_InnerDeclaration(NamedElement):

    pass
class InnerDeclaration:

    pass
class CompositeDataType:

    pass
class repository_pc_DataType:

    pass
class repository_pc_ImplementationComponentType:

    pass
class entity_pc_ComposedProvidingRequiringEntity:

    pass
class pcm_pc_completions_pc_Completion(entity_pc_ComposedProvidingRequiringEntity, repository_pc_ImplementationComponentType):

    pass
class pcm_pc_subsystem_pc_SubSystem(entity_pc_ComposedProvidingRequiringEntity, repository_pc_RepositoryComponent):

    pass
class pcm_pc_repository_pc_CompositeComponent(entity_pc_ComposedProvidingRequiringEntity, repository_pc_ImplementationComponentType):

    def __init__(self):
        
    def ProvideSameInterfaces(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ProvideSameInterfaces method
        pass

    def RequireSameInterfaces(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RequireSameInterfaces method
        pass

class ProvidesComponentType:

    pass
class InfrastructureInterface:

    pass
class pcm_pc_repository_pc_ExceptionType:

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
class OperationInterface:

    pass
class Protocol:

    pass
class Signature:

    pass
class pcm_pc_repository_pc_OperationSignature(Signature):

    def __init__(self, OperationInterface: "OperationInterface" = None, Parameter348: set["Parameter"] = None, pcm_pc_repository_pc_OperationSignature: "DataType" = None, Signature592: "pcm_pc_qosannotations_pc_SpecifiedQoSAnnotation", Signature: "pcm_pc_seff_pc_ServiceEffectSpecification", Signature604: "pcm_pc_qosannotations_pc_SpecifiedOutputParameterAbstraction"):
        self.OperationInterface = OperationInterface
        self.Parameter348 = Parameter348 if Parameter348 is not None else set()
        self.pcm_pc_repository_pc_OperationSignature = pcm_pc_repository_pc_OperationSignature
        
    @property
    def Parameter348(self):
        return self.__Parameter348

    @Parameter348.setter
    def Parameter348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_repository_pc_OperationSignature__Parameter348", None)
        self.__Parameter348 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_pc349"):
                    opp_val = getattr(item, "repository_pc349", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_pc349", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_pc349"):
                    opp_val = getattr(item, "repository_pc349", None)
                    
                    setattr(item, "repository_pc349", self)
                    

    @property
    def pcm_pc_repository_pc_OperationSignature(self):
        return self.__pcm_pc_repository_pc_OperationSignature

    @pcm_pc_repository_pc_OperationSignature.setter
    def pcm_pc_repository_pc_OperationSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_repository_pc_OperationSignature__pcm_pc_repository_pc_OperationSignature", None)
        self.__pcm_pc_repository_pc_OperationSignature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType351"):
                opp_val = getattr(old_value, "DataType351", None)
                if opp_val == self:
                    setattr(old_value, "DataType351", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType351"):
                opp_val = getattr(value, "DataType351", None)
                setattr(value, "DataType351", self)

    @property
    def OperationInterface(self):
        return self.__OperationInterface

    @OperationInterface.setter
    def OperationInterface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_repository_pc_OperationSignature__OperationInterface", None)
        self.__OperationInterface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc346"):
                opp_val = getattr(old_value, "repository_pc346", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc346", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc346"):
                opp_val = getattr(value, "repository_pc346", None)
                setattr(value, "repository_pc346", self)

    def ParameterNamesHaveToBeUniqueForASignature(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ParameterNamesHaveToBeUniqueForASignature method
        pass

class pcm_pc_repository_pc_InfrastructureSignature(Signature):

    pass
class pcm_pc_repository_pc_EventType(Signature):

    pass
class Parameter:

    pass
class pcm_pc_repository_pc_RequiredCharacterisation:

    def __init__(self, type: str, pcm_pc_repository_pc_RequiredCharacterisation: "Parameter" = None, Interface317: "Interface" = None):
        self.type = type
        self.pcm_pc_repository_pc_RequiredCharacterisation = pcm_pc_repository_pc_RequiredCharacterisation
        self.Interface317 = Interface317
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def Interface317(self):
        return self.__Interface317

    @Interface317.setter
    def Interface317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_repository_pc_RequiredCharacterisation__Interface317", None)
        self.__Interface317 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc318"):
                opp_val = getattr(old_value, "repository_pc318", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc318", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc318"):
                opp_val = getattr(value, "repository_pc318", None)
                setattr(value, "repository_pc318", self)

    @property
    def pcm_pc_repository_pc_RequiredCharacterisation(self):
        return self.__pcm_pc_repository_pc_RequiredCharacterisation

    @pcm_pc_repository_pc_RequiredCharacterisation.setter
    def pcm_pc_repository_pc_RequiredCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_repository_pc_RequiredCharacterisation__pcm_pc_repository_pc_RequiredCharacterisation", None)
        self.__pcm_pc_repository_pc_RequiredCharacterisation = value
        
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
class InfrastructureSignature:

    pass
class DataType:

    pass
class pcm_pc_repository_pc_PrimitiveDataType(DataType):

    def __init__(self, type: str, DataType372: "pcm_pc_repository_pc_InnerDeclaration", DataType: "pcm_pc_repository_pc_Parameter", repository_pc305: "pcm_pc_repository_pc_Repository", DataType351: "pcm_pc_repository_pc_OperationSignature", DataType367: "pcm_pc_repository_pc_CollectionDataType"):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class pcm_pc_repository_pc_Parameter:

    def __init__(self, parameterName: str, modifier__Parameter: str, InfrastructureSignature: "InfrastructureSignature" = None, OperationSignature288: "OperationSignature" = None, EventType: "EventType" = None, ResourceSignature: "ResourceSignature" = None, pcm_pc_repository_pc_Parameter: "DataType" = None):
        self.parameterName = parameterName
        self.modifier__Parameter = modifier__Parameter
        self.InfrastructureSignature = InfrastructureSignature
        self.OperationSignature288 = OperationSignature288
        self.EventType = EventType
        self.ResourceSignature = ResourceSignature
        self.pcm_pc_repository_pc_Parameter = pcm_pc_repository_pc_Parameter
        
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
    def ResourceSignature(self):
        return self.__ResourceSignature

    @ResourceSignature.setter
    def ResourceSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_repository_pc_Parameter__ResourceSignature", None)
        self.__ResourceSignature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcetype_pc"):
                opp_val = getattr(old_value, "resourcetype_pc", None)
                if opp_val == self:
                    setattr(old_value, "resourcetype_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcetype_pc"):
                opp_val = getattr(value, "resourcetype_pc", None)
                setattr(value, "resourcetype_pc", self)

    @property
    def EventType(self):
        return self.__EventType

    @EventType.setter
    def EventType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_repository_pc_Parameter__EventType", None)
        self.__EventType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc291"):
                opp_val = getattr(old_value, "repository_pc291", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc291", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc291"):
                opp_val = getattr(value, "repository_pc291", None)
                setattr(value, "repository_pc291", self)

    @property
    def OperationSignature288(self):
        return self.__OperationSignature288

    @OperationSignature288.setter
    def OperationSignature288(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_repository_pc_Parameter__OperationSignature288", None)
        self.__OperationSignature288 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc289"):
                opp_val = getattr(old_value, "repository_pc289", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc289", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc289"):
                opp_val = getattr(value, "repository_pc289", None)
                setattr(value, "repository_pc289", self)

    @property
    def InfrastructureSignature(self):
        return self.__InfrastructureSignature

    @InfrastructureSignature.setter
    def InfrastructureSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_repository_pc_Parameter__InfrastructureSignature", None)
        self.__InfrastructureSignature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc286"):
                opp_val = getattr(old_value, "repository_pc286", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc286", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc286"):
                opp_val = getattr(value, "repository_pc286", None)
                setattr(value, "repository_pc286", self)

    @property
    def pcm_pc_repository_pc_Parameter(self):
        return self.__pcm_pc_repository_pc_Parameter

    @pcm_pc_repository_pc_Parameter.setter
    def pcm_pc_repository_pc_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_repository_pc_Parameter__pcm_pc_repository_pc_Parameter", None)
        self.__pcm_pc_repository_pc_Parameter = value
        
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

class Repository:

    pass
class InterfaceProvidingRequiringEntity:

    pass
class pcm_pc_repository_pc_RepositoryComponent(InterfaceProvidingRequiringEntity):

    pass
class FailureType:

    pass
class pcm_pc_reliability_pc_HardwareInducedFailureType(FailureType):

    def __init__(self, ProcessingResourceType: "ProcessingResourceType" = None, reliability_pc302: "pcm_pc_repository_pc_Repository", FailureType331: "pcm_pc_repository_pc_Signature", FailureType590: "pcm_pc_seff_reliability_pc_FailureHandlingEntity", FailureType448: "pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription"):
        self.ProcessingResourceType = ProcessingResourceType
        
    @property
    def ProcessingResourceType(self):
        return self.__ProcessingResourceType

    @ProcessingResourceType.setter
    def ProcessingResourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_reliability_pc_HardwareInducedFailureType__ProcessingResourceType", None)
        self.__ProcessingResourceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcetype_pc436"):
                opp_val = getattr(old_value, "resourcetype_pc436", None)
                if opp_val == self:
                    setattr(old_value, "resourcetype_pc436", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcetype_pc436"):
                opp_val = getattr(value, "resourcetype_pc436", None)
                setattr(value, "resourcetype_pc436", self)

    def HardwareInducedFailureTypeHasProcessingResourceType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement HardwareInducedFailureTypeHasProcessingResourceType method
        pass

class pcm_pc_reliability_pc_SoftwareInducedFailureType(FailureType):

    pass
class pcm_pc_reliability_pc_NetworkInducedFailureType(FailureType):

    def __init__(self, CommunicationLinkResourceType: "CommunicationLinkResourceType" = None, reliability_pc302: "pcm_pc_repository_pc_Repository", FailureType331: "pcm_pc_repository_pc_Signature", FailureType590: "pcm_pc_seff_reliability_pc_FailureHandlingEntity", FailureType448: "pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription"):
        self.CommunicationLinkResourceType = CommunicationLinkResourceType
        
    @property
    def CommunicationLinkResourceType(self):
        return self.__CommunicationLinkResourceType

    @CommunicationLinkResourceType.setter
    def CommunicationLinkResourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_reliability_pc_NetworkInducedFailureType__CommunicationLinkResourceType", None)
        self.__CommunicationLinkResourceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcetype_pc444"):
                opp_val = getattr(old_value, "resourcetype_pc444", None)
                if opp_val == self:
                    setattr(old_value, "resourcetype_pc444", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcetype_pc444"):
                opp_val = getattr(value, "resourcetype_pc444", None)
                setattr(value, "resourcetype_pc444", self)

    def NetworkInducedFailureTypeHasCommunicationLinkResourceType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NetworkInducedFailureTypeHasCommunicationLinkResourceType method
        pass

class Interface:

    pass
class pcm_pc_repository_pc_EventGroup(Interface):

    pass
class pcm_pc_repository_pc_InfrastructureInterface(Interface):

    pass
class pcm_pc_repository_pc_OperationInterface(Interface):

    def __init__(self, OperationSignature353: set["OperationSignature"] = None, Interface307: "pcm_pc_repository_pc_Interface", repository_pc300: "pcm_pc_repository_pc_Repository", repository_pc318: "pcm_pc_repository_pc_RequiredCharacterisation"):
        self.OperationSignature353 = OperationSignature353 if OperationSignature353 is not None else set()
        
    @property
    def OperationSignature353(self):
        return self.__OperationSignature353

    @OperationSignature353.setter
    def OperationSignature353(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_repository_pc_OperationInterface__OperationSignature353", None)
        self.__OperationSignature353 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_pc354"):
                    opp_val = getattr(item, "repository_pc354", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_pc354", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_pc354"):
                    opp_val = getattr(item, "repository_pc354", None)
                    
                    setattr(item, "repository_pc354", self)
                    

    def SignaturesHaveToBeUniqueForAnInterface(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SignaturesHaveToBeUniqueForAnInterface method
        pass

class pcm_pc_repository_pc_DataType:

    pass
class ResourceSignature:

    pass
class EventType:

    pass
class ServiceEffectSpecification:

    pass
class CompleteComponentType:

    pass
class ImplementationComponentType:

    pass
class pcm_pc_repository_pc_BasicComponent(ImplementationComponentType):

    def __init__(self, ServiceEffectSpecification: set["ServiceEffectSpecification"] = None, PassiveResource273: set["PassiveResource"] = None):
        self.ServiceEffectSpecification = ServiceEffectSpecification if ServiceEffectSpecification is not None else set()
        self.PassiveResource273 = PassiveResource273 if PassiveResource273 is not None else set()
        
    @property
    def ServiceEffectSpecification(self):
        return self.__ServiceEffectSpecification

    @ServiceEffectSpecification.setter
    def ServiceEffectSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_repository_pc_BasicComponent__ServiceEffectSpecification", None)
        self.__ServiceEffectSpecification = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_pc271"):
                    opp_val = getattr(item, "seff_pc271", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_pc271", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_pc271"):
                    opp_val = getattr(item, "seff_pc271", None)
                    
                    setattr(item, "seff_pc271", self)
                    

    @property
    def PassiveResource273(self):
        return self.__PassiveResource273

    @PassiveResource273.setter
    def PassiveResource273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_repository_pc_BasicComponent__PassiveResource273", None)
        self.__PassiveResource273 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_pc274"):
                    opp_val = getattr(item, "repository_pc274", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_pc274", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_pc274"):
                    opp_val = getattr(item, "repository_pc274", None)
                    
                    setattr(item, "repository_pc274", self)
                    

    def ProvideSameInterfacesAsImplementationType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ProvideSameInterfacesAsImplementationType method
        pass

    def NoSeffTypeUsedTwice(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement NoSeffTypeUsedTwice method
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
class pcm_pc_usagemodel_pc_BranchTransition:

    def __init__(self, branchProbability: float, Branch: "Branch" = None, ScenarioBehaviour244: "ScenarioBehaviour" = None):
        self.branchProbability = branchProbability
        self.Branch = Branch
        self.ScenarioBehaviour244 = ScenarioBehaviour244
        
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
        old_value = getattr(self, f"_pcm_pc_usagemodel_pc_BranchTransition__Branch", None)
        self.__Branch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc242"):
                opp_val = getattr(old_value, "usagemodel_pc242", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc242", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc242"):
                opp_val = getattr(value, "usagemodel_pc242", None)
                setattr(value, "usagemodel_pc242", self)

    @property
    def ScenarioBehaviour244(self):
        return self.__ScenarioBehaviour244

    @ScenarioBehaviour244.setter
    def ScenarioBehaviour244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_usagemodel_pc_BranchTransition__ScenarioBehaviour244", None)
        self.__ScenarioBehaviour244 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc245"):
                opp_val = getattr(old_value, "usagemodel_pc245", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc245", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc245"):
                opp_val = getattr(value, "usagemodel_pc245", None)
                setattr(value, "usagemodel_pc245", self)

class BranchTransition:

    pass
class pcm_pc_usagemodel_pc_UserData:

    pass
class Workload:

    pass
class pcm_pc_usagemodel_pc_ClosedWorkload(Workload):

    def __init__(self, population: int, PCMRandomVariable262: "PCMRandomVariable" = None, usagemodel_pc198: "pcm_pc_usagemodel_pc_UsageScenario"):
        self.population = population
        self.PCMRandomVariable262 = PCMRandomVariable262
        
    @property
    def population(self) -> int:
        return self.__population

    @population.setter
    def population(self, population: int):
        self.__population = population

    @property
    def PCMRandomVariable262(self):
        return self.__PCMRandomVariable262

    @PCMRandomVariable262.setter
    def PCMRandomVariable262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_usagemodel_pc_ClosedWorkload__PCMRandomVariable262", None)
        self.__PCMRandomVariable262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc263"):
                opp_val = getattr(old_value, "core_pc263", None)
                if opp_val == self:
                    setattr(old_value, "core_pc263", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc263"):
                opp_val = getattr(value, "core_pc263", None)
                setattr(value, "core_pc263", self)

    def PopulationInClosedWorkloadNeedsToBeSpecified(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement PopulationInClosedWorkloadNeedsToBeSpecified method
        pass

    def ThinkTimeInClosedWorkloadNeedsToBeSpecified(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ThinkTimeInClosedWorkloadNeedsToBeSpecified method
        pass

class pcm_pc_usagemodel_pc_OpenWorkload(Workload):

    def __init__(self, PCMRandomVariable256: "PCMRandomVariable" = None, usagemodel_pc198: "pcm_pc_usagemodel_pc_UsageScenario"):
        self.PCMRandomVariable256 = PCMRandomVariable256
        
    @property
    def PCMRandomVariable256(self):
        return self.__PCMRandomVariable256

    @PCMRandomVariable256.setter
    def PCMRandomVariable256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_usagemodel_pc_OpenWorkload__PCMRandomVariable256", None)
        self.__PCMRandomVariable256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc257"):
                opp_val = getattr(old_value, "core_pc257", None)
                if opp_val == self:
                    setattr(old_value, "core_pc257", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc257"):
                opp_val = getattr(value, "core_pc257", None)
                setattr(value, "core_pc257", self)

    def InterArrivalTimeInOpenWorkloadNeedsToBeSpecified(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement InterArrivalTimeInOpenWorkloadNeedsToBeSpecified method
        pass

class ScenarioBehaviour:

    pass
class UsageModel:

    pass
class UsageScenario:

    pass
class OperationSignature:

    pass
class AbstractUserAction:

    pass
class pcm_pc_usagemodel_pc_Stop(AbstractUserAction):

    def __init__(self, usagemodel_pc226: "pcm_pc_usagemodel_pc_AbstractUserAction", usagemodel_pc240: "pcm_pc_usagemodel_pc_ScenarioBehaviour", usagemodel_pc223: "pcm_pc_usagemodel_pc_AbstractUserAction"):
        
    def StopHasNoSuccessor(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement StopHasNoSuccessor method
        pass

class pcm_pc_usagemodel_pc_Branch(AbstractUserAction):

    def __init__(self, BranchTransition247: set["BranchTransition"] = None, usagemodel_pc226: "pcm_pc_usagemodel_pc_AbstractUserAction", usagemodel_pc240: "pcm_pc_usagemodel_pc_ScenarioBehaviour", usagemodel_pc223: "pcm_pc_usagemodel_pc_AbstractUserAction"):
        self.BranchTransition247 = BranchTransition247 if BranchTransition247 is not None else set()
        
    @property
    def BranchTransition247(self):
        return self.__BranchTransition247

    @BranchTransition247.setter
    def BranchTransition247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_usagemodel_pc_Branch__BranchTransition247", None)
        self.__BranchTransition247 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "usagemodel_pc248"):
                    opp_val = getattr(item, "usagemodel_pc248", None)
                    
                    if opp_val == self:
                        setattr(item, "usagemodel_pc248", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "usagemodel_pc248"):
                    opp_val = getattr(item, "usagemodel_pc248", None)
                    
                    setattr(item, "usagemodel_pc248", self)
                    

    def AllBranchProbabilitiesMustSumUpTo1(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AllBranchProbabilitiesMustSumUpTo1 method
        pass

class pcm_pc_usagemodel_pc_Delay(AbstractUserAction):

    pass
class pcm_pc_usagemodel_pc_Loop(AbstractUserAction):

    pass
class pcm_pc_usagemodel_pc_Start(AbstractUserAction):

    def __init__(self, usagemodel_pc226: "pcm_pc_usagemodel_pc_AbstractUserAction", usagemodel_pc240: "pcm_pc_usagemodel_pc_ScenarioBehaviour", usagemodel_pc223: "pcm_pc_usagemodel_pc_AbstractUserAction"):
        
    def StartHasNoPredecessor(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement StartHasNoPredecessor method
        pass

class pcm_pc_usagemodel_pc_EntryLevelSystemCall(AbstractUserAction):

    def __init__(self, priority: int, pcm_pc_usagemodel_pc_EntryLevelSystemCall: "OperationProvidedRole" = None, pcm_pc_usagemodel_pc_EntryLevelSystemCall215: "OperationSignature" = None, VariableUsage217: set["VariableUsage"] = None, VariableUsage220: set["VariableUsage"] = None, usagemodel_pc226: "pcm_pc_usagemodel_pc_AbstractUserAction", usagemodel_pc240: "pcm_pc_usagemodel_pc_ScenarioBehaviour", usagemodel_pc223: "pcm_pc_usagemodel_pc_AbstractUserAction"):
        self.priority = priority
        self.pcm_pc_usagemodel_pc_EntryLevelSystemCall = pcm_pc_usagemodel_pc_EntryLevelSystemCall
        self.pcm_pc_usagemodel_pc_EntryLevelSystemCall215 = pcm_pc_usagemodel_pc_EntryLevelSystemCall215
        self.VariableUsage217 = VariableUsage217 if VariableUsage217 is not None else set()
        self.VariableUsage220 = VariableUsage220 if VariableUsage220 is not None else set()
        
    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def VariableUsage217(self):
        return self.__VariableUsage217

    @VariableUsage217.setter
    def VariableUsage217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_usagemodel_pc_EntryLevelSystemCall__VariableUsage217", None)
        self.__VariableUsage217 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "parameter_pc218"):
                    opp_val = getattr(item, "parameter_pc218", None)
                    
                    if opp_val == self:
                        setattr(item, "parameter_pc218", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "parameter_pc218"):
                    opp_val = getattr(item, "parameter_pc218", None)
                    
                    setattr(item, "parameter_pc218", self)
                    

    @property
    def pcm_pc_usagemodel_pc_EntryLevelSystemCall215(self):
        return self.__pcm_pc_usagemodel_pc_EntryLevelSystemCall215

    @pcm_pc_usagemodel_pc_EntryLevelSystemCall215.setter
    def pcm_pc_usagemodel_pc_EntryLevelSystemCall215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_usagemodel_pc_EntryLevelSystemCall__pcm_pc_usagemodel_pc_EntryLevelSystemCall215", None)
        self.__pcm_pc_usagemodel_pc_EntryLevelSystemCall215 = value
        
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
    def VariableUsage220(self):
        return self.__VariableUsage220

    @VariableUsage220.setter
    def VariableUsage220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_usagemodel_pc_EntryLevelSystemCall__VariableUsage220", None)
        self.__VariableUsage220 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "parameter_pc221"):
                    opp_val = getattr(item, "parameter_pc221", None)
                    
                    if opp_val == self:
                        setattr(item, "parameter_pc221", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "parameter_pc221"):
                    opp_val = getattr(item, "parameter_pc221", None)
                    
                    setattr(item, "parameter_pc221", self)
                    

    @property
    def pcm_pc_usagemodel_pc_EntryLevelSystemCall(self):
        return self.__pcm_pc_usagemodel_pc_EntryLevelSystemCall

    @pcm_pc_usagemodel_pc_EntryLevelSystemCall.setter
    def pcm_pc_usagemodel_pc_EntryLevelSystemCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_usagemodel_pc_EntryLevelSystemCall__pcm_pc_usagemodel_pc_EntryLevelSystemCall", None)
        self.__pcm_pc_usagemodel_pc_EntryLevelSystemCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationProvidedRole213"):
                opp_val = getattr(old_value, "OperationProvidedRole213", None)
                if opp_val == self:
                    setattr(old_value, "OperationProvidedRole213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationProvidedRole213"):
                opp_val = getattr(value, "OperationProvidedRole213", None)
                setattr(value, "OperationProvidedRole213", self)

    def EntryLevelSystemCallSignatureMustMatchItsProvidedRole(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement EntryLevelSystemCallSignatureMustMatchItsProvidedRole method
        pass

    def EntryLevelSystemCallMustReferenceProvidedRoleOfASystem(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EntryLevelSystemCallMustReferenceProvidedRoleOfASystem method
        pass

class UserData:

    pass
class pcm_pc_usagemodel_pc_UsageModel:

    pass
class pcm_pc_usagemodel_pc_Workload:

    pass
class InfrastructureRequiredRole:

    pass
class InfrastructureProvidedRole:

    pass
class VariableUsage:

    pass
class RepositoryComponent:

    pass
class pcm_pc_repository_pc_CompleteComponentType(RepositoryComponent):

    def __init__(self, pcm_pc_repository_pc_CompleteComponentType: set["ProvidesComponentType"] = None, RepositoryComponent: "pcm_pc_composition_pc_AssemblyContext", repository_pc298: "pcm_pc_repository_pc_Repository"):
        self.pcm_pc_repository_pc_CompleteComponentType = pcm_pc_repository_pc_CompleteComponentType if pcm_pc_repository_pc_CompleteComponentType is not None else set()
        
    @property
    def pcm_pc_repository_pc_CompleteComponentType(self):
        return self.__pcm_pc_repository_pc_CompleteComponentType

    @pcm_pc_repository_pc_CompleteComponentType.setter
    def pcm_pc_repository_pc_CompleteComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_repository_pc_CompleteComponentType__pcm_pc_repository_pc_CompleteComponentType", None)
        self.__pcm_pc_repository_pc_CompleteComponentType = value if value is not None else set()
        
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

    def AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType method
        pass

class pcm_pc_repository_pc_ProvidesComponentType(RepositoryComponent):

    def __init__(self, RepositoryComponent: "pcm_pc_composition_pc_AssemblyContext", repository_pc298: "pcm_pc_repository_pc_Repository"):
        
    def AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType method
        pass

class pcm_pc_repository_pc_ImplementationComponentType(RepositoryComponent):

    def __init__(self, componentType: str, pcm_pc_repository_pc_ImplementationComponentType: set["CompleteComponentType"] = None, pcm_pc_repository_pc_ImplementationComponentType277: set["VariableUsage"] = None, RepositoryComponent: "pcm_pc_composition_pc_AssemblyContext", repository_pc298: "pcm_pc_repository_pc_Repository"):
        self.componentType = componentType
        self.pcm_pc_repository_pc_ImplementationComponentType = pcm_pc_repository_pc_ImplementationComponentType if pcm_pc_repository_pc_ImplementationComponentType is not None else set()
        self.pcm_pc_repository_pc_ImplementationComponentType277 = pcm_pc_repository_pc_ImplementationComponentType277 if pcm_pc_repository_pc_ImplementationComponentType277 is not None else set()
        
    @property
    def componentType(self) -> str:
        return self.__componentType

    @componentType.setter
    def componentType(self, componentType: str):
        self.__componentType = componentType

    @property
    def pcm_pc_repository_pc_ImplementationComponentType277(self):
        return self.__pcm_pc_repository_pc_ImplementationComponentType277

    @pcm_pc_repository_pc_ImplementationComponentType277.setter
    def pcm_pc_repository_pc_ImplementationComponentType277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_repository_pc_ImplementationComponentType__pcm_pc_repository_pc_ImplementationComponentType277", None)
        self.__pcm_pc_repository_pc_ImplementationComponentType277 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableUsage278"):
                    opp_val = getattr(item, "VariableUsage278", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableUsage278", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableUsage278"):
                    opp_val = getattr(item, "VariableUsage278", None)
                    
                    setattr(item, "VariableUsage278", self)
                    

    @property
    def pcm_pc_repository_pc_ImplementationComponentType(self):
        return self.__pcm_pc_repository_pc_ImplementationComponentType

    @pcm_pc_repository_pc_ImplementationComponentType.setter
    def pcm_pc_repository_pc_ImplementationComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_repository_pc_ImplementationComponentType__pcm_pc_repository_pc_ImplementationComponentType", None)
        self.__pcm_pc_repository_pc_ImplementationComponentType = value if value is not None else set()
        
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
                    

    def providedInterfacesHaveToConformToCompleteType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement providedInterfacesHaveToConformToCompleteType method
        pass

    def RequiredInterfacesHaveToConformToCompleteType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RequiredInterfacesHaveToConformToCompleteType method
        pass

    def ProvidedInterfaceHaveToConformToComponentType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ProvidedInterfaceHaveToConformToComponentType method
        pass

class OperationProvidedRole:

    pass
class OperationRequiredRole:

    pass
class PCMRandomVariable:

    pass
class SinkRole:

    pass
class SourceRole:

    pass
class composition_pc_EventChannelSourceConnector:

    pass
class EventGroup:

    pass
class pcm_pc_composition_pc_ResourceRequiredDelegationConnector:

    pass
class composition_pc_Connector:

    pass
class composition_pc_EventChannel:

    pass
class composition_pc_ResourceRequiredDelegationConnector:

    pass
class composition_pc_AssemblyContext:

    pass
class DelegationConnector:

    pass
class pcm_pc_composition_pc_SinkDelegationConnector(DelegationConnector):

    pass
class pcm_pc_composition_pc_RequiredResourceDelegationConnector(DelegationConnector):

    pass
class pcm_pc_composition_pc_SourceDelegationConnector(DelegationConnector):

    pass
class pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector(DelegationConnector):

    pass
class pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector(DelegationConnector):

    pass
class pcm_pc_composition_pc_RequiredDelegationConnector(DelegationConnector):

    def __init__(self, pcm_pc_composition_pc_RequiredDelegationConnector: "OperationRequiredRole" = None, pcm_pc_composition_pc_RequiredDelegationConnector106: "OperationRequiredRole" = None, pcm_pc_composition_pc_RequiredDelegationConnector109: "composition_pc_AssemblyContext" = None):
        self.pcm_pc_composition_pc_RequiredDelegationConnector = pcm_pc_composition_pc_RequiredDelegationConnector
        self.pcm_pc_composition_pc_RequiredDelegationConnector106 = pcm_pc_composition_pc_RequiredDelegationConnector106
        self.pcm_pc_composition_pc_RequiredDelegationConnector109 = pcm_pc_composition_pc_RequiredDelegationConnector109
        
    @property
    def pcm_pc_composition_pc_RequiredDelegationConnector(self):
        return self.__pcm_pc_composition_pc_RequiredDelegationConnector

    @pcm_pc_composition_pc_RequiredDelegationConnector.setter
    def pcm_pc_composition_pc_RequiredDelegationConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_composition_pc_RequiredDelegationConnector__pcm_pc_composition_pc_RequiredDelegationConnector", None)
        self.__pcm_pc_composition_pc_RequiredDelegationConnector = value
        
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
    def pcm_pc_composition_pc_RequiredDelegationConnector109(self):
        return self.__pcm_pc_composition_pc_RequiredDelegationConnector109

    @pcm_pc_composition_pc_RequiredDelegationConnector109.setter
    def pcm_pc_composition_pc_RequiredDelegationConnector109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_composition_pc_RequiredDelegationConnector__pcm_pc_composition_pc_RequiredDelegationConnector109", None)
        self.__pcm_pc_composition_pc_RequiredDelegationConnector109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_pc_AssemblyContext110"):
                opp_val = getattr(old_value, "composition_pc_AssemblyContext110", None)
                if opp_val == self:
                    setattr(old_value, "composition_pc_AssemblyContext110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_pc_AssemblyContext110"):
                opp_val = getattr(value, "composition_pc_AssemblyContext110", None)
                setattr(value, "composition_pc_AssemblyContext110", self)

    @property
    def pcm_pc_composition_pc_RequiredDelegationConnector106(self):
        return self.__pcm_pc_composition_pc_RequiredDelegationConnector106

    @pcm_pc_composition_pc_RequiredDelegationConnector106.setter
    def pcm_pc_composition_pc_RequiredDelegationConnector106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_composition_pc_RequiredDelegationConnector__pcm_pc_composition_pc_RequiredDelegationConnector106", None)
        self.__pcm_pc_composition_pc_RequiredDelegationConnector106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationRequiredRole107"):
                opp_val = getattr(old_value, "OperationRequiredRole107", None)
                if opp_val == self:
                    setattr(old_value, "OperationRequiredRole107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationRequiredRole107"):
                opp_val = getattr(value, "OperationRequiredRole107", None)
                setattr(value, "OperationRequiredRole107", self)

    def RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector method
        pass

    def RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

    def ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame method
        pass

class pcm_pc_composition_pc_ProvidedDelegationConnector(DelegationConnector):

    def __init__(self, pcm_pc_composition_pc_ProvidedDelegationConnector: "OperationProvidedRole" = None, pcm_pc_composition_pc_ProvidedDelegationConnector99: "OperationProvidedRole" = None, pcm_pc_composition_pc_ProvidedDelegationConnector102: "composition_pc_AssemblyContext" = None):
        self.pcm_pc_composition_pc_ProvidedDelegationConnector = pcm_pc_composition_pc_ProvidedDelegationConnector
        self.pcm_pc_composition_pc_ProvidedDelegationConnector99 = pcm_pc_composition_pc_ProvidedDelegationConnector99
        self.pcm_pc_composition_pc_ProvidedDelegationConnector102 = pcm_pc_composition_pc_ProvidedDelegationConnector102
        
    @property
    def pcm_pc_composition_pc_ProvidedDelegationConnector102(self):
        return self.__pcm_pc_composition_pc_ProvidedDelegationConnector102

    @pcm_pc_composition_pc_ProvidedDelegationConnector102.setter
    def pcm_pc_composition_pc_ProvidedDelegationConnector102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_composition_pc_ProvidedDelegationConnector__pcm_pc_composition_pc_ProvidedDelegationConnector102", None)
        self.__pcm_pc_composition_pc_ProvidedDelegationConnector102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_pc_AssemblyContext103"):
                opp_val = getattr(old_value, "composition_pc_AssemblyContext103", None)
                if opp_val == self:
                    setattr(old_value, "composition_pc_AssemblyContext103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_pc_AssemblyContext103"):
                opp_val = getattr(value, "composition_pc_AssemblyContext103", None)
                setattr(value, "composition_pc_AssemblyContext103", self)

    @property
    def pcm_pc_composition_pc_ProvidedDelegationConnector99(self):
        return self.__pcm_pc_composition_pc_ProvidedDelegationConnector99

    @pcm_pc_composition_pc_ProvidedDelegationConnector99.setter
    def pcm_pc_composition_pc_ProvidedDelegationConnector99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_composition_pc_ProvidedDelegationConnector__pcm_pc_composition_pc_ProvidedDelegationConnector99", None)
        self.__pcm_pc_composition_pc_ProvidedDelegationConnector99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationProvidedRole100"):
                opp_val = getattr(old_value, "OperationProvidedRole100", None)
                if opp_val == self:
                    setattr(old_value, "OperationProvidedRole100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationProvidedRole100"):
                opp_val = getattr(value, "OperationProvidedRole100", None)
                setattr(value, "OperationProvidedRole100", self)

    @property
    def pcm_pc_composition_pc_ProvidedDelegationConnector(self):
        return self.__pcm_pc_composition_pc_ProvidedDelegationConnector

    @pcm_pc_composition_pc_ProvidedDelegationConnector.setter
    def pcm_pc_composition_pc_ProvidedDelegationConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_composition_pc_ProvidedDelegationConnector__pcm_pc_composition_pc_ProvidedDelegationConnector", None)
        self.__pcm_pc_composition_pc_ProvidedDelegationConnector = value
        
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

    def ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame method
        pass

    def ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

class Connector:

    pass
class pcm_pc_composition_pc_EventChannelSourceConnector(Connector):

    pass
class pcm_pc_composition_pc_AssemblyEventConnector(Connector):

    pass
class pcm_pc_composition_pc_EventChannelSinkConnector(Connector):

    pass
class pcm_pc_composition_pc_AssemblyConnector(Connector):

    def __init__(self, pcm_pc_composition_pc_AssemblyConnector: "composition_pc_AssemblyContext" = None, pcm_pc_composition_pc_AssemblyConnector114: "composition_pc_AssemblyContext" = None, pcm_pc_composition_pc_AssemblyConnector117: "OperationProvidedRole" = None, pcm_pc_composition_pc_AssemblyConnector120: "OperationRequiredRole" = None):
        self.pcm_pc_composition_pc_AssemblyConnector = pcm_pc_composition_pc_AssemblyConnector
        self.pcm_pc_composition_pc_AssemblyConnector114 = pcm_pc_composition_pc_AssemblyConnector114
        self.pcm_pc_composition_pc_AssemblyConnector117 = pcm_pc_composition_pc_AssemblyConnector117
        self.pcm_pc_composition_pc_AssemblyConnector120 = pcm_pc_composition_pc_AssemblyConnector120
        
    @property
    def pcm_pc_composition_pc_AssemblyConnector117(self):
        return self.__pcm_pc_composition_pc_AssemblyConnector117

    @pcm_pc_composition_pc_AssemblyConnector117.setter
    def pcm_pc_composition_pc_AssemblyConnector117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_composition_pc_AssemblyConnector__pcm_pc_composition_pc_AssemblyConnector117", None)
        self.__pcm_pc_composition_pc_AssemblyConnector117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationProvidedRole118"):
                opp_val = getattr(old_value, "OperationProvidedRole118", None)
                if opp_val == self:
                    setattr(old_value, "OperationProvidedRole118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationProvidedRole118"):
                opp_val = getattr(value, "OperationProvidedRole118", None)
                setattr(value, "OperationProvidedRole118", self)

    @property
    def pcm_pc_composition_pc_AssemblyConnector120(self):
        return self.__pcm_pc_composition_pc_AssemblyConnector120

    @pcm_pc_composition_pc_AssemblyConnector120.setter
    def pcm_pc_composition_pc_AssemblyConnector120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_composition_pc_AssemblyConnector__pcm_pc_composition_pc_AssemblyConnector120", None)
        self.__pcm_pc_composition_pc_AssemblyConnector120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationRequiredRole121"):
                opp_val = getattr(old_value, "OperationRequiredRole121", None)
                if opp_val == self:
                    setattr(old_value, "OperationRequiredRole121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationRequiredRole121"):
                opp_val = getattr(value, "OperationRequiredRole121", None)
                setattr(value, "OperationRequiredRole121", self)

    @property
    def pcm_pc_composition_pc_AssemblyConnector(self):
        return self.__pcm_pc_composition_pc_AssemblyConnector

    @pcm_pc_composition_pc_AssemblyConnector.setter
    def pcm_pc_composition_pc_AssemblyConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_composition_pc_AssemblyConnector__pcm_pc_composition_pc_AssemblyConnector", None)
        self.__pcm_pc_composition_pc_AssemblyConnector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_pc_AssemblyContext112"):
                opp_val = getattr(old_value, "composition_pc_AssemblyContext112", None)
                if opp_val == self:
                    setattr(old_value, "composition_pc_AssemblyContext112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_pc_AssemblyContext112"):
                opp_val = getattr(value, "composition_pc_AssemblyContext112", None)
                setattr(value, "composition_pc_AssemblyContext112", self)

    @property
    def pcm_pc_composition_pc_AssemblyConnector114(self):
        return self.__pcm_pc_composition_pc_AssemblyConnector114

    @pcm_pc_composition_pc_AssemblyConnector114.setter
    def pcm_pc_composition_pc_AssemblyConnector114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_composition_pc_AssemblyConnector__pcm_pc_composition_pc_AssemblyConnector114", None)
        self.__pcm_pc_composition_pc_AssemblyConnector114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_pc_AssemblyContext115"):
                opp_val = getattr(old_value, "composition_pc_AssemblyContext115", None)
                if opp_val == self:
                    setattr(old_value, "composition_pc_AssemblyContext115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_pc_AssemblyContext115"):
                opp_val = getattr(value, "composition_pc_AssemblyContext115", None)
                setattr(value, "composition_pc_AssemblyContext115", self)

    def AssemblyConnectorsReferencedInterfacesMustMatch(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AssemblyConnectorsReferencedInterfacesMustMatch method
        pass

    def AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch method
        pass

    def AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch method
        pass

class pcm_pc_composition_pc_AssemblyInfrastructureConnector(Connector):

    pass
class pcm_pc_composition_pc_DelegationConnector(Connector):

    pass
class entity_pc_NamedElement:

    pass
class Identifier:

    pass
class pcm_pc_seff_pc_ResourceDemandingSEFF(seff_pc_ServiceEffectSpecification, Identifier, seff_pc_ResourceDemandingBehaviour):

    pass
class pcm_pc_seff_pc_ResourceDemandingBehaviour(Identifier):

    def __init__(self, AbstractLoopAction: "AbstractLoopAction" = None, AbstractBranchTransition: "AbstractBranchTransition" = None, AbstractAction476: set["AbstractAction"] = None):
        self.AbstractLoopAction = AbstractLoopAction
        self.AbstractBranchTransition = AbstractBranchTransition
        self.AbstractAction476 = AbstractAction476 if AbstractAction476 is not None else set()
        
    @property
    def AbstractBranchTransition(self):
        return self.__AbstractBranchTransition

    @AbstractBranchTransition.setter
    def AbstractBranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_seff_pc_ResourceDemandingBehaviour__AbstractBranchTransition", None)
        self.__AbstractBranchTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc474"):
                opp_val = getattr(old_value, "seff_pc474", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc474", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc474"):
                opp_val = getattr(value, "seff_pc474", None)
                setattr(value, "seff_pc474", self)

    @property
    def AbstractAction476(self):
        return self.__AbstractAction476

    @AbstractAction476.setter
    def AbstractAction476(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_seff_pc_ResourceDemandingBehaviour__AbstractAction476", None)
        self.__AbstractAction476 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_pc477"):
                    opp_val = getattr(item, "seff_pc477", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_pc477", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_pc477"):
                    opp_val = getattr(item, "seff_pc477", None)
                    
                    setattr(item, "seff_pc477", self)
                    

    @property
    def AbstractLoopAction(self):
        return self.__AbstractLoopAction

    @AbstractLoopAction.setter
    def AbstractLoopAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_seff_pc_ResourceDemandingBehaviour__AbstractLoopAction", None)
        self.__AbstractLoopAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc472"):
                opp_val = getattr(old_value, "seff_pc472", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc472", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc472"):
                opp_val = getattr(value, "seff_pc472", None)
                setattr(value, "seff_pc472", self)

    def EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor method
        pass

    def ExactlyOneStopAction(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ExactlyOneStopAction method
        pass

    def ExactlyOneStartAction(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ExactlyOneStartAction method
        pass

class pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification(Identifier):

    def __init__(self, failureProbability: float, LinkingResource659: "LinkingResource" = None, pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification: "CommunicationLinkResourceType" = None, PCMRandomVariable664: "PCMRandomVariable" = None, PCMRandomVariable667: "PCMRandomVariable" = None):
        self.failureProbability = failureProbability
        self.LinkingResource659 = LinkingResource659
        self.pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification = pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification
        self.PCMRandomVariable664 = PCMRandomVariable664
        self.PCMRandomVariable667 = PCMRandomVariable667
        
    @property
    def failureProbability(self) -> float:
        return self.__failureProbability

    @failureProbability.setter
    def failureProbability(self, failureProbability: float):
        self.__failureProbability = failureProbability

    @property
    def LinkingResource659(self):
        return self.__LinkingResource659

    @LinkingResource659.setter
    def LinkingResource659(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification__LinkingResource659", None)
        self.__LinkingResource659 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_pc660"):
                opp_val = getattr(old_value, "resourceenvironment_pc660", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_pc660", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_pc660"):
                opp_val = getattr(value, "resourceenvironment_pc660", None)
                setattr(value, "resourceenvironment_pc660", self)

    @property
    def PCMRandomVariable667(self):
        return self.__PCMRandomVariable667

    @PCMRandomVariable667.setter
    def PCMRandomVariable667(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification__PCMRandomVariable667", None)
        self.__PCMRandomVariable667 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc668"):
                opp_val = getattr(old_value, "core_pc668", None)
                if opp_val == self:
                    setattr(old_value, "core_pc668", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc668"):
                opp_val = getattr(value, "core_pc668", None)
                setattr(value, "core_pc668", self)

    @property
    def pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification(self):
        return self.__pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification

    @pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification.setter
    def pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification__pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification", None)
        self.__pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CommunicationLinkResourceType662"):
                opp_val = getattr(old_value, "CommunicationLinkResourceType662", None)
                if opp_val == self:
                    setattr(old_value, "CommunicationLinkResourceType662", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CommunicationLinkResourceType662"):
                opp_val = getattr(value, "CommunicationLinkResourceType662", None)
                setattr(value, "CommunicationLinkResourceType662", self)

    @property
    def PCMRandomVariable664(self):
        return self.__PCMRandomVariable664

    @PCMRandomVariable664.setter
    def PCMRandomVariable664(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification__PCMRandomVariable664", None)
        self.__PCMRandomVariable664 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc665"):
                opp_val = getattr(old_value, "core_pc665", None)
                if opp_val == self:
                    setattr(old_value, "core_pc665", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc665"):
                opp_val = getattr(value, "core_pc665", None)
                setattr(value, "core_pc665", self)

class pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification(Identifier):

    def __init__(self, requiredByContainer: bool, numberOfReplicas: int, MTTR: float, MTTF: float, pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification: "SchedulingPolicy" = None, pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification650: "ProcessingResourceType" = None, PCMRandomVariable653: "PCMRandomVariable" = None, ResourceContainer656: "ResourceContainer" = None):
        self.requiredByContainer = requiredByContainer
        self.numberOfReplicas = numberOfReplicas
        self.MTTR = MTTR
        self.MTTF = MTTF
        self.pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification = pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification
        self.pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification650 = pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification650
        self.PCMRandomVariable653 = PCMRandomVariable653
        self.ResourceContainer656 = ResourceContainer656
        
    @property
    def MTTF(self) -> float:
        return self.__MTTF

    @MTTF.setter
    def MTTF(self, MTTF: float):
        self.__MTTF = MTTF

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
    def MTTR(self) -> float:
        return self.__MTTR

    @MTTR.setter
    def MTTR(self, MTTR: float):
        self.__MTTR = MTTR

    @property
    def PCMRandomVariable653(self):
        return self.__PCMRandomVariable653

    @PCMRandomVariable653.setter
    def PCMRandomVariable653(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification__PCMRandomVariable653", None)
        self.__PCMRandomVariable653 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc654"):
                opp_val = getattr(old_value, "core_pc654", None)
                if opp_val == self:
                    setattr(old_value, "core_pc654", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc654"):
                opp_val = getattr(value, "core_pc654", None)
                setattr(value, "core_pc654", self)

    @property
    def pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification(self):
        return self.__pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification

    @pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification.setter
    def pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification__pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification", None)
        self.__pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SchedulingPolicy648"):
                opp_val = getattr(old_value, "SchedulingPolicy648", None)
                if opp_val == self:
                    setattr(old_value, "SchedulingPolicy648", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SchedulingPolicy648"):
                opp_val = getattr(value, "SchedulingPolicy648", None)
                setattr(value, "SchedulingPolicy648", self)

    @property
    def pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification650(self):
        return self.__pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification650

    @pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification650.setter
    def pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification650(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification__pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification650", None)
        self.__pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification650 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcessingResourceType651"):
                opp_val = getattr(old_value, "ProcessingResourceType651", None)
                if opp_val == self:
                    setattr(old_value, "ProcessingResourceType651", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessingResourceType651"):
                opp_val = getattr(value, "ProcessingResourceType651", None)
                setattr(value, "ProcessingResourceType651", self)

    @property
    def ResourceContainer656(self):
        return self.__ResourceContainer656

    @ResourceContainer656.setter
    def ResourceContainer656(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification__ResourceContainer656", None)
        self.__ResourceContainer656 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_pc657"):
                opp_val = getattr(old_value, "resourceenvironment_pc657", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_pc657", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_pc657"):
                opp_val = getattr(value, "resourceenvironment_pc657", None)
                setattr(value, "resourceenvironment_pc657", self)

class pcm_pc_entity_pc_Entity(entity_pc_NamedElement, Identifier):

    pass
class pcm_pc_entity_pc_NamedElement:

    def __init__(self, entityName: str):
        self.entityName = entityName
        
    @property
    def entityName(self) -> str:
        return self.__entityName

    @entityName.setter
    def entityName(self, entityName: str):
        self.__entityName = entityName

class entity_pc_InterfaceProvidingRequiringEntity:

    pass
class composition_pc_ComposedStructure:

    pass
class pcm_pc_entity_pc_ComposedProvidingRequiringEntity(composition_pc_ComposedStructure, entity_pc_InterfaceProvidingRequiringEntity):

    def __init__(self, core_pc52: "pcm_pc_composition_pc_Connector", core_pc187: "pcm_pc_composition_pc_AssemblyContext", core_pc71: "pcm_pc_composition_pc_ResourceRequiredDelegationConnector", core_pc81: "pcm_pc_composition_pc_EventChannel"):
        
    def ProvidedRolesMustBeBound(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ProvidedRolesMustBeBound method
        pass

class entity_pc_ResourceProvidedRole:

    pass
class RequiredRole:

    pass
class pcm_pc_repository_pc_InfrastructureRequiredRole(RequiredRole):

    pass
class pcm_pc_repository_pc_OperationRequiredRole(RequiredRole):

    pass
class pcm_pc_repository_pc_SourceRole(RequiredRole):

    pass
class entity_pc_ResourceInterfaceRequiringEntity:

    pass
class entity_pc_Entity:

    pass
class pcm_pc_repository_pc_CollectionDataType(repository_pc_DataType, entity_pc_Entity):

    pass
class pcm_pc_system_pc_System(entity_pc_ComposedProvidingRequiringEntity, entity_pc_Entity):

    def __init__(self, QoSAnnotations622: set["QoSAnnotations"] = None):
        self.QoSAnnotations622 = QoSAnnotations622 if QoSAnnotations622 is not None else set()
        
    @property
    def QoSAnnotations622(self):
        return self.__QoSAnnotations622

    @QoSAnnotations622.setter
    def QoSAnnotations622(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_system_pc_System__QoSAnnotations622", None)
        self.__QoSAnnotations622 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qosannotations_pc623"):
                    opp_val = getattr(item, "qosannotations_pc623", None)
                    
                    if opp_val == self:
                        setattr(item, "qosannotations_pc623", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qosannotations_pc623"):
                    opp_val = getattr(item, "qosannotations_pc623", None)
                    
                    setattr(item, "qosannotations_pc623", self)
                    

    def SystemMustHaveAtLeastOneProvidedRole(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SystemMustHaveAtLeastOneProvidedRole method
        pass

class pcm_pc_repository_pc_CompositeDataType(repository_pc_DataType, entity_pc_Entity):

    pass
class pcm_pc_entity_pc_InterfaceRequiringEntity(entity_pc_Entity, entity_pc_ResourceInterfaceRequiringEntity):

    pass
class ProvidedRole:

    pass
class pcm_pc_repository_pc_OperationProvidedRole(ProvidedRole):

    pass
class pcm_pc_repository_pc_InfrastructureProvidedRole(ProvidedRole):

    pass
class pcm_pc_repository_pc_SinkRole(ProvidedRole):

    pass
class Entity:

    pass
class pcm_pc_composition_pc_ComposedStructure(Entity):

    def __init__(self, composition_pc54: set["composition_pc_AssemblyContext"] = None, composition_pc57: set["composition_pc_ResourceRequiredDelegationConnector"] = None, composition_pc60: set["composition_pc_EventChannel"] = None, composition_pc63: set["composition_pc_Connector"] = None):
        self.composition_pc54 = composition_pc54 if composition_pc54 is not None else set()
        self.composition_pc57 = composition_pc57 if composition_pc57 is not None else set()
        self.composition_pc60 = composition_pc60 if composition_pc60 is not None else set()
        self.composition_pc63 = composition_pc63 if composition_pc63 is not None else set()
        
    @property
    def composition_pc57(self):
        return self.__composition_pc57

    @composition_pc57.setter
    def composition_pc57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_composition_pc_ComposedStructure__composition_pc57", None)
        self.__composition_pc57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_pc58"):
                    opp_val = getattr(item, "core_pc58", None)
                    
                    if opp_val == self:
                        setattr(item, "core_pc58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_pc58"):
                    opp_val = getattr(item, "core_pc58", None)
                    
                    setattr(item, "core_pc58", self)
                    

    @property
    def composition_pc63(self):
        return self.__composition_pc63

    @composition_pc63.setter
    def composition_pc63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_composition_pc_ComposedStructure__composition_pc63", None)
        self.__composition_pc63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_pc64"):
                    opp_val = getattr(item, "core_pc64", None)
                    
                    if opp_val == self:
                        setattr(item, "core_pc64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_pc64"):
                    opp_val = getattr(item, "core_pc64", None)
                    
                    setattr(item, "core_pc64", self)
                    

    @property
    def composition_pc54(self):
        return self.__composition_pc54

    @composition_pc54.setter
    def composition_pc54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_composition_pc_ComposedStructure__composition_pc54", None)
        self.__composition_pc54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_pc55"):
                    opp_val = getattr(item, "core_pc55", None)
                    
                    if opp_val == self:
                        setattr(item, "core_pc55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_pc55"):
                    opp_val = getattr(item, "core_pc55", None)
                    
                    setattr(item, "core_pc55", self)
                    

    @property
    def composition_pc60(self):
        return self.__composition_pc60

    @composition_pc60.setter
    def composition_pc60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_composition_pc_ComposedStructure__composition_pc60", None)
        self.__composition_pc60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_pc61"):
                    opp_val = getattr(item, "core_pc61", None)
                    
                    if opp_val == self:
                        setattr(item, "core_pc61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_pc61"):
                    opp_val = getattr(item, "core_pc61", None)
                    
                    setattr(item, "core_pc61", self)
                    

    def MultipleConnectorsConstraint(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MultipleConnectorsConstraint method
        pass

    def MultipleConnectorsConstraintForAssemblyConnectors(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MultipleConnectorsConstraintForAssemblyConnectors method
        pass

class pcm_pc_seff_pc_AbstractBranchTransition(Entity):

    pass
class pcm_pc_repository_pc_Signature(Entity):

    pass
class pcm_pc_repository_pc_Interface(Entity):

    def __init__(self, pcm_pc_repository_pc_Interface309: set["Protocol"] = None, RequiredCharacterisation: set["RequiredCharacterisation"] = None, Repository313: "Repository" = None, pcm_pc_repository_pc_Interface: set["Interface"] = None):
        self.pcm_pc_repository_pc_Interface309 = pcm_pc_repository_pc_Interface309 if pcm_pc_repository_pc_Interface309 is not None else set()
        self.RequiredCharacterisation = RequiredCharacterisation if RequiredCharacterisation is not None else set()
        self.Repository313 = Repository313
        self.pcm_pc_repository_pc_Interface = pcm_pc_repository_pc_Interface if pcm_pc_repository_pc_Interface is not None else set()
        
    @property
    def pcm_pc_repository_pc_Interface(self):
        return self.__pcm_pc_repository_pc_Interface

    @pcm_pc_repository_pc_Interface.setter
    def pcm_pc_repository_pc_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_repository_pc_Interface__pcm_pc_repository_pc_Interface", None)
        self.__pcm_pc_repository_pc_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Interface307"):
                    opp_val = getattr(item, "Interface307", None)
                    
                    if opp_val == self:
                        setattr(item, "Interface307", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Interface307"):
                    opp_val = getattr(item, "Interface307", None)
                    
                    setattr(item, "Interface307", self)
                    

    @property
    def Repository313(self):
        return self.__Repository313

    @Repository313.setter
    def Repository313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_repository_pc_Interface__Repository313", None)
        self.__Repository313 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc314"):
                opp_val = getattr(old_value, "repository_pc314", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc314", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc314"):
                opp_val = getattr(value, "repository_pc314", None)
                setattr(value, "repository_pc314", self)

    @property
    def pcm_pc_repository_pc_Interface309(self):
        return self.__pcm_pc_repository_pc_Interface309

    @pcm_pc_repository_pc_Interface309.setter
    def pcm_pc_repository_pc_Interface309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_repository_pc_Interface__pcm_pc_repository_pc_Interface309", None)
        self.__pcm_pc_repository_pc_Interface309 = value if value is not None else set()
        
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
    def RequiredCharacterisation(self):
        return self.__RequiredCharacterisation

    @RequiredCharacterisation.setter
    def RequiredCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_repository_pc_Interface__RequiredCharacterisation", None)
        self.__RequiredCharacterisation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_pc311"):
                    opp_val = getattr(item, "repository_pc311", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_pc311", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_pc311"):
                    opp_val = getattr(item, "repository_pc311", None)
                    
                    setattr(item, "repository_pc311", self)
                    

    def NoProtocolTypeIDUsedTwice(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NoProtocolTypeIDUsedTwice method
        pass

class pcm_pc_resourceenvironment_pc_ResourceContainer(Entity):

    pass
class pcm_pc_repository_pc_Role(Entity):

    pass
class pcm_pc_composition_pc_EventChannel(Entity):

    pass
class pcm_pc_usagemodel_pc_AbstractUserAction(Entity):

    pass
class pcm_pc_repository_pc_PassiveResource(Entity):

    pass
class pcm_pc_resourceenvironment_pc_LinkingResource(Entity):

    pass
class pcm_pc_allocation_pc_Allocation(Entity):

    def __init__(self, pcm_pc_allocation_pc_Allocation: "ResourceEnvironment" = None, pcm_pc_allocation_pc_Allocation680: "System" = None, AllocationContext: set["AllocationContext"] = None):
        self.pcm_pc_allocation_pc_Allocation = pcm_pc_allocation_pc_Allocation
        self.pcm_pc_allocation_pc_Allocation680 = pcm_pc_allocation_pc_Allocation680
        self.AllocationContext = AllocationContext if AllocationContext is not None else set()
        
    @property
    def pcm_pc_allocation_pc_Allocation(self):
        return self.__pcm_pc_allocation_pc_Allocation

    @pcm_pc_allocation_pc_Allocation.setter
    def pcm_pc_allocation_pc_Allocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_allocation_pc_Allocation__pcm_pc_allocation_pc_Allocation", None)
        self.__pcm_pc_allocation_pc_Allocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceEnvironment678"):
                opp_val = getattr(old_value, "ResourceEnvironment678", None)
                if opp_val == self:
                    setattr(old_value, "ResourceEnvironment678", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceEnvironment678"):
                opp_val = getattr(value, "ResourceEnvironment678", None)
                setattr(value, "ResourceEnvironment678", self)

    @property
    def pcm_pc_allocation_pc_Allocation680(self):
        return self.__pcm_pc_allocation_pc_Allocation680

    @pcm_pc_allocation_pc_Allocation680.setter
    def pcm_pc_allocation_pc_Allocation680(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_allocation_pc_Allocation__pcm_pc_allocation_pc_Allocation680", None)
        self.__pcm_pc_allocation_pc_Allocation680 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "System681"):
                opp_val = getattr(old_value, "System681", None)
                if opp_val == self:
                    setattr(old_value, "System681", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "System681"):
                opp_val = getattr(value, "System681", None)
                setattr(value, "System681", self)

    @property
    def AllocationContext(self):
        return self.__AllocationContext

    @AllocationContext.setter
    def AllocationContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_allocation_pc_Allocation__AllocationContext", None)
        self.__AllocationContext = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "allocation_pc683"):
                    opp_val = getattr(item, "allocation_pc683", None)
                    
                    if opp_val == self:
                        setattr(item, "allocation_pc683", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "allocation_pc683"):
                    opp_val = getattr(item, "allocation_pc683", None)
                    
                    setattr(item, "allocation_pc683", self)
                    

    def CommunicatingServersHaveToBeConnectedByLinkingResource(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement CommunicatingServersHaveToBeConnectedByLinkingResource method
        pass

    def EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce method
        pass

class pcm_pc_reliability_pc_FailureType(Entity):

    pass
class pcm_pc_composition_pc_AssemblyContext(Entity):

    pass
class pcm_pc_composition_pc_Connector(Entity):

    pass
class pcm_pc_usagemodel_pc_UsageScenario(Entity):

    pass
class pcm_pc_qosannotations_pc_QoSAnnotations(Entity):

    def __init__(self, SpecifiedOutputParameterAbstraction598: set["SpecifiedOutputParameterAbstraction"] = None, System: "System" = None, SpecifiedQoSAnnotation: set["SpecifiedQoSAnnotation"] = None):
        self.SpecifiedOutputParameterAbstraction598 = SpecifiedOutputParameterAbstraction598 if SpecifiedOutputParameterAbstraction598 is not None else set()
        self.System = System
        self.SpecifiedQoSAnnotation = SpecifiedQoSAnnotation if SpecifiedQoSAnnotation is not None else set()
        
    @property
    def System(self):
        return self.__System

    @System.setter
    def System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_qosannotations_pc_QoSAnnotations__System", None)
        self.__System = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system_pc"):
                opp_val = getattr(old_value, "system_pc", None)
                if opp_val == self:
                    setattr(old_value, "system_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system_pc"):
                opp_val = getattr(value, "system_pc", None)
                setattr(value, "system_pc", self)

    @property
    def SpecifiedOutputParameterAbstraction598(self):
        return self.__SpecifiedOutputParameterAbstraction598

    @SpecifiedOutputParameterAbstraction598.setter
    def SpecifiedOutputParameterAbstraction598(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_qosannotations_pc_QoSAnnotations__SpecifiedOutputParameterAbstraction598", None)
        self.__SpecifiedOutputParameterAbstraction598 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qosannotations_pc599"):
                    opp_val = getattr(item, "qosannotations_pc599", None)
                    
                    if opp_val == self:
                        setattr(item, "qosannotations_pc599", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qosannotations_pc599"):
                    opp_val = getattr(item, "qosannotations_pc599", None)
                    
                    setattr(item, "qosannotations_pc599", self)
                    

    @property
    def SpecifiedQoSAnnotation(self):
        return self.__SpecifiedQoSAnnotation

    @SpecifiedQoSAnnotation.setter
    def SpecifiedQoSAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_qosannotations_pc_QoSAnnotations__SpecifiedQoSAnnotation", None)
        self.__SpecifiedQoSAnnotation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qosannotations_pc602"):
                    opp_val = getattr(item, "qosannotations_pc602", None)
                    
                    if opp_val == self:
                        setattr(item, "qosannotations_pc602", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qosannotations_pc602"):
                    opp_val = getattr(item, "qosannotations_pc602", None)
                    
                    setattr(item, "qosannotations_pc602", self)
                    

    def MultipleReliabilityAnnotationsPerExternalCallNotAllowed(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MultipleReliabilityAnnotationsPerExternalCallNotAllowed method
        pass

class pcm_pc_resourcetype_pc_ResourceSignature(Entity):

    def __init__(self, resourceServiceId: int, ResourceInterface380: "ResourceInterface" = None, Parameter377: "Parameter" = None):
        self.resourceServiceId = resourceServiceId
        self.ResourceInterface380 = ResourceInterface380
        self.Parameter377 = Parameter377
        
    @property
    def resourceServiceId(self) -> int:
        return self.__resourceServiceId

    @resourceServiceId.setter
    def resourceServiceId(self, resourceServiceId: int):
        self.__resourceServiceId = resourceServiceId

    @property
    def Parameter377(self):
        return self.__Parameter377

    @Parameter377.setter
    def Parameter377(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_resourcetype_pc_ResourceSignature__Parameter377", None)
        self.__Parameter377 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc378"):
                opp_val = getattr(old_value, "repository_pc378", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc378", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc378"):
                opp_val = getattr(value, "repository_pc378", None)
                setattr(value, "repository_pc378", self)

    @property
    def ResourceInterface380(self):
        return self.__ResourceInterface380

    @ResourceInterface380.setter
    def ResourceInterface380(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_resourcetype_pc_ResourceSignature__ResourceInterface380", None)
        self.__ResourceInterface380 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcetype_pc381"):
                opp_val = getattr(old_value, "resourcetype_pc381", None)
                if opp_val == self:
                    setattr(old_value, "resourcetype_pc381", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcetype_pc381"):
                opp_val = getattr(value, "resourcetype_pc381", None)
                setattr(value, "resourcetype_pc381", self)

class pcm_pc_usagemodel_pc_ScenarioBehaviour(Entity):

    def __init__(self, UsageScenario231: "UsageScenario" = None, BranchTransition: "BranchTransition" = None, Loop236: "Loop" = None, AbstractUserAction239: set["AbstractUserAction"] = None):
        self.UsageScenario231 = UsageScenario231
        self.BranchTransition = BranchTransition
        self.Loop236 = Loop236
        self.AbstractUserAction239 = AbstractUserAction239 if AbstractUserAction239 is not None else set()
        
    @property
    def Loop236(self):
        return self.__Loop236

    @Loop236.setter
    def Loop236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_usagemodel_pc_ScenarioBehaviour__Loop236", None)
        self.__Loop236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc237"):
                opp_val = getattr(old_value, "usagemodel_pc237", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc237"):
                opp_val = getattr(value, "usagemodel_pc237", None)
                setattr(value, "usagemodel_pc237", self)

    @property
    def UsageScenario231(self):
        return self.__UsageScenario231

    @UsageScenario231.setter
    def UsageScenario231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_usagemodel_pc_ScenarioBehaviour__UsageScenario231", None)
        self.__UsageScenario231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc232"):
                opp_val = getattr(old_value, "usagemodel_pc232", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc232", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc232"):
                opp_val = getattr(value, "usagemodel_pc232", None)
                setattr(value, "usagemodel_pc232", self)

    @property
    def AbstractUserAction239(self):
        return self.__AbstractUserAction239

    @AbstractUserAction239.setter
    def AbstractUserAction239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_usagemodel_pc_ScenarioBehaviour__AbstractUserAction239", None)
        self.__AbstractUserAction239 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "usagemodel_pc240"):
                    opp_val = getattr(item, "usagemodel_pc240", None)
                    
                    if opp_val == self:
                        setattr(item, "usagemodel_pc240", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "usagemodel_pc240"):
                    opp_val = getattr(item, "usagemodel_pc240", None)
                    
                    setattr(item, "usagemodel_pc240", self)
                    

    @property
    def BranchTransition(self):
        return self.__BranchTransition

    @BranchTransition.setter
    def BranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_usagemodel_pc_ScenarioBehaviour__BranchTransition", None)
        self.__BranchTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc234"):
                opp_val = getattr(old_value, "usagemodel_pc234", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc234"):
                opp_val = getattr(value, "usagemodel_pc234", None)
                setattr(value, "usagemodel_pc234", self)

    def EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor method
        pass

    def Exactlyonestart(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement Exactlyonestart method
        pass

    def Exactlyonestop(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement Exactlyonestop method
        pass

class pcm_pc_allocation_pc_AllocationContext(Entity):

    def __init__(self, pcm_pc_allocation_pc_AllocationContext676: "composition_pc_EventChannel" = None, pcm_pc_allocation_pc_AllocationContext: "ResourceContainer" = None, pcm_pc_allocation_pc_AllocationContext672: "composition_pc_AssemblyContext" = None, Allocation: "Allocation" = None):
        self.pcm_pc_allocation_pc_AllocationContext676 = pcm_pc_allocation_pc_AllocationContext676
        self.pcm_pc_allocation_pc_AllocationContext = pcm_pc_allocation_pc_AllocationContext
        self.pcm_pc_allocation_pc_AllocationContext672 = pcm_pc_allocation_pc_AllocationContext672
        self.Allocation = Allocation
        
    @property
    def pcm_pc_allocation_pc_AllocationContext676(self):
        return self.__pcm_pc_allocation_pc_AllocationContext676

    @pcm_pc_allocation_pc_AllocationContext676.setter
    def pcm_pc_allocation_pc_AllocationContext676(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_allocation_pc_AllocationContext__pcm_pc_allocation_pc_AllocationContext676", None)
        self.__pcm_pc_allocation_pc_AllocationContext676 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_pc_EventChannel"):
                opp_val = getattr(old_value, "composition_pc_EventChannel", None)
                if opp_val == self:
                    setattr(old_value, "composition_pc_EventChannel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_pc_EventChannel"):
                opp_val = getattr(value, "composition_pc_EventChannel", None)
                setattr(value, "composition_pc_EventChannel", self)

    @property
    def Allocation(self):
        return self.__Allocation

    @Allocation.setter
    def Allocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_allocation_pc_AllocationContext__Allocation", None)
        self.__Allocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "allocation_pc"):
                opp_val = getattr(old_value, "allocation_pc", None)
                if opp_val == self:
                    setattr(old_value, "allocation_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "allocation_pc"):
                opp_val = getattr(value, "allocation_pc", None)
                setattr(value, "allocation_pc", self)

    @property
    def pcm_pc_allocation_pc_AllocationContext(self):
        return self.__pcm_pc_allocation_pc_AllocationContext

    @pcm_pc_allocation_pc_AllocationContext.setter
    def pcm_pc_allocation_pc_AllocationContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_allocation_pc_AllocationContext__pcm_pc_allocation_pc_AllocationContext", None)
        self.__pcm_pc_allocation_pc_AllocationContext = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceContainer670"):
                opp_val = getattr(old_value, "ResourceContainer670", None)
                if opp_val == self:
                    setattr(old_value, "ResourceContainer670", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceContainer670"):
                opp_val = getattr(value, "ResourceContainer670", None)
                setattr(value, "ResourceContainer670", self)

    @property
    def pcm_pc_allocation_pc_AllocationContext672(self):
        return self.__pcm_pc_allocation_pc_AllocationContext672

    @pcm_pc_allocation_pc_AllocationContext672.setter
    def pcm_pc_allocation_pc_AllocationContext672(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_allocation_pc_AllocationContext__pcm_pc_allocation_pc_AllocationContext672", None)
        self.__pcm_pc_allocation_pc_AllocationContext672 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_pc_AssemblyContext673"):
                opp_val = getattr(old_value, "composition_pc_AssemblyContext673", None)
                if opp_val == self:
                    setattr(old_value, "composition_pc_AssemblyContext673", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_pc_AssemblyContext673"):
                opp_val = getattr(value, "composition_pc_AssemblyContext673", None)
                setattr(value, "composition_pc_AssemblyContext673", self)

    def OneAssemblyContextOrOneEventChannelShouldBeReferred(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement OneAssemblyContextOrOneEventChannelShouldBeReferred method
        pass

class pcm_pc_seff_reliability_pc_FailureHandlingEntity(Entity):

    pass
class pcm_pc_resourcetype_pc_ResourceInterface(Entity):

    pass
class pcm_pc_repository_pc_Repository(Entity):

    def __init__(self, repositoryDescription: str, RepositoryComponent297: set["RepositoryComponent"] = None, Interface: set["Interface"] = None, FailureType: set["FailureType"] = None, DataType304: set["DataType"] = None):
        self.repositoryDescription = repositoryDescription
        self.RepositoryComponent297 = RepositoryComponent297 if RepositoryComponent297 is not None else set()
        self.Interface = Interface if Interface is not None else set()
        self.FailureType = FailureType if FailureType is not None else set()
        self.DataType304 = DataType304 if DataType304 is not None else set()
        
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
        old_value = getattr(self, f"_pcm_pc_repository_pc_Repository__FailureType", None)
        self.__FailureType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reliability_pc302"):
                    opp_val = getattr(item, "reliability_pc302", None)
                    
                    if opp_val == self:
                        setattr(item, "reliability_pc302", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reliability_pc302"):
                    opp_val = getattr(item, "reliability_pc302", None)
                    
                    setattr(item, "reliability_pc302", self)
                    

    @property
    def RepositoryComponent297(self):
        return self.__RepositoryComponent297

    @RepositoryComponent297.setter
    def RepositoryComponent297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_repository_pc_Repository__RepositoryComponent297", None)
        self.__RepositoryComponent297 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_pc298"):
                    opp_val = getattr(item, "repository_pc298", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_pc298", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_pc298"):
                    opp_val = getattr(item, "repository_pc298", None)
                    
                    setattr(item, "repository_pc298", self)
                    

    @property
    def Interface(self):
        return self.__Interface

    @Interface.setter
    def Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_repository_pc_Repository__Interface", None)
        self.__Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_pc300"):
                    opp_val = getattr(item, "repository_pc300", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_pc300", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_pc300"):
                    opp_val = getattr(item, "repository_pc300", None)
                    
                    setattr(item, "repository_pc300", self)
                    

    @property
    def DataType304(self):
        return self.__DataType304

    @DataType304.setter
    def DataType304(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_repository_pc_Repository__DataType304", None)
        self.__DataType304 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_pc305"):
                    opp_val = getattr(item, "repository_pc305", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_pc305", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_pc305"):
                    opp_val = getattr(item, "repository_pc305", None)
                    
                    setattr(item, "repository_pc305", self)
                    

class pcm_pc_resourcetype_pc_SchedulingPolicy(Entity):

    pass
class pcm_pc_entity_pc_ResourceInterfaceProvidingEntity(Entity):

    pass
class pcm_pc_seff_pc_AbstractAction(Entity):

    pass
class pcm_pc_entity_pc_InterfaceProvidingEntity(Entity):

    pass
class entity_pc_InterfaceRequiringEntity:

    pass
class entity_pc_InterfaceProvidingEntity:

    pass
class pcm_pc_entity_pc_InterfaceProvidingRequiringEntity(entity_pc_InterfaceRequiringEntity, entity_pc_InterfaceProvidingEntity):

    pass
class ResourceInterface:

    pass
class entity_pc_ResourceInterfaceProvidingEntity:

    pass
class pcm_pc_entity_pc_ResourceInterfaceProvidingRequiringEntity(entity_pc_ResourceInterfaceProvidingEntity, entity_pc_ResourceInterfaceRequiringEntity):

    pass
class pcm_pc_resourcetype_pc_ResourceType(entity_pc_ResourceInterfaceProvidingEntity, entity_pc_Entity, UnitCarryingElement):

    pass
class Role:

    pass
class pcm_pc_repository_pc_ProvidedRole(Role):

    pass
class pcm_pc_repository_pc_RequiredRole(Role):

    pass
class pcm_pc_entity_pc_ResourceProvidedRole(Role):

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
class pcm_pc_entity_pc_ResourceRequiredRole(Role):

    pass
class entity_pc_ResourceRequiredRole:

    pass
class pcm_pc_entity_pc_ResourceInterfaceRequiringEntity(Entity):

    pass
class composition_pc_EventChannelSinkConnector:

    pass
class qos_performance_pc_SpecifiedExecutionTime:

    pass
class GuardedBranchTransition:

    pass
class LoopAction:

    pass
class seff_performance_pc_ParametricResourceDemand:

    pass
class seff_performance_pc_ResourceCall:

    pass
class seff_performance_pc_InfrastructureCall:

    pass
class VariableCharacterisation:

    pass
class PassiveResource:

    pass
class ClosedWorkload:

    pass
class composition_pc_AssemblyEventConnector:

    pass
class RandomVariable:

    pass
class pcm_pc_core_pc_PCMRandomVariable(RandomVariable):

    def __init__(self, composition_pc: "composition_pc_EventChannelSinkConnector" = None, composition_pc18: "composition_pc_AssemblyEventConnector" = None, ClosedWorkload: "ClosedWorkload" = None, PassiveResource: "PassiveResource" = None, VariableCharacterisation: "VariableCharacterisation" = None, seff_performance_pc: "seff_performance_pc_InfrastructureCall" = None, seff_performance_pc6: "seff_performance_pc_ResourceCall" = None, seff_performance_pc9: "seff_performance_pc_ParametricResourceDemand" = None, LoopAction: "LoopAction" = None, GuardedBranchTransition: "GuardedBranchTransition" = None, qos_performance_pc: "qos_performance_pc_SpecifiedExecutionTime" = None, Loop: "Loop" = None, OpenWorkload: "OpenWorkload" = None, Delay: "Delay" = None, CommunicationLinkResourceSpecification: "CommunicationLinkResourceSpecification" = None, ProcessingResourceSpecification: "ProcessingResourceSpecification" = None, CommunicationLinkResourceSpecification30: "CommunicationLinkResourceSpecification" = None):
        self.composition_pc = composition_pc
        self.composition_pc18 = composition_pc18
        self.ClosedWorkload = ClosedWorkload
        self.PassiveResource = PassiveResource
        self.VariableCharacterisation = VariableCharacterisation
        self.seff_performance_pc = seff_performance_pc
        self.seff_performance_pc6 = seff_performance_pc6
        self.seff_performance_pc9 = seff_performance_pc9
        self.LoopAction = LoopAction
        self.GuardedBranchTransition = GuardedBranchTransition
        self.qos_performance_pc = qos_performance_pc
        self.Loop = Loop
        self.OpenWorkload = OpenWorkload
        self.Delay = Delay
        self.CommunicationLinkResourceSpecification = CommunicationLinkResourceSpecification
        self.ProcessingResourceSpecification = ProcessingResourceSpecification
        self.CommunicationLinkResourceSpecification30 = CommunicationLinkResourceSpecification30
        
    @property
    def ClosedWorkload(self):
        return self.__ClosedWorkload

    @ClosedWorkload.setter
    def ClosedWorkload(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_core_pc_PCMRandomVariable__ClosedWorkload", None)
        self.__ClosedWorkload = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc"):
                opp_val = getattr(old_value, "usagemodel_pc", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc"):
                opp_val = getattr(value, "usagemodel_pc", None)
                setattr(value, "usagemodel_pc", self)

    @property
    def seff_performance_pc6(self):
        return self.__seff_performance_pc6

    @seff_performance_pc6.setter
    def seff_performance_pc6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_core_pc_PCMRandomVariable__seff_performance_pc6", None)
        self.__seff_performance_pc6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc7"):
                opp_val = getattr(old_value, "seff_pc7", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc7"):
                opp_val = getattr(value, "seff_pc7", None)
                setattr(value, "seff_pc7", self)

    @property
    def CommunicationLinkResourceSpecification30(self):
        return self.__CommunicationLinkResourceSpecification30

    @CommunicationLinkResourceSpecification30.setter
    def CommunicationLinkResourceSpecification30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_core_pc_PCMRandomVariable__CommunicationLinkResourceSpecification30", None)
        self.__CommunicationLinkResourceSpecification30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_pc31"):
                opp_val = getattr(old_value, "resourceenvironment_pc31", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_pc31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_pc31"):
                opp_val = getattr(value, "resourceenvironment_pc31", None)
                setattr(value, "resourceenvironment_pc31", self)

    @property
    def composition_pc(self):
        return self.__composition_pc

    @composition_pc.setter
    def composition_pc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_core_pc_PCMRandomVariable__composition_pc", None)
        self.__composition_pc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc"):
                opp_val = getattr(old_value, "core_pc", None)
                if opp_val == self:
                    setattr(old_value, "core_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc"):
                opp_val = getattr(value, "core_pc", None)
                setattr(value, "core_pc", self)

    @property
    def PassiveResource(self):
        return self.__PassiveResource

    @PassiveResource.setter
    def PassiveResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_core_pc_PCMRandomVariable__PassiveResource", None)
        self.__PassiveResource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc"):
                opp_val = getattr(old_value, "repository_pc", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc"):
                opp_val = getattr(value, "repository_pc", None)
                setattr(value, "repository_pc", self)

    @property
    def LoopAction(self):
        return self.__LoopAction

    @LoopAction.setter
    def LoopAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_core_pc_PCMRandomVariable__LoopAction", None)
        self.__LoopAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc12"):
                opp_val = getattr(old_value, "seff_pc12", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc12"):
                opp_val = getattr(value, "seff_pc12", None)
                setattr(value, "seff_pc12", self)

    @property
    def seff_performance_pc(self):
        return self.__seff_performance_pc

    @seff_performance_pc.setter
    def seff_performance_pc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_core_pc_PCMRandomVariable__seff_performance_pc", None)
        self.__seff_performance_pc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc"):
                opp_val = getattr(old_value, "seff_pc", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc"):
                opp_val = getattr(value, "seff_pc", None)
                setattr(value, "seff_pc", self)

    @property
    def seff_performance_pc9(self):
        return self.__seff_performance_pc9

    @seff_performance_pc9.setter
    def seff_performance_pc9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_core_pc_PCMRandomVariable__seff_performance_pc9", None)
        self.__seff_performance_pc9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc10"):
                opp_val = getattr(old_value, "seff_pc10", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc10"):
                opp_val = getattr(value, "seff_pc10", None)
                setattr(value, "seff_pc10", self)

    @property
    def VariableCharacterisation(self):
        return self.__VariableCharacterisation

    @VariableCharacterisation.setter
    def VariableCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_core_pc_PCMRandomVariable__VariableCharacterisation", None)
        self.__VariableCharacterisation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameter_pc"):
                opp_val = getattr(old_value, "parameter_pc", None)
                if opp_val == self:
                    setattr(old_value, "parameter_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameter_pc"):
                opp_val = getattr(value, "parameter_pc", None)
                setattr(value, "parameter_pc", self)

    @property
    def ProcessingResourceSpecification(self):
        return self.__ProcessingResourceSpecification

    @ProcessingResourceSpecification.setter
    def ProcessingResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_core_pc_PCMRandomVariable__ProcessingResourceSpecification", None)
        self.__ProcessingResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_pc28"):
                opp_val = getattr(old_value, "resourceenvironment_pc28", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_pc28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_pc28"):
                opp_val = getattr(value, "resourceenvironment_pc28", None)
                setattr(value, "resourceenvironment_pc28", self)

    @property
    def qos_performance_pc(self):
        return self.__qos_performance_pc

    @qos_performance_pc.setter
    def qos_performance_pc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_core_pc_PCMRandomVariable__qos_performance_pc", None)
        self.__qos_performance_pc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qosannotations_pc"):
                opp_val = getattr(old_value, "qosannotations_pc", None)
                if opp_val == self:
                    setattr(old_value, "qosannotations_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qosannotations_pc"):
                opp_val = getattr(value, "qosannotations_pc", None)
                setattr(value, "qosannotations_pc", self)

    @property
    def Delay(self):
        return self.__Delay

    @Delay.setter
    def Delay(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_core_pc_PCMRandomVariable__Delay", None)
        self.__Delay = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc25"):
                opp_val = getattr(old_value, "usagemodel_pc25", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc25"):
                opp_val = getattr(value, "usagemodel_pc25", None)
                setattr(value, "usagemodel_pc25", self)

    @property
    def GuardedBranchTransition(self):
        return self.__GuardedBranchTransition

    @GuardedBranchTransition.setter
    def GuardedBranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_core_pc_PCMRandomVariable__GuardedBranchTransition", None)
        self.__GuardedBranchTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc14"):
                opp_val = getattr(old_value, "seff_pc14", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc14"):
                opp_val = getattr(value, "seff_pc14", None)
                setattr(value, "seff_pc14", self)

    @property
    def OpenWorkload(self):
        return self.__OpenWorkload

    @OpenWorkload.setter
    def OpenWorkload(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_core_pc_PCMRandomVariable__OpenWorkload", None)
        self.__OpenWorkload = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc23"):
                opp_val = getattr(old_value, "usagemodel_pc23", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc23"):
                opp_val = getattr(value, "usagemodel_pc23", None)
                setattr(value, "usagemodel_pc23", self)

    @property
    def CommunicationLinkResourceSpecification(self):
        return self.__CommunicationLinkResourceSpecification

    @CommunicationLinkResourceSpecification.setter
    def CommunicationLinkResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_core_pc_PCMRandomVariable__CommunicationLinkResourceSpecification", None)
        self.__CommunicationLinkResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_pc"):
                opp_val = getattr(old_value, "resourceenvironment_pc", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_pc"):
                opp_val = getattr(value, "resourceenvironment_pc", None)
                setattr(value, "resourceenvironment_pc", self)

    @property
    def Loop(self):
        return self.__Loop

    @Loop.setter
    def Loop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_core_pc_PCMRandomVariable__Loop", None)
        self.__Loop = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc21"):
                opp_val = getattr(old_value, "usagemodel_pc21", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc21"):
                opp_val = getattr(value, "usagemodel_pc21", None)
                setattr(value, "usagemodel_pc21", self)

    @property
    def composition_pc18(self):
        return self.__composition_pc18

    @composition_pc18.setter
    def composition_pc18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_core_pc_PCMRandomVariable__composition_pc18", None)
        self.__composition_pc18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc19"):
                opp_val = getattr(old_value, "core_pc19", None)
                if opp_val == self:
                    setattr(old_value, "core_pc19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc19"):
                opp_val = getattr(value, "core_pc19", None)
                setattr(value, "core_pc19", self)

    def SpecificationMustNotBeNULL(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SpecificationMustNotBeNULL method
        pass

class pcm_pc_EObject:

    pass
class pcm_pc_Pointcut:

    pass
class pcm_pc_DummyClass:

    pass