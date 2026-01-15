from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class model_IHost:

    def __init__(self, name: str, address: str, model_IHost: "model_INetwork" = None, model_IHost3: set["model_IServiceInfo"] = None):
        self.name = name
        self.address = address
        self.model_IHost = model_IHost
        self.model_IHost3 = model_IHost3 if model_IHost3 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def model_IHost3(self):
        return self.__model_IHost3

    @model_IHost3.setter
    def model_IHost3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_IHost__model_IHost3", None)
        self.__model_IHost3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_IServiceInfo4"):
                    opp_val = getattr(item, "model_IServiceInfo4", None)
                    
                    if opp_val == self:
                        setattr(item, "model_IServiceInfo4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_IServiceInfo4"):
                    opp_val = getattr(item, "model_IServiceInfo4", None)
                    
                    setattr(item, "model_IServiceInfo4", self)
                    

    @property
    def model_IHost(self):
        return self.__model_IHost

    @model_IHost.setter
    def model_IHost(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_IHost__model_IHost", None)
        self.__model_IHost = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_INetwork"):
                opp_val = getattr(old_value, "model_INetwork", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_INetwork"):
                opp_val = getattr(value, "model_INetwork", None)
                if opp_val is None:
                    setattr(value, "model_INetwork", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_INetwork:

    pass
class model_IServiceTypeID:

    def __init__(self, ecfServiceTypeID: str, ecfNamingAuthority: str, ecfServices: str, ecfProtocols: str, ecfScopes: str, ecfServiceName: str, model_IServiceTypeID: "model_IServiceID" = None):
        self.ecfServiceTypeID = ecfServiceTypeID
        self.ecfNamingAuthority = ecfNamingAuthority
        self.ecfServices = ecfServices
        self.ecfProtocols = ecfProtocols
        self.ecfScopes = ecfScopes
        self.ecfServiceName = ecfServiceName
        self.model_IServiceTypeID = model_IServiceTypeID
        
    @property
    def ecfServiceTypeID(self) -> str:
        return self.__ecfServiceTypeID

    @ecfServiceTypeID.setter
    def ecfServiceTypeID(self, ecfServiceTypeID: str):
        self.__ecfServiceTypeID = ecfServiceTypeID

    @property
    def ecfProtocols(self) -> str:
        return self.__ecfProtocols

    @ecfProtocols.setter
    def ecfProtocols(self, ecfProtocols: str):
        self.__ecfProtocols = ecfProtocols

    @property
    def ecfScopes(self) -> str:
        return self.__ecfScopes

    @ecfScopes.setter
    def ecfScopes(self, ecfScopes: str):
        self.__ecfScopes = ecfScopes

    @property
    def ecfServices(self) -> str:
        return self.__ecfServices

    @ecfServices.setter
    def ecfServices(self, ecfServices: str):
        self.__ecfServices = ecfServices

    @property
    def ecfNamingAuthority(self) -> str:
        return self.__ecfNamingAuthority

    @ecfNamingAuthority.setter
    def ecfNamingAuthority(self, ecfNamingAuthority: str):
        self.__ecfNamingAuthority = ecfNamingAuthority

    @property
    def ecfServiceName(self) -> str:
        return self.__ecfServiceName

    @ecfServiceName.setter
    def ecfServiceName(self, ecfServiceName: str):
        self.__ecfServiceName = ecfServiceName

    @property
    def model_IServiceTypeID(self):
        return self.__model_IServiceTypeID

    @model_IServiceTypeID.setter
    def model_IServiceTypeID(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_IServiceTypeID__model_IServiceTypeID", None)
        self.__model_IServiceTypeID = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_IServiceID6"):
                opp_val = getattr(old_value, "model_IServiceID6", None)
                if opp_val == self:
                    setattr(old_value, "model_IServiceID6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_IServiceID6"):
                opp_val = getattr(value, "model_IServiceID6", None)
                setattr(value, "model_IServiceID6", self)

class model_IServiceID:

    def __init__(self, ecfServiceID: str, ecfServiceName: str, model_IServiceID: "model_IServiceInfo" = None, model_IServiceID6: "model_IServiceTypeID" = None):
        self.ecfServiceID = ecfServiceID
        self.ecfServiceName = ecfServiceName
        self.model_IServiceID = model_IServiceID
        self.model_IServiceID6 = model_IServiceID6
        
    @property
    def ecfServiceID(self) -> str:
        return self.__ecfServiceID

    @ecfServiceID.setter
    def ecfServiceID(self, ecfServiceID: str):
        self.__ecfServiceID = ecfServiceID

    @property
    def ecfServiceName(self) -> str:
        return self.__ecfServiceName

    @ecfServiceName.setter
    def ecfServiceName(self, ecfServiceName: str):
        self.__ecfServiceName = ecfServiceName

    @property
    def model_IServiceID(self):
        return self.__model_IServiceID

    @model_IServiceID.setter
    def model_IServiceID(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_IServiceID__model_IServiceID", None)
        self.__model_IServiceID = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_IServiceInfo"):
                opp_val = getattr(old_value, "model_IServiceInfo", None)
                if opp_val == self:
                    setattr(old_value, "model_IServiceInfo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_IServiceInfo"):
                opp_val = getattr(value, "model_IServiceInfo", None)
                setattr(value, "model_IServiceInfo", self)

    @property
    def model_IServiceID6(self):
        return self.__model_IServiceID6

    @model_IServiceID6.setter
    def model_IServiceID6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_IServiceID__model_IServiceID6", None)
        self.__model_IServiceID6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_IServiceTypeID"):
                opp_val = getattr(old_value, "model_IServiceTypeID", None)
                if opp_val == self:
                    setattr(old_value, "model_IServiceTypeID", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_IServiceTypeID"):
                opp_val = getattr(value, "model_IServiceTypeID", None)
                setattr(value, "model_IServiceTypeID", self)

class model_IServiceInfo:

    def __init__(self, ecfServiceInfo: str, ecfName: str, ecfLocation: str, ecfPriority: int, ecfWeight: int, model_IServiceInfo: "model_IServiceID" = None, model_IServiceInfo4: "model_IHost" = None):
        self.ecfServiceInfo = ecfServiceInfo
        self.ecfName = ecfName
        self.ecfLocation = ecfLocation
        self.ecfPriority = ecfPriority
        self.ecfWeight = ecfWeight
        self.model_IServiceInfo = model_IServiceInfo
        self.model_IServiceInfo4 = model_IServiceInfo4
        
    @property
    def ecfServiceInfo(self) -> str:
        return self.__ecfServiceInfo

    @ecfServiceInfo.setter
    def ecfServiceInfo(self, ecfServiceInfo: str):
        self.__ecfServiceInfo = ecfServiceInfo

    @property
    def ecfName(self) -> str:
        return self.__ecfName

    @ecfName.setter
    def ecfName(self, ecfName: str):
        self.__ecfName = ecfName

    @property
    def ecfPriority(self) -> int:
        return self.__ecfPriority

    @ecfPriority.setter
    def ecfPriority(self, ecfPriority: int):
        self.__ecfPriority = ecfPriority

    @property
    def ecfWeight(self) -> int:
        return self.__ecfWeight

    @ecfWeight.setter
    def ecfWeight(self, ecfWeight: int):
        self.__ecfWeight = ecfWeight

    @property
    def ecfLocation(self) -> str:
        return self.__ecfLocation

    @ecfLocation.setter
    def ecfLocation(self, ecfLocation: str):
        self.__ecfLocation = ecfLocation

    @property
    def model_IServiceInfo4(self):
        return self.__model_IServiceInfo4

    @model_IServiceInfo4.setter
    def model_IServiceInfo4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_IServiceInfo__model_IServiceInfo4", None)
        self.__model_IServiceInfo4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_IHost3"):
                opp_val = getattr(old_value, "model_IHost3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_IHost3"):
                opp_val = getattr(value, "model_IHost3", None)
                if opp_val is None:
                    setattr(value, "model_IHost3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_IServiceInfo(self):
        return self.__model_IServiceInfo

    @model_IServiceInfo.setter
    def model_IServiceInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_IServiceInfo__model_IServiceInfo", None)
        self.__model_IServiceInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_IServiceID"):
                opp_val = getattr(old_value, "model_IServiceID", None)
                if opp_val == self:
                    setattr(old_value, "model_IServiceID", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_IServiceID"):
                opp_val = getattr(value, "model_IServiceID", None)
                setattr(value, "model_IServiceID", self)
