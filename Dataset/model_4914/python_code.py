from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class UsageStateType(Enum):
    Assigned = "Assigned"
    Reserved = "Reserved"
    Free = "Free"
    Disabled = "Disabled"
class MaintenanceType(Enum):
    _1stLineMaintenance = "_1stLineMaintenance"
    _2ndLineMaintenance = "_2ndLineMaintenance"
class LifeCycleStateType(Enum):
    Planned = "Planned"
    Active = "Active"
    Removed = "Removed"
class ServiceKindType(Enum):
    RFS = "RFS"
    CFS = "CFS"
class ServiceClassType(Enum):
    Sold = "Sold"
    Silver = "Silver"
    Bronze = "Bronze"
class SecurityRatingType(Enum):
    High = "High"
    Medium = "Medium"
    Low = "Low"
class InterrestKindType(Enum):
    Escallation = "Escallation"
    Reporting = "Reporting"
    SalesManagement = "SalesManagement"
    ProductManagement = "ProductManagement"
    FinancialManagement = "FinancialManagement"
    ServiceManagement = "ServiceManagement"


############################################
# Definition of Classes
############################################

class services_Parameter:

    pass
class services_ServiceSecurityMgt:

    def __init__(self, drPlanContact: str, drPlanRepository: str, drRecoveryPlan: str, securityRating: str, services_ServiceSecurityMgt: "services_Service" = None):
        self.drPlanContact = drPlanContact
        self.drPlanRepository = drPlanRepository
        self.drRecoveryPlan = drRecoveryPlan
        self.securityRating = securityRating
        self.services_ServiceSecurityMgt = services_ServiceSecurityMgt
        
    @property
    def drPlanContact(self) -> str:
        return self.__drPlanContact

    @drPlanContact.setter
    def drPlanContact(self, drPlanContact: str):
        self.__drPlanContact = drPlanContact

    @property
    def drPlanRepository(self) -> str:
        return self.__drPlanRepository

    @drPlanRepository.setter
    def drPlanRepository(self, drPlanRepository: str):
        self.__drPlanRepository = drPlanRepository

    @property
    def securityRating(self) -> str:
        return self.__securityRating

    @securityRating.setter
    def securityRating(self, securityRating: str):
        self.__securityRating = securityRating

    @property
    def drRecoveryPlan(self) -> str:
        return self.__drRecoveryPlan

    @drRecoveryPlan.setter
    def drRecoveryPlan(self, drRecoveryPlan: str):
        self.__drRecoveryPlan = drRecoveryPlan

    @property
    def services_ServiceSecurityMgt(self):
        return self.__services_ServiceSecurityMgt

    @services_ServiceSecurityMgt.setter
    def services_ServiceSecurityMgt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceSecurityMgt__services_ServiceSecurityMgt", None)
        self.__services_ServiceSecurityMgt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_Service9"):
                opp_val = getattr(old_value, "services_Service9", None)
                if opp_val == self:
                    setattr(old_value, "services_Service9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_Service9"):
                opp_val = getattr(value, "services_Service9", None)
                setattr(value, "services_Service9", self)

class services_ServiceAdditional:

    def __init__(self, costCenter: str, history: str, kpi: str, lifeCycleState: str, link: str, report: str, usageState: str, services_ServiceAdditional: "services_Service" = None):
        self.costCenter = costCenter
        self.history = history
        self.kpi = kpi
        self.lifeCycleState = lifeCycleState
        self.link = link
        self.report = report
        self.usageState = usageState
        self.services_ServiceAdditional = services_ServiceAdditional
        
    @property
    def costCenter(self) -> str:
        return self.__costCenter

    @costCenter.setter
    def costCenter(self, costCenter: str):
        self.__costCenter = costCenter

    @property
    def history(self) -> str:
        return self.__history

    @history.setter
    def history(self, history: str):
        self.__history = history

    @property
    def kpi(self) -> str:
        return self.__kpi

    @kpi.setter
    def kpi(self, kpi: str):
        self.__kpi = kpi

    @property
    def usageState(self) -> str:
        return self.__usageState

    @usageState.setter
    def usageState(self, usageState: str):
        self.__usageState = usageState

    @property
    def link(self) -> str:
        return self.__link

    @link.setter
    def link(self, link: str):
        self.__link = link

    @property
    def report(self) -> str:
        return self.__report

    @report.setter
    def report(self, report: str):
        self.__report = report

    @property
    def lifeCycleState(self) -> str:
        return self.__lifeCycleState

    @lifeCycleState.setter
    def lifeCycleState(self, lifeCycleState: str):
        self.__lifeCycleState = lifeCycleState

    @property
    def services_ServiceAdditional(self):
        return self.__services_ServiceAdditional

    @services_ServiceAdditional.setter
    def services_ServiceAdditional(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceAdditional__services_ServiceAdditional", None)
        self.__services_ServiceAdditional = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_Service21"):
                opp_val = getattr(old_value, "services_Service21", None)
                if opp_val == self:
                    setattr(old_value, "services_Service21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_Service21"):
                opp_val = getattr(value, "services_Service21", None)
                setattr(value, "services_Service21", self)

class services_ServiceSupport:

    def __init__(self, supportDays: str, supportHours: str, services_ServiceSupport: "services_Service" = None):
        self.supportDays = supportDays
        self.supportHours = supportHours
        self.services_ServiceSupport = services_ServiceSupport
        
    @property
    def supportHours(self) -> str:
        return self.__supportHours

    @supportHours.setter
    def supportHours(self, supportHours: str):
        self.__supportHours = supportHours

    @property
    def supportDays(self) -> str:
        return self.__supportDays

    @supportDays.setter
    def supportDays(self, supportDays: str):
        self.__supportDays = supportDays

    @property
    def services_ServiceSupport(self):
        return self.__services_ServiceSupport

    @services_ServiceSupport.setter
    def services_ServiceSupport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceSupport__services_ServiceSupport", None)
        self.__services_ServiceSupport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_Service19"):
                opp_val = getattr(old_value, "services_Service19", None)
                if opp_val == self:
                    setattr(old_value, "services_Service19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_Service19"):
                opp_val = getattr(value, "services_Service19", None)
                setattr(value, "services_Service19", self)

class services_ServiceContract:

    def __init__(self, oLA: str, sLA: str, uC: str, wLA: str, services_ServiceContract: "services_Service" = None):
        self.oLA = oLA
        self.sLA = sLA
        self.uC = uC
        self.wLA = wLA
        self.services_ServiceContract = services_ServiceContract
        
    @property
    def uC(self) -> str:
        return self.__uC

    @uC.setter
    def uC(self, uC: str):
        self.__uC = uC

    @property
    def wLA(self) -> str:
        return self.__wLA

    @wLA.setter
    def wLA(self, wLA: str):
        self.__wLA = wLA

    @property
    def sLA(self) -> str:
        return self.__sLA

    @sLA.setter
    def sLA(self, sLA: str):
        self.__sLA = sLA

    @property
    def oLA(self) -> str:
        return self.__oLA

    @oLA.setter
    def oLA(self, oLA: str):
        self.__oLA = oLA

    @property
    def services_ServiceContract(self):
        return self.__services_ServiceContract

    @services_ServiceContract.setter
    def services_ServiceContract(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceContract__services_ServiceContract", None)
        self.__services_ServiceContract = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_Service17"):
                opp_val = getattr(old_value, "services_Service17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_Service17"):
                opp_val = getattr(value, "services_Service17", None)
                if opp_val is None:
                    setattr(value, "services_Service17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class services_ServiceInterrest:

    def __init__(self, contactUnit: str, interrestKind: str, services_ServiceInterrest: "services_Service" = None):
        self.contactUnit = contactUnit
        self.interrestKind = interrestKind
        self.services_ServiceInterrest = services_ServiceInterrest
        
    @property
    def interrestKind(self) -> str:
        return self.__interrestKind

    @interrestKind.setter
    def interrestKind(self, interrestKind: str):
        self.__interrestKind = interrestKind

    @property
    def contactUnit(self) -> str:
        return self.__contactUnit

    @contactUnit.setter
    def contactUnit(self, contactUnit: str):
        self.__contactUnit = contactUnit

    @property
    def services_ServiceInterrest(self):
        return self.__services_ServiceInterrest

    @services_ServiceInterrest.setter
    def services_ServiceInterrest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceInterrest__services_ServiceInterrest", None)
        self.__services_ServiceInterrest = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_Service15"):
                opp_val = getattr(old_value, "services_Service15", None)
                if opp_val == self:
                    setattr(old_value, "services_Service15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_Service15"):
                opp_val = getattr(value, "services_Service15", None)
                setattr(value, "services_Service15", self)

class services_ServiceIncidentMgt:

    def __init__(self, businessImpact: str, maintenance: str, maintenanceWindow: str, monitoring: str, services_ServiceIncidentMgt: "services_Service" = None):
        self.businessImpact = businessImpact
        self.maintenance = maintenance
        self.maintenanceWindow = maintenanceWindow
        self.monitoring = monitoring
        self.services_ServiceIncidentMgt = services_ServiceIncidentMgt
        
    @property
    def businessImpact(self) -> str:
        return self.__businessImpact

    @businessImpact.setter
    def businessImpact(self, businessImpact: str):
        self.__businessImpact = businessImpact

    @property
    def maintenance(self) -> str:
        return self.__maintenance

    @maintenance.setter
    def maintenance(self, maintenance: str):
        self.__maintenance = maintenance

    @property
    def monitoring(self) -> str:
        return self.__monitoring

    @monitoring.setter
    def monitoring(self, monitoring: str):
        self.__monitoring = monitoring

    @property
    def maintenanceWindow(self) -> str:
        return self.__maintenanceWindow

    @maintenanceWindow.setter
    def maintenanceWindow(self, maintenanceWindow: str):
        self.__maintenanceWindow = maintenanceWindow

    @property
    def services_ServiceIncidentMgt(self):
        return self.__services_ServiceIncidentMgt

    @services_ServiceIncidentMgt.setter
    def services_ServiceIncidentMgt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceIncidentMgt__services_ServiceIncidentMgt", None)
        self.__services_ServiceIncidentMgt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_Service11"):
                opp_val = getattr(old_value, "services_Service11", None)
                if opp_val == self:
                    setattr(old_value, "services_Service11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_Service11"):
                opp_val = getattr(value, "services_Service11", None)
                setattr(value, "services_Service11", self)

class services_ServiceDescription:

    def __init__(self, serviceDescriptionCommon: str, serviceDescriptionNational: str, services_ServiceDescription: "services_Service" = None):
        self.serviceDescriptionCommon = serviceDescriptionCommon
        self.serviceDescriptionNational = serviceDescriptionNational
        self.services_ServiceDescription = services_ServiceDescription
        
    @property
    def serviceDescriptionNational(self) -> str:
        return self.__serviceDescriptionNational

    @serviceDescriptionNational.setter
    def serviceDescriptionNational(self, serviceDescriptionNational: str):
        self.__serviceDescriptionNational = serviceDescriptionNational

    @property
    def serviceDescriptionCommon(self) -> str:
        return self.__serviceDescriptionCommon

    @serviceDescriptionCommon.setter
    def serviceDescriptionCommon(self, serviceDescriptionCommon: str):
        self.__serviceDescriptionCommon = serviceDescriptionCommon

    @property
    def services_ServiceDescription(self):
        return self.__services_ServiceDescription

    @services_ServiceDescription.setter
    def services_ServiceDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceDescription__services_ServiceDescription", None)
        self.__services_ServiceDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_Service7"):
                opp_val = getattr(old_value, "services_Service7", None)
                if opp_val == self:
                    setattr(old_value, "services_Service7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_Service7"):
                opp_val = getattr(value, "services_Service7", None)
                setattr(value, "services_Service7", self)

class services_ServiceName:

    def __init__(self, alias: str, identifier: str, index: str, name: str, services_ServiceName: "services_Service" = None):
        self.alias = alias
        self.identifier = identifier
        self.index = index
        self.name = name
        self.services_ServiceName = services_ServiceName
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def index(self) -> str:
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def services_ServiceName(self):
        return self.__services_ServiceName

    @services_ServiceName.setter
    def services_ServiceName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceName__services_ServiceName", None)
        self.__services_ServiceName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_Service"):
                opp_val = getattr(old_value, "services_Service", None)
                if opp_val == self:
                    setattr(old_value, "services_Service", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_Service"):
                opp_val = getattr(value, "services_Service", None)
                setattr(value, "services_Service", self)

class services_Service:

    def __init__(self, mostTopService: str, serviceCategory: str, serviceCharacterCommon: str, serviceClass: str, serviceKind: str, serviceSupport1: str, ssDomain: str, services_Service: "services_ServiceName" = None, services_Service7: "services_ServiceDescription" = None, services_Service9: "services_ServiceSecurityMgt" = None, services_Service11: "services_ServiceIncidentMgt" = None, services_Service13: "services_CIID" = None, services_Service15: "services_ServiceInterrest" = None, services_Service17: set["services_ServiceContract"] = None, services_Service19: "services_ServiceSupport" = None, services_Service21: "services_ServiceAdditional" = None, services_Service24: "services_Service" = None, services_Service22: set["services_Service"] = None):
        self.mostTopService = mostTopService
        self.serviceCategory = serviceCategory
        self.serviceCharacterCommon = serviceCharacterCommon
        self.serviceClass = serviceClass
        self.serviceKind = serviceKind
        self.serviceSupport1 = serviceSupport1
        self.ssDomain = ssDomain
        self.services_Service = services_Service
        self.services_Service7 = services_Service7
        self.services_Service9 = services_Service9
        self.services_Service11 = services_Service11
        self.services_Service13 = services_Service13
        self.services_Service15 = services_Service15
        self.services_Service17 = services_Service17 if services_Service17 is not None else set()
        self.services_Service19 = services_Service19
        self.services_Service21 = services_Service21
        self.services_Service24 = services_Service24
        self.services_Service22 = services_Service22 if services_Service22 is not None else set()
        
    @property
    def serviceKind(self) -> str:
        return self.__serviceKind

    @serviceKind.setter
    def serviceKind(self, serviceKind: str):
        self.__serviceKind = serviceKind

    @property
    def serviceSupport1(self) -> str:
        return self.__serviceSupport1

    @serviceSupport1.setter
    def serviceSupport1(self, serviceSupport1: str):
        self.__serviceSupport1 = serviceSupport1

    @property
    def serviceCategory(self) -> str:
        return self.__serviceCategory

    @serviceCategory.setter
    def serviceCategory(self, serviceCategory: str):
        self.__serviceCategory = serviceCategory

    @property
    def serviceClass(self) -> str:
        return self.__serviceClass

    @serviceClass.setter
    def serviceClass(self, serviceClass: str):
        self.__serviceClass = serviceClass

    @property
    def ssDomain(self) -> str:
        return self.__ssDomain

    @ssDomain.setter
    def ssDomain(self, ssDomain: str):
        self.__ssDomain = ssDomain

    @property
    def serviceCharacterCommon(self) -> str:
        return self.__serviceCharacterCommon

    @serviceCharacterCommon.setter
    def serviceCharacterCommon(self, serviceCharacterCommon: str):
        self.__serviceCharacterCommon = serviceCharacterCommon

    @property
    def mostTopService(self) -> str:
        return self.__mostTopService

    @mostTopService.setter
    def mostTopService(self, mostTopService: str):
        self.__mostTopService = mostTopService

    @property
    def services_Service11(self):
        return self.__services_Service11

    @services_Service11.setter
    def services_Service11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service11", None)
        self.__services_Service11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_ServiceIncidentMgt"):
                opp_val = getattr(old_value, "services_ServiceIncidentMgt", None)
                if opp_val == self:
                    setattr(old_value, "services_ServiceIncidentMgt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_ServiceIncidentMgt"):
                opp_val = getattr(value, "services_ServiceIncidentMgt", None)
                setattr(value, "services_ServiceIncidentMgt", self)

    @property
    def services_Service7(self):
        return self.__services_Service7

    @services_Service7.setter
    def services_Service7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service7", None)
        self.__services_Service7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_ServiceDescription"):
                opp_val = getattr(old_value, "services_ServiceDescription", None)
                if opp_val == self:
                    setattr(old_value, "services_ServiceDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_ServiceDescription"):
                opp_val = getattr(value, "services_ServiceDescription", None)
                setattr(value, "services_ServiceDescription", self)

    @property
    def services_Service13(self):
        return self.__services_Service13

    @services_Service13.setter
    def services_Service13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service13", None)
        self.__services_Service13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_CIID"):
                opp_val = getattr(old_value, "services_CIID", None)
                if opp_val == self:
                    setattr(old_value, "services_CIID", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_CIID"):
                opp_val = getattr(value, "services_CIID", None)
                setattr(value, "services_CIID", self)

    @property
    def services_Service17(self):
        return self.__services_Service17

    @services_Service17.setter
    def services_Service17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service17", None)
        self.__services_Service17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "services_ServiceContract"):
                    opp_val = getattr(item, "services_ServiceContract", None)
                    
                    if opp_val == self:
                        setattr(item, "services_ServiceContract", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "services_ServiceContract"):
                    opp_val = getattr(item, "services_ServiceContract", None)
                    
                    setattr(item, "services_ServiceContract", self)
                    

    @property
    def services_Service15(self):
        return self.__services_Service15

    @services_Service15.setter
    def services_Service15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service15", None)
        self.__services_Service15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_ServiceInterrest"):
                opp_val = getattr(old_value, "services_ServiceInterrest", None)
                if opp_val == self:
                    setattr(old_value, "services_ServiceInterrest", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_ServiceInterrest"):
                opp_val = getattr(value, "services_ServiceInterrest", None)
                setattr(value, "services_ServiceInterrest", self)

    @property
    def services_Service19(self):
        return self.__services_Service19

    @services_Service19.setter
    def services_Service19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service19", None)
        self.__services_Service19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_ServiceSupport"):
                opp_val = getattr(old_value, "services_ServiceSupport", None)
                if opp_val == self:
                    setattr(old_value, "services_ServiceSupport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_ServiceSupport"):
                opp_val = getattr(value, "services_ServiceSupport", None)
                setattr(value, "services_ServiceSupport", self)

    @property
    def services_Service22(self):
        return self.__services_Service22

    @services_Service22.setter
    def services_Service22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service22", None)
        self.__services_Service22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "services_Service24"):
                    opp_val = getattr(item, "services_Service24", None)
                    
                    if opp_val == self:
                        setattr(item, "services_Service24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "services_Service24"):
                    opp_val = getattr(item, "services_Service24", None)
                    
                    setattr(item, "services_Service24", self)
                    

    @property
    def services_Service(self):
        return self.__services_Service

    @services_Service.setter
    def services_Service(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service", None)
        self.__services_Service = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_ServiceName"):
                opp_val = getattr(old_value, "services_ServiceName", None)
                if opp_val == self:
                    setattr(old_value, "services_ServiceName", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_ServiceName"):
                opp_val = getattr(value, "services_ServiceName", None)
                setattr(value, "services_ServiceName", self)

    @property
    def services_Service9(self):
        return self.__services_Service9

    @services_Service9.setter
    def services_Service9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service9", None)
        self.__services_Service9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_ServiceSecurityMgt"):
                opp_val = getattr(old_value, "services_ServiceSecurityMgt", None)
                if opp_val == self:
                    setattr(old_value, "services_ServiceSecurityMgt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_ServiceSecurityMgt"):
                opp_val = getattr(value, "services_ServiceSecurityMgt", None)
                setattr(value, "services_ServiceSecurityMgt", self)

    @property
    def services_Service24(self):
        return self.__services_Service24

    @services_Service24.setter
    def services_Service24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service24", None)
        self.__services_Service24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_Service22"):
                opp_val = getattr(old_value, "services_Service22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_Service22"):
                opp_val = getattr(value, "services_Service22", None)
                if opp_val is None:
                    setattr(value, "services_Service22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def services_Service21(self):
        return self.__services_Service21

    @services_Service21.setter
    def services_Service21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service21", None)
        self.__services_Service21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_ServiceAdditional"):
                opp_val = getattr(old_value, "services_ServiceAdditional", None)
                if opp_val == self:
                    setattr(old_value, "services_ServiceAdditional", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_ServiceAdditional"):
                opp_val = getattr(value, "services_ServiceAdditional", None)
                setattr(value, "services_ServiceAdditional", self)

class services_ServiceProfile:

    def __init__(self, name: str, services_ServiceProfile: "services_RFSService" = None, services_ServiceProfile26: set["services_Parameter"] = None):
        self.name = name
        self.services_ServiceProfile = services_ServiceProfile
        self.services_ServiceProfile26 = services_ServiceProfile26 if services_ServiceProfile26 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def services_ServiceProfile(self):
        return self.__services_ServiceProfile

    @services_ServiceProfile.setter
    def services_ServiceProfile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceProfile__services_ServiceProfile", None)
        self.__services_ServiceProfile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_RFSService4"):
                opp_val = getattr(old_value, "services_RFSService4", None)
                if opp_val == self:
                    setattr(old_value, "services_RFSService4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_RFSService4"):
                opp_val = getattr(value, "services_RFSService4", None)
                setattr(value, "services_RFSService4", self)

    @property
    def services_ServiceProfile26(self):
        return self.__services_ServiceProfile26

    @services_ServiceProfile26.setter
    def services_ServiceProfile26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceProfile__services_ServiceProfile26", None)
        self.__services_ServiceProfile26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "services_Parameter"):
                    opp_val = getattr(item, "services_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "services_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "services_Parameter"):
                    opp_val = getattr(item, "services_Parameter", None)
                    
                    setattr(item, "services_Parameter", self)
                    

class services_CIID:

    def __init__(self, commonCIID: str, localCIID: str, services_CIID: "services_Service" = None):
        self.commonCIID = commonCIID
        self.localCIID = localCIID
        self.services_CIID = services_CIID
        
    @property
    def commonCIID(self) -> str:
        return self.__commonCIID

    @commonCIID.setter
    def commonCIID(self, commonCIID: str):
        self.__commonCIID = commonCIID

    @property
    def localCIID(self) -> str:
        return self.__localCIID

    @localCIID.setter
    def localCIID(self, localCIID: str):
        self.__localCIID = localCIID

    @property
    def services_CIID(self):
        return self.__services_CIID

    @services_CIID.setter
    def services_CIID(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_CIID__services_CIID", None)
        self.__services_CIID = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_Service13"):
                opp_val = getattr(old_value, "services_Service13", None)
                if opp_val == self:
                    setattr(old_value, "services_Service13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_Service13"):
                opp_val = getattr(value, "services_Service13", None)
                setattr(value, "services_Service13", self)

class services_EObject:

    pass
class Service:

    pass
class services_RFSService(Service):

    def __init__(self, functionalCategory: str, location: str, services_RFSService4: "services_ServiceProfile" = None, services_RFSService: set["services_EObject"] = None):
        self.functionalCategory = functionalCategory
        self.location = location
        self.services_RFSService4 = services_RFSService4
        self.services_RFSService = services_RFSService if services_RFSService is not None else set()
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def functionalCategory(self) -> str:
        return self.__functionalCategory

    @functionalCategory.setter
    def functionalCategory(self, functionalCategory: str):
        self.__functionalCategory = functionalCategory

    @property
    def services_RFSService4(self):
        return self.__services_RFSService4

    @services_RFSService4.setter
    def services_RFSService4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_RFSService__services_RFSService4", None)
        self.__services_RFSService4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_ServiceProfile"):
                opp_val = getattr(old_value, "services_ServiceProfile", None)
                if opp_val == self:
                    setattr(old_value, "services_ServiceProfile", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_ServiceProfile"):
                opp_val = getattr(value, "services_ServiceProfile", None)
                setattr(value, "services_ServiceProfile", self)

    @property
    def services_RFSService(self):
        return self.__services_RFSService

    @services_RFSService.setter
    def services_RFSService(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_RFSService__services_RFSService", None)
        self.__services_RFSService = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "services_EObject2"):
                    opp_val = getattr(item, "services_EObject2", None)
                    
                    if opp_val == self:
                        setattr(item, "services_EObject2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "services_EObject2"):
                    opp_val = getattr(item, "services_EObject2", None)
                    
                    setattr(item, "services_EObject2", self)
                    

class services_CFSService(Service):

    def __init__(self, provider: str, scenario: str, services_CFSService: set["services_EObject"] = None):
        self.provider = provider
        self.scenario = scenario
        self.services_CFSService = services_CFSService if services_CFSService is not None else set()
        
    @property
    def provider(self) -> str:
        return self.__provider

    @provider.setter
    def provider(self, provider: str):
        self.__provider = provider

    @property
    def scenario(self) -> str:
        return self.__scenario

    @scenario.setter
    def scenario(self, scenario: str):
        self.__scenario = scenario

    @property
    def services_CFSService(self):
        return self.__services_CFSService

    @services_CFSService.setter
    def services_CFSService(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_CFSService__services_CFSService", None)
        self.__services_CFSService = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "services_EObject"):
                    opp_val = getattr(item, "services_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "services_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "services_EObject"):
                    opp_val = getattr(item, "services_EObject", None)
                    
                    setattr(item, "services_EObject", self)
                    
