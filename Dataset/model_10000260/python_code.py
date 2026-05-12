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



class Display:

    pass


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



class PhoneApplication:

    pass


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

    def __init__(self, BoxID: int, WeightValue: float, home_Security_System5: "Cooking_System" = None):
        self.BoxID = BoxID
        self.WeightValue = WeightValue
        self.home_Security_System5 = home_Security_System5
        
        pass
    @property
    def BoxID(self):
        return self.__BoxID
    @BoxID.setter
    def BoxID(self, BoxID: int):
        self.__BoxID = BoxID

    @property
    def WeightValue(self):
        return self.__WeightValue
    @WeightValue.setter
    def WeightValue(self, WeightValue: float):
        self.__WeightValue = WeightValue

    @property
    def home_Security_System5(self):
        return self.__home_Security_System5
    @home_Security_System5.setter
    def home_Security_System5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ingredient_Box__home_Security_System5", None)
        self.__home_Security_System5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alert4"):
                opp_val = getattr(old_value, "alert4", None)
                if opp_val == self:
                    setattr(old_value, "alert4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alert4"):
                opp_val = getattr(value, "alert4", None)
                setattr(value, "alert4", self)



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

    def __init__(self, SensorID: int, SensorType: int, door0: "Interior_Container" = None, system6: "System" = None):
        self.SensorID = SensorID
        self.SensorType = SensorType
        self.door0 = door0
        self.system6 = system6
        
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
    def system6(self):
        return self.__system6
    @system6.setter
    def system6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sensor__system6", None)
        self.__system6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sensor7"):
                opp_val = getattr(old_value, "sensor7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sensor7"):
                opp_val = getattr(value, "sensor7", None)
                if opp_val is None:
                    setattr(value, "sensor7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class System:

    def __init__(self, Status: bool, Update: float, microPhone3: set["PhoneApplication"] = None, sensor7: set["Sensor"] = None, homeTheatre9: "Display" = None, Cooking_System11: "Cooking_System" = None):
        self.Status = Status
        self.Update = Update
        self.microPhone3 = microPhone3 if microPhone3 is not None else set()
        self.sensor7 = sensor7 if sensor7 is not None else set()
        self.homeTheatre9 = homeTheatre9
        self.Cooking_System11 = Cooking_System11
        
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
    def microPhone3(self):
        return self.__microPhone3
    @microPhone3.setter
    def microPhone3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__microPhone3", None)
        self.__microPhone3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "system2"):
                    opp_val = getattr(item, "system2", None)
                    
                    if opp_val == self:
                        setattr(item, "system2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "system2"):
                    opp_val = getattr(item, "system2", None)
                    
                    setattr(item, "system2", self)
                    

    @property
    def homeTheatre9(self):
        return self.__homeTheatre9
    @homeTheatre9.setter
    def homeTheatre9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__homeTheatre9", None)
        self.__homeTheatre9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system8"):
                opp_val = getattr(old_value, "system8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system8"):
                opp_val = getattr(value, "system8", None)
                if opp_val is None:
                    setattr(value, "system8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sensor7(self):
        return self.__sensor7
    @sensor7.setter
    def sensor7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__sensor7", None)
        self.__sensor7 = value if value is not None else set()
        
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
    def Cooking_System11(self):
        return self.__Cooking_System11
    @Cooking_System11.setter
    def Cooking_System11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__Cooking_System11", None)
        self.__Cooking_System11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Home_Security_System_System_010"):
                opp_val = getattr(old_value, "Home_Security_System_System_010", None)
                if opp_val == self:
                    setattr(old_value, "Home_Security_System_System_010", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Home_Security_System_System_010"):
                opp_val = getattr(value, "Home_Security_System_System_010", None)
                setattr(value, "Home_Security_System_System_010", self)

