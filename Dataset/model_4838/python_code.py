from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PrincipleCategory(Enum):
    GuidingPrinciple = "GuidingPrinciple"
    BusinessPrinciple = "BusinessPrinciple"
    DataPrinciple = "DataPrinciple"
    ApplicationPrinciple = "ApplicationPrinciple"
    IntegrationPrinciple = "IntegrationPrinciple"
    TechnologyPrinciple = "TechnologyPrinciple"
class LifeCycleStatus(Enum):
    Proposed = "Proposed"
    InDevelopment = "InDevelopment"
    Live = "Live"
    PhasingOut = "PhasingOut"
    Retired = "Retired"
class WorkPackageCategory(Enum):
    WorkPackage = "WorkPackage"
    WorkStream = "WorkStream"
    Project = "Project"
    Program = "Program"
    Portofolio = "Portofolio"
class DataEntityCategory(Enum):
    Message = "Message"
    InternallyStoredEntity = "InternallyStoredEntity"
class StandardsClass(Enum):
    NonStandard = "NonStandard"
    Proposed = "Proposed"
    Provisional = "Provisional"
    Standard = "Standard"
    PhasingOut = "PhasingOut"
    Retired = "Retired"


############################################
# Definition of Classes
############################################

class contentfwk_Standard(ABC):

    def __init__(self, standardClass: str, standardCreationDate: date, lastStandardCreationDate: date, nextStandardCreationDate: date, retireDate: date):
        self.standardClass = standardClass
        self.standardCreationDate = standardCreationDate
        self.lastStandardCreationDate = lastStandardCreationDate
        self.nextStandardCreationDate = nextStandardCreationDate
        self.retireDate = retireDate
        
    @property
    def standardClass(self) -> str:
        return self.__standardClass

    @standardClass.setter
    def standardClass(self, standardClass: str):
        self.__standardClass = standardClass

    @property
    def lastStandardCreationDate(self) -> date:
        return self.__lastStandardCreationDate

    @lastStandardCreationDate.setter
    def lastStandardCreationDate(self, lastStandardCreationDate: date):
        self.__lastStandardCreationDate = lastStandardCreationDate

    @property
    def retireDate(self) -> date:
        return self.__retireDate

    @retireDate.setter
    def retireDate(self, retireDate: date):
        self.__retireDate = retireDate

    @property
    def nextStandardCreationDate(self) -> date:
        return self.__nextStandardCreationDate

    @nextStandardCreationDate.setter
    def nextStandardCreationDate(self, nextStandardCreationDate: date):
        self.__nextStandardCreationDate = nextStandardCreationDate

    @property
    def standardCreationDate(self) -> date:
        return self.__standardCreationDate

    @standardCreationDate.setter
    def standardCreationDate(self, standardCreationDate: date):
        self.__standardCreationDate = standardCreationDate

class DataComponent:

    pass
class StrategicElement:

    pass
class contentfwk_Assumption(StrategicElement):

    pass
class contentfwk_Requirement(StrategicElement):

    def __init__(self, statementOfRequirement: str, rationale: str, acceptanceCriteria: str):
        self.statementOfRequirement = statementOfRequirement
        self.rationale = rationale
        self.acceptanceCriteria = acceptanceCriteria
        
    @property
    def acceptanceCriteria(self) -> str:
        return self.__acceptanceCriteria

    @acceptanceCriteria.setter
    def acceptanceCriteria(self, acceptanceCriteria: str):
        self.__acceptanceCriteria = acceptanceCriteria

    @property
    def statementOfRequirement(self) -> str:
        return self.__statementOfRequirement

    @statementOfRequirement.setter
    def statementOfRequirement(self, statementOfRequirement: str):
        self.__statementOfRequirement = statementOfRequirement

    @property
    def rationale(self) -> str:
        return self.__rationale

    @rationale.setter
    def rationale(self, rationale: str):
        self.__rationale = rationale

class contentfwk_Gap(StrategicElement):

    pass
class contentfwk_Constraint(StrategicElement):

    pass
class contentfwk_Principle(StrategicElement):

    def __init__(self, principleCategory: str, priority: str, statementOfPrinciple: str, rationale: str, implication: str, metric: str):
        self.principleCategory = principleCategory
        self.priority = priority
        self.statementOfPrinciple = statementOfPrinciple
        self.rationale = rationale
        self.implication = implication
        self.metric = metric
        
    @property
    def statementOfPrinciple(self) -> str:
        return self.__statementOfPrinciple

    @statementOfPrinciple.setter
    def statementOfPrinciple(self, statementOfPrinciple: str):
        self.__statementOfPrinciple = statementOfPrinciple

    @property
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

    @property
    def rationale(self) -> str:
        return self.__rationale

    @rationale.setter
    def rationale(self, rationale: str):
        self.__rationale = rationale

    @property
    def implication(self) -> str:
        return self.__implication

    @implication.setter
    def implication(self, implication: str):
        self.__implication = implication

    @property
    def metric(self) -> str:
        return self.__metric

    @metric.setter
    def metric(self, metric: str):
        self.__metric = metric

    @property
    def principleCategory(self) -> str:
        return self.__principleCategory

    @principleCategory.setter
    def principleCategory(self, principleCategory: str):
        self.__principleCategory = principleCategory

class contentfwk_WorkPackage(StrategicElement):

    def __init__(self, workPackageCategory: str, WorkPackage: "contentfwk_Capability" = None, isDeliveredBy: set["contentfwk_Capability"] = None):
        self.workPackageCategory = workPackageCategory
        self.WorkPackage = WorkPackage
        self.isDeliveredBy = isDeliveredBy if isDeliveredBy is not None else set()
        
    @property
    def workPackageCategory(self) -> str:
        return self.__workPackageCategory

    @workPackageCategory.setter
    def workPackageCategory(self, workPackageCategory: str):
        self.__workPackageCategory = workPackageCategory

    @property
    def isDeliveredBy(self):
        return self.__isDeliveredBy

    @isDeliveredBy.setter
    def isDeliveredBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_WorkPackage__isDeliveredBy", None)
        self.__isDeliveredBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Capability"):
                    opp_val = getattr(item, "Capability", None)
                    
                    if opp_val == self:
                        setattr(item, "Capability", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Capability"):
                    opp_val = getattr(item, "Capability", None)
                    
                    setattr(item, "Capability", self)
                    

    @property
    def WorkPackage(self):
        return self.__WorkPackage

    @WorkPackage.setter
    def WorkPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_WorkPackage__WorkPackage", None)
        self.__WorkPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deliversCapabilities"):
                opp_val = getattr(old_value, "deliversCapabilities", None)
                if opp_val == self:
                    setattr(old_value, "deliversCapabilities", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deliversCapabilities"):
                opp_val = getattr(value, "deliversCapabilities", None)
                setattr(value, "deliversCapabilities", self)

class contentfwk_Element:

    def __init__(self, name: str, description: str, sourceDescr: str, ownerDescr: str, ID: str, Element: "contentfwk_Element" = None, isDelegatedBy: set["contentfwk_Element"] = None, Element232: "contentfwk_Element" = None, delegates: set["contentfwk_Element"] = None, Element243: "contentfwk_Label" = None, ownedElements: set["contentfwk_Label"] = None):
        self.name = name
        self.description = description
        self.sourceDescr = sourceDescr
        self.ownerDescr = ownerDescr
        self.ID = ID
        self.Element = Element
        self.isDelegatedBy = isDelegatedBy if isDelegatedBy is not None else set()
        self.Element232 = Element232
        self.delegates = delegates if delegates is not None else set()
        self.Element243 = Element243
        self.ownedElements = ownedElements if ownedElements is not None else set()
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def sourceDescr(self) -> str:
        return self.__sourceDescr

    @sourceDescr.setter
    def sourceDescr(self, sourceDescr: str):
        self.__sourceDescr = sourceDescr

    @property
    def ownerDescr(self) -> str:
        return self.__ownerDescr

    @ownerDescr.setter
    def ownerDescr(self, ownerDescr: str):
        self.__ownerDescr = ownerDescr

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def delegates(self):
        return self.__delegates

    @delegates.setter
    def delegates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Element__delegates", None)
        self.__delegates = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element232"):
                    opp_val = getattr(item, "Element232", None)
                    
                    if opp_val == self:
                        setattr(item, "Element232", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element232"):
                    opp_val = getattr(item, "Element232", None)
                    
                    setattr(item, "Element232", self)
                    

    @property
    def Element243(self):
        return self.__Element243

    @Element243.setter
    def Element243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Element__Element243", None)
        self.__Element243 = value
        
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

    @property
    def Element(self):
        return self.__Element

    @Element.setter
    def Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Element__Element", None)
        self.__Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isDelegatedBy"):
                opp_val = getattr(old_value, "isDelegatedBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isDelegatedBy"):
                opp_val = getattr(value, "isDelegatedBy", None)
                if opp_val is None:
                    setattr(value, "isDelegatedBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Element232(self):
        return self.__Element232

    @Element232.setter
    def Element232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Element__Element232", None)
        self.__Element232 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delegates"):
                opp_val = getattr(old_value, "delegates", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delegates"):
                opp_val = getattr(value, "delegates", None)
                if opp_val is None:
                    setattr(value, "delegates", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def isDelegatedBy(self):
        return self.__isDelegatedBy

    @isDelegatedBy.setter
    def isDelegatedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Element__isDelegatedBy", None)
        self.__isDelegatedBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    if opp_val == self:
                        setattr(item, "Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    setattr(item, "Element", self)
                    

    @property
    def ownedElements(self):
        return self.__ownedElements

    @ownedElements.setter
    def ownedElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Element__ownedElements", None)
        self.__ownedElements = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Label"):
                    opp_val = getattr(item, "Label", None)
                    
                    if opp_val == self:
                        setattr(item, "Label", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Label"):
                    opp_val = getattr(item, "Label", None)
                    
                    setattr(item, "Label", self)
                    

class TechnologyComponent:

    pass
class Service:

    pass
class Standard:

    pass
class contentfwk_ApplicationComponent(Standard):

    pass
class contentfwk_DataComponent(Standard):

    pass
class contentfwk_TechnologyComponent(Standard):

    pass
class ApplicationComponent:

    pass
class contentfwk_Service(Standard):

    pass
class Element:

    pass
class contentfwk_StrategicElement(Element):

    pass
class contentfwk_PlatformService(Service, Element):

    def __init__(self, categoryTRM: str, contentfwk_PlatformService: "contentfwk_TechnologyArchitecture" = None, suppliesPlatformServices: set["contentfwk_LogicalTechnologyComponent"] = None, PlatformService: "contentfwk_LogicalTechnologyComponent" = None):
        self.categoryTRM = categoryTRM
        self.contentfwk_PlatformService = contentfwk_PlatformService
        self.suppliesPlatformServices = suppliesPlatformServices if suppliesPlatformServices is not None else set()
        self.PlatformService = PlatformService
        
    @property
    def categoryTRM(self) -> str:
        return self.__categoryTRM

    @categoryTRM.setter
    def categoryTRM(self, categoryTRM: str):
        self.__categoryTRM = categoryTRM

    @property
    def contentfwk_PlatformService(self):
        return self.__contentfwk_PlatformService

    @contentfwk_PlatformService.setter
    def contentfwk_PlatformService(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PlatformService__contentfwk_PlatformService", None)
        self.__contentfwk_PlatformService = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_TechnologyArchitecture"):
                opp_val = getattr(old_value, "contentfwk_TechnologyArchitecture", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_TechnologyArchitecture"):
                opp_val = getattr(value, "contentfwk_TechnologyArchitecture", None)
                if opp_val is None:
                    setattr(value, "contentfwk_TechnologyArchitecture", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def suppliesPlatformServices(self):
        return self.__suppliesPlatformServices

    @suppliesPlatformServices.setter
    def suppliesPlatformServices(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PlatformService__suppliesPlatformServices", None)
        self.__suppliesPlatformServices = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LogicalTechnologyComponent"):
                    opp_val = getattr(item, "LogicalTechnologyComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "LogicalTechnologyComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LogicalTechnologyComponent"):
                    opp_val = getattr(item, "LogicalTechnologyComponent", None)
                    
                    setattr(item, "LogicalTechnologyComponent", self)
                    

    @property
    def PlatformService(self):
        return self.__PlatformService

    @PlatformService.setter
    def PlatformService(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PlatformService__PlatformService", None)
        self.__PlatformService = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isSuppliedByLogicalTechnologyComponents"):
                opp_val = getattr(old_value, "isSuppliedByLogicalTechnologyComponents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isSuppliedByLogicalTechnologyComponents"):
                opp_val = getattr(value, "isSuppliedByLogicalTechnologyComponents", None)
                if opp_val is None:
                    setattr(value, "isSuppliedByLogicalTechnologyComponents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class contentfwk_Capability(Element):

    def __init__(self, businessValue: str, increments: str, deliversCapabilities: "contentfwk_WorkPackage" = None, Capability: "contentfwk_WorkPackage" = None, contentfwk_Capability: "contentfwk_StrategicArchitecture" = None):
        self.businessValue = businessValue
        self.increments = increments
        self.deliversCapabilities = deliversCapabilities
        self.Capability = Capability
        self.contentfwk_Capability = contentfwk_Capability
        
    @property
    def increments(self) -> str:
        return self.__increments

    @increments.setter
    def increments(self, increments: str):
        self.__increments = increments

    @property
    def businessValue(self) -> str:
        return self.__businessValue

    @businessValue.setter
    def businessValue(self, businessValue: str):
        self.__businessValue = businessValue

    @property
    def contentfwk_Capability(self):
        return self.__contentfwk_Capability

    @contentfwk_Capability.setter
    def contentfwk_Capability(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Capability__contentfwk_Capability", None)
        self.__contentfwk_Capability = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_StrategicArchitecture"):
                opp_val = getattr(old_value, "contentfwk_StrategicArchitecture", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_StrategicArchitecture"):
                opp_val = getattr(value, "contentfwk_StrategicArchitecture", None)
                if opp_val is None:
                    setattr(value, "contentfwk_StrategicArchitecture", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def deliversCapabilities(self):
        return self.__deliversCapabilities

    @deliversCapabilities.setter
    def deliversCapabilities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Capability__deliversCapabilities", None)
        self.__deliversCapabilities = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorkPackage"):
                opp_val = getattr(old_value, "WorkPackage", None)
                if opp_val == self:
                    setattr(old_value, "WorkPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkPackage"):
                opp_val = getattr(value, "WorkPackage", None)
                setattr(value, "WorkPackage", self)

    @property
    def Capability(self):
        return self.__Capability

    @Capability.setter
    def Capability(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Capability__Capability", None)
        self.__Capability = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isDeliveredBy"):
                opp_val = getattr(old_value, "isDeliveredBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isDeliveredBy"):
                opp_val = getattr(value, "isDeliveredBy", None)
                if opp_val is None:
                    setattr(value, "isDeliveredBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class contentfwk_LogicalApplicationComponent(Element, ApplicationComponent):

    pass
class contentfwk_PhysicalApplicationComponent(Element, ApplicationComponent):

    def __init__(self, lifeCycleStatus: str, initialLiveDate: date, dateOfLastRelease: date, dateOfNextRelease: date, retirementDate: date, availabilityQualityCharacteristics: str, servicesTimes: str, manageabilityCharacteristics: str, serviceabilityCharacteristics: str, performanceCharacteristics: str, reliabilityCharacteristics: str, recoverabilityCharacteristics: str, locatabilityCharacteristics: str, securityCharacteristics: str, privacyCharacteristics: str, integrityCharacteristics: str, credibilityCharacteristics: str, localizationCharacteristics: str, internationalizationCharacteristics: str, interoperabilityCharacteristics: str, scalabilityCharacteristics: str, portabilityCharacteristics: str, extensibilityCharacteristics: str, capacityCharacteristics: str, throughput: str, throughputPeriod: str, growth: str, growthPeriod: str, peakProfileShortTerm: str, peakProfileLongTerm: str, PhysicalApplicationComponent: "contentfwk_LogicalApplicationComponent" = None, contentfwk_PhysicalApplicationComponent: "contentfwk_PhysicalTechnologyComponent" = None, PhysicalApplicationComponent252: "contentfwk_Location" = None, contentfwk_PhysicalApplicationComponent273: "contentfwk_PhysicalDataComponent" = None, contentfwk_PhysicalApplicationComponent278: "contentfwk_ApplicationArchitecture" = None, isExtendedByPhysicalApplicationComponents: set["contentfwk_LogicalApplicationComponent"] = None, containsPhysicalApplicationComponents: set["contentfwk_Location"] = None, contentfwk_PhysicalApplicationComponent287: "contentfwk_PhysicalApplicationComponent" = None, contentfwk_PhysicalApplicationComponent285: set["contentfwk_PhysicalApplicationComponent"] = None, contentfwk_PhysicalApplicationComponent289: set["contentfwk_PhysicalDataComponent"] = None, contentfwk_PhysicalApplicationComponent292: set["contentfwk_PhysicalTechnologyComponent"] = None, contentfwk_PhysicalApplicationComponent296: "contentfwk_PhysicalApplicationComponent" = None, contentfwk_PhysicalApplicationComponent294: "contentfwk_PhysicalApplicationComponent" = None):
        self.lifeCycleStatus = lifeCycleStatus
        self.initialLiveDate = initialLiveDate
        self.dateOfLastRelease = dateOfLastRelease
        self.dateOfNextRelease = dateOfNextRelease
        self.retirementDate = retirementDate
        self.availabilityQualityCharacteristics = availabilityQualityCharacteristics
        self.servicesTimes = servicesTimes
        self.manageabilityCharacteristics = manageabilityCharacteristics
        self.serviceabilityCharacteristics = serviceabilityCharacteristics
        self.performanceCharacteristics = performanceCharacteristics
        self.reliabilityCharacteristics = reliabilityCharacteristics
        self.recoverabilityCharacteristics = recoverabilityCharacteristics
        self.locatabilityCharacteristics = locatabilityCharacteristics
        self.securityCharacteristics = securityCharacteristics
        self.privacyCharacteristics = privacyCharacteristics
        self.integrityCharacteristics = integrityCharacteristics
        self.credibilityCharacteristics = credibilityCharacteristics
        self.localizationCharacteristics = localizationCharacteristics
        self.internationalizationCharacteristics = internationalizationCharacteristics
        self.interoperabilityCharacteristics = interoperabilityCharacteristics
        self.scalabilityCharacteristics = scalabilityCharacteristics
        self.portabilityCharacteristics = portabilityCharacteristics
        self.extensibilityCharacteristics = extensibilityCharacteristics
        self.capacityCharacteristics = capacityCharacteristics
        self.throughput = throughput
        self.throughputPeriod = throughputPeriod
        self.growth = growth
        self.growthPeriod = growthPeriod
        self.peakProfileShortTerm = peakProfileShortTerm
        self.peakProfileLongTerm = peakProfileLongTerm
        self.PhysicalApplicationComponent = PhysicalApplicationComponent
        self.contentfwk_PhysicalApplicationComponent = contentfwk_PhysicalApplicationComponent
        self.PhysicalApplicationComponent252 = PhysicalApplicationComponent252
        self.contentfwk_PhysicalApplicationComponent273 = contentfwk_PhysicalApplicationComponent273
        self.contentfwk_PhysicalApplicationComponent278 = contentfwk_PhysicalApplicationComponent278
        self.isExtendedByPhysicalApplicationComponents = isExtendedByPhysicalApplicationComponents if isExtendedByPhysicalApplicationComponents is not None else set()
        self.containsPhysicalApplicationComponents = containsPhysicalApplicationComponents if containsPhysicalApplicationComponents is not None else set()
        self.contentfwk_PhysicalApplicationComponent287 = contentfwk_PhysicalApplicationComponent287
        self.contentfwk_PhysicalApplicationComponent285 = contentfwk_PhysicalApplicationComponent285 if contentfwk_PhysicalApplicationComponent285 is not None else set()
        self.contentfwk_PhysicalApplicationComponent289 = contentfwk_PhysicalApplicationComponent289 if contentfwk_PhysicalApplicationComponent289 is not None else set()
        self.contentfwk_PhysicalApplicationComponent292 = contentfwk_PhysicalApplicationComponent292 if contentfwk_PhysicalApplicationComponent292 is not None else set()
        self.contentfwk_PhysicalApplicationComponent296 = contentfwk_PhysicalApplicationComponent296
        self.contentfwk_PhysicalApplicationComponent294 = contentfwk_PhysicalApplicationComponent294
        
    @property
    def growthPeriod(self) -> str:
        return self.__growthPeriod

    @growthPeriod.setter
    def growthPeriod(self, growthPeriod: str):
        self.__growthPeriod = growthPeriod

    @property
    def privacyCharacteristics(self) -> str:
        return self.__privacyCharacteristics

    @privacyCharacteristics.setter
    def privacyCharacteristics(self, privacyCharacteristics: str):
        self.__privacyCharacteristics = privacyCharacteristics

    @property
    def peakProfileShortTerm(self) -> str:
        return self.__peakProfileShortTerm

    @peakProfileShortTerm.setter
    def peakProfileShortTerm(self, peakProfileShortTerm: str):
        self.__peakProfileShortTerm = peakProfileShortTerm

    @property
    def extensibilityCharacteristics(self) -> str:
        return self.__extensibilityCharacteristics

    @extensibilityCharacteristics.setter
    def extensibilityCharacteristics(self, extensibilityCharacteristics: str):
        self.__extensibilityCharacteristics = extensibilityCharacteristics

    @property
    def manageabilityCharacteristics(self) -> str:
        return self.__manageabilityCharacteristics

    @manageabilityCharacteristics.setter
    def manageabilityCharacteristics(self, manageabilityCharacteristics: str):
        self.__manageabilityCharacteristics = manageabilityCharacteristics

    @property
    def internationalizationCharacteristics(self) -> str:
        return self.__internationalizationCharacteristics

    @internationalizationCharacteristics.setter
    def internationalizationCharacteristics(self, internationalizationCharacteristics: str):
        self.__internationalizationCharacteristics = internationalizationCharacteristics

    @property
    def portabilityCharacteristics(self) -> str:
        return self.__portabilityCharacteristics

    @portabilityCharacteristics.setter
    def portabilityCharacteristics(self, portabilityCharacteristics: str):
        self.__portabilityCharacteristics = portabilityCharacteristics

    @property
    def lifeCycleStatus(self) -> str:
        return self.__lifeCycleStatus

    @lifeCycleStatus.setter
    def lifeCycleStatus(self, lifeCycleStatus: str):
        self.__lifeCycleStatus = lifeCycleStatus

    @property
    def growth(self) -> str:
        return self.__growth

    @growth.setter
    def growth(self, growth: str):
        self.__growth = growth

    @property
    def interoperabilityCharacteristics(self) -> str:
        return self.__interoperabilityCharacteristics

    @interoperabilityCharacteristics.setter
    def interoperabilityCharacteristics(self, interoperabilityCharacteristics: str):
        self.__interoperabilityCharacteristics = interoperabilityCharacteristics

    @property
    def throughputPeriod(self) -> str:
        return self.__throughputPeriod

    @throughputPeriod.setter
    def throughputPeriod(self, throughputPeriod: str):
        self.__throughputPeriod = throughputPeriod

    @property
    def retirementDate(self) -> date:
        return self.__retirementDate

    @retirementDate.setter
    def retirementDate(self, retirementDate: date):
        self.__retirementDate = retirementDate

    @property
    def securityCharacteristics(self) -> str:
        return self.__securityCharacteristics

    @securityCharacteristics.setter
    def securityCharacteristics(self, securityCharacteristics: str):
        self.__securityCharacteristics = securityCharacteristics

    @property
    def localizationCharacteristics(self) -> str:
        return self.__localizationCharacteristics

    @localizationCharacteristics.setter
    def localizationCharacteristics(self, localizationCharacteristics: str):
        self.__localizationCharacteristics = localizationCharacteristics

    @property
    def availabilityQualityCharacteristics(self) -> str:
        return self.__availabilityQualityCharacteristics

    @availabilityQualityCharacteristics.setter
    def availabilityQualityCharacteristics(self, availabilityQualityCharacteristics: str):
        self.__availabilityQualityCharacteristics = availabilityQualityCharacteristics

    @property
    def recoverabilityCharacteristics(self) -> str:
        return self.__recoverabilityCharacteristics

    @recoverabilityCharacteristics.setter
    def recoverabilityCharacteristics(self, recoverabilityCharacteristics: str):
        self.__recoverabilityCharacteristics = recoverabilityCharacteristics

    @property
    def dateOfLastRelease(self) -> date:
        return self.__dateOfLastRelease

    @dateOfLastRelease.setter
    def dateOfLastRelease(self, dateOfLastRelease: date):
        self.__dateOfLastRelease = dateOfLastRelease

    @property
    def dateOfNextRelease(self) -> date:
        return self.__dateOfNextRelease

    @dateOfNextRelease.setter
    def dateOfNextRelease(self, dateOfNextRelease: date):
        self.__dateOfNextRelease = dateOfNextRelease

    @property
    def reliabilityCharacteristics(self) -> str:
        return self.__reliabilityCharacteristics

    @reliabilityCharacteristics.setter
    def reliabilityCharacteristics(self, reliabilityCharacteristics: str):
        self.__reliabilityCharacteristics = reliabilityCharacteristics

    @property
    def peakProfileLongTerm(self) -> str:
        return self.__peakProfileLongTerm

    @peakProfileLongTerm.setter
    def peakProfileLongTerm(self, peakProfileLongTerm: str):
        self.__peakProfileLongTerm = peakProfileLongTerm

    @property
    def initialLiveDate(self) -> date:
        return self.__initialLiveDate

    @initialLiveDate.setter
    def initialLiveDate(self, initialLiveDate: date):
        self.__initialLiveDate = initialLiveDate

    @property
    def integrityCharacteristics(self) -> str:
        return self.__integrityCharacteristics

    @integrityCharacteristics.setter
    def integrityCharacteristics(self, integrityCharacteristics: str):
        self.__integrityCharacteristics = integrityCharacteristics

    @property
    def locatabilityCharacteristics(self) -> str:
        return self.__locatabilityCharacteristics

    @locatabilityCharacteristics.setter
    def locatabilityCharacteristics(self, locatabilityCharacteristics: str):
        self.__locatabilityCharacteristics = locatabilityCharacteristics

    @property
    def scalabilityCharacteristics(self) -> str:
        return self.__scalabilityCharacteristics

    @scalabilityCharacteristics.setter
    def scalabilityCharacteristics(self, scalabilityCharacteristics: str):
        self.__scalabilityCharacteristics = scalabilityCharacteristics

    @property
    def performanceCharacteristics(self) -> str:
        return self.__performanceCharacteristics

    @performanceCharacteristics.setter
    def performanceCharacteristics(self, performanceCharacteristics: str):
        self.__performanceCharacteristics = performanceCharacteristics

    @property
    def serviceabilityCharacteristics(self) -> str:
        return self.__serviceabilityCharacteristics

    @serviceabilityCharacteristics.setter
    def serviceabilityCharacteristics(self, serviceabilityCharacteristics: str):
        self.__serviceabilityCharacteristics = serviceabilityCharacteristics

    @property
    def credibilityCharacteristics(self) -> str:
        return self.__credibilityCharacteristics

    @credibilityCharacteristics.setter
    def credibilityCharacteristics(self, credibilityCharacteristics: str):
        self.__credibilityCharacteristics = credibilityCharacteristics

    @property
    def servicesTimes(self) -> str:
        return self.__servicesTimes

    @servicesTimes.setter
    def servicesTimes(self, servicesTimes: str):
        self.__servicesTimes = servicesTimes

    @property
    def throughput(self) -> str:
        return self.__throughput

    @throughput.setter
    def throughput(self, throughput: str):
        self.__throughput = throughput

    @property
    def capacityCharacteristics(self) -> str:
        return self.__capacityCharacteristics

    @capacityCharacteristics.setter
    def capacityCharacteristics(self, capacityCharacteristics: str):
        self.__capacityCharacteristics = capacityCharacteristics

    @property
    def contentfwk_PhysicalApplicationComponent292(self):
        return self.__contentfwk_PhysicalApplicationComponent292

    @contentfwk_PhysicalApplicationComponent292.setter
    def contentfwk_PhysicalApplicationComponent292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent292", None)
        self.__contentfwk_PhysicalApplicationComponent292 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_PhysicalTechnologyComponent293"):
                    opp_val = getattr(item, "contentfwk_PhysicalTechnologyComponent293", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_PhysicalTechnologyComponent293", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_PhysicalTechnologyComponent293"):
                    opp_val = getattr(item, "contentfwk_PhysicalTechnologyComponent293", None)
                    
                    setattr(item, "contentfwk_PhysicalTechnologyComponent293", self)
                    

    @property
    def PhysicalApplicationComponent(self):
        return self.__PhysicalApplicationComponent

    @PhysicalApplicationComponent.setter
    def PhysicalApplicationComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__PhysicalApplicationComponent", None)
        self.__PhysicalApplicationComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendsLogicalApplicationComponents"):
                opp_val = getattr(old_value, "extendsLogicalApplicationComponents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendsLogicalApplicationComponents"):
                opp_val = getattr(value, "extendsLogicalApplicationComponents", None)
                if opp_val is None:
                    setattr(value, "extendsLogicalApplicationComponents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def isExtendedByPhysicalApplicationComponents(self):
        return self.__isExtendedByPhysicalApplicationComponents

    @isExtendedByPhysicalApplicationComponents.setter
    def isExtendedByPhysicalApplicationComponents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__isExtendedByPhysicalApplicationComponents", None)
        self.__isExtendedByPhysicalApplicationComponents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LogicalApplicationComponent282"):
                    opp_val = getattr(item, "LogicalApplicationComponent282", None)
                    
                    if opp_val == self:
                        setattr(item, "LogicalApplicationComponent282", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LogicalApplicationComponent282"):
                    opp_val = getattr(item, "LogicalApplicationComponent282", None)
                    
                    setattr(item, "LogicalApplicationComponent282", self)
                    

    @property
    def contentfwk_PhysicalApplicationComponent273(self):
        return self.__contentfwk_PhysicalApplicationComponent273

    @contentfwk_PhysicalApplicationComponent273.setter
    def contentfwk_PhysicalApplicationComponent273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent273", None)
        self.__contentfwk_PhysicalApplicationComponent273 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalDataComponent272"):
                opp_val = getattr(old_value, "contentfwk_PhysicalDataComponent272", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalDataComponent272"):
                opp_val = getattr(value, "contentfwk_PhysicalDataComponent272", None)
                if opp_val is None:
                    setattr(value, "contentfwk_PhysicalDataComponent272", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_PhysicalApplicationComponent278(self):
        return self.__contentfwk_PhysicalApplicationComponent278

    @contentfwk_PhysicalApplicationComponent278.setter
    def contentfwk_PhysicalApplicationComponent278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent278", None)
        self.__contentfwk_PhysicalApplicationComponent278 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_ApplicationArchitecture277"):
                opp_val = getattr(old_value, "contentfwk_ApplicationArchitecture277", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_ApplicationArchitecture277"):
                opp_val = getattr(value, "contentfwk_ApplicationArchitecture277", None)
                if opp_val is None:
                    setattr(value, "contentfwk_ApplicationArchitecture277", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_PhysicalApplicationComponent289(self):
        return self.__contentfwk_PhysicalApplicationComponent289

    @contentfwk_PhysicalApplicationComponent289.setter
    def contentfwk_PhysicalApplicationComponent289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent289", None)
        self.__contentfwk_PhysicalApplicationComponent289 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_PhysicalDataComponent290"):
                    opp_val = getattr(item, "contentfwk_PhysicalDataComponent290", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_PhysicalDataComponent290", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_PhysicalDataComponent290"):
                    opp_val = getattr(item, "contentfwk_PhysicalDataComponent290", None)
                    
                    setattr(item, "contentfwk_PhysicalDataComponent290", self)
                    

    @property
    def contentfwk_PhysicalApplicationComponent287(self):
        return self.__contentfwk_PhysicalApplicationComponent287

    @contentfwk_PhysicalApplicationComponent287.setter
    def contentfwk_PhysicalApplicationComponent287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent287", None)
        self.__contentfwk_PhysicalApplicationComponent287 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalApplicationComponent285"):
                opp_val = getattr(old_value, "contentfwk_PhysicalApplicationComponent285", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalApplicationComponent285"):
                opp_val = getattr(value, "contentfwk_PhysicalApplicationComponent285", None)
                if opp_val is None:
                    setattr(value, "contentfwk_PhysicalApplicationComponent285", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PhysicalApplicationComponent252(self):
        return self.__PhysicalApplicationComponent252

    @PhysicalApplicationComponent252.setter
    def PhysicalApplicationComponent252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__PhysicalApplicationComponent252", None)
        self.__PhysicalApplicationComponent252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isHostedInLocation"):
                opp_val = getattr(old_value, "isHostedInLocation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isHostedInLocation"):
                opp_val = getattr(value, "isHostedInLocation", None)
                if opp_val is None:
                    setattr(value, "isHostedInLocation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_PhysicalApplicationComponent294(self):
        return self.__contentfwk_PhysicalApplicationComponent294

    @contentfwk_PhysicalApplicationComponent294.setter
    def contentfwk_PhysicalApplicationComponent294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent294", None)
        self.__contentfwk_PhysicalApplicationComponent294 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalApplicationComponent296"):
                opp_val = getattr(old_value, "contentfwk_PhysicalApplicationComponent296", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_PhysicalApplicationComponent296", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalApplicationComponent296"):
                opp_val = getattr(value, "contentfwk_PhysicalApplicationComponent296", None)
                setattr(value, "contentfwk_PhysicalApplicationComponent296", self)

    @property
    def contentfwk_PhysicalApplicationComponent(self):
        return self.__contentfwk_PhysicalApplicationComponent

    @contentfwk_PhysicalApplicationComponent.setter
    def contentfwk_PhysicalApplicationComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent", None)
        self.__contentfwk_PhysicalApplicationComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalTechnologyComponent183"):
                opp_val = getattr(old_value, "contentfwk_PhysicalTechnologyComponent183", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalTechnologyComponent183"):
                opp_val = getattr(value, "contentfwk_PhysicalTechnologyComponent183", None)
                if opp_val is None:
                    setattr(value, "contentfwk_PhysicalTechnologyComponent183", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def containsPhysicalApplicationComponents(self):
        return self.__containsPhysicalApplicationComponents

    @containsPhysicalApplicationComponents.setter
    def containsPhysicalApplicationComponents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__containsPhysicalApplicationComponents", None)
        self.__containsPhysicalApplicationComponents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Location284"):
                    opp_val = getattr(item, "Location284", None)
                    
                    if opp_val == self:
                        setattr(item, "Location284", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Location284"):
                    opp_val = getattr(item, "Location284", None)
                    
                    setattr(item, "Location284", self)
                    

    @property
    def contentfwk_PhysicalApplicationComponent296(self):
        return self.__contentfwk_PhysicalApplicationComponent296

    @contentfwk_PhysicalApplicationComponent296.setter
    def contentfwk_PhysicalApplicationComponent296(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent296", None)
        self.__contentfwk_PhysicalApplicationComponent296 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalApplicationComponent294"):
                opp_val = getattr(old_value, "contentfwk_PhysicalApplicationComponent294", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_PhysicalApplicationComponent294", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalApplicationComponent294"):
                opp_val = getattr(value, "contentfwk_PhysicalApplicationComponent294", None)
                setattr(value, "contentfwk_PhysicalApplicationComponent294", self)

    @property
    def contentfwk_PhysicalApplicationComponent285(self):
        return self.__contentfwk_PhysicalApplicationComponent285

    @contentfwk_PhysicalApplicationComponent285.setter
    def contentfwk_PhysicalApplicationComponent285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent285", None)
        self.__contentfwk_PhysicalApplicationComponent285 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_PhysicalApplicationComponent287"):
                    opp_val = getattr(item, "contentfwk_PhysicalApplicationComponent287", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_PhysicalApplicationComponent287", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_PhysicalApplicationComponent287"):
                    opp_val = getattr(item, "contentfwk_PhysicalApplicationComponent287", None)
                    
                    setattr(item, "contentfwk_PhysicalApplicationComponent287", self)
                    

class contentfwk_PhysicalDataComponent(Element, DataComponent):

    pass
class contentfwk_ServiceQuality(Element):

    pass
class contentfwk_InformationSystemService(Service, Element):

    pass
class contentfwk_DataEntity(Element):

    def __init__(self, dataEntityCategory: str, privacyClassification: str, retentionClassification: str, contentfwk_DataEntity: "contentfwk_DataArchitecture" = None, DataEntity: "contentfwk_Actor" = None, DataEntity72: "contentfwk_Actor" = None, consumesEntities: set["contentfwk_Actor"] = None, consumesEntities105: set["contentfwk_Service"] = None, providesEntities: set["contentfwk_Service"] = None, encapsulatesDataEntities: "contentfwk_LogicalDataComponent" = None, operatesOnDataEntities: set["contentfwk_LogicalApplicationComponent"] = None, suppliesEntities: set["contentfwk_Actor"] = None, DataEntity120: "contentfwk_LogicalApplicationComponent" = None, contentfwk_DataEntity113: "contentfwk_DataEntity" = None, contentfwk_DataEntity111: "contentfwk_DataEntity" = None, contentfwk_DataEntity116: "contentfwk_DataEntity" = None, contentfwk_DataEntity114: set["contentfwk_DataEntity"] = None, DataEntity261: "contentfwk_LogicalDataComponent" = None, DataEntity317: "contentfwk_Service" = None, DataEntity319: "contentfwk_Service" = None):
        self.dataEntityCategory = dataEntityCategory
        self.privacyClassification = privacyClassification
        self.retentionClassification = retentionClassification
        self.contentfwk_DataEntity = contentfwk_DataEntity
        self.DataEntity = DataEntity
        self.DataEntity72 = DataEntity72
        self.consumesEntities = consumesEntities if consumesEntities is not None else set()
        self.consumesEntities105 = consumesEntities105 if consumesEntities105 is not None else set()
        self.providesEntities = providesEntities if providesEntities is not None else set()
        self.encapsulatesDataEntities = encapsulatesDataEntities
        self.operatesOnDataEntities = operatesOnDataEntities if operatesOnDataEntities is not None else set()
        self.suppliesEntities = suppliesEntities if suppliesEntities is not None else set()
        self.DataEntity120 = DataEntity120
        self.contentfwk_DataEntity113 = contentfwk_DataEntity113
        self.contentfwk_DataEntity111 = contentfwk_DataEntity111
        self.contentfwk_DataEntity116 = contentfwk_DataEntity116
        self.contentfwk_DataEntity114 = contentfwk_DataEntity114 if contentfwk_DataEntity114 is not None else set()
        self.DataEntity261 = DataEntity261
        self.DataEntity317 = DataEntity317
        self.DataEntity319 = DataEntity319
        
    @property
    def privacyClassification(self) -> str:
        return self.__privacyClassification

    @privacyClassification.setter
    def privacyClassification(self, privacyClassification: str):
        self.__privacyClassification = privacyClassification

    @property
    def retentionClassification(self) -> str:
        return self.__retentionClassification

    @retentionClassification.setter
    def retentionClassification(self, retentionClassification: str):
        self.__retentionClassification = retentionClassification

    @property
    def dataEntityCategory(self) -> str:
        return self.__dataEntityCategory

    @dataEntityCategory.setter
    def dataEntityCategory(self, dataEntityCategory: str):
        self.__dataEntityCategory = dataEntityCategory

    @property
    def consumesEntities105(self):
        return self.__consumesEntities105

    @consumesEntities105.setter
    def consumesEntities105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__consumesEntities105", None)
        self.__consumesEntities105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service106"):
                    opp_val = getattr(item, "Service106", None)
                    
                    if opp_val == self:
                        setattr(item, "Service106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service106"):
                    opp_val = getattr(item, "Service106", None)
                    
                    setattr(item, "Service106", self)
                    

    @property
    def contentfwk_DataEntity114(self):
        return self.__contentfwk_DataEntity114

    @contentfwk_DataEntity114.setter
    def contentfwk_DataEntity114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__contentfwk_DataEntity114", None)
        self.__contentfwk_DataEntity114 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_DataEntity116"):
                    opp_val = getattr(item, "contentfwk_DataEntity116", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_DataEntity116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_DataEntity116"):
                    opp_val = getattr(item, "contentfwk_DataEntity116", None)
                    
                    setattr(item, "contentfwk_DataEntity116", self)
                    

    @property
    def contentfwk_DataEntity111(self):
        return self.__contentfwk_DataEntity111

    @contentfwk_DataEntity111.setter
    def contentfwk_DataEntity111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__contentfwk_DataEntity111", None)
        self.__contentfwk_DataEntity111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_DataEntity113"):
                opp_val = getattr(old_value, "contentfwk_DataEntity113", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_DataEntity113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_DataEntity113"):
                opp_val = getattr(value, "contentfwk_DataEntity113", None)
                setattr(value, "contentfwk_DataEntity113", self)

    @property
    def contentfwk_DataEntity113(self):
        return self.__contentfwk_DataEntity113

    @contentfwk_DataEntity113.setter
    def contentfwk_DataEntity113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__contentfwk_DataEntity113", None)
        self.__contentfwk_DataEntity113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_DataEntity111"):
                opp_val = getattr(old_value, "contentfwk_DataEntity111", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_DataEntity111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_DataEntity111"):
                opp_val = getattr(value, "contentfwk_DataEntity111", None)
                setattr(value, "contentfwk_DataEntity111", self)

    @property
    def providesEntities(self):
        return self.__providesEntities

    @providesEntities.setter
    def providesEntities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__providesEntities", None)
        self.__providesEntities = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service108"):
                    opp_val = getattr(item, "Service108", None)
                    
                    if opp_val == self:
                        setattr(item, "Service108", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service108"):
                    opp_val = getattr(item, "Service108", None)
                    
                    setattr(item, "Service108", self)
                    

    @property
    def encapsulatesDataEntities(self):
        return self.__encapsulatesDataEntities

    @encapsulatesDataEntities.setter
    def encapsulatesDataEntities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__encapsulatesDataEntities", None)
        self.__encapsulatesDataEntities = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LogicalDataComponent"):
                opp_val = getattr(old_value, "LogicalDataComponent", None)
                if opp_val == self:
                    setattr(old_value, "LogicalDataComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LogicalDataComponent"):
                opp_val = getattr(value, "LogicalDataComponent", None)
                setattr(value, "LogicalDataComponent", self)

    @property
    def DataEntity317(self):
        return self.__DataEntity317

    @DataEntity317.setter
    def DataEntity317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__DataEntity317", None)
        self.__DataEntity317 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isUpdatedThroughServices"):
                opp_val = getattr(old_value, "isUpdatedThroughServices", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isUpdatedThroughServices"):
                opp_val = getattr(value, "isUpdatedThroughServices", None)
                if opp_val is None:
                    setattr(value, "isUpdatedThroughServices", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DataEntity261(self):
        return self.__DataEntity261

    @DataEntity261.setter
    def DataEntity261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__DataEntity261", None)
        self.__DataEntity261 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "residesWithinLogicalDataComponent"):
                opp_val = getattr(old_value, "residesWithinLogicalDataComponent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "residesWithinLogicalDataComponent"):
                opp_val = getattr(value, "residesWithinLogicalDataComponent", None)
                if opp_val is None:
                    setattr(value, "residesWithinLogicalDataComponent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DataEntity72(self):
        return self.__DataEntity72

    @DataEntity72.setter
    def DataEntity72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__DataEntity72", None)
        self.__DataEntity72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isConsumedByActors"):
                opp_val = getattr(old_value, "isConsumedByActors", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isConsumedByActors"):
                opp_val = getattr(value, "isConsumedByActors", None)
                if opp_val is None:
                    setattr(value, "isConsumedByActors", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def operatesOnDataEntities(self):
        return self.__operatesOnDataEntities

    @operatesOnDataEntities.setter
    def operatesOnDataEntities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__operatesOnDataEntities", None)
        self.__operatesOnDataEntities = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LogicalApplicationComponent"):
                    opp_val = getattr(item, "LogicalApplicationComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "LogicalApplicationComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LogicalApplicationComponent"):
                    opp_val = getattr(item, "LogicalApplicationComponent", None)
                    
                    setattr(item, "LogicalApplicationComponent", self)
                    

    @property
    def consumesEntities(self):
        return self.__consumesEntities

    @consumesEntities.setter
    def consumesEntities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__consumesEntities", None)
        self.__consumesEntities = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Actor103"):
                    opp_val = getattr(item, "Actor103", None)
                    
                    if opp_val == self:
                        setattr(item, "Actor103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Actor103"):
                    opp_val = getattr(item, "Actor103", None)
                    
                    setattr(item, "Actor103", self)
                    

    @property
    def suppliesEntities(self):
        return self.__suppliesEntities

    @suppliesEntities.setter
    def suppliesEntities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__suppliesEntities", None)
        self.__suppliesEntities = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Actor101"):
                    opp_val = getattr(item, "Actor101", None)
                    
                    if opp_val == self:
                        setattr(item, "Actor101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Actor101"):
                    opp_val = getattr(item, "Actor101", None)
                    
                    setattr(item, "Actor101", self)
                    

    @property
    def DataEntity319(self):
        return self.__DataEntity319

    @DataEntity319.setter
    def DataEntity319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__DataEntity319", None)
        self.__DataEntity319 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isAccessedByServices"):
                opp_val = getattr(old_value, "isAccessedByServices", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isAccessedByServices"):
                opp_val = getattr(value, "isAccessedByServices", None)
                if opp_val is None:
                    setattr(value, "isAccessedByServices", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DataEntity(self):
        return self.__DataEntity

    @DataEntity.setter
    def DataEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__DataEntity", None)
        self.__DataEntity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isSuppliedByActors"):
                opp_val = getattr(old_value, "isSuppliedByActors", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isSuppliedByActors"):
                opp_val = getattr(value, "isSuppliedByActors", None)
                if opp_val is None:
                    setattr(value, "isSuppliedByActors", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_DataEntity116(self):
        return self.__contentfwk_DataEntity116

    @contentfwk_DataEntity116.setter
    def contentfwk_DataEntity116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__contentfwk_DataEntity116", None)
        self.__contentfwk_DataEntity116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_DataEntity114"):
                opp_val = getattr(old_value, "contentfwk_DataEntity114", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_DataEntity114"):
                opp_val = getattr(value, "contentfwk_DataEntity114", None)
                if opp_val is None:
                    setattr(value, "contentfwk_DataEntity114", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_DataEntity(self):
        return self.__contentfwk_DataEntity

    @contentfwk_DataEntity.setter
    def contentfwk_DataEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__contentfwk_DataEntity", None)
        self.__contentfwk_DataEntity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_DataArchitecture"):
                opp_val = getattr(old_value, "contentfwk_DataArchitecture", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_DataArchitecture"):
                opp_val = getattr(value, "contentfwk_DataArchitecture", None)
                if opp_val is None:
                    setattr(value, "contentfwk_DataArchitecture", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DataEntity120(self):
        return self.__DataEntity120

    @DataEntity120.setter
    def DataEntity120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__DataEntity120", None)
        self.__DataEntity120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isProcessesByLogicalApplicationComponents"):
                opp_val = getattr(old_value, "isProcessesByLogicalApplicationComponents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isProcessesByLogicalApplicationComponents"):
                opp_val = getattr(value, "isProcessesByLogicalApplicationComponents", None)
                if opp_val is None:
                    setattr(value, "isProcessesByLogicalApplicationComponents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class contentfwk_LogicalDataComponent(Element, DataComponent):

    pass
class contentfwk_LogicalTechnologyComponent(Element, TechnologyComponent):

    def __init__(self, categoryTRM: str, contentfwk_LogicalTechnologyComponent: "contentfwk_TechnologyArchitecture" = None, LogicalTechnologyComponent: "contentfwk_PlatformService" = None, LogicalTechnologyComponent185: "contentfwk_PhysicalTechnologyComponent" = None, isImplementedOnLogicalTechnologyComponents: set["contentfwk_Service"] = None, isSuppliedByLogicalTechnologyComponents: set["contentfwk_PlatformService"] = None, extendsLogicalTechnologyComponents: set["contentfwk_PhysicalTechnologyComponent"] = None, contentfwk_LogicalTechnologyComponent304: "contentfwk_LogicalTechnologyComponent" = None, contentfwk_LogicalTechnologyComponent302: "contentfwk_LogicalTechnologyComponent" = None, contentfwk_LogicalTechnologyComponent307: "contentfwk_LogicalTechnologyComponent" = None, contentfwk_LogicalTechnologyComponent305: set["contentfwk_LogicalTechnologyComponent"] = None, LogicalTechnologyComponent325: "contentfwk_Service" = None):
        self.categoryTRM = categoryTRM
        self.contentfwk_LogicalTechnologyComponent = contentfwk_LogicalTechnologyComponent
        self.LogicalTechnologyComponent = LogicalTechnologyComponent
        self.LogicalTechnologyComponent185 = LogicalTechnologyComponent185
        self.isImplementedOnLogicalTechnologyComponents = isImplementedOnLogicalTechnologyComponents if isImplementedOnLogicalTechnologyComponents is not None else set()
        self.isSuppliedByLogicalTechnologyComponents = isSuppliedByLogicalTechnologyComponents if isSuppliedByLogicalTechnologyComponents is not None else set()
        self.extendsLogicalTechnologyComponents = extendsLogicalTechnologyComponents if extendsLogicalTechnologyComponents is not None else set()
        self.contentfwk_LogicalTechnologyComponent304 = contentfwk_LogicalTechnologyComponent304
        self.contentfwk_LogicalTechnologyComponent302 = contentfwk_LogicalTechnologyComponent302
        self.contentfwk_LogicalTechnologyComponent307 = contentfwk_LogicalTechnologyComponent307
        self.contentfwk_LogicalTechnologyComponent305 = contentfwk_LogicalTechnologyComponent305 if contentfwk_LogicalTechnologyComponent305 is not None else set()
        self.LogicalTechnologyComponent325 = LogicalTechnologyComponent325
        
    @property
    def categoryTRM(self) -> str:
        return self.__categoryTRM

    @categoryTRM.setter
    def categoryTRM(self, categoryTRM: str):
        self.__categoryTRM = categoryTRM

    @property
    def contentfwk_LogicalTechnologyComponent305(self):
        return self.__contentfwk_LogicalTechnologyComponent305

    @contentfwk_LogicalTechnologyComponent305.setter
    def contentfwk_LogicalTechnologyComponent305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_LogicalTechnologyComponent__contentfwk_LogicalTechnologyComponent305", None)
        self.__contentfwk_LogicalTechnologyComponent305 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_LogicalTechnologyComponent307"):
                    opp_val = getattr(item, "contentfwk_LogicalTechnologyComponent307", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_LogicalTechnologyComponent307", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_LogicalTechnologyComponent307"):
                    opp_val = getattr(item, "contentfwk_LogicalTechnologyComponent307", None)
                    
                    setattr(item, "contentfwk_LogicalTechnologyComponent307", self)
                    

    @property
    def isImplementedOnLogicalTechnologyComponents(self):
        return self.__isImplementedOnLogicalTechnologyComponents

    @isImplementedOnLogicalTechnologyComponents.setter
    def isImplementedOnLogicalTechnologyComponents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_LogicalTechnologyComponent__isImplementedOnLogicalTechnologyComponents", None)
        self.__isImplementedOnLogicalTechnologyComponents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service298"):
                    opp_val = getattr(item, "Service298", None)
                    
                    if opp_val == self:
                        setattr(item, "Service298", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service298"):
                    opp_val = getattr(item, "Service298", None)
                    
                    setattr(item, "Service298", self)
                    

    @property
    def contentfwk_LogicalTechnologyComponent304(self):
        return self.__contentfwk_LogicalTechnologyComponent304

    @contentfwk_LogicalTechnologyComponent304.setter
    def contentfwk_LogicalTechnologyComponent304(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_LogicalTechnologyComponent__contentfwk_LogicalTechnologyComponent304", None)
        self.__contentfwk_LogicalTechnologyComponent304 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_LogicalTechnologyComponent302"):
                opp_val = getattr(old_value, "contentfwk_LogicalTechnologyComponent302", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_LogicalTechnologyComponent302", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_LogicalTechnologyComponent302"):
                opp_val = getattr(value, "contentfwk_LogicalTechnologyComponent302", None)
                setattr(value, "contentfwk_LogicalTechnologyComponent302", self)

    @property
    def LogicalTechnologyComponent185(self):
        return self.__LogicalTechnologyComponent185

    @LogicalTechnologyComponent185.setter
    def LogicalTechnologyComponent185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_LogicalTechnologyComponent__LogicalTechnologyComponent185", None)
        self.__LogicalTechnologyComponent185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isRealizedByPhysicalTechnologyComponents"):
                opp_val = getattr(old_value, "isRealizedByPhysicalTechnologyComponents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isRealizedByPhysicalTechnologyComponents"):
                opp_val = getattr(value, "isRealizedByPhysicalTechnologyComponents", None)
                if opp_val is None:
                    setattr(value, "isRealizedByPhysicalTechnologyComponents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_LogicalTechnologyComponent(self):
        return self.__contentfwk_LogicalTechnologyComponent

    @contentfwk_LogicalTechnologyComponent.setter
    def contentfwk_LogicalTechnologyComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_LogicalTechnologyComponent__contentfwk_LogicalTechnologyComponent", None)
        self.__contentfwk_LogicalTechnologyComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_TechnologyArchitecture45"):
                opp_val = getattr(old_value, "contentfwk_TechnologyArchitecture45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_TechnologyArchitecture45"):
                opp_val = getattr(value, "contentfwk_TechnologyArchitecture45", None)
                if opp_val is None:
                    setattr(value, "contentfwk_TechnologyArchitecture45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def extendsLogicalTechnologyComponents(self):
        return self.__extendsLogicalTechnologyComponents

    @extendsLogicalTechnologyComponents.setter
    def extendsLogicalTechnologyComponents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_LogicalTechnologyComponent__extendsLogicalTechnologyComponents", None)
        self.__extendsLogicalTechnologyComponents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhysicalTechnologyComponent301"):
                    opp_val = getattr(item, "PhysicalTechnologyComponent301", None)
                    
                    if opp_val == self:
                        setattr(item, "PhysicalTechnologyComponent301", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhysicalTechnologyComponent301"):
                    opp_val = getattr(item, "PhysicalTechnologyComponent301", None)
                    
                    setattr(item, "PhysicalTechnologyComponent301", self)
                    

    @property
    def LogicalTechnologyComponent(self):
        return self.__LogicalTechnologyComponent

    @LogicalTechnologyComponent.setter
    def LogicalTechnologyComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_LogicalTechnologyComponent__LogicalTechnologyComponent", None)
        self.__LogicalTechnologyComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "suppliesPlatformServices"):
                opp_val = getattr(old_value, "suppliesPlatformServices", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "suppliesPlatformServices"):
                opp_val = getattr(value, "suppliesPlatformServices", None)
                if opp_val is None:
                    setattr(value, "suppliesPlatformServices", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_LogicalTechnologyComponent302(self):
        return self.__contentfwk_LogicalTechnologyComponent302

    @contentfwk_LogicalTechnologyComponent302.setter
    def contentfwk_LogicalTechnologyComponent302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_LogicalTechnologyComponent__contentfwk_LogicalTechnologyComponent302", None)
        self.__contentfwk_LogicalTechnologyComponent302 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_LogicalTechnologyComponent304"):
                opp_val = getattr(old_value, "contentfwk_LogicalTechnologyComponent304", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_LogicalTechnologyComponent304", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_LogicalTechnologyComponent304"):
                opp_val = getattr(value, "contentfwk_LogicalTechnologyComponent304", None)
                setattr(value, "contentfwk_LogicalTechnologyComponent304", self)

    @property
    def LogicalTechnologyComponent325(self):
        return self.__LogicalTechnologyComponent325

    @LogicalTechnologyComponent325.setter
    def LogicalTechnologyComponent325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_LogicalTechnologyComponent__LogicalTechnologyComponent325", None)
        self.__LogicalTechnologyComponent325 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "providesPlatformForServices"):
                opp_val = getattr(old_value, "providesPlatformForServices", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "providesPlatformForServices"):
                opp_val = getattr(value, "providesPlatformForServices", None)
                if opp_val is None:
                    setattr(value, "providesPlatformForServices", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def isSuppliedByLogicalTechnologyComponents(self):
        return self.__isSuppliedByLogicalTechnologyComponents

    @isSuppliedByLogicalTechnologyComponents.setter
    def isSuppliedByLogicalTechnologyComponents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_LogicalTechnologyComponent__isSuppliedByLogicalTechnologyComponents", None)
        self.__isSuppliedByLogicalTechnologyComponents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PlatformService"):
                    opp_val = getattr(item, "PlatformService", None)
                    
                    if opp_val == self:
                        setattr(item, "PlatformService", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PlatformService"):
                    opp_val = getattr(item, "PlatformService", None)
                    
                    setattr(item, "PlatformService", self)
                    

    @property
    def contentfwk_LogicalTechnologyComponent307(self):
        return self.__contentfwk_LogicalTechnologyComponent307

    @contentfwk_LogicalTechnologyComponent307.setter
    def contentfwk_LogicalTechnologyComponent307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_LogicalTechnologyComponent__contentfwk_LogicalTechnologyComponent307", None)
        self.__contentfwk_LogicalTechnologyComponent307 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_LogicalTechnologyComponent305"):
                opp_val = getattr(old_value, "contentfwk_LogicalTechnologyComponent305", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_LogicalTechnologyComponent305"):
                opp_val = getattr(value, "contentfwk_LogicalTechnologyComponent305", None)
                if opp_val is None:
                    setattr(value, "contentfwk_LogicalTechnologyComponent305", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class contentfwk_PhysicalTechnologyComponent(Element, TechnologyComponent):

    def __init__(self, productName: str, moduleName: str, vendor: str, version: str, categoryTRM: str, contentfwk_PhysicalTechnologyComponent: "contentfwk_TechnologyArchitecture" = None, containsPhysicalTechnologyComponents: set["contentfwk_Location"] = None, contentfwk_PhysicalTechnologyComponent190: "contentfwk_PhysicalTechnologyComponent" = None, contentfwk_PhysicalTechnologyComponent188: "contentfwk_PhysicalTechnologyComponent" = None, contentfwk_PhysicalTechnologyComponent193: "contentfwk_PhysicalTechnologyComponent" = None, contentfwk_PhysicalTechnologyComponent191: set["contentfwk_PhysicalTechnologyComponent"] = None, contentfwk_PhysicalTechnologyComponent183: set["contentfwk_PhysicalApplicationComponent"] = None, isRealizedByPhysicalTechnologyComponents: set["contentfwk_LogicalTechnologyComponent"] = None, PhysicalTechnologyComponent: "contentfwk_Location" = None, contentfwk_PhysicalTechnologyComponent293: "contentfwk_PhysicalApplicationComponent" = None, PhysicalTechnologyComponent301: "contentfwk_LogicalTechnologyComponent" = None):
        self.productName = productName
        self.moduleName = moduleName
        self.vendor = vendor
        self.version = version
        self.categoryTRM = categoryTRM
        self.contentfwk_PhysicalTechnologyComponent = contentfwk_PhysicalTechnologyComponent
        self.containsPhysicalTechnologyComponents = containsPhysicalTechnologyComponents if containsPhysicalTechnologyComponents is not None else set()
        self.contentfwk_PhysicalTechnologyComponent190 = contentfwk_PhysicalTechnologyComponent190
        self.contentfwk_PhysicalTechnologyComponent188 = contentfwk_PhysicalTechnologyComponent188
        self.contentfwk_PhysicalTechnologyComponent193 = contentfwk_PhysicalTechnologyComponent193
        self.contentfwk_PhysicalTechnologyComponent191 = contentfwk_PhysicalTechnologyComponent191 if contentfwk_PhysicalTechnologyComponent191 is not None else set()
        self.contentfwk_PhysicalTechnologyComponent183 = contentfwk_PhysicalTechnologyComponent183 if contentfwk_PhysicalTechnologyComponent183 is not None else set()
        self.isRealizedByPhysicalTechnologyComponents = isRealizedByPhysicalTechnologyComponents if isRealizedByPhysicalTechnologyComponents is not None else set()
        self.PhysicalTechnologyComponent = PhysicalTechnologyComponent
        self.contentfwk_PhysicalTechnologyComponent293 = contentfwk_PhysicalTechnologyComponent293
        self.PhysicalTechnologyComponent301 = PhysicalTechnologyComponent301
        
    @property
    def productName(self) -> str:
        return self.__productName

    @productName.setter
    def productName(self, productName: str):
        self.__productName = productName

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def vendor(self) -> str:
        return self.__vendor

    @vendor.setter
    def vendor(self, vendor: str):
        self.__vendor = vendor

    @property
    def moduleName(self) -> str:
        return self.__moduleName

    @moduleName.setter
    def moduleName(self, moduleName: str):
        self.__moduleName = moduleName

    @property
    def categoryTRM(self) -> str:
        return self.__categoryTRM

    @categoryTRM.setter
    def categoryTRM(self, categoryTRM: str):
        self.__categoryTRM = categoryTRM

    @property
    def PhysicalTechnologyComponent301(self):
        return self.__PhysicalTechnologyComponent301

    @PhysicalTechnologyComponent301.setter
    def PhysicalTechnologyComponent301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__PhysicalTechnologyComponent301", None)
        self.__PhysicalTechnologyComponent301 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendsLogicalTechnologyComponents"):
                opp_val = getattr(old_value, "extendsLogicalTechnologyComponents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendsLogicalTechnologyComponents"):
                opp_val = getattr(value, "extendsLogicalTechnologyComponents", None)
                if opp_val is None:
                    setattr(value, "extendsLogicalTechnologyComponents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_PhysicalTechnologyComponent191(self):
        return self.__contentfwk_PhysicalTechnologyComponent191

    @contentfwk_PhysicalTechnologyComponent191.setter
    def contentfwk_PhysicalTechnologyComponent191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent191", None)
        self.__contentfwk_PhysicalTechnologyComponent191 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_PhysicalTechnologyComponent193"):
                    opp_val = getattr(item, "contentfwk_PhysicalTechnologyComponent193", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_PhysicalTechnologyComponent193", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_PhysicalTechnologyComponent193"):
                    opp_val = getattr(item, "contentfwk_PhysicalTechnologyComponent193", None)
                    
                    setattr(item, "contentfwk_PhysicalTechnologyComponent193", self)
                    

    @property
    def contentfwk_PhysicalTechnologyComponent(self):
        return self.__contentfwk_PhysicalTechnologyComponent

    @contentfwk_PhysicalTechnologyComponent.setter
    def contentfwk_PhysicalTechnologyComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent", None)
        self.__contentfwk_PhysicalTechnologyComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_TechnologyArchitecture43"):
                opp_val = getattr(old_value, "contentfwk_TechnologyArchitecture43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_TechnologyArchitecture43"):
                opp_val = getattr(value, "contentfwk_TechnologyArchitecture43", None)
                if opp_val is None:
                    setattr(value, "contentfwk_TechnologyArchitecture43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_PhysicalTechnologyComponent293(self):
        return self.__contentfwk_PhysicalTechnologyComponent293

    @contentfwk_PhysicalTechnologyComponent293.setter
    def contentfwk_PhysicalTechnologyComponent293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent293", None)
        self.__contentfwk_PhysicalTechnologyComponent293 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalApplicationComponent292"):
                opp_val = getattr(old_value, "contentfwk_PhysicalApplicationComponent292", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalApplicationComponent292"):
                opp_val = getattr(value, "contentfwk_PhysicalApplicationComponent292", None)
                if opp_val is None:
                    setattr(value, "contentfwk_PhysicalApplicationComponent292", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_PhysicalTechnologyComponent190(self):
        return self.__contentfwk_PhysicalTechnologyComponent190

    @contentfwk_PhysicalTechnologyComponent190.setter
    def contentfwk_PhysicalTechnologyComponent190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent190", None)
        self.__contentfwk_PhysicalTechnologyComponent190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalTechnologyComponent188"):
                opp_val = getattr(old_value, "contentfwk_PhysicalTechnologyComponent188", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_PhysicalTechnologyComponent188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalTechnologyComponent188"):
                opp_val = getattr(value, "contentfwk_PhysicalTechnologyComponent188", None)
                setattr(value, "contentfwk_PhysicalTechnologyComponent188", self)

    @property
    def containsPhysicalTechnologyComponents(self):
        return self.__containsPhysicalTechnologyComponents

    @containsPhysicalTechnologyComponents.setter
    def containsPhysicalTechnologyComponents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__containsPhysicalTechnologyComponents", None)
        self.__containsPhysicalTechnologyComponents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Location187"):
                    opp_val = getattr(item, "Location187", None)
                    
                    if opp_val == self:
                        setattr(item, "Location187", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Location187"):
                    opp_val = getattr(item, "Location187", None)
                    
                    setattr(item, "Location187", self)
                    

    @property
    def contentfwk_PhysicalTechnologyComponent188(self):
        return self.__contentfwk_PhysicalTechnologyComponent188

    @contentfwk_PhysicalTechnologyComponent188.setter
    def contentfwk_PhysicalTechnologyComponent188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent188", None)
        self.__contentfwk_PhysicalTechnologyComponent188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalTechnologyComponent190"):
                opp_val = getattr(old_value, "contentfwk_PhysicalTechnologyComponent190", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_PhysicalTechnologyComponent190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalTechnologyComponent190"):
                opp_val = getattr(value, "contentfwk_PhysicalTechnologyComponent190", None)
                setattr(value, "contentfwk_PhysicalTechnologyComponent190", self)

    @property
    def contentfwk_PhysicalTechnologyComponent183(self):
        return self.__contentfwk_PhysicalTechnologyComponent183

    @contentfwk_PhysicalTechnologyComponent183.setter
    def contentfwk_PhysicalTechnologyComponent183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent183", None)
        self.__contentfwk_PhysicalTechnologyComponent183 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_PhysicalApplicationComponent"):
                    opp_val = getattr(item, "contentfwk_PhysicalApplicationComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_PhysicalApplicationComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_PhysicalApplicationComponent"):
                    opp_val = getattr(item, "contentfwk_PhysicalApplicationComponent", None)
                    
                    setattr(item, "contentfwk_PhysicalApplicationComponent", self)
                    

    @property
    def contentfwk_PhysicalTechnologyComponent193(self):
        return self.__contentfwk_PhysicalTechnologyComponent193

    @contentfwk_PhysicalTechnologyComponent193.setter
    def contentfwk_PhysicalTechnologyComponent193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent193", None)
        self.__contentfwk_PhysicalTechnologyComponent193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalTechnologyComponent191"):
                opp_val = getattr(old_value, "contentfwk_PhysicalTechnologyComponent191", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalTechnologyComponent191"):
                opp_val = getattr(value, "contentfwk_PhysicalTechnologyComponent191", None)
                if opp_val is None:
                    setattr(value, "contentfwk_PhysicalTechnologyComponent191", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PhysicalTechnologyComponent(self):
        return self.__PhysicalTechnologyComponent

    @PhysicalTechnologyComponent.setter
    def PhysicalTechnologyComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__PhysicalTechnologyComponent", None)
        self.__PhysicalTechnologyComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isHostedInLocation254"):
                opp_val = getattr(old_value, "isHostedInLocation254", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isHostedInLocation254"):
                opp_val = getattr(value, "isHostedInLocation254", None)
                if opp_val is None:
                    setattr(value, "isHostedInLocation254", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def isRealizedByPhysicalTechnologyComponents(self):
        return self.__isRealizedByPhysicalTechnologyComponents

    @isRealizedByPhysicalTechnologyComponents.setter
    def isRealizedByPhysicalTechnologyComponents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__isRealizedByPhysicalTechnologyComponents", None)
        self.__isRealizedByPhysicalTechnologyComponents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LogicalTechnologyComponent185"):
                    opp_val = getattr(item, "LogicalTechnologyComponent185", None)
                    
                    if opp_val == self:
                        setattr(item, "LogicalTechnologyComponent185", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LogicalTechnologyComponent185"):
                    opp_val = getattr(item, "LogicalTechnologyComponent185", None)
                    
                    setattr(item, "LogicalTechnologyComponent185", self)
                    

class contentfwk_Process(Element, Standard):

    def __init__(self, isAutomated: bool, processVolumetrics: str, processCritiality: str, contentfwk_Process: "contentfwk_BusinessArchitecture" = None, Process: "contentfwk_OrganizationUnit" = None, Process79: "contentfwk_Actor" = None, Process134: "contentfwk_Function" = None, Process136: "contentfwk_Function" = None, isRealizedByProcesses: set["contentfwk_Function"] = None, supportsProcesses: set["contentfwk_Function"] = None, participatesInProcesses: set["contentfwk_OrganizationUnit"] = None, isRealizedByProcesses157: set["contentfwk_Service"] = None, supportsProcesses160: set["contentfwk_Service"] = None, contentfwk_Process174: "contentfwk_Process" = None, contentfwk_Process172: "contentfwk_Process" = None, Process177: "contentfwk_Process" = None, followsProcesses: set["contentfwk_Process"] = None, Process180: "contentfwk_Process" = None, precedesProcesses: set["contentfwk_Process"] = None, participatesInProcesses163: set["contentfwk_Actor"] = None, ensuresCorrectOperationOfProcesses: set["contentfwk_Control"] = None, isResolvedByProcesses: set["contentfwk_Event"] = None, isGeneratedByProcesses: set["contentfwk_Event"] = None, isProducedByProcesses: set["contentfwk_Product"] = None, Process198: "contentfwk_Product" = None, Process227: "contentfwk_Control" = None, Process217: "contentfwk_Event" = None, Process219: "contentfwk_Event" = None, Process333: "contentfwk_Service" = None, Process335: "contentfwk_Service" = None):
        self.isAutomated = isAutomated
        self.processVolumetrics = processVolumetrics
        self.processCritiality = processCritiality
        self.contentfwk_Process = contentfwk_Process
        self.Process = Process
        self.Process79 = Process79
        self.Process134 = Process134
        self.Process136 = Process136
        self.isRealizedByProcesses = isRealizedByProcesses if isRealizedByProcesses is not None else set()
        self.supportsProcesses = supportsProcesses if supportsProcesses is not None else set()
        self.participatesInProcesses = participatesInProcesses if participatesInProcesses is not None else set()
        self.isRealizedByProcesses157 = isRealizedByProcesses157 if isRealizedByProcesses157 is not None else set()
        self.supportsProcesses160 = supportsProcesses160 if supportsProcesses160 is not None else set()
        self.contentfwk_Process174 = contentfwk_Process174
        self.contentfwk_Process172 = contentfwk_Process172
        self.Process177 = Process177
        self.followsProcesses = followsProcesses if followsProcesses is not None else set()
        self.Process180 = Process180
        self.precedesProcesses = precedesProcesses if precedesProcesses is not None else set()
        self.participatesInProcesses163 = participatesInProcesses163 if participatesInProcesses163 is not None else set()
        self.ensuresCorrectOperationOfProcesses = ensuresCorrectOperationOfProcesses if ensuresCorrectOperationOfProcesses is not None else set()
        self.isResolvedByProcesses = isResolvedByProcesses if isResolvedByProcesses is not None else set()
        self.isGeneratedByProcesses = isGeneratedByProcesses if isGeneratedByProcesses is not None else set()
        self.isProducedByProcesses = isProducedByProcesses if isProducedByProcesses is not None else set()
        self.Process198 = Process198
        self.Process227 = Process227
        self.Process217 = Process217
        self.Process219 = Process219
        self.Process333 = Process333
        self.Process335 = Process335
        
    @property
    def isAutomated(self) -> bool:
        return self.__isAutomated

    @isAutomated.setter
    def isAutomated(self, isAutomated: bool):
        self.__isAutomated = isAutomated

    @property
    def processCritiality(self) -> str:
        return self.__processCritiality

    @processCritiality.setter
    def processCritiality(self, processCritiality: str):
        self.__processCritiality = processCritiality

    @property
    def processVolumetrics(self) -> str:
        return self.__processVolumetrics

    @processVolumetrics.setter
    def processVolumetrics(self, processVolumetrics: str):
        self.__processVolumetrics = processVolumetrics

    @property
    def Process198(self):
        return self.__Process198

    @Process198.setter
    def Process198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process198", None)
        self.__Process198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "producesProducts197"):
                opp_val = getattr(old_value, "producesProducts197", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "producesProducts197"):
                opp_val = getattr(value, "producesProducts197", None)
                if opp_val is None:
                    setattr(value, "producesProducts197", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def isRealizedByProcesses(self):
        return self.__isRealizedByProcesses

    @isRealizedByProcesses.setter
    def isRealizedByProcesses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__isRealizedByProcesses", None)
        self.__isRealizedByProcesses = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Function151"):
                    opp_val = getattr(item, "Function151", None)
                    
                    if opp_val == self:
                        setattr(item, "Function151", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function151"):
                    opp_val = getattr(item, "Function151", None)
                    
                    setattr(item, "Function151", self)
                    

    @property
    def Process217(self):
        return self.__Process217

    @Process217.setter
    def Process217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process217", None)
        self.__Process217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resolvesEvents216"):
                opp_val = getattr(old_value, "resolvesEvents216", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resolvesEvents216"):
                opp_val = getattr(value, "resolvesEvents216", None)
                if opp_val is None:
                    setattr(value, "resolvesEvents216", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def supportsProcesses(self):
        return self.__supportsProcesses

    @supportsProcesses.setter
    def supportsProcesses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__supportsProcesses", None)
        self.__supportsProcesses = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Function153"):
                    opp_val = getattr(item, "Function153", None)
                    
                    if opp_val == self:
                        setattr(item, "Function153", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function153"):
                    opp_val = getattr(item, "Function153", None)
                    
                    setattr(item, "Function153", self)
                    

    @property
    def Process227(self):
        return self.__Process227

    @Process227.setter
    def Process227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process227", None)
        self.__Process227 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isGuidedByControls"):
                opp_val = getattr(old_value, "isGuidedByControls", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isGuidedByControls"):
                opp_val = getattr(value, "isGuidedByControls", None)
                if opp_val is None:
                    setattr(value, "isGuidedByControls", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def isRealizedByProcesses157(self):
        return self.__isRealizedByProcesses157

    @isRealizedByProcesses157.setter
    def isRealizedByProcesses157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__isRealizedByProcesses157", None)
        self.__isRealizedByProcesses157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service158"):
                    opp_val = getattr(item, "Service158", None)
                    
                    if opp_val == self:
                        setattr(item, "Service158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service158"):
                    opp_val = getattr(item, "Service158", None)
                    
                    setattr(item, "Service158", self)
                    

    @property
    def Process136(self):
        return self.__Process136

    @Process136.setter
    def Process136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process136", None)
        self.__Process136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orchestratesFunctions"):
                opp_val = getattr(old_value, "orchestratesFunctions", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orchestratesFunctions"):
                opp_val = getattr(value, "orchestratesFunctions", None)
                if opp_val is None:
                    setattr(value, "orchestratesFunctions", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Process79(self):
        return self.__Process79

    @Process79.setter
    def Process79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process79", None)
        self.__Process79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "involvesActors"):
                opp_val = getattr(old_value, "involvesActors", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "involvesActors"):
                opp_val = getattr(value, "involvesActors", None)
                if opp_val is None:
                    setattr(value, "involvesActors", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def supportsProcesses160(self):
        return self.__supportsProcesses160

    @supportsProcesses160.setter
    def supportsProcesses160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__supportsProcesses160", None)
        self.__supportsProcesses160 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service161"):
                    opp_val = getattr(item, "Service161", None)
                    
                    if opp_val == self:
                        setattr(item, "Service161", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service161"):
                    opp_val = getattr(item, "Service161", None)
                    
                    setattr(item, "Service161", self)
                    

    @property
    def isGeneratedByProcesses(self):
        return self.__isGeneratedByProcesses

    @isGeneratedByProcesses.setter
    def isGeneratedByProcesses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__isGeneratedByProcesses", None)
        self.__isGeneratedByProcesses = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Event169"):
                    opp_val = getattr(item, "Event169", None)
                    
                    if opp_val == self:
                        setattr(item, "Event169", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Event169"):
                    opp_val = getattr(item, "Event169", None)
                    
                    setattr(item, "Event169", self)
                    

    @property
    def Process219(self):
        return self.__Process219

    @Process219.setter
    def Process219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process219", None)
        self.__Process219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generatesEvents"):
                opp_val = getattr(old_value, "generatesEvents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generatesEvents"):
                opp_val = getattr(value, "generatesEvents", None)
                if opp_val is None:
                    setattr(value, "generatesEvents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def isProducedByProcesses(self):
        return self.__isProducedByProcesses

    @isProducedByProcesses.setter
    def isProducedByProcesses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__isProducedByProcesses", None)
        self.__isProducedByProcesses = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Product171"):
                    opp_val = getattr(item, "Product171", None)
                    
                    if opp_val == self:
                        setattr(item, "Product171", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Product171"):
                    opp_val = getattr(item, "Product171", None)
                    
                    setattr(item, "Product171", self)
                    

    @property
    def isResolvedByProcesses(self):
        return self.__isResolvedByProcesses

    @isResolvedByProcesses.setter
    def isResolvedByProcesses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__isResolvedByProcesses", None)
        self.__isResolvedByProcesses = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Event167"):
                    opp_val = getattr(item, "Event167", None)
                    
                    if opp_val == self:
                        setattr(item, "Event167", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Event167"):
                    opp_val = getattr(item, "Event167", None)
                    
                    setattr(item, "Event167", self)
                    

    @property
    def participatesInProcesses(self):
        return self.__participatesInProcesses

    @participatesInProcesses.setter
    def participatesInProcesses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__participatesInProcesses", None)
        self.__participatesInProcesses = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OrganizationUnit155"):
                    opp_val = getattr(item, "OrganizationUnit155", None)
                    
                    if opp_val == self:
                        setattr(item, "OrganizationUnit155", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OrganizationUnit155"):
                    opp_val = getattr(item, "OrganizationUnit155", None)
                    
                    setattr(item, "OrganizationUnit155", self)
                    

    @property
    def contentfwk_Process(self):
        return self.__contentfwk_Process

    @contentfwk_Process.setter
    def contentfwk_Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__contentfwk_Process", None)
        self.__contentfwk_Process = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_BusinessArchitecture21"):
                opp_val = getattr(old_value, "contentfwk_BusinessArchitecture21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_BusinessArchitecture21"):
                opp_val = getattr(value, "contentfwk_BusinessArchitecture21", None)
                if opp_val is None:
                    setattr(value, "contentfwk_BusinessArchitecture21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Process134(self):
        return self.__Process134

    @Process134.setter
    def Process134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process134", None)
        self.__Process134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decomposesFunctions"):
                opp_val = getattr(old_value, "decomposesFunctions", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decomposesFunctions"):
                opp_val = getattr(value, "decomposesFunctions", None)
                if opp_val is None:
                    setattr(value, "decomposesFunctions", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def precedesProcesses(self):
        return self.__precedesProcesses

    @precedesProcesses.setter
    def precedesProcesses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__precedesProcesses", None)
        self.__precedesProcesses = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Process180"):
                    opp_val = getattr(item, "Process180", None)
                    
                    if opp_val == self:
                        setattr(item, "Process180", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Process180"):
                    opp_val = getattr(item, "Process180", None)
                    
                    setattr(item, "Process180", self)
                    

    @property
    def Process(self):
        return self.__Process

    @Process.setter
    def Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process", None)
        self.__Process = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "involvesOrganizationUnits"):
                opp_val = getattr(old_value, "involvesOrganizationUnits", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "involvesOrganizationUnits"):
                opp_val = getattr(value, "involvesOrganizationUnits", None)
                if opp_val is None:
                    setattr(value, "involvesOrganizationUnits", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def followsProcesses(self):
        return self.__followsProcesses

    @followsProcesses.setter
    def followsProcesses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__followsProcesses", None)
        self.__followsProcesses = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Process177"):
                    opp_val = getattr(item, "Process177", None)
                    
                    if opp_val == self:
                        setattr(item, "Process177", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Process177"):
                    opp_val = getattr(item, "Process177", None)
                    
                    setattr(item, "Process177", self)
                    

    @property
    def Process180(self):
        return self.__Process180

    @Process180.setter
    def Process180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process180", None)
        self.__Process180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "precedesProcesses"):
                opp_val = getattr(old_value, "precedesProcesses", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "precedesProcesses"):
                opp_val = getattr(value, "precedesProcesses", None)
                if opp_val is None:
                    setattr(value, "precedesProcesses", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def participatesInProcesses163(self):
        return self.__participatesInProcesses163

    @participatesInProcesses163.setter
    def participatesInProcesses163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__participatesInProcesses163", None)
        self.__participatesInProcesses163 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Actor164"):
                    opp_val = getattr(item, "Actor164", None)
                    
                    if opp_val == self:
                        setattr(item, "Actor164", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Actor164"):
                    opp_val = getattr(item, "Actor164", None)
                    
                    setattr(item, "Actor164", self)
                    

    @property
    def Process177(self):
        return self.__Process177

    @Process177.setter
    def Process177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process177", None)
        self.__Process177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "followsProcesses"):
                opp_val = getattr(old_value, "followsProcesses", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "followsProcesses"):
                opp_val = getattr(value, "followsProcesses", None)
                if opp_val is None:
                    setattr(value, "followsProcesses", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_Process172(self):
        return self.__contentfwk_Process172

    @contentfwk_Process172.setter
    def contentfwk_Process172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__contentfwk_Process172", None)
        self.__contentfwk_Process172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_Process174"):
                opp_val = getattr(old_value, "contentfwk_Process174", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_Process174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_Process174"):
                opp_val = getattr(value, "contentfwk_Process174", None)
                setattr(value, "contentfwk_Process174", self)

    @property
    def Process333(self):
        return self.__Process333

    @Process333.setter
    def Process333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process333", None)
        self.__Process333 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decomposesServices"):
                opp_val = getattr(old_value, "decomposesServices", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decomposesServices"):
                opp_val = getattr(value, "decomposesServices", None)
                if opp_val is None:
                    setattr(value, "decomposesServices", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Process335(self):
        return self.__Process335

    @Process335.setter
    def Process335(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process335", None)
        self.__Process335 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orchestratesServices"):
                opp_val = getattr(old_value, "orchestratesServices", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orchestratesServices"):
                opp_val = getattr(value, "orchestratesServices", None)
                if opp_val is None:
                    setattr(value, "orchestratesServices", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_Process174(self):
        return self.__contentfwk_Process174

    @contentfwk_Process174.setter
    def contentfwk_Process174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__contentfwk_Process174", None)
        self.__contentfwk_Process174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_Process172"):
                opp_val = getattr(old_value, "contentfwk_Process172", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_Process172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_Process172"):
                opp_val = getattr(value, "contentfwk_Process172", None)
                setattr(value, "contentfwk_Process172", self)

    @property
    def ensuresCorrectOperationOfProcesses(self):
        return self.__ensuresCorrectOperationOfProcesses

    @ensuresCorrectOperationOfProcesses.setter
    def ensuresCorrectOperationOfProcesses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__ensuresCorrectOperationOfProcesses", None)
        self.__ensuresCorrectOperationOfProcesses = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Control"):
                    opp_val = getattr(item, "Control", None)
                    
                    if opp_val == self:
                        setattr(item, "Control", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Control"):
                    opp_val = getattr(item, "Control", None)
                    
                    setattr(item, "Control", self)
                    

class contentfwk_BusinessService(Service, Element):

    pass
class contentfwk_Function(Element, Standard):

    pass
class contentfwk_Role(Element):

    def __init__(self, estimatedFTEs: str, contentfwk_Role: "contentfwk_BusinessArchitecture" = None, Role: "contentfwk_Actor" = None, performsTaskInRoles: set["contentfwk_Actor"] = None, canBeAccessedByRoles: set["contentfwk_Function"] = None, contentfwk_Role99: "contentfwk_Role" = None, contentfwk_Role97: "contentfwk_Role" = None, Role138: "contentfwk_Function" = None):
        self.estimatedFTEs = estimatedFTEs
        self.contentfwk_Role = contentfwk_Role
        self.Role = Role
        self.performsTaskInRoles = performsTaskInRoles if performsTaskInRoles is not None else set()
        self.canBeAccessedByRoles = canBeAccessedByRoles if canBeAccessedByRoles is not None else set()
        self.contentfwk_Role99 = contentfwk_Role99
        self.contentfwk_Role97 = contentfwk_Role97
        self.Role138 = Role138
        
    @property
    def estimatedFTEs(self) -> str:
        return self.__estimatedFTEs

    @estimatedFTEs.setter
    def estimatedFTEs(self, estimatedFTEs: str):
        self.__estimatedFTEs = estimatedFTEs

    @property
    def contentfwk_Role(self):
        return self.__contentfwk_Role

    @contentfwk_Role.setter
    def contentfwk_Role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Role__contentfwk_Role", None)
        self.__contentfwk_Role = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_BusinessArchitecture15"):
                opp_val = getattr(old_value, "contentfwk_BusinessArchitecture15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_BusinessArchitecture15"):
                opp_val = getattr(value, "contentfwk_BusinessArchitecture15", None)
                if opp_val is None:
                    setattr(value, "contentfwk_BusinessArchitecture15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Role(self):
        return self.__Role

    @Role.setter
    def Role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Role__Role", None)
        self.__Role = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isAssumedByActors"):
                opp_val = getattr(old_value, "isAssumedByActors", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isAssumedByActors"):
                opp_val = getattr(value, "isAssumedByActors", None)
                if opp_val is None:
                    setattr(value, "isAssumedByActors", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Role138(self):
        return self.__Role138

    @Role138.setter
    def Role138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Role__Role138", None)
        self.__Role138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accessesFunctions"):
                opp_val = getattr(old_value, "accessesFunctions", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accessesFunctions"):
                opp_val = getattr(value, "accessesFunctions", None)
                if opp_val is None:
                    setattr(value, "accessesFunctions", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def performsTaskInRoles(self):
        return self.__performsTaskInRoles

    @performsTaskInRoles.setter
    def performsTaskInRoles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Role__performsTaskInRoles", None)
        self.__performsTaskInRoles = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Actor94"):
                    opp_val = getattr(item, "Actor94", None)
                    
                    if opp_val == self:
                        setattr(item, "Actor94", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Actor94"):
                    opp_val = getattr(item, "Actor94", None)
                    
                    setattr(item, "Actor94", self)
                    

    @property
    def canBeAccessedByRoles(self):
        return self.__canBeAccessedByRoles

    @canBeAccessedByRoles.setter
    def canBeAccessedByRoles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Role__canBeAccessedByRoles", None)
        self.__canBeAccessedByRoles = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Function96"):
                    opp_val = getattr(item, "Function96", None)
                    
                    if opp_val == self:
                        setattr(item, "Function96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function96"):
                    opp_val = getattr(item, "Function96", None)
                    
                    setattr(item, "Function96", self)
                    

    @property
    def contentfwk_Role99(self):
        return self.__contentfwk_Role99

    @contentfwk_Role99.setter
    def contentfwk_Role99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Role__contentfwk_Role99", None)
        self.__contentfwk_Role99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_Role97"):
                opp_val = getattr(old_value, "contentfwk_Role97", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_Role97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_Role97"):
                opp_val = getattr(value, "contentfwk_Role97", None)
                setattr(value, "contentfwk_Role97", self)

    @property
    def contentfwk_Role97(self):
        return self.__contentfwk_Role97

    @contentfwk_Role97.setter
    def contentfwk_Role97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Role__contentfwk_Role97", None)
        self.__contentfwk_Role97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_Role99"):
                opp_val = getattr(old_value, "contentfwk_Role99", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_Role99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_Role99"):
                opp_val = getattr(value, "contentfwk_Role99", None)
                setattr(value, "contentfwk_Role99", self)

class contentfwk_Actor(Element):

    def __init__(self, FTEs: str, actorGoal: str, actorTasks: str, contentfwk_Actor: "contentfwk_BusinessArchitecture" = None, Actor: "contentfwk_OrganizationUnit" = None, supportsActors: set["contentfwk_Function"] = None, isAssumedByActors: set["contentfwk_Role"] = None, involvesActors: set["contentfwk_Process"] = None, contentfwk_Actor81: set["contentfwk_Service"] = None, isResolvedByActors: set["contentfwk_Event"] = None, isGeneratedByActors: set["contentfwk_Event"] = None, containsActors86: "contentfwk_Location" = None, isSuppliedByActors: set["contentfwk_DataEntity"] = None, isConsumedByActors: set["contentfwk_DataEntity"] = None, containsActors: "contentfwk_OrganizationUnit" = None, isPerformedByActors: set["contentfwk_Function"] = None, contentfwk_Actor92: "contentfwk_Actor" = None, contentfwk_Actor90: set["contentfwk_Actor"] = None, Actor94: "contentfwk_Role" = None, Actor103: "contentfwk_DataEntity" = None, Actor101: "contentfwk_DataEntity" = None, Actor140: "contentfwk_Function" = None, Actor128: "contentfwk_Function" = None, Actor164: "contentfwk_Process" = None, Actor225: "contentfwk_Event" = None, Actor222: "contentfwk_Event" = None, Actor246: "contentfwk_Location" = None, contentfwk_Actor313: "contentfwk_Service" = None):
        self.FTEs = FTEs
        self.actorGoal = actorGoal
        self.actorTasks = actorTasks
        self.contentfwk_Actor = contentfwk_Actor
        self.Actor = Actor
        self.supportsActors = supportsActors if supportsActors is not None else set()
        self.isAssumedByActors = isAssumedByActors if isAssumedByActors is not None else set()
        self.involvesActors = involvesActors if involvesActors is not None else set()
        self.contentfwk_Actor81 = contentfwk_Actor81 if contentfwk_Actor81 is not None else set()
        self.isResolvedByActors = isResolvedByActors if isResolvedByActors is not None else set()
        self.isGeneratedByActors = isGeneratedByActors if isGeneratedByActors is not None else set()
        self.containsActors86 = containsActors86
        self.isSuppliedByActors = isSuppliedByActors if isSuppliedByActors is not None else set()
        self.isConsumedByActors = isConsumedByActors if isConsumedByActors is not None else set()
        self.containsActors = containsActors
        self.isPerformedByActors = isPerformedByActors if isPerformedByActors is not None else set()
        self.contentfwk_Actor92 = contentfwk_Actor92
        self.contentfwk_Actor90 = contentfwk_Actor90 if contentfwk_Actor90 is not None else set()
        self.Actor94 = Actor94
        self.Actor103 = Actor103
        self.Actor101 = Actor101
        self.Actor140 = Actor140
        self.Actor128 = Actor128
        self.Actor164 = Actor164
        self.Actor225 = Actor225
        self.Actor222 = Actor222
        self.Actor246 = Actor246
        self.contentfwk_Actor313 = contentfwk_Actor313
        
    @property
    def actorTasks(self) -> str:
        return self.__actorTasks

    @actorTasks.setter
    def actorTasks(self, actorTasks: str):
        self.__actorTasks = actorTasks

    @property
    def actorGoal(self) -> str:
        return self.__actorGoal

    @actorGoal.setter
    def actorGoal(self, actorGoal: str):
        self.__actorGoal = actorGoal

    @property
    def FTEs(self) -> str:
        return self.__FTEs

    @FTEs.setter
    def FTEs(self, FTEs: str):
        self.__FTEs = FTEs

    @property
    def Actor222(self):
        return self.__Actor222

    @Actor222.setter
    def Actor222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor222", None)
        self.__Actor222 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resolvesEvents221"):
                opp_val = getattr(old_value, "resolvesEvents221", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resolvesEvents221"):
                opp_val = getattr(value, "resolvesEvents221", None)
                if opp_val is None:
                    setattr(value, "resolvesEvents221", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Actor164(self):
        return self.__Actor164

    @Actor164.setter
    def Actor164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor164", None)
        self.__Actor164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "participatesInProcesses163"):
                opp_val = getattr(old_value, "participatesInProcesses163", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "participatesInProcesses163"):
                opp_val = getattr(value, "participatesInProcesses163", None)
                if opp_val is None:
                    setattr(value, "participatesInProcesses163", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def supportsActors(self):
        return self.__supportsActors

    @supportsActors.setter
    def supportsActors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__supportsActors", None)
        self.__supportsActors = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Function76"):
                    opp_val = getattr(item, "Function76", None)
                    
                    if opp_val == self:
                        setattr(item, "Function76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function76"):
                    opp_val = getattr(item, "Function76", None)
                    
                    setattr(item, "Function76", self)
                    

    @property
    def isSuppliedByActors(self):
        return self.__isSuppliedByActors

    @isSuppliedByActors.setter
    def isSuppliedByActors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__isSuppliedByActors", None)
        self.__isSuppliedByActors = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataEntity"):
                    opp_val = getattr(item, "DataEntity", None)
                    
                    if opp_val == self:
                        setattr(item, "DataEntity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataEntity"):
                    opp_val = getattr(item, "DataEntity", None)
                    
                    setattr(item, "DataEntity", self)
                    

    @property
    def Actor94(self):
        return self.__Actor94

    @Actor94.setter
    def Actor94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor94", None)
        self.__Actor94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "performsTaskInRoles"):
                opp_val = getattr(old_value, "performsTaskInRoles", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "performsTaskInRoles"):
                opp_val = getattr(value, "performsTaskInRoles", None)
                if opp_val is None:
                    setattr(value, "performsTaskInRoles", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_Actor313(self):
        return self.__contentfwk_Actor313

    @contentfwk_Actor313.setter
    def contentfwk_Actor313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__contentfwk_Actor313", None)
        self.__contentfwk_Actor313 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_Service312"):
                opp_val = getattr(old_value, "contentfwk_Service312", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_Service312"):
                opp_val = getattr(value, "contentfwk_Service312", None)
                if opp_val is None:
                    setattr(value, "contentfwk_Service312", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def involvesActors(self):
        return self.__involvesActors

    @involvesActors.setter
    def involvesActors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__involvesActors", None)
        self.__involvesActors = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Process79"):
                    opp_val = getattr(item, "Process79", None)
                    
                    if opp_val == self:
                        setattr(item, "Process79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Process79"):
                    opp_val = getattr(item, "Process79", None)
                    
                    setattr(item, "Process79", self)
                    

    @property
    def isConsumedByActors(self):
        return self.__isConsumedByActors

    @isConsumedByActors.setter
    def isConsumedByActors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__isConsumedByActors", None)
        self.__isConsumedByActors = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataEntity72"):
                    opp_val = getattr(item, "DataEntity72", None)
                    
                    if opp_val == self:
                        setattr(item, "DataEntity72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataEntity72"):
                    opp_val = getattr(item, "DataEntity72", None)
                    
                    setattr(item, "DataEntity72", self)
                    

    @property
    def containsActors(self):
        return self.__containsActors

    @containsActors.setter
    def containsActors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__containsActors", None)
        self.__containsActors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OrganizationUnit74"):
                opp_val = getattr(old_value, "OrganizationUnit74", None)
                if opp_val == self:
                    setattr(old_value, "OrganizationUnit74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OrganizationUnit74"):
                opp_val = getattr(value, "OrganizationUnit74", None)
                setattr(value, "OrganizationUnit74", self)

    @property
    def Actor246(self):
        return self.__Actor246

    @Actor246.setter
    def Actor246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor246", None)
        self.__Actor246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operatesInLocation"):
                opp_val = getattr(old_value, "operatesInLocation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operatesInLocation"):
                opp_val = getattr(value, "operatesInLocation", None)
                if opp_val is None:
                    setattr(value, "operatesInLocation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def containsActors86(self):
        return self.__containsActors86

    @containsActors86.setter
    def containsActors86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__containsActors86", None)
        self.__containsActors86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Location87"):
                opp_val = getattr(old_value, "Location87", None)
                if opp_val == self:
                    setattr(old_value, "Location87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Location87"):
                opp_val = getattr(value, "Location87", None)
                setattr(value, "Location87", self)

    @property
    def Actor(self):
        return self.__Actor

    @Actor.setter
    def Actor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor", None)
        self.__Actor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "belongsTo"):
                opp_val = getattr(old_value, "belongsTo", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "belongsTo"):
                opp_val = getattr(value, "belongsTo", None)
                if opp_val is None:
                    setattr(value, "belongsTo", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_Actor(self):
        return self.__contentfwk_Actor

    @contentfwk_Actor.setter
    def contentfwk_Actor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__contentfwk_Actor", None)
        self.__contentfwk_Actor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_BusinessArchitecture13"):
                opp_val = getattr(old_value, "contentfwk_BusinessArchitecture13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_BusinessArchitecture13"):
                opp_val = getattr(value, "contentfwk_BusinessArchitecture13", None)
                if opp_val is None:
                    setattr(value, "contentfwk_BusinessArchitecture13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Actor140(self):
        return self.__Actor140

    @Actor140.setter
    def Actor140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor140", None)
        self.__Actor140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interactsWithFunctions"):
                opp_val = getattr(old_value, "interactsWithFunctions", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interactsWithFunctions"):
                opp_val = getattr(value, "interactsWithFunctions", None)
                if opp_val is None:
                    setattr(value, "interactsWithFunctions", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Actor103(self):
        return self.__Actor103

    @Actor103.setter
    def Actor103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor103", None)
        self.__Actor103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consumesEntities"):
                opp_val = getattr(old_value, "consumesEntities", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consumesEntities"):
                opp_val = getattr(value, "consumesEntities", None)
                if opp_val is None:
                    setattr(value, "consumesEntities", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_Actor81(self):
        return self.__contentfwk_Actor81

    @contentfwk_Actor81.setter
    def contentfwk_Actor81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__contentfwk_Actor81", None)
        self.__contentfwk_Actor81 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_Service"):
                    opp_val = getattr(item, "contentfwk_Service", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_Service", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_Service"):
                    opp_val = getattr(item, "contentfwk_Service", None)
                    
                    setattr(item, "contentfwk_Service", self)
                    

    @property
    def isPerformedByActors(self):
        return self.__isPerformedByActors

    @isPerformedByActors.setter
    def isPerformedByActors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__isPerformedByActors", None)
        self.__isPerformedByActors = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Function89"):
                    opp_val = getattr(item, "Function89", None)
                    
                    if opp_val == self:
                        setattr(item, "Function89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function89"):
                    opp_val = getattr(item, "Function89", None)
                    
                    setattr(item, "Function89", self)
                    

    @property
    def isGeneratedByActors(self):
        return self.__isGeneratedByActors

    @isGeneratedByActors.setter
    def isGeneratedByActors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__isGeneratedByActors", None)
        self.__isGeneratedByActors = value if value is not None else set()
        
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
    def Actor225(self):
        return self.__Actor225

    @Actor225.setter
    def Actor225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor225", None)
        self.__Actor225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generatesEvents224"):
                opp_val = getattr(old_value, "generatesEvents224", None)
                if opp_val == self:
                    setattr(old_value, "generatesEvents224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generatesEvents224"):
                opp_val = getattr(value, "generatesEvents224", None)
                setattr(value, "generatesEvents224", self)

    @property
    def isAssumedByActors(self):
        return self.__isAssumedByActors

    @isAssumedByActors.setter
    def isAssumedByActors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__isAssumedByActors", None)
        self.__isAssumedByActors = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Role"):
                    opp_val = getattr(item, "Role", None)
                    
                    if opp_val == self:
                        setattr(item, "Role", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Role"):
                    opp_val = getattr(item, "Role", None)
                    
                    setattr(item, "Role", self)
                    

    @property
    def Actor101(self):
        return self.__Actor101

    @Actor101.setter
    def Actor101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor101", None)
        self.__Actor101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "suppliesEntities"):
                opp_val = getattr(old_value, "suppliesEntities", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "suppliesEntities"):
                opp_val = getattr(value, "suppliesEntities", None)
                if opp_val is None:
                    setattr(value, "suppliesEntities", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def isResolvedByActors(self):
        return self.__isResolvedByActors

    @isResolvedByActors.setter
    def isResolvedByActors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__isResolvedByActors", None)
        self.__isResolvedByActors = value if value is not None else set()
        
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
    def Actor128(self):
        return self.__Actor128

    @Actor128.setter
    def Actor128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor128", None)
        self.__Actor128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "performsFunctions"):
                opp_val = getattr(old_value, "performsFunctions", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "performsFunctions"):
                opp_val = getattr(value, "performsFunctions", None)
                if opp_val is None:
                    setattr(value, "performsFunctions", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_Actor90(self):
        return self.__contentfwk_Actor90

    @contentfwk_Actor90.setter
    def contentfwk_Actor90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__contentfwk_Actor90", None)
        self.__contentfwk_Actor90 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_Actor92"):
                    opp_val = getattr(item, "contentfwk_Actor92", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_Actor92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_Actor92"):
                    opp_val = getattr(item, "contentfwk_Actor92", None)
                    
                    setattr(item, "contentfwk_Actor92", self)
                    

    @property
    def contentfwk_Actor92(self):
        return self.__contentfwk_Actor92

    @contentfwk_Actor92.setter
    def contentfwk_Actor92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__contentfwk_Actor92", None)
        self.__contentfwk_Actor92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_Actor90"):
                opp_val = getattr(old_value, "contentfwk_Actor90", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_Actor90"):
                opp_val = getattr(value, "contentfwk_Actor90", None)
                if opp_val is None:
                    setattr(value, "contentfwk_Actor90", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class contentfwk_OrganizationUnit(Element):

    def __init__(self, headcount: str, contentfwk_OrganizationUnit: "contentfwk_BusinessArchitecture" = None, OrganizationUnit: "contentfwk_Driver" = None, isOwnedAndGovernedByOrganizationUnits: set["contentfwk_Service"] = None, belongsTo: set["contentfwk_Actor"] = None, isOwnedByUnit: set["contentfwk_Function"] = None, involvesOrganizationUnits: set["contentfwk_Process"] = None, motivatesOrganizationUnits: set["contentfwk_Driver"] = None, isProducedByOrganizationUnits: set["contentfwk_Product"] = None, containsOrganizationUnits: "contentfwk_Location" = None, OrganizationUnit74: "contentfwk_Actor" = None, OrganizationUnit130: "contentfwk_Function" = None, OrganizationUnit155: "contentfwk_Process" = None, OrganizationUnit195: "contentfwk_Product" = None, OrganizationUnit249: "contentfwk_Location" = None, OrganizationUnit329: "contentfwk_Service" = None):
        self.headcount = headcount
        self.contentfwk_OrganizationUnit = contentfwk_OrganizationUnit
        self.OrganizationUnit = OrganizationUnit
        self.isOwnedAndGovernedByOrganizationUnits = isOwnedAndGovernedByOrganizationUnits if isOwnedAndGovernedByOrganizationUnits is not None else set()
        self.belongsTo = belongsTo if belongsTo is not None else set()
        self.isOwnedByUnit = isOwnedByUnit if isOwnedByUnit is not None else set()
        self.involvesOrganizationUnits = involvesOrganizationUnits if involvesOrganizationUnits is not None else set()
        self.motivatesOrganizationUnits = motivatesOrganizationUnits if motivatesOrganizationUnits is not None else set()
        self.isProducedByOrganizationUnits = isProducedByOrganizationUnits if isProducedByOrganizationUnits is not None else set()
        self.containsOrganizationUnits = containsOrganizationUnits
        self.OrganizationUnit74 = OrganizationUnit74
        self.OrganizationUnit130 = OrganizationUnit130
        self.OrganizationUnit155 = OrganizationUnit155
        self.OrganizationUnit195 = OrganizationUnit195
        self.OrganizationUnit249 = OrganizationUnit249
        self.OrganizationUnit329 = OrganizationUnit329
        
    @property
    def headcount(self) -> str:
        return self.__headcount

    @headcount.setter
    def headcount(self, headcount: str):
        self.__headcount = headcount

    @property
    def OrganizationUnit130(self):
        return self.__OrganizationUnit130

    @OrganizationUnit130.setter
    def OrganizationUnit130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit130", None)
        self.__OrganizationUnit130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownsFunctions"):
                opp_val = getattr(old_value, "ownsFunctions", None)
                if opp_val == self:
                    setattr(old_value, "ownsFunctions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownsFunctions"):
                opp_val = getattr(value, "ownsFunctions", None)
                setattr(value, "ownsFunctions", self)

    @property
    def isOwnedAndGovernedByOrganizationUnits(self):
        return self.__isOwnedAndGovernedByOrganizationUnits

    @isOwnedAndGovernedByOrganizationUnits.setter
    def isOwnedAndGovernedByOrganizationUnits(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__isOwnedAndGovernedByOrganizationUnits", None)
        self.__isOwnedAndGovernedByOrganizationUnits = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service"):
                    opp_val = getattr(item, "Service", None)
                    
                    if opp_val == self:
                        setattr(item, "Service", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service"):
                    opp_val = getattr(item, "Service", None)
                    
                    setattr(item, "Service", self)
                    

    @property
    def OrganizationUnit329(self):
        return self.__OrganizationUnit329

    @OrganizationUnit329.setter
    def OrganizationUnit329(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit329", None)
        self.__OrganizationUnit329 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownsAndGovernsServices"):
                opp_val = getattr(old_value, "ownsAndGovernsServices", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownsAndGovernsServices"):
                opp_val = getattr(value, "ownsAndGovernsServices", None)
                if opp_val is None:
                    setattr(value, "ownsAndGovernsServices", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def belongsTo(self):
        return self.__belongsTo

    @belongsTo.setter
    def belongsTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__belongsTo", None)
        self.__belongsTo = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Actor"):
                    opp_val = getattr(item, "Actor", None)
                    
                    if opp_val == self:
                        setattr(item, "Actor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Actor"):
                    opp_val = getattr(item, "Actor", None)
                    
                    setattr(item, "Actor", self)
                    

    @property
    def OrganizationUnit195(self):
        return self.__OrganizationUnit195

    @OrganizationUnit195.setter
    def OrganizationUnit195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit195", None)
        self.__OrganizationUnit195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "producesProducts"):
                opp_val = getattr(old_value, "producesProducts", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "producesProducts"):
                opp_val = getattr(value, "producesProducts", None)
                if opp_val is None:
                    setattr(value, "producesProducts", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def involvesOrganizationUnits(self):
        return self.__involvesOrganizationUnits

    @involvesOrganizationUnits.setter
    def involvesOrganizationUnits(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__involvesOrganizationUnits", None)
        self.__involvesOrganizationUnits = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Process"):
                    opp_val = getattr(item, "Process", None)
                    
                    if opp_val == self:
                        setattr(item, "Process", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Process"):
                    opp_val = getattr(item, "Process", None)
                    
                    setattr(item, "Process", self)
                    

    @property
    def contentfwk_OrganizationUnit(self):
        return self.__contentfwk_OrganizationUnit

    @contentfwk_OrganizationUnit.setter
    def contentfwk_OrganizationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__contentfwk_OrganizationUnit", None)
        self.__contentfwk_OrganizationUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_BusinessArchitecture11"):
                opp_val = getattr(old_value, "contentfwk_BusinessArchitecture11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_BusinessArchitecture11"):
                opp_val = getattr(value, "contentfwk_BusinessArchitecture11", None)
                if opp_val is None:
                    setattr(value, "contentfwk_BusinessArchitecture11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OrganizationUnit(self):
        return self.__OrganizationUnit

    @OrganizationUnit.setter
    def OrganizationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit", None)
        self.__OrganizationUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isMotivatedByDrivers"):
                opp_val = getattr(old_value, "isMotivatedByDrivers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isMotivatedByDrivers"):
                opp_val = getattr(value, "isMotivatedByDrivers", None)
                if opp_val is None:
                    setattr(value, "isMotivatedByDrivers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OrganizationUnit249(self):
        return self.__OrganizationUnit249

    @OrganizationUnit249.setter
    def OrganizationUnit249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit249", None)
        self.__OrganizationUnit249 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operatesInLocation248"):
                opp_val = getattr(old_value, "operatesInLocation248", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operatesInLocation248"):
                opp_val = getattr(value, "operatesInLocation248", None)
                if opp_val is None:
                    setattr(value, "operatesInLocation248", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def containsOrganizationUnits(self):
        return self.__containsOrganizationUnits

    @containsOrganizationUnits.setter
    def containsOrganizationUnits(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__containsOrganizationUnits", None)
        self.__containsOrganizationUnits = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Location"):
                opp_val = getattr(old_value, "Location", None)
                if opp_val == self:
                    setattr(old_value, "Location", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Location"):
                opp_val = getattr(value, "Location", None)
                setattr(value, "Location", self)

    @property
    def OrganizationUnit155(self):
        return self.__OrganizationUnit155

    @OrganizationUnit155.setter
    def OrganizationUnit155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit155", None)
        self.__OrganizationUnit155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "participatesInProcesses"):
                opp_val = getattr(old_value, "participatesInProcesses", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "participatesInProcesses"):
                opp_val = getattr(value, "participatesInProcesses", None)
                if opp_val is None:
                    setattr(value, "participatesInProcesses", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OrganizationUnit74(self):
        return self.__OrganizationUnit74

    @OrganizationUnit74.setter
    def OrganizationUnit74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit74", None)
        self.__OrganizationUnit74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containsActors"):
                opp_val = getattr(old_value, "containsActors", None)
                if opp_val == self:
                    setattr(old_value, "containsActors", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containsActors"):
                opp_val = getattr(value, "containsActors", None)
                setattr(value, "containsActors", self)

    @property
    def isProducedByOrganizationUnits(self):
        return self.__isProducedByOrganizationUnits

    @isProducedByOrganizationUnits.setter
    def isProducedByOrganizationUnits(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__isProducedByOrganizationUnits", None)
        self.__isProducedByOrganizationUnits = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Product"):
                    opp_val = getattr(item, "Product", None)
                    
                    if opp_val == self:
                        setattr(item, "Product", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Product"):
                    opp_val = getattr(item, "Product", None)
                    
                    setattr(item, "Product", self)
                    

    @property
    def isOwnedByUnit(self):
        return self.__isOwnedByUnit

    @isOwnedByUnit.setter
    def isOwnedByUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__isOwnedByUnit", None)
        self.__isOwnedByUnit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Function"):
                    opp_val = getattr(item, "Function", None)
                    
                    if opp_val == self:
                        setattr(item, "Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function"):
                    opp_val = getattr(item, "Function", None)
                    
                    setattr(item, "Function", self)
                    

    @property
    def motivatesOrganizationUnits(self):
        return self.__motivatesOrganizationUnits

    @motivatesOrganizationUnits.setter
    def motivatesOrganizationUnits(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__motivatesOrganizationUnits", None)
        self.__motivatesOrganizationUnits = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Driver67"):
                    opp_val = getattr(item, "Driver67", None)
                    
                    if opp_val == self:
                        setattr(item, "Driver67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Driver67"):
                    opp_val = getattr(item, "Driver67", None)
                    
                    setattr(item, "Driver67", self)
                    

class contentfwk_Objective(Element):

    pass
class contentfwk_Measure(Element):

    pass
class contentfwk_Contract(Element):

    def __init__(self, securityCharacteristics: str, privacyCharacteristics: str, integrityCharacteristics: str, credibilityCharacteristics: str, localizationCharacteristics: str, internationalizationCharacteristics: str, interoperabilityCharacteristics: str, scalabilityCharacteristics: str, portabilityCharacteristics: str, extensibilityCharacteristics: str, capacityCharacteristics: str, throughput: str, throughputPeriod: str, growth: str, growthPeriod: str, peakProfileShortTerm: str, behaviorCharacteristics: str, ServiceNameCaller: str, ServiceNameCalled: str, serviceQualityCharacteristics: str, availabilityQualityCharacteristics: str, servicesTimes: str, manageabilityCharacteristics: str, serviceabilityCharacteristics: str, performanceCharacteristics: str, responseCharacteristics: str, reliabilityCharacteristics: str, qualityOfInformationRequired: str, contractControlRequirements: str, resultControlRequirements: str, recoverabilityCharacteristics: str, locatabilityCharacteristics: str, peakProfileLongTerm: str, contentfwk_Contract: "contentfwk_BusinessArchitecture" = None, Contract: "contentfwk_ServiceQuality" = None, isGovernedAndMeasuredByContracts: set["contentfwk_Service"] = None, appliesToContracts: set["contentfwk_ServiceQuality"] = None, Contract321: "contentfwk_Service" = None):
        self.securityCharacteristics = securityCharacteristics
        self.privacyCharacteristics = privacyCharacteristics
        self.integrityCharacteristics = integrityCharacteristics
        self.credibilityCharacteristics = credibilityCharacteristics
        self.localizationCharacteristics = localizationCharacteristics
        self.internationalizationCharacteristics = internationalizationCharacteristics
        self.interoperabilityCharacteristics = interoperabilityCharacteristics
        self.scalabilityCharacteristics = scalabilityCharacteristics
        self.portabilityCharacteristics = portabilityCharacteristics
        self.extensibilityCharacteristics = extensibilityCharacteristics
        self.capacityCharacteristics = capacityCharacteristics
        self.throughput = throughput
        self.throughputPeriod = throughputPeriod
        self.growth = growth
        self.growthPeriod = growthPeriod
        self.peakProfileShortTerm = peakProfileShortTerm
        self.behaviorCharacteristics = behaviorCharacteristics
        self.ServiceNameCaller = ServiceNameCaller
        self.ServiceNameCalled = ServiceNameCalled
        self.serviceQualityCharacteristics = serviceQualityCharacteristics
        self.availabilityQualityCharacteristics = availabilityQualityCharacteristics
        self.servicesTimes = servicesTimes
        self.manageabilityCharacteristics = manageabilityCharacteristics
        self.serviceabilityCharacteristics = serviceabilityCharacteristics
        self.performanceCharacteristics = performanceCharacteristics
        self.responseCharacteristics = responseCharacteristics
        self.reliabilityCharacteristics = reliabilityCharacteristics
        self.qualityOfInformationRequired = qualityOfInformationRequired
        self.contractControlRequirements = contractControlRequirements
        self.resultControlRequirements = resultControlRequirements
        self.recoverabilityCharacteristics = recoverabilityCharacteristics
        self.locatabilityCharacteristics = locatabilityCharacteristics
        self.peakProfileLongTerm = peakProfileLongTerm
        self.contentfwk_Contract = contentfwk_Contract
        self.Contract = Contract
        self.isGovernedAndMeasuredByContracts = isGovernedAndMeasuredByContracts if isGovernedAndMeasuredByContracts is not None else set()
        self.appliesToContracts = appliesToContracts if appliesToContracts is not None else set()
        self.Contract321 = Contract321
        
    @property
    def peakProfileLongTerm(self) -> str:
        return self.__peakProfileLongTerm

    @peakProfileLongTerm.setter
    def peakProfileLongTerm(self, peakProfileLongTerm: str):
        self.__peakProfileLongTerm = peakProfileLongTerm

    @property
    def contractControlRequirements(self) -> str:
        return self.__contractControlRequirements

    @contractControlRequirements.setter
    def contractControlRequirements(self, contractControlRequirements: str):
        self.__contractControlRequirements = contractControlRequirements

    @property
    def serviceabilityCharacteristics(self) -> str:
        return self.__serviceabilityCharacteristics

    @serviceabilityCharacteristics.setter
    def serviceabilityCharacteristics(self, serviceabilityCharacteristics: str):
        self.__serviceabilityCharacteristics = serviceabilityCharacteristics

    @property
    def credibilityCharacteristics(self) -> str:
        return self.__credibilityCharacteristics

    @credibilityCharacteristics.setter
    def credibilityCharacteristics(self, credibilityCharacteristics: str):
        self.__credibilityCharacteristics = credibilityCharacteristics

    @property
    def securityCharacteristics(self) -> str:
        return self.__securityCharacteristics

    @securityCharacteristics.setter
    def securityCharacteristics(self, securityCharacteristics: str):
        self.__securityCharacteristics = securityCharacteristics

    @property
    def growthPeriod(self) -> str:
        return self.__growthPeriod

    @growthPeriod.setter
    def growthPeriod(self, growthPeriod: str):
        self.__growthPeriod = growthPeriod

    @property
    def locatabilityCharacteristics(self) -> str:
        return self.__locatabilityCharacteristics

    @locatabilityCharacteristics.setter
    def locatabilityCharacteristics(self, locatabilityCharacteristics: str):
        self.__locatabilityCharacteristics = locatabilityCharacteristics

    @property
    def internationalizationCharacteristics(self) -> str:
        return self.__internationalizationCharacteristics

    @internationalizationCharacteristics.setter
    def internationalizationCharacteristics(self, internationalizationCharacteristics: str):
        self.__internationalizationCharacteristics = internationalizationCharacteristics

    @property
    def portabilityCharacteristics(self) -> str:
        return self.__portabilityCharacteristics

    @portabilityCharacteristics.setter
    def portabilityCharacteristics(self, portabilityCharacteristics: str):
        self.__portabilityCharacteristics = portabilityCharacteristics

    @property
    def integrityCharacteristics(self) -> str:
        return self.__integrityCharacteristics

    @integrityCharacteristics.setter
    def integrityCharacteristics(self, integrityCharacteristics: str):
        self.__integrityCharacteristics = integrityCharacteristics

    @property
    def scalabilityCharacteristics(self) -> str:
        return self.__scalabilityCharacteristics

    @scalabilityCharacteristics.setter
    def scalabilityCharacteristics(self, scalabilityCharacteristics: str):
        self.__scalabilityCharacteristics = scalabilityCharacteristics

    @property
    def extensibilityCharacteristics(self) -> str:
        return self.__extensibilityCharacteristics

    @extensibilityCharacteristics.setter
    def extensibilityCharacteristics(self, extensibilityCharacteristics: str):
        self.__extensibilityCharacteristics = extensibilityCharacteristics

    @property
    def interoperabilityCharacteristics(self) -> str:
        return self.__interoperabilityCharacteristics

    @interoperabilityCharacteristics.setter
    def interoperabilityCharacteristics(self, interoperabilityCharacteristics: str):
        self.__interoperabilityCharacteristics = interoperabilityCharacteristics

    @property
    def resultControlRequirements(self) -> str:
        return self.__resultControlRequirements

    @resultControlRequirements.setter
    def resultControlRequirements(self, resultControlRequirements: str):
        self.__resultControlRequirements = resultControlRequirements

    @property
    def growth(self) -> str:
        return self.__growth

    @growth.setter
    def growth(self, growth: str):
        self.__growth = growth

    @property
    def peakProfileShortTerm(self) -> str:
        return self.__peakProfileShortTerm

    @peakProfileShortTerm.setter
    def peakProfileShortTerm(self, peakProfileShortTerm: str):
        self.__peakProfileShortTerm = peakProfileShortTerm

    @property
    def capacityCharacteristics(self) -> str:
        return self.__capacityCharacteristics

    @capacityCharacteristics.setter
    def capacityCharacteristics(self, capacityCharacteristics: str):
        self.__capacityCharacteristics = capacityCharacteristics

    @property
    def serviceQualityCharacteristics(self) -> str:
        return self.__serviceQualityCharacteristics

    @serviceQualityCharacteristics.setter
    def serviceQualityCharacteristics(self, serviceQualityCharacteristics: str):
        self.__serviceQualityCharacteristics = serviceQualityCharacteristics

    @property
    def manageabilityCharacteristics(self) -> str:
        return self.__manageabilityCharacteristics

    @manageabilityCharacteristics.setter
    def manageabilityCharacteristics(self, manageabilityCharacteristics: str):
        self.__manageabilityCharacteristics = manageabilityCharacteristics

    @property
    def throughput(self) -> str:
        return self.__throughput

    @throughput.setter
    def throughput(self, throughput: str):
        self.__throughput = throughput

    @property
    def privacyCharacteristics(self) -> str:
        return self.__privacyCharacteristics

    @privacyCharacteristics.setter
    def privacyCharacteristics(self, privacyCharacteristics: str):
        self.__privacyCharacteristics = privacyCharacteristics

    @property
    def reliabilityCharacteristics(self) -> str:
        return self.__reliabilityCharacteristics

    @reliabilityCharacteristics.setter
    def reliabilityCharacteristics(self, reliabilityCharacteristics: str):
        self.__reliabilityCharacteristics = reliabilityCharacteristics

    @property
    def qualityOfInformationRequired(self) -> str:
        return self.__qualityOfInformationRequired

    @qualityOfInformationRequired.setter
    def qualityOfInformationRequired(self, qualityOfInformationRequired: str):
        self.__qualityOfInformationRequired = qualityOfInformationRequired

    @property
    def throughputPeriod(self) -> str:
        return self.__throughputPeriod

    @throughputPeriod.setter
    def throughputPeriod(self, throughputPeriod: str):
        self.__throughputPeriod = throughputPeriod

    @property
    def localizationCharacteristics(self) -> str:
        return self.__localizationCharacteristics

    @localizationCharacteristics.setter
    def localizationCharacteristics(self, localizationCharacteristics: str):
        self.__localizationCharacteristics = localizationCharacteristics

    @property
    def behaviorCharacteristics(self) -> str:
        return self.__behaviorCharacteristics

    @behaviorCharacteristics.setter
    def behaviorCharacteristics(self, behaviorCharacteristics: str):
        self.__behaviorCharacteristics = behaviorCharacteristics

    @property
    def availabilityQualityCharacteristics(self) -> str:
        return self.__availabilityQualityCharacteristics

    @availabilityQualityCharacteristics.setter
    def availabilityQualityCharacteristics(self, availabilityQualityCharacteristics: str):
        self.__availabilityQualityCharacteristics = availabilityQualityCharacteristics

    @property
    def ServiceNameCalled(self) -> str:
        return self.__ServiceNameCalled

    @ServiceNameCalled.setter
    def ServiceNameCalled(self, ServiceNameCalled: str):
        self.__ServiceNameCalled = ServiceNameCalled

    @property
    def servicesTimes(self) -> str:
        return self.__servicesTimes

    @servicesTimes.setter
    def servicesTimes(self, servicesTimes: str):
        self.__servicesTimes = servicesTimes

    @property
    def performanceCharacteristics(self) -> str:
        return self.__performanceCharacteristics

    @performanceCharacteristics.setter
    def performanceCharacteristics(self, performanceCharacteristics: str):
        self.__performanceCharacteristics = performanceCharacteristics

    @property
    def recoverabilityCharacteristics(self) -> str:
        return self.__recoverabilityCharacteristics

    @recoverabilityCharacteristics.setter
    def recoverabilityCharacteristics(self, recoverabilityCharacteristics: str):
        self.__recoverabilityCharacteristics = recoverabilityCharacteristics

    @property
    def ServiceNameCaller(self) -> str:
        return self.__ServiceNameCaller

    @ServiceNameCaller.setter
    def ServiceNameCaller(self, ServiceNameCaller: str):
        self.__ServiceNameCaller = ServiceNameCaller

    @property
    def responseCharacteristics(self) -> str:
        return self.__responseCharacteristics

    @responseCharacteristics.setter
    def responseCharacteristics(self, responseCharacteristics: str):
        self.__responseCharacteristics = responseCharacteristics

    @property
    def appliesToContracts(self):
        return self.__appliesToContracts

    @appliesToContracts.setter
    def appliesToContracts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Contract__appliesToContracts", None)
        self.__appliesToContracts = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ServiceQuality"):
                    opp_val = getattr(item, "ServiceQuality", None)
                    
                    if opp_val == self:
                        setattr(item, "ServiceQuality", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ServiceQuality"):
                    opp_val = getattr(item, "ServiceQuality", None)
                    
                    setattr(item, "ServiceQuality", self)
                    

    @property
    def contentfwk_Contract(self):
        return self.__contentfwk_Contract

    @contentfwk_Contract.setter
    def contentfwk_Contract(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Contract__contentfwk_Contract", None)
        self.__contentfwk_Contract = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_BusinessArchitecture31"):
                opp_val = getattr(old_value, "contentfwk_BusinessArchitecture31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_BusinessArchitecture31"):
                opp_val = getattr(value, "contentfwk_BusinessArchitecture31", None)
                if opp_val is None:
                    setattr(value, "contentfwk_BusinessArchitecture31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def isGovernedAndMeasuredByContracts(self):
        return self.__isGovernedAndMeasuredByContracts

    @isGovernedAndMeasuredByContracts.setter
    def isGovernedAndMeasuredByContracts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Contract__isGovernedAndMeasuredByContracts", None)
        self.__isGovernedAndMeasuredByContracts = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service211"):
                    opp_val = getattr(item, "Service211", None)
                    
                    if opp_val == self:
                        setattr(item, "Service211", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service211"):
                    opp_val = getattr(item, "Service211", None)
                    
                    setattr(item, "Service211", self)
                    

    @property
    def Contract321(self):
        return self.__Contract321

    @Contract321.setter
    def Contract321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Contract__Contract321", None)
        self.__Contract321 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "governsAndMeasuresBusinessServices"):
                opp_val = getattr(old_value, "governsAndMeasuresBusinessServices", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "governsAndMeasuresBusinessServices"):
                opp_val = getattr(value, "governsAndMeasuresBusinessServices", None)
                if opp_val is None:
                    setattr(value, "governsAndMeasuresBusinessServices", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Contract(self):
        return self.__Contract

    @Contract.setter
    def Contract(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Contract__Contract", None)
        self.__Contract = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "meetsServiceQuality"):
                opp_val = getattr(old_value, "meetsServiceQuality", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "meetsServiceQuality"):
                opp_val = getattr(value, "meetsServiceQuality", None)
                if opp_val is None:
                    setattr(value, "meetsServiceQuality", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class contentfwk_Product(Element):

    pass
class contentfwk_Location(Element):

    pass
class contentfwk_Event(Element):

    pass
class contentfwk_Control(Element):

    pass
class contentfwk_Architecture(ABC):

    pass
class contentfwk_EnterpriseArchitecture:

    pass
class contentfwk_Goal(Element):

    pass
class contentfwk_Driver(Element):

    pass
class Architecture:

    pass
class contentfwk_ApplicationArchitecture(Architecture):

    pass
class contentfwk_DataArchitecture(Architecture):

    pass
class contentfwk_TechnologyArchitecture(Architecture):

    pass
class contentfwk_StrategicArchitecture(Architecture):

    pass
class contentfwk_BusinessArchitecture(Architecture):

    pass
class contentfwk_Label:

    def __init__(self, name: str, id: str, description: str, contentfwk_Label: "contentfwk_EnterpriseArchitecture" = None, Label238: "contentfwk_Container" = None, contentfwk_Label241: "contentfwk_Label" = None, contentfwk_Label239: set["contentfwk_Label"] = None, category: set["contentfwk_Element"] = None, labels: set["contentfwk_Container"] = None, Label: "contentfwk_Element" = None):
        self.name = name
        self.id = id
        self.description = description
        self.contentfwk_Label = contentfwk_Label
        self.Label238 = Label238
        self.contentfwk_Label241 = contentfwk_Label241
        self.contentfwk_Label239 = contentfwk_Label239 if contentfwk_Label239 is not None else set()
        self.category = category if category is not None else set()
        self.labels = labels if labels is not None else set()
        self.Label = Label
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def contentfwk_Label239(self):
        return self.__contentfwk_Label239

    @contentfwk_Label239.setter
    def contentfwk_Label239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Label__contentfwk_Label239", None)
        self.__contentfwk_Label239 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_Label241"):
                    opp_val = getattr(item, "contentfwk_Label241", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_Label241", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_Label241"):
                    opp_val = getattr(item, "contentfwk_Label241", None)
                    
                    setattr(item, "contentfwk_Label241", self)
                    

    @property
    def contentfwk_Label(self):
        return self.__contentfwk_Label

    @contentfwk_Label.setter
    def contentfwk_Label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Label__contentfwk_Label", None)
        self.__contentfwk_Label = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_EnterpriseArchitecture4"):
                opp_val = getattr(old_value, "contentfwk_EnterpriseArchitecture4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_EnterpriseArchitecture4"):
                opp_val = getattr(value, "contentfwk_EnterpriseArchitecture4", None)
                if opp_val is None:
                    setattr(value, "contentfwk_EnterpriseArchitecture4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Label(self):
        return self.__Label

    @Label.setter
    def Label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Label__Label", None)
        self.__Label = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedElements"):
                opp_val = getattr(old_value, "ownedElements", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedElements"):
                opp_val = getattr(value, "ownedElements", None)
                if opp_val is None:
                    setattr(value, "ownedElements", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Label238(self):
        return self.__Label238

    @Label238.setter
    def Label238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Label__Label238", None)
        self.__Label238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containers"):
                opp_val = getattr(old_value, "containers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containers"):
                opp_val = getattr(value, "containers", None)
                if opp_val is None:
                    setattr(value, "containers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_Label241(self):
        return self.__contentfwk_Label241

    @contentfwk_Label241.setter
    def contentfwk_Label241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Label__contentfwk_Label241", None)
        self.__contentfwk_Label241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_Label239"):
                opp_val = getattr(old_value, "contentfwk_Label239", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_Label239"):
                opp_val = getattr(value, "contentfwk_Label239", None)
                if opp_val is None:
                    setattr(value, "contentfwk_Label239", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def labels(self):
        return self.__labels

    @labels.setter
    def labels(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Label__labels", None)
        self.__labels = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Container"):
                    opp_val = getattr(item, "Container", None)
                    
                    if opp_val == self:
                        setattr(item, "Container", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Container"):
                    opp_val = getattr(item, "Container", None)
                    
                    setattr(item, "Container", self)
                    

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Label__category", None)
        self.__category = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element243"):
                    opp_val = getattr(item, "Element243", None)
                    
                    if opp_val == self:
                        setattr(item, "Element243", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element243"):
                    opp_val = getattr(item, "Element243", None)
                    
                    setattr(item, "Element243", self)
                    

class contentfwk_Container:

    def __init__(self, id: str, description: str, name: str, contentfwk_Container: "contentfwk_EnterpriseArchitecture" = None, containers: set["contentfwk_Label"] = None, Container: "contentfwk_Label" = None, contentfwk_Container236: "contentfwk_Container" = None, contentfwk_Container234: set["contentfwk_Container"] = None):
        self.id = id
        self.description = description
        self.name = name
        self.contentfwk_Container = contentfwk_Container
        self.containers = containers if containers is not None else set()
        self.Container = Container
        self.contentfwk_Container236 = contentfwk_Container236
        self.contentfwk_Container234 = contentfwk_Container234 if contentfwk_Container234 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def Container(self):
        return self.__Container

    @Container.setter
    def Container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Container__Container", None)
        self.__Container = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "labels"):
                opp_val = getattr(old_value, "labels", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "labels"):
                opp_val = getattr(value, "labels", None)
                if opp_val is None:
                    setattr(value, "labels", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_Container236(self):
        return self.__contentfwk_Container236

    @contentfwk_Container236.setter
    def contentfwk_Container236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Container__contentfwk_Container236", None)
        self.__contentfwk_Container236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_Container234"):
                opp_val = getattr(old_value, "contentfwk_Container234", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_Container234"):
                opp_val = getattr(value, "contentfwk_Container234", None)
                if opp_val is None:
                    setattr(value, "contentfwk_Container234", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_Container(self):
        return self.__contentfwk_Container

    @contentfwk_Container.setter
    def contentfwk_Container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Container__contentfwk_Container", None)
        self.__contentfwk_Container = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_EnterpriseArchitecture2"):
                opp_val = getattr(old_value, "contentfwk_EnterpriseArchitecture2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_EnterpriseArchitecture2"):
                opp_val = getattr(value, "contentfwk_EnterpriseArchitecture2", None)
                if opp_val is None:
                    setattr(value, "contentfwk_EnterpriseArchitecture2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_Container234(self):
        return self.__contentfwk_Container234

    @contentfwk_Container234.setter
    def contentfwk_Container234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Container__contentfwk_Container234", None)
        self.__contentfwk_Container234 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_Container236"):
                    opp_val = getattr(item, "contentfwk_Container236", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_Container236", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_Container236"):
                    opp_val = getattr(item, "contentfwk_Container236", None)
                    
                    setattr(item, "contentfwk_Container236", self)
                    

    @property
    def containers(self):
        return self.__containers

    @containers.setter
    def containers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Container__containers", None)
        self.__containers = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Label238"):
                    opp_val = getattr(item, "Label238", None)
                    
                    if opp_val == self:
                        setattr(item, "Label238", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Label238"):
                    opp_val = getattr(item, "Label238", None)
                    
                    setattr(item, "Label238", self)
                    
