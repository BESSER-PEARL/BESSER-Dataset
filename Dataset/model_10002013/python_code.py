from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Alert2:

    def __init__(self, AlertID: int, web12: "Web" = None):
        self.AlertID = AlertID
        self.web12 = web12
        
        pass
    @property
    def AlertID(self):
        return self.__AlertID
    @AlertID.setter
    def AlertID(self, AlertID: int):
        self.__AlertID = AlertID

    @property
    def web12(self):
        return self.__web12
    @web12.setter
    def web12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Alert2__web12", None)
        self.__web12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alert213"):
                opp_val = getattr(old_value, "alert213", None)
                if opp_val == self:
                    setattr(old_value, "alert213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alert213"):
                opp_val = getattr(value, "alert213", None)
                setattr(value, "alert213", self)



class Web:

    pass


class Arduino:

    def __init__(self, MicID: str, sensor5: set["Sensor"] = None, Arduino__Firebase_08: "Firebase" = None):
        self.MicID = MicID
        self.sensor5 = sensor5 if sensor5 is not None else set()
        self.Arduino__Firebase_08 = Arduino__Firebase_08
        
        pass
    @property
    def MicID(self):
        return self.__MicID
    @MicID.setter
    def MicID(self, MicID: str):
        self.__MicID = MicID

    @property
    def sensor5(self):
        return self.__sensor5
    @sensor5.setter
    def sensor5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arduino__sensor5", None)
        self.__sensor5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "system4"):
                    opp_val = getattr(item, "system4", None)
                    
                    if opp_val == self:
                        setattr(item, "system4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "system4"):
                    opp_val = getattr(item, "system4", None)
                    
                    setattr(item, "system4", self)
                    

    @property
    def Arduino__Firebase_08(self):
        return self.__Arduino__Firebase_08
    @Arduino__Firebase_08.setter
    def Arduino__Firebase_08(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arduino__Arduino__Firebase_08", None)
        self.__Arduino__Firebase_08 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arduino__Firebase_19"):
                opp_val = getattr(old_value, "Arduino__Firebase_19", None)
                if opp_val == self:
                    setattr(old_value, "Arduino__Firebase_19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arduino__Firebase_19"):
                opp_val = getattr(value, "Arduino__Firebase_19", None)
                setattr(value, "Arduino__Firebase_19", self)



class Count_people:

    def __init__(self, _attr: int, sensor1: "Sensor" = None):
        self._attr = _attr
        self.sensor1 = sensor1
        
        pass
    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: int):
        self.___attr = _attr

    @property
    def sensor1(self):
        return self.__sensor1
    @sensor1.setter
    def sensor1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Count_people__sensor1", None)
        self.__sensor1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "door0"):
                opp_val = getattr(old_value, "door0", None)
                if opp_val == self:
                    setattr(old_value, "door0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "door0"):
                opp_val = getattr(value, "door0", None)
                setattr(value, "door0", self)



class Alert:

    def __init__(self, AlertID: int, home_Security_System3: "Mobile_App" = None):
        self.AlertID = AlertID
        self.home_Security_System3 = home_Security_System3
        
        pass
    @property
    def AlertID(self):
        return self.__AlertID
    @AlertID.setter
    def AlertID(self, AlertID: int):
        self.__AlertID = AlertID

    @property
    def home_Security_System3(self):
        return self.__home_Security_System3
    @home_Security_System3.setter
    def home_Security_System3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Alert__home_Security_System3", None)
        self.__home_Security_System3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alert2"):
                opp_val = getattr(old_value, "alert2", None)
                if opp_val == self:
                    setattr(old_value, "alert2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alert2"):
                opp_val = getattr(value, "alert2", None)
                setattr(value, "alert2", self)



class Mobile_App:

    def __init__(self, UserID: int, alert2: "Alert" = None, system6: "Firebase" = None):
        self.UserID = UserID
        self.alert2 = alert2
        self.system6 = system6
        
        pass
    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: int):
        self.__UserID = UserID

    @property
    def system6(self):
        return self.__system6
    @system6.setter
    def system6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Mobile_App__system6", None)
        self.__system6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "home_Security_System7"):
                opp_val = getattr(old_value, "home_Security_System7", None)
                if opp_val == self:
                    setattr(old_value, "home_Security_System7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "home_Security_System7"):
                opp_val = getattr(value, "home_Security_System7", None)
                setattr(value, "home_Security_System7", self)

    @property
    def alert2(self):
        return self.__alert2
    @alert2.setter
    def alert2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Mobile_App__alert2", None)
        self.__alert2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "home_Security_System3"):
                opp_val = getattr(old_value, "home_Security_System3", None)
                if opp_val == self:
                    setattr(old_value, "home_Security_System3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "home_Security_System3"):
                opp_val = getattr(value, "home_Security_System3", None)
                setattr(value, "home_Security_System3", self)



class PressureSensor:

    pass


class Temperature_Sensor:

    pass


class Gas_Smoke_Sensor:

    def __init__(self, SmokeAlarm: bool, DispenseSprinkler: bool):
        self.SmokeAlarm = SmokeAlarm
        self.DispenseSprinkler = DispenseSprinkler
        
        pass
    @property
    def DispenseSprinkler(self):
        return self.__DispenseSprinkler
    @DispenseSprinkler.setter
    def DispenseSprinkler(self, DispenseSprinkler: bool):
        self.__DispenseSprinkler = DispenseSprinkler

    @property
    def SmokeAlarm(self):
        return self.__SmokeAlarm
    @SmokeAlarm.setter
    def SmokeAlarm(self, SmokeAlarm: bool):
        self.__SmokeAlarm = SmokeAlarm



class Sensor:

    def __init__(self, SensorID: int, SensorType: int, door0: "Count_people" = None, system4: "Arduino" = None):
        self.SensorID = SensorID
        self.SensorType = SensorType
        self.door0 = door0
        self.system4 = system4
        
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
    def system4(self):
        return self.__system4
    @system4.setter
    def system4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sensor__system4", None)
        self.__system4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sensor5"):
                opp_val = getattr(old_value, "sensor5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sensor5"):
                opp_val = getattr(value, "sensor5", None)
                if opp_val is None:
                    setattr(value, "sensor5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def door0(self):
        return self.__door0
    @door0.setter
    def door0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sensor__door0", None)
        self.__door0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sensor1"):
                opp_val = getattr(old_value, "sensor1", None)
                if opp_val == self:
                    setattr(old_value, "sensor1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sensor1"):
                opp_val = getattr(value, "sensor1", None)
                setattr(value, "sensor1", self)



class Firebase:

    def __init__(self, Status: bool, Update: float, home_Security_System7: "Mobile_App" = None, Arduino__Firebase_19: "Arduino" = None, web10: "Web" = None):
        self.Status = Status
        self.Update = Update
        self.home_Security_System7 = home_Security_System7
        self.Arduino__Firebase_19 = Arduino__Firebase_19
        self.web10 = web10
        
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
    def home_Security_System7(self):
        return self.__home_Security_System7
    @home_Security_System7.setter
    def home_Security_System7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Firebase__home_Security_System7", None)
        self.__home_Security_System7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system6"):
                opp_val = getattr(old_value, "system6", None)
                if opp_val == self:
                    setattr(old_value, "system6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system6"):
                opp_val = getattr(value, "system6", None)
                setattr(value, "system6", self)

    @property
    def web10(self):
        return self.__web10
    @web10.setter
    def web10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Firebase__web10", None)
        self.__web10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "firebase11"):
                opp_val = getattr(old_value, "firebase11", None)
                if opp_val == self:
                    setattr(old_value, "firebase11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "firebase11"):
                opp_val = getattr(value, "firebase11", None)
                setattr(value, "firebase11", self)

    @property
    def Arduino__Firebase_19(self):
        return self.__Arduino__Firebase_19
    @Arduino__Firebase_19.setter
    def Arduino__Firebase_19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Firebase__Arduino__Firebase_19", None)
        self.__Arduino__Firebase_19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arduino__Firebase_08"):
                opp_val = getattr(old_value, "Arduino__Firebase_08", None)
                if opp_val == self:
                    setattr(old_value, "Arduino__Firebase_08", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arduino__Firebase_08"):
                opp_val = getattr(value, "Arduino__Firebase_08", None)
                setattr(value, "Arduino__Firebase_08", self)

