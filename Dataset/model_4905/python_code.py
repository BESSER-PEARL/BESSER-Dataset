from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ServiceClassType(Enum):
    Gold = "Gold"
    Silver = "Silver"
    Bronze = "Bronze"


############################################
# Definition of Classes
############################################

class services_ServiceProfile:

    def __init__(self, name: str, services_ServiceProfile: set["services_NetXResource"] = None, services_ServiceProfile40: "services_ServiceUser" = None):
        self.name = name
        self.services_ServiceProfile = services_ServiceProfile if services_ServiceProfile is not None else set()
        self.services_ServiceProfile40 = services_ServiceProfile40
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def services_ServiceProfile40(self):
        return self.__services_ServiceProfile40

    @services_ServiceProfile40.setter
    def services_ServiceProfile40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceProfile__services_ServiceProfile40", None)
        self.__services_ServiceProfile40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_ServiceUser39"):
                opp_val = getattr(old_value, "services_ServiceUser39", None)
                if opp_val == self:
                    setattr(old_value, "services_ServiceUser39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_ServiceUser39"):
                opp_val = getattr(value, "services_ServiceUser39", None)
                setattr(value, "services_ServiceUser39", self)

    @property
    def services_ServiceProfile(self):
        return self.__services_ServiceProfile

    @services_ServiceProfile.setter
    def services_ServiceProfile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceProfile__services_ServiceProfile", None)
        self.__services_ServiceProfile = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "services_NetXResource37"):
                    opp_val = getattr(item, "services_NetXResource37", None)
                    
                    if opp_val == self:
                        setattr(item, "services_NetXResource37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "services_NetXResource37"):
                    opp_val = getattr(item, "services_NetXResource37", None)
                    
                    setattr(item, "services_NetXResource37", self)
                    

class services_ResourceMonitor:

    pass
class services_DateTimeRange:

    pass
class services_Value:

    pass
class services_ResourceForecast:

    pass
class services_ServiceForecastUsers:

    pass
class services_Expression:

    pass
class services_NetXResource:

    pass
class services_ServiceDistribution:

    pass
class services_ServiceUser:

    def __init__(self, name: str, services_ServiceUser: "services_Service" = None, services_ServiceUser30: "services_ServiceForecastUsers" = None, services_ServiceUser39: "services_ServiceProfile" = None, services_ServiceUser42: set["services_Expression"] = None):
        self.name = name
        self.services_ServiceUser = services_ServiceUser
        self.services_ServiceUser30 = services_ServiceUser30
        self.services_ServiceUser39 = services_ServiceUser39
        self.services_ServiceUser42 = services_ServiceUser42 if services_ServiceUser42 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def services_ServiceUser(self):
        return self.__services_ServiceUser

    @services_ServiceUser.setter
    def services_ServiceUser(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceUser__services_ServiceUser", None)
        self.__services_ServiceUser = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_Service13"):
                opp_val = getattr(old_value, "services_Service13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_Service13"):
                opp_val = getattr(value, "services_Service13", None)
                if opp_val is None:
                    setattr(value, "services_Service13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def services_ServiceUser30(self):
        return self.__services_ServiceUser30

    @services_ServiceUser30.setter
    def services_ServiceUser30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceUser__services_ServiceUser30", None)
        self.__services_ServiceUser30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_ServiceForecastUsers29"):
                opp_val = getattr(old_value, "services_ServiceForecastUsers29", None)
                if opp_val == self:
                    setattr(old_value, "services_ServiceForecastUsers29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_ServiceForecastUsers29"):
                opp_val = getattr(value, "services_ServiceForecastUsers29", None)
                setattr(value, "services_ServiceForecastUsers29", self)

    @property
    def services_ServiceUser39(self):
        return self.__services_ServiceUser39

    @services_ServiceUser39.setter
    def services_ServiceUser39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceUser__services_ServiceUser39", None)
        self.__services_ServiceUser39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_ServiceProfile40"):
                opp_val = getattr(old_value, "services_ServiceProfile40", None)
                if opp_val == self:
                    setattr(old_value, "services_ServiceProfile40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_ServiceProfile40"):
                opp_val = getattr(value, "services_ServiceProfile40", None)
                setattr(value, "services_ServiceProfile40", self)

    @property
    def services_ServiceUser42(self):
        return self.__services_ServiceUser42

    @services_ServiceUser42.setter
    def services_ServiceUser42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceUser__services_ServiceUser42", None)
        self.__services_ServiceUser42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "services_Expression43"):
                    opp_val = getattr(item, "services_Expression43", None)
                    
                    if opp_val == self:
                        setattr(item, "services_Expression43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "services_Expression43"):
                    opp_val = getattr(item, "services_Expression43", None)
                    
                    setattr(item, "services_Expression43", self)
                    

class services_ServiceMonitor:

    def __init__(self, name: str, revision: str, services_ServiceMonitor: "services_Service" = None, services_ServiceMonitor32: "services_DateTimeRange" = None, services_ServiceMonitor35: set["services_ResourceMonitor"] = None):
        self.name = name
        self.revision = revision
        self.services_ServiceMonitor = services_ServiceMonitor
        self.services_ServiceMonitor32 = services_ServiceMonitor32
        self.services_ServiceMonitor35 = services_ServiceMonitor35 if services_ServiceMonitor35 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def revision(self) -> str:
        return self.__revision

    @revision.setter
    def revision(self, revision: str):
        self.__revision = revision

    @property
    def services_ServiceMonitor(self):
        return self.__services_ServiceMonitor

    @services_ServiceMonitor.setter
    def services_ServiceMonitor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceMonitor__services_ServiceMonitor", None)
        self.__services_ServiceMonitor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_Service11"):
                opp_val = getattr(old_value, "services_Service11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_Service11"):
                opp_val = getattr(value, "services_Service11", None)
                if opp_val is None:
                    setattr(value, "services_Service11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def services_ServiceMonitor35(self):
        return self.__services_ServiceMonitor35

    @services_ServiceMonitor35.setter
    def services_ServiceMonitor35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceMonitor__services_ServiceMonitor35", None)
        self.__services_ServiceMonitor35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "services_ResourceMonitor"):
                    opp_val = getattr(item, "services_ResourceMonitor", None)
                    
                    if opp_val == self:
                        setattr(item, "services_ResourceMonitor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "services_ResourceMonitor"):
                    opp_val = getattr(item, "services_ResourceMonitor", None)
                    
                    setattr(item, "services_ResourceMonitor", self)
                    

    @property
    def services_ServiceMonitor32(self):
        return self.__services_ServiceMonitor32

    @services_ServiceMonitor32.setter
    def services_ServiceMonitor32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceMonitor__services_ServiceMonitor32", None)
        self.__services_ServiceMonitor32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_DateTimeRange33"):
                opp_val = getattr(old_value, "services_DateTimeRange33", None)
                if opp_val == self:
                    setattr(old_value, "services_DateTimeRange33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_DateTimeRange33"):
                opp_val = getattr(value, "services_DateTimeRange33", None)
                setattr(value, "services_DateTimeRange33", self)

class services_ServiceForecast:

    def __init__(self, name: str, revision: str, services_ServiceForecast: "services_Service" = None, services_ServiceForecast23: set["services_ServiceForecastUsers"] = None, services_ServiceForecast25: set["services_ResourceForecast"] = None, services_ServiceForecast21: "services_DateTimeRange" = None):
        self.name = name
        self.revision = revision
        self.services_ServiceForecast = services_ServiceForecast
        self.services_ServiceForecast23 = services_ServiceForecast23 if services_ServiceForecast23 is not None else set()
        self.services_ServiceForecast25 = services_ServiceForecast25 if services_ServiceForecast25 is not None else set()
        self.services_ServiceForecast21 = services_ServiceForecast21
        
    @property
    def revision(self) -> str:
        return self.__revision

    @revision.setter
    def revision(self, revision: str):
        self.__revision = revision

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def services_ServiceForecast23(self):
        return self.__services_ServiceForecast23

    @services_ServiceForecast23.setter
    def services_ServiceForecast23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceForecast__services_ServiceForecast23", None)
        self.__services_ServiceForecast23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "services_ServiceForecastUsers"):
                    opp_val = getattr(item, "services_ServiceForecastUsers", None)
                    
                    if opp_val == self:
                        setattr(item, "services_ServiceForecastUsers", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "services_ServiceForecastUsers"):
                    opp_val = getattr(item, "services_ServiceForecastUsers", None)
                    
                    setattr(item, "services_ServiceForecastUsers", self)
                    

    @property
    def services_ServiceForecast(self):
        return self.__services_ServiceForecast

    @services_ServiceForecast.setter
    def services_ServiceForecast(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceForecast__services_ServiceForecast", None)
        self.__services_ServiceForecast = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_Service9"):
                opp_val = getattr(old_value, "services_Service9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_Service9"):
                opp_val = getattr(value, "services_Service9", None)
                if opp_val is None:
                    setattr(value, "services_Service9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def services_ServiceForecast25(self):
        return self.__services_ServiceForecast25

    @services_ServiceForecast25.setter
    def services_ServiceForecast25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceForecast__services_ServiceForecast25", None)
        self.__services_ServiceForecast25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "services_ResourceForecast"):
                    opp_val = getattr(item, "services_ResourceForecast", None)
                    
                    if opp_val == self:
                        setattr(item, "services_ResourceForecast", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "services_ResourceForecast"):
                    opp_val = getattr(item, "services_ResourceForecast", None)
                    
                    setattr(item, "services_ResourceForecast", self)
                    

    @property
    def services_ServiceForecast21(self):
        return self.__services_ServiceForecast21

    @services_ServiceForecast21.setter
    def services_ServiceForecast21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceForecast__services_ServiceForecast21", None)
        self.__services_ServiceForecast21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_DateTimeRange"):
                opp_val = getattr(old_value, "services_DateTimeRange", None)
                if opp_val == self:
                    setattr(old_value, "services_DateTimeRange", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_DateTimeRange"):
                opp_val = getattr(value, "services_DateTimeRange", None)
                setattr(value, "services_DateTimeRange", self)

class services_Service:

    def __init__(self, serviceCategory: str, serviceDescription: str, serviceName: str, serviceClass: str, services_Service7: "services_Service" = None, services_Service5: set["services_Service"] = None, services_Service9: set["services_ServiceForecast"] = None, services_Service11: set["services_ServiceMonitor"] = None, services_Service13: set["services_ServiceUser"] = None, services_Service15: "services_ServiceDistribution" = None, services_Service: set["services_CIID"] = None):
        self.serviceCategory = serviceCategory
        self.serviceDescription = serviceDescription
        self.serviceName = serviceName
        self.serviceClass = serviceClass
        self.services_Service7 = services_Service7
        self.services_Service5 = services_Service5 if services_Service5 is not None else set()
        self.services_Service9 = services_Service9 if services_Service9 is not None else set()
        self.services_Service11 = services_Service11 if services_Service11 is not None else set()
        self.services_Service13 = services_Service13 if services_Service13 is not None else set()
        self.services_Service15 = services_Service15
        self.services_Service = services_Service if services_Service is not None else set()
        
    @property
    def serviceClass(self) -> str:
        return self.__serviceClass

    @serviceClass.setter
    def serviceClass(self, serviceClass: str):
        self.__serviceClass = serviceClass

    @property
    def serviceName(self) -> str:
        return self.__serviceName

    @serviceName.setter
    def serviceName(self, serviceName: str):
        self.__serviceName = serviceName

    @property
    def serviceDescription(self) -> str:
        return self.__serviceDescription

    @serviceDescription.setter
    def serviceDescription(self, serviceDescription: str):
        self.__serviceDescription = serviceDescription

    @property
    def serviceCategory(self) -> str:
        return self.__serviceCategory

    @serviceCategory.setter
    def serviceCategory(self, serviceCategory: str):
        self.__serviceCategory = serviceCategory

    @property
    def services_Service5(self):
        return self.__services_Service5

    @services_Service5.setter
    def services_Service5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service5", None)
        self.__services_Service5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "services_Service7"):
                    opp_val = getattr(item, "services_Service7", None)
                    
                    if opp_val == self:
                        setattr(item, "services_Service7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "services_Service7"):
                    opp_val = getattr(item, "services_Service7", None)
                    
                    setattr(item, "services_Service7", self)
                    

    @property
    def services_Service9(self):
        return self.__services_Service9

    @services_Service9.setter
    def services_Service9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service9", None)
        self.__services_Service9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "services_ServiceForecast"):
                    opp_val = getattr(item, "services_ServiceForecast", None)
                    
                    if opp_val == self:
                        setattr(item, "services_ServiceForecast", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "services_ServiceForecast"):
                    opp_val = getattr(item, "services_ServiceForecast", None)
                    
                    setattr(item, "services_ServiceForecast", self)
                    

    @property
    def services_Service11(self):
        return self.__services_Service11

    @services_Service11.setter
    def services_Service11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service11", None)
        self.__services_Service11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "services_ServiceMonitor"):
                    opp_val = getattr(item, "services_ServiceMonitor", None)
                    
                    if opp_val == self:
                        setattr(item, "services_ServiceMonitor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "services_ServiceMonitor"):
                    opp_val = getattr(item, "services_ServiceMonitor", None)
                    
                    setattr(item, "services_ServiceMonitor", self)
                    

    @property
    def services_Service13(self):
        return self.__services_Service13

    @services_Service13.setter
    def services_Service13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service13", None)
        self.__services_Service13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "services_ServiceUser"):
                    opp_val = getattr(item, "services_ServiceUser", None)
                    
                    if opp_val == self:
                        setattr(item, "services_ServiceUser", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "services_ServiceUser"):
                    opp_val = getattr(item, "services_ServiceUser", None)
                    
                    setattr(item, "services_ServiceUser", self)
                    

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
            if hasattr(old_value, "services_Service5"):
                opp_val = getattr(old_value, "services_Service5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_Service5"):
                opp_val = getattr(value, "services_Service5", None)
                if opp_val is None:
                    setattr(value, "services_Service5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "services_ServiceDistribution"):
                opp_val = getattr(old_value, "services_ServiceDistribution", None)
                if opp_val == self:
                    setattr(old_value, "services_ServiceDistribution", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_ServiceDistribution"):
                opp_val = getattr(value, "services_ServiceDistribution", None)
                setattr(value, "services_ServiceDistribution", self)

    @property
    def services_Service(self):
        return self.__services_Service

    @services_Service.setter
    def services_Service(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service", None)
        self.__services_Service = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "services_CIID"):
                    opp_val = getattr(item, "services_CIID", None)
                    
                    if opp_val == self:
                        setattr(item, "services_CIID", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "services_CIID"):
                    opp_val = getattr(item, "services_CIID", None)
                    
                    setattr(item, "services_CIID", self)
                    

class services_EObject:

    pass
class services_CIID:

    def __init__(self, commonCIID: str, localCIID: str, services_CIID: "services_Service" = None):
        self.commonCIID = commonCIID
        self.localCIID = localCIID
        self.services_CIID = services_CIID
        
    @property
    def localCIID(self) -> str:
        return self.__localCIID

    @localCIID.setter
    def localCIID(self, localCIID: str):
        self.__localCIID = localCIID

    @property
    def commonCIID(self) -> str:
        return self.__commonCIID

    @commonCIID.setter
    def commonCIID(self, commonCIID: str):
        self.__commonCIID = commonCIID

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
            if hasattr(old_value, "services_Service"):
                opp_val = getattr(old_value, "services_Service", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_Service"):
                opp_val = getattr(value, "services_Service", None)
                if opp_val is None:
                    setattr(value, "services_Service", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Service:

    pass
class services_RFSService(Service):

    def __init__(self, functionalCategory: str, services_RFSService: set["services_EObject"] = None, services_RFSService2: set["services_EObject"] = None):
        self.functionalCategory = functionalCategory
        self.services_RFSService = services_RFSService if services_RFSService is not None else set()
        self.services_RFSService2 = services_RFSService2 if services_RFSService2 is not None else set()
        
    @property
    def functionalCategory(self) -> str:
        return self.__functionalCategory

    @functionalCategory.setter
    def functionalCategory(self, functionalCategory: str):
        self.__functionalCategory = functionalCategory

    @property
    def services_RFSService2(self):
        return self.__services_RFSService2

    @services_RFSService2.setter
    def services_RFSService2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_RFSService__services_RFSService2", None)
        self.__services_RFSService2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "services_EObject3"):
                    opp_val = getattr(item, "services_EObject3", None)
                    
                    if opp_val == self:
                        setattr(item, "services_EObject3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "services_EObject3"):
                    opp_val = getattr(item, "services_EObject3", None)
                    
                    setattr(item, "services_EObject3", self)
                    

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
                    

class services_CFSService(Service):

    def __init__(self, provider: str, scenario: str):
        self.provider = provider
        self.scenario = scenario
        
    @property
    def scenario(self) -> str:
        return self.__scenario

    @scenario.setter
    def scenario(self, scenario: str):
        self.__scenario = scenario

    @property
    def provider(self) -> str:
        return self.__provider

    @provider.setter
    def provider(self, provider: str):
        self.__provider = provider
