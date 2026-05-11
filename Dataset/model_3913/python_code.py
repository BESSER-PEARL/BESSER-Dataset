from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ParameterModifier(Enum):
    in_ = "in_"
    out = "out"
    none = "none"
    inout = "inout"
class VariableCharacterisationType(Enum):
    NUMBER_OF_ELEMENTS = "NUMBER_OF_ELEMENTS"
    VALUE = "VALUE"
    BYTESIZE = "BYTESIZE"
    TYPE = "TYPE"
    STRUCTURE = "STRUCTURE"
class ComponentType(Enum):
    INFRASTRUCTURE_COMPONENT = "INFRASTRUCTURE_COMPONENT"
    BUSINESS_COMPONENT = "BUSINESS_COMPONENT"
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

class LinkingResource:

    pass
class pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction:

    pass
class SpecifiedQoSAnnotation:

    pass
class pcm_av_pc_qos_performance_av_pc_SpecifiedExecutionTime(SpecifiedQoSAnnotation):

    pass
class pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation(SpecifiedQoSAnnotation):

    def __init__(self, specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription: set["ExternalFailureOccurrenceDescription"] = None, SpecifiedQoSAnnotation: "pcm_av_pc_qosannotations_av_pc_QoSAnnotations" = None):
        self.specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription = specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription if specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription is not None else set()
        
        pass
    @property
    def specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription(self):
        return self.__specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription

    @specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription.setter
    def specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation__specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription", None)
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
                    

    def SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem method
        pass

    def MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed method
        pass

    def SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1 method
        pass

class System:

    pass
class QoSAnnotations:

    pass
class pcm_av_pc_qosannotations_av_pc_SpecifiedQoSAnnotation:

    pass
class SpecifiedExecutionTime:

    pass
class pcm_av_pc_qos_performance_av_pc_ComponentSpecifiedExecutionTime(SpecifiedExecutionTime):

    pass
class pcm_av_pc_qos_performance_av_pc_SystemSpecifiedExecutionTime(SpecifiedExecutionTime):

    def __init__(self):
        
        pass
    def SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem method
        pass

class seff_reliability_av_pc_RecoveryAction:

    pass
class seff_reliability_av_pc_RecoveryActionBehaviour:

    pass
class pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand:

    def __init__(self, parametricResourceDemand_PCMRandomVariable: "PCMRandomVariable" = None, pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand: "ProcessingResourceType" = None, resourceDemand_Action: "AbstractInternalControlFlowAction" = None):
        self.parametricResourceDemand_PCMRandomVariable = parametricResourceDemand_PCMRandomVariable
        self.pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand = pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand
        self.resourceDemand_Action = resourceDemand_Action
        
        pass
    @property
    def resourceDemand_Action(self):
        return self.__resourceDemand_Action

    @resourceDemand_Action.setter
    def resourceDemand_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand__resourceDemand_Action", None)
        self.__resourceDemand_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractInternalControlFlowAction422"):
                opp_val = getattr(old_value, "AbstractInternalControlFlowAction422", None)
                if opp_val == self:
                    setattr(old_value, "AbstractInternalControlFlowAction422", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractInternalControlFlowAction422"):
                opp_val = getattr(value, "AbstractInternalControlFlowAction422", None)
                setattr(value, "AbstractInternalControlFlowAction422", self)

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
            if hasattr(old_value, "ProcessingResourceType420"):
                opp_val = getattr(old_value, "ProcessingResourceType420", None)
                if opp_val == self:
                    setattr(old_value, "ProcessingResourceType420", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessingResourceType420"):
                opp_val = getattr(value, "ProcessingResourceType420", None)
                setattr(value, "ProcessingResourceType420", self)

    @property
    def parametricResourceDemand_PCMRandomVariable(self):
        return self.__parametricResourceDemand_PCMRandomVariable

    @parametricResourceDemand_PCMRandomVariable.setter
    def parametricResourceDemand_PCMRandomVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand__parametricResourceDemand_PCMRandomVariable", None)
        self.__parametricResourceDemand_PCMRandomVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable418"):
                opp_val = getattr(old_value, "PCMRandomVariable418", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable418", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable418"):
                opp_val = getattr(value, "PCMRandomVariable418", None)
                setattr(value, "PCMRandomVariable418", self)

    def DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

class seff_av_pc_AbstractInternalControlFlowAction:

    pass
class seff_av_pc_CallAction:

    pass
class pcm_av_pc_seff_av_pc_InternalCallAction(seff_av_pc_AbstractInternalControlFlowAction, seff_av_pc_CallAction):

    pass
class pcm_av_pc_seff_av_pc_SynchronisationPoint:

    pass
class ForkAction:

    pass
class ForkedBehaviour:

    pass
class ResourceDemandingSEFF:

    pass
class ResourceDemandingInternalBehaviour:

    pass
class seff_reliability_av_pc_FailureHandlingEntity:

    pass
class seff_av_pc_CallReturnAction:

    pass
class seff_av_pc_AbstractAction:

    pass
class pcm_av_pc_seff_av_pc_EmitEventAction(seff_av_pc_AbstractAction, seff_av_pc_CallAction):

    pass
class pcm_av_pc_seff_av_pc_ExternalCallAction(seff_av_pc_AbstractAction, seff_av_pc_CallReturnAction, seff_reliability_av_pc_FailureHandlingEntity):

    def __init__(self, retryCount: int, pcm_av_pc_seff_av_pc_ExternalCallAction: "OperationSignature" = None, pcm_av_pc_seff_av_pc_ExternalCallAction379: "OperationRequiredRole" = None):
        self.retryCount = retryCount
        self.pcm_av_pc_seff_av_pc_ExternalCallAction = pcm_av_pc_seff_av_pc_ExternalCallAction
        self.pcm_av_pc_seff_av_pc_ExternalCallAction379 = pcm_av_pc_seff_av_pc_ExternalCallAction379
        
        pass
    @property
    def retryCount(self):
        return self.__retryCount

    @retryCount.setter
    def retryCount(self, retryCount: int):
        self.__retryCount = retryCount


    @property
    def pcm_av_pc_seff_av_pc_ExternalCallAction379(self):
        return self.__pcm_av_pc_seff_av_pc_ExternalCallAction379

    @pcm_av_pc_seff_av_pc_ExternalCallAction379.setter
    def pcm_av_pc_seff_av_pc_ExternalCallAction379(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_av_pc_ExternalCallAction__pcm_av_pc_seff_av_pc_ExternalCallAction379", None)
        self.__pcm_av_pc_seff_av_pc_ExternalCallAction379 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationRequiredRole380"):
                opp_val = getattr(old_value, "OperationRequiredRole380", None)
                if opp_val == self:
                    setattr(old_value, "OperationRequiredRole380", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationRequiredRole380"):
                opp_val = getattr(value, "OperationRequiredRole380", None)
                setattr(value, "OperationRequiredRole380", self)

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
            if hasattr(old_value, "OperationSignature377"):
                opp_val = getattr(old_value, "OperationSignature377", None)
                if opp_val == self:
                    setattr(old_value, "OperationSignature377", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationSignature377"):
                opp_val = getattr(value, "OperationSignature377", None)
                setattr(value, "OperationSignature377", self)

    def SignatureBelongsToRole(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement SignatureBelongsToRole method
        pass

    def OperationRequiredRoleMustBeReferencedByContainer(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement OperationRequiredRoleMustBeReferencedByContainer method
        pass

class pcm_av_pc_seff_av_pc_ServiceEffectSpecification:

    def __init__(self, seffTypeID: str, pcm_av_pc_seff_av_pc_ServiceEffectSpecification: "Signature" = None, serviceEffectSpecifications__BasicComponent: "BasicComponent" = None):
        self.seffTypeID = seffTypeID
        self.pcm_av_pc_seff_av_pc_ServiceEffectSpecification = pcm_av_pc_seff_av_pc_ServiceEffectSpecification
        self.serviceEffectSpecifications__BasicComponent = serviceEffectSpecifications__BasicComponent
        
        pass
    @property
    def seffTypeID(self):
        return self.__seffTypeID

    @seffTypeID.setter
    def seffTypeID(self, seffTypeID: str):
        self.__seffTypeID = seffTypeID


    @property
    def serviceEffectSpecifications__BasicComponent(self):
        return self.__serviceEffectSpecifications__BasicComponent

    @serviceEffectSpecifications__BasicComponent.setter
    def serviceEffectSpecifications__BasicComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_av_pc_ServiceEffectSpecification__serviceEffectSpecifications__BasicComponent", None)
        self.__serviceEffectSpecifications__BasicComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicComponent357"):
                opp_val = getattr(old_value, "BasicComponent357", None)
                if opp_val == self:
                    setattr(old_value, "BasicComponent357", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicComponent357"):
                opp_val = getattr(value, "BasicComponent357", None)
                setattr(value, "BasicComponent357", self)

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

    def ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole method
        pass

class pcm_av_pc_seff_av_pc_CallAction:

    pass
class seff_av_pc_ResourceDemandingBehaviour:

    pass
class pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour(seff_av_pc_ResourceDemandingBehaviour, seff_reliability_av_pc_FailureHandlingEntity):

    def __init__(self, pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour: set["seff_reliability_av_pc_RecoveryActionBehaviour"] = None, recoveryActionBehaviours__RecoveryAction: "seff_reliability_av_pc_RecoveryAction" = None):
        self.pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour = pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour if pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour is not None else set()
        self.recoveryActionBehaviours__RecoveryAction = recoveryActionBehaviours__RecoveryAction
        
        pass
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
    def recoveryActionBehaviours__RecoveryAction(self):
        return self.__recoveryActionBehaviours__RecoveryAction

    @recoveryActionBehaviours__RecoveryAction.setter
    def recoveryActionBehaviours__RecoveryAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour__recoveryActionBehaviours__RecoveryAction", None)
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

    def SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes method
        pass

    def RecoveryActionBehaviourIsNotSuccessorOfItself(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement RecoveryActionBehaviourIsNotSuccessorOfItself method
        pass

    def RecoveryActionBehaviourHasOnlyOnePredecessor(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement RecoveryActionBehaviourHasOnlyOnePredecessor method
        pass

class seff_av_pc_ServiceEffectSpecification:

    pass
class AbstractBranchTransition:

    pass
class pcm_av_pc_seff_av_pc_GuardedBranchTransition(AbstractBranchTransition):

    pass
class pcm_av_pc_seff_av_pc_ProbabilisticBranchTransition(AbstractBranchTransition):

    def __init__(self, branchProbability: float, AbstractBranchTransition352: "pcm_av_pc_seff_av_pc_BranchAction" = None, AbstractBranchTransition: "pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour" = None):
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
class pcm_av_pc_seff_av_pc_CollectionIteratorAction(AbstractLoopAction):

    pass
class pcm_av_pc_seff_av_pc_LoopAction(AbstractLoopAction):

    pass
class ResourceDemandingBehaviour:

    pass
class pcm_av_pc_seff_av_pc_ForkedBehaviour(ResourceDemandingBehaviour):

    pass
class pcm_av_pc_seff_av_pc_ResourceDemandingInternalBehaviour(ResourceDemandingBehaviour):

    pass
class BranchAction:

    pass
class AbstractInternalControlFlowAction:

    pass
class pcm_av_pc_seff_av_pc_AbstractLoopAction(AbstractInternalControlFlowAction):

    pass
class pcm_av_pc_seff_av_pc_ForkAction(AbstractInternalControlFlowAction):

    pass
class pcm_av_pc_seff_av_pc_ReleaseAction(AbstractInternalControlFlowAction):

    pass
class pcm_av_pc_seff_av_pc_SetVariableAction(AbstractInternalControlFlowAction):

    pass
class pcm_av_pc_seff_av_pc_BranchAction(AbstractInternalControlFlowAction):

    def __init__(self, branchAction_AbstractBranchTransition: set["AbstractBranchTransition"] = None, AbstractInternalControlFlowAction409: "pcm_av_pc_seff_performance_av_pc_ResourceCall" = None, AbstractInternalControlFlowAction422: "pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand" = None, AbstractInternalControlFlowAction: "pcm_av_pc_seff_performance_av_pc_InfrastructureCall" = None):
        self.branchAction_AbstractBranchTransition = branchAction_AbstractBranchTransition if branchAction_AbstractBranchTransition is not None else set()
        
        pass
    @property
    def branchAction_AbstractBranchTransition(self):
        return self.__branchAction_AbstractBranchTransition

    @branchAction_AbstractBranchTransition.setter
    def branchAction_AbstractBranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_av_pc_BranchAction__branchAction_AbstractBranchTransition", None)
        self.__branchAction_AbstractBranchTransition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractBranchTransition352"):
                    opp_val = getattr(item, "AbstractBranchTransition352", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractBranchTransition352", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractBranchTransition352"):
                    opp_val = getattr(item, "AbstractBranchTransition352", None)
                    
                    setattr(item, "AbstractBranchTransition352", self)
                    

    def AllProbabilisticBranchProbabilitiesMustSumUpTo1(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement AllProbabilisticBranchProbabilitiesMustSumUpTo1 method
        pass

    def EitherGuardedBranchesOrProbabilisiticBranchTransitions(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement EitherGuardedBranchesOrProbabilisiticBranchTransitions method
        pass

class pcm_av_pc_seff_av_pc_InternalAction(AbstractInternalControlFlowAction):

    def __init__(self, internalAction__InternalFailureOccurrenceDescription: set["InternalFailureOccurrenceDescription"] = None, AbstractInternalControlFlowAction409: "pcm_av_pc_seff_performance_av_pc_ResourceCall" = None, AbstractInternalControlFlowAction422: "pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand" = None, AbstractInternalControlFlowAction: "pcm_av_pc_seff_performance_av_pc_InfrastructureCall" = None):
        self.internalAction__InternalFailureOccurrenceDescription = internalAction__InternalFailureOccurrenceDescription if internalAction__InternalFailureOccurrenceDescription is not None else set()
        
        pass
    @property
    def internalAction__InternalFailureOccurrenceDescription(self):
        return self.__internalAction__InternalFailureOccurrenceDescription

    @internalAction__InternalFailureOccurrenceDescription.setter
    def internalAction__InternalFailureOccurrenceDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_av_pc_InternalAction__internalAction__InternalFailureOccurrenceDescription", None)
        self.__internalAction__InternalFailureOccurrenceDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InternalFailureOccurrenceDescription399"):
                    opp_val = getattr(item, "InternalFailureOccurrenceDescription399", None)
                    
                    if opp_val == self:
                        setattr(item, "InternalFailureOccurrenceDescription399", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InternalFailureOccurrenceDescription399"):
                    opp_val = getattr(item, "InternalFailureOccurrenceDescription399", None)
                    
                    setattr(item, "InternalFailureOccurrenceDescription399", self)
                    

    def SumOfInternalActionFailureProbabilitiesMustNotExceed1(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement SumOfInternalActionFailureProbabilitiesMustNotExceed1 method
        pass

    def MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed method
        pass

class pcm_av_pc_seff_av_pc_AcquireAction(AbstractInternalControlFlowAction):

    def __init__(self, timeout: bool, timeoutValue: float, pcm_av_pc_seff_av_pc_AcquireAction: "PassiveResource" = None, AbstractInternalControlFlowAction409: "pcm_av_pc_seff_performance_av_pc_ResourceCall" = None, AbstractInternalControlFlowAction422: "pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand" = None, AbstractInternalControlFlowAction: "pcm_av_pc_seff_performance_av_pc_InfrastructureCall" = None):
        self.timeout = timeout
        self.timeoutValue = timeoutValue
        self.pcm_av_pc_seff_av_pc_AcquireAction = pcm_av_pc_seff_av_pc_AcquireAction
        
        pass
    @property
    def timeoutValue(self):
        return self.__timeoutValue

    @timeoutValue.setter
    def timeoutValue(self, timeoutValue: float):
        self.__timeoutValue = timeoutValue


    @property
    def timeout(self):
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
            if hasattr(old_value, "PassiveResource384"):
                opp_val = getattr(old_value, "PassiveResource384", None)
                if opp_val == self:
                    setattr(old_value, "PassiveResource384", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PassiveResource384"):
                opp_val = getattr(value, "PassiveResource384", None)
                setattr(value, "PassiveResource384", self)

    def TimeoutValueOfAcquireActionMustNotBeNegative(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement TimeoutValueOfAcquireActionMustNotBeNegative method
        pass

class pcm_av_pc_seff_av_pc_StartAction(AbstractInternalControlFlowAction):

    def __init__(self, AbstractInternalControlFlowAction409: "pcm_av_pc_seff_performance_av_pc_ResourceCall" = None, AbstractInternalControlFlowAction422: "pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand" = None, AbstractInternalControlFlowAction: "pcm_av_pc_seff_performance_av_pc_InfrastructureCall" = None):
        
        pass
    def StartActionPredecessorMustNotBeDefined(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement StartActionPredecessorMustNotBeDefined method
        pass

class pcm_av_pc_seff_reliability_av_pc_RecoveryAction(AbstractInternalControlFlowAction):

    def __init__(self, pcm_av_pc_seff_reliability_av_pc_RecoveryAction: "seff_reliability_av_pc_RecoveryActionBehaviour" = None, recoveryAction__RecoveryActionBehaviour: set["seff_reliability_av_pc_RecoveryActionBehaviour"] = None, AbstractInternalControlFlowAction409: "pcm_av_pc_seff_performance_av_pc_ResourceCall" = None, AbstractInternalControlFlowAction422: "pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand" = None, AbstractInternalControlFlowAction: "pcm_av_pc_seff_performance_av_pc_InfrastructureCall" = None):
        self.pcm_av_pc_seff_reliability_av_pc_RecoveryAction = pcm_av_pc_seff_reliability_av_pc_RecoveryAction
        self.recoveryAction__RecoveryActionBehaviour = recoveryAction__RecoveryActionBehaviour if recoveryAction__RecoveryActionBehaviour is not None else set()
        
        pass
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
            if hasattr(old_value, "seff_reliability_av_pc_RecoveryActionBehaviour426"):
                opp_val = getattr(old_value, "seff_reliability_av_pc_RecoveryActionBehaviour426", None)
                if opp_val == self:
                    setattr(old_value, "seff_reliability_av_pc_RecoveryActionBehaviour426", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_reliability_av_pc_RecoveryActionBehaviour426"):
                opp_val = getattr(value, "seff_reliability_av_pc_RecoveryActionBehaviour426", None)
                setattr(value, "seff_reliability_av_pc_RecoveryActionBehaviour426", self)

    @property
    def recoveryAction__RecoveryActionBehaviour(self):
        return self.__recoveryAction__RecoveryActionBehaviour

    @recoveryAction__RecoveryActionBehaviour.setter
    def recoveryAction__RecoveryActionBehaviour(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_reliability_av_pc_RecoveryAction__recoveryAction__RecoveryActionBehaviour", None)
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
                    

    def PrimaryBehaviourOfRecoveryActionMustBeSet(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement PrimaryBehaviourOfRecoveryActionMustBeSet method
        pass

class pcm_av_pc_seff_av_pc_StopAction(AbstractInternalControlFlowAction):

    def __init__(self, AbstractInternalControlFlowAction409: "pcm_av_pc_seff_performance_av_pc_ResourceCall" = None, AbstractInternalControlFlowAction422: "pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand" = None, AbstractInternalControlFlowAction: "pcm_av_pc_seff_performance_av_pc_InfrastructureCall" = None):
        
        pass
    def StopActionSuccessorMustNotBeDefined(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement StopActionSuccessorMustNotBeDefined method
        pass

class InfrastructureInterface:

    pass
class ExceptionType:

    pass
class repository_av_pc_RepositoryComponent:

    pass
class Signature:

    pass
class pcm_av_pc_repository_av_pc_InfrastructureSignature(Signature):

    pass
class pcm_av_pc_repository_av_pc_EventType(Signature):

    pass
class AllocationContext:

    pass
class ParametricResourceDemand:

    pass
class Parameter:

    pass
class pcm_av_pc_completions_av_pc_NetworkDemandParametricResourceDemand(ParametricResourceDemand):

    pass
class pcm_av_pc_repository_av_pc_RequiredCharacterisation:

    def __init__(self, type: str, pcm_av_pc_repository_av_pc_RequiredCharacterisation: "Parameter" = None, requiredCharacterisations: "Interface" = None):
        self.type = type
        self.pcm_av_pc_repository_av_pc_RequiredCharacterisation = pcm_av_pc_repository_av_pc_RequiredCharacterisation
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
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_RequiredCharacterisation__requiredCharacterisations", None)
        self.__requiredCharacterisations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Interface238"):
                opp_val = getattr(old_value, "Interface238", None)
                if opp_val == self:
                    setattr(old_value, "Interface238", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Interface238"):
                opp_val = getattr(value, "Interface238", None)
                setattr(value, "Interface238", self)

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

class ExternalCallAction:

    pass
class RequiredCharacterisation:

    pass
class pcm_av_pc_completions_av_pc_DelegatingExternalCallAction(ExternalCallAction):

    pass
class Protocol:

    pass
class Completion:

    pass
class pcm_av_pc_repository_av_pc_ExceptionType:

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


class pcm_av_pc_completions_av_pc_CompletionRepository:

    pass
class Interface:

    pass
class pcm_av_pc_repository_av_pc_EventGroup(Interface):

    pass
class pcm_av_pc_repository_av_pc_OperationInterface(Interface):

    def __init__(self, interface__OperationSignature: set["OperationSignature"] = None, Interface: "pcm_av_pc_repository_av_pc_Repository" = None, Interface230: "pcm_av_pc_repository_av_pc_Interface" = None, Interface238: "pcm_av_pc_repository_av_pc_RequiredCharacterisation" = None):
        self.interface__OperationSignature = interface__OperationSignature if interface__OperationSignature is not None else set()
        
        pass
    @property
    def interface__OperationSignature(self):
        return self.__interface__OperationSignature

    @interface__OperationSignature.setter
    def interface__OperationSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_OperationInterface__interface__OperationSignature", None)
        self.__interface__OperationSignature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OperationSignature263"):
                    opp_val = getattr(item, "OperationSignature263", None)
                    
                    if opp_val == self:
                        setattr(item, "OperationSignature263", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OperationSignature263"):
                    opp_val = getattr(item, "OperationSignature263", None)
                    
                    setattr(item, "OperationSignature263", self)
                    

    def SignaturesHaveToBeUniqueForAnInterface(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement SignaturesHaveToBeUniqueForAnInterface method
        pass

class pcm_av_pc_repository_av_pc_InfrastructureInterface(Interface):

    pass
class pcm_av_pc_repository_av_pc_DataType:

    pass
class Allocation:

    pass
class ResourceSignature:

    pass
class EventType:

    pass
class InfrastructureSignature:

    pass
class ResourceEnvironment:

    pass
class DataType:

    pass
class pcm_av_pc_repository_av_pc_Parameter:

    def __init__(self, parameterName: str, modifier__Parameter: str, pcm_av_pc_repository_av_pc_Parameter: "DataType" = None, parameters__InfrastructureSignature: "InfrastructureSignature" = None, parameters__OperationSignature: "OperationSignature" = None, parameter__EventType: "EventType" = None, parameter__ResourceSignature: "ResourceSignature" = None):
        self.parameterName = parameterName
        self.modifier__Parameter = modifier__Parameter
        self.pcm_av_pc_repository_av_pc_Parameter = pcm_av_pc_repository_av_pc_Parameter
        self.parameters__InfrastructureSignature = parameters__InfrastructureSignature
        self.parameters__OperationSignature = parameters__OperationSignature
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
    def parameter__ResourceSignature(self):
        return self.__parameter__ResourceSignature

    @parameter__ResourceSignature.setter
    def parameter__ResourceSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_Parameter__parameter__ResourceSignature", None)
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
    def parameters__InfrastructureSignature(self):
        return self.__parameters__InfrastructureSignature

    @parameters__InfrastructureSignature.setter
    def parameters__InfrastructureSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_Parameter__parameters__InfrastructureSignature", None)
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
    def parameter__EventType(self):
        return self.__parameter__EventType

    @parameter__EventType.setter
    def parameter__EventType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_Parameter__parameter__EventType", None)
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
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_Parameter__parameters__OperationSignature", None)
        self.__parameters__OperationSignature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationSignature218"):
                opp_val = getattr(old_value, "OperationSignature218", None)
                if opp_val == self:
                    setattr(old_value, "OperationSignature218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationSignature218"):
                opp_val = getattr(value, "OperationSignature218", None)
                setattr(value, "OperationSignature218", self)

class ExternalFailureOccurrenceDescription:

    pass
class FailureType:

    pass
class CompleteComponentType:

    pass
class ResourceContainer:

    pass
class Repository:

    pass
class InterfaceProvidingRequiringEntity:

    pass
class pcm_av_pc_repository_av_pc_RepositoryComponent(InterfaceProvidingRequiringEntity):

    pass
class ServiceEffectSpecification:

    pass
class ImplementationComponentType:

    pass
class pcm_av_pc_repository_av_pc_BasicComponent(ImplementationComponentType):

    def __init__(self, basicComponent_ServiceEffectSpecification: set["ServiceEffectSpecification"] = None, basicComponent_PassiveResource: set["PassiveResource"] = None):
        self.basicComponent_ServiceEffectSpecification = basicComponent_ServiceEffectSpecification if basicComponent_ServiceEffectSpecification is not None else set()
        self.basicComponent_PassiveResource = basicComponent_PassiveResource if basicComponent_PassiveResource is not None else set()
        
        pass
    @property
    def basicComponent_PassiveResource(self):
        return self.__basicComponent_PassiveResource

    @basicComponent_PassiveResource.setter
    def basicComponent_PassiveResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_BasicComponent__basicComponent_PassiveResource", None)
        self.__basicComponent_PassiveResource = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PassiveResource208"):
                    opp_val = getattr(item, "PassiveResource208", None)
                    
                    if opp_val == self:
                        setattr(item, "PassiveResource208", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PassiveResource208"):
                    opp_val = getattr(item, "PassiveResource208", None)
                    
                    setattr(item, "PassiveResource208", self)
                    

    @property
    def basicComponent_ServiceEffectSpecification(self):
        return self.__basicComponent_ServiceEffectSpecification

    @basicComponent_ServiceEffectSpecification.setter
    def basicComponent_ServiceEffectSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_BasicComponent__basicComponent_ServiceEffectSpecification", None)
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
                    

    def ProvideSameInterfacesAsImplementationType(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement ProvideSameInterfacesAsImplementationType method
        pass

    def NoSeffTypeUsedTwice(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement NoSeffTypeUsedTwice method
        pass

    def RequireSameInterfacesAsImplementationType(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement RequireSameInterfacesAsImplementationType method
        pass

class ResourceTimeoutFailureType:

    pass
class BasicComponent:

    pass
class Branch:

    pass
class pcm_av_pc_usagemodel_av_pc_BranchTransition:

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
    def branchTransitions_Branch(self):
        return self.__branchTransitions_Branch

    @branchTransitions_Branch.setter
    def branchTransitions_Branch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_BranchTransition__branchTransitions_Branch", None)
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

    @property
    def branchTransition_ScenarioBehaviour(self):
        return self.__branchTransition_ScenarioBehaviour

    @branchTransition_ScenarioBehaviour.setter
    def branchTransition_ScenarioBehaviour(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_BranchTransition__branchTransition_ScenarioBehaviour", None)
        self.__branchTransition_ScenarioBehaviour = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ScenarioBehaviour189"):
                opp_val = getattr(old_value, "ScenarioBehaviour189", None)
                if opp_val == self:
                    setattr(old_value, "ScenarioBehaviour189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ScenarioBehaviour189"):
                opp_val = getattr(value, "ScenarioBehaviour189", None)
                setattr(value, "ScenarioBehaviour189", self)

class BranchTransition:

    pass
class OperationSignature:

    pass
class pcm_av_pc_usagemodel_av_pc_UserData:

    pass
class Workload:

    pass
class pcm_av_pc_usagemodel_av_pc_ClosedWorkload(Workload):

    def __init__(self, population: int, closedWorkload_PCMRandomVariable: "PCMRandomVariable" = None, Workload: "pcm_av_pc_usagemodel_av_pc_UsageScenario" = None):
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
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_ClosedWorkload__closedWorkload_PCMRandomVariable", None)
        self.__closedWorkload_PCMRandomVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable201"):
                opp_val = getattr(old_value, "PCMRandomVariable201", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable201"):
                opp_val = getattr(value, "PCMRandomVariable201", None)
                setattr(value, "PCMRandomVariable201", self)

    def PopulationInClosedWorkloadNeedsToBeSpecified(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement PopulationInClosedWorkloadNeedsToBeSpecified method
        pass

    def ThinkTimeInClosedWorkloadNeedsToBeSpecified(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement ThinkTimeInClosedWorkloadNeedsToBeSpecified method
        pass

class pcm_av_pc_usagemodel_av_pc_OpenWorkload(Workload):

    def __init__(self, openWorkload_PCMRandomVariable: "PCMRandomVariable" = None, Workload: "pcm_av_pc_usagemodel_av_pc_UsageScenario" = None):
        self.openWorkload_PCMRandomVariable = openWorkload_PCMRandomVariable
        
        pass
    @property
    def openWorkload_PCMRandomVariable(self):
        return self.__openWorkload_PCMRandomVariable

    @openWorkload_PCMRandomVariable.setter
    def openWorkload_PCMRandomVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_OpenWorkload__openWorkload_PCMRandomVariable", None)
        self.__openWorkload_PCMRandomVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable197"):
                opp_val = getattr(old_value, "PCMRandomVariable197", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable197"):
                opp_val = getattr(value, "PCMRandomVariable197", None)
                setattr(value, "PCMRandomVariable197", self)

    def InterArrivalTimeInOpenWorkloadNeedsToBeSpecified(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement InterArrivalTimeInOpenWorkloadNeedsToBeSpecified method
        pass

class ScenarioBehaviour:

    pass
class UsageModel:

    pass
class UsageScenario:

    pass
class pcm_av_pc_usagemodel_av_pc_Workload:

    pass
class VariableUsage:

    pass
class RepositoryComponent:

    pass
class pcm_av_pc_repository_av_pc_ImplementationComponentType(RepositoryComponent):

    def __init__(self, componentType: str, pcm_av_pc_repository_av_pc_ImplementationComponentType: set["CompleteComponentType"] = None, pcm_av_pc_repository_av_pc_ImplementationComponentType211: set["VariableUsage"] = None, RepositoryComponent: "pcm_av_pc_composition_av_pc_AssemblyContext" = None, RepositoryComponent224: "pcm_av_pc_repository_av_pc_Repository" = None):
        self.componentType = componentType
        self.pcm_av_pc_repository_av_pc_ImplementationComponentType = pcm_av_pc_repository_av_pc_ImplementationComponentType if pcm_av_pc_repository_av_pc_ImplementationComponentType is not None else set()
        self.pcm_av_pc_repository_av_pc_ImplementationComponentType211 = pcm_av_pc_repository_av_pc_ImplementationComponentType211 if pcm_av_pc_repository_av_pc_ImplementationComponentType211 is not None else set()
        
        pass
    @property
    def componentType(self):
        return self.__componentType

    @componentType.setter
    def componentType(self, componentType: str):
        self.__componentType = componentType


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
                    

    @property
    def pcm_av_pc_repository_av_pc_ImplementationComponentType211(self):
        return self.__pcm_av_pc_repository_av_pc_ImplementationComponentType211

    @pcm_av_pc_repository_av_pc_ImplementationComponentType211.setter
    def pcm_av_pc_repository_av_pc_ImplementationComponentType211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_ImplementationComponentType__pcm_av_pc_repository_av_pc_ImplementationComponentType211", None)
        self.__pcm_av_pc_repository_av_pc_ImplementationComponentType211 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableUsage212"):
                    opp_val = getattr(item, "VariableUsage212", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableUsage212", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableUsage212"):
                    opp_val = getattr(item, "VariableUsage212", None)
                    
                    setattr(item, "VariableUsage212", self)
                    

    def RequiredInterfacesHaveToConformToCompleteType(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement RequiredInterfacesHaveToConformToCompleteType method
        pass

    def providedInterfacesHaveToConformToCompleteType(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement providedInterfacesHaveToConformToCompleteType method
        pass

    def ProvidedInterfaceHaveToConformToComponentType(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement ProvidedInterfaceHaveToConformToComponentType method
        pass

class AbstractUserAction:

    pass
class pcm_av_pc_usagemodel_av_pc_Stop(AbstractUserAction):

    def __init__(self, AbstractUserAction177: "pcm_av_pc_usagemodel_av_pc_AbstractUserAction" = None, AbstractUserAction: "pcm_av_pc_usagemodel_av_pc_AbstractUserAction" = None, AbstractUserAction186: "pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour" = None):
        
        pass
    def StopHasNoSuccessor(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement StopHasNoSuccessor method
        pass

class pcm_av_pc_usagemodel_av_pc_Loop(AbstractUserAction):

    pass
class pcm_av_pc_usagemodel_av_pc_Delay(AbstractUserAction):

    pass
class pcm_av_pc_usagemodel_av_pc_Start(AbstractUserAction):

    def __init__(self, AbstractUserAction177: "pcm_av_pc_usagemodel_av_pc_AbstractUserAction" = None, AbstractUserAction: "pcm_av_pc_usagemodel_av_pc_AbstractUserAction" = None, AbstractUserAction186: "pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour" = None):
        
        pass
    def StartHasNoPredecessor(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement StartHasNoPredecessor method
        pass

class pcm_av_pc_usagemodel_av_pc_Branch(AbstractUserAction):

    def __init__(self, branch_BranchTransition: set["BranchTransition"] = None, AbstractUserAction177: "pcm_av_pc_usagemodel_av_pc_AbstractUserAction" = None, AbstractUserAction: "pcm_av_pc_usagemodel_av_pc_AbstractUserAction" = None, AbstractUserAction186: "pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour" = None):
        self.branch_BranchTransition = branch_BranchTransition if branch_BranchTransition is not None else set()
        
        pass
    @property
    def branch_BranchTransition(self):
        return self.__branch_BranchTransition

    @branch_BranchTransition.setter
    def branch_BranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_Branch__branch_BranchTransition", None)
        self.__branch_BranchTransition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BranchTransition191"):
                    opp_val = getattr(item, "BranchTransition191", None)
                    
                    if opp_val == self:
                        setattr(item, "BranchTransition191", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BranchTransition191"):
                    opp_val = getattr(item, "BranchTransition191", None)
                    
                    setattr(item, "BranchTransition191", self)
                    

    def AllBranchProbabilitiesMustSumUpTo1(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement AllBranchProbabilitiesMustSumUpTo1 method
        pass

class pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall(AbstractUserAction):

    def __init__(self, priority: int, pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall: "OperationProvidedRole" = None, pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall170: "OperationSignature" = None, entryLevelSystemCall_OutputParameterUsage: set["VariableUsage"] = None, entryLevelSystemCall_InputParameterUsage: set["VariableUsage"] = None, AbstractUserAction177: "pcm_av_pc_usagemodel_av_pc_AbstractUserAction" = None, AbstractUserAction: "pcm_av_pc_usagemodel_av_pc_AbstractUserAction" = None, AbstractUserAction186: "pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour" = None):
        self.priority = priority
        self.pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall = pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall
        self.pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall170 = pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall170
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
    def pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall(self):
        return self.__pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall

    @pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall.setter
    def pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall__pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall", None)
        self.__pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationProvidedRole168"):
                opp_val = getattr(old_value, "OperationProvidedRole168", None)
                if opp_val == self:
                    setattr(old_value, "OperationProvidedRole168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationProvidedRole168"):
                opp_val = getattr(value, "OperationProvidedRole168", None)
                setattr(value, "OperationProvidedRole168", self)

    @property
    def entryLevelSystemCall_InputParameterUsage(self):
        return self.__entryLevelSystemCall_InputParameterUsage

    @entryLevelSystemCall_InputParameterUsage.setter
    def entryLevelSystemCall_InputParameterUsage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall__entryLevelSystemCall_InputParameterUsage", None)
        self.__entryLevelSystemCall_InputParameterUsage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableUsage174"):
                    opp_val = getattr(item, "VariableUsage174", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableUsage174", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableUsage174"):
                    opp_val = getattr(item, "VariableUsage174", None)
                    
                    setattr(item, "VariableUsage174", self)
                    

    @property
    def pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall170(self):
        return self.__pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall170

    @pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall170.setter
    def pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall__pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall170", None)
        self.__pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall170 = value
        
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
    def entryLevelSystemCall_OutputParameterUsage(self):
        return self.__entryLevelSystemCall_OutputParameterUsage

    @entryLevelSystemCall_OutputParameterUsage.setter
    def entryLevelSystemCall_OutputParameterUsage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall__entryLevelSystemCall_OutputParameterUsage", None)
        self.__entryLevelSystemCall_OutputParameterUsage = value if value is not None else set()
        
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
                    

    def EntryLevelSystemCallMustReferenceProvidedRoleOfASystem(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement EntryLevelSystemCallMustReferenceProvidedRoleOfASystem method
        pass

    def EntryLevelSystemCallSignatureMustMatchItsProvidedRole(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement EntryLevelSystemCallSignatureMustMatchItsProvidedRole method
        pass

class UserData:

    pass
class pcm_av_pc_usagemodel_av_pc_UsageModel:

    pass
class InfrastructureRequiredRole:

    pass
class InfrastructureProvidedRole:

    pass
class OperationRequiredRole:

    pass
class OperationProvidedRole:

    pass
class DelegationConnector:

    pass
class pcm_av_pc_composition_av_pc_SourceDelegationConnector(DelegationConnector):

    pass
class pcm_av_pc_composition_av_pc_SinkDelegationConnector(DelegationConnector):

    pass
class pcm_av_pc_composition_av_pc_RequiredDelegationConnector(DelegationConnector):

    def __init__(self, pcm_av_pc_composition_av_pc_RequiredDelegationConnector: "OperationRequiredRole" = None, pcm_av_pc_composition_av_pc_RequiredDelegationConnector72: "OperationRequiredRole" = None, pcm_av_pc_composition_av_pc_RequiredDelegationConnector75: "composition_av_pc_AssemblyContext" = None):
        self.pcm_av_pc_composition_av_pc_RequiredDelegationConnector = pcm_av_pc_composition_av_pc_RequiredDelegationConnector
        self.pcm_av_pc_composition_av_pc_RequiredDelegationConnector72 = pcm_av_pc_composition_av_pc_RequiredDelegationConnector72
        self.pcm_av_pc_composition_av_pc_RequiredDelegationConnector75 = pcm_av_pc_composition_av_pc_RequiredDelegationConnector75
        
        pass
    @property
    def pcm_av_pc_composition_av_pc_RequiredDelegationConnector75(self):
        return self.__pcm_av_pc_composition_av_pc_RequiredDelegationConnector75

    @pcm_av_pc_composition_av_pc_RequiredDelegationConnector75.setter
    def pcm_av_pc_composition_av_pc_RequiredDelegationConnector75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_composition_av_pc_RequiredDelegationConnector__pcm_av_pc_composition_av_pc_RequiredDelegationConnector75", None)
        self.__pcm_av_pc_composition_av_pc_RequiredDelegationConnector75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_pc_AssemblyContext76"):
                opp_val = getattr(old_value, "composition_av_pc_AssemblyContext76", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_pc_AssemblyContext76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_pc_AssemblyContext76"):
                opp_val = getattr(value, "composition_av_pc_AssemblyContext76", None)
                setattr(value, "composition_av_pc_AssemblyContext76", self)

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

    @property
    def pcm_av_pc_composition_av_pc_RequiredDelegationConnector72(self):
        return self.__pcm_av_pc_composition_av_pc_RequiredDelegationConnector72

    @pcm_av_pc_composition_av_pc_RequiredDelegationConnector72.setter
    def pcm_av_pc_composition_av_pc_RequiredDelegationConnector72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_composition_av_pc_RequiredDelegationConnector__pcm_av_pc_composition_av_pc_RequiredDelegationConnector72", None)
        self.__pcm_av_pc_composition_av_pc_RequiredDelegationConnector72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationRequiredRole73"):
                opp_val = getattr(old_value, "OperationRequiredRole73", None)
                if opp_val == self:
                    setattr(old_value, "OperationRequiredRole73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationRequiredRole73"):
                opp_val = getattr(value, "OperationRequiredRole73", None)
                setattr(value, "OperationRequiredRole73", self)

    def RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector method
        pass

    def RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

    def ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame method
        pass

class pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector(DelegationConnector):

    pass
class pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector(DelegationConnector):

    pass
class pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector(DelegationConnector):

    pass
class pcm_av_pc_composition_av_pc_ProvidedDelegationConnector(DelegationConnector):

    def __init__(self, pcm_av_pc_composition_av_pc_ProvidedDelegationConnector: "OperationProvidedRole" = None, pcm_av_pc_composition_av_pc_ProvidedDelegationConnector65: "OperationProvidedRole" = None, pcm_av_pc_composition_av_pc_ProvidedDelegationConnector68: "composition_av_pc_AssemblyContext" = None):
        self.pcm_av_pc_composition_av_pc_ProvidedDelegationConnector = pcm_av_pc_composition_av_pc_ProvidedDelegationConnector
        self.pcm_av_pc_composition_av_pc_ProvidedDelegationConnector65 = pcm_av_pc_composition_av_pc_ProvidedDelegationConnector65
        self.pcm_av_pc_composition_av_pc_ProvidedDelegationConnector68 = pcm_av_pc_composition_av_pc_ProvidedDelegationConnector68
        
        pass
    @property
    def pcm_av_pc_composition_av_pc_ProvidedDelegationConnector65(self):
        return self.__pcm_av_pc_composition_av_pc_ProvidedDelegationConnector65

    @pcm_av_pc_composition_av_pc_ProvidedDelegationConnector65.setter
    def pcm_av_pc_composition_av_pc_ProvidedDelegationConnector65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_composition_av_pc_ProvidedDelegationConnector__pcm_av_pc_composition_av_pc_ProvidedDelegationConnector65", None)
        self.__pcm_av_pc_composition_av_pc_ProvidedDelegationConnector65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationProvidedRole66"):
                opp_val = getattr(old_value, "OperationProvidedRole66", None)
                if opp_val == self:
                    setattr(old_value, "OperationProvidedRole66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationProvidedRole66"):
                opp_val = getattr(value, "OperationProvidedRole66", None)
                setattr(value, "OperationProvidedRole66", self)

    @property
    def pcm_av_pc_composition_av_pc_ProvidedDelegationConnector68(self):
        return self.__pcm_av_pc_composition_av_pc_ProvidedDelegationConnector68

    @pcm_av_pc_composition_av_pc_ProvidedDelegationConnector68.setter
    def pcm_av_pc_composition_av_pc_ProvidedDelegationConnector68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_composition_av_pc_ProvidedDelegationConnector__pcm_av_pc_composition_av_pc_ProvidedDelegationConnector68", None)
        self.__pcm_av_pc_composition_av_pc_ProvidedDelegationConnector68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_pc_AssemblyContext69"):
                opp_val = getattr(old_value, "composition_av_pc_AssemblyContext69", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_pc_AssemblyContext69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_pc_AssemblyContext69"):
                opp_val = getattr(value, "composition_av_pc_AssemblyContext69", None)
                setattr(value, "composition_av_pc_AssemblyContext69", self)

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

    def ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

    def ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame method
        pass

class PCMRandomVariable:

    pass
class SinkRole:

    pass
class SourceRole:

    pass
class pcm_av_pc_composition_av_pc_ResourceRequiredDelegationConnector:

    pass
class composition_av_pc_Connector:

    pass
class composition_av_pc_EventChannel:

    pass
class composition_av_pc_ResourceRequiredDelegationConnector:

    pass
class composition_av_pc_AssemblyContext:

    pass
class composition_av_pc_EventChannelSourceConnector:

    pass
class EventGroup:

    pass
class entity_av_pc_InterfaceProvidingRequiringEntity:

    pass
class composition_av_pc_ComposedStructure:

    pass
class pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity(composition_av_pc_ComposedStructure, entity_av_pc_InterfaceProvidingRequiringEntity):

    def __init__(self, ComposedStructure: "pcm_av_pc_composition_av_pc_Connector" = None, ComposedStructure151: "pcm_av_pc_composition_av_pc_AssemblyContext" = None, ComposedStructure50: "pcm_av_pc_composition_av_pc_EventChannel" = None, ComposedStructure44: "pcm_av_pc_composition_av_pc_ResourceRequiredDelegationConnector" = None):
        
        pass
    def ProvidedRolesMustBeBound(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement ProvidedRolesMustBeBound method
        pass

class entity_av_pc_ResourceProvidedRole:

    pass
class entity_av_pc_ResourceRequiredRole:

    pass
class RequiredRole:

    pass
class entity_av_pc_ResourceInterfaceRequiringEntity:

    pass
class entity_av_pc_Entity:

    pass
class pcm_av_pc_entity_av_pc_InterfaceRequiringEntity(entity_av_pc_Entity, entity_av_pc_ResourceInterfaceRequiringEntity):

    pass
class ProvidedRole:

    pass
class Entity:

    pass
class pcm_av_pc_allocation_av_pc_Allocation(Entity):

    def __init__(self, pcm_av_pc_allocation_av_pc_Allocation: "ResourceEnvironment" = None, pcm_av_pc_allocation_av_pc_Allocation498: "System" = None, allocation_AllocationContext: set["AllocationContext"] = None):
        self.pcm_av_pc_allocation_av_pc_Allocation = pcm_av_pc_allocation_av_pc_Allocation
        self.pcm_av_pc_allocation_av_pc_Allocation498 = pcm_av_pc_allocation_av_pc_Allocation498
        self.allocation_AllocationContext = allocation_AllocationContext if allocation_AllocationContext is not None else set()
        
        pass
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
            if hasattr(old_value, "ResourceEnvironment496"):
                opp_val = getattr(old_value, "ResourceEnvironment496", None)
                if opp_val == self:
                    setattr(old_value, "ResourceEnvironment496", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceEnvironment496"):
                opp_val = getattr(value, "ResourceEnvironment496", None)
                setattr(value, "ResourceEnvironment496", self)

    @property
    def pcm_av_pc_allocation_av_pc_Allocation498(self):
        return self.__pcm_av_pc_allocation_av_pc_Allocation498

    @pcm_av_pc_allocation_av_pc_Allocation498.setter
    def pcm_av_pc_allocation_av_pc_Allocation498(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_allocation_av_pc_Allocation__pcm_av_pc_allocation_av_pc_Allocation498", None)
        self.__pcm_av_pc_allocation_av_pc_Allocation498 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "System499"):
                opp_val = getattr(old_value, "System499", None)
                if opp_val == self:
                    setattr(old_value, "System499", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "System499"):
                opp_val = getattr(value, "System499", None)
                setattr(value, "System499", self)

    @property
    def allocation_AllocationContext(self):
        return self.__allocation_AllocationContext

    @allocation_AllocationContext.setter
    def allocation_AllocationContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_allocation_av_pc_Allocation__allocation_AllocationContext", None)
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
                    

    def EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce method
        pass

    def CommunicatingServersHaveToBeConnectedByLinkingResource(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement CommunicatingServersHaveToBeConnectedByLinkingResource method
        pass

class pcm_av_pc_allocation_av_pc_AllocationContext(Entity):

    def __init__(self, pcm_av_pc_allocation_av_pc_AllocationContext490: "composition_av_pc_AssemblyContext" = None, allocationContexts_Allocation: "Allocation" = None, pcm_av_pc_allocation_av_pc_AllocationContext494: "composition_av_pc_EventChannel" = None, pcm_av_pc_allocation_av_pc_AllocationContext: "ResourceContainer" = None):
        self.pcm_av_pc_allocation_av_pc_AllocationContext490 = pcm_av_pc_allocation_av_pc_AllocationContext490
        self.allocationContexts_Allocation = allocationContexts_Allocation
        self.pcm_av_pc_allocation_av_pc_AllocationContext494 = pcm_av_pc_allocation_av_pc_AllocationContext494
        self.pcm_av_pc_allocation_av_pc_AllocationContext = pcm_av_pc_allocation_av_pc_AllocationContext
        
        pass
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
            if hasattr(old_value, "ResourceContainer488"):
                opp_val = getattr(old_value, "ResourceContainer488", None)
                if opp_val == self:
                    setattr(old_value, "ResourceContainer488", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceContainer488"):
                opp_val = getattr(value, "ResourceContainer488", None)
                setattr(value, "ResourceContainer488", self)

    @property
    def pcm_av_pc_allocation_av_pc_AllocationContext490(self):
        return self.__pcm_av_pc_allocation_av_pc_AllocationContext490

    @pcm_av_pc_allocation_av_pc_AllocationContext490.setter
    def pcm_av_pc_allocation_av_pc_AllocationContext490(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_allocation_av_pc_AllocationContext__pcm_av_pc_allocation_av_pc_AllocationContext490", None)
        self.__pcm_av_pc_allocation_av_pc_AllocationContext490 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_pc_AssemblyContext491"):
                opp_val = getattr(old_value, "composition_av_pc_AssemblyContext491", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_pc_AssemblyContext491", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_pc_AssemblyContext491"):
                opp_val = getattr(value, "composition_av_pc_AssemblyContext491", None)
                setattr(value, "composition_av_pc_AssemblyContext491", self)

    @property
    def pcm_av_pc_allocation_av_pc_AllocationContext494(self):
        return self.__pcm_av_pc_allocation_av_pc_AllocationContext494

    @pcm_av_pc_allocation_av_pc_AllocationContext494.setter
    def pcm_av_pc_allocation_av_pc_AllocationContext494(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_allocation_av_pc_AllocationContext__pcm_av_pc_allocation_av_pc_AllocationContext494", None)
        self.__pcm_av_pc_allocation_av_pc_AllocationContext494 = value
        
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
    def allocationContexts_Allocation(self):
        return self.__allocationContexts_Allocation

    @allocationContexts_Allocation.setter
    def allocationContexts_Allocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_allocation_av_pc_AllocationContext__allocationContexts_Allocation", None)
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

    def OneAssemblyContextOrOneEventChannelShouldBeReferred(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement OneAssemblyContextOrOneEventChannelShouldBeReferred method
        pass

class pcm_av_pc_resourceenvironment_av_pc_ResourceContainer(Entity):

    pass
class pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingEntity(Entity):

    pass
class pcm_av_pc_resourceenvironment_av_pc_LinkingResource(Entity):

    pass
class pcm_av_pc_composition_av_pc_Connector(Entity):

    pass
class pcm_av_pc_repository_av_pc_Signature(Entity):

    pass
class pcm_av_pc_repository_av_pc_PassiveResource(Entity):

    pass
class pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour(Entity):

    def __init__(self, scenarioBehaviour_UsageScenario: "UsageScenario" = None, branchedBehaviour_BranchTransition: "BranchTransition" = None, bodyBehaviour_Loop: "Loop" = None, scenarioBehaviour_AbstractUserAction: set["AbstractUserAction"] = None):
        self.scenarioBehaviour_UsageScenario = scenarioBehaviour_UsageScenario
        self.branchedBehaviour_BranchTransition = branchedBehaviour_BranchTransition
        self.bodyBehaviour_Loop = bodyBehaviour_Loop
        self.scenarioBehaviour_AbstractUserAction = scenarioBehaviour_AbstractUserAction if scenarioBehaviour_AbstractUserAction is not None else set()
        
        pass
    @property
    def scenarioBehaviour_UsageScenario(self):
        return self.__scenarioBehaviour_UsageScenario

    @scenarioBehaviour_UsageScenario.setter
    def scenarioBehaviour_UsageScenario(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour__scenarioBehaviour_UsageScenario", None)
        self.__scenarioBehaviour_UsageScenario = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UsageScenario181"):
                opp_val = getattr(old_value, "UsageScenario181", None)
                if opp_val == self:
                    setattr(old_value, "UsageScenario181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UsageScenario181"):
                opp_val = getattr(value, "UsageScenario181", None)
                setattr(value, "UsageScenario181", self)

    @property
    def bodyBehaviour_Loop(self):
        return self.__bodyBehaviour_Loop

    @bodyBehaviour_Loop.setter
    def bodyBehaviour_Loop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour__bodyBehaviour_Loop", None)
        self.__bodyBehaviour_Loop = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Loop184"):
                opp_val = getattr(old_value, "Loop184", None)
                if opp_val == self:
                    setattr(old_value, "Loop184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Loop184"):
                opp_val = getattr(value, "Loop184", None)
                setattr(value, "Loop184", self)

    @property
    def scenarioBehaviour_AbstractUserAction(self):
        return self.__scenarioBehaviour_AbstractUserAction

    @scenarioBehaviour_AbstractUserAction.setter
    def scenarioBehaviour_AbstractUserAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour__scenarioBehaviour_AbstractUserAction", None)
        self.__scenarioBehaviour_AbstractUserAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractUserAction186"):
                    opp_val = getattr(item, "AbstractUserAction186", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractUserAction186", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractUserAction186"):
                    opp_val = getattr(item, "AbstractUserAction186", None)
                    
                    setattr(item, "AbstractUserAction186", self)
                    

    @property
    def branchedBehaviour_BranchTransition(self):
        return self.__branchedBehaviour_BranchTransition

    @branchedBehaviour_BranchTransition.setter
    def branchedBehaviour_BranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour__branchedBehaviour_BranchTransition", None)
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

    def Exactlyonestart(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement Exactlyonestart method
        pass

    def Exactlyonestop(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement Exactlyonestop method
        pass

    def EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor method
        pass

class pcm_av_pc_composition_av_pc_EventChannel(Entity):

    pass
class pcm_av_pc_qosannotations_av_pc_QoSAnnotations(Entity):

    def __init__(self, qosAnnotations_SpecifiedOutputParameterAbstraction: set["SpecifiedOutputParameterAbstraction"] = None, qosAnnotations_System: "System" = None, qosAnnotations_SpecifiedQoSAnnotation: set["SpecifiedQoSAnnotation"] = None):
        self.qosAnnotations_SpecifiedOutputParameterAbstraction = qosAnnotations_SpecifiedOutputParameterAbstraction if qosAnnotations_SpecifiedOutputParameterAbstraction is not None else set()
        self.qosAnnotations_System = qosAnnotations_System
        self.qosAnnotations_SpecifiedQoSAnnotation = qosAnnotations_SpecifiedQoSAnnotation if qosAnnotations_SpecifiedQoSAnnotation is not None else set()
        
        pass
    @property
    def qosAnnotations_SpecifiedOutputParameterAbstraction(self):
        return self.__qosAnnotations_SpecifiedOutputParameterAbstraction

    @qosAnnotations_SpecifiedOutputParameterAbstraction.setter
    def qosAnnotations_SpecifiedOutputParameterAbstraction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_qosannotations_av_pc_QoSAnnotations__qosAnnotations_SpecifiedOutputParameterAbstraction", None)
        self.__qosAnnotations_SpecifiedOutputParameterAbstraction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SpecifiedOutputParameterAbstraction436"):
                    opp_val = getattr(item, "SpecifiedOutputParameterAbstraction436", None)
                    
                    if opp_val == self:
                        setattr(item, "SpecifiedOutputParameterAbstraction436", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SpecifiedOutputParameterAbstraction436"):
                    opp_val = getattr(item, "SpecifiedOutputParameterAbstraction436", None)
                    
                    setattr(item, "SpecifiedOutputParameterAbstraction436", self)
                    

    @property
    def qosAnnotations_SpecifiedQoSAnnotation(self):
        return self.__qosAnnotations_SpecifiedQoSAnnotation

    @qosAnnotations_SpecifiedQoSAnnotation.setter
    def qosAnnotations_SpecifiedQoSAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_qosannotations_av_pc_QoSAnnotations__qosAnnotations_SpecifiedQoSAnnotation", None)
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
                    

    @property
    def qosAnnotations_System(self):
        return self.__qosAnnotations_System

    @qosAnnotations_System.setter
    def qosAnnotations_System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_qosannotations_av_pc_QoSAnnotations__qosAnnotations_System", None)
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

    def MultipleReliabilityAnnotationsPerExternalCallNotAllowed(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement MultipleReliabilityAnnotationsPerExternalCallNotAllowed method
        pass

class pcm_av_pc_repository_av_pc_Interface(Entity):

    def __init__(self, pcm_av_pc_repository_av_pc_Interface: set["Interface"] = None, pcm_av_pc_repository_av_pc_Interface232: set["Protocol"] = None, interface_RequiredCharacterisation: set["RequiredCharacterisation"] = None, interfaces__Repository: "Repository" = None):
        self.pcm_av_pc_repository_av_pc_Interface = pcm_av_pc_repository_av_pc_Interface if pcm_av_pc_repository_av_pc_Interface is not None else set()
        self.pcm_av_pc_repository_av_pc_Interface232 = pcm_av_pc_repository_av_pc_Interface232 if pcm_av_pc_repository_av_pc_Interface232 is not None else set()
        self.interface_RequiredCharacterisation = interface_RequiredCharacterisation if interface_RequiredCharacterisation is not None else set()
        self.interfaces__Repository = interfaces__Repository
        
        pass
    @property
    def pcm_av_pc_repository_av_pc_Interface232(self):
        return self.__pcm_av_pc_repository_av_pc_Interface232

    @pcm_av_pc_repository_av_pc_Interface232.setter
    def pcm_av_pc_repository_av_pc_Interface232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_Interface__pcm_av_pc_repository_av_pc_Interface232", None)
        self.__pcm_av_pc_repository_av_pc_Interface232 = value if value is not None else set()
        
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
    def interfaces__Repository(self):
        return self.__interfaces__Repository

    @interfaces__Repository.setter
    def interfaces__Repository(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_Interface__interfaces__Repository", None)
        self.__interfaces__Repository = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Repository235"):
                opp_val = getattr(old_value, "Repository235", None)
                if opp_val == self:
                    setattr(old_value, "Repository235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Repository235"):
                opp_val = getattr(value, "Repository235", None)
                setattr(value, "Repository235", self)

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
                if hasattr(item, "Interface230"):
                    opp_val = getattr(item, "Interface230", None)
                    
                    if opp_val == self:
                        setattr(item, "Interface230", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Interface230"):
                    opp_val = getattr(item, "Interface230", None)
                    
                    setattr(item, "Interface230", self)
                    

    @property
    def interface_RequiredCharacterisation(self):
        return self.__interface_RequiredCharacterisation

    @interface_RequiredCharacterisation.setter
    def interface_RequiredCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_Interface__interface_RequiredCharacterisation", None)
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
                    

    def NoProtocolTypeIDUsedTwice(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement NoProtocolTypeIDUsedTwice method
        pass

class pcm_av_pc_reliability_av_pc_FailureType(Entity):

    pass
class pcm_av_pc_composition_av_pc_AssemblyContext(Entity):

    pass
class pcm_av_pc_repository_av_pc_Repository(Entity):

    def __init__(self, repositoryDescription: str, repository__FailureType: set["FailureType"] = None, repository__DataType: set["DataType"] = None, repository__RepositoryComponent: set["RepositoryComponent"] = None, repository__Interface: set["Interface"] = None):
        self.repositoryDescription = repositoryDescription
        self.repository__FailureType = repository__FailureType if repository__FailureType is not None else set()
        self.repository__DataType = repository__DataType if repository__DataType is not None else set()
        self.repository__RepositoryComponent = repository__RepositoryComponent if repository__RepositoryComponent is not None else set()
        self.repository__Interface = repository__Interface if repository__Interface is not None else set()
        
        pass
    @property
    def repositoryDescription(self):
        return self.__repositoryDescription

    @repositoryDescription.setter
    def repositoryDescription(self, repositoryDescription: str):
        self.__repositoryDescription = repositoryDescription


    @property
    def repository__Interface(self):
        return self.__repository__Interface

    @repository__Interface.setter
    def repository__Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_Repository__repository__Interface", None)
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
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_Repository__repository__DataType", None)
        self.__repository__DataType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataType228"):
                    opp_val = getattr(item, "DataType228", None)
                    
                    if opp_val == self:
                        setattr(item, "DataType228", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataType228"):
                    opp_val = getattr(item, "DataType228", None)
                    
                    setattr(item, "DataType228", self)
                    

    @property
    def repository__FailureType(self):
        return self.__repository__FailureType

    @repository__FailureType.setter
    def repository__FailureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_Repository__repository__FailureType", None)
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
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_Repository__repository__RepositoryComponent", None)
        self.__repository__RepositoryComponent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RepositoryComponent224"):
                    opp_val = getattr(item, "RepositoryComponent224", None)
                    
                    if opp_val == self:
                        setattr(item, "RepositoryComponent224", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RepositoryComponent224"):
                    opp_val = getattr(item, "RepositoryComponent224", None)
                    
                    setattr(item, "RepositoryComponent224", self)
                    

class pcm_av_pc_usagemodel_av_pc_UsageScenario(Entity):

    pass
class pcm_av_pc_seff_reliability_av_pc_FailureHandlingEntity(Entity):

    pass
class pcm_av_pc_seff_av_pc_AbstractBranchTransition(Entity):

    pass
class pcm_av_pc_usagemodel_av_pc_AbstractUserAction(Entity):

    pass
class pcm_av_pc_composition_av_pc_ComposedStructure(Entity):

    def __init__(self, parentStructure__AssemblyContext: set["composition_av_pc_AssemblyContext"] = None, parentStructure_ResourceRequiredDelegationConnector: set["composition_av_pc_ResourceRequiredDelegationConnector"] = None, parentStructure__EventChannel: set["composition_av_pc_EventChannel"] = None, parentStructure__Connector: set["composition_av_pc_Connector"] = None):
        self.parentStructure__AssemblyContext = parentStructure__AssemblyContext if parentStructure__AssemblyContext is not None else set()
        self.parentStructure_ResourceRequiredDelegationConnector = parentStructure_ResourceRequiredDelegationConnector if parentStructure_ResourceRequiredDelegationConnector is not None else set()
        self.parentStructure__EventChannel = parentStructure__EventChannel if parentStructure__EventChannel is not None else set()
        self.parentStructure__Connector = parentStructure__Connector if parentStructure__Connector is not None else set()
        
        pass
    @property
    def parentStructure__AssemblyContext(self):
        return self.__parentStructure__AssemblyContext

    @parentStructure__AssemblyContext.setter
    def parentStructure__AssemblyContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_composition_av_pc_ComposedStructure__parentStructure__AssemblyContext", None)
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
                    

    @property
    def parentStructure__Connector(self):
        return self.__parentStructure__Connector

    @parentStructure__Connector.setter
    def parentStructure__Connector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_composition_av_pc_ComposedStructure__parentStructure__Connector", None)
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
        old_value = getattr(self, f"_pcm_av_pc_composition_av_pc_ComposedStructure__parentStructure_ResourceRequiredDelegationConnector", None)
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
    def parentStructure__EventChannel(self):
        return self.__parentStructure__EventChannel

    @parentStructure__EventChannel.setter
    def parentStructure__EventChannel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_composition_av_pc_ComposedStructure__parentStructure__EventChannel", None)
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
                    

    def MultipleConnectorsConstraint(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement MultipleConnectorsConstraint method
        pass

    def MultipleConnectorsConstraintForAssemblyConnectors(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement MultipleConnectorsConstraintForAssemblyConnectors method
        pass

class pcm_av_pc_entity_av_pc_ResourceInterfaceRequiringEntity(Entity):

    pass
class pcm_av_pc_entity_av_pc_InterfaceProvidingEntity(Entity):

    pass
class entity_av_pc_InterfaceRequiringEntity:

    pass
class entity_av_pc_InterfaceProvidingEntity:

    pass
class pcm_av_pc_entity_av_pc_InterfaceProvidingRequiringEntity(entity_av_pc_InterfaceRequiringEntity, entity_av_pc_InterfaceProvidingEntity):

    pass
class ResourceInterface:

    pass
class Connector:

    pass
class pcm_av_pc_composition_av_pc_AssemblyConnector(Connector):

    def __init__(self, pcm_av_pc_composition_av_pc_AssemblyConnector: "composition_av_pc_AssemblyContext" = None, pcm_av_pc_composition_av_pc_AssemblyConnector80: "composition_av_pc_AssemblyContext" = None, pcm_av_pc_composition_av_pc_AssemblyConnector83: "OperationProvidedRole" = None, pcm_av_pc_composition_av_pc_AssemblyConnector86: "OperationRequiredRole" = None):
        self.pcm_av_pc_composition_av_pc_AssemblyConnector = pcm_av_pc_composition_av_pc_AssemblyConnector
        self.pcm_av_pc_composition_av_pc_AssemblyConnector80 = pcm_av_pc_composition_av_pc_AssemblyConnector80
        self.pcm_av_pc_composition_av_pc_AssemblyConnector83 = pcm_av_pc_composition_av_pc_AssemblyConnector83
        self.pcm_av_pc_composition_av_pc_AssemblyConnector86 = pcm_av_pc_composition_av_pc_AssemblyConnector86
        
        pass
    @property
    def pcm_av_pc_composition_av_pc_AssemblyConnector83(self):
        return self.__pcm_av_pc_composition_av_pc_AssemblyConnector83

    @pcm_av_pc_composition_av_pc_AssemblyConnector83.setter
    def pcm_av_pc_composition_av_pc_AssemblyConnector83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_composition_av_pc_AssemblyConnector__pcm_av_pc_composition_av_pc_AssemblyConnector83", None)
        self.__pcm_av_pc_composition_av_pc_AssemblyConnector83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationProvidedRole84"):
                opp_val = getattr(old_value, "OperationProvidedRole84", None)
                if opp_val == self:
                    setattr(old_value, "OperationProvidedRole84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationProvidedRole84"):
                opp_val = getattr(value, "OperationProvidedRole84", None)
                setattr(value, "OperationProvidedRole84", self)

    @property
    def pcm_av_pc_composition_av_pc_AssemblyConnector80(self):
        return self.__pcm_av_pc_composition_av_pc_AssemblyConnector80

    @pcm_av_pc_composition_av_pc_AssemblyConnector80.setter
    def pcm_av_pc_composition_av_pc_AssemblyConnector80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_composition_av_pc_AssemblyConnector__pcm_av_pc_composition_av_pc_AssemblyConnector80", None)
        self.__pcm_av_pc_composition_av_pc_AssemblyConnector80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_av_pc_AssemblyContext81"):
                opp_val = getattr(old_value, "composition_av_pc_AssemblyContext81", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_pc_AssemblyContext81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_pc_AssemblyContext81"):
                opp_val = getattr(value, "composition_av_pc_AssemblyContext81", None)
                setattr(value, "composition_av_pc_AssemblyContext81", self)

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
            if hasattr(old_value, "composition_av_pc_AssemblyContext78"):
                opp_val = getattr(old_value, "composition_av_pc_AssemblyContext78", None)
                if opp_val == self:
                    setattr(old_value, "composition_av_pc_AssemblyContext78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_av_pc_AssemblyContext78"):
                opp_val = getattr(value, "composition_av_pc_AssemblyContext78", None)
                setattr(value, "composition_av_pc_AssemblyContext78", self)

    @property
    def pcm_av_pc_composition_av_pc_AssemblyConnector86(self):
        return self.__pcm_av_pc_composition_av_pc_AssemblyConnector86

    @pcm_av_pc_composition_av_pc_AssemblyConnector86.setter
    def pcm_av_pc_composition_av_pc_AssemblyConnector86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_composition_av_pc_AssemblyConnector__pcm_av_pc_composition_av_pc_AssemblyConnector86", None)
        self.__pcm_av_pc_composition_av_pc_AssemblyConnector86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationRequiredRole87"):
                opp_val = getattr(old_value, "OperationRequiredRole87", None)
                if opp_val == self:
                    setattr(old_value, "OperationRequiredRole87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationRequiredRole87"):
                opp_val = getattr(value, "OperationRequiredRole87", None)
                setattr(value, "OperationRequiredRole87", self)

    def AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch method
        pass

    def AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch method
        pass

    def AssemblyConnectorsReferencedInterfacesMustMatch(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement AssemblyConnectorsReferencedInterfacesMustMatch method
        pass

class pcm_av_pc_composition_av_pc_AssemblyEventConnector(Connector):

    pass
class pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector(Connector):

    pass
class pcm_av_pc_composition_av_pc_EventChannelSourceConnector(Connector):

    pass
class pcm_av_pc_composition_av_pc_EventChannelSinkConnector(Connector):

    pass
class pcm_av_pc_composition_av_pc_DelegationConnector(Connector):

    pass
class entity_av_pc_NamedElement:

    pass
class Identifier:

    pass
class pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification(Identifier):

    def __init__(self, failureProbability: float, communicationLinkResourceSpecifications_LinkingResource: "LinkingResource" = None, pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification: "CommunicationLinkResourceType" = None, communicationLinkResourceSpecification_latency_PCMRandomVariable: "PCMRandomVariable" = None, communicationLinkResourceSpecifcation_throughput_PCMRandomVariable: "PCMRandomVariable" = None):
        self.failureProbability = failureProbability
        self.communicationLinkResourceSpecifications_LinkingResource = communicationLinkResourceSpecifications_LinkingResource
        self.pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification = pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification
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
    def pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification(self):
        return self.__pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification

    @pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification.setter
    def pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification__pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification", None)
        self.__pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CommunicationLinkResourceType482"):
                opp_val = getattr(old_value, "CommunicationLinkResourceType482", None)
                if opp_val == self:
                    setattr(old_value, "CommunicationLinkResourceType482", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CommunicationLinkResourceType482"):
                opp_val = getattr(value, "CommunicationLinkResourceType482", None)
                setattr(value, "CommunicationLinkResourceType482", self)

    @property
    def communicationLinkResourceSpecifcation_throughput_PCMRandomVariable(self):
        return self.__communicationLinkResourceSpecifcation_throughput_PCMRandomVariable

    @communicationLinkResourceSpecifcation_throughput_PCMRandomVariable.setter
    def communicationLinkResourceSpecifcation_throughput_PCMRandomVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification__communicationLinkResourceSpecifcation_throughput_PCMRandomVariable", None)
        self.__communicationLinkResourceSpecifcation_throughput_PCMRandomVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable486"):
                opp_val = getattr(old_value, "PCMRandomVariable486", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable486", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable486"):
                opp_val = getattr(value, "PCMRandomVariable486", None)
                setattr(value, "PCMRandomVariable486", self)

    @property
    def communicationLinkResourceSpecification_latency_PCMRandomVariable(self):
        return self.__communicationLinkResourceSpecification_latency_PCMRandomVariable

    @communicationLinkResourceSpecification_latency_PCMRandomVariable.setter
    def communicationLinkResourceSpecification_latency_PCMRandomVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification__communicationLinkResourceSpecification_latency_PCMRandomVariable", None)
        self.__communicationLinkResourceSpecification_latency_PCMRandomVariable = value
        
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
    def communicationLinkResourceSpecifications_LinkingResource(self):
        return self.__communicationLinkResourceSpecifications_LinkingResource

    @communicationLinkResourceSpecifications_LinkingResource.setter
    def communicationLinkResourceSpecifications_LinkingResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification__communicationLinkResourceSpecifications_LinkingResource", None)
        self.__communicationLinkResourceSpecifications_LinkingResource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LinkingResource480"):
                opp_val = getattr(old_value, "LinkingResource480", None)
                if opp_val == self:
                    setattr(old_value, "LinkingResource480", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LinkingResource480"):
                opp_val = getattr(value, "LinkingResource480", None)
                setattr(value, "LinkingResource480", self)

class pcm_av_pc_seff_av_pc_ResourceDemandingSEFF(seff_av_pc_ResourceDemandingBehaviour, Identifier, seff_av_pc_ServiceEffectSpecification):

    pass
class pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour(Identifier):

    def __init__(self, resourceDemandingBehaviour_AbstractAction: set["AbstractAction"] = None, bodyBehaviour_Loop342: "AbstractLoopAction" = None, branchBehaviour_BranchTransition: "AbstractBranchTransition" = None):
        self.resourceDemandingBehaviour_AbstractAction = resourceDemandingBehaviour_AbstractAction if resourceDemandingBehaviour_AbstractAction is not None else set()
        self.bodyBehaviour_Loop342 = bodyBehaviour_Loop342
        self.branchBehaviour_BranchTransition = branchBehaviour_BranchTransition
        
        pass
    @property
    def branchBehaviour_BranchTransition(self):
        return self.__branchBehaviour_BranchTransition

    @branchBehaviour_BranchTransition.setter
    def branchBehaviour_BranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour__branchBehaviour_BranchTransition", None)
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
        old_value = getattr(self, f"_pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour__resourceDemandingBehaviour_AbstractAction", None)
        self.__resourceDemandingBehaviour_AbstractAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractAction345"):
                    opp_val = getattr(item, "AbstractAction345", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractAction345", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractAction345"):
                    opp_val = getattr(item, "AbstractAction345", None)
                    
                    setattr(item, "AbstractAction345", self)
                    

    @property
    def bodyBehaviour_Loop342(self):
        return self.__bodyBehaviour_Loop342

    @bodyBehaviour_Loop342.setter
    def bodyBehaviour_Loop342(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour__bodyBehaviour_Loop342", None)
        self.__bodyBehaviour_Loop342 = value
        
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

    def ExactlyOneStartAction(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement ExactlyOneStartAction method
        pass

    def ExactlyOneStopAction(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement ExactlyOneStopAction method
        pass

    def EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor method
        pass

class pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification(Identifier):

    def __init__(self, numberOfReplicas: int, MTTR: float, MTTF: float, requiredByContainer: bool, pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification473: "ProcessingResourceType" = None, processingResourceSpecification_processingRate_PCMRandomVariable: "PCMRandomVariable" = None, activeResourceSpecifications_ResourceContainer: "ResourceContainer" = None, pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification: "SchedulingPolicy" = None):
        self.numberOfReplicas = numberOfReplicas
        self.MTTR = MTTR
        self.MTTF = MTTF
        self.requiredByContainer = requiredByContainer
        self.pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification473 = pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification473
        self.processingResourceSpecification_processingRate_PCMRandomVariable = processingResourceSpecification_processingRate_PCMRandomVariable
        self.activeResourceSpecifications_ResourceContainer = activeResourceSpecifications_ResourceContainer
        self.pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification = pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification
        
        pass
    @property
    def requiredByContainer(self):
        return self.__requiredByContainer

    @requiredByContainer.setter
    def requiredByContainer(self, requiredByContainer: bool):
        self.__requiredByContainer = requiredByContainer


    @property
    def MTTF(self):
        return self.__MTTF

    @MTTF.setter
    def MTTF(self, MTTF: float):
        self.__MTTF = MTTF


    @property
    def MTTR(self):
        return self.__MTTR

    @MTTR.setter
    def MTTR(self, MTTR: float):
        self.__MTTR = MTTR


    @property
    def numberOfReplicas(self):
        return self.__numberOfReplicas

    @numberOfReplicas.setter
    def numberOfReplicas(self, numberOfReplicas: int):
        self.__numberOfReplicas = numberOfReplicas


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
            if hasattr(old_value, "SchedulingPolicy471"):
                opp_val = getattr(old_value, "SchedulingPolicy471", None)
                if opp_val == self:
                    setattr(old_value, "SchedulingPolicy471", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SchedulingPolicy471"):
                opp_val = getattr(value, "SchedulingPolicy471", None)
                setattr(value, "SchedulingPolicy471", self)

    @property
    def pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification473(self):
        return self.__pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification473

    @pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification473.setter
    def pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification473(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification__pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification473", None)
        self.__pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification473 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcessingResourceType474"):
                opp_val = getattr(old_value, "ProcessingResourceType474", None)
                if opp_val == self:
                    setattr(old_value, "ProcessingResourceType474", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessingResourceType474"):
                opp_val = getattr(value, "ProcessingResourceType474", None)
                setattr(value, "ProcessingResourceType474", self)

    @property
    def processingResourceSpecification_processingRate_PCMRandomVariable(self):
        return self.__processingResourceSpecification_processingRate_PCMRandomVariable

    @processingResourceSpecification_processingRate_PCMRandomVariable.setter
    def processingResourceSpecification_processingRate_PCMRandomVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification__processingResourceSpecification_processingRate_PCMRandomVariable", None)
        self.__processingResourceSpecification_processingRate_PCMRandomVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable476"):
                opp_val = getattr(old_value, "PCMRandomVariable476", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable476", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable476"):
                opp_val = getattr(value, "PCMRandomVariable476", None)
                setattr(value, "PCMRandomVariable476", self)

    @property
    def activeResourceSpecifications_ResourceContainer(self):
        return self.__activeResourceSpecifications_ResourceContainer

    @activeResourceSpecifications_ResourceContainer.setter
    def activeResourceSpecifications_ResourceContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification__activeResourceSpecifications_ResourceContainer", None)
        self.__activeResourceSpecifications_ResourceContainer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceContainer478"):
                opp_val = getattr(old_value, "ResourceContainer478", None)
                if opp_val == self:
                    setattr(old_value, "ResourceContainer478", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceContainer478"):
                opp_val = getattr(value, "ResourceContainer478", None)
                setattr(value, "ResourceContainer478", self)

class pcm_av_pc_entity_av_pc_Entity(entity_av_pc_NamedElement, Identifier):

    pass
class pcm_av_pc_entity_av_pc_NamedElement:

    def __init__(self, entityName: str):
        self.entityName = entityName
        
        pass
    @property
    def entityName(self):
        return self.__entityName

    @entityName.setter
    def entityName(self, entityName: str):
        self.__entityName = entityName


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
class qos_performance_av_pc_SpecifiedExecutionTime:

    pass
class GuardedBranchTransition:

    pass
class LoopAction:

    pass
class seff_performance_av_pc_ParametricResourceDemand:

    pass
class seff_performance_av_pc_ResourceCall:

    pass
class seff_performance_av_pc_InfrastructureCall:

    pass
class VariableCharacterisation:

    pass
class PassiveResource:

    pass
class ClosedWorkload:

    pass
class entity_av_pc_ResourceInterfaceProvidingEntity:

    pass
class pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingRequiringEntity(entity_av_pc_ResourceInterfaceRequiringEntity, entity_av_pc_ResourceInterfaceProvidingEntity):

    pass
class Role:

    pass
class pcm_av_pc_entity_av_pc_ResourceRequiredRole(Role):

    pass
class pcm_av_pc_repository_av_pc_ProvidedRole(Role):

    pass
class pcm_av_pc_entity_av_pc_ResourceProvidedRole(Role):

    pass
class ProcessingResourceSpecification:

    pass
class CommunicationLinkResourceSpecification:

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
class RandomVariable:

    pass
class pcm_av_pc_core_av_pc_PCMRandomVariable(RandomVariable):

    def __init__(self, throughput_CommunicationLinkResourceSpecification: "CommunicationLinkResourceSpecification" = None, processingRate_ProcessingResourceSpecification: "ProcessingResourceSpecification" = None, latency_CommunicationLinkResourceSpecification: "CommunicationLinkResourceSpecification" = None, thinkTime_ClosedWorkload: "ClosedWorkload" = None, capacity_PassiveResource: "PassiveResource" = None, specification_VariableCharacterisation: "VariableCharacterisation" = None, numberOfCalls__InfrastructureCall: "seff_performance_av_pc_InfrastructureCall" = None, numberOfCalls__ResourceCall: "seff_performance_av_pc_ResourceCall" = None, specification_ParametericResourceDemand: "seff_performance_av_pc_ParametricResourceDemand" = None, iterationCount_LoopAction: "LoopAction" = None, branchCondition_GuardedBranchTransition: "GuardedBranchTransition" = None, specification_SpecifiedExecutionTime: "qos_performance_av_pc_SpecifiedExecutionTime" = None, filterCondition__EventChannelSinkConnector: "composition_av_pc_EventChannelSinkConnector" = None, filterCondition__AssemblyEventConnector: "composition_av_pc_AssemblyEventConnector" = None, loopIteration_Loop: "Loop" = None, interArrivalTime_OpenWorkload: "OpenWorkload" = None, timeSpecification_Delay: "Delay" = None):
        self.throughput_CommunicationLinkResourceSpecification = throughput_CommunicationLinkResourceSpecification
        self.processingRate_ProcessingResourceSpecification = processingRate_ProcessingResourceSpecification
        self.latency_CommunicationLinkResourceSpecification = latency_CommunicationLinkResourceSpecification
        self.thinkTime_ClosedWorkload = thinkTime_ClosedWorkload
        self.capacity_PassiveResource = capacity_PassiveResource
        self.specification_VariableCharacterisation = specification_VariableCharacterisation
        self.numberOfCalls__InfrastructureCall = numberOfCalls__InfrastructureCall
        self.numberOfCalls__ResourceCall = numberOfCalls__ResourceCall
        self.specification_ParametericResourceDemand = specification_ParametericResourceDemand
        self.iterationCount_LoopAction = iterationCount_LoopAction
        self.branchCondition_GuardedBranchTransition = branchCondition_GuardedBranchTransition
        self.specification_SpecifiedExecutionTime = specification_SpecifiedExecutionTime
        self.filterCondition__EventChannelSinkConnector = filterCondition__EventChannelSinkConnector
        self.filterCondition__AssemblyEventConnector = filterCondition__AssemblyEventConnector
        self.loopIteration_Loop = loopIteration_Loop
        self.interArrivalTime_OpenWorkload = interArrivalTime_OpenWorkload
        self.timeSpecification_Delay = timeSpecification_Delay
        
        pass
    @property
    def branchCondition_GuardedBranchTransition(self):
        return self.__branchCondition_GuardedBranchTransition

    @branchCondition_GuardedBranchTransition.setter
    def branchCondition_GuardedBranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__branchCondition_GuardedBranchTransition", None)
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
    def filterCondition__EventChannelSinkConnector(self):
        return self.__filterCondition__EventChannelSinkConnector

    @filterCondition__EventChannelSinkConnector.setter
    def filterCondition__EventChannelSinkConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__filterCondition__EventChannelSinkConnector", None)
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
    def processingRate_ProcessingResourceSpecification(self):
        return self.__processingRate_ProcessingResourceSpecification

    @processingRate_ProcessingResourceSpecification.setter
    def processingRate_ProcessingResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__processingRate_ProcessingResourceSpecification", None)
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
    def thinkTime_ClosedWorkload(self):
        return self.__thinkTime_ClosedWorkload

    @thinkTime_ClosedWorkload.setter
    def thinkTime_ClosedWorkload(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__thinkTime_ClosedWorkload", None)
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
    def specification_ParametericResourceDemand(self):
        return self.__specification_ParametericResourceDemand

    @specification_ParametericResourceDemand.setter
    def specification_ParametericResourceDemand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__specification_ParametericResourceDemand", None)
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
    def iterationCount_LoopAction(self):
        return self.__iterationCount_LoopAction

    @iterationCount_LoopAction.setter
    def iterationCount_LoopAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__iterationCount_LoopAction", None)
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
    def loopIteration_Loop(self):
        return self.__loopIteration_Loop

    @loopIteration_Loop.setter
    def loopIteration_Loop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__loopIteration_Loop", None)
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
    def specification_SpecifiedExecutionTime(self):
        return self.__specification_SpecifiedExecutionTime

    @specification_SpecifiedExecutionTime.setter
    def specification_SpecifiedExecutionTime(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__specification_SpecifiedExecutionTime", None)
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
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__throughput_CommunicationLinkResourceSpecification", None)
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
    def numberOfCalls__ResourceCall(self):
        return self.__numberOfCalls__ResourceCall

    @numberOfCalls__ResourceCall.setter
    def numberOfCalls__ResourceCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__numberOfCalls__ResourceCall", None)
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
    def timeSpecification_Delay(self):
        return self.__timeSpecification_Delay

    @timeSpecification_Delay.setter
    def timeSpecification_Delay(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__timeSpecification_Delay", None)
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
    def specification_VariableCharacterisation(self):
        return self.__specification_VariableCharacterisation

    @specification_VariableCharacterisation.setter
    def specification_VariableCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__specification_VariableCharacterisation", None)
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
    def interArrivalTime_OpenWorkload(self):
        return self.__interArrivalTime_OpenWorkload

    @interArrivalTime_OpenWorkload.setter
    def interArrivalTime_OpenWorkload(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__interArrivalTime_OpenWorkload", None)
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
    def capacity_PassiveResource(self):
        return self.__capacity_PassiveResource

    @capacity_PassiveResource.setter
    def capacity_PassiveResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__capacity_PassiveResource", None)
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
    def latency_CommunicationLinkResourceSpecification(self):
        return self.__latency_CommunicationLinkResourceSpecification

    @latency_CommunicationLinkResourceSpecification.setter
    def latency_CommunicationLinkResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__latency_CommunicationLinkResourceSpecification", None)
        self.__latency_CommunicationLinkResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CommunicationLinkResourceSpecification24"):
                opp_val = getattr(old_value, "CommunicationLinkResourceSpecification24", None)
                if opp_val == self:
                    setattr(old_value, "CommunicationLinkResourceSpecification24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CommunicationLinkResourceSpecification24"):
                opp_val = getattr(value, "CommunicationLinkResourceSpecification24", None)
                setattr(value, "CommunicationLinkResourceSpecification24", self)

    @property
    def filterCondition__AssemblyEventConnector(self):
        return self.__filterCondition__AssemblyEventConnector

    @filterCondition__AssemblyEventConnector.setter
    def filterCondition__AssemblyEventConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__filterCondition__AssemblyEventConnector", None)
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

    @property
    def numberOfCalls__InfrastructureCall(self):
        return self.__numberOfCalls__InfrastructureCall

    @numberOfCalls__InfrastructureCall.setter
    def numberOfCalls__InfrastructureCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_core_av_pc_PCMRandomVariable__numberOfCalls__InfrastructureCall", None)
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

    def SpecificationMustNotBeNULL(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement SpecificationMustNotBeNULL method
        pass

class pcm_av_pc_Pointcut:

    pass
class qos_reliability_av_pc_SpecifiedReliabilityAnnotation:

    pass
class pcm_av_pc_seff_av_pc_AbstractAction(Entity):

    pass
class AbstractAction:

    pass
class pcm_av_pc_seff_av_pc_AbstractInternalControlFlowAction(AbstractAction):

    pass
class pcm_av_pc_reliability_av_pc_NetworkInducedFailureType(FailureType):

    def __init__(self, networkInducedFailureType__CommunicationLinkResourceType: "CommunicationLinkResourceType" = None, FailureType: "pcm_av_pc_repository_av_pc_Repository" = None, FailureType326: "pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription" = None, FailureType248: "pcm_av_pc_repository_av_pc_Signature" = None, FailureType429: "pcm_av_pc_seff_reliability_av_pc_FailureHandlingEntity" = None):
        self.networkInducedFailureType__CommunicationLinkResourceType = networkInducedFailureType__CommunicationLinkResourceType
        
        pass
    @property
    def networkInducedFailureType__CommunicationLinkResourceType(self):
        return self.__networkInducedFailureType__CommunicationLinkResourceType

    @networkInducedFailureType__CommunicationLinkResourceType.setter
    def networkInducedFailureType__CommunicationLinkResourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_reliability_av_pc_NetworkInducedFailureType__networkInducedFailureType__CommunicationLinkResourceType", None)
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

    def NetworkInducedFailureTypeHasCommunicationLinkResourceType(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement NetworkInducedFailureTypeHasCommunicationLinkResourceType method
        pass

class SoftwareInducedFailureType:

    pass
class pcm_av_pc_reliability_av_pc_ResourceTimeoutFailureType(SoftwareInducedFailureType):

    pass
class InternalAction:

    pass
class FailureOccurrenceDescription:

    pass
class pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription(FailureOccurrenceDescription):

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
        old_value = getattr(self, f"_pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription__internalFailureOccurrenceDescriptions__SoftwareInducedFailureType", None)
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
        old_value = getattr(self, f"_pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription__internalFailureOccurrenceDescriptions__InternalAction", None)
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

    def NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription method
        pass

class InternalFailureOccurrenceDescription:

    pass
class pcm_av_pc_reliability_av_pc_SoftwareInducedFailureType(FailureType):

    pass
class ProcessingResourceType:

    pass
class pcm_av_pc_reliability_av_pc_HardwareInducedFailureType(FailureType):

    def __init__(self, hardwareInducedFailureType__ProcessingResourceType: "ProcessingResourceType" = None, FailureType: "pcm_av_pc_repository_av_pc_Repository" = None, FailureType326: "pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription" = None, FailureType248: "pcm_av_pc_repository_av_pc_Signature" = None, FailureType429: "pcm_av_pc_seff_reliability_av_pc_FailureHandlingEntity" = None):
        self.hardwareInducedFailureType__ProcessingResourceType = hardwareInducedFailureType__ProcessingResourceType
        
        pass
    @property
    def hardwareInducedFailureType__ProcessingResourceType(self):
        return self.__hardwareInducedFailureType__ProcessingResourceType

    @hardwareInducedFailureType__ProcessingResourceType.setter
    def hardwareInducedFailureType__ProcessingResourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_reliability_av_pc_HardwareInducedFailureType__hardwareInducedFailureType__ProcessingResourceType", None)
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

    def HardwareInducedFailureTypeHasProcessingResourceType(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement HardwareInducedFailureTypeHasProcessingResourceType method
        pass

class pcm_av_pc_reliability_av_pc_FailureOccurrenceDescription:

    def __init__(self, failureProbability: float):
        self.failureProbability = failureProbability
        
        pass
    @property
    def failureProbability(self):
        return self.__failureProbability

    @failureProbability.setter
    def failureProbability(self, failureProbability: float):
        self.__failureProbability = failureProbability


    def EnsureValidFailureProbabilityRange(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement EnsureValidFailureProbabilityRange method
        pass

class pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription(FailureOccurrenceDescription):

    def __init__(self, externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation: "qos_reliability_av_pc_SpecifiedReliabilityAnnotation" = None, pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription: "FailureType" = None):
        self.externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation = externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation
        self.pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription = pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription
        
        pass
    @property
    def externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation(self):
        return self.__externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation

    @externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation.setter
    def externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription__externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation", None)
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
    def pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription(self):
        return self.__pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription

    @pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription.setter
    def pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription__pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription", None)
        self.__pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FailureType326"):
                opp_val = getattr(old_value, "FailureType326", None)
                if opp_val == self:
                    setattr(old_value, "FailureType326", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FailureType326"):
                opp_val = getattr(value, "FailureType326", None)
                setattr(value, "FailureType326", self)

    def NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription method
        pass

class CommunicationLinkResourceType:

    pass
class Variable:

    pass
class pcm_av_pc_parameter_av_pc_CharacterisedVariable(Variable):

    def __init__(self, characterisationType: str):
        self.characterisationType = characterisationType
        
        pass
    @property
    def characterisationType(self):
        return self.__characterisationType

    @characterisationType.setter
    def characterisationType(self, characterisationType: str):
        self.__characterisationType = characterisationType


class pcm_av_pc_parameter_av_pc_VariableCharacterisation:

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
        old_value = getattr(self, f"_pcm_av_pc_parameter_av_pc_VariableCharacterisation__variableCharacterisation_Specification", None)
        self.__variableCharacterisation_Specification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable316"):
                opp_val = getattr(old_value, "PCMRandomVariable316", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable316", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable316"):
                opp_val = getattr(value, "PCMRandomVariable316", None)
                setattr(value, "PCMRandomVariable316", self)

    @property
    def variableCharacterisation_VariableUsage(self):
        return self.__variableCharacterisation_VariableUsage

    @variableCharacterisation_VariableUsage.setter
    def variableCharacterisation_VariableUsage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_parameter_av_pc_VariableCharacterisation__variableCharacterisation_VariableUsage", None)
        self.__variableCharacterisation_VariableUsage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableUsage318"):
                opp_val = getattr(old_value, "VariableUsage318", None)
                if opp_val == self:
                    setattr(old_value, "VariableUsage318", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableUsage318"):
                opp_val = getattr(value, "VariableUsage318", None)
                setattr(value, "VariableUsage318", self)

class parameter_av_pc_pcm_av_pc_AbstractNamedReference:

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
class pcm_av_pc_seff_performance_av_pc_ResourceCall(CallAction):

    def __init__(self, resourceCall__PCMRandomVariable: "PCMRandomVariable" = None, resourceCall__Action: "AbstractInternalControlFlowAction" = None, pcm_av_pc_seff_performance_av_pc_ResourceCall: "entity_av_pc_ResourceRequiredRole" = None, pcm_av_pc_seff_performance_av_pc_ResourceCall413: "ResourceSignature" = None, CallAction: "pcm_av_pc_parameter_av_pc_VariableUsage" = None):
        self.resourceCall__PCMRandomVariable = resourceCall__PCMRandomVariable
        self.resourceCall__Action = resourceCall__Action
        self.pcm_av_pc_seff_performance_av_pc_ResourceCall = pcm_av_pc_seff_performance_av_pc_ResourceCall
        self.pcm_av_pc_seff_performance_av_pc_ResourceCall413 = pcm_av_pc_seff_performance_av_pc_ResourceCall413
        
        pass
    @property
    def resourceCall__PCMRandomVariable(self):
        return self.__resourceCall__PCMRandomVariable

    @resourceCall__PCMRandomVariable.setter
    def resourceCall__PCMRandomVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_performance_av_pc_ResourceCall__resourceCall__PCMRandomVariable", None)
        self.__resourceCall__PCMRandomVariable = value
        
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
    def pcm_av_pc_seff_performance_av_pc_ResourceCall(self):
        return self.__pcm_av_pc_seff_performance_av_pc_ResourceCall

    @pcm_av_pc_seff_performance_av_pc_ResourceCall.setter
    def pcm_av_pc_seff_performance_av_pc_ResourceCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_performance_av_pc_ResourceCall__pcm_av_pc_seff_performance_av_pc_ResourceCall", None)
        self.__pcm_av_pc_seff_performance_av_pc_ResourceCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entity_av_pc_ResourceRequiredRole411"):
                opp_val = getattr(old_value, "entity_av_pc_ResourceRequiredRole411", None)
                if opp_val == self:
                    setattr(old_value, "entity_av_pc_ResourceRequiredRole411", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entity_av_pc_ResourceRequiredRole411"):
                opp_val = getattr(value, "entity_av_pc_ResourceRequiredRole411", None)
                setattr(value, "entity_av_pc_ResourceRequiredRole411", self)

    @property
    def pcm_av_pc_seff_performance_av_pc_ResourceCall413(self):
        return self.__pcm_av_pc_seff_performance_av_pc_ResourceCall413

    @pcm_av_pc_seff_performance_av_pc_ResourceCall413.setter
    def pcm_av_pc_seff_performance_av_pc_ResourceCall413(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_performance_av_pc_ResourceCall__pcm_av_pc_seff_performance_av_pc_ResourceCall413", None)
        self.__pcm_av_pc_seff_performance_av_pc_ResourceCall413 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceSignature414"):
                opp_val = getattr(old_value, "ResourceSignature414", None)
                if opp_val == self:
                    setattr(old_value, "ResourceSignature414", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceSignature414"):
                opp_val = getattr(value, "ResourceSignature414", None)
                setattr(value, "ResourceSignature414", self)

    @property
    def resourceCall__Action(self):
        return self.__resourceCall__Action

    @resourceCall__Action.setter
    def resourceCall__Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_performance_av_pc_ResourceCall__resourceCall__Action", None)
        self.__resourceCall__Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractInternalControlFlowAction409"):
                opp_val = getattr(old_value, "AbstractInternalControlFlowAction409", None)
                if opp_val == self:
                    setattr(old_value, "AbstractInternalControlFlowAction409", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractInternalControlFlowAction409"):
                opp_val = getattr(value, "AbstractInternalControlFlowAction409", None)
                setattr(value, "AbstractInternalControlFlowAction409", self)

    def SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

    def ResourceRequiredRoleMustBeReferencedByComponent(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement ResourceRequiredRoleMustBeReferencedByComponent method
        pass

    def ResourceSignatureBelongsToResourceRequiredRole(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement ResourceSignatureBelongsToResourceRequiredRole method
        pass

class pcm_av_pc_seff_av_pc_CallReturnAction(CallAction):

    pass
class pcm_av_pc_seff_performance_av_pc_InfrastructureCall(CallAction):

    def __init__(self, pcm_av_pc_seff_performance_av_pc_InfrastructureCall406: "InfrastructureRequiredRole" = None, pcm_av_pc_seff_performance_av_pc_InfrastructureCall: "InfrastructureSignature" = None, infrastructureCall__PCMRandomVariable: "PCMRandomVariable" = None, infrastructureCall__Action: "AbstractInternalControlFlowAction" = None, CallAction: "pcm_av_pc_parameter_av_pc_VariableUsage" = None):
        self.pcm_av_pc_seff_performance_av_pc_InfrastructureCall406 = pcm_av_pc_seff_performance_av_pc_InfrastructureCall406
        self.pcm_av_pc_seff_performance_av_pc_InfrastructureCall = pcm_av_pc_seff_performance_av_pc_InfrastructureCall
        self.infrastructureCall__PCMRandomVariable = infrastructureCall__PCMRandomVariable
        self.infrastructureCall__Action = infrastructureCall__Action
        
        pass
    @property
    def infrastructureCall__PCMRandomVariable(self):
        return self.__infrastructureCall__PCMRandomVariable

    @infrastructureCall__PCMRandomVariable.setter
    def infrastructureCall__PCMRandomVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_performance_av_pc_InfrastructureCall__infrastructureCall__PCMRandomVariable", None)
        self.__infrastructureCall__PCMRandomVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable403"):
                opp_val = getattr(old_value, "PCMRandomVariable403", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable403", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable403"):
                opp_val = getattr(value, "PCMRandomVariable403", None)
                setattr(value, "PCMRandomVariable403", self)

    @property
    def pcm_av_pc_seff_performance_av_pc_InfrastructureCall406(self):
        return self.__pcm_av_pc_seff_performance_av_pc_InfrastructureCall406

    @pcm_av_pc_seff_performance_av_pc_InfrastructureCall406.setter
    def pcm_av_pc_seff_performance_av_pc_InfrastructureCall406(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_performance_av_pc_InfrastructureCall__pcm_av_pc_seff_performance_av_pc_InfrastructureCall406", None)
        self.__pcm_av_pc_seff_performance_av_pc_InfrastructureCall406 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InfrastructureRequiredRole407"):
                opp_val = getattr(old_value, "InfrastructureRequiredRole407", None)
                if opp_val == self:
                    setattr(old_value, "InfrastructureRequiredRole407", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InfrastructureRequiredRole407"):
                opp_val = getattr(value, "InfrastructureRequiredRole407", None)
                setattr(value, "InfrastructureRequiredRole407", self)

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
            if hasattr(old_value, "InfrastructureSignature401"):
                opp_val = getattr(old_value, "InfrastructureSignature401", None)
                if opp_val == self:
                    setattr(old_value, "InfrastructureSignature401", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InfrastructureSignature401"):
                opp_val = getattr(value, "InfrastructureSignature401", None)
                setattr(value, "InfrastructureSignature401", self)

    @property
    def infrastructureCall__Action(self):
        return self.__infrastructureCall__Action

    @infrastructureCall__Action.setter
    def infrastructureCall__Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_seff_performance_av_pc_InfrastructureCall__infrastructureCall__Action", None)
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

    def ReferencedRequiredRoleMustBeRequiredByComponent(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement ReferencedRequiredRoleMustBeRequiredByComponent method
        pass

    def SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

    def SignatureMustBelongToUsedRequiredRole(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement SignatureMustBelongToUsedRequiredRole method
        pass

class pcm_av_pc_parameter_av_pc_VariableUsage:

    pass
class pcm_av_pc_resourcetype_av_pc_ResourceInterface(Entity):

    pass
class NetworkInducedFailureType:

    pass
class pcm_av_pc_resourcetype_av_pc_SchedulingPolicy(Entity):

    pass
class SchedulingPolicy:

    pass
class pcm_av_pc_resourcetype_av_pc_ResourceRepository:

    pass
class ResourceRepository:

    pass
class UnitCarryingElement:

    pass
class pcm_av_pc_resourcetype_av_pc_ResourceType(entity_av_pc_Entity, UnitCarryingElement, entity_av_pc_ResourceInterfaceProvidingEntity):

    pass
class HardwareInducedFailureType:

    pass
class ResourceType:

    pass
class pcm_av_pc_resourcetype_av_pc_CommunicationLinkResourceType(ResourceType):

    pass
class pcm_av_pc_resourcetype_av_pc_ProcessingResourceType(ResourceType):

    pass
class pcm_av_pc_protocol_av_pc_Protocol:

    def __init__(self, protocolTypeID: str):
        self.protocolTypeID = protocolTypeID
        
        pass
    @property
    def protocolTypeID(self):
        return self.__protocolTypeID

    @protocolTypeID.setter
    def protocolTypeID(self, protocolTypeID: str):
        self.__protocolTypeID = protocolTypeID


class NamedElement:

    pass
class pcm_av_pc_resourceenvironment_av_pc_ResourceEnvironment(NamedElement):

    pass
class pcm_av_pc_repository_av_pc_InnerDeclaration(NamedElement):

    pass
class InnerDeclaration:

    pass
class CompositeDataType:

    pass
class repository_av_pc_DataType:

    pass
class pcm_av_pc_repository_av_pc_CompositeDataType(entity_av_pc_Entity, repository_av_pc_DataType):

    pass
class pcm_av_pc_repository_av_pc_CollectionDataType(entity_av_pc_Entity, repository_av_pc_DataType):

    pass
class pcm_av_pc_repository_av_pc_PrimitiveDataType(DataType):

    def __init__(self, type: str, DataType228: "pcm_av_pc_repository_av_pc_Repository" = None, DataType: "pcm_av_pc_repository_av_pc_Parameter" = None, DataType280: "pcm_av_pc_repository_av_pc_InnerDeclaration" = None, DataType276: "pcm_av_pc_repository_av_pc_CollectionDataType" = None, DataType261: "pcm_av_pc_repository_av_pc_OperationSignature" = None):
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class pcm_av_pc_resourcetype_av_pc_ResourceSignature(Entity):

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
        old_value = getattr(self, f"_pcm_av_pc_resourcetype_av_pc_ResourceSignature__resourceSignature__Parameter", None)
        self.__resourceSignature__Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Parameter284"):
                opp_val = getattr(old_value, "Parameter284", None)
                if opp_val == self:
                    setattr(old_value, "Parameter284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Parameter284"):
                opp_val = getattr(value, "Parameter284", None)
                setattr(value, "Parameter284", self)

    @property
    def resourceSignatures__ResourceInterface(self):
        return self.__resourceSignatures__ResourceInterface

    @resourceSignatures__ResourceInterface.setter
    def resourceSignatures__ResourceInterface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_resourcetype_av_pc_ResourceSignature__resourceSignatures__ResourceInterface", None)
        self.__resourceSignatures__ResourceInterface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceInterface286"):
                opp_val = getattr(old_value, "ResourceInterface286", None)
                if opp_val == self:
                    setattr(old_value, "ResourceInterface286", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceInterface286"):
                opp_val = getattr(value, "ResourceInterface286", None)
                setattr(value, "ResourceInterface286", self)

class pcm_av_pc_repository_av_pc_Role(Entity):

    pass
class pcm_av_pc_repository_av_pc_ProvidesComponentType(RepositoryComponent):

    def __init__(self, RepositoryComponent: "pcm_av_pc_composition_av_pc_AssemblyContext" = None, RepositoryComponent224: "pcm_av_pc_repository_av_pc_Repository" = None):
        
        pass
    def AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType method
        pass

class ProvidesComponentType:

    pass
class pcm_av_pc_repository_av_pc_CompleteComponentType(RepositoryComponent):

    def __init__(self, pcm_av_pc_repository_av_pc_CompleteComponentType: set["ProvidesComponentType"] = None, RepositoryComponent: "pcm_av_pc_composition_av_pc_AssemblyContext" = None, RepositoryComponent224: "pcm_av_pc_repository_av_pc_Repository" = None):
        self.pcm_av_pc_repository_av_pc_CompleteComponentType = pcm_av_pc_repository_av_pc_CompleteComponentType if pcm_av_pc_repository_av_pc_CompleteComponentType is not None else set()
        
        pass
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
                    

    def providedInterfacesHaveToConformToProvidedType2(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement providedInterfacesHaveToConformToProvidedType2 method
        pass

    def AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType method
        pass

class repository_av_pc_ImplementationComponentType:

    pass
class entity_av_pc_ComposedProvidingRequiringEntity:

    pass
class pcm_av_pc_system_av_pc_System(entity_av_pc_Entity, entity_av_pc_ComposedProvidingRequiringEntity):

    def __init__(self, system_QoSAnnotations: set["QoSAnnotations"] = None):
        self.system_QoSAnnotations = system_QoSAnnotations if system_QoSAnnotations is not None else set()
        
        pass
    @property
    def system_QoSAnnotations(self):
        return self.__system_QoSAnnotations

    @system_QoSAnnotations.setter
    def system_QoSAnnotations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_system_av_pc_System__system_QoSAnnotations", None)
        self.__system_QoSAnnotations = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QoSAnnotations454"):
                    opp_val = getattr(item, "QoSAnnotations454", None)
                    
                    if opp_val == self:
                        setattr(item, "QoSAnnotations454", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QoSAnnotations454"):
                    opp_val = getattr(item, "QoSAnnotations454", None)
                    
                    setattr(item, "QoSAnnotations454", self)
                    

    def SystemMustHaveAtLeastOneProvidedRole(self, pcm_av_pc_context, pcm_av_pc_diagnostics) :
        # TODO: Implement SystemMustHaveAtLeastOneProvidedRole method
        pass

class pcm_av_pc_subsystem_av_pc_SubSystem(repository_av_pc_RepositoryComponent, entity_av_pc_ComposedProvidingRequiringEntity):

    pass
class pcm_av_pc_completions_av_pc_Completion(repository_av_pc_ImplementationComponentType, entity_av_pc_ComposedProvidingRequiringEntity):

    pass
class pcm_av_pc_repository_av_pc_CompositeComponent(repository_av_pc_ImplementationComponentType, entity_av_pc_ComposedProvidingRequiringEntity):

    def __init__(self):
        
        pass
    def RequireSameInterfaces(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement RequireSameInterfaces method
        pass

    def ProvideSameInterfaces(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement ProvideSameInterfaces method
        pass

class pcm_av_pc_repository_av_pc_InfrastructureProvidedRole(ProvidedRole):

    pass
class pcm_av_pc_repository_av_pc_OperationProvidedRole(ProvidedRole):

    pass
class pcm_av_pc_repository_av_pc_SinkRole(ProvidedRole):

    pass
class pcm_av_pc_repository_av_pc_SourceRole(RequiredRole):

    pass
class pcm_av_pc_repository_av_pc_OperationRequiredRole(RequiredRole):

    pass
class OperationInterface:

    pass
class pcm_av_pc_repository_av_pc_OperationSignature(Signature):

    def __init__(self, pcm_av_pc_repository_av_pc_OperationSignature: "DataType" = None, signatures__OperationInterface: "OperationInterface" = None, operationSignature__Parameter: set["Parameter"] = None, Signature431: "pcm_av_pc_qosannotations_av_pc_SpecifiedQoSAnnotation" = None, Signature: "pcm_av_pc_seff_av_pc_ServiceEffectSpecification" = None, Signature440: "pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction" = None):
        self.pcm_av_pc_repository_av_pc_OperationSignature = pcm_av_pc_repository_av_pc_OperationSignature
        self.signatures__OperationInterface = signatures__OperationInterface
        self.operationSignature__Parameter = operationSignature__Parameter if operationSignature__Parameter is not None else set()
        
        pass
    @property
    def operationSignature__Parameter(self):
        return self.__operationSignature__Parameter

    @operationSignature__Parameter.setter
    def operationSignature__Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_OperationSignature__operationSignature__Parameter", None)
        self.__operationSignature__Parameter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter259"):
                    opp_val = getattr(item, "Parameter259", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter259", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter259"):
                    opp_val = getattr(item, "Parameter259", None)
                    
                    setattr(item, "Parameter259", self)
                    

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
            if hasattr(old_value, "DataType261"):
                opp_val = getattr(old_value, "DataType261", None)
                if opp_val == self:
                    setattr(old_value, "DataType261", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType261"):
                opp_val = getattr(value, "DataType261", None)
                setattr(value, "DataType261", self)

    @property
    def signatures__OperationInterface(self):
        return self.__signatures__OperationInterface

    @signatures__OperationInterface.setter
    def signatures__OperationInterface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_av_pc_repository_av_pc_OperationSignature__signatures__OperationInterface", None)
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

    def ParameterNamesHaveToBeUniqueForASignature(self, pcm_av_pc_diagnostics, pcm_av_pc_context) :
        # TODO: Implement ParameterNamesHaveToBeUniqueForASignature method
        pass

class pcm_av_pc_repository_av_pc_RequiredRole(Role):

    pass
class pcm_av_pc_repository_av_pc_InfrastructureRequiredRole(RequiredRole):

    pass