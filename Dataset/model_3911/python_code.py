from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class VariableCharacterisationType(Enum):
    NUMBER_OF_ELEMENTS = "NUMBER_OF_ELEMENTS"
    VALUE = "VALUE"
    BYTESIZE = "BYTESIZE"
    TYPE = "TYPE"
    STRUCTURE = "STRUCTURE"
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
class ParameterModifier(Enum):
    none = "none"
    in_ = "in_"
    out = "out"
    inout = "inout"


############################################
# Definition of Classes
############################################

class seff_pc_pc_CallReturnAction:

    pass
class seff_pc_pc_AbstractAction:

    pass
class seff_reliability_pc_pc_FailureHandlingEntity:

    pass
class pcm_pc_pc_seff_pc_pc_ExternalCallAction(seff_pc_pc_CallReturnAction, seff_reliability_pc_pc_FailureHandlingEntity, seff_pc_pc_AbstractAction):

    def __init__(self, retryCount: int, pcm_pc_pc_seff_pc_pc_ExternalCallAction: "OperationSignature" = None, pcm_pc_pc_seff_pc_pc_ExternalCallAction375: "OperationRequiredRole" = None):
        self.retryCount = retryCount
        self.pcm_pc_pc_seff_pc_pc_ExternalCallAction = pcm_pc_pc_seff_pc_pc_ExternalCallAction
        self.pcm_pc_pc_seff_pc_pc_ExternalCallAction375 = pcm_pc_pc_seff_pc_pc_ExternalCallAction375
        
        pass
    @property
    def retryCount(self):
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
            if hasattr(old_value, "OperationSignature373"):
                opp_val = getattr(old_value, "OperationSignature373", None)
                if opp_val == self:
                    setattr(old_value, "OperationSignature373", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationSignature373"):
                opp_val = getattr(value, "OperationSignature373", None)
                setattr(value, "OperationSignature373", self)

    @property
    def pcm_pc_pc_seff_pc_pc_ExternalCallAction375(self):
        return self.__pcm_pc_pc_seff_pc_pc_ExternalCallAction375

    @pcm_pc_pc_seff_pc_pc_ExternalCallAction375.setter
    def pcm_pc_pc_seff_pc_pc_ExternalCallAction375(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_pc_pc_ExternalCallAction__pcm_pc_pc_seff_pc_pc_ExternalCallAction375", None)
        self.__pcm_pc_pc_seff_pc_pc_ExternalCallAction375 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationRequiredRole376"):
                opp_val = getattr(old_value, "OperationRequiredRole376", None)
                if opp_val == self:
                    setattr(old_value, "OperationRequiredRole376", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationRequiredRole376"):
                opp_val = getattr(value, "OperationRequiredRole376", None)
                setattr(value, "OperationRequiredRole376", self)

    def OperationRequiredRoleMustBeReferencedByContainer(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement OperationRequiredRoleMustBeReferencedByContainer method
        pass

    def SignatureBelongsToRole(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement SignatureBelongsToRole method
        pass

class ResourceDemandingInternalBehaviour:

    pass
class seff_pc_pc_ResourceDemandingBehaviour:

    pass
class seff_pc_pc_ServiceEffectSpecification:

    pass
class pcm_pc_pc_seff_pc_pc_SynchronisationPoint:

    pass
class ForkAction:

    pass
class ForkedBehaviour:

    pass
class ResourceDemandingSEFF:

    pass
class pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification:

    def __init__(self, seffTypeID: str, pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification: "Signature" = None, serviceEffectSpecifications__BasicComponent: "BasicComponent" = None):
        self.seffTypeID = seffTypeID
        self.pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification = pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification
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
        old_value = getattr(self, f"_pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification__serviceEffectSpecifications__BasicComponent", None)
        self.__serviceEffectSpecifications__BasicComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicComponent353"):
                opp_val = getattr(old_value, "BasicComponent353", None)
                if opp_val == self:
                    setattr(old_value, "BasicComponent353", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicComponent353"):
                opp_val = getattr(value, "BasicComponent353", None)
                setattr(value, "BasicComponent353", self)

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

    def ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole method
        pass

class pcm_pc_pc_seff_pc_pc_CallAction:

    pass
class ResourceDemandingBehaviour:

    pass
class pcm_pc_pc_seff_pc_pc_ResourceDemandingInternalBehaviour(ResourceDemandingBehaviour):

    pass
class pcm_pc_pc_seff_pc_pc_ForkedBehaviour(ResourceDemandingBehaviour):

    pass
class BranchAction:

    pass
class AbstractBranchTransition:

    pass
class AbstractLoopAction:

    pass
class pcm_pc_pc_seff_pc_pc_CollectionIteratorAction(AbstractLoopAction):

    pass
class pcm_pc_pc_seff_pc_pc_LoopAction(AbstractLoopAction):

    pass
class qos_reliability_pc_pc_SpecifiedReliabilityAnnotation:

    pass
class AbstractAction:

    pass
class pcm_pc_pc_seff_pc_pc_AbstractInternalControlFlowAction(AbstractAction):

    pass
class AbstractInternalControlFlowAction:

    pass
class pcm_pc_pc_seff_pc_pc_ForkAction(AbstractInternalControlFlowAction):

    pass
class pcm_pc_pc_seff_pc_pc_BranchAction(AbstractInternalControlFlowAction):

    def __init__(self, branchAction_AbstractBranchTransition: set["AbstractBranchTransition"] = None, AbstractInternalControlFlowAction405: "pcm_pc_pc_seff_performance_pc_pc_ResourceCall" = None, AbstractInternalControlFlowAction418: "pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand" = None, AbstractInternalControlFlowAction: "pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall" = None):
        self.branchAction_AbstractBranchTransition = branchAction_AbstractBranchTransition if branchAction_AbstractBranchTransition is not None else set()
        
        pass
    @property
    def branchAction_AbstractBranchTransition(self):
        return self.__branchAction_AbstractBranchTransition

    @branchAction_AbstractBranchTransition.setter
    def branchAction_AbstractBranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_pc_pc_BranchAction__branchAction_AbstractBranchTransition", None)
        self.__branchAction_AbstractBranchTransition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractBranchTransition348"):
                    opp_val = getattr(item, "AbstractBranchTransition348", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractBranchTransition348", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractBranchTransition348"):
                    opp_val = getattr(item, "AbstractBranchTransition348", None)
                    
                    setattr(item, "AbstractBranchTransition348", self)
                    

    def EitherGuardedBranchesOrProbabilisiticBranchTransitions(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement EitherGuardedBranchesOrProbabilisiticBranchTransitions method
        pass

    def AllProbabilisticBranchProbabilitiesMustSumUpTo1(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement AllProbabilisticBranchProbabilitiesMustSumUpTo1 method
        pass

class pcm_pc_pc_seff_pc_pc_StartAction(AbstractInternalControlFlowAction):

    def __init__(self, AbstractInternalControlFlowAction405: "pcm_pc_pc_seff_performance_pc_pc_ResourceCall" = None, AbstractInternalControlFlowAction418: "pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand" = None, AbstractInternalControlFlowAction: "pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall" = None):
        
        pass
    def StartActionPredecessorMustNotBeDefined(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement StartActionPredecessorMustNotBeDefined method
        pass

class pcm_pc_pc_seff_pc_pc_AbstractLoopAction(AbstractInternalControlFlowAction):

    pass
class pcm_pc_pc_seff_pc_pc_ReleaseAction(AbstractInternalControlFlowAction):

    pass
class pcm_pc_pc_seff_pc_pc_StopAction(AbstractInternalControlFlowAction):

    def __init__(self, AbstractInternalControlFlowAction405: "pcm_pc_pc_seff_performance_pc_pc_ResourceCall" = None, AbstractInternalControlFlowAction418: "pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand" = None, AbstractInternalControlFlowAction: "pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall" = None):
        
        pass
    def StopActionSuccessorMustNotBeDefined(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement StopActionSuccessorMustNotBeDefined method
        pass

class ProcessingResourceType:

    pass
class CommunicationLinkResourceType:

    pass
class SoftwareInducedFailureType:

    pass
class pcm_pc_pc_reliability_pc_pc_ResourceTimeoutFailureType(SoftwareInducedFailureType):

    pass
class InternalAction:

    pass
class FailureOccurrenceDescription:

    pass
class pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription(FailureOccurrenceDescription):

    def __init__(self, externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation: "qos_reliability_pc_pc_SpecifiedReliabilityAnnotation" = None, pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription: "FailureType" = None):
        self.externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation = externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation
        self.pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription = pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription
        
        pass
    @property
    def externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation(self):
        return self.__externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation

    @externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation.setter
    def externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription__externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation", None)
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
    def pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription(self):
        return self.__pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription

    @pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription.setter
    def pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription__pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription", None)
        self.__pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FailureType322"):
                opp_val = getattr(old_value, "FailureType322", None)
                if opp_val == self:
                    setattr(old_value, "FailureType322", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FailureType322"):
                opp_val = getattr(value, "FailureType322", None)
                setattr(value, "FailureType322", self)

    def NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription method
        pass

class pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription(FailureOccurrenceDescription):

    def __init__(self, internalFailureOccurrenceDescriptions__InternalAction: "InternalAction" = None, internalFailureOccurrenceDescriptions__SoftwareInducedFailureType: "SoftwareInducedFailureType" = None):
        self.internalFailureOccurrenceDescriptions__InternalAction = internalFailureOccurrenceDescriptions__InternalAction
        self.internalFailureOccurrenceDescriptions__SoftwareInducedFailureType = internalFailureOccurrenceDescriptions__SoftwareInducedFailureType
        
        pass
    @property
    def internalFailureOccurrenceDescriptions__InternalAction(self):
        return self.__internalFailureOccurrenceDescriptions__InternalAction

    @internalFailureOccurrenceDescriptions__InternalAction.setter
    def internalFailureOccurrenceDescriptions__InternalAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription__internalFailureOccurrenceDescriptions__InternalAction", None)
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

    @property
    def internalFailureOccurrenceDescriptions__SoftwareInducedFailureType(self):
        return self.__internalFailureOccurrenceDescriptions__SoftwareInducedFailureType

    @internalFailureOccurrenceDescriptions__SoftwareInducedFailureType.setter
    def internalFailureOccurrenceDescriptions__SoftwareInducedFailureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription__internalFailureOccurrenceDescriptions__SoftwareInducedFailureType", None)
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

    def NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription method
        pass

class InternalFailureOccurrenceDescription:

    pass
class Variable:

    pass
class pcm_pc_pc_parameter_pc_pc_CharacterisedVariable(Variable):

    def __init__(self, characterisationType: str):
        self.characterisationType = characterisationType
        
        pass
    @property
    def characterisationType(self):
        return self.__characterisationType

    @characterisationType.setter
    def characterisationType(self, characterisationType: str):
        self.__characterisationType = characterisationType


class pcm_pc_pc_reliability_pc_pc_FailureOccurrenceDescription:

    def __init__(self, failureProbability: float):
        self.failureProbability = failureProbability
        
        pass
    @property
    def failureProbability(self):
        return self.__failureProbability

    @failureProbability.setter
    def failureProbability(self, failureProbability: float):
        self.__failureProbability = failureProbability


    def EnsureValidFailureProbabilityRange(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement EnsureValidFailureProbabilityRange method
        pass

class pcm_pc_pc_parameter_pc_pc_VariableUsage:

    pass
class pcm_pc_pc_parameter_pc_pc_VariableCharacterisation:

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
    def variableCharacterisation_VariableUsage(self):
        return self.__variableCharacterisation_VariableUsage

    @variableCharacterisation_VariableUsage.setter
    def variableCharacterisation_VariableUsage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_parameter_pc_pc_VariableCharacterisation__variableCharacterisation_VariableUsage", None)
        self.__variableCharacterisation_VariableUsage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableUsage314"):
                opp_val = getattr(old_value, "VariableUsage314", None)
                if opp_val == self:
                    setattr(old_value, "VariableUsage314", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableUsage314"):
                opp_val = getattr(value, "VariableUsage314", None)
                setattr(value, "VariableUsage314", self)

    @property
    def variableCharacterisation_Specification(self):
        return self.__variableCharacterisation_Specification

    @variableCharacterisation_Specification.setter
    def variableCharacterisation_Specification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_parameter_pc_pc_VariableCharacterisation__variableCharacterisation_Specification", None)
        self.__variableCharacterisation_Specification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable312"):
                opp_val = getattr(old_value, "PCMRandomVariable312", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable312", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable312"):
                opp_val = getattr(value, "PCMRandomVariable312", None)
                setattr(value, "PCMRandomVariable312", self)

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
class ResourceRepository:

    pass
class pcm_pc_pc_protocol_pc_pc_Protocol:

    def __init__(self, protocolTypeID: str):
        self.protocolTypeID = protocolTypeID
        
        pass
    @property
    def protocolTypeID(self):
        return self.__protocolTypeID

    @protocolTypeID.setter
    def protocolTypeID(self, protocolTypeID: str):
        self.__protocolTypeID = protocolTypeID


class NetworkInducedFailureType:

    pass
class SchedulingPolicy:

    pass
class pcm_pc_pc_resourcetype_pc_pc_ResourceRepository:

    pass
class CompositeDataType:

    pass
class UnitCarryingElement:

    pass
class HardwareInducedFailureType:

    pass
class ResourceType:

    pass
class pcm_pc_pc_resourcetype_pc_pc_CommunicationLinkResourceType(ResourceType):

    pass
class pcm_pc_pc_resourcetype_pc_pc_ProcessingResourceType(ResourceType):

    pass
class NamedElement:

    pass
class pcm_pc_pc_repository_pc_pc_InnerDeclaration(NamedElement):

    pass
class InnerDeclaration:

    pass
class repository_pc_pc_ImplementationComponentType:

    pass
class entity_pc_pc_ComposedProvidingRequiringEntity:

    pass
class pcm_pc_pc_repository_pc_pc_CompositeComponent(repository_pc_pc_ImplementationComponentType, entity_pc_pc_ComposedProvidingRequiringEntity):

    def __init__(self):
        
        pass
    def RequireSameInterfaces(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement RequireSameInterfaces method
        pass

    def ProvideSameInterfaces(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement ProvideSameInterfaces method
        pass

class repository_pc_pc_DataType:

    pass
class ProvidesComponentType:

    pass
class OperationInterface:

    pass
class RequiredCharacterisation:

    pass
class InfrastructureInterface:

    pass
class pcm_pc_pc_repository_pc_pc_ExceptionType:

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
class pcm_pc_pc_repository_pc_pc_InfrastructureSignature(Signature):

    pass
class pcm_pc_pc_repository_pc_pc_OperationSignature(Signature):

    def __init__(self, signatures__OperationInterface: "OperationInterface" = None, operationSignature__Parameter: set["Parameter"] = None, pcm_pc_pc_repository_pc_pc_OperationSignature: "DataType" = None, Signature: "pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification" = None, Signature436: "pcm_pc_pc_qosannotations_pc_pc_SpecifiedOutputParameterAbstraction" = None, Signature427: "pcm_pc_pc_qosannotations_pc_pc_SpecifiedQoSAnnotation" = None):
        self.signatures__OperationInterface = signatures__OperationInterface
        self.operationSignature__Parameter = operationSignature__Parameter if operationSignature__Parameter is not None else set()
        self.pcm_pc_pc_repository_pc_pc_OperationSignature = pcm_pc_pc_repository_pc_pc_OperationSignature
        
        pass
    @property
    def signatures__OperationInterface(self):
        return self.__signatures__OperationInterface

    @signatures__OperationInterface.setter
    def signatures__OperationInterface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_OperationSignature__signatures__OperationInterface", None)
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
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_OperationSignature__operationSignature__Parameter", None)
        self.__operationSignature__Parameter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter255"):
                    opp_val = getattr(item, "Parameter255", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter255", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter255"):
                    opp_val = getattr(item, "Parameter255", None)
                    
                    setattr(item, "Parameter255", self)
                    

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
            if hasattr(old_value, "DataType257"):
                opp_val = getattr(old_value, "DataType257", None)
                if opp_val == self:
                    setattr(old_value, "DataType257", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType257"):
                opp_val = getattr(value, "DataType257", None)
                setattr(value, "DataType257", self)

    def ParameterNamesHaveToBeUniqueForASignature(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement ParameterNamesHaveToBeUniqueForASignature method
        pass

class pcm_pc_pc_repository_pc_pc_EventType(Signature):

    pass
class Parameter:

    pass
class pcm_pc_pc_repository_pc_pc_RequiredCharacterisation:

    def __init__(self, type: str, pcm_pc_pc_repository_pc_pc_RequiredCharacterisation: "Parameter" = None, requiredCharacterisations: "Interface" = None):
        self.type = type
        self.pcm_pc_pc_repository_pc_pc_RequiredCharacterisation = pcm_pc_pc_repository_pc_pc_RequiredCharacterisation
        self.requiredCharacterisations = requiredCharacterisations
        
        pass
    @property
    def type(self):
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
    def requiredCharacterisations(self):
        return self.__requiredCharacterisations

    @requiredCharacterisations.setter
    def requiredCharacterisations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_RequiredCharacterisation__requiredCharacterisations", None)
        self.__requiredCharacterisations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Interface234"):
                opp_val = getattr(old_value, "Interface234", None)
                if opp_val == self:
                    setattr(old_value, "Interface234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Interface234"):
                opp_val = getattr(value, "Interface234", None)
                setattr(value, "Interface234", self)

class pcm_pc_pc_repository_pc_pc_DataType:

    pass
class ResourceSignature:

    pass
class Protocol:

    pass
class FailureType:

    pass
class pcm_pc_pc_reliability_pc_pc_SoftwareInducedFailureType(FailureType):

    pass
class pcm_pc_pc_reliability_pc_pc_HardwareInducedFailureType(FailureType):

    def __init__(self, hardwareInducedFailureType__ProcessingResourceType: "ProcessingResourceType" = None, FailureType322: "pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription" = None, FailureType: "pcm_pc_pc_repository_pc_pc_Repository" = None, FailureType244: "pcm_pc_pc_repository_pc_pc_Signature" = None, FailureType425: "pcm_pc_pc_seff_reliability_pc_pc_FailureHandlingEntity" = None):
        self.hardwareInducedFailureType__ProcessingResourceType = hardwareInducedFailureType__ProcessingResourceType
        
        pass
    @property
    def hardwareInducedFailureType__ProcessingResourceType(self):
        return self.__hardwareInducedFailureType__ProcessingResourceType

    @hardwareInducedFailureType__ProcessingResourceType.setter
    def hardwareInducedFailureType__ProcessingResourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_reliability_pc_pc_HardwareInducedFailureType__hardwareInducedFailureType__ProcessingResourceType", None)
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

    def HardwareInducedFailureTypeHasProcessingResourceType(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement HardwareInducedFailureTypeHasProcessingResourceType method
        pass

class pcm_pc_pc_reliability_pc_pc_NetworkInducedFailureType(FailureType):

    def __init__(self, networkInducedFailureType__CommunicationLinkResourceType: "CommunicationLinkResourceType" = None, FailureType322: "pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription" = None, FailureType: "pcm_pc_pc_repository_pc_pc_Repository" = None, FailureType244: "pcm_pc_pc_repository_pc_pc_Signature" = None, FailureType425: "pcm_pc_pc_seff_reliability_pc_pc_FailureHandlingEntity" = None):
        self.networkInducedFailureType__CommunicationLinkResourceType = networkInducedFailureType__CommunicationLinkResourceType
        
        pass
    @property
    def networkInducedFailureType__CommunicationLinkResourceType(self):
        return self.__networkInducedFailureType__CommunicationLinkResourceType

    @networkInducedFailureType__CommunicationLinkResourceType.setter
    def networkInducedFailureType__CommunicationLinkResourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_reliability_pc_pc_NetworkInducedFailureType__networkInducedFailureType__CommunicationLinkResourceType", None)
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

    def NetworkInducedFailureTypeHasCommunicationLinkResourceType(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement NetworkInducedFailureTypeHasCommunicationLinkResourceType method
        pass

class Interface:

    pass
class pcm_pc_pc_repository_pc_pc_EventGroup(Interface):

    pass
class pcm_pc_pc_repository_pc_pc_OperationInterface(Interface):

    def __init__(self, interface__OperationSignature: set["OperationSignature"] = None, Interface234: "pcm_pc_pc_repository_pc_pc_RequiredCharacterisation" = None, Interface: "pcm_pc_pc_repository_pc_pc_Repository" = None, Interface226: "pcm_pc_pc_repository_pc_pc_Interface" = None):
        self.interface__OperationSignature = interface__OperationSignature if interface__OperationSignature is not None else set()
        
        pass
    @property
    def interface__OperationSignature(self):
        return self.__interface__OperationSignature

    @interface__OperationSignature.setter
    def interface__OperationSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_OperationInterface__interface__OperationSignature", None)
        self.__interface__OperationSignature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OperationSignature259"):
                    opp_val = getattr(item, "OperationSignature259", None)
                    
                    if opp_val == self:
                        setattr(item, "OperationSignature259", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OperationSignature259"):
                    opp_val = getattr(item, "OperationSignature259", None)
                    
                    setattr(item, "OperationSignature259", self)
                    

    def SignaturesHaveToBeUniqueForAnInterface(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement SignaturesHaveToBeUniqueForAnInterface method
        pass

class pcm_pc_pc_repository_pc_pc_InfrastructureInterface(Interface):

    pass
class EventType:

    pass
class InfrastructureSignature:

    pass
class DataType:

    pass
class pcm_pc_pc_repository_pc_pc_PrimitiveDataType(DataType):

    def __init__(self, type: str, DataType257: "pcm_pc_pc_repository_pc_pc_OperationSignature" = None, DataType224: "pcm_pc_pc_repository_pc_pc_Repository" = None, DataType: "pcm_pc_pc_repository_pc_pc_Parameter" = None, DataType272: "pcm_pc_pc_repository_pc_pc_CollectionDataType" = None, DataType276: "pcm_pc_pc_repository_pc_pc_InnerDeclaration" = None):
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class pcm_pc_pc_repository_pc_pc_Parameter:

    def __init__(self, parameterName: str, modifier__Parameter: str, pcm_pc_pc_repository_pc_pc_Parameter: "DataType" = None, parameters__InfrastructureSignature: "InfrastructureSignature" = None, parameters__OperationSignature: "OperationSignature" = None, parameter__EventType: "EventType" = None, parameter__ResourceSignature: "ResourceSignature" = None):
        self.parameterName = parameterName
        self.modifier__Parameter = modifier__Parameter
        self.pcm_pc_pc_repository_pc_pc_Parameter = pcm_pc_pc_repository_pc_pc_Parameter
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
    def parameter__EventType(self):
        return self.__parameter__EventType

    @parameter__EventType.setter
    def parameter__EventType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_Parameter__parameter__EventType", None)
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
    def parameters__InfrastructureSignature(self):
        return self.__parameters__InfrastructureSignature

    @parameters__InfrastructureSignature.setter
    def parameters__InfrastructureSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_Parameter__parameters__InfrastructureSignature", None)
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
    def parameters__OperationSignature(self):
        return self.__parameters__OperationSignature

    @parameters__OperationSignature.setter
    def parameters__OperationSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_Parameter__parameters__OperationSignature", None)
        self.__parameters__OperationSignature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationSignature214"):
                opp_val = getattr(old_value, "OperationSignature214", None)
                if opp_val == self:
                    setattr(old_value, "OperationSignature214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationSignature214"):
                opp_val = getattr(value, "OperationSignature214", None)
                setattr(value, "OperationSignature214", self)

    @property
    def parameter__ResourceSignature(self):
        return self.__parameter__ResourceSignature

    @parameter__ResourceSignature.setter
    def parameter__ResourceSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_Parameter__parameter__ResourceSignature", None)
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
class InterfaceProvidingRequiringEntity:

    pass
class pcm_pc_pc_repository_pc_pc_RepositoryComponent(InterfaceProvidingRequiringEntity):

    pass
class CompleteComponentType:

    pass
class ImplementationComponentType:

    pass
class pcm_pc_pc_repository_pc_pc_BasicComponent(ImplementationComponentType):

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
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_BasicComponent__basicComponent_PassiveResource", None)
        self.__basicComponent_PassiveResource = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PassiveResource204"):
                    opp_val = getattr(item, "PassiveResource204", None)
                    
                    if opp_val == self:
                        setattr(item, "PassiveResource204", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PassiveResource204"):
                    opp_val = getattr(item, "PassiveResource204", None)
                    
                    setattr(item, "PassiveResource204", self)
                    

    @property
    def basicComponent_ServiceEffectSpecification(self):
        return self.__basicComponent_ServiceEffectSpecification

    @basicComponent_ServiceEffectSpecification.setter
    def basicComponent_ServiceEffectSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_BasicComponent__basicComponent_ServiceEffectSpecification", None)
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
                    

    def RequireSameInterfacesAsImplementationType(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement RequireSameInterfacesAsImplementationType method
        pass

    def NoSeffTypeUsedTwice(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement NoSeffTypeUsedTwice method
        pass

    def ProvideSameInterfacesAsImplementationType(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement ProvideSameInterfacesAsImplementationType method
        pass

class ServiceEffectSpecification:

    pass
class ResourceTimeoutFailureType:

    pass
class BasicComponent:

    pass
class Branch:

    pass
class pcm_pc_pc_usagemodel_pc_pc_BranchTransition:

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
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_BranchTransition__branchTransition_ScenarioBehaviour", None)
        self.__branchTransition_ScenarioBehaviour = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ScenarioBehaviour185"):
                opp_val = getattr(old_value, "ScenarioBehaviour185", None)
                if opp_val == self:
                    setattr(old_value, "ScenarioBehaviour185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ScenarioBehaviour185"):
                opp_val = getattr(value, "ScenarioBehaviour185", None)
                setattr(value, "ScenarioBehaviour185", self)

    @property
    def branchTransitions_Branch(self):
        return self.__branchTransitions_Branch

    @branchTransitions_Branch.setter
    def branchTransitions_Branch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_BranchTransition__branchTransitions_Branch", None)
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

class BranchTransition:

    pass
class pcm_pc_pc_usagemodel_pc_pc_UserData:

    pass
class Workload:

    pass
class pcm_pc_pc_usagemodel_pc_pc_OpenWorkload(Workload):

    def __init__(self, openWorkload_PCMRandomVariable: "PCMRandomVariable" = None, Workload: "pcm_pc_pc_usagemodel_pc_pc_UsageScenario" = None):
        self.openWorkload_PCMRandomVariable = openWorkload_PCMRandomVariable
        
        pass
    @property
    def openWorkload_PCMRandomVariable(self):
        return self.__openWorkload_PCMRandomVariable

    @openWorkload_PCMRandomVariable.setter
    def openWorkload_PCMRandomVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_OpenWorkload__openWorkload_PCMRandomVariable", None)
        self.__openWorkload_PCMRandomVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable193"):
                opp_val = getattr(old_value, "PCMRandomVariable193", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable193"):
                opp_val = getattr(value, "PCMRandomVariable193", None)
                setattr(value, "PCMRandomVariable193", self)

    def InterArrivalTimeInOpenWorkloadNeedsToBeSpecified(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement InterArrivalTimeInOpenWorkloadNeedsToBeSpecified method
        pass

class pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload(Workload):

    def __init__(self, population: int, closedWorkload_PCMRandomVariable: "PCMRandomVariable" = None, Workload: "pcm_pc_pc_usagemodel_pc_pc_UsageScenario" = None):
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
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload__closedWorkload_PCMRandomVariable", None)
        self.__closedWorkload_PCMRandomVariable = value
        
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

    def PopulationInClosedWorkloadNeedsToBeSpecified(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement PopulationInClosedWorkloadNeedsToBeSpecified method
        pass

    def ThinkTimeInClosedWorkloadNeedsToBeSpecified(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement ThinkTimeInClosedWorkloadNeedsToBeSpecified method
        pass

class ScenarioBehaviour:

    pass
class OperationSignature:

    pass
class AbstractUserAction:

    pass
class pcm_pc_pc_usagemodel_pc_pc_Loop(AbstractUserAction):

    pass
class pcm_pc_pc_usagemodel_pc_pc_Delay(AbstractUserAction):

    pass
class pcm_pc_pc_usagemodel_pc_pc_Start(AbstractUserAction):

    def __init__(self, AbstractUserAction173: "pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction" = None, AbstractUserAction: "pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction" = None, AbstractUserAction182: "pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour" = None):
        
        pass
    def StartHasNoPredecessor(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement StartHasNoPredecessor method
        pass

class pcm_pc_pc_usagemodel_pc_pc_Branch(AbstractUserAction):

    def __init__(self, branch_BranchTransition: set["BranchTransition"] = None, AbstractUserAction173: "pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction" = None, AbstractUserAction: "pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction" = None, AbstractUserAction182: "pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour" = None):
        self.branch_BranchTransition = branch_BranchTransition if branch_BranchTransition is not None else set()
        
        pass
    @property
    def branch_BranchTransition(self):
        return self.__branch_BranchTransition

    @branch_BranchTransition.setter
    def branch_BranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_Branch__branch_BranchTransition", None)
        self.__branch_BranchTransition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BranchTransition187"):
                    opp_val = getattr(item, "BranchTransition187", None)
                    
                    if opp_val == self:
                        setattr(item, "BranchTransition187", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BranchTransition187"):
                    opp_val = getattr(item, "BranchTransition187", None)
                    
                    setattr(item, "BranchTransition187", self)
                    

    def AllBranchProbabilitiesMustSumUpTo1(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement AllBranchProbabilitiesMustSumUpTo1 method
        pass

class pcm_pc_pc_usagemodel_pc_pc_Stop(AbstractUserAction):

    def __init__(self, AbstractUserAction173: "pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction" = None, AbstractUserAction: "pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction" = None, AbstractUserAction182: "pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour" = None):
        
        pass
    def StopHasNoSuccessor(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement StopHasNoSuccessor method
        pass

class pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall(AbstractUserAction):

    def __init__(self, priority: int, pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall: "OperationProvidedRole" = None, pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall166: "OperationSignature" = None, entryLevelSystemCall_OutputParameterUsage: set["VariableUsage"] = None, entryLevelSystemCall_InputParameterUsage: set["VariableUsage"] = None, AbstractUserAction173: "pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction" = None, AbstractUserAction: "pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction" = None, AbstractUserAction182: "pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour" = None):
        self.priority = priority
        self.pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall = pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall
        self.pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall166 = pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall166
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
    def pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall166(self):
        return self.__pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall166

    @pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall166.setter
    def pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall__pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall166", None)
        self.__pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall166 = value
        
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
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall__entryLevelSystemCall_OutputParameterUsage", None)
        self.__entryLevelSystemCall_OutputParameterUsage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableUsage168"):
                    opp_val = getattr(item, "VariableUsage168", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableUsage168", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableUsage168"):
                    opp_val = getattr(item, "VariableUsage168", None)
                    
                    setattr(item, "VariableUsage168", self)
                    

    @property
    def entryLevelSystemCall_InputParameterUsage(self):
        return self.__entryLevelSystemCall_InputParameterUsage

    @entryLevelSystemCall_InputParameterUsage.setter
    def entryLevelSystemCall_InputParameterUsage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall__entryLevelSystemCall_InputParameterUsage", None)
        self.__entryLevelSystemCall_InputParameterUsage = value if value is not None else set()
        
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
    def pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall(self):
        return self.__pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall

    @pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall.setter
    def pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall__pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall", None)
        self.__pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationProvidedRole164"):
                opp_val = getattr(old_value, "OperationProvidedRole164", None)
                if opp_val == self:
                    setattr(old_value, "OperationProvidedRole164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationProvidedRole164"):
                opp_val = getattr(value, "OperationProvidedRole164", None)
                setattr(value, "OperationProvidedRole164", self)

    def EntryLevelSystemCallSignatureMustMatchItsProvidedRole(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement EntryLevelSystemCallSignatureMustMatchItsProvidedRole method
        pass

    def EntryLevelSystemCallMustReferenceProvidedRoleOfASystem(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement EntryLevelSystemCallMustReferenceProvidedRoleOfASystem method
        pass

class UserData:

    pass
class pcm_pc_pc_usagemodel_pc_pc_UsageModel:

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
class pcm_pc_pc_repository_pc_pc_ProvidesComponentType(RepositoryComponent):

    def __init__(self, RepositoryComponent220: "pcm_pc_pc_repository_pc_pc_Repository" = None, RepositoryComponent: "pcm_pc_pc_composition_pc_pc_AssemblyContext" = None):
        
        pass
    def AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType method
        pass

class pcm_pc_pc_repository_pc_pc_CompleteComponentType(RepositoryComponent):

    def __init__(self, pcm_pc_pc_repository_pc_pc_CompleteComponentType: set["ProvidesComponentType"] = None, RepositoryComponent220: "pcm_pc_pc_repository_pc_pc_Repository" = None, RepositoryComponent: "pcm_pc_pc_composition_pc_pc_AssemblyContext" = None):
        self.pcm_pc_pc_repository_pc_pc_CompleteComponentType = pcm_pc_pc_repository_pc_pc_CompleteComponentType if pcm_pc_pc_repository_pc_pc_CompleteComponentType is not None else set()
        
        pass
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
                    

    def providedInterfacesHaveToConformToProvidedType2(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement providedInterfacesHaveToConformToProvidedType2 method
        pass

    def AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType method
        pass

class pcm_pc_pc_repository_pc_pc_ImplementationComponentType(RepositoryComponent):

    def __init__(self, componentType: str, pcm_pc_pc_repository_pc_pc_ImplementationComponentType: set["CompleteComponentType"] = None, pcm_pc_pc_repository_pc_pc_ImplementationComponentType207: set["VariableUsage"] = None, RepositoryComponent220: "pcm_pc_pc_repository_pc_pc_Repository" = None, RepositoryComponent: "pcm_pc_pc_composition_pc_pc_AssemblyContext" = None):
        self.componentType = componentType
        self.pcm_pc_pc_repository_pc_pc_ImplementationComponentType = pcm_pc_pc_repository_pc_pc_ImplementationComponentType if pcm_pc_pc_repository_pc_pc_ImplementationComponentType is not None else set()
        self.pcm_pc_pc_repository_pc_pc_ImplementationComponentType207 = pcm_pc_pc_repository_pc_pc_ImplementationComponentType207 if pcm_pc_pc_repository_pc_pc_ImplementationComponentType207 is not None else set()
        
        pass
    @property
    def componentType(self):
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
    def pcm_pc_pc_repository_pc_pc_ImplementationComponentType207(self):
        return self.__pcm_pc_pc_repository_pc_pc_ImplementationComponentType207

    @pcm_pc_pc_repository_pc_pc_ImplementationComponentType207.setter
    def pcm_pc_pc_repository_pc_pc_ImplementationComponentType207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_ImplementationComponentType__pcm_pc_pc_repository_pc_pc_ImplementationComponentType207", None)
        self.__pcm_pc_pc_repository_pc_pc_ImplementationComponentType207 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableUsage208"):
                    opp_val = getattr(item, "VariableUsage208", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableUsage208", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableUsage208"):
                    opp_val = getattr(item, "VariableUsage208", None)
                    
                    setattr(item, "VariableUsage208", self)
                    

    def providedInterfacesHaveToConformToCompleteType(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement providedInterfacesHaveToConformToCompleteType method
        pass

    def ProvidedInterfaceHaveToConformToComponentType(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement ProvidedInterfaceHaveToConformToComponentType method
        pass

    def RequiredInterfacesHaveToConformToCompleteType(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement RequiredInterfacesHaveToConformToCompleteType method
        pass

class InfrastructureRequiredRole:

    pass
class InfrastructureProvidedRole:

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
class composition_pc_pc_EventChannelSourceConnector:

    pass
class EventGroup:

    pass
class DelegationConnector:

    pass
class pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector(DelegationConnector):

    pass
class pcm_pc_pc_composition_pc_pc_SourceDelegationConnector(DelegationConnector):

    pass
class pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector(DelegationConnector):

    pass
class pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector(DelegationConnector):

    def __init__(self, pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector68: "OperationRequiredRole" = None, pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector71: "composition_pc_pc_AssemblyContext" = None, pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector: "OperationRequiredRole" = None):
        self.pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector68 = pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector68
        self.pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector71 = pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector71
        self.pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector = pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector
        
        pass
    @property
    def pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector71(self):
        return self.__pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector71

    @pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector71.setter
    def pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector__pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector71", None)
        self.__pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_pc_pc_AssemblyContext72"):
                opp_val = getattr(old_value, "composition_pc_pc_AssemblyContext72", None)
                if opp_val == self:
                    setattr(old_value, "composition_pc_pc_AssemblyContext72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_pc_pc_AssemblyContext72"):
                opp_val = getattr(value, "composition_pc_pc_AssemblyContext72", None)
                setattr(value, "composition_pc_pc_AssemblyContext72", self)

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

    @property
    def pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector68(self):
        return self.__pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector68

    @pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector68.setter
    def pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector__pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector68", None)
        self.__pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationRequiredRole69"):
                opp_val = getattr(old_value, "OperationRequiredRole69", None)
                if opp_val == self:
                    setattr(old_value, "OperationRequiredRole69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationRequiredRole69"):
                opp_val = getattr(value, "OperationRequiredRole69", None)
                setattr(value, "OperationRequiredRole69", self)

    def RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

    def ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame method
        pass

    def RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector method
        pass

class pcm_pc_pc_composition_pc_pc_SinkDelegationConnector(DelegationConnector):

    pass
class pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector(DelegationConnector):

    pass
class pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector(DelegationConnector):

    def __init__(self, pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector: "OperationProvidedRole" = None, pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector61: "OperationProvidedRole" = None, pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector64: "composition_pc_pc_AssemblyContext" = None):
        self.pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector = pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector
        self.pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector61 = pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector61
        self.pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector64 = pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector64
        
        pass
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
    def pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector61(self):
        return self.__pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector61

    @pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector61.setter
    def pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector__pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector61", None)
        self.__pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationProvidedRole62"):
                opp_val = getattr(old_value, "OperationProvidedRole62", None)
                if opp_val == self:
                    setattr(old_value, "OperationProvidedRole62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationProvidedRole62"):
                opp_val = getattr(value, "OperationProvidedRole62", None)
                setattr(value, "OperationProvidedRole62", self)

    @property
    def pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector64(self):
        return self.__pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector64

    @pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector64.setter
    def pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector__pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector64", None)
        self.__pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_pc_pc_AssemblyContext65"):
                opp_val = getattr(old_value, "composition_pc_pc_AssemblyContext65", None)
                if opp_val == self:
                    setattr(old_value, "composition_pc_pc_AssemblyContext65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_pc_pc_AssemblyContext65"):
                opp_val = getattr(value, "composition_pc_pc_AssemblyContext65", None)
                setattr(value, "composition_pc_pc_AssemblyContext65", self)

    def ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame method
        pass

    def ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

class composition_pc_pc_AssemblyContext:

    pass
class pcm_pc_pc_composition_pc_pc_ResourceRequiredDelegationConnector:

    pass
class composition_pc_pc_Connector:

    pass
class composition_pc_pc_EventChannel:

    pass
class composition_pc_pc_ResourceRequiredDelegationConnector:

    pass
class pcm_pc_pc_entity_pc_pc_NamedElement:

    def __init__(self, entityName: str):
        self.entityName = entityName
        
        pass
    @property
    def entityName(self):
        return self.__entityName

    @entityName.setter
    def entityName(self, entityName: str):
        self.__entityName = entityName


class entity_pc_pc_InterfaceProvidingRequiringEntity:

    pass
class composition_pc_pc_ComposedStructure:

    pass
class pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity(entity_pc_pc_InterfaceProvidingRequiringEntity, composition_pc_pc_ComposedStructure):

    def __init__(self, ComposedStructure40: "pcm_pc_pc_composition_pc_pc_ResourceRequiredDelegationConnector" = None, ComposedStructure147: "pcm_pc_pc_composition_pc_pc_AssemblyContext" = None, ComposedStructure46: "pcm_pc_pc_composition_pc_pc_EventChannel" = None, ComposedStructure: "pcm_pc_pc_composition_pc_pc_Connector" = None):
        
        pass
    def ProvidedRolesMustBeBound(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement ProvidedRolesMustBeBound method
        pass

class entity_pc_pc_ResourceProvidedRole:

    pass
class entity_pc_pc_ResourceRequiredRole:

    pass
class RequiredRole:

    pass
class pcm_pc_pc_repository_pc_pc_SourceRole(RequiredRole):

    pass
class pcm_pc_pc_repository_pc_pc_InfrastructureRequiredRole(RequiredRole):

    pass
class pcm_pc_pc_repository_pc_pc_OperationRequiredRole(RequiredRole):

    pass
class entity_pc_pc_ResourceInterfaceRequiringEntity:

    pass
class entity_pc_pc_Entity:

    pass
class pcm_pc_pc_repository_pc_pc_CollectionDataType(repository_pc_pc_DataType, entity_pc_pc_Entity):

    pass
class pcm_pc_pc_repository_pc_pc_CompositeDataType(repository_pc_pc_DataType, entity_pc_pc_Entity):

    pass
class pcm_pc_pc_entity_pc_pc_InterfaceRequiringEntity(entity_pc_pc_ResourceInterfaceRequiringEntity, entity_pc_pc_Entity):

    pass
class Connector:

    pass
class pcm_pc_pc_composition_pc_pc_AssemblyEventConnector(Connector):

    pass
class pcm_pc_pc_composition_pc_pc_EventChannelSourceConnector(Connector):

    pass
class pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector(Connector):

    pass
class pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector(Connector):

    pass
class pcm_pc_pc_composition_pc_pc_AssemblyConnector(Connector):

    def __init__(self, pcm_pc_pc_composition_pc_pc_AssemblyConnector: "composition_pc_pc_AssemblyContext" = None, pcm_pc_pc_composition_pc_pc_AssemblyConnector76: "composition_pc_pc_AssemblyContext" = None, pcm_pc_pc_composition_pc_pc_AssemblyConnector79: "OperationProvidedRole" = None, pcm_pc_pc_composition_pc_pc_AssemblyConnector82: "OperationRequiredRole" = None):
        self.pcm_pc_pc_composition_pc_pc_AssemblyConnector = pcm_pc_pc_composition_pc_pc_AssemblyConnector
        self.pcm_pc_pc_composition_pc_pc_AssemblyConnector76 = pcm_pc_pc_composition_pc_pc_AssemblyConnector76
        self.pcm_pc_pc_composition_pc_pc_AssemblyConnector79 = pcm_pc_pc_composition_pc_pc_AssemblyConnector79
        self.pcm_pc_pc_composition_pc_pc_AssemblyConnector82 = pcm_pc_pc_composition_pc_pc_AssemblyConnector82
        
        pass
    @property
    def pcm_pc_pc_composition_pc_pc_AssemblyConnector79(self):
        return self.__pcm_pc_pc_composition_pc_pc_AssemblyConnector79

    @pcm_pc_pc_composition_pc_pc_AssemblyConnector79.setter
    def pcm_pc_pc_composition_pc_pc_AssemblyConnector79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_composition_pc_pc_AssemblyConnector__pcm_pc_pc_composition_pc_pc_AssemblyConnector79", None)
        self.__pcm_pc_pc_composition_pc_pc_AssemblyConnector79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationProvidedRole80"):
                opp_val = getattr(old_value, "OperationProvidedRole80", None)
                if opp_val == self:
                    setattr(old_value, "OperationProvidedRole80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationProvidedRole80"):
                opp_val = getattr(value, "OperationProvidedRole80", None)
                setattr(value, "OperationProvidedRole80", self)

    @property
    def pcm_pc_pc_composition_pc_pc_AssemblyConnector76(self):
        return self.__pcm_pc_pc_composition_pc_pc_AssemblyConnector76

    @pcm_pc_pc_composition_pc_pc_AssemblyConnector76.setter
    def pcm_pc_pc_composition_pc_pc_AssemblyConnector76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_composition_pc_pc_AssemblyConnector__pcm_pc_pc_composition_pc_pc_AssemblyConnector76", None)
        self.__pcm_pc_pc_composition_pc_pc_AssemblyConnector76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_pc_pc_AssemblyContext77"):
                opp_val = getattr(old_value, "composition_pc_pc_AssemblyContext77", None)
                if opp_val == self:
                    setattr(old_value, "composition_pc_pc_AssemblyContext77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_pc_pc_AssemblyContext77"):
                opp_val = getattr(value, "composition_pc_pc_AssemblyContext77", None)
                setattr(value, "composition_pc_pc_AssemblyContext77", self)

    @property
    def pcm_pc_pc_composition_pc_pc_AssemblyConnector82(self):
        return self.__pcm_pc_pc_composition_pc_pc_AssemblyConnector82

    @pcm_pc_pc_composition_pc_pc_AssemblyConnector82.setter
    def pcm_pc_pc_composition_pc_pc_AssemblyConnector82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_composition_pc_pc_AssemblyConnector__pcm_pc_pc_composition_pc_pc_AssemblyConnector82", None)
        self.__pcm_pc_pc_composition_pc_pc_AssemblyConnector82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationRequiredRole83"):
                opp_val = getattr(old_value, "OperationRequiredRole83", None)
                if opp_val == self:
                    setattr(old_value, "OperationRequiredRole83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationRequiredRole83"):
                opp_val = getattr(value, "OperationRequiredRole83", None)
                setattr(value, "OperationRequiredRole83", self)

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
            if hasattr(old_value, "composition_pc_pc_AssemblyContext74"):
                opp_val = getattr(old_value, "composition_pc_pc_AssemblyContext74", None)
                if opp_val == self:
                    setattr(old_value, "composition_pc_pc_AssemblyContext74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_pc_pc_AssemblyContext74"):
                opp_val = getattr(value, "composition_pc_pc_AssemblyContext74", None)
                setattr(value, "composition_pc_pc_AssemblyContext74", self)

    def AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch method
        pass

    def AssemblyConnectorsReferencedInterfacesMustMatch(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement AssemblyConnectorsReferencedInterfacesMustMatch method
        pass

    def AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch method
        pass

class pcm_pc_pc_composition_pc_pc_DelegationConnector(Connector):

    pass
class entity_pc_pc_NamedElement:

    pass
class Identifier:

    pass
class pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF(seff_pc_pc_ServiceEffectSpecification, Identifier, seff_pc_pc_ResourceDemandingBehaviour):

    pass
class pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour(Identifier):

    def __init__(self, bodyBehaviour_Loop338: "AbstractLoopAction" = None, branchBehaviour_BranchTransition: "AbstractBranchTransition" = None, resourceDemandingBehaviour_AbstractAction: set["AbstractAction"] = None):
        self.bodyBehaviour_Loop338 = bodyBehaviour_Loop338
        self.branchBehaviour_BranchTransition = branchBehaviour_BranchTransition
        self.resourceDemandingBehaviour_AbstractAction = resourceDemandingBehaviour_AbstractAction if resourceDemandingBehaviour_AbstractAction is not None else set()
        
        pass
    @property
    def bodyBehaviour_Loop338(self):
        return self.__bodyBehaviour_Loop338

    @bodyBehaviour_Loop338.setter
    def bodyBehaviour_Loop338(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour__bodyBehaviour_Loop338", None)
        self.__bodyBehaviour_Loop338 = value
        
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
        old_value = getattr(self, f"_pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour__branchBehaviour_BranchTransition", None)
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
        old_value = getattr(self, f"_pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour__resourceDemandingBehaviour_AbstractAction", None)
        self.__resourceDemandingBehaviour_AbstractAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractAction341"):
                    opp_val = getattr(item, "AbstractAction341", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractAction341", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractAction341"):
                    opp_val = getattr(item, "AbstractAction341", None)
                    
                    setattr(item, "AbstractAction341", self)
                    

    def ExactlyOneStartAction(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement ExactlyOneStartAction method
        pass

    def ExactlyOneStopAction(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement ExactlyOneStopAction method
        pass

    def EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor method
        pass

class pcm_pc_pc_entity_pc_pc_Entity(entity_pc_pc_NamedElement, Identifier):

    pass
class Role:

    pass
class pcm_pc_pc_repository_pc_pc_RequiredRole(Role):

    pass
class pcm_pc_pc_entity_pc_pc_ResourceRequiredRole(Role):

    pass
class pcm_pc_pc_repository_pc_pc_ProvidedRole(Role):

    pass
class pcm_pc_pc_entity_pc_pc_ResourceProvidedRole(Role):

    pass
class ProcessingResourceSpecification:

    pass
class CommunicationLinkResourceSpecification:

    pass
class Delay:

    pass
class ParametricResourceDemand:

    pass
class pcm_pc_pc_completions_pc_pc_NetworkDemandParametricResourceDemand(ParametricResourceDemand):

    pass
class ExternalCallAction:

    pass
class pcm_pc_pc_completions_pc_pc_DelegatingExternalCallAction(ExternalCallAction):

    pass
class Allocation:

    pass
class Completion:

    pass
class pcm_pc_pc_completions_pc_pc_CompletionRepository:

    pass
class pcm_pc_pc_completions_pc_pc_Completion(entity_pc_pc_ComposedProvidingRequiringEntity, repository_pc_pc_ImplementationComponentType):

    pass
class repository_pc_pc_RepositoryComponent:

    pass
class pcm_pc_pc_subsystem_pc_pc_SubSystem(entity_pc_pc_ComposedProvidingRequiringEntity, repository_pc_pc_RepositoryComponent):

    pass
class AllocationContext:

    pass
class pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification(Identifier):

    def __init__(self, failureProbability: float, communicationLinkResourceSpecifications_LinkingResource: "LinkingResource" = None, pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification: "CommunicationLinkResourceType" = None, communicationLinkResourceSpecification_latency_PCMRandomVariable: "PCMRandomVariable" = None, communicationLinkResourceSpecifcation_throughput_PCMRandomVariable: "PCMRandomVariable" = None):
        self.failureProbability = failureProbability
        self.communicationLinkResourceSpecifications_LinkingResource = communicationLinkResourceSpecifications_LinkingResource
        self.pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification = pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification
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
    def communicationLinkResourceSpecification_latency_PCMRandomVariable(self):
        return self.__communicationLinkResourceSpecification_latency_PCMRandomVariable

    @communicationLinkResourceSpecification_latency_PCMRandomVariable.setter
    def communicationLinkResourceSpecification_latency_PCMRandomVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification__communicationLinkResourceSpecification_latency_PCMRandomVariable", None)
        self.__communicationLinkResourceSpecification_latency_PCMRandomVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable480"):
                opp_val = getattr(old_value, "PCMRandomVariable480", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable480", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable480"):
                opp_val = getattr(value, "PCMRandomVariable480", None)
                setattr(value, "PCMRandomVariable480", self)

    @property
    def communicationLinkResourceSpecifications_LinkingResource(self):
        return self.__communicationLinkResourceSpecifications_LinkingResource

    @communicationLinkResourceSpecifications_LinkingResource.setter
    def communicationLinkResourceSpecifications_LinkingResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification__communicationLinkResourceSpecifications_LinkingResource", None)
        self.__communicationLinkResourceSpecifications_LinkingResource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LinkingResource476"):
                opp_val = getattr(old_value, "LinkingResource476", None)
                if opp_val == self:
                    setattr(old_value, "LinkingResource476", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LinkingResource476"):
                opp_val = getattr(value, "LinkingResource476", None)
                setattr(value, "LinkingResource476", self)

    @property
    def communicationLinkResourceSpecifcation_throughput_PCMRandomVariable(self):
        return self.__communicationLinkResourceSpecifcation_throughput_PCMRandomVariable

    @communicationLinkResourceSpecifcation_throughput_PCMRandomVariable.setter
    def communicationLinkResourceSpecifcation_throughput_PCMRandomVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification__communicationLinkResourceSpecifcation_throughput_PCMRandomVariable", None)
        self.__communicationLinkResourceSpecifcation_throughput_PCMRandomVariable = value
        
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
    def pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification(self):
        return self.__pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification

    @pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification.setter
    def pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification__pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification", None)
        self.__pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CommunicationLinkResourceType478"):
                opp_val = getattr(old_value, "CommunicationLinkResourceType478", None)
                if opp_val == self:
                    setattr(old_value, "CommunicationLinkResourceType478", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CommunicationLinkResourceType478"):
                opp_val = getattr(value, "CommunicationLinkResourceType478", None)
                setattr(value, "CommunicationLinkResourceType478", self)

class ResourceContainer:

    pass
class LinkingResource:

    pass
class pcm_pc_pc_resourceenvironment_pc_pc_ResourceEnvironment(NamedElement):

    pass
class pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification(Identifier):

    def __init__(self, MTTR: float, MTTF: float, requiredByContainer: bool, numberOfReplicas: int, pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification: "SchedulingPolicy" = None, pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification469: "ProcessingResourceType" = None, processingResourceSpecification_processingRate_PCMRandomVariable: "PCMRandomVariable" = None, activeResourceSpecifications_ResourceContainer: "ResourceContainer" = None):
        self.MTTR = MTTR
        self.MTTF = MTTF
        self.requiredByContainer = requiredByContainer
        self.numberOfReplicas = numberOfReplicas
        self.pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification = pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification
        self.pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification469 = pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification469
        self.processingResourceSpecification_processingRate_PCMRandomVariable = processingResourceSpecification_processingRate_PCMRandomVariable
        self.activeResourceSpecifications_ResourceContainer = activeResourceSpecifications_ResourceContainer
        
        pass
    @property
    def requiredByContainer(self):
        return self.__requiredByContainer

    @requiredByContainer.setter
    def requiredByContainer(self, requiredByContainer: bool):
        self.__requiredByContainer = requiredByContainer


    @property
    def MTTR(self):
        return self.__MTTR

    @MTTR.setter
    def MTTR(self, MTTR: float):
        self.__MTTR = MTTR


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
    def pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification(self):
        return self.__pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification

    @pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification.setter
    def pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification__pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification", None)
        self.__pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SchedulingPolicy467"):
                opp_val = getattr(old_value, "SchedulingPolicy467", None)
                if opp_val == self:
                    setattr(old_value, "SchedulingPolicy467", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SchedulingPolicy467"):
                opp_val = getattr(value, "SchedulingPolicy467", None)
                setattr(value, "SchedulingPolicy467", self)

    @property
    def processingResourceSpecification_processingRate_PCMRandomVariable(self):
        return self.__processingResourceSpecification_processingRate_PCMRandomVariable

    @processingResourceSpecification_processingRate_PCMRandomVariable.setter
    def processingResourceSpecification_processingRate_PCMRandomVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification__processingResourceSpecification_processingRate_PCMRandomVariable", None)
        self.__processingResourceSpecification_processingRate_PCMRandomVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable472"):
                opp_val = getattr(old_value, "PCMRandomVariable472", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable472", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable472"):
                opp_val = getattr(value, "PCMRandomVariable472", None)
                setattr(value, "PCMRandomVariable472", self)

    @property
    def pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification469(self):
        return self.__pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification469

    @pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification469.setter
    def pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification469(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification__pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification469", None)
        self.__pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification469 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcessingResourceType470"):
                opp_val = getattr(old_value, "ProcessingResourceType470", None)
                if opp_val == self:
                    setattr(old_value, "ProcessingResourceType470", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessingResourceType470"):
                opp_val = getattr(value, "ProcessingResourceType470", None)
                setattr(value, "ProcessingResourceType470", self)

    @property
    def activeResourceSpecifications_ResourceContainer(self):
        return self.__activeResourceSpecifications_ResourceContainer

    @activeResourceSpecifications_ResourceContainer.setter
    def activeResourceSpecifications_ResourceContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification__activeResourceSpecifications_ResourceContainer", None)
        self.__activeResourceSpecifications_ResourceContainer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceContainer474"):
                opp_val = getattr(old_value, "ResourceContainer474", None)
                if opp_val == self:
                    setattr(old_value, "ResourceContainer474", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceContainer474"):
                opp_val = getattr(value, "ResourceContainer474", None)
                setattr(value, "ResourceContainer474", self)

class ResourceEnvironment:

    pass
class pcm_pc_pc_system_pc_pc_System(entity_pc_pc_ComposedProvidingRequiringEntity, entity_pc_pc_Entity):

    def __init__(self, system_QoSAnnotations: set["QoSAnnotations"] = None):
        self.system_QoSAnnotations = system_QoSAnnotations if system_QoSAnnotations is not None else set()
        
        pass
    @property
    def system_QoSAnnotations(self):
        return self.__system_QoSAnnotations

    @system_QoSAnnotations.setter
    def system_QoSAnnotations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_system_pc_pc_System__system_QoSAnnotations", None)
        self.__system_QoSAnnotations = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QoSAnnotations450"):
                    opp_val = getattr(item, "QoSAnnotations450", None)
                    
                    if opp_val == self:
                        setattr(item, "QoSAnnotations450", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QoSAnnotations450"):
                    opp_val = getattr(item, "QoSAnnotations450", None)
                    
                    setattr(item, "QoSAnnotations450", self)
                    

    def SystemMustHaveAtLeastOneProvidedRole(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement SystemMustHaveAtLeastOneProvidedRole method
        pass

class ExternalFailureOccurrenceDescription:

    pass
class QoSAnnotations:

    pass
class SpecifiedExecutionTime:

    pass
class pcm_pc_pc_qos_performance_pc_pc_ComponentSpecifiedExecutionTime(SpecifiedExecutionTime):

    pass
class pcm_pc_pc_qos_performance_pc_pc_SystemSpecifiedExecutionTime(SpecifiedExecutionTime):

    def __init__(self):
        
        pass
    def SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem method
        pass

class pcm_pc_pc_qosannotations_pc_pc_SpecifiedOutputParameterAbstraction:

    pass
class SpecifiedQoSAnnotation:

    pass
class pcm_pc_pc_qos_performance_pc_pc_SpecifiedExecutionTime(SpecifiedQoSAnnotation):

    pass
class pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation(SpecifiedQoSAnnotation):

    def __init__(self, specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription: set["ExternalFailureOccurrenceDescription"] = None, SpecifiedQoSAnnotation: "pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations" = None):
        self.specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription = specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription if specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription is not None else set()
        
        pass
    @property
    def specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription(self):
        return self.__specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription

    @specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription.setter
    def specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation__specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription", None)
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
                    

    def SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1 method
        pass

    def MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed method
        pass

    def SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem method
        pass

class System:

    pass
class pcm_pc_pc_qosannotations_pc_pc_SpecifiedQoSAnnotation:

    pass
class pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction(AbstractInternalControlFlowAction):

    def __init__(self, pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction: "seff_reliability_pc_pc_RecoveryActionBehaviour" = None, recoveryAction__RecoveryActionBehaviour: set["seff_reliability_pc_pc_RecoveryActionBehaviour"] = None, AbstractInternalControlFlowAction405: "pcm_pc_pc_seff_performance_pc_pc_ResourceCall" = None, AbstractInternalControlFlowAction418: "pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand" = None, AbstractInternalControlFlowAction: "pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall" = None):
        self.pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction = pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction
        self.recoveryAction__RecoveryActionBehaviour = recoveryAction__RecoveryActionBehaviour if recoveryAction__RecoveryActionBehaviour is not None else set()
        
        pass
    @property
    def recoveryAction__RecoveryActionBehaviour(self):
        return self.__recoveryAction__RecoveryActionBehaviour

    @recoveryAction__RecoveryActionBehaviour.setter
    def recoveryAction__RecoveryActionBehaviour(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction__recoveryAction__RecoveryActionBehaviour", None)
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
    def pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction(self):
        return self.__pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction

    @pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction.setter
    def pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction__pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction", None)
        self.__pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff_reliability_pc_pc_RecoveryActionBehaviour422"):
                opp_val = getattr(old_value, "seff_reliability_pc_pc_RecoveryActionBehaviour422", None)
                if opp_val == self:
                    setattr(old_value, "seff_reliability_pc_pc_RecoveryActionBehaviour422", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff_reliability_pc_pc_RecoveryActionBehaviour422"):
                opp_val = getattr(value, "seff_reliability_pc_pc_RecoveryActionBehaviour422", None)
                setattr(value, "seff_reliability_pc_pc_RecoveryActionBehaviour422", self)

    def PrimaryBehaviourOfRecoveryActionMustBeSet(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement PrimaryBehaviourOfRecoveryActionMustBeSet method
        pass

class seff_reliability_pc_pc_RecoveryAction:

    pass
class seff_reliability_pc_pc_RecoveryActionBehaviour:

    pass
class pcm_pc_pc_seff_performance_pc_pc_ResourceCall(CallAction):

    def __init__(self, resourceCall__Action: "AbstractInternalControlFlowAction" = None, pcm_pc_pc_seff_performance_pc_pc_ResourceCall: "entity_pc_pc_ResourceRequiredRole" = None, pcm_pc_pc_seff_performance_pc_pc_ResourceCall409: "ResourceSignature" = None, resourceCall__PCMRandomVariable: "PCMRandomVariable" = None, CallAction: "pcm_pc_pc_parameter_pc_pc_VariableUsage" = None):
        self.resourceCall__Action = resourceCall__Action
        self.pcm_pc_pc_seff_performance_pc_pc_ResourceCall = pcm_pc_pc_seff_performance_pc_pc_ResourceCall
        self.pcm_pc_pc_seff_performance_pc_pc_ResourceCall409 = pcm_pc_pc_seff_performance_pc_pc_ResourceCall409
        self.resourceCall__PCMRandomVariable = resourceCall__PCMRandomVariable
        
        pass
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
            if hasattr(old_value, "entity_pc_pc_ResourceRequiredRole407"):
                opp_val = getattr(old_value, "entity_pc_pc_ResourceRequiredRole407", None)
                if opp_val == self:
                    setattr(old_value, "entity_pc_pc_ResourceRequiredRole407", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entity_pc_pc_ResourceRequiredRole407"):
                opp_val = getattr(value, "entity_pc_pc_ResourceRequiredRole407", None)
                setattr(value, "entity_pc_pc_ResourceRequiredRole407", self)

    @property
    def pcm_pc_pc_seff_performance_pc_pc_ResourceCall409(self):
        return self.__pcm_pc_pc_seff_performance_pc_pc_ResourceCall409

    @pcm_pc_pc_seff_performance_pc_pc_ResourceCall409.setter
    def pcm_pc_pc_seff_performance_pc_pc_ResourceCall409(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_performance_pc_pc_ResourceCall__pcm_pc_pc_seff_performance_pc_pc_ResourceCall409", None)
        self.__pcm_pc_pc_seff_performance_pc_pc_ResourceCall409 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceSignature410"):
                opp_val = getattr(old_value, "ResourceSignature410", None)
                if opp_val == self:
                    setattr(old_value, "ResourceSignature410", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceSignature410"):
                opp_val = getattr(value, "ResourceSignature410", None)
                setattr(value, "ResourceSignature410", self)

    @property
    def resourceCall__PCMRandomVariable(self):
        return self.__resourceCall__PCMRandomVariable

    @resourceCall__PCMRandomVariable.setter
    def resourceCall__PCMRandomVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_performance_pc_pc_ResourceCall__resourceCall__PCMRandomVariable", None)
        self.__resourceCall__PCMRandomVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable412"):
                opp_val = getattr(old_value, "PCMRandomVariable412", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable412", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable412"):
                opp_val = getattr(value, "PCMRandomVariable412", None)
                setattr(value, "PCMRandomVariable412", self)

    @property
    def resourceCall__Action(self):
        return self.__resourceCall__Action

    @resourceCall__Action.setter
    def resourceCall__Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_performance_pc_pc_ResourceCall__resourceCall__Action", None)
        self.__resourceCall__Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractInternalControlFlowAction405"):
                opp_val = getattr(old_value, "AbstractInternalControlFlowAction405", None)
                if opp_val == self:
                    setattr(old_value, "AbstractInternalControlFlowAction405", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractInternalControlFlowAction405"):
                opp_val = getattr(value, "AbstractInternalControlFlowAction405", None)
                setattr(value, "AbstractInternalControlFlowAction405", self)

    def ResourceRequiredRoleMustBeReferencedByComponent(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement ResourceRequiredRoleMustBeReferencedByComponent method
        pass

    def SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

    def ResourceSignatureBelongsToResourceRequiredRole(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement ResourceSignatureBelongsToResourceRequiredRole method
        pass

class pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour(seff_reliability_pc_pc_FailureHandlingEntity, seff_pc_pc_ResourceDemandingBehaviour):

    def __init__(self, pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour: set["seff_reliability_pc_pc_RecoveryActionBehaviour"] = None, recoveryActionBehaviours__RecoveryAction: "seff_reliability_pc_pc_RecoveryAction" = None):
        self.pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour = pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour if pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour is not None else set()
        self.recoveryActionBehaviours__RecoveryAction = recoveryActionBehaviours__RecoveryAction
        
        pass
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
                    

    @property
    def recoveryActionBehaviours__RecoveryAction(self):
        return self.__recoveryActionBehaviours__RecoveryAction

    @recoveryActionBehaviours__RecoveryAction.setter
    def recoveryActionBehaviours__RecoveryAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour__recoveryActionBehaviours__RecoveryAction", None)
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

    def RecoveryActionBehaviourHasOnlyOnePredecessor(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement RecoveryActionBehaviourHasOnlyOnePredecessor method
        pass

    def RecoveryActionBehaviourIsNotSuccessorOfItself(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement RecoveryActionBehaviourIsNotSuccessorOfItself method
        pass

    def SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes method
        pass

class pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand:

    def __init__(self, parametricResourceDemand_PCMRandomVariable: "PCMRandomVariable" = None, pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand: "ProcessingResourceType" = None, resourceDemand_Action: "AbstractInternalControlFlowAction" = None):
        self.parametricResourceDemand_PCMRandomVariable = parametricResourceDemand_PCMRandomVariable
        self.pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand = pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand
        self.resourceDemand_Action = resourceDemand_Action
        
        pass
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
            if hasattr(old_value, "ProcessingResourceType416"):
                opp_val = getattr(old_value, "ProcessingResourceType416", None)
                if opp_val == self:
                    setattr(old_value, "ProcessingResourceType416", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessingResourceType416"):
                opp_val = getattr(value, "ProcessingResourceType416", None)
                setattr(value, "ProcessingResourceType416", self)

    @property
    def parametricResourceDemand_PCMRandomVariable(self):
        return self.__parametricResourceDemand_PCMRandomVariable

    @parametricResourceDemand_PCMRandomVariable.setter
    def parametricResourceDemand_PCMRandomVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand__parametricResourceDemand_PCMRandomVariable", None)
        self.__parametricResourceDemand_PCMRandomVariable = value
        
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

    @property
    def resourceDemand_Action(self):
        return self.__resourceDemand_Action

    @resourceDemand_Action.setter
    def resourceDemand_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand__resourceDemand_Action", None)
        self.__resourceDemand_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractInternalControlFlowAction418"):
                opp_val = getattr(old_value, "AbstractInternalControlFlowAction418", None)
                if opp_val == self:
                    setattr(old_value, "AbstractInternalControlFlowAction418", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractInternalControlFlowAction418"):
                opp_val = getattr(value, "AbstractInternalControlFlowAction418", None)
                setattr(value, "AbstractInternalControlFlowAction418", self)

    def DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

class pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall(CallAction):

    def __init__(self, pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall: "InfrastructureSignature" = None, infrastructureCall__PCMRandomVariable: "PCMRandomVariable" = None, infrastructureCall__Action: "AbstractInternalControlFlowAction" = None, pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall402: "InfrastructureRequiredRole" = None, CallAction: "pcm_pc_pc_parameter_pc_pc_VariableUsage" = None):
        self.pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall = pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall
        self.infrastructureCall__PCMRandomVariable = infrastructureCall__PCMRandomVariable
        self.infrastructureCall__Action = infrastructureCall__Action
        self.pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall402 = pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall402
        
        pass
    @property
    def infrastructureCall__PCMRandomVariable(self):
        return self.__infrastructureCall__PCMRandomVariable

    @infrastructureCall__PCMRandomVariable.setter
    def infrastructureCall__PCMRandomVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall__infrastructureCall__PCMRandomVariable", None)
        self.__infrastructureCall__PCMRandomVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable399"):
                opp_val = getattr(old_value, "PCMRandomVariable399", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable399", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable399"):
                opp_val = getattr(value, "PCMRandomVariable399", None)
                setattr(value, "PCMRandomVariable399", self)

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
            if hasattr(old_value, "InfrastructureSignature397"):
                opp_val = getattr(old_value, "InfrastructureSignature397", None)
                if opp_val == self:
                    setattr(old_value, "InfrastructureSignature397", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InfrastructureSignature397"):
                opp_val = getattr(value, "InfrastructureSignature397", None)
                setattr(value, "InfrastructureSignature397", self)

    @property
    def infrastructureCall__Action(self):
        return self.__infrastructureCall__Action

    @infrastructureCall__Action.setter
    def infrastructureCall__Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall__infrastructureCall__Action", None)
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
    def pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall402(self):
        return self.__pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall402

    @pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall402.setter
    def pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall402(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall__pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall402", None)
        self.__pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall402 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InfrastructureRequiredRole403"):
                opp_val = getattr(old_value, "InfrastructureRequiredRole403", None)
                if opp_val == self:
                    setattr(old_value, "InfrastructureRequiredRole403", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InfrastructureRequiredRole403"):
                opp_val = getattr(value, "InfrastructureRequiredRole403", None)
                setattr(value, "InfrastructureRequiredRole403", self)

    def ReferencedRequiredRoleMustBeRequiredByComponent(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement ReferencedRequiredRoleMustBeRequiredByComponent method
        pass

    def SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction method
        pass

    def SignatureMustBelongToUsedRequiredRole(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement SignatureMustBelongToUsedRequiredRole method
        pass

class pcm_pc_pc_seff_pc_pc_AcquireAction(AbstractInternalControlFlowAction):

    def __init__(self, timeout: bool, timeoutValue: float, pcm_pc_pc_seff_pc_pc_AcquireAction: "PassiveResource" = None, AbstractInternalControlFlowAction405: "pcm_pc_pc_seff_performance_pc_pc_ResourceCall" = None, AbstractInternalControlFlowAction418: "pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand" = None, AbstractInternalControlFlowAction: "pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall" = None):
        self.timeout = timeout
        self.timeoutValue = timeoutValue
        self.pcm_pc_pc_seff_pc_pc_AcquireAction = pcm_pc_pc_seff_pc_pc_AcquireAction
        
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
    def pcm_pc_pc_seff_pc_pc_AcquireAction(self):
        return self.__pcm_pc_pc_seff_pc_pc_AcquireAction

    @pcm_pc_pc_seff_pc_pc_AcquireAction.setter
    def pcm_pc_pc_seff_pc_pc_AcquireAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_pc_pc_AcquireAction__pcm_pc_pc_seff_pc_pc_AcquireAction", None)
        self.__pcm_pc_pc_seff_pc_pc_AcquireAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PassiveResource380"):
                opp_val = getattr(old_value, "PassiveResource380", None)
                if opp_val == self:
                    setattr(old_value, "PassiveResource380", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PassiveResource380"):
                opp_val = getattr(value, "PassiveResource380", None)
                setattr(value, "PassiveResource380", self)

    def TimeoutValueOfAcquireActionMustNotBeNegative(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement TimeoutValueOfAcquireActionMustNotBeNegative method
        pass

class pcm_pc_pc_seff_pc_pc_ProbabilisticBranchTransition(AbstractBranchTransition):

    def __init__(self, branchProbability: float, AbstractBranchTransition: "pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour" = None, AbstractBranchTransition348: "pcm_pc_pc_seff_pc_pc_BranchAction" = None):
        self.branchProbability = branchProbability
        
        pass
    @property
    def branchProbability(self):
        return self.__branchProbability

    @branchProbability.setter
    def branchProbability(self, branchProbability: float):
        self.__branchProbability = branchProbability


class pcm_pc_pc_seff_pc_pc_InternalAction(AbstractInternalControlFlowAction):

    def __init__(self, internalAction__InternalFailureOccurrenceDescription: set["InternalFailureOccurrenceDescription"] = None, AbstractInternalControlFlowAction405: "pcm_pc_pc_seff_performance_pc_pc_ResourceCall" = None, AbstractInternalControlFlowAction418: "pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand" = None, AbstractInternalControlFlowAction: "pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall" = None):
        self.internalAction__InternalFailureOccurrenceDescription = internalAction__InternalFailureOccurrenceDescription if internalAction__InternalFailureOccurrenceDescription is not None else set()
        
        pass
    @property
    def internalAction__InternalFailureOccurrenceDescription(self):
        return self.__internalAction__InternalFailureOccurrenceDescription

    @internalAction__InternalFailureOccurrenceDescription.setter
    def internalAction__InternalFailureOccurrenceDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_seff_pc_pc_InternalAction__internalAction__InternalFailureOccurrenceDescription", None)
        self.__internalAction__InternalFailureOccurrenceDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InternalFailureOccurrenceDescription395"):
                    opp_val = getattr(item, "InternalFailureOccurrenceDescription395", None)
                    
                    if opp_val == self:
                        setattr(item, "InternalFailureOccurrenceDescription395", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InternalFailureOccurrenceDescription395"):
                    opp_val = getattr(item, "InternalFailureOccurrenceDescription395", None)
                    
                    setattr(item, "InternalFailureOccurrenceDescription395", self)
                    

    def MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed method
        pass

    def SumOfInternalActionFailureProbabilitiesMustNotExceed1(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement SumOfInternalActionFailureProbabilitiesMustNotExceed1 method
        pass

class seff_pc_pc_AbstractInternalControlFlowAction:

    pass
class seff_pc_pc_CallAction:

    pass
class pcm_pc_pc_seff_pc_pc_EmitEventAction(seff_pc_pc_AbstractAction, seff_pc_pc_CallAction):

    pass
class pcm_pc_pc_seff_pc_pc_InternalCallAction(seff_pc_pc_AbstractInternalControlFlowAction, seff_pc_pc_CallAction):

    pass
class pcm_pc_pc_seff_pc_pc_SetVariableAction(AbstractInternalControlFlowAction):

    pass
class pcm_pc_pc_seff_pc_pc_GuardedBranchTransition(AbstractBranchTransition):

    pass
class OpenWorkload:

    pass
class Loop:

    pass
class composition_pc_pc_AssemblyEventConnector:

    pass
class composition_pc_pc_EventChannelSinkConnector:

    pass
class qos_performance_pc_pc_SpecifiedExecutionTime:

    pass
class ProvidedRole:

    pass
class pcm_pc_pc_repository_pc_pc_OperationProvidedRole(ProvidedRole):

    pass
class pcm_pc_pc_repository_pc_pc_InfrastructureProvidedRole(ProvidedRole):

    pass
class pcm_pc_pc_repository_pc_pc_SinkRole(ProvidedRole):

    pass
class Entity:

    pass
class pcm_pc_pc_composition_pc_pc_ComposedStructure(Entity):

    def __init__(self, parentStructure_ResourceRequiredDelegationConnector: set["composition_pc_pc_ResourceRequiredDelegationConnector"] = None, parentStructure__EventChannel: set["composition_pc_pc_EventChannel"] = None, parentStructure__Connector: set["composition_pc_pc_Connector"] = None, parentStructure__AssemblyContext: set["composition_pc_pc_AssemblyContext"] = None):
        self.parentStructure_ResourceRequiredDelegationConnector = parentStructure_ResourceRequiredDelegationConnector if parentStructure_ResourceRequiredDelegationConnector is not None else set()
        self.parentStructure__EventChannel = parentStructure__EventChannel if parentStructure__EventChannel is not None else set()
        self.parentStructure__Connector = parentStructure__Connector if parentStructure__Connector is not None else set()
        self.parentStructure__AssemblyContext = parentStructure__AssemblyContext if parentStructure__AssemblyContext is not None else set()
        
        pass
    @property
    def parentStructure__EventChannel(self):
        return self.__parentStructure__EventChannel

    @parentStructure__EventChannel.setter
    def parentStructure__EventChannel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_composition_pc_pc_ComposedStructure__parentStructure__EventChannel", None)
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
    def parentStructure_ResourceRequiredDelegationConnector(self):
        return self.__parentStructure_ResourceRequiredDelegationConnector

    @parentStructure_ResourceRequiredDelegationConnector.setter
    def parentStructure_ResourceRequiredDelegationConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_composition_pc_pc_ComposedStructure__parentStructure_ResourceRequiredDelegationConnector", None)
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
    def parentStructure__Connector(self):
        return self.__parentStructure__Connector

    @parentStructure__Connector.setter
    def parentStructure__Connector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_composition_pc_pc_ComposedStructure__parentStructure__Connector", None)
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
    def parentStructure__AssemblyContext(self):
        return self.__parentStructure__AssemblyContext

    @parentStructure__AssemblyContext.setter
    def parentStructure__AssemblyContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_composition_pc_pc_ComposedStructure__parentStructure__AssemblyContext", None)
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
                    

    def MultipleConnectorsConstraint(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement MultipleConnectorsConstraint method
        pass

    def MultipleConnectorsConstraintForAssemblyConnectors(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement MultipleConnectorsConstraintForAssemblyConnectors method
        pass

class pcm_pc_pc_resourceenvironment_pc_pc_LinkingResource(Entity):

    pass
class pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour(Entity):

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
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour__scenarioBehaviour_AbstractUserAction", None)
        self.__scenarioBehaviour_AbstractUserAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractUserAction182"):
                    opp_val = getattr(item, "AbstractUserAction182", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractUserAction182", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractUserAction182"):
                    opp_val = getattr(item, "AbstractUserAction182", None)
                    
                    setattr(item, "AbstractUserAction182", self)
                    

    @property
    def scenarioBehaviour_UsageScenario(self):
        return self.__scenarioBehaviour_UsageScenario

    @scenarioBehaviour_UsageScenario.setter
    def scenarioBehaviour_UsageScenario(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour__scenarioBehaviour_UsageScenario", None)
        self.__scenarioBehaviour_UsageScenario = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UsageScenario177"):
                opp_val = getattr(old_value, "UsageScenario177", None)
                if opp_val == self:
                    setattr(old_value, "UsageScenario177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UsageScenario177"):
                opp_val = getattr(value, "UsageScenario177", None)
                setattr(value, "UsageScenario177", self)

    @property
    def branchedBehaviour_BranchTransition(self):
        return self.__branchedBehaviour_BranchTransition

    @branchedBehaviour_BranchTransition.setter
    def branchedBehaviour_BranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour__branchedBehaviour_BranchTransition", None)
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
    def bodyBehaviour_Loop(self):
        return self.__bodyBehaviour_Loop

    @bodyBehaviour_Loop.setter
    def bodyBehaviour_Loop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour__bodyBehaviour_Loop", None)
        self.__bodyBehaviour_Loop = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Loop180"):
                opp_val = getattr(old_value, "Loop180", None)
                if opp_val == self:
                    setattr(old_value, "Loop180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Loop180"):
                opp_val = getattr(value, "Loop180", None)
                setattr(value, "Loop180", self)

    def Exactlyonestart(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement Exactlyonestart method
        pass

    def EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor method
        pass

    def Exactlyonestop(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement Exactlyonestop method
        pass

class pcm_pc_pc_allocation_pc_pc_AllocationContext(Entity):

    def __init__(self, pcm_pc_pc_allocation_pc_pc_AllocationContext: "ResourceContainer" = None, pcm_pc_pc_allocation_pc_pc_AllocationContext486: "composition_pc_pc_AssemblyContext" = None, pcm_pc_pc_allocation_pc_pc_AllocationContext490: "composition_pc_pc_EventChannel" = None, allocationContexts_Allocation: "Allocation" = None):
        self.pcm_pc_pc_allocation_pc_pc_AllocationContext = pcm_pc_pc_allocation_pc_pc_AllocationContext
        self.pcm_pc_pc_allocation_pc_pc_AllocationContext486 = pcm_pc_pc_allocation_pc_pc_AllocationContext486
        self.pcm_pc_pc_allocation_pc_pc_AllocationContext490 = pcm_pc_pc_allocation_pc_pc_AllocationContext490
        self.allocationContexts_Allocation = allocationContexts_Allocation
        
        pass
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
            if hasattr(old_value, "ResourceContainer484"):
                opp_val = getattr(old_value, "ResourceContainer484", None)
                if opp_val == self:
                    setattr(old_value, "ResourceContainer484", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceContainer484"):
                opp_val = getattr(value, "ResourceContainer484", None)
                setattr(value, "ResourceContainer484", self)

    @property
    def allocationContexts_Allocation(self):
        return self.__allocationContexts_Allocation

    @allocationContexts_Allocation.setter
    def allocationContexts_Allocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_allocation_pc_pc_AllocationContext__allocationContexts_Allocation", None)
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
    def pcm_pc_pc_allocation_pc_pc_AllocationContext490(self):
        return self.__pcm_pc_pc_allocation_pc_pc_AllocationContext490

    @pcm_pc_pc_allocation_pc_pc_AllocationContext490.setter
    def pcm_pc_pc_allocation_pc_pc_AllocationContext490(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_allocation_pc_pc_AllocationContext__pcm_pc_pc_allocation_pc_pc_AllocationContext490", None)
        self.__pcm_pc_pc_allocation_pc_pc_AllocationContext490 = value
        
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
    def pcm_pc_pc_allocation_pc_pc_AllocationContext486(self):
        return self.__pcm_pc_pc_allocation_pc_pc_AllocationContext486

    @pcm_pc_pc_allocation_pc_pc_AllocationContext486.setter
    def pcm_pc_pc_allocation_pc_pc_AllocationContext486(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_allocation_pc_pc_AllocationContext__pcm_pc_pc_allocation_pc_pc_AllocationContext486", None)
        self.__pcm_pc_pc_allocation_pc_pc_AllocationContext486 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_pc_pc_AssemblyContext487"):
                opp_val = getattr(old_value, "composition_pc_pc_AssemblyContext487", None)
                if opp_val == self:
                    setattr(old_value, "composition_pc_pc_AssemblyContext487", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_pc_pc_AssemblyContext487"):
                opp_val = getattr(value, "composition_pc_pc_AssemblyContext487", None)
                setattr(value, "composition_pc_pc_AssemblyContext487", self)

    def OneAssemblyContextOrOneEventChannelShouldBeReferred(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement OneAssemblyContextOrOneEventChannelShouldBeReferred method
        pass

class pcm_pc_pc_entity_pc_pc_ResourceInterfaceRequiringEntity(Entity):

    pass
class pcm_pc_pc_seff_reliability_pc_pc_FailureHandlingEntity(Entity):

    pass
class pcm_pc_pc_seff_pc_pc_AbstractAction(Entity):

    pass
class pcm_pc_pc_resourcetype_pc_pc_ResourceInterface(Entity):

    pass
class pcm_pc_pc_reliability_pc_pc_FailureType(Entity):

    pass
class pcm_pc_pc_allocation_pc_pc_Allocation(Entity):

    def __init__(self, pcm_pc_pc_allocation_pc_pc_Allocation: "ResourceEnvironment" = None, pcm_pc_pc_allocation_pc_pc_Allocation494: "System" = None, allocation_AllocationContext: set["AllocationContext"] = None):
        self.pcm_pc_pc_allocation_pc_pc_Allocation = pcm_pc_pc_allocation_pc_pc_Allocation
        self.pcm_pc_pc_allocation_pc_pc_Allocation494 = pcm_pc_pc_allocation_pc_pc_Allocation494
        self.allocation_AllocationContext = allocation_AllocationContext if allocation_AllocationContext is not None else set()
        
        pass
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
            if hasattr(old_value, "ResourceEnvironment492"):
                opp_val = getattr(old_value, "ResourceEnvironment492", None)
                if opp_val == self:
                    setattr(old_value, "ResourceEnvironment492", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceEnvironment492"):
                opp_val = getattr(value, "ResourceEnvironment492", None)
                setattr(value, "ResourceEnvironment492", self)

    @property
    def pcm_pc_pc_allocation_pc_pc_Allocation494(self):
        return self.__pcm_pc_pc_allocation_pc_pc_Allocation494

    @pcm_pc_pc_allocation_pc_pc_Allocation494.setter
    def pcm_pc_pc_allocation_pc_pc_Allocation494(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_allocation_pc_pc_Allocation__pcm_pc_pc_allocation_pc_pc_Allocation494", None)
        self.__pcm_pc_pc_allocation_pc_pc_Allocation494 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "System495"):
                opp_val = getattr(old_value, "System495", None)
                if opp_val == self:
                    setattr(old_value, "System495", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "System495"):
                opp_val = getattr(value, "System495", None)
                setattr(value, "System495", self)

    @property
    def allocation_AllocationContext(self):
        return self.__allocation_AllocationContext

    @allocation_AllocationContext.setter
    def allocation_AllocationContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_allocation_pc_pc_Allocation__allocation_AllocationContext", None)
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
                    

    def CommunicatingServersHaveToBeConnectedByLinkingResource(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement CommunicatingServersHaveToBeConnectedByLinkingResource method
        pass

    def EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce method
        pass

class pcm_pc_pc_composition_pc_pc_EventChannel(Entity):

    pass
class pcm_pc_pc_repository_pc_pc_Signature(Entity):

    pass
class pcm_pc_pc_repository_pc_pc_Repository(Entity):

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
    def repository__DataType(self):
        return self.__repository__DataType

    @repository__DataType.setter
    def repository__DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_Repository__repository__DataType", None)
        self.__repository__DataType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataType224"):
                    opp_val = getattr(item, "DataType224", None)
                    
                    if opp_val == self:
                        setattr(item, "DataType224", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataType224"):
                    opp_val = getattr(item, "DataType224", None)
                    
                    setattr(item, "DataType224", self)
                    

    @property
    def repository__RepositoryComponent(self):
        return self.__repository__RepositoryComponent

    @repository__RepositoryComponent.setter
    def repository__RepositoryComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_Repository__repository__RepositoryComponent", None)
        self.__repository__RepositoryComponent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RepositoryComponent220"):
                    opp_val = getattr(item, "RepositoryComponent220", None)
                    
                    if opp_val == self:
                        setattr(item, "RepositoryComponent220", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RepositoryComponent220"):
                    opp_val = getattr(item, "RepositoryComponent220", None)
                    
                    setattr(item, "RepositoryComponent220", self)
                    

    @property
    def repository__FailureType(self):
        return self.__repository__FailureType

    @repository__FailureType.setter
    def repository__FailureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_Repository__repository__FailureType", None)
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
    def repository__Interface(self):
        return self.__repository__Interface

    @repository__Interface.setter
    def repository__Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_Repository__repository__Interface", None)
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
                    

class pcm_pc_pc_resourceenvironment_pc_pc_ResourceContainer(Entity):

    pass
class pcm_pc_pc_resourcetype_pc_pc_ResourceSignature(Entity):

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
    def resourceSignatures__ResourceInterface(self):
        return self.__resourceSignatures__ResourceInterface

    @resourceSignatures__ResourceInterface.setter
    def resourceSignatures__ResourceInterface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_resourcetype_pc_pc_ResourceSignature__resourceSignatures__ResourceInterface", None)
        self.__resourceSignatures__ResourceInterface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceInterface282"):
                opp_val = getattr(old_value, "ResourceInterface282", None)
                if opp_val == self:
                    setattr(old_value, "ResourceInterface282", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceInterface282"):
                opp_val = getattr(value, "ResourceInterface282", None)
                setattr(value, "ResourceInterface282", self)

    @property
    def resourceSignature__Parameter(self):
        return self.__resourceSignature__Parameter

    @resourceSignature__Parameter.setter
    def resourceSignature__Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_resourcetype_pc_pc_ResourceSignature__resourceSignature__Parameter", None)
        self.__resourceSignature__Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Parameter280"):
                opp_val = getattr(old_value, "Parameter280", None)
                if opp_val == self:
                    setattr(old_value, "Parameter280", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Parameter280"):
                opp_val = getattr(value, "Parameter280", None)
                setattr(value, "Parameter280", self)

class pcm_pc_pc_composition_pc_pc_AssemblyContext(Entity):

    pass
class pcm_pc_pc_repository_pc_pc_Interface(Entity):

    def __init__(self, pcm_pc_pc_repository_pc_pc_Interface: set["Interface"] = None, pcm_pc_pc_repository_pc_pc_Interface228: set["Protocol"] = None, interface_RequiredCharacterisation: set["RequiredCharacterisation"] = None, interfaces__Repository: "Repository" = None):
        self.pcm_pc_pc_repository_pc_pc_Interface = pcm_pc_pc_repository_pc_pc_Interface if pcm_pc_pc_repository_pc_pc_Interface is not None else set()
        self.pcm_pc_pc_repository_pc_pc_Interface228 = pcm_pc_pc_repository_pc_pc_Interface228 if pcm_pc_pc_repository_pc_pc_Interface228 is not None else set()
        self.interface_RequiredCharacterisation = interface_RequiredCharacterisation if interface_RequiredCharacterisation is not None else set()
        self.interfaces__Repository = interfaces__Repository
        
        pass
    @property
    def pcm_pc_pc_repository_pc_pc_Interface228(self):
        return self.__pcm_pc_pc_repository_pc_pc_Interface228

    @pcm_pc_pc_repository_pc_pc_Interface228.setter
    def pcm_pc_pc_repository_pc_pc_Interface228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_Interface__pcm_pc_pc_repository_pc_pc_Interface228", None)
        self.__pcm_pc_pc_repository_pc_pc_Interface228 = value if value is not None else set()
        
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
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_Interface__interfaces__Repository", None)
        self.__interfaces__Repository = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Repository231"):
                opp_val = getattr(old_value, "Repository231", None)
                if opp_val == self:
                    setattr(old_value, "Repository231", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Repository231"):
                opp_val = getattr(value, "Repository231", None)
                setattr(value, "Repository231", self)

    @property
    def interface_RequiredCharacterisation(self):
        return self.__interface_RequiredCharacterisation

    @interface_RequiredCharacterisation.setter
    def interface_RequiredCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_repository_pc_pc_Interface__interface_RequiredCharacterisation", None)
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
                if hasattr(item, "Interface226"):
                    opp_val = getattr(item, "Interface226", None)
                    
                    if opp_val == self:
                        setattr(item, "Interface226", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Interface226"):
                    opp_val = getattr(item, "Interface226", None)
                    
                    setattr(item, "Interface226", self)
                    

    def NoProtocolTypeIDUsedTwice(self, pcm_pc_pc_context, pcm_pc_pc_diagnostics) :
        # TODO: Implement NoProtocolTypeIDUsedTwice method
        pass

class pcm_pc_pc_seff_pc_pc_AbstractBranchTransition(Entity):

    pass
class pcm_pc_pc_usagemodel_pc_pc_UsageScenario(Entity):

    pass
class pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction(Entity):

    pass
class pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingEntity(Entity):

    pass
class pcm_pc_pc_resourcetype_pc_pc_SchedulingPolicy(Entity):

    pass
class pcm_pc_pc_repository_pc_pc_PassiveResource(Entity):

    pass
class pcm_pc_pc_repository_pc_pc_Role(Entity):

    pass
class pcm_pc_pc_composition_pc_pc_Connector(Entity):

    pass
class pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations(Entity):

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
        old_value = getattr(self, f"_pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations__qosAnnotations_System", None)
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
        old_value = getattr(self, f"_pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations__qosAnnotations_SpecifiedOutputParameterAbstraction", None)
        self.__qosAnnotations_SpecifiedOutputParameterAbstraction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SpecifiedOutputParameterAbstraction432"):
                    opp_val = getattr(item, "SpecifiedOutputParameterAbstraction432", None)
                    
                    if opp_val == self:
                        setattr(item, "SpecifiedOutputParameterAbstraction432", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SpecifiedOutputParameterAbstraction432"):
                    opp_val = getattr(item, "SpecifiedOutputParameterAbstraction432", None)
                    
                    setattr(item, "SpecifiedOutputParameterAbstraction432", self)
                    

    @property
    def qosAnnotations_SpecifiedQoSAnnotation(self):
        return self.__qosAnnotations_SpecifiedQoSAnnotation

    @qosAnnotations_SpecifiedQoSAnnotation.setter
    def qosAnnotations_SpecifiedQoSAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations__qosAnnotations_SpecifiedQoSAnnotation", None)
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
                    

    def MultipleReliabilityAnnotationsPerExternalCallNotAllowed(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement MultipleReliabilityAnnotationsPerExternalCallNotAllowed method
        pass

class pcm_pc_pc_entity_pc_pc_InterfaceProvidingEntity(Entity):

    pass
class entity_pc_pc_InterfaceRequiringEntity:

    pass
class entity_pc_pc_InterfaceProvidingEntity:

    pass
class pcm_pc_pc_entity_pc_pc_InterfaceProvidingRequiringEntity(entity_pc_pc_InterfaceProvidingEntity, entity_pc_pc_InterfaceRequiringEntity):

    pass
class ResourceInterface:

    pass
class entity_pc_pc_ResourceInterfaceProvidingEntity:

    pass
class pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingRequiringEntity(entity_pc_pc_ResourceInterfaceProvidingEntity, entity_pc_pc_ResourceInterfaceRequiringEntity):

    pass
class pcm_pc_pc_resourcetype_pc_pc_ResourceType(entity_pc_pc_ResourceInterfaceProvidingEntity, entity_pc_pc_Entity, UnitCarryingElement):

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

    def __init__(self, numberOfCalls__InfrastructureCall: "seff_performance_pc_pc_InfrastructureCall" = None, numberOfCalls__ResourceCall: "seff_performance_pc_pc_ResourceCall" = None, specification_ParametericResourceDemand: "seff_performance_pc_pc_ParametricResourceDemand" = None, iterationCount_LoopAction: "LoopAction" = None, thinkTime_ClosedWorkload: "ClosedWorkload" = None, capacity_PassiveResource: "PassiveResource" = None, specification_VariableCharacterisation: "VariableCharacterisation" = None, branchCondition_GuardedBranchTransition: "GuardedBranchTransition" = None, specification_SpecifiedExecutionTime: "qos_performance_pc_pc_SpecifiedExecutionTime" = None, filterCondition__EventChannelSinkConnector: "composition_pc_pc_EventChannelSinkConnector" = None, filterCondition__AssemblyEventConnector: "composition_pc_pc_AssemblyEventConnector" = None, loopIteration_Loop: "Loop" = None, interArrivalTime_OpenWorkload: "OpenWorkload" = None, timeSpecification_Delay: "Delay" = None, throughput_CommunicationLinkResourceSpecification: "CommunicationLinkResourceSpecification" = None, processingRate_ProcessingResourceSpecification: "ProcessingResourceSpecification" = None, latency_CommunicationLinkResourceSpecification: "CommunicationLinkResourceSpecification" = None):
        self.numberOfCalls__InfrastructureCall = numberOfCalls__InfrastructureCall
        self.numberOfCalls__ResourceCall = numberOfCalls__ResourceCall
        self.specification_ParametericResourceDemand = specification_ParametericResourceDemand
        self.iterationCount_LoopAction = iterationCount_LoopAction
        self.thinkTime_ClosedWorkload = thinkTime_ClosedWorkload
        self.capacity_PassiveResource = capacity_PassiveResource
        self.specification_VariableCharacterisation = specification_VariableCharacterisation
        self.branchCondition_GuardedBranchTransition = branchCondition_GuardedBranchTransition
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
    def iterationCount_LoopAction(self):
        return self.__iterationCount_LoopAction

    @iterationCount_LoopAction.setter
    def iterationCount_LoopAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__iterationCount_LoopAction", None)
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
    def timeSpecification_Delay(self):
        return self.__timeSpecification_Delay

    @timeSpecification_Delay.setter
    def timeSpecification_Delay(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__timeSpecification_Delay", None)
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
    def numberOfCalls__ResourceCall(self):
        return self.__numberOfCalls__ResourceCall

    @numberOfCalls__ResourceCall.setter
    def numberOfCalls__ResourceCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__numberOfCalls__ResourceCall", None)
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
    def specification_VariableCharacterisation(self):
        return self.__specification_VariableCharacterisation

    @specification_VariableCharacterisation.setter
    def specification_VariableCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__specification_VariableCharacterisation", None)
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
    def thinkTime_ClosedWorkload(self):
        return self.__thinkTime_ClosedWorkload

    @thinkTime_ClosedWorkload.setter
    def thinkTime_ClosedWorkload(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__thinkTime_ClosedWorkload", None)
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
    def branchCondition_GuardedBranchTransition(self):
        return self.__branchCondition_GuardedBranchTransition

    @branchCondition_GuardedBranchTransition.setter
    def branchCondition_GuardedBranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__branchCondition_GuardedBranchTransition", None)
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
    def loopIteration_Loop(self):
        return self.__loopIteration_Loop

    @loopIteration_Loop.setter
    def loopIteration_Loop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__loopIteration_Loop", None)
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
    def processingRate_ProcessingResourceSpecification(self):
        return self.__processingRate_ProcessingResourceSpecification

    @processingRate_ProcessingResourceSpecification.setter
    def processingRate_ProcessingResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__processingRate_ProcessingResourceSpecification", None)
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
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__latency_CommunicationLinkResourceSpecification", None)
        self.__latency_CommunicationLinkResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CommunicationLinkResourceSpecification20"):
                opp_val = getattr(old_value, "CommunicationLinkResourceSpecification20", None)
                if opp_val == self:
                    setattr(old_value, "CommunicationLinkResourceSpecification20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CommunicationLinkResourceSpecification20"):
                opp_val = getattr(value, "CommunicationLinkResourceSpecification20", None)
                setattr(value, "CommunicationLinkResourceSpecification20", self)

    @property
    def capacity_PassiveResource(self):
        return self.__capacity_PassiveResource

    @capacity_PassiveResource.setter
    def capacity_PassiveResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__capacity_PassiveResource", None)
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
    def specification_SpecifiedExecutionTime(self):
        return self.__specification_SpecifiedExecutionTime

    @specification_SpecifiedExecutionTime.setter
    def specification_SpecifiedExecutionTime(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__specification_SpecifiedExecutionTime", None)
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
    def filterCondition__AssemblyEventConnector(self):
        return self.__filterCondition__AssemblyEventConnector

    @filterCondition__AssemblyEventConnector.setter
    def filterCondition__AssemblyEventConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__filterCondition__AssemblyEventConnector", None)
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
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__numberOfCalls__InfrastructureCall", None)
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
    def interArrivalTime_OpenWorkload(self):
        return self.__interArrivalTime_OpenWorkload

    @interArrivalTime_OpenWorkload.setter
    def interArrivalTime_OpenWorkload(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__interArrivalTime_OpenWorkload", None)
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
    def throughput_CommunicationLinkResourceSpecification(self):
        return self.__throughput_CommunicationLinkResourceSpecification

    @throughput_CommunicationLinkResourceSpecification.setter
    def throughput_CommunicationLinkResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__throughput_CommunicationLinkResourceSpecification", None)
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
    def filterCondition__EventChannelSinkConnector(self):
        return self.__filterCondition__EventChannelSinkConnector

    @filterCondition__EventChannelSinkConnector.setter
    def filterCondition__EventChannelSinkConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__filterCondition__EventChannelSinkConnector", None)
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
    def specification_ParametericResourceDemand(self):
        return self.__specification_ParametericResourceDemand

    @specification_ParametericResourceDemand.setter
    def specification_ParametericResourceDemand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_pc_pc_core_pc_pc_PCMRandomVariable__specification_ParametericResourceDemand", None)
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

    def SpecificationMustNotBeNULL(self, pcm_pc_pc_diagnostics, pcm_pc_pc_context) :
        # TODO: Implement SpecificationMustNotBeNULL method
        pass

class pcm_pc_pc_Pointcut:

    pass
class pcm_pc_pc_EObject:

    pass
class pcm_pc_pc_PointcutPointcut:

    pass
class pcm_pc_pc_DummyClass:

    pass
class GuardedBranchTransition:

    pass
class LoopAction:

    pass
class seff_performance_pc_pc_ParametricResourceDemand:

    pass
class seff_performance_pc_pc_ResourceCall:

    pass