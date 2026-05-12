from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class SteamGenerator:

    def __init__(self, Status: bool):
        self.Status = Status
        
        pass
    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: bool):
        self.__Status = Status



class Entertainment:

    def __init__(self, DeviceID: int, tV17: set["TV"] = None, speakers19: set["Speakers"] = None, homeTheatre21: set["HomeTheatre"] = None):
        self.DeviceID = DeviceID
        self.tV17 = tV17 if tV17 is not None else set()
        self.speakers19 = speakers19 if speakers19 is not None else set()
        self.homeTheatre21 = homeTheatre21 if homeTheatre21 is not None else set()
        
        pass
    @property
    def DeviceID(self):
        return self.__DeviceID
    @DeviceID.setter
    def DeviceID(self, DeviceID: int):
        self.__DeviceID = DeviceID

    @property
    def speakers19(self):
        return self.__speakers19
    @speakers19.setter
    def speakers19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entertainment__speakers19", None)
        self.__speakers19 = value if value is not None else set()
        
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
                    

    @property
    def tV17(self):
        return self.__tV17
    @tV17.setter
    def tV17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entertainment__tV17", None)
        self.__tV17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entertainment16"):
                    opp_val = getattr(item, "entertainment16", None)
                    
                    if opp_val == self:
                        setattr(item, "entertainment16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entertainment16"):
                    opp_val = getattr(item, "entertainment16", None)
                    
                    setattr(item, "entertainment16", self)
                    

    @property
    def homeTheatre21(self):
        return self.__homeTheatre21
    @homeTheatre21.setter
    def homeTheatre21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entertainment__homeTheatre21", None)
        self.__homeTheatre21 = value if value is not None else set()
        
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
                    



class HomeTheatre:

    def __init__(self, HTID: str, speakers4: "Speakers" = None, system12: set["System"] = None, entertainment20: "Entertainment" = None, tV2: "TV" = None):
        self.HTID = HTID
        self.speakers4 = speakers4
        self.system12 = system12 if system12 is not None else set()
        self.entertainment20 = entertainment20
        self.tV2 = tV2
        
        pass
    @property
    def HTID(self):
        return self.__HTID
    @HTID.setter
    def HTID(self, HTID: str):
        self.__HTID = HTID

    @property
    def entertainment20(self):
        return self.__entertainment20
    @entertainment20.setter
    def entertainment20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HomeTheatre__entertainment20", None)
        self.__entertainment20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "homeTheatre21"):
                opp_val = getattr(old_value, "homeTheatre21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "homeTheatre21"):
                opp_val = getattr(value, "homeTheatre21", None)
                if opp_val is None:
                    setattr(value, "homeTheatre21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def speakers4(self):
        return self.__speakers4
    @speakers4.setter
    def speakers4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HomeTheatre__speakers4", None)
        self.__speakers4 = value
        
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
    def system12(self):
        return self.__system12
    @system12.setter
    def system12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HomeTheatre__system12", None)
        self.__system12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "homeTheatre13"):
                    opp_val = getattr(item, "homeTheatre13", None)
                    
                    if opp_val == self:
                        setattr(item, "homeTheatre13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "homeTheatre13"):
                    opp_val = getattr(item, "homeTheatre13", None)
                    
                    setattr(item, "homeTheatre13", self)
                    

    @property
    def tV2(self):
        return self.__tV2
    @tV2.setter
    def tV2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HomeTheatre__tV2", None)
        self.__tV2 = value
        
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



class TV:

    def __init__(self, TVID: int, entertainment16: "Entertainment" = None, homeTheatre3: set["HomeTheatre"] = None):
        self.TVID = TVID
        self.entertainment16 = entertainment16
        self.homeTheatre3 = homeTheatre3 if homeTheatre3 is not None else set()
        
        pass
    @property
    def TVID(self):
        return self.__TVID
    @TVID.setter
    def TVID(self, TVID: int):
        self.__TVID = TVID

    @property
    def homeTheatre3(self):
        return self.__homeTheatre3
    @homeTheatre3.setter
    def homeTheatre3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TV__homeTheatre3", None)
        self.__homeTheatre3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tV2"):
                    opp_val = getattr(item, "tV2", None)
                    
                    if opp_val == self:
                        setattr(item, "tV2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tV2"):
                    opp_val = getattr(item, "tV2", None)
                    
                    setattr(item, "tV2", self)
                    

    @property
    def entertainment16(self):
        return self.__entertainment16
    @entertainment16.setter
    def entertainment16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TV__entertainment16", None)
        self.__entertainment16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tV17"):
                opp_val = getattr(old_value, "tV17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tV17"):
                opp_val = getattr(value, "tV17", None)
                if opp_val is None:
                    setattr(value, "tV17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Heater:

    def __init__(self, Status: bool):
        self.Status = Status
        
        pass
    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: bool):
        self.__Status = Status



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



class Speakers:

    def __init__(self, SpeakerID: int, homeTheatre5: set["HomeTheatre"] = None, entertainment18: "Entertainment" = None):
        self.SpeakerID = SpeakerID
        self.homeTheatre5 = homeTheatre5 if homeTheatre5 is not None else set()
        self.entertainment18 = entertainment18
        
        pass
    @property
    def SpeakerID(self):
        return self.__SpeakerID
    @SpeakerID.setter
    def SpeakerID(self, SpeakerID: int):
        self.__SpeakerID = SpeakerID

    @property
    def entertainment18(self):
        return self.__entertainment18
    @entertainment18.setter
    def entertainment18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Speakers__entertainment18", None)
        self.__entertainment18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "speakers19"):
                opp_val = getattr(old_value, "speakers19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "speakers19"):
                opp_val = getattr(value, "speakers19", None)
                if opp_val is None:
                    setattr(value, "speakers19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def homeTheatre5(self):
        return self.__homeTheatre5
    @homeTheatre5.setter
    def homeTheatre5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Speakers__homeTheatre5", None)
        self.__homeTheatre5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "speakers4"):
                    opp_val = getattr(item, "speakers4", None)
                    
                    if opp_val == self:
                        setattr(item, "speakers4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "speakers4"):
                    opp_val = getattr(item, "speakers4", None)
                    
                    setattr(item, "speakers4", self)
                    



class Interior_Container:

    def __init__(self, WorkMode: int, sensor1: "Sensor" = None):
        self.WorkMode = WorkMode
        self.sensor1 = sensor1
        
        pass
    @property
    def WorkMode(self):
        return self.__WorkMode
    @WorkMode.setter
    def WorkMode(self, WorkMode: int):
        self.__WorkMode = WorkMode

    @property
    def sensor1(self):
        return self.__sensor1
    @sensor1.setter
    def sensor1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Interior_Container__sensor1", None)
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



class Ingredient_Box:

    def __init__(self, BoxID: int, WeightValue: float, home_Security_System9: "Cooking_System" = None):
        self.BoxID = BoxID
        self.WeightValue = WeightValue
        self.home_Security_System9 = home_Security_System9
        
        pass
    @property
    def WeightValue(self):
        return self.__WeightValue
    @WeightValue.setter
    def WeightValue(self, WeightValue: float):
        self.__WeightValue = WeightValue

    @property
    def BoxID(self):
        return self.__BoxID
    @BoxID.setter
    def BoxID(self, BoxID: int):
        self.__BoxID = BoxID

    @property
    def home_Security_System9(self):
        return self.__home_Security_System9
    @home_Security_System9.setter
    def home_Security_System9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ingredient_Box__home_Security_System9", None)
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



class Cooking_System:

    pass


class Humidity_Sensor:

    def __init__(self, CurrentValue: float):
        self.CurrentValue = CurrentValue
        
        pass
    @property
    def CurrentValue(self):
        return self.__CurrentValue
    @CurrentValue.setter
    def CurrentValue(self, CurrentValue: float):
        self.__CurrentValue = CurrentValue



class Temperature_Sensor:

    def __init__(self, CurrentValue: float):
        self.CurrentValue = CurrentValue
        
        pass
    @property
    def CurrentValue(self):
        return self.__CurrentValue
    @CurrentValue.setter
    def CurrentValue(self, CurrentValue: float):
        self.__CurrentValue = CurrentValue



class Sensor:

    def __init__(self, SensorID: int, SensorType: int, system10: "System" = None, door0: "Interior_Container" = None):
        self.SensorID = SensorID
        self.SensorType = SensorType
        self.system10 = system10
        self.door0 = door0
        
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

    def __init__(self, Status: bool, Update: float, microPhone7: set["MicroPhone"] = None, sensor11: set["Sensor"] = None, homeTheatre13: "HomeTheatre" = None, Cooking_System15: "Cooking_System" = None):
        self.Status = Status
        self.Update = Update
        self.microPhone7 = microPhone7 if microPhone7 is not None else set()
        self.sensor11 = sensor11 if sensor11 is not None else set()
        self.homeTheatre13 = homeTheatre13
        self.Cooking_System15 = Cooking_System15
        
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
    def Cooking_System15(self):
        return self.__Cooking_System15
    @Cooking_System15.setter
    def Cooking_System15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__Cooking_System15", None)
        self.__Cooking_System15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Home_Security_System_System_014"):
                opp_val = getattr(old_value, "Home_Security_System_System_014", None)
                if opp_val == self:
                    setattr(old_value, "Home_Security_System_System_014", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Home_Security_System_System_014"):
                opp_val = getattr(value, "Home_Security_System_System_014", None)
                setattr(value, "Home_Security_System_System_014", self)

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
    def homeTheatre13(self):
        return self.__homeTheatre13
    @homeTheatre13.setter
    def homeTheatre13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__homeTheatre13", None)
        self.__homeTheatre13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system12"):
                opp_val = getattr(old_value, "system12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system12"):
                opp_val = getattr(value, "system12", None)
                if opp_val is None:
                    setattr(value, "system12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                    

