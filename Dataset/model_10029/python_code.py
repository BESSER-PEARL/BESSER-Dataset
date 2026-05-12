from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Mode(Enum):
    Initialization = "Initialization"
    Rescue = "Rescue"
    EmergencyStop = "EmergencyStop"
    Normal = "Normal"
    Dameged = "Dameged"
    Degraded = "Degraded"
class ValveState(Enum):
    Open = "Open"
    Closed = "Closed"
class State(Enum):
    On = "On"
    Off = "Off"


############################################
# Definition of Classes
############################################

class SBCS_Transition:

    pass
class SBCS_SteamBoiler:

    def __init__(self, minimalNormal: float, maximalNormal: float, valveOpen: str, capacity: float, SBCS_SteamBoiler: "SBCS_Snapshot" = None, SBCS_SteamBoiler3: "SBCS_ControlProgram" = None, SBCS_SteamBoiler6: "SBCS_WaterLevelMeasurementDevice" = None, SBCS_SteamBoiler17: "SBCS_SteamBoiler_OpenValve" = None, SBCS_SteamBoiler24: "SBCS_WaterLevelMeasurementDevice" = None, SBCS_SteamBoiler14: "SBCS_SteamBoiler_OpenValve" = None):
        self.minimalNormal = minimalNormal
        self.maximalNormal = maximalNormal
        self.valveOpen = valveOpen
        self.capacity = capacity
        self.SBCS_SteamBoiler = SBCS_SteamBoiler
        self.SBCS_SteamBoiler3 = SBCS_SteamBoiler3
        self.SBCS_SteamBoiler6 = SBCS_SteamBoiler6
        self.SBCS_SteamBoiler17 = SBCS_SteamBoiler17
        self.SBCS_SteamBoiler24 = SBCS_SteamBoiler24
        self.SBCS_SteamBoiler14 = SBCS_SteamBoiler14
        
        pass
    @property
    def minimalNormal(self):
        return self.__minimalNormal

    @minimalNormal.setter
    def minimalNormal(self, minimalNormal: float):
        self.__minimalNormal = minimalNormal


    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: float):
        self.__capacity = capacity


    @property
    def valveOpen(self):
        return self.__valveOpen

    @valveOpen.setter
    def valveOpen(self, valveOpen: str):
        self.__valveOpen = valveOpen


    @property
    def maximalNormal(self):
        return self.__maximalNormal

    @maximalNormal.setter
    def maximalNormal(self, maximalNormal: float):
        self.__maximalNormal = maximalNormal


    @property
    def SBCS_SteamBoiler(self):
        return self.__SBCS_SteamBoiler

    @SBCS_SteamBoiler.setter
    def SBCS_SteamBoiler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamBoiler__SBCS_SteamBoiler", None)
        self.__SBCS_SteamBoiler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_Snapshot"):
                opp_val = getattr(old_value, "SBCS_Snapshot", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_Snapshot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_Snapshot"):
                opp_val = getattr(value, "SBCS_Snapshot", None)
                setattr(value, "SBCS_Snapshot", self)

    @property
    def SBCS_SteamBoiler17(self):
        return self.__SBCS_SteamBoiler17

    @SBCS_SteamBoiler17.setter
    def SBCS_SteamBoiler17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamBoiler__SBCS_SteamBoiler17", None)
        self.__SBCS_SteamBoiler17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_SteamBoiler_OpenValve16"):
                opp_val = getattr(old_value, "SBCS_SteamBoiler_OpenValve16", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_SteamBoiler_OpenValve16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_SteamBoiler_OpenValve16"):
                opp_val = getattr(value, "SBCS_SteamBoiler_OpenValve16", None)
                setattr(value, "SBCS_SteamBoiler_OpenValve16", self)

    @property
    def SBCS_SteamBoiler6(self):
        return self.__SBCS_SteamBoiler6

    @SBCS_SteamBoiler6.setter
    def SBCS_SteamBoiler6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamBoiler__SBCS_SteamBoiler6", None)
        self.__SBCS_SteamBoiler6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_WaterLevelMeasurementDevice"):
                opp_val = getattr(old_value, "SBCS_WaterLevelMeasurementDevice", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_WaterLevelMeasurementDevice", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_WaterLevelMeasurementDevice"):
                opp_val = getattr(value, "SBCS_WaterLevelMeasurementDevice", None)
                setattr(value, "SBCS_WaterLevelMeasurementDevice", self)

    @property
    def SBCS_SteamBoiler14(self):
        return self.__SBCS_SteamBoiler14

    @SBCS_SteamBoiler14.setter
    def SBCS_SteamBoiler14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamBoiler__SBCS_SteamBoiler14", None)
        self.__SBCS_SteamBoiler14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_SteamBoiler_OpenValve"):
                opp_val = getattr(old_value, "SBCS_SteamBoiler_OpenValve", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_SteamBoiler_OpenValve", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_SteamBoiler_OpenValve"):
                opp_val = getattr(value, "SBCS_SteamBoiler_OpenValve", None)
                setattr(value, "SBCS_SteamBoiler_OpenValve", self)

    @property
    def SBCS_SteamBoiler24(self):
        return self.__SBCS_SteamBoiler24

    @SBCS_SteamBoiler24.setter
    def SBCS_SteamBoiler24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamBoiler__SBCS_SteamBoiler24", None)
        self.__SBCS_SteamBoiler24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_WaterLevelMeasurementDevice23"):
                opp_val = getattr(old_value, "SBCS_WaterLevelMeasurementDevice23", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_WaterLevelMeasurementDevice23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_WaterLevelMeasurementDevice23"):
                opp_val = getattr(value, "SBCS_WaterLevelMeasurementDevice23", None)
                setattr(value, "SBCS_WaterLevelMeasurementDevice23", self)

    @property
    def SBCS_SteamBoiler3(self):
        return self.__SBCS_SteamBoiler3

    @SBCS_SteamBoiler3.setter
    def SBCS_SteamBoiler3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamBoiler__SBCS_SteamBoiler3", None)
        self.__SBCS_SteamBoiler3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_ControlProgram4"):
                opp_val = getattr(old_value, "SBCS_ControlProgram4", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_ControlProgram4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_ControlProgram4"):
                opp_val = getattr(value, "SBCS_ControlProgram4", None)
                setattr(value, "SBCS_ControlProgram4", self)

class SBCS_ControlProgram:

    def __init__(self, mode: str, SBCS_ControlProgram4: "SBCS_SteamBoiler" = None, SBCS_ControlProgram: "SBCS_ControlProgram_Start" = None, SBCS_ControlProgram27: "SBCS_Snapshot" = None):
        self.mode = mode
        self.SBCS_ControlProgram4 = SBCS_ControlProgram4
        self.SBCS_ControlProgram = SBCS_ControlProgram
        self.SBCS_ControlProgram27 = SBCS_ControlProgram27
        
        pass
    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode


    @property
    def SBCS_ControlProgram4(self):
        return self.__SBCS_ControlProgram4

    @SBCS_ControlProgram4.setter
    def SBCS_ControlProgram4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_ControlProgram__SBCS_ControlProgram4", None)
        self.__SBCS_ControlProgram4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_SteamBoiler3"):
                opp_val = getattr(old_value, "SBCS_SteamBoiler3", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_SteamBoiler3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_SteamBoiler3"):
                opp_val = getattr(value, "SBCS_SteamBoiler3", None)
                setattr(value, "SBCS_SteamBoiler3", self)

    @property
    def SBCS_ControlProgram27(self):
        return self.__SBCS_ControlProgram27

    @SBCS_ControlProgram27.setter
    def SBCS_ControlProgram27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_ControlProgram__SBCS_ControlProgram27", None)
        self.__SBCS_ControlProgram27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_Snapshot26"):
                opp_val = getattr(old_value, "SBCS_Snapshot26", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_Snapshot26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_Snapshot26"):
                opp_val = getattr(value, "SBCS_Snapshot26", None)
                setattr(value, "SBCS_Snapshot26", self)

    @property
    def SBCS_ControlProgram(self):
        return self.__SBCS_ControlProgram

    @SBCS_ControlProgram.setter
    def SBCS_ControlProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_ControlProgram__SBCS_ControlProgram", None)
        self.__SBCS_ControlProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_ControlProgram_Start"):
                opp_val = getattr(old_value, "SBCS_ControlProgram_Start", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_ControlProgram_Start", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_ControlProgram_Start"):
                opp_val = getattr(value, "SBCS_ControlProgram_Start", None)
                setattr(value, "SBCS_ControlProgram_Start", self)

class Transition:

    pass
class SBCS_PumpController_ClosePump(Transition):

    pass
class SBCS_PumpController_OpenPump(Transition):

    pass
class SBCS_SteamBoiler_OpenValve(Transition):

    pass
class SBCS_WaterLevelMeaurementDevice_getLevel(Transition):

    def __init__(self, ret: float, SBCS_WaterLevelMeaurementDevice_getLevel: "SBCS_WaterLevelMeasurementDevice" = None):
        self.ret = ret
        self.SBCS_WaterLevelMeaurementDevice_getLevel = SBCS_WaterLevelMeaurementDevice_getLevel
        
        pass
    @property
    def ret(self):
        return self.__ret

    @ret.setter
    def ret(self, ret: float):
        self.__ret = ret


    @property
    def SBCS_WaterLevelMeaurementDevice_getLevel(self):
        return self.__SBCS_WaterLevelMeaurementDevice_getLevel

    @SBCS_WaterLevelMeaurementDevice_getLevel.setter
    def SBCS_WaterLevelMeaurementDevice_getLevel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_WaterLevelMeaurementDevice_getLevel__SBCS_WaterLevelMeaurementDevice_getLevel", None)
        self.__SBCS_WaterLevelMeaurementDevice_getLevel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_WaterLevelMeasurementDevice21"):
                opp_val = getattr(old_value, "SBCS_WaterLevelMeasurementDevice21", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_WaterLevelMeasurementDevice21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_WaterLevelMeasurementDevice21"):
                opp_val = getattr(value, "SBCS_WaterLevelMeasurementDevice21", None)
                setattr(value, "SBCS_WaterLevelMeasurementDevice21", self)

class SBCS_ControlProgram_Start(Transition):

    pass
class SBCS_Pump:

    def __init__(self, mode: str, SBCS_Pump: "SBCS_PumpControler" = None):
        self.mode = mode
        self.SBCS_Pump = SBCS_Pump
        
        pass
    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode


    @property
    def SBCS_Pump(self):
        return self.__SBCS_Pump

    @SBCS_Pump.setter
    def SBCS_Pump(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Pump__SBCS_Pump", None)
        self.__SBCS_Pump = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_PumpControler"):
                opp_val = getattr(old_value, "SBCS_PumpControler", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_PumpControler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_PumpControler"):
                opp_val = getattr(value, "SBCS_PumpControler", None)
                setattr(value, "SBCS_PumpControler", self)

class SBCS_PumpControler:

    pass
class SBCS_WaterLevelMeasurementDevice:

    def __init__(self, waterLevel: float, SBCS_WaterLevelMeasurementDevice: "SBCS_SteamBoiler" = None, SBCS_WaterLevelMeasurementDevice21: "SBCS_WaterLevelMeaurementDevice_getLevel" = None, SBCS_WaterLevelMeasurementDevice23: "SBCS_SteamBoiler" = None):
        self.waterLevel = waterLevel
        self.SBCS_WaterLevelMeasurementDevice = SBCS_WaterLevelMeasurementDevice
        self.SBCS_WaterLevelMeasurementDevice21 = SBCS_WaterLevelMeasurementDevice21
        self.SBCS_WaterLevelMeasurementDevice23 = SBCS_WaterLevelMeasurementDevice23
        
        pass
    @property
    def waterLevel(self):
        return self.__waterLevel

    @waterLevel.setter
    def waterLevel(self, waterLevel: float):
        self.__waterLevel = waterLevel


    @property
    def SBCS_WaterLevelMeasurementDevice23(self):
        return self.__SBCS_WaterLevelMeasurementDevice23

    @SBCS_WaterLevelMeasurementDevice23.setter
    def SBCS_WaterLevelMeasurementDevice23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_WaterLevelMeasurementDevice__SBCS_WaterLevelMeasurementDevice23", None)
        self.__SBCS_WaterLevelMeasurementDevice23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_SteamBoiler24"):
                opp_val = getattr(old_value, "SBCS_SteamBoiler24", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_SteamBoiler24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_SteamBoiler24"):
                opp_val = getattr(value, "SBCS_SteamBoiler24", None)
                setattr(value, "SBCS_SteamBoiler24", self)

    @property
    def SBCS_WaterLevelMeasurementDevice(self):
        return self.__SBCS_WaterLevelMeasurementDevice

    @SBCS_WaterLevelMeasurementDevice.setter
    def SBCS_WaterLevelMeasurementDevice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_WaterLevelMeasurementDevice__SBCS_WaterLevelMeasurementDevice", None)
        self.__SBCS_WaterLevelMeasurementDevice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_SteamBoiler6"):
                opp_val = getattr(old_value, "SBCS_SteamBoiler6", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_SteamBoiler6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_SteamBoiler6"):
                opp_val = getattr(value, "SBCS_SteamBoiler6", None)
                setattr(value, "SBCS_SteamBoiler6", self)

    @property
    def SBCS_WaterLevelMeasurementDevice21(self):
        return self.__SBCS_WaterLevelMeasurementDevice21

    @SBCS_WaterLevelMeasurementDevice21.setter
    def SBCS_WaterLevelMeasurementDevice21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_WaterLevelMeasurementDevice__SBCS_WaterLevelMeasurementDevice21", None)
        self.__SBCS_WaterLevelMeasurementDevice21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_WaterLevelMeaurementDevice_getLevel"):
                opp_val = getattr(old_value, "SBCS_WaterLevelMeaurementDevice_getLevel", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_WaterLevelMeaurementDevice_getLevel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_WaterLevelMeaurementDevice_getLevel"):
                opp_val = getattr(value, "SBCS_WaterLevelMeaurementDevice_getLevel", None)
                setattr(value, "SBCS_WaterLevelMeaurementDevice_getLevel", self)

class SBCS_Snapshot:

    def __init__(self, SBCS_Snapshot: "SBCS_SteamBoiler" = None, SBCS_Snapshot19: "SBCS_Transition" = None, SBCS_Snapshot26: "SBCS_ControlProgram" = None, SBCS_Snapshot29: "SBCS_Transition" = None):
        self.SBCS_Snapshot = SBCS_Snapshot
        self.SBCS_Snapshot19 = SBCS_Snapshot19
        self.SBCS_Snapshot26 = SBCS_Snapshot26
        self.SBCS_Snapshot29 = SBCS_Snapshot29
        
        pass
    @property
    def SBCS_Snapshot19(self):
        return self.__SBCS_Snapshot19

    @SBCS_Snapshot19.setter
    def SBCS_Snapshot19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__SBCS_Snapshot19", None)
        self.__SBCS_Snapshot19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_Transition"):
                opp_val = getattr(old_value, "SBCS_Transition", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_Transition"):
                opp_val = getattr(value, "SBCS_Transition", None)
                setattr(value, "SBCS_Transition", self)

    @property
    def SBCS_Snapshot26(self):
        return self.__SBCS_Snapshot26

    @SBCS_Snapshot26.setter
    def SBCS_Snapshot26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__SBCS_Snapshot26", None)
        self.__SBCS_Snapshot26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_ControlProgram27"):
                opp_val = getattr(old_value, "SBCS_ControlProgram27", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_ControlProgram27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_ControlProgram27"):
                opp_val = getattr(value, "SBCS_ControlProgram27", None)
                setattr(value, "SBCS_ControlProgram27", self)

    @property
    def SBCS_Snapshot29(self):
        return self.__SBCS_Snapshot29

    @SBCS_Snapshot29.setter
    def SBCS_Snapshot29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__SBCS_Snapshot29", None)
        self.__SBCS_Snapshot29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_Transition30"):
                opp_val = getattr(old_value, "SBCS_Transition30", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_Transition30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_Transition30"):
                opp_val = getattr(value, "SBCS_Transition30", None)
                setattr(value, "SBCS_Transition30", self)

    @property
    def SBCS_Snapshot(self):
        return self.__SBCS_Snapshot

    @SBCS_Snapshot.setter
    def SBCS_Snapshot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__SBCS_Snapshot", None)
        self.__SBCS_Snapshot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_SteamBoiler"):
                opp_val = getattr(old_value, "SBCS_SteamBoiler", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_SteamBoiler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_SteamBoiler"):
                opp_val = getattr(value, "SBCS_SteamBoiler", None)
                setattr(value, "SBCS_SteamBoiler", self)

    def getNext(self) :
        # TODO: Implement getNext method
        pass
