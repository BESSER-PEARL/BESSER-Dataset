from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class netxstudio_Room:

    pass
class netxstudio_Meta:

    pass
class netxstudio_RFSService:

    pass
class netxstudio_Unit:

    pass
class netxstudio_Site:

    pass
class netxstudio_Country:

    pass
class netxstudio_User:

    pass
class netxstudio_Expression:

    pass
class netxstudio_Tolerance:

    pass
class netxstudio_Company:

    pass
class netxstudio_Protocol:

    pass
class netxstudio_Parameter:

    pass
class netxstudio_Metric:

    pass
class netxstudio_Equipment:

    pass
class netxstudio_Function:

    pass
class netxstudio_Network:

    pass
class netxstudio_Library:

    def __init__(self, description: str, name: str, version: str, netxstudio_Library: set["netxstudio_Network"] = None, netxstudio_Library2: set["netxstudio_Function"] = None, netxstudio_Library4: set["netxstudio_Equipment"] = None, netxstudio_Library6: set["netxstudio_Metric"] = None, netxstudio_Library10: set["netxstudio_Protocol"] = None, netxstudio_Library12: set["netxstudio_Company"] = None, netxstudio_Library14: set["netxstudio_Tolerance"] = None, netxstudio_Library16: set["netxstudio_Expression"] = None, netxstudio_Library18: set["netxstudio_User"] = None, netxstudio_Library8: set["netxstudio_Parameter"] = None, netxstudio_Library22: set["netxstudio_Country"] = None, netxstudio_Library24: set["netxstudio_Site"] = None, netxstudio_Library26: set["netxstudio_Unit"] = None, netxstudio_Library28: set["netxstudio_RFSService"] = None, netxstudio_Library30: set["netxstudio_Meta"] = None, netxstudio_Library20: set["netxstudio_Room"] = None):
        self.description = description
        self.name = name
        self.version = version
        self.netxstudio_Library = netxstudio_Library if netxstudio_Library is not None else set()
        self.netxstudio_Library2 = netxstudio_Library2 if netxstudio_Library2 is not None else set()
        self.netxstudio_Library4 = netxstudio_Library4 if netxstudio_Library4 is not None else set()
        self.netxstudio_Library6 = netxstudio_Library6 if netxstudio_Library6 is not None else set()
        self.netxstudio_Library10 = netxstudio_Library10 if netxstudio_Library10 is not None else set()
        self.netxstudio_Library12 = netxstudio_Library12 if netxstudio_Library12 is not None else set()
        self.netxstudio_Library14 = netxstudio_Library14 if netxstudio_Library14 is not None else set()
        self.netxstudio_Library16 = netxstudio_Library16 if netxstudio_Library16 is not None else set()
        self.netxstudio_Library18 = netxstudio_Library18 if netxstudio_Library18 is not None else set()
        self.netxstudio_Library8 = netxstudio_Library8 if netxstudio_Library8 is not None else set()
        self.netxstudio_Library22 = netxstudio_Library22 if netxstudio_Library22 is not None else set()
        self.netxstudio_Library24 = netxstudio_Library24 if netxstudio_Library24 is not None else set()
        self.netxstudio_Library26 = netxstudio_Library26 if netxstudio_Library26 is not None else set()
        self.netxstudio_Library28 = netxstudio_Library28 if netxstudio_Library28 is not None else set()
        self.netxstudio_Library30 = netxstudio_Library30 if netxstudio_Library30 is not None else set()
        self.netxstudio_Library20 = netxstudio_Library20 if netxstudio_Library20 is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def netxstudio_Library2(self):
        return self.__netxstudio_Library2

    @netxstudio_Library2.setter
    def netxstudio_Library2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netxstudio_Library__netxstudio_Library2", None)
        self.__netxstudio_Library2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "netxstudio_Function"):
                    opp_val = getattr(item, "netxstudio_Function", None)
                    
                    if opp_val == self:
                        setattr(item, "netxstudio_Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "netxstudio_Function"):
                    opp_val = getattr(item, "netxstudio_Function", None)
                    
                    setattr(item, "netxstudio_Function", self)
                    

    @property
    def netxstudio_Library4(self):
        return self.__netxstudio_Library4

    @netxstudio_Library4.setter
    def netxstudio_Library4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netxstudio_Library__netxstudio_Library4", None)
        self.__netxstudio_Library4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "netxstudio_Equipment"):
                    opp_val = getattr(item, "netxstudio_Equipment", None)
                    
                    if opp_val == self:
                        setattr(item, "netxstudio_Equipment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "netxstudio_Equipment"):
                    opp_val = getattr(item, "netxstudio_Equipment", None)
                    
                    setattr(item, "netxstudio_Equipment", self)
                    

    @property
    def netxstudio_Library10(self):
        return self.__netxstudio_Library10

    @netxstudio_Library10.setter
    def netxstudio_Library10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netxstudio_Library__netxstudio_Library10", None)
        self.__netxstudio_Library10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "netxstudio_Protocol"):
                    opp_val = getattr(item, "netxstudio_Protocol", None)
                    
                    if opp_val == self:
                        setattr(item, "netxstudio_Protocol", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "netxstudio_Protocol"):
                    opp_val = getattr(item, "netxstudio_Protocol", None)
                    
                    setattr(item, "netxstudio_Protocol", self)
                    

    @property
    def netxstudio_Library30(self):
        return self.__netxstudio_Library30

    @netxstudio_Library30.setter
    def netxstudio_Library30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netxstudio_Library__netxstudio_Library30", None)
        self.__netxstudio_Library30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "netxstudio_Meta"):
                    opp_val = getattr(item, "netxstudio_Meta", None)
                    
                    if opp_val == self:
                        setattr(item, "netxstudio_Meta", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "netxstudio_Meta"):
                    opp_val = getattr(item, "netxstudio_Meta", None)
                    
                    setattr(item, "netxstudio_Meta", self)
                    

    @property
    def netxstudio_Library(self):
        return self.__netxstudio_Library

    @netxstudio_Library.setter
    def netxstudio_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netxstudio_Library__netxstudio_Library", None)
        self.__netxstudio_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "netxstudio_Network"):
                    opp_val = getattr(item, "netxstudio_Network", None)
                    
                    if opp_val == self:
                        setattr(item, "netxstudio_Network", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "netxstudio_Network"):
                    opp_val = getattr(item, "netxstudio_Network", None)
                    
                    setattr(item, "netxstudio_Network", self)
                    

    @property
    def netxstudio_Library24(self):
        return self.__netxstudio_Library24

    @netxstudio_Library24.setter
    def netxstudio_Library24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netxstudio_Library__netxstudio_Library24", None)
        self.__netxstudio_Library24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "netxstudio_Site"):
                    opp_val = getattr(item, "netxstudio_Site", None)
                    
                    if opp_val == self:
                        setattr(item, "netxstudio_Site", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "netxstudio_Site"):
                    opp_val = getattr(item, "netxstudio_Site", None)
                    
                    setattr(item, "netxstudio_Site", self)
                    

    @property
    def netxstudio_Library6(self):
        return self.__netxstudio_Library6

    @netxstudio_Library6.setter
    def netxstudio_Library6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netxstudio_Library__netxstudio_Library6", None)
        self.__netxstudio_Library6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "netxstudio_Metric"):
                    opp_val = getattr(item, "netxstudio_Metric", None)
                    
                    if opp_val == self:
                        setattr(item, "netxstudio_Metric", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "netxstudio_Metric"):
                    opp_val = getattr(item, "netxstudio_Metric", None)
                    
                    setattr(item, "netxstudio_Metric", self)
                    

    @property
    def netxstudio_Library18(self):
        return self.__netxstudio_Library18

    @netxstudio_Library18.setter
    def netxstudio_Library18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netxstudio_Library__netxstudio_Library18", None)
        self.__netxstudio_Library18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "netxstudio_User"):
                    opp_val = getattr(item, "netxstudio_User", None)
                    
                    if opp_val == self:
                        setattr(item, "netxstudio_User", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "netxstudio_User"):
                    opp_val = getattr(item, "netxstudio_User", None)
                    
                    setattr(item, "netxstudio_User", self)
                    

    @property
    def netxstudio_Library8(self):
        return self.__netxstudio_Library8

    @netxstudio_Library8.setter
    def netxstudio_Library8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netxstudio_Library__netxstudio_Library8", None)
        self.__netxstudio_Library8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "netxstudio_Parameter"):
                    opp_val = getattr(item, "netxstudio_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "netxstudio_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "netxstudio_Parameter"):
                    opp_val = getattr(item, "netxstudio_Parameter", None)
                    
                    setattr(item, "netxstudio_Parameter", self)
                    

    @property
    def netxstudio_Library20(self):
        return self.__netxstudio_Library20

    @netxstudio_Library20.setter
    def netxstudio_Library20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netxstudio_Library__netxstudio_Library20", None)
        self.__netxstudio_Library20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "netxstudio_Room"):
                    opp_val = getattr(item, "netxstudio_Room", None)
                    
                    if opp_val == self:
                        setattr(item, "netxstudio_Room", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "netxstudio_Room"):
                    opp_val = getattr(item, "netxstudio_Room", None)
                    
                    setattr(item, "netxstudio_Room", self)
                    

    @property
    def netxstudio_Library16(self):
        return self.__netxstudio_Library16

    @netxstudio_Library16.setter
    def netxstudio_Library16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netxstudio_Library__netxstudio_Library16", None)
        self.__netxstudio_Library16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "netxstudio_Expression"):
                    opp_val = getattr(item, "netxstudio_Expression", None)
                    
                    if opp_val == self:
                        setattr(item, "netxstudio_Expression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "netxstudio_Expression"):
                    opp_val = getattr(item, "netxstudio_Expression", None)
                    
                    setattr(item, "netxstudio_Expression", self)
                    

    @property
    def netxstudio_Library28(self):
        return self.__netxstudio_Library28

    @netxstudio_Library28.setter
    def netxstudio_Library28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netxstudio_Library__netxstudio_Library28", None)
        self.__netxstudio_Library28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "netxstudio_RFSService"):
                    opp_val = getattr(item, "netxstudio_RFSService", None)
                    
                    if opp_val == self:
                        setattr(item, "netxstudio_RFSService", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "netxstudio_RFSService"):
                    opp_val = getattr(item, "netxstudio_RFSService", None)
                    
                    setattr(item, "netxstudio_RFSService", self)
                    

    @property
    def netxstudio_Library12(self):
        return self.__netxstudio_Library12

    @netxstudio_Library12.setter
    def netxstudio_Library12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netxstudio_Library__netxstudio_Library12", None)
        self.__netxstudio_Library12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "netxstudio_Company"):
                    opp_val = getattr(item, "netxstudio_Company", None)
                    
                    if opp_val == self:
                        setattr(item, "netxstudio_Company", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "netxstudio_Company"):
                    opp_val = getattr(item, "netxstudio_Company", None)
                    
                    setattr(item, "netxstudio_Company", self)
                    

    @property
    def netxstudio_Library26(self):
        return self.__netxstudio_Library26

    @netxstudio_Library26.setter
    def netxstudio_Library26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netxstudio_Library__netxstudio_Library26", None)
        self.__netxstudio_Library26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "netxstudio_Unit"):
                    opp_val = getattr(item, "netxstudio_Unit", None)
                    
                    if opp_val == self:
                        setattr(item, "netxstudio_Unit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "netxstudio_Unit"):
                    opp_val = getattr(item, "netxstudio_Unit", None)
                    
                    setattr(item, "netxstudio_Unit", self)
                    

    @property
    def netxstudio_Library14(self):
        return self.__netxstudio_Library14

    @netxstudio_Library14.setter
    def netxstudio_Library14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netxstudio_Library__netxstudio_Library14", None)
        self.__netxstudio_Library14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "netxstudio_Tolerance"):
                    opp_val = getattr(item, "netxstudio_Tolerance", None)
                    
                    if opp_val == self:
                        setattr(item, "netxstudio_Tolerance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "netxstudio_Tolerance"):
                    opp_val = getattr(item, "netxstudio_Tolerance", None)
                    
                    setattr(item, "netxstudio_Tolerance", self)
                    

    @property
    def netxstudio_Library22(self):
        return self.__netxstudio_Library22

    @netxstudio_Library22.setter
    def netxstudio_Library22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netxstudio_Library__netxstudio_Library22", None)
        self.__netxstudio_Library22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "netxstudio_Country"):
                    opp_val = getattr(item, "netxstudio_Country", None)
                    
                    if opp_val == self:
                        setattr(item, "netxstudio_Country", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "netxstudio_Country"):
                    opp_val = getattr(item, "netxstudio_Country", None)
                    
                    setattr(item, "netxstudio_Country", self)
                    
