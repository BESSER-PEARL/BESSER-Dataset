from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Entertainment:

    def __init__(self, DeviceID: int, tV25: set["TV"] = None, speakers27: set["Speakers"] = None, homeTheatre29: set["HomeTheatre"] = None):
        self.DeviceID = DeviceID
        self.tV25 = tV25 if tV25 is not None else set()
        self.speakers27 = speakers27 if speakers27 is not None else set()
        self.homeTheatre29 = homeTheatre29 if homeTheatre29 is not None else set()
        
        pass
    @property
    def DeviceID(self):
        return self.__DeviceID
    @DeviceID.setter
    def DeviceID(self, DeviceID: int):
        self.__DeviceID = DeviceID

    @property
    def speakers27(self):
        return self.__speakers27
    @speakers27.setter
    def speakers27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entertainment__speakers27", None)
        self.__speakers27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entertainment26"):
                    opp_val = getattr(item, "entertainment26", None)
                    
                    if opp_val == self:
                        setattr(item, "entertainment26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entertainment26"):
                    opp_val = getattr(item, "entertainment26", None)
                    
                    setattr(item, "entertainment26", self)
                    

    @property
    def tV25(self):
        return self.__tV25
    @tV25.setter
    def tV25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entertainment__tV25", None)
        self.__tV25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entertainment24"):
                    opp_val = getattr(item, "entertainment24", None)
                    
                    if opp_val == self:
                        setattr(item, "entertainment24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entertainment24"):
                    opp_val = getattr(item, "entertainment24", None)
                    
                    setattr(item, "entertainment24", self)
                    

    @property
    def homeTheatre29(self):
        return self.__homeTheatre29
    @homeTheatre29.setter
    def homeTheatre29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entertainment__homeTheatre29", None)
        self.__homeTheatre29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entertainment28"):
                    opp_val = getattr(item, "entertainment28", None)
                    
                    if opp_val == self:
                        setattr(item, "entertainment28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entertainment28"):
                    opp_val = getattr(item, "entertainment28", None)
                    
                    setattr(item, "entertainment28", self)
                    



class HouseHolds:

    def __init__(self, TimeID: str, Coffee: str, DishWasher: str, Alarm: str, WashingMachine: str, end_Of_Day10: "End_Of_Day" = None, system19: "System" = None, start_Of_Day8: "Start_Of_Day" = None):
        self.TimeID = TimeID
        self.Coffee = Coffee
        self.DishWasher = DishWasher
        self.Alarm = Alarm
        self.WashingMachine = WashingMachine
        self.end_Of_Day10 = end_Of_Day10
        self.system19 = system19
        self.start_Of_Day8 = start_Of_Day8
        
        pass
    @property
    def DishWasher(self):
        return self.__DishWasher
    @DishWasher.setter
    def DishWasher(self, DishWasher: str):
        self.__DishWasher = DishWasher

    @property
    def Alarm(self):
        return self.__Alarm
    @Alarm.setter
    def Alarm(self, Alarm: str):
        self.__Alarm = Alarm

    @property
    def Coffee(self):
        return self.__Coffee
    @Coffee.setter
    def Coffee(self, Coffee: str):
        self.__Coffee = Coffee

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
    def start_Of_Day8(self):
        return self.__start_Of_Day8
    @start_Of_Day8.setter
    def start_Of_Day8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HouseHolds__start_Of_Day8", None)
        self.__start_Of_Day8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "houseHolds9"):
                opp_val = getattr(old_value, "houseHolds9", None)
                if opp_val == self:
                    setattr(old_value, "houseHolds9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "houseHolds9"):
                opp_val = getattr(value, "houseHolds9", None)
                setattr(value, "houseHolds9", self)

    @property
    def end_Of_Day10(self):
        return self.__end_Of_Day10
    @end_Of_Day10.setter
    def end_Of_Day10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HouseHolds__end_Of_Day10", None)
        self.__end_Of_Day10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "houseHolds11"):
                opp_val = getattr(old_value, "houseHolds11", None)
                if opp_val == self:
                    setattr(old_value, "houseHolds11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "houseHolds11"):
                opp_val = getattr(value, "houseHolds11", None)
                setattr(value, "houseHolds11", self)

    @property
    def system19(self):
        return self.__system19
    @system19.setter
    def system19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HouseHolds__system19", None)
        self.__system19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "houseHolds18"):
                opp_val = getattr(old_value, "houseHolds18", None)
                if opp_val == self:
                    setattr(old_value, "houseHolds18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "houseHolds18"):
                opp_val = getattr(value, "houseHolds18", None)
                setattr(value, "houseHolds18", self)



class HomeTheatre:

    def __init__(self, HTID: str, entertainment28: "Entertainment" = None, system20: "System" = None, tV4: "TV" = None, speakers6: "Speakers" = None):
        self.HTID = HTID
        self.entertainment28 = entertainment28
        self.system20 = system20
        self.tV4 = tV4
        self.speakers6 = speakers6
        
        pass
    @property
    def HTID(self):
        return self.__HTID
    @HTID.setter
    def HTID(self, HTID: str):
        self.__HTID = HTID

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

    @property
    def system20(self):
        return self.__system20
    @system20.setter
    def system20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HomeTheatre__system20", None)
        self.__system20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "homeTheatre21"):
                opp_val = getattr(old_value, "homeTheatre21", None)
                if opp_val == self:
                    setattr(old_value, "homeTheatre21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "homeTheatre21"):
                opp_val = getattr(value, "homeTheatre21", None)
                setattr(value, "homeTheatre21", self)

    @property
    def entertainment28(self):
        return self.__entertainment28
    @entertainment28.setter
    def entertainment28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HomeTheatre__entertainment28", None)
        self.__entertainment28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "homeTheatre29"):
                opp_val = getattr(old_value, "homeTheatre29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "homeTheatre29"):
                opp_val = getattr(value, "homeTheatre29", None)
                if opp_val is None:
                    setattr(value, "homeTheatre29", set([self]))
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



class TV:

    def __init__(self, TVID: int, entertainment24: "Entertainment" = None, homeTheatre5: set["HomeTheatre"] = None):
        self.TVID = TVID
        self.entertainment24 = entertainment24
        self.homeTheatre5 = homeTheatre5 if homeTheatre5 is not None else set()
        
        pass
    @property
    def TVID(self):
        return self.__TVID
    @TVID.setter
    def TVID(self, TVID: int):
        self.__TVID = TVID

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
                    

    @property
    def entertainment24(self):
        return self.__entertainment24
    @entertainment24.setter
    def entertainment24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TV__entertainment24", None)
        self.__entertainment24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tV25"):
                opp_val = getattr(old_value, "tV25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tV25"):
                opp_val = getattr(value, "tV25", None)
                if opp_val is None:
                    setattr(value, "tV25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class End_Of_Day:

    def __init__(self, EOT: int, houseHolds11: "HouseHolds" = None):
        self.EOT = EOT
        self.houseHolds11 = houseHolds11
        
        pass
    @property
    def EOT(self):
        return self.__EOT
    @EOT.setter
    def EOT(self, EOT: int):
        self.__EOT = EOT

    @property
    def houseHolds11(self):
        return self.__houseHolds11
    @houseHolds11.setter
    def houseHolds11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_End_Of_Day__houseHolds11", None)
        self.__houseHolds11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "end_Of_Day10"):
                opp_val = getattr(old_value, "end_Of_Day10", None)
                if opp_val == self:
                    setattr(old_value, "end_Of_Day10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "end_Of_Day10"):
                opp_val = getattr(value, "end_Of_Day10", None)
                setattr(value, "end_Of_Day10", self)



class Start_Of_Day:

    def __init__(self, SOT: int, houseHolds9: "HouseHolds" = None):
        self.SOT = SOT
        self.houseHolds9 = houseHolds9
        
        pass
    @property
    def SOT(self):
        return self.__SOT
    @SOT.setter
    def SOT(self, SOT: int):
        self.__SOT = SOT

    @property
    def houseHolds9(self):
        return self.__houseHolds9
    @houseHolds9.setter
    def houseHolds9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Start_Of_Day__houseHolds9", None)
        self.__houseHolds9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "start_Of_Day8"):
                opp_val = getattr(old_value, "start_Of_Day8", None)
                if opp_val == self:
                    setattr(old_value, "start_Of_Day8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "start_Of_Day8"):
                opp_val = getattr(value, "start_Of_Day8", None)
                setattr(value, "start_Of_Day8", self)



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

    def __init__(self, MicID: str, system12: "System" = None):
        self.MicID = MicID
        self.system12 = system12
        
        pass
    @property
    def MicID(self):
        return self.__MicID
    @MicID.setter
    def MicID(self, MicID: str):
        self.__MicID = MicID

    @property
    def system12(self):
        return self.__system12
    @system12.setter
    def system12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicroPhone__system12", None)
        self.__system12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "microPhone13"):
                opp_val = getattr(old_value, "microPhone13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "microPhone13"):
                opp_val = getattr(value, "microPhone13", None)
                if opp_val is None:
                    setattr(value, "microPhone13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Speakers:

    def __init__(self, SpeakerID: int, entertainment26: "Entertainment" = None, homeTheatre7: set["HomeTheatre"] = None):
        self.SpeakerID = SpeakerID
        self.entertainment26 = entertainment26
        self.homeTheatre7 = homeTheatre7 if homeTheatre7 is not None else set()
        
        pass
    @property
    def SpeakerID(self):
        return self.__SpeakerID
    @SpeakerID.setter
    def SpeakerID(self, SpeakerID: int):
        self.__SpeakerID = SpeakerID

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
                    

    @property
    def entertainment26(self):
        return self.__entertainment26
    @entertainment26.setter
    def entertainment26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Speakers__entertainment26", None)
        self.__entertainment26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "speakers27"):
                opp_val = getattr(old_value, "speakers27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "speakers27"):
                opp_val = getattr(value, "speakers27", None)
                if opp_val is None:
                    setattr(value, "speakers27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



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



class Alert:

    def __init__(self, AlertID: int, home_Security_System15: "Home_Security_System" = None):
        self.AlertID = AlertID
        self.home_Security_System15 = home_Security_System15
        
        pass
    @property
    def AlertID(self):
        return self.__AlertID
    @AlertID.setter
    def AlertID(self, AlertID: int):
        self.__AlertID = AlertID

    @property
    def home_Security_System15(self):
        return self.__home_Security_System15
    @home_Security_System15.setter
    def home_Security_System15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Alert__home_Security_System15", None)
        self.__home_Security_System15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alert14"):
                opp_val = getattr(old_value, "alert14", None)
                if opp_val == self:
                    setattr(old_value, "alert14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alert14"):
                opp_val = getattr(value, "alert14", None)
                setattr(value, "alert14", self)



class Home_Security_System:

    def __init__(self, UserID: int, alert14: "Alert" = None, system22: "System" = None):
        self.UserID = UserID
        self.alert14 = alert14
        self.system22 = system22
        
        pass
    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: int):
        self.__UserID = UserID

    @property
    def system22(self):
        return self.__system22
    @system22.setter
    def system22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Home_Security_System__system22", None)
        self.__system22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "home_Security_System23"):
                opp_val = getattr(old_value, "home_Security_System23", None)
                if opp_val == self:
                    setattr(old_value, "home_Security_System23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "home_Security_System23"):
                opp_val = getattr(value, "home_Security_System23", None)
                setattr(value, "home_Security_System23", self)

    @property
    def alert14(self):
        return self.__alert14
    @alert14.setter
    def alert14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Home_Security_System__alert14", None)
        self.__alert14 = value
        
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



class PressureSensor:

    pass


class Motion_Sensor:

    pass


class FireAlarm_Sensor:

    def __init__(self, SmokeAlarm: bool, DispenseSprinkler: bool):
        self.SmokeAlarm = SmokeAlarm
        self.DispenseSprinkler = DispenseSprinkler
        
        pass
    @property
    def SmokeAlarm(self):
        return self.__SmokeAlarm
    @SmokeAlarm.setter
    def SmokeAlarm(self, SmokeAlarm: bool):
        self.__SmokeAlarm = SmokeAlarm

    @property
    def DispenseSprinkler(self):
        return self.__DispenseSprinkler
    @DispenseSprinkler.setter
    def DispenseSprinkler(self, DispenseSprinkler: bool):
        self.__DispenseSprinkler = DispenseSprinkler



class Sensor:

    def __init__(self, SensorID: int, SensorType: int, system16: "System" = None, door0: "Door" = None):
        self.SensorID = SensorID
        self.SensorType = SensorType
        self.system16 = system16
        self.door0 = door0
        
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
    def system16(self):
        return self.__system16
    @system16.setter
    def system16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sensor__system16", None)
        self.__system16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sensor17"):
                opp_val = getattr(old_value, "sensor17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sensor17"):
                opp_val = getattr(value, "sensor17", None)
                if opp_val is None:
                    setattr(value, "sensor17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class System:

    def __init__(self, Status: bool, Update: float, microPhone13: set["MicroPhone"] = None, sensor17: set["Sensor"] = None, houseHolds18: "HouseHolds" = None, homeTheatre21: "HomeTheatre" = None, home_Security_System23: "Home_Security_System" = None):
        self.Status = Status
        self.Update = Update
        self.microPhone13 = microPhone13 if microPhone13 is not None else set()
        self.sensor17 = sensor17 if sensor17 is not None else set()
        self.houseHolds18 = houseHolds18
        self.homeTheatre21 = homeTheatre21
        self.home_Security_System23 = home_Security_System23
        
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
    def microPhone13(self):
        return self.__microPhone13
    @microPhone13.setter
    def microPhone13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__microPhone13", None)
        self.__microPhone13 = value if value is not None else set()
        
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
    def homeTheatre21(self):
        return self.__homeTheatre21
    @homeTheatre21.setter
    def homeTheatre21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__homeTheatre21", None)
        self.__homeTheatre21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system20"):
                opp_val = getattr(old_value, "system20", None)
                if opp_val == self:
                    setattr(old_value, "system20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system20"):
                opp_val = getattr(value, "system20", None)
                setattr(value, "system20", self)

    @property
    def houseHolds18(self):
        return self.__houseHolds18
    @houseHolds18.setter
    def houseHolds18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__houseHolds18", None)
        self.__houseHolds18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system19"):
                opp_val = getattr(old_value, "system19", None)
                if opp_val == self:
                    setattr(old_value, "system19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system19"):
                opp_val = getattr(value, "system19", None)
                setattr(value, "system19", self)

    @property
    def home_Security_System23(self):
        return self.__home_Security_System23
    @home_Security_System23.setter
    def home_Security_System23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__home_Security_System23", None)
        self.__home_Security_System23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system22"):
                opp_val = getattr(old_value, "system22", None)
                if opp_val == self:
                    setattr(old_value, "system22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system22"):
                opp_val = getattr(value, "system22", None)
                setattr(value, "system22", self)

    @property
    def sensor17(self):
        return self.__sensor17
    @sensor17.setter
    def sensor17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__sensor17", None)
        self.__sensor17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "system16"):
                    opp_val = getattr(item, "system16", None)
                    
                    if opp_val == self:
                        setattr(item, "system16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "system16"):
                    opp_val = getattr(item, "system16", None)
                    
                    setattr(item, "system16", self)
                    

