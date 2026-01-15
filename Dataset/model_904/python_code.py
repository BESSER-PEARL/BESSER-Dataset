from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RiskLevel(Enum):
    LOW = "LOW"
    MID = "MID"
    HIGH = "HIGH"
class ActivityUseKind(Enum):
    na = "na"
    extension = "extension"
    localContribution = "localContribution"
    localReplacement = "localReplacement"
class OptionalityKind(Enum):
    mandatory = "mandatory"
    optional = "optional"
class ExpertiseLevel(Enum):
    LOW = "LOW"
    MID = "MID"
    LEVEL = "LEVEL"
class ContractKind(Enum):
    EXPRESS = "EXPRESS"
    IMPLIED = "IMPLIED"
    OTHER = "OTHER"
class WorkProductRelationshipKind(Enum):
    impactedBy = "impactedBy"
    composition = "composition"
    aggregation = "aggregation"
class EstimatingTechnique(Enum):
    COST = "COST"
    TIME = "TIME"
    SKILLS = "SKILLS"
    DEFECTS = "DEFECTS"
    OTHER = "OTHER"
class ParameterDirectionKind(Enum):
    in = "in"
    out = "out"
    inout = "inout"
class WorkSequenceKind(Enum):
    finishToStart = "finishToStart"
    finishToFinish = "finishToFinish"
    startToStart = "startToStart"
    startToFinish = "startToFinish"
class VariabilityType(Enum):
    na = "na"
    contributes = "contributes"
    extends = "extends"
    replaces = "replaces"
    extends_replaces = "extends_replaces"


############################################
# Definition of Classes
############################################

class uma_spem_RoleDefinition:

    pass
class Concept:

    pass
class spem_uma_Whitepaper(Concept):

    pass
class uma_spem_MethodContentElement:

    pass
class uma_spem_WorkProductDefinition:

    pass
class uma_spem_MethodPlugin:

    pass
class uma_spem_MethodLibrary:

    pass
class uma_spem_MethodConfiguration:

    pass
class spem_uma_Root:

    pass
class uma_spem_TaskDefinition:

    pass
class uma_spem_Activity:

    pass
class Practice:

    pass
class uma_spem_WorkProductPortConnector:

    pass
class CapabilityPattern:

    pass
class Activity:

    pass
class spem_uma_Phase(Activity):

    pass
class spem_uma_Iteration(Activity):

    pass
class spem_uma_Process(Activity):

    def __init__(self, scope: str, usageNote: str, spem_uma_Process: set["CapabilityPattern"] = None, spem_uma_Process183: set["uma_spem_WorkProductPortConnector"] = None):
        self.scope = scope
        self.usageNote = usageNote
        self.spem_uma_Process = spem_uma_Process if spem_uma_Process is not None else set()
        self.spem_uma_Process183 = spem_uma_Process183 if spem_uma_Process183 is not None else set()
        
    @property
    def scope(self) -> str:
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope

    @property
    def usageNote(self) -> str:
        return self.__usageNote

    @usageNote.setter
    def usageNote(self, usageNote: str):
        self.__usageNote = usageNote

    @property
    def spem_uma_Process(self):
        return self.__spem_uma_Process

    @spem_uma_Process.setter
    def spem_uma_Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_uma_Process__spem_uma_Process", None)
        self.__spem_uma_Process = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CapabilityPattern"):
                    opp_val = getattr(item, "CapabilityPattern", None)
                    
                    if opp_val == self:
                        setattr(item, "CapabilityPattern", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CapabilityPattern"):
                    opp_val = getattr(item, "CapabilityPattern", None)
                    
                    setattr(item, "CapabilityPattern", self)
                    

    @property
    def spem_uma_Process183(self):
        return self.__spem_uma_Process183

    @spem_uma_Process183.setter
    def spem_uma_Process183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_uma_Process__spem_uma_Process183", None)
        self.__spem_uma_Process183 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_spem_WorkProductPortConnector"):
                    opp_val = getattr(item, "uma_spem_WorkProductPortConnector", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_spem_WorkProductPortConnector", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_spem_WorkProductPortConnector"):
                    opp_val = getattr(item, "uma_spem_WorkProductPortConnector", None)
                    
                    setattr(item, "uma_spem_WorkProductPortConnector", self)
                    

class uma_spem_WorkProductUse:

    pass
class Category:

    pass
class spem_uma_Discipline(Category):

    pass
class spem_uma_DisciplineGrouping(Category):

    pass
class spem_uma_Domain(Category):

    pass
class spem_uma_CustomCategory(Category):

    pass
class MethodContentPackage:

    pass
class spem_uma_RoleSetPackage(MethodContentPackage):

    pass
class spem_uma_DisciplinePackage(MethodContentPackage):

    pass
class spem_uma_TaskDefinitionPackage(MethodContentPackage):

    pass
class spem_uma_ConfigurationPackage(MethodContentPackage):

    pass
class spem_uma_WorkProductKindPackage(MethodContentPackage):

    pass
class spem_uma_GuidancePackage(MethodContentPackage):

    pass
class spem_uma_RoleDefinitionPackage(MethodContentPackage):

    pass
class spem_uma_ToolDefinitionPackage(MethodContentPackage):

    pass
class spem_uma_DomainPackage(MethodContentPackage):

    pass
class spem_uma_WorkProductDefinitionPackage(MethodContentPackage):

    pass
class spem_uma_QualificationPackage(MethodContentPackage):

    pass
class spem_uma_CategoryPackage(MethodContentPackage):

    pass
class Guidance:

    pass
class spem_uma_Practice(Guidance):

    def __init__(self, additionalInfo: str, application: str, background: str, goal: str, levelOfAdoption: str, problem: str, spem_uma_Practice: set["Practice"] = None, spem_uma_Practice199: set["uma_spem_Activity"] = None, spem_uma_Practice201: set["uma_spem_MethodContentElement"] = None):
        self.additionalInfo = additionalInfo
        self.application = application
        self.background = background
        self.goal = goal
        self.levelOfAdoption = levelOfAdoption
        self.problem = problem
        self.spem_uma_Practice = spem_uma_Practice if spem_uma_Practice is not None else set()
        self.spem_uma_Practice199 = spem_uma_Practice199 if spem_uma_Practice199 is not None else set()
        self.spem_uma_Practice201 = spem_uma_Practice201 if spem_uma_Practice201 is not None else set()
        
    @property
    def problem(self) -> str:
        return self.__problem

    @problem.setter
    def problem(self, problem: str):
        self.__problem = problem

    @property
    def goal(self) -> str:
        return self.__goal

    @goal.setter
    def goal(self, goal: str):
        self.__goal = goal

    @property
    def application(self) -> str:
        return self.__application

    @application.setter
    def application(self, application: str):
        self.__application = application

    @property
    def levelOfAdoption(self) -> str:
        return self.__levelOfAdoption

    @levelOfAdoption.setter
    def levelOfAdoption(self, levelOfAdoption: str):
        self.__levelOfAdoption = levelOfAdoption

    @property
    def additionalInfo(self) -> str:
        return self.__additionalInfo

    @additionalInfo.setter
    def additionalInfo(self, additionalInfo: str):
        self.__additionalInfo = additionalInfo

    @property
    def background(self) -> str:
        return self.__background

    @background.setter
    def background(self, background: str):
        self.__background = background

    @property
    def spem_uma_Practice199(self):
        return self.__spem_uma_Practice199

    @spem_uma_Practice199.setter
    def spem_uma_Practice199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_uma_Practice__spem_uma_Practice199", None)
        self.__spem_uma_Practice199 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_spem_Activity"):
                    opp_val = getattr(item, "uma_spem_Activity", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_spem_Activity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_spem_Activity"):
                    opp_val = getattr(item, "uma_spem_Activity", None)
                    
                    setattr(item, "uma_spem_Activity", self)
                    

    @property
    def spem_uma_Practice201(self):
        return self.__spem_uma_Practice201

    @spem_uma_Practice201.setter
    def spem_uma_Practice201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_uma_Practice__spem_uma_Practice201", None)
        self.__spem_uma_Practice201 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_spem_MethodContentElement"):
                    opp_val = getattr(item, "uma_spem_MethodContentElement", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_spem_MethodContentElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_spem_MethodContentElement"):
                    opp_val = getattr(item, "uma_spem_MethodContentElement", None)
                    
                    setattr(item, "uma_spem_MethodContentElement", self)
                    

    @property
    def spem_uma_Practice(self):
        return self.__spem_uma_Practice

    @spem_uma_Practice.setter
    def spem_uma_Practice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_uma_Practice__spem_uma_Practice", None)
        self.__spem_uma_Practice = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Practice"):
                    opp_val = getattr(item, "Practice", None)
                    
                    if opp_val == self:
                        setattr(item, "Practice", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Practice"):
                    opp_val = getattr(item, "Practice", None)
                    
                    setattr(item, "Practice", self)
                    

class spem_uma_SupportingMaterial(Guidance):

    pass
class spem_uma_Report(Guidance):

    pass
class spem_uma_ToolMentor(Guidance):

    pass
class spem_uma_Example(Guidance):

    pass
class spem_uma_ReusableAsset(Guidance):

    pass
class spem_uma_EstimatingConsideration(Guidance):

    pass
class spem_uma_Template(Guidance):

    pass
class spem_uma_TermDefinition(Guidance):

    pass
class spem_uma_Guideline(Guidance):

    pass
class spem_uma_Roadmap(Guidance):

    pass
class spem_uma_Concept(Guidance):

    pass
class spem_uma_Checklist(Guidance):

    pass
class Process:

    pass
class spem_uma_DeliveryProcess(Process):

    def __init__(self, scale: str, projectCharacteristics: str, riskLevel: str, estimatingTechnique: str, projectMemberExpertise: str, typeOfContract: str, spem_uma_DeliveryProcess: set["SupportingMaterial"] = None, spem_uma_DeliveryProcess186: set["SupportingMaterial"] = None, Process203: "spem_uma_ProcessPlanningTemplate", Process: "spem_uma_Discipline"):
        self.scale = scale
        self.projectCharacteristics = projectCharacteristics
        self.riskLevel = riskLevel
        self.estimatingTechnique = estimatingTechnique
        self.projectMemberExpertise = projectMemberExpertise
        self.typeOfContract = typeOfContract
        self.spem_uma_DeliveryProcess = spem_uma_DeliveryProcess if spem_uma_DeliveryProcess is not None else set()
        self.spem_uma_DeliveryProcess186 = spem_uma_DeliveryProcess186 if spem_uma_DeliveryProcess186 is not None else set()
        
    @property
    def estimatingTechnique(self) -> str:
        return self.__estimatingTechnique

    @estimatingTechnique.setter
    def estimatingTechnique(self, estimatingTechnique: str):
        self.__estimatingTechnique = estimatingTechnique

    @property
    def typeOfContract(self) -> str:
        return self.__typeOfContract

    @typeOfContract.setter
    def typeOfContract(self, typeOfContract: str):
        self.__typeOfContract = typeOfContract

    @property
    def projectCharacteristics(self) -> str:
        return self.__projectCharacteristics

    @projectCharacteristics.setter
    def projectCharacteristics(self, projectCharacteristics: str):
        self.__projectCharacteristics = projectCharacteristics

    @property
    def scale(self) -> str:
        return self.__scale

    @scale.setter
    def scale(self, scale: str):
        self.__scale = scale

    @property
    def projectMemberExpertise(self) -> str:
        return self.__projectMemberExpertise

    @projectMemberExpertise.setter
    def projectMemberExpertise(self, projectMemberExpertise: str):
        self.__projectMemberExpertise = projectMemberExpertise

    @property
    def riskLevel(self) -> str:
        return self.__riskLevel

    @riskLevel.setter
    def riskLevel(self, riskLevel: str):
        self.__riskLevel = riskLevel

    @property
    def spem_uma_DeliveryProcess186(self):
        return self.__spem_uma_DeliveryProcess186

    @spem_uma_DeliveryProcess186.setter
    def spem_uma_DeliveryProcess186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_uma_DeliveryProcess__spem_uma_DeliveryProcess186", None)
        self.__spem_uma_DeliveryProcess186 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SupportingMaterial187"):
                    opp_val = getattr(item, "SupportingMaterial187", None)
                    
                    if opp_val == self:
                        setattr(item, "SupportingMaterial187", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SupportingMaterial187"):
                    opp_val = getattr(item, "SupportingMaterial187", None)
                    
                    setattr(item, "SupportingMaterial187", self)
                    

    @property
    def spem_uma_DeliveryProcess(self):
        return self.__spem_uma_DeliveryProcess

    @spem_uma_DeliveryProcess.setter
    def spem_uma_DeliveryProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_uma_DeliveryProcess__spem_uma_DeliveryProcess", None)
        self.__spem_uma_DeliveryProcess = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SupportingMaterial"):
                    opp_val = getattr(item, "SupportingMaterial", None)
                    
                    if opp_val == self:
                        setattr(item, "SupportingMaterial", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SupportingMaterial"):
                    opp_val = getattr(item, "SupportingMaterial", None)
                    
                    setattr(item, "SupportingMaterial", self)
                    

class spem_uma_ProcessPlanningTemplate(Process):

    pass
class spem_uma_CapabilityPattern(Process):

    pass
class Artifact:

    pass
class WorkProductUse:

    pass
class spem_uma_Deliverable(WorkProductUse):

    def __init__(self, externalDescription: str, packagingGuidance: str, spem_uma_Deliverable: set["uma_spem_WorkProductUse"] = None):
        self.externalDescription = externalDescription
        self.packagingGuidance = packagingGuidance
        self.spem_uma_Deliverable = spem_uma_Deliverable if spem_uma_Deliverable is not None else set()
        
    @property
    def externalDescription(self) -> str:
        return self.__externalDescription

    @externalDescription.setter
    def externalDescription(self, externalDescription: str):
        self.__externalDescription = externalDescription

    @property
    def packagingGuidance(self) -> str:
        return self.__packagingGuidance

    @packagingGuidance.setter
    def packagingGuidance(self, packagingGuidance: str):
        self.__packagingGuidance = packagingGuidance

    @property
    def spem_uma_Deliverable(self):
        return self.__spem_uma_Deliverable

    @spem_uma_Deliverable.setter
    def spem_uma_Deliverable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_uma_Deliverable__spem_uma_Deliverable", None)
        self.__spem_uma_Deliverable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_spem_WorkProductUse"):
                    opp_val = getattr(item, "uma_spem_WorkProductUse", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_spem_WorkProductUse", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_spem_WorkProductUse"):
                    opp_val = getattr(item, "uma_spem_WorkProductUse", None)
                    
                    setattr(item, "uma_spem_WorkProductUse", self)
                    

class spem_uma_Outcome(WorkProductUse):

    pass
class spem_uma_Artifact(WorkProductUse):

    pass
class SupportingMaterial:

    pass
class spem_MethodLibrary:

    def __init__(self, name: str, spem_MethodLibrary: set["spem_MethodPlugin"] = None, spem_MethodLibrary169: set["spem_MethodConfiguration"] = None, spem_MethodLibrary172: "spem_MethodContentPackage" = None):
        self.name = name
        self.spem_MethodLibrary = spem_MethodLibrary if spem_MethodLibrary is not None else set()
        self.spem_MethodLibrary169 = spem_MethodLibrary169 if spem_MethodLibrary169 is not None else set()
        self.spem_MethodLibrary172 = spem_MethodLibrary172
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def spem_MethodLibrary172(self):
        return self.__spem_MethodLibrary172

    @spem_MethodLibrary172.setter
    def spem_MethodLibrary172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_MethodLibrary__spem_MethodLibrary172", None)
        self.__spem_MethodLibrary172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_MethodContentPackage173"):
                opp_val = getattr(old_value, "spem_MethodContentPackage173", None)
                if opp_val == self:
                    setattr(old_value, "spem_MethodContentPackage173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_MethodContentPackage173"):
                opp_val = getattr(value, "spem_MethodContentPackage173", None)
                setattr(value, "spem_MethodContentPackage173", self)

    @property
    def spem_MethodLibrary(self):
        return self.__spem_MethodLibrary

    @spem_MethodLibrary.setter
    def spem_MethodLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_MethodLibrary__spem_MethodLibrary", None)
        self.__spem_MethodLibrary = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_MethodPlugin167"):
                    opp_val = getattr(item, "spem_MethodPlugin167", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_MethodPlugin167", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_MethodPlugin167"):
                    opp_val = getattr(item, "spem_MethodPlugin167", None)
                    
                    setattr(item, "spem_MethodPlugin167", self)
                    

    @property
    def spem_MethodLibrary169(self):
        return self.__spem_MethodLibrary169

    @spem_MethodLibrary169.setter
    def spem_MethodLibrary169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_MethodLibrary__spem_MethodLibrary169", None)
        self.__spem_MethodLibrary169 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_MethodConfiguration170"):
                    opp_val = getattr(item, "spem_MethodConfiguration170", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_MethodConfiguration170", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_MethodConfiguration170"):
                    opp_val = getattr(item, "spem_MethodConfiguration170", None)
                    
                    setattr(item, "spem_MethodConfiguration170", self)
                    

class ProcessPackage:

    pass
class spem_uma_ProcessComponentPackage(ProcessPackage):

    pass
class spem_uma_DeliveryProcessPackage(ProcessPackage):

    pass
class spem_uma_CapabilityPatternPackage(ProcessPackage):

    pass
class spem_ProcessComponent(ProcessPackage):

    pass
class spem_VariabilityElement(ABC):

    def __init__(self, variabilityType: str, spem_VariabilityElement: "spem_VariabilityElement" = None, spem_VariabilityElement126: "spem_VariabilityElement" = None):
        self.variabilityType = variabilityType
        self.spem_VariabilityElement = spem_VariabilityElement
        self.spem_VariabilityElement126 = spem_VariabilityElement126
        
    @property
    def variabilityType(self) -> str:
        return self.__variabilityType

    @variabilityType.setter
    def variabilityType(self, variabilityType: str):
        self.__variabilityType = variabilityType

    @property
    def spem_VariabilityElement126(self):
        return self.__spem_VariabilityElement126

    @spem_VariabilityElement126.setter
    def spem_VariabilityElement126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_VariabilityElement__spem_VariabilityElement126", None)
        self.__spem_VariabilityElement126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_VariabilityElement"):
                opp_val = getattr(old_value, "spem_VariabilityElement", None)
                if opp_val == self:
                    setattr(old_value, "spem_VariabilityElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_VariabilityElement"):
                opp_val = getattr(value, "spem_VariabilityElement", None)
                setattr(value, "spem_VariabilityElement", self)

    @property
    def spem_VariabilityElement(self):
        return self.__spem_VariabilityElement

    @spem_VariabilityElement.setter
    def spem_VariabilityElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_VariabilityElement__spem_VariabilityElement", None)
        self.__spem_VariabilityElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_VariabilityElement126"):
                opp_val = getattr(old_value, "spem_VariabilityElement126", None)
                if opp_val == self:
                    setattr(old_value, "spem_VariabilityElement126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_VariabilityElement126"):
                opp_val = getattr(value, "spem_VariabilityElement126", None)
                setattr(value, "spem_VariabilityElement126", self)

class RoleUse:

    pass
class spem_CompositeRole(RoleUse):

    pass
class MethodLibraryPackageableElement:

    pass
class spem_MethodPlugin(MethodLibraryPackageableElement):

    pass
class spem_MethodPluginPackageableElement(ABC):

    pass
class spem_MethodLibraryPackageableElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Kind:

    pass
class MethodPluginPackageableElement:

    pass
class spem_ProcessPackageableElement(ABC):

    def __init__(self, name: str, spem_ProcessPackageableElement: "spem_ProcessPackage" = None):
        self.name = name
        self.spem_ProcessPackageableElement = spem_ProcessPackageableElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def spem_ProcessPackageableElement(self):
        return self.__spem_ProcessPackageableElement

    @spem_ProcessPackageableElement.setter
    def spem_ProcessPackageableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_ProcessPackageableElement__spem_ProcessPackageableElement", None)
        self.__spem_ProcessPackageableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_ProcessPackage"):
                opp_val = getattr(old_value, "spem_ProcessPackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_ProcessPackage"):
                opp_val = getattr(value, "spem_ProcessPackage", None)
                if opp_val is None:
                    setattr(value, "spem_ProcessPackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class spem_MethodContentPackageableElement(ABC):

    def __init__(self, name: str, spem_MethodContentPackageableElement: "spem_MethodContentPackage" = None):
        self.name = name
        self.spem_MethodContentPackageableElement = spem_MethodContentPackageableElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def spem_MethodContentPackageableElement(self):
        return self.__spem_MethodContentPackageableElement

    @spem_MethodContentPackageableElement.setter
    def spem_MethodContentPackageableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_MethodContentPackageableElement__spem_MethodContentPackageableElement", None)
        self.__spem_MethodContentPackageableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_MethodContentPackage"):
                opp_val = getattr(old_value, "spem_MethodContentPackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_MethodContentPackage"):
                opp_val = getattr(value, "spem_MethodContentPackage", None)
                if opp_val is None:
                    setattr(value, "spem_MethodContentPackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MethodContentElement:

    pass
class spem_uma_WorkProductKind(Kind, MethodContentElement):

    pass
class spem_WorkProductDefinitionRelationship(MethodContentElement):

    pass
class spem_uma_RoleSet(MethodContentElement):

    pass
class spem_Default_TaskDefinitionPerformer(MethodContentElement):

    pass
class spem_Default_ResponsibilityAssignment(MethodContentElement):

    pass
class spem_Category(MethodContentElement):

    pass
class spem_Guidance(MethodContentElement):

    pass
class ProcessPackageableElement:

    pass
class spem_ProcessPackage(ProcessPackageableElement, MethodPluginPackageableElement):

    pass
class DescribableElement:

    pass
class spem_Metric(DescribableElement):

    def __init__(self, expression: str, spem_Metric: "spem_DescribableElement" = None):
        self.expression = expression
        self.spem_Metric = spem_Metric
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def spem_Metric(self):
        return self.__spem_Metric

    @spem_Metric.setter
    def spem_Metric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Metric__spem_Metric", None)
        self.__spem_Metric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_DescribableElement55"):
                opp_val = getattr(old_value, "spem_DescribableElement55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_DescribableElement55"):
                opp_val = getattr(value, "spem_DescribableElement55", None)
                if opp_val is None:
                    setattr(value, "spem_DescribableElement55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class spem_ProcessElement(DescribableElement, ProcessPackageableElement):

    pass
class spem_ToolDefinition(MethodContentElement):

    pass
class spem_MethodContentKind(Kind, MethodContentElement):

    pass
class MethodContentPackageableElement:

    pass
class spem_MethodContentPackage(MethodContentPackageableElement, MethodPluginPackageableElement):

    pass
class spem_WorkProductDefinition(MethodContentElement):

    pass
class spem_Qualification(MethodContentElement):

    pass
class spem_RoleDefinition(MethodContentElement):

    def __init__(self, synonym: str, spem_RoleDefinition: "spem_RoleUse" = None, spem_RoleDefinition91: "spem_Default_TaskDefinitionPerformer" = None, spem_RoleDefinition93: "spem_Default_ResponsibilityAssignment" = None, spem_RoleDefinition80: set["spem_Qualification"] = None, spem_RoleDefinition118: "spem_CompositeRole" = None):
        self.synonym = synonym
        self.spem_RoleDefinition = spem_RoleDefinition
        self.spem_RoleDefinition91 = spem_RoleDefinition91
        self.spem_RoleDefinition93 = spem_RoleDefinition93
        self.spem_RoleDefinition80 = spem_RoleDefinition80 if spem_RoleDefinition80 is not None else set()
        self.spem_RoleDefinition118 = spem_RoleDefinition118
        
    @property
    def synonym(self) -> str:
        return self.__synonym

    @synonym.setter
    def synonym(self, synonym: str):
        self.__synonym = synonym

    @property
    def spem_RoleDefinition(self):
        return self.__spem_RoleDefinition

    @spem_RoleDefinition.setter
    def spem_RoleDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_RoleDefinition__spem_RoleDefinition", None)
        self.__spem_RoleDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_RoleUse33"):
                opp_val = getattr(old_value, "spem_RoleUse33", None)
                if opp_val == self:
                    setattr(old_value, "spem_RoleUse33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_RoleUse33"):
                opp_val = getattr(value, "spem_RoleUse33", None)
                setattr(value, "spem_RoleUse33", self)

    @property
    def spem_RoleDefinition118(self):
        return self.__spem_RoleDefinition118

    @spem_RoleDefinition118.setter
    def spem_RoleDefinition118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_RoleDefinition__spem_RoleDefinition118", None)
        self.__spem_RoleDefinition118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_CompositeRole"):
                opp_val = getattr(old_value, "spem_CompositeRole", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_CompositeRole"):
                opp_val = getattr(value, "spem_CompositeRole", None)
                if opp_val is None:
                    setattr(value, "spem_CompositeRole", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def spem_RoleDefinition93(self):
        return self.__spem_RoleDefinition93

    @spem_RoleDefinition93.setter
    def spem_RoleDefinition93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_RoleDefinition__spem_RoleDefinition93", None)
        self.__spem_RoleDefinition93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_Default_ResponsibilityAssignment"):
                opp_val = getattr(old_value, "spem_Default_ResponsibilityAssignment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_Default_ResponsibilityAssignment"):
                opp_val = getattr(value, "spem_Default_ResponsibilityAssignment", None)
                if opp_val is None:
                    setattr(value, "spem_Default_ResponsibilityAssignment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def spem_RoleDefinition80(self):
        return self.__spem_RoleDefinition80

    @spem_RoleDefinition80.setter
    def spem_RoleDefinition80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_RoleDefinition__spem_RoleDefinition80", None)
        self.__spem_RoleDefinition80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_Qualification81"):
                    opp_val = getattr(item, "spem_Qualification81", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_Qualification81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_Qualification81"):
                    opp_val = getattr(item, "spem_Qualification81", None)
                    
                    setattr(item, "spem_Qualification81", self)
                    

    @property
    def spem_RoleDefinition91(self):
        return self.__spem_RoleDefinition91

    @spem_RoleDefinition91.setter
    def spem_RoleDefinition91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_RoleDefinition__spem_RoleDefinition91", None)
        self.__spem_RoleDefinition91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_Default_TaskDefinitionPerformer90"):
                opp_val = getattr(old_value, "spem_Default_TaskDefinitionPerformer90", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_Default_TaskDefinitionPerformer90"):
                opp_val = getattr(value, "spem_Default_TaskDefinitionPerformer90", None)
                if opp_val is None:
                    setattr(value, "spem_Default_TaskDefinitionPerformer90", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MethodContentUse:

    pass
class spem_WorkProductUse(MethodContentUse):

    pass
class spem_ProcessComponentUse(MethodContentUse):

    pass
class spem_RoleUse(MethodContentUse):

    pass
class WorkDefinitionPerformer:

    pass
class WorkDefinitionParameter:

    pass
class spem_Default_TaskDefinitionParameter(WorkDefinitionParameter):

    def __init__(self, name: str, optionality: str, spem_Default_TaskDefinitionParameter: "spem_TaskDefinition" = None, spem_Default_TaskDefinitionParameter98: "spem_WorkProductDefinition" = None):
        self.name = name
        self.optionality = optionality
        self.spem_Default_TaskDefinitionParameter = spem_Default_TaskDefinitionParameter
        self.spem_Default_TaskDefinitionParameter98 = spem_Default_TaskDefinitionParameter98
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def optionality(self) -> str:
        return self.__optionality

    @optionality.setter
    def optionality(self, optionality: str):
        self.__optionality = optionality

    @property
    def spem_Default_TaskDefinitionParameter(self):
        return self.__spem_Default_TaskDefinitionParameter

    @spem_Default_TaskDefinitionParameter.setter
    def spem_Default_TaskDefinitionParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Default_TaskDefinitionParameter__spem_Default_TaskDefinitionParameter", None)
        self.__spem_Default_TaskDefinitionParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_TaskDefinition"):
                opp_val = getattr(old_value, "spem_TaskDefinition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_TaskDefinition"):
                opp_val = getattr(value, "spem_TaskDefinition", None)
                if opp_val is None:
                    setattr(value, "spem_TaskDefinition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def spem_Default_TaskDefinitionParameter98(self):
        return self.__spem_Default_TaskDefinitionParameter98

    @spem_Default_TaskDefinitionParameter98.setter
    def spem_Default_TaskDefinitionParameter98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Default_TaskDefinitionParameter__spem_Default_TaskDefinitionParameter98", None)
        self.__spem_Default_TaskDefinitionParameter98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_WorkProductDefinition99"):
                opp_val = getattr(old_value, "spem_WorkProductDefinition99", None)
                if opp_val == self:
                    setattr(old_value, "spem_WorkProductDefinition99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_WorkProductDefinition99"):
                opp_val = getattr(value, "spem_WorkProductDefinition99", None)
                setattr(value, "spem_WorkProductDefinition99", self)

class VariabilityElement:

    pass
class spem_MethodContentElement(DescribableElement, MethodContentPackageableElement, VariabilityElement):

    pass
class WorkBreakdownElement:

    pass
class spem_TaskUse(MethodContentUse, WorkBreakdownElement):

    def __init__(self, preCondition: str, postCondition: str, spem_TaskUse: "spem_ProcessPerformer" = None, spem_TaskUse106: "spem_TaskDefinition" = None, spem_TaskUse109: set["spem_Qualification"] = None, spem_TaskUse112: set["spem_Step"] = None, spem_TaskUse115: set["spem_ProcessParameter"] = None):
        self.preCondition = preCondition
        self.postCondition = postCondition
        self.spem_TaskUse = spem_TaskUse
        self.spem_TaskUse106 = spem_TaskUse106
        self.spem_TaskUse109 = spem_TaskUse109 if spem_TaskUse109 is not None else set()
        self.spem_TaskUse112 = spem_TaskUse112 if spem_TaskUse112 is not None else set()
        self.spem_TaskUse115 = spem_TaskUse115 if spem_TaskUse115 is not None else set()
        
    @property
    def preCondition(self) -> str:
        return self.__preCondition

    @preCondition.setter
    def preCondition(self, preCondition: str):
        self.__preCondition = preCondition

    @property
    def postCondition(self) -> str:
        return self.__postCondition

    @postCondition.setter
    def postCondition(self, postCondition: str):
        self.__postCondition = postCondition

    @property
    def spem_TaskUse109(self):
        return self.__spem_TaskUse109

    @spem_TaskUse109.setter
    def spem_TaskUse109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_TaskUse__spem_TaskUse109", None)
        self.__spem_TaskUse109 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_Qualification110"):
                    opp_val = getattr(item, "spem_Qualification110", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_Qualification110", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_Qualification110"):
                    opp_val = getattr(item, "spem_Qualification110", None)
                    
                    setattr(item, "spem_Qualification110", self)
                    

    @property
    def spem_TaskUse106(self):
        return self.__spem_TaskUse106

    @spem_TaskUse106.setter
    def spem_TaskUse106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_TaskUse__spem_TaskUse106", None)
        self.__spem_TaskUse106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_TaskDefinition107"):
                opp_val = getattr(old_value, "spem_TaskDefinition107", None)
                if opp_val == self:
                    setattr(old_value, "spem_TaskDefinition107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_TaskDefinition107"):
                opp_val = getattr(value, "spem_TaskDefinition107", None)
                setattr(value, "spem_TaskDefinition107", self)

    @property
    def spem_TaskUse115(self):
        return self.__spem_TaskUse115

    @spem_TaskUse115.setter
    def spem_TaskUse115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_TaskUse__spem_TaskUse115", None)
        self.__spem_TaskUse115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_ProcessParameter116"):
                    opp_val = getattr(item, "spem_ProcessParameter116", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_ProcessParameter116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_ProcessParameter116"):
                    opp_val = getattr(item, "spem_ProcessParameter116", None)
                    
                    setattr(item, "spem_ProcessParameter116", self)
                    

    @property
    def spem_TaskUse(self):
        return self.__spem_TaskUse

    @spem_TaskUse.setter
    def spem_TaskUse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_TaskUse__spem_TaskUse", None)
        self.__spem_TaskUse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_ProcessPerformer31"):
                opp_val = getattr(old_value, "spem_ProcessPerformer31", None)
                if opp_val == self:
                    setattr(old_value, "spem_ProcessPerformer31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_ProcessPerformer31"):
                opp_val = getattr(value, "spem_ProcessPerformer31", None)
                setattr(value, "spem_ProcessPerformer31", self)

    @property
    def spem_TaskUse112(self):
        return self.__spem_TaskUse112

    @spem_TaskUse112.setter
    def spem_TaskUse112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_TaskUse__spem_TaskUse112", None)
        self.__spem_TaskUse112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_Step113"):
                    opp_val = getattr(item, "spem_Step113", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_Step113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_Step113"):
                    opp_val = getattr(item, "spem_Step113", None)
                    
                    setattr(item, "spem_Step113", self)
                    

class spem_Milestone(WorkBreakdownElement):

    pass
class WorkDefinition:

    pass
class spem_Step(DescribableElement, VariabilityElement, WorkDefinition):

    def __init__(self, name: str, spem_Step: "spem_TaskDefinition" = None, Step: "spem_Step" = None, successor74: "spem_Step" = None, Step78: "spem_Step" = None, predecessor77: "spem_Step" = None, spem_Step113: "spem_TaskUse" = None):
        self.name = name
        self.spem_Step = spem_Step
        self.Step = Step
        self.successor74 = successor74
        self.Step78 = Step78
        self.predecessor77 = predecessor77
        self.spem_Step113 = spem_Step113
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def spem_Step(self):
        return self.__spem_Step

    @spem_Step.setter
    def spem_Step(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Step__spem_Step", None)
        self.__spem_Step = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_TaskDefinition68"):
                opp_val = getattr(old_value, "spem_TaskDefinition68", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_TaskDefinition68"):
                opp_val = getattr(value, "spem_TaskDefinition68", None)
                if opp_val is None:
                    setattr(value, "spem_TaskDefinition68", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def spem_Step113(self):
        return self.__spem_Step113

    @spem_Step113.setter
    def spem_Step113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Step__spem_Step113", None)
        self.__spem_Step113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_TaskUse112"):
                opp_val = getattr(old_value, "spem_TaskUse112", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_TaskUse112"):
                opp_val = getattr(value, "spem_TaskUse112", None)
                if opp_val is None:
                    setattr(value, "spem_TaskUse112", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Step(self):
        return self.__Step

    @Step.setter
    def Step(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Step__Step", None)
        self.__Step = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "successor74"):
                opp_val = getattr(old_value, "successor74", None)
                if opp_val == self:
                    setattr(old_value, "successor74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "successor74"):
                opp_val = getattr(value, "successor74", None)
                setattr(value, "successor74", self)

    @property
    def predecessor77(self):
        return self.__predecessor77

    @predecessor77.setter
    def predecessor77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Step__predecessor77", None)
        self.__predecessor77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Step78"):
                opp_val = getattr(old_value, "Step78", None)
                if opp_val == self:
                    setattr(old_value, "Step78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Step78"):
                opp_val = getattr(value, "Step78", None)
                setattr(value, "Step78", self)

    @property
    def successor74(self):
        return self.__successor74

    @successor74.setter
    def successor74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Step__successor74", None)
        self.__successor74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Step"):
                opp_val = getattr(old_value, "Step", None)
                if opp_val == self:
                    setattr(old_value, "Step", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Step"):
                opp_val = getattr(value, "Step", None)
                setattr(value, "Step", self)

    @property
    def Step78(self):
        return self.__Step78

    @Step78.setter
    def Step78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Step__Step78", None)
        self.__Step78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "predecessor77"):
                opp_val = getattr(old_value, "predecessor77", None)
                if opp_val == self:
                    setattr(old_value, "predecessor77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "predecessor77"):
                opp_val = getattr(value, "predecessor77", None)
                setattr(value, "predecessor77", self)

class spem_TaskDefinition(WorkDefinition, MethodContentElement):

    pass
class spem_Activity(VariabilityElement, WorkBreakdownElement, WorkDefinition):

    def __init__(self, isEnactable: bool, useKind: str, spem_Activity14: set["spem_BreakdownElement"] = None, spem_Activity17: set["spem_BreakdownElement"] = None, spem_Activity20: set["spem_ProcessParameter"] = None, spem_Activity22: "spem_MethodConfiguration" = None, spem_Activity24: set["spem_MethodConfiguration"] = None, spem_Activity: "spem_Activity" = None, spem_Activity11: "spem_Activity" = None, spem_Activity29: "spem_ProcessPerformer" = None, spem_Activity129: "spem_ProcessComponent" = None):
        self.isEnactable = isEnactable
        self.useKind = useKind
        self.spem_Activity14 = spem_Activity14 if spem_Activity14 is not None else set()
        self.spem_Activity17 = spem_Activity17 if spem_Activity17 is not None else set()
        self.spem_Activity20 = spem_Activity20 if spem_Activity20 is not None else set()
        self.spem_Activity22 = spem_Activity22
        self.spem_Activity24 = spem_Activity24 if spem_Activity24 is not None else set()
        self.spem_Activity = spem_Activity
        self.spem_Activity11 = spem_Activity11
        self.spem_Activity29 = spem_Activity29
        self.spem_Activity129 = spem_Activity129
        
    @property
    def useKind(self) -> str:
        return self.__useKind

    @useKind.setter
    def useKind(self, useKind: str):
        self.__useKind = useKind

    @property
    def isEnactable(self) -> bool:
        return self.__isEnactable

    @isEnactable.setter
    def isEnactable(self, isEnactable: bool):
        self.__isEnactable = isEnactable

    @property
    def spem_Activity22(self):
        return self.__spem_Activity22

    @spem_Activity22.setter
    def spem_Activity22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Activity__spem_Activity22", None)
        self.__spem_Activity22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_MethodConfiguration"):
                opp_val = getattr(old_value, "spem_MethodConfiguration", None)
                if opp_val == self:
                    setattr(old_value, "spem_MethodConfiguration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_MethodConfiguration"):
                opp_val = getattr(value, "spem_MethodConfiguration", None)
                setattr(value, "spem_MethodConfiguration", self)

    @property
    def spem_Activity(self):
        return self.__spem_Activity

    @spem_Activity.setter
    def spem_Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Activity__spem_Activity", None)
        self.__spem_Activity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_Activity11"):
                opp_val = getattr(old_value, "spem_Activity11", None)
                if opp_val == self:
                    setattr(old_value, "spem_Activity11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_Activity11"):
                opp_val = getattr(value, "spem_Activity11", None)
                setattr(value, "spem_Activity11", self)

    @property
    def spem_Activity29(self):
        return self.__spem_Activity29

    @spem_Activity29.setter
    def spem_Activity29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Activity__spem_Activity29", None)
        self.__spem_Activity29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_ProcessPerformer28"):
                opp_val = getattr(old_value, "spem_ProcessPerformer28", None)
                if opp_val == self:
                    setattr(old_value, "spem_ProcessPerformer28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_ProcessPerformer28"):
                opp_val = getattr(value, "spem_ProcessPerformer28", None)
                setattr(value, "spem_ProcessPerformer28", self)

    @property
    def spem_Activity20(self):
        return self.__spem_Activity20

    @spem_Activity20.setter
    def spem_Activity20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Activity__spem_Activity20", None)
        self.__spem_Activity20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_ProcessParameter"):
                    opp_val = getattr(item, "spem_ProcessParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_ProcessParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_ProcessParameter"):
                    opp_val = getattr(item, "spem_ProcessParameter", None)
                    
                    setattr(item, "spem_ProcessParameter", self)
                    

    @property
    def spem_Activity24(self):
        return self.__spem_Activity24

    @spem_Activity24.setter
    def spem_Activity24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Activity__spem_Activity24", None)
        self.__spem_Activity24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_MethodConfiguration25"):
                    opp_val = getattr(item, "spem_MethodConfiguration25", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_MethodConfiguration25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_MethodConfiguration25"):
                    opp_val = getattr(item, "spem_MethodConfiguration25", None)
                    
                    setattr(item, "spem_MethodConfiguration25", self)
                    

    @property
    def spem_Activity129(self):
        return self.__spem_Activity129

    @spem_Activity129.setter
    def spem_Activity129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Activity__spem_Activity129", None)
        self.__spem_Activity129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_ProcessComponent"):
                opp_val = getattr(old_value, "spem_ProcessComponent", None)
                if opp_val == self:
                    setattr(old_value, "spem_ProcessComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_ProcessComponent"):
                opp_val = getattr(value, "spem_ProcessComponent", None)
                setattr(value, "spem_ProcessComponent", self)

    @property
    def spem_Activity17(self):
        return self.__spem_Activity17

    @spem_Activity17.setter
    def spem_Activity17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Activity__spem_Activity17", None)
        self.__spem_Activity17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_BreakdownElement18"):
                    opp_val = getattr(item, "spem_BreakdownElement18", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_BreakdownElement18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_BreakdownElement18"):
                    opp_val = getattr(item, "spem_BreakdownElement18", None)
                    
                    setattr(item, "spem_BreakdownElement18", self)
                    

    @property
    def spem_Activity14(self):
        return self.__spem_Activity14

    @spem_Activity14.setter
    def spem_Activity14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Activity__spem_Activity14", None)
        self.__spem_Activity14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_BreakdownElement15"):
                    opp_val = getattr(item, "spem_BreakdownElement15", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_BreakdownElement15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_BreakdownElement15"):
                    opp_val = getattr(item, "spem_BreakdownElement15", None)
                    
                    setattr(item, "spem_BreakdownElement15", self)
                    

    @property
    def spem_Activity11(self):
        return self.__spem_Activity11

    @spem_Activity11.setter
    def spem_Activity11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Activity__spem_Activity11", None)
        self.__spem_Activity11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_Activity"):
                opp_val = getattr(old_value, "spem_Activity", None)
                if opp_val == self:
                    setattr(old_value, "spem_Activity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_Activity"):
                opp_val = getattr(value, "spem_Activity", None)
                setattr(value, "spem_Activity", self)

class BreakdownElement:

    pass
class spem_ProcessResponsibilityAssignment(BreakdownElement):

    pass
class spem_MethodContentUse(BreakdownElement):

    def __init__(self, isSynchronizedWithSource: bool):
        self.isSynchronizedWithSource = isSynchronizedWithSource
        
    @property
    def isSynchronizedWithSource(self) -> bool:
        return self.__isSynchronizedWithSource

    @isSynchronizedWithSource.setter
    def isSynchronizedWithSource(self, isSynchronizedWithSource: bool):
        self.__isSynchronizedWithSource = isSynchronizedWithSource

class spem_TeamProfile(BreakdownElement):

    pass
class spem_WorkSequence(BreakdownElement):

    def __init__(self, linkKind: str, WorkSequence: "spem_WorkBreakdownElement" = None, WorkSequence7: "spem_WorkBreakdownElement" = None, linkToSuccessor: "spem_WorkBreakdownElement" = None, linkToPredecessor: "spem_WorkBreakdownElement" = None):
        self.linkKind = linkKind
        self.WorkSequence = WorkSequence
        self.WorkSequence7 = WorkSequence7
        self.linkToSuccessor = linkToSuccessor
        self.linkToPredecessor = linkToPredecessor
        
    @property
    def linkKind(self) -> str:
        return self.__linkKind

    @linkKind.setter
    def linkKind(self, linkKind: str):
        self.__linkKind = linkKind

    @property
    def linkToPredecessor(self):
        return self.__linkToPredecessor

    @linkToPredecessor.setter
    def linkToPredecessor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkSequence__linkToPredecessor", None)
        self.__linkToPredecessor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorkBreakdownElement10"):
                opp_val = getattr(old_value, "WorkBreakdownElement10", None)
                if opp_val == self:
                    setattr(old_value, "WorkBreakdownElement10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkBreakdownElement10"):
                opp_val = getattr(value, "WorkBreakdownElement10", None)
                setattr(value, "WorkBreakdownElement10", self)

    @property
    def WorkSequence7(self):
        return self.__WorkSequence7

    @WorkSequence7.setter
    def WorkSequence7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkSequence__WorkSequence7", None)
        self.__WorkSequence7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "predecessor"):
                opp_val = getattr(old_value, "predecessor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "predecessor"):
                opp_val = getattr(value, "predecessor", None)
                if opp_val is None:
                    setattr(value, "predecessor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def linkToSuccessor(self):
        return self.__linkToSuccessor

    @linkToSuccessor.setter
    def linkToSuccessor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkSequence__linkToSuccessor", None)
        self.__linkToSuccessor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorkBreakdownElement"):
                opp_val = getattr(old_value, "WorkBreakdownElement", None)
                if opp_val == self:
                    setattr(old_value, "WorkBreakdownElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkBreakdownElement"):
                opp_val = getattr(value, "WorkBreakdownElement", None)
                setattr(value, "WorkBreakdownElement", self)

    @property
    def WorkSequence(self):
        return self.__WorkSequence

    @WorkSequence.setter
    def WorkSequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkSequence__WorkSequence", None)
        self.__WorkSequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "successor"):
                opp_val = getattr(old_value, "successor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "successor"):
                opp_val = getattr(value, "successor", None)
                if opp_val is None:
                    setattr(value, "successor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class spem_WorkProductUseRelationship(BreakdownElement):

    def __init__(self, relationshipKind: str, spem_WorkProductUseRelationship: "spem_WorkProductUse" = None, spem_WorkProductUseRelationship45: set["spem_WorkProductUse"] = None):
        self.relationshipKind = relationshipKind
        self.spem_WorkProductUseRelationship = spem_WorkProductUseRelationship
        self.spem_WorkProductUseRelationship45 = spem_WorkProductUseRelationship45 if spem_WorkProductUseRelationship45 is not None else set()
        
    @property
    def relationshipKind(self) -> str:
        return self.__relationshipKind

    @relationshipKind.setter
    def relationshipKind(self, relationshipKind: str):
        self.__relationshipKind = relationshipKind

    @property
    def spem_WorkProductUseRelationship(self):
        return self.__spem_WorkProductUseRelationship

    @spem_WorkProductUseRelationship.setter
    def spem_WorkProductUseRelationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkProductUseRelationship__spem_WorkProductUseRelationship", None)
        self.__spem_WorkProductUseRelationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_WorkProductUse43"):
                opp_val = getattr(old_value, "spem_WorkProductUse43", None)
                if opp_val == self:
                    setattr(old_value, "spem_WorkProductUse43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_WorkProductUse43"):
                opp_val = getattr(value, "spem_WorkProductUse43", None)
                setattr(value, "spem_WorkProductUse43", self)

    @property
    def spem_WorkProductUseRelationship45(self):
        return self.__spem_WorkProductUseRelationship45

    @spem_WorkProductUseRelationship45.setter
    def spem_WorkProductUseRelationship45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkProductUseRelationship__spem_WorkProductUseRelationship45", None)
        self.__spem_WorkProductUseRelationship45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_WorkProductUse46"):
                    opp_val = getattr(item, "spem_WorkProductUse46", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_WorkProductUse46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_WorkProductUse46"):
                    opp_val = getattr(item, "spem_WorkProductUse46", None)
                    
                    setattr(item, "spem_WorkProductUse46", self)
                    

class spem_ProcessPerformer(WorkDefinitionPerformer, BreakdownElement):

    pass
class spem_WorkBreakdownElement(BreakdownElement):

    def __init__(self, isRepeatable: bool, isOngoing: bool, isEventDriven: bool, successor: set["spem_WorkSequence"] = None, predecessor: set["spem_WorkSequence"] = None, WorkBreakdownElement: "spem_WorkSequence" = None, WorkBreakdownElement10: "spem_WorkSequence" = None):
        self.isRepeatable = isRepeatable
        self.isOngoing = isOngoing
        self.isEventDriven = isEventDriven
        self.successor = successor if successor is not None else set()
        self.predecessor = predecessor if predecessor is not None else set()
        self.WorkBreakdownElement = WorkBreakdownElement
        self.WorkBreakdownElement10 = WorkBreakdownElement10
        
    @property
    def isEventDriven(self) -> bool:
        return self.__isEventDriven

    @isEventDriven.setter
    def isEventDriven(self, isEventDriven: bool):
        self.__isEventDriven = isEventDriven

    @property
    def isRepeatable(self) -> bool:
        return self.__isRepeatable

    @isRepeatable.setter
    def isRepeatable(self, isRepeatable: bool):
        self.__isRepeatable = isRepeatable

    @property
    def isOngoing(self) -> bool:
        return self.__isOngoing

    @isOngoing.setter
    def isOngoing(self, isOngoing: bool):
        self.__isOngoing = isOngoing

    @property
    def predecessor(self):
        return self.__predecessor

    @predecessor.setter
    def predecessor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkBreakdownElement__predecessor", None)
        self.__predecessor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkSequence7"):
                    opp_val = getattr(item, "WorkSequence7", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkSequence7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkSequence7"):
                    opp_val = getattr(item, "WorkSequence7", None)
                    
                    setattr(item, "WorkSequence7", self)
                    

    @property
    def WorkBreakdownElement(self):
        return self.__WorkBreakdownElement

    @WorkBreakdownElement.setter
    def WorkBreakdownElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkBreakdownElement__WorkBreakdownElement", None)
        self.__WorkBreakdownElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "linkToSuccessor"):
                opp_val = getattr(old_value, "linkToSuccessor", None)
                if opp_val == self:
                    setattr(old_value, "linkToSuccessor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "linkToSuccessor"):
                opp_val = getattr(value, "linkToSuccessor", None)
                setattr(value, "linkToSuccessor", self)

    @property
    def successor(self):
        return self.__successor

    @successor.setter
    def successor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkBreakdownElement__successor", None)
        self.__successor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkSequence"):
                    opp_val = getattr(item, "WorkSequence", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkSequence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkSequence"):
                    opp_val = getattr(item, "WorkSequence", None)
                    
                    setattr(item, "WorkSequence", self)
                    

    @property
    def WorkBreakdownElement10(self):
        return self.__WorkBreakdownElement10

    @WorkBreakdownElement10.setter
    def WorkBreakdownElement10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkBreakdownElement__WorkBreakdownElement10", None)
        self.__WorkBreakdownElement10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "linkToPredecessor"):
                opp_val = getattr(old_value, "linkToPredecessor", None)
                if opp_val == self:
                    setattr(old_value, "linkToPredecessor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "linkToPredecessor"):
                opp_val = getattr(value, "linkToPredecessor", None)
                setattr(value, "linkToPredecessor", self)

class spem_MethodConfiguration(MethodLibraryPackageableElement):

    pass
class spem_ProcessParameter(WorkDefinitionParameter, BreakdownElement):

    def __init__(self, optionality: str, spem_ProcessParameter: "spem_Activity" = None, spem_ProcessParameter48: "spem_WorkProductUse" = None, spem_ProcessParameter116: "spem_TaskUse" = None):
        self.optionality = optionality
        self.spem_ProcessParameter = spem_ProcessParameter
        self.spem_ProcessParameter48 = spem_ProcessParameter48
        self.spem_ProcessParameter116 = spem_ProcessParameter116
        
    @property
    def optionality(self) -> str:
        return self.__optionality

    @optionality.setter
    def optionality(self, optionality: str):
        self.__optionality = optionality

    @property
    def spem_ProcessParameter(self):
        return self.__spem_ProcessParameter

    @spem_ProcessParameter.setter
    def spem_ProcessParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_ProcessParameter__spem_ProcessParameter", None)
        self.__spem_ProcessParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_Activity20"):
                opp_val = getattr(old_value, "spem_Activity20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_Activity20"):
                opp_val = getattr(value, "spem_Activity20", None)
                if opp_val is None:
                    setattr(value, "spem_Activity20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def spem_ProcessParameter48(self):
        return self.__spem_ProcessParameter48

    @spem_ProcessParameter48.setter
    def spem_ProcessParameter48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_ProcessParameter__spem_ProcessParameter48", None)
        self.__spem_ProcessParameter48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_WorkProductUse49"):
                opp_val = getattr(old_value, "spem_WorkProductUse49", None)
                if opp_val == self:
                    setattr(old_value, "spem_WorkProductUse49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_WorkProductUse49"):
                opp_val = getattr(value, "spem_WorkProductUse49", None)
                setattr(value, "spem_WorkProductUse49", self)

    @property
    def spem_ProcessParameter116(self):
        return self.__spem_ProcessParameter116

    @spem_ProcessParameter116.setter
    def spem_ProcessParameter116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_ProcessParameter__spem_ProcessParameter116", None)
        self.__spem_ProcessParameter116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_TaskUse115"):
                opp_val = getattr(old_value, "spem_TaskUse115", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_TaskUse115"):
                opp_val = getattr(value, "spem_TaskUse115", None)
                if opp_val is None:
                    setattr(value, "spem_TaskUse115", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class spem_WorkDefinitionParameter:

    def __init__(self, direction: str, spem_WorkDefinitionParameter: "spem_WorkDefinition" = None):
        self.direction = direction
        self.spem_WorkDefinitionParameter = spem_WorkDefinitionParameter
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def spem_WorkDefinitionParameter(self):
        return self.__spem_WorkDefinitionParameter

    @spem_WorkDefinitionParameter.setter
    def spem_WorkDefinitionParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkDefinitionParameter__spem_WorkDefinitionParameter", None)
        self.__spem_WorkDefinitionParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_WorkDefinition3"):
                opp_val = getattr(old_value, "spem_WorkDefinition3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_WorkDefinition3"):
                opp_val = getattr(value, "spem_WorkDefinition3", None)
                if opp_val is None:
                    setattr(value, "spem_WorkDefinition3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class spem_WorkDefinition(ABC):

    def __init__(self, preCondition: str, postCondition: str, spem_WorkDefinition: "spem_WorkDefinitionPerformer" = None, spem_WorkDefinition3: set["spem_WorkDefinitionParameter"] = None):
        self.preCondition = preCondition
        self.postCondition = postCondition
        self.spem_WorkDefinition = spem_WorkDefinition
        self.spem_WorkDefinition3 = spem_WorkDefinition3 if spem_WorkDefinition3 is not None else set()
        
    @property
    def preCondition(self) -> str:
        return self.__preCondition

    @preCondition.setter
    def preCondition(self, preCondition: str):
        self.__preCondition = preCondition

    @property
    def postCondition(self) -> str:
        return self.__postCondition

    @postCondition.setter
    def postCondition(self, postCondition: str):
        self.__postCondition = postCondition

    @property
    def spem_WorkDefinition(self):
        return self.__spem_WorkDefinition

    @spem_WorkDefinition.setter
    def spem_WorkDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkDefinition__spem_WorkDefinition", None)
        self.__spem_WorkDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_WorkDefinitionPerformer"):
                opp_val = getattr(old_value, "spem_WorkDefinitionPerformer", None)
                if opp_val == self:
                    setattr(old_value, "spem_WorkDefinitionPerformer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_WorkDefinitionPerformer"):
                opp_val = getattr(value, "spem_WorkDefinitionPerformer", None)
                setattr(value, "spem_WorkDefinitionPerformer", self)

    @property
    def spem_WorkDefinition3(self):
        return self.__spem_WorkDefinition3

    @spem_WorkDefinition3.setter
    def spem_WorkDefinition3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkDefinition__spem_WorkDefinition3", None)
        self.__spem_WorkDefinition3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_WorkDefinitionParameter"):
                    opp_val = getattr(item, "spem_WorkDefinitionParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_WorkDefinitionParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_WorkDefinitionParameter"):
                    opp_val = getattr(item, "spem_WorkDefinitionParameter", None)
                    
                    setattr(item, "spem_WorkDefinitionParameter", self)
                    

class spem_WorkDefinitionPerformer(ABC):

    pass
class ExtensibleElement:

    pass
class spem_DescribableElement(ExtensibleElement):

    def __init__(self, presentationName: str, briefDescription: str, mainDescription: str, purpose: str, copyright: str, author: str, changeDate: date, changeDescription: str, version: str, DescribableElement: "spem_Category" = None, spem_DescribableElement: set["spem_Guidance"] = None, spem_DescribableElement55: set["spem_Metric"] = None, categorizedElement: set["spem_Category"] = None):
        self.presentationName = presentationName
        self.briefDescription = briefDescription
        self.mainDescription = mainDescription
        self.purpose = purpose
        self.copyright = copyright
        self.author = author
        self.changeDate = changeDate
        self.changeDescription = changeDescription
        self.version = version
        self.DescribableElement = DescribableElement
        self.spem_DescribableElement = spem_DescribableElement if spem_DescribableElement is not None else set()
        self.spem_DescribableElement55 = spem_DescribableElement55 if spem_DescribableElement55 is not None else set()
        self.categorizedElement = categorizedElement if categorizedElement is not None else set()
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def changeDescription(self) -> str:
        return self.__changeDescription

    @changeDescription.setter
    def changeDescription(self, changeDescription: str):
        self.__changeDescription = changeDescription

    @property
    def purpose(self) -> str:
        return self.__purpose

    @purpose.setter
    def purpose(self, purpose: str):
        self.__purpose = purpose

    @property
    def briefDescription(self) -> str:
        return self.__briefDescription

    @briefDescription.setter
    def briefDescription(self, briefDescription: str):
        self.__briefDescription = briefDescription

    @property
    def copyright(self) -> str:
        return self.__copyright

    @copyright.setter
    def copyright(self, copyright: str):
        self.__copyright = copyright

    @property
    def mainDescription(self) -> str:
        return self.__mainDescription

    @mainDescription.setter
    def mainDescription(self, mainDescription: str):
        self.__mainDescription = mainDescription

    @property
    def presentationName(self) -> str:
        return self.__presentationName

    @presentationName.setter
    def presentationName(self, presentationName: str):
        self.__presentationName = presentationName

    @property
    def changeDate(self) -> date:
        return self.__changeDate

    @changeDate.setter
    def changeDate(self, changeDate: date):
        self.__changeDate = changeDate

    @property
    def spem_DescribableElement55(self):
        return self.__spem_DescribableElement55

    @spem_DescribableElement55.setter
    def spem_DescribableElement55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_DescribableElement__spem_DescribableElement55", None)
        self.__spem_DescribableElement55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_Metric"):
                    opp_val = getattr(item, "spem_Metric", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_Metric", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_Metric"):
                    opp_val = getattr(item, "spem_Metric", None)
                    
                    setattr(item, "spem_Metric", self)
                    

    @property
    def spem_DescribableElement(self):
        return self.__spem_DescribableElement

    @spem_DescribableElement.setter
    def spem_DescribableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_DescribableElement__spem_DescribableElement", None)
        self.__spem_DescribableElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_Guidance"):
                    opp_val = getattr(item, "spem_Guidance", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_Guidance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_Guidance"):
                    opp_val = getattr(item, "spem_Guidance", None)
                    
                    setattr(item, "spem_Guidance", self)
                    

    @property
    def categorizedElement(self):
        return self.__categorizedElement

    @categorizedElement.setter
    def categorizedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_DescribableElement__categorizedElement", None)
        self.__categorizedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Category"):
                    opp_val = getattr(item, "Category", None)
                    
                    if opp_val == self:
                        setattr(item, "Category", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Category"):
                    opp_val = getattr(item, "Category", None)
                    
                    setattr(item, "Category", self)
                    

    @property
    def DescribableElement(self):
        return self.__DescribableElement

    @DescribableElement.setter
    def DescribableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_DescribableElement__DescribableElement", None)
        self.__DescribableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "category"):
                opp_val = getattr(old_value, "category", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "category"):
                opp_val = getattr(value, "category", None)
                if opp_val is None:
                    setattr(value, "category", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class spem_Kind(ExtensibleElement):

    pass
class spem_ExtensibleElement(ABC):

    pass
class ProcessElement:

    pass
class spem_WorkProductPortConnector(ProcessElement):

    pass
class spem_ProcessKind(Kind, ProcessElement):

    pass
class spem_WorkProductPort(ProcessElement):

    def __init__(self, portKind: str, isOptional: bool, spem_WorkProductPort: "spem_ProcessComponent" = None, spem_WorkProductPort136: "spem_ProcessComponentUse" = None, spem_WorkProductPort175: "spem_WorkProductDefinition" = None, spem_WorkProductPort178: "spem_WorkProductPortConnector" = None):
        self.portKind = portKind
        self.isOptional = isOptional
        self.spem_WorkProductPort = spem_WorkProductPort
        self.spem_WorkProductPort136 = spem_WorkProductPort136
        self.spem_WorkProductPort175 = spem_WorkProductPort175
        self.spem_WorkProductPort178 = spem_WorkProductPort178
        
    @property
    def portKind(self) -> str:
        return self.__portKind

    @portKind.setter
    def portKind(self, portKind: str):
        self.__portKind = portKind

    @property
    def isOptional(self) -> bool:
        return self.__isOptional

    @isOptional.setter
    def isOptional(self, isOptional: bool):
        self.__isOptional = isOptional

    @property
    def spem_WorkProductPort178(self):
        return self.__spem_WorkProductPort178

    @spem_WorkProductPort178.setter
    def spem_WorkProductPort178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkProductPort__spem_WorkProductPort178", None)
        self.__spem_WorkProductPort178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_WorkProductPortConnector"):
                opp_val = getattr(old_value, "spem_WorkProductPortConnector", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_WorkProductPortConnector"):
                opp_val = getattr(value, "spem_WorkProductPortConnector", None)
                if opp_val is None:
                    setattr(value, "spem_WorkProductPortConnector", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def spem_WorkProductPort(self):
        return self.__spem_WorkProductPort

    @spem_WorkProductPort.setter
    def spem_WorkProductPort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkProductPort__spem_WorkProductPort", None)
        self.__spem_WorkProductPort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_ProcessComponent131"):
                opp_val = getattr(old_value, "spem_ProcessComponent131", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_ProcessComponent131"):
                opp_val = getattr(value, "spem_ProcessComponent131", None)
                if opp_val is None:
                    setattr(value, "spem_ProcessComponent131", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def spem_WorkProductPort136(self):
        return self.__spem_WorkProductPort136

    @spem_WorkProductPort136.setter
    def spem_WorkProductPort136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkProductPort__spem_WorkProductPort136", None)
        self.__spem_WorkProductPort136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_ProcessComponentUse135"):
                opp_val = getattr(old_value, "spem_ProcessComponentUse135", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_ProcessComponentUse135"):
                opp_val = getattr(value, "spem_ProcessComponentUse135", None)
                if opp_val is None:
                    setattr(value, "spem_ProcessComponentUse135", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def spem_WorkProductPort175(self):
        return self.__spem_WorkProductPort175

    @spem_WorkProductPort175.setter
    def spem_WorkProductPort175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkProductPort__spem_WorkProductPort175", None)
        self.__spem_WorkProductPort175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_WorkProductDefinition176"):
                opp_val = getattr(old_value, "spem_WorkProductDefinition176", None)
                if opp_val == self:
                    setattr(old_value, "spem_WorkProductDefinition176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_WorkProductDefinition176"):
                opp_val = getattr(value, "spem_WorkProductDefinition176", None)
                setattr(value, "spem_WorkProductDefinition176", self)

class spem_PlanningData(ProcessElement):

    def __init__(self, startDate: date, finishDate: date, rank: int, duration: str, spem_PlanningData: "spem_BreakdownElement" = None):
        self.startDate = startDate
        self.finishDate = finishDate
        self.rank = rank
        self.duration = duration
        self.spem_PlanningData = spem_PlanningData
        
    @property
    def startDate(self) -> date:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate

    @property
    def duration(self) -> str:
        return self.__duration

    @duration.setter
    def duration(self, duration: str):
        self.__duration = duration

    @property
    def finishDate(self) -> date:
        return self.__finishDate

    @finishDate.setter
    def finishDate(self, finishDate: date):
        self.__finishDate = finishDate

    @property
    def rank(self) -> int:
        return self.__rank

    @rank.setter
    def rank(self, rank: int):
        self.__rank = rank

    @property
    def spem_PlanningData(self):
        return self.__spem_PlanningData

    @spem_PlanningData.setter
    def spem_PlanningData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_PlanningData__spem_PlanningData", None)
        self.__spem_PlanningData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_BreakdownElement"):
                opp_val = getattr(old_value, "spem_BreakdownElement", None)
                if opp_val == self:
                    setattr(old_value, "spem_BreakdownElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_BreakdownElement"):
                opp_val = getattr(value, "spem_BreakdownElement", None)
                setattr(value, "spem_BreakdownElement", self)

class spem_BreakdownElement(ProcessElement):

    def __init__(self, hasMultipleOccurrences: bool, isOptional: bool, isPlanned: bool, spem_BreakdownElement15: "spem_Activity" = None, spem_BreakdownElement18: "spem_Activity" = None, spem_BreakdownElement: "spem_PlanningData" = None):
        self.hasMultipleOccurrences = hasMultipleOccurrences
        self.isOptional = isOptional
        self.isPlanned = isPlanned
        self.spem_BreakdownElement15 = spem_BreakdownElement15
        self.spem_BreakdownElement18 = spem_BreakdownElement18
        self.spem_BreakdownElement = spem_BreakdownElement
        
    @property
    def isOptional(self) -> bool:
        return self.__isOptional

    @isOptional.setter
    def isOptional(self, isOptional: bool):
        self.__isOptional = isOptional

    @property
    def hasMultipleOccurrences(self) -> bool:
        return self.__hasMultipleOccurrences

    @hasMultipleOccurrences.setter
    def hasMultipleOccurrences(self, hasMultipleOccurrences: bool):
        self.__hasMultipleOccurrences = hasMultipleOccurrences

    @property
    def isPlanned(self) -> bool:
        return self.__isPlanned

    @isPlanned.setter
    def isPlanned(self, isPlanned: bool):
        self.__isPlanned = isPlanned

    @property
    def spem_BreakdownElement(self):
        return self.__spem_BreakdownElement

    @spem_BreakdownElement.setter
    def spem_BreakdownElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_BreakdownElement__spem_BreakdownElement", None)
        self.__spem_BreakdownElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_PlanningData"):
                opp_val = getattr(old_value, "spem_PlanningData", None)
                if opp_val == self:
                    setattr(old_value, "spem_PlanningData", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_PlanningData"):
                opp_val = getattr(value, "spem_PlanningData", None)
                setattr(value, "spem_PlanningData", self)

    @property
    def spem_BreakdownElement15(self):
        return self.__spem_BreakdownElement15

    @spem_BreakdownElement15.setter
    def spem_BreakdownElement15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_BreakdownElement__spem_BreakdownElement15", None)
        self.__spem_BreakdownElement15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_Activity14"):
                opp_val = getattr(old_value, "spem_Activity14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_Activity14"):
                opp_val = getattr(value, "spem_Activity14", None)
                if opp_val is None:
                    setattr(value, "spem_Activity14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def spem_BreakdownElement18(self):
        return self.__spem_BreakdownElement18

    @spem_BreakdownElement18.setter
    def spem_BreakdownElement18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_BreakdownElement__spem_BreakdownElement18", None)
        self.__spem_BreakdownElement18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_Activity17"):
                opp_val = getattr(old_value, "spem_Activity17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_Activity17"):
                opp_val = getattr(value, "spem_Activity17", None)
                if opp_val is None:
                    setattr(value, "spem_Activity17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
