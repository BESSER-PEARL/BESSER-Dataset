from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RoleType(Enum):
    Composite = "Composite"
    Decision = "Decision"
    Transformation = "Transformation"
    Controle = "Controle"
class ProductState(Enum):
    None = "None"
    Ready_for_customer = "Ready_for_customer"
    Intermediary = "Intermediary"
class CapabilityType(Enum):
    Functional = "Functional"
    ObjectRelated = "ObjectRelated"
    Performance = "Performance"
    Operational = "Operational"
class StakeholderType(Enum):
    EEnumLiteral0 = "EEnumLiteral0"
class RequirementNature(Enum):
    None = "None"
    Functional = "Functional"
    Non_functional = "Non_functional"
    Constraint = "Constraint"
    Verification_and_Validation = "Verification_and_Validation"
class ObjectiveNature(Enum):
    None = "None"
    Performance = "Performance"
    Quality = "Quality"
    Delay = "Delay"
    Cost = "Cost"
    Environmental = "Environmental"
    Legacy = "Legacy"
    Human = "Human"
    Economical = "Economical"
    Other = "Other"
class Origin(Enum):
    None = "None"
    Internal_provider = "Internal_provider"
    External_provider = "External_provider"
class EnterpriseObjectiveType(Enum):
    None = "None"
    Strategic = "Strategic"
    Tactic = "Tactic"
    Operational = "Operational"
class ServiceState(Enum):
    For_external_customer = "For_external_customer"
    For_internal_usage = "For_internal_usage"
class ProductNature(Enum):
    None = "None"
    Physical = "Physical"
    Information = "Information"
class RequirementOrigin(Enum):
    None = "None"
    Stackeholder_requirement = "Stackeholder_requirement"
    System_requirement = "System_requirement"
    Expectation = "Expectation"


############################################
# Definition of Classes
############################################

class sipme_SIPME_object(ABC):

    def __init__(self, name: str, description: str, UUID: str):
        self.name = name
        self.description = description
        self.UUID = UUID
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UUID(self) -> str:
        return self.__UUID

    @UUID.setter
    def UUID(self, UUID: str):
        self.__UUID = UUID

class ObjectView:

    pass
class Stakeholder:

    pass
class EnterpriseObject:

    pass
class sipme_EnterpriseProduct(EnterpriseObject):

    def __init__(self, productState: str, productNarure: str, sipme_EnterpriseProduct: "sipme_Enterprise" = None):
        self.productState = productState
        self.productNarure = productNarure
        self.sipme_EnterpriseProduct = sipme_EnterpriseProduct
        
    @property
    def productNarure(self) -> str:
        return self.__productNarure

    @productNarure.setter
    def productNarure(self, productNarure: str):
        self.__productNarure = productNarure

    @property
    def productState(self) -> str:
        return self.__productState

    @productState.setter
    def productState(self, productState: str):
        self.__productState = productState

    @property
    def sipme_EnterpriseProduct(self):
        return self.__sipme_EnterpriseProduct

    @sipme_EnterpriseProduct.setter
    def sipme_EnterpriseProduct(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseProduct__sipme_EnterpriseProduct", None)
        self.__sipme_EnterpriseProduct = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_Enterprise32"):
                opp_val = getattr(old_value, "sipme_Enterprise32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_Enterprise32"):
                opp_val = getattr(value, "sipme_Enterprise32", None)
                if opp_val is None:
                    setattr(value, "sipme_Enterprise32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sipme_Objective(EnterpriseObject):

    def __init__(self, objectiveType: str, objectiveNature: str, sipme_Objective: "sipme_Enterprise" = None, Objective: "sipme_Objective" = None, refines: set["sipme_Objective"] = None, Objective100: "sipme_Requirement" = None, Objective79: "sipme_Objective" = None, subObjectives: "sipme_Objective" = None, associatedObjective: set["sipme_Requirement"] = None):
        self.objectiveType = objectiveType
        self.objectiveNature = objectiveNature
        self.sipme_Objective = sipme_Objective
        self.Objective = Objective
        self.refines = refines if refines is not None else set()
        self.Objective100 = Objective100
        self.Objective79 = Objective79
        self.subObjectives = subObjectives
        self.associatedObjective = associatedObjective if associatedObjective is not None else set()
        
    @property
    def objectiveType(self) -> str:
        return self.__objectiveType

    @objectiveType.setter
    def objectiveType(self, objectiveType: str):
        self.__objectiveType = objectiveType

    @property
    def objectiveNature(self) -> str:
        return self.__objectiveNature

    @objectiveNature.setter
    def objectiveNature(self, objectiveNature: str):
        self.__objectiveNature = objectiveNature

    @property
    def Objective(self):
        return self.__Objective

    @Objective.setter
    def Objective(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Objective__Objective", None)
        self.__Objective = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "refines"):
                opp_val = getattr(old_value, "refines", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "refines"):
                opp_val = getattr(value, "refines", None)
                if opp_val is None:
                    setattr(value, "refines", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def subObjectives(self):
        return self.__subObjectives

    @subObjectives.setter
    def subObjectives(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Objective__subObjectives", None)
        self.__subObjectives = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Objective79"):
                opp_val = getattr(old_value, "Objective79", None)
                if opp_val == self:
                    setattr(old_value, "Objective79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Objective79"):
                opp_val = getattr(value, "Objective79", None)
                setattr(value, "Objective79", self)

    @property
    def Objective100(self):
        return self.__Objective100

    @Objective100.setter
    def Objective100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Objective__Objective100", None)
        self.__Objective100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "takenIntoAccountBy"):
                opp_val = getattr(old_value, "takenIntoAccountBy", None)
                if opp_val == self:
                    setattr(old_value, "takenIntoAccountBy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "takenIntoAccountBy"):
                opp_val = getattr(value, "takenIntoAccountBy", None)
                setattr(value, "takenIntoAccountBy", self)

    @property
    def sipme_Objective(self):
        return self.__sipme_Objective

    @sipme_Objective.setter
    def sipme_Objective(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Objective__sipme_Objective", None)
        self.__sipme_Objective = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_Enterprise"):
                opp_val = getattr(old_value, "sipme_Enterprise", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_Enterprise"):
                opp_val = getattr(value, "sipme_Enterprise", None)
                if opp_val is None:
                    setattr(value, "sipme_Enterprise", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Objective79(self):
        return self.__Objective79

    @Objective79.setter
    def Objective79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Objective__Objective79", None)
        self.__Objective79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subObjectives"):
                opp_val = getattr(old_value, "subObjectives", None)
                if opp_val == self:
                    setattr(old_value, "subObjectives", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subObjectives"):
                opp_val = getattr(value, "subObjectives", None)
                setattr(value, "subObjectives", self)

    @property
    def refines(self):
        return self.__refines

    @refines.setter
    def refines(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Objective__refines", None)
        self.__refines = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Objective"):
                    opp_val = getattr(item, "Objective", None)
                    
                    if opp_val == self:
                        setattr(item, "Objective", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Objective"):
                    opp_val = getattr(item, "Objective", None)
                    
                    setattr(item, "Objective", self)
                    

    @property
    def associatedObjective(self):
        return self.__associatedObjective

    @associatedObjective.setter
    def associatedObjective(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Objective__associatedObjective", None)
        self.__associatedObjective = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Requirement"):
                    opp_val = getattr(item, "Requirement", None)
                    
                    if opp_val == self:
                        setattr(item, "Requirement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Requirement"):
                    opp_val = getattr(item, "Requirement", None)
                    
                    setattr(item, "Requirement", self)
                    

class sipme_EnterpriseProcessor(EnterpriseObject):

    def __init__(self, processorOrigin: str, generatedBy: set["sipme_Event"] = None, sipme_EnterpriseProcessor: set["sipme_ObjectView"] = None, sipme_EnterpriseProcessor46: set["sipme_ObjectView"] = None, initiates: set["sipme_Event"] = None, EnterpriseProcessor: "sipme_Event" = None, EnterpriseProcessor70: "sipme_Event" = None, sipme_EnterpriseProcessor51: set["sipme_ObjectView"] = None, implementedBy: set["sipme_Role_Function"] = None, sipme_EnterpriseProcessor55: set["sipme_Capacity"] = None, sipme_EnterpriseProcessor58: set["sipme_Capability"] = None, sipme_EnterpriseProcessor110: "sipme_Requirement" = None, EnterpriseProcessor119: "sipme_Role_Function" = None):
        self.processorOrigin = processorOrigin
        self.generatedBy = generatedBy if generatedBy is not None else set()
        self.sipme_EnterpriseProcessor = sipme_EnterpriseProcessor if sipme_EnterpriseProcessor is not None else set()
        self.sipme_EnterpriseProcessor46 = sipme_EnterpriseProcessor46 if sipme_EnterpriseProcessor46 is not None else set()
        self.initiates = initiates if initiates is not None else set()
        self.EnterpriseProcessor = EnterpriseProcessor
        self.EnterpriseProcessor70 = EnterpriseProcessor70
        self.sipme_EnterpriseProcessor51 = sipme_EnterpriseProcessor51 if sipme_EnterpriseProcessor51 is not None else set()
        self.implementedBy = implementedBy if implementedBy is not None else set()
        self.sipme_EnterpriseProcessor55 = sipme_EnterpriseProcessor55 if sipme_EnterpriseProcessor55 is not None else set()
        self.sipme_EnterpriseProcessor58 = sipme_EnterpriseProcessor58 if sipme_EnterpriseProcessor58 is not None else set()
        self.sipme_EnterpriseProcessor110 = sipme_EnterpriseProcessor110
        self.EnterpriseProcessor119 = EnterpriseProcessor119
        
    @property
    def processorOrigin(self) -> str:
        return self.__processorOrigin

    @processorOrigin.setter
    def processorOrigin(self, processorOrigin: str):
        self.__processorOrigin = processorOrigin

    @property
    def sipme_EnterpriseProcessor110(self):
        return self.__sipme_EnterpriseProcessor110

    @sipme_EnterpriseProcessor110.setter
    def sipme_EnterpriseProcessor110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseProcessor__sipme_EnterpriseProcessor110", None)
        self.__sipme_EnterpriseProcessor110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_Requirement109"):
                opp_val = getattr(old_value, "sipme_Requirement109", None)
                if opp_val == self:
                    setattr(old_value, "sipme_Requirement109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_Requirement109"):
                opp_val = getattr(value, "sipme_Requirement109", None)
                setattr(value, "sipme_Requirement109", self)

    @property
    def implementedBy(self):
        return self.__implementedBy

    @implementedBy.setter
    def implementedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseProcessor__implementedBy", None)
        self.__implementedBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Role_Function"):
                    opp_val = getattr(item, "Role_Function", None)
                    
                    if opp_val == self:
                        setattr(item, "Role_Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Role_Function"):
                    opp_val = getattr(item, "Role_Function", None)
                    
                    setattr(item, "Role_Function", self)
                    

    @property
    def sipme_EnterpriseProcessor58(self):
        return self.__sipme_EnterpriseProcessor58

    @sipme_EnterpriseProcessor58.setter
    def sipme_EnterpriseProcessor58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseProcessor__sipme_EnterpriseProcessor58", None)
        self.__sipme_EnterpriseProcessor58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_Capability59"):
                    opp_val = getattr(item, "sipme_Capability59", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_Capability59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_Capability59"):
                    opp_val = getattr(item, "sipme_Capability59", None)
                    
                    setattr(item, "sipme_Capability59", self)
                    

    @property
    def EnterpriseProcessor70(self):
        return self.__EnterpriseProcessor70

    @EnterpriseProcessor70.setter
    def EnterpriseProcessor70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseProcessor__EnterpriseProcessor70", None)
        self.__EnterpriseProcessor70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "initiatedBy"):
                opp_val = getattr(old_value, "initiatedBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "initiatedBy"):
                opp_val = getattr(value, "initiatedBy", None)
                if opp_val is None:
                    setattr(value, "initiatedBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sipme_EnterpriseProcessor55(self):
        return self.__sipme_EnterpriseProcessor55

    @sipme_EnterpriseProcessor55.setter
    def sipme_EnterpriseProcessor55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseProcessor__sipme_EnterpriseProcessor55", None)
        self.__sipme_EnterpriseProcessor55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_Capacity56"):
                    opp_val = getattr(item, "sipme_Capacity56", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_Capacity56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_Capacity56"):
                    opp_val = getattr(item, "sipme_Capacity56", None)
                    
                    setattr(item, "sipme_Capacity56", self)
                    

    @property
    def EnterpriseProcessor119(self):
        return self.__EnterpriseProcessor119

    @EnterpriseProcessor119.setter
    def EnterpriseProcessor119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseProcessor__EnterpriseProcessor119", None)
        self.__EnterpriseProcessor119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "implements"):
                opp_val = getattr(old_value, "implements", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "implements"):
                opp_val = getattr(value, "implements", None)
                if opp_val is None:
                    setattr(value, "implements", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sipme_EnterpriseProcessor(self):
        return self.__sipme_EnterpriseProcessor

    @sipme_EnterpriseProcessor.setter
    def sipme_EnterpriseProcessor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseProcessor__sipme_EnterpriseProcessor", None)
        self.__sipme_EnterpriseProcessor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_ObjectView"):
                    opp_val = getattr(item, "sipme_ObjectView", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_ObjectView", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_ObjectView"):
                    opp_val = getattr(item, "sipme_ObjectView", None)
                    
                    setattr(item, "sipme_ObjectView", self)
                    

    @property
    def sipme_EnterpriseProcessor51(self):
        return self.__sipme_EnterpriseProcessor51

    @sipme_EnterpriseProcessor51.setter
    def sipme_EnterpriseProcessor51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseProcessor__sipme_EnterpriseProcessor51", None)
        self.__sipme_EnterpriseProcessor51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_ObjectView52"):
                    opp_val = getattr(item, "sipme_ObjectView52", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_ObjectView52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_ObjectView52"):
                    opp_val = getattr(item, "sipme_ObjectView52", None)
                    
                    setattr(item, "sipme_ObjectView52", self)
                    

    @property
    def generatedBy(self):
        return self.__generatedBy

    @generatedBy.setter
    def generatedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseProcessor__generatedBy", None)
        self.__generatedBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Event"):
                    opp_val = getattr(item, "Event", None)
                    
                    if opp_val == self:
                        setattr(item, "Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Event"):
                    opp_val = getattr(item, "Event", None)
                    
                    setattr(item, "Event", self)
                    

    @property
    def sipme_EnterpriseProcessor46(self):
        return self.__sipme_EnterpriseProcessor46

    @sipme_EnterpriseProcessor46.setter
    def sipme_EnterpriseProcessor46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseProcessor__sipme_EnterpriseProcessor46", None)
        self.__sipme_EnterpriseProcessor46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_ObjectView47"):
                    opp_val = getattr(item, "sipme_ObjectView47", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_ObjectView47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_ObjectView47"):
                    opp_val = getattr(item, "sipme_ObjectView47", None)
                    
                    setattr(item, "sipme_ObjectView47", self)
                    

    @property
    def initiates(self):
        return self.__initiates

    @initiates.setter
    def initiates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseProcessor__initiates", None)
        self.__initiates = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Event49"):
                    opp_val = getattr(item, "Event49", None)
                    
                    if opp_val == self:
                        setattr(item, "Event49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Event49"):
                    opp_val = getattr(item, "Event49", None)
                    
                    setattr(item, "Event49", self)
                    

    @property
    def EnterpriseProcessor(self):
        return self.__EnterpriseProcessor

    @EnterpriseProcessor.setter
    def EnterpriseProcessor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseProcessor__EnterpriseProcessor", None)
        self.__EnterpriseProcessor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generates"):
                opp_val = getattr(old_value, "generates", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generates"):
                opp_val = getattr(value, "generates", None)
                if opp_val is None:
                    setattr(value, "generates", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sipme_EnterpriseResource(EnterpriseObject):

    def __init__(self, resourceOrigin: str, sipme_EnterpriseResource: "sipme_Task" = None, playedBy: set["sipme_Role_Function"] = None, canBePlayedBy: set["sipme_Role_Function"] = None, sipme_EnterpriseResource66: set["sipme_Capability"] = None, sipme_EnterpriseResource107: "sipme_Requirement" = None, EnterpriseResource: "sipme_Role_Function" = None, EnterpriseResource117: "sipme_Role_Function" = None):
        self.resourceOrigin = resourceOrigin
        self.sipme_EnterpriseResource = sipme_EnterpriseResource
        self.playedBy = playedBy if playedBy is not None else set()
        self.canBePlayedBy = canBePlayedBy if canBePlayedBy is not None else set()
        self.sipme_EnterpriseResource66 = sipme_EnterpriseResource66 if sipme_EnterpriseResource66 is not None else set()
        self.sipme_EnterpriseResource107 = sipme_EnterpriseResource107
        self.EnterpriseResource = EnterpriseResource
        self.EnterpriseResource117 = EnterpriseResource117
        
    @property
    def resourceOrigin(self) -> str:
        return self.__resourceOrigin

    @resourceOrigin.setter
    def resourceOrigin(self, resourceOrigin: str):
        self.__resourceOrigin = resourceOrigin

    @property
    def sipme_EnterpriseResource(self):
        return self.__sipme_EnterpriseResource

    @sipme_EnterpriseResource.setter
    def sipme_EnterpriseResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseResource__sipme_EnterpriseResource", None)
        self.__sipme_EnterpriseResource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_Task"):
                opp_val = getattr(old_value, "sipme_Task", None)
                if opp_val == self:
                    setattr(old_value, "sipme_Task", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_Task"):
                opp_val = getattr(value, "sipme_Task", None)
                setattr(value, "sipme_Task", self)

    @property
    def sipme_EnterpriseResource66(self):
        return self.__sipme_EnterpriseResource66

    @sipme_EnterpriseResource66.setter
    def sipme_EnterpriseResource66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseResource__sipme_EnterpriseResource66", None)
        self.__sipme_EnterpriseResource66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_Capability67"):
                    opp_val = getattr(item, "sipme_Capability67", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_Capability67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_Capability67"):
                    opp_val = getattr(item, "sipme_Capability67", None)
                    
                    setattr(item, "sipme_Capability67", self)
                    

    @property
    def EnterpriseResource(self):
        return self.__EnterpriseResource

    @EnterpriseResource.setter
    def EnterpriseResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseResource__EnterpriseResource", None)
        self.__EnterpriseResource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plays"):
                opp_val = getattr(old_value, "plays", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plays"):
                opp_val = getattr(value, "plays", None)
                if opp_val is None:
                    setattr(value, "plays", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def playedBy(self):
        return self.__playedBy

    @playedBy.setter
    def playedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseResource__playedBy", None)
        self.__playedBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Role_Function62"):
                    opp_val = getattr(item, "Role_Function62", None)
                    
                    if opp_val == self:
                        setattr(item, "Role_Function62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Role_Function62"):
                    opp_val = getattr(item, "Role_Function62", None)
                    
                    setattr(item, "Role_Function62", self)
                    

    @property
    def canBePlayedBy(self):
        return self.__canBePlayedBy

    @canBePlayedBy.setter
    def canBePlayedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseResource__canBePlayedBy", None)
        self.__canBePlayedBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Role_Function64"):
                    opp_val = getattr(item, "Role_Function64", None)
                    
                    if opp_val == self:
                        setattr(item, "Role_Function64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Role_Function64"):
                    opp_val = getattr(item, "Role_Function64", None)
                    
                    setattr(item, "Role_Function64", self)
                    

    @property
    def sipme_EnterpriseResource107(self):
        return self.__sipme_EnterpriseResource107

    @sipme_EnterpriseResource107.setter
    def sipme_EnterpriseResource107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseResource__sipme_EnterpriseResource107", None)
        self.__sipme_EnterpriseResource107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_Requirement106"):
                opp_val = getattr(old_value, "sipme_Requirement106", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_Requirement106"):
                opp_val = getattr(value, "sipme_Requirement106", None)
                if opp_val is None:
                    setattr(value, "sipme_Requirement106", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EnterpriseResource117(self):
        return self.__EnterpriseResource117

    @EnterpriseResource117.setter
    def EnterpriseResource117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseResource__EnterpriseResource117", None)
        self.__EnterpriseResource117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isAbleToPlay"):
                opp_val = getattr(old_value, "isAbleToPlay", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isAbleToPlay"):
                opp_val = getattr(value, "isAbleToPlay", None)
                if opp_val is None:
                    setattr(value, "isAbleToPlay", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sipme_EnterpriseService(EnterpriseObject):

    def __init__(self, serviceState: str, sipme_EnterpriseService: "sipme_Enterprise" = None):
        self.serviceState = serviceState
        self.sipme_EnterpriseService = sipme_EnterpriseService
        
    @property
    def serviceState(self) -> str:
        return self.__serviceState

    @serviceState.setter
    def serviceState(self, serviceState: str):
        self.__serviceState = serviceState

    @property
    def sipme_EnterpriseService(self):
        return self.__sipme_EnterpriseService

    @sipme_EnterpriseService.setter
    def sipme_EnterpriseService(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseService__sipme_EnterpriseService", None)
        self.__sipme_EnterpriseService = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_Enterprise30"):
                opp_val = getattr(old_value, "sipme_Enterprise30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_Enterprise30"):
                opp_val = getattr(value, "sipme_Enterprise30", None)
                if opp_val is None:
                    setattr(value, "sipme_Enterprise30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sipme_Capability(EnterpriseObject):

    def __init__(self, capabilityType: str, sipme_Capability: "sipme_Capacity" = None, sipme_Capability59: "sipme_EnterpriseProcessor" = None, sipme_Capability67: "sipme_EnterpriseResource" = None):
        self.capabilityType = capabilityType
        self.sipme_Capability = sipme_Capability
        self.sipme_Capability59 = sipme_Capability59
        self.sipme_Capability67 = sipme_Capability67
        
    @property
    def capabilityType(self) -> str:
        return self.__capabilityType

    @capabilityType.setter
    def capabilityType(self, capabilityType: str):
        self.__capabilityType = capabilityType

    @property
    def sipme_Capability67(self):
        return self.__sipme_Capability67

    @sipme_Capability67.setter
    def sipme_Capability67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Capability__sipme_Capability67", None)
        self.__sipme_Capability67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_EnterpriseResource66"):
                opp_val = getattr(old_value, "sipme_EnterpriseResource66", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_EnterpriseResource66"):
                opp_val = getattr(value, "sipme_EnterpriseResource66", None)
                if opp_val is None:
                    setattr(value, "sipme_EnterpriseResource66", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sipme_Capability59(self):
        return self.__sipme_Capability59

    @sipme_Capability59.setter
    def sipme_Capability59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Capability__sipme_Capability59", None)
        self.__sipme_Capability59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_EnterpriseProcessor58"):
                opp_val = getattr(old_value, "sipme_EnterpriseProcessor58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_EnterpriseProcessor58"):
                opp_val = getattr(value, "sipme_EnterpriseProcessor58", None)
                if opp_val is None:
                    setattr(value, "sipme_EnterpriseProcessor58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sipme_Capability(self):
        return self.__sipme_Capability

    @sipme_Capability.setter
    def sipme_Capability(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Capability__sipme_Capability", None)
        self.__sipme_Capability = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_Capacity"):
                opp_val = getattr(old_value, "sipme_Capacity", None)
                if opp_val == self:
                    setattr(old_value, "sipme_Capacity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_Capacity"):
                opp_val = getattr(value, "sipme_Capacity", None)
                setattr(value, "sipme_Capacity", self)

class sipme_Capacity(EnterpriseObject):

    def __init__(self, value: float, unit: str, sipme_Capacity: "sipme_Capability" = None, sipme_Capacity56: "sipme_EnterpriseProcessor" = None):
        self.value = value
        self.unit = unit
        self.sipme_Capacity = sipme_Capacity
        self.sipme_Capacity56 = sipme_Capacity56
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def sipme_Capacity56(self):
        return self.__sipme_Capacity56

    @sipme_Capacity56.setter
    def sipme_Capacity56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Capacity__sipme_Capacity56", None)
        self.__sipme_Capacity56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_EnterpriseProcessor55"):
                opp_val = getattr(old_value, "sipme_EnterpriseProcessor55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_EnterpriseProcessor55"):
                opp_val = getattr(value, "sipme_EnterpriseProcessor55", None)
                if opp_val is None:
                    setattr(value, "sipme_EnterpriseProcessor55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sipme_Capacity(self):
        return self.__sipme_Capacity

    @sipme_Capacity.setter
    def sipme_Capacity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Capacity__sipme_Capacity", None)
        self.__sipme_Capacity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_Capability"):
                opp_val = getattr(old_value, "sipme_Capability", None)
                if opp_val == self:
                    setattr(old_value, "sipme_Capability", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_Capability"):
                opp_val = getattr(value, "sipme_Capability", None)
                setattr(value, "sipme_Capability", self)

class sipme_BusinessRules(EnterpriseObject):

    pass
class OrganisationCell:

    pass
class SIPME_object:

    pass
class sipme_ObjectView(SIPME_object):

    def __init__(self, viewPoint: str, ObjectView: "sipme_EnterpriseObject" = None, sipme_ObjectView: "sipme_EnterpriseProcessor" = None, sipme_ObjectView47: "sipme_EnterpriseProcessor" = None, ObjectView74: "sipme_Event" = None, sipme_ObjectView52: "sipme_EnterpriseProcessor" = None, sipme_ObjectView93: "sipme_ObjectsFileView" = None, representedBy: "sipme_EnterpriseObject" = None, hasAssociatedEvents: set["sipme_Event"] = None):
        self.viewPoint = viewPoint
        self.ObjectView = ObjectView
        self.sipme_ObjectView = sipme_ObjectView
        self.sipme_ObjectView47 = sipme_ObjectView47
        self.ObjectView74 = ObjectView74
        self.sipme_ObjectView52 = sipme_ObjectView52
        self.sipme_ObjectView93 = sipme_ObjectView93
        self.representedBy = representedBy
        self.hasAssociatedEvents = hasAssociatedEvents if hasAssociatedEvents is not None else set()
        
    @property
    def viewPoint(self) -> str:
        return self.__viewPoint

    @viewPoint.setter
    def viewPoint(self, viewPoint: str):
        self.__viewPoint = viewPoint

    @property
    def ObjectView74(self):
        return self.__ObjectView74

    @ObjectView74.setter
    def ObjectView74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_ObjectView__ObjectView74", None)
        self.__ObjectView74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "events"):
                opp_val = getattr(old_value, "events", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "events"):
                opp_val = getattr(value, "events", None)
                if opp_val is None:
                    setattr(value, "events", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sipme_ObjectView47(self):
        return self.__sipme_ObjectView47

    @sipme_ObjectView47.setter
    def sipme_ObjectView47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_ObjectView__sipme_ObjectView47", None)
        self.__sipme_ObjectView47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_EnterpriseProcessor46"):
                opp_val = getattr(old_value, "sipme_EnterpriseProcessor46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_EnterpriseProcessor46"):
                opp_val = getattr(value, "sipme_EnterpriseProcessor46", None)
                if opp_val is None:
                    setattr(value, "sipme_EnterpriseProcessor46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def representedBy(self):
        return self.__representedBy

    @representedBy.setter
    def representedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_ObjectView__representedBy", None)
        self.__representedBy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EnterpriseObject82"):
                opp_val = getattr(old_value, "EnterpriseObject82", None)
                if opp_val == self:
                    setattr(old_value, "EnterpriseObject82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EnterpriseObject82"):
                opp_val = getattr(value, "EnterpriseObject82", None)
                setattr(value, "EnterpriseObject82", self)

    @property
    def sipme_ObjectView(self):
        return self.__sipme_ObjectView

    @sipme_ObjectView.setter
    def sipme_ObjectView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_ObjectView__sipme_ObjectView", None)
        self.__sipme_ObjectView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_EnterpriseProcessor"):
                opp_val = getattr(old_value, "sipme_EnterpriseProcessor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_EnterpriseProcessor"):
                opp_val = getattr(value, "sipme_EnterpriseProcessor", None)
                if opp_val is None:
                    setattr(value, "sipme_EnterpriseProcessor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sipme_ObjectView93(self):
        return self.__sipme_ObjectView93

    @sipme_ObjectView93.setter
    def sipme_ObjectView93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_ObjectView__sipme_ObjectView93", None)
        self.__sipme_ObjectView93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_ObjectsFileView"):
                opp_val = getattr(old_value, "sipme_ObjectsFileView", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_ObjectsFileView"):
                opp_val = getattr(value, "sipme_ObjectsFileView", None)
                if opp_val is None:
                    setattr(value, "sipme_ObjectsFileView", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hasAssociatedEvents(self):
        return self.__hasAssociatedEvents

    @hasAssociatedEvents.setter
    def hasAssociatedEvents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_ObjectView__hasAssociatedEvents", None)
        self.__hasAssociatedEvents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Event84"):
                    opp_val = getattr(item, "Event84", None)
                    
                    if opp_val == self:
                        setattr(item, "Event84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Event84"):
                    opp_val = getattr(item, "Event84", None)
                    
                    setattr(item, "Event84", self)
                    

    @property
    def sipme_ObjectView52(self):
        return self.__sipme_ObjectView52

    @sipme_ObjectView52.setter
    def sipme_ObjectView52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_ObjectView__sipme_ObjectView52", None)
        self.__sipme_ObjectView52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_EnterpriseProcessor51"):
                opp_val = getattr(old_value, "sipme_EnterpriseProcessor51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_EnterpriseProcessor51"):
                opp_val = getattr(value, "sipme_EnterpriseProcessor51", None)
                if opp_val is None:
                    setattr(value, "sipme_EnterpriseProcessor51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ObjectView(self):
        return self.__ObjectView

    @ObjectView.setter
    def ObjectView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_ObjectView__ObjectView", None)
        self.__ObjectView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "represents"):
                opp_val = getattr(old_value, "represents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "represents"):
                opp_val = getattr(value, "represents", None)
                if opp_val is None:
                    setattr(value, "represents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sipme_Stakeholder(SIPME_object):

    def __init__(self, stakeholderType: str, stakeholderOrganism: str, sipme_Stakeholder: "sipme_Requirement" = None, sipme_Stakeholder124: set["sipme_Requirement"] = None):
        self.stakeholderType = stakeholderType
        self.stakeholderOrganism = stakeholderOrganism
        self.sipme_Stakeholder = sipme_Stakeholder
        self.sipme_Stakeholder124 = sipme_Stakeholder124 if sipme_Stakeholder124 is not None else set()
        
    @property
    def stakeholderType(self) -> str:
        return self.__stakeholderType

    @stakeholderType.setter
    def stakeholderType(self, stakeholderType: str):
        self.__stakeholderType = stakeholderType

    @property
    def stakeholderOrganism(self) -> str:
        return self.__stakeholderOrganism

    @stakeholderOrganism.setter
    def stakeholderOrganism(self, stakeholderOrganism: str):
        self.__stakeholderOrganism = stakeholderOrganism

    @property
    def sipme_Stakeholder124(self):
        return self.__sipme_Stakeholder124

    @sipme_Stakeholder124.setter
    def sipme_Stakeholder124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Stakeholder__sipme_Stakeholder124", None)
        self.__sipme_Stakeholder124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_Requirement125"):
                    opp_val = getattr(item, "sipme_Requirement125", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_Requirement125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_Requirement125"):
                    opp_val = getattr(item, "sipme_Requirement125", None)
                    
                    setattr(item, "sipme_Requirement125", self)
                    

    @property
    def sipme_Stakeholder(self):
        return self.__sipme_Stakeholder

    @sipme_Stakeholder.setter
    def sipme_Stakeholder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Stakeholder__sipme_Stakeholder", None)
        self.__sipme_Stakeholder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_Requirement"):
                opp_val = getattr(old_value, "sipme_Requirement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_Requirement"):
                opp_val = getattr(value, "sipme_Requirement", None)
                if opp_val is None:
                    setattr(value, "sipme_Requirement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sipme_Requirement(SIPME_object):

    def __init__(self, requirementOrigin: str, requirementNature: str, requirementVersion: str, requirementDate: date, requirementStatement: str, requirementPriority: int, requirementMaturity: int, requirementStatus: str, takenIntoAccountBy: "sipme_Objective" = None, sipme_Requirement: set["sipme_Stakeholder"] = None, sipme_Requirement104: "sipme_Requirement" = None, sipme_Requirement102: set["sipme_Requirement"] = None, sipme_Requirement106: set["sipme_EnterpriseResource"] = None, Requirement: "sipme_Objective" = None, sipme_Requirement125: "sipme_Stakeholder" = None, sipme_Requirement109: "sipme_EnterpriseProcessor" = None, sipme_Requirement112: "sipme_Activity" = None):
        self.requirementOrigin = requirementOrigin
        self.requirementNature = requirementNature
        self.requirementVersion = requirementVersion
        self.requirementDate = requirementDate
        self.requirementStatement = requirementStatement
        self.requirementPriority = requirementPriority
        self.requirementMaturity = requirementMaturity
        self.requirementStatus = requirementStatus
        self.takenIntoAccountBy = takenIntoAccountBy
        self.sipme_Requirement = sipme_Requirement if sipme_Requirement is not None else set()
        self.sipme_Requirement104 = sipme_Requirement104
        self.sipme_Requirement102 = sipme_Requirement102 if sipme_Requirement102 is not None else set()
        self.sipme_Requirement106 = sipme_Requirement106 if sipme_Requirement106 is not None else set()
        self.Requirement = Requirement
        self.sipme_Requirement125 = sipme_Requirement125
        self.sipme_Requirement109 = sipme_Requirement109
        self.sipme_Requirement112 = sipme_Requirement112
        
    @property
    def requirementVersion(self) -> str:
        return self.__requirementVersion

    @requirementVersion.setter
    def requirementVersion(self, requirementVersion: str):
        self.__requirementVersion = requirementVersion

    @property
    def requirementOrigin(self) -> str:
        return self.__requirementOrigin

    @requirementOrigin.setter
    def requirementOrigin(self, requirementOrigin: str):
        self.__requirementOrigin = requirementOrigin

    @property
    def requirementMaturity(self) -> int:
        return self.__requirementMaturity

    @requirementMaturity.setter
    def requirementMaturity(self, requirementMaturity: int):
        self.__requirementMaturity = requirementMaturity

    @property
    def requirementStatus(self) -> str:
        return self.__requirementStatus

    @requirementStatus.setter
    def requirementStatus(self, requirementStatus: str):
        self.__requirementStatus = requirementStatus

    @property
    def requirementStatement(self) -> str:
        return self.__requirementStatement

    @requirementStatement.setter
    def requirementStatement(self, requirementStatement: str):
        self.__requirementStatement = requirementStatement

    @property
    def requirementPriority(self) -> int:
        return self.__requirementPriority

    @requirementPriority.setter
    def requirementPriority(self, requirementPriority: int):
        self.__requirementPriority = requirementPriority

    @property
    def requirementDate(self) -> date:
        return self.__requirementDate

    @requirementDate.setter
    def requirementDate(self, requirementDate: date):
        self.__requirementDate = requirementDate

    @property
    def requirementNature(self) -> str:
        return self.__requirementNature

    @requirementNature.setter
    def requirementNature(self, requirementNature: str):
        self.__requirementNature = requirementNature

    @property
    def Requirement(self):
        return self.__Requirement

    @Requirement.setter
    def Requirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Requirement__Requirement", None)
        self.__Requirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "associatedObjective"):
                opp_val = getattr(old_value, "associatedObjective", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "associatedObjective"):
                opp_val = getattr(value, "associatedObjective", None)
                if opp_val is None:
                    setattr(value, "associatedObjective", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sipme_Requirement102(self):
        return self.__sipme_Requirement102

    @sipme_Requirement102.setter
    def sipme_Requirement102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Requirement__sipme_Requirement102", None)
        self.__sipme_Requirement102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_Requirement104"):
                    opp_val = getattr(item, "sipme_Requirement104", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_Requirement104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_Requirement104"):
                    opp_val = getattr(item, "sipme_Requirement104", None)
                    
                    setattr(item, "sipme_Requirement104", self)
                    

    @property
    def sipme_Requirement125(self):
        return self.__sipme_Requirement125

    @sipme_Requirement125.setter
    def sipme_Requirement125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Requirement__sipme_Requirement125", None)
        self.__sipme_Requirement125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_Stakeholder124"):
                opp_val = getattr(old_value, "sipme_Stakeholder124", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_Stakeholder124"):
                opp_val = getattr(value, "sipme_Stakeholder124", None)
                if opp_val is None:
                    setattr(value, "sipme_Stakeholder124", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sipme_Requirement(self):
        return self.__sipme_Requirement

    @sipme_Requirement.setter
    def sipme_Requirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Requirement__sipme_Requirement", None)
        self.__sipme_Requirement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_Stakeholder"):
                    opp_val = getattr(item, "sipme_Stakeholder", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_Stakeholder", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_Stakeholder"):
                    opp_val = getattr(item, "sipme_Stakeholder", None)
                    
                    setattr(item, "sipme_Stakeholder", self)
                    

    @property
    def sipme_Requirement109(self):
        return self.__sipme_Requirement109

    @sipme_Requirement109.setter
    def sipme_Requirement109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Requirement__sipme_Requirement109", None)
        self.__sipme_Requirement109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_EnterpriseProcessor110"):
                opp_val = getattr(old_value, "sipme_EnterpriseProcessor110", None)
                if opp_val == self:
                    setattr(old_value, "sipme_EnterpriseProcessor110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_EnterpriseProcessor110"):
                opp_val = getattr(value, "sipme_EnterpriseProcessor110", None)
                setattr(value, "sipme_EnterpriseProcessor110", self)

    @property
    def takenIntoAccountBy(self):
        return self.__takenIntoAccountBy

    @takenIntoAccountBy.setter
    def takenIntoAccountBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Requirement__takenIntoAccountBy", None)
        self.__takenIntoAccountBy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Objective100"):
                opp_val = getattr(old_value, "Objective100", None)
                if opp_val == self:
                    setattr(old_value, "Objective100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Objective100"):
                opp_val = getattr(value, "Objective100", None)
                setattr(value, "Objective100", self)

    @property
    def sipme_Requirement112(self):
        return self.__sipme_Requirement112

    @sipme_Requirement112.setter
    def sipme_Requirement112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Requirement__sipme_Requirement112", None)
        self.__sipme_Requirement112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_Activity"):
                opp_val = getattr(old_value, "sipme_Activity", None)
                if opp_val == self:
                    setattr(old_value, "sipme_Activity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_Activity"):
                opp_val = getattr(value, "sipme_Activity", None)
                setattr(value, "sipme_Activity", self)

    @property
    def sipme_Requirement104(self):
        return self.__sipme_Requirement104

    @sipme_Requirement104.setter
    def sipme_Requirement104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Requirement__sipme_Requirement104", None)
        self.__sipme_Requirement104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_Requirement102"):
                opp_val = getattr(old_value, "sipme_Requirement102", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_Requirement102"):
                opp_val = getattr(value, "sipme_Requirement102", None)
                if opp_val is None:
                    setattr(value, "sipme_Requirement102", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sipme_Requirement106(self):
        return self.__sipme_Requirement106

    @sipme_Requirement106.setter
    def sipme_Requirement106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Requirement__sipme_Requirement106", None)
        self.__sipme_Requirement106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_EnterpriseResource107"):
                    opp_val = getattr(item, "sipme_EnterpriseResource107", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_EnterpriseResource107", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_EnterpriseResource107"):
                    opp_val = getattr(item, "sipme_EnterpriseResource107", None)
                    
                    setattr(item, "sipme_EnterpriseResource107", self)
                    

class sipme_Event(SIPME_object):

    def __init__(self, occurenceProbability: str, frequency: str, timeStamp: date, source: str, Event: "sipme_EnterpriseProcessor" = None, Event49: "sipme_EnterpriseProcessor" = None, generates: set["sipme_EnterpriseProcessor"] = None, initiatedBy: set["sipme_EnterpriseProcessor"] = None, sipme_Event: "sipme_Event" = None, sipme_Event71: set["sipme_Event"] = None, events: set["sipme_ObjectView"] = None, Event84: "sipme_ObjectView" = None):
        self.occurenceProbability = occurenceProbability
        self.frequency = frequency
        self.timeStamp = timeStamp
        self.source = source
        self.Event = Event
        self.Event49 = Event49
        self.generates = generates if generates is not None else set()
        self.initiatedBy = initiatedBy if initiatedBy is not None else set()
        self.sipme_Event = sipme_Event
        self.sipme_Event71 = sipme_Event71 if sipme_Event71 is not None else set()
        self.events = events if events is not None else set()
        self.Event84 = Event84
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def frequency(self) -> str:
        return self.__frequency

    @frequency.setter
    def frequency(self, frequency: str):
        self.__frequency = frequency

    @property
    def occurenceProbability(self) -> str:
        return self.__occurenceProbability

    @occurenceProbability.setter
    def occurenceProbability(self, occurenceProbability: str):
        self.__occurenceProbability = occurenceProbability

    @property
    def timeStamp(self) -> date:
        return self.__timeStamp

    @timeStamp.setter
    def timeStamp(self, timeStamp: date):
        self.__timeStamp = timeStamp

    @property
    def Event49(self):
        return self.__Event49

    @Event49.setter
    def Event49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Event__Event49", None)
        self.__Event49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "initiates"):
                opp_val = getattr(old_value, "initiates", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "initiates"):
                opp_val = getattr(value, "initiates", None)
                if opp_val is None:
                    setattr(value, "initiates", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def events(self):
        return self.__events

    @events.setter
    def events(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Event__events", None)
        self.__events = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ObjectView74"):
                    opp_val = getattr(item, "ObjectView74", None)
                    
                    if opp_val == self:
                        setattr(item, "ObjectView74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ObjectView74"):
                    opp_val = getattr(item, "ObjectView74", None)
                    
                    setattr(item, "ObjectView74", self)
                    

    @property
    def Event(self):
        return self.__Event

    @Event.setter
    def Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Event__Event", None)
        self.__Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generatedBy"):
                opp_val = getattr(old_value, "generatedBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generatedBy"):
                opp_val = getattr(value, "generatedBy", None)
                if opp_val is None:
                    setattr(value, "generatedBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def generates(self):
        return self.__generates

    @generates.setter
    def generates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Event__generates", None)
        self.__generates = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EnterpriseProcessor"):
                    opp_val = getattr(item, "EnterpriseProcessor", None)
                    
                    if opp_val == self:
                        setattr(item, "EnterpriseProcessor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EnterpriseProcessor"):
                    opp_val = getattr(item, "EnterpriseProcessor", None)
                    
                    setattr(item, "EnterpriseProcessor", self)
                    

    @property
    def initiatedBy(self):
        return self.__initiatedBy

    @initiatedBy.setter
    def initiatedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Event__initiatedBy", None)
        self.__initiatedBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EnterpriseProcessor70"):
                    opp_val = getattr(item, "EnterpriseProcessor70", None)
                    
                    if opp_val == self:
                        setattr(item, "EnterpriseProcessor70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EnterpriseProcessor70"):
                    opp_val = getattr(item, "EnterpriseProcessor70", None)
                    
                    setattr(item, "EnterpriseProcessor70", self)
                    

    @property
    def sipme_Event(self):
        return self.__sipme_Event

    @sipme_Event.setter
    def sipme_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Event__sipme_Event", None)
        self.__sipme_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_Event71"):
                opp_val = getattr(old_value, "sipme_Event71", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_Event71"):
                opp_val = getattr(value, "sipme_Event71", None)
                if opp_val is None:
                    setattr(value, "sipme_Event71", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Event84(self):
        return self.__Event84

    @Event84.setter
    def Event84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Event__Event84", None)
        self.__Event84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hasAssociatedEvents"):
                opp_val = getattr(old_value, "hasAssociatedEvents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hasAssociatedEvents"):
                opp_val = getattr(value, "hasAssociatedEvents", None)
                if opp_val is None:
                    setattr(value, "hasAssociatedEvents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sipme_Event71(self):
        return self.__sipme_Event71

    @sipme_Event71.setter
    def sipme_Event71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Event__sipme_Event71", None)
        self.__sipme_Event71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_Event"):
                    opp_val = getattr(item, "sipme_Event", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_Event"):
                    opp_val = getattr(item, "sipme_Event", None)
                    
                    setattr(item, "sipme_Event", self)
                    

class sipme_EnterpriseObject(SIPME_object):

    def __init__(self, reference: str, properties: str, sipme_EnterpriseObject: "sipme_BusinessRules" = None, sipme_EnterpriseObject7: "sipme_BusinessRules" = None, EnterpriseObject: "sipme_EnterpriseObject" = None, decomposedIn: "sipme_EnterpriseObject" = None, represents: set["sipme_ObjectView"] = None, EnterpriseObject42: "sipme_EnterpriseObject" = None, partOf: set["sipme_EnterpriseObject"] = None, sipme_EnterpriseObject28: "sipme_Enterprise" = None, EnterpriseObject82: "sipme_ObjectView" = None):
        self.reference = reference
        self.properties = properties
        self.sipme_EnterpriseObject = sipme_EnterpriseObject
        self.sipme_EnterpriseObject7 = sipme_EnterpriseObject7
        self.EnterpriseObject = EnterpriseObject
        self.decomposedIn = decomposedIn
        self.represents = represents if represents is not None else set()
        self.EnterpriseObject42 = EnterpriseObject42
        self.partOf = partOf if partOf is not None else set()
        self.sipme_EnterpriseObject28 = sipme_EnterpriseObject28
        self.EnterpriseObject82 = EnterpriseObject82
        
    @property
    def reference(self) -> str:
        return self.__reference

    @reference.setter
    def reference(self, reference: str):
        self.__reference = reference

    @property
    def properties(self) -> str:
        return self.__properties

    @properties.setter
    def properties(self, properties: str):
        self.__properties = properties

    @property
    def EnterpriseObject(self):
        return self.__EnterpriseObject

    @EnterpriseObject.setter
    def EnterpriseObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseObject__EnterpriseObject", None)
        self.__EnterpriseObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decomposedIn"):
                opp_val = getattr(old_value, "decomposedIn", None)
                if opp_val == self:
                    setattr(old_value, "decomposedIn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decomposedIn"):
                opp_val = getattr(value, "decomposedIn", None)
                setattr(value, "decomposedIn", self)

    @property
    def partOf(self):
        return self.__partOf

    @partOf.setter
    def partOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseObject__partOf", None)
        self.__partOf = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EnterpriseObject42"):
                    opp_val = getattr(item, "EnterpriseObject42", None)
                    
                    if opp_val == self:
                        setattr(item, "EnterpriseObject42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EnterpriseObject42"):
                    opp_val = getattr(item, "EnterpriseObject42", None)
                    
                    setattr(item, "EnterpriseObject42", self)
                    

    @property
    def sipme_EnterpriseObject7(self):
        return self.__sipme_EnterpriseObject7

    @sipme_EnterpriseObject7.setter
    def sipme_EnterpriseObject7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseObject__sipme_EnterpriseObject7", None)
        self.__sipme_EnterpriseObject7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_BusinessRules6"):
                opp_val = getattr(old_value, "sipme_BusinessRules6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_BusinessRules6"):
                opp_val = getattr(value, "sipme_BusinessRules6", None)
                if opp_val is None:
                    setattr(value, "sipme_BusinessRules6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EnterpriseObject42(self):
        return self.__EnterpriseObject42

    @EnterpriseObject42.setter
    def EnterpriseObject42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseObject__EnterpriseObject42", None)
        self.__EnterpriseObject42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "partOf"):
                opp_val = getattr(old_value, "partOf", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "partOf"):
                opp_val = getattr(value, "partOf", None)
                if opp_val is None:
                    setattr(value, "partOf", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sipme_EnterpriseObject28(self):
        return self.__sipme_EnterpriseObject28

    @sipme_EnterpriseObject28.setter
    def sipme_EnterpriseObject28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseObject__sipme_EnterpriseObject28", None)
        self.__sipme_EnterpriseObject28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_Enterprise27"):
                opp_val = getattr(old_value, "sipme_Enterprise27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_Enterprise27"):
                opp_val = getattr(value, "sipme_Enterprise27", None)
                if opp_val is None:
                    setattr(value, "sipme_Enterprise27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sipme_EnterpriseObject(self):
        return self.__sipme_EnterpriseObject

    @sipme_EnterpriseObject.setter
    def sipme_EnterpriseObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseObject__sipme_EnterpriseObject", None)
        self.__sipme_EnterpriseObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_BusinessRules"):
                opp_val = getattr(old_value, "sipme_BusinessRules", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_BusinessRules"):
                opp_val = getattr(value, "sipme_BusinessRules", None)
                if opp_val is None:
                    setattr(value, "sipme_BusinessRules", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def represents(self):
        return self.__represents

    @represents.setter
    def represents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseObject__represents", None)
        self.__represents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ObjectView"):
                    opp_val = getattr(item, "ObjectView", None)
                    
                    if opp_val == self:
                        setattr(item, "ObjectView", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ObjectView"):
                    opp_val = getattr(item, "ObjectView", None)
                    
                    setattr(item, "ObjectView", self)
                    

    @property
    def decomposedIn(self):
        return self.__decomposedIn

    @decomposedIn.setter
    def decomposedIn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseObject__decomposedIn", None)
        self.__decomposedIn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EnterpriseObject"):
                opp_val = getattr(old_value, "EnterpriseObject", None)
                if opp_val == self:
                    setattr(old_value, "EnterpriseObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EnterpriseObject"):
                opp_val = getattr(value, "EnterpriseObject", None)
                setattr(value, "EnterpriseObject", self)

    @property
    def EnterpriseObject82(self):
        return self.__EnterpriseObject82

    @EnterpriseObject82.setter
    def EnterpriseObject82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_EnterpriseObject__EnterpriseObject82", None)
        self.__EnterpriseObject82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "representedBy"):
                opp_val = getattr(old_value, "representedBy", None)
                if opp_val == self:
                    setattr(old_value, "representedBy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "representedBy"):
                opp_val = getattr(value, "representedBy", None)
                setattr(value, "representedBy", self)

class sipme_ObjectsFileView(ObjectView):

    def __init__(self, filePriority: int, fileState: str, ObjectsFileView: "sipme_CompanyMember" = None, sipme_ObjectsFileView: set["sipme_ObjectView"] = None, sipme_ObjectsFileView96: "sipme_ObjectsFileView" = None, sipme_ObjectsFileView94: set["sipme_ObjectsFileView"] = None, responsibleOfFile: "sipme_CompanyMember" = None):
        self.filePriority = filePriority
        self.fileState = fileState
        self.ObjectsFileView = ObjectsFileView
        self.sipme_ObjectsFileView = sipme_ObjectsFileView if sipme_ObjectsFileView is not None else set()
        self.sipme_ObjectsFileView96 = sipme_ObjectsFileView96
        self.sipme_ObjectsFileView94 = sipme_ObjectsFileView94 if sipme_ObjectsFileView94 is not None else set()
        self.responsibleOfFile = responsibleOfFile
        
    @property
    def filePriority(self) -> int:
        return self.__filePriority

    @filePriority.setter
    def filePriority(self, filePriority: int):
        self.__filePriority = filePriority

    @property
    def fileState(self) -> str:
        return self.__fileState

    @fileState.setter
    def fileState(self, fileState: str):
        self.__fileState = fileState

    @property
    def sipme_ObjectsFileView94(self):
        return self.__sipme_ObjectsFileView94

    @sipme_ObjectsFileView94.setter
    def sipme_ObjectsFileView94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_ObjectsFileView__sipme_ObjectsFileView94", None)
        self.__sipme_ObjectsFileView94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_ObjectsFileView96"):
                    opp_val = getattr(item, "sipme_ObjectsFileView96", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_ObjectsFileView96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_ObjectsFileView96"):
                    opp_val = getattr(item, "sipme_ObjectsFileView96", None)
                    
                    setattr(item, "sipme_ObjectsFileView96", self)
                    

    @property
    def sipme_ObjectsFileView96(self):
        return self.__sipme_ObjectsFileView96

    @sipme_ObjectsFileView96.setter
    def sipme_ObjectsFileView96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_ObjectsFileView__sipme_ObjectsFileView96", None)
        self.__sipme_ObjectsFileView96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_ObjectsFileView94"):
                opp_val = getattr(old_value, "sipme_ObjectsFileView94", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_ObjectsFileView94"):
                opp_val = getattr(value, "sipme_ObjectsFileView94", None)
                if opp_val is None:
                    setattr(value, "sipme_ObjectsFileView94", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sipme_ObjectsFileView(self):
        return self.__sipme_ObjectsFileView

    @sipme_ObjectsFileView.setter
    def sipme_ObjectsFileView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_ObjectsFileView__sipme_ObjectsFileView", None)
        self.__sipme_ObjectsFileView = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_ObjectView93"):
                    opp_val = getattr(item, "sipme_ObjectView93", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_ObjectView93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_ObjectView93"):
                    opp_val = getattr(item, "sipme_ObjectView93", None)
                    
                    setattr(item, "sipme_ObjectView93", self)
                    

    @property
    def ObjectsFileView(self):
        return self.__ObjectsFileView

    @ObjectsFileView.setter
    def ObjectsFileView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_ObjectsFileView__ObjectsFileView", None)
        self.__ObjectsFileView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fileResponsible"):
                opp_val = getattr(old_value, "fileResponsible", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fileResponsible"):
                opp_val = getattr(value, "fileResponsible", None)
                if opp_val is None:
                    setattr(value, "fileResponsible", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def responsibleOfFile(self):
        return self.__responsibleOfFile

    @responsibleOfFile.setter
    def responsibleOfFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_ObjectsFileView__responsibleOfFile", None)
        self.__responsibleOfFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompanyMember98"):
                opp_val = getattr(old_value, "CompanyMember98", None)
                if opp_val == self:
                    setattr(old_value, "CompanyMember98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompanyMember98"):
                opp_val = getattr(value, "CompanyMember98", None)
                setattr(value, "CompanyMember98", self)

class EnterpriseResource:

    pass
class sipme_Device_Machine(EnterpriseResource):

    def __init__(self, manufacturer: str, machineMaintainer: str):
        self.manufacturer = manufacturer
        self.machineMaintainer = machineMaintainer
        
    @property
    def machineMaintainer(self) -> str:
        return self.__machineMaintainer

    @machineMaintainer.setter
    def machineMaintainer(self, machineMaintainer: str):
        self.__machineMaintainer = machineMaintainer

    @property
    def manufacturer(self) -> str:
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer: str):
        self.__manufacturer = manufacturer

class sipme_CompanyMember(EnterpriseResource, Stakeholder):

    def __init__(self, fullName: str, socialSecurityNumber: int, address: str, cellResponsible: set["sipme_OrganisationCell"] = None, fileResponsible: set["sipme_ObjectsFileView"] = None, owners: set["sipme_Workstation"] = None, responsible: set["sipme_Workstation"] = None, sipme_CompanyMember: "sipme_Enterprise" = None, CompanyMember98: "sipme_ObjectsFileView" = None, CompanyMember: "sipme_OrganisationCell" = None, CompanyMember137: "sipme_Workstation" = None, CompanyMember139: "sipme_Workstation" = None):
        self.fullName = fullName
        self.socialSecurityNumber = socialSecurityNumber
        self.address = address
        self.cellResponsible = cellResponsible if cellResponsible is not None else set()
        self.fileResponsible = fileResponsible if fileResponsible is not None else set()
        self.owners = owners if owners is not None else set()
        self.responsible = responsible if responsible is not None else set()
        self.sipme_CompanyMember = sipme_CompanyMember
        self.CompanyMember98 = CompanyMember98
        self.CompanyMember = CompanyMember
        self.CompanyMember137 = CompanyMember137
        self.CompanyMember139 = CompanyMember139
        
    @property
    def socialSecurityNumber(self) -> int:
        return self.__socialSecurityNumber

    @socialSecurityNumber.setter
    def socialSecurityNumber(self, socialSecurityNumber: int):
        self.__socialSecurityNumber = socialSecurityNumber

    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def CompanyMember137(self):
        return self.__CompanyMember137

    @CompanyMember137.setter
    def CompanyMember137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_CompanyMember__CompanyMember137", None)
        self.__CompanyMember137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "responsibleOf"):
                opp_val = getattr(old_value, "responsibleOf", None)
                if opp_val == self:
                    setattr(old_value, "responsibleOf", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "responsibleOf"):
                opp_val = getattr(value, "responsibleOf", None)
                setattr(value, "responsibleOf", self)

    @property
    def CompanyMember98(self):
        return self.__CompanyMember98

    @CompanyMember98.setter
    def CompanyMember98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_CompanyMember__CompanyMember98", None)
        self.__CompanyMember98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "responsibleOfFile"):
                opp_val = getattr(old_value, "responsibleOfFile", None)
                if opp_val == self:
                    setattr(old_value, "responsibleOfFile", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "responsibleOfFile"):
                opp_val = getattr(value, "responsibleOfFile", None)
                setattr(value, "responsibleOfFile", self)

    @property
    def sipme_CompanyMember(self):
        return self.__sipme_CompanyMember

    @sipme_CompanyMember.setter
    def sipme_CompanyMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_CompanyMember__sipme_CompanyMember", None)
        self.__sipme_CompanyMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_Enterprise34"):
                opp_val = getattr(old_value, "sipme_Enterprise34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_Enterprise34"):
                opp_val = getattr(value, "sipme_Enterprise34", None)
                if opp_val is None:
                    setattr(value, "sipme_Enterprise34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def owners(self):
        return self.__owners

    @owners.setter
    def owners(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_CompanyMember__owners", None)
        self.__owners = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Workstation"):
                    opp_val = getattr(item, "Workstation", None)
                    
                    if opp_val == self:
                        setattr(item, "Workstation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Workstation"):
                    opp_val = getattr(item, "Workstation", None)
                    
                    setattr(item, "Workstation", self)
                    

    @property
    def fileResponsible(self):
        return self.__fileResponsible

    @fileResponsible.setter
    def fileResponsible(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_CompanyMember__fileResponsible", None)
        self.__fileResponsible = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ObjectsFileView"):
                    opp_val = getattr(item, "ObjectsFileView", None)
                    
                    if opp_val == self:
                        setattr(item, "ObjectsFileView", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ObjectsFileView"):
                    opp_val = getattr(item, "ObjectsFileView", None)
                    
                    setattr(item, "ObjectsFileView", self)
                    

    @property
    def responsible(self):
        return self.__responsible

    @responsible.setter
    def responsible(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_CompanyMember__responsible", None)
        self.__responsible = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Workstation11"):
                    opp_val = getattr(item, "Workstation11", None)
                    
                    if opp_val == self:
                        setattr(item, "Workstation11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Workstation11"):
                    opp_val = getattr(item, "Workstation11", None)
                    
                    setattr(item, "Workstation11", self)
                    

    @property
    def CompanyMember139(self):
        return self.__CompanyMember139

    @CompanyMember139.setter
    def CompanyMember139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_CompanyMember__CompanyMember139", None)
        self.__CompanyMember139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inChargeOf"):
                opp_val = getattr(old_value, "inChargeOf", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inChargeOf"):
                opp_val = getattr(value, "inChargeOf", None)
                if opp_val is None:
                    setattr(value, "inChargeOf", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cellResponsible(self):
        return self.__cellResponsible

    @cellResponsible.setter
    def cellResponsible(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_CompanyMember__cellResponsible", None)
        self.__cellResponsible = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OrganisationCell"):
                    opp_val = getattr(item, "OrganisationCell", None)
                    
                    if opp_val == self:
                        setattr(item, "OrganisationCell", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OrganisationCell"):
                    opp_val = getattr(item, "OrganisationCell", None)
                    
                    setattr(item, "OrganisationCell", self)
                    

    @property
    def CompanyMember(self):
        return self.__CompanyMember

    @CompanyMember.setter
    def CompanyMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_CompanyMember__CompanyMember", None)
        self.__CompanyMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "responsibleOfCell"):
                opp_val = getattr(old_value, "responsibleOfCell", None)
                if opp_val == self:
                    setattr(old_value, "responsibleOfCell", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "responsibleOfCell"):
                opp_val = getattr(value, "responsibleOfCell", None)
                setattr(value, "responsibleOfCell", self)

class sipme_Application(EnterpriseResource):

    def __init__(self, applicationEditor: str, applicationMaintainer: str):
        self.applicationEditor = applicationEditor
        self.applicationMaintainer = applicationMaintainer
        
    @property
    def applicationEditor(self) -> str:
        return self.__applicationEditor

    @applicationEditor.setter
    def applicationEditor(self, applicationEditor: str):
        self.__applicationEditor = applicationEditor

    @property
    def applicationMaintainer(self) -> str:
        return self.__applicationMaintainer

    @applicationMaintainer.setter
    def applicationMaintainer(self, applicationMaintainer: str):
        self.__applicationMaintainer = applicationMaintainer

class EnterpriseProcessor:

    pass
class sipme_Domain(OrganisationCell, SIPME_object, EnterpriseProcessor):

    def __init__(self, domainCharacterization: str, performanceIndicators: float, sipme_Domain: "sipme_BusinessProcess" = None, sipme_Domain15: set["sipme_BusinessProcess"] = None, covers: set["sipme_OrganisationCell"] = None, sipme_Domain20: set["sipme_BusinessRules"] = None, sipme_Domain25: "sipme_Enterprise" = None, Domain: "sipme_OrganisationCell" = None):
        self.domainCharacterization = domainCharacterization
        self.performanceIndicators = performanceIndicators
        self.sipme_Domain = sipme_Domain
        self.sipme_Domain15 = sipme_Domain15 if sipme_Domain15 is not None else set()
        self.covers = covers if covers is not None else set()
        self.sipme_Domain20 = sipme_Domain20 if sipme_Domain20 is not None else set()
        self.sipme_Domain25 = sipme_Domain25
        self.Domain = Domain
        
    @property
    def domainCharacterization(self) -> str:
        return self.__domainCharacterization

    @domainCharacterization.setter
    def domainCharacterization(self, domainCharacterization: str):
        self.__domainCharacterization = domainCharacterization

    @property
    def performanceIndicators(self) -> float:
        return self.__performanceIndicators

    @performanceIndicators.setter
    def performanceIndicators(self, performanceIndicators: float):
        self.__performanceIndicators = performanceIndicators

    @property
    def covers(self):
        return self.__covers

    @covers.setter
    def covers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Domain__covers", None)
        self.__covers = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OrganisationCell18"):
                    opp_val = getattr(item, "OrganisationCell18", None)
                    
                    if opp_val == self:
                        setattr(item, "OrganisationCell18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OrganisationCell18"):
                    opp_val = getattr(item, "OrganisationCell18", None)
                    
                    setattr(item, "OrganisationCell18", self)
                    

    @property
    def sipme_Domain25(self):
        return self.__sipme_Domain25

    @sipme_Domain25.setter
    def sipme_Domain25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Domain__sipme_Domain25", None)
        self.__sipme_Domain25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_Enterprise24"):
                opp_val = getattr(old_value, "sipme_Enterprise24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_Enterprise24"):
                opp_val = getattr(value, "sipme_Enterprise24", None)
                if opp_val is None:
                    setattr(value, "sipme_Enterprise24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sipme_Domain20(self):
        return self.__sipme_Domain20

    @sipme_Domain20.setter
    def sipme_Domain20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Domain__sipme_Domain20", None)
        self.__sipme_Domain20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_BusinessRules21"):
                    opp_val = getattr(item, "sipme_BusinessRules21", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_BusinessRules21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_BusinessRules21"):
                    opp_val = getattr(item, "sipme_BusinessRules21", None)
                    
                    setattr(item, "sipme_BusinessRules21", self)
                    

    @property
    def sipme_Domain15(self):
        return self.__sipme_Domain15

    @sipme_Domain15.setter
    def sipme_Domain15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Domain__sipme_Domain15", None)
        self.__sipme_Domain15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_BusinessProcess16"):
                    opp_val = getattr(item, "sipme_BusinessProcess16", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_BusinessProcess16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_BusinessProcess16"):
                    opp_val = getattr(item, "sipme_BusinessProcess16", None)
                    
                    setattr(item, "sipme_BusinessProcess16", self)
                    

    @property
    def Domain(self):
        return self.__Domain

    @Domain.setter
    def Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Domain__Domain", None)
        self.__Domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coveredBy"):
                opp_val = getattr(old_value, "coveredBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coveredBy"):
                opp_val = getattr(value, "coveredBy", None)
                if opp_val is None:
                    setattr(value, "coveredBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sipme_Domain(self):
        return self.__sipme_Domain

    @sipme_Domain.setter
    def sipme_Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Domain__sipme_Domain", None)
        self.__sipme_Domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_BusinessProcess"):
                opp_val = getattr(old_value, "sipme_BusinessProcess", None)
                if opp_val == self:
                    setattr(old_value, "sipme_BusinessProcess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_BusinessProcess"):
                opp_val = getattr(value, "sipme_BusinessProcess", None)
                setattr(value, "sipme_BusinessProcess", self)

class sipme_Workstation(EnterpriseProcessor):

    def __init__(self, ProfileDeescription: str, Workstation: "sipme_CompanyMember" = None, Workstation11: "sipme_CompanyMember" = None, Workstation86: "sipme_OrganisationCell" = None, workstations: "sipme_OrganisationCell" = None, responsibleOf: "sipme_CompanyMember" = None, inChargeOf: set["sipme_CompanyMember"] = None):
        self.ProfileDeescription = ProfileDeescription
        self.Workstation = Workstation
        self.Workstation11 = Workstation11
        self.Workstation86 = Workstation86
        self.workstations = workstations
        self.responsibleOf = responsibleOf
        self.inChargeOf = inChargeOf if inChargeOf is not None else set()
        
    @property
    def ProfileDeescription(self) -> str:
        return self.__ProfileDeescription

    @ProfileDeescription.setter
    def ProfileDeescription(self, ProfileDeescription: str):
        self.__ProfileDeescription = ProfileDeescription

    @property
    def workstations(self):
        return self.__workstations

    @workstations.setter
    def workstations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Workstation__workstations", None)
        self.__workstations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OrganisationCell135"):
                opp_val = getattr(old_value, "OrganisationCell135", None)
                if opp_val == self:
                    setattr(old_value, "OrganisationCell135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OrganisationCell135"):
                opp_val = getattr(value, "OrganisationCell135", None)
                setattr(value, "OrganisationCell135", self)

    @property
    def Workstation86(self):
        return self.__Workstation86

    @Workstation86.setter
    def Workstation86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Workstation__Workstation86", None)
        self.__Workstation86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "organisationCell"):
                opp_val = getattr(old_value, "organisationCell", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "organisationCell"):
                opp_val = getattr(value, "organisationCell", None)
                if opp_val is None:
                    setattr(value, "organisationCell", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Workstation(self):
        return self.__Workstation

    @Workstation.setter
    def Workstation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Workstation__Workstation", None)
        self.__Workstation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owners"):
                opp_val = getattr(old_value, "owners", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owners"):
                opp_val = getattr(value, "owners", None)
                if opp_val is None:
                    setattr(value, "owners", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def inChargeOf(self):
        return self.__inChargeOf

    @inChargeOf.setter
    def inChargeOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Workstation__inChargeOf", None)
        self.__inChargeOf = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompanyMember139"):
                    opp_val = getattr(item, "CompanyMember139", None)
                    
                    if opp_val == self:
                        setattr(item, "CompanyMember139", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompanyMember139"):
                    opp_val = getattr(item, "CompanyMember139", None)
                    
                    setattr(item, "CompanyMember139", self)
                    

    @property
    def Workstation11(self):
        return self.__Workstation11

    @Workstation11.setter
    def Workstation11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Workstation__Workstation11", None)
        self.__Workstation11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "responsible"):
                opp_val = getattr(old_value, "responsible", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "responsible"):
                opp_val = getattr(value, "responsible", None)
                if opp_val is None:
                    setattr(value, "responsible", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def responsibleOf(self):
        return self.__responsibleOf

    @responsibleOf.setter
    def responsibleOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Workstation__responsibleOf", None)
        self.__responsibleOf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompanyMember137"):
                opp_val = getattr(old_value, "CompanyMember137", None)
                if opp_val == self:
                    setattr(old_value, "CompanyMember137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompanyMember137"):
                opp_val = getattr(value, "CompanyMember137", None)
                setattr(value, "CompanyMember137", self)

class sipme_BusinessProcess(EnterpriseProcessor):

    def __init__(self, ProcessPriority: int, BusinessProcess: "sipme_Activity" = None, activityOf: set["sipme_Activity"] = None, sipme_BusinessProcess: "sipme_Domain" = None, sipme_BusinessProcess16: "sipme_Domain" = None):
        self.ProcessPriority = ProcessPriority
        self.BusinessProcess = BusinessProcess
        self.activityOf = activityOf if activityOf is not None else set()
        self.sipme_BusinessProcess = sipme_BusinessProcess
        self.sipme_BusinessProcess16 = sipme_BusinessProcess16
        
    @property
    def ProcessPriority(self) -> int:
        return self.__ProcessPriority

    @ProcessPriority.setter
    def ProcessPriority(self, ProcessPriority: int):
        self.__ProcessPriority = ProcessPriority

    @property
    def sipme_BusinessProcess16(self):
        return self.__sipme_BusinessProcess16

    @sipme_BusinessProcess16.setter
    def sipme_BusinessProcess16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_BusinessProcess__sipme_BusinessProcess16", None)
        self.__sipme_BusinessProcess16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_Domain15"):
                opp_val = getattr(old_value, "sipme_Domain15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_Domain15"):
                opp_val = getattr(value, "sipme_Domain15", None)
                if opp_val is None:
                    setattr(value, "sipme_Domain15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activityOf(self):
        return self.__activityOf

    @activityOf.setter
    def activityOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_BusinessProcess__activityOf", None)
        self.__activityOf = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Activity"):
                    opp_val = getattr(item, "Activity", None)
                    
                    if opp_val == self:
                        setattr(item, "Activity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Activity"):
                    opp_val = getattr(item, "Activity", None)
                    
                    setattr(item, "Activity", self)
                    

    @property
    def sipme_BusinessProcess(self):
        return self.__sipme_BusinessProcess

    @sipme_BusinessProcess.setter
    def sipme_BusinessProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_BusinessProcess__sipme_BusinessProcess", None)
        self.__sipme_BusinessProcess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_Domain"):
                opp_val = getattr(old_value, "sipme_Domain", None)
                if opp_val == self:
                    setattr(old_value, "sipme_Domain", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_Domain"):
                opp_val = getattr(value, "sipme_Domain", None)
                setattr(value, "sipme_Domain", self)

    @property
    def BusinessProcess(self):
        return self.__BusinessProcess

    @BusinessProcess.setter
    def BusinessProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_BusinessProcess__BusinessProcess", None)
        self.__BusinessProcess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activities"):
                opp_val = getattr(old_value, "activities", None)
                if opp_val == self:
                    setattr(old_value, "activities", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activities"):
                opp_val = getattr(value, "activities", None)
                setattr(value, "activities", self)

class sipme_Enterprise(EnterpriseProcessor):

    def __init__(self, acronym: str, status: str, sipme_Enterprise: set["sipme_Objective"] = None, sipme_Enterprise24: set["sipme_Domain"] = None, sipme_Enterprise27: set["sipme_EnterpriseObject"] = None, sipme_Enterprise30: set["sipme_EnterpriseService"] = None, sipme_Enterprise32: set["sipme_EnterpriseProduct"] = None, sipme_Enterprise34: set["sipme_CompanyMember"] = None, sipme_Enterprise36: set["sipme_OrganisationCell"] = None):
        self.acronym = acronym
        self.status = status
        self.sipme_Enterprise = sipme_Enterprise if sipme_Enterprise is not None else set()
        self.sipme_Enterprise24 = sipme_Enterprise24 if sipme_Enterprise24 is not None else set()
        self.sipme_Enterprise27 = sipme_Enterprise27 if sipme_Enterprise27 is not None else set()
        self.sipme_Enterprise30 = sipme_Enterprise30 if sipme_Enterprise30 is not None else set()
        self.sipme_Enterprise32 = sipme_Enterprise32 if sipme_Enterprise32 is not None else set()
        self.sipme_Enterprise34 = sipme_Enterprise34 if sipme_Enterprise34 is not None else set()
        self.sipme_Enterprise36 = sipme_Enterprise36 if sipme_Enterprise36 is not None else set()
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def acronym(self) -> str:
        return self.__acronym

    @acronym.setter
    def acronym(self, acronym: str):
        self.__acronym = acronym

    @property
    def sipme_Enterprise34(self):
        return self.__sipme_Enterprise34

    @sipme_Enterprise34.setter
    def sipme_Enterprise34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Enterprise__sipme_Enterprise34", None)
        self.__sipme_Enterprise34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_CompanyMember"):
                    opp_val = getattr(item, "sipme_CompanyMember", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_CompanyMember", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_CompanyMember"):
                    opp_val = getattr(item, "sipme_CompanyMember", None)
                    
                    setattr(item, "sipme_CompanyMember", self)
                    

    @property
    def sipme_Enterprise36(self):
        return self.__sipme_Enterprise36

    @sipme_Enterprise36.setter
    def sipme_Enterprise36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Enterprise__sipme_Enterprise36", None)
        self.__sipme_Enterprise36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_OrganisationCell"):
                    opp_val = getattr(item, "sipme_OrganisationCell", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_OrganisationCell", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_OrganisationCell"):
                    opp_val = getattr(item, "sipme_OrganisationCell", None)
                    
                    setattr(item, "sipme_OrganisationCell", self)
                    

    @property
    def sipme_Enterprise30(self):
        return self.__sipme_Enterprise30

    @sipme_Enterprise30.setter
    def sipme_Enterprise30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Enterprise__sipme_Enterprise30", None)
        self.__sipme_Enterprise30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_EnterpriseService"):
                    opp_val = getattr(item, "sipme_EnterpriseService", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_EnterpriseService", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_EnterpriseService"):
                    opp_val = getattr(item, "sipme_EnterpriseService", None)
                    
                    setattr(item, "sipme_EnterpriseService", self)
                    

    @property
    def sipme_Enterprise32(self):
        return self.__sipme_Enterprise32

    @sipme_Enterprise32.setter
    def sipme_Enterprise32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Enterprise__sipme_Enterprise32", None)
        self.__sipme_Enterprise32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_EnterpriseProduct"):
                    opp_val = getattr(item, "sipme_EnterpriseProduct", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_EnterpriseProduct", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_EnterpriseProduct"):
                    opp_val = getattr(item, "sipme_EnterpriseProduct", None)
                    
                    setattr(item, "sipme_EnterpriseProduct", self)
                    

    @property
    def sipme_Enterprise24(self):
        return self.__sipme_Enterprise24

    @sipme_Enterprise24.setter
    def sipme_Enterprise24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Enterprise__sipme_Enterprise24", None)
        self.__sipme_Enterprise24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_Domain25"):
                    opp_val = getattr(item, "sipme_Domain25", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_Domain25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_Domain25"):
                    opp_val = getattr(item, "sipme_Domain25", None)
                    
                    setattr(item, "sipme_Domain25", self)
                    

    @property
    def sipme_Enterprise27(self):
        return self.__sipme_Enterprise27

    @sipme_Enterprise27.setter
    def sipme_Enterprise27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Enterprise__sipme_Enterprise27", None)
        self.__sipme_Enterprise27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_EnterpriseObject28"):
                    opp_val = getattr(item, "sipme_EnterpriseObject28", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_EnterpriseObject28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_EnterpriseObject28"):
                    opp_val = getattr(item, "sipme_EnterpriseObject28", None)
                    
                    setattr(item, "sipme_EnterpriseObject28", self)
                    

    @property
    def sipme_Enterprise(self):
        return self.__sipme_Enterprise

    @sipme_Enterprise.setter
    def sipme_Enterprise(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Enterprise__sipme_Enterprise", None)
        self.__sipme_Enterprise = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_Objective"):
                    opp_val = getattr(item, "sipme_Objective", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_Objective", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_Objective"):
                    opp_val = getattr(item, "sipme_Objective", None)
                    
                    setattr(item, "sipme_Objective", self)
                    

class sipme_Role_Function(EnterpriseProcessor):

    def __init__(self, roleType: str, Role_Function: "sipme_EnterpriseProcessor" = None, Role_Function62: "sipme_EnterpriseResource" = None, Role_Function64: "sipme_EnterpriseResource" = None, sipme_Role_Function121: set["sipme_BusinessRules"] = None, sipme_Role_Function: set["sipme_Task"] = None, plays: set["sipme_EnterpriseResource"] = None, isAbleToPlay: set["sipme_EnterpriseResource"] = None, implements: set["sipme_EnterpriseProcessor"] = None):
        self.roleType = roleType
        self.Role_Function = Role_Function
        self.Role_Function62 = Role_Function62
        self.Role_Function64 = Role_Function64
        self.sipme_Role_Function121 = sipme_Role_Function121 if sipme_Role_Function121 is not None else set()
        self.sipme_Role_Function = sipme_Role_Function if sipme_Role_Function is not None else set()
        self.plays = plays if plays is not None else set()
        self.isAbleToPlay = isAbleToPlay if isAbleToPlay is not None else set()
        self.implements = implements if implements is not None else set()
        
    @property
    def roleType(self) -> str:
        return self.__roleType

    @roleType.setter
    def roleType(self, roleType: str):
        self.__roleType = roleType

    @property
    def plays(self):
        return self.__plays

    @plays.setter
    def plays(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Role_Function__plays", None)
        self.__plays = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EnterpriseResource"):
                    opp_val = getattr(item, "EnterpriseResource", None)
                    
                    if opp_val == self:
                        setattr(item, "EnterpriseResource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EnterpriseResource"):
                    opp_val = getattr(item, "EnterpriseResource", None)
                    
                    setattr(item, "EnterpriseResource", self)
                    

    @property
    def sipme_Role_Function121(self):
        return self.__sipme_Role_Function121

    @sipme_Role_Function121.setter
    def sipme_Role_Function121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Role_Function__sipme_Role_Function121", None)
        self.__sipme_Role_Function121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_BusinessRules122"):
                    opp_val = getattr(item, "sipme_BusinessRules122", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_BusinessRules122", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_BusinessRules122"):
                    opp_val = getattr(item, "sipme_BusinessRules122", None)
                    
                    setattr(item, "sipme_BusinessRules122", self)
                    

    @property
    def Role_Function62(self):
        return self.__Role_Function62

    @Role_Function62.setter
    def Role_Function62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Role_Function__Role_Function62", None)
        self.__Role_Function62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "playedBy"):
                opp_val = getattr(old_value, "playedBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "playedBy"):
                opp_val = getattr(value, "playedBy", None)
                if opp_val is None:
                    setattr(value, "playedBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def isAbleToPlay(self):
        return self.__isAbleToPlay

    @isAbleToPlay.setter
    def isAbleToPlay(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Role_Function__isAbleToPlay", None)
        self.__isAbleToPlay = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EnterpriseResource117"):
                    opp_val = getattr(item, "EnterpriseResource117", None)
                    
                    if opp_val == self:
                        setattr(item, "EnterpriseResource117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EnterpriseResource117"):
                    opp_val = getattr(item, "EnterpriseResource117", None)
                    
                    setattr(item, "EnterpriseResource117", self)
                    

    @property
    def Role_Function(self):
        return self.__Role_Function

    @Role_Function.setter
    def Role_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Role_Function__Role_Function", None)
        self.__Role_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "implementedBy"):
                opp_val = getattr(old_value, "implementedBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "implementedBy"):
                opp_val = getattr(value, "implementedBy", None)
                if opp_val is None:
                    setattr(value, "implementedBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Role_Function64(self):
        return self.__Role_Function64

    @Role_Function64.setter
    def Role_Function64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Role_Function__Role_Function64", None)
        self.__Role_Function64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "canBePlayedBy"):
                opp_val = getattr(old_value, "canBePlayedBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "canBePlayedBy"):
                opp_val = getattr(value, "canBePlayedBy", None)
                if opp_val is None:
                    setattr(value, "canBePlayedBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def implements(self):
        return self.__implements

    @implements.setter
    def implements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Role_Function__implements", None)
        self.__implements = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EnterpriseProcessor119"):
                    opp_val = getattr(item, "EnterpriseProcessor119", None)
                    
                    if opp_val == self:
                        setattr(item, "EnterpriseProcessor119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EnterpriseProcessor119"):
                    opp_val = getattr(item, "EnterpriseProcessor119", None)
                    
                    setattr(item, "EnterpriseProcessor119", self)
                    

    @property
    def sipme_Role_Function(self):
        return self.__sipme_Role_Function

    @sipme_Role_Function.setter
    def sipme_Role_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Role_Function__sipme_Role_Function", None)
        self.__sipme_Role_Function = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_Task114"):
                    opp_val = getattr(item, "sipme_Task114", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_Task114", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_Task114"):
                    opp_val = getattr(item, "sipme_Task114", None)
                    
                    setattr(item, "sipme_Task114", self)
                    

class sipme_OrganisationCell(EnterpriseProcessor):

    def __init__(self, organisationLevel: int, OrganisationCell: "sipme_CompanyMember" = None, OrganisationCell18: "sipme_Domain" = None, sipme_OrganisationCell: "sipme_Enterprise" = None, organisationCell: set["sipme_Workstation"] = None, coveredBy: set["sipme_Domain"] = None, responsibleOfCell: "sipme_CompanyMember" = None, sipme_OrganisationCell91: "sipme_OrganisationCell" = None, sipme_OrganisationCell89: set["sipme_OrganisationCell"] = None, OrganisationCell135: "sipme_Workstation" = None):
        self.organisationLevel = organisationLevel
        self.OrganisationCell = OrganisationCell
        self.OrganisationCell18 = OrganisationCell18
        self.sipme_OrganisationCell = sipme_OrganisationCell
        self.organisationCell = organisationCell if organisationCell is not None else set()
        self.coveredBy = coveredBy if coveredBy is not None else set()
        self.responsibleOfCell = responsibleOfCell
        self.sipme_OrganisationCell91 = sipme_OrganisationCell91
        self.sipme_OrganisationCell89 = sipme_OrganisationCell89 if sipme_OrganisationCell89 is not None else set()
        self.OrganisationCell135 = OrganisationCell135
        
    @property
    def organisationLevel(self) -> int:
        return self.__organisationLevel

    @organisationLevel.setter
    def organisationLevel(self, organisationLevel: int):
        self.__organisationLevel = organisationLevel

    @property
    def organisationCell(self):
        return self.__organisationCell

    @organisationCell.setter
    def organisationCell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_OrganisationCell__organisationCell", None)
        self.__organisationCell = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Workstation86"):
                    opp_val = getattr(item, "Workstation86", None)
                    
                    if opp_val == self:
                        setattr(item, "Workstation86", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Workstation86"):
                    opp_val = getattr(item, "Workstation86", None)
                    
                    setattr(item, "Workstation86", self)
                    

    @property
    def OrganisationCell135(self):
        return self.__OrganisationCell135

    @OrganisationCell135.setter
    def OrganisationCell135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_OrganisationCell__OrganisationCell135", None)
        self.__OrganisationCell135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workstations"):
                opp_val = getattr(old_value, "workstations", None)
                if opp_val == self:
                    setattr(old_value, "workstations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workstations"):
                opp_val = getattr(value, "workstations", None)
                setattr(value, "workstations", self)

    @property
    def sipme_OrganisationCell91(self):
        return self.__sipme_OrganisationCell91

    @sipme_OrganisationCell91.setter
    def sipme_OrganisationCell91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_OrganisationCell__sipme_OrganisationCell91", None)
        self.__sipme_OrganisationCell91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_OrganisationCell89"):
                opp_val = getattr(old_value, "sipme_OrganisationCell89", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_OrganisationCell89"):
                opp_val = getattr(value, "sipme_OrganisationCell89", None)
                if opp_val is None:
                    setattr(value, "sipme_OrganisationCell89", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def responsibleOfCell(self):
        return self.__responsibleOfCell

    @responsibleOfCell.setter
    def responsibleOfCell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_OrganisationCell__responsibleOfCell", None)
        self.__responsibleOfCell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompanyMember"):
                opp_val = getattr(old_value, "CompanyMember", None)
                if opp_val == self:
                    setattr(old_value, "CompanyMember", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompanyMember"):
                opp_val = getattr(value, "CompanyMember", None)
                setattr(value, "CompanyMember", self)

    @property
    def coveredBy(self):
        return self.__coveredBy

    @coveredBy.setter
    def coveredBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_OrganisationCell__coveredBy", None)
        self.__coveredBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Domain"):
                    opp_val = getattr(item, "Domain", None)
                    
                    if opp_val == self:
                        setattr(item, "Domain", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Domain"):
                    opp_val = getattr(item, "Domain", None)
                    
                    setattr(item, "Domain", self)
                    

    @property
    def sipme_OrganisationCell89(self):
        return self.__sipme_OrganisationCell89

    @sipme_OrganisationCell89.setter
    def sipme_OrganisationCell89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_OrganisationCell__sipme_OrganisationCell89", None)
        self.__sipme_OrganisationCell89 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_OrganisationCell91"):
                    opp_val = getattr(item, "sipme_OrganisationCell91", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_OrganisationCell91", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_OrganisationCell91"):
                    opp_val = getattr(item, "sipme_OrganisationCell91", None)
                    
                    setattr(item, "sipme_OrganisationCell91", self)
                    

    @property
    def OrganisationCell18(self):
        return self.__OrganisationCell18

    @OrganisationCell18.setter
    def OrganisationCell18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_OrganisationCell__OrganisationCell18", None)
        self.__OrganisationCell18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "covers"):
                opp_val = getattr(old_value, "covers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "covers"):
                opp_val = getattr(value, "covers", None)
                if opp_val is None:
                    setattr(value, "covers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sipme_OrganisationCell(self):
        return self.__sipme_OrganisationCell

    @sipme_OrganisationCell.setter
    def sipme_OrganisationCell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_OrganisationCell__sipme_OrganisationCell", None)
        self.__sipme_OrganisationCell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_Enterprise36"):
                opp_val = getattr(old_value, "sipme_Enterprise36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_Enterprise36"):
                opp_val = getattr(value, "sipme_Enterprise36", None)
                if opp_val is None:
                    setattr(value, "sipme_Enterprise36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OrganisationCell(self):
        return self.__OrganisationCell

    @OrganisationCell.setter
    def OrganisationCell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_OrganisationCell__OrganisationCell", None)
        self.__OrganisationCell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cellResponsible"):
                opp_val = getattr(old_value, "cellResponsible", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cellResponsible"):
                opp_val = getattr(value, "cellResponsible", None)
                if opp_val is None:
                    setattr(value, "cellResponsible", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sipme_Task(EnterpriseProcessor):

    def __init__(self, taskDuration: int, Task: "sipme_Activity" = None, sipme_Task: "sipme_EnterpriseResource" = None, sipme_Task127: "sipme_BusinessRules" = None, tasks: "sipme_Activity" = None, sipme_Task133: "sipme_Task" = None, sipme_Task131: set["sipme_Task"] = None, sipme_Task114: "sipme_Role_Function" = None):
        self.taskDuration = taskDuration
        self.Task = Task
        self.sipme_Task = sipme_Task
        self.sipme_Task127 = sipme_Task127
        self.tasks = tasks
        self.sipme_Task133 = sipme_Task133
        self.sipme_Task131 = sipme_Task131 if sipme_Task131 is not None else set()
        self.sipme_Task114 = sipme_Task114
        
    @property
    def taskDuration(self) -> int:
        return self.__taskDuration

    @taskDuration.setter
    def taskDuration(self, taskDuration: int):
        self.__taskDuration = taskDuration

    @property
    def Task(self):
        return self.__Task

    @Task.setter
    def Task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Task__Task", None)
        self.__Task = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "taskOf"):
                opp_val = getattr(old_value, "taskOf", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "taskOf"):
                opp_val = getattr(value, "taskOf", None)
                if opp_val is None:
                    setattr(value, "taskOf", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sipme_Task114(self):
        return self.__sipme_Task114

    @sipme_Task114.setter
    def sipme_Task114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Task__sipme_Task114", None)
        self.__sipme_Task114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_Role_Function"):
                opp_val = getattr(old_value, "sipme_Role_Function", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_Role_Function"):
                opp_val = getattr(value, "sipme_Role_Function", None)
                if opp_val is None:
                    setattr(value, "sipme_Role_Function", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sipme_Task131(self):
        return self.__sipme_Task131

    @sipme_Task131.setter
    def sipme_Task131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Task__sipme_Task131", None)
        self.__sipme_Task131 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sipme_Task133"):
                    opp_val = getattr(item, "sipme_Task133", None)
                    
                    if opp_val == self:
                        setattr(item, "sipme_Task133", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sipme_Task133"):
                    opp_val = getattr(item, "sipme_Task133", None)
                    
                    setattr(item, "sipme_Task133", self)
                    

    @property
    def sipme_Task127(self):
        return self.__sipme_Task127

    @sipme_Task127.setter
    def sipme_Task127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Task__sipme_Task127", None)
        self.__sipme_Task127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_BusinessRules128"):
                opp_val = getattr(old_value, "sipme_BusinessRules128", None)
                if opp_val == self:
                    setattr(old_value, "sipme_BusinessRules128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_BusinessRules128"):
                opp_val = getattr(value, "sipme_BusinessRules128", None)
                setattr(value, "sipme_BusinessRules128", self)

    @property
    def sipme_Task(self):
        return self.__sipme_Task

    @sipme_Task.setter
    def sipme_Task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Task__sipme_Task", None)
        self.__sipme_Task = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_EnterpriseResource"):
                opp_val = getattr(old_value, "sipme_EnterpriseResource", None)
                if opp_val == self:
                    setattr(old_value, "sipme_EnterpriseResource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_EnterpriseResource"):
                opp_val = getattr(value, "sipme_EnterpriseResource", None)
                setattr(value, "sipme_EnterpriseResource", self)

    @property
    def tasks(self):
        return self.__tasks

    @tasks.setter
    def tasks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Task__tasks", None)
        self.__tasks = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Activity130"):
                opp_val = getattr(old_value, "Activity130", None)
                if opp_val == self:
                    setattr(old_value, "Activity130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Activity130"):
                opp_val = getattr(value, "Activity130", None)
                setattr(value, "Activity130", self)

    @property
    def sipme_Task133(self):
        return self.__sipme_Task133

    @sipme_Task133.setter
    def sipme_Task133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Task__sipme_Task133", None)
        self.__sipme_Task133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_Task131"):
                opp_val = getattr(old_value, "sipme_Task131", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_Task131"):
                opp_val = getattr(value, "sipme_Task131", None)
                if opp_val is None:
                    setattr(value, "sipme_Task131", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sipme_Activity(EnterpriseProcessor):

    def __init__(self, ActivityDuration: int, endingStatus: str, taskOf: set["sipme_Task"] = None, activities: "sipme_BusinessProcess" = None, Activity: "sipme_BusinessProcess" = None, Activity130: "sipme_Task" = None, sipme_Activity: "sipme_Requirement" = None):
        self.ActivityDuration = ActivityDuration
        self.endingStatus = endingStatus
        self.taskOf = taskOf if taskOf is not None else set()
        self.activities = activities
        self.Activity = Activity
        self.Activity130 = Activity130
        self.sipme_Activity = sipme_Activity
        
    @property
    def ActivityDuration(self) -> int:
        return self.__ActivityDuration

    @ActivityDuration.setter
    def ActivityDuration(self, ActivityDuration: int):
        self.__ActivityDuration = ActivityDuration

    @property
    def endingStatus(self) -> str:
        return self.__endingStatus

    @endingStatus.setter
    def endingStatus(self, endingStatus: str):
        self.__endingStatus = endingStatus

    @property
    def Activity(self):
        return self.__Activity

    @Activity.setter
    def Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Activity__Activity", None)
        self.__Activity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityOf"):
                opp_val = getattr(old_value, "activityOf", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityOf"):
                opp_val = getattr(value, "activityOf", None)
                if opp_val is None:
                    setattr(value, "activityOf", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def taskOf(self):
        return self.__taskOf

    @taskOf.setter
    def taskOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Activity__taskOf", None)
        self.__taskOf = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Task"):
                    opp_val = getattr(item, "Task", None)
                    
                    if opp_val == self:
                        setattr(item, "Task", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Task"):
                    opp_val = getattr(item, "Task", None)
                    
                    setattr(item, "Task", self)
                    

    @property
    def activities(self):
        return self.__activities

    @activities.setter
    def activities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Activity__activities", None)
        self.__activities = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BusinessProcess"):
                opp_val = getattr(old_value, "BusinessProcess", None)
                if opp_val == self:
                    setattr(old_value, "BusinessProcess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BusinessProcess"):
                opp_val = getattr(value, "BusinessProcess", None)
                setattr(value, "BusinessProcess", self)

    @property
    def sipme_Activity(self):
        return self.__sipme_Activity

    @sipme_Activity.setter
    def sipme_Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Activity__sipme_Activity", None)
        self.__sipme_Activity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sipme_Requirement112"):
                opp_val = getattr(old_value, "sipme_Requirement112", None)
                if opp_val == self:
                    setattr(old_value, "sipme_Requirement112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sipme_Requirement112"):
                opp_val = getattr(value, "sipme_Requirement112", None)
                setattr(value, "sipme_Requirement112", self)

    @property
    def Activity130(self):
        return self.__Activity130

    @Activity130.setter
    def Activity130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sipme_Activity__Activity130", None)
        self.__Activity130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tasks"):
                opp_val = getattr(old_value, "tasks", None)
                if opp_val == self:
                    setattr(old_value, "tasks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tasks"):
                opp_val = getattr(value, "tasks", None)
                setattr(value, "tasks", self)
