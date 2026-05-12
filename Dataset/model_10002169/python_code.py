from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class HouseHolds:

    def __init__(self, TimeID: str, LampLight: str, start_Of_Day2: "Start_Of_Day" = None, end_Of_Day4: "End_Of_Day" = None, system13: "System" = None):
        self.TimeID = TimeID
        self.LampLight = LampLight
        self.start_Of_Day2 = start_Of_Day2
        self.end_Of_Day4 = end_Of_Day4
        self.system13 = system13
        
        pass
    @property
    def LampLight(self):
        return self.__LampLight
    @LampLight.setter
    def LampLight(self, LampLight: str):
        self.__LampLight = LampLight

    @property
    def TimeID(self):
        return self.__TimeID
    @TimeID.setter
    def TimeID(self, TimeID: str):
        self.__TimeID = TimeID

    @property
    def end_Of_Day4(self):
        return self.__end_Of_Day4
    @end_Of_Day4.setter
    def end_Of_Day4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HouseHolds__end_Of_Day4", None)
        self.__end_Of_Day4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "houseHolds5"):
                opp_val = getattr(old_value, "houseHolds5", None)
                if opp_val == self:
                    setattr(old_value, "houseHolds5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "houseHolds5"):
                opp_val = getattr(value, "houseHolds5", None)
                setattr(value, "houseHolds5", self)

    @property
    def system13(self):
        return self.__system13
    @system13.setter
    def system13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HouseHolds__system13", None)
        self.__system13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "houseHolds12"):
                opp_val = getattr(old_value, "houseHolds12", None)
                if opp_val == self:
                    setattr(old_value, "houseHolds12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "houseHolds12"):
                opp_val = getattr(value, "houseHolds12", None)
                setattr(value, "houseHolds12", self)

    @property
    def start_Of_Day2(self):
        return self.__start_Of_Day2
    @start_Of_Day2.setter
    def start_Of_Day2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HouseHolds__start_Of_Day2", None)
        self.__start_Of_Day2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "houseHolds3"):
                opp_val = getattr(old_value, "houseHolds3", None)
                if opp_val == self:
                    setattr(old_value, "houseHolds3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "houseHolds3"):
                opp_val = getattr(value, "houseHolds3", None)
                setattr(value, "houseHolds3", self)



class End_Of_Day:

    def __init__(self, EOT: int, houseHolds5: "HouseHolds" = None):
        self.EOT = EOT
        self.houseHolds5 = houseHolds5
        
        pass
    @property
    def EOT(self):
        return self.__EOT
    @EOT.setter
    def EOT(self, EOT: int):
        self.__EOT = EOT

    @property
    def houseHolds5(self):
        return self.__houseHolds5
    @houseHolds5.setter
    def houseHolds5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_End_Of_Day__houseHolds5", None)
        self.__houseHolds5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "end_Of_Day4"):
                opp_val = getattr(old_value, "end_Of_Day4", None)
                if opp_val == self:
                    setattr(old_value, "end_Of_Day4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "end_Of_Day4"):
                opp_val = getattr(value, "end_Of_Day4", None)
                setattr(value, "end_Of_Day4", self)



class Start_Of_Day:

    def __init__(self, SOT: int, houseHolds3: "HouseHolds" = None):
        self.SOT = SOT
        self.houseHolds3 = houseHolds3
        
        pass
    @property
    def SOT(self):
        return self.__SOT
    @SOT.setter
    def SOT(self, SOT: int):
        self.__SOT = SOT

    @property
    def houseHolds3(self):
        return self.__houseHolds3
    @houseHolds3.setter
    def houseHolds3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Start_Of_Day__houseHolds3", None)
        self.__houseHolds3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "start_Of_Day2"):
                opp_val = getattr(old_value, "start_Of_Day2", None)
                if opp_val == self:
                    setattr(old_value, "start_Of_Day2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "start_Of_Day2"):
                opp_val = getattr(value, "start_Of_Day2", None)
                setattr(value, "start_Of_Day2", self)



class MicroPhone:

    def __init__(self, MicID: str, system6: "System" = None):
        self.MicID = MicID
        self.system6 = system6
        
        pass
    @property
    def MicID(self):
        return self.__MicID
    @MicID.setter
    def MicID(self, MicID: str):
        self.__MicID = MicID

    @property
    def system6(self):
        return self.__system6
    @system6.setter
    def system6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicroPhone__system6", None)
        self.__system6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "microPhone7"):
                opp_val = getattr(old_value, "microPhone7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "microPhone7"):
                opp_val = getattr(value, "microPhone7", None)
                if opp_val is None:
                    setattr(value, "microPhone7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Lamp:

    def __init__(self, LampID: int, sensor1: "Relay" = None):
        self.LampID = LampID
        self.sensor1 = sensor1
        
        pass
    @property
    def LampID(self):
        return self.__LampID
    @LampID.setter
    def LampID(self, LampID: int):
        self.__LampID = LampID

    @property
    def sensor1(self):
        return self.__sensor1
    @sensor1.setter
    def sensor1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lamp__sensor1", None)
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

    def __init__(self, AlertID: int, home_Security_System9: "Home_Security_System" = None):
        self.AlertID = AlertID
        self.home_Security_System9 = home_Security_System9
        
        pass
    @property
    def AlertID(self):
        return self.__AlertID
    @AlertID.setter
    def AlertID(self, AlertID: int):
        self.__AlertID = AlertID

    @property
    def home_Security_System9(self):
        return self.__home_Security_System9
    @home_Security_System9.setter
    def home_Security_System9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Alert__home_Security_System9", None)
        self.__home_Security_System9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alert8"):
                opp_val = getattr(old_value, "alert8", None)
                if opp_val == self:
                    setattr(old_value, "alert8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alert8"):
                opp_val = getattr(value, "alert8", None)
                setattr(value, "alert8", self)



class Home_Security_System:

    def __init__(self, UserID: int, alert8: "Alert" = None, system14: "System" = None):
        self.UserID = UserID
        self.alert8 = alert8
        self.system14 = system14
        
        pass
    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: int):
        self.__UserID = UserID

    @property
    def system14(self):
        return self.__system14
    @system14.setter
    def system14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Home_Security_System__system14", None)
        self.__system14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "home_Security_System15"):
                opp_val = getattr(old_value, "home_Security_System15", None)
                if opp_val == self:
                    setattr(old_value, "home_Security_System15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "home_Security_System15"):
                opp_val = getattr(value, "home_Security_System15", None)
                setattr(value, "home_Security_System15", self)

    @property
    def alert8(self):
        return self.__alert8
    @alert8.setter
    def alert8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Home_Security_System__alert8", None)
        self.__alert8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "home_Security_System9"):
                opp_val = getattr(old_value, "home_Security_System9", None)
                if opp_val == self:
                    setattr(old_value, "home_Security_System9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "home_Security_System9"):
                opp_val = getattr(value, "home_Security_System9", None)
                setattr(value, "home_Security_System9", self)



class Relay:

    def __init__(self, SensorID: int, SensorType: int, door0: "Lamp" = None, system10: "System" = None):
        self.SensorID = SensorID
        self.SensorType = SensorType
        self.door0 = door0
        self.system10 = system10
        
        pass
    @property
    def SensorType(self):
        return self.__SensorType
    @SensorType.setter
    def SensorType(self, SensorType: int):
        self.__SensorType = SensorType

    @property
    def SensorID(self):
        return self.__SensorID
    @SensorID.setter
    def SensorID(self, SensorID: int):
        self.__SensorID = SensorID

    @property
    def system10(self):
        return self.__system10
    @system10.setter
    def system10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Relay__system10", None)
        self.__system10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sensor11"):
                opp_val = getattr(old_value, "sensor11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sensor11"):
                opp_val = getattr(value, "sensor11", None)
                if opp_val is None:
                    setattr(value, "sensor11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def door0(self):
        return self.__door0
    @door0.setter
    def door0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Relay__door0", None)
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



class System:

    def __init__(self, Status: bool, Update: float, microPhone7: set["MicroPhone"] = None, sensor11: set["Relay"] = None, houseHolds12: "HouseHolds" = None, home_Security_System15: "Home_Security_System" = None):
        self.Status = Status
        self.Update = Update
        self.microPhone7 = microPhone7 if microPhone7 is not None else set()
        self.sensor11 = sensor11 if sensor11 is not None else set()
        self.houseHolds12 = houseHolds12
        self.home_Security_System15 = home_Security_System15
        
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
    def sensor11(self):
        return self.__sensor11
    @sensor11.setter
    def sensor11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__sensor11", None)
        self.__sensor11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "system10"):
                    opp_val = getattr(item, "system10", None)
                    
                    if opp_val == self:
                        setattr(item, "system10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "system10"):
                    opp_val = getattr(item, "system10", None)
                    
                    setattr(item, "system10", self)
                    

    @property
    def microPhone7(self):
        return self.__microPhone7
    @microPhone7.setter
    def microPhone7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__microPhone7", None)
        self.__microPhone7 = value if value is not None else set()
        
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
    def home_Security_System15(self):
        return self.__home_Security_System15
    @home_Security_System15.setter
    def home_Security_System15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__home_Security_System15", None)
        self.__home_Security_System15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system14"):
                opp_val = getattr(old_value, "system14", None)
                if opp_val == self:
                    setattr(old_value, "system14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system14"):
                opp_val = getattr(value, "system14", None)
                setattr(value, "system14", self)

    @property
    def houseHolds12(self):
        return self.__houseHolds12
    @houseHolds12.setter
    def houseHolds12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__houseHolds12", None)
        self.__houseHolds12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system13"):
                opp_val = getattr(old_value, "system13", None)
                if opp_val == self:
                    setattr(old_value, "system13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system13"):
                opp_val = getattr(value, "system13", None)
                setattr(value, "system13", self)

