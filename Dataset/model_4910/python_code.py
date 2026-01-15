from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ServiceClassType(Enum):
    Gold = "Gold"
    Silver = "Silver"
    Bronze = "Bronze"
class ResourceOriginType(Enum):
    InBound = "InBound"
    OutBound = "OutBound"
    Internal = "Internal"


############################################
# Definition of Classes
############################################

class services_ResourceMonitor:

    pass
class services_ResourceForecast:

    pass
class services_DateTimeRange:

    pass
class services_Expression:

    pass
class services_Lifecycle:

    pass
class services_Tolerance:

    pass
class services_Node:

    pass
class services_NetXResource:

    pass
class services_Value:

    pass
class BaseResource:

    pass
class services_DerivedResource(BaseResource):

    pass
class Base:

    pass
class services_ServiceMonitor(Base):

    def __init__(self, name: str, revision: str, services_ServiceMonitor: "services_Service" = None, services_ServiceMonitor46: "services_DateTimeRange" = None, services_ServiceMonitor49: set["services_ResourceMonitor"] = None):
        self.name = name
        self.revision = revision
        self.services_ServiceMonitor = services_ServiceMonitor
        self.services_ServiceMonitor46 = services_ServiceMonitor46
        self.services_ServiceMonitor49 = services_ServiceMonitor49 if services_ServiceMonitor49 is not None else set()
        
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
    def services_ServiceMonitor(self):
        return self.__services_ServiceMonitor

    @services_ServiceMonitor.setter
    def services_ServiceMonitor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceMonitor__services_ServiceMonitor", None)
        self.__services_ServiceMonitor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_Service23"):
                opp_val = getattr(old_value, "services_Service23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_Service23"):
                opp_val = getattr(value, "services_Service23", None)
                if opp_val is None:
                    setattr(value, "services_Service23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def services_ServiceMonitor46(self):
        return self.__services_ServiceMonitor46

    @services_ServiceMonitor46.setter
    def services_ServiceMonitor46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceMonitor__services_ServiceMonitor46", None)
        self.__services_ServiceMonitor46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_DateTimeRange47"):
                opp_val = getattr(old_value, "services_DateTimeRange47", None)
                if opp_val == self:
                    setattr(old_value, "services_DateTimeRange47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_DateTimeRange47"):
                opp_val = getattr(value, "services_DateTimeRange47", None)
                setattr(value, "services_DateTimeRange47", self)

    @property
    def services_ServiceMonitor49(self):
        return self.__services_ServiceMonitor49

    @services_ServiceMonitor49.setter
    def services_ServiceMonitor49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceMonitor__services_ServiceMonitor49", None)
        self.__services_ServiceMonitor49 = value if value is not None else set()
        
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
                    

class services_Service(Base):

    def __init__(self, serviceCategory: str, serviceClass: str, serviceDescription: str, serviceName: str, services_Service: set["services_CIID"] = None, services_Service16: "services_Lifecycle" = None, services_Service19: "services_Service" = None, services_Service17: set["services_Service"] = None, services_Service23: set["services_ServiceMonitor"] = None, services_Service25: set["services_ServiceUser"] = None, services_Service27: "services_ServiceDistribution" = None, services_Service21: set["services_ServiceForecast"] = None):
        self.serviceCategory = serviceCategory
        self.serviceClass = serviceClass
        self.serviceDescription = serviceDescription
        self.serviceName = serviceName
        self.services_Service = services_Service if services_Service is not None else set()
        self.services_Service16 = services_Service16
        self.services_Service19 = services_Service19
        self.services_Service17 = services_Service17 if services_Service17 is not None else set()
        self.services_Service23 = services_Service23 if services_Service23 is not None else set()
        self.services_Service25 = services_Service25 if services_Service25 is not None else set()
        self.services_Service27 = services_Service27
        self.services_Service21 = services_Service21 if services_Service21 is not None else set()
        
    @property
    def serviceName(self) -> str:
        return self.__serviceName

    @serviceName.setter
    def serviceName(self, serviceName: str):
        self.__serviceName = serviceName

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
    def serviceDescription(self) -> str:
        return self.__serviceDescription

    @serviceDescription.setter
    def serviceDescription(self, serviceDescription: str):
        self.__serviceDescription = serviceDescription

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
    def services_Service16(self):
        return self.__services_Service16

    @services_Service16.setter
    def services_Service16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service16", None)
        self.__services_Service16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_Lifecycle"):
                opp_val = getattr(old_value, "services_Lifecycle", None)
                if opp_val == self:
                    setattr(old_value, "services_Lifecycle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_Lifecycle"):
                opp_val = getattr(value, "services_Lifecycle", None)
                setattr(value, "services_Lifecycle", self)

    @property
    def services_Service27(self):
        return self.__services_Service27

    @services_Service27.setter
    def services_Service27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service27", None)
        self.__services_Service27 = value
        
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
    def services_Service25(self):
        return self.__services_Service25

    @services_Service25.setter
    def services_Service25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service25", None)
        self.__services_Service25 = value if value is not None else set()
        
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
    def services_Service23(self):
        return self.__services_Service23

    @services_Service23.setter
    def services_Service23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service23", None)
        self.__services_Service23 = value if value is not None else set()
        
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
    def services_Service21(self):
        return self.__services_Service21

    @services_Service21.setter
    def services_Service21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_Service__services_Service21", None)
        self.__services_Service21 = value if value is not None else set()
        
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
                if hasattr(item, "services_Service19"):
                    opp_val = getattr(item, "services_Service19", None)
                    
                    if opp_val == self:
                        setattr(item, "services_Service19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "services_Service19"):
                    opp_val = getattr(item, "services_Service19", None)
                    
                    setattr(item, "services_Service19", self)
                    

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

class services_ServiceForecast(Base):

    def __init__(self, name: str, revision: str, services_ServiceForecast: "services_Service" = None, services_ServiceForecast34: "services_DateTimeRange" = None, services_ServiceForecast36: set["services_ServiceForecastUsers"] = None, services_ServiceForecast38: set["services_ResourceForecast"] = None):
        self.name = name
        self.revision = revision
        self.services_ServiceForecast = services_ServiceForecast
        self.services_ServiceForecast34 = services_ServiceForecast34
        self.services_ServiceForecast36 = services_ServiceForecast36 if services_ServiceForecast36 is not None else set()
        self.services_ServiceForecast38 = services_ServiceForecast38 if services_ServiceForecast38 is not None else set()
        
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
    def services_ServiceForecast36(self):
        return self.__services_ServiceForecast36

    @services_ServiceForecast36.setter
    def services_ServiceForecast36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceForecast__services_ServiceForecast36", None)
        self.__services_ServiceForecast36 = value if value is not None else set()
        
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
    def services_ServiceForecast34(self):
        return self.__services_ServiceForecast34

    @services_ServiceForecast34.setter
    def services_ServiceForecast34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceForecast__services_ServiceForecast34", None)
        self.__services_ServiceForecast34 = value
        
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
    def services_ServiceForecast(self):
        return self.__services_ServiceForecast

    @services_ServiceForecast.setter
    def services_ServiceForecast(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceForecast__services_ServiceForecast", None)
        self.__services_ServiceForecast = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_Service21"):
                opp_val = getattr(old_value, "services_Service21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_Service21"):
                opp_val = getattr(value, "services_Service21", None)
                if opp_val is None:
                    setattr(value, "services_Service21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def services_ServiceForecast38(self):
        return self.__services_ServiceForecast38

    @services_ServiceForecast38.setter
    def services_ServiceForecast38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceForecast__services_ServiceForecast38", None)
        self.__services_ServiceForecast38 = value if value is not None else set()
        
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
                    

class services_ServiceUser(Base):

    def __init__(self, description: str, name: str, services_ServiceUser: "services_Service" = None, services_ServiceUser44: "services_ServiceForecastUsers" = None, services_ServiceUser53: "services_ServiceProfile" = None, services_ServiceUser56: "services_Expression" = None):
        self.description = description
        self.name = name
        self.services_ServiceUser = services_ServiceUser
        self.services_ServiceUser44 = services_ServiceUser44
        self.services_ServiceUser53 = services_ServiceUser53
        self.services_ServiceUser56 = services_ServiceUser56
        
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
    def services_ServiceUser(self):
        return self.__services_ServiceUser

    @services_ServiceUser.setter
    def services_ServiceUser(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceUser__services_ServiceUser", None)
        self.__services_ServiceUser = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_Service25"):
                opp_val = getattr(old_value, "services_Service25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_Service25"):
                opp_val = getattr(value, "services_Service25", None)
                if opp_val is None:
                    setattr(value, "services_Service25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def services_ServiceUser56(self):
        return self.__services_ServiceUser56

    @services_ServiceUser56.setter
    def services_ServiceUser56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceUser__services_ServiceUser56", None)
        self.__services_ServiceUser56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_Expression57"):
                opp_val = getattr(old_value, "services_Expression57", None)
                if opp_val == self:
                    setattr(old_value, "services_Expression57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_Expression57"):
                opp_val = getattr(value, "services_Expression57", None)
                setattr(value, "services_Expression57", self)

    @property
    def services_ServiceUser53(self):
        return self.__services_ServiceUser53

    @services_ServiceUser53.setter
    def services_ServiceUser53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceUser__services_ServiceUser53", None)
        self.__services_ServiceUser53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_ServiceProfile54"):
                opp_val = getattr(old_value, "services_ServiceProfile54", None)
                if opp_val == self:
                    setattr(old_value, "services_ServiceProfile54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_ServiceProfile54"):
                opp_val = getattr(value, "services_ServiceProfile54", None)
                setattr(value, "services_ServiceProfile54", self)

    @property
    def services_ServiceUser44(self):
        return self.__services_ServiceUser44

    @services_ServiceUser44.setter
    def services_ServiceUser44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceUser__services_ServiceUser44", None)
        self.__services_ServiceUser44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_ServiceForecastUsers43"):
                opp_val = getattr(old_value, "services_ServiceForecastUsers43", None)
                if opp_val == self:
                    setattr(old_value, "services_ServiceForecastUsers43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_ServiceForecastUsers43"):
                opp_val = getattr(value, "services_ServiceForecastUsers43", None)
                setattr(value, "services_ServiceForecastUsers43", self)

class services_ServiceDistribution(Base):

    pass
class services_ServiceProfile(Base):

    def __init__(self, name: str, services_ServiceProfile: set["services_DerivedResource"] = None, services_ServiceProfile54: "services_ServiceUser" = None):
        self.name = name
        self.services_ServiceProfile = services_ServiceProfile if services_ServiceProfile is not None else set()
        self.services_ServiceProfile54 = services_ServiceProfile54
        
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
        self.__services_ServiceProfile = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "services_DerivedResource51"):
                    opp_val = getattr(item, "services_DerivedResource51", None)
                    
                    if opp_val == self:
                        setattr(item, "services_DerivedResource51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "services_DerivedResource51"):
                    opp_val = getattr(item, "services_DerivedResource51", None)
                    
                    setattr(item, "services_DerivedResource51", self)
                    

    @property
    def services_ServiceProfile54(self):
        return self.__services_ServiceProfile54

    @services_ServiceProfile54.setter
    def services_ServiceProfile54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_ServiceProfile__services_ServiceProfile54", None)
        self.__services_ServiceProfile54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_ServiceUser53"):
                opp_val = getattr(old_value, "services_ServiceUser53", None)
                if opp_val == self:
                    setattr(old_value, "services_ServiceUser53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_ServiceUser53"):
                opp_val = getattr(value, "services_ServiceUser53", None)
                setattr(value, "services_ServiceUser53", self)

class services_ServiceForecastUsers(Base):

    pass
class services_DistributionEntry(Base):

    def __init__(self, resourceOrigin: str, services_DistributionEntry: "services_NetXResource" = None, services_DistributionEntry9: "services_DerivedResource" = None, services_DistributionEntry30: "services_ServiceDistribution" = None):
        self.resourceOrigin = resourceOrigin
        self.services_DistributionEntry = services_DistributionEntry
        self.services_DistributionEntry9 = services_DistributionEntry9
        self.services_DistributionEntry30 = services_DistributionEntry30
        
    @property
    def resourceOrigin(self) -> str:
        return self.__resourceOrigin

    @resourceOrigin.setter
    def resourceOrigin(self, resourceOrigin: str):
        self.__resourceOrigin = resourceOrigin

    @property
    def services_DistributionEntry(self):
        return self.__services_DistributionEntry

    @services_DistributionEntry.setter
    def services_DistributionEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_DistributionEntry__services_DistributionEntry", None)
        self.__services_DistributionEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_NetXResource"):
                opp_val = getattr(old_value, "services_NetXResource", None)
                if opp_val == self:
                    setattr(old_value, "services_NetXResource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_NetXResource"):
                opp_val = getattr(value, "services_NetXResource", None)
                setattr(value, "services_NetXResource", self)

    @property
    def services_DistributionEntry30(self):
        return self.__services_DistributionEntry30

    @services_DistributionEntry30.setter
    def services_DistributionEntry30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_DistributionEntry__services_DistributionEntry30", None)
        self.__services_DistributionEntry30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_ServiceDistribution29"):
                opp_val = getattr(old_value, "services_ServiceDistribution29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_ServiceDistribution29"):
                opp_val = getattr(value, "services_ServiceDistribution29", None)
                if opp_val is None:
                    setattr(value, "services_ServiceDistribution29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def services_DistributionEntry9(self):
        return self.__services_DistributionEntry9

    @services_DistributionEntry9.setter
    def services_DistributionEntry9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_DistributionEntry__services_DistributionEntry9", None)
        self.__services_DistributionEntry9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_DerivedResource10"):
                opp_val = getattr(old_value, "services_DerivedResource10", None)
                if opp_val == self:
                    setattr(old_value, "services_DerivedResource10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_DerivedResource10"):
                opp_val = getattr(value, "services_DerivedResource10", None)
                setattr(value, "services_DerivedResource10", self)

class services_CIID(Base):

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

    def __init__(self, functionalCategory: str, services_RFSService: set["services_Node"] = None, services_RFSService13: set["services_Tolerance"] = None):
        self.functionalCategory = functionalCategory
        self.services_RFSService = services_RFSService if services_RFSService is not None else set()
        self.services_RFSService13 = services_RFSService13 if services_RFSService13 is not None else set()
        
    @property
    def functionalCategory(self) -> str:
        return self.__functionalCategory

    @functionalCategory.setter
    def functionalCategory(self, functionalCategory: str):
        self.__functionalCategory = functionalCategory

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
                    

    @property
    def services_RFSService13(self):
        return self.__services_RFSService13

    @services_RFSService13.setter
    def services_RFSService13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_RFSService__services_RFSService13", None)
        self.__services_RFSService13 = value if value is not None else set()
        
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
