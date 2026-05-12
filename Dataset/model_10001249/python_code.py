from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Newsfeed:

    def __init__(self, Email: str, News: str, Weather: str, Calendar: str, Phone: str, smart_mirror15: "Smart_mirror" = None):
        self.Email = Email
        self.News = News
        self.Weather = Weather
        self.Calendar = Calendar
        self.Phone = Phone
        self.smart_mirror15 = smart_mirror15
        
        pass
    @property
    def Phone(self):
        return self.__Phone
    @Phone.setter
    def Phone(self, Phone: str):
        self.__Phone = Phone

    @property
    def Weather(self):
        return self.__Weather
    @Weather.setter
    def Weather(self, Weather: str):
        self.__Weather = Weather

    @property
    def News(self):
        return self.__News
    @News.setter
    def News(self, News: str):
        self.__News = News

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Calendar(self):
        return self.__Calendar
    @Calendar.setter
    def Calendar(self, Calendar: str):
        self.__Calendar = Calendar

    @property
    def smart_mirror15(self):
        return self.__smart_mirror15
    @smart_mirror15.setter
    def smart_mirror15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Newsfeed__smart_mirror15", None)
        self.__smart_mirror15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "voice_control214"):
                opp_val = getattr(old_value, "voice_control214", None)
                if opp_val == self:
                    setattr(old_value, "voice_control214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "voice_control214"):
                opp_val = getattr(value, "voice_control214", None)
                setattr(value, "voice_control214", self)



class HomeAutomation:

    def __init__(self, Lights: str, Apllicances: str, system10: "Smart_mirror" = None):
        self.Lights = Lights
        self.Apllicances = Apllicances
        self.system10 = system10
        
        pass
    @property
    def Apllicances(self):
        return self.__Apllicances
    @Apllicances.setter
    def Apllicances(self, Apllicances: str):
        self.__Apllicances = Apllicances

    @property
    def Lights(self):
        return self.__Lights
    @Lights.setter
    def Lights(self, Lights: str):
        self.__Lights = Lights

    @property
    def system10(self):
        return self.__system10
    @system10.setter
    def system10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HomeAutomation__system10", None)
        self.__system10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "homeTheatre11"):
                opp_val = getattr(old_value, "homeTheatre11", None)
                if opp_val == self:
                    setattr(old_value, "homeTheatre11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "homeTheatre11"):
                opp_val = getattr(value, "homeTheatre11", None)
                setattr(value, "homeTheatre11", self)



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



class Voice_control:

    def __init__(self, MicID: str, system4: "Smart_mirror" = None):
        self.MicID = MicID
        self.system4 = system4
        
        pass
    @property
    def MicID(self):
        return self.__MicID
    @MicID.setter
    def MicID(self, MicID: str):
        self.__MicID = MicID

    @property
    def system4(self):
        return self.__system4
    @system4.setter
    def system4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Voice_control__system4", None)
        self.__system4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "microPhone5"):
                opp_val = getattr(old_value, "microPhone5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "microPhone5"):
                opp_val = getattr(value, "microPhone5", None)
                if opp_val is None:
                    setattr(value, "microPhone5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Camera:

    def __init__(self, CameraID: int, door3: "Door_Sensor" = None):
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



class Door_Sensor:

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
        old_value = getattr(self, f"_Door_Sensor__sensor1", None)
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
        old_value = getattr(self, f"_Door_Sensor__camera2", None)
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

    def __init__(self, AlertID: int, home_Security_System7: "Home_Security_System" = None):
        self.AlertID = AlertID
        self.home_Security_System7 = home_Security_System7
        
        pass
    @property
    def AlertID(self):
        return self.__AlertID
    @AlertID.setter
    def AlertID(self, AlertID: int):
        self.__AlertID = AlertID

    @property
    def home_Security_System7(self):
        return self.__home_Security_System7
    @home_Security_System7.setter
    def home_Security_System7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Alert__home_Security_System7", None)
        self.__home_Security_System7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alert6"):
                opp_val = getattr(old_value, "alert6", None)
                if opp_val == self:
                    setattr(old_value, "alert6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alert6"):
                opp_val = getattr(value, "alert6", None)
                setattr(value, "alert6", self)



class Home_Security_System:

    def __init__(self, UserID: int, alert6: "Alert" = None, system12: "Smart_mirror" = None):
        self.UserID = UserID
        self.alert6 = alert6
        self.system12 = system12
        
        pass
    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: int):
        self.__UserID = UserID

    @property
    def alert6(self):
        return self.__alert6
    @alert6.setter
    def alert6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Home_Security_System__alert6", None)
        self.__alert6 = value
        
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
    def system12(self):
        return self.__system12
    @system12.setter
    def system12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Home_Security_System__system12", None)
        self.__system12 = value
        
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

    def __init__(self, SensorName: int, SensorID: int, door0: "Door_Sensor" = None, system8: "Smart_mirror" = None):
        self.SensorName = SensorName
        self.SensorID = SensorID
        self.door0 = door0
        self.system8 = system8
        
        pass
    @property
    def SensorID(self):
        return self.__SensorID
    @SensorID.setter
    def SensorID(self, SensorID: int):
        self.__SensorID = SensorID

    @property
    def SensorName(self):
        return self.__SensorName
    @SensorName.setter
    def SensorName(self, SensorName: int):
        self.__SensorName = SensorName

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
    def system8(self):
        return self.__system8
    @system8.setter
    def system8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sensor__system8", None)
        self.__system8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sensor9"):
                opp_val = getattr(old_value, "sensor9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sensor9"):
                opp_val = getattr(value, "sensor9", None)
                if opp_val is None:
                    setattr(value, "sensor9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Smart_mirror:

    def __init__(self, Status: bool, Update: float, PhoneConnect: bool, Display_newsfeed: Newsfeed, security: Home_Security_System, microPhone5: set["Voice_control"] = None, sensor9: set["Sensor"] = None, homeTheatre11: "HomeAutomation" = None, home_Security_System13: "Home_Security_System" = None, voice_control214: "Newsfeed" = None):
        self.Status = Status
        self.Update = Update
        self.PhoneConnect = PhoneConnect
        self.Display_newsfeed = Display_newsfeed
        self.security = security
        self.microPhone5 = microPhone5 if microPhone5 is not None else set()
        self.sensor9 = sensor9 if sensor9 is not None else set()
        self.homeTheatre11 = homeTheatre11
        self.home_Security_System13 = home_Security_System13
        self.voice_control214 = voice_control214
        
        pass
    @property
    def Update(self):
        return self.__Update
    @Update.setter
    def Update(self, Update: float):
        self.__Update = Update

    @property
    def security(self):
        return self.__security
    @security.setter
    def security(self, security: Home_Security_System):
        self.__security = security

    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: bool):
        self.__Status = Status

    @property
    def PhoneConnect(self):
        return self.__PhoneConnect
    @PhoneConnect.setter
    def PhoneConnect(self, PhoneConnect: bool):
        self.__PhoneConnect = PhoneConnect

    @property
    def Display_newsfeed(self):
        return self.__Display_newsfeed
    @Display_newsfeed.setter
    def Display_newsfeed(self, Display_newsfeed: Newsfeed):
        self.__Display_newsfeed = Display_newsfeed

    @property
    def homeTheatre11(self):
        return self.__homeTheatre11
    @homeTheatre11.setter
    def homeTheatre11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Smart_mirror__homeTheatre11", None)
        self.__homeTheatre11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system10"):
                opp_val = getattr(old_value, "system10", None)
                if opp_val == self:
                    setattr(old_value, "system10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system10"):
                opp_val = getattr(value, "system10", None)
                setattr(value, "system10", self)

    @property
    def home_Security_System13(self):
        return self.__home_Security_System13
    @home_Security_System13.setter
    def home_Security_System13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Smart_mirror__home_Security_System13", None)
        self.__home_Security_System13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system12"):
                opp_val = getattr(old_value, "system12", None)
                if opp_val == self:
                    setattr(old_value, "system12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system12"):
                opp_val = getattr(value, "system12", None)
                setattr(value, "system12", self)

    @property
    def voice_control214(self):
        return self.__voice_control214
    @voice_control214.setter
    def voice_control214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Smart_mirror__voice_control214", None)
        self.__voice_control214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smart_mirror15"):
                opp_val = getattr(old_value, "smart_mirror15", None)
                if opp_val == self:
                    setattr(old_value, "smart_mirror15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smart_mirror15"):
                opp_val = getattr(value, "smart_mirror15", None)
                setattr(value, "smart_mirror15", self)

    @property
    def microPhone5(self):
        return self.__microPhone5
    @microPhone5.setter
    def microPhone5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Smart_mirror__microPhone5", None)
        self.__microPhone5 = value if value is not None else set()
        
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
    def sensor9(self):
        return self.__sensor9
    @sensor9.setter
    def sensor9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Smart_mirror__sensor9", None)
        self.__sensor9 = value if value is not None else set()
        
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
                    

