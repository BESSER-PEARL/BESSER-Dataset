from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class TV:

    def __init__(self, TVID: int, entertainment22: "Entertainment" = None, homeTheatre5: set["HomeTheatre"] = None):
        self.TVID = TVID
        self.entertainment22 = entertainment22
        self.homeTheatre5 = homeTheatre5 if homeTheatre5 is not None else set()
        
        pass
    @property
    def TVID(self):
        return self.__TVID
    @TVID.setter
    def TVID(self, TVID: int):
        self.__TVID = TVID

    @property
    def entertainment22(self):
        return self.__entertainment22
    @entertainment22.setter
    def entertainment22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TV__entertainment22", None)
        self.__entertainment22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tV23"):
                opp_val = getattr(old_value, "tV23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tV23"):
                opp_val = getattr(value, "tV23", None)
                if opp_val is None:
                    setattr(value, "tV23", set([self]))
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
                    



class Evening:

    def __init__(self, Night: int, houseHolds11: "MyHome" = None):
        self.Night = Night
        self.houseHolds11 = houseHolds11
        
        pass
    @property
    def Night(self):
        return self.__Night
    @Night.setter
    def Night(self, Night: int):
        self.__Night = Night

    @property
    def houseHolds11(self):
        return self.__houseHolds11
    @houseHolds11.setter
    def houseHolds11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Evening__houseHolds11", None)
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



class Morning:

    def __init__(self, Morn: int, houseHolds9: "MyHome" = None):
        self.Morn = Morn
        self.houseHolds9 = houseHolds9
        
        pass
    @property
    def Morn(self):
        return self.__Morn
    @Morn.setter
    def Morn(self, Morn: int):
        self.__Morn = Morn

    @property
    def houseHolds9(self):
        return self.__houseHolds9
    @houseHolds9.setter
    def houseHolds9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Morning__houseHolds9", None)
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



class Radio:

    def __init__(self, RadioID: int, entertainment24: "Entertainment" = None, homeTheatre7: set["HomeTheatre"] = None):
        self.RadioID = RadioID
        self.entertainment24 = entertainment24
        self.homeTheatre7 = homeTheatre7 if homeTheatre7 is not None else set()
        
        pass
    @property
    def RadioID(self):
        return self.__RadioID
    @RadioID.setter
    def RadioID(self, RadioID: int):
        self.__RadioID = RadioID

    @property
    def homeTheatre7(self):
        return self.__homeTheatre7
    @homeTheatre7.setter
    def homeTheatre7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Radio__homeTheatre7", None)
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
    def entertainment24(self):
        return self.__entertainment24
    @entertainment24.setter
    def entertainment24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Radio__entertainment24", None)
        self.__entertainment24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "speakers25"):
                opp_val = getattr(old_value, "speakers25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "speakers25"):
                opp_val = getattr(value, "speakers25", None)
                if opp_val is None:
                    setattr(value, "speakers25", set([self]))
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

    def __init__(self, AlertID: int, home_Security_System13: "Home_Security_System" = None):
        self.AlertID = AlertID
        self.home_Security_System13 = home_Security_System13
        
        pass
    @property
    def AlertID(self):
        return self.__AlertID
    @AlertID.setter
    def AlertID(self, AlertID: int):
        self.__AlertID = AlertID

    @property
    def home_Security_System13(self):
        return self.__home_Security_System13
    @home_Security_System13.setter
    def home_Security_System13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Alert__home_Security_System13", None)
        self.__home_Security_System13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alert12"):
                opp_val = getattr(old_value, "alert12", None)
                if opp_val == self:
                    setattr(old_value, "alert12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alert12"):
                opp_val = getattr(value, "alert12", None)
                setattr(value, "alert12", self)



class Home_Security_System:

    def __init__(self, UserID: int, system20: "System___mirror" = None, alert12: "Alert" = None):
        self.UserID = UserID
        self.system20 = system20
        self.alert12 = alert12
        
        pass
    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: int):
        self.__UserID = UserID

    @property
    def system20(self):
        return self.__system20
    @system20.setter
    def system20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Home_Security_System__system20", None)
        self.__system20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "home_Security_System21"):
                opp_val = getattr(old_value, "home_Security_System21", None)
                if opp_val == self:
                    setattr(old_value, "home_Security_System21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "home_Security_System21"):
                opp_val = getattr(value, "home_Security_System21", None)
                setattr(value, "home_Security_System21", self)

    @property
    def alert12(self):
        return self.__alert12
    @alert12.setter
    def alert12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Home_Security_System__alert12", None)
        self.__alert12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "home_Security_System13"):
                opp_val = getattr(old_value, "home_Security_System13", None)
                if opp_val == self:
                    setattr(old_value, "home_Security_System13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "home_Security_System13"):
                opp_val = getattr(value, "home_Security_System13", None)
                setattr(value, "home_Security_System13", self)



class Door_Sensor:

    pass


class Motion_Sensor:

    pass


class FireAlarm_Sensor:

    def __init__(self, SmokeAlarm: bool):
        self.SmokeAlarm = SmokeAlarm
        
        pass
    @property
    def SmokeAlarm(self):
        return self.__SmokeAlarm
    @SmokeAlarm.setter
    def SmokeAlarm(self, SmokeAlarm: bool):
        self.__SmokeAlarm = SmokeAlarm



class Sensor:

    def __init__(self, SensorID: int, SensorType: int, door0: "Door" = None, system14: "System___mirror" = None):
        self.SensorID = SensorID
        self.SensorType = SensorType
        self.door0 = door0
        self.system14 = system14
        
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
    def system14(self):
        return self.__system14
    @system14.setter
    def system14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sensor__system14", None)
        self.__system14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sensor15"):
                opp_val = getattr(old_value, "sensor15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sensor15"):
                opp_val = getattr(value, "sensor15", None)
                if opp_val is None:
                    setattr(value, "sensor15", set([self]))
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



class System___mirror:

    def __init__(self, Status: bool, Update: float, PhoneConnect: bool, Display_feed: Newsfeed, security: Home_Security_System, houseHolds16: "MyHome" = None, homeTheatre19: "HomeTheatre" = None, home_Security_System21: "Home_Security_System" = None, newsfeed28: "Newsfeed" = None, sensor15: set["Sensor"] = None):
        self.Status = Status
        self.Update = Update
        self.PhoneConnect = PhoneConnect
        self.Display_feed = Display_feed
        self.security = security
        self.houseHolds16 = houseHolds16
        self.homeTheatre19 = homeTheatre19
        self.home_Security_System21 = home_Security_System21
        self.newsfeed28 = newsfeed28
        self.sensor15 = sensor15 if sensor15 is not None else set()
        
        pass
    @property
    def Display_feed(self):
        return self.__Display_feed
    @Display_feed.setter
    def Display_feed(self, Display_feed: Newsfeed):
        self.__Display_feed = Display_feed

    @property
    def PhoneConnect(self):
        return self.__PhoneConnect
    @PhoneConnect.setter
    def PhoneConnect(self, PhoneConnect: bool):
        self.__PhoneConnect = PhoneConnect

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
    def security(self):
        return self.__security
    @security.setter
    def security(self, security: Home_Security_System):
        self.__security = security

    @property
    def sensor15(self):
        return self.__sensor15
    @sensor15.setter
    def sensor15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System___mirror__sensor15", None)
        self.__sensor15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "system14"):
                    opp_val = getattr(item, "system14", None)
                    
                    if opp_val == self:
                        setattr(item, "system14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "system14"):
                    opp_val = getattr(item, "system14", None)
                    
                    setattr(item, "system14", self)
                    

    @property
    def homeTheatre19(self):
        return self.__homeTheatre19
    @homeTheatre19.setter
    def homeTheatre19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System___mirror__homeTheatre19", None)
        self.__homeTheatre19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system18"):
                opp_val = getattr(old_value, "system18", None)
                if opp_val == self:
                    setattr(old_value, "system18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system18"):
                opp_val = getattr(value, "system18", None)
                setattr(value, "system18", self)

    @property
    def houseHolds16(self):
        return self.__houseHolds16
    @houseHolds16.setter
    def houseHolds16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System___mirror__houseHolds16", None)
        self.__houseHolds16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system17"):
                opp_val = getattr(old_value, "system17", None)
                if opp_val == self:
                    setattr(old_value, "system17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system17"):
                opp_val = getattr(value, "system17", None)
                setattr(value, "system17", self)

    @property
    def home_Security_System21(self):
        return self.__home_Security_System21
    @home_Security_System21.setter
    def home_Security_System21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System___mirror__home_Security_System21", None)
        self.__home_Security_System21 = value
        
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
    def newsfeed28(self):
        return self.__newsfeed28
    @newsfeed28.setter
    def newsfeed28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System___mirror__newsfeed28", None)
        self.__newsfeed28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system___mirror29"):
                opp_val = getattr(old_value, "system___mirror29", None)
                if opp_val == self:
                    setattr(old_value, "system___mirror29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system___mirror29"):
                opp_val = getattr(value, "system___mirror29", None)
                setattr(value, "system___mirror29", self)



class Newsfeed:

    def __init__(self, Email: str, TimeID: str, News: str, weather: str, Calendar: str, system___mirror29: "System___mirror" = None):
        self.Email = Email
        self.TimeID = TimeID
        self.News = News
        self.weather = weather
        self.Calendar = Calendar
        self.system___mirror29 = system___mirror29
        
        pass
    @property
    def TimeID(self):
        return self.__TimeID
    @TimeID.setter
    def TimeID(self, TimeID: str):
        self.__TimeID = TimeID

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def News(self):
        return self.__News
    @News.setter
    def News(self, News: str):
        self.__News = News

    @property
    def Calendar(self):
        return self.__Calendar
    @Calendar.setter
    def Calendar(self, Calendar: str):
        self.__Calendar = Calendar

    @property
    def weather(self):
        return self.__weather
    @weather.setter
    def weather(self, weather: str):
        self.__weather = weather

    @property
    def system___mirror29(self):
        return self.__system___mirror29
    @system___mirror29.setter
    def system___mirror29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Newsfeed__system___mirror29", None)
        self.__system___mirror29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "newsfeed28"):
                opp_val = getattr(old_value, "newsfeed28", None)
                if opp_val == self:
                    setattr(old_value, "newsfeed28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "newsfeed28"):
                opp_val = getattr(value, "newsfeed28", None)
                setattr(value, "newsfeed28", self)



class Entertainment:

    def __init__(self, DeviceID: int, tV23: set["TV"] = None, speakers25: set["Radio"] = None, homeTheatre27: set["HomeTheatre"] = None):
        self.DeviceID = DeviceID
        self.tV23 = tV23 if tV23 is not None else set()
        self.speakers25 = speakers25 if speakers25 is not None else set()
        self.homeTheatre27 = homeTheatre27 if homeTheatre27 is not None else set()
        
        pass
    @property
    def DeviceID(self):
        return self.__DeviceID
    @DeviceID.setter
    def DeviceID(self, DeviceID: int):
        self.__DeviceID = DeviceID

    @property
    def tV23(self):
        return self.__tV23
    @tV23.setter
    def tV23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entertainment__tV23", None)
        self.__tV23 = value if value is not None else set()
        
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
    def speakers25(self):
        return self.__speakers25
    @speakers25.setter
    def speakers25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entertainment__speakers25", None)
        self.__speakers25 = value if value is not None else set()
        
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
    def homeTheatre27(self):
        return self.__homeTheatre27
    @homeTheatre27.setter
    def homeTheatre27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entertainment__homeTheatre27", None)
        self.__homeTheatre27 = value if value is not None else set()
        
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
                    



class MyHome:

    def __init__(self, TimeID: str, Coffee: str, DishWasher: str, Alarm: str, WashingMachine: str, system17: "System___mirror" = None, start_Of_Day8: "Morning" = None, end_Of_Day10: "Evening" = None):
        self.TimeID = TimeID
        self.Coffee = Coffee
        self.DishWasher = DishWasher
        self.Alarm = Alarm
        self.WashingMachine = WashingMachine
        self.system17 = system17
        self.start_Of_Day8 = start_Of_Day8
        self.end_Of_Day10 = end_Of_Day10
        
        pass
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
    def WashingMachine(self):
        return self.__WashingMachine
    @WashingMachine.setter
    def WashingMachine(self, WashingMachine: str):
        self.__WashingMachine = WashingMachine

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
    def start_Of_Day8(self):
        return self.__start_Of_Day8
    @start_Of_Day8.setter
    def start_Of_Day8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MyHome__start_Of_Day8", None)
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
        old_value = getattr(self, f"_MyHome__end_Of_Day10", None)
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
    def system17(self):
        return self.__system17
    @system17.setter
    def system17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MyHome__system17", None)
        self.__system17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "houseHolds16"):
                opp_val = getattr(old_value, "houseHolds16", None)
                if opp_val == self:
                    setattr(old_value, "houseHolds16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "houseHolds16"):
                opp_val = getattr(value, "houseHolds16", None)
                setattr(value, "houseHolds16", self)



class HomeTheatre:

    def __init__(self, HTID: str, system18: "System___mirror" = None, entertainment26: "Entertainment" = None, tV4: "TV" = None, speakers6: "Radio" = None):
        self.HTID = HTID
        self.system18 = system18
        self.entertainment26 = entertainment26
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
    def system18(self):
        return self.__system18
    @system18.setter
    def system18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HomeTheatre__system18", None)
        self.__system18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "homeTheatre19"):
                opp_val = getattr(old_value, "homeTheatre19", None)
                if opp_val == self:
                    setattr(old_value, "homeTheatre19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "homeTheatre19"):
                opp_val = getattr(value, "homeTheatre19", None)
                setattr(value, "homeTheatre19", self)

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
    def entertainment26(self):
        return self.__entertainment26
    @entertainment26.setter
    def entertainment26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HomeTheatre__entertainment26", None)
        self.__entertainment26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "homeTheatre27"):
                opp_val = getattr(old_value, "homeTheatre27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "homeTheatre27"):
                opp_val = getattr(value, "homeTheatre27", None)
                if opp_val is None:
                    setattr(value, "homeTheatre27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

