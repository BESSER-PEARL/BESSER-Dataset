from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ParameterModifier(Enum):
    none = "none"
    in_ = "in_"
    out = "out"
    inout = "inout"
class SchedulingPolicy(Enum):
    DELAY = "DELAY"
    PROCESSOR_SHARING = "PROCESSOR_SHARING"
    FCFS = "FCFS"
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


############################################
# Definition of Classes
############################################

class pcm_usagemodel_BranchTransition:

    def __init__(self, branchProbability: float, pcm_usagemodel_BranchTransition: "ScenarioBehaviour" = None):
        self.branchProbability = branchProbability
        self.pcm_usagemodel_BranchTransition = pcm_usagemodel_BranchTransition
        
        pass
    @property
    def branchProbability(self):
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
            if hasattr(old_value, "ScenarioBehaviour245"):
                opp_val = getattr(old_value, "ScenarioBehaviour245", None)
                if opp_val == self:
                    setattr(old_value, "ScenarioBehaviour245", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ScenarioBehaviour245"):
                opp_val = getattr(value, "ScenarioBehaviour245", None)
                setattr(value, "ScenarioBehaviour245", self)

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
class pcm_usagemodel_EntryLevelSystemCall(AbstractUserAction):

    pass
class pcm_usagemodel_Stop(AbstractUserAction):

    def __init__(self, AbstractUserAction214: "pcm_usagemodel_AbstractUserAction" = None, AbstractUserAction212: "pcm_usagemodel_AbstractUserAction" = None, AbstractUserAction: "pcm_usagemodel_ScenarioBehaviour" = None):
        
        pass
    def StopHasNoSuccessor(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement StopHasNoSuccessor method
        pass

class pcm_usagemodel_Delay(AbstractUserAction):

    pass
class pcm_usagemodel_Branch(AbstractUserAction):

    def __init__(self, pcm_usagemodel_Branch: set["BranchTransition"] = None, AbstractUserAction214: "pcm_usagemodel_AbstractUserAction" = None, AbstractUserAction212: "pcm_usagemodel_AbstractUserAction" = None, AbstractUserAction: "pcm_usagemodel_ScenarioBehaviour" = None):
        self.pcm_usagemodel_Branch = pcm_usagemodel_Branch if pcm_usagemodel_Branch is not None else set()
        
        pass
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
                    

    def AllBranchProbabilitiesMustSumUpTo1(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement AllBranchProbabilitiesMustSumUpTo1 method
        pass

class pcm_usagemodel_Start(AbstractUserAction):

    def __init__(self, AbstractUserAction214: "pcm_usagemodel_AbstractUserAction" = None, AbstractUserAction212: "pcm_usagemodel_AbstractUserAction" = None, AbstractUserAction: "pcm_usagemodel_ScenarioBehaviour" = None):
        
        pass
    def StartHasNoPredecessor(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement StartHasNoPredecessor method
        pass

class pcm_usagemodel_Loop(AbstractUserAction):

    pass
class ScenarioBehaviour:

    pass
class Workload:

    pass
class pcm_usagemodel_OpenWorkload(Workload):

    def __init__(self, pcm_usagemodel_OpenWorkload: "PCMRandomVariable" = None, Workload: "pcm_usagemodel_UsageScenario" = None):
        self.pcm_usagemodel_OpenWorkload = pcm_usagemodel_OpenWorkload
        
        pass
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
            if hasattr(old_value, "PCMRandomVariable224"):
                opp_val = getattr(old_value, "PCMRandomVariable224", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable224"):
                opp_val = getattr(value, "PCMRandomVariable224", None)
                setattr(value, "PCMRandomVariable224", self)

    def InterArrivalTimeInOpenWorkloadNeedsToBeSpecified(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement InterArrivalTimeInOpenWorkloadNeedsToBeSpecified method
        pass

class pcm_usagemodel_ClosedWorkload(Workload):

    def __init__(self, population: int, pcm_usagemodel_ClosedWorkload: "PCMRandomVariable" = None, Workload: "pcm_usagemodel_UsageScenario" = None):
        self.population = population
        self.pcm_usagemodel_ClosedWorkload = pcm_usagemodel_ClosedWorkload
        
        pass
    @property
    def population(self):
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
            if hasattr(old_value, "PCMRandomVariable242"):
                opp_val = getattr(old_value, "PCMRandomVariable242", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable242", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable242"):
                opp_val = getattr(value, "PCMRandomVariable242", None)
                setattr(value, "PCMRandomVariable242", self)

    def ThinkTimeInClosedWorkloadNeedsToBeSpecified(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement ThinkTimeInClosedWorkloadNeedsToBeSpecified method
        pass

    def PopulationInClosedWorkloadNeedsToBeSpecified(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement PopulationInClosedWorkloadNeedsToBeSpecified method
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
class pcm_qosannotations_SpecifiedFailureProbability:

    pass
class pcm_qosannotations_SpecifiedExecutionTime(ABC):

    pass
class QoSAnnotations:

    pass
class ProcessingResourceSpecification:

    pass
class pcm_resourceenvironment_ProcessingResourceSpecification:

    def __init__(self, schedulingPolicy: str, pcm_resourceenvironment_ProcessingResourceSpecification: "ProcessingResourceType" = None, pcm_resourceenvironment_ProcessingResourceSpecification182: "PCMRandomVariable" = None):
        self.schedulingPolicy = schedulingPolicy
        self.pcm_resourceenvironment_ProcessingResourceSpecification = pcm_resourceenvironment_ProcessingResourceSpecification
        self.pcm_resourceenvironment_ProcessingResourceSpecification182 = pcm_resourceenvironment_ProcessingResourceSpecification182
        
        pass
    @property
    def schedulingPolicy(self):
        return self.__schedulingPolicy

    @schedulingPolicy.setter
    def schedulingPolicy(self, schedulingPolicy: str):
        self.__schedulingPolicy = schedulingPolicy


    @property
    def pcm_resourceenvironment_ProcessingResourceSpecification182(self):
        return self.__pcm_resourceenvironment_ProcessingResourceSpecification182

    @pcm_resourceenvironment_ProcessingResourceSpecification182.setter
    def pcm_resourceenvironment_ProcessingResourceSpecification182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_resourceenvironment_ProcessingResourceSpecification__pcm_resourceenvironment_ProcessingResourceSpecification182", None)
        self.__pcm_resourceenvironment_ProcessingResourceSpecification182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable183"):
                opp_val = getattr(old_value, "PCMRandomVariable183", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable183"):
                opp_val = getattr(value, "PCMRandomVariable183", None)
                setattr(value, "PCMRandomVariable183", self)

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
            if hasattr(old_value, "ProcessingResourceType180"):
                opp_val = getattr(old_value, "ProcessingResourceType180", None)
                if opp_val == self:
                    setattr(old_value, "ProcessingResourceType180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessingResourceType180"):
                opp_val = getattr(value, "ProcessingResourceType180", None)
                setattr(value, "ProcessingResourceType180", self)

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
class System:

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
        
        pass
    @property
    def seffTypeID(self):
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
            if hasattr(old_value, "Signature150"):
                opp_val = getattr(old_value, "Signature150", None)
                if opp_val == self:
                    setattr(old_value, "Signature150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Signature150"):
                opp_val = getattr(value, "Signature150", None)
                setattr(value, "Signature150", self)

class AbstractBranchTransition:

    pass
class pcm_seff_GuardedBranchTransition(AbstractBranchTransition):

    pass
class pcm_seff_ProbabilisticBranchTransition(AbstractBranchTransition):

    def __init__(self, branchProbability: float, AbstractBranchTransition: "pcm_seff_BranchAction" = None):
        self.branchProbability = branchProbability
        
        pass
    @property
    def branchProbability(self):
        return self.__branchProbability

    @branchProbability.setter
    def branchProbability(self, branchProbability: float):
        self.__branchProbability = branchProbability


class SynchronisationPoint:

    pass
class ForkedBehaviour:

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
class pcm_seff_SynchronisationPoint:

    pass
class pcm_seff_ResourceDemandingBehaviour:

    def __init__(self, pcm_seff_ResourceDemandingBehaviour: set["AbstractAction"] = None):
        self.pcm_seff_ResourceDemandingBehaviour = pcm_seff_ResourceDemandingBehaviour if pcm_seff_ResourceDemandingBehaviour is not None else set()
        
        pass
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
                if hasattr(item, "AbstractAction114"):
                    opp_val = getattr(item, "AbstractAction114", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractAction114", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractAction114"):
                    opp_val = getattr(item, "AbstractAction114", None)
                    
                    setattr(item, "AbstractAction114", self)
                    

    def EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor method
        pass

    def ExactlyOneStartAction(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement ExactlyOneStartAction method
        pass

    def ExactlyOneStopAction(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement ExactlyOneStopAction method
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
class AbstractAction:

    pass
class pcm_seff_ExternalCallAction(AbstractAction):

    pass
class pcm_seff_AbstractResourceDemandingAction(AbstractAction):

    pass
class AbstractResourceDemandingAction:

    pass
class pcm_seff_ReleaseAction(AbstractResourceDemandingAction):

    pass
class pcm_seff_BranchAction(AbstractResourceDemandingAction):

    def __init__(self, pcm_seff_BranchAction: set["AbstractBranchTransition"] = None, AbstractResourceDemandingAction: "pcm_seff_ParametricResourceDemand" = None):
        self.pcm_seff_BranchAction = pcm_seff_BranchAction if pcm_seff_BranchAction is not None else set()
        
        pass
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
                    

    def EitherGuardedBranchesOrProbabilisiticBranchTransitions(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement EitherGuardedBranchesOrProbabilisiticBranchTransitions method
        pass

    def AllProbabilisticBranchProbabilitiesMustSumUpTo1(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement AllProbabilisticBranchProbabilitiesMustSumUpTo1 method
        pass

class pcm_seff_ForkAction(AbstractResourceDemandingAction):

    pass
class pcm_seff_SetVariableAction(AbstractResourceDemandingAction):

    pass
class pcm_seff_InternalAction(AbstractResourceDemandingAction):

    def __init__(self, failureProbability: str, AbstractResourceDemandingAction: "pcm_seff_ParametricResourceDemand" = None):
        self.failureProbability = failureProbability
        
        pass
    @property
    def failureProbability(self):
        return self.__failureProbability

    @failureProbability.setter
    def failureProbability(self, failureProbability: str):
        self.__failureProbability = failureProbability


class pcm_seff_StartAction(AbstractResourceDemandingAction):

    def __init__(self, AbstractResourceDemandingAction: "pcm_seff_ParametricResourceDemand" = None):
        
        pass
    def StartActionPredecessorMustNotBeDefined(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement StartActionPredecessorMustNotBeDefined method
        pass

class pcm_seff_AbstractLoopAction(AbstractResourceDemandingAction):

    pass
class pcm_seff_AcquireAction(AbstractResourceDemandingAction):

    pass
class pcm_seff_StopAction(AbstractResourceDemandingAction):

    def __init__(self, AbstractResourceDemandingAction: "pcm_seff_ParametricResourceDemand" = None):
        
        pass
    def StopActionSuccessorMustNotBeDefined(self, pcm_context, pcm_diagnostics) :
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
        
        pass
    @property
    def characterisationType(self):
        return self.__characterisationType

    @characterisationType.setter
    def characterisationType(self, characterisationType: str):
        self.__characterisationType = characterisationType


class pcm_parameter_VariableCharacterisation:

    def __init__(self, type: str, pcm_parameter_VariableCharacterisation: "PCMRandomVariable" = None):
        self.type = type
        self.pcm_parameter_VariableCharacterisation = pcm_parameter_VariableCharacterisation
        
        pass
    @property
    def type(self):
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
            if hasattr(old_value, "PCMRandomVariable100"):
                opp_val = getattr(old_value, "PCMRandomVariable100", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable100"):
                opp_val = getattr(value, "PCMRandomVariable100", None)
                setattr(value, "PCMRandomVariable100", self)

class pcm_protocol_Protocol(ABC):

    def __init__(self, protocolTypeID: str):
        self.protocolTypeID = protocolTypeID
        
        pass
    @property
    def protocolTypeID(self):
        return self.__protocolTypeID

    @protocolTypeID.setter
    def protocolTypeID(self, protocolTypeID: str):
        self.__protocolTypeID = protocolTypeID


class pcm_protocol_ServiceCall(ABC):

    pass
class ParametricResourceDemand:

    pass
class NamedElement:

    pass
class pcm_repository_InnerDeclaration(NamedElement):

    pass
class InnerDeclaration:

    pass
class CompositeDataType:

    pass
class repository_DataType:

    pass
class PassiveResource:

    pass
class ServiceEffectSpecification:

    pass
class ImplementationComponentType:

    pass
class pcm_repository_BasicComponent(ImplementationComponentType):

    def __init__(self, pcm_repository_BasicComponent: "ImplementationComponentType" = None, pcm_repository_BasicComponent84: set["ServiceEffectSpecification"] = None, pcm_repository_BasicComponent86: set["PassiveResource"] = None, ImplementationComponentType: "pcm_repository_CompositeComponent" = None, ImplementationComponentType82: "pcm_repository_BasicComponent" = None):
        self.pcm_repository_BasicComponent = pcm_repository_BasicComponent
        self.pcm_repository_BasicComponent84 = pcm_repository_BasicComponent84 if pcm_repository_BasicComponent84 is not None else set()
        self.pcm_repository_BasicComponent86 = pcm_repository_BasicComponent86 if pcm_repository_BasicComponent86 is not None else set()
        
        pass
    @property
    def pcm_repository_BasicComponent86(self):
        return self.__pcm_repository_BasicComponent86

    @pcm_repository_BasicComponent86.setter
    def pcm_repository_BasicComponent86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_BasicComponent__pcm_repository_BasicComponent86", None)
        self.__pcm_repository_BasicComponent86 = value if value is not None else set()
        
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
                    

    @property
    def pcm_repository_BasicComponent84(self):
        return self.__pcm_repository_BasicComponent84

    @pcm_repository_BasicComponent84.setter
    def pcm_repository_BasicComponent84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_BasicComponent__pcm_repository_BasicComponent84", None)
        self.__pcm_repository_BasicComponent84 = value if value is not None else set()
        
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
    def pcm_repository_BasicComponent(self):
        return self.__pcm_repository_BasicComponent

    @pcm_repository_BasicComponent.setter
    def pcm_repository_BasicComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_BasicComponent__pcm_repository_BasicComponent", None)
        self.__pcm_repository_BasicComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ImplementationComponentType82"):
                opp_val = getattr(old_value, "ImplementationComponentType82", None)
                if opp_val == self:
                    setattr(old_value, "ImplementationComponentType82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ImplementationComponentType82"):
                opp_val = getattr(value, "ImplementationComponentType82", None)
                setattr(value, "ImplementationComponentType82", self)

    def NoSeffTypeUsedTwice(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement NoSeffTypeUsedTwice method
        pass

    def RequireSameInterfacesAsImplementationType(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement RequireSameInterfacesAsImplementationType method
        pass

    def ProvideSameInterfacesAsImplementationType(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement ProvideSameInterfacesAsImplementationType method
        pass

class entity_ComposedProvidingRequiringEntity:

    pass
class repository_ImplementationComponentType:

    pass
class pcm_repository_CompositeComponent(entity_ComposedProvidingRequiringEntity, repository_ImplementationComponentType):

    def __init__(self, pcm_repository_CompositeComponent: "ImplementationComponentType" = None):
        self.pcm_repository_CompositeComponent = pcm_repository_CompositeComponent
        
        pass
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

    def RequireSameInterfaces(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement RequireSameInterfaces method
        pass

    def ProvideSameInterfaces(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement ProvideSameInterfaces method
        pass

class Connector:

    pass
class pcm_repository_DelegationConnector(Connector):

    pass
class CompleteComponentType:

    pass
class pcm_repository_ImplementationComponentType(CompleteComponentType):

    def __init__(self, pcm_repository_ImplementationComponentType: set["CompleteComponentType"] = None, pcm_repository_ImplementationComponentType76: set["VariableUsage"] = None, CompleteComponentType: "pcm_repository_ImplementationComponentType" = None):
        self.pcm_repository_ImplementationComponentType = pcm_repository_ImplementationComponentType if pcm_repository_ImplementationComponentType is not None else set()
        self.pcm_repository_ImplementationComponentType76 = pcm_repository_ImplementationComponentType76 if pcm_repository_ImplementationComponentType76 is not None else set()
        
        pass
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
                    

    @property
    def pcm_repository_ImplementationComponentType76(self):
        return self.__pcm_repository_ImplementationComponentType76

    @pcm_repository_ImplementationComponentType76.setter
    def pcm_repository_ImplementationComponentType76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_ImplementationComponentType__pcm_repository_ImplementationComponentType76", None)
        self.__pcm_repository_ImplementationComponentType76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableUsage77"):
                    opp_val = getattr(item, "VariableUsage77", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableUsage77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableUsage77"):
                    opp_val = getattr(item, "VariableUsage77", None)
                    
                    setattr(item, "VariableUsage77", self)
                    

    def RequiredInterfacesHaveToConformToCompleteType(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement RequiredInterfacesHaveToConformToCompleteType method
        pass

    def providedInterfacesHaveToConformToCompleteType(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement providedInterfacesHaveToConformToCompleteType method
        pass

class pcm_repository_ExceptionType:

    def __init__(self, exceptionName: str, exceptionMessage: str):
        self.exceptionName = exceptionName
        self.exceptionMessage = exceptionMessage
        
        pass
    @property
    def exceptionMessage(self):
        return self.__exceptionMessage

    @exceptionMessage.setter
    def exceptionMessage(self, exceptionMessage: str):
        self.__exceptionMessage = exceptionMessage


    @property
    def exceptionName(self):
        return self.__exceptionName

    @exceptionName.setter
    def exceptionName(self, exceptionName: str):
        self.__exceptionName = exceptionName


class Protocol:

    pass
class Role:

    pass
class pcm_repository_ProvidedRole(Role):

    pass
class pcm_repository_RequiredRole(Role):

    pass
class Repository:

    pass
class pcm_repository_DataType(ABC):

    pass
class Signature:

    pass
class pcm_repository_Parameter:

    def __init__(self, parameterName: str, modifier__Parameter: str, pcm_repository_Parameter: "DataType" = None, parameters__Signature: "Signature" = None):
        self.parameterName = parameterName
        self.modifier__Parameter = modifier__Parameter
        self.pcm_repository_Parameter = pcm_repository_Parameter
        self.parameters__Signature = parameters__Signature
        
        pass
    @property
    def modifier__Parameter(self):
        return self.__modifier__Parameter

    @modifier__Parameter.setter
    def modifier__Parameter(self, modifier__Parameter: str):
        self.__modifier__Parameter = modifier__Parameter


    @property
    def parameterName(self):
        return self.__parameterName

    @parameterName.setter
    def parameterName(self, parameterName: str):
        self.__parameterName = parameterName


    @property
    def parameters__Signature(self):
        return self.__parameters__Signature

    @parameters__Signature.setter
    def parameters__Signature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Parameter__parameters__Signature", None)
        self.__parameters__Signature = value
        
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
    def pcm_repository_Parameter(self):
        return self.__pcm_repository_Parameter

    @pcm_repository_Parameter.setter
    def pcm_repository_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Parameter__pcm_repository_Parameter", None)
        self.__pcm_repository_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType49"):
                opp_val = getattr(old_value, "DataType49", None)
                if opp_val == self:
                    setattr(old_value, "DataType49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType49"):
                opp_val = getattr(value, "DataType49", None)
                setattr(value, "DataType49", self)

class ExceptionType:

    pass
class DataType:

    pass
class pcm_repository_PrimitiveDataType(DataType):

    def __init__(self, type: str, DataType57: "pcm_repository_Repository" = None, DataType49: "pcm_repository_Parameter" = None, DataType93: "pcm_repository_InnerDeclaration" = None, DataType88: "pcm_repository_CollectionDataType" = None, DataType: "pcm_repository_Signature" = None):
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class Interface:

    pass
class Parameter:

    pass
class pcm_repository_Signature:

    def __init__(self, serviceName: str, signature_Parameter: set["Parameter"] = None, signatures__Interface: "Interface" = None, pcm_repository_Signature: "DataType" = None, pcm_repository_Signature47: set["ExceptionType"] = None):
        self.serviceName = serviceName
        self.signature_Parameter = signature_Parameter if signature_Parameter is not None else set()
        self.signatures__Interface = signatures__Interface
        self.pcm_repository_Signature = pcm_repository_Signature
        self.pcm_repository_Signature47 = pcm_repository_Signature47 if pcm_repository_Signature47 is not None else set()
        
        pass
    @property
    def serviceName(self):
        return self.__serviceName

    @serviceName.setter
    def serviceName(self, serviceName: str):
        self.__serviceName = serviceName


    @property
    def signatures__Interface(self):
        return self.__signatures__Interface

    @signatures__Interface.setter
    def signatures__Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Signature__signatures__Interface", None)
        self.__signatures__Interface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Interface"):
                opp_val = getattr(old_value, "Interface", None)
                if opp_val == self:
                    setattr(old_value, "Interface", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Interface"):
                opp_val = getattr(value, "Interface", None)
                setattr(value, "Interface", self)

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
    def pcm_repository_Signature47(self):
        return self.__pcm_repository_Signature47

    @pcm_repository_Signature47.setter
    def pcm_repository_Signature47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Signature__pcm_repository_Signature47", None)
        self.__pcm_repository_Signature47 = value if value is not None else set()
        
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
                    

    @property
    def signature_Parameter(self):
        return self.__signature_Parameter

    @signature_Parameter.setter
    def signature_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Signature__signature_Parameter", None)
        self.__signature_Parameter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    setattr(item, "Parameter", self)
                    

    def ParameterNamesHaveToBeUniqueForASignature(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement ParameterNamesHaveToBeUniqueForASignature method
        pass

class PCMRandomVariable:

    pass
class composition_AssemblyConnector:

    pass
class composition_RequiredDelegationConnector:

    pass
class composition_ProvidedDelegationConnector:

    pass
class entity_Entity:

    pass
class pcm_repository_CollectionDataType(entity_Entity, repository_DataType):

    pass
class pcm_repository_CompositeDataType(entity_Entity, repository_DataType):

    pass
class pcm_system_System(entity_ComposedProvidingRequiringEntity, entity_Entity):

    pass
class pcm_resourcetype_ResourceType(entity_Entity, UnitCarryingElement):

    pass
class connectors_Connector:

    pass
class pcm_composition_AssemblyConnector(entity_Entity, connectors_Connector):

    pass
class VariableUsage:

    pass
class ProvidesComponentType:

    pass
class pcm_repository_CompleteComponentType(ProvidesComponentType):

    def __init__(self, pcm_repository_CompleteComponentType: set["ProvidesComponentType"] = None, ProvidesComponentType53: "pcm_repository_Repository" = None, ProvidesComponentType: "pcm_composition_AssemblyContext" = None, ProvidesComponentType79: "pcm_repository_CompleteComponentType" = None):
        self.pcm_repository_CompleteComponentType = pcm_repository_CompleteComponentType if pcm_repository_CompleteComponentType is not None else set()
        
        pass
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
                if hasattr(item, "ProvidesComponentType79"):
                    opp_val = getattr(item, "ProvidesComponentType79", None)
                    
                    if opp_val == self:
                        setattr(item, "ProvidesComponentType79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProvidesComponentType79"):
                    opp_val = getattr(item, "ProvidesComponentType79", None)
                    
                    setattr(item, "ProvidesComponentType79", self)
                    

    def AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType method
        pass

    def providedInterfacesHaveToConformToProvidedType2(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement providedInterfacesHaveToConformToProvidedType2 method
        pass

class composition_AssemblyContext:

    pass
class DelegationConnector:

    pass
class pcm_composition_RequiredDelegationConnector(DelegationConnector):

    def __init__(self, pcm_composition_RequiredDelegationConnector: "RequiredRole" = None, pcm_composition_RequiredDelegationConnector18: "RequiredRole" = None, pcm_composition_RequiredDelegationConnector21: "composition_AssemblyContext" = None, requiredDelegationConnectors_ComposedStructure: "composition_ComposedStructure" = None):
        self.pcm_composition_RequiredDelegationConnector = pcm_composition_RequiredDelegationConnector
        self.pcm_composition_RequiredDelegationConnector18 = pcm_composition_RequiredDelegationConnector18
        self.pcm_composition_RequiredDelegationConnector21 = pcm_composition_RequiredDelegationConnector21
        self.requiredDelegationConnectors_ComposedStructure = requiredDelegationConnectors_ComposedStructure
        
        pass
    @property
    def pcm_composition_RequiredDelegationConnector21(self):
        return self.__pcm_composition_RequiredDelegationConnector21

    @pcm_composition_RequiredDelegationConnector21.setter
    def pcm_composition_RequiredDelegationConnector21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_RequiredDelegationConnector__pcm_composition_RequiredDelegationConnector21", None)
        self.__pcm_composition_RequiredDelegationConnector21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_AssemblyContext22"):
                opp_val = getattr(old_value, "composition_AssemblyContext22", None)
                if opp_val == self:
                    setattr(old_value, "composition_AssemblyContext22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_AssemblyContext22"):
                opp_val = getattr(value, "composition_AssemblyContext22", None)
                setattr(value, "composition_AssemblyContext22", self)

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
            if hasattr(old_value, "RequiredRole16"):
                opp_val = getattr(old_value, "RequiredRole16", None)
                if opp_val == self:
                    setattr(old_value, "RequiredRole16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RequiredRole16"):
                opp_val = getattr(value, "RequiredRole16", None)
                setattr(value, "RequiredRole16", self)

    @property
    def requiredDelegationConnectors_ComposedStructure(self):
        return self.__requiredDelegationConnectors_ComposedStructure

    @requiredDelegationConnectors_ComposedStructure.setter
    def requiredDelegationConnectors_ComposedStructure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_RequiredDelegationConnector__requiredDelegationConnectors_ComposedStructure", None)
        self.__requiredDelegationConnectors_ComposedStructure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ComposedStructure24"):
                opp_val = getattr(old_value, "ComposedStructure24", None)
                if opp_val == self:
                    setattr(old_value, "ComposedStructure24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ComposedStructure24"):
                opp_val = getattr(value, "ComposedStructure24", None)
                setattr(value, "ComposedStructure24", self)

    @property
    def pcm_composition_RequiredDelegationConnector18(self):
        return self.__pcm_composition_RequiredDelegationConnector18

    @pcm_composition_RequiredDelegationConnector18.setter
    def pcm_composition_RequiredDelegationConnector18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_RequiredDelegationConnector__pcm_composition_RequiredDelegationConnector18", None)
        self.__pcm_composition_RequiredDelegationConnector18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RequiredRole19"):
                opp_val = getattr(old_value, "RequiredRole19", None)
                if opp_val == self:
                    setattr(old_value, "RequiredRole19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RequiredRole19"):
                opp_val = getattr(value, "RequiredRole19", None)
                setattr(value, "RequiredRole19", self)

    def ComponentOfChildComponentContextAndInnerRoleRequiringComponentNeedToBeTheSame(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement ComponentOfChildComponentContextAndInnerRoleRequiringComponentNeedToBeTheSame method
        pass

    def RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

class pcm_composition_ProvidedDelegationConnector(DelegationConnector):

    def __init__(self, pcm_composition_ProvidedDelegationConnector: "ProvidedRole" = None, pcm_composition_ProvidedDelegationConnector5: "ProvidedRole" = None, pcm_composition_ProvidedDelegationConnector8: "composition_AssemblyContext" = None, providedDelegationConnectors_ComposedStructure: "composition_ComposedStructure" = None):
        self.pcm_composition_ProvidedDelegationConnector = pcm_composition_ProvidedDelegationConnector
        self.pcm_composition_ProvidedDelegationConnector5 = pcm_composition_ProvidedDelegationConnector5
        self.pcm_composition_ProvidedDelegationConnector8 = pcm_composition_ProvidedDelegationConnector8
        self.providedDelegationConnectors_ComposedStructure = providedDelegationConnectors_ComposedStructure
        
        pass
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
            if hasattr(old_value, "ProvidedRole3"):
                opp_val = getattr(old_value, "ProvidedRole3", None)
                if opp_val == self:
                    setattr(old_value, "ProvidedRole3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProvidedRole3"):
                opp_val = getattr(value, "ProvidedRole3", None)
                setattr(value, "ProvidedRole3", self)

    @property
    def providedDelegationConnectors_ComposedStructure(self):
        return self.__providedDelegationConnectors_ComposedStructure

    @providedDelegationConnectors_ComposedStructure.setter
    def providedDelegationConnectors_ComposedStructure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_ProvidedDelegationConnector__providedDelegationConnectors_ComposedStructure", None)
        self.__providedDelegationConnectors_ComposedStructure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ComposedStructure"):
                opp_val = getattr(old_value, "ComposedStructure", None)
                if opp_val == self:
                    setattr(old_value, "ComposedStructure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ComposedStructure"):
                opp_val = getattr(value, "ComposedStructure", None)
                setattr(value, "ComposedStructure", self)

    @property
    def pcm_composition_ProvidedDelegationConnector5(self):
        return self.__pcm_composition_ProvidedDelegationConnector5

    @pcm_composition_ProvidedDelegationConnector5.setter
    def pcm_composition_ProvidedDelegationConnector5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_ProvidedDelegationConnector__pcm_composition_ProvidedDelegationConnector5", None)
        self.__pcm_composition_ProvidedDelegationConnector5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProvidedRole6"):
                opp_val = getattr(old_value, "ProvidedRole6", None)
                if opp_val == self:
                    setattr(old_value, "ProvidedRole6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProvidedRole6"):
                opp_val = getattr(value, "ProvidedRole6", None)
                setattr(value, "ProvidedRole6", self)

    @property
    def pcm_composition_ProvidedDelegationConnector8(self):
        return self.__pcm_composition_ProvidedDelegationConnector8

    @pcm_composition_ProvidedDelegationConnector8.setter
    def pcm_composition_ProvidedDelegationConnector8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_ProvidedDelegationConnector__pcm_composition_ProvidedDelegationConnector8", None)
        self.__pcm_composition_ProvidedDelegationConnector8 = value
        
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

    def ComponentOfChildComponentContextAndInnerRoleProvidingComponentNeedToBeTheSame(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement ComponentOfChildComponentContextAndInnerRoleProvidingComponentNeedToBeTheSame method
        pass

    def ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

class entity_InterfaceProvidingRequiringEntity:

    pass
class pcm_repository_ProvidesComponentType(entity_Entity, entity_InterfaceProvidingRequiringEntity):

    def __init__(self, components__Repository: "Repository" = None):
        self.components__Repository = components__Repository
        
        pass
    @property
    def components__Repository(self):
        return self.__components__Repository

    @components__Repository.setter
    def components__Repository(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_ProvidesComponentType__components__Repository", None)
        self.__components__Repository = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Repository59"):
                opp_val = getattr(old_value, "Repository59", None)
                if opp_val == self:
                    setattr(old_value, "Repository59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Repository59"):
                opp_val = getattr(value, "Repository59", None)
                setattr(value, "Repository59", self)

    def AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType method
        pass

class composition_ComposedStructure:

    pass
class pcm_entity_ComposedProvidingRequiringEntity(composition_ComposedStructure, entity_InterfaceProvidingRequiringEntity):

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
class pcm_resourceenvironment_ResourceContainer(Entity):

    pass
class pcm_entity_InterfaceRequiringEntity(Entity):

    pass
class pcm_usagemodel_ScenarioBehaviour(Entity):

    def __init__(self, pcm_usagemodel_ScenarioBehaviour: set["AbstractUserAction"] = None):
        self.pcm_usagemodel_ScenarioBehaviour = pcm_usagemodel_ScenarioBehaviour if pcm_usagemodel_ScenarioBehaviour is not None else set()
        
        pass
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
                    

    def EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor method
        pass

    def Exactlyonestart(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement Exactlyonestart method
        pass

    def Exactlyonestop(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement Exactlyonestop method
        pass

class pcm_repository_Role(Entity):

    pass
class pcm_usagemodel_UsageScenario(Entity):

    pass
class pcm_usagemodel_AbstractUserAction(Entity):

    pass
class pcm_connectors_Connector(Entity):

    pass
class pcm_allocation_AllocationContext(Entity):

    pass
class pcm_repository_Interface(Entity):

    def __init__(self, pcm_repository_Interface66: set["Interface"] = None, pcm_repository_Interface69: set["Protocol"] = None, interface_Signature: set["Signature"] = None, interfaces__Repository: "Repository" = None, pcm_repository_Interface: set["Interface"] = None):
        self.pcm_repository_Interface66 = pcm_repository_Interface66 if pcm_repository_Interface66 is not None else set()
        self.pcm_repository_Interface69 = pcm_repository_Interface69 if pcm_repository_Interface69 is not None else set()
        self.interface_Signature = interface_Signature if interface_Signature is not None else set()
        self.interfaces__Repository = interfaces__Repository
        self.pcm_repository_Interface = pcm_repository_Interface if pcm_repository_Interface is not None else set()
        
        pass
    @property
    def pcm_repository_Interface69(self):
        return self.__pcm_repository_Interface69

    @pcm_repository_Interface69.setter
    def pcm_repository_Interface69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Interface__pcm_repository_Interface69", None)
        self.__pcm_repository_Interface69 = value if value is not None else set()
        
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
    def pcm_repository_Interface66(self):
        return self.__pcm_repository_Interface66

    @pcm_repository_Interface66.setter
    def pcm_repository_Interface66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Interface__pcm_repository_Interface66", None)
        self.__pcm_repository_Interface66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Interface67"):
                    opp_val = getattr(item, "Interface67", None)
                    
                    if opp_val == self:
                        setattr(item, "Interface67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Interface67"):
                    opp_val = getattr(item, "Interface67", None)
                    
                    setattr(item, "Interface67", self)
                    

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
                if hasattr(item, "Interface64"):
                    opp_val = getattr(item, "Interface64", None)
                    
                    if opp_val == self:
                        setattr(item, "Interface64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Interface64"):
                    opp_val = getattr(item, "Interface64", None)
                    
                    setattr(item, "Interface64", self)
                    

    @property
    def interface_Signature(self):
        return self.__interface_Signature

    @interface_Signature.setter
    def interface_Signature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Interface__interface_Signature", None)
        self.__interface_Signature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Signature71"):
                    opp_val = getattr(item, "Signature71", None)
                    
                    if opp_val == self:
                        setattr(item, "Signature71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Signature71"):
                    opp_val = getattr(item, "Signature71", None)
                    
                    setattr(item, "Signature71", self)
                    

    @property
    def interfaces__Repository(self):
        return self.__interfaces__Repository

    @interfaces__Repository.setter
    def interfaces__Repository(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Interface__interfaces__Repository", None)
        self.__interfaces__Repository = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Repository73"):
                opp_val = getattr(old_value, "Repository73", None)
                if opp_val == self:
                    setattr(old_value, "Repository73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Repository73"):
                opp_val = getattr(value, "Repository73", None)
                setattr(value, "Repository73", self)

    def NoProtocolTypeIDUsedTwice(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement NoProtocolTypeIDUsedTwice method
        pass

    def SignaturesHaveToBeUniqueForAnInterface(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement SignaturesHaveToBeUniqueForAnInterface method
        pass

class pcm_seff_AbstractAction(Entity):

    pass
class pcm_allocation_Allocation(Entity):

    def __init__(self, pcm_allocation_Allocation: set["AllocationContext"] = None, pcm_allocation_Allocation158: "ResourceEnvironment" = None, pcm_allocation_Allocation160: "System" = None):
        self.pcm_allocation_Allocation = pcm_allocation_Allocation if pcm_allocation_Allocation is not None else set()
        self.pcm_allocation_Allocation158 = pcm_allocation_Allocation158
        self.pcm_allocation_Allocation160 = pcm_allocation_Allocation160
        
        pass
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
    def pcm_allocation_Allocation160(self):
        return self.__pcm_allocation_Allocation160

    @pcm_allocation_Allocation160.setter
    def pcm_allocation_Allocation160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_allocation_Allocation__pcm_allocation_Allocation160", None)
        self.__pcm_allocation_Allocation160 = value
        
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
    def pcm_allocation_Allocation158(self):
        return self.__pcm_allocation_Allocation158

    @pcm_allocation_Allocation158.setter
    def pcm_allocation_Allocation158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_allocation_Allocation__pcm_allocation_Allocation158", None)
        self.__pcm_allocation_Allocation158 = value
        
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

    def EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce method
        pass

class pcm_repository_Repository(Entity):

    def __init__(self, repositoryDescription: str, repository_ProvidesComponentType: set["ProvidesComponentType"] = None, repository_Interface: set["Interface"] = None, repository_DataType: set["DataType"] = None):
        self.repositoryDescription = repositoryDescription
        self.repository_ProvidesComponentType = repository_ProvidesComponentType if repository_ProvidesComponentType is not None else set()
        self.repository_Interface = repository_Interface if repository_Interface is not None else set()
        self.repository_DataType = repository_DataType if repository_DataType is not None else set()
        
        pass
    @property
    def repositoryDescription(self):
        return self.__repositoryDescription

    @repositoryDescription.setter
    def repositoryDescription(self, repositoryDescription: str):
        self.__repositoryDescription = repositoryDescription


    @property
    def repository_DataType(self):
        return self.__repository_DataType

    @repository_DataType.setter
    def repository_DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Repository__repository_DataType", None)
        self.__repository_DataType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataType57"):
                    opp_val = getattr(item, "DataType57", None)
                    
                    if opp_val == self:
                        setattr(item, "DataType57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataType57"):
                    opp_val = getattr(item, "DataType57", None)
                    
                    setattr(item, "DataType57", self)
                    

    @property
    def repository_Interface(self):
        return self.__repository_Interface

    @repository_Interface.setter
    def repository_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Repository__repository_Interface", None)
        self.__repository_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Interface55"):
                    opp_val = getattr(item, "Interface55", None)
                    
                    if opp_val == self:
                        setattr(item, "Interface55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Interface55"):
                    opp_val = getattr(item, "Interface55", None)
                    
                    setattr(item, "Interface55", self)
                    

    @property
    def repository_ProvidesComponentType(self):
        return self.__repository_ProvidesComponentType

    @repository_ProvidesComponentType.setter
    def repository_ProvidesComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Repository__repository_ProvidesComponentType", None)
        self.__repository_ProvidesComponentType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProvidesComponentType53"):
                    opp_val = getattr(item, "ProvidesComponentType53", None)
                    
                    if opp_val == self:
                        setattr(item, "ProvidesComponentType53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProvidesComponentType53"):
                    opp_val = getattr(item, "ProvidesComponentType53", None)
                    
                    setattr(item, "ProvidesComponentType53", self)
                    

class pcm_composition_AssemblyContext(Entity):

    pass
class pcm_repository_PassiveResource(Entity):

    pass
class pcm_qosannotations_QoSAnnotations(Entity):

    pass
class pcm_resourceenvironment_LinkingResource(Entity):

    pass
class pcm_composition_ComposedStructure(Entity):

    pass
class pcm_entity_InterfaceProvidingEntity(Entity):

    pass
class pcm_entity_NamedElement(ABC):

    def __init__(self, entityName: str):
        self.entityName = entityName
        
        pass
    @property
    def entityName(self):
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
class pcm_seff_ResourceDemandingSEFF(seff_ServiceEffectSpecification, Identifier, seff_ResourceDemandingBehaviour):

    pass
class pcm_entity_Entity(Identifier, entity_NamedElement):

    pass
class RandomVariable:

    pass
class pcm_core_PCMRandomVariable(RandomVariable):

    def __init__(self):
        
        pass
    def SpecificationMustNotBeNULL(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement SpecificationMustNotBeNULL method
        pass
