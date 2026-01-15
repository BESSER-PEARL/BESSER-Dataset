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

class services_ResourceMonitor:

    pass
class services_ServiceProfile:

    def __init__(self, name: str, services_ServiceProfile: set["services_NetXResource"] = None, services_ServiceProfile39: "services_ServiceUser" = None):
        self.name = name
        self.services_ServiceProfile = services_ServiceProfile if services_ServiceProfile is not None else set()
        self.services_ServiceProfile39 = services_ServiceProfile39
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def services_ServiceProfile39(self):
        return self.__services_ServiceProfile39

    @services_ServiceProfile39.setter
    def services_ServiceProfile39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceProfile__services_ServiceProfile39", None)
        self.__services_ServiceProfile39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_ServiceUser38"):
                opp_val = getattr(old_value, "services_ServiceUser38", None)
                if opp_val == self:
                    setattr(old_value, "services_ServiceUser38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_ServiceUser38"):
                opp_val = getattr(value, "services_ServiceUser38", None)
                setattr(value, "services_ServiceUser38", self)

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
                if hasattr(item, "services_NetXResource36"):
                    opp_val = getattr(item, "services_NetXResource36", None)
                    
                    if opp_val == self:
                        setattr(item, "services_NetXResource36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "services_NetXResource36"):
                    opp_val = getattr(item, "services_NetXResource36", None)
                    
                    setattr(item, "services_NetXResource36", self)
                    

class services_ServiceForecastUsers:

    pass
class services_DateTimeRange:

    pass
class services_Value:

    pass
class services_ResourceForecast:

    pass
class services_Expression:

    pass
class services_NetXResource:

    pass
class services_Tolerance:

    pass
class services_ServiceDistribution:

    pass
class services_ServiceUser:

    def __init__(self, name: str, services_ServiceUser: "services_Service" = None, services_ServiceUser29: "services_ServiceForecastUsers" = None, services_ServiceUser38: "services_ServiceProfile" = None, services_ServiceUser41: set["services_Expression"] = None):
        self.name = name
        self.services_ServiceUser = services_ServiceUser
        self.services_ServiceUser29 = services_ServiceUser29
        self.services_ServiceUser38 = services_ServiceUser38
        self.services_ServiceUser41 = services_ServiceUser41 if services_ServiceUser41 is not None else set()
        
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
            if hasattr(old_value, "services_Service12"):
                opp_val = getattr(old_value, "services_Service12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_Service12"):
                opp_val = getattr(value, "services_Service12", None)
                if opp_val is None:
                    setattr(value, "services_Service12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def services_ServiceUser41(self):
        return self.__services_ServiceUser41

    @services_ServiceUser41.setter
    def services_ServiceUser41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceUser__services_ServiceUser41", None)
        self.__services_ServiceUser41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "services_Expression42"):
                    opp_val = getattr(item, "services_Expression42", None)
                    
                    if opp_val == self:
                        setattr(item, "services_Expression42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "services_Expression42"):
                    opp_val = getattr(item, "services_Expression42", None)
                    
                    setattr(item, "services_Expression42", self)
                    

    @property
    def services_ServiceUser29(self):
        return self.__services_ServiceUser29

    @services_ServiceUser29.setter
    def services_ServiceUser29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceUser__services_ServiceUser29", None)
        self.__services_ServiceUser29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_ServiceForecastUsers28"):
                opp_val = getattr(old_value, "services_ServiceForecastUsers28", None)
                if opp_val == self:
                    setattr(old_value, "services_ServiceForecastUsers28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_ServiceForecastUsers28"):
                opp_val = getattr(value, "services_ServiceForecastUsers28", None)
                setattr(value, "services_ServiceForecastUsers28", self)

    @property
    def services_ServiceUser38(self):
        return self.__services_ServiceUser38

    @services_ServiceUser38.setter
    def services_ServiceUser38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceUser__services_ServiceUser38", None)
        self.__services_ServiceUser38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_ServiceProfile39"):
                opp_val = getattr(old_value, "services_ServiceProfile39", None)
                if opp_val == self:
                    setattr(old_value, "services_ServiceProfile39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_ServiceProfile39"):
                opp_val = getattr(value, "services_ServiceProfile39", None)
                setattr(value, "services_ServiceProfile39", self)

class services_ServiceMonitor:

    def __init__(self, name: str, revision: str, services_ServiceMonitor: "services_Service" = None, services_ServiceMonitor31: "services_DateTimeRange" = None, services_ServiceMonitor34: set["services_ResourceMonitor"] = None):
        self.name = name
        self.revision = revision
        self.services_ServiceMonitor = services_ServiceMonitor
        self.services_ServiceMonitor31 = services_ServiceMonitor31
        self.services_ServiceMonitor34 = services_ServiceMonitor34 if services_ServiceMonitor34 is not None else set()
        
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
    def services_ServiceMonitor31(self):
        return self.__services_ServiceMonitor31

    @services_ServiceMonitor31.setter
    def services_ServiceMonitor31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceMonitor__services_ServiceMonitor31", None)
        self.__services_ServiceMonitor31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_DateTimeRange32"):
                opp_val = getattr(old_value, "services_DateTimeRange32", None)
                if opp_val == self:
                    setattr(old_value, "services_DateTimeRange32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_DateTimeRange32"):
                opp_val = getattr(value, "services_DateTimeRange32", None)
                setattr(value, "services_DateTimeRange32", self)

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
            if hasattr(old_value, "services_Service10"):
                opp_val = getattr(old_value, "services_Service10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_Service10"):
                opp_val = getattr(value, "services_Service10", None)
                if opp_val is None:
                    setattr(value, "services_Service10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def services_ServiceMonitor34(self):
        return self.__services_ServiceMonitor34

    @services_ServiceMonitor34.setter
    def services_ServiceMonitor34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceMonitor__services_ServiceMonitor34", None)
        self.__services_ServiceMonitor34 = value if value is not None else set()
        
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
                    

class services_ServiceForecast:

    def __init__(self, name: str, revision: str, services_ServiceForecast: "services_Service" = None, services_ServiceForecast22: set["services_ServiceForecastUsers"] = None, services_ServiceForecast24: set["services_ResourceForecast"] = None, services_ServiceForecast20: "services_DateTimeRange" = None):
        self.name = name
        self.revision = revision
        self.services_ServiceForecast = services_ServiceForecast
        self.services_ServiceForecast22 = services_ServiceForecast22 if services_ServiceForecast22 is not None else set()
        self.services_ServiceForecast24 = services_ServiceForecast24 if services_ServiceForecast24 is not None else set()
        self.services_ServiceForecast20 = services_ServiceForecast20
        
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
    def services_ServiceForecast(self):
        return self.__services_ServiceForecast

    @services_ServiceForecast.setter
    def services_ServiceForecast(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceForecast__services_ServiceForecast", None)
        self.__services_ServiceForecast = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_Service8"):
                opp_val = getattr(old_value, "services_Service8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_Service8"):
                opp_val = getattr(value, "services_Service8", None)
                if opp_val is None:
                    setattr(value, "services_Service8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def services_ServiceForecast24(self):
        return self.__services_ServiceForecast24

    @services_ServiceForecast24.setter
    def services_ServiceForecast24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceForecast__services_ServiceForecast24", None)
        self.__services_ServiceForecast24 = value if value is not None else set()
        
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
    def services_ServiceForecast20(self):
        return self.__services_ServiceForecast20

    @services_ServiceForecast20.setter
    def services_ServiceForecast20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceForecast__services_ServiceForecast20", None)
        self.__services_ServiceForecast20 = value
        
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

    @property
    def services_ServiceForecast22(self):
        return self.__services_ServiceForecast22

    @services_ServiceForecast22.setter
    def services_ServiceForecast22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceForecast__services_ServiceForecast22", None)
        self.__services_ServiceForecast22 = value if value is not None else set()
        
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
                    

class services_Service:

    def __init__(self, serviceClass: str, serviceDescription: str, serviceName: str, serviceCategory: str, services_Service: set["services_CIID"] = None, services_Service6: "services_Service" = None, services_Service4: set["services_Service"] = None, services_Service8: set["services_ServiceForecast"] = None, services_Service10: set["services_ServiceMonitor"] = None, services_Service12: set["services_ServiceUser"] = None, services_Service14: "services_ServiceDistribution" = None):
        self.serviceClass = serviceClass
        self.serviceDescription = serviceDescription
        self.serviceName = serviceName
        self.serviceCategory = serviceCategory
        self.services_Service = services_Service if services_Service is not None else set()
        self.services_Service6 = services_Service6
        self.services_Service4 = services_Service4 if services_Service4 is not None else set()
        self.services_Service8 = services_Service8 if services_Service8 is not None else set()
        self.services_Service10 = services_Service10 if services_Service10 is not None else set()
        self.services_Service12 = services_Service12 if services_Service12 is not None else set()
        self.services_Service14 = services_Service14
        
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
    def serviceClass(self) -> str:
        return self.__serviceClass

    @serviceClass.setter
    def serviceClass(self, serviceClass: str):
        self.__serviceClass = serviceClass

    @property
    def serviceCategory(self) -> str:
        return self.__serviceCategory

    @serviceCategory.setter
    def serviceCategory(self, serviceCategory: str):
        self.__serviceCategory = serviceCategory

    @property
    def services_Service6(self):
        return self.__services_Service6

    @services_Service6.setter
    def services_Service6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service6", None)
        self.__services_Service6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_Service4"):
                opp_val = getattr(old_value, "services_Service4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_Service4"):
                opp_val = getattr(value, "services_Service4", None)
                if opp_val is None:
                    setattr(value, "services_Service4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def services_Service10(self):
        return self.__services_Service10

    @services_Service10.setter
    def services_Service10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service10", None)
        self.__services_Service10 = value if value is not None else set()
        
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
    def services_Service4(self):
        return self.__services_Service4

    @services_Service4.setter
    def services_Service4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service4", None)
        self.__services_Service4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "services_Service6"):
                    opp_val = getattr(item, "services_Service6", None)
                    
                    if opp_val == self:
                        setattr(item, "services_Service6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "services_Service6"):
                    opp_val = getattr(item, "services_Service6", None)
                    
                    setattr(item, "services_Service6", self)
                    

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
                    

    @property
    def services_Service12(self):
        return self.__services_Service12

    @services_Service12.setter
    def services_Service12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service12", None)
        self.__services_Service12 = value if value is not None else set()
        
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
    def services_Service8(self):
        return self.__services_Service8

    @services_Service8.setter
    def services_Service8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service8", None)
        self.__services_Service8 = value if value is not None else set()
        
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
    def services_Service14(self):
        return self.__services_Service14

    @services_Service14.setter
    def services_Service14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service14", None)
        self.__services_Service14 = value
        
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

class services_Node:

    pass
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

    def __init__(self, functionalCategory: str, services_RFSService: set["services_Node"] = None, services_RFSService2: set["services_Tolerance"] = None):
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
                if hasattr(item, "services_Tolerance"):
                    opp_val = getattr(item, "services_Tolerance", None)
                    
                    if opp_val == self:
                        setattr(item, "services_Tolerance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "services_Tolerance"):
                    opp_val = getattr(item, "services_Tolerance", None)
                    
                    setattr(item, "services_Tolerance", self)
                    

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
                if hasattr(item, "services_Node"):
                    opp_val = getattr(item, "services_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "services_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "services_Node"):
                    opp_val = getattr(item, "services_Node", None)
                    
                    setattr(item, "services_Node", self)
                    

class services_CFSService(Service):

    def __init__(self, provider: str, scenario: str):
        self.provider = provider
        self.scenario = scenario
        
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
