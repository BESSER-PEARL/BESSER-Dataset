from datetime import datetime, date, time
from abc import ABC, abstractmethod

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
class SchedulingPolicy(Enum):
    DELAY = "DELAY"
    PROCESSOR_SHARING = "PROCESSOR_SHARING"
    FCFS = "FCFS"
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


############################################
# Definition of Classes
############################################

class pcm_usagemodel_BranchTransition:

    def __init__(self, branchProbability: float, pcm_usagemodel_BranchTransition: "ScenarioBehaviour" = None):
        self.branchProbability = branchProbability
        self.pcm_usagemodel_BranchTransition = pcm_usagemodel_BranchTransition
        
    @property
    def branchProbability(self) -> float:
        return self.__branchProbability

    @branchProbability.setter
    def branchProbability(self, branchProbability: float):
        self.__branchProbability = branchProbability

    @property
    def pcm_usagemodel_BranchTransition(self):
        return self.__pcm_usagemodel_BranchTransition

    @pcm_usagemodel_BranchTransition.setter
    def pcm_usagemodel_BranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_usagemodel_BranchTransition__pcm_usagemodel_BranchTransition", None)
        self.__pcm_usagemodel_BranchTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ScenarioBehaviour274"):
                opp_val = getattr(old_value, "ScenarioBehaviour274", None)
                if opp_val == self:
                    setattr(old_value, "ScenarioBehaviour274", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ScenarioBehaviour274"):
                opp_val = getattr(value, "ScenarioBehaviour274", None)
                setattr(value, "ScenarioBehaviour274", self)

class BranchTransition:

    pass
class pcm_usagemodel_UserData:

    pass
class UserData:

    pass
class UsageScenario:

    pass
class pcm_usagemodel_UsageModel:

    pass
class AbstractUserAction:

    pass
class pcm_usagemodel_Delay(AbstractUserAction):

    pass
class pcm_usagemodel_Branch(AbstractUserAction):

    def __init__(self, pcm_usagemodel_Branch: set["BranchTransition"] = None, usagemodel: "pcm_usagemodel_AbstractUserAction", AbstractUserAction: "pcm_usagemodel_ScenarioBehaviour", usagemodel243: "pcm_usagemodel_AbstractUserAction"):
        self.pcm_usagemodel_Branch = pcm_usagemodel_Branch if pcm_usagemodel_Branch is not None else set()
        
    @property
    def pcm_usagemodel_Branch(self):
        return self.__pcm_usagemodel_Branch

    @pcm_usagemodel_Branch.setter
    def pcm_usagemodel_Branch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_usagemodel_Branch__pcm_usagemodel_Branch", None)
        self.__pcm_usagemodel_Branch = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BranchTransition"):
                    opp_val = getattr(item, "BranchTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "BranchTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BranchTransition"):
                    opp_val = getattr(item, "BranchTransition", None)
                    
                    setattr(item, "BranchTransition", self)
                    

    def AllBranchProbabilitiesMustSumUpTo1(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AllBranchProbabilitiesMustSumUpTo1 method
        pass

class pcm_usagemodel_Stop(AbstractUserAction):

    def __init__(self, usagemodel: "pcm_usagemodel_AbstractUserAction", AbstractUserAction: "pcm_usagemodel_ScenarioBehaviour", usagemodel243: "pcm_usagemodel_AbstractUserAction"):
        
    def StopHasNoSuccessor(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement StopHasNoSuccessor method
        pass

class pcm_usagemodel_Start(AbstractUserAction):

    def __init__(self, usagemodel: "pcm_usagemodel_AbstractUserAction", AbstractUserAction: "pcm_usagemodel_ScenarioBehaviour", usagemodel243: "pcm_usagemodel_AbstractUserAction"):
        
    def StartHasNoPredecessor(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement StartHasNoPredecessor method
        pass

class pcm_usagemodel_Loop(AbstractUserAction):

    pass
class pcm_usagemodel_EntryLevelSystemCall(AbstractUserAction):

    pass
class pcm_qosannotations_SpecifiedExecutionTime(ABC):

    pass
class QoSAnnotations:

    pass
class ScenarioBehaviour:

    pass
class Workload:

    pass
class pcm_usagemodel_OpenWorkload(Workload):

    def __init__(self, pcm_usagemodel_OpenWorkload: "PCMRandomVariable" = None, Workload: "pcm_usagemodel_UsageScenario"):
        self.pcm_usagemodel_OpenWorkload = pcm_usagemodel_OpenWorkload
        
    @property
    def pcm_usagemodel_OpenWorkload(self):
        return self.__pcm_usagemodel_OpenWorkload

    @pcm_usagemodel_OpenWorkload.setter
    def pcm_usagemodel_OpenWorkload(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_usagemodel_OpenWorkload__pcm_usagemodel_OpenWorkload", None)
        self.__pcm_usagemodel_OpenWorkload = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable253"):
                opp_val = getattr(old_value, "PCMRandomVariable253", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable253"):
                opp_val = getattr(value, "PCMRandomVariable253", None)
                setattr(value, "PCMRandomVariable253", self)

    def InterArrivalTimeInOpenWorkloadNeedsToBeSpecified(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement InterArrivalTimeInOpenWorkloadNeedsToBeSpecified method
        pass

class pcm_usagemodel_ClosedWorkload(Workload):

    def __init__(self, population: int, pcm_usagemodel_ClosedWorkload: "PCMRandomVariable" = None, Workload: "pcm_usagemodel_UsageScenario"):
        self.population = population
        self.pcm_usagemodel_ClosedWorkload = pcm_usagemodel_ClosedWorkload
        
    @property
    def population(self) -> int:
        return self.__population

    @population.setter
    def population(self, population: int):
        self.__population = population

    @property
    def pcm_usagemodel_ClosedWorkload(self):
        return self.__pcm_usagemodel_ClosedWorkload

    @pcm_usagemodel_ClosedWorkload.setter
    def pcm_usagemodel_ClosedWorkload(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_usagemodel_ClosedWorkload__pcm_usagemodel_ClosedWorkload", None)
        self.__pcm_usagemodel_ClosedWorkload = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable271"):
                opp_val = getattr(old_value, "PCMRandomVariable271", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable271", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable271"):
                opp_val = getattr(value, "PCMRandomVariable271", None)
                setattr(value, "PCMRandomVariable271", self)

    def PopulationInClosedWorkloadNeedsToBeSpecified(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement PopulationInClosedWorkloadNeedsToBeSpecified method
        pass

    def ThinkTimeInClosedWorkloadNeedsToBeSpecified(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ThinkTimeInClosedWorkloadNeedsToBeSpecified method
        pass

class pcm_usagemodel_Workload(ABC):

    pass
class SpecifiedOutputParameterAbstraction:

    pass
class pcm_qosannotations_SpecifiedOutputParameterAbstraction:

    pass
class SpecifiedExecutionTime:

    pass
class pcm_qosannotations_ComponentSpecifiedExecutionTime(SpecifiedExecutionTime):

    pass
class pcm_qosannotations_SystemSpecifiedExecutionTime(SpecifiedExecutionTime):

    pass
class System:

    pass
class pcm_qosannotations_SpecifiedFailureProbability:

    pass
class ProcessingResourceSpecification:

    pass
class pcm_resourceenvironment_ProcessingResourceSpecification:

    def __init__(self, schedulingPolicy: str, pcm_resourceenvironment_ProcessingResourceSpecification: "ProcessingResourceType" = None, pcm_resourceenvironment_ProcessingResourceSpecification210: "PCMRandomVariable" = None):
        self.schedulingPolicy = schedulingPolicy
        self.pcm_resourceenvironment_ProcessingResourceSpecification = pcm_resourceenvironment_ProcessingResourceSpecification
        self.pcm_resourceenvironment_ProcessingResourceSpecification210 = pcm_resourceenvironment_ProcessingResourceSpecification210
        
    @property
    def schedulingPolicy(self) -> str:
        return self.__schedulingPolicy

    @schedulingPolicy.setter
    def schedulingPolicy(self, schedulingPolicy: str):
        self.__schedulingPolicy = schedulingPolicy

    @property
    def pcm_resourceenvironment_ProcessingResourceSpecification(self):
        return self.__pcm_resourceenvironment_ProcessingResourceSpecification

    @pcm_resourceenvironment_ProcessingResourceSpecification.setter
    def pcm_resourceenvironment_ProcessingResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_resourceenvironment_ProcessingResourceSpecification__pcm_resourceenvironment_ProcessingResourceSpecification", None)
        self.__pcm_resourceenvironment_ProcessingResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcessingResourceType208"):
                opp_val = getattr(old_value, "ProcessingResourceType208", None)
                if opp_val == self:
                    setattr(old_value, "ProcessingResourceType208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessingResourceType208"):
                opp_val = getattr(value, "ProcessingResourceType208", None)
                setattr(value, "ProcessingResourceType208", self)

    @property
    def pcm_resourceenvironment_ProcessingResourceSpecification210(self):
        return self.__pcm_resourceenvironment_ProcessingResourceSpecification210

    @pcm_resourceenvironment_ProcessingResourceSpecification210.setter
    def pcm_resourceenvironment_ProcessingResourceSpecification210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_resourceenvironment_ProcessingResourceSpecification__pcm_resourceenvironment_ProcessingResourceSpecification210", None)
        self.__pcm_resourceenvironment_ProcessingResourceSpecification210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable211"):
                opp_val = getattr(old_value, "PCMRandomVariable211", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable211"):
                opp_val = getattr(value, "PCMRandomVariable211", None)
                setattr(value, "PCMRandomVariable211", self)

class CommunicationLinkResourceType:

    pass
class pcm_resourceenvironment_CommunicationLinkResourceSpecification:

    pass
class CommunicationLinkResourceSpecification:

    pass
class LinkingResource:

    pass
class pcm_resourceenvironment_ResourceEnvironment:

    pass
class ResourceEnvironment:

    pass
class AllocationContext:

    pass
class ResourceContainer:

    pass
class ResourceType:

    pass
class pcm_resourcetype_ProcessingResourceType(ResourceType):

    pass
class pcm_resourcetype_ResourceRepository:

    pass
class UnitCarryingElement:

    pass
class pcm_seff_ServiceEffectSpecification(ABC):

    def __init__(self, seffTypeID: str, pcm_seff_ServiceEffectSpecification: "Signature" = None):
        self.seffTypeID = seffTypeID
        self.pcm_seff_ServiceEffectSpecification = pcm_seff_ServiceEffectSpecification
        
    @property
    def seffTypeID(self) -> str:
        return self.__seffTypeID

    @seffTypeID.setter
    def seffTypeID(self, seffTypeID: str):
        self.__seffTypeID = seffTypeID

    @property
    def pcm_seff_ServiceEffectSpecification(self):
        return self.__pcm_seff_ServiceEffectSpecification

    @pcm_seff_ServiceEffectSpecification.setter
    def pcm_seff_ServiceEffectSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_seff_ServiceEffectSpecification__pcm_seff_ServiceEffectSpecification", None)
        self.__pcm_seff_ServiceEffectSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Signature178"):
                opp_val = getattr(old_value, "Signature178", None)
                if opp_val == self:
                    setattr(old_value, "Signature178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Signature178"):
                opp_val = getattr(value, "Signature178", None)
                setattr(value, "Signature178", self)

class ForkedBehaviour:

    pass
class AbstractBranchTransition:

    pass
class pcm_seff_GuardedBranchTransition(AbstractBranchTransition):

    pass
class pcm_seff_ProbabilisticBranchTransition(AbstractBranchTransition):

    def __init__(self, branchProbability: float, AbstractBranchTransition: "pcm_seff_BranchAction"):
        self.branchProbability = branchProbability
        
    @property
    def branchProbability(self) -> float:
        return self.__branchProbability

    @branchProbability.setter
    def branchProbability(self, branchProbability: float):
        self.__branchProbability = branchProbability

class pcm_seff_SynchronisationPoint:

    pass
class SynchronisationPoint:

    pass
class ResourceDemandingBehaviour:

    pass
class pcm_seff_ForkedBehaviour(ResourceDemandingBehaviour):

    pass
class AbstractLoopAction:

    pass
class pcm_seff_CollectionIteratorAction(AbstractLoopAction):

    pass
class pcm_seff_LoopAction(AbstractLoopAction):

    pass
class pcm_seff_ResourceDemandingBehaviour:

    def __init__(self, pcm_seff_ResourceDemandingBehaviour: set["AbstractAction"] = None):
        self.pcm_seff_ResourceDemandingBehaviour = pcm_seff_ResourceDemandingBehaviour if pcm_seff_ResourceDemandingBehaviour is not None else set()
        
    @property
    def pcm_seff_ResourceDemandingBehaviour(self):
        return self.__pcm_seff_ResourceDemandingBehaviour

    @pcm_seff_ResourceDemandingBehaviour.setter
    def pcm_seff_ResourceDemandingBehaviour(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_seff_ResourceDemandingBehaviour__pcm_seff_ResourceDemandingBehaviour", None)
        self.__pcm_seff_ResourceDemandingBehaviour = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractAction142"):
                    opp_val = getattr(item, "AbstractAction142", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractAction142", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractAction142"):
                    opp_val = getattr(item, "AbstractAction142", None)
                    
                    setattr(item, "AbstractAction142", self)
                    

    def ExactlyOneStartAction(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ExactlyOneStartAction method
        pass

    def EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor method
        pass

    def ExactlyOneStopAction(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ExactlyOneStopAction method
        pass

class AbstractAction:

    pass
class pcm_seff_ExternalCallAction(AbstractAction):

    pass
class pcm_seff_AbstractResourceDemandingAction(AbstractAction):

    pass
class seff_ResourceDemandingBehaviour:

    pass
class seff_ServiceEffectSpecification:

    pass
class ProcessingResourceType:

    pass
class pcm_resourcetype_CommunicationLinkResourceType(ProcessingResourceType):

    pass
class pcm_seff_ParametricResourceDemand:

    pass
class NamedElement:

    pass
class ParametricResourceDemand:

    pass
class pcm_repository_InnerDeclaration(NamedElement):

    pass
class InnerDeclaration:

    pass
class CompositeDataType:

    pass
class AbstractResourceDemandingAction:

    pass
class pcm_seff_AcquireAction(AbstractResourceDemandingAction):

    pass
class pcm_seff_BranchAction(AbstractResourceDemandingAction):

    def __init__(self, pcm_seff_BranchAction: set["AbstractBranchTransition"] = None, seff140: "pcm_seff_ParametricResourceDemand"):
        self.pcm_seff_BranchAction = pcm_seff_BranchAction if pcm_seff_BranchAction is not None else set()
        
    @property
    def pcm_seff_BranchAction(self):
        return self.__pcm_seff_BranchAction

    @pcm_seff_BranchAction.setter
    def pcm_seff_BranchAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_seff_BranchAction__pcm_seff_BranchAction", None)
        self.__pcm_seff_BranchAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractBranchTransition"):
                    opp_val = getattr(item, "AbstractBranchTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractBranchTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractBranchTransition"):
                    opp_val = getattr(item, "AbstractBranchTransition", None)
                    
                    setattr(item, "AbstractBranchTransition", self)
                    

    def AllProbabilisticBranchProbabilitiesMustSumUpTo1(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AllProbabilisticBranchProbabilitiesMustSumUpTo1 method
        pass

    def EitherGuardedBranchesOrProbabilisiticBranchTransitions(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement EitherGuardedBranchesOrProbabilisiticBranchTransitions method
        pass

class pcm_seff_StartAction(AbstractResourceDemandingAction):

    def __init__(self, seff140: "pcm_seff_ParametricResourceDemand"):
        
    def StartActionPredecessorMustNotBeDefined(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement StartActionPredecessorMustNotBeDefined method
        pass

class pcm_seff_ReleaseAction(AbstractResourceDemandingAction):

    pass
class pcm_seff_SetVariableAction(AbstractResourceDemandingAction):

    pass
class pcm_seff_ForkAction(AbstractResourceDemandingAction):

    pass
class pcm_seff_InternalAction(AbstractResourceDemandingAction):

    def __init__(self, failureProbability: str, seff140: "pcm_seff_ParametricResourceDemand"):
        self.failureProbability = failureProbability
        
    @property
    def failureProbability(self) -> str:
        return self.__failureProbability

    @failureProbability.setter
    def failureProbability(self, failureProbability: str):
        self.__failureProbability = failureProbability

class pcm_seff_AbstractLoopAction(AbstractResourceDemandingAction):

    pass
class pcm_seff_StopAction(AbstractResourceDemandingAction):

    def __init__(self, seff140: "pcm_seff_ParametricResourceDemand"):
        
    def StopActionSuccessorMustNotBeDefined(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement StopActionSuccessorMustNotBeDefined method
        pass

class parameter_pcm_AbstractNamedReference:

    pass
class VariableCharacterisation:

    pass
class pcm_parameter_VariableUsage:

    pass
class Variable:

    pass
class pcm_parameter_CharacterisedVariable(Variable):

    def __init__(self, characterisationType: str):
        self.characterisationType = characterisationType
        
    @property
    def characterisationType(self) -> str:
        return self.__characterisationType

    @characterisationType.setter
    def characterisationType(self, characterisationType: str):
        self.__characterisationType = characterisationType

class pcm_parameter_VariableCharacterisation:

    def __init__(self, type: str, pcm_parameter_VariableCharacterisation: "PCMRandomVariable" = None):
        self.type = type
        self.pcm_parameter_VariableCharacterisation = pcm_parameter_VariableCharacterisation
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def pcm_parameter_VariableCharacterisation(self):
        return self.__pcm_parameter_VariableCharacterisation

    @pcm_parameter_VariableCharacterisation.setter
    def pcm_parameter_VariableCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_parameter_VariableCharacterisation__pcm_parameter_VariableCharacterisation", None)
        self.__pcm_parameter_VariableCharacterisation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable125"):
                opp_val = getattr(old_value, "PCMRandomVariable125", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable125"):
                opp_val = getattr(value, "PCMRandomVariable125", None)
                setattr(value, "PCMRandomVariable125", self)

class pcm_protocol_Protocol(ABC):

    def __init__(self, protocolTypeID: str):
        self.protocolTypeID = protocolTypeID
        
    @property
    def protocolTypeID(self) -> str:
        return self.__protocolTypeID

    @protocolTypeID.setter
    def protocolTypeID(self, protocolTypeID: str):
        self.__protocolTypeID = protocolTypeID

class pcm_protocol_ServiceCall(ABC):

    pass
class ImplementationComponentType:

    pass
class pcm_repository_BasicComponent(ImplementationComponentType):

    def __init__(self, pcm_repository_BasicComponent: "ImplementationComponentType" = None, pcm_repository_BasicComponent107: set["ServiceEffectSpecification"] = None, pcm_repository_BasicComponent109: set["PassiveResource"] = None, ImplementationComponentType105: "pcm_repository_BasicComponent", ImplementationComponentType: "pcm_repository_CompositeComponent"):
        self.pcm_repository_BasicComponent = pcm_repository_BasicComponent
        self.pcm_repository_BasicComponent107 = pcm_repository_BasicComponent107 if pcm_repository_BasicComponent107 is not None else set()
        self.pcm_repository_BasicComponent109 = pcm_repository_BasicComponent109 if pcm_repository_BasicComponent109 is not None else set()
        
    @property
    def pcm_repository_BasicComponent(self):
        return self.__pcm_repository_BasicComponent

    @pcm_repository_BasicComponent.setter
    def pcm_repository_BasicComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_BasicComponent__pcm_repository_BasicComponent", None)
        self.__pcm_repository_BasicComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ImplementationComponentType105"):
                opp_val = getattr(old_value, "ImplementationComponentType105", None)
                if opp_val == self:
                    setattr(old_value, "ImplementationComponentType105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ImplementationComponentType105"):
                opp_val = getattr(value, "ImplementationComponentType105", None)
                setattr(value, "ImplementationComponentType105", self)

    @property
    def pcm_repository_BasicComponent107(self):
        return self.__pcm_repository_BasicComponent107

    @pcm_repository_BasicComponent107.setter
    def pcm_repository_BasicComponent107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_BasicComponent__pcm_repository_BasicComponent107", None)
        self.__pcm_repository_BasicComponent107 = value if value is not None else set()
        
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
    def pcm_repository_BasicComponent109(self):
        return self.__pcm_repository_BasicComponent109

    @pcm_repository_BasicComponent109.setter
    def pcm_repository_BasicComponent109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_BasicComponent__pcm_repository_BasicComponent109", None)
        self.__pcm_repository_BasicComponent109 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PassiveResource"):
                    opp_val = getattr(item, "PassiveResource", None)
                    
                    if opp_val == self:
                        setattr(item, "PassiveResource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PassiveResource"):
                    opp_val = getattr(item, "PassiveResource", None)
                    
                    setattr(item, "PassiveResource", self)
                    

    def RequireSameInterfacesAsImplementationType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RequireSameInterfacesAsImplementationType method
        pass

    def ProvideSameInterfacesAsImplementationType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ProvideSameInterfacesAsImplementationType method
        pass

    def NoSeffTypeUsedTwice(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NoSeffTypeUsedTwice method
        pass

class repository_DataType:

    pass
class PassiveResource:

    pass
class ServiceEffectSpecification:

    pass
class entity_ComposedProvidingRequiringEntity:

    pass
class repository_ImplementationComponentType:

    pass
class pcm_repository_CompositeComponent(entity_ComposedProvidingRequiringEntity, repository_ImplementationComponentType):

    def __init__(self, pcm_repository_CompositeComponent: "ImplementationComponentType" = None):
        self.pcm_repository_CompositeComponent = pcm_repository_CompositeComponent
        
    @property
    def pcm_repository_CompositeComponent(self):
        return self.__pcm_repository_CompositeComponent

    @pcm_repository_CompositeComponent.setter
    def pcm_repository_CompositeComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_CompositeComponent__pcm_repository_CompositeComponent", None)
        self.__pcm_repository_CompositeComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ImplementationComponentType"):
                opp_val = getattr(old_value, "ImplementationComponentType", None)
                if opp_val == self:
                    setattr(old_value, "ImplementationComponentType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ImplementationComponentType"):
                opp_val = getattr(value, "ImplementationComponentType", None)
                setattr(value, "ImplementationComponentType", self)

    def ProvideSameInterfaces(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ProvideSameInterfaces method
        pass

    def RequireSameInterfaces(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement RequireSameInterfaces method
        pass

class Connector:

    pass
class pcm_repository_DelegationConnector(Connector):

    pass
class Role:

    pass
class pcm_repository_ProvidedRole(Role):

    pass
class pcm_repository_RequiredRole(Role):

    pass
class CompleteComponentType:

    pass
class pcm_repository_ImplementationComponentType(CompleteComponentType):

    def __init__(self, pcm_repository_ImplementationComponentType: set["CompleteComponentType"] = None, pcm_repository_ImplementationComponentType99: set["VariableUsage"] = None, CompleteComponentType: "pcm_repository_ImplementationComponentType"):
        self.pcm_repository_ImplementationComponentType = pcm_repository_ImplementationComponentType if pcm_repository_ImplementationComponentType is not None else set()
        self.pcm_repository_ImplementationComponentType99 = pcm_repository_ImplementationComponentType99 if pcm_repository_ImplementationComponentType99 is not None else set()
        
    @property
    def pcm_repository_ImplementationComponentType99(self):
        return self.__pcm_repository_ImplementationComponentType99

    @pcm_repository_ImplementationComponentType99.setter
    def pcm_repository_ImplementationComponentType99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_ImplementationComponentType__pcm_repository_ImplementationComponentType99", None)
        self.__pcm_repository_ImplementationComponentType99 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableUsage100"):
                    opp_val = getattr(item, "VariableUsage100", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableUsage100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableUsage100"):
                    opp_val = getattr(item, "VariableUsage100", None)
                    
                    setattr(item, "VariableUsage100", self)
                    

    @property
    def pcm_repository_ImplementationComponentType(self):
        return self.__pcm_repository_ImplementationComponentType

    @pcm_repository_ImplementationComponentType.setter
    def pcm_repository_ImplementationComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_ImplementationComponentType__pcm_repository_ImplementationComponentType", None)
        self.__pcm_repository_ImplementationComponentType = value if value is not None else set()
        
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
                    

    def providedInterfacesHaveToConformToCompleteType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement providedInterfacesHaveToConformToCompleteType method
        pass

    def RequiredInterfacesHaveToConformToCompleteType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement RequiredInterfacesHaveToConformToCompleteType method
        pass

class pcm_repository_ExceptionType:

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

class Protocol:

    pass
class Interface:

    pass
class Parameter:

    pass
class pcm_repository_Signature:

    def __init__(self, serviceName: str, pcm_repository_Signature: "DataType" = None, pcm_repository_Signature61: set["ExceptionType"] = None, Parameter: set["Parameter"] = None, Interface: "Interface" = None):
        self.serviceName = serviceName
        self.pcm_repository_Signature = pcm_repository_Signature
        self.pcm_repository_Signature61 = pcm_repository_Signature61 if pcm_repository_Signature61 is not None else set()
        self.Parameter = Parameter if Parameter is not None else set()
        self.Interface = Interface
        
    @property
    def serviceName(self) -> str:
        return self.__serviceName

    @serviceName.setter
    def serviceName(self, serviceName: str):
        self.__serviceName = serviceName

    @property
    def Interface(self):
        return self.__Interface

    @Interface.setter
    def Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Signature__Interface", None)
        self.__Interface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository58"):
                opp_val = getattr(old_value, "repository58", None)
                if opp_val == self:
                    setattr(old_value, "repository58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository58"):
                opp_val = getattr(value, "repository58", None)
                setattr(value, "repository58", self)

    @property
    def Parameter(self):
        return self.__Parameter

    @Parameter.setter
    def Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Signature__Parameter", None)
        self.__Parameter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository56"):
                    opp_val = getattr(item, "repository56", None)
                    
                    if opp_val == self:
                        setattr(item, "repository56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository56"):
                    opp_val = getattr(item, "repository56", None)
                    
                    setattr(item, "repository56", self)
                    

    @property
    def pcm_repository_Signature(self):
        return self.__pcm_repository_Signature

    @pcm_repository_Signature.setter
    def pcm_repository_Signature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Signature__pcm_repository_Signature", None)
        self.__pcm_repository_Signature = value
        
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
    def pcm_repository_Signature61(self):
        return self.__pcm_repository_Signature61

    @pcm_repository_Signature61.setter
    def pcm_repository_Signature61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Signature__pcm_repository_Signature61", None)
        self.__pcm_repository_Signature61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExceptionType"):
                    opp_val = getattr(item, "ExceptionType", None)
                    
                    if opp_val == self:
                        setattr(item, "ExceptionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExceptionType"):
                    opp_val = getattr(item, "ExceptionType", None)
                    
                    setattr(item, "ExceptionType", self)
                    

    def ParameterNamesHaveToBeUniqueForASignature(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ParameterNamesHaveToBeUniqueForASignature method
        pass

class Repository:

    pass
class pcm_repository_DataType(ABC):

    pass
class Signature:

    pass
class pcm_repository_Parameter:

    def __init__(self, parameterName: str, modifier__Parameter: str, pcm_repository_Parameter: "DataType" = None, Signature: "Signature" = None):
        self.parameterName = parameterName
        self.modifier__Parameter = modifier__Parameter
        self.pcm_repository_Parameter = pcm_repository_Parameter
        self.Signature = Signature
        
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
    def pcm_repository_Parameter(self):
        return self.__pcm_repository_Parameter

    @pcm_repository_Parameter.setter
    def pcm_repository_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Parameter__pcm_repository_Parameter", None)
        self.__pcm_repository_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType63"):
                opp_val = getattr(old_value, "DataType63", None)
                if opp_val == self:
                    setattr(old_value, "DataType63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType63"):
                opp_val = getattr(value, "DataType63", None)
                setattr(value, "DataType63", self)

    @property
    def Signature(self):
        return self.__Signature

    @Signature.setter
    def Signature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Parameter__Signature", None)
        self.__Signature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository65"):
                opp_val = getattr(old_value, "repository65", None)
                if opp_val == self:
                    setattr(old_value, "repository65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository65"):
                opp_val = getattr(value, "repository65", None)
                setattr(value, "repository65", self)

class ExceptionType:

    pass
class DataType:

    pass
class pcm_repository_PrimitiveDataType(DataType):

    def __init__(self, type: str, repository76: "pcm_repository_Repository", DataType111: "pcm_repository_CollectionDataType", DataType63: "pcm_repository_Parameter", DataType: "pcm_repository_Signature", DataType116: "pcm_repository_InnerDeclaration"):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class entity_Entity:

    pass
class pcm_system_System(entity_ComposedProvidingRequiringEntity, entity_Entity):

    pass
class pcm_repository_CollectionDataType(repository_DataType, entity_Entity):

    pass
class pcm_repository_CompositeDataType(repository_DataType, entity_Entity):

    pass
class pcm_resourcetype_ResourceType(UnitCarryingElement, entity_Entity):

    pass
class connectors_Connector:

    pass
class pcm_composition_AssemblyConnector(connectors_Connector, entity_Entity):

    pass
class PCMRandomVariable:

    pass
class composition_AssemblyConnector:

    pass
class composition_RequiredDelegationConnector:

    pass
class composition_ProvidedDelegationConnector:

    pass
class composition_AssemblyContext:

    pass
class DelegationConnector:

    pass
class pcm_composition_ProvidedDelegationConnector(DelegationConnector):

    def __init__(self, composition: "composition_ComposedStructure" = None, pcm_composition_ProvidedDelegationConnector: "ProvidedRole" = None, pcm_composition_ProvidedDelegationConnector6: "ProvidedRole" = None, pcm_composition_ProvidedDelegationConnector9: "composition_AssemblyContext" = None):
        self.composition = composition
        self.pcm_composition_ProvidedDelegationConnector = pcm_composition_ProvidedDelegationConnector
        self.pcm_composition_ProvidedDelegationConnector6 = pcm_composition_ProvidedDelegationConnector6
        self.pcm_composition_ProvidedDelegationConnector9 = pcm_composition_ProvidedDelegationConnector9
        
    @property
    def composition(self):
        return self.__composition

    @composition.setter
    def composition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_ProvidedDelegationConnector__composition", None)
        self.__composition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core"):
                opp_val = getattr(old_value, "core", None)
                if opp_val == self:
                    setattr(old_value, "core", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core"):
                opp_val = getattr(value, "core", None)
                setattr(value, "core", self)

    @property
    def pcm_composition_ProvidedDelegationConnector6(self):
        return self.__pcm_composition_ProvidedDelegationConnector6

    @pcm_composition_ProvidedDelegationConnector6.setter
    def pcm_composition_ProvidedDelegationConnector6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_ProvidedDelegationConnector__pcm_composition_ProvidedDelegationConnector6", None)
        self.__pcm_composition_ProvidedDelegationConnector6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProvidedRole7"):
                opp_val = getattr(old_value, "ProvidedRole7", None)
                if opp_val == self:
                    setattr(old_value, "ProvidedRole7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProvidedRole7"):
                opp_val = getattr(value, "ProvidedRole7", None)
                setattr(value, "ProvidedRole7", self)

    @property
    def pcm_composition_ProvidedDelegationConnector9(self):
        return self.__pcm_composition_ProvidedDelegationConnector9

    @pcm_composition_ProvidedDelegationConnector9.setter
    def pcm_composition_ProvidedDelegationConnector9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_ProvidedDelegationConnector__pcm_composition_ProvidedDelegationConnector9", None)
        self.__pcm_composition_ProvidedDelegationConnector9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_AssemblyContext"):
                opp_val = getattr(old_value, "composition_AssemblyContext", None)
                if opp_val == self:
                    setattr(old_value, "composition_AssemblyContext", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_AssemblyContext"):
                opp_val = getattr(value, "composition_AssemblyContext", None)
                setattr(value, "composition_AssemblyContext", self)

    @property
    def pcm_composition_ProvidedDelegationConnector(self):
        return self.__pcm_composition_ProvidedDelegationConnector

    @pcm_composition_ProvidedDelegationConnector.setter
    def pcm_composition_ProvidedDelegationConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_ProvidedDelegationConnector__pcm_composition_ProvidedDelegationConnector", None)
        self.__pcm_composition_ProvidedDelegationConnector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProvidedRole4"):
                opp_val = getattr(old_value, "ProvidedRole4", None)
                if opp_val == self:
                    setattr(old_value, "ProvidedRole4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProvidedRole4"):
                opp_val = getattr(value, "ProvidedRole4", None)
                setattr(value, "ProvidedRole4", self)

    def ComponentOfChildComponentContextAndInnerRoleProvidingComponentNeedToBeTheSame(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ComponentOfChildComponentContextAndInnerRoleProvidingComponentNeedToBeTheSame method
        pass

    def ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

class entity_InterfaceProvidingRequiringEntity:

    pass
class pcm_repository_ProvidesComponentType(entity_InterfaceProvidingRequiringEntity, entity_Entity):

    def __init__(self, Repository78: "Repository" = None):
        self.Repository78 = Repository78
        
    @property
    def Repository78(self):
        return self.__Repository78

    @Repository78.setter
    def Repository78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_ProvidesComponentType__Repository78", None)
        self.__Repository78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository79"):
                opp_val = getattr(old_value, "repository79", None)
                if opp_val == self:
                    setattr(old_value, "repository79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository79"):
                opp_val = getattr(value, "repository79", None)
                setattr(value, "repository79", self)

    def AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType method
        pass

class composition_ComposedStructure:

    pass
class pcm_entity_ComposedProvidingRequiringEntity(composition_ComposedStructure, entity_InterfaceProvidingRequiringEntity):

    pass
class pcm_composition_RequiredDelegationConnector(DelegationConnector):

    def __init__(self, pcm_composition_RequiredDelegationConnector: "RequiredRole" = None, pcm_composition_RequiredDelegationConnector20: "RequiredRole" = None, pcm_composition_RequiredDelegationConnector23: "composition_AssemblyContext" = None, composition26: "composition_ComposedStructure" = None):
        self.pcm_composition_RequiredDelegationConnector = pcm_composition_RequiredDelegationConnector
        self.pcm_composition_RequiredDelegationConnector20 = pcm_composition_RequiredDelegationConnector20
        self.pcm_composition_RequiredDelegationConnector23 = pcm_composition_RequiredDelegationConnector23
        self.composition26 = composition26
        
    @property
    def pcm_composition_RequiredDelegationConnector20(self):
        return self.__pcm_composition_RequiredDelegationConnector20

    @pcm_composition_RequiredDelegationConnector20.setter
    def pcm_composition_RequiredDelegationConnector20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_RequiredDelegationConnector__pcm_composition_RequiredDelegationConnector20", None)
        self.__pcm_composition_RequiredDelegationConnector20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RequiredRole21"):
                opp_val = getattr(old_value, "RequiredRole21", None)
                if opp_val == self:
                    setattr(old_value, "RequiredRole21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RequiredRole21"):
                opp_val = getattr(value, "RequiredRole21", None)
                setattr(value, "RequiredRole21", self)

    @property
    def composition26(self):
        return self.__composition26

    @composition26.setter
    def composition26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_RequiredDelegationConnector__composition26", None)
        self.__composition26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core27"):
                opp_val = getattr(old_value, "core27", None)
                if opp_val == self:
                    setattr(old_value, "core27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core27"):
                opp_val = getattr(value, "core27", None)
                setattr(value, "core27", self)

    @property
    def pcm_composition_RequiredDelegationConnector(self):
        return self.__pcm_composition_RequiredDelegationConnector

    @pcm_composition_RequiredDelegationConnector.setter
    def pcm_composition_RequiredDelegationConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_RequiredDelegationConnector__pcm_composition_RequiredDelegationConnector", None)
        self.__pcm_composition_RequiredDelegationConnector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RequiredRole18"):
                opp_val = getattr(old_value, "RequiredRole18", None)
                if opp_val == self:
                    setattr(old_value, "RequiredRole18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RequiredRole18"):
                opp_val = getattr(value, "RequiredRole18", None)
                setattr(value, "RequiredRole18", self)

    @property
    def pcm_composition_RequiredDelegationConnector23(self):
        return self.__pcm_composition_RequiredDelegationConnector23

    @pcm_composition_RequiredDelegationConnector23.setter
    def pcm_composition_RequiredDelegationConnector23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_RequiredDelegationConnector__pcm_composition_RequiredDelegationConnector23", None)
        self.__pcm_composition_RequiredDelegationConnector23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_AssemblyContext24"):
                opp_val = getattr(old_value, "composition_AssemblyContext24", None)
                if opp_val == self:
                    setattr(old_value, "composition_AssemblyContext24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_AssemblyContext24"):
                opp_val = getattr(value, "composition_AssemblyContext24", None)
                setattr(value, "composition_AssemblyContext24", self)

    def RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

    def ComponentOfChildComponentContextAndInnerRoleRequiringComponentNeedToBeTheSame(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ComponentOfChildComponentContextAndInnerRoleRequiringComponentNeedToBeTheSame method
        pass

class VariableUsage:

    pass
class ProvidesComponentType:

    pass
class pcm_repository_CompleteComponentType(ProvidesComponentType):

    def __init__(self, pcm_repository_CompleteComponentType: set["ProvidesComponentType"] = None, ProvidesComponentType: "pcm_composition_AssemblyContext", ProvidesComponentType102: "pcm_repository_CompleteComponentType", repository70: "pcm_repository_Repository"):
        self.pcm_repository_CompleteComponentType = pcm_repository_CompleteComponentType if pcm_repository_CompleteComponentType is not None else set()
        
    @property
    def pcm_repository_CompleteComponentType(self):
        return self.__pcm_repository_CompleteComponentType

    @pcm_repository_CompleteComponentType.setter
    def pcm_repository_CompleteComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_CompleteComponentType__pcm_repository_CompleteComponentType", None)
        self.__pcm_repository_CompleteComponentType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProvidesComponentType102"):
                    opp_val = getattr(item, "ProvidesComponentType102", None)
                    
                    if opp_val == self:
                        setattr(item, "ProvidesComponentType102", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProvidesComponentType102"):
                    opp_val = getattr(item, "ProvidesComponentType102", None)
                    
                    setattr(item, "ProvidesComponentType102", self)
                    

    def AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType method
        pass

    def providedInterfacesHaveToConformToProvidedType2(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement providedInterfacesHaveToConformToProvidedType2 method
        pass

class RandomVariable:

    pass
class pcm_core_PCMRandomVariable(RandomVariable):

    def __init__(self):
        
    def SpecificationMustNotBeNULL(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SpecificationMustNotBeNULL method
        pass

class RequiredRole:

    pass
class entity_InterfaceRequiringEntity:

    pass
class entity_InterfaceProvidingEntity:

    pass
class pcm_entity_InterfaceProvidingRequiringEntity(entity_InterfaceProvidingEntity, entity_InterfaceRequiringEntity):

    pass
class ProvidedRole:

    pass
class Entity:

    pass
class pcm_resourceenvironment_LinkingResource(Entity):

    pass
class pcm_repository_Repository(Entity):

    def __init__(self, repositoryDescription: str, ProvidesComponentType69: set["ProvidesComponentType"] = None, Interface72: set["Interface"] = None, DataType75: set["DataType"] = None):
        self.repositoryDescription = repositoryDescription
        self.ProvidesComponentType69 = ProvidesComponentType69 if ProvidesComponentType69 is not None else set()
        self.Interface72 = Interface72 if Interface72 is not None else set()
        self.DataType75 = DataType75 if DataType75 is not None else set()
        
    @property
    def repositoryDescription(self) -> str:
        return self.__repositoryDescription

    @repositoryDescription.setter
    def repositoryDescription(self, repositoryDescription: str):
        self.__repositoryDescription = repositoryDescription

    @property
    def Interface72(self):
        return self.__Interface72

    @Interface72.setter
    def Interface72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Repository__Interface72", None)
        self.__Interface72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository73"):
                    opp_val = getattr(item, "repository73", None)
                    
                    if opp_val == self:
                        setattr(item, "repository73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository73"):
                    opp_val = getattr(item, "repository73", None)
                    
                    setattr(item, "repository73", self)
                    

    @property
    def ProvidesComponentType69(self):
        return self.__ProvidesComponentType69

    @ProvidesComponentType69.setter
    def ProvidesComponentType69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Repository__ProvidesComponentType69", None)
        self.__ProvidesComponentType69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository70"):
                    opp_val = getattr(item, "repository70", None)
                    
                    if opp_val == self:
                        setattr(item, "repository70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository70"):
                    opp_val = getattr(item, "repository70", None)
                    
                    setattr(item, "repository70", self)
                    

    @property
    def DataType75(self):
        return self.__DataType75

    @DataType75.setter
    def DataType75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Repository__DataType75", None)
        self.__DataType75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository76"):
                    opp_val = getattr(item, "repository76", None)
                    
                    if opp_val == self:
                        setattr(item, "repository76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository76"):
                    opp_val = getattr(item, "repository76", None)
                    
                    setattr(item, "repository76", self)
                    

class pcm_repository_Interface(Entity):

    def __init__(self, pcm_repository_Interface: set["Interface"] = None, pcm_repository_Interface87: set["Interface"] = None, pcm_repository_Interface90: set["Protocol"] = None, Signature92: set["Signature"] = None, Repository95: "Repository" = None):
        self.pcm_repository_Interface = pcm_repository_Interface if pcm_repository_Interface is not None else set()
        self.pcm_repository_Interface87 = pcm_repository_Interface87 if pcm_repository_Interface87 is not None else set()
        self.pcm_repository_Interface90 = pcm_repository_Interface90 if pcm_repository_Interface90 is not None else set()
        self.Signature92 = Signature92 if Signature92 is not None else set()
        self.Repository95 = Repository95
        
    @property
    def pcm_repository_Interface90(self):
        return self.__pcm_repository_Interface90

    @pcm_repository_Interface90.setter
    def pcm_repository_Interface90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Interface__pcm_repository_Interface90", None)
        self.__pcm_repository_Interface90 = value if value is not None else set()
        
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
    def Signature92(self):
        return self.__Signature92

    @Signature92.setter
    def Signature92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Interface__Signature92", None)
        self.__Signature92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository93"):
                    opp_val = getattr(item, "repository93", None)
                    
                    if opp_val == self:
                        setattr(item, "repository93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository93"):
                    opp_val = getattr(item, "repository93", None)
                    
                    setattr(item, "repository93", self)
                    

    @property
    def Repository95(self):
        return self.__Repository95

    @Repository95.setter
    def Repository95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Interface__Repository95", None)
        self.__Repository95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository96"):
                opp_val = getattr(old_value, "repository96", None)
                if opp_val == self:
                    setattr(old_value, "repository96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository96"):
                opp_val = getattr(value, "repository96", None)
                setattr(value, "repository96", self)

    @property
    def pcm_repository_Interface(self):
        return self.__pcm_repository_Interface

    @pcm_repository_Interface.setter
    def pcm_repository_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Interface__pcm_repository_Interface", None)
        self.__pcm_repository_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Interface85"):
                    opp_val = getattr(item, "Interface85", None)
                    
                    if opp_val == self:
                        setattr(item, "Interface85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Interface85"):
                    opp_val = getattr(item, "Interface85", None)
                    
                    setattr(item, "Interface85", self)
                    

    @property
    def pcm_repository_Interface87(self):
        return self.__pcm_repository_Interface87

    @pcm_repository_Interface87.setter
    def pcm_repository_Interface87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Interface__pcm_repository_Interface87", None)
        self.__pcm_repository_Interface87 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Interface88"):
                    opp_val = getattr(item, "Interface88", None)
                    
                    if opp_val == self:
                        setattr(item, "Interface88", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Interface88"):
                    opp_val = getattr(item, "Interface88", None)
                    
                    setattr(item, "Interface88", self)
                    

    def SignaturesHaveToBeUniqueForAnInterface(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SignaturesHaveToBeUniqueForAnInterface method
        pass

    def NoProtocolTypeIDUsedTwice(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NoProtocolTypeIDUsedTwice method
        pass

class pcm_repository_PassiveResource(Entity):

    pass
class pcm_qosannotations_QoSAnnotations(Entity):

    pass
class pcm_allocation_Allocation(Entity):

    def __init__(self, pcm_allocation_Allocation: set["AllocationContext"] = None, pcm_allocation_Allocation186: "ResourceEnvironment" = None, pcm_allocation_Allocation188: "System" = None):
        self.pcm_allocation_Allocation = pcm_allocation_Allocation if pcm_allocation_Allocation is not None else set()
        self.pcm_allocation_Allocation186 = pcm_allocation_Allocation186
        self.pcm_allocation_Allocation188 = pcm_allocation_Allocation188
        
    @property
    def pcm_allocation_Allocation188(self):
        return self.__pcm_allocation_Allocation188

    @pcm_allocation_Allocation188.setter
    def pcm_allocation_Allocation188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_allocation_Allocation__pcm_allocation_Allocation188", None)
        self.__pcm_allocation_Allocation188 = value
        
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
    def pcm_allocation_Allocation(self):
        return self.__pcm_allocation_Allocation

    @pcm_allocation_Allocation.setter
    def pcm_allocation_Allocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_allocation_Allocation__pcm_allocation_Allocation", None)
        self.__pcm_allocation_Allocation = value if value is not None else set()
        
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
                    

    @property
    def pcm_allocation_Allocation186(self):
        return self.__pcm_allocation_Allocation186

    @pcm_allocation_Allocation186.setter
    def pcm_allocation_Allocation186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_allocation_Allocation__pcm_allocation_Allocation186", None)
        self.__pcm_allocation_Allocation186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceEnvironment"):
                opp_val = getattr(old_value, "ResourceEnvironment", None)
                if opp_val == self:
                    setattr(old_value, "ResourceEnvironment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceEnvironment"):
                opp_val = getattr(value, "ResourceEnvironment", None)
                setattr(value, "ResourceEnvironment", self)

    def EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce method
        pass

class pcm_seff_AbstractAction(Entity):

    pass
class pcm_composition_AssemblyContext(Entity):

    pass
class pcm_resourceenvironment_ResourceContainer(Entity):

    pass
class pcm_usagemodel_AbstractUserAction(Entity):

    pass
class pcm_connectors_Connector(Entity):

    pass
class pcm_entity_InterfaceRequiringEntity(Entity):

    pass
class pcm_usagemodel_UsageScenario(Entity):

    pass
class pcm_repository_Role(Entity):

    pass
class pcm_composition_ComposedStructure(Entity):

    pass
class pcm_usagemodel_ScenarioBehaviour(Entity):

    def __init__(self, pcm_usagemodel_ScenarioBehaviour: set["AbstractUserAction"] = None):
        self.pcm_usagemodel_ScenarioBehaviour = pcm_usagemodel_ScenarioBehaviour if pcm_usagemodel_ScenarioBehaviour is not None else set()
        
    @property
    def pcm_usagemodel_ScenarioBehaviour(self):
        return self.__pcm_usagemodel_ScenarioBehaviour

    @pcm_usagemodel_ScenarioBehaviour.setter
    def pcm_usagemodel_ScenarioBehaviour(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_usagemodel_ScenarioBehaviour__pcm_usagemodel_ScenarioBehaviour", None)
        self.__pcm_usagemodel_ScenarioBehaviour = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractUserAction"):
                    opp_val = getattr(item, "AbstractUserAction", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractUserAction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractUserAction"):
                    opp_val = getattr(item, "AbstractUserAction", None)
                    
                    setattr(item, "AbstractUserAction", self)
                    

    def EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor method
        pass

    def Exactlyonestart(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement Exactlyonestart method
        pass

    def Exactlyonestop(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement Exactlyonestop method
        pass

class pcm_allocation_AllocationContext(Entity):

    pass
class pcm_entity_InterfaceProvidingEntity(Entity):

    pass
class pcm_entity_NamedElement(ABC):

    def __init__(self, entityName: str):
        self.entityName = entityName
        
    @property
    def entityName(self) -> str:
        return self.__entityName

    @entityName.setter
    def entityName(self, entityName: str):
        self.__entityName = entityName

class entity_NamedElement:

    pass
class Identifier:

    pass
class pcm_seff_AbstractBranchTransition(Identifier):

    pass
class pcm_seff_ResourceDemandingSEFF(Identifier, seff_ServiceEffectSpecification, seff_ResourceDemandingBehaviour):

    pass
class pcm_entity_Entity(entity_NamedElement, Identifier):

    pass