from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Sensors_Actor:

    pass


class Fire_Department__Actor:

    pass


class Building_Owner__Actor:

    pass





class Set_time_external:

    pass


class View_sensors_data_external:

    pass


class Sense_and_Update_Data_external:

    pass


class Disable_detector_external:

    pass


class Add_new_alarm_external:

    pass


class Notify_User_of_fire_external:

    pass


class WebPage:

    def __init__(self, TempValue: float, HomeLoc: str, People_: int, OwnerData: str, SmokeValue: float, Firebase_Web_17: "Firebase" = None):
        self.TempValue = TempValue
        self.HomeLoc = HomeLoc
        self.People_ = People_
        self.OwnerData = OwnerData
        self.SmokeValue = SmokeValue
        self.Firebase_Web_17 = Firebase_Web_17
        
        pass
    @property
    def HomeLoc(self):
        return self.__HomeLoc
    @HomeLoc.setter
    def HomeLoc(self, HomeLoc: str):
        self.__HomeLoc = HomeLoc

    @property
    def SmokeValue(self):
        return self.__SmokeValue
    @SmokeValue.setter
    def SmokeValue(self, SmokeValue: float):
        self.__SmokeValue = SmokeValue

    @property
    def People_(self):
        return self.__People_
    @People_.setter
    def People_(self, People_: int):
        self.__People_ = People_

    @property
    def OwnerData(self):
        return self.__OwnerData
    @OwnerData.setter
    def OwnerData(self, OwnerData: str):
        self.__OwnerData = OwnerData

    @property
    def TempValue(self):
        return self.__TempValue
    @TempValue.setter
    def TempValue(self, TempValue: float):
        self.__TempValue = TempValue

    @property
    def Firebase_Web_17(self):
        return self.__Firebase_Web_17
    @Firebase_Web_17.setter
    def Firebase_Web_17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebPage__Firebase_Web_17", None)
        self.__Firebase_Web_17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Firebase_Web_06"):
                opp_val = getattr(old_value, "Firebase_Web_06", None)
                if opp_val == self:
                    setattr(old_value, "Firebase_Web_06", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Firebase_Web_06"):
                opp_val = getattr(value, "Firebase_Web_06", None)
                setattr(value, "Firebase_Web_06", self)



class Alarm:

    def __init__(self, AlarmID: str, Notification_Alarm_121: "Notification" = None, ViewTemp_Smoke_Alarm_123: "ViewTemp_Smoke" = None, AddAlarm_Alarm_125: "AddAlarm" = None, TurnDownAlarm_Alarm_127: "TurnDownAlarm" = None, Alarm_Mobile_App_028: "MobileApp" = None):
        self.AlarmID = AlarmID
        self.Notification_Alarm_121 = Notification_Alarm_121
        self.ViewTemp_Smoke_Alarm_123 = ViewTemp_Smoke_Alarm_123
        self.AddAlarm_Alarm_125 = AddAlarm_Alarm_125
        self.TurnDownAlarm_Alarm_127 = TurnDownAlarm_Alarm_127
        self.Alarm_Mobile_App_028 = Alarm_Mobile_App_028
        
        pass
    @property
    def AlarmID(self):
        return self.__AlarmID
    @AlarmID.setter
    def AlarmID(self, AlarmID: str):
        self.__AlarmID = AlarmID

    @property
    def Notification_Alarm_121(self):
        return self.__Notification_Alarm_121
    @Notification_Alarm_121.setter
    def Notification_Alarm_121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Alarm__Notification_Alarm_121", None)
        self.__Notification_Alarm_121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Notification_Alarm_020"):
                opp_val = getattr(old_value, "Notification_Alarm_020", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Notification_Alarm_020"):
                opp_val = getattr(value, "Notification_Alarm_020", None)
                if opp_val is None:
                    setattr(value, "Notification_Alarm_020", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Alarm_Mobile_App_028(self):
        return self.__Alarm_Mobile_App_028
    @Alarm_Mobile_App_028.setter
    def Alarm_Mobile_App_028(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Alarm__Alarm_Mobile_App_028", None)
        self.__Alarm_Mobile_App_028 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Alarm_Mobile_App_129"):
                opp_val = getattr(old_value, "Alarm_Mobile_App_129", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Alarm_Mobile_App_129"):
                opp_val = getattr(value, "Alarm_Mobile_App_129", None)
                if opp_val is None:
                    setattr(value, "Alarm_Mobile_App_129", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def AddAlarm_Alarm_125(self):
        return self.__AddAlarm_Alarm_125
    @AddAlarm_Alarm_125.setter
    def AddAlarm_Alarm_125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Alarm__AddAlarm_Alarm_125", None)
        self.__AddAlarm_Alarm_125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AddAlarm_Alarm_024"):
                opp_val = getattr(old_value, "AddAlarm_Alarm_024", None)
                if opp_val == self:
                    setattr(old_value, "AddAlarm_Alarm_024", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AddAlarm_Alarm_024"):
                opp_val = getattr(value, "AddAlarm_Alarm_024", None)
                setattr(value, "AddAlarm_Alarm_024", self)

    @property
    def TurnDownAlarm_Alarm_127(self):
        return self.__TurnDownAlarm_Alarm_127
    @TurnDownAlarm_Alarm_127.setter
    def TurnDownAlarm_Alarm_127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Alarm__TurnDownAlarm_Alarm_127", None)
        self.__TurnDownAlarm_Alarm_127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TurnDownAlarm_Alarm_026"):
                opp_val = getattr(old_value, "TurnDownAlarm_Alarm_026", None)
                if opp_val == self:
                    setattr(old_value, "TurnDownAlarm_Alarm_026", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TurnDownAlarm_Alarm_026"):
                opp_val = getattr(value, "TurnDownAlarm_Alarm_026", None)
                setattr(value, "TurnDownAlarm_Alarm_026", self)

    @property
    def ViewTemp_Smoke_Alarm_123(self):
        return self.__ViewTemp_Smoke_Alarm_123
    @ViewTemp_Smoke_Alarm_123.setter
    def ViewTemp_Smoke_Alarm_123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Alarm__ViewTemp_Smoke_Alarm_123", None)
        self.__ViewTemp_Smoke_Alarm_123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ViewTemp_Smoke_Alarm_022"):
                opp_val = getattr(old_value, "ViewTemp_Smoke_Alarm_022", None)
                if opp_val == self:
                    setattr(old_value, "ViewTemp_Smoke_Alarm_022", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ViewTemp_Smoke_Alarm_022"):
                opp_val = getattr(value, "ViewTemp_Smoke_Alarm_022", None)
                setattr(value, "ViewTemp_Smoke_Alarm_022", self)



class ViewTemp_Smoke:

    def __init__(self, TempValue: float, SmokeValue: float, ViewTemp_Smoke_Alarm_022: "Alarm" = None):
        self.TempValue = TempValue
        self.SmokeValue = SmokeValue
        self.ViewTemp_Smoke_Alarm_022 = ViewTemp_Smoke_Alarm_022
        
        pass
    @property
    def SmokeValue(self):
        return self.__SmokeValue
    @SmokeValue.setter
    def SmokeValue(self, SmokeValue: float):
        self.__SmokeValue = SmokeValue

    @property
    def TempValue(self):
        return self.__TempValue
    @TempValue.setter
    def TempValue(self, TempValue: float):
        self.__TempValue = TempValue

    @property
    def ViewTemp_Smoke_Alarm_022(self):
        return self.__ViewTemp_Smoke_Alarm_022
    @ViewTemp_Smoke_Alarm_022.setter
    def ViewTemp_Smoke_Alarm_022(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ViewTemp_Smoke__ViewTemp_Smoke_Alarm_022", None)
        self.__ViewTemp_Smoke_Alarm_022 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ViewTemp_Smoke_Alarm_123"):
                opp_val = getattr(old_value, "ViewTemp_Smoke_Alarm_123", None)
                if opp_val == self:
                    setattr(old_value, "ViewTemp_Smoke_Alarm_123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ViewTemp_Smoke_Alarm_123"):
                opp_val = getattr(value, "ViewTemp_Smoke_Alarm_123", None)
                setattr(value, "ViewTemp_Smoke_Alarm_123", self)



class AddAlarm:

    def __init__(self, AlarmName: str, AddAlarm_Alarm_024: "Alarm" = None):
        self.AlarmName = AlarmName
        self.AddAlarm_Alarm_024 = AddAlarm_Alarm_024
        
        pass
    @property
    def AlarmName(self):
        return self.__AlarmName
    @AlarmName.setter
    def AlarmName(self, AlarmName: str):
        self.__AlarmName = AlarmName

    @property
    def AddAlarm_Alarm_024(self):
        return self.__AddAlarm_Alarm_024
    @AddAlarm_Alarm_024.setter
    def AddAlarm_Alarm_024(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AddAlarm__AddAlarm_Alarm_024", None)
        self.__AddAlarm_Alarm_024 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AddAlarm_Alarm_125"):
                opp_val = getattr(old_value, "AddAlarm_Alarm_125", None)
                if opp_val == self:
                    setattr(old_value, "AddAlarm_Alarm_125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AddAlarm_Alarm_125"):
                opp_val = getattr(value, "AddAlarm_Alarm_125", None)
                setattr(value, "AddAlarm_Alarm_125", self)



class TurnDownAlarm:

    pass


class Fire_Alarm_System__Component:

    pass


class Arduino:

    pass


class Count_Sensor:

    def __init__(self, People_: int):
        self.People_ = People_
        
        pass
    @property
    def People_(self):
        return self.__People_
    @People_.setter
    def People_(self, People_: int):
        self.__People_ = People_



class Notification:

    def __init__(self, TempThreshold: float, SmokeThreshold: float, Notification_Alarm_020: set["Alarm"] = None):
        self.TempThreshold = TempThreshold
        self.SmokeThreshold = SmokeThreshold
        self.Notification_Alarm_020 = Notification_Alarm_020 if Notification_Alarm_020 is not None else set()
        
        pass
    @property
    def SmokeThreshold(self):
        return self.__SmokeThreshold
    @SmokeThreshold.setter
    def SmokeThreshold(self, SmokeThreshold: float):
        self.__SmokeThreshold = SmokeThreshold

    @property
    def TempThreshold(self):
        return self.__TempThreshold
    @TempThreshold.setter
    def TempThreshold(self, TempThreshold: float):
        self.__TempThreshold = TempThreshold

    @property
    def Notification_Alarm_020(self):
        return self.__Notification_Alarm_020
    @Notification_Alarm_020.setter
    def Notification_Alarm_020(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Notification__Notification_Alarm_020", None)
        self.__Notification_Alarm_020 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Notification_Alarm_121"):
                    opp_val = getattr(item, "Notification_Alarm_121", None)
                    
                    if opp_val == self:
                        setattr(item, "Notification_Alarm_121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Notification_Alarm_121"):
                    opp_val = getattr(item, "Notification_Alarm_121", None)
                    
                    setattr(item, "Notification_Alarm_121", self)
                    



class MobileApp:

    def __init__(self, UserID: int, AlarmID: int, Home_Security_System_System_02: "Firebase" = None, Alarm_Mobile_App_129: set["Alarm"] = None):
        self.UserID = UserID
        self.AlarmID = AlarmID
        self.Home_Security_System_System_02 = Home_Security_System_System_02
        self.Alarm_Mobile_App_129 = Alarm_Mobile_App_129 if Alarm_Mobile_App_129 is not None else set()
        
        pass
    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: int):
        self.__UserID = UserID

    @property
    def AlarmID(self):
        return self.__AlarmID
    @AlarmID.setter
    def AlarmID(self, AlarmID: int):
        self.__AlarmID = AlarmID

    @property
    def Alarm_Mobile_App_129(self):
        return self.__Alarm_Mobile_App_129
    @Alarm_Mobile_App_129.setter
    def Alarm_Mobile_App_129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MobileApp__Alarm_Mobile_App_129", None)
        self.__Alarm_Mobile_App_129 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Alarm_Mobile_App_028"):
                    opp_val = getattr(item, "Alarm_Mobile_App_028", None)
                    
                    if opp_val == self:
                        setattr(item, "Alarm_Mobile_App_028", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Alarm_Mobile_App_028"):
                    opp_val = getattr(item, "Alarm_Mobile_App_028", None)
                    
                    setattr(item, "Alarm_Mobile_App_028", self)
                    

    @property
    def Home_Security_System_System_02(self):
        return self.__Home_Security_System_System_02
    @Home_Security_System_System_02.setter
    def Home_Security_System_System_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MobileApp__Home_Security_System_System_02", None)
        self.__Home_Security_System_System_02 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Home_Security_System_System_13"):
                opp_val = getattr(old_value, "Home_Security_System_System_13", None)
                if opp_val == self:
                    setattr(old_value, "Home_Security_System_System_13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Home_Security_System_System_13"):
                opp_val = getattr(value, "Home_Security_System_System_13", None)
                setattr(value, "Home_Security_System_System_13", self)



class Temperature_Sensor:

    pass


class Gas_Smoke_Sensor:

    def __init__(self, SmokeAlarm: bool, CheckSmoke: bool):
        self.SmokeAlarm = SmokeAlarm
        self.CheckSmoke = CheckSmoke
        
        pass
    @property
    def SmokeAlarm(self):
        return self.__SmokeAlarm
    @SmokeAlarm.setter
    def SmokeAlarm(self, SmokeAlarm: bool):
        self.__SmokeAlarm = SmokeAlarm

    @property
    def CheckSmoke(self):
        return self.__CheckSmoke
    @CheckSmoke.setter
    def CheckSmoke(self, CheckSmoke: bool):
        self.__CheckSmoke = CheckSmoke



class Sensor:

    def __init__(self, SensorID: int, SensorType: int, system0: "Arduino" = None):
        self.SensorID = SensorID
        self.SensorType = SensorType
        self.system0 = system0
        
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
    def system0(self):
        return self.__system0
    @system0.setter
    def system0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sensor__system0", None)
        self.__system0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sensor1"):
                opp_val = getattr(old_value, "sensor1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sensor1"):
                opp_val = getattr(value, "sensor1", None)
                if opp_val is None:
                    setattr(value, "sensor1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Firebase:

    pass
