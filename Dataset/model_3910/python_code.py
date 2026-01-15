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
class ComponentType(Enum):
    BUSINESS_COMPONENT = "BUSINESS_COMPONENT"
    INFRASTRUCTURE_COMPONENT = "INFRASTRUCTURE_COMPONENT"
class VariableCharacterisationType(Enum):
    STRUCTURE = "STRUCTURE"
    NUMBER_OF_ELEMENTS = "NUMBER_OF_ELEMENTS"
    VALUE = "VALUE"
    BYTESIZE = "BYTESIZE"
    TYPE = "TYPE"
class ParameterModifier(Enum):
    none = "none"
    in = "in"
    out = "out"
    inout = "inout"


############################################
# Definition of Classes
############################################

class AllocationContext:

    pass
class ParametricResourceDemand:

    pass
class pcm_pc_pc_completions_pc_pc_NetworkDemandParametricResourceDemand(ParametricResourceDemand):

    pass
class ExternalCallAction:

    pass
class pcm_pc_pc_completions_pc_pc_DelegatingExternalCallAction(ExternalCallAction):

    pass
class Completion:

    pass
class pcm_pc_pc_completions_pc_pc_CompletionRepository:

    pass
class repository_pc_pc_RepositoryComponent:

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
class SpecifiedExecutionTime:

    pass
class pcm_pc_pc_qos_performance_pc_pc_SystemSpecifiedExecutionTime(SpecifiedExecutionTime):

    def __init__(self):
        
    def SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem method
        pass

class pcm_pc_pc_qosannotations_pc_pc_SpecifiedOutputParameterAbstraction:

    pass
class SpecifiedQoSAnnotation:

    pass
class System:

    pass
class pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation(SpecifiedQoSAnnotation):

    def __init__(self, ExternalFailureOccurrenceDescription: set["ExternalFailureOccurrenceDescription"] = None, qosannotations_pc_pc604: "pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations"):
        self.ExternalFailureOccurrenceDescription = ExternalFailureOccurrenceDescription if ExternalFailureOccurrenceDescription is not None else set()
        
    @property
    def ExternalFailureOccurrenceDescription(self):
        return self.__ExternalFailureOccurrenceDescription

    @ExternalFailureOccurrenceDescription.setter
    def ExternalFailureOccurrenceDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription", None)
        self.__ExternalFailureOccurrenceDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reliability_pc_pc622"):
                    opp_val = getattr(item, "reliability_pc_pc622", None)
                    
                    if opp_val == self:
                        setattr(item, "reliability_pc_pc622", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reliability_pc_pc622"):
                    opp_val = getattr(item, "reliability_pc_pc622", None)
                    
                    setattr(item, "reliability_pc_pc622", self)
                    

    def MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed method
        pass

    def SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1 method
        pass

    def SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem method
        pass

class pcm_pc_pc_qos_performance_pc_pc_ComponentSpecifiedExecutionTime(SpecifiedExecutionTime):

    pass
class pcm_pc_pc_qos_performance_pc_pc_SpecifiedExecutionTime(SpecifiedQoSAnnotation):

    pass
class seff_reliability_pc_pc_RecoveryAction:

    pass
class QoSAnnotations:

    pass
class pcm_pc_pc_qosannotations_pc_pc_SpecifiedQoSAnnotation:

    pass
class pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand:

    def __init__(self, PCMRandomVariable576: "PCMRandomVariable" = None, pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand: "ProcessingResourceType" = None, AbstractInternalControlFlowAction581: "AbstractInternalControlFlowAction" = None):
        self.PCMRandomVariable576 = PCMRandomVariable576
        self.pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand = pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand
        self.AbstractInternalControlFlowAction581 = AbstractInternalControlFlowAction581
        
    @property
    def pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand(self):
        return self.__pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand

    @pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand.setter
    def pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand__pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand", None)
        self.__pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcessingResourceType579"):
                opp_val = getattr(old_value, "ProcessingResourceType579", None)
                if opp_val == self:
                    setattr(old_value, "ProcessingResourceType579", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessingResourceType579"):
                opp_val = getattr(value, "ProcessingResourceType579", None)
                setattr(value, "ProcessingResourceType579", self)

    @property
    def PCMRandomVariable576(self):
        return self.__PCMRandomVariable576

    @PCMRandomVariable576.setter
    def PCMRandomVariable576(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand__PCMRandomVariable576", None)
        self.__PCMRandomVariable576 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc_pc577"):
                opp_val = getattr(old_value, "core_pc_pc577", None)
                if opp_val == self:
                    setattr(old_value, "core_pc_pc577", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc_pc577"):
                opp_val = getattr(value, "core_pc_pc577", None)
                setattr(value, "core_pc_pc577", self)

    @property
    def AbstractInternalControlFlowAction581(self):
        return self.__AbstractInternalControlFlowAction581

    @AbstractInternalControlFlowAction581.setter
    def AbstractInternalControlFlowAction581(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand__AbstractInternalControlFlowAction581", None)
        self.__AbstractInternalControlFlowAction581 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc_pc582"):
                opp_val = getattr(old_value, "seff_pc_pc582", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc_pc582", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc_pc582"):
                opp_val = getattr(value, "seff_pc_pc582", None)
                setattr(value, "seff_pc_pc582", self)

    def DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

class seff_reliability_pc_pc_RecoveryActionBehaviour:

    pass
class seff_pc_pc_AbstractInternalControlFlowAction:

    pass
class seff_pc_pc_CallAction:

    pass
class pcm_pc_pc_seff_pc_pc_InternalCallAction(seff_pc_pc_CallAction, seff_pc_pc_AbstractInternalControlFlowAction):

    pass
class pcm_pc_pc_seff_pc_pc_SynchronisationPoint:

    pass
class ForkAction:

    pass
class ForkedBehaviour:

    pass
class seff_reliability_pc_pc_FailureHandlingEntity:

    pass
class seff_pc_pc_CallReturnAction:

    pass
class seff_pc_pc_AbstractAction:

    pass
class pcm_pc_pc_seff_pc_pc_EmitEventAction(seff_pc_pc_CallAction, seff_pc_pc_AbstractAction):

    pass
class pcm_pc_pc_seff_pc_pc_ExternalCallAction(seff_pc_pc_CallReturnAction, seff_pc_pc_AbstractAction, seff_reliability_pc_pc_FailureHandlingEntity):

    def __init__(self, retryCount: int, pcm_pc_pc_seff_pc_pc_ExternalCallAction: "OperationSignature" = None, pcm_pc_pc_seff_pc_pc_ExternalCallAction529: "OperationRequiredRole" = None):
        self.retryCount = retryCount
        self.pcm_pc_pc_seff_pc_pc_ExternalCallAction = pcm_pc_pc_seff_pc_pc_ExternalCallAction
        self.pcm_pc_pc_seff_pc_pc_ExternalCallAction529 = pcm_pc_pc_seff_pc_pc_ExternalCallAction529
        
    @property
    def retryCount(self) -> int:
        return self.__retryCount

    @retryCount.setter
    def retryCount(self, retryCount: int):
        self.__retryCount = retryCount

    @property
    def pcm_pc_pc_seff_pc_pc_ExternalCallAction(self):
        return self.__pcm_pc_pc_seff_pc_pc_ExternalCallAction

    @pcm_pc_pc_seff_pc_pc_ExternalCallAction.setter
    def pcm_pc_pc_seff_pc_pc_ExternalCallAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_pc_pc_ExternalCallAction__pcm_pc_pc_seff_pc_pc_ExternalCallAction", None)
        self.__pcm_pc_pc_seff_pc_pc_ExternalCallAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationSignature527"):
                opp_val = getattr(old_value, "OperationSignature527", None)
                if opp_val == self:
                    setattr(old_value, "OperationSignature527", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationSignature527"):
                opp_val = getattr(value, "OperationSignature527", None)
                setattr(value, "OperationSignature527", self)

    @property
    def pcm_pc_pc_seff_pc_pc_ExternalCallAction529(self):
        return self.__pcm_pc_pc_seff_pc_pc_ExternalCallAction529

    @pcm_pc_pc_seff_pc_pc_ExternalCallAction529.setter
    def pcm_pc_pc_seff_pc_pc_ExternalCallAction529(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_pc_pc_ExternalCallAction__pcm_pc_pc_seff_pc_pc_ExternalCallAction529", None)
        self.__pcm_pc_pc_seff_pc_pc_ExternalCallAction529 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationRequiredRole530"):
                opp_val = getattr(old_value, "OperationRequiredRole530", None)
                if opp_val == self:
                    setattr(old_value, "OperationRequiredRole530", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationRequiredRole530"):
                opp_val = getattr(value, "OperationRequiredRole530", None)
                setattr(value, "OperationRequiredRole530", self)

    def OperationRequiredRoleMustBeReferencedByContainer(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement OperationRequiredRoleMustBeReferencedByContainer method
        pass

    def SignatureBelongsToRole(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SignatureBelongsToRole method
        pass

class pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification:

    def __init__(self, seffTypeID: str, pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification: "Signature" = None, BasicComponent496: "BasicComponent" = None):
        self.seffTypeID = seffTypeID
        self.pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification = pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification
        self.BasicComponent496 = BasicComponent496
        
    @property
    def seffTypeID(self) -> str:
        return self.__seffTypeID

    @seffTypeID.setter
    def seffTypeID(self, seffTypeID: str):
        self.__seffTypeID = seffTypeID

    @property
    def pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification(self):
        return self.__pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification

    @pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification.setter
    def pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification__pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification", None)
        self.__pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification = value
        
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
    def BasicComponent496(self):
        return self.__BasicComponent496

    @BasicComponent496.setter
    def BasicComponent496(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification__BasicComponent496", None)
        self.__BasicComponent496 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc_pc497"):
                opp_val = getattr(old_value, "repository_pc_pc497", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc_pc497", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc_pc497"):
                opp_val = getattr(value, "repository_pc_pc497", None)
                setattr(value, "repository_pc_pc497", self)

    def ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole method
        pass

class ResourceDemandingSEFF:

    pass
class ResourceDemandingInternalBehaviour:

    pass
class seff_pc_pc_ResourceDemandingBehaviour:

    pass
class pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour(seff_pc_pc_ResourceDemandingBehaviour, seff_reliability_pc_pc_FailureHandlingEntity):

    def __init__(self, pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour: set["seff_reliability_pc_pc_RecoveryActionBehaviour"] = None, seff_reliability_pc_pc: "seff_reliability_pc_pc_RecoveryAction" = None):
        self.pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour = pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour if pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour is not None else set()
        self.seff_reliability_pc_pc = seff_reliability_pc_pc
        
    @property
    def seff_reliability_pc_pc(self):
        return self.__seff_reliability_pc_pc

    @seff_reliability_pc_pc.setter
    def seff_reliability_pc_pc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour__seff_reliability_pc_pc", None)
        self.__seff_reliability_pc_pc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc_pc585"):
                opp_val = getattr(old_value, "seff_pc_pc585", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc_pc585", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc_pc585"):
                opp_val = getattr(value, "seff_pc_pc585", None)
                setattr(value, "seff_pc_pc585", self)

    @property
    def pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour(self):
        return self.__pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour

    @pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour.setter
    def pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour__pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour", None)
        self.__pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_reliability_pc_pc_RecoveryActionBehaviour"):
                    opp_val = getattr(item, "seff_reliability_pc_pc_RecoveryActionBehaviour", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_reliability_pc_pc_RecoveryActionBehaviour", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_reliability_pc_pc_RecoveryActionBehaviour"):
                    opp_val = getattr(item, "seff_reliability_pc_pc_RecoveryActionBehaviour", None)
                    
                    setattr(item, "seff_reliability_pc_pc_RecoveryActionBehaviour", self)
                    

    def SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes method
        pass

    def RecoveryActionBehaviourHasOnlyOnePredecessor(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RecoveryActionBehaviourHasOnlyOnePredecessor method
        pass

    def RecoveryActionBehaviourIsNotSuccessorOfItself(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RecoveryActionBehaviourIsNotSuccessorOfItself method
        pass

class seff_pc_pc_ServiceEffectSpecification:

    pass
class AbstractBranchTransition:

    pass
class pcm_pc_pc_seff_pc_pc_GuardedBranchTransition(AbstractBranchTransition):

    pass
class pcm_pc_pc_seff_pc_pc_ProbabilisticBranchTransition(AbstractBranchTransition):

    def __init__(self, branchProbability: float, seff_pc_pc490: "pcm_pc_pc_seff_pc_pc_BranchAction", seff_pc_pc476: "pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour"):
        self.branchProbability = branchProbability
        
    @property
    def branchProbability(self) -> float:
        return self.__branchProbability

    @branchProbability.setter
    def branchProbability(self, branchProbability: float):
        self.__branchProbability = branchProbability

class AbstractLoopAction:

    pass
class pcm_pc_pc_seff_pc_pc_LoopAction(AbstractLoopAction):

    pass
class pcm_pc_pc_seff_pc_pc_CollectionIteratorAction(AbstractLoopAction):

    pass
class pcm_pc_pc_seff_pc_pc_CallAction:

    pass
class BranchAction:

    pass
class AbstractAction:

    pass
class pcm_pc_pc_seff_pc_pc_AbstractInternalControlFlowAction(AbstractAction):

    pass
class AbstractInternalControlFlowAction:

    pass
class pcm_pc_pc_seff_pc_pc_ReleaseAction(AbstractInternalControlFlowAction):

    pass
class pcm_pc_pc_seff_pc_pc_BranchAction(AbstractInternalControlFlowAction):

    def __init__(self, AbstractBranchTransition489: set["AbstractBranchTransition"] = None, seff_pc_pc582: "pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand", seff_pc_pc566: "pcm_pc_pc_seff_performance_pc_pc_ResourceCall", seff_pc_pc560: "pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall"):
        self.AbstractBranchTransition489 = AbstractBranchTransition489 if AbstractBranchTransition489 is not None else set()
        
    @property
    def AbstractBranchTransition489(self):
        return self.__AbstractBranchTransition489

    @AbstractBranchTransition489.setter
    def AbstractBranchTransition489(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_pc_pc_BranchAction__AbstractBranchTransition489", None)
        self.__AbstractBranchTransition489 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_pc_pc490"):
                    opp_val = getattr(item, "seff_pc_pc490", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_pc_pc490", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_pc_pc490"):
                    opp_val = getattr(item, "seff_pc_pc490", None)
                    
                    setattr(item, "seff_pc_pc490", self)
                    

    def EitherGuardedBranchesOrProbabilisiticBranchTransitions(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement EitherGuardedBranchesOrProbabilisiticBranchTransitions method
        pass

    def AllProbabilisticBranchProbabilitiesMustSumUpTo1(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AllProbabilisticBranchProbabilitiesMustSumUpTo1 method
        pass

class pcm_pc_pc_seff_pc_pc_AbstractLoopAction(AbstractInternalControlFlowAction):

    pass
class pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction(AbstractInternalControlFlowAction):

    def __init__(self, pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction: "seff_reliability_pc_pc_RecoveryActionBehaviour" = None, seff_reliability_pc_pc589: set["seff_reliability_pc_pc_RecoveryActionBehaviour"] = None, seff_pc_pc582: "pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand", seff_pc_pc566: "pcm_pc_pc_seff_performance_pc_pc_ResourceCall", seff_pc_pc560: "pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall"):
        self.pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction = pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction
        self.seff_reliability_pc_pc589 = seff_reliability_pc_pc589 if seff_reliability_pc_pc589 is not None else set()
        
    @property
    def pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction(self):
        return self.__pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction

    @pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction.setter
    def pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction__pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction", None)
        self.__pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_reliability_pc_pc_RecoveryActionBehaviour587"):
                opp_val = getattr(old_value, "seff_reliability_pc_pc_RecoveryActionBehaviour587", None)
                if opp_val == self:
                    setattr(old_value, "seff_reliability_pc_pc_RecoveryActionBehaviour587", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_reliability_pc_pc_RecoveryActionBehaviour587"):
                opp_val = getattr(value, "seff_reliability_pc_pc_RecoveryActionBehaviour587", None)
                setattr(value, "seff_reliability_pc_pc_RecoveryActionBehaviour587", self)

    @property
    def seff_reliability_pc_pc589(self):
        return self.__seff_reliability_pc_pc589

    @seff_reliability_pc_pc589.setter
    def seff_reliability_pc_pc589(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction__seff_reliability_pc_pc589", None)
        self.__seff_reliability_pc_pc589 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_pc_pc590"):
                    opp_val = getattr(item, "seff_pc_pc590", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_pc_pc590", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_pc_pc590"):
                    opp_val = getattr(item, "seff_pc_pc590", None)
                    
                    setattr(item, "seff_pc_pc590", self)
                    

    def PrimaryBehaviourOfRecoveryActionMustBeSet(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement PrimaryBehaviourOfRecoveryActionMustBeSet method
        pass

class pcm_pc_pc_seff_pc_pc_InternalAction(AbstractInternalControlFlowAction):

    def __init__(self, InternalFailureOccurrenceDescription552: set["InternalFailureOccurrenceDescription"] = None, seff_pc_pc582: "pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand", seff_pc_pc566: "pcm_pc_pc_seff_performance_pc_pc_ResourceCall", seff_pc_pc560: "pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall"):
        self.InternalFailureOccurrenceDescription552 = InternalFailureOccurrenceDescription552 if InternalFailureOccurrenceDescription552 is not None else set()
        
    @property
    def InternalFailureOccurrenceDescription552(self):
        return self.__InternalFailureOccurrenceDescription552

    @InternalFailureOccurrenceDescription552.setter
    def InternalFailureOccurrenceDescription552(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_pc_pc_InternalAction__InternalFailureOccurrenceDescription552", None)
        self.__InternalFailureOccurrenceDescription552 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reliability_pc_pc553"):
                    opp_val = getattr(item, "reliability_pc_pc553", None)
                    
                    if opp_val == self:
                        setattr(item, "reliability_pc_pc553", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reliability_pc_pc553"):
                    opp_val = getattr(item, "reliability_pc_pc553", None)
                    
                    setattr(item, "reliability_pc_pc553", self)
                    

    def MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed method
        pass

    def SumOfInternalActionFailureProbabilitiesMustNotExceed1(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SumOfInternalActionFailureProbabilitiesMustNotExceed1 method
        pass

class pcm_pc_pc_seff_pc_pc_AcquireAction(AbstractInternalControlFlowAction):

    def __init__(self, timeout: bool, timeoutValue: float, pcm_pc_pc_seff_pc_pc_AcquireAction: "PassiveResource" = None, seff_pc_pc582: "pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand", seff_pc_pc566: "pcm_pc_pc_seff_performance_pc_pc_ResourceCall", seff_pc_pc560: "pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall"):
        self.timeout = timeout
        self.timeoutValue = timeoutValue
        self.pcm_pc_pc_seff_pc_pc_AcquireAction = pcm_pc_pc_seff_pc_pc_AcquireAction
        
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
    def pcm_pc_pc_seff_pc_pc_AcquireAction(self):
        return self.__pcm_pc_pc_seff_pc_pc_AcquireAction

    @pcm_pc_pc_seff_pc_pc_AcquireAction.setter
    def pcm_pc_pc_seff_pc_pc_AcquireAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_pc_pc_AcquireAction__pcm_pc_pc_seff_pc_pc_AcquireAction", None)
        self.__pcm_pc_pc_seff_pc_pc_AcquireAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PassiveResource535"):
                opp_val = getattr(old_value, "PassiveResource535", None)
                if opp_val == self:
                    setattr(old_value, "PassiveResource535", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PassiveResource535"):
                opp_val = getattr(value, "PassiveResource535", None)
                setattr(value, "PassiveResource535", self)

    def TimeoutValueOfAcquireActionMustNotBeNegative(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement TimeoutValueOfAcquireActionMustNotBeNegative method
        pass

class pcm_pc_pc_seff_pc_pc_ForkAction(AbstractInternalControlFlowAction):

    pass
class pcm_pc_pc_seff_pc_pc_SetVariableAction(AbstractInternalControlFlowAction):

    pass
class pcm_pc_pc_seff_pc_pc_StartAction(AbstractInternalControlFlowAction):

    def __init__(self, seff_pc_pc582: "pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand", seff_pc_pc566: "pcm_pc_pc_seff_performance_pc_pc_ResourceCall", seff_pc_pc560: "pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall"):
        
    def StartActionPredecessorMustNotBeDefined(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement StartActionPredecessorMustNotBeDefined method
        pass

class pcm_pc_pc_seff_pc_pc_StopAction(AbstractInternalControlFlowAction):

    def __init__(self, seff_pc_pc582: "pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand", seff_pc_pc566: "pcm_pc_pc_seff_performance_pc_pc_ResourceCall", seff_pc_pc560: "pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall"):
        
    def StopActionSuccessorMustNotBeDefined(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement StopActionSuccessorMustNotBeDefined method
        pass

class ResourceDemandingBehaviour:

    pass
class pcm_pc_pc_seff_pc_pc_ForkedBehaviour(ResourceDemandingBehaviour):

    pass
class pcm_pc_pc_seff_pc_pc_ResourceDemandingInternalBehaviour(ResourceDemandingBehaviour):

    pass
class SoftwareInducedFailureType:

    pass
class InternalAction:

    pass
class pcm_pc_pc_reliability_pc_pc_ResourceTimeoutFailureType(SoftwareInducedFailureType):

    pass
class qos_reliability_pc_pc_SpecifiedReliabilityAnnotation:

    pass
class CommunicationLinkResourceType:

    pass
class pcm_pc_pc_reliability_pc_pc_FailureOccurrenceDescription:

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

class FailureOccurrenceDescription:

    pass
class pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription(FailureOccurrenceDescription):

    def __init__(self, qos_reliability_pc_pc: "qos_reliability_pc_pc_SpecifiedReliabilityAnnotation" = None, pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription: "FailureType" = None):
        self.qos_reliability_pc_pc = qos_reliability_pc_pc
        self.pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription = pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription
        
    @property
    def pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription(self):
        return self.__pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription

    @pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription.setter
    def pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription__pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription", None)
        self.__pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FailureType450"):
                opp_val = getattr(old_value, "FailureType450", None)
                if opp_val == self:
                    setattr(old_value, "FailureType450", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FailureType450"):
                opp_val = getattr(value, "FailureType450", None)
                setattr(value, "FailureType450", self)

    @property
    def qos_reliability_pc_pc(self):
        return self.__qos_reliability_pc_pc

    @qos_reliability_pc_pc.setter
    def qos_reliability_pc_pc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription__qos_reliability_pc_pc", None)
        self.__qos_reliability_pc_pc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qosannotations_pc_pc448"):
                opp_val = getattr(old_value, "qosannotations_pc_pc448", None)
                if opp_val == self:
                    setattr(old_value, "qosannotations_pc_pc448", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qosannotations_pc_pc448"):
                opp_val = getattr(value, "qosannotations_pc_pc448", None)
                setattr(value, "qosannotations_pc_pc448", self)

    def NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription method
        pass

class pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription(FailureOccurrenceDescription):

    def __init__(self, InternalAction: "InternalAction" = None, SoftwareInducedFailureType: "SoftwareInducedFailureType" = None):
        self.InternalAction = InternalAction
        self.SoftwareInducedFailureType = SoftwareInducedFailureType
        
    @property
    def SoftwareInducedFailureType(self):
        return self.__SoftwareInducedFailureType

    @SoftwareInducedFailureType.setter
    def SoftwareInducedFailureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription__SoftwareInducedFailureType", None)
        self.__SoftwareInducedFailureType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reliability_pc_pc444"):
                opp_val = getattr(old_value, "reliability_pc_pc444", None)
                if opp_val == self:
                    setattr(old_value, "reliability_pc_pc444", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reliability_pc_pc444"):
                opp_val = getattr(value, "reliability_pc_pc444", None)
                setattr(value, "reliability_pc_pc444", self)

    @property
    def InternalAction(self):
        return self.__InternalAction

    @InternalAction.setter
    def InternalAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription__InternalAction", None)
        self.__InternalAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc_pc442"):
                opp_val = getattr(old_value, "seff_pc_pc442", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc_pc442", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc_pc442"):
                opp_val = getattr(value, "seff_pc_pc442", None)
                setattr(value, "seff_pc_pc442", self)

    def NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription method
        pass

class InternalFailureOccurrenceDescription:

    pass
class ProcessingResourceType:

    pass
class parameter_pc_pc_pcm_pc_pc_AbstractNamedReference:

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
class pcm_pc_pc_seff_pc_pc_CallReturnAction(CallAction):

    pass
class pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall(CallAction):

    def __init__(self, pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall562: "InfrastructureRequiredRole" = None, pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall: "InfrastructureSignature" = None, PCMRandomVariable557: "PCMRandomVariable" = None, AbstractInternalControlFlowAction: "AbstractInternalControlFlowAction" = None, seff_pc_pc413: "pcm_pc_pc_parameter_pc_pc_VariableUsage"):
        self.pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall562 = pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall562
        self.pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall = pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall
        self.PCMRandomVariable557 = PCMRandomVariable557
        self.AbstractInternalControlFlowAction = AbstractInternalControlFlowAction
        
    @property
    def pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall562(self):
        return self.__pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall562

    @pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall562.setter
    def pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall562(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall__pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall562", None)
        self.__pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall562 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InfrastructureRequiredRole563"):
                opp_val = getattr(old_value, "InfrastructureRequiredRole563", None)
                if opp_val == self:
                    setattr(old_value, "InfrastructureRequiredRole563", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InfrastructureRequiredRole563"):
                opp_val = getattr(value, "InfrastructureRequiredRole563", None)
                setattr(value, "InfrastructureRequiredRole563", self)

    @property
    def PCMRandomVariable557(self):
        return self.__PCMRandomVariable557

    @PCMRandomVariable557.setter
    def PCMRandomVariable557(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall__PCMRandomVariable557", None)
        self.__PCMRandomVariable557 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc_pc558"):
                opp_val = getattr(old_value, "core_pc_pc558", None)
                if opp_val == self:
                    setattr(old_value, "core_pc_pc558", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc_pc558"):
                opp_val = getattr(value, "core_pc_pc558", None)
                setattr(value, "core_pc_pc558", self)

    @property
    def AbstractInternalControlFlowAction(self):
        return self.__AbstractInternalControlFlowAction

    @AbstractInternalControlFlowAction.setter
    def AbstractInternalControlFlowAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall__AbstractInternalControlFlowAction", None)
        self.__AbstractInternalControlFlowAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc_pc560"):
                opp_val = getattr(old_value, "seff_pc_pc560", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc_pc560", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc_pc560"):
                opp_val = getattr(value, "seff_pc_pc560", None)
                setattr(value, "seff_pc_pc560", self)

    @property
    def pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall(self):
        return self.__pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall

    @pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall.setter
    def pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall__pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall", None)
        self.__pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InfrastructureSignature555"):
                opp_val = getattr(old_value, "InfrastructureSignature555", None)
                if opp_val == self:
                    setattr(old_value, "InfrastructureSignature555", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InfrastructureSignature555"):
                opp_val = getattr(value, "InfrastructureSignature555", None)
                setattr(value, "InfrastructureSignature555", self)

    def SignatureMustBelongToUsedRequiredRole(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SignatureMustBelongToUsedRequiredRole method
        pass

    def SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

    def ReferencedRequiredRoleMustBeRequiredByComponent(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ReferencedRequiredRoleMustBeRequiredByComponent method
        pass

class pcm_pc_pc_seff_performance_pc_pc_ResourceCall(CallAction):

    def __init__(self, AbstractInternalControlFlowAction565: "AbstractInternalControlFlowAction" = None, pcm_pc_pc_seff_performance_pc_pc_ResourceCall: "entity_pc_pc_ResourceRequiredRole" = None, pcm_pc_pc_seff_performance_pc_pc_ResourceCall570: "ResourceSignature" = None, PCMRandomVariable573: "PCMRandomVariable" = None, seff_pc_pc413: "pcm_pc_pc_parameter_pc_pc_VariableUsage"):
        self.AbstractInternalControlFlowAction565 = AbstractInternalControlFlowAction565
        self.pcm_pc_pc_seff_performance_pc_pc_ResourceCall = pcm_pc_pc_seff_performance_pc_pc_ResourceCall
        self.pcm_pc_pc_seff_performance_pc_pc_ResourceCall570 = pcm_pc_pc_seff_performance_pc_pc_ResourceCall570
        self.PCMRandomVariable573 = PCMRandomVariable573
        
    @property
    def AbstractInternalControlFlowAction565(self):
        return self.__AbstractInternalControlFlowAction565

    @AbstractInternalControlFlowAction565.setter
    def AbstractInternalControlFlowAction565(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_performance_pc_pc_ResourceCall__AbstractInternalControlFlowAction565", None)
        self.__AbstractInternalControlFlowAction565 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc_pc566"):
                opp_val = getattr(old_value, "seff_pc_pc566", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc_pc566", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc_pc566"):
                opp_val = getattr(value, "seff_pc_pc566", None)
                setattr(value, "seff_pc_pc566", self)

    @property
    def pcm_pc_pc_seff_performance_pc_pc_ResourceCall570(self):
        return self.__pcm_pc_pc_seff_performance_pc_pc_ResourceCall570

    @pcm_pc_pc_seff_performance_pc_pc_ResourceCall570.setter
    def pcm_pc_pc_seff_performance_pc_pc_ResourceCall570(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_performance_pc_pc_ResourceCall__pcm_pc_pc_seff_performance_pc_pc_ResourceCall570", None)
        self.__pcm_pc_pc_seff_performance_pc_pc_ResourceCall570 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceSignature571"):
                opp_val = getattr(old_value, "ResourceSignature571", None)
                if opp_val == self:
                    setattr(old_value, "ResourceSignature571", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceSignature571"):
                opp_val = getattr(value, "ResourceSignature571", None)
                setattr(value, "ResourceSignature571", self)

    @property
    def PCMRandomVariable573(self):
        return self.__PCMRandomVariable573

    @PCMRandomVariable573.setter
    def PCMRandomVariable573(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_performance_pc_pc_ResourceCall__PCMRandomVariable573", None)
        self.__PCMRandomVariable573 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc_pc574"):
                opp_val = getattr(old_value, "core_pc_pc574", None)
                if opp_val == self:
                    setattr(old_value, "core_pc_pc574", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc_pc574"):
                opp_val = getattr(value, "core_pc_pc574", None)
                setattr(value, "core_pc_pc574", self)

    @property
    def pcm_pc_pc_seff_performance_pc_pc_ResourceCall(self):
        return self.__pcm_pc_pc_seff_performance_pc_pc_ResourceCall

    @pcm_pc_pc_seff_performance_pc_pc_ResourceCall.setter
    def pcm_pc_pc_seff_performance_pc_pc_ResourceCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_performance_pc_pc_ResourceCall__pcm_pc_pc_seff_performance_pc_pc_ResourceCall", None)
        self.__pcm_pc_pc_seff_performance_pc_pc_ResourceCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entity_pc_pc_ResourceRequiredRole568"):
                opp_val = getattr(old_value, "entity_pc_pc_ResourceRequiredRole568", None)
                if opp_val == self:
                    setattr(old_value, "entity_pc_pc_ResourceRequiredRole568", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entity_pc_pc_ResourceRequiredRole568"):
                opp_val = getattr(value, "entity_pc_pc_ResourceRequiredRole568", None)
                setattr(value, "entity_pc_pc_ResourceRequiredRole568", self)

    def ResourceSignatureBelongsToResourceRequiredRole(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ResourceSignatureBelongsToResourceRequiredRole method
        pass

    def ResourceRequiredRoleMustBeReferencedByComponent(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ResourceRequiredRoleMustBeReferencedByComponent method
        pass

    def SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

class Variable:

    pass
class pcm_pc_pc_parameter_pc_pc_CharacterisedVariable(Variable):

    def __init__(self, characterisationType: str):
        self.characterisationType = characterisationType
        
    @property
    def characterisationType(self) -> str:
        return self.__characterisationType

    @characterisationType.setter
    def characterisationType(self, characterisationType: str):
        self.__characterisationType = characterisationType

class pcm_pc_pc_parameter_pc_pc_VariableCharacterisation:

    def __init__(self, type: str, PCMRandomVariable432: "PCMRandomVariable" = None, VariableUsage435: "VariableUsage" = None):
        self.type = type
        self.PCMRandomVariable432 = PCMRandomVariable432
        self.VariableUsage435 = VariableUsage435
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def VariableUsage435(self):
        return self.__VariableUsage435

    @VariableUsage435.setter
    def VariableUsage435(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_parameter_pc_pc_VariableCharacterisation__VariableUsage435", None)
        self.__VariableUsage435 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameter_pc_pc436"):
                opp_val = getattr(old_value, "parameter_pc_pc436", None)
                if opp_val == self:
                    setattr(old_value, "parameter_pc_pc436", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameter_pc_pc436"):
                opp_val = getattr(value, "parameter_pc_pc436", None)
                setattr(value, "parameter_pc_pc436", self)

    @property
    def PCMRandomVariable432(self):
        return self.__PCMRandomVariable432

    @PCMRandomVariable432.setter
    def PCMRandomVariable432(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_parameter_pc_pc_VariableCharacterisation__PCMRandomVariable432", None)
        self.__PCMRandomVariable432 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc_pc433"):
                opp_val = getattr(old_value, "core_pc_pc433", None)
                if opp_val == self:
                    setattr(old_value, "core_pc_pc433", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc_pc433"):
                opp_val = getattr(value, "core_pc_pc433", None)
                setattr(value, "core_pc_pc433", self)

class SchedulingPolicy:

    pass
class pcm_pc_pc_resourcetype_pc_pc_ResourceRepository:

    pass
class ResourceRepository:

    pass
class UnitCarryingElement:

    pass
class HardwareInducedFailureType:

    pass
class ResourceType:

    pass
class pcm_pc_pc_resourcetype_pc_pc_ProcessingResourceType(ResourceType):

    pass
class pcm_pc_pc_parameter_pc_pc_VariableUsage:

    pass
class pcm_pc_pc_protocol_pc_pc_Protocol:

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
class pcm_pc_pc_resourcetype_pc_pc_CommunicationLinkResourceType(ResourceType):

    pass
class CompositeDataType:

    pass
class repository_pc_pc_DataType:

    pass
class NamedElement:

    pass
class pcm_pc_pc_resourceenvironment_pc_pc_ResourceEnvironment(NamedElement):

    pass
class pcm_pc_pc_repository_pc_pc_InnerDeclaration(NamedElement):

    pass
class InnerDeclaration:

    pass
class ProvidesComponentType:

    pass
class repository_pc_pc_ImplementationComponentType:

    pass
class entity_pc_pc_ComposedProvidingRequiringEntity:

    pass
class pcm_pc_pc_subsystem_pc_pc_SubSystem(repository_pc_pc_RepositoryComponent, entity_pc_pc_ComposedProvidingRequiringEntity):

    pass
class pcm_pc_pc_completions_pc_pc_Completion(repository_pc_pc_ImplementationComponentType, entity_pc_pc_ComposedProvidingRequiringEntity):

    pass
class pcm_pc_pc_repository_pc_pc_CompositeComponent(repository_pc_pc_ImplementationComponentType, entity_pc_pc_ComposedProvidingRequiringEntity):

    def __init__(self):
        
    def RequireSameInterfaces(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RequireSameInterfaces method
        pass

    def ProvideSameInterfaces(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ProvideSameInterfaces method
        pass

class InfrastructureInterface:

    pass
class pcm_pc_pc_repository_pc_pc_ExceptionType:

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
class OperationInterface:

    pass
class RequiredCharacterisation:

    pass
class Protocol:

    pass
class FailureType:

    pass
class pcm_pc_pc_reliability_pc_pc_NetworkInducedFailureType(FailureType):

    def __init__(self, CommunicationLinkResourceType: "CommunicationLinkResourceType" = None, FailureType333: "pcm_pc_pc_repository_pc_pc_Signature", FailureType592: "pcm_pc_pc_seff_reliability_pc_pc_FailureHandlingEntity", reliability_pc_pc304: "pcm_pc_pc_repository_pc_pc_Repository", FailureType450: "pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription"):
        self.CommunicationLinkResourceType = CommunicationLinkResourceType
        
    @property
    def CommunicationLinkResourceType(self):
        return self.__CommunicationLinkResourceType

    @CommunicationLinkResourceType.setter
    def CommunicationLinkResourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_reliability_pc_pc_NetworkInducedFailureType__CommunicationLinkResourceType", None)
        self.__CommunicationLinkResourceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcetype_pc_pc446"):
                opp_val = getattr(old_value, "resourcetype_pc_pc446", None)
                if opp_val == self:
                    setattr(old_value, "resourcetype_pc_pc446", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcetype_pc_pc446"):
                opp_val = getattr(value, "resourcetype_pc_pc446", None)
                setattr(value, "resourcetype_pc_pc446", self)

    def NetworkInducedFailureTypeHasCommunicationLinkResourceType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NetworkInducedFailureTypeHasCommunicationLinkResourceType method
        pass

class pcm_pc_pc_reliability_pc_pc_SoftwareInducedFailureType(FailureType):

    pass
class pcm_pc_pc_reliability_pc_pc_HardwareInducedFailureType(FailureType):

    def __init__(self, ProcessingResourceType: "ProcessingResourceType" = None, FailureType333: "pcm_pc_pc_repository_pc_pc_Signature", FailureType592: "pcm_pc_pc_seff_reliability_pc_pc_FailureHandlingEntity", reliability_pc_pc304: "pcm_pc_pc_repository_pc_pc_Repository", FailureType450: "pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription"):
        self.ProcessingResourceType = ProcessingResourceType
        
    @property
    def ProcessingResourceType(self):
        return self.__ProcessingResourceType

    @ProcessingResourceType.setter
    def ProcessingResourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_reliability_pc_pc_HardwareInducedFailureType__ProcessingResourceType", None)
        self.__ProcessingResourceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcetype_pc_pc438"):
                opp_val = getattr(old_value, "resourcetype_pc_pc438", None)
                if opp_val == self:
                    setattr(old_value, "resourcetype_pc_pc438", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcetype_pc_pc438"):
                opp_val = getattr(value, "resourcetype_pc_pc438", None)
                setattr(value, "resourcetype_pc_pc438", self)

    def HardwareInducedFailureTypeHasProcessingResourceType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement HardwareInducedFailureTypeHasProcessingResourceType method
        pass

class Signature:

    pass
class pcm_pc_pc_repository_pc_pc_InfrastructureSignature(Signature):

    pass
class pcm_pc_pc_repository_pc_pc_OperationSignature(Signature):

    def __init__(self, OperationInterface: "OperationInterface" = None, Parameter350: set["Parameter"] = None, pcm_pc_pc_repository_pc_pc_OperationSignature: "DataType" = None, Signature606: "pcm_pc_pc_qosannotations_pc_pc_SpecifiedOutputParameterAbstraction", Signature: "pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification", Signature594: "pcm_pc_pc_qosannotations_pc_pc_SpecifiedQoSAnnotation"):
        self.OperationInterface = OperationInterface
        self.Parameter350 = Parameter350 if Parameter350 is not None else set()
        self.pcm_pc_pc_repository_pc_pc_OperationSignature = pcm_pc_pc_repository_pc_pc_OperationSignature
        
    @property
    def OperationInterface(self):
        return self.__OperationInterface

    @OperationInterface.setter
    def OperationInterface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_OperationSignature__OperationInterface", None)
        self.__OperationInterface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc_pc348"):
                opp_val = getattr(old_value, "repository_pc_pc348", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc_pc348", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc_pc348"):
                opp_val = getattr(value, "repository_pc_pc348", None)
                setattr(value, "repository_pc_pc348", self)

    @property
    def Parameter350(self):
        return self.__Parameter350

    @Parameter350.setter
    def Parameter350(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_OperationSignature__Parameter350", None)
        self.__Parameter350 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_pc_pc351"):
                    opp_val = getattr(item, "repository_pc_pc351", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_pc_pc351", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_pc_pc351"):
                    opp_val = getattr(item, "repository_pc_pc351", None)
                    
                    setattr(item, "repository_pc_pc351", self)
                    

    @property
    def pcm_pc_pc_repository_pc_pc_OperationSignature(self):
        return self.__pcm_pc_pc_repository_pc_pc_OperationSignature

    @pcm_pc_pc_repository_pc_pc_OperationSignature.setter
    def pcm_pc_pc_repository_pc_pc_OperationSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_OperationSignature__pcm_pc_pc_repository_pc_pc_OperationSignature", None)
        self.__pcm_pc_pc_repository_pc_pc_OperationSignature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType353"):
                opp_val = getattr(old_value, "DataType353", None)
                if opp_val == self:
                    setattr(old_value, "DataType353", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType353"):
                opp_val = getattr(value, "DataType353", None)
                setattr(value, "DataType353", self)

    def ParameterNamesHaveToBeUniqueForASignature(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ParameterNamesHaveToBeUniqueForASignature method
        pass

class pcm_pc_pc_repository_pc_pc_EventType(Signature):

    pass
class Parameter:

    pass
class pcm_pc_pc_repository_pc_pc_RequiredCharacterisation:

    def __init__(self, type: str, pcm_pc_pc_repository_pc_pc_RequiredCharacterisation: "Parameter" = None, Interface319: "Interface" = None):
        self.type = type
        self.pcm_pc_pc_repository_pc_pc_RequiredCharacterisation = pcm_pc_pc_repository_pc_pc_RequiredCharacterisation
        self.Interface319 = Interface319
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def pcm_pc_pc_repository_pc_pc_RequiredCharacterisation(self):
        return self.__pcm_pc_pc_repository_pc_pc_RequiredCharacterisation

    @pcm_pc_pc_repository_pc_pc_RequiredCharacterisation.setter
    def pcm_pc_pc_repository_pc_pc_RequiredCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_RequiredCharacterisation__pcm_pc_pc_repository_pc_pc_RequiredCharacterisation", None)
        self.__pcm_pc_pc_repository_pc_pc_RequiredCharacterisation = value
        
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
    def Interface319(self):
        return self.__Interface319

    @Interface319.setter
    def Interface319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_RequiredCharacterisation__Interface319", None)
        self.__Interface319 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc_pc320"):
                opp_val = getattr(old_value, "repository_pc_pc320", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc_pc320", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc_pc320"):
                opp_val = getattr(value, "repository_pc_pc320", None)
                setattr(value, "repository_pc_pc320", self)

class EventType:

    pass
class InfrastructureSignature:

    pass
class DataType:

    pass
class pcm_pc_pc_repository_pc_pc_PrimitiveDataType(DataType):

    def __init__(self, type: str, DataType374: "pcm_pc_pc_repository_pc_pc_InnerDeclaration", DataType: "pcm_pc_pc_repository_pc_pc_Parameter", DataType369: "pcm_pc_pc_repository_pc_pc_CollectionDataType", DataType353: "pcm_pc_pc_repository_pc_pc_OperationSignature", repository_pc_pc307: "pcm_pc_pc_repository_pc_pc_Repository"):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class pcm_pc_pc_repository_pc_pc_Parameter:

    def __init__(self, modifier__Parameter: str, parameterName: str, ResourceSignature: "ResourceSignature" = None, pcm_pc_pc_repository_pc_pc_Parameter: "DataType" = None, InfrastructureSignature: "InfrastructureSignature" = None, OperationSignature290: "OperationSignature" = None, EventType: "EventType" = None):
        self.modifier__Parameter = modifier__Parameter
        self.parameterName = parameterName
        self.ResourceSignature = ResourceSignature
        self.pcm_pc_pc_repository_pc_pc_Parameter = pcm_pc_pc_repository_pc_pc_Parameter
        self.InfrastructureSignature = InfrastructureSignature
        self.OperationSignature290 = OperationSignature290
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
    def OperationSignature290(self):
        return self.__OperationSignature290

    @OperationSignature290.setter
    def OperationSignature290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_Parameter__OperationSignature290", None)
        self.__OperationSignature290 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc_pc291"):
                opp_val = getattr(old_value, "repository_pc_pc291", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc_pc291", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc_pc291"):
                opp_val = getattr(value, "repository_pc_pc291", None)
                setattr(value, "repository_pc_pc291", self)

    @property
    def ResourceSignature(self):
        return self.__ResourceSignature

    @ResourceSignature.setter
    def ResourceSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_Parameter__ResourceSignature", None)
        self.__ResourceSignature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcetype_pc_pc"):
                opp_val = getattr(old_value, "resourcetype_pc_pc", None)
                if opp_val == self:
                    setattr(old_value, "resourcetype_pc_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcetype_pc_pc"):
                opp_val = getattr(value, "resourcetype_pc_pc", None)
                setattr(value, "resourcetype_pc_pc", self)

    @property
    def EventType(self):
        return self.__EventType

    @EventType.setter
    def EventType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_Parameter__EventType", None)
        self.__EventType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc_pc293"):
                opp_val = getattr(old_value, "repository_pc_pc293", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc_pc293", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc_pc293"):
                opp_val = getattr(value, "repository_pc_pc293", None)
                setattr(value, "repository_pc_pc293", self)

    @property
    def pcm_pc_pc_repository_pc_pc_Parameter(self):
        return self.__pcm_pc_pc_repository_pc_pc_Parameter

    @pcm_pc_pc_repository_pc_pc_Parameter.setter
    def pcm_pc_pc_repository_pc_pc_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_Parameter__pcm_pc_pc_repository_pc_pc_Parameter", None)
        self.__pcm_pc_pc_repository_pc_pc_Parameter = value
        
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
    def InfrastructureSignature(self):
        return self.__InfrastructureSignature

    @InfrastructureSignature.setter
    def InfrastructureSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_Parameter__InfrastructureSignature", None)
        self.__InfrastructureSignature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc_pc288"):
                opp_val = getattr(old_value, "repository_pc_pc288", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc_pc288", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc_pc288"):
                opp_val = getattr(value, "repository_pc_pc288", None)
                setattr(value, "repository_pc_pc288", self)

class Repository:

    pass
class InterfaceProvidingRequiringEntity:

    pass
class pcm_pc_pc_repository_pc_pc_RepositoryComponent(InterfaceProvidingRequiringEntity):

    pass
class Interface:

    pass
class pcm_pc_pc_repository_pc_pc_OperationInterface(Interface):

    def __init__(self, OperationSignature355: set["OperationSignature"] = None, repository_pc_pc320: "pcm_pc_pc_repository_pc_pc_RequiredCharacterisation", repository_pc_pc302: "pcm_pc_pc_repository_pc_pc_Repository", Interface309: "pcm_pc_pc_repository_pc_pc_Interface"):
        self.OperationSignature355 = OperationSignature355 if OperationSignature355 is not None else set()
        
    @property
    def OperationSignature355(self):
        return self.__OperationSignature355

    @OperationSignature355.setter
    def OperationSignature355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_OperationInterface__OperationSignature355", None)
        self.__OperationSignature355 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_pc_pc356"):
                    opp_val = getattr(item, "repository_pc_pc356", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_pc_pc356", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_pc_pc356"):
                    opp_val = getattr(item, "repository_pc_pc356", None)
                    
                    setattr(item, "repository_pc_pc356", self)
                    

    def SignaturesHaveToBeUniqueForAnInterface(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SignaturesHaveToBeUniqueForAnInterface method
        pass

class pcm_pc_pc_repository_pc_pc_InfrastructureInterface(Interface):

    pass
class pcm_pc_pc_repository_pc_pc_EventGroup(Interface):

    pass
class pcm_pc_pc_repository_pc_pc_DataType:

    pass
class ResourceSignature:

    pass
class ServiceEffectSpecification:

    pass
class CompleteComponentType:

    pass
class ImplementationComponentType:

    pass
class pcm_pc_pc_repository_pc_pc_BasicComponent(ImplementationComponentType):

    def __init__(self, ServiceEffectSpecification: set["ServiceEffectSpecification"] = None, PassiveResource275: set["PassiveResource"] = None):
        self.ServiceEffectSpecification = ServiceEffectSpecification if ServiceEffectSpecification is not None else set()
        self.PassiveResource275 = PassiveResource275 if PassiveResource275 is not None else set()
        
    @property
    def ServiceEffectSpecification(self):
        return self.__ServiceEffectSpecification

    @ServiceEffectSpecification.setter
    def ServiceEffectSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_BasicComponent__ServiceEffectSpecification", None)
        self.__ServiceEffectSpecification = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_pc_pc273"):
                    opp_val = getattr(item, "seff_pc_pc273", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_pc_pc273", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_pc_pc273"):
                    opp_val = getattr(item, "seff_pc_pc273", None)
                    
                    setattr(item, "seff_pc_pc273", self)
                    

    @property
    def PassiveResource275(self):
        return self.__PassiveResource275

    @PassiveResource275.setter
    def PassiveResource275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_BasicComponent__PassiveResource275", None)
        self.__PassiveResource275 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_pc_pc276"):
                    opp_val = getattr(item, "repository_pc_pc276", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_pc_pc276", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_pc_pc276"):
                    opp_val = getattr(item, "repository_pc_pc276", None)
                    
                    setattr(item, "repository_pc_pc276", self)
                    

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
class pcm_pc_pc_usagemodel_pc_pc_BranchTransition:

    def __init__(self, branchProbability: float, Branch: "Branch" = None, ScenarioBehaviour246: "ScenarioBehaviour" = None):
        self.branchProbability = branchProbability
        self.Branch = Branch
        self.ScenarioBehaviour246 = ScenarioBehaviour246
        
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
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_BranchTransition__Branch", None)
        self.__Branch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc_pc244"):
                opp_val = getattr(old_value, "usagemodel_pc_pc244", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc_pc244", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc_pc244"):
                opp_val = getattr(value, "usagemodel_pc_pc244", None)
                setattr(value, "usagemodel_pc_pc244", self)

    @property
    def ScenarioBehaviour246(self):
        return self.__ScenarioBehaviour246

    @ScenarioBehaviour246.setter
    def ScenarioBehaviour246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_BranchTransition__ScenarioBehaviour246", None)
        self.__ScenarioBehaviour246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc_pc247"):
                opp_val = getattr(old_value, "usagemodel_pc_pc247", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc_pc247", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc_pc247"):
                opp_val = getattr(value, "usagemodel_pc_pc247", None)
                setattr(value, "usagemodel_pc_pc247", self)

class OperationSignature:

    pass
class BranchTransition:

    pass
class pcm_pc_pc_usagemodel_pc_pc_UserData:

    pass
class Workload:

    pass
class pcm_pc_pc_usagemodel_pc_pc_OpenWorkload(Workload):

    def __init__(self, PCMRandomVariable258: "PCMRandomVariable" = None, usagemodel_pc_pc200: "pcm_pc_pc_usagemodel_pc_pc_UsageScenario"):
        self.PCMRandomVariable258 = PCMRandomVariable258
        
    @property
    def PCMRandomVariable258(self):
        return self.__PCMRandomVariable258

    @PCMRandomVariable258.setter
    def PCMRandomVariable258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_OpenWorkload__PCMRandomVariable258", None)
        self.__PCMRandomVariable258 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc_pc259"):
                opp_val = getattr(old_value, "core_pc_pc259", None)
                if opp_val == self:
                    setattr(old_value, "core_pc_pc259", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc_pc259"):
                opp_val = getattr(value, "core_pc_pc259", None)
                setattr(value, "core_pc_pc259", self)

    def InterArrivalTimeInOpenWorkloadNeedsToBeSpecified(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement InterArrivalTimeInOpenWorkloadNeedsToBeSpecified method
        pass

class pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload(Workload):

    def __init__(self, population: int, PCMRandomVariable264: "PCMRandomVariable" = None, usagemodel_pc_pc200: "pcm_pc_pc_usagemodel_pc_pc_UsageScenario"):
        self.population = population
        self.PCMRandomVariable264 = PCMRandomVariable264
        
    @property
    def population(self) -> int:
        return self.__population

    @population.setter
    def population(self, population: int):
        self.__population = population

    @property
    def PCMRandomVariable264(self):
        return self.__PCMRandomVariable264

    @PCMRandomVariable264.setter
    def PCMRandomVariable264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload__PCMRandomVariable264", None)
        self.__PCMRandomVariable264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc_pc265"):
                opp_val = getattr(old_value, "core_pc_pc265", None)
                if opp_val == self:
                    setattr(old_value, "core_pc_pc265", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc_pc265"):
                opp_val = getattr(value, "core_pc_pc265", None)
                setattr(value, "core_pc_pc265", self)

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
class pcm_pc_pc_usagemodel_pc_pc_Workload:

    pass
class VariableUsage:

    pass
class RepositoryComponent:

    pass
class pcm_pc_pc_repository_pc_pc_CompleteComponentType(RepositoryComponent):

    def __init__(self, pcm_pc_pc_repository_pc_pc_CompleteComponentType: set["ProvidesComponentType"] = None, RepositoryComponent: "pcm_pc_pc_composition_pc_pc_AssemblyContext", repository_pc_pc300: "pcm_pc_pc_repository_pc_pc_Repository"):
        self.pcm_pc_pc_repository_pc_pc_CompleteComponentType = pcm_pc_pc_repository_pc_pc_CompleteComponentType if pcm_pc_pc_repository_pc_pc_CompleteComponentType is not None else set()
        
    @property
    def pcm_pc_pc_repository_pc_pc_CompleteComponentType(self):
        return self.__pcm_pc_pc_repository_pc_pc_CompleteComponentType

    @pcm_pc_pc_repository_pc_pc_CompleteComponentType.setter
    def pcm_pc_pc_repository_pc_pc_CompleteComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_CompleteComponentType__pcm_pc_pc_repository_pc_pc_CompleteComponentType", None)
        self.__pcm_pc_pc_repository_pc_pc_CompleteComponentType = value if value is not None else set()
        
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

class pcm_pc_pc_repository_pc_pc_ImplementationComponentType(RepositoryComponent):

    def __init__(self, componentType: str, pcm_pc_pc_repository_pc_pc_ImplementationComponentType: set["CompleteComponentType"] = None, pcm_pc_pc_repository_pc_pc_ImplementationComponentType279: set["VariableUsage"] = None, RepositoryComponent: "pcm_pc_pc_composition_pc_pc_AssemblyContext", repository_pc_pc300: "pcm_pc_pc_repository_pc_pc_Repository"):
        self.componentType = componentType
        self.pcm_pc_pc_repository_pc_pc_ImplementationComponentType = pcm_pc_pc_repository_pc_pc_ImplementationComponentType if pcm_pc_pc_repository_pc_pc_ImplementationComponentType is not None else set()
        self.pcm_pc_pc_repository_pc_pc_ImplementationComponentType279 = pcm_pc_pc_repository_pc_pc_ImplementationComponentType279 if pcm_pc_pc_repository_pc_pc_ImplementationComponentType279 is not None else set()
        
    @property
    def componentType(self) -> str:
        return self.__componentType

    @componentType.setter
    def componentType(self, componentType: str):
        self.__componentType = componentType

    @property
    def pcm_pc_pc_repository_pc_pc_ImplementationComponentType(self):
        return self.__pcm_pc_pc_repository_pc_pc_ImplementationComponentType

    @pcm_pc_pc_repository_pc_pc_ImplementationComponentType.setter
    def pcm_pc_pc_repository_pc_pc_ImplementationComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_ImplementationComponentType__pcm_pc_pc_repository_pc_pc_ImplementationComponentType", None)
        self.__pcm_pc_pc_repository_pc_pc_ImplementationComponentType = value if value is not None else set()
        
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
    def pcm_pc_pc_repository_pc_pc_ImplementationComponentType279(self):
        return self.__pcm_pc_pc_repository_pc_pc_ImplementationComponentType279

    @pcm_pc_pc_repository_pc_pc_ImplementationComponentType279.setter
    def pcm_pc_pc_repository_pc_pc_ImplementationComponentType279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_ImplementationComponentType__pcm_pc_pc_repository_pc_pc_ImplementationComponentType279", None)
        self.__pcm_pc_pc_repository_pc_pc_ImplementationComponentType279 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableUsage280"):
                    opp_val = getattr(item, "VariableUsage280", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableUsage280", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableUsage280"):
                    opp_val = getattr(item, "VariableUsage280", None)
                    
                    setattr(item, "VariableUsage280", self)
                    

    def providedInterfacesHaveToConformToCompleteType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement providedInterfacesHaveToConformToCompleteType method
        pass

    def ProvidedInterfaceHaveToConformToComponentType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ProvidedInterfaceHaveToConformToComponentType method
        pass

    def RequiredInterfacesHaveToConformToCompleteType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement RequiredInterfacesHaveToConformToCompleteType method
        pass

class pcm_pc_pc_repository_pc_pc_ProvidesComponentType(RepositoryComponent):

    def __init__(self, RepositoryComponent: "pcm_pc_pc_composition_pc_pc_AssemblyContext", repository_pc_pc300: "pcm_pc_pc_repository_pc_pc_Repository"):
        
    def AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType method
        pass

class AbstractUserAction:

    pass
class pcm_pc_pc_usagemodel_pc_pc_Delay(AbstractUserAction):

    pass
class pcm_pc_pc_usagemodel_pc_pc_Start(AbstractUserAction):

    def __init__(self, usagemodel_pc_pc225: "pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction", usagemodel_pc_pc242: "pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour", usagemodel_pc_pc228: "pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction"):
        
    def StartHasNoPredecessor(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement StartHasNoPredecessor method
        pass

class pcm_pc_pc_usagemodel_pc_pc_Loop(AbstractUserAction):

    pass
class pcm_pc_pc_usagemodel_pc_pc_Branch(AbstractUserAction):

    def __init__(self, BranchTransition249: set["BranchTransition"] = None, usagemodel_pc_pc225: "pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction", usagemodel_pc_pc242: "pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour", usagemodel_pc_pc228: "pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction"):
        self.BranchTransition249 = BranchTransition249 if BranchTransition249 is not None else set()
        
    @property
    def BranchTransition249(self):
        return self.__BranchTransition249

    @BranchTransition249.setter
    def BranchTransition249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_Branch__BranchTransition249", None)
        self.__BranchTransition249 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "usagemodel_pc_pc250"):
                    opp_val = getattr(item, "usagemodel_pc_pc250", None)
                    
                    if opp_val == self:
                        setattr(item, "usagemodel_pc_pc250", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "usagemodel_pc_pc250"):
                    opp_val = getattr(item, "usagemodel_pc_pc250", None)
                    
                    setattr(item, "usagemodel_pc_pc250", self)
                    

    def AllBranchProbabilitiesMustSumUpTo1(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AllBranchProbabilitiesMustSumUpTo1 method
        pass

class pcm_pc_pc_usagemodel_pc_pc_Stop(AbstractUserAction):

    def __init__(self, usagemodel_pc_pc225: "pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction", usagemodel_pc_pc242: "pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour", usagemodel_pc_pc228: "pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction"):
        
    def StopHasNoSuccessor(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement StopHasNoSuccessor method
        pass

class pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall(AbstractUserAction):

    def __init__(self, priority: int, pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall: "OperationProvidedRole" = None, pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall217: "OperationSignature" = None, VariableUsage219: set["VariableUsage"] = None, VariableUsage222: set["VariableUsage"] = None, usagemodel_pc_pc225: "pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction", usagemodel_pc_pc242: "pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour", usagemodel_pc_pc228: "pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction"):
        self.priority = priority
        self.pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall = pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall
        self.pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall217 = pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall217
        self.VariableUsage219 = VariableUsage219 if VariableUsage219 is not None else set()
        self.VariableUsage222 = VariableUsage222 if VariableUsage222 is not None else set()
        
    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def VariableUsage222(self):
        return self.__VariableUsage222

    @VariableUsage222.setter
    def VariableUsage222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall__VariableUsage222", None)
        self.__VariableUsage222 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "parameter_pc_pc223"):
                    opp_val = getattr(item, "parameter_pc_pc223", None)
                    
                    if opp_val == self:
                        setattr(item, "parameter_pc_pc223", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "parameter_pc_pc223"):
                    opp_val = getattr(item, "parameter_pc_pc223", None)
                    
                    setattr(item, "parameter_pc_pc223", self)
                    

    @property
    def VariableUsage219(self):
        return self.__VariableUsage219

    @VariableUsage219.setter
    def VariableUsage219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall__VariableUsage219", None)
        self.__VariableUsage219 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "parameter_pc_pc220"):
                    opp_val = getattr(item, "parameter_pc_pc220", None)
                    
                    if opp_val == self:
                        setattr(item, "parameter_pc_pc220", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "parameter_pc_pc220"):
                    opp_val = getattr(item, "parameter_pc_pc220", None)
                    
                    setattr(item, "parameter_pc_pc220", self)
                    

    @property
    def pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall(self):
        return self.__pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall

    @pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall.setter
    def pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall__pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall", None)
        self.__pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationProvidedRole215"):
                opp_val = getattr(old_value, "OperationProvidedRole215", None)
                if opp_val == self:
                    setattr(old_value, "OperationProvidedRole215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationProvidedRole215"):
                opp_val = getattr(value, "OperationProvidedRole215", None)
                setattr(value, "OperationProvidedRole215", self)

    @property
    def pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall217(self):
        return self.__pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall217

    @pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall217.setter
    def pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall__pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall217", None)
        self.__pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall217 = value
        
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

    def EntryLevelSystemCallSignatureMustMatchItsProvidedRole(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EntryLevelSystemCallSignatureMustMatchItsProvidedRole method
        pass

    def EntryLevelSystemCallMustReferenceProvidedRoleOfASystem(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EntryLevelSystemCallMustReferenceProvidedRoleOfASystem method
        pass

class UserData:

    pass
class pcm_pc_pc_usagemodel_pc_pc_UsageModel:

    pass
class InfrastructureRequiredRole:

    pass
class InfrastructureProvidedRole:

    pass
class OperationProvidedRole:

    pass
class DelegationConnector:

    pass
class pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector(DelegationConnector):

    pass
class pcm_pc_pc_composition_pc_pc_SinkDelegationConnector(DelegationConnector):

    pass
class pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector(DelegationConnector):

    pass
class pcm_pc_pc_composition_pc_pc_SourceDelegationConnector(DelegationConnector):

    pass
class pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector(DelegationConnector):

    def __init__(self, pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector: "OperationRequiredRole" = None, pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector108: "OperationRequiredRole" = None, pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector111: "composition_pc_pc_AssemblyContext" = None):
        self.pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector = pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector
        self.pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector108 = pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector108
        self.pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector111 = pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector111
        
    @property
    def pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector108(self):
        return self.__pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector108

    @pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector108.setter
    def pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector__pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector108", None)
        self.__pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationRequiredRole109"):
                opp_val = getattr(old_value, "OperationRequiredRole109", None)
                if opp_val == self:
                    setattr(old_value, "OperationRequiredRole109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationRequiredRole109"):
                opp_val = getattr(value, "OperationRequiredRole109", None)
                setattr(value, "OperationRequiredRole109", self)

    @property
    def pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector111(self):
        return self.__pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector111

    @pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector111.setter
    def pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector__pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector111", None)
        self.__pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_pc_pc_AssemblyContext112"):
                opp_val = getattr(old_value, "composition_pc_pc_AssemblyContext112", None)
                if opp_val == self:
                    setattr(old_value, "composition_pc_pc_AssemblyContext112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_pc_pc_AssemblyContext112"):
                opp_val = getattr(value, "composition_pc_pc_AssemblyContext112", None)
                setattr(value, "composition_pc_pc_AssemblyContext112", self)

    @property
    def pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector(self):
        return self.__pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector

    @pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector.setter
    def pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector__pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector", None)
        self.__pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector = value
        
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

    def RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

    def ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame method
        pass

    def RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector method
        pass

class pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector(DelegationConnector):

    pass
class pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector(DelegationConnector):

    def __init__(self, pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector: "OperationProvidedRole" = None, pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector101: "OperationProvidedRole" = None, pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector104: "composition_pc_pc_AssemblyContext" = None):
        self.pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector = pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector
        self.pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector101 = pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector101
        self.pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector104 = pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector104
        
    @property
    def pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector104(self):
        return self.__pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector104

    @pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector104.setter
    def pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector__pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector104", None)
        self.__pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_pc_pc_AssemblyContext105"):
                opp_val = getattr(old_value, "composition_pc_pc_AssemblyContext105", None)
                if opp_val == self:
                    setattr(old_value, "composition_pc_pc_AssemblyContext105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_pc_pc_AssemblyContext105"):
                opp_val = getattr(value, "composition_pc_pc_AssemblyContext105", None)
                setattr(value, "composition_pc_pc_AssemblyContext105", self)

    @property
    def pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector(self):
        return self.__pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector

    @pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector.setter
    def pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector__pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector", None)
        self.__pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector = value
        
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
    def pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector101(self):
        return self.__pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector101

    @pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector101.setter
    def pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector__pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector101", None)
        self.__pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationProvidedRole102"):
                opp_val = getattr(old_value, "OperationProvidedRole102", None)
                if opp_val == self:
                    setattr(old_value, "OperationProvidedRole102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationProvidedRole102"):
                opp_val = getattr(value, "OperationProvidedRole102", None)
                setattr(value, "OperationProvidedRole102", self)

    def ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

    def ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame method
        pass

class OperationRequiredRole:

    pass
class composition_pc_pc_EventChannelSourceConnector:

    pass
class EventGroup:

    pass
class pcm_pc_pc_composition_pc_pc_ResourceRequiredDelegationConnector:

    pass
class composition_pc_pc_Connector:

    pass
class composition_pc_pc_EventChannel:

    pass
class composition_pc_pc_ResourceRequiredDelegationConnector:

    pass
class composition_pc_pc_AssemblyContext:

    pass
class PCMRandomVariable:

    pass
class SinkRole:

    pass
class SourceRole:

    pass
class entity_pc_pc_NamedElement:

    pass
class Identifier:

    pass
class pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF(seff_pc_pc_ServiceEffectSpecification, seff_pc_pc_ResourceDemandingBehaviour, Identifier):

    pass
class pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification(Identifier):

    def __init__(self, failureProbability: float, LinkingResource661: "LinkingResource" = None, pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification: "CommunicationLinkResourceType" = None, PCMRandomVariable666: "PCMRandomVariable" = None, PCMRandomVariable669: "PCMRandomVariable" = None):
        self.failureProbability = failureProbability
        self.LinkingResource661 = LinkingResource661
        self.pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification = pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification
        self.PCMRandomVariable666 = PCMRandomVariable666
        self.PCMRandomVariable669 = PCMRandomVariable669
        
    @property
    def failureProbability(self) -> float:
        return self.__failureProbability

    @failureProbability.setter
    def failureProbability(self, failureProbability: float):
        self.__failureProbability = failureProbability

    @property
    def pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification(self):
        return self.__pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification

    @pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification.setter
    def pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification__pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification", None)
        self.__pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CommunicationLinkResourceType664"):
                opp_val = getattr(old_value, "CommunicationLinkResourceType664", None)
                if opp_val == self:
                    setattr(old_value, "CommunicationLinkResourceType664", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CommunicationLinkResourceType664"):
                opp_val = getattr(value, "CommunicationLinkResourceType664", None)
                setattr(value, "CommunicationLinkResourceType664", self)

    @property
    def PCMRandomVariable669(self):
        return self.__PCMRandomVariable669

    @PCMRandomVariable669.setter
    def PCMRandomVariable669(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification__PCMRandomVariable669", None)
        self.__PCMRandomVariable669 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc_pc670"):
                opp_val = getattr(old_value, "core_pc_pc670", None)
                if opp_val == self:
                    setattr(old_value, "core_pc_pc670", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc_pc670"):
                opp_val = getattr(value, "core_pc_pc670", None)
                setattr(value, "core_pc_pc670", self)

    @property
    def LinkingResource661(self):
        return self.__LinkingResource661

    @LinkingResource661.setter
    def LinkingResource661(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification__LinkingResource661", None)
        self.__LinkingResource661 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_pc_pc662"):
                opp_val = getattr(old_value, "resourceenvironment_pc_pc662", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_pc_pc662", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_pc_pc662"):
                opp_val = getattr(value, "resourceenvironment_pc_pc662", None)
                setattr(value, "resourceenvironment_pc_pc662", self)

    @property
    def PCMRandomVariable666(self):
        return self.__PCMRandomVariable666

    @PCMRandomVariable666.setter
    def PCMRandomVariable666(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification__PCMRandomVariable666", None)
        self.__PCMRandomVariable666 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc_pc667"):
                opp_val = getattr(old_value, "core_pc_pc667", None)
                if opp_val == self:
                    setattr(old_value, "core_pc_pc667", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc_pc667"):
                opp_val = getattr(value, "core_pc_pc667", None)
                setattr(value, "core_pc_pc667", self)

class pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour(Identifier):

    def __init__(self, AbstractLoopAction: "AbstractLoopAction" = None, AbstractBranchTransition: "AbstractBranchTransition" = None, AbstractAction478: set["AbstractAction"] = None):
        self.AbstractLoopAction = AbstractLoopAction
        self.AbstractBranchTransition = AbstractBranchTransition
        self.AbstractAction478 = AbstractAction478 if AbstractAction478 is not None else set()
        
    @property
    def AbstractLoopAction(self):
        return self.__AbstractLoopAction

    @AbstractLoopAction.setter
    def AbstractLoopAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour__AbstractLoopAction", None)
        self.__AbstractLoopAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc_pc474"):
                opp_val = getattr(old_value, "seff_pc_pc474", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc_pc474", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc_pc474"):
                opp_val = getattr(value, "seff_pc_pc474", None)
                setattr(value, "seff_pc_pc474", self)

    @property
    def AbstractBranchTransition(self):
        return self.__AbstractBranchTransition

    @AbstractBranchTransition.setter
    def AbstractBranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour__AbstractBranchTransition", None)
        self.__AbstractBranchTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc_pc476"):
                opp_val = getattr(old_value, "seff_pc_pc476", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc_pc476", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc_pc476"):
                opp_val = getattr(value, "seff_pc_pc476", None)
                setattr(value, "seff_pc_pc476", self)

    @property
    def AbstractAction478(self):
        return self.__AbstractAction478

    @AbstractAction478.setter
    def AbstractAction478(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour__AbstractAction478", None)
        self.__AbstractAction478 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seff_pc_pc479"):
                    opp_val = getattr(item, "seff_pc_pc479", None)
                    
                    if opp_val == self:
                        setattr(item, "seff_pc_pc479", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seff_pc_pc479"):
                    opp_val = getattr(item, "seff_pc_pc479", None)
                    
                    setattr(item, "seff_pc_pc479", self)
                    

    def ExactlyOneStopAction(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ExactlyOneStopAction method
        pass

    def ExactlyOneStartAction(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ExactlyOneStartAction method
        pass

    def EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor method
        pass

class pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification(Identifier):

    def __init__(self, MTTR: float, MTTF: float, requiredByContainer: bool, numberOfReplicas: int, pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification: "SchedulingPolicy" = None, pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification652: "ProcessingResourceType" = None, PCMRandomVariable655: "PCMRandomVariable" = None, ResourceContainer658: "ResourceContainer" = None):
        self.MTTR = MTTR
        self.MTTF = MTTF
        self.requiredByContainer = requiredByContainer
        self.numberOfReplicas = numberOfReplicas
        self.pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification = pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification
        self.pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification652 = pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification652
        self.PCMRandomVariable655 = PCMRandomVariable655
        self.ResourceContainer658 = ResourceContainer658
        
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
    def pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification(self):
        return self.__pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification

    @pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification.setter
    def pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification__pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification", None)
        self.__pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SchedulingPolicy650"):
                opp_val = getattr(old_value, "SchedulingPolicy650", None)
                if opp_val == self:
                    setattr(old_value, "SchedulingPolicy650", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SchedulingPolicy650"):
                opp_val = getattr(value, "SchedulingPolicy650", None)
                setattr(value, "SchedulingPolicy650", self)

    @property
    def ResourceContainer658(self):
        return self.__ResourceContainer658

    @ResourceContainer658.setter
    def ResourceContainer658(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification__ResourceContainer658", None)
        self.__ResourceContainer658 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_pc_pc659"):
                opp_val = getattr(old_value, "resourceenvironment_pc_pc659", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_pc_pc659", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_pc_pc659"):
                opp_val = getattr(value, "resourceenvironment_pc_pc659", None)
                setattr(value, "resourceenvironment_pc_pc659", self)

    @property
    def PCMRandomVariable655(self):
        return self.__PCMRandomVariable655

    @PCMRandomVariable655.setter
    def PCMRandomVariable655(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification__PCMRandomVariable655", None)
        self.__PCMRandomVariable655 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc_pc656"):
                opp_val = getattr(old_value, "core_pc_pc656", None)
                if opp_val == self:
                    setattr(old_value, "core_pc_pc656", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc_pc656"):
                opp_val = getattr(value, "core_pc_pc656", None)
                setattr(value, "core_pc_pc656", self)

    @property
    def pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification652(self):
        return self.__pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification652

    @pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification652.setter
    def pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification652(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification__pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification652", None)
        self.__pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification652 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcessingResourceType653"):
                opp_val = getattr(old_value, "ProcessingResourceType653", None)
                if opp_val == self:
                    setattr(old_value, "ProcessingResourceType653", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessingResourceType653"):
                opp_val = getattr(value, "ProcessingResourceType653", None)
                setattr(value, "ProcessingResourceType653", self)

class pcm_pc_pc_entity_pc_pc_Entity(entity_pc_pc_NamedElement, Identifier):

    pass
class pcm_pc_pc_entity_pc_pc_NamedElement:

    def __init__(self, entityName: str):
        self.entityName = entityName
        
    @property
    def entityName(self) -> str:
        return self.__entityName

    @entityName.setter
    def entityName(self, entityName: str):
        self.__entityName = entityName

class entity_pc_pc_InterfaceProvidingRequiringEntity:

    pass
class composition_pc_pc_ComposedStructure:

    pass
class pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity(composition_pc_pc_ComposedStructure, entity_pc_pc_InterfaceProvidingRequiringEntity):

    def __init__(self, core_pc_pc73: "pcm_pc_pc_composition_pc_pc_ResourceRequiredDelegationConnector", core_pc_pc189: "pcm_pc_pc_composition_pc_pc_AssemblyContext", core_pc_pc83: "pcm_pc_pc_composition_pc_pc_EventChannel", core_pc_pc54: "pcm_pc_pc_composition_pc_pc_Connector"):
        
    def ProvidedRolesMustBeBound(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ProvidedRolesMustBeBound method
        pass

class entity_pc_pc_ResourceProvidedRole:

    pass
class Connector:

    pass
class pcm_pc_pc_composition_pc_pc_AssemblyEventConnector(Connector):

    pass
class pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector(Connector):

    pass
class pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector(Connector):

    pass
class pcm_pc_pc_composition_pc_pc_AssemblyConnector(Connector):

    def __init__(self, pcm_pc_pc_composition_pc_pc_AssemblyConnector122: "OperationRequiredRole" = None, pcm_pc_pc_composition_pc_pc_AssemblyConnector: "composition_pc_pc_AssemblyContext" = None, pcm_pc_pc_composition_pc_pc_AssemblyConnector116: "composition_pc_pc_AssemblyContext" = None, pcm_pc_pc_composition_pc_pc_AssemblyConnector119: "OperationProvidedRole" = None):
        self.pcm_pc_pc_composition_pc_pc_AssemblyConnector122 = pcm_pc_pc_composition_pc_pc_AssemblyConnector122
        self.pcm_pc_pc_composition_pc_pc_AssemblyConnector = pcm_pc_pc_composition_pc_pc_AssemblyConnector
        self.pcm_pc_pc_composition_pc_pc_AssemblyConnector116 = pcm_pc_pc_composition_pc_pc_AssemblyConnector116
        self.pcm_pc_pc_composition_pc_pc_AssemblyConnector119 = pcm_pc_pc_composition_pc_pc_AssemblyConnector119
        
    @property
    def pcm_pc_pc_composition_pc_pc_AssemblyConnector122(self):
        return self.__pcm_pc_pc_composition_pc_pc_AssemblyConnector122

    @pcm_pc_pc_composition_pc_pc_AssemblyConnector122.setter
    def pcm_pc_pc_composition_pc_pc_AssemblyConnector122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_composition_pc_pc_AssemblyConnector__pcm_pc_pc_composition_pc_pc_AssemblyConnector122", None)
        self.__pcm_pc_pc_composition_pc_pc_AssemblyConnector122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationRequiredRole123"):
                opp_val = getattr(old_value, "OperationRequiredRole123", None)
                if opp_val == self:
                    setattr(old_value, "OperationRequiredRole123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationRequiredRole123"):
                opp_val = getattr(value, "OperationRequiredRole123", None)
                setattr(value, "OperationRequiredRole123", self)

    @property
    def pcm_pc_pc_composition_pc_pc_AssemblyConnector116(self):
        return self.__pcm_pc_pc_composition_pc_pc_AssemblyConnector116

    @pcm_pc_pc_composition_pc_pc_AssemblyConnector116.setter
    def pcm_pc_pc_composition_pc_pc_AssemblyConnector116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_composition_pc_pc_AssemblyConnector__pcm_pc_pc_composition_pc_pc_AssemblyConnector116", None)
        self.__pcm_pc_pc_composition_pc_pc_AssemblyConnector116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_pc_pc_AssemblyContext117"):
                opp_val = getattr(old_value, "composition_pc_pc_AssemblyContext117", None)
                if opp_val == self:
                    setattr(old_value, "composition_pc_pc_AssemblyContext117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_pc_pc_AssemblyContext117"):
                opp_val = getattr(value, "composition_pc_pc_AssemblyContext117", None)
                setattr(value, "composition_pc_pc_AssemblyContext117", self)

    @property
    def pcm_pc_pc_composition_pc_pc_AssemblyConnector(self):
        return self.__pcm_pc_pc_composition_pc_pc_AssemblyConnector

    @pcm_pc_pc_composition_pc_pc_AssemblyConnector.setter
    def pcm_pc_pc_composition_pc_pc_AssemblyConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_composition_pc_pc_AssemblyConnector__pcm_pc_pc_composition_pc_pc_AssemblyConnector", None)
        self.__pcm_pc_pc_composition_pc_pc_AssemblyConnector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_pc_pc_AssemblyContext114"):
                opp_val = getattr(old_value, "composition_pc_pc_AssemblyContext114", None)
                if opp_val == self:
                    setattr(old_value, "composition_pc_pc_AssemblyContext114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_pc_pc_AssemblyContext114"):
                opp_val = getattr(value, "composition_pc_pc_AssemblyContext114", None)
                setattr(value, "composition_pc_pc_AssemblyContext114", self)

    @property
    def pcm_pc_pc_composition_pc_pc_AssemblyConnector119(self):
        return self.__pcm_pc_pc_composition_pc_pc_AssemblyConnector119

    @pcm_pc_pc_composition_pc_pc_AssemblyConnector119.setter
    def pcm_pc_pc_composition_pc_pc_AssemblyConnector119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_composition_pc_pc_AssemblyConnector__pcm_pc_pc_composition_pc_pc_AssemblyConnector119", None)
        self.__pcm_pc_pc_composition_pc_pc_AssemblyConnector119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationProvidedRole120"):
                opp_val = getattr(old_value, "OperationProvidedRole120", None)
                if opp_val == self:
                    setattr(old_value, "OperationProvidedRole120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationProvidedRole120"):
                opp_val = getattr(value, "OperationProvidedRole120", None)
                setattr(value, "OperationProvidedRole120", self)

    def AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch method
        pass

    def AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch method
        pass

    def AssemblyConnectorsReferencedInterfacesMustMatch(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AssemblyConnectorsReferencedInterfacesMustMatch method
        pass

class pcm_pc_pc_composition_pc_pc_EventChannelSourceConnector(Connector):

    pass
class pcm_pc_pc_composition_pc_pc_DelegationConnector(Connector):

    pass
class entity_pc_pc_InterfaceRequiringEntity:

    pass
class entity_pc_pc_InterfaceProvidingEntity:

    pass
class pcm_pc_pc_entity_pc_pc_InterfaceProvidingRequiringEntity(entity_pc_pc_InterfaceRequiringEntity, entity_pc_pc_InterfaceProvidingEntity):

    pass
class ResourceInterface:

    pass
class entity_pc_pc_ResourceInterfaceProvidingEntity:

    pass
class Role:

    pass
class pcm_pc_pc_repository_pc_pc_ProvidedRole(Role):

    pass
class pcm_pc_pc_repository_pc_pc_RequiredRole(Role):

    pass
class pcm_pc_pc_entity_pc_pc_ResourceProvidedRole(Role):

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
class pcm_pc_pc_entity_pc_pc_ResourceRequiredRole(Role):

    pass
class entity_pc_pc_ResourceRequiredRole:

    pass
class RequiredRole:

    pass
class pcm_pc_pc_repository_pc_pc_InfrastructureRequiredRole(RequiredRole):

    pass
class pcm_pc_pc_repository_pc_pc_OperationRequiredRole(RequiredRole):

    pass
class pcm_pc_pc_repository_pc_pc_SourceRole(RequiredRole):

    pass
class entity_pc_pc_ResourceInterfaceRequiringEntity:

    pass
class pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingRequiringEntity(entity_pc_pc_ResourceInterfaceRequiringEntity, entity_pc_pc_ResourceInterfaceProvidingEntity):

    pass
class entity_pc_pc_Entity:

    pass
class pcm_pc_pc_repository_pc_pc_CompositeDataType(repository_pc_pc_DataType, entity_pc_pc_Entity):

    pass
class pcm_pc_pc_repository_pc_pc_CollectionDataType(repository_pc_pc_DataType, entity_pc_pc_Entity):

    pass
class pcm_pc_pc_resourcetype_pc_pc_ResourceType(entity_pc_pc_ResourceInterfaceProvidingEntity, UnitCarryingElement, entity_pc_pc_Entity):

    pass
class pcm_pc_pc_system_pc_pc_System(entity_pc_pc_ComposedProvidingRequiringEntity, entity_pc_pc_Entity):

    def __init__(self, QoSAnnotations624: set["QoSAnnotations"] = None):
        self.QoSAnnotations624 = QoSAnnotations624 if QoSAnnotations624 is not None else set()
        
    @property
    def QoSAnnotations624(self):
        return self.__QoSAnnotations624

    @QoSAnnotations624.setter
    def QoSAnnotations624(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_system_pc_pc_System__QoSAnnotations624", None)
        self.__QoSAnnotations624 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qosannotations_pc_pc625"):
                    opp_val = getattr(item, "qosannotations_pc_pc625", None)
                    
                    if opp_val == self:
                        setattr(item, "qosannotations_pc_pc625", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qosannotations_pc_pc625"):
                    opp_val = getattr(item, "qosannotations_pc_pc625", None)
                    
                    setattr(item, "qosannotations_pc_pc625", self)
                    

    def SystemMustHaveAtLeastOneProvidedRole(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SystemMustHaveAtLeastOneProvidedRole method
        pass

class pcm_pc_pc_entity_pc_pc_InterfaceRequiringEntity(entity_pc_pc_ResourceInterfaceRequiringEntity, entity_pc_pc_Entity):

    pass
class ProvidedRole:

    pass
class pcm_pc_pc_repository_pc_pc_SinkRole(ProvidedRole):

    pass
class pcm_pc_pc_repository_pc_pc_InfrastructureProvidedRole(ProvidedRole):

    pass
class pcm_pc_pc_repository_pc_pc_OperationProvidedRole(ProvidedRole):

    pass
class Entity:

    pass
class pcm_pc_pc_seff_pc_pc_AbstractBranchTransition(Entity):

    pass
class pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingEntity(Entity):

    pass
class pcm_pc_pc_resourceenvironment_pc_pc_ResourceContainer(Entity):

    pass
class pcm_pc_pc_composition_pc_pc_ComposedStructure(Entity):

    def __init__(self, composition_pc_pc56: set["composition_pc_pc_AssemblyContext"] = None, composition_pc_pc59: set["composition_pc_pc_ResourceRequiredDelegationConnector"] = None, composition_pc_pc62: set["composition_pc_pc_EventChannel"] = None, composition_pc_pc65: set["composition_pc_pc_Connector"] = None):
        self.composition_pc_pc56 = composition_pc_pc56 if composition_pc_pc56 is not None else set()
        self.composition_pc_pc59 = composition_pc_pc59 if composition_pc_pc59 is not None else set()
        self.composition_pc_pc62 = composition_pc_pc62 if composition_pc_pc62 is not None else set()
        self.composition_pc_pc65 = composition_pc_pc65 if composition_pc_pc65 is not None else set()
        
    @property
    def composition_pc_pc59(self):
        return self.__composition_pc_pc59

    @composition_pc_pc59.setter
    def composition_pc_pc59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_composition_pc_pc_ComposedStructure__composition_pc_pc59", None)
        self.__composition_pc_pc59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_pc_pc60"):
                    opp_val = getattr(item, "core_pc_pc60", None)
                    
                    if opp_val == self:
                        setattr(item, "core_pc_pc60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_pc_pc60"):
                    opp_val = getattr(item, "core_pc_pc60", None)
                    
                    setattr(item, "core_pc_pc60", self)
                    

    @property
    def composition_pc_pc56(self):
        return self.__composition_pc_pc56

    @composition_pc_pc56.setter
    def composition_pc_pc56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_composition_pc_pc_ComposedStructure__composition_pc_pc56", None)
        self.__composition_pc_pc56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_pc_pc57"):
                    opp_val = getattr(item, "core_pc_pc57", None)
                    
                    if opp_val == self:
                        setattr(item, "core_pc_pc57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_pc_pc57"):
                    opp_val = getattr(item, "core_pc_pc57", None)
                    
                    setattr(item, "core_pc_pc57", self)
                    

    @property
    def composition_pc_pc62(self):
        return self.__composition_pc_pc62

    @composition_pc_pc62.setter
    def composition_pc_pc62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_composition_pc_pc_ComposedStructure__composition_pc_pc62", None)
        self.__composition_pc_pc62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_pc_pc63"):
                    opp_val = getattr(item, "core_pc_pc63", None)
                    
                    if opp_val == self:
                        setattr(item, "core_pc_pc63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_pc_pc63"):
                    opp_val = getattr(item, "core_pc_pc63", None)
                    
                    setattr(item, "core_pc_pc63", self)
                    

    @property
    def composition_pc_pc65(self):
        return self.__composition_pc_pc65

    @composition_pc_pc65.setter
    def composition_pc_pc65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_composition_pc_pc_ComposedStructure__composition_pc_pc65", None)
        self.__composition_pc_pc65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_pc_pc66"):
                    opp_val = getattr(item, "core_pc_pc66", None)
                    
                    if opp_val == self:
                        setattr(item, "core_pc_pc66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_pc_pc66"):
                    opp_val = getattr(item, "core_pc_pc66", None)
                    
                    setattr(item, "core_pc_pc66", self)
                    

    def MultipleConnectorsConstraintForAssemblyConnectors(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MultipleConnectorsConstraintForAssemblyConnectors method
        pass

    def MultipleConnectorsConstraint(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MultipleConnectorsConstraint method
        pass

class pcm_pc_pc_resourcetype_pc_pc_SchedulingPolicy(Entity):

    pass
class pcm_pc_pc_repository_pc_pc_Signature(Entity):

    pass
class pcm_pc_pc_seff_pc_pc_AbstractAction(Entity):

    pass
class pcm_pc_pc_seff_reliability_pc_pc_FailureHandlingEntity(Entity):

    pass
class pcm_pc_pc_resourcetype_pc_pc_ResourceInterface(Entity):

    pass
class pcm_pc_pc_allocation_pc_pc_Allocation(Entity):

    def __init__(self, pcm_pc_pc_allocation_pc_pc_Allocation: "ResourceEnvironment" = None, pcm_pc_pc_allocation_pc_pc_Allocation682: "System" = None, AllocationContext: set["AllocationContext"] = None):
        self.pcm_pc_pc_allocation_pc_pc_Allocation = pcm_pc_pc_allocation_pc_pc_Allocation
        self.pcm_pc_pc_allocation_pc_pc_Allocation682 = pcm_pc_pc_allocation_pc_pc_Allocation682
        self.AllocationContext = AllocationContext if AllocationContext is not None else set()
        
    @property
    def AllocationContext(self):
        return self.__AllocationContext

    @AllocationContext.setter
    def AllocationContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_allocation_pc_pc_Allocation__AllocationContext", None)
        self.__AllocationContext = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "allocation_pc_pc685"):
                    opp_val = getattr(item, "allocation_pc_pc685", None)
                    
                    if opp_val == self:
                        setattr(item, "allocation_pc_pc685", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "allocation_pc_pc685"):
                    opp_val = getattr(item, "allocation_pc_pc685", None)
                    
                    setattr(item, "allocation_pc_pc685", self)
                    

    @property
    def pcm_pc_pc_allocation_pc_pc_Allocation682(self):
        return self.__pcm_pc_pc_allocation_pc_pc_Allocation682

    @pcm_pc_pc_allocation_pc_pc_Allocation682.setter
    def pcm_pc_pc_allocation_pc_pc_Allocation682(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_allocation_pc_pc_Allocation__pcm_pc_pc_allocation_pc_pc_Allocation682", None)
        self.__pcm_pc_pc_allocation_pc_pc_Allocation682 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "System683"):
                opp_val = getattr(old_value, "System683", None)
                if opp_val == self:
                    setattr(old_value, "System683", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "System683"):
                opp_val = getattr(value, "System683", None)
                setattr(value, "System683", self)

    @property
    def pcm_pc_pc_allocation_pc_pc_Allocation(self):
        return self.__pcm_pc_pc_allocation_pc_pc_Allocation

    @pcm_pc_pc_allocation_pc_pc_Allocation.setter
    def pcm_pc_pc_allocation_pc_pc_Allocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_allocation_pc_pc_Allocation__pcm_pc_pc_allocation_pc_pc_Allocation", None)
        self.__pcm_pc_pc_allocation_pc_pc_Allocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceEnvironment680"):
                opp_val = getattr(old_value, "ResourceEnvironment680", None)
                if opp_val == self:
                    setattr(old_value, "ResourceEnvironment680", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceEnvironment680"):
                opp_val = getattr(value, "ResourceEnvironment680", None)
                setattr(value, "ResourceEnvironment680", self)

    def EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce method
        pass

    def CommunicatingServersHaveToBeConnectedByLinkingResource(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement CommunicatingServersHaveToBeConnectedByLinkingResource method
        pass

class pcm_pc_pc_allocation_pc_pc_AllocationContext(Entity):

    def __init__(self, pcm_pc_pc_allocation_pc_pc_AllocationContext: "ResourceContainer" = None, pcm_pc_pc_allocation_pc_pc_AllocationContext674: "composition_pc_pc_AssemblyContext" = None, Allocation: "Allocation" = None, pcm_pc_pc_allocation_pc_pc_AllocationContext678: "composition_pc_pc_EventChannel" = None):
        self.pcm_pc_pc_allocation_pc_pc_AllocationContext = pcm_pc_pc_allocation_pc_pc_AllocationContext
        self.pcm_pc_pc_allocation_pc_pc_AllocationContext674 = pcm_pc_pc_allocation_pc_pc_AllocationContext674
        self.Allocation = Allocation
        self.pcm_pc_pc_allocation_pc_pc_AllocationContext678 = pcm_pc_pc_allocation_pc_pc_AllocationContext678
        
    @property
    def pcm_pc_pc_allocation_pc_pc_AllocationContext(self):
        return self.__pcm_pc_pc_allocation_pc_pc_AllocationContext

    @pcm_pc_pc_allocation_pc_pc_AllocationContext.setter
    def pcm_pc_pc_allocation_pc_pc_AllocationContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_allocation_pc_pc_AllocationContext__pcm_pc_pc_allocation_pc_pc_AllocationContext", None)
        self.__pcm_pc_pc_allocation_pc_pc_AllocationContext = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceContainer672"):
                opp_val = getattr(old_value, "ResourceContainer672", None)
                if opp_val == self:
                    setattr(old_value, "ResourceContainer672", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceContainer672"):
                opp_val = getattr(value, "ResourceContainer672", None)
                setattr(value, "ResourceContainer672", self)

    @property
    def pcm_pc_pc_allocation_pc_pc_AllocationContext674(self):
        return self.__pcm_pc_pc_allocation_pc_pc_AllocationContext674

    @pcm_pc_pc_allocation_pc_pc_AllocationContext674.setter
    def pcm_pc_pc_allocation_pc_pc_AllocationContext674(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_allocation_pc_pc_AllocationContext__pcm_pc_pc_allocation_pc_pc_AllocationContext674", None)
        self.__pcm_pc_pc_allocation_pc_pc_AllocationContext674 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_pc_pc_AssemblyContext675"):
                opp_val = getattr(old_value, "composition_pc_pc_AssemblyContext675", None)
                if opp_val == self:
                    setattr(old_value, "composition_pc_pc_AssemblyContext675", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_pc_pc_AssemblyContext675"):
                opp_val = getattr(value, "composition_pc_pc_AssemblyContext675", None)
                setattr(value, "composition_pc_pc_AssemblyContext675", self)

    @property
    def pcm_pc_pc_allocation_pc_pc_AllocationContext678(self):
        return self.__pcm_pc_pc_allocation_pc_pc_AllocationContext678

    @pcm_pc_pc_allocation_pc_pc_AllocationContext678.setter
    def pcm_pc_pc_allocation_pc_pc_AllocationContext678(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_allocation_pc_pc_AllocationContext__pcm_pc_pc_allocation_pc_pc_AllocationContext678", None)
        self.__pcm_pc_pc_allocation_pc_pc_AllocationContext678 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_pc_pc_EventChannel"):
                opp_val = getattr(old_value, "composition_pc_pc_EventChannel", None)
                if opp_val == self:
                    setattr(old_value, "composition_pc_pc_EventChannel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_pc_pc_EventChannel"):
                opp_val = getattr(value, "composition_pc_pc_EventChannel", None)
                setattr(value, "composition_pc_pc_EventChannel", self)

    @property
    def Allocation(self):
        return self.__Allocation

    @Allocation.setter
    def Allocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_allocation_pc_pc_AllocationContext__Allocation", None)
        self.__Allocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "allocation_pc_pc"):
                opp_val = getattr(old_value, "allocation_pc_pc", None)
                if opp_val == self:
                    setattr(old_value, "allocation_pc_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "allocation_pc_pc"):
                opp_val = getattr(value, "allocation_pc_pc", None)
                setattr(value, "allocation_pc_pc", self)

    def OneAssemblyContextOrOneEventChannelShouldBeReferred(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement OneAssemblyContextOrOneEventChannelShouldBeReferred method
        pass

class pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour(Entity):

    def __init__(self, UsageScenario233: "UsageScenario" = None, BranchTransition: "BranchTransition" = None, Loop238: "Loop" = None, AbstractUserAction241: set["AbstractUserAction"] = None):
        self.UsageScenario233 = UsageScenario233
        self.BranchTransition = BranchTransition
        self.Loop238 = Loop238
        self.AbstractUserAction241 = AbstractUserAction241 if AbstractUserAction241 is not None else set()
        
    @property
    def Loop238(self):
        return self.__Loop238

    @Loop238.setter
    def Loop238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour__Loop238", None)
        self.__Loop238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc_pc239"):
                opp_val = getattr(old_value, "usagemodel_pc_pc239", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc_pc239", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc_pc239"):
                opp_val = getattr(value, "usagemodel_pc_pc239", None)
                setattr(value, "usagemodel_pc_pc239", self)

    @property
    def BranchTransition(self):
        return self.__BranchTransition

    @BranchTransition.setter
    def BranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour__BranchTransition", None)
        self.__BranchTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc_pc236"):
                opp_val = getattr(old_value, "usagemodel_pc_pc236", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc_pc236", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc_pc236"):
                opp_val = getattr(value, "usagemodel_pc_pc236", None)
                setattr(value, "usagemodel_pc_pc236", self)

    @property
    def UsageScenario233(self):
        return self.__UsageScenario233

    @UsageScenario233.setter
    def UsageScenario233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour__UsageScenario233", None)
        self.__UsageScenario233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc_pc234"):
                opp_val = getattr(old_value, "usagemodel_pc_pc234", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc_pc234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc_pc234"):
                opp_val = getattr(value, "usagemodel_pc_pc234", None)
                setattr(value, "usagemodel_pc_pc234", self)

    @property
    def AbstractUserAction241(self):
        return self.__AbstractUserAction241

    @AbstractUserAction241.setter
    def AbstractUserAction241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour__AbstractUserAction241", None)
        self.__AbstractUserAction241 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "usagemodel_pc_pc242"):
                    opp_val = getattr(item, "usagemodel_pc_pc242", None)
                    
                    if opp_val == self:
                        setattr(item, "usagemodel_pc_pc242", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "usagemodel_pc_pc242"):
                    opp_val = getattr(item, "usagemodel_pc_pc242", None)
                    
                    setattr(item, "usagemodel_pc_pc242", self)
                    

    def EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor method
        pass

    def Exactlyonestart(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement Exactlyonestart method
        pass

    def Exactlyonestop(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement Exactlyonestop method
        pass

class pcm_pc_pc_usagemodel_pc_pc_UsageScenario(Entity):

    pass
class pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations(Entity):

    def __init__(self, SpecifiedOutputParameterAbstraction600: set["SpecifiedOutputParameterAbstraction"] = None, System: "System" = None, SpecifiedQoSAnnotation: set["SpecifiedQoSAnnotation"] = None):
        self.SpecifiedOutputParameterAbstraction600 = SpecifiedOutputParameterAbstraction600 if SpecifiedOutputParameterAbstraction600 is not None else set()
        self.System = System
        self.SpecifiedQoSAnnotation = SpecifiedQoSAnnotation if SpecifiedQoSAnnotation is not None else set()
        
    @property
    def System(self):
        return self.__System

    @System.setter
    def System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations__System", None)
        self.__System = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system_pc_pc"):
                opp_val = getattr(old_value, "system_pc_pc", None)
                if opp_val == self:
                    setattr(old_value, "system_pc_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system_pc_pc"):
                opp_val = getattr(value, "system_pc_pc", None)
                setattr(value, "system_pc_pc", self)

    @property
    def SpecifiedQoSAnnotation(self):
        return self.__SpecifiedQoSAnnotation

    @SpecifiedQoSAnnotation.setter
    def SpecifiedQoSAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations__SpecifiedQoSAnnotation", None)
        self.__SpecifiedQoSAnnotation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qosannotations_pc_pc604"):
                    opp_val = getattr(item, "qosannotations_pc_pc604", None)
                    
                    if opp_val == self:
                        setattr(item, "qosannotations_pc_pc604", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qosannotations_pc_pc604"):
                    opp_val = getattr(item, "qosannotations_pc_pc604", None)
                    
                    setattr(item, "qosannotations_pc_pc604", self)
                    

    @property
    def SpecifiedOutputParameterAbstraction600(self):
        return self.__SpecifiedOutputParameterAbstraction600

    @SpecifiedOutputParameterAbstraction600.setter
    def SpecifiedOutputParameterAbstraction600(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations__SpecifiedOutputParameterAbstraction600", None)
        self.__SpecifiedOutputParameterAbstraction600 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qosannotations_pc_pc601"):
                    opp_val = getattr(item, "qosannotations_pc_pc601", None)
                    
                    if opp_val == self:
                        setattr(item, "qosannotations_pc_pc601", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qosannotations_pc_pc601"):
                    opp_val = getattr(item, "qosannotations_pc_pc601", None)
                    
                    setattr(item, "qosannotations_pc_pc601", self)
                    

    def MultipleReliabilityAnnotationsPerExternalCallNotAllowed(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MultipleReliabilityAnnotationsPerExternalCallNotAllowed method
        pass

class pcm_pc_pc_reliability_pc_pc_FailureType(Entity):

    pass
class pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction(Entity):

    pass
class pcm_pc_pc_composition_pc_pc_Connector(Entity):

    pass
class pcm_pc_pc_repository_pc_pc_PassiveResource(Entity):

    pass
class pcm_pc_pc_repository_pc_pc_Interface(Entity):

    def __init__(self, Repository315: "Repository" = None, pcm_pc_pc_repository_pc_pc_Interface: set["Interface"] = None, pcm_pc_pc_repository_pc_pc_Interface311: set["Protocol"] = None, RequiredCharacterisation: set["RequiredCharacterisation"] = None):
        self.Repository315 = Repository315
        self.pcm_pc_pc_repository_pc_pc_Interface = pcm_pc_pc_repository_pc_pc_Interface if pcm_pc_pc_repository_pc_pc_Interface is not None else set()
        self.pcm_pc_pc_repository_pc_pc_Interface311 = pcm_pc_pc_repository_pc_pc_Interface311 if pcm_pc_pc_repository_pc_pc_Interface311 is not None else set()
        self.RequiredCharacterisation = RequiredCharacterisation if RequiredCharacterisation is not None else set()
        
    @property
    def pcm_pc_pc_repository_pc_pc_Interface(self):
        return self.__pcm_pc_pc_repository_pc_pc_Interface

    @pcm_pc_pc_repository_pc_pc_Interface.setter
    def pcm_pc_pc_repository_pc_pc_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_Interface__pcm_pc_pc_repository_pc_pc_Interface", None)
        self.__pcm_pc_pc_repository_pc_pc_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Interface309"):
                    opp_val = getattr(item, "Interface309", None)
                    
                    if opp_val == self:
                        setattr(item, "Interface309", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Interface309"):
                    opp_val = getattr(item, "Interface309", None)
                    
                    setattr(item, "Interface309", self)
                    

    @property
    def pcm_pc_pc_repository_pc_pc_Interface311(self):
        return self.__pcm_pc_pc_repository_pc_pc_Interface311

    @pcm_pc_pc_repository_pc_pc_Interface311.setter
    def pcm_pc_pc_repository_pc_pc_Interface311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_Interface__pcm_pc_pc_repository_pc_pc_Interface311", None)
        self.__pcm_pc_pc_repository_pc_pc_Interface311 = value if value is not None else set()
        
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
    def Repository315(self):
        return self.__Repository315

    @Repository315.setter
    def Repository315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_Interface__Repository315", None)
        self.__Repository315 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc_pc316"):
                opp_val = getattr(old_value, "repository_pc_pc316", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc_pc316", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc_pc316"):
                opp_val = getattr(value, "repository_pc_pc316", None)
                setattr(value, "repository_pc_pc316", self)

    @property
    def RequiredCharacterisation(self):
        return self.__RequiredCharacterisation

    @RequiredCharacterisation.setter
    def RequiredCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_Interface__RequiredCharacterisation", None)
        self.__RequiredCharacterisation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_pc_pc313"):
                    opp_val = getattr(item, "repository_pc_pc313", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_pc_pc313", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_pc_pc313"):
                    opp_val = getattr(item, "repository_pc_pc313", None)
                    
                    setattr(item, "repository_pc_pc313", self)
                    

    def NoProtocolTypeIDUsedTwice(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NoProtocolTypeIDUsedTwice method
        pass

class pcm_pc_pc_resourceenvironment_pc_pc_LinkingResource(Entity):

    pass
class pcm_pc_pc_repository_pc_pc_Role(Entity):

    pass
class pcm_pc_pc_composition_pc_pc_EventChannel(Entity):

    pass
class pcm_pc_pc_resourcetype_pc_pc_ResourceSignature(Entity):

    def __init__(self, resourceServiceId: int, Parameter379: "Parameter" = None, ResourceInterface382: "ResourceInterface" = None):
        self.resourceServiceId = resourceServiceId
        self.Parameter379 = Parameter379
        self.ResourceInterface382 = ResourceInterface382
        
    @property
    def resourceServiceId(self) -> int:
        return self.__resourceServiceId

    @resourceServiceId.setter
    def resourceServiceId(self, resourceServiceId: int):
        self.__resourceServiceId = resourceServiceId

    @property
    def Parameter379(self):
        return self.__Parameter379

    @Parameter379.setter
    def Parameter379(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_resourcetype_pc_pc_ResourceSignature__Parameter379", None)
        self.__Parameter379 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc_pc380"):
                opp_val = getattr(old_value, "repository_pc_pc380", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc_pc380", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc_pc380"):
                opp_val = getattr(value, "repository_pc_pc380", None)
                setattr(value, "repository_pc_pc380", self)

    @property
    def ResourceInterface382(self):
        return self.__ResourceInterface382

    @ResourceInterface382.setter
    def ResourceInterface382(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_resourcetype_pc_pc_ResourceSignature__ResourceInterface382", None)
        self.__ResourceInterface382 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcetype_pc_pc383"):
                opp_val = getattr(old_value, "resourcetype_pc_pc383", None)
                if opp_val == self:
                    setattr(old_value, "resourcetype_pc_pc383", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcetype_pc_pc383"):
                opp_val = getattr(value, "resourcetype_pc_pc383", None)
                setattr(value, "resourcetype_pc_pc383", self)

class pcm_pc_pc_entity_pc_pc_ResourceInterfaceRequiringEntity(Entity):

    pass
class pcm_pc_pc_repository_pc_pc_Repository(Entity):

    def __init__(self, repositoryDescription: str, RepositoryComponent299: set["RepositoryComponent"] = None, Interface: set["Interface"] = None, FailureType: set["FailureType"] = None, DataType306: set["DataType"] = None):
        self.repositoryDescription = repositoryDescription
        self.RepositoryComponent299 = RepositoryComponent299 if RepositoryComponent299 is not None else set()
        self.Interface = Interface if Interface is not None else set()
        self.FailureType = FailureType if FailureType is not None else set()
        self.DataType306 = DataType306 if DataType306 is not None else set()
        
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
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_Repository__FailureType", None)
        self.__FailureType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reliability_pc_pc304"):
                    opp_val = getattr(item, "reliability_pc_pc304", None)
                    
                    if opp_val == self:
                        setattr(item, "reliability_pc_pc304", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reliability_pc_pc304"):
                    opp_val = getattr(item, "reliability_pc_pc304", None)
                    
                    setattr(item, "reliability_pc_pc304", self)
                    

    @property
    def RepositoryComponent299(self):
        return self.__RepositoryComponent299

    @RepositoryComponent299.setter
    def RepositoryComponent299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_Repository__RepositoryComponent299", None)
        self.__RepositoryComponent299 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_pc_pc300"):
                    opp_val = getattr(item, "repository_pc_pc300", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_pc_pc300", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_pc_pc300"):
                    opp_val = getattr(item, "repository_pc_pc300", None)
                    
                    setattr(item, "repository_pc_pc300", self)
                    

    @property
    def Interface(self):
        return self.__Interface

    @Interface.setter
    def Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_Repository__Interface", None)
        self.__Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_pc_pc302"):
                    opp_val = getattr(item, "repository_pc_pc302", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_pc_pc302", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_pc_pc302"):
                    opp_val = getattr(item, "repository_pc_pc302", None)
                    
                    setattr(item, "repository_pc_pc302", self)
                    

    @property
    def DataType306(self):
        return self.__DataType306

    @DataType306.setter
    def DataType306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_Repository__DataType306", None)
        self.__DataType306 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository_pc_pc307"):
                    opp_val = getattr(item, "repository_pc_pc307", None)
                    
                    if opp_val == self:
                        setattr(item, "repository_pc_pc307", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository_pc_pc307"):
                    opp_val = getattr(item, "repository_pc_pc307", None)
                    
                    setattr(item, "repository_pc_pc307", self)
                    

class pcm_pc_pc_composition_pc_pc_AssemblyContext(Entity):

    pass
class pcm_pc_pc_entity_pc_pc_InterfaceProvidingEntity(Entity):

    pass
class seff_performance_pc_pc_InfrastructureCall:

    pass
class VariableCharacterisation:

    pass
class PassiveResource:

    pass
class ClosedWorkload:

    pass
class RandomVariable:

    pass
class pcm_pc_pc_core_pc_pc_PCMRandomVariable(RandomVariable):

    def __init__(self, seff_performance_pc_pc8: "seff_performance_pc_pc_ResourceCall" = None, seff_performance_pc_pc11: "seff_performance_pc_pc_ParametricResourceDemand" = None, LoopAction: "LoopAction" = None, GuardedBranchTransition: "GuardedBranchTransition" = None, qos_performance_pc_pc: "qos_performance_pc_pc_SpecifiedExecutionTime" = None, composition_pc_pc: "composition_pc_pc_EventChannelSinkConnector" = None, composition_pc_pc20: "composition_pc_pc_AssemblyEventConnector" = None, ClosedWorkload: "ClosedWorkload" = None, PassiveResource: "PassiveResource" = None, VariableCharacterisation: "VariableCharacterisation" = None, seff_performance_pc_pc: "seff_performance_pc_pc_InfrastructureCall" = None, Loop: "Loop" = None, OpenWorkload: "OpenWorkload" = None, Delay: "Delay" = None, CommunicationLinkResourceSpecification: "CommunicationLinkResourceSpecification" = None, ProcessingResourceSpecification: "ProcessingResourceSpecification" = None, CommunicationLinkResourceSpecification32: "CommunicationLinkResourceSpecification" = None):
        self.seff_performance_pc_pc8 = seff_performance_pc_pc8
        self.seff_performance_pc_pc11 = seff_performance_pc_pc11
        self.LoopAction = LoopAction
        self.GuardedBranchTransition = GuardedBranchTransition
        self.qos_performance_pc_pc = qos_performance_pc_pc
        self.composition_pc_pc = composition_pc_pc
        self.composition_pc_pc20 = composition_pc_pc20
        self.ClosedWorkload = ClosedWorkload
        self.PassiveResource = PassiveResource
        self.VariableCharacterisation = VariableCharacterisation
        self.seff_performance_pc_pc = seff_performance_pc_pc
        self.Loop = Loop
        self.OpenWorkload = OpenWorkload
        self.Delay = Delay
        self.CommunicationLinkResourceSpecification = CommunicationLinkResourceSpecification
        self.ProcessingResourceSpecification = ProcessingResourceSpecification
        self.CommunicationLinkResourceSpecification32 = CommunicationLinkResourceSpecification32
        
    @property
    def seff_performance_pc_pc11(self):
        return self.__seff_performance_pc_pc11

    @seff_performance_pc_pc11.setter
    def seff_performance_pc_pc11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__seff_performance_pc_pc11", None)
        self.__seff_performance_pc_pc11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc_pc12"):
                opp_val = getattr(old_value, "seff_pc_pc12", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc_pc12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc_pc12"):
                opp_val = getattr(value, "seff_pc_pc12", None)
                setattr(value, "seff_pc_pc12", self)

    @property
    def LoopAction(self):
        return self.__LoopAction

    @LoopAction.setter
    def LoopAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__LoopAction", None)
        self.__LoopAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc_pc14"):
                opp_val = getattr(old_value, "seff_pc_pc14", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc_pc14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc_pc14"):
                opp_val = getattr(value, "seff_pc_pc14", None)
                setattr(value, "seff_pc_pc14", self)

    @property
    def ClosedWorkload(self):
        return self.__ClosedWorkload

    @ClosedWorkload.setter
    def ClosedWorkload(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__ClosedWorkload", None)
        self.__ClosedWorkload = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc_pc"):
                opp_val = getattr(old_value, "usagemodel_pc_pc", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc_pc"):
                opp_val = getattr(value, "usagemodel_pc_pc", None)
                setattr(value, "usagemodel_pc_pc", self)

    @property
    def composition_pc_pc20(self):
        return self.__composition_pc_pc20

    @composition_pc_pc20.setter
    def composition_pc_pc20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__composition_pc_pc20", None)
        self.__composition_pc_pc20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc_pc21"):
                opp_val = getattr(old_value, "core_pc_pc21", None)
                if opp_val == self:
                    setattr(old_value, "core_pc_pc21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc_pc21"):
                opp_val = getattr(value, "core_pc_pc21", None)
                setattr(value, "core_pc_pc21", self)

    @property
    def seff_performance_pc_pc(self):
        return self.__seff_performance_pc_pc

    @seff_performance_pc_pc.setter
    def seff_performance_pc_pc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__seff_performance_pc_pc", None)
        self.__seff_performance_pc_pc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc_pc"):
                opp_val = getattr(old_value, "seff_pc_pc", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc_pc"):
                opp_val = getattr(value, "seff_pc_pc", None)
                setattr(value, "seff_pc_pc", self)

    @property
    def VariableCharacterisation(self):
        return self.__VariableCharacterisation

    @VariableCharacterisation.setter
    def VariableCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__VariableCharacterisation", None)
        self.__VariableCharacterisation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameter_pc_pc"):
                opp_val = getattr(old_value, "parameter_pc_pc", None)
                if opp_val == self:
                    setattr(old_value, "parameter_pc_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameter_pc_pc"):
                opp_val = getattr(value, "parameter_pc_pc", None)
                setattr(value, "parameter_pc_pc", self)

    @property
    def Loop(self):
        return self.__Loop

    @Loop.setter
    def Loop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__Loop", None)
        self.__Loop = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc_pc23"):
                opp_val = getattr(old_value, "usagemodel_pc_pc23", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc_pc23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc_pc23"):
                opp_val = getattr(value, "usagemodel_pc_pc23", None)
                setattr(value, "usagemodel_pc_pc23", self)

    @property
    def PassiveResource(self):
        return self.__PassiveResource

    @PassiveResource.setter
    def PassiveResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__PassiveResource", None)
        self.__PassiveResource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository_pc_pc"):
                opp_val = getattr(old_value, "repository_pc_pc", None)
                if opp_val == self:
                    setattr(old_value, "repository_pc_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository_pc_pc"):
                opp_val = getattr(value, "repository_pc_pc", None)
                setattr(value, "repository_pc_pc", self)

    @property
    def composition_pc_pc(self):
        return self.__composition_pc_pc

    @composition_pc_pc.setter
    def composition_pc_pc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__composition_pc_pc", None)
        self.__composition_pc_pc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_pc_pc"):
                opp_val = getattr(old_value, "core_pc_pc", None)
                if opp_val == self:
                    setattr(old_value, "core_pc_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_pc_pc"):
                opp_val = getattr(value, "core_pc_pc", None)
                setattr(value, "core_pc_pc", self)

    @property
    def GuardedBranchTransition(self):
        return self.__GuardedBranchTransition

    @GuardedBranchTransition.setter
    def GuardedBranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__GuardedBranchTransition", None)
        self.__GuardedBranchTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc_pc16"):
                opp_val = getattr(old_value, "seff_pc_pc16", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc_pc16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc_pc16"):
                opp_val = getattr(value, "seff_pc_pc16", None)
                setattr(value, "seff_pc_pc16", self)

    @property
    def seff_performance_pc_pc8(self):
        return self.__seff_performance_pc_pc8

    @seff_performance_pc_pc8.setter
    def seff_performance_pc_pc8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__seff_performance_pc_pc8", None)
        self.__seff_performance_pc_pc8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_pc_pc9"):
                opp_val = getattr(old_value, "seff_pc_pc9", None)
                if opp_val == self:
                    setattr(old_value, "seff_pc_pc9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_pc_pc9"):
                opp_val = getattr(value, "seff_pc_pc9", None)
                setattr(value, "seff_pc_pc9", self)

    @property
    def qos_performance_pc_pc(self):
        return self.__qos_performance_pc_pc

    @qos_performance_pc_pc.setter
    def qos_performance_pc_pc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__qos_performance_pc_pc", None)
        self.__qos_performance_pc_pc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qosannotations_pc_pc"):
                opp_val = getattr(old_value, "qosannotations_pc_pc", None)
                if opp_val == self:
                    setattr(old_value, "qosannotations_pc_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qosannotations_pc_pc"):
                opp_val = getattr(value, "qosannotations_pc_pc", None)
                setattr(value, "qosannotations_pc_pc", self)

    @property
    def OpenWorkload(self):
        return self.__OpenWorkload

    @OpenWorkload.setter
    def OpenWorkload(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__OpenWorkload", None)
        self.__OpenWorkload = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc_pc25"):
                opp_val = getattr(old_value, "usagemodel_pc_pc25", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc_pc25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc_pc25"):
                opp_val = getattr(value, "usagemodel_pc_pc25", None)
                setattr(value, "usagemodel_pc_pc25", self)

    @property
    def ProcessingResourceSpecification(self):
        return self.__ProcessingResourceSpecification

    @ProcessingResourceSpecification.setter
    def ProcessingResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__ProcessingResourceSpecification", None)
        self.__ProcessingResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_pc_pc30"):
                opp_val = getattr(old_value, "resourceenvironment_pc_pc30", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_pc_pc30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_pc_pc30"):
                opp_val = getattr(value, "resourceenvironment_pc_pc30", None)
                setattr(value, "resourceenvironment_pc_pc30", self)

    @property
    def CommunicationLinkResourceSpecification(self):
        return self.__CommunicationLinkResourceSpecification

    @CommunicationLinkResourceSpecification.setter
    def CommunicationLinkResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__CommunicationLinkResourceSpecification", None)
        self.__CommunicationLinkResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_pc_pc"):
                opp_val = getattr(old_value, "resourceenvironment_pc_pc", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_pc_pc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_pc_pc"):
                opp_val = getattr(value, "resourceenvironment_pc_pc", None)
                setattr(value, "resourceenvironment_pc_pc", self)

    @property
    def CommunicationLinkResourceSpecification32(self):
        return self.__CommunicationLinkResourceSpecification32

    @CommunicationLinkResourceSpecification32.setter
    def CommunicationLinkResourceSpecification32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__CommunicationLinkResourceSpecification32", None)
        self.__CommunicationLinkResourceSpecification32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceenvironment_pc_pc33"):
                opp_val = getattr(old_value, "resourceenvironment_pc_pc33", None)
                if opp_val == self:
                    setattr(old_value, "resourceenvironment_pc_pc33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceenvironment_pc_pc33"):
                opp_val = getattr(value, "resourceenvironment_pc_pc33", None)
                setattr(value, "resourceenvironment_pc_pc33", self)

    @property
    def Delay(self):
        return self.__Delay

    @Delay.setter
    def Delay(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__Delay", None)
        self.__Delay = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagemodel_pc_pc27"):
                opp_val = getattr(old_value, "usagemodel_pc_pc27", None)
                if opp_val == self:
                    setattr(old_value, "usagemodel_pc_pc27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagemodel_pc_pc27"):
                opp_val = getattr(value, "usagemodel_pc_pc27", None)
                setattr(value, "usagemodel_pc_pc27", self)

    def SpecificationMustNotBeNULL(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SpecificationMustNotBeNULL method
        pass

class composition_pc_pc_AssemblyEventConnector:

    pass
class composition_pc_pc_EventChannelSinkConnector:

    pass
class qos_performance_pc_pc_SpecifiedExecutionTime:

    pass
class GuardedBranchTransition:

    pass
class LoopAction:

    pass
class seff_performance_pc_pc_ParametricResourceDemand:

    pass
class seff_performance_pc_pc_ResourceCall:

    pass
class pcm_pc_pc_Pointcut:

    pass
class pcm_pc_pc_EObject:

    pass
class pcm_pc_pc_PointcutPointcut:

    pass
class pcm_pc_pc_DummyClass:

    pass