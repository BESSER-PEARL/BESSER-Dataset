from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

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

    def __init__(self, standardClass: str, standardCreationDate: date, lastStandardCreationDate: date, nextStandardCreationDate: date, retireDate: str):
        self.standardClass = standardClass
        self.standardCreationDate = standardCreationDate
        self.lastStandardCreationDate = lastStandardCreationDate
        self.nextStandardCreationDate = nextStandardCreationDate
        self.retireDate = retireDate
        
    @property
    def nextStandardCreationDate(self) -> date:
        return self.__nextStandardCreationDate

    @nextStandardCreationDate.setter
    def nextStandardCreationDate(self, nextStandardCreationDate: date):
        self.__nextStandardCreationDate = nextStandardCreationDate

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

    @property
    def retireDate(self) -> str:
        return self.__retireDate

    @retireDate.setter
    def retireDate(self, retireDate: str):
        self.__retireDate = retireDate

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
class contentfwk_Constraint(StrategicElement):

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

class contentfwk_Assumption(StrategicElement):

    pass
class contentfwk_Gap(StrategicElement):

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
    def metric(self) -> str:
        return self.__metric

    @metric.setter
    def metric(self, metric: str):
        self.__metric = metric

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

    @property
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

class contentfwk_WorkPackage(StrategicElement):

    def __init__(self, workPackageCategory: str, 336: "contentfwk_Capability" = None, 338: set["contentfwk_Capability"] = None):
        self.workPackageCategory = workPackageCategory
        self.336 = 336
        self.338 = 338 if 338 is not None else set()
        
    @property
    def workPackageCategory(self) -> str:
        return self.__workPackageCategory

    @workPackageCategory.setter
    def workPackageCategory(self, workPackageCategory: str):
        self.__workPackageCategory = workPackageCategory

    @property
    def 336(self):
        return self.__336

    @336.setter
    def 336(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_WorkPackage__336", None)
        self.__336 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "335"):
                opp_val = getattr(old_value, "335", None)
                if opp_val == self:
                    setattr(old_value, "335", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "335"):
                opp_val = getattr(value, "335", None)
                setattr(value, "335", self)

    @property
    def 338(self):
        return self.__338

    @338.setter
    def 338(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_WorkPackage__338", None)
        self.__338 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "339"):
                    opp_val = getattr(item, "339", None)
                    
                    if opp_val == self:
                        setattr(item, "339", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "339"):
                    opp_val = getattr(item, "339", None)
                    
                    setattr(item, "339", self)
                    

class contentfwk_Element:

    def __init__(self, name: str, description: str, category: str, sourceDescr: str, ownerDescr: str, ID: str, 309: "contentfwk_Element" = None, 308: set["contentfwk_Element"] = None, 313: "contentfwk_Element" = None, 312: set["contentfwk_Element"] = None, contentfwk_Element: "contentfwk_Container" = None):
        self.name = name
        self.description = description
        self.category = category
        self.sourceDescr = sourceDescr
        self.ownerDescr = ownerDescr
        self.ID = ID
        self.309 = 309
        self.308 = 308 if 308 is not None else set()
        self.313 = 313
        self.312 = 312 if 312 is not None else set()
        self.contentfwk_Element = contentfwk_Element
        
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
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 313(self):
        return self.__313

    @313.setter
    def 313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Element__313", None)
        self.__313 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "312"):
                opp_val = getattr(old_value, "312", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "312"):
                opp_val = getattr(value, "312", None)
                if opp_val is None:
                    setattr(value, "312", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 312(self):
        return self.__312

    @312.setter
    def 312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Element__312", None)
        self.__312 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "313"):
                    opp_val = getattr(item, "313", None)
                    
                    if opp_val == self:
                        setattr(item, "313", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "313"):
                    opp_val = getattr(item, "313", None)
                    
                    setattr(item, "313", self)
                    

    @property
    def 309(self):
        return self.__309

    @309.setter
    def 309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Element__309", None)
        self.__309 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "308"):
                opp_val = getattr(old_value, "308", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "308"):
                opp_val = getattr(value, "308", None)
                if opp_val is None:
                    setattr(value, "308", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "contentfwk_Container315"):
                opp_val = getattr(old_value, "contentfwk_Container315", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_Container315"):
                opp_val = getattr(value, "contentfwk_Container315", None)
                if opp_val is None:
                    setattr(value, "contentfwk_Container315", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 308(self):
        return self.__308

    @308.setter
    def 308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Element__308", None)
        self.__308 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "309"):
                    opp_val = getattr(item, "309", None)
                    
                    if opp_val == self:
                        setattr(item, "309", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "309"):
                    opp_val = getattr(item, "309", None)
                    
                    setattr(item, "309", self)
                    

class TechnologyComponent:

    pass
class Service:

    pass
class ApplicationComponent:

    pass
class Standard:

    pass
class contentfwk_ApplicationComponent(Standard):

    pass
class contentfwk_DataComponent(Standard):

    pass
class contentfwk_TechnologyComponent(Standard):

    pass
class contentfwk_Service(Standard):

    pass
class Element:

    pass
class contentfwk_LogicalApplicationComponent(Element, ApplicationComponent):

    pass
class contentfwk_PhysicalApplicationComponent(Element, ApplicationComponent):

    def __init__(self, dateOfNextRelease: date, retirementDate: date, availabilityQualityCharacteristics: str, servicesTimes: str, manageabilityCharacteristics: str, serviceabilityCharacteristics: str, performanceCharacteristics: str, reliabilityCharacteristics: str, recoverabilityCharacteristics: str, locatabilityCharacteristics: str, securityCharacteristics: str, privacyCharacteristics: str, integrityCharacteristics: str, credibilityCharacteristics: str, localizationCharacteristics: str, internationalizationCharacteristics: str, interoperabilityCharacteristics: str, scalabilityCharacteristics: str, portabilityCharacteristics: str, extensibilityCharacteristics: str, capacityCharacteristics: str, throughput: str, throughputPeriod: str, growth: str, growthPeriod: str, peakProfileShortTerm: str, peakProfileLongTerm: str, lifeCycleStatus: str, initialLiveDate: date, dateOfLastRelease: date, 167: "contentfwk_LogicalApplicationComponent" = None, contentfwk_PhysicalApplicationComponent: "contentfwk_PhysicalTechnologyComponent" = None, 327: "contentfwk_Location" = None, contentfwk_PhysicalApplicationComponent357: "contentfwk_PhysicalDataComponent" = None, contentfwk_PhysicalApplicationComponent362: "contentfwk_ApplicationArchitecture" = None, 366: set["contentfwk_LogicalApplicationComponent"] = None, 369: set["contentfwk_Location"] = None, contentfwk_PhysicalApplicationComponent375: set["contentfwk_PhysicalDataComponent"] = None, contentfwk_PhysicalApplicationComponent378: set["contentfwk_PhysicalTechnologyComponent"] = None, contentfwk_PhysicalApplicationComponent373: "contentfwk_PhysicalApplicationComponent" = None, contentfwk_PhysicalApplicationComponent371: set["contentfwk_PhysicalApplicationComponent"] = None, contentfwk_PhysicalApplicationComponent382: "contentfwk_PhysicalApplicationComponent" = None, contentfwk_PhysicalApplicationComponent380: "contentfwk_PhysicalApplicationComponent" = None):
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
        self.lifeCycleStatus = lifeCycleStatus
        self.initialLiveDate = initialLiveDate
        self.dateOfLastRelease = dateOfLastRelease
        self.167 = 167
        self.contentfwk_PhysicalApplicationComponent = contentfwk_PhysicalApplicationComponent
        self.327 = 327
        self.contentfwk_PhysicalApplicationComponent357 = contentfwk_PhysicalApplicationComponent357
        self.contentfwk_PhysicalApplicationComponent362 = contentfwk_PhysicalApplicationComponent362
        self.366 = 366 if 366 is not None else set()
        self.369 = 369 if 369 is not None else set()
        self.contentfwk_PhysicalApplicationComponent375 = contentfwk_PhysicalApplicationComponent375 if contentfwk_PhysicalApplicationComponent375 is not None else set()
        self.contentfwk_PhysicalApplicationComponent378 = contentfwk_PhysicalApplicationComponent378 if contentfwk_PhysicalApplicationComponent378 is not None else set()
        self.contentfwk_PhysicalApplicationComponent373 = contentfwk_PhysicalApplicationComponent373
        self.contentfwk_PhysicalApplicationComponent371 = contentfwk_PhysicalApplicationComponent371 if contentfwk_PhysicalApplicationComponent371 is not None else set()
        self.contentfwk_PhysicalApplicationComponent382 = contentfwk_PhysicalApplicationComponent382
        self.contentfwk_PhysicalApplicationComponent380 = contentfwk_PhysicalApplicationComponent380
        
    @property
    def localizationCharacteristics(self) -> str:
        return self.__localizationCharacteristics

    @localizationCharacteristics.setter
    def localizationCharacteristics(self, localizationCharacteristics: str):
        self.__localizationCharacteristics = localizationCharacteristics

    @property
    def interoperabilityCharacteristics(self) -> str:
        return self.__interoperabilityCharacteristics

    @interoperabilityCharacteristics.setter
    def interoperabilityCharacteristics(self, interoperabilityCharacteristics: str):
        self.__interoperabilityCharacteristics = interoperabilityCharacteristics

    @property
    def scalabilityCharacteristics(self) -> str:
        return self.__scalabilityCharacteristics

    @scalabilityCharacteristics.setter
    def scalabilityCharacteristics(self, scalabilityCharacteristics: str):
        self.__scalabilityCharacteristics = scalabilityCharacteristics

    @property
    def initialLiveDate(self) -> date:
        return self.__initialLiveDate

    @initialLiveDate.setter
    def initialLiveDate(self, initialLiveDate: date):
        self.__initialLiveDate = initialLiveDate

    @property
    def recoverabilityCharacteristics(self) -> str:
        return self.__recoverabilityCharacteristics

    @recoverabilityCharacteristics.setter
    def recoverabilityCharacteristics(self, recoverabilityCharacteristics: str):
        self.__recoverabilityCharacteristics = recoverabilityCharacteristics

    @property
    def throughput(self) -> str:
        return self.__throughput

    @throughput.setter
    def throughput(self, throughput: str):
        self.__throughput = throughput

    @property
    def dateOfNextRelease(self) -> date:
        return self.__dateOfNextRelease

    @dateOfNextRelease.setter
    def dateOfNextRelease(self, dateOfNextRelease: date):
        self.__dateOfNextRelease = dateOfNextRelease

    @property
    def servicesTimes(self) -> str:
        return self.__servicesTimes

    @servicesTimes.setter
    def servicesTimes(self, servicesTimes: str):
        self.__servicesTimes = servicesTimes

    @property
    def reliabilityCharacteristics(self) -> str:
        return self.__reliabilityCharacteristics

    @reliabilityCharacteristics.setter
    def reliabilityCharacteristics(self, reliabilityCharacteristics: str):
        self.__reliabilityCharacteristics = reliabilityCharacteristics

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
    def lifeCycleStatus(self) -> str:
        return self.__lifeCycleStatus

    @lifeCycleStatus.setter
    def lifeCycleStatus(self, lifeCycleStatus: str):
        self.__lifeCycleStatus = lifeCycleStatus

    @property
    def growthPeriod(self) -> str:
        return self.__growthPeriod

    @growthPeriod.setter
    def growthPeriod(self, growthPeriod: str):
        self.__growthPeriod = growthPeriod

    @property
    def performanceCharacteristics(self) -> str:
        return self.__performanceCharacteristics

    @performanceCharacteristics.setter
    def performanceCharacteristics(self, performanceCharacteristics: str):
        self.__performanceCharacteristics = performanceCharacteristics

    @property
    def growth(self) -> str:
        return self.__growth

    @growth.setter
    def growth(self, growth: str):
        self.__growth = growth

    @property
    def internationalizationCharacteristics(self) -> str:
        return self.__internationalizationCharacteristics

    @internationalizationCharacteristics.setter
    def internationalizationCharacteristics(self, internationalizationCharacteristics: str):
        self.__internationalizationCharacteristics = internationalizationCharacteristics

    @property
    def peakProfileLongTerm(self) -> str:
        return self.__peakProfileLongTerm

    @peakProfileLongTerm.setter
    def peakProfileLongTerm(self, peakProfileLongTerm: str):
        self.__peakProfileLongTerm = peakProfileLongTerm

    @property
    def dateOfLastRelease(self) -> date:
        return self.__dateOfLastRelease

    @dateOfLastRelease.setter
    def dateOfLastRelease(self, dateOfLastRelease: date):
        self.__dateOfLastRelease = dateOfLastRelease

    @property
    def capacityCharacteristics(self) -> str:
        return self.__capacityCharacteristics

    @capacityCharacteristics.setter
    def capacityCharacteristics(self, capacityCharacteristics: str):
        self.__capacityCharacteristics = capacityCharacteristics

    @property
    def throughputPeriod(self) -> str:
        return self.__throughputPeriod

    @throughputPeriod.setter
    def throughputPeriod(self, throughputPeriod: str):
        self.__throughputPeriod = throughputPeriod

    @property
    def serviceabilityCharacteristics(self) -> str:
        return self.__serviceabilityCharacteristics

    @serviceabilityCharacteristics.setter
    def serviceabilityCharacteristics(self, serviceabilityCharacteristics: str):
        self.__serviceabilityCharacteristics = serviceabilityCharacteristics

    @property
    def securityCharacteristics(self) -> str:
        return self.__securityCharacteristics

    @securityCharacteristics.setter
    def securityCharacteristics(self, securityCharacteristics: str):
        self.__securityCharacteristics = securityCharacteristics

    @property
    def locatabilityCharacteristics(self) -> str:
        return self.__locatabilityCharacteristics

    @locatabilityCharacteristics.setter
    def locatabilityCharacteristics(self, locatabilityCharacteristics: str):
        self.__locatabilityCharacteristics = locatabilityCharacteristics

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
    def credibilityCharacteristics(self) -> str:
        return self.__credibilityCharacteristics

    @credibilityCharacteristics.setter
    def credibilityCharacteristics(self, credibilityCharacteristics: str):
        self.__credibilityCharacteristics = credibilityCharacteristics

    @property
    def retirementDate(self) -> date:
        return self.__retirementDate

    @retirementDate.setter
    def retirementDate(self, retirementDate: date):
        self.__retirementDate = retirementDate

    @property
    def privacyCharacteristics(self) -> str:
        return self.__privacyCharacteristics

    @privacyCharacteristics.setter
    def privacyCharacteristics(self, privacyCharacteristics: str):
        self.__privacyCharacteristics = privacyCharacteristics

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
    def contentfwk_PhysicalApplicationComponent380(self):
        return self.__contentfwk_PhysicalApplicationComponent380

    @contentfwk_PhysicalApplicationComponent380.setter
    def contentfwk_PhysicalApplicationComponent380(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent380", None)
        self.__contentfwk_PhysicalApplicationComponent380 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalApplicationComponent382"):
                opp_val = getattr(old_value, "contentfwk_PhysicalApplicationComponent382", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_PhysicalApplicationComponent382", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalApplicationComponent382"):
                opp_val = getattr(value, "contentfwk_PhysicalApplicationComponent382", None)
                setattr(value, "contentfwk_PhysicalApplicationComponent382", self)

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
            if hasattr(old_value, "contentfwk_PhysicalTechnologyComponent248"):
                opp_val = getattr(old_value, "contentfwk_PhysicalTechnologyComponent248", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalTechnologyComponent248"):
                opp_val = getattr(value, "contentfwk_PhysicalTechnologyComponent248", None)
                if opp_val is None:
                    setattr(value, "contentfwk_PhysicalTechnologyComponent248", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 369(self):
        return self.__369

    @369.setter
    def 369(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__369", None)
        self.__369 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "370"):
                    opp_val = getattr(item, "370", None)
                    
                    if opp_val == self:
                        setattr(item, "370", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "370"):
                    opp_val = getattr(item, "370", None)
                    
                    setattr(item, "370", self)
                    

    @property
    def 327(self):
        return self.__327

    @327.setter
    def 327(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__327", None)
        self.__327 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "326"):
                opp_val = getattr(old_value, "326", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "326"):
                opp_val = getattr(value, "326", None)
                if opp_val is None:
                    setattr(value, "326", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_PhysicalApplicationComponent375(self):
        return self.__contentfwk_PhysicalApplicationComponent375

    @contentfwk_PhysicalApplicationComponent375.setter
    def contentfwk_PhysicalApplicationComponent375(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent375", None)
        self.__contentfwk_PhysicalApplicationComponent375 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_PhysicalDataComponent376"):
                    opp_val = getattr(item, "contentfwk_PhysicalDataComponent376", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_PhysicalDataComponent376", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_PhysicalDataComponent376"):
                    opp_val = getattr(item, "contentfwk_PhysicalDataComponent376", None)
                    
                    setattr(item, "contentfwk_PhysicalDataComponent376", self)
                    

    @property
    def contentfwk_PhysicalApplicationComponent362(self):
        return self.__contentfwk_PhysicalApplicationComponent362

    @contentfwk_PhysicalApplicationComponent362.setter
    def contentfwk_PhysicalApplicationComponent362(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent362", None)
        self.__contentfwk_PhysicalApplicationComponent362 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_ApplicationArchitecture361"):
                opp_val = getattr(old_value, "contentfwk_ApplicationArchitecture361", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_ApplicationArchitecture361"):
                opp_val = getattr(value, "contentfwk_ApplicationArchitecture361", None)
                if opp_val is None:
                    setattr(value, "contentfwk_ApplicationArchitecture361", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_PhysicalApplicationComponent371(self):
        return self.__contentfwk_PhysicalApplicationComponent371

    @contentfwk_PhysicalApplicationComponent371.setter
    def contentfwk_PhysicalApplicationComponent371(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent371", None)
        self.__contentfwk_PhysicalApplicationComponent371 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_PhysicalApplicationComponent373"):
                    opp_val = getattr(item, "contentfwk_PhysicalApplicationComponent373", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_PhysicalApplicationComponent373", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_PhysicalApplicationComponent373"):
                    opp_val = getattr(item, "contentfwk_PhysicalApplicationComponent373", None)
                    
                    setattr(item, "contentfwk_PhysicalApplicationComponent373", self)
                    

    @property
    def 167(self):
        return self.__167

    @167.setter
    def 167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__167", None)
        self.__167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "166"):
                opp_val = getattr(old_value, "166", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "166"):
                opp_val = getattr(value, "166", None)
                if opp_val is None:
                    setattr(value, "166", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 366(self):
        return self.__366

    @366.setter
    def 366(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__366", None)
        self.__366 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "367"):
                    opp_val = getattr(item, "367", None)
                    
                    if opp_val == self:
                        setattr(item, "367", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "367"):
                    opp_val = getattr(item, "367", None)
                    
                    setattr(item, "367", self)
                    

    @property
    def contentfwk_PhysicalApplicationComponent378(self):
        return self.__contentfwk_PhysicalApplicationComponent378

    @contentfwk_PhysicalApplicationComponent378.setter
    def contentfwk_PhysicalApplicationComponent378(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent378", None)
        self.__contentfwk_PhysicalApplicationComponent378 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_PhysicalTechnologyComponent379"):
                    opp_val = getattr(item, "contentfwk_PhysicalTechnologyComponent379", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_PhysicalTechnologyComponent379", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_PhysicalTechnologyComponent379"):
                    opp_val = getattr(item, "contentfwk_PhysicalTechnologyComponent379", None)
                    
                    setattr(item, "contentfwk_PhysicalTechnologyComponent379", self)
                    

    @property
    def contentfwk_PhysicalApplicationComponent373(self):
        return self.__contentfwk_PhysicalApplicationComponent373

    @contentfwk_PhysicalApplicationComponent373.setter
    def contentfwk_PhysicalApplicationComponent373(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent373", None)
        self.__contentfwk_PhysicalApplicationComponent373 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalApplicationComponent371"):
                opp_val = getattr(old_value, "contentfwk_PhysicalApplicationComponent371", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalApplicationComponent371"):
                opp_val = getattr(value, "contentfwk_PhysicalApplicationComponent371", None)
                if opp_val is None:
                    setattr(value, "contentfwk_PhysicalApplicationComponent371", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_PhysicalApplicationComponent382(self):
        return self.__contentfwk_PhysicalApplicationComponent382

    @contentfwk_PhysicalApplicationComponent382.setter
    def contentfwk_PhysicalApplicationComponent382(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent382", None)
        self.__contentfwk_PhysicalApplicationComponent382 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalApplicationComponent380"):
                opp_val = getattr(old_value, "contentfwk_PhysicalApplicationComponent380", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_PhysicalApplicationComponent380", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalApplicationComponent380"):
                opp_val = getattr(value, "contentfwk_PhysicalApplicationComponent380", None)
                setattr(value, "contentfwk_PhysicalApplicationComponent380", self)

    @property
    def contentfwk_PhysicalApplicationComponent357(self):
        return self.__contentfwk_PhysicalApplicationComponent357

    @contentfwk_PhysicalApplicationComponent357.setter
    def contentfwk_PhysicalApplicationComponent357(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent357", None)
        self.__contentfwk_PhysicalApplicationComponent357 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalDataComponent356"):
                opp_val = getattr(old_value, "contentfwk_PhysicalDataComponent356", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalDataComponent356"):
                opp_val = getattr(value, "contentfwk_PhysicalDataComponent356", None)
                if opp_val is None:
                    setattr(value, "contentfwk_PhysicalDataComponent356", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class contentfwk_Capability(Element):

    def __init__(self, businessValue: str, increments: str, 335: "contentfwk_WorkPackage" = None, 339: "contentfwk_WorkPackage" = None, contentfwk_Capability: "contentfwk_StrategicArchitecture" = None):
        self.businessValue = businessValue
        self.increments = increments
        self.335 = 335
        self.339 = 339
        self.contentfwk_Capability = contentfwk_Capability
        
    @property
    def businessValue(self) -> str:
        return self.__businessValue

    @businessValue.setter
    def businessValue(self, businessValue: str):
        self.__businessValue = businessValue

    @property
    def increments(self) -> str:
        return self.__increments

    @increments.setter
    def increments(self, increments: str):
        self.__increments = increments

    @property
    def 339(self):
        return self.__339

    @339.setter
    def 339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Capability__339", None)
        self.__339 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "338"):
                opp_val = getattr(old_value, "338", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "338"):
                opp_val = getattr(value, "338", None)
                if opp_val is None:
                    setattr(value, "338", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def 335(self):
        return self.__335

    @335.setter
    def 335(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Capability__335", None)
        self.__335 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "336"):
                opp_val = getattr(old_value, "336", None)
                if opp_val == self:
                    setattr(old_value, "336", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "336"):
                opp_val = getattr(value, "336", None)
                setattr(value, "336", self)

class contentfwk_InformationSystemService(Element, Service):

    pass
class contentfwk_DataEntity(Element):

    def __init__(self, dataEntityCategory: str, privacyClassification: str, retentionClassification: str, contentfwk_DataEntity: "contentfwk_DataArchitecture" = None, 93: "contentfwk_Actor" = None, 96: "contentfwk_Actor" = None, 136: set["contentfwk_Actor"] = None, 139: set["contentfwk_Actor"] = None, 142: set["contentfwk_Service"] = None, 145: set["contentfwk_Service"] = None, 148: "contentfwk_LogicalDataComponent" = None, 151: set["contentfwk_LogicalApplicationComponent"] = None, 164: "contentfwk_LogicalApplicationComponent" = None, contentfwk_DataEntity155: "contentfwk_DataEntity" = None, contentfwk_DataEntity153: "contentfwk_DataEntity" = None, contentfwk_DataEntity158: "contentfwk_DataEntity" = None, contentfwk_DataEntity156: set["contentfwk_DataEntity"] = None, 342: "contentfwk_LogicalDataComponent" = None, 409: "contentfwk_Service" = None, 412: "contentfwk_Service" = None):
        self.dataEntityCategory = dataEntityCategory
        self.privacyClassification = privacyClassification
        self.retentionClassification = retentionClassification
        self.contentfwk_DataEntity = contentfwk_DataEntity
        self.93 = 93
        self.96 = 96
        self.136 = 136 if 136 is not None else set()
        self.139 = 139 if 139 is not None else set()
        self.142 = 142 if 142 is not None else set()
        self.145 = 145 if 145 is not None else set()
        self.148 = 148
        self.151 = 151 if 151 is not None else set()
        self.164 = 164
        self.contentfwk_DataEntity155 = contentfwk_DataEntity155
        self.contentfwk_DataEntity153 = contentfwk_DataEntity153
        self.contentfwk_DataEntity158 = contentfwk_DataEntity158
        self.contentfwk_DataEntity156 = contentfwk_DataEntity156 if contentfwk_DataEntity156 is not None else set()
        self.342 = 342
        self.409 = 409
        self.412 = 412
        
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
    def privacyClassification(self) -> str:
        return self.__privacyClassification

    @privacyClassification.setter
    def privacyClassification(self, privacyClassification: str):
        self.__privacyClassification = privacyClassification

    @property
    def 148(self):
        return self.__148

    @148.setter
    def 148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__148", None)
        self.__148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "149"):
                opp_val = getattr(old_value, "149", None)
                if opp_val == self:
                    setattr(old_value, "149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "149"):
                opp_val = getattr(value, "149", None)
                setattr(value, "149", self)

    @property
    def contentfwk_DataEntity156(self):
        return self.__contentfwk_DataEntity156

    @contentfwk_DataEntity156.setter
    def contentfwk_DataEntity156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__contentfwk_DataEntity156", None)
        self.__contentfwk_DataEntity156 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_DataEntity158"):
                    opp_val = getattr(item, "contentfwk_DataEntity158", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_DataEntity158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_DataEntity158"):
                    opp_val = getattr(item, "contentfwk_DataEntity158", None)
                    
                    setattr(item, "contentfwk_DataEntity158", self)
                    

    @property
    def 342(self):
        return self.__342

    @342.setter
    def 342(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__342", None)
        self.__342 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "341"):
                opp_val = getattr(old_value, "341", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "341"):
                opp_val = getattr(value, "341", None)
                if opp_val is None:
                    setattr(value, "341", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 93(self):
        return self.__93

    @93.setter
    def 93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__93", None)
        self.__93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "92"):
                opp_val = getattr(old_value, "92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "92"):
                opp_val = getattr(value, "92", None)
                if opp_val is None:
                    setattr(value, "92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_DataEntity153(self):
        return self.__contentfwk_DataEntity153

    @contentfwk_DataEntity153.setter
    def contentfwk_DataEntity153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__contentfwk_DataEntity153", None)
        self.__contentfwk_DataEntity153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_DataEntity155"):
                opp_val = getattr(old_value, "contentfwk_DataEntity155", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_DataEntity155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_DataEntity155"):
                opp_val = getattr(value, "contentfwk_DataEntity155", None)
                setattr(value, "contentfwk_DataEntity155", self)

    @property
    def 142(self):
        return self.__142

    @142.setter
    def 142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__142", None)
        self.__142 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "143"):
                    opp_val = getattr(item, "143", None)
                    
                    if opp_val == self:
                        setattr(item, "143", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "143"):
                    opp_val = getattr(item, "143", None)
                    
                    setattr(item, "143", self)
                    

    @property
    def contentfwk_DataEntity158(self):
        return self.__contentfwk_DataEntity158

    @contentfwk_DataEntity158.setter
    def contentfwk_DataEntity158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__contentfwk_DataEntity158", None)
        self.__contentfwk_DataEntity158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_DataEntity156"):
                opp_val = getattr(old_value, "contentfwk_DataEntity156", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_DataEntity156"):
                opp_val = getattr(value, "contentfwk_DataEntity156", None)
                if opp_val is None:
                    setattr(value, "contentfwk_DataEntity156", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 139(self):
        return self.__139

    @139.setter
    def 139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__139", None)
        self.__139 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "140"):
                    opp_val = getattr(item, "140", None)
                    
                    if opp_val == self:
                        setattr(item, "140", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "140"):
                    opp_val = getattr(item, "140", None)
                    
                    setattr(item, "140", self)
                    

    @property
    def 409(self):
        return self.__409

    @409.setter
    def 409(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__409", None)
        self.__409 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "408"):
                opp_val = getattr(old_value, "408", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "408"):
                opp_val = getattr(value, "408", None)
                if opp_val is None:
                    setattr(value, "408", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 164(self):
        return self.__164

    @164.setter
    def 164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__164", None)
        self.__164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "163"):
                opp_val = getattr(old_value, "163", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "163"):
                opp_val = getattr(value, "163", None)
                if opp_val is None:
                    setattr(value, "163", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_DataEntity155(self):
        return self.__contentfwk_DataEntity155

    @contentfwk_DataEntity155.setter
    def contentfwk_DataEntity155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__contentfwk_DataEntity155", None)
        self.__contentfwk_DataEntity155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_DataEntity153"):
                opp_val = getattr(old_value, "contentfwk_DataEntity153", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_DataEntity153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_DataEntity153"):
                opp_val = getattr(value, "contentfwk_DataEntity153", None)
                setattr(value, "contentfwk_DataEntity153", self)

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
    def 412(self):
        return self.__412

    @412.setter
    def 412(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__412", None)
        self.__412 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "411"):
                opp_val = getattr(old_value, "411", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "411"):
                opp_val = getattr(value, "411", None)
                if opp_val is None:
                    setattr(value, "411", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 96(self):
        return self.__96

    @96.setter
    def 96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__96", None)
        self.__96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "95"):
                opp_val = getattr(old_value, "95", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "95"):
                opp_val = getattr(value, "95", None)
                if opp_val is None:
                    setattr(value, "95", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 145(self):
        return self.__145

    @145.setter
    def 145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__145", None)
        self.__145 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "146"):
                    opp_val = getattr(item, "146", None)
                    
                    if opp_val == self:
                        setattr(item, "146", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "146"):
                    opp_val = getattr(item, "146", None)
                    
                    setattr(item, "146", self)
                    

    @property
    def 136(self):
        return self.__136

    @136.setter
    def 136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__136", None)
        self.__136 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "137"):
                    opp_val = getattr(item, "137", None)
                    
                    if opp_val == self:
                        setattr(item, "137", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "137"):
                    opp_val = getattr(item, "137", None)
                    
                    setattr(item, "137", self)
                    

    @property
    def 151(self):
        return self.__151

    @151.setter
    def 151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__151", None)
        self.__151 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "152"):
                    opp_val = getattr(item, "152", None)
                    
                    if opp_val == self:
                        setattr(item, "152", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "152"):
                    opp_val = getattr(item, "152", None)
                    
                    setattr(item, "152", self)
                    

class contentfwk_PhysicalDataComponent(Element, DataComponent):

    pass
class contentfwk_LogicalDataComponent(Element, DataComponent):

    pass
class contentfwk_StrategicElement(Element):

    pass
class contentfwk_LogicalTechnologyComponent(TechnologyComponent, Element):

    pass
class contentfwk_PhysicalTechnologyComponent(TechnologyComponent, Element):

    def __init__(self, productName: str, moduleName: str, vendor: str, version: str, contentfwk_PhysicalTechnologyComponent: "contentfwk_TechnologyArchitecture" = None, contentfwk_PhysicalTechnologyComponent248: set["contentfwk_PhysicalApplicationComponent"] = None, 250: set["contentfwk_LogicalTechnologyComponent"] = None, 253: set["contentfwk_Location"] = None, contentfwk_PhysicalTechnologyComponent257: "contentfwk_PhysicalTechnologyComponent" = None, contentfwk_PhysicalTechnologyComponent255: "contentfwk_PhysicalTechnologyComponent" = None, contentfwk_PhysicalTechnologyComponent260: "contentfwk_PhysicalTechnologyComponent" = None, contentfwk_PhysicalTechnologyComponent258: set["contentfwk_PhysicalTechnologyComponent"] = None, 330: "contentfwk_Location" = None, contentfwk_PhysicalTechnologyComponent379: "contentfwk_PhysicalApplicationComponent" = None, 391: "contentfwk_LogicalTechnologyComponent" = None):
        self.productName = productName
        self.moduleName = moduleName
        self.vendor = vendor
        self.version = version
        self.contentfwk_PhysicalTechnologyComponent = contentfwk_PhysicalTechnologyComponent
        self.contentfwk_PhysicalTechnologyComponent248 = contentfwk_PhysicalTechnologyComponent248 if contentfwk_PhysicalTechnologyComponent248 is not None else set()
        self.250 = 250 if 250 is not None else set()
        self.253 = 253 if 253 is not None else set()
        self.contentfwk_PhysicalTechnologyComponent257 = contentfwk_PhysicalTechnologyComponent257
        self.contentfwk_PhysicalTechnologyComponent255 = contentfwk_PhysicalTechnologyComponent255
        self.contentfwk_PhysicalTechnologyComponent260 = contentfwk_PhysicalTechnologyComponent260
        self.contentfwk_PhysicalTechnologyComponent258 = contentfwk_PhysicalTechnologyComponent258 if contentfwk_PhysicalTechnologyComponent258 is not None else set()
        self.330 = 330
        self.contentfwk_PhysicalTechnologyComponent379 = contentfwk_PhysicalTechnologyComponent379
        self.391 = 391
        
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
    def contentfwk_PhysicalTechnologyComponent255(self):
        return self.__contentfwk_PhysicalTechnologyComponent255

    @contentfwk_PhysicalTechnologyComponent255.setter
    def contentfwk_PhysicalTechnologyComponent255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent255", None)
        self.__contentfwk_PhysicalTechnologyComponent255 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalTechnologyComponent257"):
                opp_val = getattr(old_value, "contentfwk_PhysicalTechnologyComponent257", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_PhysicalTechnologyComponent257", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalTechnologyComponent257"):
                opp_val = getattr(value, "contentfwk_PhysicalTechnologyComponent257", None)
                setattr(value, "contentfwk_PhysicalTechnologyComponent257", self)

    @property
    def contentfwk_PhysicalTechnologyComponent260(self):
        return self.__contentfwk_PhysicalTechnologyComponent260

    @contentfwk_PhysicalTechnologyComponent260.setter
    def contentfwk_PhysicalTechnologyComponent260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent260", None)
        self.__contentfwk_PhysicalTechnologyComponent260 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalTechnologyComponent258"):
                opp_val = getattr(old_value, "contentfwk_PhysicalTechnologyComponent258", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalTechnologyComponent258"):
                opp_val = getattr(value, "contentfwk_PhysicalTechnologyComponent258", None)
                if opp_val is None:
                    setattr(value, "contentfwk_PhysicalTechnologyComponent258", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_PhysicalTechnologyComponent248(self):
        return self.__contentfwk_PhysicalTechnologyComponent248

    @contentfwk_PhysicalTechnologyComponent248.setter
    def contentfwk_PhysicalTechnologyComponent248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent248", None)
        self.__contentfwk_PhysicalTechnologyComponent248 = value if value is not None else set()
        
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
    def 391(self):
        return self.__391

    @391.setter
    def 391(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__391", None)
        self.__391 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "390"):
                opp_val = getattr(old_value, "390", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "390"):
                opp_val = getattr(value, "390", None)
                if opp_val is None:
                    setattr(value, "390", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_PhysicalTechnologyComponent258(self):
        return self.__contentfwk_PhysicalTechnologyComponent258

    @contentfwk_PhysicalTechnologyComponent258.setter
    def contentfwk_PhysicalTechnologyComponent258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent258", None)
        self.__contentfwk_PhysicalTechnologyComponent258 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_PhysicalTechnologyComponent260"):
                    opp_val = getattr(item, "contentfwk_PhysicalTechnologyComponent260", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_PhysicalTechnologyComponent260", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_PhysicalTechnologyComponent260"):
                    opp_val = getattr(item, "contentfwk_PhysicalTechnologyComponent260", None)
                    
                    setattr(item, "contentfwk_PhysicalTechnologyComponent260", self)
                    

    @property
    def contentfwk_PhysicalTechnologyComponent257(self):
        return self.__contentfwk_PhysicalTechnologyComponent257

    @contentfwk_PhysicalTechnologyComponent257.setter
    def contentfwk_PhysicalTechnologyComponent257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent257", None)
        self.__contentfwk_PhysicalTechnologyComponent257 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalTechnologyComponent255"):
                opp_val = getattr(old_value, "contentfwk_PhysicalTechnologyComponent255", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_PhysicalTechnologyComponent255", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalTechnologyComponent255"):
                opp_val = getattr(value, "contentfwk_PhysicalTechnologyComponent255", None)
                setattr(value, "contentfwk_PhysicalTechnologyComponent255", self)

    @property
    def 253(self):
        return self.__253

    @253.setter
    def 253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__253", None)
        self.__253 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "254"):
                    opp_val = getattr(item, "254", None)
                    
                    if opp_val == self:
                        setattr(item, "254", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "254"):
                    opp_val = getattr(item, "254", None)
                    
                    setattr(item, "254", self)
                    

    @property
    def 330(self):
        return self.__330

    @330.setter
    def 330(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__330", None)
        self.__330 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "329"):
                opp_val = getattr(old_value, "329", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "329"):
                opp_val = getattr(value, "329", None)
                if opp_val is None:
                    setattr(value, "329", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_PhysicalTechnologyComponent379(self):
        return self.__contentfwk_PhysicalTechnologyComponent379

    @contentfwk_PhysicalTechnologyComponent379.setter
    def contentfwk_PhysicalTechnologyComponent379(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent379", None)
        self.__contentfwk_PhysicalTechnologyComponent379 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalApplicationComponent378"):
                opp_val = getattr(old_value, "contentfwk_PhysicalApplicationComponent378", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalApplicationComponent378"):
                opp_val = getattr(value, "contentfwk_PhysicalApplicationComponent378", None)
                if opp_val is None:
                    setattr(value, "contentfwk_PhysicalApplicationComponent378", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 250(self):
        return self.__250

    @250.setter
    def 250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__250", None)
        self.__250 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "251"):
                    opp_val = getattr(item, "251", None)
                    
                    if opp_val == self:
                        setattr(item, "251", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "251"):
                    opp_val = getattr(item, "251", None)
                    
                    setattr(item, "251", self)
                    

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

class contentfwk_PlatformService(Element, Service):

    pass
class contentfwk_Container:

    def __init__(self, name: str, contentfwk_Container: "contentfwk_EnterpriseArchitecture" = None, contentfwk_Container315: set["contentfwk_Element"] = None):
        self.name = name
        self.contentfwk_Container = contentfwk_Container
        self.contentfwk_Container315 = contentfwk_Container315 if contentfwk_Container315 is not None else set()
        
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
    def contentfwk_Container315(self):
        return self.__contentfwk_Container315

    @contentfwk_Container315.setter
    def contentfwk_Container315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Container__contentfwk_Container315", None)
        self.__contentfwk_Container315 = value if value is not None else set()
        
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
                    

class contentfwk_ServiceQuality(Element):

    pass
class contentfwk_Measure(Element):

    pass
class contentfwk_Contract(Element):

    def __init__(self, ServiceNameCalled: str, serviceQualityCharacteristics: str, availabilityQualityCharacteristics: str, servicesTimes: str, manageabilityCharacteristics: str, serviceabilityCharacteristics: str, performanceCharacteristics: str, responseCharacteristics: str, reliabilityCharacteristics: str, qualityOfInformationRequired: str, contractControlRequirements: str, resultControlRequirements: str, recoverabilityCharacteristics: str, locatabilityCharacteristics: str, securityCharacteristics: str, privacyCharacteristics: str, integrityCharacteristics: str, credibilityCharacteristics: str, localizationCharacteristics: str, internationalizationCharacteristics: str, interoperabilityCharacteristics: str, scalabilityCharacteristics: str, portabilityCharacteristics: str, behaviorCharacteristics: str, ServiceNameCaller: str, growthPeriod: str, peakProfileShortTerm: str, peakProfileLongTerm: str, extensibilityCharacteristics: str, capacityCharacteristics: str, throughput: str, throughputPeriod: str, growth: str, contentfwk_Contract: "contentfwk_BusinessArchitecture" = None, 281: "contentfwk_ServiceQuality" = None, 283: set["contentfwk_Service"] = None, 286: set["contentfwk_ServiceQuality"] = None, 415: "contentfwk_Service" = None):
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
        self.securityCharacteristics = securityCharacteristics
        self.privacyCharacteristics = privacyCharacteristics
        self.integrityCharacteristics = integrityCharacteristics
        self.credibilityCharacteristics = credibilityCharacteristics
        self.localizationCharacteristics = localizationCharacteristics
        self.internationalizationCharacteristics = internationalizationCharacteristics
        self.interoperabilityCharacteristics = interoperabilityCharacteristics
        self.scalabilityCharacteristics = scalabilityCharacteristics
        self.portabilityCharacteristics = portabilityCharacteristics
        self.behaviorCharacteristics = behaviorCharacteristics
        self.ServiceNameCaller = ServiceNameCaller
        self.growthPeriod = growthPeriod
        self.peakProfileShortTerm = peakProfileShortTerm
        self.peakProfileLongTerm = peakProfileLongTerm
        self.extensibilityCharacteristics = extensibilityCharacteristics
        self.capacityCharacteristics = capacityCharacteristics
        self.throughput = throughput
        self.throughputPeriod = throughputPeriod
        self.growth = growth
        self.contentfwk_Contract = contentfwk_Contract
        self.281 = 281
        self.283 = 283 if 283 is not None else set()
        self.286 = 286 if 286 is not None else set()
        self.415 = 415
        
    @property
    def reliabilityCharacteristics(self) -> str:
        return self.__reliabilityCharacteristics

    @reliabilityCharacteristics.setter
    def reliabilityCharacteristics(self, reliabilityCharacteristics: str):
        self.__reliabilityCharacteristics = reliabilityCharacteristics

    @property
    def locatabilityCharacteristics(self) -> str:
        return self.__locatabilityCharacteristics

    @locatabilityCharacteristics.setter
    def locatabilityCharacteristics(self, locatabilityCharacteristics: str):
        self.__locatabilityCharacteristics = locatabilityCharacteristics

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
    def growthPeriod(self) -> str:
        return self.__growthPeriod

    @growthPeriod.setter
    def growthPeriod(self, growthPeriod: str):
        self.__growthPeriod = growthPeriod

    @property
    def peakProfileShortTerm(self) -> str:
        return self.__peakProfileShortTerm

    @peakProfileShortTerm.setter
    def peakProfileShortTerm(self, peakProfileShortTerm: str):
        self.__peakProfileShortTerm = peakProfileShortTerm

    @property
    def servicesTimes(self) -> str:
        return self.__servicesTimes

    @servicesTimes.setter
    def servicesTimes(self, servicesTimes: str):
        self.__servicesTimes = servicesTimes

    @property
    def contractControlRequirements(self) -> str:
        return self.__contractControlRequirements

    @contractControlRequirements.setter
    def contractControlRequirements(self, contractControlRequirements: str):
        self.__contractControlRequirements = contractControlRequirements

    @property
    def internationalizationCharacteristics(self) -> str:
        return self.__internationalizationCharacteristics

    @internationalizationCharacteristics.setter
    def internationalizationCharacteristics(self, internationalizationCharacteristics: str):
        self.__internationalizationCharacteristics = internationalizationCharacteristics

    @property
    def qualityOfInformationRequired(self) -> str:
        return self.__qualityOfInformationRequired

    @qualityOfInformationRequired.setter
    def qualityOfInformationRequired(self, qualityOfInformationRequired: str):
        self.__qualityOfInformationRequired = qualityOfInformationRequired

    @property
    def portabilityCharacteristics(self) -> str:
        return self.__portabilityCharacteristics

    @portabilityCharacteristics.setter
    def portabilityCharacteristics(self, portabilityCharacteristics: str):
        self.__portabilityCharacteristics = portabilityCharacteristics

    @property
    def resultControlRequirements(self) -> str:
        return self.__resultControlRequirements

    @resultControlRequirements.setter
    def resultControlRequirements(self, resultControlRequirements: str):
        self.__resultControlRequirements = resultControlRequirements

    @property
    def ServiceNameCalled(self) -> str:
        return self.__ServiceNameCalled

    @ServiceNameCalled.setter
    def ServiceNameCalled(self, ServiceNameCalled: str):
        self.__ServiceNameCalled = ServiceNameCalled

    @property
    def serviceabilityCharacteristics(self) -> str:
        return self.__serviceabilityCharacteristics

    @serviceabilityCharacteristics.setter
    def serviceabilityCharacteristics(self, serviceabilityCharacteristics: str):
        self.__serviceabilityCharacteristics = serviceabilityCharacteristics

    @property
    def ServiceNameCaller(self) -> str:
        return self.__ServiceNameCaller

    @ServiceNameCaller.setter
    def ServiceNameCaller(self, ServiceNameCaller: str):
        self.__ServiceNameCaller = ServiceNameCaller

    @property
    def performanceCharacteristics(self) -> str:
        return self.__performanceCharacteristics

    @performanceCharacteristics.setter
    def performanceCharacteristics(self, performanceCharacteristics: str):
        self.__performanceCharacteristics = performanceCharacteristics

    @property
    def extensibilityCharacteristics(self) -> str:
        return self.__extensibilityCharacteristics

    @extensibilityCharacteristics.setter
    def extensibilityCharacteristics(self, extensibilityCharacteristics: str):
        self.__extensibilityCharacteristics = extensibilityCharacteristics

    @property
    def localizationCharacteristics(self) -> str:
        return self.__localizationCharacteristics

    @localizationCharacteristics.setter
    def localizationCharacteristics(self, localizationCharacteristics: str):
        self.__localizationCharacteristics = localizationCharacteristics

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
    def behaviorCharacteristics(self) -> str:
        return self.__behaviorCharacteristics

    @behaviorCharacteristics.setter
    def behaviorCharacteristics(self, behaviorCharacteristics: str):
        self.__behaviorCharacteristics = behaviorCharacteristics

    @property
    def recoverabilityCharacteristics(self) -> str:
        return self.__recoverabilityCharacteristics

    @recoverabilityCharacteristics.setter
    def recoverabilityCharacteristics(self, recoverabilityCharacteristics: str):
        self.__recoverabilityCharacteristics = recoverabilityCharacteristics

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
    def privacyCharacteristics(self) -> str:
        return self.__privacyCharacteristics

    @privacyCharacteristics.setter
    def privacyCharacteristics(self, privacyCharacteristics: str):
        self.__privacyCharacteristics = privacyCharacteristics

    @property
    def serviceQualityCharacteristics(self) -> str:
        return self.__serviceQualityCharacteristics

    @serviceQualityCharacteristics.setter
    def serviceQualityCharacteristics(self, serviceQualityCharacteristics: str):
        self.__serviceQualityCharacteristics = serviceQualityCharacteristics

    @property
    def availabilityQualityCharacteristics(self) -> str:
        return self.__availabilityQualityCharacteristics

    @availabilityQualityCharacteristics.setter
    def availabilityQualityCharacteristics(self, availabilityQualityCharacteristics: str):
        self.__availabilityQualityCharacteristics = availabilityQualityCharacteristics

    @property
    def capacityCharacteristics(self) -> str:
        return self.__capacityCharacteristics

    @capacityCharacteristics.setter
    def capacityCharacteristics(self, capacityCharacteristics: str):
        self.__capacityCharacteristics = capacityCharacteristics

    @property
    def throughputPeriod(self) -> str:
        return self.__throughputPeriod

    @throughputPeriod.setter
    def throughputPeriod(self, throughputPeriod: str):
        self.__throughputPeriod = throughputPeriod

    @property
    def responseCharacteristics(self) -> str:
        return self.__responseCharacteristics

    @responseCharacteristics.setter
    def responseCharacteristics(self, responseCharacteristics: str):
        self.__responseCharacteristics = responseCharacteristics

    @property
    def securityCharacteristics(self) -> str:
        return self.__securityCharacteristics

    @securityCharacteristics.setter
    def securityCharacteristics(self, securityCharacteristics: str):
        self.__securityCharacteristics = securityCharacteristics

    @property
    def 281(self):
        return self.__281

    @281.setter
    def 281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Contract__281", None)
        self.__281 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "280"):
                opp_val = getattr(old_value, "280", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "280"):
                opp_val = getattr(value, "280", None)
                if opp_val is None:
                    setattr(value, "280", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 286(self):
        return self.__286

    @286.setter
    def 286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Contract__286", None)
        self.__286 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "287"):
                    opp_val = getattr(item, "287", None)
                    
                    if opp_val == self:
                        setattr(item, "287", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "287"):
                    opp_val = getattr(item, "287", None)
                    
                    setattr(item, "287", self)
                    

    @property
    def 283(self):
        return self.__283

    @283.setter
    def 283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Contract__283", None)
        self.__283 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "284"):
                    opp_val = getattr(item, "284", None)
                    
                    if opp_val == self:
                        setattr(item, "284", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "284"):
                    opp_val = getattr(item, "284", None)
                    
                    setattr(item, "284", self)
                    

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
            if hasattr(old_value, "contentfwk_BusinessArchitecture29"):
                opp_val = getattr(old_value, "contentfwk_BusinessArchitecture29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_BusinessArchitecture29"):
                opp_val = getattr(value, "contentfwk_BusinessArchitecture29", None)
                if opp_val is None:
                    setattr(value, "contentfwk_BusinessArchitecture29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 415(self):
        return self.__415

    @415.setter
    def 415(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Contract__415", None)
        self.__415 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "414"):
                opp_val = getattr(old_value, "414", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "414"):
                opp_val = getattr(value, "414", None)
                if opp_val is None:
                    setattr(value, "414", set([self]))
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
class contentfwk_Process(Standard, Element):

    def __init__(self, processCritiality: str, isAutomated: bool, processVolumetrics: str, contentfwk_Process: "contentfwk_BusinessArchitecture" = None, 108: "contentfwk_Actor" = None, 81: "contentfwk_OrganizationUnit" = None, 184: "contentfwk_Function" = None, 187: "contentfwk_Function" = None, 204: set["contentfwk_Function"] = None, 207: set["contentfwk_Function"] = None, 210: set["contentfwk_OrganizationUnit"] = None, 213: set["contentfwk_Service"] = None, 216: set["contentfwk_Service"] = None, 219: set["contentfwk_Actor"] = None, 222: set["contentfwk_Control"] = None, 225: set["contentfwk_Event"] = None, 228: set["contentfwk_Event"] = None, 231: set["contentfwk_Product"] = None, contentfwk_Process235: "contentfwk_Process" = None, contentfwk_Process233: "contentfwk_Process" = None, 239: "contentfwk_Process" = None, 238: set["contentfwk_Process"] = None, 243: "contentfwk_Process" = None, 242: set["contentfwk_Process"] = None, 266: "contentfwk_Product" = None, 293: "contentfwk_Event" = None, 296: "contentfwk_Event" = None, 305: "contentfwk_Control" = None, 433: "contentfwk_Service" = None, 436: "contentfwk_Service" = None):
        self.processCritiality = processCritiality
        self.isAutomated = isAutomated
        self.processVolumetrics = processVolumetrics
        self.contentfwk_Process = contentfwk_Process
        self.108 = 108
        self.81 = 81
        self.184 = 184
        self.187 = 187
        self.204 = 204 if 204 is not None else set()
        self.207 = 207 if 207 is not None else set()
        self.210 = 210 if 210 is not None else set()
        self.213 = 213 if 213 is not None else set()
        self.216 = 216 if 216 is not None else set()
        self.219 = 219 if 219 is not None else set()
        self.222 = 222 if 222 is not None else set()
        self.225 = 225 if 225 is not None else set()
        self.228 = 228 if 228 is not None else set()
        self.231 = 231 if 231 is not None else set()
        self.contentfwk_Process235 = contentfwk_Process235
        self.contentfwk_Process233 = contentfwk_Process233
        self.239 = 239
        self.238 = 238 if 238 is not None else set()
        self.243 = 243
        self.242 = 242 if 242 is not None else set()
        self.266 = 266
        self.293 = 293
        self.296 = 296
        self.305 = 305
        self.433 = 433
        self.436 = 436
        
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
    def 243(self):
        return self.__243

    @243.setter
    def 243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__243", None)
        self.__243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "242"):
                opp_val = getattr(old_value, "242", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "242"):
                opp_val = getattr(value, "242", None)
                if opp_val is None:
                    setattr(value, "242", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 242(self):
        return self.__242

    @242.setter
    def 242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__242", None)
        self.__242 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "243"):
                    opp_val = getattr(item, "243", None)
                    
                    if opp_val == self:
                        setattr(item, "243", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "243"):
                    opp_val = getattr(item, "243", None)
                    
                    setattr(item, "243", self)
                    

    @property
    def 207(self):
        return self.__207

    @207.setter
    def 207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__207", None)
        self.__207 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "208"):
                    opp_val = getattr(item, "208", None)
                    
                    if opp_val == self:
                        setattr(item, "208", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "208"):
                    opp_val = getattr(item, "208", None)
                    
                    setattr(item, "208", self)
                    

    @property
    def 108(self):
        return self.__108

    @108.setter
    def 108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__108", None)
        self.__108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "107"):
                opp_val = getattr(old_value, "107", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "107"):
                opp_val = getattr(value, "107", None)
                if opp_val is None:
                    setattr(value, "107", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 228(self):
        return self.__228

    @228.setter
    def 228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__228", None)
        self.__228 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "229"):
                    opp_val = getattr(item, "229", None)
                    
                    if opp_val == self:
                        setattr(item, "229", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "229"):
                    opp_val = getattr(item, "229", None)
                    
                    setattr(item, "229", self)
                    

    @property
    def 239(self):
        return self.__239

    @239.setter
    def 239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__239", None)
        self.__239 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "238"):
                opp_val = getattr(old_value, "238", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "238"):
                opp_val = getattr(value, "238", None)
                if opp_val is None:
                    setattr(value, "238", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_Process235(self):
        return self.__contentfwk_Process235

    @contentfwk_Process235.setter
    def contentfwk_Process235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__contentfwk_Process235", None)
        self.__contentfwk_Process235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_Process233"):
                opp_val = getattr(old_value, "contentfwk_Process233", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_Process233", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_Process233"):
                opp_val = getattr(value, "contentfwk_Process233", None)
                setattr(value, "contentfwk_Process233", self)

    @property
    def 305(self):
        return self.__305

    @305.setter
    def 305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__305", None)
        self.__305 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "304"):
                opp_val = getattr(old_value, "304", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "304"):
                opp_val = getattr(value, "304", None)
                if opp_val is None:
                    setattr(value, "304", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 187(self):
        return self.__187

    @187.setter
    def 187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__187", None)
        self.__187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "186"):
                opp_val = getattr(old_value, "186", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "186"):
                opp_val = getattr(value, "186", None)
                if opp_val is None:
                    setattr(value, "186", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 210(self):
        return self.__210

    @210.setter
    def 210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__210", None)
        self.__210 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "211"):
                    opp_val = getattr(item, "211", None)
                    
                    if opp_val == self:
                        setattr(item, "211", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "211"):
                    opp_val = getattr(item, "211", None)
                    
                    setattr(item, "211", self)
                    

    @property
    def 296(self):
        return self.__296

    @296.setter
    def 296(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__296", None)
        self.__296 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "295"):
                opp_val = getattr(old_value, "295", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "295"):
                opp_val = getattr(value, "295", None)
                if opp_val is None:
                    setattr(value, "295", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 225(self):
        return self.__225

    @225.setter
    def 225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__225", None)
        self.__225 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "226"):
                    opp_val = getattr(item, "226", None)
                    
                    if opp_val == self:
                        setattr(item, "226", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "226"):
                    opp_val = getattr(item, "226", None)
                    
                    setattr(item, "226", self)
                    

    @property
    def 213(self):
        return self.__213

    @213.setter
    def 213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__213", None)
        self.__213 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "214"):
                    opp_val = getattr(item, "214", None)
                    
                    if opp_val == self:
                        setattr(item, "214", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "214"):
                    opp_val = getattr(item, "214", None)
                    
                    setattr(item, "214", self)
                    

    @property
    def 184(self):
        return self.__184

    @184.setter
    def 184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__184", None)
        self.__184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "183"):
                opp_val = getattr(old_value, "183", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "183"):
                opp_val = getattr(value, "183", None)
                if opp_val is None:
                    setattr(value, "183", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 219(self):
        return self.__219

    @219.setter
    def 219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__219", None)
        self.__219 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "220"):
                    opp_val = getattr(item, "220", None)
                    
                    if opp_val == self:
                        setattr(item, "220", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "220"):
                    opp_val = getattr(item, "220", None)
                    
                    setattr(item, "220", self)
                    

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
            if hasattr(old_value, "contentfwk_BusinessArchitecture19"):
                opp_val = getattr(old_value, "contentfwk_BusinessArchitecture19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_BusinessArchitecture19"):
                opp_val = getattr(value, "contentfwk_BusinessArchitecture19", None)
                if opp_val is None:
                    setattr(value, "contentfwk_BusinessArchitecture19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 266(self):
        return self.__266

    @266.setter
    def 266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__266", None)
        self.__266 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "265"):
                opp_val = getattr(old_value, "265", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "265"):
                opp_val = getattr(value, "265", None)
                if opp_val is None:
                    setattr(value, "265", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 433(self):
        return self.__433

    @433.setter
    def 433(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__433", None)
        self.__433 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "432"):
                opp_val = getattr(old_value, "432", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "432"):
                opp_val = getattr(value, "432", None)
                if opp_val is None:
                    setattr(value, "432", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_Process233(self):
        return self.__contentfwk_Process233

    @contentfwk_Process233.setter
    def contentfwk_Process233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__contentfwk_Process233", None)
        self.__contentfwk_Process233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_Process235"):
                opp_val = getattr(old_value, "contentfwk_Process235", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_Process235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_Process235"):
                opp_val = getattr(value, "contentfwk_Process235", None)
                setattr(value, "contentfwk_Process235", self)

    @property
    def 216(self):
        return self.__216

    @216.setter
    def 216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__216", None)
        self.__216 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "217"):
                    opp_val = getattr(item, "217", None)
                    
                    if opp_val == self:
                        setattr(item, "217", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "217"):
                    opp_val = getattr(item, "217", None)
                    
                    setattr(item, "217", self)
                    

    @property
    def 204(self):
        return self.__204

    @204.setter
    def 204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__204", None)
        self.__204 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "205"):
                    opp_val = getattr(item, "205", None)
                    
                    if opp_val == self:
                        setattr(item, "205", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "205"):
                    opp_val = getattr(item, "205", None)
                    
                    setattr(item, "205", self)
                    

    @property
    def 436(self):
        return self.__436

    @436.setter
    def 436(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__436", None)
        self.__436 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "435"):
                opp_val = getattr(old_value, "435", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "435"):
                opp_val = getattr(value, "435", None)
                if opp_val is None:
                    setattr(value, "435", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 81(self):
        return self.__81

    @81.setter
    def 81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__81", None)
        self.__81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "80"):
                opp_val = getattr(old_value, "80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "80"):
                opp_val = getattr(value, "80", None)
                if opp_val is None:
                    setattr(value, "80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 238(self):
        return self.__238

    @238.setter
    def 238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__238", None)
        self.__238 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "239"):
                    opp_val = getattr(item, "239", None)
                    
                    if opp_val == self:
                        setattr(item, "239", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "239"):
                    opp_val = getattr(item, "239", None)
                    
                    setattr(item, "239", self)
                    

    @property
    def 231(self):
        return self.__231

    @231.setter
    def 231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__231", None)
        self.__231 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "232"):
                    opp_val = getattr(item, "232", None)
                    
                    if opp_val == self:
                        setattr(item, "232", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "232"):
                    opp_val = getattr(item, "232", None)
                    
                    setattr(item, "232", self)
                    

    @property
    def 293(self):
        return self.__293

    @293.setter
    def 293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__293", None)
        self.__293 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "292"):
                opp_val = getattr(old_value, "292", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "292"):
                opp_val = getattr(value, "292", None)
                if opp_val is None:
                    setattr(value, "292", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 222(self):
        return self.__222

    @222.setter
    def 222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__222", None)
        self.__222 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "223"):
                    opp_val = getattr(item, "223", None)
                    
                    if opp_val == self:
                        setattr(item, "223", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "223"):
                    opp_val = getattr(item, "223", None)
                    
                    setattr(item, "223", self)
                    

class contentfwk_BusinessService(Element, Service):

    pass
class contentfwk_Function(Standard, Element):

    pass
class contentfwk_Role(Element):

    def __init__(self, estimatedFTEs: str, contentfwk_Role: "contentfwk_BusinessArchitecture" = None, 105: "contentfwk_Actor" = None, 127: set["contentfwk_Actor"] = None, 130: set["contentfwk_Function"] = None, contentfwk_Role134: "contentfwk_Role" = None, contentfwk_Role132: "contentfwk_Role" = None, 190: "contentfwk_Function" = None):
        self.estimatedFTEs = estimatedFTEs
        self.contentfwk_Role = contentfwk_Role
        self.105 = 105
        self.127 = 127 if 127 is not None else set()
        self.130 = 130 if 130 is not None else set()
        self.contentfwk_Role134 = contentfwk_Role134
        self.contentfwk_Role132 = contentfwk_Role132
        self.190 = 190
        
    @property
    def estimatedFTEs(self) -> str:
        return self.__estimatedFTEs

    @estimatedFTEs.setter
    def estimatedFTEs(self, estimatedFTEs: str):
        self.__estimatedFTEs = estimatedFTEs

    @property
    def 190(self):
        return self.__190

    @190.setter
    def 190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Role__190", None)
        self.__190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "189"):
                opp_val = getattr(old_value, "189", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "189"):
                opp_val = getattr(value, "189", None)
                if opp_val is None:
                    setattr(value, "189", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_Role132(self):
        return self.__contentfwk_Role132

    @contentfwk_Role132.setter
    def contentfwk_Role132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Role__contentfwk_Role132", None)
        self.__contentfwk_Role132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_Role134"):
                opp_val = getattr(old_value, "contentfwk_Role134", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_Role134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_Role134"):
                opp_val = getattr(value, "contentfwk_Role134", None)
                setattr(value, "contentfwk_Role134", self)

    @property
    def 130(self):
        return self.__130

    @130.setter
    def 130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Role__130", None)
        self.__130 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "131"):
                    opp_val = getattr(item, "131", None)
                    
                    if opp_val == self:
                        setattr(item, "131", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "131"):
                    opp_val = getattr(item, "131", None)
                    
                    setattr(item, "131", self)
                    

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
    def 105(self):
        return self.__105

    @105.setter
    def 105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Role__105", None)
        self.__105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "104"):
                opp_val = getattr(old_value, "104", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "104"):
                opp_val = getattr(value, "104", None)
                if opp_val is None:
                    setattr(value, "104", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 127(self):
        return self.__127

    @127.setter
    def 127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Role__127", None)
        self.__127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "128"):
                    opp_val = getattr(item, "128", None)
                    
                    if opp_val == self:
                        setattr(item, "128", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "128"):
                    opp_val = getattr(item, "128", None)
                    
                    setattr(item, "128", self)
                    

    @property
    def contentfwk_Role134(self):
        return self.__contentfwk_Role134

    @contentfwk_Role134.setter
    def contentfwk_Role134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Role__contentfwk_Role134", None)
        self.__contentfwk_Role134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_Role132"):
                opp_val = getattr(old_value, "contentfwk_Role132", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_Role132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_Role132"):
                opp_val = getattr(value, "contentfwk_Role132", None)
                setattr(value, "contentfwk_Role132", self)

class contentfwk_Actor(Element):

    def __init__(self, FTEs: str, actorGoal: str, actorTasks: str, contentfwk_Actor: "contentfwk_BusinessArchitecture" = None, 92: set["contentfwk_DataEntity"] = None, 95: set["contentfwk_DataEntity"] = None, 98: "contentfwk_OrganizationUnit" = None, 101: set["contentfwk_Function"] = None, 104: set["contentfwk_Role"] = None, 107: set["contentfwk_Process"] = None, contentfwk_Actor110: set["contentfwk_Service"] = None, 112: set["contentfwk_Event"] = None, 115: set["contentfwk_Event"] = None, 118: "contentfwk_Location" = None, 75: "contentfwk_OrganizationUnit" = None, 121: set["contentfwk_Function"] = None, contentfwk_Actor125: "contentfwk_Actor" = None, contentfwk_Actor123: set["contentfwk_Actor"] = None, 128: "contentfwk_Role" = None, 137: "contentfwk_DataEntity" = None, 140: "contentfwk_DataEntity" = None, 175: "contentfwk_Function" = None, 193: "contentfwk_Function" = None, 220: "contentfwk_Process" = None, 299: "contentfwk_Event" = None, 302: "contentfwk_Event" = None, 318: "contentfwk_Location" = None, contentfwk_Actor403: "contentfwk_Service" = None):
        self.FTEs = FTEs
        self.actorGoal = actorGoal
        self.actorTasks = actorTasks
        self.contentfwk_Actor = contentfwk_Actor
        self.92 = 92 if 92 is not None else set()
        self.95 = 95 if 95 is not None else set()
        self.98 = 98
        self.101 = 101 if 101 is not None else set()
        self.104 = 104 if 104 is not None else set()
        self.107 = 107 if 107 is not None else set()
        self.contentfwk_Actor110 = contentfwk_Actor110 if contentfwk_Actor110 is not None else set()
        self.112 = 112 if 112 is not None else set()
        self.115 = 115 if 115 is not None else set()
        self.118 = 118
        self.75 = 75
        self.121 = 121 if 121 is not None else set()
        self.contentfwk_Actor125 = contentfwk_Actor125
        self.contentfwk_Actor123 = contentfwk_Actor123 if contentfwk_Actor123 is not None else set()
        self.128 = 128
        self.137 = 137
        self.140 = 140
        self.175 = 175
        self.193 = 193
        self.220 = 220
        self.299 = 299
        self.302 = 302
        self.318 = 318
        self.contentfwk_Actor403 = contentfwk_Actor403
        
    @property
    def FTEs(self) -> str:
        return self.__FTEs

    @FTEs.setter
    def FTEs(self, FTEs: str):
        self.__FTEs = FTEs

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
    def contentfwk_Actor110(self):
        return self.__contentfwk_Actor110

    @contentfwk_Actor110.setter
    def contentfwk_Actor110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__contentfwk_Actor110", None)
        self.__contentfwk_Actor110 = value if value is not None else set()
        
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
    def 193(self):
        return self.__193

    @193.setter
    def 193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__193", None)
        self.__193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "192"):
                opp_val = getattr(old_value, "192", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "192"):
                opp_val = getattr(value, "192", None)
                if opp_val is None:
                    setattr(value, "192", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 104(self):
        return self.__104

    @104.setter
    def 104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__104", None)
        self.__104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "105"):
                    opp_val = getattr(item, "105", None)
                    
                    if opp_val == self:
                        setattr(item, "105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "105"):
                    opp_val = getattr(item, "105", None)
                    
                    setattr(item, "105", self)
                    

    @property
    def 128(self):
        return self.__128

    @128.setter
    def 128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__128", None)
        self.__128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "127"):
                opp_val = getattr(old_value, "127", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "127"):
                opp_val = getattr(value, "127", None)
                if opp_val is None:
                    setattr(value, "127", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 299(self):
        return self.__299

    @299.setter
    def 299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__299", None)
        self.__299 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "298"):
                opp_val = getattr(old_value, "298", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "298"):
                opp_val = getattr(value, "298", None)
                if opp_val is None:
                    setattr(value, "298", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 121(self):
        return self.__121

    @121.setter
    def 121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__121", None)
        self.__121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "122"):
                    opp_val = getattr(item, "122", None)
                    
                    if opp_val == self:
                        setattr(item, "122", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "122"):
                    opp_val = getattr(item, "122", None)
                    
                    setattr(item, "122", self)
                    

    @property
    def 140(self):
        return self.__140

    @140.setter
    def 140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__140", None)
        self.__140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "139"):
                opp_val = getattr(old_value, "139", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "139"):
                opp_val = getattr(value, "139", None)
                if opp_val is None:
                    setattr(value, "139", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 98(self):
        return self.__98

    @98.setter
    def 98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__98", None)
        self.__98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "99"):
                opp_val = getattr(old_value, "99", None)
                if opp_val == self:
                    setattr(old_value, "99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "99"):
                opp_val = getattr(value, "99", None)
                setattr(value, "99", self)

    @property
    def 302(self):
        return self.__302

    @302.setter
    def 302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__302", None)
        self.__302 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "301"):
                opp_val = getattr(old_value, "301", None)
                if opp_val == self:
                    setattr(old_value, "301", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "301"):
                opp_val = getattr(value, "301", None)
                setattr(value, "301", self)

    @property
    def 115(self):
        return self.__115

    @115.setter
    def 115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__115", None)
        self.__115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "116"):
                    opp_val = getattr(item, "116", None)
                    
                    if opp_val == self:
                        setattr(item, "116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "116"):
                    opp_val = getattr(item, "116", None)
                    
                    setattr(item, "116", self)
                    

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
    def 75(self):
        return self.__75

    @75.setter
    def 75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__75", None)
        self.__75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "74"):
                opp_val = getattr(old_value, "74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "74"):
                opp_val = getattr(value, "74", None)
                if opp_val is None:
                    setattr(value, "74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 95(self):
        return self.__95

    @95.setter
    def 95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__95", None)
        self.__95 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "96"):
                    opp_val = getattr(item, "96", None)
                    
                    if opp_val == self:
                        setattr(item, "96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "96"):
                    opp_val = getattr(item, "96", None)
                    
                    setattr(item, "96", self)
                    

    @property
    def 107(self):
        return self.__107

    @107.setter
    def 107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__107", None)
        self.__107 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "108"):
                    opp_val = getattr(item, "108", None)
                    
                    if opp_val == self:
                        setattr(item, "108", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "108"):
                    opp_val = getattr(item, "108", None)
                    
                    setattr(item, "108", self)
                    

    @property
    def 220(self):
        return self.__220

    @220.setter
    def 220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__220", None)
        self.__220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "219"):
                opp_val = getattr(old_value, "219", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "219"):
                opp_val = getattr(value, "219", None)
                if opp_val is None:
                    setattr(value, "219", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_Actor125(self):
        return self.__contentfwk_Actor125

    @contentfwk_Actor125.setter
    def contentfwk_Actor125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__contentfwk_Actor125", None)
        self.__contentfwk_Actor125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_Actor123"):
                opp_val = getattr(old_value, "contentfwk_Actor123", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_Actor123"):
                opp_val = getattr(value, "contentfwk_Actor123", None)
                if opp_val is None:
                    setattr(value, "contentfwk_Actor123", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 112(self):
        return self.__112

    @112.setter
    def 112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__112", None)
        self.__112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "113"):
                    opp_val = getattr(item, "113", None)
                    
                    if opp_val == self:
                        setattr(item, "113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "113"):
                    opp_val = getattr(item, "113", None)
                    
                    setattr(item, "113", self)
                    

    @property
    def 175(self):
        return self.__175

    @175.setter
    def 175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__175", None)
        self.__175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "174"):
                opp_val = getattr(old_value, "174", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "174"):
                opp_val = getattr(value, "174", None)
                if opp_val is None:
                    setattr(value, "174", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 137(self):
        return self.__137

    @137.setter
    def 137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__137", None)
        self.__137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "136"):
                opp_val = getattr(old_value, "136", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "136"):
                opp_val = getattr(value, "136", None)
                if opp_val is None:
                    setattr(value, "136", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 101(self):
        return self.__101

    @101.setter
    def 101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__101", None)
        self.__101 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "102"):
                    opp_val = getattr(item, "102", None)
                    
                    if opp_val == self:
                        setattr(item, "102", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "102"):
                    opp_val = getattr(item, "102", None)
                    
                    setattr(item, "102", self)
                    

    @property
    def 318(self):
        return self.__318

    @318.setter
    def 318(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__318", None)
        self.__318 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "317"):
                opp_val = getattr(old_value, "317", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "317"):
                opp_val = getattr(value, "317", None)
                if opp_val is None:
                    setattr(value, "317", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_Actor123(self):
        return self.__contentfwk_Actor123

    @contentfwk_Actor123.setter
    def contentfwk_Actor123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__contentfwk_Actor123", None)
        self.__contentfwk_Actor123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_Actor125"):
                    opp_val = getattr(item, "contentfwk_Actor125", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_Actor125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_Actor125"):
                    opp_val = getattr(item, "contentfwk_Actor125", None)
                    
                    setattr(item, "contentfwk_Actor125", self)
                    

    @property
    def 118(self):
        return self.__118

    @118.setter
    def 118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__118", None)
        self.__118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "119"):
                opp_val = getattr(old_value, "119", None)
                if opp_val == self:
                    setattr(old_value, "119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "119"):
                opp_val = getattr(value, "119", None)
                setattr(value, "119", self)

    @property
    def contentfwk_Actor403(self):
        return self.__contentfwk_Actor403

    @contentfwk_Actor403.setter
    def contentfwk_Actor403(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__contentfwk_Actor403", None)
        self.__contentfwk_Actor403 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_Service402"):
                opp_val = getattr(old_value, "contentfwk_Service402", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_Service402"):
                opp_val = getattr(value, "contentfwk_Service402", None)
                if opp_val is None:
                    setattr(value, "contentfwk_Service402", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 92(self):
        return self.__92

    @92.setter
    def 92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__92", None)
        self.__92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "93"):
                    opp_val = getattr(item, "93", None)
                    
                    if opp_val == self:
                        setattr(item, "93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "93"):
                    opp_val = getattr(item, "93", None)
                    
                    setattr(item, "93", self)
                    

class contentfwk_OrganizationUnit(Element):

    def __init__(self, headcount: str, contentfwk_OrganizationUnit: "contentfwk_BusinessArchitecture" = None, 48: "contentfwk_Driver" = None, 83: set["contentfwk_Driver"] = None, 86: set["contentfwk_Product"] = None, 89: "contentfwk_Location" = None, 99: "contentfwk_Actor" = None, 71: set["contentfwk_Service"] = None, 74: set["contentfwk_Actor"] = None, 77: set["contentfwk_Function"] = None, 80: set["contentfwk_Process"] = None, 178: "contentfwk_Function" = None, 211: "contentfwk_Process" = None, 263: "contentfwk_Product" = None, 321: "contentfwk_Location" = None, 427: "contentfwk_Service" = None):
        self.headcount = headcount
        self.contentfwk_OrganizationUnit = contentfwk_OrganizationUnit
        self.48 = 48
        self.83 = 83 if 83 is not None else set()
        self.86 = 86 if 86 is not None else set()
        self.89 = 89
        self.99 = 99
        self.71 = 71 if 71 is not None else set()
        self.74 = 74 if 74 is not None else set()
        self.77 = 77 if 77 is not None else set()
        self.80 = 80 if 80 is not None else set()
        self.178 = 178
        self.211 = 211
        self.263 = 263
        self.321 = 321
        self.427 = 427
        
    @property
    def headcount(self) -> str:
        return self.__headcount

    @headcount.setter
    def headcount(self, headcount: str):
        self.__headcount = headcount

    @property
    def 48(self):
        return self.__48

    @48.setter
    def 48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__48", None)
        self.__48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "47"):
                opp_val = getattr(old_value, "47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "47"):
                opp_val = getattr(value, "47", None)
                if opp_val is None:
                    setattr(value, "47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 99(self):
        return self.__99

    @99.setter
    def 99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__99", None)
        self.__99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "98"):
                opp_val = getattr(old_value, "98", None)
                if opp_val == self:
                    setattr(old_value, "98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "98"):
                opp_val = getattr(value, "98", None)
                setattr(value, "98", self)

    @property
    def 80(self):
        return self.__80

    @80.setter
    def 80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__80", None)
        self.__80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "81"):
                    opp_val = getattr(item, "81", None)
                    
                    if opp_val == self:
                        setattr(item, "81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "81"):
                    opp_val = getattr(item, "81", None)
                    
                    setattr(item, "81", self)
                    

    @property
    def 427(self):
        return self.__427

    @427.setter
    def 427(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__427", None)
        self.__427 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "426"):
                opp_val = getattr(old_value, "426", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "426"):
                opp_val = getattr(value, "426", None)
                if opp_val is None:
                    setattr(value, "426", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 86(self):
        return self.__86

    @86.setter
    def 86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__86", None)
        self.__86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "87"):
                    opp_val = getattr(item, "87", None)
                    
                    if opp_val == self:
                        setattr(item, "87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "87"):
                    opp_val = getattr(item, "87", None)
                    
                    setattr(item, "87", self)
                    

    @property
    def 77(self):
        return self.__77

    @77.setter
    def 77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__77", None)
        self.__77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "78"):
                    opp_val = getattr(item, "78", None)
                    
                    if opp_val == self:
                        setattr(item, "78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "78"):
                    opp_val = getattr(item, "78", None)
                    
                    setattr(item, "78", self)
                    

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
    def 74(self):
        return self.__74

    @74.setter
    def 74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__74", None)
        self.__74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "75"):
                    opp_val = getattr(item, "75", None)
                    
                    if opp_val == self:
                        setattr(item, "75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "75"):
                    opp_val = getattr(item, "75", None)
                    
                    setattr(item, "75", self)
                    

    @property
    def 178(self):
        return self.__178

    @178.setter
    def 178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__178", None)
        self.__178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "177"):
                opp_val = getattr(old_value, "177", None)
                if opp_val == self:
                    setattr(old_value, "177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "177"):
                opp_val = getattr(value, "177", None)
                setattr(value, "177", self)

    @property
    def 83(self):
        return self.__83

    @83.setter
    def 83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__83", None)
        self.__83 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "84"):
                    opp_val = getattr(item, "84", None)
                    
                    if opp_val == self:
                        setattr(item, "84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "84"):
                    opp_val = getattr(item, "84", None)
                    
                    setattr(item, "84", self)
                    

    @property
    def 211(self):
        return self.__211

    @211.setter
    def 211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__211", None)
        self.__211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "210"):
                opp_val = getattr(old_value, "210", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "210"):
                opp_val = getattr(value, "210", None)
                if opp_val is None:
                    setattr(value, "210", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 89(self):
        return self.__89

    @89.setter
    def 89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__89", None)
        self.__89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "90"):
                opp_val = getattr(old_value, "90", None)
                if opp_val == self:
                    setattr(old_value, "90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "90"):
                opp_val = getattr(value, "90", None)
                setattr(value, "90", self)

    @property
    def 263(self):
        return self.__263

    @263.setter
    def 263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__263", None)
        self.__263 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "262"):
                opp_val = getattr(old_value, "262", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "262"):
                opp_val = getattr(value, "262", None)
                if opp_val is None:
                    setattr(value, "262", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 71(self):
        return self.__71

    @71.setter
    def 71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__71", None)
        self.__71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "72"):
                    opp_val = getattr(item, "72", None)
                    
                    if opp_val == self:
                        setattr(item, "72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "72"):
                    opp_val = getattr(item, "72", None)
                    
                    setattr(item, "72", self)
                    

    @property
    def 321(self):
        return self.__321

    @321.setter
    def 321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__321", None)
        self.__321 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "320"):
                opp_val = getattr(old_value, "320", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "320"):
                opp_val = getattr(value, "320", None)
                if opp_val is None:
                    setattr(value, "320", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class contentfwk_Objective(Element):

    pass
class contentfwk_Goal(Element):

    pass
class contentfwk_Driver(Element):

    pass
class Architecture:

    pass
class contentfwk_StrategicArchitecture(Architecture):

    pass
class contentfwk_ApplicationArchitecture(Architecture):

    pass
class contentfwk_DataArchitecture(Architecture):

    pass
class contentfwk_TechnologyArchitecture(Architecture):

    pass
class contentfwk_BusinessArchitecture(Architecture):

    pass
class contentfwk_Architecture(ABC):

    pass
class contentfwk_EnterpriseArchitecture:

    pass