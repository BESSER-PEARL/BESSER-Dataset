from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

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
class LifeCycleStatus(Enum):
    Proposed = "Proposed"
    InDevelopment = "InDevelopment"
    Live = "Live"
    PhasingOut = "PhasingOut"
    Retired = "Retired"
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

    def __init__(self, standardClass: str, standardCreationDate: date, lastStandardCreationDate: date, nextStandardCreationDate: date, retireDate: str):
        self.standardClass = standardClass
        self.standardCreationDate = standardCreationDate
        self.lastStandardCreationDate = lastStandardCreationDate
        self.nextStandardCreationDate = nextStandardCreationDate
        self.retireDate = retireDate
        
        pass
    @property
    def retireDate(self):
        return self.__retireDate

    @retireDate.setter
    def retireDate(self, retireDate: str):
        self.__retireDate = retireDate


    @property
    def lastStandardCreationDate(self):
        return self.__lastStandardCreationDate

    @lastStandardCreationDate.setter
    def lastStandardCreationDate(self, lastStandardCreationDate: date):
        self.__lastStandardCreationDate = lastStandardCreationDate


    @property
    def standardCreationDate(self):
        return self.__standardCreationDate

    @standardCreationDate.setter
    def standardCreationDate(self, standardCreationDate: date):
        self.__standardCreationDate = standardCreationDate


    @property
    def standardClass(self):
        return self.__standardClass

    @standardClass.setter
    def standardClass(self, standardClass: str):
        self.__standardClass = standardClass


    @property
    def nextStandardCreationDate(self):
        return self.__nextStandardCreationDate

    @nextStandardCreationDate.setter
    def nextStandardCreationDate(self, nextStandardCreationDate: date):
        self.__nextStandardCreationDate = nextStandardCreationDate


class DataComponent:

    pass
class StrategicElement:

    pass
class contentfwk_Principle(StrategicElement):

    def __init__(self, rationale: str, implication: str, metric: str, principleCategory: str, priority: str, statementOfPrinciple: str):
        self.rationale = rationale
        self.implication = implication
        self.metric = metric
        self.principleCategory = principleCategory
        self.priority = priority
        self.statementOfPrinciple = statementOfPrinciple
        
        pass
    @property
    def statementOfPrinciple(self):
        return self.__statementOfPrinciple

    @statementOfPrinciple.setter
    def statementOfPrinciple(self, statementOfPrinciple: str):
        self.__statementOfPrinciple = statementOfPrinciple


    @property
    def rationale(self):
        return self.__rationale

    @rationale.setter
    def rationale(self, rationale: str):
        self.__rationale = rationale


    @property
    def metric(self):
        return self.__metric

    @metric.setter
    def metric(self, metric: str):
        self.__metric = metric


    @property
    def principleCategory(self):
        return self.__principleCategory

    @principleCategory.setter
    def principleCategory(self, principleCategory: str):
        self.__principleCategory = principleCategory


    @property
    def implication(self):
        return self.__implication

    @implication.setter
    def implication(self, implication: str):
        self.__implication = implication


    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority


class contentfwk_WorkPackage(StrategicElement):

    def __init__(self, workPackageCategory: str, WorkPackage: "contentfwk_Capability" = None, isDeliveredBy: set["contentfwk_Capability"] = None):
        self.workPackageCategory = workPackageCategory
        self.WorkPackage = WorkPackage
        self.isDeliveredBy = isDeliveredBy if isDeliveredBy is not None else set()
        
        pass
    @property
    def workPackageCategory(self):
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

class contentfwk_Gap(StrategicElement):

    pass
class contentfwk_Requirement(StrategicElement):

    def __init__(self, statementOfRequirement: str, rationale: str, acceptanceCriteria: str):
        self.statementOfRequirement = statementOfRequirement
        self.rationale = rationale
        self.acceptanceCriteria = acceptanceCriteria
        
        pass
    @property
    def acceptanceCriteria(self):
        return self.__acceptanceCriteria

    @acceptanceCriteria.setter
    def acceptanceCriteria(self, acceptanceCriteria: str):
        self.__acceptanceCriteria = acceptanceCriteria


    @property
    def statementOfRequirement(self):
        return self.__statementOfRequirement

    @statementOfRequirement.setter
    def statementOfRequirement(self, statementOfRequirement: str):
        self.__statementOfRequirement = statementOfRequirement


    @property
    def rationale(self):
        return self.__rationale

    @rationale.setter
    def rationale(self, rationale: str):
        self.__rationale = rationale


class contentfwk_Assumption(StrategicElement):

    pass
class contentfwk_Constraint(StrategicElement):

    pass
class contentfwk_Element:

    def __init__(self, name: str, description: str, category: str, sourceDescr: str, ownerDescr: str, ID: str, contentfwk_Element: "contentfwk_Container" = None, Element: "contentfwk_Element" = None, isDelegatedBy: set["contentfwk_Element"] = None, Element230: "contentfwk_Element" = None, delegates: set["contentfwk_Element"] = None):
        self.name = name
        self.description = description
        self.category = category
        self.sourceDescr = sourceDescr
        self.ownerDescr = ownerDescr
        self.ID = ID
        self.contentfwk_Element = contentfwk_Element
        self.Element = Element
        self.isDelegatedBy = isDelegatedBy if isDelegatedBy is not None else set()
        self.Element230 = Element230
        self.delegates = delegates if delegates is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sourceDescr(self):
        return self.__sourceDescr

    @sourceDescr.setter
    def sourceDescr(self, sourceDescr: str):
        self.__sourceDescr = sourceDescr


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def ownerDescr(self):
        return self.__ownerDescr

    @ownerDescr.setter
    def ownerDescr(self, ownerDescr: str):
        self.__ownerDescr = ownerDescr


    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID


    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category


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
            if hasattr(old_value, "contentfwk_Container232"):
                opp_val = getattr(old_value, "contentfwk_Container232", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_Container232"):
                opp_val = getattr(value, "contentfwk_Container232", None)
                if opp_val is None:
                    setattr(value, "contentfwk_Container232", set([self]))
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
    def Element230(self):
        return self.__Element230

    @Element230.setter
    def Element230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Element__Element230", None)
        self.__Element230 = value
        
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
                if hasattr(item, "Element230"):
                    opp_val = getattr(item, "Element230", None)
                    
                    if opp_val == self:
                        setattr(item, "Element230", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element230"):
                    opp_val = getattr(item, "Element230", None)
                    
                    setattr(item, "Element230", self)
                    

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
                    

class TechnologyComponent:

    pass
class Service:

    pass
class ApplicationComponent:

    pass
class Standard:

    pass
class contentfwk_TechnologyComponent(Standard):

    pass
class contentfwk_DataComponent(Standard):

    pass
class contentfwk_ApplicationComponent(Standard):

    pass
class Element:

    pass
class contentfwk_InformationSystemService(Element, Service):

    pass
class contentfwk_LogicalApplicationComponent(ApplicationComponent, Element):

    pass
class contentfwk_Capability(Element):

    def __init__(self, businessValue: str, increments: str, deliversCapabilities: "contentfwk_WorkPackage" = None, Capability: "contentfwk_WorkPackage" = None, contentfwk_Capability: "contentfwk_StrategicArchitecture" = None):
        self.businessValue = businessValue
        self.increments = increments
        self.deliversCapabilities = deliversCapabilities
        self.Capability = Capability
        self.contentfwk_Capability = contentfwk_Capability
        
        pass
    @property
    def businessValue(self):
        return self.__businessValue

    @businessValue.setter
    def businessValue(self, businessValue: str):
        self.__businessValue = businessValue


    @property
    def increments(self):
        return self.__increments

    @increments.setter
    def increments(self, increments: str):
        self.__increments = increments


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

class contentfwk_PhysicalApplicationComponent(ApplicationComponent, Element):

    def __init__(self, securityCharacteristics: str, privacyCharacteristics: str, integrityCharacteristics: str, credibilityCharacteristics: str, localizationCharacteristics: str, internationalizationCharacteristics: str, interoperabilityCharacteristics: str, scalabilityCharacteristics: str, portabilityCharacteristics: str, extensibilityCharacteristics: str, capacityCharacteristics: str, throughput: str, throughputPeriod: str, growth: str, growthPeriod: str, peakProfileShortTerm: str, lifeCycleStatus: str, initialLiveDate: date, dateOfLastRelease: date, dateOfNextRelease: date, retirementDate: date, availabilityQualityCharacteristics: str, servicesTimes: str, manageabilityCharacteristics: str, serviceabilityCharacteristics: str, performanceCharacteristics: str, reliabilityCharacteristics: str, recoverabilityCharacteristics: str, locatabilityCharacteristics: str, peakProfileLongTerm: str, contentfwk_PhysicalApplicationComponent: "contentfwk_PhysicalTechnologyComponent" = None, PhysicalApplicationComponent: "contentfwk_LogicalApplicationComponent" = None, PhysicalApplicationComponent240: "contentfwk_Location" = None, contentfwk_PhysicalApplicationComponent261: "contentfwk_PhysicalDataComponent" = None, contentfwk_PhysicalApplicationComponent266: "contentfwk_ApplicationArchitecture" = None, isExtendedByPhysicalApplicationComponents: set["contentfwk_LogicalApplicationComponent"] = None, containsPhysicalApplicationComponents: set["contentfwk_Location"] = None, contentfwk_PhysicalApplicationComponent275: "contentfwk_PhysicalApplicationComponent" = None, contentfwk_PhysicalApplicationComponent273: set["contentfwk_PhysicalApplicationComponent"] = None, contentfwk_PhysicalApplicationComponent277: set["contentfwk_PhysicalDataComponent"] = None, contentfwk_PhysicalApplicationComponent280: set["contentfwk_PhysicalTechnologyComponent"] = None, contentfwk_PhysicalApplicationComponent284: "contentfwk_PhysicalApplicationComponent" = None, contentfwk_PhysicalApplicationComponent282: "contentfwk_PhysicalApplicationComponent" = None):
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
        self.peakProfileLongTerm = peakProfileLongTerm
        self.contentfwk_PhysicalApplicationComponent = contentfwk_PhysicalApplicationComponent
        self.PhysicalApplicationComponent = PhysicalApplicationComponent
        self.PhysicalApplicationComponent240 = PhysicalApplicationComponent240
        self.contentfwk_PhysicalApplicationComponent261 = contentfwk_PhysicalApplicationComponent261
        self.contentfwk_PhysicalApplicationComponent266 = contentfwk_PhysicalApplicationComponent266
        self.isExtendedByPhysicalApplicationComponents = isExtendedByPhysicalApplicationComponents if isExtendedByPhysicalApplicationComponents is not None else set()
        self.containsPhysicalApplicationComponents = containsPhysicalApplicationComponents if containsPhysicalApplicationComponents is not None else set()
        self.contentfwk_PhysicalApplicationComponent275 = contentfwk_PhysicalApplicationComponent275
        self.contentfwk_PhysicalApplicationComponent273 = contentfwk_PhysicalApplicationComponent273 if contentfwk_PhysicalApplicationComponent273 is not None else set()
        self.contentfwk_PhysicalApplicationComponent277 = contentfwk_PhysicalApplicationComponent277 if contentfwk_PhysicalApplicationComponent277 is not None else set()
        self.contentfwk_PhysicalApplicationComponent280 = contentfwk_PhysicalApplicationComponent280 if contentfwk_PhysicalApplicationComponent280 is not None else set()
        self.contentfwk_PhysicalApplicationComponent284 = contentfwk_PhysicalApplicationComponent284
        self.contentfwk_PhysicalApplicationComponent282 = contentfwk_PhysicalApplicationComponent282
        
        pass
    @property
    def locatabilityCharacteristics(self):
        return self.__locatabilityCharacteristics

    @locatabilityCharacteristics.setter
    def locatabilityCharacteristics(self, locatabilityCharacteristics: str):
        self.__locatabilityCharacteristics = locatabilityCharacteristics


    @property
    def peakProfileShortTerm(self):
        return self.__peakProfileShortTerm

    @peakProfileShortTerm.setter
    def peakProfileShortTerm(self, peakProfileShortTerm: str):
        self.__peakProfileShortTerm = peakProfileShortTerm


    @property
    def growth(self):
        return self.__growth

    @growth.setter
    def growth(self, growth: str):
        self.__growth = growth


    @property
    def credibilityCharacteristics(self):
        return self.__credibilityCharacteristics

    @credibilityCharacteristics.setter
    def credibilityCharacteristics(self, credibilityCharacteristics: str):
        self.__credibilityCharacteristics = credibilityCharacteristics


    @property
    def peakProfileLongTerm(self):
        return self.__peakProfileLongTerm

    @peakProfileLongTerm.setter
    def peakProfileLongTerm(self, peakProfileLongTerm: str):
        self.__peakProfileLongTerm = peakProfileLongTerm


    @property
    def throughputPeriod(self):
        return self.__throughputPeriod

    @throughputPeriod.setter
    def throughputPeriod(self, throughputPeriod: str):
        self.__throughputPeriod = throughputPeriod


    @property
    def portabilityCharacteristics(self):
        return self.__portabilityCharacteristics

    @portabilityCharacteristics.setter
    def portabilityCharacteristics(self, portabilityCharacteristics: str):
        self.__portabilityCharacteristics = portabilityCharacteristics


    @property
    def interoperabilityCharacteristics(self):
        return self.__interoperabilityCharacteristics

    @interoperabilityCharacteristics.setter
    def interoperabilityCharacteristics(self, interoperabilityCharacteristics: str):
        self.__interoperabilityCharacteristics = interoperabilityCharacteristics


    @property
    def manageabilityCharacteristics(self):
        return self.__manageabilityCharacteristics

    @manageabilityCharacteristics.setter
    def manageabilityCharacteristics(self, manageabilityCharacteristics: str):
        self.__manageabilityCharacteristics = manageabilityCharacteristics


    @property
    def localizationCharacteristics(self):
        return self.__localizationCharacteristics

    @localizationCharacteristics.setter
    def localizationCharacteristics(self, localizationCharacteristics: str):
        self.__localizationCharacteristics = localizationCharacteristics


    @property
    def privacyCharacteristics(self):
        return self.__privacyCharacteristics

    @privacyCharacteristics.setter
    def privacyCharacteristics(self, privacyCharacteristics: str):
        self.__privacyCharacteristics = privacyCharacteristics


    @property
    def availabilityQualityCharacteristics(self):
        return self.__availabilityQualityCharacteristics

    @availabilityQualityCharacteristics.setter
    def availabilityQualityCharacteristics(self, availabilityQualityCharacteristics: str):
        self.__availabilityQualityCharacteristics = availabilityQualityCharacteristics


    @property
    def reliabilityCharacteristics(self):
        return self.__reliabilityCharacteristics

    @reliabilityCharacteristics.setter
    def reliabilityCharacteristics(self, reliabilityCharacteristics: str):
        self.__reliabilityCharacteristics = reliabilityCharacteristics


    @property
    def capacityCharacteristics(self):
        return self.__capacityCharacteristics

    @capacityCharacteristics.setter
    def capacityCharacteristics(self, capacityCharacteristics: str):
        self.__capacityCharacteristics = capacityCharacteristics


    @property
    def scalabilityCharacteristics(self):
        return self.__scalabilityCharacteristics

    @scalabilityCharacteristics.setter
    def scalabilityCharacteristics(self, scalabilityCharacteristics: str):
        self.__scalabilityCharacteristics = scalabilityCharacteristics


    @property
    def securityCharacteristics(self):
        return self.__securityCharacteristics

    @securityCharacteristics.setter
    def securityCharacteristics(self, securityCharacteristics: str):
        self.__securityCharacteristics = securityCharacteristics


    @property
    def initialLiveDate(self):
        return self.__initialLiveDate

    @initialLiveDate.setter
    def initialLiveDate(self, initialLiveDate: date):
        self.__initialLiveDate = initialLiveDate


    @property
    def extensibilityCharacteristics(self):
        return self.__extensibilityCharacteristics

    @extensibilityCharacteristics.setter
    def extensibilityCharacteristics(self, extensibilityCharacteristics: str):
        self.__extensibilityCharacteristics = extensibilityCharacteristics


    @property
    def integrityCharacteristics(self):
        return self.__integrityCharacteristics

    @integrityCharacteristics.setter
    def integrityCharacteristics(self, integrityCharacteristics: str):
        self.__integrityCharacteristics = integrityCharacteristics


    @property
    def servicesTimes(self):
        return self.__servicesTimes

    @servicesTimes.setter
    def servicesTimes(self, servicesTimes: str):
        self.__servicesTimes = servicesTimes


    @property
    def throughput(self):
        return self.__throughput

    @throughput.setter
    def throughput(self, throughput: str):
        self.__throughput = throughput


    @property
    def performanceCharacteristics(self):
        return self.__performanceCharacteristics

    @performanceCharacteristics.setter
    def performanceCharacteristics(self, performanceCharacteristics: str):
        self.__performanceCharacteristics = performanceCharacteristics


    @property
    def lifeCycleStatus(self):
        return self.__lifeCycleStatus

    @lifeCycleStatus.setter
    def lifeCycleStatus(self, lifeCycleStatus: str):
        self.__lifeCycleStatus = lifeCycleStatus


    @property
    def growthPeriod(self):
        return self.__growthPeriod

    @growthPeriod.setter
    def growthPeriod(self, growthPeriod: str):
        self.__growthPeriod = growthPeriod


    @property
    def recoverabilityCharacteristics(self):
        return self.__recoverabilityCharacteristics

    @recoverabilityCharacteristics.setter
    def recoverabilityCharacteristics(self, recoverabilityCharacteristics: str):
        self.__recoverabilityCharacteristics = recoverabilityCharacteristics


    @property
    def dateOfLastRelease(self):
        return self.__dateOfLastRelease

    @dateOfLastRelease.setter
    def dateOfLastRelease(self, dateOfLastRelease: date):
        self.__dateOfLastRelease = dateOfLastRelease


    @property
    def retirementDate(self):
        return self.__retirementDate

    @retirementDate.setter
    def retirementDate(self, retirementDate: date):
        self.__retirementDate = retirementDate


    @property
    def serviceabilityCharacteristics(self):
        return self.__serviceabilityCharacteristics

    @serviceabilityCharacteristics.setter
    def serviceabilityCharacteristics(self, serviceabilityCharacteristics: str):
        self.__serviceabilityCharacteristics = serviceabilityCharacteristics


    @property
    def dateOfNextRelease(self):
        return self.__dateOfNextRelease

    @dateOfNextRelease.setter
    def dateOfNextRelease(self, dateOfNextRelease: date):
        self.__dateOfNextRelease = dateOfNextRelease


    @property
    def internationalizationCharacteristics(self):
        return self.__internationalizationCharacteristics

    @internationalizationCharacteristics.setter
    def internationalizationCharacteristics(self, internationalizationCharacteristics: str):
        self.__internationalizationCharacteristics = internationalizationCharacteristics


    @property
    def contentfwk_PhysicalApplicationComponent277(self):
        return self.__contentfwk_PhysicalApplicationComponent277

    @contentfwk_PhysicalApplicationComponent277.setter
    def contentfwk_PhysicalApplicationComponent277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent277", None)
        self.__contentfwk_PhysicalApplicationComponent277 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_PhysicalDataComponent278"):
                    opp_val = getattr(item, "contentfwk_PhysicalDataComponent278", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_PhysicalDataComponent278", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_PhysicalDataComponent278"):
                    opp_val = getattr(item, "contentfwk_PhysicalDataComponent278", None)
                    
                    setattr(item, "contentfwk_PhysicalDataComponent278", self)
                    

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
            if hasattr(old_value, "contentfwk_PhysicalTechnologyComponent181"):
                opp_val = getattr(old_value, "contentfwk_PhysicalTechnologyComponent181", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalTechnologyComponent181"):
                opp_val = getattr(value, "contentfwk_PhysicalTechnologyComponent181", None)
                if opp_val is None:
                    setattr(value, "contentfwk_PhysicalTechnologyComponent181", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_PhysicalApplicationComponent266(self):
        return self.__contentfwk_PhysicalApplicationComponent266

    @contentfwk_PhysicalApplicationComponent266.setter
    def contentfwk_PhysicalApplicationComponent266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent266", None)
        self.__contentfwk_PhysicalApplicationComponent266 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_ApplicationArchitecture265"):
                opp_val = getattr(old_value, "contentfwk_ApplicationArchitecture265", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_ApplicationArchitecture265"):
                opp_val = getattr(value, "contentfwk_ApplicationArchitecture265", None)
                if opp_val is None:
                    setattr(value, "contentfwk_ApplicationArchitecture265", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_PhysicalApplicationComponent273(self):
        return self.__contentfwk_PhysicalApplicationComponent273

    @contentfwk_PhysicalApplicationComponent273.setter
    def contentfwk_PhysicalApplicationComponent273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent273", None)
        self.__contentfwk_PhysicalApplicationComponent273 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_PhysicalApplicationComponent275"):
                    opp_val = getattr(item, "contentfwk_PhysicalApplicationComponent275", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_PhysicalApplicationComponent275", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_PhysicalApplicationComponent275"):
                    opp_val = getattr(item, "contentfwk_PhysicalApplicationComponent275", None)
                    
                    setattr(item, "contentfwk_PhysicalApplicationComponent275", self)
                    

    @property
    def PhysicalApplicationComponent240(self):
        return self.__PhysicalApplicationComponent240

    @PhysicalApplicationComponent240.setter
    def PhysicalApplicationComponent240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__PhysicalApplicationComponent240", None)
        self.__PhysicalApplicationComponent240 = value
        
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
    def contentfwk_PhysicalApplicationComponent284(self):
        return self.__contentfwk_PhysicalApplicationComponent284

    @contentfwk_PhysicalApplicationComponent284.setter
    def contentfwk_PhysicalApplicationComponent284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent284", None)
        self.__contentfwk_PhysicalApplicationComponent284 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalApplicationComponent282"):
                opp_val = getattr(old_value, "contentfwk_PhysicalApplicationComponent282", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_PhysicalApplicationComponent282", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalApplicationComponent282"):
                opp_val = getattr(value, "contentfwk_PhysicalApplicationComponent282", None)
                setattr(value, "contentfwk_PhysicalApplicationComponent282", self)

    @property
    def contentfwk_PhysicalApplicationComponent275(self):
        return self.__contentfwk_PhysicalApplicationComponent275

    @contentfwk_PhysicalApplicationComponent275.setter
    def contentfwk_PhysicalApplicationComponent275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent275", None)
        self.__contentfwk_PhysicalApplicationComponent275 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalApplicationComponent273"):
                opp_val = getattr(old_value, "contentfwk_PhysicalApplicationComponent273", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalApplicationComponent273"):
                opp_val = getattr(value, "contentfwk_PhysicalApplicationComponent273", None)
                if opp_val is None:
                    setattr(value, "contentfwk_PhysicalApplicationComponent273", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_PhysicalApplicationComponent261(self):
        return self.__contentfwk_PhysicalApplicationComponent261

    @contentfwk_PhysicalApplicationComponent261.setter
    def contentfwk_PhysicalApplicationComponent261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent261", None)
        self.__contentfwk_PhysicalApplicationComponent261 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalDataComponent260"):
                opp_val = getattr(old_value, "contentfwk_PhysicalDataComponent260", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalDataComponent260"):
                opp_val = getattr(value, "contentfwk_PhysicalDataComponent260", None)
                if opp_val is None:
                    setattr(value, "contentfwk_PhysicalDataComponent260", set([self]))
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
                if hasattr(item, "LogicalApplicationComponent270"):
                    opp_val = getattr(item, "LogicalApplicationComponent270", None)
                    
                    if opp_val == self:
                        setattr(item, "LogicalApplicationComponent270", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LogicalApplicationComponent270"):
                    opp_val = getattr(item, "LogicalApplicationComponent270", None)
                    
                    setattr(item, "LogicalApplicationComponent270", self)
                    

    @property
    def contentfwk_PhysicalApplicationComponent282(self):
        return self.__contentfwk_PhysicalApplicationComponent282

    @contentfwk_PhysicalApplicationComponent282.setter
    def contentfwk_PhysicalApplicationComponent282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent282", None)
        self.__contentfwk_PhysicalApplicationComponent282 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalApplicationComponent284"):
                opp_val = getattr(old_value, "contentfwk_PhysicalApplicationComponent284", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_PhysicalApplicationComponent284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalApplicationComponent284"):
                opp_val = getattr(value, "contentfwk_PhysicalApplicationComponent284", None)
                setattr(value, "contentfwk_PhysicalApplicationComponent284", self)

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
                if hasattr(item, "Location272"):
                    opp_val = getattr(item, "Location272", None)
                    
                    if opp_val == self:
                        setattr(item, "Location272", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Location272"):
                    opp_val = getattr(item, "Location272", None)
                    
                    setattr(item, "Location272", self)
                    

    @property
    def contentfwk_PhysicalApplicationComponent280(self):
        return self.__contentfwk_PhysicalApplicationComponent280

    @contentfwk_PhysicalApplicationComponent280.setter
    def contentfwk_PhysicalApplicationComponent280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent280", None)
        self.__contentfwk_PhysicalApplicationComponent280 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_PhysicalTechnologyComponent281"):
                    opp_val = getattr(item, "contentfwk_PhysicalTechnologyComponent281", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_PhysicalTechnologyComponent281", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_PhysicalTechnologyComponent281"):
                    opp_val = getattr(item, "contentfwk_PhysicalTechnologyComponent281", None)
                    
                    setattr(item, "contentfwk_PhysicalTechnologyComponent281", self)
                    

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

class contentfwk_StrategicElement(Element):

    pass
class contentfwk_LogicalTechnologyComponent(Element, TechnologyComponent):

    pass
class contentfwk_Service(Standard):

    pass
class contentfwk_Location(Element):

    pass
class contentfwk_Event(Element):

    pass
class contentfwk_Control(Element):

    pass
class contentfwk_Process(Standard, Element):

    def __init__(self, processCritiality: str, isAutomated: bool, processVolumetrics: str, contentfwk_Process: "contentfwk_BusinessArchitecture" = None, Process: "contentfwk_OrganizationUnit" = None, Process77: "contentfwk_Actor" = None, ensuresCorrectOperationOfProcesses: set["contentfwk_Control"] = None, isResolvedByProcesses: set["contentfwk_Event"] = None, isGeneratedByProcesses: set["contentfwk_Event"] = None, isProducedByProcesses: set["contentfwk_Product"] = None, contentfwk_Process172: "contentfwk_Process" = None, contentfwk_Process170: "contentfwk_Process" = None, Process175: "contentfwk_Process" = None, followsProcesses: set["contentfwk_Process"] = None, supportsProcesses: set["contentfwk_Function"] = None, participatesInProcesses: set["contentfwk_OrganizationUnit"] = None, isRealizedByProcesses155: set["contentfwk_Service"] = None, supportsProcesses158: set["contentfwk_Service"] = None, participatesInProcesses161: set["contentfwk_Actor"] = None, Process196: "contentfwk_Product" = None, Process178: "contentfwk_Process" = None, precedesProcesses: set["contentfwk_Process"] = None, isRealizedByProcesses: set["contentfwk_Function"] = None, Process132: "contentfwk_Function" = None, Process134: "contentfwk_Function" = None, Process215: "contentfwk_Event" = None, Process217: "contentfwk_Event" = None, Process225: "contentfwk_Control" = None, Process321: "contentfwk_Service" = None, Process323: "contentfwk_Service" = None):
        self.processCritiality = processCritiality
        self.isAutomated = isAutomated
        self.processVolumetrics = processVolumetrics
        self.contentfwk_Process = contentfwk_Process
        self.Process = Process
        self.Process77 = Process77
        self.ensuresCorrectOperationOfProcesses = ensuresCorrectOperationOfProcesses if ensuresCorrectOperationOfProcesses is not None else set()
        self.isResolvedByProcesses = isResolvedByProcesses if isResolvedByProcesses is not None else set()
        self.isGeneratedByProcesses = isGeneratedByProcesses if isGeneratedByProcesses is not None else set()
        self.isProducedByProcesses = isProducedByProcesses if isProducedByProcesses is not None else set()
        self.contentfwk_Process172 = contentfwk_Process172
        self.contentfwk_Process170 = contentfwk_Process170
        self.Process175 = Process175
        self.followsProcesses = followsProcesses if followsProcesses is not None else set()
        self.supportsProcesses = supportsProcesses if supportsProcesses is not None else set()
        self.participatesInProcesses = participatesInProcesses if participatesInProcesses is not None else set()
        self.isRealizedByProcesses155 = isRealizedByProcesses155 if isRealizedByProcesses155 is not None else set()
        self.supportsProcesses158 = supportsProcesses158 if supportsProcesses158 is not None else set()
        self.participatesInProcesses161 = participatesInProcesses161 if participatesInProcesses161 is not None else set()
        self.Process196 = Process196
        self.Process178 = Process178
        self.precedesProcesses = precedesProcesses if precedesProcesses is not None else set()
        self.isRealizedByProcesses = isRealizedByProcesses if isRealizedByProcesses is not None else set()
        self.Process132 = Process132
        self.Process134 = Process134
        self.Process215 = Process215
        self.Process217 = Process217
        self.Process225 = Process225
        self.Process321 = Process321
        self.Process323 = Process323
        
        pass
    @property
    def isAutomated(self):
        return self.__isAutomated

    @isAutomated.setter
    def isAutomated(self, isAutomated: bool):
        self.__isAutomated = isAutomated


    @property
    def processCritiality(self):
        return self.__processCritiality

    @processCritiality.setter
    def processCritiality(self, processCritiality: str):
        self.__processCritiality = processCritiality


    @property
    def processVolumetrics(self):
        return self.__processVolumetrics

    @processVolumetrics.setter
    def processVolumetrics(self, processVolumetrics: str):
        self.__processVolumetrics = processVolumetrics


    @property
    def Process196(self):
        return self.__Process196

    @Process196.setter
    def Process196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process196", None)
        self.__Process196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "producesProducts195"):
                opp_val = getattr(old_value, "producesProducts195", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "producesProducts195"):
                opp_val = getattr(value, "producesProducts195", None)
                if opp_val is None:
                    setattr(value, "producesProducts195", set([self]))
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
    def Process178(self):
        return self.__Process178

    @Process178.setter
    def Process178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process178", None)
        self.__Process178 = value
        
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
    def contentfwk_Process170(self):
        return self.__contentfwk_Process170

    @contentfwk_Process170.setter
    def contentfwk_Process170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__contentfwk_Process170", None)
        self.__contentfwk_Process170 = value
        
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
    def Process215(self):
        return self.__Process215

    @Process215.setter
    def Process215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process215", None)
        self.__Process215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resolvesEvents214"):
                opp_val = getattr(old_value, "resolvesEvents214", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resolvesEvents214"):
                opp_val = getattr(value, "resolvesEvents214", None)
                if opp_val is None:
                    setattr(value, "resolvesEvents214", set([self]))
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
                if hasattr(item, "Process178"):
                    opp_val = getattr(item, "Process178", None)
                    
                    if opp_val == self:
                        setattr(item, "Process178", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Process178"):
                    opp_val = getattr(item, "Process178", None)
                    
                    setattr(item, "Process178", self)
                    

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
    def Process225(self):
        return self.__Process225

    @Process225.setter
    def Process225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process225", None)
        self.__Process225 = value
        
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
    def Process217(self):
        return self.__Process217

    @Process217.setter
    def Process217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process217", None)
        self.__Process217 = value
        
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
    def supportsProcesses158(self):
        return self.__supportsProcesses158

    @supportsProcesses158.setter
    def supportsProcesses158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__supportsProcesses158", None)
        self.__supportsProcesses158 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service159"):
                    opp_val = getattr(item, "Service159", None)
                    
                    if opp_val == self:
                        setattr(item, "Service159", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service159"):
                    opp_val = getattr(item, "Service159", None)
                    
                    setattr(item, "Service159", self)
                    

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
                if hasattr(item, "Process175"):
                    opp_val = getattr(item, "Process175", None)
                    
                    if opp_val == self:
                        setattr(item, "Process175", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Process175"):
                    opp_val = getattr(item, "Process175", None)
                    
                    setattr(item, "Process175", self)
                    

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
                if hasattr(item, "Function149"):
                    opp_val = getattr(item, "Function149", None)
                    
                    if opp_val == self:
                        setattr(item, "Function149", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function149"):
                    opp_val = getattr(item, "Function149", None)
                    
                    setattr(item, "Function149", self)
                    

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
            if hasattr(old_value, "contentfwk_Process170"):
                opp_val = getattr(old_value, "contentfwk_Process170", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_Process170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_Process170"):
                opp_val = getattr(value, "contentfwk_Process170", None)
                setattr(value, "contentfwk_Process170", self)

    @property
    def Process321(self):
        return self.__Process321

    @Process321.setter
    def Process321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process321", None)
        self.__Process321 = value
        
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
                if hasattr(item, "Product169"):
                    opp_val = getattr(item, "Product169", None)
                    
                    if opp_val == self:
                        setattr(item, "Product169", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Product169"):
                    opp_val = getattr(item, "Product169", None)
                    
                    setattr(item, "Product169", self)
                    

    @property
    def Process175(self):
        return self.__Process175

    @Process175.setter
    def Process175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process175", None)
        self.__Process175 = value
        
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
    def isRealizedByProcesses155(self):
        return self.__isRealizedByProcesses155

    @isRealizedByProcesses155.setter
    def isRealizedByProcesses155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__isRealizedByProcesses155", None)
        self.__isRealizedByProcesses155 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service156"):
                    opp_val = getattr(item, "Service156", None)
                    
                    if opp_val == self:
                        setattr(item, "Service156", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service156"):
                    opp_val = getattr(item, "Service156", None)
                    
                    setattr(item, "Service156", self)
                    

    @property
    def Process323(self):
        return self.__Process323

    @Process323.setter
    def Process323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process323", None)
        self.__Process323 = value
        
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
    def Process134(self):
        return self.__Process134

    @Process134.setter
    def Process134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process134", None)
        self.__Process134 = value
        
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
    def participatesInProcesses161(self):
        return self.__participatesInProcesses161

    @participatesInProcesses161.setter
    def participatesInProcesses161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__participatesInProcesses161", None)
        self.__participatesInProcesses161 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Actor162"):
                    opp_val = getattr(item, "Actor162", None)
                    
                    if opp_val == self:
                        setattr(item, "Actor162", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Actor162"):
                    opp_val = getattr(item, "Actor162", None)
                    
                    setattr(item, "Actor162", self)
                    

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
                if hasattr(item, "Event165"):
                    opp_val = getattr(item, "Event165", None)
                    
                    if opp_val == self:
                        setattr(item, "Event165", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Event165"):
                    opp_val = getattr(item, "Event165", None)
                    
                    setattr(item, "Event165", self)
                    

    @property
    def Process132(self):
        return self.__Process132

    @Process132.setter
    def Process132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process132", None)
        self.__Process132 = value
        
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
    def Process77(self):
        return self.__Process77

    @Process77.setter
    def Process77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Process__Process77", None)
        self.__Process77 = value
        
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
                if hasattr(item, "OrganizationUnit153"):
                    opp_val = getattr(item, "OrganizationUnit153", None)
                    
                    if opp_val == self:
                        setattr(item, "OrganizationUnit153", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OrganizationUnit153"):
                    opp_val = getattr(item, "OrganizationUnit153", None)
                    
                    setattr(item, "OrganizationUnit153", self)
                    

class contentfwk_BusinessService(Element, Service):

    pass
class contentfwk_Function(Standard, Element):

    pass
class contentfwk_Role(Element):

    def __init__(self, estimatedFTEs: str, contentfwk_Role: "contentfwk_BusinessArchitecture" = None, performsTaskInRoles: set["contentfwk_Actor"] = None, canBeAccessedByRoles: set["contentfwk_Function"] = None, contentfwk_Role97: "contentfwk_Role" = None, contentfwk_Role95: "contentfwk_Role" = None, Role: "contentfwk_Actor" = None, Role136: "contentfwk_Function" = None):
        self.estimatedFTEs = estimatedFTEs
        self.contentfwk_Role = contentfwk_Role
        self.performsTaskInRoles = performsTaskInRoles if performsTaskInRoles is not None else set()
        self.canBeAccessedByRoles = canBeAccessedByRoles if canBeAccessedByRoles is not None else set()
        self.contentfwk_Role97 = contentfwk_Role97
        self.contentfwk_Role95 = contentfwk_Role95
        self.Role = Role
        self.Role136 = Role136
        
        pass
    @property
    def estimatedFTEs(self):
        return self.__estimatedFTEs

    @estimatedFTEs.setter
    def estimatedFTEs(self, estimatedFTEs: str):
        self.__estimatedFTEs = estimatedFTEs


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
                if hasattr(item, "Function94"):
                    opp_val = getattr(item, "Function94", None)
                    
                    if opp_val == self:
                        setattr(item, "Function94", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function94"):
                    opp_val = getattr(item, "Function94", None)
                    
                    setattr(item, "Function94", self)
                    

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
    def contentfwk_Role95(self):
        return self.__contentfwk_Role95

    @contentfwk_Role95.setter
    def contentfwk_Role95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Role__contentfwk_Role95", None)
        self.__contentfwk_Role95 = value
        
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
                if hasattr(item, "Actor92"):
                    opp_val = getattr(item, "Actor92", None)
                    
                    if opp_val == self:
                        setattr(item, "Actor92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Actor92"):
                    opp_val = getattr(item, "Actor92", None)
                    
                    setattr(item, "Actor92", self)
                    

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
            if hasattr(old_value, "contentfwk_Role95"):
                opp_val = getattr(old_value, "contentfwk_Role95", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_Role95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_Role95"):
                opp_val = getattr(value, "contentfwk_Role95", None)
                setattr(value, "contentfwk_Role95", self)

    @property
    def Role136(self):
        return self.__Role136

    @Role136.setter
    def Role136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Role__Role136", None)
        self.__Role136 = value
        
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

class contentfwk_PhysicalTechnologyComponent(Element, TechnologyComponent):

    def __init__(self, productName: str, moduleName: str, vendor: str, version: str, contentfwk_PhysicalTechnologyComponent: "contentfwk_TechnologyArchitecture" = None, contentfwk_PhysicalTechnologyComponent188: "contentfwk_PhysicalTechnologyComponent" = None, contentfwk_PhysicalTechnologyComponent186: "contentfwk_PhysicalTechnologyComponent" = None, contentfwk_PhysicalTechnologyComponent191: "contentfwk_PhysicalTechnologyComponent" = None, contentfwk_PhysicalTechnologyComponent189: set["contentfwk_PhysicalTechnologyComponent"] = None, PhysicalTechnologyComponent: "contentfwk_Location" = None, contentfwk_PhysicalTechnologyComponent181: set["contentfwk_PhysicalApplicationComponent"] = None, isRealizedByPhysicalTechnologyComponents: set["contentfwk_LogicalTechnologyComponent"] = None, containsPhysicalTechnologyComponents: set["contentfwk_Location"] = None, PhysicalTechnologyComponent289: "contentfwk_LogicalTechnologyComponent" = None, contentfwk_PhysicalTechnologyComponent281: "contentfwk_PhysicalApplicationComponent" = None):
        self.productName = productName
        self.moduleName = moduleName
        self.vendor = vendor
        self.version = version
        self.contentfwk_PhysicalTechnologyComponent = contentfwk_PhysicalTechnologyComponent
        self.contentfwk_PhysicalTechnologyComponent188 = contentfwk_PhysicalTechnologyComponent188
        self.contentfwk_PhysicalTechnologyComponent186 = contentfwk_PhysicalTechnologyComponent186
        self.contentfwk_PhysicalTechnologyComponent191 = contentfwk_PhysicalTechnologyComponent191
        self.contentfwk_PhysicalTechnologyComponent189 = contentfwk_PhysicalTechnologyComponent189 if contentfwk_PhysicalTechnologyComponent189 is not None else set()
        self.PhysicalTechnologyComponent = PhysicalTechnologyComponent
        self.contentfwk_PhysicalTechnologyComponent181 = contentfwk_PhysicalTechnologyComponent181 if contentfwk_PhysicalTechnologyComponent181 is not None else set()
        self.isRealizedByPhysicalTechnologyComponents = isRealizedByPhysicalTechnologyComponents if isRealizedByPhysicalTechnologyComponents is not None else set()
        self.containsPhysicalTechnologyComponents = containsPhysicalTechnologyComponents if containsPhysicalTechnologyComponents is not None else set()
        self.PhysicalTechnologyComponent289 = PhysicalTechnologyComponent289
        self.contentfwk_PhysicalTechnologyComponent281 = contentfwk_PhysicalTechnologyComponent281
        
        pass
    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def productName(self):
        return self.__productName

    @productName.setter
    def productName(self, productName: str):
        self.__productName = productName


    @property
    def moduleName(self):
        return self.__moduleName

    @moduleName.setter
    def moduleName(self, moduleName: str):
        self.__moduleName = moduleName


    @property
    def vendor(self):
        return self.__vendor

    @vendor.setter
    def vendor(self, vendor: str):
        self.__vendor = vendor


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
            if hasattr(old_value, "contentfwk_PhysicalTechnologyComponent186"):
                opp_val = getattr(old_value, "contentfwk_PhysicalTechnologyComponent186", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_PhysicalTechnologyComponent186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalTechnologyComponent186"):
                opp_val = getattr(value, "contentfwk_PhysicalTechnologyComponent186", None)
                setattr(value, "contentfwk_PhysicalTechnologyComponent186", self)

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
                if hasattr(item, "Location185"):
                    opp_val = getattr(item, "Location185", None)
                    
                    if opp_val == self:
                        setattr(item, "Location185", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Location185"):
                    opp_val = getattr(item, "Location185", None)
                    
                    setattr(item, "Location185", self)
                    

    @property
    def PhysicalTechnologyComponent289(self):
        return self.__PhysicalTechnologyComponent289

    @PhysicalTechnologyComponent289.setter
    def PhysicalTechnologyComponent289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__PhysicalTechnologyComponent289", None)
        self.__PhysicalTechnologyComponent289 = value
        
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
    def contentfwk_PhysicalTechnologyComponent281(self):
        return self.__contentfwk_PhysicalTechnologyComponent281

    @contentfwk_PhysicalTechnologyComponent281.setter
    def contentfwk_PhysicalTechnologyComponent281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent281", None)
        self.__contentfwk_PhysicalTechnologyComponent281 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalApplicationComponent280"):
                opp_val = getattr(old_value, "contentfwk_PhysicalApplicationComponent280", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalApplicationComponent280"):
                opp_val = getattr(value, "contentfwk_PhysicalApplicationComponent280", None)
                if opp_val is None:
                    setattr(value, "contentfwk_PhysicalApplicationComponent280", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_PhysicalTechnologyComponent181(self):
        return self.__contentfwk_PhysicalTechnologyComponent181

    @contentfwk_PhysicalTechnologyComponent181.setter
    def contentfwk_PhysicalTechnologyComponent181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent181", None)
        self.__contentfwk_PhysicalTechnologyComponent181 = value if value is not None else set()
        
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
    def contentfwk_PhysicalTechnologyComponent191(self):
        return self.__contentfwk_PhysicalTechnologyComponent191

    @contentfwk_PhysicalTechnologyComponent191.setter
    def contentfwk_PhysicalTechnologyComponent191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent191", None)
        self.__contentfwk_PhysicalTechnologyComponent191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_PhysicalTechnologyComponent189"):
                opp_val = getattr(old_value, "contentfwk_PhysicalTechnologyComponent189", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_PhysicalTechnologyComponent189"):
                opp_val = getattr(value, "contentfwk_PhysicalTechnologyComponent189", None)
                if opp_val is None:
                    setattr(value, "contentfwk_PhysicalTechnologyComponent189", set([self]))
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
                if hasattr(item, "LogicalTechnologyComponent183"):
                    opp_val = getattr(item, "LogicalTechnologyComponent183", None)
                    
                    if opp_val == self:
                        setattr(item, "LogicalTechnologyComponent183", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LogicalTechnologyComponent183"):
                    opp_val = getattr(item, "LogicalTechnologyComponent183", None)
                    
                    setattr(item, "LogicalTechnologyComponent183", self)
                    

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

    @property
    def contentfwk_PhysicalTechnologyComponent189(self):
        return self.__contentfwk_PhysicalTechnologyComponent189

    @contentfwk_PhysicalTechnologyComponent189.setter
    def contentfwk_PhysicalTechnologyComponent189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent189", None)
        self.__contentfwk_PhysicalTechnologyComponent189 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_PhysicalTechnologyComponent191"):
                    opp_val = getattr(item, "contentfwk_PhysicalTechnologyComponent191", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_PhysicalTechnologyComponent191", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_PhysicalTechnologyComponent191"):
                    opp_val = getattr(item, "contentfwk_PhysicalTechnologyComponent191", None)
                    
                    setattr(item, "contentfwk_PhysicalTechnologyComponent191", self)
                    

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
            if hasattr(old_value, "isHostedInLocation242"):
                opp_val = getattr(old_value, "isHostedInLocation242", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isHostedInLocation242"):
                opp_val = getattr(value, "isHostedInLocation242", None)
                if opp_val is None:
                    setattr(value, "isHostedInLocation242", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_PhysicalTechnologyComponent186(self):
        return self.__contentfwk_PhysicalTechnologyComponent186

    @contentfwk_PhysicalTechnologyComponent186.setter
    def contentfwk_PhysicalTechnologyComponent186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent186", None)
        self.__contentfwk_PhysicalTechnologyComponent186 = value
        
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

class contentfwk_PlatformService(Element, Service):

    pass
class contentfwk_PhysicalDataComponent(Element, DataComponent):

    pass
class contentfwk_LogicalDataComponent(Element, DataComponent):

    pass
class contentfwk_DataEntity(Element):

    def __init__(self, dataEntityCategory: str, privacyClassification: str, retentionClassification: str, contentfwk_DataEntity: "contentfwk_DataArchitecture" = None, DataEntity: "contentfwk_Actor" = None, DataEntity70: "contentfwk_Actor" = None, suppliesEntities: set["contentfwk_Actor"] = None, consumesEntities: set["contentfwk_Actor"] = None, consumesEntities103: set["contentfwk_Service"] = None, providesEntities: set["contentfwk_Service"] = None, encapsulatesDataEntities: "contentfwk_LogicalDataComponent" = None, operatesOnDataEntities: set["contentfwk_LogicalApplicationComponent"] = None, contentfwk_DataEntity111: "contentfwk_DataEntity" = None, contentfwk_DataEntity109: "contentfwk_DataEntity" = None, contentfwk_DataEntity114: "contentfwk_DataEntity" = None, contentfwk_DataEntity112: set["contentfwk_DataEntity"] = None, DataEntity118: "contentfwk_LogicalApplicationComponent" = None, DataEntity249: "contentfwk_LogicalDataComponent" = None, DataEntity305: "contentfwk_Service" = None, DataEntity307: "contentfwk_Service" = None):
        self.dataEntityCategory = dataEntityCategory
        self.privacyClassification = privacyClassification
        self.retentionClassification = retentionClassification
        self.contentfwk_DataEntity = contentfwk_DataEntity
        self.DataEntity = DataEntity
        self.DataEntity70 = DataEntity70
        self.suppliesEntities = suppliesEntities if suppliesEntities is not None else set()
        self.consumesEntities = consumesEntities if consumesEntities is not None else set()
        self.consumesEntities103 = consumesEntities103 if consumesEntities103 is not None else set()
        self.providesEntities = providesEntities if providesEntities is not None else set()
        self.encapsulatesDataEntities = encapsulatesDataEntities
        self.operatesOnDataEntities = operatesOnDataEntities if operatesOnDataEntities is not None else set()
        self.contentfwk_DataEntity111 = contentfwk_DataEntity111
        self.contentfwk_DataEntity109 = contentfwk_DataEntity109
        self.contentfwk_DataEntity114 = contentfwk_DataEntity114
        self.contentfwk_DataEntity112 = contentfwk_DataEntity112 if contentfwk_DataEntity112 is not None else set()
        self.DataEntity118 = DataEntity118
        self.DataEntity249 = DataEntity249
        self.DataEntity305 = DataEntity305
        self.DataEntity307 = DataEntity307
        
        pass
    @property
    def dataEntityCategory(self):
        return self.__dataEntityCategory

    @dataEntityCategory.setter
    def dataEntityCategory(self, dataEntityCategory: str):
        self.__dataEntityCategory = dataEntityCategory


    @property
    def privacyClassification(self):
        return self.__privacyClassification

    @privacyClassification.setter
    def privacyClassification(self, privacyClassification: str):
        self.__privacyClassification = privacyClassification


    @property
    def retentionClassification(self):
        return self.__retentionClassification

    @retentionClassification.setter
    def retentionClassification(self, retentionClassification: str):
        self.__retentionClassification = retentionClassification


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
    def DataEntity70(self):
        return self.__DataEntity70

    @DataEntity70.setter
    def DataEntity70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__DataEntity70", None)
        self.__DataEntity70 = value
        
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
    def contentfwk_DataEntity111(self):
        return self.__contentfwk_DataEntity111

    @contentfwk_DataEntity111.setter
    def contentfwk_DataEntity111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__contentfwk_DataEntity111", None)
        self.__contentfwk_DataEntity111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_DataEntity109"):
                opp_val = getattr(old_value, "contentfwk_DataEntity109", None)
                if opp_val == self:
                    setattr(old_value, "contentfwk_DataEntity109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_DataEntity109"):
                opp_val = getattr(value, "contentfwk_DataEntity109", None)
                setattr(value, "contentfwk_DataEntity109", self)

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
    def DataEntity118(self):
        return self.__DataEntity118

    @DataEntity118.setter
    def DataEntity118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__DataEntity118", None)
        self.__DataEntity118 = value
        
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
    def consumesEntities103(self):
        return self.__consumesEntities103

    @consumesEntities103.setter
    def consumesEntities103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__consumesEntities103", None)
        self.__consumesEntities103 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service104"):
                    opp_val = getattr(item, "Service104", None)
                    
                    if opp_val == self:
                        setattr(item, "Service104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service104"):
                    opp_val = getattr(item, "Service104", None)
                    
                    setattr(item, "Service104", self)
                    

    @property
    def contentfwk_DataEntity112(self):
        return self.__contentfwk_DataEntity112

    @contentfwk_DataEntity112.setter
    def contentfwk_DataEntity112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__contentfwk_DataEntity112", None)
        self.__contentfwk_DataEntity112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_DataEntity114"):
                    opp_val = getattr(item, "contentfwk_DataEntity114", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_DataEntity114", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_DataEntity114"):
                    opp_val = getattr(item, "contentfwk_DataEntity114", None)
                    
                    setattr(item, "contentfwk_DataEntity114", self)
                    

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
    def contentfwk_DataEntity114(self):
        return self.__contentfwk_DataEntity114

    @contentfwk_DataEntity114.setter
    def contentfwk_DataEntity114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__contentfwk_DataEntity114", None)
        self.__contentfwk_DataEntity114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_DataEntity112"):
                opp_val = getattr(old_value, "contentfwk_DataEntity112", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_DataEntity112"):
                opp_val = getattr(value, "contentfwk_DataEntity112", None)
                if opp_val is None:
                    setattr(value, "contentfwk_DataEntity112", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DataEntity307(self):
        return self.__DataEntity307

    @DataEntity307.setter
    def DataEntity307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__DataEntity307", None)
        self.__DataEntity307 = value
        
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
    def contentfwk_DataEntity109(self):
        return self.__contentfwk_DataEntity109

    @contentfwk_DataEntity109.setter
    def contentfwk_DataEntity109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__contentfwk_DataEntity109", None)
        self.__contentfwk_DataEntity109 = value
        
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
    def DataEntity305(self):
        return self.__DataEntity305

    @DataEntity305.setter
    def DataEntity305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__DataEntity305", None)
        self.__DataEntity305 = value
        
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
                if hasattr(item, "Actor99"):
                    opp_val = getattr(item, "Actor99", None)
                    
                    if opp_val == self:
                        setattr(item, "Actor99", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Actor99"):
                    opp_val = getattr(item, "Actor99", None)
                    
                    setattr(item, "Actor99", self)
                    

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
    def DataEntity249(self):
        return self.__DataEntity249

    @DataEntity249.setter
    def DataEntity249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_DataEntity__DataEntity249", None)
        self.__DataEntity249 = value
        
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

class contentfwk_ServiceQuality(Element):

    pass
class contentfwk_Measure(Element):

    pass
class contentfwk_Contract(Element):

    def __init__(self, ServiceNameCalled: str, serviceQualityCharacteristics: str, availabilityQualityCharacteristics: str, servicesTimes: str, manageabilityCharacteristics: str, serviceabilityCharacteristics: str, performanceCharacteristics: str, responseCharacteristics: str, reliabilityCharacteristics: str, qualityOfInformationRequired: str, contractControlRequirements: str, resultControlRequirements: str, recoverabilityCharacteristics: str, locatabilityCharacteristics: str, securityCharacteristics: str, privacyCharacteristics: str, behaviorCharacteristics: str, ServiceNameCaller: str, peakProfileShortTerm: str, peakProfileLongTerm: str, integrityCharacteristics: str, credibilityCharacteristics: str, localizationCharacteristics: str, internationalizationCharacteristics: str, interoperabilityCharacteristics: str, scalabilityCharacteristics: str, portabilityCharacteristics: str, extensibilityCharacteristics: str, capacityCharacteristics: str, throughput: str, throughputPeriod: str, growth: str, growthPeriod: str, contentfwk_Contract: "contentfwk_BusinessArchitecture" = None, Contract: "contentfwk_ServiceQuality" = None, isGovernedAndMeasuredByContracts: set["contentfwk_Service"] = None, appliesToContracts: set["contentfwk_ServiceQuality"] = None, Contract309: "contentfwk_Service" = None):
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
        self.behaviorCharacteristics = behaviorCharacteristics
        self.ServiceNameCaller = ServiceNameCaller
        self.peakProfileShortTerm = peakProfileShortTerm
        self.peakProfileLongTerm = peakProfileLongTerm
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
        self.contentfwk_Contract = contentfwk_Contract
        self.Contract = Contract
        self.isGovernedAndMeasuredByContracts = isGovernedAndMeasuredByContracts if isGovernedAndMeasuredByContracts is not None else set()
        self.appliesToContracts = appliesToContracts if appliesToContracts is not None else set()
        self.Contract309 = Contract309
        
        pass
    @property
    def peakProfileLongTerm(self):
        return self.__peakProfileLongTerm

    @peakProfileLongTerm.setter
    def peakProfileLongTerm(self, peakProfileLongTerm: str):
        self.__peakProfileLongTerm = peakProfileLongTerm


    @property
    def internationalizationCharacteristics(self):
        return self.__internationalizationCharacteristics

    @internationalizationCharacteristics.setter
    def internationalizationCharacteristics(self, internationalizationCharacteristics: str):
        self.__internationalizationCharacteristics = internationalizationCharacteristics


    @property
    def privacyCharacteristics(self):
        return self.__privacyCharacteristics

    @privacyCharacteristics.setter
    def privacyCharacteristics(self, privacyCharacteristics: str):
        self.__privacyCharacteristics = privacyCharacteristics


    @property
    def throughput(self):
        return self.__throughput

    @throughput.setter
    def throughput(self, throughput: str):
        self.__throughput = throughput


    @property
    def securityCharacteristics(self):
        return self.__securityCharacteristics

    @securityCharacteristics.setter
    def securityCharacteristics(self, securityCharacteristics: str):
        self.__securityCharacteristics = securityCharacteristics


    @property
    def contractControlRequirements(self):
        return self.__contractControlRequirements

    @contractControlRequirements.setter
    def contractControlRequirements(self, contractControlRequirements: str):
        self.__contractControlRequirements = contractControlRequirements


    @property
    def serviceabilityCharacteristics(self):
        return self.__serviceabilityCharacteristics

    @serviceabilityCharacteristics.setter
    def serviceabilityCharacteristics(self, serviceabilityCharacteristics: str):
        self.__serviceabilityCharacteristics = serviceabilityCharacteristics


    @property
    def availabilityQualityCharacteristics(self):
        return self.__availabilityQualityCharacteristics

    @availabilityQualityCharacteristics.setter
    def availabilityQualityCharacteristics(self, availabilityQualityCharacteristics: str):
        self.__availabilityQualityCharacteristics = availabilityQualityCharacteristics


    @property
    def recoverabilityCharacteristics(self):
        return self.__recoverabilityCharacteristics

    @recoverabilityCharacteristics.setter
    def recoverabilityCharacteristics(self, recoverabilityCharacteristics: str):
        self.__recoverabilityCharacteristics = recoverabilityCharacteristics


    @property
    def peakProfileShortTerm(self):
        return self.__peakProfileShortTerm

    @peakProfileShortTerm.setter
    def peakProfileShortTerm(self, peakProfileShortTerm: str):
        self.__peakProfileShortTerm = peakProfileShortTerm


    @property
    def credibilityCharacteristics(self):
        return self.__credibilityCharacteristics

    @credibilityCharacteristics.setter
    def credibilityCharacteristics(self, credibilityCharacteristics: str):
        self.__credibilityCharacteristics = credibilityCharacteristics


    @property
    def resultControlRequirements(self):
        return self.__resultControlRequirements

    @resultControlRequirements.setter
    def resultControlRequirements(self, resultControlRequirements: str):
        self.__resultControlRequirements = resultControlRequirements


    @property
    def qualityOfInformationRequired(self):
        return self.__qualityOfInformationRequired

    @qualityOfInformationRequired.setter
    def qualityOfInformationRequired(self, qualityOfInformationRequired: str):
        self.__qualityOfInformationRequired = qualityOfInformationRequired


    @property
    def extensibilityCharacteristics(self):
        return self.__extensibilityCharacteristics

    @extensibilityCharacteristics.setter
    def extensibilityCharacteristics(self, extensibilityCharacteristics: str):
        self.__extensibilityCharacteristics = extensibilityCharacteristics


    @property
    def capacityCharacteristics(self):
        return self.__capacityCharacteristics

    @capacityCharacteristics.setter
    def capacityCharacteristics(self, capacityCharacteristics: str):
        self.__capacityCharacteristics = capacityCharacteristics


    @property
    def growthPeriod(self):
        return self.__growthPeriod

    @growthPeriod.setter
    def growthPeriod(self, growthPeriod: str):
        self.__growthPeriod = growthPeriod


    @property
    def reliabilityCharacteristics(self):
        return self.__reliabilityCharacteristics

    @reliabilityCharacteristics.setter
    def reliabilityCharacteristics(self, reliabilityCharacteristics: str):
        self.__reliabilityCharacteristics = reliabilityCharacteristics


    @property
    def locatabilityCharacteristics(self):
        return self.__locatabilityCharacteristics

    @locatabilityCharacteristics.setter
    def locatabilityCharacteristics(self, locatabilityCharacteristics: str):
        self.__locatabilityCharacteristics = locatabilityCharacteristics


    @property
    def scalabilityCharacteristics(self):
        return self.__scalabilityCharacteristics

    @scalabilityCharacteristics.setter
    def scalabilityCharacteristics(self, scalabilityCharacteristics: str):
        self.__scalabilityCharacteristics = scalabilityCharacteristics


    @property
    def behaviorCharacteristics(self):
        return self.__behaviorCharacteristics

    @behaviorCharacteristics.setter
    def behaviorCharacteristics(self, behaviorCharacteristics: str):
        self.__behaviorCharacteristics = behaviorCharacteristics


    @property
    def localizationCharacteristics(self):
        return self.__localizationCharacteristics

    @localizationCharacteristics.setter
    def localizationCharacteristics(self, localizationCharacteristics: str):
        self.__localizationCharacteristics = localizationCharacteristics


    @property
    def growth(self):
        return self.__growth

    @growth.setter
    def growth(self, growth: str):
        self.__growth = growth


    @property
    def servicesTimes(self):
        return self.__servicesTimes

    @servicesTimes.setter
    def servicesTimes(self, servicesTimes: str):
        self.__servicesTimes = servicesTimes


    @property
    def manageabilityCharacteristics(self):
        return self.__manageabilityCharacteristics

    @manageabilityCharacteristics.setter
    def manageabilityCharacteristics(self, manageabilityCharacteristics: str):
        self.__manageabilityCharacteristics = manageabilityCharacteristics


    @property
    def ServiceNameCalled(self):
        return self.__ServiceNameCalled

    @ServiceNameCalled.setter
    def ServiceNameCalled(self, ServiceNameCalled: str):
        self.__ServiceNameCalled = ServiceNameCalled


    @property
    def serviceQualityCharacteristics(self):
        return self.__serviceQualityCharacteristics

    @serviceQualityCharacteristics.setter
    def serviceQualityCharacteristics(self, serviceQualityCharacteristics: str):
        self.__serviceQualityCharacteristics = serviceQualityCharacteristics


    @property
    def throughputPeriod(self):
        return self.__throughputPeriod

    @throughputPeriod.setter
    def throughputPeriod(self, throughputPeriod: str):
        self.__throughputPeriod = throughputPeriod


    @property
    def interoperabilityCharacteristics(self):
        return self.__interoperabilityCharacteristics

    @interoperabilityCharacteristics.setter
    def interoperabilityCharacteristics(self, interoperabilityCharacteristics: str):
        self.__interoperabilityCharacteristics = interoperabilityCharacteristics


    @property
    def integrityCharacteristics(self):
        return self.__integrityCharacteristics

    @integrityCharacteristics.setter
    def integrityCharacteristics(self, integrityCharacteristics: str):
        self.__integrityCharacteristics = integrityCharacteristics


    @property
    def performanceCharacteristics(self):
        return self.__performanceCharacteristics

    @performanceCharacteristics.setter
    def performanceCharacteristics(self, performanceCharacteristics: str):
        self.__performanceCharacteristics = performanceCharacteristics


    @property
    def ServiceNameCaller(self):
        return self.__ServiceNameCaller

    @ServiceNameCaller.setter
    def ServiceNameCaller(self, ServiceNameCaller: str):
        self.__ServiceNameCaller = ServiceNameCaller


    @property
    def portabilityCharacteristics(self):
        return self.__portabilityCharacteristics

    @portabilityCharacteristics.setter
    def portabilityCharacteristics(self, portabilityCharacteristics: str):
        self.__portabilityCharacteristics = portabilityCharacteristics


    @property
    def responseCharacteristics(self):
        return self.__responseCharacteristics

    @responseCharacteristics.setter
    def responseCharacteristics(self, responseCharacteristics: str):
        self.__responseCharacteristics = responseCharacteristics


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
                if hasattr(item, "Service209"):
                    opp_val = getattr(item, "Service209", None)
                    
                    if opp_val == self:
                        setattr(item, "Service209", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service209"):
                    opp_val = getattr(item, "Service209", None)
                    
                    setattr(item, "Service209", self)
                    

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

    @property
    def Contract309(self):
        return self.__Contract309

    @Contract309.setter
    def Contract309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Contract__Contract309", None)
        self.__Contract309 = value
        
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
                    

class contentfwk_Product(Element):

    pass
class contentfwk_Architecture(ABC):

    pass
class contentfwk_EnterpriseArchitecture:

    pass
class contentfwk_Actor(Element):

    def __init__(self, FTEs: str, actorGoal: str, actorTasks: str, contentfwk_Actor: "contentfwk_BusinessArchitecture" = None, Actor: "contentfwk_OrganizationUnit" = None, isResolvedByActors: set["contentfwk_Event"] = None, isGeneratedByActors: set["contentfwk_Event"] = None, containsActors84: "contentfwk_Location" = None, isPerformedByActors: set["contentfwk_Function"] = None, isSuppliedByActors: set["contentfwk_DataEntity"] = None, isConsumedByActors: set["contentfwk_DataEntity"] = None, containsActors: "contentfwk_OrganizationUnit" = None, Actor99: "contentfwk_DataEntity" = None, Actor101: "contentfwk_DataEntity" = None, contentfwk_Actor90: "contentfwk_Actor" = None, contentfwk_Actor88: set["contentfwk_Actor"] = None, Actor92: "contentfwk_Role" = None, Actor126: "contentfwk_Function" = None, supportsActors: set["contentfwk_Function"] = None, isAssumedByActors: set["contentfwk_Role"] = None, involvesActors: set["contentfwk_Process"] = None, contentfwk_Actor79: set["contentfwk_Service"] = None, Actor138: "contentfwk_Function" = None, Actor162: "contentfwk_Process" = None, Actor220: "contentfwk_Event" = None, Actor223: "contentfwk_Event" = None, Actor234: "contentfwk_Location" = None, contentfwk_Actor301: "contentfwk_Service" = None):
        self.FTEs = FTEs
        self.actorGoal = actorGoal
        self.actorTasks = actorTasks
        self.contentfwk_Actor = contentfwk_Actor
        self.Actor = Actor
        self.isResolvedByActors = isResolvedByActors if isResolvedByActors is not None else set()
        self.isGeneratedByActors = isGeneratedByActors if isGeneratedByActors is not None else set()
        self.containsActors84 = containsActors84
        self.isPerformedByActors = isPerformedByActors if isPerformedByActors is not None else set()
        self.isSuppliedByActors = isSuppliedByActors if isSuppliedByActors is not None else set()
        self.isConsumedByActors = isConsumedByActors if isConsumedByActors is not None else set()
        self.containsActors = containsActors
        self.Actor99 = Actor99
        self.Actor101 = Actor101
        self.contentfwk_Actor90 = contentfwk_Actor90
        self.contentfwk_Actor88 = contentfwk_Actor88 if contentfwk_Actor88 is not None else set()
        self.Actor92 = Actor92
        self.Actor126 = Actor126
        self.supportsActors = supportsActors if supportsActors is not None else set()
        self.isAssumedByActors = isAssumedByActors if isAssumedByActors is not None else set()
        self.involvesActors = involvesActors if involvesActors is not None else set()
        self.contentfwk_Actor79 = contentfwk_Actor79 if contentfwk_Actor79 is not None else set()
        self.Actor138 = Actor138
        self.Actor162 = Actor162
        self.Actor220 = Actor220
        self.Actor223 = Actor223
        self.Actor234 = Actor234
        self.contentfwk_Actor301 = contentfwk_Actor301
        
        pass
    @property
    def FTEs(self):
        return self.__FTEs

    @FTEs.setter
    def FTEs(self, FTEs: str):
        self.__FTEs = FTEs


    @property
    def actorGoal(self):
        return self.__actorGoal

    @actorGoal.setter
    def actorGoal(self, actorGoal: str):
        self.__actorGoal = actorGoal


    @property
    def actorTasks(self):
        return self.__actorTasks

    @actorTasks.setter
    def actorTasks(self, actorTasks: str):
        self.__actorTasks = actorTasks


    @property
    def containsActors84(self):
        return self.__containsActors84

    @containsActors84.setter
    def containsActors84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__containsActors84", None)
        self.__containsActors84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Location85"):
                opp_val = getattr(old_value, "Location85", None)
                if opp_val == self:
                    setattr(old_value, "Location85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Location85"):
                opp_val = getattr(value, "Location85", None)
                setattr(value, "Location85", self)

    @property
    def Actor223(self):
        return self.__Actor223

    @Actor223.setter
    def Actor223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor223", None)
        self.__Actor223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generatesEvents222"):
                opp_val = getattr(old_value, "generatesEvents222", None)
                if opp_val == self:
                    setattr(old_value, "generatesEvents222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generatesEvents222"):
                opp_val = getattr(value, "generatesEvents222", None)
                setattr(value, "generatesEvents222", self)

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
    def containsActors(self):
        return self.__containsActors

    @containsActors.setter
    def containsActors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__containsActors", None)
        self.__containsActors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OrganizationUnit72"):
                opp_val = getattr(old_value, "OrganizationUnit72", None)
                if opp_val == self:
                    setattr(old_value, "OrganizationUnit72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OrganizationUnit72"):
                opp_val = getattr(value, "OrganizationUnit72", None)
                setattr(value, "OrganizationUnit72", self)

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
                if hasattr(item, "Function74"):
                    opp_val = getattr(item, "Function74", None)
                    
                    if opp_val == self:
                        setattr(item, "Function74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function74"):
                    opp_val = getattr(item, "Function74", None)
                    
                    setattr(item, "Function74", self)
                    

    @property
    def Actor126(self):
        return self.__Actor126

    @Actor126.setter
    def Actor126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor126", None)
        self.__Actor126 = value
        
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
    def Actor92(self):
        return self.__Actor92

    @Actor92.setter
    def Actor92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor92", None)
        self.__Actor92 = value
        
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
                if hasattr(item, "DataEntity70"):
                    opp_val = getattr(item, "DataEntity70", None)
                    
                    if opp_val == self:
                        setattr(item, "DataEntity70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataEntity70"):
                    opp_val = getattr(item, "DataEntity70", None)
                    
                    setattr(item, "DataEntity70", self)
                    

    @property
    def Actor220(self):
        return self.__Actor220

    @Actor220.setter
    def Actor220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor220", None)
        self.__Actor220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resolvesEvents219"):
                opp_val = getattr(old_value, "resolvesEvents219", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resolvesEvents219"):
                opp_val = getattr(value, "resolvesEvents219", None)
                if opp_val is None:
                    setattr(value, "resolvesEvents219", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "Event82"):
                    opp_val = getattr(item, "Event82", None)
                    
                    if opp_val == self:
                        setattr(item, "Event82", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Event82"):
                    opp_val = getattr(item, "Event82", None)
                    
                    setattr(item, "Event82", self)
                    

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
    def Actor234(self):
        return self.__Actor234

    @Actor234.setter
    def Actor234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor234", None)
        self.__Actor234 = value
        
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
    def contentfwk_Actor301(self):
        return self.__contentfwk_Actor301

    @contentfwk_Actor301.setter
    def contentfwk_Actor301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__contentfwk_Actor301", None)
        self.__contentfwk_Actor301 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_Service300"):
                opp_val = getattr(old_value, "contentfwk_Service300", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_Service300"):
                opp_val = getattr(value, "contentfwk_Service300", None)
                if opp_val is None:
                    setattr(value, "contentfwk_Service300", set([self]))
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
    def Actor99(self):
        return self.__Actor99

    @Actor99.setter
    def Actor99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor99", None)
        self.__Actor99 = value
        
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
    def contentfwk_Actor79(self):
        return self.__contentfwk_Actor79

    @contentfwk_Actor79.setter
    def contentfwk_Actor79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__contentfwk_Actor79", None)
        self.__contentfwk_Actor79 = value if value is not None else set()
        
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
    def Actor138(self):
        return self.__Actor138

    @Actor138.setter
    def Actor138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor138", None)
        self.__Actor138 = value
        
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
    def Actor162(self):
        return self.__Actor162

    @Actor162.setter
    def Actor162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__Actor162", None)
        self.__Actor162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "participatesInProcesses161"):
                opp_val = getattr(old_value, "participatesInProcesses161", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "participatesInProcesses161"):
                opp_val = getattr(value, "participatesInProcesses161", None)
                if opp_val is None:
                    setattr(value, "participatesInProcesses161", set([self]))
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
                if hasattr(item, "Process77"):
                    opp_val = getattr(item, "Process77", None)
                    
                    if opp_val == self:
                        setattr(item, "Process77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Process77"):
                    opp_val = getattr(item, "Process77", None)
                    
                    setattr(item, "Process77", self)
                    

    @property
    def contentfwk_Actor90(self):
        return self.__contentfwk_Actor90

    @contentfwk_Actor90.setter
    def contentfwk_Actor90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__contentfwk_Actor90", None)
        self.__contentfwk_Actor90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentfwk_Actor88"):
                opp_val = getattr(old_value, "contentfwk_Actor88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentfwk_Actor88"):
                opp_val = getattr(value, "contentfwk_Actor88", None)
                if opp_val is None:
                    setattr(value, "contentfwk_Actor88", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentfwk_Actor88(self):
        return self.__contentfwk_Actor88

    @contentfwk_Actor88.setter
    def contentfwk_Actor88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Actor__contentfwk_Actor88", None)
        self.__contentfwk_Actor88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentfwk_Actor90"):
                    opp_val = getattr(item, "contentfwk_Actor90", None)
                    
                    if opp_val == self:
                        setattr(item, "contentfwk_Actor90", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentfwk_Actor90"):
                    opp_val = getattr(item, "contentfwk_Actor90", None)
                    
                    setattr(item, "contentfwk_Actor90", self)
                    

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
                if hasattr(item, "Function87"):
                    opp_val = getattr(item, "Function87", None)
                    
                    if opp_val == self:
                        setattr(item, "Function87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function87"):
                    opp_val = getattr(item, "Function87", None)
                    
                    setattr(item, "Function87", self)
                    

class contentfwk_OrganizationUnit(Element):

    def __init__(self, headcount: str, isOwnedAndGovernedByOrganizationUnits: set["contentfwk_Service"] = None, belongsTo: set["contentfwk_Actor"] = None, isOwnedByUnit: set["contentfwk_Function"] = None, involvesOrganizationUnits: set["contentfwk_Process"] = None, motivatesOrganizationUnits: set["contentfwk_Driver"] = None, contentfwk_OrganizationUnit: "contentfwk_BusinessArchitecture" = None, isProducedByOrganizationUnits: set["contentfwk_Product"] = None, containsOrganizationUnits: "contentfwk_Location" = None, OrganizationUnit72: "contentfwk_Actor" = None, OrganizationUnit: "contentfwk_Driver" = None, OrganizationUnit153: "contentfwk_Process" = None, OrganizationUnit193: "contentfwk_Product" = None, OrganizationUnit128: "contentfwk_Function" = None, OrganizationUnit237: "contentfwk_Location" = None, OrganizationUnit317: "contentfwk_Service" = None):
        self.headcount = headcount
        self.isOwnedAndGovernedByOrganizationUnits = isOwnedAndGovernedByOrganizationUnits if isOwnedAndGovernedByOrganizationUnits is not None else set()
        self.belongsTo = belongsTo if belongsTo is not None else set()
        self.isOwnedByUnit = isOwnedByUnit if isOwnedByUnit is not None else set()
        self.involvesOrganizationUnits = involvesOrganizationUnits if involvesOrganizationUnits is not None else set()
        self.motivatesOrganizationUnits = motivatesOrganizationUnits if motivatesOrganizationUnits is not None else set()
        self.contentfwk_OrganizationUnit = contentfwk_OrganizationUnit
        self.isProducedByOrganizationUnits = isProducedByOrganizationUnits if isProducedByOrganizationUnits is not None else set()
        self.containsOrganizationUnits = containsOrganizationUnits
        self.OrganizationUnit72 = OrganizationUnit72
        self.OrganizationUnit = OrganizationUnit
        self.OrganizationUnit153 = OrganizationUnit153
        self.OrganizationUnit193 = OrganizationUnit193
        self.OrganizationUnit128 = OrganizationUnit128
        self.OrganizationUnit237 = OrganizationUnit237
        self.OrganizationUnit317 = OrganizationUnit317
        
        pass
    @property
    def headcount(self):
        return self.__headcount

    @headcount.setter
    def headcount(self, headcount: str):
        self.__headcount = headcount


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
    def OrganizationUnit193(self):
        return self.__OrganizationUnit193

    @OrganizationUnit193.setter
    def OrganizationUnit193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit193", None)
        self.__OrganizationUnit193 = value
        
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
    def OrganizationUnit128(self):
        return self.__OrganizationUnit128

    @OrganizationUnit128.setter
    def OrganizationUnit128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit128", None)
        self.__OrganizationUnit128 = value
        
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
                if hasattr(item, "Driver65"):
                    opp_val = getattr(item, "Driver65", None)
                    
                    if opp_val == self:
                        setattr(item, "Driver65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Driver65"):
                    opp_val = getattr(item, "Driver65", None)
                    
                    setattr(item, "Driver65", self)
                    

    @property
    def OrganizationUnit237(self):
        return self.__OrganizationUnit237

    @OrganizationUnit237.setter
    def OrganizationUnit237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit237", None)
        self.__OrganizationUnit237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operatesInLocation236"):
                opp_val = getattr(old_value, "operatesInLocation236", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operatesInLocation236"):
                opp_val = getattr(value, "operatesInLocation236", None)
                if opp_val is None:
                    setattr(value, "operatesInLocation236", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OrganizationUnit317(self):
        return self.__OrganizationUnit317

    @OrganizationUnit317.setter
    def OrganizationUnit317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit317", None)
        self.__OrganizationUnit317 = value
        
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
    def OrganizationUnit153(self):
        return self.__OrganizationUnit153

    @OrganizationUnit153.setter
    def OrganizationUnit153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit153", None)
        self.__OrganizationUnit153 = value
        
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
    def OrganizationUnit72(self):
        return self.__OrganizationUnit72

    @OrganizationUnit72.setter
    def OrganizationUnit72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_OrganizationUnit__OrganizationUnit72", None)
        self.__OrganizationUnit72 = value
        
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
class contentfwk_StrategicArchitecture(Architecture):

    pass
class contentfwk_TechnologyArchitecture(Architecture):

    pass
class contentfwk_ApplicationArchitecture(Architecture):

    pass
class contentfwk_BusinessArchitecture(Architecture):

    pass
class contentfwk_Container:

    def __init__(self, name: str, contentfwk_Container: "contentfwk_EnterpriseArchitecture" = None, contentfwk_Container232: set["contentfwk_Element"] = None):
        self.name = name
        self.contentfwk_Container = contentfwk_Container
        self.contentfwk_Container232 = contentfwk_Container232 if contentfwk_Container232 is not None else set()
        
        pass
    @property
    def name(self):
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
    def contentfwk_Container232(self):
        return self.__contentfwk_Container232

    @contentfwk_Container232.setter
    def contentfwk_Container232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contentfwk_Container__contentfwk_Container232", None)
        self.__contentfwk_Container232 = value if value is not None else set()
        
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
                    
