from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class VariableCharacterisationType(Enum):
    STRUCTURE = "STRUCTURE"
    NUMBER_OF_ELEMENTS = "NUMBER_OF_ELEMENTS"
    VALUE = "VALUE"
    BYTESIZE = "BYTESIZE"
    TYPE = "TYPE"
class ParameterModifier(Enum):
    none = "none"
    in_ = "in_"
    out = "out"
    inout = "inout"
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


############################################
# Definition of Classes
############################################

class repository_av_RepositoryComponent:

    pass
class AllocationContext:

    pass
class ParametricResourceDemand:

    pass
class pcm_av_completions_av_NetworkDemandParametricResourceDemand(ParametricResourceDemand):

    pass
class ExternalCallAction:

    pass
class pcm_av_completions_av_DelegatingExternalCallAction(ExternalCallAction):

    pass
class Completion:

    pass
class pcm_av_completions_av_CompletionRepository:

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
class pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction:

    pass
class SpecifiedQoSAnnotation:

    pass
class pcm_av_qos_performance_av_SpecifiedExecutionTime(SpecifiedQoSAnnotation):

    pass
class pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation(SpecifiedQoSAnnotation):

    def __init__(self, specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription: set["ExternalFailureOccurrenceDescription"] = None, SpecifiedQoSAnnotation: "pcm_av_qosannotations_av_QoSAnnotations" = None):
        self.specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription = specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription if specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription is not None else set()
        
        pass
    @property
    def specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription(self):
        return self.__specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription

    @specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription.setter
    def specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation__specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription", None)
        self.__specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExternalFailureOccurrenceDescription"):
                    opp_val = getattr(item, "ExternalFailureOccurrenceDescription", None)
                    
                    if opp_val == self:
                        setattr(item, "ExternalFailureOccurrenceDescription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExternalFailureOccurrenceDescription"):
                    opp_val = getattr(item, "ExternalFailureOccurrenceDescription", None)
                    
                    setattr(item, "ExternalFailureOccurrenceDescription", self)
                    

    def MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed method
        pass

    def SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem method
        pass

    def SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1 method
        pass

class System:

    pass
class QoSAnnotations:

    pass
class pcm_av_qosannotations_av_SpecifiedQoSAnnotation:

    pass
class SpecifiedExecutionTime:

    pass
class pcm_av_qos_performance_av_ComponentSpecifiedExecutionTime(SpecifiedExecutionTime):

    pass
class pcm_av_qos_performance_av_SystemSpecifiedExecutionTime(SpecifiedExecutionTime):

    def __init__(self):
        
        pass
    def SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem method
        pass

class seff_reliability_av_RecoveryAction:

    pass
class seff_reliability_av_RecoveryActionBehaviour:

    pass
class pcm_av_seff_performance_av_ParametricResourceDemand:

    def __init__(self, parametricResourceDemand_PCMRandomVariable: "PCMRandomVariable" = None, pcm_av_seff_performance_av_ParametricResourceDemand: "ProcessingResourceType" = None, resourceDemand_Action: "AbstractInternalControlFlowAction" = None):
        self.parametricResourceDemand_PCMRandomVariable = parametricResourceDemand_PCMRandomVariable
        self.pcm_av_seff_performance_av_ParametricResourceDemand = pcm_av_seff_performance_av_ParametricResourceDemand
        self.resourceDemand_Action = resourceDemand_Action
        
        pass
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
            if hasattr(old_value, "ProcessingResourceType418"):
                opp_val = getattr(old_value, "ProcessingResourceType418", None)
                if opp_val == self:
                    setattr(old_value, "ProcessingResourceType418", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessingResourceType418"):
                opp_val = getattr(value, "ProcessingResourceType418", None)
                setattr(value, "ProcessingResourceType418", self)

    @property
    def parametricResourceDemand_PCMRandomVariable(self):
        return self.__parametricResourceDemand_PCMRandomVariable

    @parametricResourceDemand_PCMRandomVariable.setter
    def parametricResourceDemand_PCMRandomVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_performance_av_ParametricResourceDemand__parametricResourceDemand_PCMRandomVariable", None)
        self.__parametricResourceDemand_PCMRandomVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable416"):
                opp_val = getattr(old_value, "PCMRandomVariable416", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable416", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable416"):
                opp_val = getattr(value, "PCMRandomVariable416", None)
                setattr(value, "PCMRandomVariable416", self)

    @property
    def resourceDemand_Action(self):
        return self.__resourceDemand_Action

    @resourceDemand_Action.setter
    def resourceDemand_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_performance_av_ParametricResourceDemand__resourceDemand_Action", None)
        self.__resourceDemand_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractInternalControlFlowAction420"):
                opp_val = getattr(old_value, "AbstractInternalControlFlowAction420", None)
                if opp_val == self:
                    setattr(old_value, "AbstractInternalControlFlowAction420", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractInternalControlFlowAction420"):
                opp_val = getattr(value, "AbstractInternalControlFlowAction420", None)
                setattr(value, "AbstractInternalControlFlowAction420", self)

    def DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

class seff_av_AbstractInternalControlFlowAction:

    pass
class seff_av_CallAction:

    pass
class pcm_av_seff_av_InternalCallAction(seff_av_CallAction, seff_av_AbstractInternalControlFlowAction):

    pass
class pcm_av_seff_av_SynchronisationPoint:

    pass
class ForkAction:

    pass
class ForkedBehaviour:

    pass
class ResourceDemandingSEFF:

    pass
class ResourceDemandingInternalBehaviour:

    pass
class seff_av_ResourceDemandingBehaviour:

    pass
class seff_reliability_av_FailureHandlingEntity:

    pass
class pcm_av_seff_reliability_av_RecoveryActionBehaviour(seff_reliability_av_FailureHandlingEntity, seff_av_ResourceDemandingBehaviour):

    def __init__(self, pcm_av_seff_reliability_av_RecoveryActionBehaviour: set["seff_reliability_av_RecoveryActionBehaviour"] = None, recoveryActionBehaviours__RecoveryAction: "seff_reliability_av_RecoveryAction" = None):
        self.pcm_av_seff_reliability_av_RecoveryActionBehaviour = pcm_av_seff_reliability_av_RecoveryActionBehaviour if pcm_av_seff_reliability_av_RecoveryActionBehaviour is not None else set()
        self.recoveryActionBehaviours__RecoveryAction = recoveryActionBehaviours__RecoveryAction
        
        pass
    @property
    def recoveryActionBehaviours__RecoveryAction(self):
        return self.__recoveryActionBehaviours__RecoveryAction

    @recoveryActionBehaviours__RecoveryAction.setter
    def recoveryActionBehaviours__RecoveryAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_reliability_av_RecoveryActionBehaviour__recoveryActionBehaviours__RecoveryAction", None)
        self.__recoveryActionBehaviours__RecoveryAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RecoveryAction"):
                opp_val = getattr(old_value, "RecoveryAction", None)
                if opp_val == self:
                    setattr(old_value, "RecoveryAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RecoveryAction"):
                opp_val = getattr(value, "RecoveryAction", None)
                setattr(value, "RecoveryAction", self)

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
                    

    def RecoveryActionBehaviourIsNotSuccessorOfItself(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement RecoveryActionBehaviourIsNotSuccessorOfItself method
        pass

    def SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes method
        pass

    def RecoveryActionBehaviourHasOnlyOnePredecessor(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement RecoveryActionBehaviourHasOnlyOnePredecessor method
        pass

class seff_av_CallReturnAction:

    pass
class seff_av_AbstractAction:

    pass
class pcm_av_seff_av_EmitEventAction(seff_av_CallAction, seff_av_AbstractAction):

    pass
class pcm_av_seff_av_ExternalCallAction(seff_av_CallReturnAction, seff_av_AbstractAction, seff_reliability_av_FailureHandlingEntity):

    def __init__(self, retryCount: int, pcm_av_seff_av_ExternalCallAction: "OperationSignature" = None, pcm_av_seff_av_ExternalCallAction377: "OperationRequiredRole" = None):
        self.retryCount = retryCount
        self.pcm_av_seff_av_ExternalCallAction = pcm_av_seff_av_ExternalCallAction
        self.pcm_av_seff_av_ExternalCallAction377 = pcm_av_seff_av_ExternalCallAction377
        
        pass
    @property
    def retryCount(self):
        return self.__retryCount

    @retryCount.setter
    def retryCount(self, retryCount: int):
        self.__retryCount = retryCount


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
            if hasattr(old_value, "OperationSignature375"):
                opp_val = getattr(old_value, "OperationSignature375", None)
                if opp_val == self:
                    setattr(old_value, "OperationSignature375", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationSignature375"):
                opp_val = getattr(value, "OperationSignature375", None)
                setattr(value, "OperationSignature375", self)

    @property
    def pcm_av_seff_av_ExternalCallAction377(self):
        return self.__pcm_av_seff_av_ExternalCallAction377

    @pcm_av_seff_av_ExternalCallAction377.setter
    def pcm_av_seff_av_ExternalCallAction377(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_av_ExternalCallAction__pcm_av_seff_av_ExternalCallAction377", None)
        self.__pcm_av_seff_av_ExternalCallAction377 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationRequiredRole378"):
                opp_val = getattr(old_value, "OperationRequiredRole378", None)
                if opp_val == self:
                    setattr(old_value, "OperationRequiredRole378", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationRequiredRole378"):
                opp_val = getattr(value, "OperationRequiredRole378", None)
                setattr(value, "OperationRequiredRole378", self)

    def OperationRequiredRoleMustBeReferencedByContainer(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement OperationRequiredRoleMustBeReferencedByContainer method
        pass

    def SignatureBelongsToRole(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement SignatureBelongsToRole method
        pass

class pcm_av_seff_av_ServiceEffectSpecification:

    def __init__(self, seffTypeID: str, pcm_av_seff_av_ServiceEffectSpecification: "Signature" = None, serviceEffectSpecifications__BasicComponent: "BasicComponent" = None):
        self.seffTypeID = seffTypeID
        self.pcm_av_seff_av_ServiceEffectSpecification = pcm_av_seff_av_ServiceEffectSpecification
        self.serviceEffectSpecifications__BasicComponent = serviceEffectSpecifications__BasicComponent
        
        pass
    @property
    def seffTypeID(self):
        return self.__seffTypeID

    @seffTypeID.setter
    def seffTypeID(self, seffTypeID: str):
        self.__seffTypeID = seffTypeID


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

    @property
    def serviceEffectSpecifications__BasicComponent(self):
        return self.__serviceEffectSpecifications__BasicComponent

    @serviceEffectSpecifications__BasicComponent.setter
    def serviceEffectSpecifications__BasicComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_av_ServiceEffectSpecification__serviceEffectSpecifications__BasicComponent", None)
        self.__serviceEffectSpecifications__BasicComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicComponent355"):
                opp_val = getattr(old_value, "BasicComponent355", None)
                if opp_val == self:
                    setattr(old_value, "BasicComponent355", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicComponent355"):
                opp_val = getattr(value, "BasicComponent355", None)
                setattr(value, "BasicComponent355", self)

    def ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole method
        pass

class pcm_av_seff_av_CallAction:

    pass
class seff_av_ServiceEffectSpecification:

    pass
class AbstractBranchTransition:

    pass
class pcm_av_seff_av_GuardedBranchTransition(AbstractBranchTransition):

    pass
class pcm_av_seff_av_ProbabilisticBranchTransition(AbstractBranchTransition):

    def __init__(self, branchProbability: float, AbstractBranchTransition350: "pcm_av_seff_av_BranchAction" = None, AbstractBranchTransition: "pcm_av_seff_av_ResourceDemandingBehaviour" = None):
        self.branchProbability = branchProbability
        
        pass
    @property
    def branchProbability(self):
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
class ResourceDemandingBehaviour:

    pass
class pcm_av_seff_av_ResourceDemandingInternalBehaviour(ResourceDemandingBehaviour):

    pass
class pcm_av_seff_av_ForkedBehaviour(ResourceDemandingBehaviour):

    pass
class BranchAction:

    pass
class AbstractAction:

    pass
class pcm_av_seff_av_AbstractInternalControlFlowAction(AbstractAction):

    pass
class AbstractInternalControlFlowAction:

    pass
class pcm_av_seff_reliability_av_RecoveryAction(AbstractInternalControlFlowAction):

    def __init__(self, pcm_av_seff_reliability_av_RecoveryAction: "seff_reliability_av_RecoveryActionBehaviour" = None, recoveryAction__RecoveryActionBehaviour: set["seff_reliability_av_RecoveryActionBehaviour"] = None, AbstractInternalControlFlowAction: "pcm_av_seff_performance_av_InfrastructureCall" = None, AbstractInternalControlFlowAction420: "pcm_av_seff_performance_av_ParametricResourceDemand" = None, AbstractInternalControlFlowAction407: "pcm_av_seff_performance_av_ResourceCall" = None):
        self.pcm_av_seff_reliability_av_RecoveryAction = pcm_av_seff_reliability_av_RecoveryAction
        self.recoveryAction__RecoveryActionBehaviour = recoveryAction__RecoveryActionBehaviour if recoveryAction__RecoveryActionBehaviour is not None else set()
        
        pass
    @property
    def recoveryAction__RecoveryActionBehaviour(self):
        return self.__recoveryAction__RecoveryActionBehaviour

    @recoveryAction__RecoveryActionBehaviour.setter
    def recoveryAction__RecoveryActionBehaviour(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_reliability_av_RecoveryAction__recoveryAction__RecoveryActionBehaviour", None)
        self.__recoveryAction__RecoveryActionBehaviour = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RecoveryActionBehaviour"):
                    opp_val = getattr(item, "RecoveryActionBehaviour", None)
                    
                    if opp_val == self:
                        setattr(item, "RecoveryActionBehaviour", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RecoveryActionBehaviour"):
                    opp_val = getattr(item, "RecoveryActionBehaviour", None)
                    
                    setattr(item, "RecoveryActionBehaviour", self)
                    

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
            if hasattr(old_value, "seff_reliability_av_RecoveryActionBehaviour424"):
                opp_val = getattr(old_value, "seff_reliability_av_RecoveryActionBehaviour424", None)
                if opp_val == self:
                    setattr(old_value, "seff_reliability_av_RecoveryActionBehaviour424", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_reliability_av_RecoveryActionBehaviour424"):
                opp_val = getattr(value, "seff_reliability_av_RecoveryActionBehaviour424", None)
                setattr(value, "seff_reliability_av_RecoveryActionBehaviour424", self)

    def PrimaryBehaviourOfRecoveryActionMustBeSet(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement PrimaryBehaviourOfRecoveryActionMustBeSet method
        pass

class pcm_av_seff_av_SetVariableAction(AbstractInternalControlFlowAction):

    pass
class pcm_av_seff_av_AcquireAction(AbstractInternalControlFlowAction):

    def __init__(self, timeout: bool, timeoutValue: float, pcm_av_seff_av_AcquireAction: "PassiveResource" = None, AbstractInternalControlFlowAction: "pcm_av_seff_performance_av_InfrastructureCall" = None, AbstractInternalControlFlowAction420: "pcm_av_seff_performance_av_ParametricResourceDemand" = None, AbstractInternalControlFlowAction407: "pcm_av_seff_performance_av_ResourceCall" = None):
        self.timeout = timeout
        self.timeoutValue = timeoutValue
        self.pcm_av_seff_av_AcquireAction = pcm_av_seff_av_AcquireAction
        
        pass
    @property
    def timeout(self):
        return self.__timeout

    @timeout.setter
    def timeout(self, timeout: bool):
        self.__timeout = timeout


    @property
    def timeoutValue(self):
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
            if hasattr(old_value, "PassiveResource382"):
                opp_val = getattr(old_value, "PassiveResource382", None)
                if opp_val == self:
                    setattr(old_value, "PassiveResource382", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PassiveResource382"):
                opp_val = getattr(value, "PassiveResource382", None)
                setattr(value, "PassiveResource382", self)

    def TimeoutValueOfAcquireActionMustNotBeNegative(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement TimeoutValueOfAcquireActionMustNotBeNegative method
        pass

class pcm_av_seff_av_ForkAction(AbstractInternalControlFlowAction):

    pass
class pcm_av_seff_av_ReleaseAction(AbstractInternalControlFlowAction):

    pass
class pcm_av_seff_av_InternalAction(AbstractInternalControlFlowAction):

    def __init__(self, internalAction__InternalFailureOccurrenceDescription: set["InternalFailureOccurrenceDescription"] = None, AbstractInternalControlFlowAction: "pcm_av_seff_performance_av_InfrastructureCall" = None, AbstractInternalControlFlowAction420: "pcm_av_seff_performance_av_ParametricResourceDemand" = None, AbstractInternalControlFlowAction407: "pcm_av_seff_performance_av_ResourceCall" = None):
        self.internalAction__InternalFailureOccurrenceDescription = internalAction__InternalFailureOccurrenceDescription if internalAction__InternalFailureOccurrenceDescription is not None else set()
        
        pass
    @property
    def internalAction__InternalFailureOccurrenceDescription(self):
        return self.__internalAction__InternalFailureOccurrenceDescription

    @internalAction__InternalFailureOccurrenceDescription.setter
    def internalAction__InternalFailureOccurrenceDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_av_InternalAction__internalAction__InternalFailureOccurrenceDescription", None)
        self.__internalAction__InternalFailureOccurrenceDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InternalFailureOccurrenceDescription397"):
                    opp_val = getattr(item, "InternalFailureOccurrenceDescription397", None)
                    
                    if opp_val == self:
                        setattr(item, "InternalFailureOccurrenceDescription397", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InternalFailureOccurrenceDescription397"):
                    opp_val = getattr(item, "InternalFailureOccurrenceDescription397", None)
                    
                    setattr(item, "InternalFailureOccurrenceDescription397", self)
                    

    def MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed method
        pass

    def SumOfInternalActionFailureProbabilitiesMustNotExceed1(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement SumOfInternalActionFailureProbabilitiesMustNotExceed1 method
        pass

class pcm_av_seff_av_AbstractLoopAction(AbstractInternalControlFlowAction):

    pass
class pcm_av_seff_av_StartAction(AbstractInternalControlFlowAction):

    def __init__(self, AbstractInternalControlFlowAction: "pcm_av_seff_performance_av_InfrastructureCall" = None, AbstractInternalControlFlowAction420: "pcm_av_seff_performance_av_ParametricResourceDemand" = None, AbstractInternalControlFlowAction407: "pcm_av_seff_performance_av_ResourceCall" = None):
        
        pass
    def StartActionPredecessorMustNotBeDefined(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement StartActionPredecessorMustNotBeDefined method
        pass

class pcm_av_seff_av_BranchAction(AbstractInternalControlFlowAction):

    def __init__(self, branchAction_AbstractBranchTransition: set["AbstractBranchTransition"] = None, AbstractInternalControlFlowAction: "pcm_av_seff_performance_av_InfrastructureCall" = None, AbstractInternalControlFlowAction420: "pcm_av_seff_performance_av_ParametricResourceDemand" = None, AbstractInternalControlFlowAction407: "pcm_av_seff_performance_av_ResourceCall" = None):
        self.branchAction_AbstractBranchTransition = branchAction_AbstractBranchTransition if branchAction_AbstractBranchTransition is not None else set()
        
        pass
    @property
    def branchAction_AbstractBranchTransition(self):
        return self.__branchAction_AbstractBranchTransition

    @branchAction_AbstractBranchTransition.setter
    def branchAction_AbstractBranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_av_BranchAction__branchAction_AbstractBranchTransition", None)
        self.__branchAction_AbstractBranchTransition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractBranchTransition350"):
                    opp_val = getattr(item, "AbstractBranchTransition350", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractBranchTransition350", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractBranchTransition350"):
                    opp_val = getattr(item, "AbstractBranchTransition350", None)
                    
                    setattr(item, "AbstractBranchTransition350", self)
                    

    def AllProbabilisticBranchProbabilitiesMustSumUpTo1(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement AllProbabilisticBranchProbabilitiesMustSumUpTo1 method
        pass

    def EitherGuardedBranchesOrProbabilisiticBranchTransitions(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement EitherGuardedBranchesOrProbabilisiticBranchTransitions method
        pass

class pcm_av_seff_av_StopAction(AbstractInternalControlFlowAction):

    def __init__(self, AbstractInternalControlFlowAction: "pcm_av_seff_performance_av_InfrastructureCall" = None, AbstractInternalControlFlowAction420: "pcm_av_seff_performance_av_ParametricResourceDemand" = None, AbstractInternalControlFlowAction407: "pcm_av_seff_performance_av_ResourceCall" = None):
        
        pass
    def StopActionSuccessorMustNotBeDefined(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement StopActionSuccessorMustNotBeDefined method
        pass

class qos_reliability_av_SpecifiedReliabilityAnnotation:

    pass
class CommunicationLinkResourceType:

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

    def __init__(self, externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation: "qos_reliability_av_SpecifiedReliabilityAnnotation" = None, pcm_av_reliability_av_ExternalFailureOccurrenceDescription: "FailureType" = None):
        self.externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation = externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation
        self.pcm_av_reliability_av_ExternalFailureOccurrenceDescription = pcm_av_reliability_av_ExternalFailureOccurrenceDescription
        
        pass
    @property
    def externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation(self):
        return self.__externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation

    @externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation.setter
    def externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_reliability_av_ExternalFailureOccurrenceDescription__externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation", None)
        self.__externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SpecifiedReliabilityAnnotation"):
                opp_val = getattr(old_value, "SpecifiedReliabilityAnnotation", None)
                if opp_val == self:
                    setattr(old_value, "SpecifiedReliabilityAnnotation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SpecifiedReliabilityAnnotation"):
                opp_val = getattr(value, "SpecifiedReliabilityAnnotation", None)
                setattr(value, "SpecifiedReliabilityAnnotation", self)

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
            if hasattr(old_value, "FailureType324"):
                opp_val = getattr(old_value, "FailureType324", None)
                if opp_val == self:
                    setattr(old_value, "FailureType324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FailureType324"):
                opp_val = getattr(value, "FailureType324", None)
                setattr(value, "FailureType324", self)

    def NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription method
        pass

class pcm_av_reliability_av_InternalFailureOccurrenceDescription(FailureOccurrenceDescription):

    def __init__(self, internalFailureOccurrenceDescriptions__InternalAction: "InternalAction" = None, internalFailureOccurrenceDescriptions__SoftwareInducedFailureType: "SoftwareInducedFailureType" = None):
        self.internalFailureOccurrenceDescriptions__InternalAction = internalFailureOccurrenceDescriptions__InternalAction
        self.internalFailureOccurrenceDescriptions__SoftwareInducedFailureType = internalFailureOccurrenceDescriptions__SoftwareInducedFailureType
        
        pass
    @property
    def internalFailureOccurrenceDescriptions__SoftwareInducedFailureType(self):
        return self.__internalFailureOccurrenceDescriptions__SoftwareInducedFailureType

    @internalFailureOccurrenceDescriptions__SoftwareInducedFailureType.setter
    def internalFailureOccurrenceDescriptions__SoftwareInducedFailureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_reliability_av_InternalFailureOccurrenceDescription__internalFailureOccurrenceDescriptions__SoftwareInducedFailureType", None)
        self.__internalFailureOccurrenceDescriptions__SoftwareInducedFailureType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SoftwareInducedFailureType"):
                opp_val = getattr(old_value, "SoftwareInducedFailureType", None)
                if opp_val == self:
                    setattr(old_value, "SoftwareInducedFailureType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SoftwareInducedFailureType"):
                opp_val = getattr(value, "SoftwareInducedFailureType", None)
                setattr(value, "SoftwareInducedFailureType", self)

    @property
    def internalFailureOccurrenceDescriptions__InternalAction(self):
        return self.__internalFailureOccurrenceDescriptions__InternalAction

    @internalFailureOccurrenceDescriptions__InternalAction.setter
    def internalFailureOccurrenceDescriptions__InternalAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_reliability_av_InternalFailureOccurrenceDescription__internalFailureOccurrenceDescriptions__InternalAction", None)
        self.__internalFailureOccurrenceDescriptions__InternalAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InternalAction"):
                opp_val = getattr(old_value, "InternalAction", None)
                if opp_val == self:
                    setattr(old_value, "InternalAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InternalAction"):
                opp_val = getattr(value, "InternalAction", None)
                setattr(value, "InternalAction", self)

    def NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription method
        pass

class InternalFailureOccurrenceDescription:

    pass
class ProcessingResourceType:

    pass
class Variable:

    pass
class pcm_av_parameter_av_CharacterisedVariable(Variable):

    def __init__(self, characterisationType: str):
        self.characterisationType = characterisationType
        
        pass
    @property
    def characterisationType(self):
        return self.__characterisationType

    @characterisationType.setter
    def characterisationType(self, characterisationType: str):
        self.__characterisationType = characterisationType


class pcm_av_parameter_av_VariableCharacterisation:

    def __init__(self, type: str, variableCharacterisation_Specification: "PCMRandomVariable" = None, variableCharacterisation_VariableUsage: "VariableUsage" = None):
        self.type = type
        self.variableCharacterisation_Specification = variableCharacterisation_Specification
        self.variableCharacterisation_VariableUsage = variableCharacterisation_VariableUsage
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def variableCharacterisation_Specification(self):
        return self.__variableCharacterisation_Specification

    @variableCharacterisation_Specification.setter
    def variableCharacterisation_Specification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_parameter_av_VariableCharacterisation__variableCharacterisation_Specification", None)
        self.__variableCharacterisation_Specification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable314"):
                opp_val = getattr(old_value, "PCMRandomVariable314", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable314", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable314"):
                opp_val = getattr(value, "PCMRandomVariable314", None)
                setattr(value, "PCMRandomVariable314", self)

    @property
    def variableCharacterisation_VariableUsage(self):
        return self.__variableCharacterisation_VariableUsage

    @variableCharacterisation_VariableUsage.setter
    def variableCharacterisation_VariableUsage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_parameter_av_VariableCharacterisation__variableCharacterisation_VariableUsage", None)
        self.__variableCharacterisation_VariableUsage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableUsage316"):
                opp_val = getattr(old_value, "VariableUsage316", None)
                if opp_val == self:
                    setattr(old_value, "VariableUsage316", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableUsage316"):
                opp_val = getattr(value, "VariableUsage316", None)
                setattr(value, "VariableUsage316", self)

class parameter_av_pcm_av_AbstractNamedReference:

    pass
class pcm_av_reliability_av_FailureOccurrenceDescription:

    def __init__(self, failureProbability: float):
        self.failureProbability = failureProbability
        
        pass
    @property
    def failureProbability(self):
        return self.__failureProbability

    @failureProbability.setter
    def failureProbability(self, failureProbability: float):
        self.__failureProbability = failureProbability


    def EnsureValidFailureProbabilityRange(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement EnsureValidFailureProbabilityRange method
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
class pcm_av_seff_performance_av_InfrastructureCall(CallAction):

    def __init__(self, pcm_av_seff_performance_av_InfrastructureCall: "InfrastructureSignature" = None, infrastructureCall__PCMRandomVariable: "PCMRandomVariable" = None, infrastructureCall__Action: "AbstractInternalControlFlowAction" = None, pcm_av_seff_performance_av_InfrastructureCall404: "InfrastructureRequiredRole" = None, CallAction: "pcm_av_parameter_av_VariableUsage" = None):
        self.pcm_av_seff_performance_av_InfrastructureCall = pcm_av_seff_performance_av_InfrastructureCall
        self.infrastructureCall__PCMRandomVariable = infrastructureCall__PCMRandomVariable
        self.infrastructureCall__Action = infrastructureCall__Action
        self.pcm_av_seff_performance_av_InfrastructureCall404 = pcm_av_seff_performance_av_InfrastructureCall404
        
        pass
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
            if hasattr(old_value, "InfrastructureSignature399"):
                opp_val = getattr(old_value, "InfrastructureSignature399", None)
                if opp_val == self:
                    setattr(old_value, "InfrastructureSignature399", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InfrastructureSignature399"):
                opp_val = getattr(value, "InfrastructureSignature399", None)
                setattr(value, "InfrastructureSignature399", self)

    @property
    def pcm_av_seff_performance_av_InfrastructureCall404(self):
        return self.__pcm_av_seff_performance_av_InfrastructureCall404

    @pcm_av_seff_performance_av_InfrastructureCall404.setter
    def pcm_av_seff_performance_av_InfrastructureCall404(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_performance_av_InfrastructureCall__pcm_av_seff_performance_av_InfrastructureCall404", None)
        self.__pcm_av_seff_performance_av_InfrastructureCall404 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InfrastructureRequiredRole405"):
                opp_val = getattr(old_value, "InfrastructureRequiredRole405", None)
                if opp_val == self:
                    setattr(old_value, "InfrastructureRequiredRole405", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InfrastructureRequiredRole405"):
                opp_val = getattr(value, "InfrastructureRequiredRole405", None)
                setattr(value, "InfrastructureRequiredRole405", self)

    @property
    def infrastructureCall__Action(self):
        return self.__infrastructureCall__Action

    @infrastructureCall__Action.setter
    def infrastructureCall__Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_performance_av_InfrastructureCall__infrastructureCall__Action", None)
        self.__infrastructureCall__Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractInternalControlFlowAction"):
                opp_val = getattr(old_value, "AbstractInternalControlFlowAction", None)
                if opp_val == self:
                    setattr(old_value, "AbstractInternalControlFlowAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractInternalControlFlowAction"):
                opp_val = getattr(value, "AbstractInternalControlFlowAction", None)
                setattr(value, "AbstractInternalControlFlowAction", self)

    @property
    def infrastructureCall__PCMRandomVariable(self):
        return self.__infrastructureCall__PCMRandomVariable

    @infrastructureCall__PCMRandomVariable.setter
    def infrastructureCall__PCMRandomVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_performance_av_InfrastructureCall__infrastructureCall__PCMRandomVariable", None)
        self.__infrastructureCall__PCMRandomVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable401"):
                opp_val = getattr(old_value, "PCMRandomVariable401", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable401", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable401"):
                opp_val = getattr(value, "PCMRandomVariable401", None)
                setattr(value, "PCMRandomVariable401", self)

    def ReferencedRequiredRoleMustBeRequiredByComponent(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement ReferencedRequiredRoleMustBeRequiredByComponent method
        pass

    def SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

    def SignatureMustBelongToUsedRequiredRole(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement SignatureMustBelongToUsedRequiredRole method
        pass

class pcm_av_seff_performance_av_ResourceCall(CallAction):

    def __init__(self, resourceCall__Action: "AbstractInternalControlFlowAction" = None, pcm_av_seff_performance_av_ResourceCall: "entity_av_ResourceRequiredRole" = None, pcm_av_seff_performance_av_ResourceCall411: "ResourceSignature" = None, resourceCall__PCMRandomVariable: "PCMRandomVariable" = None, CallAction: "pcm_av_parameter_av_VariableUsage" = None):
        self.resourceCall__Action = resourceCall__Action
        self.pcm_av_seff_performance_av_ResourceCall = pcm_av_seff_performance_av_ResourceCall
        self.pcm_av_seff_performance_av_ResourceCall411 = pcm_av_seff_performance_av_ResourceCall411
        self.resourceCall__PCMRandomVariable = resourceCall__PCMRandomVariable
        
        pass
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
            if hasattr(old_value, "entity_av_ResourceRequiredRole409"):
                opp_val = getattr(old_value, "entity_av_ResourceRequiredRole409", None)
                if opp_val == self:
                    setattr(old_value, "entity_av_ResourceRequiredRole409", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entity_av_ResourceRequiredRole409"):
                opp_val = getattr(value, "entity_av_ResourceRequiredRole409", None)
                setattr(value, "entity_av_ResourceRequiredRole409", self)

    @property
    def resourceCall__Action(self):
        return self.__resourceCall__Action

    @resourceCall__Action.setter
    def resourceCall__Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_performance_av_ResourceCall__resourceCall__Action", None)
        self.__resourceCall__Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractInternalControlFlowAction407"):
                opp_val = getattr(old_value, "AbstractInternalControlFlowAction407", None)
                if opp_val == self:
                    setattr(old_value, "AbstractInternalControlFlowAction407", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractInternalControlFlowAction407"):
                opp_val = getattr(value, "AbstractInternalControlFlowAction407", None)
                setattr(value, "AbstractInternalControlFlowAction407", self)

    @property
    def pcm_av_seff_performance_av_ResourceCall411(self):
        return self.__pcm_av_seff_performance_av_ResourceCall411

    @pcm_av_seff_performance_av_ResourceCall411.setter
    def pcm_av_seff_performance_av_ResourceCall411(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_performance_av_ResourceCall__pcm_av_seff_performance_av_ResourceCall411", None)
        self.__pcm_av_seff_performance_av_ResourceCall411 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceSignature412"):
                opp_val = getattr(old_value, "ResourceSignature412", None)
                if opp_val == self:
                    setattr(old_value, "ResourceSignature412", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceSignature412"):
                opp_val = getattr(value, "ResourceSignature412", None)
                setattr(value, "ResourceSignature412", self)

    @property
    def resourceCall__PCMRandomVariable(self):
        return self.__resourceCall__PCMRandomVariable

    @resourceCall__PCMRandomVariable.setter
    def resourceCall__PCMRandomVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_performance_av_ResourceCall__resourceCall__PCMRandomVariable", None)
        self.__resourceCall__PCMRandomVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable414"):
                opp_val = getattr(old_value, "PCMRandomVariable414", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable414", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable414"):
                opp_val = getattr(value, "PCMRandomVariable414", None)
                setattr(value, "PCMRandomVariable414", self)

    def SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

    def ResourceRequiredRoleMustBeReferencedByComponent(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement ResourceRequiredRoleMustBeReferencedByComponent method
        pass

    def ResourceSignatureBelongsToResourceRequiredRole(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement ResourceSignatureBelongsToResourceRequiredRole method
        pass

class pcm_av_seff_av_CallReturnAction(CallAction):

    pass
class pcm_av_parameter_av_VariableUsage:

    pass
class pcm_av_protocol_av_Protocol:

    def __init__(self, protocolTypeID: str):
        self.protocolTypeID = protocolTypeID
        
        pass
    @property
    def protocolTypeID(self):
        return self.__protocolTypeID

    @protocolTypeID.setter
    def protocolTypeID(self, protocolTypeID: str):
        self.__protocolTypeID = protocolTypeID


class EntryLevelSystemCall:

    pass
class NetworkInducedFailureType:

    pass
class SchedulingPolicy:

    pass
class pcm_av_resourcetype_av_ResourceRepository:

    pass
class ResourceRepository:

    pass
class UnitCarryingElement:

    pass
class HardwareInducedFailureType:

    pass
class ResourceType:

    pass
class pcm_av_resourcetype_av_CommunicationLinkResourceType(ResourceType):

    pass
class pcm_av_resourcetype_av_ProcessingResourceType(ResourceType):

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
class pcm_av_subsystem_av_SubSystem(entity_av_ComposedProvidingRequiringEntity, repository_av_RepositoryComponent):

    pass
class pcm_av_repository_av_CompositeComponent(entity_av_ComposedProvidingRequiringEntity, repository_av_ImplementationComponentType):

    def __init__(self):
        
        pass
    def ProvideSameInterfaces(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement ProvideSameInterfaces method
        pass

    def RequireSameInterfaces(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement RequireSameInterfaces method
        pass

class ProvidesComponentType:

    pass
class OperationInterface:

    pass
class pcm_av_repository_av_ExceptionType:

    def __init__(self, exceptionName: str, exceptionMessage: str):
        self.exceptionName = exceptionName
        self.exceptionMessage = exceptionMessage
        
        pass
    @property
    def exceptionName(self):
        return self.__exceptionName

    @exceptionName.setter
    def exceptionName(self, exceptionName: str):
        self.__exceptionName = exceptionName


    @property
    def exceptionMessage(self):
        return self.__exceptionMessage

    @exceptionMessage.setter
    def exceptionMessage(self, exceptionMessage: str):
        self.__exceptionMessage = exceptionMessage


class ExceptionType:

    pass
class Signature:

    pass
class pcm_av_repository_av_OperationSignature(Signature):

    def __init__(self, signatures__OperationInterface: "OperationInterface" = None, operationSignature__Parameter: set["Parameter"] = None, pcm_av_repository_av_OperationSignature: "DataType" = None, Signature438: "pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction" = None, Signature429: "pcm_av_qosannotations_av_SpecifiedQoSAnnotation" = None, Signature: "pcm_av_seff_av_ServiceEffectSpecification" = None):
        self.signatures__OperationInterface = signatures__OperationInterface
        self.operationSignature__Parameter = operationSignature__Parameter if operationSignature__Parameter is not None else set()
        self.pcm_av_repository_av_OperationSignature = pcm_av_repository_av_OperationSignature
        
        pass
    @property
    def signatures__OperationInterface(self):
        return self.__signatures__OperationInterface

    @signatures__OperationInterface.setter
    def signatures__OperationInterface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_OperationSignature__signatures__OperationInterface", None)
        self.__signatures__OperationInterface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationInterface"):
                opp_val = getattr(old_value, "OperationInterface", None)
                if opp_val == self:
                    setattr(old_value, "OperationInterface", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationInterface"):
                opp_val = getattr(value, "OperationInterface", None)
                setattr(value, "OperationInterface", self)

    @property
    def operationSignature__Parameter(self):
        return self.__operationSignature__Parameter

    @operationSignature__Parameter.setter
    def operationSignature__Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_OperationSignature__operationSignature__Parameter", None)
        self.__operationSignature__Parameter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter257"):
                    opp_val = getattr(item, "Parameter257", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter257", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter257"):
                    opp_val = getattr(item, "Parameter257", None)
                    
                    setattr(item, "Parameter257", self)
                    

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
            if hasattr(old_value, "DataType259"):
                opp_val = getattr(old_value, "DataType259", None)
                if opp_val == self:
                    setattr(old_value, "DataType259", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType259"):
                opp_val = getattr(value, "DataType259", None)
                setattr(value, "DataType259", self)

    def ParameterNamesHaveToBeUniqueForASignature(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement ParameterNamesHaveToBeUniqueForASignature method
        pass

class pcm_av_repository_av_EventType(Signature):

    pass
class Parameter:

    pass
class pcm_av_repository_av_RequiredCharacterisation:

    def __init__(self, type: str, pcm_av_repository_av_RequiredCharacterisation: "Parameter" = None, requiredCharacterisations: "Interface" = None):
        self.type = type
        self.pcm_av_repository_av_RequiredCharacterisation = pcm_av_repository_av_RequiredCharacterisation
        self.requiredCharacterisations = requiredCharacterisations
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def requiredCharacterisations(self):
        return self.__requiredCharacterisations

    @requiredCharacterisations.setter
    def requiredCharacterisations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_RequiredCharacterisation__requiredCharacterisations", None)
        self.__requiredCharacterisations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Interface236"):
                opp_val = getattr(old_value, "Interface236", None)
                if opp_val == self:
                    setattr(old_value, "Interface236", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Interface236"):
                opp_val = getattr(value, "Interface236", None)
                setattr(value, "Interface236", self)

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
class InfrastructureInterface:

    pass
class pcm_av_repository_av_InfrastructureSignature(Signature):

    pass
class FailureType:

    pass
class pcm_av_reliability_av_SoftwareInducedFailureType(FailureType):

    pass
class pcm_av_reliability_av_NetworkInducedFailureType(FailureType):

    def __init__(self, networkInducedFailureType__CommunicationLinkResourceType: "CommunicationLinkResourceType" = None, FailureType324: "pcm_av_reliability_av_ExternalFailureOccurrenceDescription" = None, FailureType246: "pcm_av_repository_av_Signature" = None, FailureType427: "pcm_av_seff_reliability_av_FailureHandlingEntity" = None, FailureType: "pcm_av_repository_av_Repository" = None):
        self.networkInducedFailureType__CommunicationLinkResourceType = networkInducedFailureType__CommunicationLinkResourceType
        
        pass
    @property
    def networkInducedFailureType__CommunicationLinkResourceType(self):
        return self.__networkInducedFailureType__CommunicationLinkResourceType

    @networkInducedFailureType__CommunicationLinkResourceType.setter
    def networkInducedFailureType__CommunicationLinkResourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_reliability_av_NetworkInducedFailureType__networkInducedFailureType__CommunicationLinkResourceType", None)
        self.__networkInducedFailureType__CommunicationLinkResourceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CommunicationLinkResourceType"):
                opp_val = getattr(old_value, "CommunicationLinkResourceType", None)
                if opp_val == self:
                    setattr(old_value, "CommunicationLinkResourceType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CommunicationLinkResourceType"):
                opp_val = getattr(value, "CommunicationLinkResourceType", None)
                setattr(value, "CommunicationLinkResourceType", self)

    def NetworkInducedFailureTypeHasCommunicationLinkResourceType(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement NetworkInducedFailureTypeHasCommunicationLinkResourceType method
        pass

class pcm_av_reliability_av_HardwareInducedFailureType(FailureType):

    def __init__(self, hardwareInducedFailureType__ProcessingResourceType: "ProcessingResourceType" = None, FailureType324: "pcm_av_reliability_av_ExternalFailureOccurrenceDescription" = None, FailureType246: "pcm_av_repository_av_Signature" = None, FailureType427: "pcm_av_seff_reliability_av_FailureHandlingEntity" = None, FailureType: "pcm_av_repository_av_Repository" = None):
        self.hardwareInducedFailureType__ProcessingResourceType = hardwareInducedFailureType__ProcessingResourceType
        
        pass
    @property
    def hardwareInducedFailureType__ProcessingResourceType(self):
        return self.__hardwareInducedFailureType__ProcessingResourceType

    @hardwareInducedFailureType__ProcessingResourceType.setter
    def hardwareInducedFailureType__ProcessingResourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_reliability_av_HardwareInducedFailureType__hardwareInducedFailureType__ProcessingResourceType", None)
        self.__hardwareInducedFailureType__ProcessingResourceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcessingResourceType"):
                opp_val = getattr(old_value, "ProcessingResourceType", None)
                if opp_val == self:
                    setattr(old_value, "ProcessingResourceType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessingResourceType"):
                opp_val = getattr(value, "ProcessingResourceType", None)
                setattr(value, "ProcessingResourceType", self)

    def HardwareInducedFailureTypeHasProcessingResourceType(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement HardwareInducedFailureTypeHasProcessingResourceType method
        pass

class Interface:

    pass
class pcm_av_repository_av_OperationInterface(Interface):

    def __init__(self, interface__OperationSignature: set["OperationSignature"] = None, Interface228: "pcm_av_repository_av_Interface" = None, Interface: "pcm_av_repository_av_Repository" = None, Interface236: "pcm_av_repository_av_RequiredCharacterisation" = None):
        self.interface__OperationSignature = interface__OperationSignature if interface__OperationSignature is not None else set()
        
        pass
    @property
    def interface__OperationSignature(self):
        return self.__interface__OperationSignature

    @interface__OperationSignature.setter
    def interface__OperationSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_OperationInterface__interface__OperationSignature", None)
        self.__interface__OperationSignature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OperationSignature261"):
                    opp_val = getattr(item, "OperationSignature261", None)
                    
                    if opp_val == self:
                        setattr(item, "OperationSignature261", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OperationSignature261"):
                    opp_val = getattr(item, "OperationSignature261", None)
                    
                    setattr(item, "OperationSignature261", self)
                    

    def SignaturesHaveToBeUniqueForAnInterface(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement SignaturesHaveToBeUniqueForAnInterface method
        pass

class pcm_av_repository_av_InfrastructureInterface(Interface):

    pass
class pcm_av_repository_av_EventGroup(Interface):

    pass
class pcm_av_repository_av_DataType:

    pass
class ResourceSignature:

    pass
class EventType:

    pass
class DataType:

    pass
class pcm_av_repository_av_PrimitiveDataType(DataType):

    def __init__(self, type: str, DataType: "pcm_av_repository_av_Parameter" = None, DataType274: "pcm_av_repository_av_CollectionDataType" = None, DataType226: "pcm_av_repository_av_Repository" = None, DataType259: "pcm_av_repository_av_OperationSignature" = None, DataType278: "pcm_av_repository_av_InnerDeclaration" = None):
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class pcm_av_repository_av_Parameter:

    def __init__(self, parameterName: str, modifier__Parameter: str, parameters__InfrastructureSignature: "InfrastructureSignature" = None, parameters__OperationSignature: "OperationSignature" = None, pcm_av_repository_av_Parameter: "DataType" = None, parameter__EventType: "EventType" = None, parameter__ResourceSignature: "ResourceSignature" = None):
        self.parameterName = parameterName
        self.modifier__Parameter = modifier__Parameter
        self.parameters__InfrastructureSignature = parameters__InfrastructureSignature
        self.parameters__OperationSignature = parameters__OperationSignature
        self.pcm_av_repository_av_Parameter = pcm_av_repository_av_Parameter
        self.parameter__EventType = parameter__EventType
        self.parameter__ResourceSignature = parameter__ResourceSignature
        
        pass
    @property
    def parameterName(self):
        return self.__parameterName

    @parameterName.setter
    def parameterName(self, parameterName: str):
        self.__parameterName = parameterName


    @property
    def modifier__Parameter(self):
        return self.__modifier__Parameter

    @modifier__Parameter.setter
    def modifier__Parameter(self, modifier__Parameter: str):
        self.__modifier__Parameter = modifier__Parameter


    @property
    def parameter__EventType(self):
        return self.__parameter__EventType

    @parameter__EventType.setter
    def parameter__EventType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_Parameter__parameter__EventType", None)
        self.__parameter__EventType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EventType"):
                opp_val = getattr(old_value, "EventType", None)
                if opp_val == self:
                    setattr(old_value, "EventType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EventType"):
                opp_val = getattr(value, "EventType", None)
                setattr(value, "EventType", self)

    @property
    def parameters__OperationSignature(self):
        return self.__parameters__OperationSignature

    @parameters__OperationSignature.setter
    def parameters__OperationSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_Parameter__parameters__OperationSignature", None)
        self.__parameters__OperationSignature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationSignature216"):
                opp_val = getattr(old_value, "OperationSignature216", None)
                if opp_val == self:
                    setattr(old_value, "OperationSignature216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationSignature216"):
                opp_val = getattr(value, "OperationSignature216", None)
                setattr(value, "OperationSignature216", self)

    @property
    def parameters__InfrastructureSignature(self):
        return self.__parameters__InfrastructureSignature

    @parameters__InfrastructureSignature.setter
    def parameters__InfrastructureSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_Parameter__parameters__InfrastructureSignature", None)
        self.__parameters__InfrastructureSignature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InfrastructureSignature"):
                opp_val = getattr(old_value, "InfrastructureSignature", None)
                if opp_val == self:
                    setattr(old_value, "InfrastructureSignature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InfrastructureSignature"):
                opp_val = getattr(value, "InfrastructureSignature", None)
                setattr(value, "InfrastructureSignature", self)

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

    @property
    def parameter__ResourceSignature(self):
        return self.__parameter__ResourceSignature

    @parameter__ResourceSignature.setter
    def parameter__ResourceSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_Parameter__parameter__ResourceSignature", None)
        self.__parameter__ResourceSignature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceSignature"):
                opp_val = getattr(old_value, "ResourceSignature", None)
                if opp_val == self:
                    setattr(old_value, "ResourceSignature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceSignature"):
                opp_val = getattr(value, "ResourceSignature", None)
                setattr(value, "ResourceSignature", self)

class Repository:

    pass
class pcm_av_usagemodel_av_UserData:

    pass
class Workload:

    pass
class ScenarioBehaviour:

    pass
class UsageModel:

    pass
class UsageScenario:

    pass
class pcm_av_usagemodel_av_Workload:

    pass
class OperationSignature:

    pass
class VariableUsage:

    pass
class RepositoryComponent:

    pass
class pcm_av_repository_av_CompleteComponentType(RepositoryComponent):

    def __init__(self, pcm_av_repository_av_CompleteComponentType: set["ProvidesComponentType"] = None, RepositoryComponent: "pcm_av_composition_av_AssemblyContext" = None, RepositoryComponent222: "pcm_av_repository_av_Repository" = None):
        self.pcm_av_repository_av_CompleteComponentType = pcm_av_repository_av_CompleteComponentType if pcm_av_repository_av_CompleteComponentType is not None else set()
        
        pass
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
                    

    def providedInterfacesHaveToConformToProvidedType2(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement providedInterfacesHaveToConformToProvidedType2 method
        pass

    def AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType method
        pass

class pcm_av_repository_av_ProvidesComponentType(RepositoryComponent):

    def __init__(self, RepositoryComponent: "pcm_av_composition_av_AssemblyContext" = None, RepositoryComponent222: "pcm_av_repository_av_Repository" = None):
        
        pass
    def AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType method
        pass

class InfrastructureRequiredRole:

    pass
class InfrastructureProvidedRole:

    pass
class OperationRequiredRole:

    pass
class OperationProvidedRole:

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
class composition_av_Connector:

    pass
class composition_av_EventChannel:

    pass
class composition_av_ResourceRequiredDelegationConnector:

    pass
class composition_av_AssemblyContext:

    pass
class DelegationConnector:

    pass
class pcm_av_composition_av_RequiredInfrastructureDelegationConnector(DelegationConnector):

    pass
class pcm_av_composition_av_RequiredDelegationConnector(DelegationConnector):

    def __init__(self, pcm_av_composition_av_RequiredDelegationConnector: "OperationRequiredRole" = None, pcm_av_composition_av_RequiredDelegationConnector70: "OperationRequiredRole" = None, pcm_av_composition_av_RequiredDelegationConnector73: "composition_av_AssemblyContext" = None):
        self.pcm_av_composition_av_RequiredDelegationConnector = pcm_av_composition_av_RequiredDelegationConnector
        self.pcm_av_composition_av_RequiredDelegationConnector70 = pcm_av_composition_av_RequiredDelegationConnector70
        self.pcm_av_composition_av_RequiredDelegationConnector73 = pcm_av_composition_av_RequiredDelegationConnector73
        
        pass
    @property
    def pcm_av_composition_av_RequiredDelegationConnector70(self):
        return self.__pcm_av_composition_av_RequiredDelegationConnector70

    @pcm_av_composition_av_RequiredDelegationConnector70.setter
    def pcm_av_composition_av_RequiredDelegationConnector70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_composition_av_RequiredDelegationConnector__pcm_av_composition_av_RequiredDelegationConnector70", None)
        self.__pcm_av_composition_av_RequiredDelegationConnector70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationRequiredRole71"):
                opp_val = getattr(old_value, "OperationRequiredRole71", None)
                if opp_val == self:
                    setattr(old_value, "OperationRequiredRole71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationRequiredRole71"):
                opp_val = getattr(value, "OperationRequiredRole71", None)
                setattr(value, "OperationRequiredRole71", self)

    @property
    def pcm_av_composition_av_RequiredDelegationConnector73(self):
        return self.__pcm_av_composition_av_RequiredDelegationConnector73

    @pcm_av_composition_av_RequiredDelegationConnector73.setter
    def pcm_av_composition_av_RequiredDelegationConnector73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_composition_av_RequiredDelegationConnector__pcm_av_composition_av_RequiredDelegationConnector73", None)
        self.__pcm_av_composition_av_RequiredDelegationConnector73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_AssemblyContext74"):
                opp_val = getattr(old_value, "composition_av_AssemblyContext74", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_AssemblyContext74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_AssemblyContext74"):
                opp_val = getattr(value, "composition_av_AssemblyContext74", None)
                setattr(value, "composition_av_AssemblyContext74", self)

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

    def RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

    def RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector method
        pass

    def ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame method
        pass

class pcm_av_composition_av_SourceDelegationConnector(DelegationConnector):

    pass
class pcm_av_composition_av_ProvidedInfrastructureDelegationConnector(DelegationConnector):

    pass
class pcm_av_composition_av_RequiredResourceDelegationConnector(DelegationConnector):

    pass
class pcm_av_composition_av_SinkDelegationConnector(DelegationConnector):

    pass
class pcm_av_composition_av_ProvidedDelegationConnector(DelegationConnector):

    def __init__(self, pcm_av_composition_av_ProvidedDelegationConnector: "OperationProvidedRole" = None, pcm_av_composition_av_ProvidedDelegationConnector63: "OperationProvidedRole" = None, pcm_av_composition_av_ProvidedDelegationConnector66: "composition_av_AssemblyContext" = None):
        self.pcm_av_composition_av_ProvidedDelegationConnector = pcm_av_composition_av_ProvidedDelegationConnector
        self.pcm_av_composition_av_ProvidedDelegationConnector63 = pcm_av_composition_av_ProvidedDelegationConnector63
        self.pcm_av_composition_av_ProvidedDelegationConnector66 = pcm_av_composition_av_ProvidedDelegationConnector66
        
        pass
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
    def pcm_av_composition_av_ProvidedDelegationConnector66(self):
        return self.__pcm_av_composition_av_ProvidedDelegationConnector66

    @pcm_av_composition_av_ProvidedDelegationConnector66.setter
    def pcm_av_composition_av_ProvidedDelegationConnector66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_composition_av_ProvidedDelegationConnector__pcm_av_composition_av_ProvidedDelegationConnector66", None)
        self.__pcm_av_composition_av_ProvidedDelegationConnector66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_AssemblyContext67"):
                opp_val = getattr(old_value, "composition_av_AssemblyContext67", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_AssemblyContext67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_AssemblyContext67"):
                opp_val = getattr(value, "composition_av_AssemblyContext67", None)
                setattr(value, "composition_av_AssemblyContext67", self)

    @property
    def pcm_av_composition_av_ProvidedDelegationConnector63(self):
        return self.__pcm_av_composition_av_ProvidedDelegationConnector63

    @pcm_av_composition_av_ProvidedDelegationConnector63.setter
    def pcm_av_composition_av_ProvidedDelegationConnector63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_composition_av_ProvidedDelegationConnector__pcm_av_composition_av_ProvidedDelegationConnector63", None)
        self.__pcm_av_composition_av_ProvidedDelegationConnector63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationProvidedRole64"):
                opp_val = getattr(old_value, "OperationProvidedRole64", None)
                if opp_val == self:
                    setattr(old_value, "OperationProvidedRole64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationProvidedRole64"):
                opp_val = getattr(value, "OperationProvidedRole64", None)
                setattr(value, "OperationProvidedRole64", self)

    def ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

    def ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame method
        pass

class Connector:

    pass
class pcm_av_composition_av_AssemblyConnector(Connector):

    def __init__(self, pcm_av_composition_av_AssemblyConnector: "composition_av_AssemblyContext" = None, pcm_av_composition_av_AssemblyConnector78: "composition_av_AssemblyContext" = None, pcm_av_composition_av_AssemblyConnector81: "OperationProvidedRole" = None, pcm_av_composition_av_AssemblyConnector84: "OperationRequiredRole" = None):
        self.pcm_av_composition_av_AssemblyConnector = pcm_av_composition_av_AssemblyConnector
        self.pcm_av_composition_av_AssemblyConnector78 = pcm_av_composition_av_AssemblyConnector78
        self.pcm_av_composition_av_AssemblyConnector81 = pcm_av_composition_av_AssemblyConnector81
        self.pcm_av_composition_av_AssemblyConnector84 = pcm_av_composition_av_AssemblyConnector84
        
        pass
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
            if hasattr(old_value, "composition_av_AssemblyContext76"):
                opp_val = getattr(old_value, "composition_av_AssemblyContext76", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_AssemblyContext76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_AssemblyContext76"):
                opp_val = getattr(value, "composition_av_AssemblyContext76", None)
                setattr(value, "composition_av_AssemblyContext76", self)

    @property
    def pcm_av_composition_av_AssemblyConnector81(self):
        return self.__pcm_av_composition_av_AssemblyConnector81

    @pcm_av_composition_av_AssemblyConnector81.setter
    def pcm_av_composition_av_AssemblyConnector81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_composition_av_AssemblyConnector__pcm_av_composition_av_AssemblyConnector81", None)
        self.__pcm_av_composition_av_AssemblyConnector81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationProvidedRole82"):
                opp_val = getattr(old_value, "OperationProvidedRole82", None)
                if opp_val == self:
                    setattr(old_value, "OperationProvidedRole82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationProvidedRole82"):
                opp_val = getattr(value, "OperationProvidedRole82", None)
                setattr(value, "OperationProvidedRole82", self)

    @property
    def pcm_av_composition_av_AssemblyConnector78(self):
        return self.__pcm_av_composition_av_AssemblyConnector78

    @pcm_av_composition_av_AssemblyConnector78.setter
    def pcm_av_composition_av_AssemblyConnector78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_composition_av_AssemblyConnector__pcm_av_composition_av_AssemblyConnector78", None)
        self.__pcm_av_composition_av_AssemblyConnector78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_AssemblyContext79"):
                opp_val = getattr(old_value, "composition_av_AssemblyContext79", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_AssemblyContext79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_AssemblyContext79"):
                opp_val = getattr(value, "composition_av_AssemblyContext79", None)
                setattr(value, "composition_av_AssemblyContext79", self)

    @property
    def pcm_av_composition_av_AssemblyConnector84(self):
        return self.__pcm_av_composition_av_AssemblyConnector84

    @pcm_av_composition_av_AssemblyConnector84.setter
    def pcm_av_composition_av_AssemblyConnector84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_composition_av_AssemblyConnector__pcm_av_composition_av_AssemblyConnector84", None)
        self.__pcm_av_composition_av_AssemblyConnector84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationRequiredRole85"):
                opp_val = getattr(old_value, "OperationRequiredRole85", None)
                if opp_val == self:
                    setattr(old_value, "OperationRequiredRole85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationRequiredRole85"):
                opp_val = getattr(value, "OperationRequiredRole85", None)
                setattr(value, "OperationRequiredRole85", self)

    def AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch method
        pass

    def AssemblyConnectorsReferencedInterfacesMustMatch(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement AssemblyConnectorsReferencedInterfacesMustMatch method
        pass

    def AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch method
        pass

class pcm_av_composition_av_AssemblyEventConnector(Connector):

    pass
class pcm_av_composition_av_EventChannelSinkConnector(Connector):

    pass
class pcm_av_composition_av_EventChannelSourceConnector(Connector):

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

    def __init__(self, MTTR: float, MTTF: float, requiredByContainer: bool, numberOfReplicas: int, pcm_av_resourceenvironment_av_ProcessingResourceSpecification: "SchedulingPolicy" = None, pcm_av_resourceenvironment_av_ProcessingResourceSpecification471: "ProcessingResourceType" = None, processingResourceSpecification_processingRate_PCMRandomVariable: "PCMRandomVariable" = None, activeResourceSpecifications_ResourceContainer: "ResourceContainer" = None):
        self.MTTR = MTTR
        self.MTTF = MTTF
        self.requiredByContainer = requiredByContainer
        self.numberOfReplicas = numberOfReplicas
        self.pcm_av_resourceenvironment_av_ProcessingResourceSpecification = pcm_av_resourceenvironment_av_ProcessingResourceSpecification
        self.pcm_av_resourceenvironment_av_ProcessingResourceSpecification471 = pcm_av_resourceenvironment_av_ProcessingResourceSpecification471
        self.processingResourceSpecification_processingRate_PCMRandomVariable = processingResourceSpecification_processingRate_PCMRandomVariable
        self.activeResourceSpecifications_ResourceContainer = activeResourceSpecifications_ResourceContainer
        
        pass
    @property
    def MTTF(self):
        return self.__MTTF

    @MTTF.setter
    def MTTF(self, MTTF: float):
        self.__MTTF = MTTF


    @property
    def numberOfReplicas(self):
        return self.__numberOfReplicas

    @numberOfReplicas.setter
    def numberOfReplicas(self, numberOfReplicas: int):
        self.__numberOfReplicas = numberOfReplicas


    @property
    def MTTR(self):
        return self.__MTTR

    @MTTR.setter
    def MTTR(self, MTTR: float):
        self.__MTTR = MTTR


    @property
    def requiredByContainer(self):
        return self.__requiredByContainer

    @requiredByContainer.setter
    def requiredByContainer(self, requiredByContainer: bool):
        self.__requiredByContainer = requiredByContainer


    @property
    def processingResourceSpecification_processingRate_PCMRandomVariable(self):
        return self.__processingResourceSpecification_processingRate_PCMRandomVariable

    @processingResourceSpecification_processingRate_PCMRandomVariable.setter
    def processingResourceSpecification_processingRate_PCMRandomVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_resourceenvironment_av_ProcessingResourceSpecification__processingResourceSpecification_processingRate_PCMRandomVariable", None)
        self.__processingResourceSpecification_processingRate_PCMRandomVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable474"):
                opp_val = getattr(old_value, "PCMRandomVariable474", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable474", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable474"):
                opp_val = getattr(value, "PCMRandomVariable474", None)
                setattr(value, "PCMRandomVariable474", self)

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
            if hasattr(old_value, "SchedulingPolicy469"):
                opp_val = getattr(old_value, "SchedulingPolicy469", None)
                if opp_val == self:
                    setattr(old_value, "SchedulingPolicy469", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SchedulingPolicy469"):
                opp_val = getattr(value, "SchedulingPolicy469", None)
                setattr(value, "SchedulingPolicy469", self)

    @property
    def pcm_av_resourceenvironment_av_ProcessingResourceSpecification471(self):
        return self.__pcm_av_resourceenvironment_av_ProcessingResourceSpecification471

    @pcm_av_resourceenvironment_av_ProcessingResourceSpecification471.setter
    def pcm_av_resourceenvironment_av_ProcessingResourceSpecification471(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_resourceenvironment_av_ProcessingResourceSpecification__pcm_av_resourceenvironment_av_ProcessingResourceSpecification471", None)
        self.__pcm_av_resourceenvironment_av_ProcessingResourceSpecification471 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcessingResourceType472"):
                opp_val = getattr(old_value, "ProcessingResourceType472", None)
                if opp_val == self:
                    setattr(old_value, "ProcessingResourceType472", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessingResourceType472"):
                opp_val = getattr(value, "ProcessingResourceType472", None)
                setattr(value, "ProcessingResourceType472", self)

    @property
    def activeResourceSpecifications_ResourceContainer(self):
        return self.__activeResourceSpecifications_ResourceContainer

    @activeResourceSpecifications_ResourceContainer.setter
    def activeResourceSpecifications_ResourceContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_resourceenvironment_av_ProcessingResourceSpecification__activeResourceSpecifications_ResourceContainer", None)
        self.__activeResourceSpecifications_ResourceContainer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceContainer476"):
                opp_val = getattr(old_value, "ResourceContainer476", None)
                if opp_val == self:
                    setattr(old_value, "ResourceContainer476", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceContainer476"):
                opp_val = getattr(value, "ResourceContainer476", None)
                setattr(value, "ResourceContainer476", self)

class pcm_av_seff_av_ResourceDemandingSEFF(Identifier, seff_av_ServiceEffectSpecification, seff_av_ResourceDemandingBehaviour):

    pass
class pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification(Identifier):

    def __init__(self, failureProbability: float, communicationLinkResourceSpecifications_LinkingResource: "LinkingResource" = None, pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification: "CommunicationLinkResourceType" = None, communicationLinkResourceSpecification_latency_PCMRandomVariable: "PCMRandomVariable" = None, communicationLinkResourceSpecifcation_throughput_PCMRandomVariable: "PCMRandomVariable" = None):
        self.failureProbability = failureProbability
        self.communicationLinkResourceSpecifications_LinkingResource = communicationLinkResourceSpecifications_LinkingResource
        self.pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification = pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification
        self.communicationLinkResourceSpecification_latency_PCMRandomVariable = communicationLinkResourceSpecification_latency_PCMRandomVariable
        self.communicationLinkResourceSpecifcation_throughput_PCMRandomVariable = communicationLinkResourceSpecifcation_throughput_PCMRandomVariable
        
        pass
    @property
    def failureProbability(self):
        return self.__failureProbability

    @failureProbability.setter
    def failureProbability(self, failureProbability: float):
        self.__failureProbability = failureProbability


    @property
    def communicationLinkResourceSpecifcation_throughput_PCMRandomVariable(self):
        return self.__communicationLinkResourceSpecifcation_throughput_PCMRandomVariable

    @communicationLinkResourceSpecifcation_throughput_PCMRandomVariable.setter
    def communicationLinkResourceSpecifcation_throughput_PCMRandomVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification__communicationLinkResourceSpecifcation_throughput_PCMRandomVariable", None)
        self.__communicationLinkResourceSpecifcation_throughput_PCMRandomVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable484"):
                opp_val = getattr(old_value, "PCMRandomVariable484", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable484", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable484"):
                opp_val = getattr(value, "PCMRandomVariable484", None)
                setattr(value, "PCMRandomVariable484", self)

    @property
    def communicationLinkResourceSpecification_latency_PCMRandomVariable(self):
        return self.__communicationLinkResourceSpecification_latency_PCMRandomVariable

    @communicationLinkResourceSpecification_latency_PCMRandomVariable.setter
    def communicationLinkResourceSpecification_latency_PCMRandomVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification__communicationLinkResourceSpecification_latency_PCMRandomVariable", None)
        self.__communicationLinkResourceSpecification_latency_PCMRandomVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable482"):
                opp_val = getattr(old_value, "PCMRandomVariable482", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable482", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable482"):
                opp_val = getattr(value, "PCMRandomVariable482", None)
                setattr(value, "PCMRandomVariable482", self)

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
            if hasattr(old_value, "CommunicationLinkResourceType480"):
                opp_val = getattr(old_value, "CommunicationLinkResourceType480", None)
                if opp_val == self:
                    setattr(old_value, "CommunicationLinkResourceType480", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CommunicationLinkResourceType480"):
                opp_val = getattr(value, "CommunicationLinkResourceType480", None)
                setattr(value, "CommunicationLinkResourceType480", self)

    @property
    def communicationLinkResourceSpecifications_LinkingResource(self):
        return self.__communicationLinkResourceSpecifications_LinkingResource

    @communicationLinkResourceSpecifications_LinkingResource.setter
    def communicationLinkResourceSpecifications_LinkingResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification__communicationLinkResourceSpecifications_LinkingResource", None)
        self.__communicationLinkResourceSpecifications_LinkingResource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LinkingResource478"):
                opp_val = getattr(old_value, "LinkingResource478", None)
                if opp_val == self:
                    setattr(old_value, "LinkingResource478", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LinkingResource478"):
                opp_val = getattr(value, "LinkingResource478", None)
                setattr(value, "LinkingResource478", self)

class pcm_av_seff_av_ResourceDemandingBehaviour(Identifier):

    def __init__(self, bodyBehaviour_Loop340: "AbstractLoopAction" = None, branchBehaviour_BranchTransition: "AbstractBranchTransition" = None, resourceDemandingBehaviour_AbstractAction: set["AbstractAction"] = None):
        self.bodyBehaviour_Loop340 = bodyBehaviour_Loop340
        self.branchBehaviour_BranchTransition = branchBehaviour_BranchTransition
        self.resourceDemandingBehaviour_AbstractAction = resourceDemandingBehaviour_AbstractAction if resourceDemandingBehaviour_AbstractAction is not None else set()
        
        pass
    @property
    def bodyBehaviour_Loop340(self):
        return self.__bodyBehaviour_Loop340

    @bodyBehaviour_Loop340.setter
    def bodyBehaviour_Loop340(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_av_ResourceDemandingBehaviour__bodyBehaviour_Loop340", None)
        self.__bodyBehaviour_Loop340 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractLoopAction"):
                opp_val = getattr(old_value, "AbstractLoopAction", None)
                if opp_val == self:
                    setattr(old_value, "AbstractLoopAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractLoopAction"):
                opp_val = getattr(value, "AbstractLoopAction", None)
                setattr(value, "AbstractLoopAction", self)

    @property
    def branchBehaviour_BranchTransition(self):
        return self.__branchBehaviour_BranchTransition

    @branchBehaviour_BranchTransition.setter
    def branchBehaviour_BranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_av_ResourceDemandingBehaviour__branchBehaviour_BranchTransition", None)
        self.__branchBehaviour_BranchTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractBranchTransition"):
                opp_val = getattr(old_value, "AbstractBranchTransition", None)
                if opp_val == self:
                    setattr(old_value, "AbstractBranchTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractBranchTransition"):
                opp_val = getattr(value, "AbstractBranchTransition", None)
                setattr(value, "AbstractBranchTransition", self)

    @property
    def resourceDemandingBehaviour_AbstractAction(self):
        return self.__resourceDemandingBehaviour_AbstractAction

    @resourceDemandingBehaviour_AbstractAction.setter
    def resourceDemandingBehaviour_AbstractAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_seff_av_ResourceDemandingBehaviour__resourceDemandingBehaviour_AbstractAction", None)
        self.__resourceDemandingBehaviour_AbstractAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractAction343"):
                    opp_val = getattr(item, "AbstractAction343", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractAction343", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractAction343"):
                    opp_val = getattr(item, "AbstractAction343", None)
                    
                    setattr(item, "AbstractAction343", self)
                    

    def EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor method
        pass

    def ExactlyOneStartAction(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement ExactlyOneStartAction method
        pass

    def ExactlyOneStopAction(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement ExactlyOneStopAction method
        pass

class pcm_av_entity_av_Entity(Identifier, entity_av_NamedElement):

    pass
class pcm_av_entity_av_NamedElement:

    def __init__(self, entityName: str):
        self.entityName = entityName
        
        pass
    @property
    def entityName(self):
        return self.__entityName

    @entityName.setter
    def entityName(self, entityName: str):
        self.__entityName = entityName


class entity_av_InterfaceProvidingRequiringEntity:

    pass
class composition_av_ComposedStructure:

    pass
class pcm_av_entity_av_ComposedProvidingRequiringEntity(composition_av_ComposedStructure, entity_av_InterfaceProvidingRequiringEntity):

    def __init__(self, ComposedStructure149: "pcm_av_composition_av_AssemblyContext" = None, ComposedStructure42: "pcm_av_composition_av_ResourceRequiredDelegationConnector" = None, ComposedStructure: "pcm_av_composition_av_Connector" = None, ComposedStructure48: "pcm_av_composition_av_EventChannel" = None):
        
        pass
    def ProvidedRolesMustBeBound(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement ProvidedRolesMustBeBound method
        pass

class entity_av_ResourceProvidedRole:

    pass
class RequiredRole:

    pass
class pcm_av_repository_av_SourceRole(RequiredRole):

    pass
class pcm_av_repository_av_OperationRequiredRole(RequiredRole):

    pass
class pcm_av_repository_av_InfrastructureRequiredRole(RequiredRole):

    pass
class entity_av_ResourceInterfaceRequiringEntity:

    pass
class entity_av_Entity:

    pass
class pcm_av_system_av_System(entity_av_ComposedProvidingRequiringEntity, entity_av_Entity):

    def __init__(self, system_QoSAnnotations: set["QoSAnnotations"] = None):
        self.system_QoSAnnotations = system_QoSAnnotations if system_QoSAnnotations is not None else set()
        
        pass
    @property
    def system_QoSAnnotations(self):
        return self.__system_QoSAnnotations

    @system_QoSAnnotations.setter
    def system_QoSAnnotations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_system_av_System__system_QoSAnnotations", None)
        self.__system_QoSAnnotations = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QoSAnnotations452"):
                    opp_val = getattr(item, "QoSAnnotations452", None)
                    
                    if opp_val == self:
                        setattr(item, "QoSAnnotations452", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QoSAnnotations452"):
                    opp_val = getattr(item, "QoSAnnotations452", None)
                    
                    setattr(item, "QoSAnnotations452", self)
                    

    def SystemMustHaveAtLeastOneProvidedRole(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement SystemMustHaveAtLeastOneProvidedRole method
        pass

class pcm_av_repository_av_CollectionDataType(repository_av_DataType, entity_av_Entity):

    pass
class pcm_av_repository_av_CompositeDataType(repository_av_DataType, entity_av_Entity):

    pass
class pcm_av_entity_av_InterfaceRequiringEntity(entity_av_ResourceInterfaceRequiringEntity, entity_av_Entity):

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
class pcm_av_seff_av_AbstractBranchTransition(Entity):

    pass
class pcm_av_entity_av_ResourceInterfaceProvidingEntity(Entity):

    pass
class pcm_av_repository_av_Interface(Entity):

    def __init__(self, pcm_av_repository_av_Interface: set["Interface"] = None, pcm_av_repository_av_Interface230: set["Protocol"] = None, interface_RequiredCharacterisation: set["RequiredCharacterisation"] = None, interfaces__Repository: "Repository" = None):
        self.pcm_av_repository_av_Interface = pcm_av_repository_av_Interface if pcm_av_repository_av_Interface is not None else set()
        self.pcm_av_repository_av_Interface230 = pcm_av_repository_av_Interface230 if pcm_av_repository_av_Interface230 is not None else set()
        self.interface_RequiredCharacterisation = interface_RequiredCharacterisation if interface_RequiredCharacterisation is not None else set()
        self.interfaces__Repository = interfaces__Repository
        
        pass
    @property
    def interfaces__Repository(self):
        return self.__interfaces__Repository

    @interfaces__Repository.setter
    def interfaces__Repository(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_Interface__interfaces__Repository", None)
        self.__interfaces__Repository = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Repository233"):
                opp_val = getattr(old_value, "Repository233", None)
                if opp_val == self:
                    setattr(old_value, "Repository233", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Repository233"):
                opp_val = getattr(value, "Repository233", None)
                setattr(value, "Repository233", self)

    @property
    def interface_RequiredCharacterisation(self):
        return self.__interface_RequiredCharacterisation

    @interface_RequiredCharacterisation.setter
    def interface_RequiredCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_Interface__interface_RequiredCharacterisation", None)
        self.__interface_RequiredCharacterisation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RequiredCharacterisation"):
                    opp_val = getattr(item, "RequiredCharacterisation", None)
                    
                    if opp_val == self:
                        setattr(item, "RequiredCharacterisation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RequiredCharacterisation"):
                    opp_val = getattr(item, "RequiredCharacterisation", None)
                    
                    setattr(item, "RequiredCharacterisation", self)
                    

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
                if hasattr(item, "Interface228"):
                    opp_val = getattr(item, "Interface228", None)
                    
                    if opp_val == self:
                        setattr(item, "Interface228", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Interface228"):
                    opp_val = getattr(item, "Interface228", None)
                    
                    setattr(item, "Interface228", self)
                    

    @property
    def pcm_av_repository_av_Interface230(self):
        return self.__pcm_av_repository_av_Interface230

    @pcm_av_repository_av_Interface230.setter
    def pcm_av_repository_av_Interface230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_Interface__pcm_av_repository_av_Interface230", None)
        self.__pcm_av_repository_av_Interface230 = value if value is not None else set()
        
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
                    

    def NoProtocolTypeIDUsedTwice(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement NoProtocolTypeIDUsedTwice method
        pass

class pcm_av_resourceenvironment_av_LinkingResource(Entity):

    pass
class pcm_av_resourceenvironment_av_ResourceContainer(Entity):

    pass
class pcm_av_usagemodel_av_UsageScenario(Entity):

    pass
class pcm_av_reliability_av_FailureType(Entity):

    pass
class pcm_av_resourcetype_av_ResourceSignature(Entity):

    def __init__(self, resourceServiceId: int, resourceSignature__Parameter: "Parameter" = None, resourceSignatures__ResourceInterface: "ResourceInterface" = None):
        self.resourceServiceId = resourceServiceId
        self.resourceSignature__Parameter = resourceSignature__Parameter
        self.resourceSignatures__ResourceInterface = resourceSignatures__ResourceInterface
        
        pass
    @property
    def resourceServiceId(self):
        return self.__resourceServiceId

    @resourceServiceId.setter
    def resourceServiceId(self, resourceServiceId: int):
        self.__resourceServiceId = resourceServiceId


    @property
    def resourceSignature__Parameter(self):
        return self.__resourceSignature__Parameter

    @resourceSignature__Parameter.setter
    def resourceSignature__Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_resourcetype_av_ResourceSignature__resourceSignature__Parameter", None)
        self.__resourceSignature__Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Parameter282"):
                opp_val = getattr(old_value, "Parameter282", None)
                if opp_val == self:
                    setattr(old_value, "Parameter282", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Parameter282"):
                opp_val = getattr(value, "Parameter282", None)
                setattr(value, "Parameter282", self)

    @property
    def resourceSignatures__ResourceInterface(self):
        return self.__resourceSignatures__ResourceInterface

    @resourceSignatures__ResourceInterface.setter
    def resourceSignatures__ResourceInterface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_resourcetype_av_ResourceSignature__resourceSignatures__ResourceInterface", None)
        self.__resourceSignatures__ResourceInterface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceInterface284"):
                opp_val = getattr(old_value, "ResourceInterface284", None)
                if opp_val == self:
                    setattr(old_value, "ResourceInterface284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceInterface284"):
                opp_val = getattr(value, "ResourceInterface284", None)
                setattr(value, "ResourceInterface284", self)

class pcm_av_repository_av_Repository(Entity):

    def __init__(self, repositoryDescription: str, repository__RepositoryComponent: set["RepositoryComponent"] = None, repository__Interface: set["Interface"] = None, repository__FailureType: set["FailureType"] = None, repository__DataType: set["DataType"] = None):
        self.repositoryDescription = repositoryDescription
        self.repository__RepositoryComponent = repository__RepositoryComponent if repository__RepositoryComponent is not None else set()
        self.repository__Interface = repository__Interface if repository__Interface is not None else set()
        self.repository__FailureType = repository__FailureType if repository__FailureType is not None else set()
        self.repository__DataType = repository__DataType if repository__DataType is not None else set()
        
        pass
    @property
    def repositoryDescription(self):
        return self.__repositoryDescription

    @repositoryDescription.setter
    def repositoryDescription(self, repositoryDescription: str):
        self.__repositoryDescription = repositoryDescription


    @property
    def repository__FailureType(self):
        return self.__repository__FailureType

    @repository__FailureType.setter
    def repository__FailureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_Repository__repository__FailureType", None)
        self.__repository__FailureType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FailureType"):
                    opp_val = getattr(item, "FailureType", None)
                    
                    if opp_val == self:
                        setattr(item, "FailureType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FailureType"):
                    opp_val = getattr(item, "FailureType", None)
                    
                    setattr(item, "FailureType", self)
                    

    @property
    def repository__RepositoryComponent(self):
        return self.__repository__RepositoryComponent

    @repository__RepositoryComponent.setter
    def repository__RepositoryComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_Repository__repository__RepositoryComponent", None)
        self.__repository__RepositoryComponent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RepositoryComponent222"):
                    opp_val = getattr(item, "RepositoryComponent222", None)
                    
                    if opp_val == self:
                        setattr(item, "RepositoryComponent222", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RepositoryComponent222"):
                    opp_val = getattr(item, "RepositoryComponent222", None)
                    
                    setattr(item, "RepositoryComponent222", self)
                    

    @property
    def repository__Interface(self):
        return self.__repository__Interface

    @repository__Interface.setter
    def repository__Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_Repository__repository__Interface", None)
        self.__repository__Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Interface"):
                    opp_val = getattr(item, "Interface", None)
                    
                    if opp_val == self:
                        setattr(item, "Interface", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Interface"):
                    opp_val = getattr(item, "Interface", None)
                    
                    setattr(item, "Interface", self)
                    

    @property
    def repository__DataType(self):
        return self.__repository__DataType

    @repository__DataType.setter
    def repository__DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_Repository__repository__DataType", None)
        self.__repository__DataType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataType226"):
                    opp_val = getattr(item, "DataType226", None)
                    
                    if opp_val == self:
                        setattr(item, "DataType226", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataType226"):
                    opp_val = getattr(item, "DataType226", None)
                    
                    setattr(item, "DataType226", self)
                    

class pcm_av_entity_av_ResourceInterfaceRequiringEntity(Entity):

    pass
class pcm_av_repository_av_Signature(Entity):

    pass
class pcm_av_repository_av_Role(Entity):

    pass
class pcm_av_composition_av_Connector(Entity):

    pass
class pcm_av_seff_av_AbstractAction(Entity):

    pass
class pcm_av_allocation_av_Allocation(Entity):

    def __init__(self, pcm_av_allocation_av_Allocation: "ResourceEnvironment" = None, pcm_av_allocation_av_Allocation496: "System" = None, allocation_AllocationContext: set["AllocationContext"] = None):
        self.pcm_av_allocation_av_Allocation = pcm_av_allocation_av_Allocation
        self.pcm_av_allocation_av_Allocation496 = pcm_av_allocation_av_Allocation496
        self.allocation_AllocationContext = allocation_AllocationContext if allocation_AllocationContext is not None else set()
        
        pass
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
            if hasattr(old_value, "ResourceEnvironment494"):
                opp_val = getattr(old_value, "ResourceEnvironment494", None)
                if opp_val == self:
                    setattr(old_value, "ResourceEnvironment494", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceEnvironment494"):
                opp_val = getattr(value, "ResourceEnvironment494", None)
                setattr(value, "ResourceEnvironment494", self)

    @property
    def pcm_av_allocation_av_Allocation496(self):
        return self.__pcm_av_allocation_av_Allocation496

    @pcm_av_allocation_av_Allocation496.setter
    def pcm_av_allocation_av_Allocation496(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_allocation_av_Allocation__pcm_av_allocation_av_Allocation496", None)
        self.__pcm_av_allocation_av_Allocation496 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "System497"):
                opp_val = getattr(old_value, "System497", None)
                if opp_val == self:
                    setattr(old_value, "System497", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "System497"):
                opp_val = getattr(value, "System497", None)
                setattr(value, "System497", self)

    @property
    def allocation_AllocationContext(self):
        return self.__allocation_AllocationContext

    @allocation_AllocationContext.setter
    def allocation_AllocationContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_allocation_av_Allocation__allocation_AllocationContext", None)
        self.__allocation_AllocationContext = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AllocationContext"):
                    opp_val = getattr(item, "AllocationContext", None)
                    
                    if opp_val == self:
                        setattr(item, "AllocationContext", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AllocationContext"):
                    opp_val = getattr(item, "AllocationContext", None)
                    
                    setattr(item, "AllocationContext", self)
                    

    def EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce method
        pass

    def CommunicatingServersHaveToBeConnectedByLinkingResource(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement CommunicatingServersHaveToBeConnectedByLinkingResource method
        pass

class pcm_av_composition_av_EventChannel(Entity):

    pass
class pcm_av_qosannotations_av_QoSAnnotations(Entity):

    def __init__(self, qosAnnotations_SpecifiedOutputParameterAbstraction: set["SpecifiedOutputParameterAbstraction"] = None, qosAnnotations_System: "System" = None, qosAnnotations_SpecifiedQoSAnnotation: set["SpecifiedQoSAnnotation"] = None):
        self.qosAnnotations_SpecifiedOutputParameterAbstraction = qosAnnotations_SpecifiedOutputParameterAbstraction if qosAnnotations_SpecifiedOutputParameterAbstraction is not None else set()
        self.qosAnnotations_System = qosAnnotations_System
        self.qosAnnotations_SpecifiedQoSAnnotation = qosAnnotations_SpecifiedQoSAnnotation if qosAnnotations_SpecifiedQoSAnnotation is not None else set()
        
        pass
    @property
    def qosAnnotations_System(self):
        return self.__qosAnnotations_System

    @qosAnnotations_System.setter
    def qosAnnotations_System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_qosannotations_av_QoSAnnotations__qosAnnotations_System", None)
        self.__qosAnnotations_System = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "System"):
                opp_val = getattr(old_value, "System", None)
                if opp_val == self:
                    setattr(old_value, "System", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "System"):
                opp_val = getattr(value, "System", None)
                setattr(value, "System", self)

    @property
    def qosAnnotations_SpecifiedOutputParameterAbstraction(self):
        return self.__qosAnnotations_SpecifiedOutputParameterAbstraction

    @qosAnnotations_SpecifiedOutputParameterAbstraction.setter
    def qosAnnotations_SpecifiedOutputParameterAbstraction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_qosannotations_av_QoSAnnotations__qosAnnotations_SpecifiedOutputParameterAbstraction", None)
        self.__qosAnnotations_SpecifiedOutputParameterAbstraction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SpecifiedOutputParameterAbstraction434"):
                    opp_val = getattr(item, "SpecifiedOutputParameterAbstraction434", None)
                    
                    if opp_val == self:
                        setattr(item, "SpecifiedOutputParameterAbstraction434", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SpecifiedOutputParameterAbstraction434"):
                    opp_val = getattr(item, "SpecifiedOutputParameterAbstraction434", None)
                    
                    setattr(item, "SpecifiedOutputParameterAbstraction434", self)
                    

    @property
    def qosAnnotations_SpecifiedQoSAnnotation(self):
        return self.__qosAnnotations_SpecifiedQoSAnnotation

    @qosAnnotations_SpecifiedQoSAnnotation.setter
    def qosAnnotations_SpecifiedQoSAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_qosannotations_av_QoSAnnotations__qosAnnotations_SpecifiedQoSAnnotation", None)
        self.__qosAnnotations_SpecifiedQoSAnnotation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SpecifiedQoSAnnotation"):
                    opp_val = getattr(item, "SpecifiedQoSAnnotation", None)
                    
                    if opp_val == self:
                        setattr(item, "SpecifiedQoSAnnotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SpecifiedQoSAnnotation"):
                    opp_val = getattr(item, "SpecifiedQoSAnnotation", None)
                    
                    setattr(item, "SpecifiedQoSAnnotation", self)
                    

    def MultipleReliabilityAnnotationsPerExternalCallNotAllowed(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement MultipleReliabilityAnnotationsPerExternalCallNotAllowed method
        pass

class pcm_av_composition_av_ComposedStructure(Entity):

    def __init__(self, parentStructure__AssemblyContext: set["composition_av_AssemblyContext"] = None, parentStructure_ResourceRequiredDelegationConnector: set["composition_av_ResourceRequiredDelegationConnector"] = None, parentStructure__EventChannel: set["composition_av_EventChannel"] = None, parentStructure__Connector: set["composition_av_Connector"] = None):
        self.parentStructure__AssemblyContext = parentStructure__AssemblyContext if parentStructure__AssemblyContext is not None else set()
        self.parentStructure_ResourceRequiredDelegationConnector = parentStructure_ResourceRequiredDelegationConnector if parentStructure_ResourceRequiredDelegationConnector is not None else set()
        self.parentStructure__EventChannel = parentStructure__EventChannel if parentStructure__EventChannel is not None else set()
        self.parentStructure__Connector = parentStructure__Connector if parentStructure__Connector is not None else set()
        
        pass
    @property
    def parentStructure__EventChannel(self):
        return self.__parentStructure__EventChannel

    @parentStructure__EventChannel.setter
    def parentStructure__EventChannel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_composition_av_ComposedStructure__parentStructure__EventChannel", None)
        self.__parentStructure__EventChannel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EventChannel"):
                    opp_val = getattr(item, "EventChannel", None)
                    
                    if opp_val == self:
                        setattr(item, "EventChannel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EventChannel"):
                    opp_val = getattr(item, "EventChannel", None)
                    
                    setattr(item, "EventChannel", self)
                    

    @property
    def parentStructure__Connector(self):
        return self.__parentStructure__Connector

    @parentStructure__Connector.setter
    def parentStructure__Connector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_composition_av_ComposedStructure__parentStructure__Connector", None)
        self.__parentStructure__Connector = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Connector"):
                    opp_val = getattr(item, "Connector", None)
                    
                    if opp_val == self:
                        setattr(item, "Connector", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connector"):
                    opp_val = getattr(item, "Connector", None)
                    
                    setattr(item, "Connector", self)
                    

    @property
    def parentStructure_ResourceRequiredDelegationConnector(self):
        return self.__parentStructure_ResourceRequiredDelegationConnector

    @parentStructure_ResourceRequiredDelegationConnector.setter
    def parentStructure_ResourceRequiredDelegationConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_composition_av_ComposedStructure__parentStructure_ResourceRequiredDelegationConnector", None)
        self.__parentStructure_ResourceRequiredDelegationConnector = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ResourceRequiredDelegationConnector"):
                    opp_val = getattr(item, "ResourceRequiredDelegationConnector", None)
                    
                    if opp_val == self:
                        setattr(item, "ResourceRequiredDelegationConnector", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ResourceRequiredDelegationConnector"):
                    opp_val = getattr(item, "ResourceRequiredDelegationConnector", None)
                    
                    setattr(item, "ResourceRequiredDelegationConnector", self)
                    

    @property
    def parentStructure__AssemblyContext(self):
        return self.__parentStructure__AssemblyContext

    @parentStructure__AssemblyContext.setter
    def parentStructure__AssemblyContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_composition_av_ComposedStructure__parentStructure__AssemblyContext", None)
        self.__parentStructure__AssemblyContext = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AssemblyContext"):
                    opp_val = getattr(item, "AssemblyContext", None)
                    
                    if opp_val == self:
                        setattr(item, "AssemblyContext", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AssemblyContext"):
                    opp_val = getattr(item, "AssemblyContext", None)
                    
                    setattr(item, "AssemblyContext", self)
                    

    def MultipleConnectorsConstraint(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement MultipleConnectorsConstraint method
        pass

    def MultipleConnectorsConstraintForAssemblyConnectors(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement MultipleConnectorsConstraintForAssemblyConnectors method
        pass

class pcm_av_resourcetype_av_ResourceInterface(Entity):

    pass
class pcm_av_seff_reliability_av_FailureHandlingEntity(Entity):

    pass
class pcm_av_resourcetype_av_SchedulingPolicy(Entity):

    pass
class pcm_av_allocation_av_AllocationContext(Entity):

    def __init__(self, pcm_av_allocation_av_AllocationContext488: "composition_av_AssemblyContext" = None, allocationContexts_Allocation: "Allocation" = None, pcm_av_allocation_av_AllocationContext492: "composition_av_EventChannel" = None, pcm_av_allocation_av_AllocationContext: "ResourceContainer" = None):
        self.pcm_av_allocation_av_AllocationContext488 = pcm_av_allocation_av_AllocationContext488
        self.allocationContexts_Allocation = allocationContexts_Allocation
        self.pcm_av_allocation_av_AllocationContext492 = pcm_av_allocation_av_AllocationContext492
        self.pcm_av_allocation_av_AllocationContext = pcm_av_allocation_av_AllocationContext
        
        pass
    @property
    def pcm_av_allocation_av_AllocationContext492(self):
        return self.__pcm_av_allocation_av_AllocationContext492

    @pcm_av_allocation_av_AllocationContext492.setter
    def pcm_av_allocation_av_AllocationContext492(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_allocation_av_AllocationContext__pcm_av_allocation_av_AllocationContext492", None)
        self.__pcm_av_allocation_av_AllocationContext492 = value
        
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
    def pcm_av_allocation_av_AllocationContext488(self):
        return self.__pcm_av_allocation_av_AllocationContext488

    @pcm_av_allocation_av_AllocationContext488.setter
    def pcm_av_allocation_av_AllocationContext488(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_allocation_av_AllocationContext__pcm_av_allocation_av_AllocationContext488", None)
        self.__pcm_av_allocation_av_AllocationContext488 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_AssemblyContext489"):
                opp_val = getattr(old_value, "composition_av_AssemblyContext489", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_AssemblyContext489", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_AssemblyContext489"):
                opp_val = getattr(value, "composition_av_AssemblyContext489", None)
                setattr(value, "composition_av_AssemblyContext489", self)

    @property
    def allocationContexts_Allocation(self):
        return self.__allocationContexts_Allocation

    @allocationContexts_Allocation.setter
    def allocationContexts_Allocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_allocation_av_AllocationContext__allocationContexts_Allocation", None)
        self.__allocationContexts_Allocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Allocation"):
                opp_val = getattr(old_value, "Allocation", None)
                if opp_val == self:
                    setattr(old_value, "Allocation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Allocation"):
                opp_val = getattr(value, "Allocation", None)
                setattr(value, "Allocation", self)

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
            if hasattr(old_value, "ResourceContainer486"):
                opp_val = getattr(old_value, "ResourceContainer486", None)
                if opp_val == self:
                    setattr(old_value, "ResourceContainer486", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceContainer486"):
                opp_val = getattr(value, "ResourceContainer486", None)
                setattr(value, "ResourceContainer486", self)

    def OneAssemblyContextOrOneEventChannelShouldBeReferred(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement OneAssemblyContextOrOneEventChannelShouldBeReferred method
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
class pcm_av_resourcetype_av_ResourceType(entity_av_ResourceInterfaceProvidingEntity, UnitCarryingElement, entity_av_Entity):

    pass
class pcm_av_entity_av_ResourceInterfaceProvidingRequiringEntity(entity_av_ResourceInterfaceProvidingEntity, entity_av_ResourceInterfaceRequiringEntity):

    pass
class Role:

    pass
class pcm_av_repository_av_RequiredRole(Role):

    pass
class pcm_av_repository_av_ProvidedRole(Role):

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
class Loop:

    pass
class composition_av_AssemblyEventConnector:

    pass
class composition_av_EventChannelSinkConnector:

    pass
class pcm_av_entity_av_ResourceRequiredRole(Role):

    pass
class entity_av_ResourceRequiredRole:

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

    def __init__(self, branchCondition_GuardedBranchTransition: "GuardedBranchTransition" = None, thinkTime_ClosedWorkload: "ClosedWorkload" = None, capacity_PassiveResource: "PassiveResource" = None, specification_VariableCharacterisation: "VariableCharacterisation" = None, numberOfCalls__InfrastructureCall: "seff_performance_av_InfrastructureCall" = None, numberOfCalls__ResourceCall: "seff_performance_av_ResourceCall" = None, specification_ParametericResourceDemand: "seff_performance_av_ParametricResourceDemand" = None, iterationCount_LoopAction: "LoopAction" = None, specification_SpecifiedExecutionTime: "qos_performance_av_SpecifiedExecutionTime" = None, filterCondition__EventChannelSinkConnector: "composition_av_EventChannelSinkConnector" = None, filterCondition__AssemblyEventConnector: "composition_av_AssemblyEventConnector" = None, loopIteration_Loop: "Loop" = None, interArrivalTime_OpenWorkload: "OpenWorkload" = None, timeSpecification_Delay: "Delay" = None, throughput_CommunicationLinkResourceSpecification: "CommunicationLinkResourceSpecification" = None, processingRate_ProcessingResourceSpecification: "ProcessingResourceSpecification" = None, latency_CommunicationLinkResourceSpecification: "CommunicationLinkResourceSpecification" = None):
        self.branchCondition_GuardedBranchTransition = branchCondition_GuardedBranchTransition
        self.thinkTime_ClosedWorkload = thinkTime_ClosedWorkload
        self.capacity_PassiveResource = capacity_PassiveResource
        self.specification_VariableCharacterisation = specification_VariableCharacterisation
        self.numberOfCalls__InfrastructureCall = numberOfCalls__InfrastructureCall
        self.numberOfCalls__ResourceCall = numberOfCalls__ResourceCall
        self.specification_ParametericResourceDemand = specification_ParametericResourceDemand
        self.iterationCount_LoopAction = iterationCount_LoopAction
        self.specification_SpecifiedExecutionTime = specification_SpecifiedExecutionTime
        self.filterCondition__EventChannelSinkConnector = filterCondition__EventChannelSinkConnector
        self.filterCondition__AssemblyEventConnector = filterCondition__AssemblyEventConnector
        self.loopIteration_Loop = loopIteration_Loop
        self.interArrivalTime_OpenWorkload = interArrivalTime_OpenWorkload
        self.timeSpecification_Delay = timeSpecification_Delay
        self.throughput_CommunicationLinkResourceSpecification = throughput_CommunicationLinkResourceSpecification
        self.processingRate_ProcessingResourceSpecification = processingRate_ProcessingResourceSpecification
        self.latency_CommunicationLinkResourceSpecification = latency_CommunicationLinkResourceSpecification
        
        pass
    @property
    def specification_SpecifiedExecutionTime(self):
        return self.__specification_SpecifiedExecutionTime

    @specification_SpecifiedExecutionTime.setter
    def specification_SpecifiedExecutionTime(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__specification_SpecifiedExecutionTime", None)
        self.__specification_SpecifiedExecutionTime = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SpecifiedExecutionTime"):
                opp_val = getattr(old_value, "SpecifiedExecutionTime", None)
                if opp_val == self:
                    setattr(old_value, "SpecifiedExecutionTime", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SpecifiedExecutionTime"):
                opp_val = getattr(value, "SpecifiedExecutionTime", None)
                setattr(value, "SpecifiedExecutionTime", self)

    @property
    def throughput_CommunicationLinkResourceSpecification(self):
        return self.__throughput_CommunicationLinkResourceSpecification

    @throughput_CommunicationLinkResourceSpecification.setter
    def throughput_CommunicationLinkResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__throughput_CommunicationLinkResourceSpecification", None)
        self.__throughput_CommunicationLinkResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CommunicationLinkResourceSpecification"):
                opp_val = getattr(old_value, "CommunicationLinkResourceSpecification", None)
                if opp_val == self:
                    setattr(old_value, "CommunicationLinkResourceSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CommunicationLinkResourceSpecification"):
                opp_val = getattr(value, "CommunicationLinkResourceSpecification", None)
                setattr(value, "CommunicationLinkResourceSpecification", self)

    @property
    def processingRate_ProcessingResourceSpecification(self):
        return self.__processingRate_ProcessingResourceSpecification

    @processingRate_ProcessingResourceSpecification.setter
    def processingRate_ProcessingResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__processingRate_ProcessingResourceSpecification", None)
        self.__processingRate_ProcessingResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcessingResourceSpecification"):
                opp_val = getattr(old_value, "ProcessingResourceSpecification", None)
                if opp_val == self:
                    setattr(old_value, "ProcessingResourceSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessingResourceSpecification"):
                opp_val = getattr(value, "ProcessingResourceSpecification", None)
                setattr(value, "ProcessingResourceSpecification", self)

    @property
    def latency_CommunicationLinkResourceSpecification(self):
        return self.__latency_CommunicationLinkResourceSpecification

    @latency_CommunicationLinkResourceSpecification.setter
    def latency_CommunicationLinkResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__latency_CommunicationLinkResourceSpecification", None)
        self.__latency_CommunicationLinkResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CommunicationLinkResourceSpecification22"):
                opp_val = getattr(old_value, "CommunicationLinkResourceSpecification22", None)
                if opp_val == self:
                    setattr(old_value, "CommunicationLinkResourceSpecification22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CommunicationLinkResourceSpecification22"):
                opp_val = getattr(value, "CommunicationLinkResourceSpecification22", None)
                setattr(value, "CommunicationLinkResourceSpecification22", self)

    @property
    def specification_VariableCharacterisation(self):
        return self.__specification_VariableCharacterisation

    @specification_VariableCharacterisation.setter
    def specification_VariableCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__specification_VariableCharacterisation", None)
        self.__specification_VariableCharacterisation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableCharacterisation"):
                opp_val = getattr(old_value, "VariableCharacterisation", None)
                if opp_val == self:
                    setattr(old_value, "VariableCharacterisation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableCharacterisation"):
                opp_val = getattr(value, "VariableCharacterisation", None)
                setattr(value, "VariableCharacterisation", self)

    @property
    def specification_ParametericResourceDemand(self):
        return self.__specification_ParametericResourceDemand

    @specification_ParametericResourceDemand.setter
    def specification_ParametericResourceDemand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__specification_ParametericResourceDemand", None)
        self.__specification_ParametericResourceDemand = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ParametricResourceDemand"):
                opp_val = getattr(old_value, "ParametricResourceDemand", None)
                if opp_val == self:
                    setattr(old_value, "ParametricResourceDemand", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ParametricResourceDemand"):
                opp_val = getattr(value, "ParametricResourceDemand", None)
                setattr(value, "ParametricResourceDemand", self)

    @property
    def interArrivalTime_OpenWorkload(self):
        return self.__interArrivalTime_OpenWorkload

    @interArrivalTime_OpenWorkload.setter
    def interArrivalTime_OpenWorkload(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__interArrivalTime_OpenWorkload", None)
        self.__interArrivalTime_OpenWorkload = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OpenWorkload"):
                opp_val = getattr(old_value, "OpenWorkload", None)
                if opp_val == self:
                    setattr(old_value, "OpenWorkload", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OpenWorkload"):
                opp_val = getattr(value, "OpenWorkload", None)
                setattr(value, "OpenWorkload", self)

    @property
    def thinkTime_ClosedWorkload(self):
        return self.__thinkTime_ClosedWorkload

    @thinkTime_ClosedWorkload.setter
    def thinkTime_ClosedWorkload(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__thinkTime_ClosedWorkload", None)
        self.__thinkTime_ClosedWorkload = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClosedWorkload"):
                opp_val = getattr(old_value, "ClosedWorkload", None)
                if opp_val == self:
                    setattr(old_value, "ClosedWorkload", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClosedWorkload"):
                opp_val = getattr(value, "ClosedWorkload", None)
                setattr(value, "ClosedWorkload", self)

    @property
    def capacity_PassiveResource(self):
        return self.__capacity_PassiveResource

    @capacity_PassiveResource.setter
    def capacity_PassiveResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__capacity_PassiveResource", None)
        self.__capacity_PassiveResource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PassiveResource"):
                opp_val = getattr(old_value, "PassiveResource", None)
                if opp_val == self:
                    setattr(old_value, "PassiveResource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PassiveResource"):
                opp_val = getattr(value, "PassiveResource", None)
                setattr(value, "PassiveResource", self)

    @property
    def timeSpecification_Delay(self):
        return self.__timeSpecification_Delay

    @timeSpecification_Delay.setter
    def timeSpecification_Delay(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__timeSpecification_Delay", None)
        self.__timeSpecification_Delay = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Delay"):
                opp_val = getattr(old_value, "Delay", None)
                if opp_val == self:
                    setattr(old_value, "Delay", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Delay"):
                opp_val = getattr(value, "Delay", None)
                setattr(value, "Delay", self)

    @property
    def loopIteration_Loop(self):
        return self.__loopIteration_Loop

    @loopIteration_Loop.setter
    def loopIteration_Loop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__loopIteration_Loop", None)
        self.__loopIteration_Loop = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Loop"):
                opp_val = getattr(old_value, "Loop", None)
                if opp_val == self:
                    setattr(old_value, "Loop", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Loop"):
                opp_val = getattr(value, "Loop", None)
                setattr(value, "Loop", self)

    @property
    def iterationCount_LoopAction(self):
        return self.__iterationCount_LoopAction

    @iterationCount_LoopAction.setter
    def iterationCount_LoopAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__iterationCount_LoopAction", None)
        self.__iterationCount_LoopAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LoopAction"):
                opp_val = getattr(old_value, "LoopAction", None)
                if opp_val == self:
                    setattr(old_value, "LoopAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LoopAction"):
                opp_val = getattr(value, "LoopAction", None)
                setattr(value, "LoopAction", self)

    @property
    def numberOfCalls__ResourceCall(self):
        return self.__numberOfCalls__ResourceCall

    @numberOfCalls__ResourceCall.setter
    def numberOfCalls__ResourceCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__numberOfCalls__ResourceCall", None)
        self.__numberOfCalls__ResourceCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceCall"):
                opp_val = getattr(old_value, "ResourceCall", None)
                if opp_val == self:
                    setattr(old_value, "ResourceCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceCall"):
                opp_val = getattr(value, "ResourceCall", None)
                setattr(value, "ResourceCall", self)

    @property
    def filterCondition__EventChannelSinkConnector(self):
        return self.__filterCondition__EventChannelSinkConnector

    @filterCondition__EventChannelSinkConnector.setter
    def filterCondition__EventChannelSinkConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__filterCondition__EventChannelSinkConnector", None)
        self.__filterCondition__EventChannelSinkConnector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EventChannelSinkConnector"):
                opp_val = getattr(old_value, "EventChannelSinkConnector", None)
                if opp_val == self:
                    setattr(old_value, "EventChannelSinkConnector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EventChannelSinkConnector"):
                opp_val = getattr(value, "EventChannelSinkConnector", None)
                setattr(value, "EventChannelSinkConnector", self)

    @property
    def numberOfCalls__InfrastructureCall(self):
        return self.__numberOfCalls__InfrastructureCall

    @numberOfCalls__InfrastructureCall.setter
    def numberOfCalls__InfrastructureCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__numberOfCalls__InfrastructureCall", None)
        self.__numberOfCalls__InfrastructureCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InfrastructureCall"):
                opp_val = getattr(old_value, "InfrastructureCall", None)
                if opp_val == self:
                    setattr(old_value, "InfrastructureCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InfrastructureCall"):
                opp_val = getattr(value, "InfrastructureCall", None)
                setattr(value, "InfrastructureCall", self)

    @property
    def branchCondition_GuardedBranchTransition(self):
        return self.__branchCondition_GuardedBranchTransition

    @branchCondition_GuardedBranchTransition.setter
    def branchCondition_GuardedBranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__branchCondition_GuardedBranchTransition", None)
        self.__branchCondition_GuardedBranchTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GuardedBranchTransition"):
                opp_val = getattr(old_value, "GuardedBranchTransition", None)
                if opp_val == self:
                    setattr(old_value, "GuardedBranchTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GuardedBranchTransition"):
                opp_val = getattr(value, "GuardedBranchTransition", None)
                setattr(value, "GuardedBranchTransition", self)

    @property
    def filterCondition__AssemblyEventConnector(self):
        return self.__filterCondition__AssemblyEventConnector

    @filterCondition__AssemblyEventConnector.setter
    def filterCondition__AssemblyEventConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_core_av_PCMRandomVariable__filterCondition__AssemblyEventConnector", None)
        self.__filterCondition__AssemblyEventConnector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AssemblyEventConnector"):
                opp_val = getattr(old_value, "AssemblyEventConnector", None)
                if opp_val == self:
                    setattr(old_value, "AssemblyEventConnector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AssemblyEventConnector"):
                opp_val = getattr(value, "AssemblyEventConnector", None)
                setattr(value, "AssemblyEventConnector", self)

    def SpecificationMustNotBeNULL(self, pcm_av_diagnostics, pcm_av_context) :
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
class qos_performance_av_SpecifiedExecutionTime:

    pass
class GuardedBranchTransition:

    pass
class InterfaceProvidingRequiringEntity:

    pass
class pcm_av_repository_av_RepositoryComponent(InterfaceProvidingRequiringEntity):

    pass
class CompleteComponentType:

    pass
class InfrastructureSignature:

    pass
class pcm_av_repository_av_ImplementationComponentType(RepositoryComponent):

    def __init__(self, componentType: str, pcm_av_repository_av_ImplementationComponentType: set["CompleteComponentType"] = None, pcm_av_repository_av_ImplementationComponentType209: set["VariableUsage"] = None, RepositoryComponent: "pcm_av_composition_av_AssemblyContext" = None, RepositoryComponent222: "pcm_av_repository_av_Repository" = None):
        self.componentType = componentType
        self.pcm_av_repository_av_ImplementationComponentType = pcm_av_repository_av_ImplementationComponentType if pcm_av_repository_av_ImplementationComponentType is not None else set()
        self.pcm_av_repository_av_ImplementationComponentType209 = pcm_av_repository_av_ImplementationComponentType209 if pcm_av_repository_av_ImplementationComponentType209 is not None else set()
        
        pass
    @property
    def componentType(self):
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
    def pcm_av_repository_av_ImplementationComponentType209(self):
        return self.__pcm_av_repository_av_ImplementationComponentType209

    @pcm_av_repository_av_ImplementationComponentType209.setter
    def pcm_av_repository_av_ImplementationComponentType209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_ImplementationComponentType__pcm_av_repository_av_ImplementationComponentType209", None)
        self.__pcm_av_repository_av_ImplementationComponentType209 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableUsage210"):
                    opp_val = getattr(item, "VariableUsage210", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableUsage210", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableUsage210"):
                    opp_val = getattr(item, "VariableUsage210", None)
                    
                    setattr(item, "VariableUsage210", self)
                    

    def ProvidedInterfaceHaveToConformToComponentType(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement ProvidedInterfaceHaveToConformToComponentType method
        pass

    def providedInterfacesHaveToConformToCompleteType(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement providedInterfacesHaveToConformToCompleteType method
        pass

    def RequiredInterfacesHaveToConformToCompleteType(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement RequiredInterfacesHaveToConformToCompleteType method
        pass

class ServiceEffectSpecification:

    pass
class ImplementationComponentType:

    pass
class pcm_av_repository_av_BasicComponent(ImplementationComponentType):

    def __init__(self, basicComponent_ServiceEffectSpecification: set["ServiceEffectSpecification"] = None, basicComponent_PassiveResource: set["PassiveResource"] = None):
        self.basicComponent_ServiceEffectSpecification = basicComponent_ServiceEffectSpecification if basicComponent_ServiceEffectSpecification is not None else set()
        self.basicComponent_PassiveResource = basicComponent_PassiveResource if basicComponent_PassiveResource is not None else set()
        
        pass
    @property
    def basicComponent_ServiceEffectSpecification(self):
        return self.__basicComponent_ServiceEffectSpecification

    @basicComponent_ServiceEffectSpecification.setter
    def basicComponent_ServiceEffectSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_BasicComponent__basicComponent_ServiceEffectSpecification", None)
        self.__basicComponent_ServiceEffectSpecification = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ServiceEffectSpecification"):
                    opp_val = getattr(item, "ServiceEffectSpecification", None)
                    
                    if opp_val == self:
                        setattr(item, "ServiceEffectSpecification", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ServiceEffectSpecification"):
                    opp_val = getattr(item, "ServiceEffectSpecification", None)
                    
                    setattr(item, "ServiceEffectSpecification", self)
                    

    @property
    def basicComponent_PassiveResource(self):
        return self.__basicComponent_PassiveResource

    @basicComponent_PassiveResource.setter
    def basicComponent_PassiveResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_repository_av_BasicComponent__basicComponent_PassiveResource", None)
        self.__basicComponent_PassiveResource = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PassiveResource206"):
                    opp_val = getattr(item, "PassiveResource206", None)
                    
                    if opp_val == self:
                        setattr(item, "PassiveResource206", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PassiveResource206"):
                    opp_val = getattr(item, "PassiveResource206", None)
                    
                    setattr(item, "PassiveResource206", self)
                    

    def NoSeffTypeUsedTwice(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement NoSeffTypeUsedTwice method
        pass

    def RequireSameInterfacesAsImplementationType(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement RequireSameInterfacesAsImplementationType method
        pass

    def ProvideSameInterfacesAsImplementationType(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement ProvideSameInterfacesAsImplementationType method
        pass

class ResourceTimeoutFailureType:

    pass
class BasicComponent:

    pass
class pcm_av_repository_av_PassiveResource(Entity):

    pass
class pcm_av_usagemodel_av_ClosedWorkload(Workload):

    def __init__(self, population: int, closedWorkload_PCMRandomVariable: "PCMRandomVariable" = None, Workload: "pcm_av_usagemodel_av_UsageScenario" = None):
        self.population = population
        self.closedWorkload_PCMRandomVariable = closedWorkload_PCMRandomVariable
        
        pass
    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, population: int):
        self.__population = population


    @property
    def closedWorkload_PCMRandomVariable(self):
        return self.__closedWorkload_PCMRandomVariable

    @closedWorkload_PCMRandomVariable.setter
    def closedWorkload_PCMRandomVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_usagemodel_av_ClosedWorkload__closedWorkload_PCMRandomVariable", None)
        self.__closedWorkload_PCMRandomVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable199"):
                opp_val = getattr(old_value, "PCMRandomVariable199", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable199", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable199"):
                opp_val = getattr(value, "PCMRandomVariable199", None)
                setattr(value, "PCMRandomVariable199", self)

    def ThinkTimeInClosedWorkloadNeedsToBeSpecified(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement ThinkTimeInClosedWorkloadNeedsToBeSpecified method
        pass

    def PopulationInClosedWorkloadNeedsToBeSpecified(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement PopulationInClosedWorkloadNeedsToBeSpecified method
        pass

class pcm_av_usagemodel_av_OpenWorkload(Workload):

    def __init__(self, openWorkload_PCMRandomVariable: "PCMRandomVariable" = None, Workload: "pcm_av_usagemodel_av_UsageScenario" = None):
        self.openWorkload_PCMRandomVariable = openWorkload_PCMRandomVariable
        
        pass
    @property
    def openWorkload_PCMRandomVariable(self):
        return self.__openWorkload_PCMRandomVariable

    @openWorkload_PCMRandomVariable.setter
    def openWorkload_PCMRandomVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_usagemodel_av_OpenWorkload__openWorkload_PCMRandomVariable", None)
        self.__openWorkload_PCMRandomVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable195"):
                opp_val = getattr(old_value, "PCMRandomVariable195", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable195"):
                opp_val = getattr(value, "PCMRandomVariable195", None)
                setattr(value, "PCMRandomVariable195", self)

    def InterArrivalTimeInOpenWorkloadNeedsToBeSpecified(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement InterArrivalTimeInOpenWorkloadNeedsToBeSpecified method
        pass

class BranchTransition:

    pass
class pcm_av_usagemodel_av_ScenarioBehaviour(Entity):

    def __init__(self, scenarioBehaviour_UsageScenario: "UsageScenario" = None, branchedBehaviour_BranchTransition: "BranchTransition" = None, bodyBehaviour_Loop: "Loop" = None, scenarioBehaviour_AbstractUserAction: set["AbstractUserAction"] = None):
        self.scenarioBehaviour_UsageScenario = scenarioBehaviour_UsageScenario
        self.branchedBehaviour_BranchTransition = branchedBehaviour_BranchTransition
        self.bodyBehaviour_Loop = bodyBehaviour_Loop
        self.scenarioBehaviour_AbstractUserAction = scenarioBehaviour_AbstractUserAction if scenarioBehaviour_AbstractUserAction is not None else set()
        
        pass
    @property
    def scenarioBehaviour_AbstractUserAction(self):
        return self.__scenarioBehaviour_AbstractUserAction

    @scenarioBehaviour_AbstractUserAction.setter
    def scenarioBehaviour_AbstractUserAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_usagemodel_av_ScenarioBehaviour__scenarioBehaviour_AbstractUserAction", None)
        self.__scenarioBehaviour_AbstractUserAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractUserAction184"):
                    opp_val = getattr(item, "AbstractUserAction184", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractUserAction184", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractUserAction184"):
                    opp_val = getattr(item, "AbstractUserAction184", None)
                    
                    setattr(item, "AbstractUserAction184", self)
                    

    @property
    def bodyBehaviour_Loop(self):
        return self.__bodyBehaviour_Loop

    @bodyBehaviour_Loop.setter
    def bodyBehaviour_Loop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_usagemodel_av_ScenarioBehaviour__bodyBehaviour_Loop", None)
        self.__bodyBehaviour_Loop = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Loop182"):
                opp_val = getattr(old_value, "Loop182", None)
                if opp_val == self:
                    setattr(old_value, "Loop182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Loop182"):
                opp_val = getattr(value, "Loop182", None)
                setattr(value, "Loop182", self)

    @property
    def branchedBehaviour_BranchTransition(self):
        return self.__branchedBehaviour_BranchTransition

    @branchedBehaviour_BranchTransition.setter
    def branchedBehaviour_BranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_usagemodel_av_ScenarioBehaviour__branchedBehaviour_BranchTransition", None)
        self.__branchedBehaviour_BranchTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BranchTransition"):
                opp_val = getattr(old_value, "BranchTransition", None)
                if opp_val == self:
                    setattr(old_value, "BranchTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BranchTransition"):
                opp_val = getattr(value, "BranchTransition", None)
                setattr(value, "BranchTransition", self)

    @property
    def scenarioBehaviour_UsageScenario(self):
        return self.__scenarioBehaviour_UsageScenario

    @scenarioBehaviour_UsageScenario.setter
    def scenarioBehaviour_UsageScenario(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_usagemodel_av_ScenarioBehaviour__scenarioBehaviour_UsageScenario", None)
        self.__scenarioBehaviour_UsageScenario = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UsageScenario179"):
                opp_val = getattr(old_value, "UsageScenario179", None)
                if opp_val == self:
                    setattr(old_value, "UsageScenario179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UsageScenario179"):
                opp_val = getattr(value, "UsageScenario179", None)
                setattr(value, "UsageScenario179", self)

    def EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor method
        pass

    def Exactlyonestop(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement Exactlyonestop method
        pass

    def Exactlyonestart(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement Exactlyonestart method
        pass

class pcm_av_usagemodel_av_AbstractUserAction(Entity):

    pass
class Branch:

    pass
class pcm_av_usagemodel_av_BranchTransition:

    def __init__(self, branchProbability: float, branchTransitions_Branch: "Branch" = None, branchTransition_ScenarioBehaviour: "ScenarioBehaviour" = None):
        self.branchProbability = branchProbability
        self.branchTransitions_Branch = branchTransitions_Branch
        self.branchTransition_ScenarioBehaviour = branchTransition_ScenarioBehaviour
        
        pass
    @property
    def branchProbability(self):
        return self.__branchProbability

    @branchProbability.setter
    def branchProbability(self, branchProbability: float):
        self.__branchProbability = branchProbability


    @property
    def branchTransition_ScenarioBehaviour(self):
        return self.__branchTransition_ScenarioBehaviour

    @branchTransition_ScenarioBehaviour.setter
    def branchTransition_ScenarioBehaviour(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_usagemodel_av_BranchTransition__branchTransition_ScenarioBehaviour", None)
        self.__branchTransition_ScenarioBehaviour = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ScenarioBehaviour187"):
                opp_val = getattr(old_value, "ScenarioBehaviour187", None)
                if opp_val == self:
                    setattr(old_value, "ScenarioBehaviour187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ScenarioBehaviour187"):
                opp_val = getattr(value, "ScenarioBehaviour187", None)
                setattr(value, "ScenarioBehaviour187", self)

    @property
    def branchTransitions_Branch(self):
        return self.__branchTransitions_Branch

    @branchTransitions_Branch.setter
    def branchTransitions_Branch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_usagemodel_av_BranchTransition__branchTransitions_Branch", None)
        self.__branchTransitions_Branch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Branch"):
                opp_val = getattr(old_value, "Branch", None)
                if opp_val == self:
                    setattr(old_value, "Branch", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Branch"):
                opp_val = getattr(value, "Branch", None)
                setattr(value, "Branch", self)

class AbstractUserAction:

    pass
class pcm_av_usagemodel_av_Loop(AbstractUserAction):

    pass
class pcm_av_usagemodel_av_Branch(AbstractUserAction):

    def __init__(self, branch_BranchTransition: set["BranchTransition"] = None, AbstractUserAction175: "pcm_av_usagemodel_av_AbstractUserAction" = None, AbstractUserAction184: "pcm_av_usagemodel_av_ScenarioBehaviour" = None, AbstractUserAction: "pcm_av_usagemodel_av_AbstractUserAction" = None):
        self.branch_BranchTransition = branch_BranchTransition if branch_BranchTransition is not None else set()
        
        pass
    @property
    def branch_BranchTransition(self):
        return self.__branch_BranchTransition

    @branch_BranchTransition.setter
    def branch_BranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_usagemodel_av_Branch__branch_BranchTransition", None)
        self.__branch_BranchTransition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BranchTransition189"):
                    opp_val = getattr(item, "BranchTransition189", None)
                    
                    if opp_val == self:
                        setattr(item, "BranchTransition189", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BranchTransition189"):
                    opp_val = getattr(item, "BranchTransition189", None)
                    
                    setattr(item, "BranchTransition189", self)
                    

    def AllBranchProbabilitiesMustSumUpTo1(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement AllBranchProbabilitiesMustSumUpTo1 method
        pass

class pcm_av_usagemodel_av_Start(AbstractUserAction):

    def __init__(self, AbstractUserAction175: "pcm_av_usagemodel_av_AbstractUserAction" = None, AbstractUserAction184: "pcm_av_usagemodel_av_ScenarioBehaviour" = None, AbstractUserAction: "pcm_av_usagemodel_av_AbstractUserAction" = None):
        
        pass
    def StartHasNoPredecessor(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement StartHasNoPredecessor method
        pass

class pcm_av_usagemodel_av_Delay(AbstractUserAction):

    pass
class pcm_av_usagemodel_av_Stop(AbstractUserAction):

    def __init__(self, AbstractUserAction175: "pcm_av_usagemodel_av_AbstractUserAction" = None, AbstractUserAction184: "pcm_av_usagemodel_av_ScenarioBehaviour" = None, AbstractUserAction: "pcm_av_usagemodel_av_AbstractUserAction" = None):
        
        pass
    def StopHasNoSuccessor(self, pcm_av_diagnostics, pcm_av_context) :
        # TODO: Implement StopHasNoSuccessor method
        pass

class pcm_av_usagemodel_av_EntryLevelSystemCall(AbstractUserAction):

    def __init__(self, priority: int, pcm_av_usagemodel_av_EntryLevelSystemCall: "OperationProvidedRole" = None, pcm_av_usagemodel_av_EntryLevelSystemCall168: "OperationSignature" = None, entryLevelSystemCall_OutputParameterUsage: set["VariableUsage"] = None, entryLevelSystemCall_InputParameterUsage: set["VariableUsage"] = None, AbstractUserAction175: "pcm_av_usagemodel_av_AbstractUserAction" = None, AbstractUserAction184: "pcm_av_usagemodel_av_ScenarioBehaviour" = None, AbstractUserAction: "pcm_av_usagemodel_av_AbstractUserAction" = None):
        self.priority = priority
        self.pcm_av_usagemodel_av_EntryLevelSystemCall = pcm_av_usagemodel_av_EntryLevelSystemCall
        self.pcm_av_usagemodel_av_EntryLevelSystemCall168 = pcm_av_usagemodel_av_EntryLevelSystemCall168
        self.entryLevelSystemCall_OutputParameterUsage = entryLevelSystemCall_OutputParameterUsage if entryLevelSystemCall_OutputParameterUsage is not None else set()
        self.entryLevelSystemCall_InputParameterUsage = entryLevelSystemCall_InputParameterUsage if entryLevelSystemCall_InputParameterUsage is not None else set()
        
        pass
    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority


    @property
    def entryLevelSystemCall_OutputParameterUsage(self):
        return self.__entryLevelSystemCall_OutputParameterUsage

    @entryLevelSystemCall_OutputParameterUsage.setter
    def entryLevelSystemCall_OutputParameterUsage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_usagemodel_av_EntryLevelSystemCall__entryLevelSystemCall_OutputParameterUsage", None)
        self.__entryLevelSystemCall_OutputParameterUsage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableUsage170"):
                    opp_val = getattr(item, "VariableUsage170", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableUsage170", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableUsage170"):
                    opp_val = getattr(item, "VariableUsage170", None)
                    
                    setattr(item, "VariableUsage170", self)
                    

    @property
    def pcm_av_usagemodel_av_EntryLevelSystemCall168(self):
        return self.__pcm_av_usagemodel_av_EntryLevelSystemCall168

    @pcm_av_usagemodel_av_EntryLevelSystemCall168.setter
    def pcm_av_usagemodel_av_EntryLevelSystemCall168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_usagemodel_av_EntryLevelSystemCall__pcm_av_usagemodel_av_EntryLevelSystemCall168", None)
        self.__pcm_av_usagemodel_av_EntryLevelSystemCall168 = value
        
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
    def entryLevelSystemCall_InputParameterUsage(self):
        return self.__entryLevelSystemCall_InputParameterUsage

    @entryLevelSystemCall_InputParameterUsage.setter
    def entryLevelSystemCall_InputParameterUsage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_usagemodel_av_EntryLevelSystemCall__entryLevelSystemCall_InputParameterUsage", None)
        self.__entryLevelSystemCall_InputParameterUsage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableUsage172"):
                    opp_val = getattr(item, "VariableUsage172", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableUsage172", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableUsage172"):
                    opp_val = getattr(item, "VariableUsage172", None)
                    
                    setattr(item, "VariableUsage172", self)
                    

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
            if hasattr(old_value, "OperationProvidedRole166"):
                opp_val = getattr(old_value, "OperationProvidedRole166", None)
                if opp_val == self:
                    setattr(old_value, "OperationProvidedRole166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationProvidedRole166"):
                opp_val = getattr(value, "OperationProvidedRole166", None)
                setattr(value, "OperationProvidedRole166", self)

    def EntryLevelSystemCallSignatureMustMatchItsProvidedRole(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement EntryLevelSystemCallSignatureMustMatchItsProvidedRole method
        pass

    def EntryLevelSystemCallMustReferenceProvidedRoleOfASystem(self, pcm_av_context, pcm_av_diagnostics) :
        # TODO: Implement EntryLevelSystemCallMustReferenceProvidedRoleOfASystem method
        pass

class UserData:

    pass
class pcm_av_usagemodel_av_UsageModel:

    pass