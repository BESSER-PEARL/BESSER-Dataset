from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Lock_doors_sensors:

    def __init__(self, attribute: str, home_Security7: "Door_Security" = None):
        self.attribute = attribute
        self.home_Security7 = home_Security7
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def home_Security7(self):
        return self.__home_Security7
    @home_Security7.setter
    def home_Security7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lock_doors_sensors__home_Security7", None)
        self.__home_Security7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doors6"):
                opp_val = getattr(old_value, "doors6", None)
                if opp_val == self:
                    setattr(old_value, "doors6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doors6"):
                opp_val = getattr(value, "doors6", None)
                setattr(value, "doors6", self)



class Light_PIR_Sensor:

    def __init__(self, attribute: str, home_Security5: "Door_Security" = None):
        self.attribute = attribute
        self.home_Security5 = home_Security5
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def home_Security5(self):
        return self.__home_Security5
    @home_Security5.setter
    def home_Security5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Light_PIR_Sensor__home_Security5", None)
        self.__home_Security5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "light_Sensor4"):
                opp_val = getattr(old_value, "light_Sensor4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "light_Sensor4"):
                opp_val = getattr(value, "light_Sensor4", None)
                if opp_val is None:
                    setattr(value, "light_Sensor4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Event_Log:

    def __init__(self, attribute: str, home_Security3: "Door_Security" = None):
        self.attribute = attribute
        self.home_Security3 = home_Security3
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def home_Security3(self):
        return self.__home_Security3
    @home_Security3.setter
    def home_Security3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Event_Log__home_Security3", None)
        self.__home_Security3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "event_Log2"):
                opp_val = getattr(old_value, "event_Log2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "event_Log2"):
                opp_val = getattr(value, "event_Log2", None)
                if opp_val is None:
                    setattr(value, "event_Log2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Camera_sensor:

    def __init__(self, Image_ID: int, Video_ID: int, home_Security1: "Door_Security" = None):
        self.Image_ID = Image_ID
        self.Video_ID = Video_ID
        self.home_Security1 = home_Security1
        
        pass
    @property
    def Image_ID(self):
        return self.__Image_ID
    @Image_ID.setter
    def Image_ID(self, Image_ID: int):
        self.__Image_ID = Image_ID

    @property
    def Video_ID(self):
        return self.__Video_ID
    @Video_ID.setter
    def Video_ID(self, Video_ID: int):
        self.__Video_ID = Video_ID

    @property
    def home_Security1(self):
        return self.__home_Security1
    @home_Security1.setter
    def home_Security1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Camera_sensor__home_Security1", None)
        self.__home_Security1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "camera0"):
                opp_val = getattr(old_value, "camera0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "camera0"):
                opp_val = getattr(value, "camera0", None)
                if opp_val is None:
                    setattr(value, "camera0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Door_Security:

    pass
