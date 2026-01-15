from datetime import datetime, date, time
from abc import ABC, abstractmethod

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
    in = "in"
    out = "out"
    inout = "inout"
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


############################################
# Definition of Classes
############################################

class repository_RepositoryComponent:

    pass
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
            if hasattr(old_value, "ScenarioBehaviour287"):
                opp_val = getattr(old_value, "ScenarioBehaviour287", None)
                if opp_val == self:
                    setattr(old_value, "ScenarioBehaviour287", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ScenarioBehaviour287"):
                opp_val = getattr(value, "ScenarioBehaviour287", None)
                setattr(value, "ScenarioBehaviour287", self)

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
class pcm_usagemodel_Loop(AbstractUserAction):

    pass
class pcm_usagemodel_Delay(AbstractUserAction):

    pass
class pcm_usagemodel_Branch(AbstractUserAction):

    def __init__(self, pcm_usagemodel_Branch: set["BranchTransition"] = None, usagemodel256: "pcm_usagemodel_AbstractUserAction", AbstractUserAction: "pcm_usagemodel_ScenarioBehaviour", usagemodel: "pcm_usagemodel_AbstractUserAction"):
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

class pcm_usagemodel_Start(AbstractUserAction):

    def __init__(self, usagemodel256: "pcm_usagemodel_AbstractUserAction", AbstractUserAction: "pcm_usagemodel_ScenarioBehaviour", usagemodel: "pcm_usagemodel_AbstractUserAction"):
        
    def StartHasNoPredecessor(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement StartHasNoPredecessor method
        pass

class pcm_usagemodel_Stop(AbstractUserAction):

    def __init__(self, usagemodel256: "pcm_usagemodel_AbstractUserAction", AbstractUserAction: "pcm_usagemodel_ScenarioBehaviour", usagemodel: "pcm_usagemodel_AbstractUserAction"):
        
    def StopHasNoSuccessor(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement StopHasNoSuccessor method
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
            if hasattr(old_value, "PCMRandomVariable266"):
                opp_val = getattr(old_value, "PCMRandomVariable266", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable266", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable266"):
                opp_val = getattr(value, "PCMRandomVariable266", None)
                setattr(value, "PCMRandomVariable266", self)

    def InterArrivalTimeInOpenWorkloadNeedsToBeSpecified(self, context: str, diagnostics: str) -> bool:
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
            if hasattr(old_value, "PCMRandomVariable284"):
                opp_val = getattr(old_value, "PCMRandomVariable284", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable284"):
                opp_val = getattr(value, "PCMRandomVariable284", None)
                setattr(value, "PCMRandomVariable284", self)

    def ThinkTimeInClosedWorkloadNeedsToBeSpecified(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ThinkTimeInClosedWorkloadNeedsToBeSpecified method
        pass

    def PopulationInClosedWorkloadNeedsToBeSpecified(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement PopulationInClosedWorkloadNeedsToBeSpecified method
        pass

class pcm_usagemodel_Workload(ABC):

    pass
class pcm_qosannotations_SpecifiedQoSAnnotation(ABC):

    pass
class QoSAnnotations:

    pass
class ProcessingResourceSpecification:

    pass
class SpecifiedOutputParameterAbstraction:

    pass
class SpecifiedQoSAnnotation:

    pass
class pcm_performance_ComponentSpecifiedExecutionTime(SpecifiedQoSAnnotation):

    pass
class pcm_reliability_SpecifiedFailureProbability(SpecifiedQoSAnnotation):

    def __init__(self, failureProbability: float, SpecifiedQoSAnnotation: "pcm_qosannotations_QoSAnnotations"):
        self.failureProbability = failureProbability
        
    @property
    def failureProbability(self) -> float:
        return self.__failureProbability

    @failureProbability.setter
    def failureProbability(self, failureProbability: float):
        self.__failureProbability = failureProbability

class pcm_performance_SystemSpecifiedExecutionTime(SpecifiedQoSAnnotation):

    pass
class pcm_qosannotations_SpecifiedOutputParameterAbstraction(ABC):

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
class pcm_resourceenvironment_ProcessingResourceSpecification:

    def __init__(self, MTTR: float, MTTF: float, schedulingPolicy: str, pcm_resourceenvironment_ProcessingResourceSpecification: "ProcessingResourceType" = None, pcm_resourceenvironment_ProcessingResourceSpecification223: "PCMRandomVariable" = None):
        self.MTTR = MTTR
        self.MTTF = MTTF
        self.schedulingPolicy = schedulingPolicy
        self.pcm_resourceenvironment_ProcessingResourceSpecification = pcm_resourceenvironment_ProcessingResourceSpecification
        self.pcm_resourceenvironment_ProcessingResourceSpecification223 = pcm_resourceenvironment_ProcessingResourceSpecification223
        
    @property
    def schedulingPolicy(self) -> str:
        return self.__schedulingPolicy

    @schedulingPolicy.setter
    def schedulingPolicy(self, schedulingPolicy: str):
        self.__schedulingPolicy = schedulingPolicy

    @property
    def MTTR(self) -> float:
        return self.__MTTR

    @MTTR.setter
    def MTTR(self, MTTR: float):
        self.__MTTR = MTTR

    @property
    def MTTF(self) -> float:
        return self.__MTTF

    @MTTF.setter
    def MTTF(self, MTTF: float):
        self.__MTTF = MTTF

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
            if hasattr(old_value, "ProcessingResourceType221"):
                opp_val = getattr(old_value, "ProcessingResourceType221", None)
                if opp_val == self:
                    setattr(old_value, "ProcessingResourceType221", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessingResourceType221"):
                opp_val = getattr(value, "ProcessingResourceType221", None)
                setattr(value, "ProcessingResourceType221", self)

    @property
    def pcm_resourceenvironment_ProcessingResourceSpecification223(self):
        return self.__pcm_resourceenvironment_ProcessingResourceSpecification223

    @pcm_resourceenvironment_ProcessingResourceSpecification223.setter
    def pcm_resourceenvironment_ProcessingResourceSpecification223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_resourceenvironment_ProcessingResourceSpecification__pcm_resourceenvironment_ProcessingResourceSpecification223", None)
        self.__pcm_resourceenvironment_ProcessingResourceSpecification223 = value
        
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

class CommunicationLinkResourceType:

    pass
class pcm_resourceenvironment_CommunicationLinkResourceSpecification:

    def __init__(self, failureProbability: float, pcm_resourceenvironment_CommunicationLinkResourceSpecification: "CommunicationLinkResourceType" = None, pcm_resourceenvironment_CommunicationLinkResourceSpecification215: "PCMRandomVariable" = None, pcm_resourceenvironment_CommunicationLinkResourceSpecification218: "PCMRandomVariable" = None):
        self.failureProbability = failureProbability
        self.pcm_resourceenvironment_CommunicationLinkResourceSpecification = pcm_resourceenvironment_CommunicationLinkResourceSpecification
        self.pcm_resourceenvironment_CommunicationLinkResourceSpecification215 = pcm_resourceenvironment_CommunicationLinkResourceSpecification215
        self.pcm_resourceenvironment_CommunicationLinkResourceSpecification218 = pcm_resourceenvironment_CommunicationLinkResourceSpecification218
        
    @property
    def failureProbability(self) -> float:
        return self.__failureProbability

    @failureProbability.setter
    def failureProbability(self, failureProbability: float):
        self.__failureProbability = failureProbability

    @property
    def pcm_resourceenvironment_CommunicationLinkResourceSpecification218(self):
        return self.__pcm_resourceenvironment_CommunicationLinkResourceSpecification218

    @pcm_resourceenvironment_CommunicationLinkResourceSpecification218.setter
    def pcm_resourceenvironment_CommunicationLinkResourceSpecification218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_resourceenvironment_CommunicationLinkResourceSpecification__pcm_resourceenvironment_CommunicationLinkResourceSpecification218", None)
        self.__pcm_resourceenvironment_CommunicationLinkResourceSpecification218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable219"):
                opp_val = getattr(old_value, "PCMRandomVariable219", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable219"):
                opp_val = getattr(value, "PCMRandomVariable219", None)
                setattr(value, "PCMRandomVariable219", self)

    @property
    def pcm_resourceenvironment_CommunicationLinkResourceSpecification(self):
        return self.__pcm_resourceenvironment_CommunicationLinkResourceSpecification

    @pcm_resourceenvironment_CommunicationLinkResourceSpecification.setter
    def pcm_resourceenvironment_CommunicationLinkResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_resourceenvironment_CommunicationLinkResourceSpecification__pcm_resourceenvironment_CommunicationLinkResourceSpecification", None)
        self.__pcm_resourceenvironment_CommunicationLinkResourceSpecification = value
        
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

    @property
    def pcm_resourceenvironment_CommunicationLinkResourceSpecification215(self):
        return self.__pcm_resourceenvironment_CommunicationLinkResourceSpecification215

    @pcm_resourceenvironment_CommunicationLinkResourceSpecification215.setter
    def pcm_resourceenvironment_CommunicationLinkResourceSpecification215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_resourceenvironment_CommunicationLinkResourceSpecification__pcm_resourceenvironment_CommunicationLinkResourceSpecification215", None)
        self.__pcm_resourceenvironment_CommunicationLinkResourceSpecification215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable216"):
                opp_val = getattr(old_value, "PCMRandomVariable216", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable216"):
                opp_val = getattr(value, "PCMRandomVariable216", None)
                setattr(value, "PCMRandomVariable216", self)

class ProcessingResourceType:

    pass
class pcm_performance_ParametricResourceDemand:

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
            if hasattr(old_value, "Signature185"):
                opp_val = getattr(old_value, "Signature185", None)
                if opp_val == self:
                    setattr(old_value, "Signature185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Signature185"):
                opp_val = getattr(value, "Signature185", None)
                setattr(value, "Signature185", self)

class ResourceContainer:

    pass
class pcm_resourcetype_CommunicationLinkResourceType(ProcessingResourceType):

    pass
class ResourceType:

    pass
class pcm_resourcetype_ProcessingResourceType(ResourceType):

    pass
class pcm_resourcetype_ResourceRepository:

    pass
class UnitCarryingElement:

    pass
class AbstractBranchTransition:

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

class pcm_seff_GuardedBranchTransition(AbstractBranchTransition):

    pass
class ResourceDemandingBehaviour:

    pass
class AbstractLoopAction:

    pass
class pcm_seff_CollectionIteratorAction(AbstractLoopAction):

    pass
class pcm_seff_LoopAction(AbstractLoopAction):

    pass
class pcm_seff_SynchronisationPoint:

    pass
class pcm_seff_ForkedBehaviour(ResourceDemandingBehaviour):

    pass
class SynchronisationPoint:

    pass
class ForkedBehaviour:

    pass
class seff_ResourceDemandingBehaviour:

    pass
class seff_ServiceEffectSpecification:

    pass
class performance_ParametricResourceDemand:

    pass
class AbstractAction:

    pass
class pcm_seff_ExternalCallAction(AbstractAction):

    def __init__(self, retryCount: int, pcm_seff_ExternalCallAction: "Signature" = None, pcm_seff_ExternalCallAction166: set["VariableUsage"] = None, pcm_seff_ExternalCallAction169: set["VariableUsage"] = None, pcm_seff_ExternalCallAction172: "Role" = None, seff144: "pcm_seff_AbstractAction", AbstractAction149: "pcm_seff_ResourceDemandingBehaviour", seff147: "pcm_seff_AbstractAction"):
        self.retryCount = retryCount
        self.pcm_seff_ExternalCallAction = pcm_seff_ExternalCallAction
        self.pcm_seff_ExternalCallAction166 = pcm_seff_ExternalCallAction166 if pcm_seff_ExternalCallAction166 is not None else set()
        self.pcm_seff_ExternalCallAction169 = pcm_seff_ExternalCallAction169 if pcm_seff_ExternalCallAction169 is not None else set()
        self.pcm_seff_ExternalCallAction172 = pcm_seff_ExternalCallAction172
        
    @property
    def retryCount(self) -> int:
        return self.__retryCount

    @retryCount.setter
    def retryCount(self, retryCount: int):
        self.__retryCount = retryCount

    @property
    def pcm_seff_ExternalCallAction166(self):
        return self.__pcm_seff_ExternalCallAction166

    @pcm_seff_ExternalCallAction166.setter
    def pcm_seff_ExternalCallAction166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_seff_ExternalCallAction__pcm_seff_ExternalCallAction166", None)
        self.__pcm_seff_ExternalCallAction166 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableUsage167"):
                    opp_val = getattr(item, "VariableUsage167", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableUsage167", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableUsage167"):
                    opp_val = getattr(item, "VariableUsage167", None)
                    
                    setattr(item, "VariableUsage167", self)
                    

    @property
    def pcm_seff_ExternalCallAction(self):
        return self.__pcm_seff_ExternalCallAction

    @pcm_seff_ExternalCallAction.setter
    def pcm_seff_ExternalCallAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_seff_ExternalCallAction__pcm_seff_ExternalCallAction", None)
        self.__pcm_seff_ExternalCallAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Signature164"):
                opp_val = getattr(old_value, "Signature164", None)
                if opp_val == self:
                    setattr(old_value, "Signature164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Signature164"):
                opp_val = getattr(value, "Signature164", None)
                setattr(value, "Signature164", self)

    @property
    def pcm_seff_ExternalCallAction172(self):
        return self.__pcm_seff_ExternalCallAction172

    @pcm_seff_ExternalCallAction172.setter
    def pcm_seff_ExternalCallAction172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_seff_ExternalCallAction__pcm_seff_ExternalCallAction172", None)
        self.__pcm_seff_ExternalCallAction172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Role"):
                opp_val = getattr(old_value, "Role", None)
                if opp_val == self:
                    setattr(old_value, "Role", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Role"):
                opp_val = getattr(value, "Role", None)
                setattr(value, "Role", self)

    @property
    def pcm_seff_ExternalCallAction169(self):
        return self.__pcm_seff_ExternalCallAction169

    @pcm_seff_ExternalCallAction169.setter
    def pcm_seff_ExternalCallAction169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_seff_ExternalCallAction__pcm_seff_ExternalCallAction169", None)
        self.__pcm_seff_ExternalCallAction169 = value if value is not None else set()
        
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
                    

class pcm_seff_AbstractInternalControlFlowAction(AbstractAction):

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
                if hasattr(item, "AbstractAction149"):
                    opp_val = getattr(item, "AbstractAction149", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractAction149", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractAction149"):
                    opp_val = getattr(item, "AbstractAction149", None)
                    
                    setattr(item, "AbstractAction149", self)
                    

    def ExactlyOneStopAction(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ExactlyOneStopAction method
        pass

    def EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor method
        pass

    def ExactlyOneStartAction(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ExactlyOneStartAction method
        pass

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
            if hasattr(old_value, "PCMRandomVariable138"):
                opp_val = getattr(old_value, "PCMRandomVariable138", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable138"):
                opp_val = getattr(value, "PCMRandomVariable138", None)
                setattr(value, "PCMRandomVariable138", self)

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
class AbstractInternalControlFlowAction:

    pass
class pcm_seff_ForkAction(AbstractInternalControlFlowAction):

    pass
class pcm_seff_SetVariableAction(AbstractInternalControlFlowAction):

    pass
class pcm_seff_StartAction(AbstractInternalControlFlowAction):

    def __init__(self, seff191: "pcm_performance_ParametricResourceDemand"):
        
    def StartActionPredecessorMustNotBeDefined(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement StartActionPredecessorMustNotBeDefined method
        pass

class pcm_seff_ReleaseAction(AbstractInternalControlFlowAction):

    pass
class pcm_seff_BranchAction(AbstractInternalControlFlowAction):

    def __init__(self, pcm_seff_BranchAction: set["AbstractBranchTransition"] = None, seff191: "pcm_performance_ParametricResourceDemand"):
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
                    

    def AllProbabilisticBranchProbabilitiesMustSumUpTo1(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AllProbabilisticBranchProbabilitiesMustSumUpTo1 method
        pass

    def EitherGuardedBranchesOrProbabilisiticBranchTransitions(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement EitherGuardedBranchesOrProbabilisiticBranchTransitions method
        pass

class pcm_seff_AcquireAction(AbstractInternalControlFlowAction):

    pass
class pcm_seff_InternalAction(AbstractInternalControlFlowAction):

    def __init__(self, failureProbability: float, seff191: "pcm_performance_ParametricResourceDemand"):
        self.failureProbability = failureProbability
        
    @property
    def failureProbability(self) -> float:
        return self.__failureProbability

    @failureProbability.setter
    def failureProbability(self, failureProbability: float):
        self.__failureProbability = failureProbability

class pcm_seff_AbstractLoopAction(AbstractInternalControlFlowAction):

    pass
class pcm_seff_StopAction(AbstractInternalControlFlowAction):

    def __init__(self, seff191: "pcm_performance_ParametricResourceDemand"):
        
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

class repository_DataType:

    pass
class entity_Entity:

    pass
class pcm_repository_CompositeDataType(entity_Entity, repository_DataType):

    pass
class pcm_resourcetype_ResourceType(entity_Entity, UnitCarryingElement):

    pass
class pcm_repository_CollectionDataType(entity_Entity, repository_DataType):

    pass
class PassiveResource:

    pass
class ServiceEffectSpecification:

    pass
class NamedElement:

    pass
class pcm_seff_AbstractBranchTransition(NamedElement):

    pass
class pcm_repository_InnerDeclaration(NamedElement):

    pass
class InnerDeclaration:

    pass
class CompositeDataType:

    pass
class repository_ImplementationComponentType:

    pass
class entity_ComposedProvidingRequiringEntity:

    pass
class pcm_subsystem_SubSystem(entity_ComposedProvidingRequiringEntity, repository_RepositoryComponent):

    pass
class pcm_system_System(entity_Entity, entity_ComposedProvidingRequiringEntity):

    pass
class pcm_repository_CompositeComponent(repository_ImplementationComponentType, entity_ComposedProvidingRequiringEntity):

    def __init__(self):
        
    def RequireSameInterfaces(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RequireSameInterfaces method
        pass

    def ProvideSameInterfaces(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ProvideSameInterfaces method
        pass

class ProvidesComponentType:

    pass
class ImplementationComponentType:

    pass
class pcm_repository_BasicComponent(ImplementationComponentType):

    def __init__(self, pcm_repository_BasicComponent: set["ServiceEffectSpecification"] = None, pcm_repository_BasicComponent122: set["PassiveResource"] = None):
        self.pcm_repository_BasicComponent = pcm_repository_BasicComponent if pcm_repository_BasicComponent is not None else set()
        self.pcm_repository_BasicComponent122 = pcm_repository_BasicComponent122 if pcm_repository_BasicComponent122 is not None else set()
        
    @property
    def pcm_repository_BasicComponent(self):
        return self.__pcm_repository_BasicComponent

    @pcm_repository_BasicComponent.setter
    def pcm_repository_BasicComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_BasicComponent__pcm_repository_BasicComponent", None)
        self.__pcm_repository_BasicComponent = value if value is not None else set()
        
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
    def pcm_repository_BasicComponent122(self):
        return self.__pcm_repository_BasicComponent122

    @pcm_repository_BasicComponent122.setter
    def pcm_repository_BasicComponent122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_BasicComponent__pcm_repository_BasicComponent122", None)
        self.__pcm_repository_BasicComponent122 = value if value is not None else set()
        
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
                    

    def NoSeffTypeUsedTwice(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement NoSeffTypeUsedTwice method
        pass

    def ProvideSameInterfacesAsImplementationType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ProvideSameInterfacesAsImplementationType method
        pass

    def RequireSameInterfacesAsImplementationType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement RequireSameInterfacesAsImplementationType method
        pass

class pcm_repository_ExceptionType:

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

class CompleteComponentType:

    pass
class Protocol:

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
            if hasattr(old_value, "DataType76"):
                opp_val = getattr(old_value, "DataType76", None)
                if opp_val == self:
                    setattr(old_value, "DataType76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType76"):
                opp_val = getattr(value, "DataType76", None)
                setattr(value, "DataType76", self)

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
            if hasattr(old_value, "repository78"):
                opp_val = getattr(old_value, "repository78", None)
                if opp_val == self:
                    setattr(old_value, "repository78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository78"):
                opp_val = getattr(value, "repository78", None)
                setattr(value, "repository78", self)

class Role:

    pass
class pcm_repository_ProvidedRole(Role):

    pass
class pcm_repository_ResourceRequiredRole(Role):

    pass
class pcm_repository_RequiredRole(Role):

    pass
class InterfaceProvidingRequiringEntity:

    pass
class pcm_repository_RepositoryComponent(InterfaceProvidingRequiringEntity):

    pass
class pcm_repository_Signature:

    def __init__(self, serviceName: str, Parameter: set["Parameter"] = None, Interface: "Interface" = None, pcm_repository_Signature: "DataType" = None, pcm_repository_Signature74: set["ExceptionType"] = None):
        self.serviceName = serviceName
        self.Parameter = Parameter if Parameter is not None else set()
        self.Interface = Interface
        self.pcm_repository_Signature = pcm_repository_Signature
        self.pcm_repository_Signature74 = pcm_repository_Signature74 if pcm_repository_Signature74 is not None else set()
        
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
            if hasattr(old_value, "repository71"):
                opp_val = getattr(old_value, "repository71", None)
                if opp_val == self:
                    setattr(old_value, "repository71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository71"):
                opp_val = getattr(value, "repository71", None)
                setattr(value, "repository71", self)

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
    def pcm_repository_Signature74(self):
        return self.__pcm_repository_Signature74

    @pcm_repository_Signature74.setter
    def pcm_repository_Signature74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Signature__pcm_repository_Signature74", None)
        self.__pcm_repository_Signature74 = value if value is not None else set()
        
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
                if hasattr(item, "repository69"):
                    opp_val = getattr(item, "repository69", None)
                    
                    if opp_val == self:
                        setattr(item, "repository69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository69"):
                    opp_val = getattr(item, "repository69", None)
                    
                    setattr(item, "repository69", self)
                    

    def ParameterNamesHaveToBeUniqueForASignature(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ParameterNamesHaveToBeUniqueForASignature method
        pass

class PCMRandomVariable:

    pass
class composition_ResourceRequiredDelegationConnector:

    pass
class composition_AssemblyConnector:

    pass
class ExceptionType:

    pass
class composition_RequiredDelegationConnector:

    pass
class DataType:

    pass
class pcm_repository_PrimitiveDataType(DataType):

    def __init__(self, type: str, DataType: "pcm_repository_Signature", DataType76: "pcm_repository_Parameter", repository89: "pcm_repository_Repository", DataType129: "pcm_repository_InnerDeclaration", DataType124: "pcm_repository_CollectionDataType"):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class Interface:

    pass
class Parameter:

    pass
class pcm_composition_ResourceRequiredDelegationConnector:

    pass
class composition_ProvidedDelegationConnector:

    pass
class Connector:

    pass
class pcm_repository_DelegationConnector(Connector):

    pass
class pcm_composition_AssemblyConnector(Connector):

    def __init__(self, pcm_composition_AssemblyConnector: "composition_AssemblyContext" = None, pcm_composition_AssemblyConnector33: "composition_AssemblyContext" = None, pcm_composition_AssemblyConnector36: "ProvidedRole" = None, pcm_composition_AssemblyConnector39: "RequiredRole" = None, composition42: "composition_ComposedStructure" = None):
        self.pcm_composition_AssemblyConnector = pcm_composition_AssemblyConnector
        self.pcm_composition_AssemblyConnector33 = pcm_composition_AssemblyConnector33
        self.pcm_composition_AssemblyConnector36 = pcm_composition_AssemblyConnector36
        self.pcm_composition_AssemblyConnector39 = pcm_composition_AssemblyConnector39
        self.composition42 = composition42
        
    @property
    def pcm_composition_AssemblyConnector36(self):
        return self.__pcm_composition_AssemblyConnector36

    @pcm_composition_AssemblyConnector36.setter
    def pcm_composition_AssemblyConnector36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_AssemblyConnector__pcm_composition_AssemblyConnector36", None)
        self.__pcm_composition_AssemblyConnector36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProvidedRole37"):
                opp_val = getattr(old_value, "ProvidedRole37", None)
                if opp_val == self:
                    setattr(old_value, "ProvidedRole37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProvidedRole37"):
                opp_val = getattr(value, "ProvidedRole37", None)
                setattr(value, "ProvidedRole37", self)

    @property
    def pcm_composition_AssemblyConnector(self):
        return self.__pcm_composition_AssemblyConnector

    @pcm_composition_AssemblyConnector.setter
    def pcm_composition_AssemblyConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_AssemblyConnector__pcm_composition_AssemblyConnector", None)
        self.__pcm_composition_AssemblyConnector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_AssemblyContext31"):
                opp_val = getattr(old_value, "composition_AssemblyContext31", None)
                if opp_val == self:
                    setattr(old_value, "composition_AssemblyContext31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_AssemblyContext31"):
                opp_val = getattr(value, "composition_AssemblyContext31", None)
                setattr(value, "composition_AssemblyContext31", self)

    @property
    def pcm_composition_AssemblyConnector39(self):
        return self.__pcm_composition_AssemblyConnector39

    @pcm_composition_AssemblyConnector39.setter
    def pcm_composition_AssemblyConnector39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_AssemblyConnector__pcm_composition_AssemblyConnector39", None)
        self.__pcm_composition_AssemblyConnector39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RequiredRole40"):
                opp_val = getattr(old_value, "RequiredRole40", None)
                if opp_val == self:
                    setattr(old_value, "RequiredRole40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RequiredRole40"):
                opp_val = getattr(value, "RequiredRole40", None)
                setattr(value, "RequiredRole40", self)

    @property
    def composition42(self):
        return self.__composition42

    @composition42.setter
    def composition42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_AssemblyConnector__composition42", None)
        self.__composition42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core43"):
                opp_val = getattr(old_value, "core43", None)
                if opp_val == self:
                    setattr(old_value, "core43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core43"):
                opp_val = getattr(value, "core43", None)
                setattr(value, "core43", self)

    @property
    def pcm_composition_AssemblyConnector33(self):
        return self.__pcm_composition_AssemblyConnector33

    @pcm_composition_AssemblyConnector33.setter
    def pcm_composition_AssemblyConnector33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_AssemblyConnector__pcm_composition_AssemblyConnector33", None)
        self.__pcm_composition_AssemblyConnector33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_AssemblyContext34"):
                opp_val = getattr(old_value, "composition_AssemblyContext34", None)
                if opp_val == self:
                    setattr(old_value, "composition_AssemblyContext34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_AssemblyContext34"):
                opp_val = getattr(value, "composition_AssemblyContext34", None)
                setattr(value, "composition_AssemblyContext34", self)

    def AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch method
        pass

    def AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch method
        pass

class composition_AssemblyContext:

    pass
class DelegationConnector:

    pass
class pcm_composition_ProvidedDelegationConnector(DelegationConnector):

    def __init__(self, pcm_composition_ProvidedDelegationConnector: "ProvidedRole" = None, pcm_composition_ProvidedDelegationConnector8: "ProvidedRole" = None, pcm_composition_ProvidedDelegationConnector11: "composition_AssemblyContext" = None, composition: "composition_ComposedStructure" = None):
        self.pcm_composition_ProvidedDelegationConnector = pcm_composition_ProvidedDelegationConnector
        self.pcm_composition_ProvidedDelegationConnector8 = pcm_composition_ProvidedDelegationConnector8
        self.pcm_composition_ProvidedDelegationConnector11 = pcm_composition_ProvidedDelegationConnector11
        self.composition = composition
        
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
            if hasattr(old_value, "ProvidedRole9"):
                opp_val = getattr(old_value, "ProvidedRole9", None)
                if opp_val == self:
                    setattr(old_value, "ProvidedRole9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProvidedRole9"):
                opp_val = getattr(value, "ProvidedRole9", None)
                setattr(value, "ProvidedRole9", self)

    @property
    def pcm_composition_ProvidedDelegationConnector11(self):
        return self.__pcm_composition_ProvidedDelegationConnector11

    @pcm_composition_ProvidedDelegationConnector11.setter
    def pcm_composition_ProvidedDelegationConnector11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_ProvidedDelegationConnector__pcm_composition_ProvidedDelegationConnector11", None)
        self.__pcm_composition_ProvidedDelegationConnector11 = value
        
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

    def ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame method
        pass

    def ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

class pcm_composition_RequiredDelegationConnector(DelegationConnector):

    def __init__(self, pcm_composition_RequiredDelegationConnector: "RequiredRole" = None, pcm_composition_RequiredDelegationConnector22: "RequiredRole" = None, pcm_composition_RequiredDelegationConnector25: "composition_AssemblyContext" = None, composition28: "composition_ComposedStructure" = None):
        self.pcm_composition_RequiredDelegationConnector = pcm_composition_RequiredDelegationConnector
        self.pcm_composition_RequiredDelegationConnector22 = pcm_composition_RequiredDelegationConnector22
        self.pcm_composition_RequiredDelegationConnector25 = pcm_composition_RequiredDelegationConnector25
        self.composition28 = composition28
        
    @property
    def composition28(self):
        return self.__composition28

    @composition28.setter
    def composition28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_RequiredDelegationConnector__composition28", None)
        self.__composition28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core29"):
                opp_val = getattr(old_value, "core29", None)
                if opp_val == self:
                    setattr(old_value, "core29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core29"):
                opp_val = getattr(value, "core29", None)
                setattr(value, "core29", self)

    @property
    def pcm_composition_RequiredDelegationConnector22(self):
        return self.__pcm_composition_RequiredDelegationConnector22

    @pcm_composition_RequiredDelegationConnector22.setter
    def pcm_composition_RequiredDelegationConnector22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_RequiredDelegationConnector__pcm_composition_RequiredDelegationConnector22", None)
        self.__pcm_composition_RequiredDelegationConnector22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RequiredRole23"):
                opp_val = getattr(old_value, "RequiredRole23", None)
                if opp_val == self:
                    setattr(old_value, "RequiredRole23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RequiredRole23"):
                opp_val = getattr(value, "RequiredRole23", None)
                setattr(value, "RequiredRole23", self)

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
            if hasattr(old_value, "RequiredRole20"):
                opp_val = getattr(old_value, "RequiredRole20", None)
                if opp_val == self:
                    setattr(old_value, "RequiredRole20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RequiredRole20"):
                opp_val = getattr(value, "RequiredRole20", None)
                setattr(value, "RequiredRole20", self)

    @property
    def pcm_composition_RequiredDelegationConnector25(self):
        return self.__pcm_composition_RequiredDelegationConnector25

    @pcm_composition_RequiredDelegationConnector25.setter
    def pcm_composition_RequiredDelegationConnector25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_RequiredDelegationConnector__pcm_composition_RequiredDelegationConnector25", None)
        self.__pcm_composition_RequiredDelegationConnector25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_AssemblyContext26"):
                opp_val = getattr(old_value, "composition_AssemblyContext26", None)
                if opp_val == self:
                    setattr(old_value, "composition_AssemblyContext26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_AssemblyContext26"):
                opp_val = getattr(value, "composition_AssemblyContext26", None)
                setattr(value, "composition_AssemblyContext26", self)

    def RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

    def ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame method
        pass

class VariableUsage:

    pass
class RepositoryComponent:

    pass
class pcm_repository_ImplementationComponentType(RepositoryComponent):

    def __init__(self, pcm_repository_ImplementationComponentType: set["CompleteComponentType"] = None, pcm_repository_ImplementationComponentType117: set["VariableUsage"] = None, repository83: "pcm_repository_Repository", RepositoryComponent: "pcm_composition_AssemblyContext"):
        self.pcm_repository_ImplementationComponentType = pcm_repository_ImplementationComponentType if pcm_repository_ImplementationComponentType is not None else set()
        self.pcm_repository_ImplementationComponentType117 = pcm_repository_ImplementationComponentType117 if pcm_repository_ImplementationComponentType117 is not None else set()
        
    @property
    def pcm_repository_ImplementationComponentType117(self):
        return self.__pcm_repository_ImplementationComponentType117

    @pcm_repository_ImplementationComponentType117.setter
    def pcm_repository_ImplementationComponentType117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_ImplementationComponentType__pcm_repository_ImplementationComponentType117", None)
        self.__pcm_repository_ImplementationComponentType117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableUsage118"):
                    opp_val = getattr(item, "VariableUsage118", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableUsage118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableUsage118"):
                    opp_val = getattr(item, "VariableUsage118", None)
                    
                    setattr(item, "VariableUsage118", self)
                    

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
                    

    def RequiredInterfacesHaveToConformToCompleteType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RequiredInterfacesHaveToConformToCompleteType method
        pass

    def providedInterfacesHaveToConformToCompleteType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement providedInterfacesHaveToConformToCompleteType method
        pass

class pcm_repository_CompleteComponentType(RepositoryComponent):

    def __init__(self, pcm_repository_CompleteComponentType: set["ProvidesComponentType"] = None, repository83: "pcm_repository_Repository", RepositoryComponent: "pcm_composition_AssemblyContext"):
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

class pcm_repository_ProvidesComponentType(RepositoryComponent):

    def __init__(self, repository83: "pcm_repository_Repository", RepositoryComponent: "pcm_composition_AssemblyContext"):
        
    def AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType method
        pass

class RequiredRole:

    pass
class entity_ResourceInterfaceRequiringEntity:

    pass
class entity_InterfaceRequiringEntity:

    pass
class entity_InterfaceProvidingEntity:

    pass
class pcm_entity_InterfaceProvidingRequiringEntity(entity_InterfaceProvidingEntity, entity_InterfaceRequiringEntity, entity_ResourceInterfaceRequiringEntity):

    pass
class ProvidedRole:

    pass
class Entity:

    pass
class pcm_repository_PassiveResource(Entity):

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

    def Exactlyonestart(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement Exactlyonestart method
        pass

    def Exactlyonestop(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement Exactlyonestop method
        pass

class pcm_allocation_AllocationContext(Entity):

    pass
class pcm_connectors_Connector(Entity):

    pass
class pcm_entity_InterfaceRequiringEntity(Entity):

    pass
class pcm_resourceenvironment_ResourceContainer(Entity):

    pass
class pcm_composition_ComposedStructure(Entity):

    pass
class pcm_repository_Repository(Entity):

    def __init__(self, repositoryDescription: str, RepositoryComponent82: set["RepositoryComponent"] = None, Interface85: set["Interface"] = None, DataType88: set["DataType"] = None):
        self.repositoryDescription = repositoryDescription
        self.RepositoryComponent82 = RepositoryComponent82 if RepositoryComponent82 is not None else set()
        self.Interface85 = Interface85 if Interface85 is not None else set()
        self.DataType88 = DataType88 if DataType88 is not None else set()
        
    @property
    def repositoryDescription(self) -> str:
        return self.__repositoryDescription

    @repositoryDescription.setter
    def repositoryDescription(self, repositoryDescription: str):
        self.__repositoryDescription = repositoryDescription

    @property
    def Interface85(self):
        return self.__Interface85

    @Interface85.setter
    def Interface85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Repository__Interface85", None)
        self.__Interface85 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository86"):
                    opp_val = getattr(item, "repository86", None)
                    
                    if opp_val == self:
                        setattr(item, "repository86", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository86"):
                    opp_val = getattr(item, "repository86", None)
                    
                    setattr(item, "repository86", self)
                    

    @property
    def RepositoryComponent82(self):
        return self.__RepositoryComponent82

    @RepositoryComponent82.setter
    def RepositoryComponent82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Repository__RepositoryComponent82", None)
        self.__RepositoryComponent82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository83"):
                    opp_val = getattr(item, "repository83", None)
                    
                    if opp_val == self:
                        setattr(item, "repository83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository83"):
                    opp_val = getattr(item, "repository83", None)
                    
                    setattr(item, "repository83", self)
                    

    @property
    def DataType88(self):
        return self.__DataType88

    @DataType88.setter
    def DataType88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Repository__DataType88", None)
        self.__DataType88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository89"):
                    opp_val = getattr(item, "repository89", None)
                    
                    if opp_val == self:
                        setattr(item, "repository89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository89"):
                    opp_val = getattr(item, "repository89", None)
                    
                    setattr(item, "repository89", self)
                    

class pcm_usagemodel_UsageScenario(Entity):

    pass
class pcm_repository_Interface(Entity):

    def __init__(self, pcm_repository_Interface100: set["Interface"] = None, pcm_repository_Interface103: set["Protocol"] = None, Signature105: set["Signature"] = None, Repository108: "Repository" = None, pcm_repository_Interface: set["Interface"] = None):
        self.pcm_repository_Interface100 = pcm_repository_Interface100 if pcm_repository_Interface100 is not None else set()
        self.pcm_repository_Interface103 = pcm_repository_Interface103 if pcm_repository_Interface103 is not None else set()
        self.Signature105 = Signature105 if Signature105 is not None else set()
        self.Repository108 = Repository108
        self.pcm_repository_Interface = pcm_repository_Interface if pcm_repository_Interface is not None else set()
        
    @property
    def Repository108(self):
        return self.__Repository108

    @Repository108.setter
    def Repository108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Interface__Repository108", None)
        self.__Repository108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository109"):
                opp_val = getattr(old_value, "repository109", None)
                if opp_val == self:
                    setattr(old_value, "repository109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository109"):
                opp_val = getattr(value, "repository109", None)
                setattr(value, "repository109", self)

    @property
    def Signature105(self):
        return self.__Signature105

    @Signature105.setter
    def Signature105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Interface__Signature105", None)
        self.__Signature105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository106"):
                    opp_val = getattr(item, "repository106", None)
                    
                    if opp_val == self:
                        setattr(item, "repository106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository106"):
                    opp_val = getattr(item, "repository106", None)
                    
                    setattr(item, "repository106", self)
                    

    @property
    def pcm_repository_Interface103(self):
        return self.__pcm_repository_Interface103

    @pcm_repository_Interface103.setter
    def pcm_repository_Interface103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Interface__pcm_repository_Interface103", None)
        self.__pcm_repository_Interface103 = value if value is not None else set()
        
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
                if hasattr(item, "Interface98"):
                    opp_val = getattr(item, "Interface98", None)
                    
                    if opp_val == self:
                        setattr(item, "Interface98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Interface98"):
                    opp_val = getattr(item, "Interface98", None)
                    
                    setattr(item, "Interface98", self)
                    

    @property
    def pcm_repository_Interface100(self):
        return self.__pcm_repository_Interface100

    @pcm_repository_Interface100.setter
    def pcm_repository_Interface100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Interface__pcm_repository_Interface100", None)
        self.__pcm_repository_Interface100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Interface101"):
                    opp_val = getattr(item, "Interface101", None)
                    
                    if opp_val == self:
                        setattr(item, "Interface101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Interface101"):
                    opp_val = getattr(item, "Interface101", None)
                    
                    setattr(item, "Interface101", self)
                    

    def SignaturesHaveToBeUniqueForAnInterface(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SignaturesHaveToBeUniqueForAnInterface method
        pass

    def NoProtocolTypeIDUsedTwice(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NoProtocolTypeIDUsedTwice method
        pass

class pcm_repository_Role(Entity):

    pass
class pcm_composition_AssemblyContext(Entity):

    pass
class pcm_qosannotations_QoSAnnotations(Entity):

    pass
class pcm_resourceenvironment_LinkingResource(Entity):

    pass
class pcm_usagemodel_AbstractUserAction(Entity):

    pass
class pcm_seff_AbstractAction(Entity):

    pass
class pcm_allocation_Allocation(Entity):

    def __init__(self, pcm_allocation_Allocation: set["AllocationContext"] = None, pcm_allocation_Allocation199: "ResourceEnvironment" = None, pcm_allocation_Allocation201: "System" = None):
        self.pcm_allocation_Allocation = pcm_allocation_Allocation if pcm_allocation_Allocation is not None else set()
        self.pcm_allocation_Allocation199 = pcm_allocation_Allocation199
        self.pcm_allocation_Allocation201 = pcm_allocation_Allocation201
        
    @property
    def pcm_allocation_Allocation199(self):
        return self.__pcm_allocation_Allocation199

    @pcm_allocation_Allocation199.setter
    def pcm_allocation_Allocation199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_allocation_Allocation__pcm_allocation_Allocation199", None)
        self.__pcm_allocation_Allocation199 = value
        
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
    def pcm_allocation_Allocation201(self):
        return self.__pcm_allocation_Allocation201

    @pcm_allocation_Allocation201.setter
    def pcm_allocation_Allocation201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_allocation_Allocation__pcm_allocation_Allocation201", None)
        self.__pcm_allocation_Allocation201 = value
        
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

    def EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce method
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
class pcm_seff_ResourceDemandingSEFF(seff_ServiceEffectSpecification, Identifier, seff_ResourceDemandingBehaviour):

    pass
class pcm_entity_Entity(Identifier, entity_NamedElement):

    pass
class entity_InterfaceProvidingRequiringEntity:

    pass
class composition_ComposedStructure:

    pass
class pcm_entity_ComposedProvidingRequiringEntity(composition_ComposedStructure, entity_InterfaceProvidingRequiringEntity):

    def __init__(self, core43: "pcm_composition_AssemblyConnector", core16: "pcm_composition_AssemblyContext", core29: "pcm_composition_RequiredDelegationConnector", core: "pcm_composition_ProvidedDelegationConnector", core46: "pcm_composition_ResourceRequiredDelegationConnector"):
        
    def ProvidedRolesMustBeBound(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ProvidedRolesMustBeBound method
        pass

class ResourceRequiredRole:

    pass
class pcm_entity_ResourceInterfaceRequiringEntity(Entity):

    pass
class RandomVariable:

    pass
class pcm_core_PCMRandomVariable(RandomVariable):

    def __init__(self):
        
    def SpecificationMustNotBeNULL(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SpecificationMustNotBeNULL method
        pass
