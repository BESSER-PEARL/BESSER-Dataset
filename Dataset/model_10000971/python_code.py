from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Symbol_Meaning:

    def __init__(self, ____: str):
        self.____ = ____
        
        pass
    @property
    def ____(self):
        return self.______
    @____.setter
    def ____(self, ____: str):
        self.______ = ____



class _unnamed:

    pass


class Class:

    pass


class Entertainment:

    def __init__(self, DeviceID: int, tV19: set["TV"] = None, speakers21: set["Speakers"] = None, homeTheatre23: set["HomeTheatre"] = None):
        self.DeviceID = DeviceID
        self.tV19 = tV19 if tV19 is not None else set()
        self.speakers21 = speakers21 if speakers21 is not None else set()
        self.homeTheatre23 = homeTheatre23 if homeTheatre23 is not None else set()
        
        pass
    @property
    def DeviceID(self):
        return self.__DeviceID
    @DeviceID.setter
    def DeviceID(self, DeviceID: int):
        self.__DeviceID = DeviceID

    @property
    def speakers21(self):
        return self.__speakers21
    @speakers21.setter
    def speakers21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entertainment__speakers21", None)
        self.__speakers21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entertainment20"):
                    opp_val = getattr(item, "entertainment20", None)
                    
                    if opp_val == self:
                        setattr(item, "entertainment20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entertainment20"):
                    opp_val = getattr(item, "entertainment20", None)
                    
                    setattr(item, "entertainment20", self)
                    

    @property
    def homeTheatre23(self):
        return self.__homeTheatre23
    @homeTheatre23.setter
    def homeTheatre23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entertainment__homeTheatre23", None)
        self.__homeTheatre23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entertainment22"):
                    opp_val = getattr(item, "entertainment22", None)
                    
                    if opp_val == self:
                        setattr(item, "entertainment22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entertainment22"):
                    opp_val = getattr(item, "entertainment22", None)
                    
                    setattr(item, "entertainment22", self)
                    

    @property
    def tV19(self):
        return self.__tV19
    @tV19.setter
    def tV19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entertainment__tV19", None)
        self.__tV19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entertainment18"):
                    opp_val = getattr(item, "entertainment18", None)
                    
                    if opp_val == self:
                        setattr(item, "entertainment18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entertainment18"):
                    opp_val = getattr(item, "entertainment18", None)
                    
                    setattr(item, "entertainment18", self)
                    



class HouseHolds:

    def __init__(self, TimeID: str, Coffee: str, DishWasher: str, Alarm: str, WashingMachine: str, system13: "System" = None):
        self.TimeID = TimeID
        self.Coffee = Coffee
        self.DishWasher = DishWasher
        self.Alarm = Alarm
        self.WashingMachine = WashingMachine
        self.system13 = system13
        
        pass
    @property
    def Alarm(self):
        return self.__Alarm
    @Alarm.setter
    def Alarm(self, Alarm: str):
        self.__Alarm = Alarm

    @property
    def WashingMachine(self):
        return self.__WashingMachine
    @WashingMachine.setter
    def WashingMachine(self, WashingMachine: str):
        self.__WashingMachine = WashingMachine

    @property
    def TimeID(self):
        return self.__TimeID
    @TimeID.setter
    def TimeID(self, TimeID: str):
        self.__TimeID = TimeID

    @property
    def DishWasher(self):
        return self.__DishWasher
    @DishWasher.setter
    def DishWasher(self, DishWasher: str):
        self.__DishWasher = DishWasher

    @property
    def Coffee(self):
        return self.__Coffee
    @Coffee.setter
    def Coffee(self, Coffee: str):
        self.__Coffee = Coffee

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



class HomeTheatre:

    def __init__(self, HTID: str, tV4: "TV" = None, speakers6: "Speakers" = None, system14: "System" = None, entertainment22: "Entertainment" = None):
        self.HTID = HTID
        self.tV4 = tV4
        self.speakers6 = speakers6
        self.system14 = system14
        self.entertainment22 = entertainment22
        
        pass
    @property
    def HTID(self):
        return self.__HTID
    @HTID.setter
    def HTID(self, HTID: str):
        self.__HTID = HTID

    @property
    def entertainment22(self):
        return self.__entertainment22
    @entertainment22.setter
    def entertainment22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HomeTheatre__entertainment22", None)
        self.__entertainment22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "homeTheatre23"):
                opp_val = getattr(old_value, "homeTheatre23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "homeTheatre23"):
                opp_val = getattr(value, "homeTheatre23", None)
                if opp_val is None:
                    setattr(value, "homeTheatre23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tV4(self):
        return self.__tV4
    @tV4.setter
    def tV4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HomeTheatre__tV4", None)
        self.__tV4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "homeTheatre5"):
                opp_val = getattr(old_value, "homeTheatre5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "homeTheatre5"):
                opp_val = getattr(value, "homeTheatre5", None)
                if opp_val is None:
                    setattr(value, "homeTheatre5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def system14(self):
        return self.__system14
    @system14.setter
    def system14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HomeTheatre__system14", None)
        self.__system14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "homeTheatre15"):
                opp_val = getattr(old_value, "homeTheatre15", None)
                if opp_val == self:
                    setattr(old_value, "homeTheatre15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "homeTheatre15"):
                opp_val = getattr(value, "homeTheatre15", None)
                setattr(value, "homeTheatre15", self)

    @property
    def speakers6(self):
        return self.__speakers6
    @speakers6.setter
    def speakers6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HomeTheatre__speakers6", None)
        self.__speakers6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "homeTheatre7"):
                opp_val = getattr(old_value, "homeTheatre7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "homeTheatre7"):
                opp_val = getattr(value, "homeTheatre7", None)
                if opp_val is None:
                    setattr(value, "homeTheatre7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class TV:

    def __init__(self, TVID: int, homeTheatre5: set["HomeTheatre"] = None, entertainment18: "Entertainment" = None):
        self.TVID = TVID
        self.homeTheatre5 = homeTheatre5 if homeTheatre5 is not None else set()
        self.entertainment18 = entertainment18
        
        pass
    @property
    def TVID(self):
        return self.__TVID
    @TVID.setter
    def TVID(self, TVID: int):
        self.__TVID = TVID

    @property
    def entertainment18(self):
        return self.__entertainment18
    @entertainment18.setter
    def entertainment18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TV__entertainment18", None)
        self.__entertainment18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tV19"):
                opp_val = getattr(old_value, "tV19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tV19"):
                opp_val = getattr(value, "tV19", None)
                if opp_val is None:
                    setattr(value, "tV19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def homeTheatre5(self):
        return self.__homeTheatre5
    @homeTheatre5.setter
    def homeTheatre5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TV__homeTheatre5", None)
        self.__homeTheatre5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tV4"):
                    opp_val = getattr(item, "tV4", None)
                    
                    if opp_val == self:
                        setattr(item, "tV4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tV4"):
                    opp_val = getattr(item, "tV4", None)
                    
                    setattr(item, "tV4", self)
                    



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



class Speakers:

    def __init__(self, SpeakerID: int, homeTheatre7: set["HomeTheatre"] = None, entertainment20: "Entertainment" = None):
        self.SpeakerID = SpeakerID
        self.homeTheatre7 = homeTheatre7 if homeTheatre7 is not None else set()
        self.entertainment20 = entertainment20
        
        pass
    @property
    def SpeakerID(self):
        return self.__SpeakerID
    @SpeakerID.setter
    def SpeakerID(self, SpeakerID: int):
        self.__SpeakerID = SpeakerID

    @property
    def entertainment20(self):
        return self.__entertainment20
    @entertainment20.setter
    def entertainment20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Speakers__entertainment20", None)
        self.__entertainment20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "speakers21"):
                opp_val = getattr(old_value, "speakers21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "speakers21"):
                opp_val = getattr(value, "speakers21", None)
                if opp_val is None:
                    setattr(value, "speakers21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def homeTheatre7(self):
        return self.__homeTheatre7
    @homeTheatre7.setter
    def homeTheatre7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Speakers__homeTheatre7", None)
        self.__homeTheatre7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "speakers6"):
                    opp_val = getattr(item, "speakers6", None)
                    
                    if opp_val == self:
                        setattr(item, "speakers6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "speakers6"):
                    opp_val = getattr(item, "speakers6", None)
                    
                    setattr(item, "speakers6", self)
                    



class Camera:

    def __init__(self, CameraID: int, door3: "Door" = None):
        self.CameraID = CameraID
        self.door3 = door3
        
        pass
    @property
    def CameraID(self):
        return self.__CameraID
    @CameraID.setter
    def CameraID(self, CameraID: int):
        self.__CameraID = CameraID

    @property
    def door3(self):
        return self.__door3
    @door3.setter
    def door3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Camera__door3", None)
        self.__door3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "camera2"):
                opp_val = getattr(old_value, "camera2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "camera2"):
                opp_val = getattr(value, "camera2", None)
                if opp_val is None:
                    setattr(value, "camera2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Door:

    def __init__(self, DoorID: int, sensor1: "Sensor" = None, camera2: set["Camera"] = None):
        self.DoorID = DoorID
        self.sensor1 = sensor1
        self.camera2 = camera2 if camera2 is not None else set()
        
        pass
    @property
    def DoorID(self):
        return self.__DoorID
    @DoorID.setter
    def DoorID(self, DoorID: int):
        self.__DoorID = DoorID

    @property
    def sensor1(self):
        return self.__sensor1
    @sensor1.setter
    def sensor1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Door__sensor1", None)
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

    @property
    def camera2(self):
        return self.__camera2
    @camera2.setter
    def camera2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Door__camera2", None)
        self.__camera2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "door3"):
                    opp_val = getattr(item, "door3", None)
                    
                    if opp_val == self:
                        setattr(item, "door3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "door3"):
                    opp_val = getattr(item, "door3", None)
                    
                    setattr(item, "door3", self)
                    



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

    def __init__(self, UserID: int, alert8: "Alert" = None, system16: "System" = None):
        self.UserID = UserID
        self.alert8 = alert8
        self.system16 = system16
        
        pass
    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: int):
        self.__UserID = UserID

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

    @property
    def system16(self):
        return self.__system16
    @system16.setter
    def system16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Home_Security_System__system16", None)
        self.__system16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "home_Security_System17"):
                opp_val = getattr(old_value, "home_Security_System17", None)
                if opp_val == self:
                    setattr(old_value, "home_Security_System17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "home_Security_System17"):
                opp_val = getattr(value, "home_Security_System17", None)
                setattr(value, "home_Security_System17", self)



class PressureSensor:

    pass


class Motion_Sensor:

    pass


class FireAlarm_Sensor:

    def __init__(self, DispenseSprinkler: bool, SmokeAlarm: bool):
        self.DispenseSprinkler = DispenseSprinkler
        self.SmokeAlarm = SmokeAlarm
        
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

    def __init__(self, SensorID: int, SensorType: int, door0: "Door" = None, system10: "System" = None):
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
    def system10(self):
        return self.__system10
    @system10.setter
    def system10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sensor__system10", None)
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



class System:

    def __init__(self, Update: float, Status: bool, sensor11: set["Sensor"] = None, houseHolds12: "HouseHolds" = None, homeTheatre15: "HomeTheatre" = None, home_Security_System17: "Home_Security_System" = None):
        self.Update = Update
        self.Status = Status
        self.sensor11 = sensor11 if sensor11 is not None else set()
        self.houseHolds12 = houseHolds12
        self.homeTheatre15 = homeTheatre15
        self.home_Security_System17 = home_Security_System17
        
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
    def homeTheatre15(self):
        return self.__homeTheatre15
    @homeTheatre15.setter
    def homeTheatre15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__homeTheatre15", None)
        self.__homeTheatre15 = value
        
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

    @property
    def home_Security_System17(self):
        return self.__home_Security_System17
    @home_Security_System17.setter
    def home_Security_System17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__home_Security_System17", None)
        self.__home_Security_System17 = value
        
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

