from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Motion_Sensor:

    def __init__(self, Sensor_ID: str):
        self.Sensor_ID = Sensor_ID
        
        pass
    @property
    def Sensor_ID(self):
        return self.__Sensor_ID
    @Sensor_ID.setter
    def Sensor_ID(self, Sensor_ID: str):
        self.__Sensor_ID = Sensor_ID



class T:

    pass


class Dispatch_drown:

    def __init__(self, Drown_ID: str, Camera_ID: str):
        self.Drown_ID = Drown_ID
        self.Camera_ID = Camera_ID
        
        pass
    @property
    def Camera_ID(self):
        return self.__Camera_ID
    @Camera_ID.setter
    def Camera_ID(self, Camera_ID: str):
        self.__Camera_ID = Camera_ID

    @property
    def Drown_ID(self):
        return self.__Drown_ID
    @Drown_ID.setter
    def Drown_ID(self, Drown_ID: str):
        self.__Drown_ID = Drown_ID



class Temperature_sensor:

    def __init__(self, Temp_ID: str, home_Security11: "Camera_1" = None):
        self.Temp_ID = Temp_ID
        self.home_Security11 = home_Security11
        
        pass
    @property
    def Temp_ID(self):
        return self.__Temp_ID
    @Temp_ID.setter
    def Temp_ID(self, Temp_ID: str):
        self.__Temp_ID = Temp_ID

    @property
    def home_Security11(self):
        return self.__home_Security11
    @home_Security11.setter
    def home_Security11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Temperature_sensor__home_Security11", None)
        self.__home_Security11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "temperature_sensor10"):
                opp_val = getattr(old_value, "temperature_sensor10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "temperature_sensor10"):
                opp_val = getattr(value, "temperature_sensor10", None)
                if opp_val is None:
                    setattr(value, "temperature_sensor10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Security_logs:

    def __init__(self, Log_ID: str, Sensor_ID: str, Camera_ID: str, home_Security1: "Home_Security__Hub_" = None):
        self.Log_ID = Log_ID
        self.Sensor_ID = Sensor_ID
        self.Camera_ID = Camera_ID
        self.home_Security1 = home_Security1
        
        pass
    @property
    def Sensor_ID(self):
        return self.__Sensor_ID
    @Sensor_ID.setter
    def Sensor_ID(self, Sensor_ID: str):
        self.__Sensor_ID = Sensor_ID

    @property
    def Log_ID(self):
        return self.__Log_ID
    @Log_ID.setter
    def Log_ID(self, Log_ID: str):
        self.__Log_ID = Log_ID

    @property
    def Camera_ID(self):
        return self.__Camera_ID
    @Camera_ID.setter
    def Camera_ID(self, Camera_ID: str):
        self.__Camera_ID = Camera_ID

    @property
    def home_Security1(self):
        return self.__home_Security1
    @home_Security1.setter
    def home_Security1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Security_logs__home_Security1", None)
        self.__home_Security1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "server0"):
                opp_val = getattr(old_value, "server0", None)
                if opp_val == self:
                    setattr(old_value, "server0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "server0"):
                opp_val = getattr(value, "server0", None)
                setattr(value, "server0", self)



class Lock_doors:

    def __init__(self, Door_ID: str, home_Security9: "Home_Security__Hub_" = None):
        self.Door_ID = Door_ID
        self.home_Security9 = home_Security9
        
        pass
    @property
    def Door_ID(self):
        return self.__Door_ID
    @Door_ID.setter
    def Door_ID(self, Door_ID: str):
        self.__Door_ID = Door_ID

    @property
    def home_Security9(self):
        return self.__home_Security9
    @home_Security9.setter
    def home_Security9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lock_doors__home_Security9", None)
        self.__home_Security9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doors8"):
                opp_val = getattr(old_value, "doors8", None)
                if opp_val == self:
                    setattr(old_value, "doors8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doors8"):
                opp_val = getattr(value, "doors8", None)
                setattr(value, "doors8", self)



class Light_Sensor:

    def __init__(self, Sensor_ID: str, home_Security7: "Camera_1" = None):
        self.Sensor_ID = Sensor_ID
        self.home_Security7 = home_Security7
        
        pass
    @property
    def Sensor_ID(self):
        return self.__Sensor_ID
    @Sensor_ID.setter
    def Sensor_ID(self, Sensor_ID: str):
        self.__Sensor_ID = Sensor_ID

    @property
    def home_Security7(self):
        return self.__home_Security7
    @home_Security7.setter
    def home_Security7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Light_Sensor__home_Security7", None)
        self.__home_Security7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "light_Sensor6"):
                opp_val = getattr(old_value, "light_Sensor6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "light_Sensor6"):
                opp_val = getattr(value, "light_Sensor6", None)
                if opp_val is None:
                    setattr(value, "light_Sensor6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Event_Log:

    def __init__(self, Status: bool, home_Security5: "Home_Security__Hub_" = None):
        self.Status = Status
        self.home_Security5 = home_Security5
        
        pass
    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: bool):
        self.__Status = Status

    @property
    def home_Security5(self):
        return self.__home_Security5
    @home_Security5.setter
    def home_Security5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Event_Log__home_Security5", None)
        self.__home_Security5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "event_Log4"):
                opp_val = getattr(old_value, "event_Log4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "event_Log4"):
                opp_val = getattr(value, "event_Log4", None)
                if opp_val is None:
                    setattr(value, "event_Log4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Camera_1:

    def __init__(self, Camera_ID: str, Sensor_ID: str, home_Security3: "Home_Security__Hub_" = None, light_Sensor6: set["Light_Sensor"] = None, temperature_sensor10: set["Temperature_sensor"] = None, camera_112: "Camera_1" = None, camera_113: "Camera_1" = None):
        self.Camera_ID = Camera_ID
        self.Sensor_ID = Sensor_ID
        self.home_Security3 = home_Security3
        self.light_Sensor6 = light_Sensor6 if light_Sensor6 is not None else set()
        self.temperature_sensor10 = temperature_sensor10 if temperature_sensor10 is not None else set()
        self.camera_112 = camera_112
        self.camera_113 = camera_113
        
        pass
    @property
    def Sensor_ID(self):
        return self.__Sensor_ID
    @Sensor_ID.setter
    def Sensor_ID(self, Sensor_ID: str):
        self.__Sensor_ID = Sensor_ID

    @property
    def Camera_ID(self):
        return self.__Camera_ID
    @Camera_ID.setter
    def Camera_ID(self, Camera_ID: str):
        self.__Camera_ID = Camera_ID

    @property
    def camera_112(self):
        return self.__camera_112
    @camera_112.setter
    def camera_112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Camera_1__camera_112", None)
        self.__camera_112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "camera_113"):
                opp_val = getattr(old_value, "camera_113", None)
                if opp_val == self:
                    setattr(old_value, "camera_113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "camera_113"):
                opp_val = getattr(value, "camera_113", None)
                setattr(value, "camera_113", self)

    @property
    def temperature_sensor10(self):
        return self.__temperature_sensor10
    @temperature_sensor10.setter
    def temperature_sensor10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Camera_1__temperature_sensor10", None)
        self.__temperature_sensor10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "home_Security11"):
                    opp_val = getattr(item, "home_Security11", None)
                    
                    if opp_val == self:
                        setattr(item, "home_Security11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "home_Security11"):
                    opp_val = getattr(item, "home_Security11", None)
                    
                    setattr(item, "home_Security11", self)
                    

    @property
    def light_Sensor6(self):
        return self.__light_Sensor6
    @light_Sensor6.setter
    def light_Sensor6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Camera_1__light_Sensor6", None)
        self.__light_Sensor6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "home_Security7"):
                    opp_val = getattr(item, "home_Security7", None)
                    
                    if opp_val == self:
                        setattr(item, "home_Security7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "home_Security7"):
                    opp_val = getattr(item, "home_Security7", None)
                    
                    setattr(item, "home_Security7", self)
                    

    @property
    def camera_113(self):
        return self.__camera_113
    @camera_113.setter
    def camera_113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Camera_1__camera_113", None)
        self.__camera_113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "camera_112"):
                opp_val = getattr(old_value, "camera_112", None)
                if opp_val == self:
                    setattr(old_value, "camera_112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "camera_112"):
                opp_val = getattr(value, "camera_112", None)
                setattr(value, "camera_112", self)

    @property
    def home_Security3(self):
        return self.__home_Security3
    @home_Security3.setter
    def home_Security3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Camera_1__home_Security3", None)
        self.__home_Security3 = value
        
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



class Home_Security__Hub_:

    def __init__(self, Sensor_ID: str, Camera_ID: str, Hub_ID: str, Login_ID: str, server0: "Security_logs" = None, camera2: set["Camera_1"] = None, event_Log4: set["Event_Log"] = None, doors8: "Lock_doors" = None):
        self.Sensor_ID = Sensor_ID
        self.Camera_ID = Camera_ID
        self.Hub_ID = Hub_ID
        self.Login_ID = Login_ID
        self.server0 = server0
        self.camera2 = camera2 if camera2 is not None else set()
        self.event_Log4 = event_Log4 if event_Log4 is not None else set()
        self.doors8 = doors8
        
        pass
    @property
    def Login_ID(self):
        return self.__Login_ID
    @Login_ID.setter
    def Login_ID(self, Login_ID: str):
        self.__Login_ID = Login_ID

    @property
    def Hub_ID(self):
        return self.__Hub_ID
    @Hub_ID.setter
    def Hub_ID(self, Hub_ID: str):
        self.__Hub_ID = Hub_ID

    @property
    def Camera_ID(self):
        return self.__Camera_ID
    @Camera_ID.setter
    def Camera_ID(self, Camera_ID: str):
        self.__Camera_ID = Camera_ID

    @property
    def Sensor_ID(self):
        return self.__Sensor_ID
    @Sensor_ID.setter
    def Sensor_ID(self, Sensor_ID: str):
        self.__Sensor_ID = Sensor_ID

    @property
    def doors8(self):
        return self.__doors8
    @doors8.setter
    def doors8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Home_Security__Hub___doors8", None)
        self.__doors8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "home_Security9"):
                opp_val = getattr(old_value, "home_Security9", None)
                if opp_val == self:
                    setattr(old_value, "home_Security9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "home_Security9"):
                opp_val = getattr(value, "home_Security9", None)
                setattr(value, "home_Security9", self)

    @property
    def camera2(self):
        return self.__camera2
    @camera2.setter
    def camera2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Home_Security__Hub___camera2", None)
        self.__camera2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "home_Security3"):
                    opp_val = getattr(item, "home_Security3", None)
                    
                    if opp_val == self:
                        setattr(item, "home_Security3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "home_Security3"):
                    opp_val = getattr(item, "home_Security3", None)
                    
                    setattr(item, "home_Security3", self)
                    

    @property
    def server0(self):
        return self.__server0
    @server0.setter
    def server0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Home_Security__Hub___server0", None)
        self.__server0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "home_Security1"):
                opp_val = getattr(old_value, "home_Security1", None)
                if opp_val == self:
                    setattr(old_value, "home_Security1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "home_Security1"):
                opp_val = getattr(value, "home_Security1", None)
                setattr(value, "home_Security1", self)

    @property
    def event_Log4(self):
        return self.__event_Log4
    @event_Log4.setter
    def event_Log4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Home_Security__Hub___event_Log4", None)
        self.__event_Log4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "home_Security5"):
                    opp_val = getattr(item, "home_Security5", None)
                    
                    if opp_val == self:
                        setattr(item, "home_Security5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "home_Security5"):
                    opp_val = getattr(item, "home_Security5", None)
                    
                    setattr(item, "home_Security5", self)
                    

