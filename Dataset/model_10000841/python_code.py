from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class SolarPanel:

    def __init__(self, SPID: int, IoT_based_Smart_Resort_System_SolarPanel_119: "IoT_based_Smart_Resort_System" = None):
        self.SPID = SPID
        self.IoT_based_Smart_Resort_System_SolarPanel_119 = IoT_based_Smart_Resort_System_SolarPanel_119
        
        pass
    @property
    def SPID(self):
        return self.__SPID
    @SPID.setter
    def SPID(self, SPID: int):
        self.__SPID = SPID

    @property
    def IoT_based_Smart_Resort_System_SolarPanel_119(self):
        return self.__IoT_based_Smart_Resort_System_SolarPanel_119
    @IoT_based_Smart_Resort_System_SolarPanel_119.setter
    def IoT_based_Smart_Resort_System_SolarPanel_119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolarPanel__IoT_based_Smart_Resort_System_SolarPanel_119", None)
        self.__IoT_based_Smart_Resort_System_SolarPanel_119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IoT_based_Smart_Resort_System_SolarPanel_018"):
                opp_val = getattr(old_value, "IoT_based_Smart_Resort_System_SolarPanel_018", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IoT_based_Smart_Resort_System_SolarPanel_018"):
                opp_val = getattr(value, "IoT_based_Smart_Resort_System_SolarPanel_018", None)
                if opp_val is None:
                    setattr(value, "IoT_based_Smart_Resort_System_SolarPanel_018", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Security_Guard_Police:

    def __init__(self, sgpID: int, Security_Guard_Police_Alert_016: "Alert" = None):
        self.sgpID = sgpID
        self.Security_Guard_Police_Alert_016 = Security_Guard_Police_Alert_016
        
        pass
    @property
    def sgpID(self):
        return self.__sgpID
    @sgpID.setter
    def sgpID(self, sgpID: int):
        self.__sgpID = sgpID

    @property
    def Security_Guard_Police_Alert_016(self):
        return self.__Security_Guard_Police_Alert_016
    @Security_Guard_Police_Alert_016.setter
    def Security_Guard_Police_Alert_016(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Security_Guard_Police__Security_Guard_Police_Alert_016", None)
        self.__Security_Guard_Police_Alert_016 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Security_Guard_Police_Alert_117"):
                opp_val = getattr(old_value, "Security_Guard_Police_Alert_117", None)
                if opp_val == self:
                    setattr(old_value, "Security_Guard_Police_Alert_117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Security_Guard_Police_Alert_117"):
                opp_val = getattr(value, "Security_Guard_Police_Alert_117", None)
                setattr(value, "Security_Guard_Police_Alert_117", self)



class User_Home_Owner:

    def __init__(self, UserID: int, User_Home_Owner_Alert_014: "Alert" = None):
        self.UserID = UserID
        self.User_Home_Owner_Alert_014 = User_Home_Owner_Alert_014
        
        pass
    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: int):
        self.__UserID = UserID

    @property
    def User_Home_Owner_Alert_014(self):
        return self.__User_Home_Owner_Alert_014
    @User_Home_Owner_Alert_014.setter
    def User_Home_Owner_Alert_014(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User_Home_Owner__User_Home_Owner_Alert_014", None)
        self.__User_Home_Owner_Alert_014 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User_Home_Owner_Alert_115"):
                opp_val = getattr(old_value, "User_Home_Owner_Alert_115", None)
                if opp_val == self:
                    setattr(old_value, "User_Home_Owner_Alert_115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User_Home_Owner_Alert_115"):
                opp_val = getattr(value, "User_Home_Owner_Alert_115", None)
                setattr(value, "User_Home_Owner_Alert_115", self)



class HomeAppliances:

    def __init__(self, HAID: int, speakers0: "Fans" = None, system8: "IoT_based_Smart_Resort_System" = None, HomeAppliances_Light_010: "Light" = None, HomeAppliances_Door_012: "Door" = None):
        self.HAID = HAID
        self.speakers0 = speakers0
        self.system8 = system8
        self.HomeAppliances_Light_010 = HomeAppliances_Light_010
        self.HomeAppliances_Door_012 = HomeAppliances_Door_012
        
        pass
    @property
    def HAID(self):
        return self.__HAID
    @HAID.setter
    def HAID(self, HAID: int):
        self.__HAID = HAID

    @property
    def HomeAppliances_Light_010(self):
        return self.__HomeAppliances_Light_010
    @HomeAppliances_Light_010.setter
    def HomeAppliances_Light_010(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HomeAppliances__HomeAppliances_Light_010", None)
        self.__HomeAppliances_Light_010 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HomeAppliances_Light_111"):
                opp_val = getattr(old_value, "HomeAppliances_Light_111", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HomeAppliances_Light_111"):
                opp_val = getattr(value, "HomeAppliances_Light_111", None)
                if opp_val is None:
                    setattr(value, "HomeAppliances_Light_111", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def speakers0(self):
        return self.__speakers0
    @speakers0.setter
    def speakers0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HomeAppliances__speakers0", None)
        self.__speakers0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "homeTheatre1"):
                opp_val = getattr(old_value, "homeTheatre1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "homeTheatre1"):
                opp_val = getattr(value, "homeTheatre1", None)
                if opp_val is None:
                    setattr(value, "homeTheatre1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def HomeAppliances_Door_012(self):
        return self.__HomeAppliances_Door_012
    @HomeAppliances_Door_012.setter
    def HomeAppliances_Door_012(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HomeAppliances__HomeAppliances_Door_012", None)
        self.__HomeAppliances_Door_012 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HomeAppliances_Door_113"):
                opp_val = getattr(old_value, "HomeAppliances_Door_113", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HomeAppliances_Door_113"):
                opp_val = getattr(value, "HomeAppliances_Door_113", None)
                if opp_val is None:
                    setattr(value, "HomeAppliances_Door_113", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def system8(self):
        return self.__system8
    @system8.setter
    def system8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HomeAppliances__system8", None)
        self.__system8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "homeTheatre9"):
                opp_val = getattr(old_value, "homeTheatre9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "homeTheatre9"):
                opp_val = getattr(value, "homeTheatre9", None)
                if opp_val is None:
                    setattr(value, "homeTheatre9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Light:

    def __init__(self, LightID: str, HomeAppliances_Light_111: set["HomeAppliances"] = None):
        self.LightID = LightID
        self.HomeAppliances_Light_111 = HomeAppliances_Light_111 if HomeAppliances_Light_111 is not None else set()
        
        pass
    @property
    def LightID(self):
        return self.__LightID
    @LightID.setter
    def LightID(self, LightID: str):
        self.__LightID = LightID

    @property
    def HomeAppliances_Light_111(self):
        return self.__HomeAppliances_Light_111
    @HomeAppliances_Light_111.setter
    def HomeAppliances_Light_111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Light__HomeAppliances_Light_111", None)
        self.__HomeAppliances_Light_111 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HomeAppliances_Light_010"):
                    opp_val = getattr(item, "HomeAppliances_Light_010", None)
                    
                    if opp_val == self:
                        setattr(item, "HomeAppliances_Light_010", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HomeAppliances_Light_010"):
                    opp_val = getattr(item, "HomeAppliances_Light_010", None)
                    
                    setattr(item, "HomeAppliances_Light_010", self)
                    



class Gardening:

    def __init__(self, GID: int, system2: "IoT_based_Smart_Resort_System" = None):
        self.GID = GID
        self.system2 = system2
        
        pass
    @property
    def GID(self):
        return self.__GID
    @GID.setter
    def GID(self, GID: int):
        self.__GID = GID

    @property
    def system2(self):
        return self.__system2
    @system2.setter
    def system2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Gardening__system2", None)
        self.__system2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "microPhone3"):
                opp_val = getattr(old_value, "microPhone3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "microPhone3"):
                opp_val = getattr(value, "microPhone3", None)
                if opp_val is None:
                    setattr(value, "microPhone3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Fans:

    def __init__(self, FANID: int, homeTheatre1: set["HomeAppliances"] = None):
        self.FANID = FANID
        self.homeTheatre1 = homeTheatre1 if homeTheatre1 is not None else set()
        
        pass
    @property
    def FANID(self):
        return self.__FANID
    @FANID.setter
    def FANID(self, FANID: int):
        self.__FANID = FANID

    @property
    def homeTheatre1(self):
        return self.__homeTheatre1
    @homeTheatre1.setter
    def homeTheatre1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Fans__homeTheatre1", None)
        self.__homeTheatre1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "speakers0"):
                    opp_val = getattr(item, "speakers0", None)
                    
                    if opp_val == self:
                        setattr(item, "speakers0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "speakers0"):
                    opp_val = getattr(item, "speakers0", None)
                    
                    setattr(item, "speakers0", self)
                    



class Door:

    def __init__(self, DoorID: int, HomeAppliances_Door_113: set["HomeAppliances"] = None):
        self.DoorID = DoorID
        self.HomeAppliances_Door_113 = HomeAppliances_Door_113 if HomeAppliances_Door_113 is not None else set()
        
        pass
    @property
    def DoorID(self):
        return self.__DoorID
    @DoorID.setter
    def DoorID(self, DoorID: int):
        self.__DoorID = DoorID

    @property
    def HomeAppliances_Door_113(self):
        return self.__HomeAppliances_Door_113
    @HomeAppliances_Door_113.setter
    def HomeAppliances_Door_113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Door__HomeAppliances_Door_113", None)
        self.__HomeAppliances_Door_113 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HomeAppliances_Door_012"):
                    opp_val = getattr(item, "HomeAppliances_Door_012", None)
                    
                    if opp_val == self:
                        setattr(item, "HomeAppliances_Door_012", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HomeAppliances_Door_012"):
                    opp_val = getattr(item, "HomeAppliances_Door_012", None)
                    
                    setattr(item, "HomeAppliances_Door_012", self)
                    



class Alert:

    def __init__(self, AlertID: int, home_Security_System5: "Home_Security_System" = None, User_Home_Owner_Alert_115: "User_Home_Owner" = None, Security_Guard_Police_Alert_117: "Security_Guard_Police" = None):
        self.AlertID = AlertID
        self.home_Security_System5 = home_Security_System5
        self.User_Home_Owner_Alert_115 = User_Home_Owner_Alert_115
        self.Security_Guard_Police_Alert_117 = Security_Guard_Police_Alert_117
        
        pass
    @property
    def AlertID(self):
        return self.__AlertID
    @AlertID.setter
    def AlertID(self, AlertID: int):
        self.__AlertID = AlertID

    @property
    def home_Security_System5(self):
        return self.__home_Security_System5
    @home_Security_System5.setter
    def home_Security_System5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Alert__home_Security_System5", None)
        self.__home_Security_System5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alert4"):
                opp_val = getattr(old_value, "alert4", None)
                if opp_val == self:
                    setattr(old_value, "alert4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alert4"):
                opp_val = getattr(value, "alert4", None)
                setattr(value, "alert4", self)

    @property
    def Security_Guard_Police_Alert_117(self):
        return self.__Security_Guard_Police_Alert_117
    @Security_Guard_Police_Alert_117.setter
    def Security_Guard_Police_Alert_117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Alert__Security_Guard_Police_Alert_117", None)
        self.__Security_Guard_Police_Alert_117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Security_Guard_Police_Alert_016"):
                opp_val = getattr(old_value, "Security_Guard_Police_Alert_016", None)
                if opp_val == self:
                    setattr(old_value, "Security_Guard_Police_Alert_016", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Security_Guard_Police_Alert_016"):
                opp_val = getattr(value, "Security_Guard_Police_Alert_016", None)
                setattr(value, "Security_Guard_Police_Alert_016", self)

    @property
    def User_Home_Owner_Alert_115(self):
        return self.__User_Home_Owner_Alert_115
    @User_Home_Owner_Alert_115.setter
    def User_Home_Owner_Alert_115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Alert__User_Home_Owner_Alert_115", None)
        self.__User_Home_Owner_Alert_115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User_Home_Owner_Alert_014"):
                opp_val = getattr(old_value, "User_Home_Owner_Alert_014", None)
                if opp_val == self:
                    setattr(old_value, "User_Home_Owner_Alert_014", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User_Home_Owner_Alert_014"):
                opp_val = getattr(value, "User_Home_Owner_Alert_014", None)
                setattr(value, "User_Home_Owner_Alert_014", self)



class Home_Security_System:

    def __init__(self, UserID: int, alert4: "Alert" = None, IoT_based_Smart_Resort_System_Home_Security_System_121: "IoT_based_Smart_Resort_System" = None):
        self.UserID = UserID
        self.alert4 = alert4
        self.IoT_based_Smart_Resort_System_Home_Security_System_121 = IoT_based_Smart_Resort_System_Home_Security_System_121
        
        pass
    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: int):
        self.__UserID = UserID

    @property
    def IoT_based_Smart_Resort_System_Home_Security_System_121(self):
        return self.__IoT_based_Smart_Resort_System_Home_Security_System_121
    @IoT_based_Smart_Resort_System_Home_Security_System_121.setter
    def IoT_based_Smart_Resort_System_Home_Security_System_121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Home_Security_System__IoT_based_Smart_Resort_System_Home_Security_System_121", None)
        self.__IoT_based_Smart_Resort_System_Home_Security_System_121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IoT_based_Smart_Resort_System_Home_Security_System_020"):
                opp_val = getattr(old_value, "IoT_based_Smart_Resort_System_Home_Security_System_020", None)
                if opp_val == self:
                    setattr(old_value, "IoT_based_Smart_Resort_System_Home_Security_System_020", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IoT_based_Smart_Resort_System_Home_Security_System_020"):
                opp_val = getattr(value, "IoT_based_Smart_Resort_System_Home_Security_System_020", None)
                setattr(value, "IoT_based_Smart_Resort_System_Home_Security_System_020", self)

    @property
    def alert4(self):
        return self.__alert4
    @alert4.setter
    def alert4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Home_Security_System__alert4", None)
        self.__alert4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "home_Security_System5"):
                opp_val = getattr(old_value, "home_Security_System5", None)
                if opp_val == self:
                    setattr(old_value, "home_Security_System5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "home_Security_System5"):
                opp_val = getattr(value, "home_Security_System5", None)
                setattr(value, "home_Security_System5", self)



class MoistureSensor:

    pass


class Motion_Sensor:

    pass


class Sensor:

    def __init__(self, SensorID: int, SensorType: int, system6: "IoT_based_Smart_Resort_System" = None):
        self.SensorID = SensorID
        self.SensorType = SensorType
        self.system6 = system6
        
        pass
    @property
    def SensorID(self):
        return self.__SensorID
    @SensorID.setter
    def SensorID(self, SensorID: int):
        self.__SensorID = SensorID

    @property
    def SensorType(self):
        return self.__SensorType
    @SensorType.setter
    def SensorType(self, SensorType: int):
        self.__SensorType = SensorType

    @property
    def system6(self):
        return self.__system6
    @system6.setter
    def system6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sensor__system6", None)
        self.__system6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sensor7"):
                opp_val = getattr(old_value, "sensor7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sensor7"):
                opp_val = getattr(value, "sensor7", None)
                if opp_val is None:
                    setattr(value, "sensor7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class IoT_based_Smart_Resort_System:

    def __init__(self, Status: bool, Update: float, microPhone3: set["Gardening"] = None, sensor7: set["Sensor"] = None, homeTheatre9: set["HomeAppliances"] = None, IoT_based_Smart_Resort_System_SolarPanel_018: set["SolarPanel"] = None, IoT_based_Smart_Resort_System_Home_Security_System_020: "Home_Security_System" = None):
        self.Status = Status
        self.Update = Update
        self.microPhone3 = microPhone3 if microPhone3 is not None else set()
        self.sensor7 = sensor7 if sensor7 is not None else set()
        self.homeTheatre9 = homeTheatre9 if homeTheatre9 is not None else set()
        self.IoT_based_Smart_Resort_System_SolarPanel_018 = IoT_based_Smart_Resort_System_SolarPanel_018 if IoT_based_Smart_Resort_System_SolarPanel_018 is not None else set()
        self.IoT_based_Smart_Resort_System_Home_Security_System_020 = IoT_based_Smart_Resort_System_Home_Security_System_020
        
        pass
    @property
    def Update(self):
        return self.__Update
    @Update.setter
    def Update(self, Update: float):
        self.__Update = Update

    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: bool):
        self.__Status = Status

    @property
    def microPhone3(self):
        return self.__microPhone3
    @microPhone3.setter
    def microPhone3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IoT_based_Smart_Resort_System__microPhone3", None)
        self.__microPhone3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "system2"):
                    opp_val = getattr(item, "system2", None)
                    
                    if opp_val == self:
                        setattr(item, "system2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "system2"):
                    opp_val = getattr(item, "system2", None)
                    
                    setattr(item, "system2", self)
                    

    @property
    def homeTheatre9(self):
        return self.__homeTheatre9
    @homeTheatre9.setter
    def homeTheatre9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IoT_based_Smart_Resort_System__homeTheatre9", None)
        self.__homeTheatre9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "system8"):
                    opp_val = getattr(item, "system8", None)
                    
                    if opp_val == self:
                        setattr(item, "system8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "system8"):
                    opp_val = getattr(item, "system8", None)
                    
                    setattr(item, "system8", self)
                    

    @property
    def IoT_based_Smart_Resort_System_Home_Security_System_020(self):
        return self.__IoT_based_Smart_Resort_System_Home_Security_System_020
    @IoT_based_Smart_Resort_System_Home_Security_System_020.setter
    def IoT_based_Smart_Resort_System_Home_Security_System_020(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IoT_based_Smart_Resort_System__IoT_based_Smart_Resort_System_Home_Security_System_020", None)
        self.__IoT_based_Smart_Resort_System_Home_Security_System_020 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IoT_based_Smart_Resort_System_Home_Security_System_121"):
                opp_val = getattr(old_value, "IoT_based_Smart_Resort_System_Home_Security_System_121", None)
                if opp_val == self:
                    setattr(old_value, "IoT_based_Smart_Resort_System_Home_Security_System_121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IoT_based_Smart_Resort_System_Home_Security_System_121"):
                opp_val = getattr(value, "IoT_based_Smart_Resort_System_Home_Security_System_121", None)
                setattr(value, "IoT_based_Smart_Resort_System_Home_Security_System_121", self)

    @property
    def sensor7(self):
        return self.__sensor7
    @sensor7.setter
    def sensor7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IoT_based_Smart_Resort_System__sensor7", None)
        self.__sensor7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "system6"):
                    opp_val = getattr(item, "system6", None)
                    
                    if opp_val == self:
                        setattr(item, "system6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "system6"):
                    opp_val = getattr(item, "system6", None)
                    
                    setattr(item, "system6", self)
                    

    @property
    def IoT_based_Smart_Resort_System_SolarPanel_018(self):
        return self.__IoT_based_Smart_Resort_System_SolarPanel_018
    @IoT_based_Smart_Resort_System_SolarPanel_018.setter
    def IoT_based_Smart_Resort_System_SolarPanel_018(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IoT_based_Smart_Resort_System__IoT_based_Smart_Resort_System_SolarPanel_018", None)
        self.__IoT_based_Smart_Resort_System_SolarPanel_018 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IoT_based_Smart_Resort_System_SolarPanel_119"):
                    opp_val = getattr(item, "IoT_based_Smart_Resort_System_SolarPanel_119", None)
                    
                    if opp_val == self:
                        setattr(item, "IoT_based_Smart_Resort_System_SolarPanel_119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IoT_based_Smart_Resort_System_SolarPanel_119"):
                    opp_val = getattr(item, "IoT_based_Smart_Resort_System_SolarPanel_119", None)
                    
                    setattr(item, "IoT_based_Smart_Resort_System_SolarPanel_119", self)
                    

