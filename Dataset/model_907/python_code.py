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
class ParameterDirectionKind(Enum):
    in = "in"
    out = "out"
    inout = "inout"
class ExpertiseLevel(Enum):
    LOW = "LOW"
    MID = "MID"
    LEVEL = "LEVEL"
class WorkSequenceKind(Enum):
    finishToStart = "finishToStart"
    finishToFinish = "finishToFinish"
    startToStart = "startToStart"
    startToFinish = "startToFinish"
class EstimatingTechnique(Enum):
    COST = "COST"
    TIME = "TIME"
    SKILLS = "SKILLS"
    DEFECTS = "DEFECTS"
    OTHER = "OTHER"
class OptionalityKind(Enum):
    mandatory = "mandatory"
    optional = "optional"
class ContractKind(Enum):
    EXPRESS = "EXPRESS"
    IMPLIED = "IMPLIED"
    OTHER = "OTHER"
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
class uma_spem_MethodContentElement:

    pass
class uma_spem_Activity:

    pass
class Practice:

    pass
class Concept:

    pass
class spem_uma_Whitepaper(Concept):

    pass
class uma_spem_TaskDefinition:

    pass
class SupportingMaterial:

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
class uma_spem_WorkProductUse:

    pass
class Category:

    pass
class spem_uma_Domain(Category):

    pass
class spem_uma_Discipline(Category):

    pass
class spem_uma_DisciplineGrouping(Category):

    pass
class spem_uma_CustomCategory(Category):

    pass
class MethodContentPackage:

    pass
class spem_uma_GuidancePackage(MethodContentPackage):

    pass
class spem_uma_WorkProductDefinitionPackage(MethodContentPackage):

    pass
class spem_uma_QualificationPackage(MethodContentPackage):

    pass
class spem_uma_TaskDefinitionPackage(MethodContentPackage):

    pass
class spem_uma_ConfigurationPackage(MethodContentPackage):

    pass
class spem_uma_RoleDefinitionPackage(MethodContentPackage):

    pass
class spem_uma_RoleSetPackage(MethodContentPackage):

    pass
class spem_uma_WorkProductKindPackage(MethodContentPackage):

    pass
class spem_uma_ToolDefinitionPackage(MethodContentPackage):

    pass
class spem_uma_DomainPackage(MethodContentPackage):

    pass
class spem_uma_DisciplinePackage(MethodContentPackage):

    pass
class spem_uma_CategoryPackage(MethodContentPackage):

    pass
class Process:

    pass
class spem_uma_ProcessPlanningTemplate(Process):

    pass
class spem_uma_CapabilityPattern(Process):

    pass
class Artifact:

    pass
class WorkProductUse:

    pass
class spem_uma_Deliverable(WorkProductUse):

    def __init__(self, packagingGuidance: str, externalDescription: str, spem_uma_Deliverable: set["uma_spem_WorkProductUse"] = None):
        self.packagingGuidance = packagingGuidance
        self.externalDescription = externalDescription
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
class MethodContentKind:

    pass
class spem_WorkProductKind(MethodContentKind):

    pass
class spem_uma_DeliveryProcess(Process):

    def __init__(self, scale: str, projectCharacteristics: str, riskLevel: str, estimatingTechnique: str, projectMemberExpertise: str, typeOfContract: str, spem_uma_DeliveryProcess: set["SupportingMaterial"] = None, spem_uma_DeliveryProcess214: set["SupportingMaterial"] = None, Process231: "spem_uma_ProcessPlanningTemplate", Process: "spem_uma_Discipline"):
        self.scale = scale
        self.projectCharacteristics = projectCharacteristics
        self.riskLevel = riskLevel
        self.estimatingTechnique = estimatingTechnique
        self.projectMemberExpertise = projectMemberExpertise
        self.typeOfContract = typeOfContract
        self.spem_uma_DeliveryProcess = spem_uma_DeliveryProcess if spem_uma_DeliveryProcess is not None else set()
        self.spem_uma_DeliveryProcess214 = spem_uma_DeliveryProcess214 if spem_uma_DeliveryProcess214 is not None else set()
        
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
    def estimatingTechnique(self) -> str:
        return self.__estimatingTechnique

    @estimatingTechnique.setter
    def estimatingTechnique(self, estimatingTechnique: str):
        self.__estimatingTechnique = estimatingTechnique

    @property
    def riskLevel(self) -> str:
        return self.__riskLevel

    @riskLevel.setter
    def riskLevel(self, riskLevel: str):
        self.__riskLevel = riskLevel

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
    def spem_uma_DeliveryProcess214(self):
        return self.__spem_uma_DeliveryProcess214

    @spem_uma_DeliveryProcess214.setter
    def spem_uma_DeliveryProcess214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_uma_DeliveryProcess__spem_uma_DeliveryProcess214", None)
        self.__spem_uma_DeliveryProcess214 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SupportingMaterial215"):
                    opp_val = getattr(item, "SupportingMaterial215", None)
                    
                    if opp_val == self:
                        setattr(item, "SupportingMaterial215", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SupportingMaterial215"):
                    opp_val = getattr(item, "SupportingMaterial215", None)
                    
                    setattr(item, "SupportingMaterial215", self)
                    

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
                    

class uma_spem_WorkProductPortConnector:

    pass
class CapabilityPattern:

    pass
class Activity:

    pass
class spem_uma_Iteration(Activity):

    pass
class spem_uma_Phase(Activity):

    pass
class spem_uma_Process(Activity):

    def __init__(self, scope: str, usageNote: str, spem_uma_Process: set["CapabilityPattern"] = None, spem_uma_Process211: set["uma_spem_WorkProductPortConnector"] = None):
        self.scope = scope
        self.usageNote = usageNote
        self.spem_uma_Process = spem_uma_Process if spem_uma_Process is not None else set()
        self.spem_uma_Process211 = spem_uma_Process211 if spem_uma_Process211 is not None else set()
        
    @property
    def usageNote(self) -> str:
        return self.__usageNote

    @usageNote.setter
    def usageNote(self, usageNote: str):
        self.__usageNote = usageNote

    @property
    def scope(self) -> str:
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope

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
    def spem_uma_Process211(self):
        return self.__spem_uma_Process211

    @spem_uma_Process211.setter
    def spem_uma_Process211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_uma_Process__spem_uma_Process211", None)
        self.__spem_uma_Process211 = value if value is not None else set()
        
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
                    

class spem_MethodLibrary:

    def __init__(self, name: str, spem_MethodLibrary196: "spem_ToolDefinition" = None, spem_MethodLibrary199: "ConfigurationPackage" = None, spem_MethodLibrary201: set["spem_EObject"] = None, spem_MethodLibrary: set["spem_MethodPlugin"] = None, spem_MethodLibrary193: set["spem_MethodConfiguration"] = None):
        self.name = name
        self.spem_MethodLibrary196 = spem_MethodLibrary196
        self.spem_MethodLibrary199 = spem_MethodLibrary199
        self.spem_MethodLibrary201 = spem_MethodLibrary201 if spem_MethodLibrary201 is not None else set()
        self.spem_MethodLibrary = spem_MethodLibrary if spem_MethodLibrary is not None else set()
        self.spem_MethodLibrary193 = spem_MethodLibrary193 if spem_MethodLibrary193 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def spem_MethodLibrary193(self):
        return self.__spem_MethodLibrary193

    @spem_MethodLibrary193.setter
    def spem_MethodLibrary193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_MethodLibrary__spem_MethodLibrary193", None)
        self.__spem_MethodLibrary193 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_MethodConfiguration194"):
                    opp_val = getattr(item, "spem_MethodConfiguration194", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_MethodConfiguration194", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_MethodConfiguration194"):
                    opp_val = getattr(item, "spem_MethodConfiguration194", None)
                    
                    setattr(item, "spem_MethodConfiguration194", self)
                    

    @property
    def spem_MethodLibrary196(self):
        return self.__spem_MethodLibrary196

    @spem_MethodLibrary196.setter
    def spem_MethodLibrary196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_MethodLibrary__spem_MethodLibrary196", None)
        self.__spem_MethodLibrary196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_ToolDefinition197"):
                opp_val = getattr(old_value, "spem_ToolDefinition197", None)
                if opp_val == self:
                    setattr(old_value, "spem_ToolDefinition197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_ToolDefinition197"):
                opp_val = getattr(value, "spem_ToolDefinition197", None)
                setattr(value, "spem_ToolDefinition197", self)

    @property
    def spem_MethodLibrary199(self):
        return self.__spem_MethodLibrary199

    @spem_MethodLibrary199.setter
    def spem_MethodLibrary199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_MethodLibrary__spem_MethodLibrary199", None)
        self.__spem_MethodLibrary199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConfigurationPackage"):
                opp_val = getattr(old_value, "ConfigurationPackage", None)
                if opp_val == self:
                    setattr(old_value, "ConfigurationPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConfigurationPackage"):
                opp_val = getattr(value, "ConfigurationPackage", None)
                setattr(value, "ConfigurationPackage", self)

    @property
    def spem_MethodLibrary201(self):
        return self.__spem_MethodLibrary201

    @spem_MethodLibrary201.setter
    def spem_MethodLibrary201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_MethodLibrary__spem_MethodLibrary201", None)
        self.__spem_MethodLibrary201 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_EObject"):
                    opp_val = getattr(item, "spem_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_EObject"):
                    opp_val = getattr(item, "spem_EObject", None)
                    
                    setattr(item, "spem_EObject", self)
                    

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
                if hasattr(item, "spem_MethodPlugin191"):
                    opp_val = getattr(item, "spem_MethodPlugin191", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_MethodPlugin191", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_MethodPlugin191"):
                    opp_val = getattr(item, "spem_MethodPlugin191", None)
                    
                    setattr(item, "spem_MethodPlugin191", self)
                    

class spem_EObject:

    pass
class ConfigurationPackage:

    pass
class MethodLibraryPackageableElement:

    pass
class spem_MethodPlugin(MethodLibraryPackageableElement):

    def __init__(self, userChangeable: bool, supporting: str, spem_MethodPlugin: "spem_MethodConfiguration" = None, spem_MethodPlugin179: set["spem_MethodContentPackage"] = None, spem_MethodPlugin182: set["spem_ProcessPackage"] = None, spem_MethodPlugin186: "spem_MethodPlugin" = None, spem_MethodPlugin184: set["spem_MethodPlugin"] = None, spem_MethodPlugin189: "spem_MethodPlugin" = None, spem_MethodPlugin187: set["spem_MethodPlugin"] = None, spem_MethodPlugin191: "spem_MethodLibrary" = None):
        self.userChangeable = userChangeable
        self.supporting = supporting
        self.spem_MethodPlugin = spem_MethodPlugin
        self.spem_MethodPlugin179 = spem_MethodPlugin179 if spem_MethodPlugin179 is not None else set()
        self.spem_MethodPlugin182 = spem_MethodPlugin182 if spem_MethodPlugin182 is not None else set()
        self.spem_MethodPlugin186 = spem_MethodPlugin186
        self.spem_MethodPlugin184 = spem_MethodPlugin184 if spem_MethodPlugin184 is not None else set()
        self.spem_MethodPlugin189 = spem_MethodPlugin189
        self.spem_MethodPlugin187 = spem_MethodPlugin187 if spem_MethodPlugin187 is not None else set()
        self.spem_MethodPlugin191 = spem_MethodPlugin191
        
    @property
    def userChangeable(self) -> bool:
        return self.__userChangeable

    @userChangeable.setter
    def userChangeable(self, userChangeable: bool):
        self.__userChangeable = userChangeable

    @property
    def supporting(self) -> str:
        return self.__supporting

    @supporting.setter
    def supporting(self, supporting: str):
        self.__supporting = supporting

    @property
    def spem_MethodPlugin184(self):
        return self.__spem_MethodPlugin184

    @spem_MethodPlugin184.setter
    def spem_MethodPlugin184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_MethodPlugin__spem_MethodPlugin184", None)
        self.__spem_MethodPlugin184 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_MethodPlugin186"):
                    opp_val = getattr(item, "spem_MethodPlugin186", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_MethodPlugin186", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_MethodPlugin186"):
                    opp_val = getattr(item, "spem_MethodPlugin186", None)
                    
                    setattr(item, "spem_MethodPlugin186", self)
                    

    @property
    def spem_MethodPlugin191(self):
        return self.__spem_MethodPlugin191

    @spem_MethodPlugin191.setter
    def spem_MethodPlugin191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_MethodPlugin__spem_MethodPlugin191", None)
        self.__spem_MethodPlugin191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_MethodLibrary"):
                opp_val = getattr(old_value, "spem_MethodLibrary", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_MethodLibrary"):
                opp_val = getattr(value, "spem_MethodLibrary", None)
                if opp_val is None:
                    setattr(value, "spem_MethodLibrary", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def spem_MethodPlugin182(self):
        return self.__spem_MethodPlugin182

    @spem_MethodPlugin182.setter
    def spem_MethodPlugin182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_MethodPlugin__spem_MethodPlugin182", None)
        self.__spem_MethodPlugin182 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_ProcessPackage183"):
                    opp_val = getattr(item, "spem_ProcessPackage183", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_ProcessPackage183", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_ProcessPackage183"):
                    opp_val = getattr(item, "spem_ProcessPackage183", None)
                    
                    setattr(item, "spem_ProcessPackage183", self)
                    

    @property
    def spem_MethodPlugin186(self):
        return self.__spem_MethodPlugin186

    @spem_MethodPlugin186.setter
    def spem_MethodPlugin186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_MethodPlugin__spem_MethodPlugin186", None)
        self.__spem_MethodPlugin186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_MethodPlugin184"):
                opp_val = getattr(old_value, "spem_MethodPlugin184", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_MethodPlugin184"):
                opp_val = getattr(value, "spem_MethodPlugin184", None)
                if opp_val is None:
                    setattr(value, "spem_MethodPlugin184", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def spem_MethodPlugin187(self):
        return self.__spem_MethodPlugin187

    @spem_MethodPlugin187.setter
    def spem_MethodPlugin187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_MethodPlugin__spem_MethodPlugin187", None)
        self.__spem_MethodPlugin187 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_MethodPlugin189"):
                    opp_val = getattr(item, "spem_MethodPlugin189", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_MethodPlugin189", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_MethodPlugin189"):
                    opp_val = getattr(item, "spem_MethodPlugin189", None)
                    
                    setattr(item, "spem_MethodPlugin189", self)
                    

    @property
    def spem_MethodPlugin189(self):
        return self.__spem_MethodPlugin189

    @spem_MethodPlugin189.setter
    def spem_MethodPlugin189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_MethodPlugin__spem_MethodPlugin189", None)
        self.__spem_MethodPlugin189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_MethodPlugin187"):
                opp_val = getattr(old_value, "spem_MethodPlugin187", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_MethodPlugin187"):
                opp_val = getattr(value, "spem_MethodPlugin187", None)
                if opp_val is None:
                    setattr(value, "spem_MethodPlugin187", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def spem_MethodPlugin(self):
        return self.__spem_MethodPlugin

    @spem_MethodPlugin.setter
    def spem_MethodPlugin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_MethodPlugin__spem_MethodPlugin", None)
        self.__spem_MethodPlugin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_MethodConfiguration159"):
                opp_val = getattr(old_value, "spem_MethodConfiguration159", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_MethodConfiguration159"):
                opp_val = getattr(value, "spem_MethodConfiguration159", None)
                if opp_val is None:
                    setattr(value, "spem_MethodConfiguration159", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def spem_MethodPlugin179(self):
        return self.__spem_MethodPlugin179

    @spem_MethodPlugin179.setter
    def spem_MethodPlugin179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_MethodPlugin__spem_MethodPlugin179", None)
        self.__spem_MethodPlugin179 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_MethodContentPackage180"):
                    opp_val = getattr(item, "spem_MethodContentPackage180", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_MethodContentPackage180", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_MethodContentPackage180"):
                    opp_val = getattr(item, "spem_MethodContentPackage180", None)
                    
                    setattr(item, "spem_MethodContentPackage180", self)
                    

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
class ProcessPackage:

    pass
class spem_uma_CapabilityPatternPackage(ProcessPackage):

    pass
class spem_uma_ProcessComponentPackage(ProcessPackage):

    pass
class spem_uma_DeliveryProcessPackage(ProcessPackage):

    pass
class spem_ProcessComponent(ProcessPackage):

    def __init__(self, copyright: str, author: str, version: str, changeDate: date, changeDescription: str, spem_ProcessComponent: "spem_Activity" = None, spem_ProcessComponent149: set["spem_WorkProductPort"] = None, spem_ProcessComponent151: "spem_ProcessComponentUse" = None):
        self.copyright = copyright
        self.author = author
        self.version = version
        self.changeDate = changeDate
        self.changeDescription = changeDescription
        self.spem_ProcessComponent = spem_ProcessComponent
        self.spem_ProcessComponent149 = spem_ProcessComponent149 if spem_ProcessComponent149 is not None else set()
        self.spem_ProcessComponent151 = spem_ProcessComponent151
        
    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def changeDate(self) -> date:
        return self.__changeDate

    @changeDate.setter
    def changeDate(self, changeDate: date):
        self.__changeDate = changeDate

    @property
    def changeDescription(self) -> str:
        return self.__changeDescription

    @changeDescription.setter
    def changeDescription(self, changeDescription: str):
        self.__changeDescription = changeDescription

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def copyright(self) -> str:
        return self.__copyright

    @copyright.setter
    def copyright(self, copyright: str):
        self.__copyright = copyright

    @property
    def spem_ProcessComponent149(self):
        return self.__spem_ProcessComponent149

    @spem_ProcessComponent149.setter
    def spem_ProcessComponent149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_ProcessComponent__spem_ProcessComponent149", None)
        self.__spem_ProcessComponent149 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_WorkProductPort"):
                    opp_val = getattr(item, "spem_WorkProductPort", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_WorkProductPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_WorkProductPort"):
                    opp_val = getattr(item, "spem_WorkProductPort", None)
                    
                    setattr(item, "spem_WorkProductPort", self)
                    

    @property
    def spem_ProcessComponent(self):
        return self.__spem_ProcessComponent

    @spem_ProcessComponent.setter
    def spem_ProcessComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_ProcessComponent__spem_ProcessComponent", None)
        self.__spem_ProcessComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_Activity147"):
                opp_val = getattr(old_value, "spem_Activity147", None)
                if opp_val == self:
                    setattr(old_value, "spem_Activity147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_Activity147"):
                opp_val = getattr(value, "spem_Activity147", None)
                setattr(value, "spem_Activity147", self)

    @property
    def spem_ProcessComponent151(self):
        return self.__spem_ProcessComponent151

    @spem_ProcessComponent151.setter
    def spem_ProcessComponent151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_ProcessComponent__spem_ProcessComponent151", None)
        self.__spem_ProcessComponent151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_ProcessComponentUse"):
                opp_val = getattr(old_value, "spem_ProcessComponentUse", None)
                if opp_val == self:
                    setattr(old_value, "spem_ProcessComponentUse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_ProcessComponentUse"):
                opp_val = getattr(value, "spem_ProcessComponentUse", None)
                setattr(value, "spem_ProcessComponentUse", self)

class spem_VariabilityElement(ABC):

    def __init__(self, variabilityType: str, spem_VariabilityElement: "spem_VariabilityElement" = None, spem_VariabilityElement144: "spem_VariabilityElement" = None):
        self.variabilityType = variabilityType
        self.spem_VariabilityElement = spem_VariabilityElement
        self.spem_VariabilityElement144 = spem_VariabilityElement144
        
    @property
    def variabilityType(self) -> str:
        return self.__variabilityType

    @variabilityType.setter
    def variabilityType(self, variabilityType: str):
        self.__variabilityType = variabilityType

    @property
    def spem_VariabilityElement144(self):
        return self.__spem_VariabilityElement144

    @spem_VariabilityElement144.setter
    def spem_VariabilityElement144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_VariabilityElement__spem_VariabilityElement144", None)
        self.__spem_VariabilityElement144 = value
        
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
            if hasattr(old_value, "spem_VariabilityElement144"):
                opp_val = getattr(old_value, "spem_VariabilityElement144", None)
                if opp_val == self:
                    setattr(old_value, "spem_VariabilityElement144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_VariabilityElement144"):
                opp_val = getattr(value, "spem_VariabilityElement144", None)
                setattr(value, "spem_VariabilityElement144", self)

class RoleUse:

    pass
class spem_CompositeRole(RoleUse):

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

class ToolMentor:

    pass
class Template:

    pass
class Report:

    pass
class EstimatingConsideration:

    pass
class ProcessPackageableElement:

    pass
class spem_ProcessPackage(ProcessPackageableElement, MethodPluginPackageableElement):

    pass
class MethodContentPackageableElement:

    pass
class spem_MethodContentPackage(MethodContentPackageableElement, MethodPluginPackageableElement):

    pass
class Guidance:

    pass
class spem_uma_Template(Guidance):

    pass
class spem_uma_EstimatingConsideration(Guidance):

    pass
class spem_uma_Report(Guidance):

    pass
class spem_uma_SupportingMaterial(Guidance):

    pass
class spem_Metric(Guidance):

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
            if hasattr(old_value, "spem_DescribableElement59"):
                opp_val = getattr(old_value, "spem_DescribableElement59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_DescribableElement59"):
                opp_val = getattr(value, "spem_DescribableElement59", None)
                if opp_val is None:
                    setattr(value, "spem_DescribableElement59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class spem_uma_Practice(Guidance):

    def __init__(self, additionalInfo: str, application: str, background: str, goal: str, levelOfAdoption: str, problem: str, spem_uma_Practice: set["Practice"] = None, spem_uma_Practice227: set["uma_spem_Activity"] = None, spem_uma_Practice229: set["uma_spem_MethodContentElement"] = None):
        self.additionalInfo = additionalInfo
        self.application = application
        self.background = background
        self.goal = goal
        self.levelOfAdoption = levelOfAdoption
        self.problem = problem
        self.spem_uma_Practice = spem_uma_Practice if spem_uma_Practice is not None else set()
        self.spem_uma_Practice227 = spem_uma_Practice227 if spem_uma_Practice227 is not None else set()
        self.spem_uma_Practice229 = spem_uma_Practice229 if spem_uma_Practice229 is not None else set()
        
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
    def problem(self) -> str:
        return self.__problem

    @problem.setter
    def problem(self, problem: str):
        self.__problem = problem

    @property
    def background(self) -> str:
        return self.__background

    @background.setter
    def background(self, background: str):
        self.__background = background

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
                    

    @property
    def spem_uma_Practice229(self):
        return self.__spem_uma_Practice229

    @spem_uma_Practice229.setter
    def spem_uma_Practice229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_uma_Practice__spem_uma_Practice229", None)
        self.__spem_uma_Practice229 = value if value is not None else set()
        
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
    def spem_uma_Practice227(self):
        return self.__spem_uma_Practice227

    @spem_uma_Practice227.setter
    def spem_uma_Practice227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_uma_Practice__spem_uma_Practice227", None)
        self.__spem_uma_Practice227 = value if value is not None else set()
        
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
                    

class spem_uma_Checklist(Guidance):

    pass
class spem_uma_Concept(Guidance):

    pass
class spem_uma_Example(Guidance):

    pass
class spem_uma_TermDefinition(Guidance):

    pass
class spem_uma_ToolMentor(Guidance):

    pass
class spem_uma_Guideline(Guidance):

    pass
class spem_uma_ReusableAsset(Guidance):

    pass
class spem_uma_Roadmap(Guidance):

    pass
class MethodContentElement:

    pass
class spem_Category(MethodContentElement):

    pass
class spem_ToolDefinition(MethodContentElement):

    pass
class spem_Qualification(MethodContentElement):

    pass
class spem_WorkProductDefinitionRelationship(MethodContentElement):

    pass
class spem_uma_RoleSet(MethodContentElement):

    pass
class spem_MethodContentKind(MethodContentElement, Kind):

    pass
class spem_Default_ResponsibilityAssignment(MethodContentElement):

    pass
class spem_Default_TaskDefinitionPerformer(MethodContentElement):

    pass
class spem_RoleDefinition(MethodContentElement):

    def __init__(self, synonym: str, spem_RoleDefinition: "spem_RoleUse" = None, spem_RoleDefinition104: set["spem_Qualification"] = None, spem_RoleDefinition115: "spem_Default_TaskDefinitionPerformer" = None, spem_RoleDefinition117: "spem_Default_ResponsibilityAssignment" = None, spem_RoleDefinition136: "spem_CompositeRole" = None):
        self.synonym = synonym
        self.spem_RoleDefinition = spem_RoleDefinition
        self.spem_RoleDefinition104 = spem_RoleDefinition104 if spem_RoleDefinition104 is not None else set()
        self.spem_RoleDefinition115 = spem_RoleDefinition115
        self.spem_RoleDefinition117 = spem_RoleDefinition117
        self.spem_RoleDefinition136 = spem_RoleDefinition136
        
    @property
    def synonym(self) -> str:
        return self.__synonym

    @synonym.setter
    def synonym(self, synonym: str):
        self.__synonym = synonym

    @property
    def spem_RoleDefinition117(self):
        return self.__spem_RoleDefinition117

    @spem_RoleDefinition117.setter
    def spem_RoleDefinition117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_RoleDefinition__spem_RoleDefinition117", None)
        self.__spem_RoleDefinition117 = value
        
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
    def spem_RoleDefinition(self):
        return self.__spem_RoleDefinition

    @spem_RoleDefinition.setter
    def spem_RoleDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_RoleDefinition__spem_RoleDefinition", None)
        self.__spem_RoleDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_RoleUse38"):
                opp_val = getattr(old_value, "spem_RoleUse38", None)
                if opp_val == self:
                    setattr(old_value, "spem_RoleUse38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_RoleUse38"):
                opp_val = getattr(value, "spem_RoleUse38", None)
                setattr(value, "spem_RoleUse38", self)

    @property
    def spem_RoleDefinition115(self):
        return self.__spem_RoleDefinition115

    @spem_RoleDefinition115.setter
    def spem_RoleDefinition115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_RoleDefinition__spem_RoleDefinition115", None)
        self.__spem_RoleDefinition115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_Default_TaskDefinitionPerformer114"):
                opp_val = getattr(old_value, "spem_Default_TaskDefinitionPerformer114", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_Default_TaskDefinitionPerformer114"):
                opp_val = getattr(value, "spem_Default_TaskDefinitionPerformer114", None)
                if opp_val is None:
                    setattr(value, "spem_Default_TaskDefinitionPerformer114", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def spem_RoleDefinition104(self):
        return self.__spem_RoleDefinition104

    @spem_RoleDefinition104.setter
    def spem_RoleDefinition104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_RoleDefinition__spem_RoleDefinition104", None)
        self.__spem_RoleDefinition104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_Qualification105"):
                    opp_val = getattr(item, "spem_Qualification105", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_Qualification105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_Qualification105"):
                    opp_val = getattr(item, "spem_Qualification105", None)
                    
                    setattr(item, "spem_Qualification105", self)
                    

    @property
    def spem_RoleDefinition136(self):
        return self.__spem_RoleDefinition136

    @spem_RoleDefinition136.setter
    def spem_RoleDefinition136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_RoleDefinition__spem_RoleDefinition136", None)
        self.__spem_RoleDefinition136 = value
        
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
class DescribableElement:

    pass
class spem_ProcessElement(ProcessPackageableElement, DescribableElement):

    pass
class WorkDefinitionParameter:

    pass
class spem_Default_TaskDefinitionParameter(WorkDefinitionParameter):

    pass
class spem_LifeCycleSpecification(ABC):

    pass
class VariabilityElement:

    pass
class spem_MethodContentElement(VariabilityElement, DescribableElement, MethodContentPackageableElement):

    def __init__(self, copyright: str, author: str, changeDate: date, changeDescription: str, version: str, spem_MethodContentElement: "spem_MethodContentElement" = None, spem_MethodContentElement73: set["spem_MethodContentElement"] = None, spem_MethodContentElement76: "spem_MethodContentKind" = None):
        self.copyright = copyright
        self.author = author
        self.changeDate = changeDate
        self.changeDescription = changeDescription
        self.version = version
        self.spem_MethodContentElement = spem_MethodContentElement
        self.spem_MethodContentElement73 = spem_MethodContentElement73 if spem_MethodContentElement73 is not None else set()
        self.spem_MethodContentElement76 = spem_MethodContentElement76
        
    @property
    def copyright(self) -> str:
        return self.__copyright

    @copyright.setter
    def copyright(self, copyright: str):
        self.__copyright = copyright

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def changeDate(self) -> date:
        return self.__changeDate

    @changeDate.setter
    def changeDate(self, changeDate: date):
        self.__changeDate = changeDate

    @property
    def changeDescription(self) -> str:
        return self.__changeDescription

    @changeDescription.setter
    def changeDescription(self, changeDescription: str):
        self.__changeDescription = changeDescription

    @property
    def spem_MethodContentElement(self):
        return self.__spem_MethodContentElement

    @spem_MethodContentElement.setter
    def spem_MethodContentElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_MethodContentElement__spem_MethodContentElement", None)
        self.__spem_MethodContentElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_MethodContentElement73"):
                opp_val = getattr(old_value, "spem_MethodContentElement73", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_MethodContentElement73"):
                opp_val = getattr(value, "spem_MethodContentElement73", None)
                if opp_val is None:
                    setattr(value, "spem_MethodContentElement73", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def spem_MethodContentElement76(self):
        return self.__spem_MethodContentElement76

    @spem_MethodContentElement76.setter
    def spem_MethodContentElement76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_MethodContentElement__spem_MethodContentElement76", None)
        self.__spem_MethodContentElement76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_MethodContentKind"):
                opp_val = getattr(old_value, "spem_MethodContentKind", None)
                if opp_val == self:
                    setattr(old_value, "spem_MethodContentKind", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_MethodContentKind"):
                opp_val = getattr(value, "spem_MethodContentKind", None)
                setattr(value, "spem_MethodContentKind", self)

    @property
    def spem_MethodContentElement73(self):
        return self.__spem_MethodContentElement73

    @spem_MethodContentElement73.setter
    def spem_MethodContentElement73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_MethodContentElement__spem_MethodContentElement73", None)
        self.__spem_MethodContentElement73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_MethodContentElement"):
                    opp_val = getattr(item, "spem_MethodContentElement", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_MethodContentElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_MethodContentElement"):
                    opp_val = getattr(item, "spem_MethodContentElement", None)
                    
                    setattr(item, "spem_MethodContentElement", self)
                    

class spem_MethodContentPackageableElement(VariabilityElement):

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

class WorkBreakdownElement:

    pass
class spem_TaskUse(WorkBreakdownElement, MethodContentUse):

    def __init__(self, preCondition: str, postCondition: str, spem_TaskUse: "spem_ProcessPerformer" = None, spem_TaskUse127: "spem_TaskDefinition" = None, spem_TaskUse130: set["spem_ProcessParameter"] = None, spem_TaskUse133: set["spem_Step"] = None):
        self.preCondition = preCondition
        self.postCondition = postCondition
        self.spem_TaskUse = spem_TaskUse
        self.spem_TaskUse127 = spem_TaskUse127
        self.spem_TaskUse130 = spem_TaskUse130 if spem_TaskUse130 is not None else set()
        self.spem_TaskUse133 = spem_TaskUse133 if spem_TaskUse133 is not None else set()
        
    @property
    def postCondition(self) -> str:
        return self.__postCondition

    @postCondition.setter
    def postCondition(self, postCondition: str):
        self.__postCondition = postCondition

    @property
    def preCondition(self) -> str:
        return self.__preCondition

    @preCondition.setter
    def preCondition(self, preCondition: str):
        self.__preCondition = preCondition

    @property
    def spem_TaskUse130(self):
        return self.__spem_TaskUse130

    @spem_TaskUse130.setter
    def spem_TaskUse130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_TaskUse__spem_TaskUse130", None)
        self.__spem_TaskUse130 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_ProcessParameter131"):
                    opp_val = getattr(item, "spem_ProcessParameter131", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_ProcessParameter131", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_ProcessParameter131"):
                    opp_val = getattr(item, "spem_ProcessParameter131", None)
                    
                    setattr(item, "spem_ProcessParameter131", self)
                    

    @property
    def spem_TaskUse127(self):
        return self.__spem_TaskUse127

    @spem_TaskUse127.setter
    def spem_TaskUse127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_TaskUse__spem_TaskUse127", None)
        self.__spem_TaskUse127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_TaskDefinition128"):
                opp_val = getattr(old_value, "spem_TaskDefinition128", None)
                if opp_val == self:
                    setattr(old_value, "spem_TaskDefinition128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_TaskDefinition128"):
                opp_val = getattr(value, "spem_TaskDefinition128", None)
                setattr(value, "spem_TaskDefinition128", self)

    @property
    def spem_TaskUse133(self):
        return self.__spem_TaskUse133

    @spem_TaskUse133.setter
    def spem_TaskUse133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_TaskUse__spem_TaskUse133", None)
        self.__spem_TaskUse133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_Step134"):
                    opp_val = getattr(item, "spem_Step134", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_Step134", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_Step134"):
                    opp_val = getattr(item, "spem_Step134", None)
                    
                    setattr(item, "spem_Step134", self)
                    

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
            if hasattr(old_value, "spem_ProcessPerformer36"):
                opp_val = getattr(old_value, "spem_ProcessPerformer36", None)
                if opp_val == self:
                    setattr(old_value, "spem_ProcessPerformer36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_ProcessPerformer36"):
                opp_val = getattr(value, "spem_ProcessPerformer36", None)
                setattr(value, "spem_ProcessPerformer36", self)

class spem_Milestone(WorkBreakdownElement):

    pass
class WorkDefinition:

    pass
class spem_TaskDefinition(MethodContentElement, WorkDefinition):

    pass
class spem_Step(VariabilityElement, DescribableElement, WorkDefinition):

    def __init__(self, name: str, spem_Step92: "spem_Step" = None, spem_Step90: "spem_Step" = None, spem_Step: "spem_TaskDefinition" = None, spem_Step134: "spem_TaskUse" = None):
        self.name = name
        self.spem_Step92 = spem_Step92
        self.spem_Step90 = spem_Step90
        self.spem_Step = spem_Step
        self.spem_Step134 = spem_Step134
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def spem_Step134(self):
        return self.__spem_Step134

    @spem_Step134.setter
    def spem_Step134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Step__spem_Step134", None)
        self.__spem_Step134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_TaskUse133"):
                opp_val = getattr(old_value, "spem_TaskUse133", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_TaskUse133"):
                opp_val = getattr(value, "spem_TaskUse133", None)
                if opp_val is None:
                    setattr(value, "spem_TaskUse133", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def spem_Step92(self):
        return self.__spem_Step92

    @spem_Step92.setter
    def spem_Step92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Step__spem_Step92", None)
        self.__spem_Step92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_Step90"):
                opp_val = getattr(old_value, "spem_Step90", None)
                if opp_val == self:
                    setattr(old_value, "spem_Step90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_Step90"):
                opp_val = getattr(value, "spem_Step90", None)
                setattr(value, "spem_Step90", self)

    @property
    def spem_Step90(self):
        return self.__spem_Step90

    @spem_Step90.setter
    def spem_Step90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Step__spem_Step90", None)
        self.__spem_Step90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_Step92"):
                opp_val = getattr(old_value, "spem_Step92", None)
                if opp_val == self:
                    setattr(old_value, "spem_Step92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_Step92"):
                opp_val = getattr(value, "spem_Step92", None)
                setattr(value, "spem_Step92", self)

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
            if hasattr(old_value, "spem_TaskDefinition84"):
                opp_val = getattr(old_value, "spem_TaskDefinition84", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_TaskDefinition84"):
                opp_val = getattr(value, "spem_TaskDefinition84", None)
                if opp_val is None:
                    setattr(value, "spem_TaskDefinition84", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class spem_Activity(WorkBreakdownElement, VariabilityElement, WorkDefinition):

    def __init__(self, useKind: str, howToStaff: str, isEnactable: bool, spem_Activity: "spem_Activity" = None, spem_Activity13: "spem_Activity" = None, spem_Activity16: set["spem_BreakdownElement"] = None, spem_Activity19: set["spem_BreakdownElement"] = None, spem_Activity22: set["spem_ProcessParameter"] = None, spem_Activity24: "spem_MethodConfiguration" = None, spem_Activity26: set["spem_MethodConfiguration"] = None, spem_Activity30: "spem_Activity" = None, spem_Activity28: set["spem_Activity"] = None, spem_Activity34: "spem_ProcessPerformer" = None, spem_Activity147: "spem_ProcessComponent" = None):
        self.useKind = useKind
        self.howToStaff = howToStaff
        self.isEnactable = isEnactable
        self.spem_Activity = spem_Activity
        self.spem_Activity13 = spem_Activity13
        self.spem_Activity16 = spem_Activity16 if spem_Activity16 is not None else set()
        self.spem_Activity19 = spem_Activity19 if spem_Activity19 is not None else set()
        self.spem_Activity22 = spem_Activity22 if spem_Activity22 is not None else set()
        self.spem_Activity24 = spem_Activity24
        self.spem_Activity26 = spem_Activity26 if spem_Activity26 is not None else set()
        self.spem_Activity30 = spem_Activity30
        self.spem_Activity28 = spem_Activity28 if spem_Activity28 is not None else set()
        self.spem_Activity34 = spem_Activity34
        self.spem_Activity147 = spem_Activity147
        
    @property
    def useKind(self) -> str:
        return self.__useKind

    @useKind.setter
    def useKind(self, useKind: str):
        self.__useKind = useKind

    @property
    def howToStaff(self) -> str:
        return self.__howToStaff

    @howToStaff.setter
    def howToStaff(self, howToStaff: str):
        self.__howToStaff = howToStaff

    @property
    def isEnactable(self) -> bool:
        return self.__isEnactable

    @isEnactable.setter
    def isEnactable(self, isEnactable: bool):
        self.__isEnactable = isEnactable

    @property
    def spem_Activity147(self):
        return self.__spem_Activity147

    @spem_Activity147.setter
    def spem_Activity147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Activity__spem_Activity147", None)
        self.__spem_Activity147 = value
        
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
    def spem_Activity30(self):
        return self.__spem_Activity30

    @spem_Activity30.setter
    def spem_Activity30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Activity__spem_Activity30", None)
        self.__spem_Activity30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_Activity28"):
                opp_val = getattr(old_value, "spem_Activity28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_Activity28"):
                opp_val = getattr(value, "spem_Activity28", None)
                if opp_val is None:
                    setattr(value, "spem_Activity28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def spem_Activity16(self):
        return self.__spem_Activity16

    @spem_Activity16.setter
    def spem_Activity16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Activity__spem_Activity16", None)
        self.__spem_Activity16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_BreakdownElement17"):
                    opp_val = getattr(item, "spem_BreakdownElement17", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_BreakdownElement17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_BreakdownElement17"):
                    opp_val = getattr(item, "spem_BreakdownElement17", None)
                    
                    setattr(item, "spem_BreakdownElement17", self)
                    

    @property
    def spem_Activity13(self):
        return self.__spem_Activity13

    @spem_Activity13.setter
    def spem_Activity13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Activity__spem_Activity13", None)
        self.__spem_Activity13 = value
        
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

    @property
    def spem_Activity34(self):
        return self.__spem_Activity34

    @spem_Activity34.setter
    def spem_Activity34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Activity__spem_Activity34", None)
        self.__spem_Activity34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_ProcessPerformer33"):
                opp_val = getattr(old_value, "spem_ProcessPerformer33", None)
                if opp_val == self:
                    setattr(old_value, "spem_ProcessPerformer33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_ProcessPerformer33"):
                opp_val = getattr(value, "spem_ProcessPerformer33", None)
                setattr(value, "spem_ProcessPerformer33", self)

    @property
    def spem_Activity28(self):
        return self.__spem_Activity28

    @spem_Activity28.setter
    def spem_Activity28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Activity__spem_Activity28", None)
        self.__spem_Activity28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_Activity30"):
                    opp_val = getattr(item, "spem_Activity30", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_Activity30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_Activity30"):
                    opp_val = getattr(item, "spem_Activity30", None)
                    
                    setattr(item, "spem_Activity30", self)
                    

    @property
    def spem_Activity24(self):
        return self.__spem_Activity24

    @spem_Activity24.setter
    def spem_Activity24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Activity__spem_Activity24", None)
        self.__spem_Activity24 = value
        
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
    def spem_Activity26(self):
        return self.__spem_Activity26

    @spem_Activity26.setter
    def spem_Activity26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Activity__spem_Activity26", None)
        self.__spem_Activity26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_MethodConfiguration27"):
                    opp_val = getattr(item, "spem_MethodConfiguration27", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_MethodConfiguration27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_MethodConfiguration27"):
                    opp_val = getattr(item, "spem_MethodConfiguration27", None)
                    
                    setattr(item, "spem_MethodConfiguration27", self)
                    

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
            if hasattr(old_value, "spem_Activity13"):
                opp_val = getattr(old_value, "spem_Activity13", None)
                if opp_val == self:
                    setattr(old_value, "spem_Activity13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_Activity13"):
                opp_val = getattr(value, "spem_Activity13", None)
                setattr(value, "spem_Activity13", self)

    @property
    def spem_Activity22(self):
        return self.__spem_Activity22

    @spem_Activity22.setter
    def spem_Activity22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Activity__spem_Activity22", None)
        self.__spem_Activity22 = value if value is not None else set()
        
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
    def spem_Activity19(self):
        return self.__spem_Activity19

    @spem_Activity19.setter
    def spem_Activity19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Activity__spem_Activity19", None)
        self.__spem_Activity19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_BreakdownElement20"):
                    opp_val = getattr(item, "spem_BreakdownElement20", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_BreakdownElement20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_BreakdownElement20"):
                    opp_val = getattr(item, "spem_BreakdownElement20", None)
                    
                    setattr(item, "spem_BreakdownElement20", self)
                    

class spem_MethodConfiguration(MethodLibraryPackageableElement):

    pass
class spem_ProcessParameter(WorkDefinitionParameter):

    pass
class spem_WorkProductDefinition(MethodContentElement):

    def __init__(self, impactOfNotHaving: str, reasonForNotNeeding: str, spem_WorkProductDefinition: "spem_WorkDefinitionParameter" = None, spem_WorkProductDefinition45: "spem_WorkProductUse" = None, spem_WorkProductDefinition94: set["EstimatingConsideration"] = None, spem_WorkProductDefinition97: set["Report"] = None, spem_WorkProductDefinition99: set["Template"] = None, spem_WorkProductDefinition101: set["ToolMentor"] = None, spem_WorkProductDefinition78: "spem_ToolDefinition" = None, spem_WorkProductDefinition107: "spem_WorkProductDefinitionRelationship" = None, spem_WorkProductDefinition110: "spem_WorkProductDefinitionRelationship" = None, spem_WorkProductDefinition120: "spem_Default_ResponsibilityAssignment" = None, spem_WorkProductDefinition204: "spem_WorkProductPort" = None):
        self.impactOfNotHaving = impactOfNotHaving
        self.reasonForNotNeeding = reasonForNotNeeding
        self.spem_WorkProductDefinition = spem_WorkProductDefinition
        self.spem_WorkProductDefinition45 = spem_WorkProductDefinition45
        self.spem_WorkProductDefinition94 = spem_WorkProductDefinition94 if spem_WorkProductDefinition94 is not None else set()
        self.spem_WorkProductDefinition97 = spem_WorkProductDefinition97 if spem_WorkProductDefinition97 is not None else set()
        self.spem_WorkProductDefinition99 = spem_WorkProductDefinition99 if spem_WorkProductDefinition99 is not None else set()
        self.spem_WorkProductDefinition101 = spem_WorkProductDefinition101 if spem_WorkProductDefinition101 is not None else set()
        self.spem_WorkProductDefinition78 = spem_WorkProductDefinition78
        self.spem_WorkProductDefinition107 = spem_WorkProductDefinition107
        self.spem_WorkProductDefinition110 = spem_WorkProductDefinition110
        self.spem_WorkProductDefinition120 = spem_WorkProductDefinition120
        self.spem_WorkProductDefinition204 = spem_WorkProductDefinition204
        
    @property
    def reasonForNotNeeding(self) -> str:
        return self.__reasonForNotNeeding

    @reasonForNotNeeding.setter
    def reasonForNotNeeding(self, reasonForNotNeeding: str):
        self.__reasonForNotNeeding = reasonForNotNeeding

    @property
    def impactOfNotHaving(self) -> str:
        return self.__impactOfNotHaving

    @impactOfNotHaving.setter
    def impactOfNotHaving(self, impactOfNotHaving: str):
        self.__impactOfNotHaving = impactOfNotHaving

    @property
    def spem_WorkProductDefinition101(self):
        return self.__spem_WorkProductDefinition101

    @spem_WorkProductDefinition101.setter
    def spem_WorkProductDefinition101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkProductDefinition__spem_WorkProductDefinition101", None)
        self.__spem_WorkProductDefinition101 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ToolMentor102"):
                    opp_val = getattr(item, "ToolMentor102", None)
                    
                    if opp_val == self:
                        setattr(item, "ToolMentor102", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ToolMentor102"):
                    opp_val = getattr(item, "ToolMentor102", None)
                    
                    setattr(item, "ToolMentor102", self)
                    

    @property
    def spem_WorkProductDefinition110(self):
        return self.__spem_WorkProductDefinition110

    @spem_WorkProductDefinition110.setter
    def spem_WorkProductDefinition110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkProductDefinition__spem_WorkProductDefinition110", None)
        self.__spem_WorkProductDefinition110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_WorkProductDefinitionRelationship109"):
                opp_val = getattr(old_value, "spem_WorkProductDefinitionRelationship109", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_WorkProductDefinitionRelationship109"):
                opp_val = getattr(value, "spem_WorkProductDefinitionRelationship109", None)
                if opp_val is None:
                    setattr(value, "spem_WorkProductDefinitionRelationship109", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def spem_WorkProductDefinition99(self):
        return self.__spem_WorkProductDefinition99

    @spem_WorkProductDefinition99.setter
    def spem_WorkProductDefinition99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkProductDefinition__spem_WorkProductDefinition99", None)
        self.__spem_WorkProductDefinition99 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Template"):
                    opp_val = getattr(item, "Template", None)
                    
                    if opp_val == self:
                        setattr(item, "Template", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Template"):
                    opp_val = getattr(item, "Template", None)
                    
                    setattr(item, "Template", self)
                    

    @property
    def spem_WorkProductDefinition45(self):
        return self.__spem_WorkProductDefinition45

    @spem_WorkProductDefinition45.setter
    def spem_WorkProductDefinition45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkProductDefinition__spem_WorkProductDefinition45", None)
        self.__spem_WorkProductDefinition45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_WorkProductUse44"):
                opp_val = getattr(old_value, "spem_WorkProductUse44", None)
                if opp_val == self:
                    setattr(old_value, "spem_WorkProductUse44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_WorkProductUse44"):
                opp_val = getattr(value, "spem_WorkProductUse44", None)
                setattr(value, "spem_WorkProductUse44", self)

    @property
    def spem_WorkProductDefinition94(self):
        return self.__spem_WorkProductDefinition94

    @spem_WorkProductDefinition94.setter
    def spem_WorkProductDefinition94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkProductDefinition__spem_WorkProductDefinition94", None)
        self.__spem_WorkProductDefinition94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EstimatingConsideration95"):
                    opp_val = getattr(item, "EstimatingConsideration95", None)
                    
                    if opp_val == self:
                        setattr(item, "EstimatingConsideration95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EstimatingConsideration95"):
                    opp_val = getattr(item, "EstimatingConsideration95", None)
                    
                    setattr(item, "EstimatingConsideration95", self)
                    

    @property
    def spem_WorkProductDefinition120(self):
        return self.__spem_WorkProductDefinition120

    @spem_WorkProductDefinition120.setter
    def spem_WorkProductDefinition120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkProductDefinition__spem_WorkProductDefinition120", None)
        self.__spem_WorkProductDefinition120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_Default_ResponsibilityAssignment119"):
                opp_val = getattr(old_value, "spem_Default_ResponsibilityAssignment119", None)
                if opp_val == self:
                    setattr(old_value, "spem_Default_ResponsibilityAssignment119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_Default_ResponsibilityAssignment119"):
                opp_val = getattr(value, "spem_Default_ResponsibilityAssignment119", None)
                setattr(value, "spem_Default_ResponsibilityAssignment119", self)

    @property
    def spem_WorkProductDefinition107(self):
        return self.__spem_WorkProductDefinition107

    @spem_WorkProductDefinition107.setter
    def spem_WorkProductDefinition107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkProductDefinition__spem_WorkProductDefinition107", None)
        self.__spem_WorkProductDefinition107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_WorkProductDefinitionRelationship"):
                opp_val = getattr(old_value, "spem_WorkProductDefinitionRelationship", None)
                if opp_val == self:
                    setattr(old_value, "spem_WorkProductDefinitionRelationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_WorkProductDefinitionRelationship"):
                opp_val = getattr(value, "spem_WorkProductDefinitionRelationship", None)
                setattr(value, "spem_WorkProductDefinitionRelationship", self)

    @property
    def spem_WorkProductDefinition(self):
        return self.__spem_WorkProductDefinition

    @spem_WorkProductDefinition.setter
    def spem_WorkProductDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkProductDefinition__spem_WorkProductDefinition", None)
        self.__spem_WorkProductDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_WorkDefinitionParameter3"):
                opp_val = getattr(old_value, "spem_WorkDefinitionParameter3", None)
                if opp_val == self:
                    setattr(old_value, "spem_WorkDefinitionParameter3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_WorkDefinitionParameter3"):
                opp_val = getattr(value, "spem_WorkDefinitionParameter3", None)
                setattr(value, "spem_WorkDefinitionParameter3", self)

    @property
    def spem_WorkProductDefinition204(self):
        return self.__spem_WorkProductDefinition204

    @spem_WorkProductDefinition204.setter
    def spem_WorkProductDefinition204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkProductDefinition__spem_WorkProductDefinition204", None)
        self.__spem_WorkProductDefinition204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_WorkProductPort203"):
                opp_val = getattr(old_value, "spem_WorkProductPort203", None)
                if opp_val == self:
                    setattr(old_value, "spem_WorkProductPort203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_WorkProductPort203"):
                opp_val = getattr(value, "spem_WorkProductPort203", None)
                setattr(value, "spem_WorkProductPort203", self)

    @property
    def spem_WorkProductDefinition78(self):
        return self.__spem_WorkProductDefinition78

    @spem_WorkProductDefinition78.setter
    def spem_WorkProductDefinition78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkProductDefinition__spem_WorkProductDefinition78", None)
        self.__spem_WorkProductDefinition78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_ToolDefinition"):
                opp_val = getattr(old_value, "spem_ToolDefinition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_ToolDefinition"):
                opp_val = getattr(value, "spem_ToolDefinition", None)
                if opp_val is None:
                    setattr(value, "spem_ToolDefinition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def spem_WorkProductDefinition97(self):
        return self.__spem_WorkProductDefinition97

    @spem_WorkProductDefinition97.setter
    def spem_WorkProductDefinition97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkProductDefinition__spem_WorkProductDefinition97", None)
        self.__spem_WorkProductDefinition97 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Report"):
                    opp_val = getattr(item, "Report", None)
                    
                    if opp_val == self:
                        setattr(item, "Report", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Report"):
                    opp_val = getattr(item, "Report", None)
                    
                    setattr(item, "Report", self)
                    

class spem_WorkDefinitionParameter:

    def __init__(self, name: str, direction: str, optionality: str, spem_WorkDefinitionParameter3: "spem_WorkProductDefinition" = None, spem_WorkDefinitionParameter: "spem_WorkDefinition" = None):
        self.name = name
        self.direction = direction
        self.optionality = optionality
        self.spem_WorkDefinitionParameter3 = spem_WorkDefinitionParameter3
        self.spem_WorkDefinitionParameter = spem_WorkDefinitionParameter
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def optionality(self) -> str:
        return self.__optionality

    @optionality.setter
    def optionality(self, optionality: str):
        self.__optionality = optionality

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def spem_WorkDefinitionParameter3(self):
        return self.__spem_WorkDefinitionParameter3

    @spem_WorkDefinitionParameter3.setter
    def spem_WorkDefinitionParameter3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkDefinitionParameter__spem_WorkDefinitionParameter3", None)
        self.__spem_WorkDefinitionParameter3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_WorkProductDefinition"):
                opp_val = getattr(old_value, "spem_WorkProductDefinition", None)
                if opp_val == self:
                    setattr(old_value, "spem_WorkProductDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_WorkProductDefinition"):
                opp_val = getattr(value, "spem_WorkProductDefinition", None)
                setattr(value, "spem_WorkProductDefinition", self)

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
            if hasattr(old_value, "spem_WorkDefinition"):
                opp_val = getattr(old_value, "spem_WorkDefinition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_WorkDefinition"):
                opp_val = getattr(value, "spem_WorkDefinition", None)
                if opp_val is None:
                    setattr(value, "spem_WorkDefinition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class spem_WorkDefinition(ABC):

    def __init__(self, preCondition: str, postCondition: str, spem_WorkDefinition: set["spem_WorkDefinitionParameter"] = None):
        self.preCondition = preCondition
        self.postCondition = postCondition
        self.spem_WorkDefinition = spem_WorkDefinition if spem_WorkDefinition is not None else set()
        
    @property
    def postCondition(self) -> str:
        return self.__postCondition

    @postCondition.setter
    def postCondition(self, postCondition: str):
        self.__postCondition = postCondition

    @property
    def preCondition(self) -> str:
        return self.__preCondition

    @preCondition.setter
    def preCondition(self, preCondition: str):
        self.__preCondition = preCondition

    @property
    def spem_WorkDefinition(self):
        return self.__spem_WorkDefinition

    @spem_WorkDefinition.setter
    def spem_WorkDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkDefinition__spem_WorkDefinition", None)
        self.__spem_WorkDefinition = value if value is not None else set()
        
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

    def __init__(self, presentationName: str, briefDescription: str, purpose: str, mainDescription: str, spem_DescribableElement: set["spem_Guidance"] = None, spem_DescribableElement59: set["spem_Metric"] = None, spem_DescribableElement62: "spem_DescribableElement" = None, spem_DescribableElement60: "spem_DescribableElement" = None, spem_DescribableElement65: "spem_DescribableElement" = None, spem_DescribableElement63: "spem_DescribableElement" = None, spem_DescribableElement67: set["EstimatingConsideration"] = None, spem_DescribableElement69: set["spem_Category"] = None):
        self.presentationName = presentationName
        self.briefDescription = briefDescription
        self.purpose = purpose
        self.mainDescription = mainDescription
        self.spem_DescribableElement = spem_DescribableElement if spem_DescribableElement is not None else set()
        self.spem_DescribableElement59 = spem_DescribableElement59 if spem_DescribableElement59 is not None else set()
        self.spem_DescribableElement62 = spem_DescribableElement62
        self.spem_DescribableElement60 = spem_DescribableElement60
        self.spem_DescribableElement65 = spem_DescribableElement65
        self.spem_DescribableElement63 = spem_DescribableElement63
        self.spem_DescribableElement67 = spem_DescribableElement67 if spem_DescribableElement67 is not None else set()
        self.spem_DescribableElement69 = spem_DescribableElement69 if spem_DescribableElement69 is not None else set()
        
    @property
    def briefDescription(self) -> str:
        return self.__briefDescription

    @briefDescription.setter
    def briefDescription(self, briefDescription: str):
        self.__briefDescription = briefDescription

    @property
    def presentationName(self) -> str:
        return self.__presentationName

    @presentationName.setter
    def presentationName(self, presentationName: str):
        self.__presentationName = presentationName

    @property
    def mainDescription(self) -> str:
        return self.__mainDescription

    @mainDescription.setter
    def mainDescription(self, mainDescription: str):
        self.__mainDescription = mainDescription

    @property
    def purpose(self) -> str:
        return self.__purpose

    @purpose.setter
    def purpose(self, purpose: str):
        self.__purpose = purpose

    @property
    def spem_DescribableElement65(self):
        return self.__spem_DescribableElement65

    @spem_DescribableElement65.setter
    def spem_DescribableElement65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_DescribableElement__spem_DescribableElement65", None)
        self.__spem_DescribableElement65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_DescribableElement63"):
                opp_val = getattr(old_value, "spem_DescribableElement63", None)
                if opp_val == self:
                    setattr(old_value, "spem_DescribableElement63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_DescribableElement63"):
                opp_val = getattr(value, "spem_DescribableElement63", None)
                setattr(value, "spem_DescribableElement63", self)

    @property
    def spem_DescribableElement69(self):
        return self.__spem_DescribableElement69

    @spem_DescribableElement69.setter
    def spem_DescribableElement69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_DescribableElement__spem_DescribableElement69", None)
        self.__spem_DescribableElement69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spem_Category"):
                    opp_val = getattr(item, "spem_Category", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_Category", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_Category"):
                    opp_val = getattr(item, "spem_Category", None)
                    
                    setattr(item, "spem_Category", self)
                    

    @property
    def spem_DescribableElement59(self):
        return self.__spem_DescribableElement59

    @spem_DescribableElement59.setter
    def spem_DescribableElement59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_DescribableElement__spem_DescribableElement59", None)
        self.__spem_DescribableElement59 = value if value is not None else set()
        
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
    def spem_DescribableElement60(self):
        return self.__spem_DescribableElement60

    @spem_DescribableElement60.setter
    def spem_DescribableElement60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_DescribableElement__spem_DescribableElement60", None)
        self.__spem_DescribableElement60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_DescribableElement62"):
                opp_val = getattr(old_value, "spem_DescribableElement62", None)
                if opp_val == self:
                    setattr(old_value, "spem_DescribableElement62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_DescribableElement62"):
                opp_val = getattr(value, "spem_DescribableElement62", None)
                setattr(value, "spem_DescribableElement62", self)

    @property
    def spem_DescribableElement63(self):
        return self.__spem_DescribableElement63

    @spem_DescribableElement63.setter
    def spem_DescribableElement63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_DescribableElement__spem_DescribableElement63", None)
        self.__spem_DescribableElement63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_DescribableElement65"):
                opp_val = getattr(old_value, "spem_DescribableElement65", None)
                if opp_val == self:
                    setattr(old_value, "spem_DescribableElement65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_DescribableElement65"):
                opp_val = getattr(value, "spem_DescribableElement65", None)
                setattr(value, "spem_DescribableElement65", self)

    @property
    def spem_DescribableElement62(self):
        return self.__spem_DescribableElement62

    @spem_DescribableElement62.setter
    def spem_DescribableElement62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_DescribableElement__spem_DescribableElement62", None)
        self.__spem_DescribableElement62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_DescribableElement60"):
                opp_val = getattr(old_value, "spem_DescribableElement60", None)
                if opp_val == self:
                    setattr(old_value, "spem_DescribableElement60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_DescribableElement60"):
                opp_val = getattr(value, "spem_DescribableElement60", None)
                setattr(value, "spem_DescribableElement60", self)

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
                if hasattr(item, "spem_Guidance57"):
                    opp_val = getattr(item, "spem_Guidance57", None)
                    
                    if opp_val == self:
                        setattr(item, "spem_Guidance57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spem_Guidance57"):
                    opp_val = getattr(item, "spem_Guidance57", None)
                    
                    setattr(item, "spem_Guidance57", self)
                    

    @property
    def spem_DescribableElement67(self):
        return self.__spem_DescribableElement67

    @spem_DescribableElement67.setter
    def spem_DescribableElement67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_DescribableElement__spem_DescribableElement67", None)
        self.__spem_DescribableElement67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EstimatingConsideration"):
                    opp_val = getattr(item, "EstimatingConsideration", None)
                    
                    if opp_val == self:
                        setattr(item, "EstimatingConsideration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EstimatingConsideration"):
                    opp_val = getattr(item, "EstimatingConsideration", None)
                    
                    setattr(item, "EstimatingConsideration", self)
                    

class spem_Kind(ExtensibleElement):

    pass
class spem_ExtensibleElement(ABC):

    pass
class BreakdownElement:

    pass
class spem_WorkProductUseRelationship(BreakdownElement):

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

    def __init__(self, linkKind: str, WorkSequence: "spem_WorkBreakdownElement" = None, WorkSequence9: "spem_WorkBreakdownElement" = None, linkToSuccessor: "spem_WorkBreakdownElement" = None, linkToPredecessor: "spem_WorkBreakdownElement" = None):
        self.linkKind = linkKind
        self.WorkSequence = WorkSequence
        self.WorkSequence9 = WorkSequence9
        self.linkToSuccessor = linkToSuccessor
        self.linkToPredecessor = linkToPredecessor
        
    @property
    def linkKind(self) -> str:
        return self.__linkKind

    @linkKind.setter
    def linkKind(self, linkKind: str):
        self.__linkKind = linkKind

    @property
    def WorkSequence9(self):
        return self.__WorkSequence9

    @WorkSequence9.setter
    def WorkSequence9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkSequence__WorkSequence9", None)
        self.__WorkSequence9 = value
        
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
    def linkToPredecessor(self):
        return self.__linkToPredecessor

    @linkToPredecessor.setter
    def linkToPredecessor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkSequence__linkToPredecessor", None)
        self.__linkToPredecessor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorkBreakdownElement12"):
                opp_val = getattr(old_value, "WorkBreakdownElement12", None)
                if opp_val == self:
                    setattr(old_value, "WorkBreakdownElement12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkBreakdownElement12"):
                opp_val = getattr(value, "WorkBreakdownElement12", None)
                setattr(value, "WorkBreakdownElement12", self)

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

class spem_ProcessPerformer(WorkDefinitionPerformer, BreakdownElement):

    pass
class spem_ProcessResponsibilityAssignment(BreakdownElement):

    pass
class spem_WorkBreakdownElement(BreakdownElement):

    def __init__(self, isRepeatable: bool, isOngoing: bool, isEventDriven: bool, successor: set["spem_WorkSequence"] = None, predecessor: set["spem_WorkSequence"] = None, WorkBreakdownElement: "spem_WorkSequence" = None, WorkBreakdownElement12: "spem_WorkSequence" = None):
        self.isRepeatable = isRepeatable
        self.isOngoing = isOngoing
        self.isEventDriven = isEventDriven
        self.successor = successor if successor is not None else set()
        self.predecessor = predecessor if predecessor is not None else set()
        self.WorkBreakdownElement = WorkBreakdownElement
        self.WorkBreakdownElement12 = WorkBreakdownElement12
        
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
                if hasattr(item, "WorkSequence9"):
                    opp_val = getattr(item, "WorkSequence9", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkSequence9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkSequence9"):
                    opp_val = getattr(item, "WorkSequence9", None)
                    
                    setattr(item, "WorkSequence9", self)
                    

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
    def WorkBreakdownElement12(self):
        return self.__WorkBreakdownElement12

    @WorkBreakdownElement12.setter
    def WorkBreakdownElement12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkBreakdownElement__WorkBreakdownElement12", None)
        self.__WorkBreakdownElement12 = value
        
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
                    

class spem_Guidance(MethodContentElement):

    def __init__(self, attachment: str, spem_Guidance: "spem_BreakdownElement" = None, spem_Guidance57: "spem_DescribableElement" = None):
        self.attachment = attachment
        self.spem_Guidance = spem_Guidance
        self.spem_Guidance57 = spem_Guidance57
        
    @property
    def attachment(self) -> str:
        return self.__attachment

    @attachment.setter
    def attachment(self, attachment: str):
        self.__attachment = attachment

    @property
    def spem_Guidance(self):
        return self.__spem_Guidance

    @spem_Guidance.setter
    def spem_Guidance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Guidance__spem_Guidance", None)
        self.__spem_Guidance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_BreakdownElement6"):
                opp_val = getattr(old_value, "spem_BreakdownElement6", None)
                if opp_val == self:
                    setattr(old_value, "spem_BreakdownElement6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_BreakdownElement6"):
                opp_val = getattr(value, "spem_BreakdownElement6", None)
                setattr(value, "spem_BreakdownElement6", self)

    @property
    def spem_Guidance57(self):
        return self.__spem_Guidance57

    @spem_Guidance57.setter
    def spem_Guidance57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Guidance__spem_Guidance57", None)
        self.__spem_Guidance57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_DescribableElement"):
                opp_val = getattr(old_value, "spem_DescribableElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_DescribableElement"):
                opp_val = getattr(value, "spem_DescribableElement", None)
                if opp_val is None:
                    setattr(value, "spem_DescribableElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ProcessElement:

    pass
class spem_WorkProductPortConnector(ProcessElement):

    pass
class spem_ProcessKind(ProcessElement, Kind):

    pass
class spem_PlanningData(ProcessElement):

    def __init__(self, startDate: date, finishDate: date, rank: int, duration: str, spem_PlanningData: "spem_BreakdownElement" = None):
        self.startDate = startDate
        self.finishDate = finishDate
        self.rank = rank
        self.duration = duration
        self.spem_PlanningData = spem_PlanningData
        
    @property
    def finishDate(self) -> date:
        return self.__finishDate

    @finishDate.setter
    def finishDate(self, finishDate: date):
        self.__finishDate = finishDate

    @property
    def duration(self) -> str:
        return self.__duration

    @duration.setter
    def duration(self, duration: str):
        self.__duration = duration

    @property
    def rank(self) -> int:
        return self.__rank

    @rank.setter
    def rank(self, rank: int):
        self.__rank = rank

    @property
    def startDate(self) -> date:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate

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

class spem_WorkProductPort(ProcessElement):

    def __init__(self, isOptional: bool, portKind: str, spem_WorkProductPort: "spem_ProcessComponent" = None, spem_WorkProductPort154: "spem_ProcessComponentUse" = None, spem_WorkProductPort203: "spem_WorkProductDefinition" = None, spem_WorkProductPort206: "spem_WorkProductPortConnector" = None):
        self.isOptional = isOptional
        self.portKind = portKind
        self.spem_WorkProductPort = spem_WorkProductPort
        self.spem_WorkProductPort154 = spem_WorkProductPort154
        self.spem_WorkProductPort203 = spem_WorkProductPort203
        self.spem_WorkProductPort206 = spem_WorkProductPort206
        
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
    def spem_WorkProductPort154(self):
        return self.__spem_WorkProductPort154

    @spem_WorkProductPort154.setter
    def spem_WorkProductPort154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkProductPort__spem_WorkProductPort154", None)
        self.__spem_WorkProductPort154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_ProcessComponentUse153"):
                opp_val = getattr(old_value, "spem_ProcessComponentUse153", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_ProcessComponentUse153"):
                opp_val = getattr(value, "spem_ProcessComponentUse153", None)
                if opp_val is None:
                    setattr(value, "spem_ProcessComponentUse153", set([self]))
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
            if hasattr(old_value, "spem_ProcessComponent149"):
                opp_val = getattr(old_value, "spem_ProcessComponent149", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_ProcessComponent149"):
                opp_val = getattr(value, "spem_ProcessComponent149", None)
                if opp_val is None:
                    setattr(value, "spem_ProcessComponent149", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def spem_WorkProductPort203(self):
        return self.__spem_WorkProductPort203

    @spem_WorkProductPort203.setter
    def spem_WorkProductPort203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkProductPort__spem_WorkProductPort203", None)
        self.__spem_WorkProductPort203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_WorkProductDefinition204"):
                opp_val = getattr(old_value, "spem_WorkProductDefinition204", None)
                if opp_val == self:
                    setattr(old_value, "spem_WorkProductDefinition204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_WorkProductDefinition204"):
                opp_val = getattr(value, "spem_WorkProductDefinition204", None)
                setattr(value, "spem_WorkProductDefinition204", self)

    @property
    def spem_WorkProductPort206(self):
        return self.__spem_WorkProductPort206

    @spem_WorkProductPort206.setter
    def spem_WorkProductPort206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkProductPort__spem_WorkProductPort206", None)
        self.__spem_WorkProductPort206 = value
        
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

class spem_BreakdownElement(ProcessElement):

    def __init__(self, hasMultipleOccurrences: bool, isOptional: bool, isPlanned: bool, spem_BreakdownElement: "spem_PlanningData" = None, spem_BreakdownElement6: "spem_Guidance" = None, spem_BreakdownElement17: "spem_Activity" = None, spem_BreakdownElement20: "spem_Activity" = None):
        self.hasMultipleOccurrences = hasMultipleOccurrences
        self.isOptional = isOptional
        self.isPlanned = isPlanned
        self.spem_BreakdownElement = spem_BreakdownElement
        self.spem_BreakdownElement6 = spem_BreakdownElement6
        self.spem_BreakdownElement17 = spem_BreakdownElement17
        self.spem_BreakdownElement20 = spem_BreakdownElement20
        
    @property
    def isPlanned(self) -> bool:
        return self.__isPlanned

    @isPlanned.setter
    def isPlanned(self, isPlanned: bool):
        self.__isPlanned = isPlanned

    @property
    def hasMultipleOccurrences(self) -> bool:
        return self.__hasMultipleOccurrences

    @hasMultipleOccurrences.setter
    def hasMultipleOccurrences(self, hasMultipleOccurrences: bool):
        self.__hasMultipleOccurrences = hasMultipleOccurrences

    @property
    def isOptional(self) -> bool:
        return self.__isOptional

    @isOptional.setter
    def isOptional(self, isOptional: bool):
        self.__isOptional = isOptional

    @property
    def spem_BreakdownElement20(self):
        return self.__spem_BreakdownElement20

    @spem_BreakdownElement20.setter
    def spem_BreakdownElement20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_BreakdownElement__spem_BreakdownElement20", None)
        self.__spem_BreakdownElement20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_Activity19"):
                opp_val = getattr(old_value, "spem_Activity19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_Activity19"):
                opp_val = getattr(value, "spem_Activity19", None)
                if opp_val is None:
                    setattr(value, "spem_Activity19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def spem_BreakdownElement6(self):
        return self.__spem_BreakdownElement6

    @spem_BreakdownElement6.setter
    def spem_BreakdownElement6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_BreakdownElement__spem_BreakdownElement6", None)
        self.__spem_BreakdownElement6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_Guidance"):
                opp_val = getattr(old_value, "spem_Guidance", None)
                if opp_val == self:
                    setattr(old_value, "spem_Guidance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_Guidance"):
                opp_val = getattr(value, "spem_Guidance", None)
                setattr(value, "spem_Guidance", self)

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
    def spem_BreakdownElement17(self):
        return self.__spem_BreakdownElement17

    @spem_BreakdownElement17.setter
    def spem_BreakdownElement17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_BreakdownElement__spem_BreakdownElement17", None)
        self.__spem_BreakdownElement17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spem_Activity16"):
                opp_val = getattr(old_value, "spem_Activity16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spem_Activity16"):
                opp_val = getattr(value, "spem_Activity16", None)
                if opp_val is None:
                    setattr(value, "spem_Activity16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
