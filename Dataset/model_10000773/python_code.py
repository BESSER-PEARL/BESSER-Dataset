from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class UserProfile:

    def __init__(self, ProfileID: int):
        self.ProfileID = ProfileID
        
        pass
    @property
    def ProfileID(self):
        return self.__ProfileID
    @ProfileID.setter
    def ProfileID(self, ProfileID: int):
        self.__ProfileID = ProfileID



class ROOM:

    def __init__(self, RoomID: str):
        self.RoomID = RoomID
        
        pass
    @property
    def RoomID(self):
        return self.__RoomID
    @RoomID.setter
    def RoomID(self, RoomID: str):
        self.__RoomID = RoomID



class TechSupport:

    def __init__(self, TechID: int):
        self.TechID = TechID
        
        pass
    @property
    def TechID(self):
        return self.__TechID
    @TechID.setter
    def TechID(self, TechID: int):
        self.__TechID = TechID



class Kitchen:

    def __init__(self, TimeID: str, start_Of_Day4: "Start_Of_Day" = None, end_Of_Day6: "End_Of_Day" = None, system15: "System" = None):
        self.TimeID = TimeID
        self.start_Of_Day4 = start_Of_Day4
        self.end_Of_Day6 = end_Of_Day6
        self.system15 = system15
        
        pass
    @property
    def TimeID(self):
        return self.__TimeID
    @TimeID.setter
    def TimeID(self, TimeID: str):
        self.__TimeID = TimeID

    @property
    def start_Of_Day4(self):
        return self.__start_Of_Day4
    @start_Of_Day4.setter
    def start_Of_Day4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kitchen__start_Of_Day4", None)
        self.__start_Of_Day4 = value
        
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
    def end_Of_Day6(self):
        return self.__end_Of_Day6
    @end_Of_Day6.setter
    def end_Of_Day6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kitchen__end_Of_Day6", None)
        self.__end_Of_Day6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "houseHolds7"):
                opp_val = getattr(old_value, "houseHolds7", None)
                if opp_val == self:
                    setattr(old_value, "houseHolds7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "houseHolds7"):
                opp_val = getattr(value, "houseHolds7", None)
                setattr(value, "houseHolds7", self)

    @property
    def system15(self):
        return self.__system15
    @system15.setter
    def system15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kitchen__system15", None)
        self.__system15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "houseHolds14"):
                opp_val = getattr(old_value, "houseHolds14", None)
                if opp_val == self:
                    setattr(old_value, "houseHolds14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "houseHolds14"):
                opp_val = getattr(value, "houseHolds14", None)
                setattr(value, "houseHolds14", self)



class HomeTheatre:

    def __init__(self, SSID: str, speakers2: "Speakers" = None, system16: "System" = None):
        self.SSID = SSID
        self.speakers2 = speakers2
        self.system16 = system16
        
        pass
    @property
    def SSID(self):
        return self.__SSID
    @SSID.setter
    def SSID(self, SSID: str):
        self.__SSID = SSID

    @property
    def speakers2(self):
        return self.__speakers2
    @speakers2.setter
    def speakers2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HomeTheatre__speakers2", None)
        self.__speakers2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "homeTheatre3"):
                opp_val = getattr(old_value, "homeTheatre3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "homeTheatre3"):
                opp_val = getattr(value, "homeTheatre3", None)
                if opp_val is None:
                    setattr(value, "homeTheatre3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def system16(self):
        return self.__system16
    @system16.setter
    def system16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HomeTheatre__system16", None)
        self.__system16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "homeTheatre17"):
                opp_val = getattr(old_value, "homeTheatre17", None)
                if opp_val == self:
                    setattr(old_value, "homeTheatre17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "homeTheatre17"):
                opp_val = getattr(value, "homeTheatre17", None)
                setattr(value, "homeTheatre17", self)



class End_Of_Day:

    def __init__(self, EOT: int, houseHolds7: "Kitchen" = None):
        self.EOT = EOT
        self.houseHolds7 = houseHolds7
        
        pass
    @property
    def EOT(self):
        return self.__EOT
    @EOT.setter
    def EOT(self, EOT: int):
        self.__EOT = EOT

    @property
    def houseHolds7(self):
        return self.__houseHolds7
    @houseHolds7.setter
    def houseHolds7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_End_Of_Day__houseHolds7", None)
        self.__houseHolds7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "end_Of_Day6"):
                opp_val = getattr(old_value, "end_Of_Day6", None)
                if opp_val == self:
                    setattr(old_value, "end_Of_Day6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "end_Of_Day6"):
                opp_val = getattr(value, "end_Of_Day6", None)
                setattr(value, "end_Of_Day6", self)



class Start_Of_Day:

    def __init__(self, SOT: int, houseHolds5: "Kitchen" = None):
        self.SOT = SOT
        self.houseHolds5 = houseHolds5
        
        pass
    @property
    def SOT(self):
        return self.__SOT
    @SOT.setter
    def SOT(self, SOT: int):
        self.__SOT = SOT

    @property
    def houseHolds5(self):
        return self.__houseHolds5
    @houseHolds5.setter
    def houseHolds5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Start_Of_Day__houseHolds5", None)
        self.__houseHolds5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "start_Of_Day4"):
                opp_val = getattr(old_value, "start_Of_Day4", None)
                if opp_val == self:
                    setattr(old_value, "start_Of_Day4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "start_Of_Day4"):
                opp_val = getattr(value, "start_Of_Day4", None)
                setattr(value, "start_Of_Day4", self)



class Light:

    def __init__(self, LightID: int):
        self.LightID = LightID
        
        pass
    @property
    def LightID(self):
        return self.__LightID
    @LightID.setter
    def LightID(self, LightID: int):
        self.__LightID = LightID



class PowerSystem:

    def __init__(self, DeviceID: int, system8: "System" = None):
        self.DeviceID = DeviceID
        self.system8 = system8
        
        pass
    @property
    def DeviceID(self):
        return self.__DeviceID
    @DeviceID.setter
    def DeviceID(self, DeviceID: int):
        self.__DeviceID = DeviceID

    @property
    def system8(self):
        return self.__system8
    @system8.setter
    def system8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PowerSystem__system8", None)
        self.__system8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "microPhone9"):
                opp_val = getattr(old_value, "microPhone9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "microPhone9"):
                opp_val = getattr(value, "microPhone9", None)
                if opp_val is None:
                    setattr(value, "microPhone9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Speakers:

    def __init__(self, SpeakerID: int, homeTheatre3: set["HomeTheatre"] = None):
        self.SpeakerID = SpeakerID
        self.homeTheatre3 = homeTheatre3 if homeTheatre3 is not None else set()
        
        pass
    @property
    def SpeakerID(self):
        return self.__SpeakerID
    @SpeakerID.setter
    def SpeakerID(self, SpeakerID: int):
        self.__SpeakerID = SpeakerID

    @property
    def homeTheatre3(self):
        return self.__homeTheatre3
    @homeTheatre3.setter
    def homeTheatre3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Speakers__homeTheatre3", None)
        self.__homeTheatre3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "speakers2"):
                    opp_val = getattr(item, "speakers2", None)
                    
                    if opp_val == self:
                        setattr(item, "speakers2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "speakers2"):
                    opp_val = getattr(item, "speakers2", None)
                    
                    setattr(item, "speakers2", self)
                    



class Curtains:

    def __init__(self, CurtaiunID: int, sensor1: "Sensor" = None):
        self.CurtaiunID = CurtaiunID
        self.sensor1 = sensor1
        
        pass
    @property
    def CurtaiunID(self):
        return self.__CurtaiunID
    @CurtaiunID.setter
    def CurtaiunID(self, CurtaiunID: int):
        self.__CurtaiunID = CurtaiunID

    @property
    def sensor1(self):
        return self.__sensor1
    @sensor1.setter
    def sensor1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Curtains__sensor1", None)
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

    def __init__(self, AlertID: int, home_Security_System11: "Security_System" = None):
        self.AlertID = AlertID
        self.home_Security_System11 = home_Security_System11
        
        pass
    @property
    def AlertID(self):
        return self.__AlertID
    @AlertID.setter
    def AlertID(self, AlertID: int):
        self.__AlertID = AlertID

    @property
    def home_Security_System11(self):
        return self.__home_Security_System11
    @home_Security_System11.setter
    def home_Security_System11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Alert__home_Security_System11", None)
        self.__home_Security_System11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alert10"):
                opp_val = getattr(old_value, "alert10", None)
                if opp_val == self:
                    setattr(old_value, "alert10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alert10"):
                opp_val = getattr(value, "alert10", None)
                setattr(value, "alert10", self)



class Security_System:

    def __init__(self, UserID: int, alert10: "Alert" = None, Home_Security_System_System_018: "System" = None):
        self.UserID = UserID
        self.alert10 = alert10
        self.Home_Security_System_System_018 = Home_Security_System_System_018
        
        pass
    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: int):
        self.__UserID = UserID

    @property
    def Home_Security_System_System_018(self):
        return self.__Home_Security_System_System_018
    @Home_Security_System_System_018.setter
    def Home_Security_System_System_018(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Security_System__Home_Security_System_System_018", None)
        self.__Home_Security_System_System_018 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Home_Security_System_System_119"):
                opp_val = getattr(old_value, "Home_Security_System_System_119", None)
                if opp_val == self:
                    setattr(old_value, "Home_Security_System_System_119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Home_Security_System_System_119"):
                opp_val = getattr(value, "Home_Security_System_System_119", None)
                setattr(value, "Home_Security_System_System_119", self)

    @property
    def alert10(self):
        return self.__alert10
    @alert10.setter
    def alert10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Security_System__alert10", None)
        self.__alert10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "home_Security_System11"):
                opp_val = getattr(old_value, "home_Security_System11", None)
                if opp_val == self:
                    setattr(old_value, "home_Security_System11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "home_Security_System11"):
                opp_val = getattr(value, "home_Security_System11", None)
                setattr(value, "home_Security_System11", self)



class MotionSensor:

    pass


class Sensor:

    def __init__(self, SensorID: int, SensorType: int, door0: "Curtains" = None, system12: "System" = None):
        self.SensorID = SensorID
        self.SensorType = SensorType
        self.door0 = door0
        self.system12 = system12
        
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

    @property
    def system12(self):
        return self.__system12
    @system12.setter
    def system12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sensor__system12", None)
        self.__system12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sensor13"):
                opp_val = getattr(old_value, "sensor13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sensor13"):
                opp_val = getattr(value, "sensor13", None)
                if opp_val is None:
                    setattr(value, "sensor13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class System:

    def __init__(self, Status: bool, Update: float, microPhone9: set["PowerSystem"] = None, sensor13: set["Sensor"] = None, houseHolds14: "Kitchen" = None, homeTheatre17: "HomeTheatre" = None, Home_Security_System_System_119: "Security_System" = None):
        self.Status = Status
        self.Update = Update
        self.microPhone9 = microPhone9 if microPhone9 is not None else set()
        self.sensor13 = sensor13 if sensor13 is not None else set()
        self.houseHolds14 = houseHolds14
        self.homeTheatre17 = homeTheatre17
        self.Home_Security_System_System_119 = Home_Security_System_System_119
        
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
    def microPhone9(self):
        return self.__microPhone9
    @microPhone9.setter
    def microPhone9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__microPhone9", None)
        self.__microPhone9 = value if value is not None else set()
        
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
    def homeTheatre17(self):
        return self.__homeTheatre17
    @homeTheatre17.setter
    def homeTheatre17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__homeTheatre17", None)
        self.__homeTheatre17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system16"):
                opp_val = getattr(old_value, "system16", None)
                if opp_val == self:
                    setattr(old_value, "system16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system16"):
                opp_val = getattr(value, "system16", None)
                setattr(value, "system16", self)

    @property
    def sensor13(self):
        return self.__sensor13
    @sensor13.setter
    def sensor13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__sensor13", None)
        self.__sensor13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "system12"):
                    opp_val = getattr(item, "system12", None)
                    
                    if opp_val == self:
                        setattr(item, "system12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "system12"):
                    opp_val = getattr(item, "system12", None)
                    
                    setattr(item, "system12", self)
                    

    @property
    def houseHolds14(self):
        return self.__houseHolds14
    @houseHolds14.setter
    def houseHolds14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__houseHolds14", None)
        self.__houseHolds14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system15"):
                opp_val = getattr(old_value, "system15", None)
                if opp_val == self:
                    setattr(old_value, "system15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system15"):
                opp_val = getattr(value, "system15", None)
                setattr(value, "system15", self)

    @property
    def Home_Security_System_System_119(self):
        return self.__Home_Security_System_System_119
    @Home_Security_System_System_119.setter
    def Home_Security_System_System_119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__Home_Security_System_System_119", None)
        self.__Home_Security_System_System_119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Home_Security_System_System_018"):
                opp_val = getattr(old_value, "Home_Security_System_System_018", None)
                if opp_val == self:
                    setattr(old_value, "Home_Security_System_System_018", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Home_Security_System_System_018"):
                opp_val = getattr(value, "Home_Security_System_System_018", None)
                setattr(value, "Home_Security_System_System_018", self)

