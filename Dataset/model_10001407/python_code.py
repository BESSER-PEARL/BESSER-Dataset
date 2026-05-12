from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Fan_Regulator_Box:

    def __init__(self, FAN_ID: str):
        self.FAN_ID = FAN_ID
        
        pass
    @property
    def FAN_ID(self):
        return self.__FAN_ID
    @FAN_ID.setter
    def FAN_ID(self, FAN_ID: str):
        self.__FAN_ID = FAN_ID



class Control_Box:

    def __init__(self, Status: bool, Update: float):
        self.Status = Status
        self.Update = Update
        
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



class FAN:

    def __init__(self, FAN_ID: str):
        self.FAN_ID = FAN_ID
        
        pass
    @property
    def FAN_ID(self):
        return self.__FAN_ID
    @FAN_ID.setter
    def FAN_ID(self, FAN_ID: str):
        self.__FAN_ID = FAN_ID



class HouseHolds:

    def __init__(self, TimeID: str, Alarm: str, WashingMachine: str, system5: "System" = None):
        self.TimeID = TimeID
        self.Alarm = Alarm
        self.WashingMachine = WashingMachine
        self.system5 = system5
        
        pass
    @property
    def Alarm(self):
        return self.__Alarm
    @Alarm.setter
    def Alarm(self, Alarm: str):
        self.__Alarm = Alarm

    @property
    def TimeID(self):
        return self.__TimeID
    @TimeID.setter
    def TimeID(self, TimeID: str):
        self.__TimeID = TimeID

    @property
    def WashingMachine(self):
        return self.__WashingMachine
    @WashingMachine.setter
    def WashingMachine(self, WashingMachine: str):
        self.__WashingMachine = WashingMachine

    @property
    def system5(self):
        return self.__system5
    @system5.setter
    def system5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HouseHolds__system5", None)
        self.__system5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "houseHolds4"):
                opp_val = getattr(old_value, "houseHolds4", None)
                if opp_val == self:
                    setattr(old_value, "houseHolds4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "houseHolds4"):
                opp_val = getattr(value, "houseHolds4", None)
                setattr(value, "houseHolds4", self)



class Light:

    def __init__(self, LightID: str):
        self.LightID = LightID
        
        pass
    @property
    def LightID(self):
        return self.__LightID
    @LightID.setter
    def LightID(self, LightID: str):
        self.__LightID = LightID



class MicroPhone:

    def __init__(self, MicID: str, system0: "System" = None):
        self.MicID = MicID
        self.system0 = system0
        
        pass
    @property
    def MicID(self):
        return self.__MicID
    @MicID.setter
    def MicID(self, MicID: str):
        self.__MicID = MicID

    @property
    def system0(self):
        return self.__system0
    @system0.setter
    def system0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicroPhone__system0", None)
        self.__system0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "microPhone1"):
                opp_val = getattr(old_value, "microPhone1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "microPhone1"):
                opp_val = getattr(value, "microPhone1", None)
                if opp_val is None:
                    setattr(value, "microPhone1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Alert:

    def __init__(self, AlertID: int, home_Security_System3: "Home_Security_System" = None):
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



class Home_Security_System:

    def __init__(self, UserID: int, alert2: "Alert" = None, system6: "System" = None):
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
        old_value = getattr(self, f"_Home_Security_System__system6", None)
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
        old_value = getattr(self, f"_Home_Security_System__alert2", None)
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



class FireAlarm_Sensor:

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

    def __init__(self, SensorID: int, SensorType: int):
        self.SensorID = SensorID
        self.SensorType = SensorType
        
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



class System:

    def __init__(self, Status: bool, Update: float, microPhone1: set["MicroPhone"] = None, houseHolds4: "HouseHolds" = None, home_Security_System7: "Home_Security_System" = None):
        self.Status = Status
        self.Update = Update
        self.microPhone1 = microPhone1 if microPhone1 is not None else set()
        self.houseHolds4 = houseHolds4
        self.home_Security_System7 = home_Security_System7
        
        pass
    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: bool):
        self.__Status = Status

    @property
    def Update(self):
        return self.__Update
    @Update.setter
    def Update(self, Update: float):
        self.__Update = Update

    @property
    def microPhone1(self):
        return self.__microPhone1
    @microPhone1.setter
    def microPhone1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__microPhone1", None)
        self.__microPhone1 = value if value is not None else set()
        
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
    def houseHolds4(self):
        return self.__houseHolds4
    @houseHolds4.setter
    def houseHolds4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__houseHolds4", None)
        self.__houseHolds4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system5"):
                opp_val = getattr(old_value, "system5", None)
                if opp_val == self:
                    setattr(old_value, "system5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system5"):
                opp_val = getattr(value, "system5", None)
                setattr(value, "system5", self)

    @property
    def home_Security_System7(self):
        return self.__home_Security_System7
    @home_Security_System7.setter
    def home_Security_System7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__home_Security_System7", None)
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

