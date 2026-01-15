from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class LifeCycleStatus(Enum):
    Proposed = "Proposed"
    InDevelopment = "InDevelopment"
    Live = "Live"
    PhasingOut = "PhasingOut"
    Retired = "Retired"
class PrincipleCategory(Enum):
    GuidingPrinciple = "GuidingPrinciple"
    BusinessPrinciple = "BusinessPrinciple"
    DataPrinciple = "DataPrinciple"
    ApplicationPrinciple = "ApplicationPrinciple"
    IntegrationPrinciple = "IntegrationPrinciple"
    TechnologyPrinciple = "TechnologyPrinciple"
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
class WorkPackageCategory(Enum):
    WorkPackage = "WorkPackage"
    WorkStream = "WorkStream"
    Project = "Project"
    Program = "Program"
    Portofolio = "Portofolio"


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
    def standardCreationDate(self) -> date:
        return self.__standardCreationDate

    @standardCreationDate.setter
    def standardCreationDate(self, standardCreationDate: date):
        self.__standardCreationDate = standardCreationDate

    @property
    def nextStandardCreationDate(self) -> date:
        return self.__nextStandardCreationDate

    @nextStandardCreationDate.setter
    def nextStandardCreationDate(self, nextStandardCreationDate: date):
        self.__nextStandardCreationDate = nextStandardCreationDate

    @property
    def retireDate(self) -> date:
        return self.__retireDate

    @retireDate.setter
    def retireDate(self, retireDate: date):
        self.__retireDate = retireDate

    @property
    def lastStandardCreationDate(self) -> date:
        return self.__lastStandardCreationDate

    @lastStandardCreationDate.setter
    def lastStandardCreationDate(self, lastStandardCreationDate: date):
        self.__lastStandardCreationDate = lastStandardCreationDate

    @property
    def standardClass(self) -> str:
        return self.__standardClass

    @standardClass.setter
    def standardClass(self, standardClass: str):
        self.__standardClass = standardClass

class DataComponent:

    pass
class StrategicElement:

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
    def rationale(self) -> str:
        return self.__rationale

    @rationale.setter
    def rationale(self, rationale: str):
        self.__rationale = rationale

    @property
    def statementOfRequirement(self) -> str:
        return self.__statementOfRequirement

    @statementOfRequirement.setter
    def statementOfRequirement(self, statementOfRequirement: str):
        self.__statementOfRequirement = statementOfRequirement

class contentfwk_Constraint(StrategicElement):

    pass
class contentfwk_Gap(StrategicElement):

    pass
class contentfwk_Assumption(StrategicElement):

    pass
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
                    

class contentfwk_Principle(StrategicElement):

    def __init__(self, principleCategory: str, priority: str, statementOfPrinciple: str, rationale: str, implication: str, metric: str):
        self.principleCategory = principleCategory
        self.priority = priority
        self.statementOfPrinciple = statementOfPrinciple
        self.rationale = rationale
        self.implication = implication
        self.metric = metric
        
    @property
    def metric(self) -> str:
        return self.__metric

    @metric.setter
    def metric(self, metric: str):
        self.__metric = metric

    @property
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

    @property
    def statementOfPrinciple(self) -> str:
        return self.__statementOfPrinciple

    @statementOfPrinciple.setter
    def statementOfPrinciple(self, statementOfPrinciple: str):
        self.__statementOfPrinciple = statementOfPrinciple

    @property
    def principleCategory(self) -> str:
        return self.__principleCategory

    @principleCategory.setter
    def principleCategory(self, principleCategory: str):
        self.__principleCategory = principleCategory

    @property
    def implication(self) -> str:
        return self.__implication

    @implication.setter
    def implication(self, implication: str):
        self.__implication = implication

    @property
    def rationale(self) -> str:
        return self.__rationale

    @rationale.setter
    def rationale(self, rationale: str):
        self.__rationale = rationale

class contentfwk_Element:

    def __init__(self, name: str, description: str, category: str, sourceDescr: str, ownerDescr: str, ID: str, Element241: "contentfwk_Element" = None, delegates: set["contentfwk_Element"] = None, contentfwk_Element: "contentfwk_Container" = None, Element: "contentfwk_Element" = None, isDelegatedBy: set["contentfwk_Element"] = None):
        self.name = name
        self.description = description
        self.category = category
        self.sourceDescr = sourceDescr
        self.ownerDescr = ownerDescr
        self.ID = ID
        self.Element241 = Element241
        self.delegates = delegates if delegates is not None else set()
        self.contentfwk_Element = contentfwk_Element
        self.Element = Element
        self.isDelegatedBy = isDelegatedBy if isDelegatedBy is not None else set()
        
    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def ownerDescr(self) -> str:
        return self.__ownerDescr

    @ownerDescr.setter
    def ownerDescr(self, ownerDescr: str):
        self.__ownerDescr = ownerDescr

    @property
    def sourceDescr(self) -> str:
        return self.__sourceDescr

    @sourceDescr.setter
    def sourceDescr(self, sourceDescr: str):
        self.__sourceDescr = sourceDescr

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def contentfwk_Element(self):
        return self.__contentfwk_Element

    @contentfwk_Element.setter
    def contentfwk_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Element__contentfwk_Element", None)
        self.__contentfwk_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_Container243"):
                opp_val = getattr(old_value, "contentfwk_Container243", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_Container243"):
                opp_val = getattr(value, "contentfwk_Container243", None)
                if opp_val is None:
                    setattr(value, "contentfwk_Container243", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "Element241"):
                    opp_val = getattr(item, "Element241", None)
                    
                    if opp_val == self:
                        setattr(item, "Element241", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element241"):
                    opp_val = getattr(item, "Element241", None)
                    
                    setattr(item, "Element241", self)
                    

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
    def Element241(self):
        return self.__Element241

    @Element241.setter
    def Element241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Element__Element241", None)
        self.__Element241 = value
        
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

class TechnologyComponent:

    pass
class Service:

    pass
class Standard:

    pass
class contentfwk_TechnologyComponent(Standard):

    pass
class contentfwk_ApplicationComponent(Standard):

    pass
class contentfwk_DataComponent(Standard):

    pass
class ApplicationComponent:

    pass
class contentfwk_Service(Standard):

    pass
class Element:

    pass
class contentfwk_ServiceQuality(Element):

    pass
class contentfwk_PhysicalApplicationComponent(Element, ApplicationComponent):

    def __init__(self, peakProfileShortTerm: str, peakProfileLongTerm: str, lifeCycleStatus: str, initialLiveDate: date, dateOfLastRelease: date, dateOfNextRelease: date, retirementDate: date, availabilityQualityCharacteristics: str, servicesTimes: str, manageabilityCharacteristics: str, serviceabilityCharacteristics: str, performanceCharacteristics: str, reliabilityCharacteristics: str, recoverabilityCharacteristics: str, locatabilityCharacteristics: str, securityCharacteristics: str, privacyCharacteristics: str, integrityCharacteristics: str, credibilityCharacteristics: str, localizationCharacteristics: str, internationalizationCharacteristics: str, interoperabilityCharacteristics: str, scalabilityCharacteristics: str, portabilityCharacteristics: str, extensibilityCharacteristics: str, capacityCharacteristics: str, throughput: str, throughputPeriod: str, growth: str, growthPeriod: str, PhysicalApplicationComponent: "contentfwk_LogicalApplicationComponent" = None, contentfwk_PhysicalApplicationComponent: "contentfwk_PhysicalTechnologyComponent" = None, PhysicalApplicationComponent251: "contentfwk_Location" = None, contentfwk_PhysicalApplicationComponent272: "contentfwk_PhysicalDataComponent" = None, contentfwk_PhysicalApplicationComponent277: "contentfwk_ApplicationArchitecture" = None, isExtendedByPhysicalApplicationComponents: set["contentfwk_LogicalApplicationComponent"] = None, containsPhysicalApplicationComponents: set["contentfwk_Location"] = None, contentfwk_PhysicalApplicationComponent289: "contentfwk_PhysicalApplicationComponent" = None, contentfwk_PhysicalApplicationComponent287: set["contentfwk_PhysicalApplicationComponent"] = None, contentfwk_PhysicalApplicationComponent291: set["contentfwk_PhysicalDataComponent"] = None, contentfwk_PhysicalApplicationComponent294: set["contentfwk_PhysicalTechnologyComponent"] = None, contentfwk_PhysicalApplicationComponent298: "contentfwk_PhysicalApplicationComponent" = None, contentfwk_PhysicalApplicationComponent296: "contentfwk_PhysicalApplicationComponent" = None):
        self.peakProfileShortTerm = peakProfileShortTerm
        self.peakProfileLongTerm = peakProfileLongTerm
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
        self.PhysicalApplicationComponent = PhysicalApplicationComponent
        self.contentfwk_PhysicalApplicationComponent = contentfwk_PhysicalApplicationComponent
        self.PhysicalApplicationComponent251 = PhysicalApplicationComponent251
        self.contentfwk_PhysicalApplicationComponent272 = contentfwk_PhysicalApplicationComponent272
        self.contentfwk_PhysicalApplicationComponent277 = contentfwk_PhysicalApplicationComponent277
        self.isExtendedByPhysicalApplicationComponents = isExtendedByPhysicalApplicationComponents if isExtendedByPhysicalApplicationComponents is not None else set()
        self.containsPhysicalApplicationComponents = containsPhysicalApplicationComponents if containsPhysicalApplicationComponents is not None else set()
        self.contentfwk_PhysicalApplicationComponent289 = contentfwk_PhysicalApplicationComponent289
        self.contentfwk_PhysicalApplicationComponent287 = contentfwk_PhysicalApplicationComponent287 if contentfwk_PhysicalApplicationComponent287 is not None else set()
        self.contentfwk_PhysicalApplicationComponent291 = contentfwk_PhysicalApplicationComponent291 if contentfwk_PhysicalApplicationComponent291 is not None else set()
        self.contentfwk_PhysicalApplicationComponent294 = contentfwk_PhysicalApplicationComponent294 if contentfwk_PhysicalApplicationComponent294 is not None else set()
        self.contentfwk_PhysicalApplicationComponent298 = contentfwk_PhysicalApplicationComponent298
        self.contentfwk_PhysicalApplicationComponent296 = contentfwk_PhysicalApplicationComponent296
        
    @property
    def locatabilityCharacteristics(self) -> str:
        return self.__locatabilityCharacteristics

    @locatabilityCharacteristics.setter
    def locatabilityCharacteristics(self, locatabilityCharacteristics: str):
        self.__locatabilityCharacteristics = locatabilityCharacteristics

    @property
    def portabilityCharacteristics(self) -> str:
        return self.__portabilityCharacteristics

    @portabilityCharacteristics.setter
    def portabilityCharacteristics(self, portabilityCharacteristics: str):
        self.__portabilityCharacteristics = portabilityCharacteristics

    @property
    def initialLiveDate(self) -> date:
        return self.__initialLiveDate

    @initialLiveDate.setter
    def initialLiveDate(self, initialLiveDate: date):
        self.__initialLiveDate = initialLiveDate

    @property
    def manageabilityCharacteristics(self) -> str:
        return self.__manageabilityCharacteristics

    @manageabilityCharacteristics.setter
    def manageabilityCharacteristics(self, manageabilityCharacteristics: str):
        self.__manageabilityCharacteristics = manageabilityCharacteristics

    @property
    def peakProfileShortTerm(self) -> str:
        return self.__peakProfileShortTerm

    @peakProfileShortTerm.setter
    def peakProfileShortTerm(self, peakProfileShortTerm: str):
        self.__peakProfileShortTerm = peakProfileShortTerm

    @property
    def scalabilityCharacteristics(self) -> str:
        return self.__scalabilityCharacteristics

    @scalabilityCharacteristics.setter
    def scalabilityCharacteristics(self, scalabilityCharacteristics: str):
        self.__scalabilityCharacteristics = scalabilityCharacteristics

    @property
    def privacyCharacteristics(self) -> str:
        return self.__privacyCharacteristics

    @privacyCharacteristics.setter
    def privacyCharacteristics(self, privacyCharacteristics: str):
        self.__privacyCharacteristics = privacyCharacteristics

    @property
    def lifeCycleStatus(self) -> str:
        return self.__lifeCycleStatus

    @lifeCycleStatus.setter
    def lifeCycleStatus(self, lifeCycleStatus: str):
        self.__lifeCycleStatus = lifeCycleStatus

    @property
    def credibilityCharacteristics(self) -> str:
        return self.__credibilityCharacteristics

    @credibilityCharacteristics.setter
    def credibilityCharacteristics(self, credibilityCharacteristics: str):
        self.__credibilityCharacteristics = credibilityCharacteristics

    @property
    def growth(self) -> str:
        return self.__growth

    @growth.setter
    def growth(self, growth: str):
        self.__growth = growth

    @property
    def reliabilityCharacteristics(self) -> str:
        return self.__reliabilityCharacteristics

    @reliabilityCharacteristics.setter
    def reliabilityCharacteristics(self, reliabilityCharacteristics: str):
        self.__reliabilityCharacteristics = reliabilityCharacteristics

    @property
    def localizationCharacteristics(self) -> str:
        return self.__localizationCharacteristics

    @localizationCharacteristics.setter
    def localizationCharacteristics(self, localizationCharacteristics: str):
        self.__localizationCharacteristics = localizationCharacteristics

    @property
    def retirementDate(self) -> date:
        return self.__retirementDate

    @retirementDate.setter
    def retirementDate(self, retirementDate: date):
        self.__retirementDate = retirementDate

    @property
    def internationalizationCharacteristics(self) -> str:
        return self.__internationalizationCharacteristics

    @internationalizationCharacteristics.setter
    def internationalizationCharacteristics(self, internationalizationCharacteristics: str):
        self.__internationalizationCharacteristics = internationalizationCharacteristics

    @property
    def capacityCharacteristics(self) -> str:
        return self.__capacityCharacteristics

    @capacityCharacteristics.setter
    def capacityCharacteristics(self, capacityCharacteristics: str):
        self.__capacityCharacteristics = capacityCharacteristics

    @property
    def availabilityQualityCharacteristics(self) -> str:
        return self.__availabilityQualityCharacteristics

    @availabilityQualityCharacteristics.setter
    def availabilityQualityCharacteristics(self, availabilityQualityCharacteristics: str):
        self.__availabilityQualityCharacteristics = availabilityQualityCharacteristics

    @property
    def dateOfNextRelease(self) -> date:
        return self.__dateOfNextRelease

    @dateOfNextRelease.setter
    def dateOfNextRelease(self, dateOfNextRelease: date):
        self.__dateOfNextRelease = dateOfNextRelease

    @property
    def securityCharacteristics(self) -> str:
        return self.__securityCharacteristics

    @securityCharacteristics.setter
    def securityCharacteristics(self, securityCharacteristics: str):
        self.__securityCharacteristics = securityCharacteristics

    @property
    def throughputPeriod(self) -> str:
        return self.__throughputPeriod

    @throughputPeriod.setter
    def throughputPeriod(self, throughputPeriod: str):
        self.__throughputPeriod = throughputPeriod

    @property
    def integrityCharacteristics(self) -> str:
        return self.__integrityCharacteristics

    @integrityCharacteristics.setter
    def integrityCharacteristics(self, integrityCharacteristics: str):
        self.__integrityCharacteristics = integrityCharacteristics

    @property
    def interoperabilityCharacteristics(self) -> str:
        return self.__interoperabilityCharacteristics

    @interoperabilityCharacteristics.setter
    def interoperabilityCharacteristics(self, interoperabilityCharacteristics: str):
        self.__interoperabilityCharacteristics = interoperabilityCharacteristics

    @property
    def peakProfileLongTerm(self) -> str:
        return self.__peakProfileLongTerm

    @peakProfileLongTerm.setter
    def peakProfileLongTerm(self, peakProfileLongTerm: str):
        self.__peakProfileLongTerm = peakProfileLongTerm

    @property
    def growthPeriod(self) -> str:
        return self.__growthPeriod

    @growthPeriod.setter
    def growthPeriod(self, growthPeriod: str):
        self.__growthPeriod = growthPeriod

    @property
    def dateOfLastRelease(self) -> date:
        return self.__dateOfLastRelease

    @dateOfLastRelease.setter
    def dateOfLastRelease(self, dateOfLastRelease: date):
        self.__dateOfLastRelease = dateOfLastRelease

    @property
    def recoverabilityCharacteristics(self) -> str:
        return self.__recoverabilityCharacteristics

    @recoverabilityCharacteristics.setter
    def recoverabilityCharacteristics(self, recoverabilityCharacteristics: str):
        self.__recoverabilityCharacteristics = recoverabilityCharacteristics

    @property
    def extensibilityCharacteristics(self) -> str:
        return self.__extensibilityCharacteristics

    @extensibilityCharacteristics.setter
    def extensibilityCharacteristics(self, extensibilityCharacteristics: str):
        self.__extensibilityCharacteristics = extensibilityCharacteristics

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
    def throughput(self) -> str:
        return self.__throughput

    @throughput.setter
    def throughput(self, throughput: str):
        self.__throughput = throughput

    @property
    def servicesTimes(self) -> str:
        return self.__servicesTimes

    @servicesTimes.setter
    def servicesTimes(self, servicesTimes: str):
        self.__servicesTimes = servicesTimes

    @property
    def contentfwk_PhysicalApplicationComponent291(self):
        return self.__contentfwk_PhysicalApplicationComponent291

    @contentfwk_PhysicalApplicationComponent291.setter
    def contentfwk_PhysicalApplicationComponent291(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent291", None)
        self.__contentfwk_PhysicalApplicationComponent291 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_PhysicalDataComponent292"):
                    opp_val = getattr(item, "contentfwk_PhysicalDataComponent292", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_PhysicalDataComponent292", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_PhysicalDataComponent292"):
                    opp_val = getattr(item, "contentfwk_PhysicalDataComponent292", None)
                    
                    setattr(item, "contentfwk_PhysicalDataComponent292", self)
                    

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
                if hasattr(item, "Location286"):
                    opp_val = getattr(item, "Location286", None)
                    
                    if opp_val == self:
                        setattr(item, "Location286", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Location286"):
                    opp_val = getattr(item, "Location286", None)
                    
                    setattr(item, "Location286", self)
                    

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
            if hasattr(old_value, "contentfwk_PhysicalTechnologyComponent192"):
                opp_val = getattr(old_value, "contentfwk_PhysicalTechnologyComponent192", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalTechnologyComponent192"):
                opp_val = getattr(value, "contentfwk_PhysicalTechnologyComponent192", None)
                if opp_val is None:
                    setattr(value, "contentfwk_PhysicalTechnologyComponent192", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def contentfwk_PhysicalApplicationComponent272(self):
        return self.__contentfwk_PhysicalApplicationComponent272

    @contentfwk_PhysicalApplicationComponent272.setter
    def contentfwk_PhysicalApplicationComponent272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent272", None)
        self.__contentfwk_PhysicalApplicationComponent272 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalDataComponent271"):
                opp_val = getattr(old_value, "contentfwk_PhysicalDataComponent271", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalDataComponent271"):
                opp_val = getattr(value, "contentfwk_PhysicalDataComponent271", None)
                if opp_val is None:
                    setattr(value, "contentfwk_PhysicalDataComponent271", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PhysicalApplicationComponent251(self):
        return self.__PhysicalApplicationComponent251

    @PhysicalApplicationComponent251.setter
    def PhysicalApplicationComponent251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__PhysicalApplicationComponent251", None)
        self.__PhysicalApplicationComponent251 = value
        
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
        self.__contentfwk_PhysicalApplicationComponent294 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_PhysicalTechnologyComponent295"):
                    opp_val = getattr(item, "contentfwk_PhysicalTechnologyComponent295", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_PhysicalTechnologyComponent295", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_PhysicalTechnologyComponent295"):
                    opp_val = getattr(item, "contentfwk_PhysicalTechnologyComponent295", None)
                    
                    setattr(item, "contentfwk_PhysicalTechnologyComponent295", self)
                    

    @property
    def contentfwk_PhysicalApplicationComponent277(self):
        return self.__contentfwk_PhysicalApplicationComponent277

    @contentfwk_PhysicalApplicationComponent277.setter
    def contentfwk_PhysicalApplicationComponent277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent277", None)
        self.__contentfwk_PhysicalApplicationComponent277 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_ApplicationArchitecture276"):
                opp_val = getattr(old_value, "contentfwk_ApplicationArchitecture276", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_ApplicationArchitecture276"):
                opp_val = getattr(value, "contentfwk_ApplicationArchitecture276", None)
                if opp_val is None:
                    setattr(value, "contentfwk_ApplicationArchitecture276", set([self]))
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
                if hasattr(item, "LogicalApplicationComponent284"):
                    opp_val = getattr(item, "LogicalApplicationComponent284", None)
                    
                    if opp_val == self:
                        setattr(item, "LogicalApplicationComponent284", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LogicalApplicationComponent284"):
                    opp_val = getattr(item, "LogicalApplicationComponent284", None)
                    
                    setattr(item, "LogicalApplicationComponent284", self)
                    

    @property
    def contentfwk_PhysicalApplicationComponent287(self):
        return self.__contentfwk_PhysicalApplicationComponent287

    @contentfwk_PhysicalApplicationComponent287.setter
    def contentfwk_PhysicalApplicationComponent287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent287", None)
        self.__contentfwk_PhysicalApplicationComponent287 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_PhysicalApplicationComponent289"):
                    opp_val = getattr(item, "contentfwk_PhysicalApplicationComponent289", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_PhysicalApplicationComponent289", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_PhysicalApplicationComponent289"):
                    opp_val = getattr(item, "contentfwk_PhysicalApplicationComponent289", None)
                    
                    setattr(item, "contentfwk_PhysicalApplicationComponent289", self)
                    

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
            if hasattr(old_value, "contentfwk_PhysicalApplicationComponent298"):
                opp_val = getattr(old_value, "contentfwk_PhysicalApplicationComponent298", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_PhysicalApplicationComponent298", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalApplicationComponent298"):
                opp_val = getattr(value, "contentfwk_PhysicalApplicationComponent298", None)
                setattr(value, "contentfwk_PhysicalApplicationComponent298", self)

    @property
    def contentfwk_PhysicalApplicationComponent289(self):
        return self.__contentfwk_PhysicalApplicationComponent289

    @contentfwk_PhysicalApplicationComponent289.setter
    def contentfwk_PhysicalApplicationComponent289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent289", None)
        self.__contentfwk_PhysicalApplicationComponent289 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalApplicationComponent287"):
                opp_val = getattr(old_value, "contentfwk_PhysicalApplicationComponent287", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalApplicationComponent287"):
                opp_val = getattr(value, "contentfwk_PhysicalApplicationComponent287", None)
                if opp_val is None:
                    setattr(value, "contentfwk_PhysicalApplicationComponent287", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_PhysicalApplicationComponent298(self):
        return self.__contentfwk_PhysicalApplicationComponent298

    @contentfwk_PhysicalApplicationComponent298.setter
    def contentfwk_PhysicalApplicationComponent298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent298", None)
        self.__contentfwk_PhysicalApplicationComponent298 = value
        
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

class contentfwk_Product(Element):

    pass
class contentfwk_Process(Element, Standard):

    def __init__(self, processCritiality: str, isAutomated: bool, processVolumetrics: str, contentfwk_Process: "contentfwk_BusinessArchitecture" = None, Process: "contentfwk_OrganizationUnit" = None, Process79: "contentfwk_Actor" = None, Process140: "contentfwk_Function" = None, Process142: "contentfwk_Function" = None, participatesInProcesses169: set["contentfwk_Actor"] = None, ensuresCorrectOperationOfProcesses: set["contentfwk_Control"] = None, isResolvedByProcesses: set["contentfwk_Event"] = None, isGeneratedByProcesses: set["contentfwk_Event"] = None, isProducedByProcesses: set["contentfwk_Product"] = None, contentfwk_Process180: "contentfwk_Process" = None, contentfwk_Process178: "contentfwk_Process" = None, Process183: "contentfwk_Process" = None, followsProcesses: set["contentfwk_Process"] = None, isRealizedByProcesses: set["contentfwk_Function"] = None, supportsProcesses: set["contentfwk_Function"] = None, participatesInProcesses: set["contentfwk_OrganizationUnit"] = None, isRealizedByProcesses163: set["contentfwk_Service"] = None, supportsProcesses166: set["contentfwk_Service"] = None, Process207: "contentfwk_Product" = None, Process186: "contentfwk_Process" = None, precedesProcesses: set["contentfwk_Process"] = None, contentfwk_Process188: "contentfwk_EObject" = None, Process226: "contentfwk_Event" = None, Process228: "contentfwk_Event" = None, Process236: "contentfwk_Control" = None, Process335: "contentfwk_Service" = None, Process337: "contentfwk_Service" = None):
        self.processCritiality = processCritiality
        self.isAutomated = isAutomated
        self.processVolumetrics = processVolumetrics
        self.contentfwk_Process = contentfwk_Process
        self.Process = Process
        self.Process79 = Process79
        self.Process140 = Process140
        self.Process142 = Process142
        self.participatesInProcesses169 = participatesInProcesses169 if participatesInProcesses169 is not None else set()
        self.ensuresCorrectOperationOfProcesses = ensuresCorrectOperationOfProcesses if ensuresCorrectOperationOfProcesses is not None else set()
        self.isResolvedByProcesses = isResolvedByProcesses if isResolvedByProcesses is not None else set()
        self.isGeneratedByProcesses = isGeneratedByProcesses if isGeneratedByProcesses is not None else set()
        self.isProducedByProcesses = isProducedByProcesses if isProducedByProcesses is not None else set()
        self.contentfwk_Process180 = contentfwk_Process180
        self.contentfwk_Process178 = contentfwk_Process178
        self.Process183 = Process183
        self.followsProcesses = followsProcesses if followsProcesses is not None else set()
        self.isRealizedByProcesses = isRealizedByProcesses if isRealizedByProcesses is not None else set()
        self.supportsProcesses = supportsProcesses if supportsProcesses is not None else set()
        self.participatesInProcesses = participatesInProcesses if participatesInProcesses is not None else set()
        self.isRealizedByProcesses163 = isRealizedByProcesses163 if isRealizedByProcesses163 is not None else set()
        self.supportsProcesses166 = supportsProcesses166 if supportsProcesses166 is not None else set()
        self.Process207 = Process207
        self.Process186 = Process186
        self.precedesProcesses = precedesProcesses if precedesProcesses is not None else set()
        self.contentfwk_Process188 = contentfwk_Process188
        self.Process226 = Process226
        self.Process228 = Process228
        self.Process236 = Process236
        self.Process335 = Process335
        self.Process337 = Process337
        
    @property
    def processVolumetrics(self) -> str:
        return self.__processVolumetrics

    @processVolumetrics.setter
    def processVolumetrics(self, processVolumetrics: str):
        self.__processVolumetrics = processVolumetrics

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
                if hasattr(item, "Event175"):
                    opp_val = getattr(item, "Event175", None)
                    
                    if opp_val == self:
                        setattr(item, "Event175", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Event175"):
                    opp_val = getattr(item, "Event175", None)
                    
                    setattr(item, "Event175", self)
                    

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
                if hasattr(item, "Event173"):
                    opp_val = getattr(item, "Event173", None)
                    
                    if opp_val == self:
                        setattr(item, "Event173", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Event173"):
                    opp_val = getattr(item, "Event173", None)
                    
                    setattr(item, "Event173", self)
                    

    @property
    def Process337(self):
        return self.__Process337

    @Process337.setter
    def Process337(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process337", None)
        self.__Process337 = value
        
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
                if hasattr(item, "Product177"):
                    opp_val = getattr(item, "Product177", None)
                    
                    if opp_val == self:
                        setattr(item, "Product177", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Product177"):
                    opp_val = getattr(item, "Product177", None)
                    
                    setattr(item, "Product177", self)
                    

    @property
    def contentfwk_Process180(self):
        return self.__contentfwk_Process180

    @contentfwk_Process180.setter
    def contentfwk_Process180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__contentfwk_Process180", None)
        self.__contentfwk_Process180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_Process178"):
                opp_val = getattr(old_value, "contentfwk_Process178", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_Process178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_Process178"):
                opp_val = getattr(value, "contentfwk_Process178", None)
                setattr(value, "contentfwk_Process178", self)

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
                if hasattr(item, "Process183"):
                    opp_val = getattr(item, "Process183", None)
                    
                    if opp_val == self:
                        setattr(item, "Process183", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Process183"):
                    opp_val = getattr(item, "Process183", None)
                    
                    setattr(item, "Process183", self)
                    

    @property
    def contentfwk_Process178(self):
        return self.__contentfwk_Process178

    @contentfwk_Process178.setter
    def contentfwk_Process178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__contentfwk_Process178", None)
        self.__contentfwk_Process178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_Process180"):
                opp_val = getattr(old_value, "contentfwk_Process180", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_Process180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_Process180"):
                opp_val = getattr(value, "contentfwk_Process180", None)
                setattr(value, "contentfwk_Process180", self)

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
                if hasattr(item, "Process186"):
                    opp_val = getattr(item, "Process186", None)
                    
                    if opp_val == self:
                        setattr(item, "Process186", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Process186"):
                    opp_val = getattr(item, "Process186", None)
                    
                    setattr(item, "Process186", self)
                    

    @property
    def Process226(self):
        return self.__Process226

    @Process226.setter
    def Process226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process226", None)
        self.__Process226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resolvesEvents225"):
                opp_val = getattr(old_value, "resolvesEvents225", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resolvesEvents225"):
                opp_val = getattr(value, "resolvesEvents225", None)
                if opp_val is None:
                    setattr(value, "resolvesEvents225", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Process183(self):
        return self.__Process183

    @Process183.setter
    def Process183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process183", None)
        self.__Process183 = value
        
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
    def participatesInProcesses169(self):
        return self.__participatesInProcesses169

    @participatesInProcesses169.setter
    def participatesInProcesses169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__participatesInProcesses169", None)
        self.__participatesInProcesses169 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Actor170"):
                    opp_val = getattr(item, "Actor170", None)
                    
                    if opp_val == self:
                        setattr(item, "Actor170", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Actor170"):
                    opp_val = getattr(item, "Actor170", None)
                    
                    setattr(item, "Actor170", self)
                    

    @property
    def supportsProcesses166(self):
        return self.__supportsProcesses166

    @supportsProcesses166.setter
    def supportsProcesses166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__supportsProcesses166", None)
        self.__supportsProcesses166 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service167"):
                    opp_val = getattr(item, "Service167", None)
                    
                    if opp_val == self:
                        setattr(item, "Service167", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service167"):
                    opp_val = getattr(item, "Service167", None)
                    
                    setattr(item, "Service167", self)
                    

    @property
    def Process186(self):
        return self.__Process186

    @Process186.setter
    def Process186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process186", None)
        self.__Process186 = value
        
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
    def Process207(self):
        return self.__Process207

    @Process207.setter
    def Process207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process207", None)
        self.__Process207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "producesProducts206"):
                opp_val = getattr(old_value, "producesProducts206", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "producesProducts206"):
                opp_val = getattr(value, "producesProducts206", None)
                if opp_val is None:
                    setattr(value, "producesProducts206", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Process228(self):
        return self.__Process228

    @Process228.setter
    def Process228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process228", None)
        self.__Process228 = value
        
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
    def Process140(self):
        return self.__Process140

    @Process140.setter
    def Process140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process140", None)
        self.__Process140 = value
        
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
    def isRealizedByProcesses163(self):
        return self.__isRealizedByProcesses163

    @isRealizedByProcesses163.setter
    def isRealizedByProcesses163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__isRealizedByProcesses163", None)
        self.__isRealizedByProcesses163 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service164"):
                    opp_val = getattr(item, "Service164", None)
                    
                    if opp_val == self:
                        setattr(item, "Service164", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service164"):
                    opp_val = getattr(item, "Service164", None)
                    
                    setattr(item, "Service164", self)
                    

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
                if hasattr(item, "Function157"):
                    opp_val = getattr(item, "Function157", None)
                    
                    if opp_val == self:
                        setattr(item, "Function157", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function157"):
                    opp_val = getattr(item, "Function157", None)
                    
                    setattr(item, "Function157", self)
                    

    @property
    def Process236(self):
        return self.__Process236

    @Process236.setter
    def Process236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process236", None)
        self.__Process236 = value
        
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
                if hasattr(item, "Function159"):
                    opp_val = getattr(item, "Function159", None)
                    
                    if opp_val == self:
                        setattr(item, "Function159", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function159"):
                    opp_val = getattr(item, "Function159", None)
                    
                    setattr(item, "Function159", self)
                    

    @property
    def contentfwk_Process188(self):
        return self.__contentfwk_Process188

    @contentfwk_Process188.setter
    def contentfwk_Process188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__contentfwk_Process188", None)
        self.__contentfwk_Process188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_EObject189"):
                opp_val = getattr(old_value, "contentfwk_EObject189", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_EObject189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_EObject189"):
                opp_val = getattr(value, "contentfwk_EObject189", None)
                setattr(value, "contentfwk_EObject189", self)

    @property
    def Process142(self):
        return self.__Process142

    @Process142.setter
    def Process142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process142", None)
        self.__Process142 = value
        
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
                if hasattr(item, "OrganizationUnit161"):
                    opp_val = getattr(item, "OrganizationUnit161", None)
                    
                    if opp_val == self:
                        setattr(item, "OrganizationUnit161", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OrganizationUnit161"):
                    opp_val = getattr(item, "OrganizationUnit161", None)
                    
                    setattr(item, "OrganizationUnit161", self)
                    

class contentfwk_LogicalApplicationComponent(Element, ApplicationComponent):

    pass
class contentfwk_BusinessService(Element, Service):

    pass
class contentfwk_Event(Element):

    pass
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

class contentfwk_Contract(Element):

    def __init__(self, reliabilityCharacteristics: str, qualityOfInformationRequired: str, contractControlRequirements: str, resultControlRequirements: str, recoverabilityCharacteristics: str, locatabilityCharacteristics: str, securityCharacteristics: str, privacyCharacteristics: str, integrityCharacteristics: str, credibilityCharacteristics: str, localizationCharacteristics: str, internationalizationCharacteristics: str, interoperabilityCharacteristics: str, scalabilityCharacteristics: str, portabilityCharacteristics: str, extensibilityCharacteristics: str, capacityCharacteristics: str, throughput: str, throughputPeriod: str, growth: str, growthPeriod: str, peakProfileShortTerm: str, peakProfileLongTerm: str, behaviorCharacteristics: str, ServiceNameCaller: str, ServiceNameCalled: str, serviceQualityCharacteristics: str, availabilityQualityCharacteristics: str, servicesTimes: str, manageabilityCharacteristics: str, serviceabilityCharacteristics: str, performanceCharacteristics: str, responseCharacteristics: str, contentfwk_Contract: "contentfwk_BusinessArchitecture" = None, Contract: "contentfwk_ServiceQuality" = None, isGovernedAndMeasuredByContracts: set["contentfwk_Service"] = None, appliesToContracts: set["contentfwk_ServiceQuality"] = None, Contract323: "contentfwk_Service" = None):
        self.reliabilityCharacteristics = reliabilityCharacteristics
        self.qualityOfInformationRequired = qualityOfInformationRequired
        self.contractControlRequirements = contractControlRequirements
        self.resultControlRequirements = resultControlRequirements
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
        self.contentfwk_Contract = contentfwk_Contract
        self.Contract = Contract
        self.isGovernedAndMeasuredByContracts = isGovernedAndMeasuredByContracts if isGovernedAndMeasuredByContracts is not None else set()
        self.appliesToContracts = appliesToContracts if appliesToContracts is not None else set()
        self.Contract323 = Contract323
        
    @property
    def responseCharacteristics(self) -> str:
        return self.__responseCharacteristics

    @responseCharacteristics.setter
    def responseCharacteristics(self, responseCharacteristics: str):
        self.__responseCharacteristics = responseCharacteristics

    @property
    def privacyCharacteristics(self) -> str:
        return self.__privacyCharacteristics

    @privacyCharacteristics.setter
    def privacyCharacteristics(self, privacyCharacteristics: str):
        self.__privacyCharacteristics = privacyCharacteristics

    @property
    def growthPeriod(self) -> str:
        return self.__growthPeriod

    @growthPeriod.setter
    def growthPeriod(self, growthPeriod: str):
        self.__growthPeriod = growthPeriod

    @property
    def contractControlRequirements(self) -> str:
        return self.__contractControlRequirements

    @contractControlRequirements.setter
    def contractControlRequirements(self, contractControlRequirements: str):
        self.__contractControlRequirements = contractControlRequirements

    @property
    def servicesTimes(self) -> str:
        return self.__servicesTimes

    @servicesTimes.setter
    def servicesTimes(self, servicesTimes: str):
        self.__servicesTimes = servicesTimes

    @property
    def portabilityCharacteristics(self) -> str:
        return self.__portabilityCharacteristics

    @portabilityCharacteristics.setter
    def portabilityCharacteristics(self, portabilityCharacteristics: str):
        self.__portabilityCharacteristics = portabilityCharacteristics

    @property
    def peakProfileLongTerm(self) -> str:
        return self.__peakProfileLongTerm

    @peakProfileLongTerm.setter
    def peakProfileLongTerm(self, peakProfileLongTerm: str):
        self.__peakProfileLongTerm = peakProfileLongTerm

    @property
    def locatabilityCharacteristics(self) -> str:
        return self.__locatabilityCharacteristics

    @locatabilityCharacteristics.setter
    def locatabilityCharacteristics(self, locatabilityCharacteristics: str):
        self.__locatabilityCharacteristics = locatabilityCharacteristics

    @property
    def ServiceNameCaller(self) -> str:
        return self.__ServiceNameCaller

    @ServiceNameCaller.setter
    def ServiceNameCaller(self, ServiceNameCaller: str):
        self.__ServiceNameCaller = ServiceNameCaller

    @property
    def resultControlRequirements(self) -> str:
        return self.__resultControlRequirements

    @resultControlRequirements.setter
    def resultControlRequirements(self, resultControlRequirements: str):
        self.__resultControlRequirements = resultControlRequirements

    @property
    def recoverabilityCharacteristics(self) -> str:
        return self.__recoverabilityCharacteristics

    @recoverabilityCharacteristics.setter
    def recoverabilityCharacteristics(self, recoverabilityCharacteristics: str):
        self.__recoverabilityCharacteristics = recoverabilityCharacteristics

    @property
    def peakProfileShortTerm(self) -> str:
        return self.__peakProfileShortTerm

    @peakProfileShortTerm.setter
    def peakProfileShortTerm(self, peakProfileShortTerm: str):
        self.__peakProfileShortTerm = peakProfileShortTerm

    @property
    def reliabilityCharacteristics(self) -> str:
        return self.__reliabilityCharacteristics

    @reliabilityCharacteristics.setter
    def reliabilityCharacteristics(self, reliabilityCharacteristics: str):
        self.__reliabilityCharacteristics = reliabilityCharacteristics

    @property
    def ServiceNameCalled(self) -> str:
        return self.__ServiceNameCalled

    @ServiceNameCalled.setter
    def ServiceNameCalled(self, ServiceNameCalled: str):
        self.__ServiceNameCalled = ServiceNameCalled

    @property
    def scalabilityCharacteristics(self) -> str:
        return self.__scalabilityCharacteristics

    @scalabilityCharacteristics.setter
    def scalabilityCharacteristics(self, scalabilityCharacteristics: str):
        self.__scalabilityCharacteristics = scalabilityCharacteristics

    @property
    def integrityCharacteristics(self) -> str:
        return self.__integrityCharacteristics

    @integrityCharacteristics.setter
    def integrityCharacteristics(self, integrityCharacteristics: str):
        self.__integrityCharacteristics = integrityCharacteristics

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
    def growth(self) -> str:
        return self.__growth

    @growth.setter
    def growth(self, growth: str):
        self.__growth = growth

    @property
    def serviceabilityCharacteristics(self) -> str:
        return self.__serviceabilityCharacteristics

    @serviceabilityCharacteristics.setter
    def serviceabilityCharacteristics(self, serviceabilityCharacteristics: str):
        self.__serviceabilityCharacteristics = serviceabilityCharacteristics

    @property
    def internationalizationCharacteristics(self) -> str:
        return self.__internationalizationCharacteristics

    @internationalizationCharacteristics.setter
    def internationalizationCharacteristics(self, internationalizationCharacteristics: str):
        self.__internationalizationCharacteristics = internationalizationCharacteristics

    @property
    def serviceQualityCharacteristics(self) -> str:
        return self.__serviceQualityCharacteristics

    @serviceQualityCharacteristics.setter
    def serviceQualityCharacteristics(self, serviceQualityCharacteristics: str):
        self.__serviceQualityCharacteristics = serviceQualityCharacteristics

    @property
    def capacityCharacteristics(self) -> str:
        return self.__capacityCharacteristics

    @capacityCharacteristics.setter
    def capacityCharacteristics(self, capacityCharacteristics: str):
        self.__capacityCharacteristics = capacityCharacteristics

    @property
    def qualityOfInformationRequired(self) -> str:
        return self.__qualityOfInformationRequired

    @qualityOfInformationRequired.setter
    def qualityOfInformationRequired(self, qualityOfInformationRequired: str):
        self.__qualityOfInformationRequired = qualityOfInformationRequired

    @property
    def throughput(self) -> str:
        return self.__throughput

    @throughput.setter
    def throughput(self, throughput: str):
        self.__throughput = throughput

    @property
    def interoperabilityCharacteristics(self) -> str:
        return self.__interoperabilityCharacteristics

    @interoperabilityCharacteristics.setter
    def interoperabilityCharacteristics(self, interoperabilityCharacteristics: str):
        self.__interoperabilityCharacteristics = interoperabilityCharacteristics

    @property
    def behaviorCharacteristics(self) -> str:
        return self.__behaviorCharacteristics

    @behaviorCharacteristics.setter
    def behaviorCharacteristics(self, behaviorCharacteristics: str):
        self.__behaviorCharacteristics = behaviorCharacteristics

    @property
    def performanceCharacteristics(self) -> str:
        return self.__performanceCharacteristics

    @performanceCharacteristics.setter
    def performanceCharacteristics(self, performanceCharacteristics: str):
        self.__performanceCharacteristics = performanceCharacteristics

    @property
    def credibilityCharacteristics(self) -> str:
        return self.__credibilityCharacteristics

    @credibilityCharacteristics.setter
    def credibilityCharacteristics(self, credibilityCharacteristics: str):
        self.__credibilityCharacteristics = credibilityCharacteristics

    @property
    def manageabilityCharacteristics(self) -> str:
        return self.__manageabilityCharacteristics

    @manageabilityCharacteristics.setter
    def manageabilityCharacteristics(self, manageabilityCharacteristics: str):
        self.__manageabilityCharacteristics = manageabilityCharacteristics

    @property
    def availabilityQualityCharacteristics(self) -> str:
        return self.__availabilityQualityCharacteristics

    @availabilityQualityCharacteristics.setter
    def availabilityQualityCharacteristics(self, availabilityQualityCharacteristics: str):
        self.__availabilityQualityCharacteristics = availabilityQualityCharacteristics

    @property
    def extensibilityCharacteristics(self) -> str:
        return self.__extensibilityCharacteristics

    @extensibilityCharacteristics.setter
    def extensibilityCharacteristics(self, extensibilityCharacteristics: str):
        self.__extensibilityCharacteristics = extensibilityCharacteristics

    @property
    def throughputPeriod(self) -> str:
        return self.__throughputPeriod

    @throughputPeriod.setter
    def throughputPeriod(self, throughputPeriod: str):
        self.__throughputPeriod = throughputPeriod

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
                if hasattr(item, "Service220"):
                    opp_val = getattr(item, "Service220", None)
                    
                    if opp_val == self:
                        setattr(item, "Service220", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service220"):
                    opp_val = getattr(item, "Service220", None)
                    
                    setattr(item, "Service220", self)
                    

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
    def Contract323(self):
        return self.__Contract323

    @Contract323.setter
    def Contract323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Contract__Contract323", None)
        self.__Contract323 = value
        
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

class contentfwk_Measure(Element):

    pass
class contentfwk_Control(Element):

    pass
class contentfwk_StrategicElement(Element):

    pass
class contentfwk_Location(Element):

    pass
class contentfwk_InformationSystemService(Element, Service):

    pass
class contentfwk_LogicalTechnologyComponent(Element, TechnologyComponent):

    pass
class contentfwk_PhysicalTechnologyComponent(Element, TechnologyComponent):

    def __init__(self, vendor: str, version: str, productName: str, moduleName: str, contentfwk_PhysicalTechnologyComponent: "contentfwk_TechnologyArchitecture" = None, contentfwk_PhysicalTechnologyComponent199: "contentfwk_PhysicalTechnologyComponent" = None, contentfwk_PhysicalTechnologyComponent197: "contentfwk_PhysicalTechnologyComponent" = None, contentfwk_PhysicalTechnologyComponent202: "contentfwk_PhysicalTechnologyComponent" = None, contentfwk_PhysicalTechnologyComponent200: set["contentfwk_PhysicalTechnologyComponent"] = None, contentfwk_PhysicalTechnologyComponent192: set["contentfwk_PhysicalApplicationComponent"] = None, isRealizedByPhysicalTechnologyComponents: set["contentfwk_LogicalTechnologyComponent"] = None, containsPhysicalTechnologyComponents: set["contentfwk_Location"] = None, PhysicalTechnologyComponent: "contentfwk_Location" = None, contentfwk_PhysicalTechnologyComponent295: "contentfwk_PhysicalApplicationComponent" = None, PhysicalTechnologyComponent303: "contentfwk_LogicalTechnologyComponent" = None):
        self.vendor = vendor
        self.version = version
        self.productName = productName
        self.moduleName = moduleName
        self.contentfwk_PhysicalTechnologyComponent = contentfwk_PhysicalTechnologyComponent
        self.contentfwk_PhysicalTechnologyComponent199 = contentfwk_PhysicalTechnologyComponent199
        self.contentfwk_PhysicalTechnologyComponent197 = contentfwk_PhysicalTechnologyComponent197
        self.contentfwk_PhysicalTechnologyComponent202 = contentfwk_PhysicalTechnologyComponent202
        self.contentfwk_PhysicalTechnologyComponent200 = contentfwk_PhysicalTechnologyComponent200 if contentfwk_PhysicalTechnologyComponent200 is not None else set()
        self.contentfwk_PhysicalTechnologyComponent192 = contentfwk_PhysicalTechnologyComponent192 if contentfwk_PhysicalTechnologyComponent192 is not None else set()
        self.isRealizedByPhysicalTechnologyComponents = isRealizedByPhysicalTechnologyComponents if isRealizedByPhysicalTechnologyComponents is not None else set()
        self.containsPhysicalTechnologyComponents = containsPhysicalTechnologyComponents if containsPhysicalTechnologyComponents is not None else set()
        self.PhysicalTechnologyComponent = PhysicalTechnologyComponent
        self.contentfwk_PhysicalTechnologyComponent295 = contentfwk_PhysicalTechnologyComponent295
        self.PhysicalTechnologyComponent303 = PhysicalTechnologyComponent303
        
    @property
    def moduleName(self) -> str:
        return self.__moduleName

    @moduleName.setter
    def moduleName(self, moduleName: str):
        self.__moduleName = moduleName

    @property
    def productName(self) -> str:
        return self.__productName

    @productName.setter
    def productName(self, productName: str):
        self.__productName = productName

    @property
    def vendor(self) -> str:
        return self.__vendor

    @vendor.setter
    def vendor(self, vendor: str):
        self.__vendor = vendor

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

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
                if hasattr(item, "LogicalTechnologyComponent194"):
                    opp_val = getattr(item, "LogicalTechnologyComponent194", None)
                    
                    if opp_val == self:
                        setattr(item, "LogicalTechnologyComponent194", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LogicalTechnologyComponent194"):
                    opp_val = getattr(item, "LogicalTechnologyComponent194", None)
                    
                    setattr(item, "LogicalTechnologyComponent194", self)
                    

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
                if hasattr(item, "Location196"):
                    opp_val = getattr(item, "Location196", None)
                    
                    if opp_val == self:
                        setattr(item, "Location196", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Location196"):
                    opp_val = getattr(item, "Location196", None)
                    
                    setattr(item, "Location196", self)
                    

    @property
    def contentfwk_PhysicalTechnologyComponent192(self):
        return self.__contentfwk_PhysicalTechnologyComponent192

    @contentfwk_PhysicalTechnologyComponent192.setter
    def contentfwk_PhysicalTechnologyComponent192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent192", None)
        self.__contentfwk_PhysicalTechnologyComponent192 = value if value is not None else set()
        
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
    def PhysicalTechnologyComponent(self):
        return self.__PhysicalTechnologyComponent

    @PhysicalTechnologyComponent.setter
    def PhysicalTechnologyComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__PhysicalTechnologyComponent", None)
        self.__PhysicalTechnologyComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isHostedInLocation253"):
                opp_val = getattr(old_value, "isHostedInLocation253", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isHostedInLocation253"):
                opp_val = getattr(value, "isHostedInLocation253", None)
                if opp_val is None:
                    setattr(value, "isHostedInLocation253", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_PhysicalTechnologyComponent197(self):
        return self.__contentfwk_PhysicalTechnologyComponent197

    @contentfwk_PhysicalTechnologyComponent197.setter
    def contentfwk_PhysicalTechnologyComponent197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent197", None)
        self.__contentfwk_PhysicalTechnologyComponent197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalTechnologyComponent199"):
                opp_val = getattr(old_value, "contentfwk_PhysicalTechnologyComponent199", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_PhysicalTechnologyComponent199", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalTechnologyComponent199"):
                opp_val = getattr(value, "contentfwk_PhysicalTechnologyComponent199", None)
                setattr(value, "contentfwk_PhysicalTechnologyComponent199", self)

    @property
    def contentfwk_PhysicalTechnologyComponent295(self):
        return self.__contentfwk_PhysicalTechnologyComponent295

    @contentfwk_PhysicalTechnologyComponent295.setter
    def contentfwk_PhysicalTechnologyComponent295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent295", None)
        self.__contentfwk_PhysicalTechnologyComponent295 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalApplicationComponent294"):
                opp_val = getattr(old_value, "contentfwk_PhysicalApplicationComponent294", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalApplicationComponent294"):
                opp_val = getattr(value, "contentfwk_PhysicalApplicationComponent294", None)
                if opp_val is None:
                    setattr(value, "contentfwk_PhysicalApplicationComponent294", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def PhysicalTechnologyComponent303(self):
        return self.__PhysicalTechnologyComponent303

    @PhysicalTechnologyComponent303.setter
    def PhysicalTechnologyComponent303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__PhysicalTechnologyComponent303", None)
        self.__PhysicalTechnologyComponent303 = value
        
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
    def contentfwk_PhysicalTechnologyComponent199(self):
        return self.__contentfwk_PhysicalTechnologyComponent199

    @contentfwk_PhysicalTechnologyComponent199.setter
    def contentfwk_PhysicalTechnologyComponent199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent199", None)
        self.__contentfwk_PhysicalTechnologyComponent199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalTechnologyComponent197"):
                opp_val = getattr(old_value, "contentfwk_PhysicalTechnologyComponent197", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_PhysicalTechnologyComponent197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalTechnologyComponent197"):
                opp_val = getattr(value, "contentfwk_PhysicalTechnologyComponent197", None)
                setattr(value, "contentfwk_PhysicalTechnologyComponent197", self)

    @property
    def contentfwk_PhysicalTechnologyComponent202(self):
        return self.__contentfwk_PhysicalTechnologyComponent202

    @contentfwk_PhysicalTechnologyComponent202.setter
    def contentfwk_PhysicalTechnologyComponent202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent202", None)
        self.__contentfwk_PhysicalTechnologyComponent202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalTechnologyComponent200"):
                opp_val = getattr(old_value, "contentfwk_PhysicalTechnologyComponent200", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalTechnologyComponent200"):
                opp_val = getattr(value, "contentfwk_PhysicalTechnologyComponent200", None)
                if opp_val is None:
                    setattr(value, "contentfwk_PhysicalTechnologyComponent200", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_PhysicalTechnologyComponent200(self):
        return self.__contentfwk_PhysicalTechnologyComponent200

    @contentfwk_PhysicalTechnologyComponent200.setter
    def contentfwk_PhysicalTechnologyComponent200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent200", None)
        self.__contentfwk_PhysicalTechnologyComponent200 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_PhysicalTechnologyComponent202"):
                    opp_val = getattr(item, "contentfwk_PhysicalTechnologyComponent202", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_PhysicalTechnologyComponent202", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_PhysicalTechnologyComponent202"):
                    opp_val = getattr(item, "contentfwk_PhysicalTechnologyComponent202", None)
                    
                    setattr(item, "contentfwk_PhysicalTechnologyComponent202", self)
                    

class contentfwk_PlatformService(Element, Service):

    pass
class contentfwk_PhysicalDataComponent(DataComponent, Element):

    pass
class contentfwk_LogicalDataComponent(DataComponent, Element):

    pass
class contentfwk_DataEntity(Element):

    def __init__(self, dataEntityCategory: str, privacyClassification: str, retentionClassification: str, contentfwk_DataEntity: "contentfwk_DataArchitecture" = None, DataEntity: "contentfwk_Actor" = None, DataEntity72: "contentfwk_Actor" = None, suppliesEntities: set["contentfwk_Actor"] = None, consumesEntities: set["contentfwk_Actor"] = None, consumesEntities105: set["contentfwk_Service"] = None, DataEntity123: "contentfwk_LogicalApplicationComponent" = None, providesEntities: set["contentfwk_Service"] = None, encapsulatesDataEntities: "contentfwk_LogicalDataComponent" = None, operatesOnDataEntities: set["contentfwk_LogicalApplicationComponent"] = None, contentfwk_DataEntity113: "contentfwk_DataEntity" = None, contentfwk_DataEntity111: "contentfwk_DataEntity" = None, contentfwk_DataEntity116: "contentfwk_DataEntity" = None, contentfwk_DataEntity114: set["contentfwk_DataEntity"] = None, contentfwk_DataEntity118: "contentfwk_EObject" = None, DataEntity260: "contentfwk_LogicalDataComponent" = None, DataEntity319: "contentfwk_Service" = None, DataEntity321: "contentfwk_Service" = None):
        self.dataEntityCategory = dataEntityCategory
        self.privacyClassification = privacyClassification
        self.retentionClassification = retentionClassification
        self.contentfwk_DataEntity = contentfwk_DataEntity
        self.DataEntity = DataEntity
        self.DataEntity72 = DataEntity72
        self.suppliesEntities = suppliesEntities if suppliesEntities is not None else set()
        self.consumesEntities = consumesEntities if consumesEntities is not None else set()
        self.consumesEntities105 = consumesEntities105 if consumesEntities105 is not None else set()
        self.DataEntity123 = DataEntity123
        self.providesEntities = providesEntities if providesEntities is not None else set()
        self.encapsulatesDataEntities = encapsulatesDataEntities
        self.operatesOnDataEntities = operatesOnDataEntities if operatesOnDataEntities is not None else set()
        self.contentfwk_DataEntity113 = contentfwk_DataEntity113
        self.contentfwk_DataEntity111 = contentfwk_DataEntity111
        self.contentfwk_DataEntity116 = contentfwk_DataEntity116
        self.contentfwk_DataEntity114 = contentfwk_DataEntity114 if contentfwk_DataEntity114 is not None else set()
        self.contentfwk_DataEntity118 = contentfwk_DataEntity118
        self.DataEntity260 = DataEntity260
        self.DataEntity319 = DataEntity319
        self.DataEntity321 = DataEntity321
        
    @property
    def privacyClassification(self) -> str:
        return self.__privacyClassification

    @privacyClassification.setter
    def privacyClassification(self, privacyClassification: str):
        self.__privacyClassification = privacyClassification

    @property
    def dataEntityCategory(self) -> str:
        return self.__dataEntityCategory

    @dataEntityCategory.setter
    def dataEntityCategory(self, dataEntityCategory: str):
        self.__dataEntityCategory = dataEntityCategory

    @property
    def retentionClassification(self) -> str:
        return self.__retentionClassification

    @retentionClassification.setter
    def retentionClassification(self, retentionClassification: str):
        self.__retentionClassification = retentionClassification

    @property
    def DataEntity260(self):
        return self.__DataEntity260

    @DataEntity260.setter
    def DataEntity260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__DataEntity260", None)
        self.__DataEntity260 = value
        
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
    def DataEntity321(self):
        return self.__DataEntity321

    @DataEntity321.setter
    def DataEntity321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__DataEntity321", None)
        self.__DataEntity321 = value
        
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
    def DataEntity319(self):
        return self.__DataEntity319

    @DataEntity319.setter
    def DataEntity319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__DataEntity319", None)
        self.__DataEntity319 = value
        
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
    def DataEntity123(self):
        return self.__DataEntity123

    @DataEntity123.setter
    def DataEntity123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__DataEntity123", None)
        self.__DataEntity123 = value
        
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

    @property
    def contentfwk_DataEntity118(self):
        return self.__contentfwk_DataEntity118

    @contentfwk_DataEntity118.setter
    def contentfwk_DataEntity118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__contentfwk_DataEntity118", None)
        self.__contentfwk_DataEntity118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_EObject119"):
                opp_val = getattr(old_value, "contentfwk_EObject119", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_EObject119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_EObject119"):
                opp_val = getattr(value, "contentfwk_EObject119", None)
                setattr(value, "contentfwk_EObject119", self)

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
                    

class contentfwk_Architecture(ABC):

    pass
class contentfwk_EnterpriseArchitecture:

    pass
class contentfwk_Function(Element, Standard):

    pass
class contentfwk_Role(Element):

    def __init__(self, estimatedFTEs: str, contentfwk_Role: "contentfwk_BusinessArchitecture" = None, Role: "contentfwk_Actor" = None, performsTaskInRoles: set["contentfwk_Actor"] = None, canBeAccessedByRoles: set["contentfwk_Function"] = None, contentfwk_Role99: "contentfwk_Role" = None, contentfwk_Role97: "contentfwk_Role" = None, Role144: "contentfwk_Function" = None):
        self.estimatedFTEs = estimatedFTEs
        self.contentfwk_Role = contentfwk_Role
        self.Role = Role
        self.performsTaskInRoles = performsTaskInRoles if performsTaskInRoles is not None else set()
        self.canBeAccessedByRoles = canBeAccessedByRoles if canBeAccessedByRoles is not None else set()
        self.contentfwk_Role99 = contentfwk_Role99
        self.contentfwk_Role97 = contentfwk_Role97
        self.Role144 = Role144
        
    @property
    def estimatedFTEs(self) -> str:
        return self.__estimatedFTEs

    @estimatedFTEs.setter
    def estimatedFTEs(self, estimatedFTEs: str):
        self.__estimatedFTEs = estimatedFTEs

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
    def Role144(self):
        return self.__Role144

    @Role144.setter
    def Role144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Role__Role144", None)
        self.__Role144 = value
        
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

class contentfwk_Actor(Element):

    def __init__(self, FTEs: str, actorGoal: str, actorTasks: str, contentfwk_Actor: "contentfwk_BusinessArchitecture" = None, isSuppliedByActors: set["contentfwk_DataEntity"] = None, isConsumedByActors: set["contentfwk_DataEntity"] = None, containsActors: "contentfwk_OrganizationUnit" = None, supportsActors: set["contentfwk_Function"] = None, isAssumedByActors: set["contentfwk_Role"] = None, Actor: "contentfwk_OrganizationUnit" = None, Actor94: "contentfwk_Role" = None, Actor101: "contentfwk_DataEntity" = None, Actor103: "contentfwk_DataEntity" = None, involvesActors: set["contentfwk_Process"] = None, contentfwk_Actor81: set["contentfwk_Service"] = None, isResolvedByActors: set["contentfwk_Event"] = None, isGeneratedByActors: set["contentfwk_Event"] = None, containsActors86: "contentfwk_Location" = None, isPerformedByActors: set["contentfwk_Function"] = None, contentfwk_Actor92: "contentfwk_Actor" = None, contentfwk_Actor90: set["contentfwk_Actor"] = None, Actor146: "contentfwk_Function" = None, Actor134: "contentfwk_Function" = None, Actor170: "contentfwk_Process" = None, Actor245: "contentfwk_Location" = None, Actor231: "contentfwk_Event" = None, Actor234: "contentfwk_Event" = None, contentfwk_Actor315: "contentfwk_Service" = None):
        self.FTEs = FTEs
        self.actorGoal = actorGoal
        self.actorTasks = actorTasks
        self.contentfwk_Actor = contentfwk_Actor
        self.isSuppliedByActors = isSuppliedByActors if isSuppliedByActors is not None else set()
        self.isConsumedByActors = isConsumedByActors if isConsumedByActors is not None else set()
        self.containsActors = containsActors
        self.supportsActors = supportsActors if supportsActors is not None else set()
        self.isAssumedByActors = isAssumedByActors if isAssumedByActors is not None else set()
        self.Actor = Actor
        self.Actor94 = Actor94
        self.Actor101 = Actor101
        self.Actor103 = Actor103
        self.involvesActors = involvesActors if involvesActors is not None else set()
        self.contentfwk_Actor81 = contentfwk_Actor81 if contentfwk_Actor81 is not None else set()
        self.isResolvedByActors = isResolvedByActors if isResolvedByActors is not None else set()
        self.isGeneratedByActors = isGeneratedByActors if isGeneratedByActors is not None else set()
        self.containsActors86 = containsActors86
        self.isPerformedByActors = isPerformedByActors if isPerformedByActors is not None else set()
        self.contentfwk_Actor92 = contentfwk_Actor92
        self.contentfwk_Actor90 = contentfwk_Actor90 if contentfwk_Actor90 is not None else set()
        self.Actor146 = Actor146
        self.Actor134 = Actor134
        self.Actor170 = Actor170
        self.Actor245 = Actor245
        self.Actor231 = Actor231
        self.Actor234 = Actor234
        self.contentfwk_Actor315 = contentfwk_Actor315
        
    @property
    def actorTasks(self) -> str:
        return self.__actorTasks

    @actorTasks.setter
    def actorTasks(self, actorTasks: str):
        self.__actorTasks = actorTasks

    @property
    def FTEs(self) -> str:
        return self.__FTEs

    @FTEs.setter
    def FTEs(self, FTEs: str):
        self.__FTEs = FTEs

    @property
    def actorGoal(self) -> str:
        return self.__actorGoal

    @actorGoal.setter
    def actorGoal(self, actorGoal: str):
        self.__actorGoal = actorGoal

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
    def Actor170(self):
        return self.__Actor170

    @Actor170.setter
    def Actor170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor170", None)
        self.__Actor170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "participatesInProcesses169"):
                opp_val = getattr(old_value, "participatesInProcesses169", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "participatesInProcesses169"):
                opp_val = getattr(value, "participatesInProcesses169", None)
                if opp_val is None:
                    setattr(value, "participatesInProcesses169", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Actor234(self):
        return self.__Actor234

    @Actor234.setter
    def Actor234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor234", None)
        self.__Actor234 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generatesEvents233"):
                opp_val = getattr(old_value, "generatesEvents233", None)
                if opp_val == self:
                    setattr(old_value, "generatesEvents233", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generatesEvents233"):
                opp_val = getattr(value, "generatesEvents233", None)
                setattr(value, "generatesEvents233", self)

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
    def Actor146(self):
        return self.__Actor146

    @Actor146.setter
    def Actor146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor146", None)
        self.__Actor146 = value
        
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
    def Actor245(self):
        return self.__Actor245

    @Actor245.setter
    def Actor245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor245", None)
        self.__Actor245 = value
        
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
    def contentfwk_Actor315(self):
        return self.__contentfwk_Actor315

    @contentfwk_Actor315.setter
    def contentfwk_Actor315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__contentfwk_Actor315", None)
        self.__contentfwk_Actor315 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_Service314"):
                opp_val = getattr(old_value, "contentfwk_Service314", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_Service314"):
                opp_val = getattr(value, "contentfwk_Service314", None)
                if opp_val is None:
                    setattr(value, "contentfwk_Service314", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def Actor134(self):
        return self.__Actor134

    @Actor134.setter
    def Actor134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor134", None)
        self.__Actor134 = value
        
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
    def Actor231(self):
        return self.__Actor231

    @Actor231.setter
    def Actor231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor231", None)
        self.__Actor231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resolvesEvents230"):
                opp_val = getattr(old_value, "resolvesEvents230", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resolvesEvents230"):
                opp_val = getattr(value, "resolvesEvents230", None)
                if opp_val is None:
                    setattr(value, "resolvesEvents230", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class contentfwk_OrganizationUnit(Element):

    def __init__(self, headcount: str, contentfwk_OrganizationUnit: "contentfwk_BusinessArchitecture" = None, OrganizationUnit: "contentfwk_Driver" = None, involvesOrganizationUnits: set["contentfwk_Process"] = None, motivatesOrganizationUnits: set["contentfwk_Driver"] = None, isProducedByOrganizationUnits: set["contentfwk_Product"] = None, containsOrganizationUnits: "contentfwk_Location" = None, OrganizationUnit74: "contentfwk_Actor" = None, isOwnedAndGovernedByOrganizationUnits: set["contentfwk_Service"] = None, belongsTo: set["contentfwk_Actor"] = None, isOwnedByUnit: set["contentfwk_Function"] = None, OrganizationUnit136: "contentfwk_Function" = None, OrganizationUnit161: "contentfwk_Process" = None, OrganizationUnit204: "contentfwk_Product" = None, OrganizationUnit248: "contentfwk_Location" = None, OrganizationUnit331: "contentfwk_Service" = None):
        self.headcount = headcount
        self.contentfwk_OrganizationUnit = contentfwk_OrganizationUnit
        self.OrganizationUnit = OrganizationUnit
        self.involvesOrganizationUnits = involvesOrganizationUnits if involvesOrganizationUnits is not None else set()
        self.motivatesOrganizationUnits = motivatesOrganizationUnits if motivatesOrganizationUnits is not None else set()
        self.isProducedByOrganizationUnits = isProducedByOrganizationUnits if isProducedByOrganizationUnits is not None else set()
        self.containsOrganizationUnits = containsOrganizationUnits
        self.OrganizationUnit74 = OrganizationUnit74
        self.isOwnedAndGovernedByOrganizationUnits = isOwnedAndGovernedByOrganizationUnits if isOwnedAndGovernedByOrganizationUnits is not None else set()
        self.belongsTo = belongsTo if belongsTo is not None else set()
        self.isOwnedByUnit = isOwnedByUnit if isOwnedByUnit is not None else set()
        self.OrganizationUnit136 = OrganizationUnit136
        self.OrganizationUnit161 = OrganizationUnit161
        self.OrganizationUnit204 = OrganizationUnit204
        self.OrganizationUnit248 = OrganizationUnit248
        self.OrganizationUnit331 = OrganizationUnit331
        
    @property
    def headcount(self) -> str:
        return self.__headcount

    @headcount.setter
    def headcount(self, headcount: str):
        self.__headcount = headcount

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
    def OrganizationUnit331(self):
        return self.__OrganizationUnit331

    @OrganizationUnit331.setter
    def OrganizationUnit331(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit331", None)
        self.__OrganizationUnit331 = value
        
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
    def OrganizationUnit136(self):
        return self.__OrganizationUnit136

    @OrganizationUnit136.setter
    def OrganizationUnit136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit136", None)
        self.__OrganizationUnit136 = value
        
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
    def OrganizationUnit161(self):
        return self.__OrganizationUnit161

    @OrganizationUnit161.setter
    def OrganizationUnit161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit161", None)
        self.__OrganizationUnit161 = value
        
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
    def OrganizationUnit204(self):
        return self.__OrganizationUnit204

    @OrganizationUnit204.setter
    def OrganizationUnit204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit204", None)
        self.__OrganizationUnit204 = value
        
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
    def OrganizationUnit248(self):
        return self.__OrganizationUnit248

    @OrganizationUnit248.setter
    def OrganizationUnit248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit248", None)
        self.__OrganizationUnit248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operatesInLocation247"):
                opp_val = getattr(old_value, "operatesInLocation247", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operatesInLocation247"):
                opp_val = getattr(value, "operatesInLocation247", None)
                if opp_val is None:
                    setattr(value, "operatesInLocation247", set([self]))
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
                    

class contentfwk_Objective(Element):

    pass
class contentfwk_Goal(Element):

    pass
class contentfwk_Driver(Element):

    pass
class Architecture:

    pass
class contentfwk_ApplicationArchitecture(Architecture):

    pass
class contentfwk_StrategicArchitecture(Architecture):

    pass
class contentfwk_DataArchitecture(Architecture):

    pass
class contentfwk_TechnologyArchitecture(Architecture):

    pass
class contentfwk_BusinessArchitecture(Architecture):

    pass
class contentfwk_EObject:

    pass
class contentfwk_Container:

    def __init__(self, name: str, contentfwk_Container: "contentfwk_EnterpriseArchitecture" = None, contentfwk_Container243: set["contentfwk_Element"] = None):
        self.name = name
        self.contentfwk_Container = contentfwk_Container
        self.contentfwk_Container243 = contentfwk_Container243 if contentfwk_Container243 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def contentfwk_Container243(self):
        return self.__contentfwk_Container243

    @contentfwk_Container243.setter
    def contentfwk_Container243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Container__contentfwk_Container243", None)
        self.__contentfwk_Container243 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_Element"):
                    opp_val = getattr(item, "contentfwk_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_Element"):
                    opp_val = getattr(item, "contentfwk_Element", None)
                    
                    setattr(item, "contentfwk_Element", self)
                    
