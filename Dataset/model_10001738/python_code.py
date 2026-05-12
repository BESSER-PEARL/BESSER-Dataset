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





class View_sensors_data_external:

    pass


class Sense_and_Update_Data_external:

    pass


class Close_Alarm_external:

    pass


class Add_new_alarm_external:

    pass


class Notify_User_of_fire_external:

    pass


class Fire_Alarm_System__Component:

    pass


class Web:

    def __init__(self, People_: int, OwnerData: str, SmokeValue: float, TempValue: float, HomeLoc: str, Firebase_Web_17: "Firebase" = None):
        self.People_ = People_
        self.OwnerData = OwnerData
        self.SmokeValue = SmokeValue
        self.TempValue = TempValue
        self.HomeLoc = HomeLoc
        self.Firebase_Web_17 = Firebase_Web_17
        
        pass
    @property
    def People_(self):
        return self.__People_
    @People_.setter
    def People_(self, People_: int):
        self.__People_ = People_

    @property
    def TempValue(self):
        return self.__TempValue
    @TempValue.setter
    def TempValue(self, TempValue: float):
        self.__TempValue = TempValue

    @property
    def OwnerData(self):
        return self.__OwnerData
    @OwnerData.setter
    def OwnerData(self, OwnerData: str):
        self.__OwnerData = OwnerData

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
    def Firebase_Web_17(self):
        return self.__Firebase_Web_17
    @Firebase_Web_17.setter
    def Firebase_Web_17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Web__Firebase_Web_17", None)
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



class Arduino:

    def __init__(self, MicID: str, sensor1: set["Sensor"] = None, Arduino__Firebase_04: "Firebase" = None):
        self.MicID = MicID
        self.sensor1 = sensor1 if sensor1 is not None else set()
        self.Arduino__Firebase_04 = Arduino__Firebase_04
        
        pass
    @property
    def MicID(self):
        return self.__MicID
    @MicID.setter
    def MicID(self, MicID: str):
        self.__MicID = MicID

    @property
    def sensor1(self):
        return self.__sensor1
    @sensor1.setter
    def sensor1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arduino__sensor1", None)
        self.__sensor1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "system0"):
                    opp_val = getattr(item, "system0", None)
                    
                    if opp_val == self:
                        setattr(item, "system0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "system0"):
                    opp_val = getattr(item, "system0", None)
                    
                    setattr(item, "system0", self)
                    

    @property
    def Arduino__Firebase_04(self):
        return self.__Arduino__Firebase_04
    @Arduino__Firebase_04.setter
    def Arduino__Firebase_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arduino__Arduino__Firebase_04", None)
        self.__Arduino__Firebase_04 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arduino__Firebase_15"):
                opp_val = getattr(old_value, "Arduino__Firebase_15", None)
                if opp_val == self:
                    setattr(old_value, "Arduino__Firebase_15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arduino__Firebase_15"):
                opp_val = getattr(value, "Arduino__Firebase_15", None)
                setattr(value, "Arduino__Firebase_15", self)



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



class Mobile_App:

    def __init__(self, UserID: int, AlarmID: int, Home_Security_System_System_02: "Firebase" = None):
        self.UserID = UserID
        self.AlarmID = AlarmID
        self.Home_Security_System_System_02 = Home_Security_System_System_02
        
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
    def Home_Security_System_System_02(self):
        return self.__Home_Security_System_System_02
    @Home_Security_System_System_02.setter
    def Home_Security_System_System_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Mobile_App__Home_Security_System_System_02", None)
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
