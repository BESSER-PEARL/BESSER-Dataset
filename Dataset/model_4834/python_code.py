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
class LifeCycleStatus(Enum):
    Proposed = "Proposed"
    InDevelopment = "InDevelopment"
    Live = "Live"
    PhasingOut = "PhasingOut"
    Retired = "Retired"


############################################
# Definition of Classes
############################################

class contentfwk_Standard(ABC):

    def __init__(self, standardClass: str, standardCreationDate: date, lastStandardReviewDate: date, nextStandardReviewDate: date, retireDate: date):
        self.standardClass = standardClass
        self.standardCreationDate = standardCreationDate
        self.lastStandardReviewDate = lastStandardReviewDate
        self.nextStandardReviewDate = nextStandardReviewDate
        self.retireDate = retireDate
        
    @property
    def lastStandardReviewDate(self) -> date:
        return self.__lastStandardReviewDate

    @lastStandardReviewDate.setter
    def lastStandardReviewDate(self, lastStandardReviewDate: date):
        self.__lastStandardReviewDate = lastStandardReviewDate

    @property
    def standardCreationDate(self) -> date:
        return self.__standardCreationDate

    @standardCreationDate.setter
    def standardCreationDate(self, standardCreationDate: date):
        self.__standardCreationDate = standardCreationDate

    @property
    def retireDate(self) -> date:
        return self.__retireDate

    @retireDate.setter
    def retireDate(self, retireDate: date):
        self.__retireDate = retireDate

    @property
    def nextStandardReviewDate(self) -> date:
        return self.__nextStandardReviewDate

    @nextStandardReviewDate.setter
    def nextStandardReviewDate(self, nextStandardReviewDate: date):
        self.__nextStandardReviewDate = nextStandardReviewDate

    @property
    def standardClass(self) -> str:
        return self.__standardClass

    @standardClass.setter
    def standardClass(self, standardClass: str):
        self.__standardClass = standardClass

class StrategicElement:

    pass
class contentfwk_Principle(StrategicElement):

    def __init__(self, statementOfPrinciple: str, rationale: str, implication: str, metric: str, principleCategory: str, priority: str):
        self.statementOfPrinciple = statementOfPrinciple
        self.rationale = rationale
        self.implication = implication
        self.metric = metric
        self.principleCategory = principleCategory
        self.priority = priority
        
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
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

    @property
    def principleCategory(self) -> str:
        return self.__principleCategory

    @principleCategory.setter
    def principleCategory(self, principleCategory: str):
        self.__principleCategory = principleCategory

    @property
    def rationale(self) -> str:
        return self.__rationale

    @rationale.setter
    def rationale(self, rationale: str):
        self.__rationale = rationale

    @property
    def statementOfPrinciple(self) -> str:
        return self.__statementOfPrinciple

    @statementOfPrinciple.setter
    def statementOfPrinciple(self, statementOfPrinciple: str):
        self.__statementOfPrinciple = statementOfPrinciple

class DataComponent:

    pass
class contentfwk_Gap(StrategicElement):

    pass
class contentfwk_Requirement(StrategicElement):

    def __init__(self, statementOfRequirement: str, rationale: str, acceptanceCriteria: str):
        self.statementOfRequirement = statementOfRequirement
        self.rationale = rationale
        self.acceptanceCriteria = acceptanceCriteria
        
    @property
    def statementOfRequirement(self) -> str:
        return self.__statementOfRequirement

    @statementOfRequirement.setter
    def statementOfRequirement(self, statementOfRequirement: str):
        self.__statementOfRequirement = statementOfRequirement

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

class contentfwk_Assumption(StrategicElement):

    pass
class contentfwk_Constraint(StrategicElement):

    pass
class contentfwk_Element:

    def __init__(self, name: str, description: str, sourceDescr: str, ownerDescr: str, ID: str, category: str, Element: "contentfwk_Element" = None, isDelegatedBy: set["contentfwk_Element"] = None, Element270: "contentfwk_Element" = None, delegates: set["contentfwk_Element"] = None):
        self.name = name
        self.description = description
        self.sourceDescr = sourceDescr
        self.ownerDescr = ownerDescr
        self.ID = ID
        self.category = category
        self.Element = Element
        self.isDelegatedBy = isDelegatedBy if isDelegatedBy is not None else set()
        self.Element270 = Element270
        self.delegates = delegates if delegates is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def ownerDescr(self) -> str:
        return self.__ownerDescr

    @ownerDescr.setter
    def ownerDescr(self, ownerDescr: str):
        self.__ownerDescr = ownerDescr

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def sourceDescr(self) -> str:
        return self.__sourceDescr

    @sourceDescr.setter
    def sourceDescr(self, sourceDescr: str):
        self.__sourceDescr = sourceDescr

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

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
    def Element270(self):
        return self.__Element270

    @Element270.setter
    def Element270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Element__Element270", None)
        self.__Element270 = value
        
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
                if hasattr(item, "Element270"):
                    opp_val = getattr(item, "Element270", None)
                    
                    if opp_val == self:
                        setattr(item, "Element270", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element270"):
                    opp_val = getattr(item, "Element270", None)
                    
                    setattr(item, "Element270", self)
                    

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
                    

    def forceID(self, newID: str):
        # TODO: Implement forceID method
        pass

class contentfwk_WorkPackage(StrategicElement):

    def __init__(self, workPackageCategory: str, capabilityDelivered: str, WorkPackage: "contentfwk_Capability" = None, isDeliveredBy: set["contentfwk_Capability"] = None):
        self.workPackageCategory = workPackageCategory
        self.capabilityDelivered = capabilityDelivered
        self.WorkPackage = WorkPackage
        self.isDeliveredBy = isDeliveredBy if isDeliveredBy is not None else set()
        
    @property
    def capabilityDelivered(self) -> str:
        return self.__capabilityDelivered

    @capabilityDelivered.setter
    def capabilityDelivered(self, capabilityDelivered: str):
        self.__capabilityDelivered = capabilityDelivered

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

class TechnologyComponent:

    pass
class ApplicationComponent:

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
class contentfwk_Service(Standard):

    pass
class Element:

    pass
class contentfwk_Event(Element):

    pass
class contentfwk_Product(Element):

    pass
class contentfwk_Control(Element):

    pass
class contentfwk_InformationSystemService(Element, Service):

    pass
class contentfwk_PhysicalApplicationComponent(ApplicationComponent, Element):

    def __init__(self, lifeCycleStatus: str, initialLiveDate: date, dateOfLastRelease: date, dateOfNextRelease: date, retirementDate: date, availabilityCharacteristics: str, servicesTimes: str, manageabilityCharacteristics: str, serviceabilityCharacteristics: str, performanceCharacteristics: str, reliabilityCharacteristics: str, recoverabilityCharacteristics: str, locatabilityCharacteristics: str, securityCharacteristics: str, privacyCharacteristics: str, integrityCharacteristics: str, credibilityCharacteristics: str, localizationCharacteristics: str, internationalizationCharacteristics: str, interoperabilityCharacteristics: str, scalabilityCharacteristics: str, portabilityCharacteristics: str, extensibilityCharacteristics: str, capacityCharacteristics: str, throughput: str, throughputPeriod: str, growth: str, growthPeriod: str, peakProfileShortTerm: str, peakProfileLongTerm: str, PhysicalApplicationComponent: "contentfwk_LogicalApplicationComponent" = None, PhysicalApplicationComponent212: "contentfwk_PhysicalTechnologyComponent" = None, PhysicalApplicationComponent278: "contentfwk_Location" = None, contentfwk_PhysicalApplicationComponent: "contentfwk_ApplicationArchitecture" = None, isExtendedByPhysicalApplicationComponents: set["contentfwk_LogicalApplicationComponent"] = None, containsPhysicalApplicationComponents: set["contentfwk_Location"] = None, contentfwk_PhysicalApplicationComponent318: "contentfwk_PhysicalApplicationComponent" = None, contentfwk_PhysicalApplicationComponent316: set["contentfwk_PhysicalApplicationComponent"] = None, PhysicalApplicationComponent302: "contentfwk_PhysicalDataComponent" = None, realizesPhysicalApplicationComponents: set["contentfwk_PhysicalTechnologyComponent"] = None, PhysicalApplicationComponent325: "contentfwk_PhysicalApplicationComponent" = None, isDecomposedByPhysicalApplicationComponents: "contentfwk_PhysicalApplicationComponent" = None, PhysicalApplicationComponent328: "contentfwk_PhysicalApplicationComponent" = None, decomposesPhysicalApplicationComponent: set["contentfwk_PhysicalApplicationComponent"] = None, encapsulatesPhysicalApplicationComponents: set["contentfwk_PhysicalDataComponent"] = None):
        self.lifeCycleStatus = lifeCycleStatus
        self.initialLiveDate = initialLiveDate
        self.dateOfLastRelease = dateOfLastRelease
        self.dateOfNextRelease = dateOfNextRelease
        self.retirementDate = retirementDate
        self.availabilityCharacteristics = availabilityCharacteristics
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
        self.PhysicalApplicationComponent212 = PhysicalApplicationComponent212
        self.PhysicalApplicationComponent278 = PhysicalApplicationComponent278
        self.contentfwk_PhysicalApplicationComponent = contentfwk_PhysicalApplicationComponent
        self.isExtendedByPhysicalApplicationComponents = isExtendedByPhysicalApplicationComponents if isExtendedByPhysicalApplicationComponents is not None else set()
        self.containsPhysicalApplicationComponents = containsPhysicalApplicationComponents if containsPhysicalApplicationComponents is not None else set()
        self.contentfwk_PhysicalApplicationComponent318 = contentfwk_PhysicalApplicationComponent318
        self.contentfwk_PhysicalApplicationComponent316 = contentfwk_PhysicalApplicationComponent316 if contentfwk_PhysicalApplicationComponent316 is not None else set()
        self.PhysicalApplicationComponent302 = PhysicalApplicationComponent302
        self.realizesPhysicalApplicationComponents = realizesPhysicalApplicationComponents if realizesPhysicalApplicationComponents is not None else set()
        self.PhysicalApplicationComponent325 = PhysicalApplicationComponent325
        self.isDecomposedByPhysicalApplicationComponents = isDecomposedByPhysicalApplicationComponents
        self.PhysicalApplicationComponent328 = PhysicalApplicationComponent328
        self.decomposesPhysicalApplicationComponent = decomposesPhysicalApplicationComponent if decomposesPhysicalApplicationComponent is not None else set()
        self.encapsulatesPhysicalApplicationComponents = encapsulatesPhysicalApplicationComponents if encapsulatesPhysicalApplicationComponents is not None else set()
        
    @property
    def growthPeriod(self) -> str:
        return self.__growthPeriod

    @growthPeriod.setter
    def growthPeriod(self, growthPeriod: str):
        self.__growthPeriod = growthPeriod

    @property
    def throughput(self) -> str:
        return self.__throughput

    @throughput.setter
    def throughput(self, throughput: str):
        self.__throughput = throughput

    @property
    def locatabilityCharacteristics(self) -> str:
        return self.__locatabilityCharacteristics

    @locatabilityCharacteristics.setter
    def locatabilityCharacteristics(self, locatabilityCharacteristics: str):
        self.__locatabilityCharacteristics = locatabilityCharacteristics

    @property
    def privacyCharacteristics(self) -> str:
        return self.__privacyCharacteristics

    @privacyCharacteristics.setter
    def privacyCharacteristics(self, privacyCharacteristics: str):
        self.__privacyCharacteristics = privacyCharacteristics

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
    def serviceabilityCharacteristics(self) -> str:
        return self.__serviceabilityCharacteristics

    @serviceabilityCharacteristics.setter
    def serviceabilityCharacteristics(self, serviceabilityCharacteristics: str):
        self.__serviceabilityCharacteristics = serviceabilityCharacteristics

    @property
    def throughputPeriod(self) -> str:
        return self.__throughputPeriod

    @throughputPeriod.setter
    def throughputPeriod(self, throughputPeriod: str):
        self.__throughputPeriod = throughputPeriod

    @property
    def manageabilityCharacteristics(self) -> str:
        return self.__manageabilityCharacteristics

    @manageabilityCharacteristics.setter
    def manageabilityCharacteristics(self, manageabilityCharacteristics: str):
        self.__manageabilityCharacteristics = manageabilityCharacteristics

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
    def interoperabilityCharacteristics(self) -> str:
        return self.__interoperabilityCharacteristics

    @interoperabilityCharacteristics.setter
    def interoperabilityCharacteristics(self, interoperabilityCharacteristics: str):
        self.__interoperabilityCharacteristics = interoperabilityCharacteristics

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
    def initialLiveDate(self) -> date:
        return self.__initialLiveDate

    @initialLiveDate.setter
    def initialLiveDate(self, initialLiveDate: date):
        self.__initialLiveDate = initialLiveDate

    @property
    def servicesTimes(self) -> str:
        return self.__servicesTimes

    @servicesTimes.setter
    def servicesTimes(self, servicesTimes: str):
        self.__servicesTimes = servicesTimes

    @property
    def internationalizationCharacteristics(self) -> str:
        return self.__internationalizationCharacteristics

    @internationalizationCharacteristics.setter
    def internationalizationCharacteristics(self, internationalizationCharacteristics: str):
        self.__internationalizationCharacteristics = internationalizationCharacteristics

    @property
    def peakProfileShortTerm(self) -> str:
        return self.__peakProfileShortTerm

    @peakProfileShortTerm.setter
    def peakProfileShortTerm(self, peakProfileShortTerm: str):
        self.__peakProfileShortTerm = peakProfileShortTerm

    @property
    def securityCharacteristics(self) -> str:
        return self.__securityCharacteristics

    @securityCharacteristics.setter
    def securityCharacteristics(self, securityCharacteristics: str):
        self.__securityCharacteristics = securityCharacteristics

    @property
    def availabilityCharacteristics(self) -> str:
        return self.__availabilityCharacteristics

    @availabilityCharacteristics.setter
    def availabilityCharacteristics(self, availabilityCharacteristics: str):
        self.__availabilityCharacteristics = availabilityCharacteristics

    @property
    def performanceCharacteristics(self) -> str:
        return self.__performanceCharacteristics

    @performanceCharacteristics.setter
    def performanceCharacteristics(self, performanceCharacteristics: str):
        self.__performanceCharacteristics = performanceCharacteristics

    @property
    def capacityCharacteristics(self) -> str:
        return self.__capacityCharacteristics

    @capacityCharacteristics.setter
    def capacityCharacteristics(self, capacityCharacteristics: str):
        self.__capacityCharacteristics = capacityCharacteristics

    @property
    def extensibilityCharacteristics(self) -> str:
        return self.__extensibilityCharacteristics

    @extensibilityCharacteristics.setter
    def extensibilityCharacteristics(self, extensibilityCharacteristics: str):
        self.__extensibilityCharacteristics = extensibilityCharacteristics

    @property
    def dateOfNextRelease(self) -> date:
        return self.__dateOfNextRelease

    @dateOfNextRelease.setter
    def dateOfNextRelease(self, dateOfNextRelease: date):
        self.__dateOfNextRelease = dateOfNextRelease

    @property
    def realizesPhysicalApplicationComponents(self):
        return self.__realizesPhysicalApplicationComponents

    @realizesPhysicalApplicationComponents.setter
    def realizesPhysicalApplicationComponents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__realizesPhysicalApplicationComponents", None)
        self.__realizesPhysicalApplicationComponents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhysicalTechnologyComponent322"):
                    opp_val = getattr(item, "PhysicalTechnologyComponent322", None)
                    
                    if opp_val == self:
                        setattr(item, "PhysicalTechnologyComponent322", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhysicalTechnologyComponent322"):
                    opp_val = getattr(item, "PhysicalTechnologyComponent322", None)
                    
                    setattr(item, "PhysicalTechnologyComponent322", self)
                    

    @property
    def PhysicalApplicationComponent325(self):
        return self.__PhysicalApplicationComponent325

    @PhysicalApplicationComponent325.setter
    def PhysicalApplicationComponent325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__PhysicalApplicationComponent325", None)
        self.__PhysicalApplicationComponent325 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isDecomposedByPhysicalApplicationComponents"):
                opp_val = getattr(old_value, "isDecomposedByPhysicalApplicationComponents", None)
                if opp_val == self:
                    setattr(old_value, "isDecomposedByPhysicalApplicationComponents", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isDecomposedByPhysicalApplicationComponents"):
                opp_val = getattr(value, "isDecomposedByPhysicalApplicationComponents", None)
                setattr(value, "isDecomposedByPhysicalApplicationComponents", self)

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
            if hasattr(old_value, "contentfwk_ApplicationArchitecture309"):
                opp_val = getattr(old_value, "contentfwk_ApplicationArchitecture309", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_ApplicationArchitecture309"):
                opp_val = getattr(value, "contentfwk_ApplicationArchitecture309", None)
                if opp_val is None:
                    setattr(value, "contentfwk_ApplicationArchitecture309", set([self]))
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
                if hasattr(item, "LogicalApplicationComponent313"):
                    opp_val = getattr(item, "LogicalApplicationComponent313", None)
                    
                    if opp_val == self:
                        setattr(item, "LogicalApplicationComponent313", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LogicalApplicationComponent313"):
                    opp_val = getattr(item, "LogicalApplicationComponent313", None)
                    
                    setattr(item, "LogicalApplicationComponent313", self)
                    

    @property
    def decomposesPhysicalApplicationComponent(self):
        return self.__decomposesPhysicalApplicationComponent

    @decomposesPhysicalApplicationComponent.setter
    def decomposesPhysicalApplicationComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__decomposesPhysicalApplicationComponent", None)
        self.__decomposesPhysicalApplicationComponent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhysicalApplicationComponent328"):
                    opp_val = getattr(item, "PhysicalApplicationComponent328", None)
                    
                    if opp_val == self:
                        setattr(item, "PhysicalApplicationComponent328", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhysicalApplicationComponent328"):
                    opp_val = getattr(item, "PhysicalApplicationComponent328", None)
                    
                    setattr(item, "PhysicalApplicationComponent328", self)
                    

    @property
    def PhysicalApplicationComponent212(self):
        return self.__PhysicalApplicationComponent212

    @PhysicalApplicationComponent212.setter
    def PhysicalApplicationComponent212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__PhysicalApplicationComponent212", None)
        self.__PhysicalApplicationComponent212 = value
        
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
    def PhysicalApplicationComponent278(self):
        return self.__PhysicalApplicationComponent278

    @PhysicalApplicationComponent278.setter
    def PhysicalApplicationComponent278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__PhysicalApplicationComponent278", None)
        self.__PhysicalApplicationComponent278 = value
        
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
                if hasattr(item, "Location315"):
                    opp_val = getattr(item, "Location315", None)
                    
                    if opp_val == self:
                        setattr(item, "Location315", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Location315"):
                    opp_val = getattr(item, "Location315", None)
                    
                    setattr(item, "Location315", self)
                    

    @property
    def encapsulatesPhysicalApplicationComponents(self):
        return self.__encapsulatesPhysicalApplicationComponents

    @encapsulatesPhysicalApplicationComponents.setter
    def encapsulatesPhysicalApplicationComponents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__encapsulatesPhysicalApplicationComponents", None)
        self.__encapsulatesPhysicalApplicationComponents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhysicalDataComponent320"):
                    opp_val = getattr(item, "PhysicalDataComponent320", None)
                    
                    if opp_val == self:
                        setattr(item, "PhysicalDataComponent320", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhysicalDataComponent320"):
                    opp_val = getattr(item, "PhysicalDataComponent320", None)
                    
                    setattr(item, "PhysicalDataComponent320", self)
                    

    @property
    def contentfwk_PhysicalApplicationComponent316(self):
        return self.__contentfwk_PhysicalApplicationComponent316

    @contentfwk_PhysicalApplicationComponent316.setter
    def contentfwk_PhysicalApplicationComponent316(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent316", None)
        self.__contentfwk_PhysicalApplicationComponent316 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_PhysicalApplicationComponent318"):
                    opp_val = getattr(item, "contentfwk_PhysicalApplicationComponent318", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_PhysicalApplicationComponent318", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_PhysicalApplicationComponent318"):
                    opp_val = getattr(item, "contentfwk_PhysicalApplicationComponent318", None)
                    
                    setattr(item, "contentfwk_PhysicalApplicationComponent318", self)
                    

    @property
    def isDecomposedByPhysicalApplicationComponents(self):
        return self.__isDecomposedByPhysicalApplicationComponents

    @isDecomposedByPhysicalApplicationComponents.setter
    def isDecomposedByPhysicalApplicationComponents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__isDecomposedByPhysicalApplicationComponents", None)
        self.__isDecomposedByPhysicalApplicationComponents = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhysicalApplicationComponent325"):
                opp_val = getattr(old_value, "PhysicalApplicationComponent325", None)
                if opp_val == self:
                    setattr(old_value, "PhysicalApplicationComponent325", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhysicalApplicationComponent325"):
                opp_val = getattr(value, "PhysicalApplicationComponent325", None)
                setattr(value, "PhysicalApplicationComponent325", self)

    @property
    def PhysicalApplicationComponent328(self):
        return self.__PhysicalApplicationComponent328

    @PhysicalApplicationComponent328.setter
    def PhysicalApplicationComponent328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__PhysicalApplicationComponent328", None)
        self.__PhysicalApplicationComponent328 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decomposesPhysicalApplicationComponent"):
                opp_val = getattr(old_value, "decomposesPhysicalApplicationComponent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decomposesPhysicalApplicationComponent"):
                opp_val = getattr(value, "decomposesPhysicalApplicationComponent", None)
                if opp_val is None:
                    setattr(value, "decomposesPhysicalApplicationComponent", set([self]))
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
    def contentfwk_PhysicalApplicationComponent318(self):
        return self.__contentfwk_PhysicalApplicationComponent318

    @contentfwk_PhysicalApplicationComponent318.setter
    def contentfwk_PhysicalApplicationComponent318(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent318", None)
        self.__contentfwk_PhysicalApplicationComponent318 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalApplicationComponent316"):
                opp_val = getattr(old_value, "contentfwk_PhysicalApplicationComponent316", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalApplicationComponent316"):
                opp_val = getattr(value, "contentfwk_PhysicalApplicationComponent316", None)
                if opp_val is None:
                    setattr(value, "contentfwk_PhysicalApplicationComponent316", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PhysicalApplicationComponent302(self):
        return self.__PhysicalApplicationComponent302

    @PhysicalApplicationComponent302.setter
    def PhysicalApplicationComponent302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__PhysicalApplicationComponent302", None)
        self.__PhysicalApplicationComponent302 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encapsulatesPhysicalDataComponents"):
                opp_val = getattr(old_value, "encapsulatesPhysicalDataComponents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encapsulatesPhysicalDataComponents"):
                opp_val = getattr(value, "encapsulatesPhysicalDataComponents", None)
                if opp_val is None:
                    setattr(value, "encapsulatesPhysicalDataComponents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class contentfwk_LogicalApplicationComponent(ApplicationComponent, Element):

    pass
class contentfwk_Contract(Element):

    def __init__(self, servicesTimes: str, manageabilityCharacteristics: str, serviceabilityCharacteristics: str, performanceCharacteristics: str, responseCharacteristics: str, reliabilityCharacteristics: str, qualityOfInformationRequired: str, contractControlRequirements: str, resultControlRequirements: str, recoverabilityCharacteristics: str, locatabilityCharacteristics: str, securityCharacteristics: str, privacyCharacteristics: str, integrityCharacteristics: str, credibilityCharacteristics: str, localizationCharacteristics: str, internationalizationCharacteristics: str, interoperabilityCharacteristics: str, scalabilityCharacteristics: str, portabilityCharacteristics: str, extensibilityCharacteristics: str, capacityCharacteristics: str, throughput: str, throughputPeriod: str, growth: str, growthPeriod: str, peakProfileShortTerm: str, peakProfileLongTerm: str, behaviorCharacteristics: str, serviceNameCaller: str, serviceNameCalled: str, serviceQualityCharacteristics: str, availabilityQualityCharacteristics: str, contentfwk_Contract: "contentfwk_BusinessArchitecture" = None, Contract: "contentfwk_ServiceQuality" = None, isGovernedAndMeasuredByContracts: set["contentfwk_Service"] = None, appliesToContracts: set["contentfwk_ServiceQuality"] = None, Contract361: "contentfwk_Service" = None):
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
        self.serviceNameCaller = serviceNameCaller
        self.serviceNameCalled = serviceNameCalled
        self.serviceQualityCharacteristics = serviceQualityCharacteristics
        self.availabilityQualityCharacteristics = availabilityQualityCharacteristics
        self.contentfwk_Contract = contentfwk_Contract
        self.Contract = Contract
        self.isGovernedAndMeasuredByContracts = isGovernedAndMeasuredByContracts if isGovernedAndMeasuredByContracts is not None else set()
        self.appliesToContracts = appliesToContracts if appliesToContracts is not None else set()
        self.Contract361 = Contract361
        
    @property
    def throughputPeriod(self) -> str:
        return self.__throughputPeriod

    @throughputPeriod.setter
    def throughputPeriod(self, throughputPeriod: str):
        self.__throughputPeriod = throughputPeriod

    @property
    def interoperabilityCharacteristics(self) -> str:
        return self.__interoperabilityCharacteristics

    @interoperabilityCharacteristics.setter
    def interoperabilityCharacteristics(self, interoperabilityCharacteristics: str):
        self.__interoperabilityCharacteristics = interoperabilityCharacteristics

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
    def manageabilityCharacteristics(self) -> str:
        return self.__manageabilityCharacteristics

    @manageabilityCharacteristics.setter
    def manageabilityCharacteristics(self, manageabilityCharacteristics: str):
        self.__manageabilityCharacteristics = manageabilityCharacteristics

    @property
    def serviceQualityCharacteristics(self) -> str:
        return self.__serviceQualityCharacteristics

    @serviceQualityCharacteristics.setter
    def serviceQualityCharacteristics(self, serviceQualityCharacteristics: str):
        self.__serviceQualityCharacteristics = serviceQualityCharacteristics

    @property
    def portabilityCharacteristics(self) -> str:
        return self.__portabilityCharacteristics

    @portabilityCharacteristics.setter
    def portabilityCharacteristics(self, portabilityCharacteristics: str):
        self.__portabilityCharacteristics = portabilityCharacteristics

    @property
    def localizationCharacteristics(self) -> str:
        return self.__localizationCharacteristics

    @localizationCharacteristics.setter
    def localizationCharacteristics(self, localizationCharacteristics: str):
        self.__localizationCharacteristics = localizationCharacteristics

    @property
    def peakProfileShortTerm(self) -> str:
        return self.__peakProfileShortTerm

    @peakProfileShortTerm.setter
    def peakProfileShortTerm(self, peakProfileShortTerm: str):
        self.__peakProfileShortTerm = peakProfileShortTerm

    @property
    def recoverabilityCharacteristics(self) -> str:
        return self.__recoverabilityCharacteristics

    @recoverabilityCharacteristics.setter
    def recoverabilityCharacteristics(self, recoverabilityCharacteristics: str):
        self.__recoverabilityCharacteristics = recoverabilityCharacteristics

    @property
    def locatabilityCharacteristics(self) -> str:
        return self.__locatabilityCharacteristics

    @locatabilityCharacteristics.setter
    def locatabilityCharacteristics(self, locatabilityCharacteristics: str):
        self.__locatabilityCharacteristics = locatabilityCharacteristics

    @property
    def behaviorCharacteristics(self) -> str:
        return self.__behaviorCharacteristics

    @behaviorCharacteristics.setter
    def behaviorCharacteristics(self, behaviorCharacteristics: str):
        self.__behaviorCharacteristics = behaviorCharacteristics

    @property
    def qualityOfInformationRequired(self) -> str:
        return self.__qualityOfInformationRequired

    @qualityOfInformationRequired.setter
    def qualityOfInformationRequired(self, qualityOfInformationRequired: str):
        self.__qualityOfInformationRequired = qualityOfInformationRequired

    @property
    def growth(self) -> str:
        return self.__growth

    @growth.setter
    def growth(self, growth: str):
        self.__growth = growth

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
    def privacyCharacteristics(self) -> str:
        return self.__privacyCharacteristics

    @privacyCharacteristics.setter
    def privacyCharacteristics(self, privacyCharacteristics: str):
        self.__privacyCharacteristics = privacyCharacteristics

    @property
    def peakProfileLongTerm(self) -> str:
        return self.__peakProfileLongTerm

    @peakProfileLongTerm.setter
    def peakProfileLongTerm(self, peakProfileLongTerm: str):
        self.__peakProfileLongTerm = peakProfileLongTerm

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
    def contractControlRequirements(self) -> str:
        return self.__contractControlRequirements

    @contractControlRequirements.setter
    def contractControlRequirements(self, contractControlRequirements: str):
        self.__contractControlRequirements = contractControlRequirements

    @property
    def credibilityCharacteristics(self) -> str:
        return self.__credibilityCharacteristics

    @credibilityCharacteristics.setter
    def credibilityCharacteristics(self, credibilityCharacteristics: str):
        self.__credibilityCharacteristics = credibilityCharacteristics

    @property
    def growthPeriod(self) -> str:
        return self.__growthPeriod

    @growthPeriod.setter
    def growthPeriod(self, growthPeriod: str):
        self.__growthPeriod = growthPeriod

    @property
    def serviceNameCaller(self) -> str:
        return self.__serviceNameCaller

    @serviceNameCaller.setter
    def serviceNameCaller(self, serviceNameCaller: str):
        self.__serviceNameCaller = serviceNameCaller

    @property
    def throughput(self) -> str:
        return self.__throughput

    @throughput.setter
    def throughput(self, throughput: str):
        self.__throughput = throughput

    @property
    def serviceabilityCharacteristics(self) -> str:
        return self.__serviceabilityCharacteristics

    @serviceabilityCharacteristics.setter
    def serviceabilityCharacteristics(self, serviceabilityCharacteristics: str):
        self.__serviceabilityCharacteristics = serviceabilityCharacteristics

    @property
    def responseCharacteristics(self) -> str:
        return self.__responseCharacteristics

    @responseCharacteristics.setter
    def responseCharacteristics(self, responseCharacteristics: str):
        self.__responseCharacteristics = responseCharacteristics

    @property
    def serviceNameCalled(self) -> str:
        return self.__serviceNameCalled

    @serviceNameCalled.setter
    def serviceNameCalled(self, serviceNameCalled: str):
        self.__serviceNameCalled = serviceNameCalled

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
    def internationalizationCharacteristics(self) -> str:
        return self.__internationalizationCharacteristics

    @internationalizationCharacteristics.setter
    def internationalizationCharacteristics(self, internationalizationCharacteristics: str):
        self.__internationalizationCharacteristics = internationalizationCharacteristics

    @property
    def reliabilityCharacteristics(self) -> str:
        return self.__reliabilityCharacteristics

    @reliabilityCharacteristics.setter
    def reliabilityCharacteristics(self, reliabilityCharacteristics: str):
        self.__reliabilityCharacteristics = reliabilityCharacteristics

    @property
    def resultControlRequirements(self) -> str:
        return self.__resultControlRequirements

    @resultControlRequirements.setter
    def resultControlRequirements(self, resultControlRequirements: str):
        self.__resultControlRequirements = resultControlRequirements

    @property
    def Contract361(self):
        return self.__Contract361

    @Contract361.setter
    def Contract361(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Contract__Contract361", None)
        self.__Contract361 = value
        
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
                if hasattr(item, "Service249"):
                    opp_val = getattr(item, "Service249", None)
                    
                    if opp_val == self:
                        setattr(item, "Service249", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service249"):
                    opp_val = getattr(item, "Service249", None)
                    
                    setattr(item, "Service249", self)
                    

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
            if hasattr(old_value, "contentfwk_BusinessArchitecture27"):
                opp_val = getattr(old_value, "contentfwk_BusinessArchitecture27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_BusinessArchitecture27"):
                opp_val = getattr(value, "contentfwk_BusinessArchitecture27", None)
                if opp_val is None:
                    setattr(value, "contentfwk_BusinessArchitecture27", set([self]))
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

class contentfwk_Location(Element):

    pass
class contentfwk_StrategicElement(Element):

    pass
class contentfwk_LogicalTechnologyComponent(Element, TechnologyComponent):

    def __init__(self, categoryTRM: str, contentfwk_LogicalTechnologyComponent: "contentfwk_TechnologyArchitecture" = None, LogicalTechnologyComponent: "contentfwk_PlatformService" = None, LogicalTechnologyComponent215: "contentfwk_PhysicalTechnologyComponent" = None, isImplementedOnLogicalTechnologyComponents: set["contentfwk_Service"] = None, isSuppliedByLogicalTechnologyComponents: set["contentfwk_PlatformService"] = None, extendsLogicalTechnologyComponents: set["contentfwk_PhysicalTechnologyComponent"] = None, LogicalTechnologyComponent336: "contentfwk_LogicalTechnologyComponent" = None, isDecomposedByLogicalTechnologyComponents: "contentfwk_LogicalTechnologyComponent" = None, LogicalTechnologyComponent339: "contentfwk_LogicalTechnologyComponent" = None, isRequiredByLogicalTechnologyComponents: set["contentfwk_LogicalTechnologyComponent"] = None, contentfwk_LogicalTechnologyComponent341: set["contentfwk_PhysicalTechnologyComponent"] = None, LogicalTechnologyComponent345: "contentfwk_LogicalTechnologyComponent" = None, isDependentOnLogicalTechnologyComponents: set["contentfwk_LogicalTechnologyComponent"] = None, LogicalTechnologyComponent348: "contentfwk_LogicalTechnologyComponent" = None, decomposesLogicalTechnologyComponent: set["contentfwk_LogicalTechnologyComponent"] = None, LogicalTechnologyComponent365: "contentfwk_Service" = None):
        self.categoryTRM = categoryTRM
        self.contentfwk_LogicalTechnologyComponent = contentfwk_LogicalTechnologyComponent
        self.LogicalTechnologyComponent = LogicalTechnologyComponent
        self.LogicalTechnologyComponent215 = LogicalTechnologyComponent215
        self.isImplementedOnLogicalTechnologyComponents = isImplementedOnLogicalTechnologyComponents if isImplementedOnLogicalTechnologyComponents is not None else set()
        self.isSuppliedByLogicalTechnologyComponents = isSuppliedByLogicalTechnologyComponents if isSuppliedByLogicalTechnologyComponents is not None else set()
        self.extendsLogicalTechnologyComponents = extendsLogicalTechnologyComponents if extendsLogicalTechnologyComponents is not None else set()
        self.LogicalTechnologyComponent336 = LogicalTechnologyComponent336
        self.isDecomposedByLogicalTechnologyComponents = isDecomposedByLogicalTechnologyComponents
        self.LogicalTechnologyComponent339 = LogicalTechnologyComponent339
        self.isRequiredByLogicalTechnologyComponents = isRequiredByLogicalTechnologyComponents if isRequiredByLogicalTechnologyComponents is not None else set()
        self.contentfwk_LogicalTechnologyComponent341 = contentfwk_LogicalTechnologyComponent341 if contentfwk_LogicalTechnologyComponent341 is not None else set()
        self.LogicalTechnologyComponent345 = LogicalTechnologyComponent345
        self.isDependentOnLogicalTechnologyComponents = isDependentOnLogicalTechnologyComponents if isDependentOnLogicalTechnologyComponents is not None else set()
        self.LogicalTechnologyComponent348 = LogicalTechnologyComponent348
        self.decomposesLogicalTechnologyComponent = decomposesLogicalTechnologyComponent if decomposesLogicalTechnologyComponent is not None else set()
        self.LogicalTechnologyComponent365 = LogicalTechnologyComponent365
        
    @property
    def categoryTRM(self) -> str:
        return self.__categoryTRM

    @categoryTRM.setter
    def categoryTRM(self, categoryTRM: str):
        self.__categoryTRM = categoryTRM

    @property
    def decomposesLogicalTechnologyComponent(self):
        return self.__decomposesLogicalTechnologyComponent

    @decomposesLogicalTechnologyComponent.setter
    def decomposesLogicalTechnologyComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_LogicalTechnologyComponent__decomposesLogicalTechnologyComponent", None)
        self.__decomposesLogicalTechnologyComponent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LogicalTechnologyComponent348"):
                    opp_val = getattr(item, "LogicalTechnologyComponent348", None)
                    
                    if opp_val == self:
                        setattr(item, "LogicalTechnologyComponent348", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LogicalTechnologyComponent348"):
                    opp_val = getattr(item, "LogicalTechnologyComponent348", None)
                    
                    setattr(item, "LogicalTechnologyComponent348", self)
                    

    @property
    def isDecomposedByLogicalTechnologyComponents(self):
        return self.__isDecomposedByLogicalTechnologyComponents

    @isDecomposedByLogicalTechnologyComponents.setter
    def isDecomposedByLogicalTechnologyComponents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_LogicalTechnologyComponent__isDecomposedByLogicalTechnologyComponents", None)
        self.__isDecomposedByLogicalTechnologyComponents = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LogicalTechnologyComponent336"):
                opp_val = getattr(old_value, "LogicalTechnologyComponent336", None)
                if opp_val == self:
                    setattr(old_value, "LogicalTechnologyComponent336", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LogicalTechnologyComponent336"):
                opp_val = getattr(value, "LogicalTechnologyComponent336", None)
                setattr(value, "LogicalTechnologyComponent336", self)

    @property
    def LogicalTechnologyComponent365(self):
        return self.__LogicalTechnologyComponent365

    @LogicalTechnologyComponent365.setter
    def LogicalTechnologyComponent365(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_LogicalTechnologyComponent__LogicalTechnologyComponent365", None)
        self.__LogicalTechnologyComponent365 = value
        
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
    def LogicalTechnologyComponent336(self):
        return self.__LogicalTechnologyComponent336

    @LogicalTechnologyComponent336.setter
    def LogicalTechnologyComponent336(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_LogicalTechnologyComponent__LogicalTechnologyComponent336", None)
        self.__LogicalTechnologyComponent336 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isDecomposedByLogicalTechnologyComponents"):
                opp_val = getattr(old_value, "isDecomposedByLogicalTechnologyComponents", None)
                if opp_val == self:
                    setattr(old_value, "isDecomposedByLogicalTechnologyComponents", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isDecomposedByLogicalTechnologyComponents"):
                opp_val = getattr(value, "isDecomposedByLogicalTechnologyComponents", None)
                setattr(value, "isDecomposedByLogicalTechnologyComponents", self)

    @property
    def isDependentOnLogicalTechnologyComponents(self):
        return self.__isDependentOnLogicalTechnologyComponents

    @isDependentOnLogicalTechnologyComponents.setter
    def isDependentOnLogicalTechnologyComponents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_LogicalTechnologyComponent__isDependentOnLogicalTechnologyComponents", None)
        self.__isDependentOnLogicalTechnologyComponents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LogicalTechnologyComponent345"):
                    opp_val = getattr(item, "LogicalTechnologyComponent345", None)
                    
                    if opp_val == self:
                        setattr(item, "LogicalTechnologyComponent345", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LogicalTechnologyComponent345"):
                    opp_val = getattr(item, "LogicalTechnologyComponent345", None)
                    
                    setattr(item, "LogicalTechnologyComponent345", self)
                    

    @property
    def LogicalTechnologyComponent339(self):
        return self.__LogicalTechnologyComponent339

    @LogicalTechnologyComponent339.setter
    def LogicalTechnologyComponent339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_LogicalTechnologyComponent__LogicalTechnologyComponent339", None)
        self.__LogicalTechnologyComponent339 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isRequiredByLogicalTechnologyComponents"):
                opp_val = getattr(old_value, "isRequiredByLogicalTechnologyComponents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isRequiredByLogicalTechnologyComponents"):
                opp_val = getattr(value, "isRequiredByLogicalTechnologyComponents", None)
                if opp_val is None:
                    setattr(value, "isRequiredByLogicalTechnologyComponents", set([self]))
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
                if hasattr(item, "PhysicalTechnologyComponent333"):
                    opp_val = getattr(item, "PhysicalTechnologyComponent333", None)
                    
                    if opp_val == self:
                        setattr(item, "PhysicalTechnologyComponent333", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhysicalTechnologyComponent333"):
                    opp_val = getattr(item, "PhysicalTechnologyComponent333", None)
                    
                    setattr(item, "PhysicalTechnologyComponent333", self)
                    

    @property
    def isRequiredByLogicalTechnologyComponents(self):
        return self.__isRequiredByLogicalTechnologyComponents

    @isRequiredByLogicalTechnologyComponents.setter
    def isRequiredByLogicalTechnologyComponents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_LogicalTechnologyComponent__isRequiredByLogicalTechnologyComponents", None)
        self.__isRequiredByLogicalTechnologyComponents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LogicalTechnologyComponent339"):
                    opp_val = getattr(item, "LogicalTechnologyComponent339", None)
                    
                    if opp_val == self:
                        setattr(item, "LogicalTechnologyComponent339", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LogicalTechnologyComponent339"):
                    opp_val = getattr(item, "LogicalTechnologyComponent339", None)
                    
                    setattr(item, "LogicalTechnologyComponent339", self)
                    

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
    def LogicalTechnologyComponent348(self):
        return self.__LogicalTechnologyComponent348

    @LogicalTechnologyComponent348.setter
    def LogicalTechnologyComponent348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_LogicalTechnologyComponent__LogicalTechnologyComponent348", None)
        self.__LogicalTechnologyComponent348 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decomposesLogicalTechnologyComponent"):
                opp_val = getattr(old_value, "decomposesLogicalTechnologyComponent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decomposesLogicalTechnologyComponent"):
                opp_val = getattr(value, "decomposesLogicalTechnologyComponent", None)
                if opp_val is None:
                    setattr(value, "decomposesLogicalTechnologyComponent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def LogicalTechnologyComponent345(self):
        return self.__LogicalTechnologyComponent345

    @LogicalTechnologyComponent345.setter
    def LogicalTechnologyComponent345(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_LogicalTechnologyComponent__LogicalTechnologyComponent345", None)
        self.__LogicalTechnologyComponent345 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isDependentOnLogicalTechnologyComponents"):
                opp_val = getattr(old_value, "isDependentOnLogicalTechnologyComponents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isDependentOnLogicalTechnologyComponents"):
                opp_val = getattr(value, "isDependentOnLogicalTechnologyComponents", None)
                if opp_val is None:
                    setattr(value, "isDependentOnLogicalTechnologyComponents", set([self]))
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
                if hasattr(item, "Service330"):
                    opp_val = getattr(item, "Service330", None)
                    
                    if opp_val == self:
                        setattr(item, "Service330", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service330"):
                    opp_val = getattr(item, "Service330", None)
                    
                    setattr(item, "Service330", self)
                    

    @property
    def contentfwk_LogicalTechnologyComponent341(self):
        return self.__contentfwk_LogicalTechnologyComponent341

    @contentfwk_LogicalTechnologyComponent341.setter
    def contentfwk_LogicalTechnologyComponent341(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_LogicalTechnologyComponent__contentfwk_LogicalTechnologyComponent341", None)
        self.__contentfwk_LogicalTechnologyComponent341 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_PhysicalTechnologyComponent342"):
                    opp_val = getattr(item, "contentfwk_PhysicalTechnologyComponent342", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_PhysicalTechnologyComponent342", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_PhysicalTechnologyComponent342"):
                    opp_val = getattr(item, "contentfwk_PhysicalTechnologyComponent342", None)
                    
                    setattr(item, "contentfwk_PhysicalTechnologyComponent342", self)
                    

    @property
    def LogicalTechnologyComponent215(self):
        return self.__LogicalTechnologyComponent215

    @LogicalTechnologyComponent215.setter
    def LogicalTechnologyComponent215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_LogicalTechnologyComponent__LogicalTechnologyComponent215", None)
        self.__LogicalTechnologyComponent215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isRealizedByPhysicalTechnologyComponents214"):
                opp_val = getattr(old_value, "isRealizedByPhysicalTechnologyComponents214", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isRealizedByPhysicalTechnologyComponents214"):
                opp_val = getattr(value, "isRealizedByPhysicalTechnologyComponents214", None)
                if opp_val is None:
                    setattr(value, "isRealizedByPhysicalTechnologyComponents214", set([self]))
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
            if hasattr(old_value, "contentfwk_TechnologyArchitecture41"):
                opp_val = getattr(old_value, "contentfwk_TechnologyArchitecture41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_TechnologyArchitecture41"):
                opp_val = getattr(value, "contentfwk_TechnologyArchitecture41", None)
                if opp_val is None:
                    setattr(value, "contentfwk_TechnologyArchitecture41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class contentfwk_PhysicalTechnologyComponent(Element, TechnologyComponent):

    def __init__(self, productName: str, moduleName: str, vendor: str, version: str, categoryTRM: str, contentfwk_PhysicalTechnologyComponent: "contentfwk_TechnologyArchitecture" = None, PhysicalTechnologyComponent: "contentfwk_PhysicalTechnologyComponent" = None, isDecomposedByPhysicalTechnologyComponents: "contentfwk_PhysicalTechnologyComponent" = None, PhysicalTechnologyComponent222: "contentfwk_PhysicalTechnologyComponent" = None, isRequiredByPhysicalTechnologyComponent: set["contentfwk_PhysicalTechnologyComponent"] = None, PhysicalTechnologyComponent225: "contentfwk_PhysicalTechnologyComponent" = None, isDependentOnPhysicalTechnologyComponents: set["contentfwk_PhysicalTechnologyComponent"] = None, PhysicalTechnologyComponent228: "contentfwk_PhysicalTechnologyComponent" = None, decomposesPhysicalTechnologyComponent: set["contentfwk_PhysicalTechnologyComponent"] = None, isRealizedByPhysicalTechnologyComponents: set["contentfwk_PhysicalApplicationComponent"] = None, isRealizedByPhysicalTechnologyComponents214: set["contentfwk_LogicalTechnologyComponent"] = None, containsPhysicalTechnologyComponents: set["contentfwk_Location"] = None, PhysicalTechnologyComponent281: "contentfwk_Location" = None, PhysicalTechnologyComponent322: "contentfwk_PhysicalApplicationComponent" = None, PhysicalTechnologyComponent333: "contentfwk_LogicalTechnologyComponent" = None, contentfwk_PhysicalTechnologyComponent342: "contentfwk_LogicalTechnologyComponent" = None):
        self.productName = productName
        self.moduleName = moduleName
        self.vendor = vendor
        self.version = version
        self.categoryTRM = categoryTRM
        self.contentfwk_PhysicalTechnologyComponent = contentfwk_PhysicalTechnologyComponent
        self.PhysicalTechnologyComponent = PhysicalTechnologyComponent
        self.isDecomposedByPhysicalTechnologyComponents = isDecomposedByPhysicalTechnologyComponents
        self.PhysicalTechnologyComponent222 = PhysicalTechnologyComponent222
        self.isRequiredByPhysicalTechnologyComponent = isRequiredByPhysicalTechnologyComponent if isRequiredByPhysicalTechnologyComponent is not None else set()
        self.PhysicalTechnologyComponent225 = PhysicalTechnologyComponent225
        self.isDependentOnPhysicalTechnologyComponents = isDependentOnPhysicalTechnologyComponents if isDependentOnPhysicalTechnologyComponents is not None else set()
        self.PhysicalTechnologyComponent228 = PhysicalTechnologyComponent228
        self.decomposesPhysicalTechnologyComponent = decomposesPhysicalTechnologyComponent if decomposesPhysicalTechnologyComponent is not None else set()
        self.isRealizedByPhysicalTechnologyComponents = isRealizedByPhysicalTechnologyComponents if isRealizedByPhysicalTechnologyComponents is not None else set()
        self.isRealizedByPhysicalTechnologyComponents214 = isRealizedByPhysicalTechnologyComponents214 if isRealizedByPhysicalTechnologyComponents214 is not None else set()
        self.containsPhysicalTechnologyComponents = containsPhysicalTechnologyComponents if containsPhysicalTechnologyComponents is not None else set()
        self.PhysicalTechnologyComponent281 = PhysicalTechnologyComponent281
        self.PhysicalTechnologyComponent322 = PhysicalTechnologyComponent322
        self.PhysicalTechnologyComponent333 = PhysicalTechnologyComponent333
        self.contentfwk_PhysicalTechnologyComponent342 = contentfwk_PhysicalTechnologyComponent342
        
    @property
    def categoryTRM(self) -> str:
        return self.__categoryTRM

    @categoryTRM.setter
    def categoryTRM(self, categoryTRM: str):
        self.__categoryTRM = categoryTRM

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def moduleName(self) -> str:
        return self.__moduleName

    @moduleName.setter
    def moduleName(self, moduleName: str):
        self.__moduleName = moduleName

    @property
    def vendor(self) -> str:
        return self.__vendor

    @vendor.setter
    def vendor(self, vendor: str):
        self.__vendor = vendor

    @property
    def productName(self) -> str:
        return self.__productName

    @productName.setter
    def productName(self, productName: str):
        self.__productName = productName

    @property
    def contentfwk_PhysicalTechnologyComponent342(self):
        return self.__contentfwk_PhysicalTechnologyComponent342

    @contentfwk_PhysicalTechnologyComponent342.setter
    def contentfwk_PhysicalTechnologyComponent342(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent342", None)
        self.__contentfwk_PhysicalTechnologyComponent342 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_LogicalTechnologyComponent341"):
                opp_val = getattr(old_value, "contentfwk_LogicalTechnologyComponent341", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_LogicalTechnologyComponent341"):
                opp_val = getattr(value, "contentfwk_LogicalTechnologyComponent341", None)
                if opp_val is None:
                    setattr(value, "contentfwk_LogicalTechnologyComponent341", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def isRequiredByPhysicalTechnologyComponent(self):
        return self.__isRequiredByPhysicalTechnologyComponent

    @isRequiredByPhysicalTechnologyComponent.setter
    def isRequiredByPhysicalTechnologyComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__isRequiredByPhysicalTechnologyComponent", None)
        self.__isRequiredByPhysicalTechnologyComponent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhysicalTechnologyComponent222"):
                    opp_val = getattr(item, "PhysicalTechnologyComponent222", None)
                    
                    if opp_val == self:
                        setattr(item, "PhysicalTechnologyComponent222", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhysicalTechnologyComponent222"):
                    opp_val = getattr(item, "PhysicalTechnologyComponent222", None)
                    
                    setattr(item, "PhysicalTechnologyComponent222", self)
                    

    @property
    def PhysicalTechnologyComponent281(self):
        return self.__PhysicalTechnologyComponent281

    @PhysicalTechnologyComponent281.setter
    def PhysicalTechnologyComponent281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__PhysicalTechnologyComponent281", None)
        self.__PhysicalTechnologyComponent281 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isHostedInLocation280"):
                opp_val = getattr(old_value, "isHostedInLocation280", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isHostedInLocation280"):
                opp_val = getattr(value, "isHostedInLocation280", None)
                if opp_val is None:
                    setattr(value, "isHostedInLocation280", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PhysicalTechnologyComponent322(self):
        return self.__PhysicalTechnologyComponent322

    @PhysicalTechnologyComponent322.setter
    def PhysicalTechnologyComponent322(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__PhysicalTechnologyComponent322", None)
        self.__PhysicalTechnologyComponent322 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "realizesPhysicalApplicationComponents"):
                opp_val = getattr(old_value, "realizesPhysicalApplicationComponents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "realizesPhysicalApplicationComponents"):
                opp_val = getattr(value, "realizesPhysicalApplicationComponents", None)
                if opp_val is None:
                    setattr(value, "realizesPhysicalApplicationComponents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PhysicalTechnologyComponent225(self):
        return self.__PhysicalTechnologyComponent225

    @PhysicalTechnologyComponent225.setter
    def PhysicalTechnologyComponent225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__PhysicalTechnologyComponent225", None)
        self.__PhysicalTechnologyComponent225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isDependentOnPhysicalTechnologyComponents"):
                opp_val = getattr(old_value, "isDependentOnPhysicalTechnologyComponents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isDependentOnPhysicalTechnologyComponents"):
                opp_val = getattr(value, "isDependentOnPhysicalTechnologyComponents", None)
                if opp_val is None:
                    setattr(value, "isDependentOnPhysicalTechnologyComponents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def isDependentOnPhysicalTechnologyComponents(self):
        return self.__isDependentOnPhysicalTechnologyComponents

    @isDependentOnPhysicalTechnologyComponents.setter
    def isDependentOnPhysicalTechnologyComponents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__isDependentOnPhysicalTechnologyComponents", None)
        self.__isDependentOnPhysicalTechnologyComponents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhysicalTechnologyComponent225"):
                    opp_val = getattr(item, "PhysicalTechnologyComponent225", None)
                    
                    if opp_val == self:
                        setattr(item, "PhysicalTechnologyComponent225", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhysicalTechnologyComponent225"):
                    opp_val = getattr(item, "PhysicalTechnologyComponent225", None)
                    
                    setattr(item, "PhysicalTechnologyComponent225", self)
                    

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
                if hasattr(item, "Location217"):
                    opp_val = getattr(item, "Location217", None)
                    
                    if opp_val == self:
                        setattr(item, "Location217", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Location217"):
                    opp_val = getattr(item, "Location217", None)
                    
                    setattr(item, "Location217", self)
                    

    @property
    def PhysicalTechnologyComponent333(self):
        return self.__PhysicalTechnologyComponent333

    @PhysicalTechnologyComponent333.setter
    def PhysicalTechnologyComponent333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__PhysicalTechnologyComponent333", None)
        self.__PhysicalTechnologyComponent333 = value
        
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
    def PhysicalTechnologyComponent(self):
        return self.__PhysicalTechnologyComponent

    @PhysicalTechnologyComponent.setter
    def PhysicalTechnologyComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__PhysicalTechnologyComponent", None)
        self.__PhysicalTechnologyComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isDecomposedByPhysicalTechnologyComponents"):
                opp_val = getattr(old_value, "isDecomposedByPhysicalTechnologyComponents", None)
                if opp_val == self:
                    setattr(old_value, "isDecomposedByPhysicalTechnologyComponents", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isDecomposedByPhysicalTechnologyComponents"):
                opp_val = getattr(value, "isDecomposedByPhysicalTechnologyComponents", None)
                setattr(value, "isDecomposedByPhysicalTechnologyComponents", self)

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
            if hasattr(old_value, "contentfwk_TechnologyArchitecture39"):
                opp_val = getattr(old_value, "contentfwk_TechnologyArchitecture39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_TechnologyArchitecture39"):
                opp_val = getattr(value, "contentfwk_TechnologyArchitecture39", None)
                if opp_val is None:
                    setattr(value, "contentfwk_TechnologyArchitecture39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def isRealizedByPhysicalTechnologyComponents214(self):
        return self.__isRealizedByPhysicalTechnologyComponents214

    @isRealizedByPhysicalTechnologyComponents214.setter
    def isRealizedByPhysicalTechnologyComponents214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__isRealizedByPhysicalTechnologyComponents214", None)
        self.__isRealizedByPhysicalTechnologyComponents214 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LogicalTechnologyComponent215"):
                    opp_val = getattr(item, "LogicalTechnologyComponent215", None)
                    
                    if opp_val == self:
                        setattr(item, "LogicalTechnologyComponent215", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LogicalTechnologyComponent215"):
                    opp_val = getattr(item, "LogicalTechnologyComponent215", None)
                    
                    setattr(item, "LogicalTechnologyComponent215", self)
                    

    @property
    def isDecomposedByPhysicalTechnologyComponents(self):
        return self.__isDecomposedByPhysicalTechnologyComponents

    @isDecomposedByPhysicalTechnologyComponents.setter
    def isDecomposedByPhysicalTechnologyComponents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__isDecomposedByPhysicalTechnologyComponents", None)
        self.__isDecomposedByPhysicalTechnologyComponents = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhysicalTechnologyComponent"):
                opp_val = getattr(old_value, "PhysicalTechnologyComponent", None)
                if opp_val == self:
                    setattr(old_value, "PhysicalTechnologyComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhysicalTechnologyComponent"):
                opp_val = getattr(value, "PhysicalTechnologyComponent", None)
                setattr(value, "PhysicalTechnologyComponent", self)

    @property
    def decomposesPhysicalTechnologyComponent(self):
        return self.__decomposesPhysicalTechnologyComponent

    @decomposesPhysicalTechnologyComponent.setter
    def decomposesPhysicalTechnologyComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__decomposesPhysicalTechnologyComponent", None)
        self.__decomposesPhysicalTechnologyComponent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhysicalTechnologyComponent228"):
                    opp_val = getattr(item, "PhysicalTechnologyComponent228", None)
                    
                    if opp_val == self:
                        setattr(item, "PhysicalTechnologyComponent228", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhysicalTechnologyComponent228"):
                    opp_val = getattr(item, "PhysicalTechnologyComponent228", None)
                    
                    setattr(item, "PhysicalTechnologyComponent228", self)
                    

    @property
    def PhysicalTechnologyComponent222(self):
        return self.__PhysicalTechnologyComponent222

    @PhysicalTechnologyComponent222.setter
    def PhysicalTechnologyComponent222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__PhysicalTechnologyComponent222", None)
        self.__PhysicalTechnologyComponent222 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isRequiredByPhysicalTechnologyComponent"):
                opp_val = getattr(old_value, "isRequiredByPhysicalTechnologyComponent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isRequiredByPhysicalTechnologyComponent"):
                opp_val = getattr(value, "isRequiredByPhysicalTechnologyComponent", None)
                if opp_val is None:
                    setattr(value, "isRequiredByPhysicalTechnologyComponent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PhysicalTechnologyComponent228(self):
        return self.__PhysicalTechnologyComponent228

    @PhysicalTechnologyComponent228.setter
    def PhysicalTechnologyComponent228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__PhysicalTechnologyComponent228", None)
        self.__PhysicalTechnologyComponent228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decomposesPhysicalTechnologyComponent"):
                opp_val = getattr(old_value, "decomposesPhysicalTechnologyComponent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decomposesPhysicalTechnologyComponent"):
                opp_val = getattr(value, "decomposesPhysicalTechnologyComponent", None)
                if opp_val is None:
                    setattr(value, "decomposesPhysicalTechnologyComponent", set([self]))
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
                if hasattr(item, "PhysicalApplicationComponent212"):
                    opp_val = getattr(item, "PhysicalApplicationComponent212", None)
                    
                    if opp_val == self:
                        setattr(item, "PhysicalApplicationComponent212", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhysicalApplicationComponent212"):
                    opp_val = getattr(item, "PhysicalApplicationComponent212", None)
                    
                    setattr(item, "PhysicalApplicationComponent212", self)
                    

class contentfwk_PlatformService(Element):

    def __init__(self, categoryTRM: str, standardClass: str, contentfwk_PlatformService: "contentfwk_TechnologyArchitecture" = None, suppliesPlatformServices: set["contentfwk_LogicalTechnologyComponent"] = None, PlatformService: "contentfwk_LogicalTechnologyComponent" = None):
        self.categoryTRM = categoryTRM
        self.standardClass = standardClass
        self.contentfwk_PlatformService = contentfwk_PlatformService
        self.suppliesPlatformServices = suppliesPlatformServices if suppliesPlatformServices is not None else set()
        self.PlatformService = PlatformService
        
    @property
    def standardClass(self) -> str:
        return self.__standardClass

    @standardClass.setter
    def standardClass(self, standardClass: str):
        self.__standardClass = standardClass

    @property
    def categoryTRM(self) -> str:
        return self.__categoryTRM

    @categoryTRM.setter
    def categoryTRM(self, categoryTRM: str):
        self.__categoryTRM = categoryTRM

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
                    

class contentfwk_PhysicalDataComponent(DataComponent, Element):

    pass
class contentfwk_LogicalDataComponent(DataComponent, Element):

    pass
class contentfwk_DataEntity(Element):

    def __init__(self, dataEntityCategory: str, privacyClassification: str, retentionClassification: str, contentfwk_DataEntity: "contentfwk_DataArchitecture" = None, DataEntity: "contentfwk_Actor" = None, DataEntity84: "contentfwk_Actor" = None, suppliesDataEntities: set["contentfwk_Actor"] = None, consumesDataEntities: set["contentfwk_Actor"] = None, consumesDataEntities123: set["contentfwk_Service"] = None, providesDataEntities: set["contentfwk_Service"] = None, encapsulatesDataEntities: "contentfwk_LogicalDataComponent" = None, operatesOnDataEntities: set["contentfwk_LogicalApplicationComponent"] = None, contentfwk_DataEntity131: "contentfwk_DataEntity" = None, contentfwk_DataEntity129: "contentfwk_DataEntity" = None, contentfwk_DataEntity134: "contentfwk_DataEntity" = None, contentfwk_DataEntity132: set["contentfwk_DataEntity"] = None, contentfwk_DataEntity137: "contentfwk_DataEntity" = None, contentfwk_DataEntity135: set["contentfwk_DataEntity"] = None, DataEntity141: "contentfwk_LogicalApplicationComponent" = None, DataEntity291: "contentfwk_LogicalDataComponent" = None, DataEntity357: "contentfwk_Service" = None, DataEntity359: "contentfwk_Service" = None):
        self.dataEntityCategory = dataEntityCategory
        self.privacyClassification = privacyClassification
        self.retentionClassification = retentionClassification
        self.contentfwk_DataEntity = contentfwk_DataEntity
        self.DataEntity = DataEntity
        self.DataEntity84 = DataEntity84
        self.suppliesDataEntities = suppliesDataEntities if suppliesDataEntities is not None else set()
        self.consumesDataEntities = consumesDataEntities if consumesDataEntities is not None else set()
        self.consumesDataEntities123 = consumesDataEntities123 if consumesDataEntities123 is not None else set()
        self.providesDataEntities = providesDataEntities if providesDataEntities is not None else set()
        self.encapsulatesDataEntities = encapsulatesDataEntities
        self.operatesOnDataEntities = operatesOnDataEntities if operatesOnDataEntities is not None else set()
        self.contentfwk_DataEntity131 = contentfwk_DataEntity131
        self.contentfwk_DataEntity129 = contentfwk_DataEntity129
        self.contentfwk_DataEntity134 = contentfwk_DataEntity134
        self.contentfwk_DataEntity132 = contentfwk_DataEntity132 if contentfwk_DataEntity132 is not None else set()
        self.contentfwk_DataEntity137 = contentfwk_DataEntity137
        self.contentfwk_DataEntity135 = contentfwk_DataEntity135 if contentfwk_DataEntity135 is not None else set()
        self.DataEntity141 = DataEntity141
        self.DataEntity291 = DataEntity291
        self.DataEntity357 = DataEntity357
        self.DataEntity359 = DataEntity359
        
    @property
    def retentionClassification(self) -> str:
        return self.__retentionClassification

    @retentionClassification.setter
    def retentionClassification(self, retentionClassification: str):
        self.__retentionClassification = retentionClassification

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
    def DataEntity291(self):
        return self.__DataEntity291

    @DataEntity291.setter
    def DataEntity291(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__DataEntity291", None)
        self.__DataEntity291 = value
        
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
    def contentfwk_DataEntity135(self):
        return self.__contentfwk_DataEntity135

    @contentfwk_DataEntity135.setter
    def contentfwk_DataEntity135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__contentfwk_DataEntity135", None)
        self.__contentfwk_DataEntity135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_DataEntity137"):
                    opp_val = getattr(item, "contentfwk_DataEntity137", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_DataEntity137", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_DataEntity137"):
                    opp_val = getattr(item, "contentfwk_DataEntity137", None)
                    
                    setattr(item, "contentfwk_DataEntity137", self)
                    

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
    def contentfwk_DataEntity132(self):
        return self.__contentfwk_DataEntity132

    @contentfwk_DataEntity132.setter
    def contentfwk_DataEntity132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__contentfwk_DataEntity132", None)
        self.__contentfwk_DataEntity132 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_DataEntity134"):
                    opp_val = getattr(item, "contentfwk_DataEntity134", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_DataEntity134", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_DataEntity134"):
                    opp_val = getattr(item, "contentfwk_DataEntity134", None)
                    
                    setattr(item, "contentfwk_DataEntity134", self)
                    

    @property
    def DataEntity357(self):
        return self.__DataEntity357

    @DataEntity357.setter
    def DataEntity357(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__DataEntity357", None)
        self.__DataEntity357 = value
        
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
    def providesDataEntities(self):
        return self.__providesDataEntities

    @providesDataEntities.setter
    def providesDataEntities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__providesDataEntities", None)
        self.__providesDataEntities = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service126"):
                    opp_val = getattr(item, "Service126", None)
                    
                    if opp_val == self:
                        setattr(item, "Service126", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service126"):
                    opp_val = getattr(item, "Service126", None)
                    
                    setattr(item, "Service126", self)
                    

    @property
    def DataEntity84(self):
        return self.__DataEntity84

    @DataEntity84.setter
    def DataEntity84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__DataEntity84", None)
        self.__DataEntity84 = value
        
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
    def contentfwk_DataEntity137(self):
        return self.__contentfwk_DataEntity137

    @contentfwk_DataEntity137.setter
    def contentfwk_DataEntity137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__contentfwk_DataEntity137", None)
        self.__contentfwk_DataEntity137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_DataEntity135"):
                opp_val = getattr(old_value, "contentfwk_DataEntity135", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_DataEntity135"):
                opp_val = getattr(value, "contentfwk_DataEntity135", None)
                if opp_val is None:
                    setattr(value, "contentfwk_DataEntity135", set([self]))
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
    def DataEntity141(self):
        return self.__DataEntity141

    @DataEntity141.setter
    def DataEntity141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__DataEntity141", None)
        self.__DataEntity141 = value
        
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
    def consumesDataEntities(self):
        return self.__consumesDataEntities

    @consumesDataEntities.setter
    def consumesDataEntities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__consumesDataEntities", None)
        self.__consumesDataEntities = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Actor121"):
                    opp_val = getattr(item, "Actor121", None)
                    
                    if opp_val == self:
                        setattr(item, "Actor121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Actor121"):
                    opp_val = getattr(item, "Actor121", None)
                    
                    setattr(item, "Actor121", self)
                    

    @property
    def DataEntity359(self):
        return self.__DataEntity359

    @DataEntity359.setter
    def DataEntity359(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__DataEntity359", None)
        self.__DataEntity359 = value
        
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
    def contentfwk_DataEntity134(self):
        return self.__contentfwk_DataEntity134

    @contentfwk_DataEntity134.setter
    def contentfwk_DataEntity134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__contentfwk_DataEntity134", None)
        self.__contentfwk_DataEntity134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_DataEntity132"):
                opp_val = getattr(old_value, "contentfwk_DataEntity132", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_DataEntity132"):
                opp_val = getattr(value, "contentfwk_DataEntity132", None)
                if opp_val is None:
                    setattr(value, "contentfwk_DataEntity132", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_DataEntity129(self):
        return self.__contentfwk_DataEntity129

    @contentfwk_DataEntity129.setter
    def contentfwk_DataEntity129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__contentfwk_DataEntity129", None)
        self.__contentfwk_DataEntity129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_DataEntity131"):
                opp_val = getattr(old_value, "contentfwk_DataEntity131", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_DataEntity131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_DataEntity131"):
                opp_val = getattr(value, "contentfwk_DataEntity131", None)
                setattr(value, "contentfwk_DataEntity131", self)

    @property
    def consumesDataEntities123(self):
        return self.__consumesDataEntities123

    @consumesDataEntities123.setter
    def consumesDataEntities123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__consumesDataEntities123", None)
        self.__consumesDataEntities123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service124"):
                    opp_val = getattr(item, "Service124", None)
                    
                    if opp_val == self:
                        setattr(item, "Service124", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service124"):
                    opp_val = getattr(item, "Service124", None)
                    
                    setattr(item, "Service124", self)
                    

    @property
    def suppliesDataEntities(self):
        return self.__suppliesDataEntities

    @suppliesDataEntities.setter
    def suppliesDataEntities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__suppliesDataEntities", None)
        self.__suppliesDataEntities = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Actor119"):
                    opp_val = getattr(item, "Actor119", None)
                    
                    if opp_val == self:
                        setattr(item, "Actor119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Actor119"):
                    opp_val = getattr(item, "Actor119", None)
                    
                    setattr(item, "Actor119", self)
                    

    @property
    def contentfwk_DataEntity131(self):
        return self.__contentfwk_DataEntity131

    @contentfwk_DataEntity131.setter
    def contentfwk_DataEntity131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__contentfwk_DataEntity131", None)
        self.__contentfwk_DataEntity131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_DataEntity129"):
                opp_val = getattr(old_value, "contentfwk_DataEntity129", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_DataEntity129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_DataEntity129"):
                opp_val = getattr(value, "contentfwk_DataEntity129", None)
                setattr(value, "contentfwk_DataEntity129", self)

class contentfwk_ServiceQuality(Element):

    pass
class contentfwk_Measure(Element):

    pass
class contentfwk_EnterpriseArchitecture:

    def __init__(self, ID: str, contentfwk_EnterpriseArchitecture: set["contentfwk_Architecture"] = None):
        self.ID = ID
        self.contentfwk_EnterpriseArchitecture = contentfwk_EnterpriseArchitecture if contentfwk_EnterpriseArchitecture is not None else set()
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def contentfwk_EnterpriseArchitecture(self):
        return self.__contentfwk_EnterpriseArchitecture

    @contentfwk_EnterpriseArchitecture.setter
    def contentfwk_EnterpriseArchitecture(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_EnterpriseArchitecture__contentfwk_EnterpriseArchitecture", None)
        self.__contentfwk_EnterpriseArchitecture = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_Architecture"):
                    opp_val = getattr(item, "contentfwk_Architecture", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_Architecture", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_Architecture"):
                    opp_val = getattr(item, "contentfwk_Architecture", None)
                    
                    setattr(item, "contentfwk_Architecture", self)
                    

    def forceID(self, newID: str):
        # TODO: Implement forceID method
        pass

class contentfwk_Process(Element, Standard):

    def __init__(self, processCritiality: str, isAutomated: bool, processVolumetrics: str, contentfwk_Process: "contentfwk_BusinessArchitecture" = None, Process: "contentfwk_OrganizationUnit" = None, Process91: "contentfwk_Actor" = None, Process158: "contentfwk_Function" = None, Process160: "contentfwk_Function" = None, participatesInProcesses: set["contentfwk_OrganizationUnit"] = None, isRealizedByProcesses183: set["contentfwk_Service"] = None, supportsProcesses186: set["contentfwk_Service"] = None, participatesInProcesses189: set["contentfwk_Actor"] = None, ensuresCorrectOperationOfProcesses: set["contentfwk_Control"] = None, isResolvedByProcesses: set["contentfwk_Event"] = None, isGeneratedByProcesses: set["contentfwk_Event"] = None, isProducedByProcesses: set["contentfwk_Product"] = None, Process200: "contentfwk_Process" = None, isDecomposedByProcesses: "contentfwk_Process" = None, Process203: "contentfwk_Process" = None, followsProcesses: set["contentfwk_Process"] = None, Process206: "contentfwk_Process" = None, precedesProcesses: set["contentfwk_Process"] = None, Process209: "contentfwk_Process" = None, decomposesProcess: set["contentfwk_Process"] = None, isRealizedByProcesses: set["contentfwk_Function"] = None, supportsProcesses: set["contentfwk_Function"] = None, Process233: "contentfwk_Product" = None, Process255: "contentfwk_Event" = None, Process257: "contentfwk_Event" = None, Process265: "contentfwk_Control" = None, Process373: "contentfwk_Service" = None, Process375: "contentfwk_Service" = None):
        self.processCritiality = processCritiality
        self.isAutomated = isAutomated
        self.processVolumetrics = processVolumetrics
        self.contentfwk_Process = contentfwk_Process
        self.Process = Process
        self.Process91 = Process91
        self.Process158 = Process158
        self.Process160 = Process160
        self.participatesInProcesses = participatesInProcesses if participatesInProcesses is not None else set()
        self.isRealizedByProcesses183 = isRealizedByProcesses183 if isRealizedByProcesses183 is not None else set()
        self.supportsProcesses186 = supportsProcesses186 if supportsProcesses186 is not None else set()
        self.participatesInProcesses189 = participatesInProcesses189 if participatesInProcesses189 is not None else set()
        self.ensuresCorrectOperationOfProcesses = ensuresCorrectOperationOfProcesses if ensuresCorrectOperationOfProcesses is not None else set()
        self.isResolvedByProcesses = isResolvedByProcesses if isResolvedByProcesses is not None else set()
        self.isGeneratedByProcesses = isGeneratedByProcesses if isGeneratedByProcesses is not None else set()
        self.isProducedByProcesses = isProducedByProcesses if isProducedByProcesses is not None else set()
        self.Process200 = Process200
        self.isDecomposedByProcesses = isDecomposedByProcesses
        self.Process203 = Process203
        self.followsProcesses = followsProcesses if followsProcesses is not None else set()
        self.Process206 = Process206
        self.precedesProcesses = precedesProcesses if precedesProcesses is not None else set()
        self.Process209 = Process209
        self.decomposesProcess = decomposesProcess if decomposesProcess is not None else set()
        self.isRealizedByProcesses = isRealizedByProcesses if isRealizedByProcesses is not None else set()
        self.supportsProcesses = supportsProcesses if supportsProcesses is not None else set()
        self.Process233 = Process233
        self.Process255 = Process255
        self.Process257 = Process257
        self.Process265 = Process265
        self.Process373 = Process373
        self.Process375 = Process375
        
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
    def isAutomated(self) -> bool:
        return self.__isAutomated

    @isAutomated.setter
    def isAutomated(self, isAutomated: bool):
        self.__isAutomated = isAutomated

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
                if hasattr(item, "Product197"):
                    opp_val = getattr(item, "Product197", None)
                    
                    if opp_val == self:
                        setattr(item, "Product197", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Product197"):
                    opp_val = getattr(item, "Product197", None)
                    
                    setattr(item, "Product197", self)
                    

    @property
    def Process200(self):
        return self.__Process200

    @Process200.setter
    def Process200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process200", None)
        self.__Process200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isDecomposedByProcesses"):
                opp_val = getattr(old_value, "isDecomposedByProcesses", None)
                if opp_val == self:
                    setattr(old_value, "isDecomposedByProcesses", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isDecomposedByProcesses"):
                opp_val = getattr(value, "isDecomposedByProcesses", None)
                setattr(value, "isDecomposedByProcesses", self)

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
                if hasattr(item, "OrganizationUnit181"):
                    opp_val = getattr(item, "OrganizationUnit181", None)
                    
                    if opp_val == self:
                        setattr(item, "OrganizationUnit181", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OrganizationUnit181"):
                    opp_val = getattr(item, "OrganizationUnit181", None)
                    
                    setattr(item, "OrganizationUnit181", self)
                    

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
                if hasattr(item, "Function177"):
                    opp_val = getattr(item, "Function177", None)
                    
                    if opp_val == self:
                        setattr(item, "Function177", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function177"):
                    opp_val = getattr(item, "Function177", None)
                    
                    setattr(item, "Function177", self)
                    

    @property
    def Process209(self):
        return self.__Process209

    @Process209.setter
    def Process209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process209", None)
        self.__Process209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decomposesProcess"):
                opp_val = getattr(old_value, "decomposesProcess", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decomposesProcess"):
                opp_val = getattr(value, "decomposesProcess", None)
                if opp_val is None:
                    setattr(value, "decomposesProcess", set([self]))
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
            if hasattr(old_value, "contentfwk_BusinessArchitecture17"):
                opp_val = getattr(old_value, "contentfwk_BusinessArchitecture17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_BusinessArchitecture17"):
                opp_val = getattr(value, "contentfwk_BusinessArchitecture17", None)
                if opp_val is None:
                    setattr(value, "contentfwk_BusinessArchitecture17", set([self]))
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
                if hasattr(item, "Function179"):
                    opp_val = getattr(item, "Function179", None)
                    
                    if opp_val == self:
                        setattr(item, "Function179", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function179"):
                    opp_val = getattr(item, "Function179", None)
                    
                    setattr(item, "Function179", self)
                    

    @property
    def Process255(self):
        return self.__Process255

    @Process255.setter
    def Process255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process255", None)
        self.__Process255 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resolvesEvents254"):
                opp_val = getattr(old_value, "resolvesEvents254", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resolvesEvents254"):
                opp_val = getattr(value, "resolvesEvents254", None)
                if opp_val is None:
                    setattr(value, "resolvesEvents254", set([self]))
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
    def Process373(self):
        return self.__Process373

    @Process373.setter
    def Process373(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process373", None)
        self.__Process373 = value
        
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
    def Process91(self):
        return self.__Process91

    @Process91.setter
    def Process91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process91", None)
        self.__Process91 = value
        
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
    def decomposesProcess(self):
        return self.__decomposesProcess

    @decomposesProcess.setter
    def decomposesProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__decomposesProcess", None)
        self.__decomposesProcess = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Process209"):
                    opp_val = getattr(item, "Process209", None)
                    
                    if opp_val == self:
                        setattr(item, "Process209", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Process209"):
                    opp_val = getattr(item, "Process209", None)
                    
                    setattr(item, "Process209", self)
                    

    @property
    def Process375(self):
        return self.__Process375

    @Process375.setter
    def Process375(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process375", None)
        self.__Process375 = value
        
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
    def Process257(self):
        return self.__Process257

    @Process257.setter
    def Process257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process257", None)
        self.__Process257 = value
        
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
    def Process158(self):
        return self.__Process158

    @Process158.setter
    def Process158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process158", None)
        self.__Process158 = value
        
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
                if hasattr(item, "Process203"):
                    opp_val = getattr(item, "Process203", None)
                    
                    if opp_val == self:
                        setattr(item, "Process203", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Process203"):
                    opp_val = getattr(item, "Process203", None)
                    
                    setattr(item, "Process203", self)
                    

    @property
    def Process203(self):
        return self.__Process203

    @Process203.setter
    def Process203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process203", None)
        self.__Process203 = value
        
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
    def Process265(self):
        return self.__Process265

    @Process265.setter
    def Process265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process265", None)
        self.__Process265 = value
        
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
    def supportsProcesses186(self):
        return self.__supportsProcesses186

    @supportsProcesses186.setter
    def supportsProcesses186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__supportsProcesses186", None)
        self.__supportsProcesses186 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service187"):
                    opp_val = getattr(item, "Service187", None)
                    
                    if opp_val == self:
                        setattr(item, "Service187", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service187"):
                    opp_val = getattr(item, "Service187", None)
                    
                    setattr(item, "Service187", self)
                    

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
                if hasattr(item, "Event195"):
                    opp_val = getattr(item, "Event195", None)
                    
                    if opp_val == self:
                        setattr(item, "Event195", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Event195"):
                    opp_val = getattr(item, "Event195", None)
                    
                    setattr(item, "Event195", self)
                    

    @property
    def isDecomposedByProcesses(self):
        return self.__isDecomposedByProcesses

    @isDecomposedByProcesses.setter
    def isDecomposedByProcesses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__isDecomposedByProcesses", None)
        self.__isDecomposedByProcesses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Process200"):
                opp_val = getattr(old_value, "Process200", None)
                if opp_val == self:
                    setattr(old_value, "Process200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Process200"):
                opp_val = getattr(value, "Process200", None)
                setattr(value, "Process200", self)

    @property
    def participatesInProcesses189(self):
        return self.__participatesInProcesses189

    @participatesInProcesses189.setter
    def participatesInProcesses189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__participatesInProcesses189", None)
        self.__participatesInProcesses189 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Actor190"):
                    opp_val = getattr(item, "Actor190", None)
                    
                    if opp_val == self:
                        setattr(item, "Actor190", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Actor190"):
                    opp_val = getattr(item, "Actor190", None)
                    
                    setattr(item, "Actor190", self)
                    

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
                if hasattr(item, "Event193"):
                    opp_val = getattr(item, "Event193", None)
                    
                    if opp_val == self:
                        setattr(item, "Event193", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Event193"):
                    opp_val = getattr(item, "Event193", None)
                    
                    setattr(item, "Event193", self)
                    

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
                if hasattr(item, "Process206"):
                    opp_val = getattr(item, "Process206", None)
                    
                    if opp_val == self:
                        setattr(item, "Process206", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Process206"):
                    opp_val = getattr(item, "Process206", None)
                    
                    setattr(item, "Process206", self)
                    

    @property
    def Process233(self):
        return self.__Process233

    @Process233.setter
    def Process233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process233", None)
        self.__Process233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "producesProducts232"):
                opp_val = getattr(old_value, "producesProducts232", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "producesProducts232"):
                opp_val = getattr(value, "producesProducts232", None)
                if opp_val is None:
                    setattr(value, "producesProducts232", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def isRealizedByProcesses183(self):
        return self.__isRealizedByProcesses183

    @isRealizedByProcesses183.setter
    def isRealizedByProcesses183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__isRealizedByProcesses183", None)
        self.__isRealizedByProcesses183 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service184"):
                    opp_val = getattr(item, "Service184", None)
                    
                    if opp_val == self:
                        setattr(item, "Service184", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service184"):
                    opp_val = getattr(item, "Service184", None)
                    
                    setattr(item, "Service184", self)
                    

    @property
    def Process160(self):
        return self.__Process160

    @Process160.setter
    def Process160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process160", None)
        self.__Process160 = value
        
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
    def Process206(self):
        return self.__Process206

    @Process206.setter
    def Process206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process206", None)
        self.__Process206 = value
        
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

class contentfwk_BusinessService(Element, Service):

    pass
class contentfwk_Function(Element, Standard):

    pass
class contentfwk_Role(Element):

    def __init__(self, estimatedFTEs: str, contentfwk_Role: "contentfwk_BusinessArchitecture" = None, Role: "contentfwk_Actor" = None, performsTaskInRoles: set["contentfwk_Actor"] = None, canBeAccessedByRoles: set["contentfwk_Function"] = None, Role114: "contentfwk_Role" = None, isDecomposedByRoles: "contentfwk_Role" = None, Role117: "contentfwk_Role" = None, decomposesRole: set["contentfwk_Role"] = None, Role162: "contentfwk_Function" = None):
        self.estimatedFTEs = estimatedFTEs
        self.contentfwk_Role = contentfwk_Role
        self.Role = Role
        self.performsTaskInRoles = performsTaskInRoles if performsTaskInRoles is not None else set()
        self.canBeAccessedByRoles = canBeAccessedByRoles if canBeAccessedByRoles is not None else set()
        self.Role114 = Role114
        self.isDecomposedByRoles = isDecomposedByRoles
        self.Role117 = Role117
        self.decomposesRole = decomposesRole if decomposesRole is not None else set()
        self.Role162 = Role162
        
    @property
    def estimatedFTEs(self) -> str:
        return self.__estimatedFTEs

    @estimatedFTEs.setter
    def estimatedFTEs(self, estimatedFTEs: str):
        self.__estimatedFTEs = estimatedFTEs

    @property
    def Role117(self):
        return self.__Role117

    @Role117.setter
    def Role117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Role__Role117", None)
        self.__Role117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decomposesRole"):
                opp_val = getattr(old_value, "decomposesRole", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decomposesRole"):
                opp_val = getattr(value, "decomposesRole", None)
                if opp_val is None:
                    setattr(value, "decomposesRole", set([self]))
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
                if hasattr(item, "Actor109"):
                    opp_val = getattr(item, "Actor109", None)
                    
                    if opp_val == self:
                        setattr(item, "Actor109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Actor109"):
                    opp_val = getattr(item, "Actor109", None)
                    
                    setattr(item, "Actor109", self)
                    

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
                if hasattr(item, "Function111"):
                    opp_val = getattr(item, "Function111", None)
                    
                    if opp_val == self:
                        setattr(item, "Function111", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function111"):
                    opp_val = getattr(item, "Function111", None)
                    
                    setattr(item, "Function111", self)
                    

    @property
    def isDecomposedByRoles(self):
        return self.__isDecomposedByRoles

    @isDecomposedByRoles.setter
    def isDecomposedByRoles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Role__isDecomposedByRoles", None)
        self.__isDecomposedByRoles = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Role114"):
                opp_val = getattr(old_value, "Role114", None)
                if opp_val == self:
                    setattr(old_value, "Role114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Role114"):
                opp_val = getattr(value, "Role114", None)
                setattr(value, "Role114", self)

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
    def decomposesRole(self):
        return self.__decomposesRole

    @decomposesRole.setter
    def decomposesRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Role__decomposesRole", None)
        self.__decomposesRole = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Role117"):
                    opp_val = getattr(item, "Role117", None)
                    
                    if opp_val == self:
                        setattr(item, "Role117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Role117"):
                    opp_val = getattr(item, "Role117", None)
                    
                    setattr(item, "Role117", self)
                    

    @property
    def Role114(self):
        return self.__Role114

    @Role114.setter
    def Role114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Role__Role114", None)
        self.__Role114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isDecomposedByRoles"):
                opp_val = getattr(old_value, "isDecomposedByRoles", None)
                if opp_val == self:
                    setattr(old_value, "isDecomposedByRoles", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isDecomposedByRoles"):
                opp_val = getattr(value, "isDecomposedByRoles", None)
                setattr(value, "isDecomposedByRoles", self)

    @property
    def Role162(self):
        return self.__Role162

    @Role162.setter
    def Role162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Role__Role162", None)
        self.__Role162 = value
        
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

class contentfwk_Actor(Element):

    def __init__(self, FTEs: str, actorGoal: str, actorTasks: str, contentfwk_Actor: "contentfwk_BusinessArchitecture" = None, Actor: "contentfwk_OrganizationUnit" = None, supportsActors: set["contentfwk_Function"] = None, isAssumedByActors: set["contentfwk_Role"] = None, involvesActors: set["contentfwk_Process"] = None, isProvidedToActors: set["contentfwk_Service"] = None, isResolvedByActors: set["contentfwk_Event"] = None, isGeneratedByActors: set["contentfwk_Event"] = None, containsActors98: "contentfwk_Location" = None, isPerformedByActors: set["contentfwk_Function"] = None, Actor104: "contentfwk_Actor" = None, isDecomposedByActors: "contentfwk_Actor" = None, Actor107: "contentfwk_Actor" = None, decomposesActor: set["contentfwk_Actor"] = None, Actor109: "contentfwk_Role" = None, isSuppliedByActors: set["contentfwk_DataEntity"] = None, isConsumedByActors: set["contentfwk_DataEntity"] = None, containsActors: "contentfwk_OrganizationUnit" = None, Actor119: "contentfwk_DataEntity" = None, Actor121: "contentfwk_DataEntity" = None, Actor152: "contentfwk_Function" = None, Actor164: "contentfwk_Function" = None, Actor190: "contentfwk_Process" = None, Actor260: "contentfwk_Event" = None, Actor263: "contentfwk_Event" = None, Actor272: "contentfwk_Location" = None, Actor353: "contentfwk_Service" = None):
        self.FTEs = FTEs
        self.actorGoal = actorGoal
        self.actorTasks = actorTasks
        self.contentfwk_Actor = contentfwk_Actor
        self.Actor = Actor
        self.supportsActors = supportsActors if supportsActors is not None else set()
        self.isAssumedByActors = isAssumedByActors if isAssumedByActors is not None else set()
        self.involvesActors = involvesActors if involvesActors is not None else set()
        self.isProvidedToActors = isProvidedToActors if isProvidedToActors is not None else set()
        self.isResolvedByActors = isResolvedByActors if isResolvedByActors is not None else set()
        self.isGeneratedByActors = isGeneratedByActors if isGeneratedByActors is not None else set()
        self.containsActors98 = containsActors98
        self.isPerformedByActors = isPerformedByActors if isPerformedByActors is not None else set()
        self.Actor104 = Actor104
        self.isDecomposedByActors = isDecomposedByActors
        self.Actor107 = Actor107
        self.decomposesActor = decomposesActor if decomposesActor is not None else set()
        self.Actor109 = Actor109
        self.isSuppliedByActors = isSuppliedByActors if isSuppliedByActors is not None else set()
        self.isConsumedByActors = isConsumedByActors if isConsumedByActors is not None else set()
        self.containsActors = containsActors
        self.Actor119 = Actor119
        self.Actor121 = Actor121
        self.Actor152 = Actor152
        self.Actor164 = Actor164
        self.Actor190 = Actor190
        self.Actor260 = Actor260
        self.Actor263 = Actor263
        self.Actor272 = Actor272
        self.Actor353 = Actor353
        
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
    def Actor109(self):
        return self.__Actor109

    @Actor109.setter
    def Actor109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor109", None)
        self.__Actor109 = value
        
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
    def Actor164(self):
        return self.__Actor164

    @Actor164.setter
    def Actor164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor164", None)
        self.__Actor164 = value
        
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
    def isProvidedToActors(self):
        return self.__isProvidedToActors

    @isProvidedToActors.setter
    def isProvidedToActors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__isProvidedToActors", None)
        self.__isProvidedToActors = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service93"):
                    opp_val = getattr(item, "Service93", None)
                    
                    if opp_val == self:
                        setattr(item, "Service93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service93"):
                    opp_val = getattr(item, "Service93", None)
                    
                    setattr(item, "Service93", self)
                    

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
            if hasattr(old_value, "contentfwk_BusinessArchitecture9"):
                opp_val = getattr(old_value, "contentfwk_BusinessArchitecture9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_BusinessArchitecture9"):
                opp_val = getattr(value, "contentfwk_BusinessArchitecture9", None)
                if opp_val is None:
                    setattr(value, "contentfwk_BusinessArchitecture9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "belongsToOrganizationUnit"):
                opp_val = getattr(old_value, "belongsToOrganizationUnit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "belongsToOrganizationUnit"):
                opp_val = getattr(value, "belongsToOrganizationUnit", None)
                if opp_val is None:
                    setattr(value, "belongsToOrganizationUnit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Actor263(self):
        return self.__Actor263

    @Actor263.setter
    def Actor263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor263", None)
        self.__Actor263 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generatesEvents262"):
                opp_val = getattr(old_value, "generatesEvents262", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generatesEvents262"):
                opp_val = getattr(value, "generatesEvents262", None)
                if opp_val is None:
                    setattr(value, "generatesEvents262", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def containsActors98(self):
        return self.__containsActors98

    @containsActors98.setter
    def containsActors98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__containsActors98", None)
        self.__containsActors98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Location99"):
                opp_val = getattr(old_value, "Location99", None)
                if opp_val == self:
                    setattr(old_value, "Location99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Location99"):
                opp_val = getattr(value, "Location99", None)
                setattr(value, "Location99", self)

    @property
    def isDecomposedByActors(self):
        return self.__isDecomposedByActors

    @isDecomposedByActors.setter
    def isDecomposedByActors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__isDecomposedByActors", None)
        self.__isDecomposedByActors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Actor104"):
                opp_val = getattr(old_value, "Actor104", None)
                if opp_val == self:
                    setattr(old_value, "Actor104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actor104"):
                opp_val = getattr(value, "Actor104", None)
                setattr(value, "Actor104", self)

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
                if hasattr(item, "Function88"):
                    opp_val = getattr(item, "Function88", None)
                    
                    if opp_val == self:
                        setattr(item, "Function88", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function88"):
                    opp_val = getattr(item, "Function88", None)
                    
                    setattr(item, "Function88", self)
                    

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
                if hasattr(item, "Function101"):
                    opp_val = getattr(item, "Function101", None)
                    
                    if opp_val == self:
                        setattr(item, "Function101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function101"):
                    opp_val = getattr(item, "Function101", None)
                    
                    setattr(item, "Function101", self)
                    

    @property
    def Actor353(self):
        return self.__Actor353

    @Actor353.setter
    def Actor353(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor353", None)
        self.__Actor353 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consumesServices"):
                opp_val = getattr(old_value, "consumesServices", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consumesServices"):
                opp_val = getattr(value, "consumesServices", None)
                if opp_val is None:
                    setattr(value, "consumesServices", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Actor190(self):
        return self.__Actor190

    @Actor190.setter
    def Actor190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor190", None)
        self.__Actor190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "participatesInProcesses189"):
                opp_val = getattr(old_value, "participatesInProcesses189", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "participatesInProcesses189"):
                opp_val = getattr(value, "participatesInProcesses189", None)
                if opp_val is None:
                    setattr(value, "participatesInProcesses189", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Actor104(self):
        return self.__Actor104

    @Actor104.setter
    def Actor104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor104", None)
        self.__Actor104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isDecomposedByActors"):
                opp_val = getattr(old_value, "isDecomposedByActors", None)
                if opp_val == self:
                    setattr(old_value, "isDecomposedByActors", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isDecomposedByActors"):
                opp_val = getattr(value, "isDecomposedByActors", None)
                setattr(value, "isDecomposedByActors", self)

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
                if hasattr(item, "DataEntity84"):
                    opp_val = getattr(item, "DataEntity84", None)
                    
                    if opp_val == self:
                        setattr(item, "DataEntity84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataEntity84"):
                    opp_val = getattr(item, "DataEntity84", None)
                    
                    setattr(item, "DataEntity84", self)
                    

    @property
    def Actor260(self):
        return self.__Actor260

    @Actor260.setter
    def Actor260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor260", None)
        self.__Actor260 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resolvesEvents259"):
                opp_val = getattr(old_value, "resolvesEvents259", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resolvesEvents259"):
                opp_val = getattr(value, "resolvesEvents259", None)
                if opp_val is None:
                    setattr(value, "resolvesEvents259", set([self]))
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
                if hasattr(item, "Process91"):
                    opp_val = getattr(item, "Process91", None)
                    
                    if opp_val == self:
                        setattr(item, "Process91", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Process91"):
                    opp_val = getattr(item, "Process91", None)
                    
                    setattr(item, "Process91", self)
                    

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
            if hasattr(old_value, "OrganizationUnit86"):
                opp_val = getattr(old_value, "OrganizationUnit86", None)
                if opp_val == self:
                    setattr(old_value, "OrganizationUnit86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OrganizationUnit86"):
                opp_val = getattr(value, "OrganizationUnit86", None)
                setattr(value, "OrganizationUnit86", self)

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
                if hasattr(item, "Event96"):
                    opp_val = getattr(item, "Event96", None)
                    
                    if opp_val == self:
                        setattr(item, "Event96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Event96"):
                    opp_val = getattr(item, "Event96", None)
                    
                    setattr(item, "Event96", self)
                    

    @property
    def Actor272(self):
        return self.__Actor272

    @Actor272.setter
    def Actor272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor272", None)
        self.__Actor272 = value
        
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
    def Actor121(self):
        return self.__Actor121

    @Actor121.setter
    def Actor121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor121", None)
        self.__Actor121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consumesDataEntities"):
                opp_val = getattr(old_value, "consumesDataEntities", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consumesDataEntities"):
                opp_val = getattr(value, "consumesDataEntities", None)
                if opp_val is None:
                    setattr(value, "consumesDataEntities", set([self]))
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
    def decomposesActor(self):
        return self.__decomposesActor

    @decomposesActor.setter
    def decomposesActor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__decomposesActor", None)
        self.__decomposesActor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Actor107"):
                    opp_val = getattr(item, "Actor107", None)
                    
                    if opp_val == self:
                        setattr(item, "Actor107", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Actor107"):
                    opp_val = getattr(item, "Actor107", None)
                    
                    setattr(item, "Actor107", self)
                    

    @property
    def Actor107(self):
        return self.__Actor107

    @Actor107.setter
    def Actor107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor107", None)
        self.__Actor107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decomposesActor"):
                opp_val = getattr(old_value, "decomposesActor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decomposesActor"):
                opp_val = getattr(value, "decomposesActor", None)
                if opp_val is None:
                    setattr(value, "decomposesActor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Actor119(self):
        return self.__Actor119

    @Actor119.setter
    def Actor119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor119", None)
        self.__Actor119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "suppliesDataEntities"):
                opp_val = getattr(old_value, "suppliesDataEntities", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "suppliesDataEntities"):
                opp_val = getattr(value, "suppliesDataEntities", None)
                if opp_val is None:
                    setattr(value, "suppliesDataEntities", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Actor152(self):
        return self.__Actor152

    @Actor152.setter
    def Actor152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor152", None)
        self.__Actor152 = value
        
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

class contentfwk_OrganizationUnit(Element):

    def __init__(self, headcount: str, contentfwk_OrganizationUnit: "contentfwk_BusinessArchitecture" = None, OrganizationUnit: "contentfwk_Driver" = None, isOwnedAndGovernedByOrganizationUnits: set["contentfwk_Service"] = None, belongsToOrganizationUnit: set["contentfwk_Actor"] = None, isOwnedByOrganizationUnit: set["contentfwk_Function"] = None, involvesOrganizationUnits: set["contentfwk_Process"] = None, motivatesOrganizationUnits: set["contentfwk_Driver"] = None, isProducedByOrganizationUnits: set["contentfwk_Product"] = None, containsOrganizationUnits: "contentfwk_Location" = None, OrganizationUnit78: "contentfwk_OrganizationUnit" = None, isDecomposedByOrganizationUnits: "contentfwk_OrganizationUnit" = None, OrganizationUnit81: "contentfwk_OrganizationUnit" = None, decomposesOrganizationUnit: set["contentfwk_OrganizationUnit"] = None, OrganizationUnit86: "contentfwk_Actor" = None, OrganizationUnit154: "contentfwk_Function" = None, OrganizationUnit181: "contentfwk_Process" = None, OrganizationUnit230: "contentfwk_Product" = None, OrganizationUnit275: "contentfwk_Location" = None, OrganizationUnit369: "contentfwk_Service" = None):
        self.headcount = headcount
        self.contentfwk_OrganizationUnit = contentfwk_OrganizationUnit
        self.OrganizationUnit = OrganizationUnit
        self.isOwnedAndGovernedByOrganizationUnits = isOwnedAndGovernedByOrganizationUnits if isOwnedAndGovernedByOrganizationUnits is not None else set()
        self.belongsToOrganizationUnit = belongsToOrganizationUnit if belongsToOrganizationUnit is not None else set()
        self.isOwnedByOrganizationUnit = isOwnedByOrganizationUnit if isOwnedByOrganizationUnit is not None else set()
        self.involvesOrganizationUnits = involvesOrganizationUnits if involvesOrganizationUnits is not None else set()
        self.motivatesOrganizationUnits = motivatesOrganizationUnits if motivatesOrganizationUnits is not None else set()
        self.isProducedByOrganizationUnits = isProducedByOrganizationUnits if isProducedByOrganizationUnits is not None else set()
        self.containsOrganizationUnits = containsOrganizationUnits
        self.OrganizationUnit78 = OrganizationUnit78
        self.isDecomposedByOrganizationUnits = isDecomposedByOrganizationUnits
        self.OrganizationUnit81 = OrganizationUnit81
        self.decomposesOrganizationUnit = decomposesOrganizationUnit if decomposesOrganizationUnit is not None else set()
        self.OrganizationUnit86 = OrganizationUnit86
        self.OrganizationUnit154 = OrganizationUnit154
        self.OrganizationUnit181 = OrganizationUnit181
        self.OrganizationUnit230 = OrganizationUnit230
        self.OrganizationUnit275 = OrganizationUnit275
        self.OrganizationUnit369 = OrganizationUnit369
        
    @property
    def headcount(self) -> str:
        return self.__headcount

    @headcount.setter
    def headcount(self, headcount: str):
        self.__headcount = headcount

    @property
    def OrganizationUnit81(self):
        return self.__OrganizationUnit81

    @OrganizationUnit81.setter
    def OrganizationUnit81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit81", None)
        self.__OrganizationUnit81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decomposesOrganizationUnit"):
                opp_val = getattr(old_value, "decomposesOrganizationUnit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decomposesOrganizationUnit"):
                opp_val = getattr(value, "decomposesOrganizationUnit", None)
                if opp_val is None:
                    setattr(value, "decomposesOrganizationUnit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OrganizationUnit86(self):
        return self.__OrganizationUnit86

    @OrganizationUnit86.setter
    def OrganizationUnit86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit86", None)
        self.__OrganizationUnit86 = value
        
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
    def decomposesOrganizationUnit(self):
        return self.__decomposesOrganizationUnit

    @decomposesOrganizationUnit.setter
    def decomposesOrganizationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__decomposesOrganizationUnit", None)
        self.__decomposesOrganizationUnit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OrganizationUnit81"):
                    opp_val = getattr(item, "OrganizationUnit81", None)
                    
                    if opp_val == self:
                        setattr(item, "OrganizationUnit81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OrganizationUnit81"):
                    opp_val = getattr(item, "OrganizationUnit81", None)
                    
                    setattr(item, "OrganizationUnit81", self)
                    

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
    def OrganizationUnit275(self):
        return self.__OrganizationUnit275

    @OrganizationUnit275.setter
    def OrganizationUnit275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit275", None)
        self.__OrganizationUnit275 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operatesInLocation274"):
                opp_val = getattr(old_value, "operatesInLocation274", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operatesInLocation274"):
                opp_val = getattr(value, "operatesInLocation274", None)
                if opp_val is None:
                    setattr(value, "operatesInLocation274", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OrganizationUnit369(self):
        return self.__OrganizationUnit369

    @OrganizationUnit369.setter
    def OrganizationUnit369(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit369", None)
        self.__OrganizationUnit369 = value
        
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
    def isOwnedByOrganizationUnit(self):
        return self.__isOwnedByOrganizationUnit

    @isOwnedByOrganizationUnit.setter
    def isOwnedByOrganizationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__isOwnedByOrganizationUnit", None)
        self.__isOwnedByOrganizationUnit = value if value is not None else set()
        
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
    def contentfwk_OrganizationUnit(self):
        return self.__contentfwk_OrganizationUnit

    @contentfwk_OrganizationUnit.setter
    def contentfwk_OrganizationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__contentfwk_OrganizationUnit", None)
        self.__contentfwk_OrganizationUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_BusinessArchitecture7"):
                opp_val = getattr(old_value, "contentfwk_BusinessArchitecture7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_BusinessArchitecture7"):
                opp_val = getattr(value, "contentfwk_BusinessArchitecture7", None)
                if opp_val is None:
                    setattr(value, "contentfwk_BusinessArchitecture7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OrganizationUnit154(self):
        return self.__OrganizationUnit154

    @OrganizationUnit154.setter
    def OrganizationUnit154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit154", None)
        self.__OrganizationUnit154 = value
        
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
    def OrganizationUnit181(self):
        return self.__OrganizationUnit181

    @OrganizationUnit181.setter
    def OrganizationUnit181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit181", None)
        self.__OrganizationUnit181 = value
        
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
    def belongsToOrganizationUnit(self):
        return self.__belongsToOrganizationUnit

    @belongsToOrganizationUnit.setter
    def belongsToOrganizationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__belongsToOrganizationUnit", None)
        self.__belongsToOrganizationUnit = value if value is not None else set()
        
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
    def OrganizationUnit230(self):
        return self.__OrganizationUnit230

    @OrganizationUnit230.setter
    def OrganizationUnit230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit230", None)
        self.__OrganizationUnit230 = value
        
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
    def isDecomposedByOrganizationUnits(self):
        return self.__isDecomposedByOrganizationUnits

    @isDecomposedByOrganizationUnits.setter
    def isDecomposedByOrganizationUnits(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__isDecomposedByOrganizationUnits", None)
        self.__isDecomposedByOrganizationUnits = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OrganizationUnit78"):
                opp_val = getattr(old_value, "OrganizationUnit78", None)
                if opp_val == self:
                    setattr(old_value, "OrganizationUnit78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OrganizationUnit78"):
                opp_val = getattr(value, "OrganizationUnit78", None)
                setattr(value, "OrganizationUnit78", self)

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
                if hasattr(item, "Driver73"):
                    opp_val = getattr(item, "Driver73", None)
                    
                    if opp_val == self:
                        setattr(item, "Driver73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Driver73"):
                    opp_val = getattr(item, "Driver73", None)
                    
                    setattr(item, "Driver73", self)
                    

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
    def OrganizationUnit78(self):
        return self.__OrganizationUnit78

    @OrganizationUnit78.setter
    def OrganizationUnit78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit78", None)
        self.__OrganizationUnit78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isDecomposedByOrganizationUnits"):
                opp_val = getattr(old_value, "isDecomposedByOrganizationUnits", None)
                if opp_val == self:
                    setattr(old_value, "isDecomposedByOrganizationUnits", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isDecomposedByOrganizationUnits"):
                opp_val = getattr(value, "isDecomposedByOrganizationUnits", None)
                setattr(value, "isDecomposedByOrganizationUnits", self)

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

class contentfwk_Objective(Element):

    pass
class contentfwk_Goal(Element):

    pass
class contentfwk_Driver(Element):

    pass
class Architecture:

    pass
class contentfwk_DataArchitecture(Architecture):

    pass
class contentfwk_TechnologyArchitecture(Architecture):

    pass
class contentfwk_StrategicArchitecture(Architecture):

    pass
class contentfwk_ApplicationArchitecture(Architecture):

    pass
class contentfwk_BusinessArchitecture(Architecture):

    pass
class contentfwk_Architecture(ABC):

    def __init__(self, ID: str, contentfwk_Architecture: "contentfwk_EnterpriseArchitecture" = None):
        self.ID = ID
        self.contentfwk_Architecture = contentfwk_Architecture
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def contentfwk_Architecture(self):
        return self.__contentfwk_Architecture

    @contentfwk_Architecture.setter
    def contentfwk_Architecture(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Architecture__contentfwk_Architecture", None)
        self.__contentfwk_Architecture = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_EnterpriseArchitecture"):
                opp_val = getattr(old_value, "contentfwk_EnterpriseArchitecture", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_EnterpriseArchitecture"):
                opp_val = getattr(value, "contentfwk_EnterpriseArchitecture", None)
                if opp_val is None:
                    setattr(value, "contentfwk_EnterpriseArchitecture", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def forceID(self, newID: str):
        # TODO: Implement forceID method
        pass
