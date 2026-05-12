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
class State(Enum):
    On = "On"
    Off = "Off"
class ValveState(Enum):
    Open = "Open"
    Closed = "Closed"


############################################
# Definition of Classes
############################################

class SBCS_WaterLevelMeasurementDevice:

    def __init__(self, waterLevel: float, SBCS_WaterLevelMeasurementDevice: "SBCS_WaterLevelMeaurementDevice_getLevel" = None, SBCS_WaterLevelMeasurementDevice17: "SBCS_Snapshot" = None, SBCS_WaterLevelMeasurementDevice21: "SBCS_SteamBoiler" = None):
        self.waterLevel = waterLevel
        self.SBCS_WaterLevelMeasurementDevice = SBCS_WaterLevelMeasurementDevice
        self.SBCS_WaterLevelMeasurementDevice17 = SBCS_WaterLevelMeasurementDevice17
        self.SBCS_WaterLevelMeasurementDevice21 = SBCS_WaterLevelMeasurementDevice21
        
        pass
    @property
    def waterLevel(self):
        return self.__waterLevel

    @waterLevel.setter
    def waterLevel(self, waterLevel: float):
        self.__waterLevel = waterLevel


    @property
    def SBCS_WaterLevelMeasurementDevice17(self):
        return self.__SBCS_WaterLevelMeasurementDevice17

    @SBCS_WaterLevelMeasurementDevice17.setter
    def SBCS_WaterLevelMeasurementDevice17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_WaterLevelMeasurementDevice__SBCS_WaterLevelMeasurementDevice17", None)
        self.__SBCS_WaterLevelMeasurementDevice17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_Snapshot16"):
                opp_val = getattr(old_value, "SBCS_Snapshot16", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_Snapshot16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_Snapshot16"):
                opp_val = getattr(value, "SBCS_Snapshot16", None)
                setattr(value, "SBCS_Snapshot16", self)

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
            if hasattr(old_value, "SBCS_WaterLevelMeaurementDevice_getLevel"):
                opp_val = getattr(old_value, "SBCS_WaterLevelMeaurementDevice_getLevel", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_WaterLevelMeaurementDevice_getLevel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_WaterLevelMeaurementDevice_getLevel"):
                opp_val = getattr(value, "SBCS_WaterLevelMeaurementDevice_getLevel", None)
                setattr(value, "SBCS_WaterLevelMeaurementDevice_getLevel", self)

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
            if hasattr(old_value, "SBCS_SteamBoiler22"):
                opp_val = getattr(old_value, "SBCS_SteamBoiler22", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_SteamBoiler22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_SteamBoiler22"):
                opp_val = getattr(value, "SBCS_SteamBoiler22", None)
                setattr(value, "SBCS_SteamBoiler22", self)

class SBCS_Transition:

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
            if hasattr(old_value, "SBCS_PumpControler13"):
                opp_val = getattr(old_value, "SBCS_PumpControler13", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_PumpControler13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_PumpControler13"):
                opp_val = getattr(value, "SBCS_PumpControler13", None)
                setattr(value, "SBCS_PumpControler13", self)

class SBCS_ControlProgram:

    def __init__(self, mode: str, SBCS_ControlProgram: "SBCS_SteamBoiler" = None, SBCS_ControlProgram24: "SBCS_ControlProgram_Start" = None):
        self.mode = mode
        self.SBCS_ControlProgram = SBCS_ControlProgram
        self.SBCS_ControlProgram24 = SBCS_ControlProgram24
        
        pass
    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode


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
            if hasattr(old_value, "SBCS_SteamBoiler11"):
                opp_val = getattr(old_value, "SBCS_SteamBoiler11", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_SteamBoiler11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_SteamBoiler11"):
                opp_val = getattr(value, "SBCS_SteamBoiler11", None)
                setattr(value, "SBCS_SteamBoiler11", self)

    @property
    def SBCS_ControlProgram24(self):
        return self.__SBCS_ControlProgram24

    @SBCS_ControlProgram24.setter
    def SBCS_ControlProgram24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_ControlProgram__SBCS_ControlProgram24", None)
        self.__SBCS_ControlProgram24 = value
        
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

class SBCS_Snapshot:

    def __init__(self, SBCS_Snapshot: "SBCS_SteamBoiler" = None, SBCS_Snapshot16: "SBCS_WaterLevelMeasurementDevice" = None, SBCS_Snapshot19: "SBCS_Transition" = None, SBCS_Snapshot27: "SBCS_Transition" = None):
        self.SBCS_Snapshot = SBCS_Snapshot
        self.SBCS_Snapshot16 = SBCS_Snapshot16
        self.SBCS_Snapshot19 = SBCS_Snapshot19
        self.SBCS_Snapshot27 = SBCS_Snapshot27
        
        pass
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
            if hasattr(old_value, "SBCS_SteamBoiler9"):
                opp_val = getattr(old_value, "SBCS_SteamBoiler9", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_SteamBoiler9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_SteamBoiler9"):
                opp_val = getattr(value, "SBCS_SteamBoiler9", None)
                setattr(value, "SBCS_SteamBoiler9", self)

    @property
    def SBCS_Snapshot27(self):
        return self.__SBCS_Snapshot27

    @SBCS_Snapshot27.setter
    def SBCS_Snapshot27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__SBCS_Snapshot27", None)
        self.__SBCS_Snapshot27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_Transition26"):
                opp_val = getattr(old_value, "SBCS_Transition26", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_Transition26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_Transition26"):
                opp_val = getattr(value, "SBCS_Transition26", None)
                setattr(value, "SBCS_Transition26", self)

    @property
    def SBCS_Snapshot16(self):
        return self.__SBCS_Snapshot16

    @SBCS_Snapshot16.setter
    def SBCS_Snapshot16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__SBCS_Snapshot16", None)
        self.__SBCS_Snapshot16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_WaterLevelMeasurementDevice17"):
                opp_val = getattr(old_value, "SBCS_WaterLevelMeasurementDevice17", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_WaterLevelMeasurementDevice17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_WaterLevelMeasurementDevice17"):
                opp_val = getattr(value, "SBCS_WaterLevelMeasurementDevice17", None)
                setattr(value, "SBCS_WaterLevelMeasurementDevice17", self)

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

    def getPost(self) :
        # TODO: Implement getPost method
        pass

    def getNext(self) :
        # TODO: Implement getNext method
        pass

    def futureClosure(self, SBCS_s) :
        # TODO: Implement futureClosure method
        pass

class SBCS_PumpControler:

    pass
class SBCS_SteamBoiler:

    def __init__(self, capacity: float, maximalNormal: float, valveOpen: str, SBCS_SteamBoiler9: "SBCS_Snapshot" = None, SBCS_SteamBoiler11: "SBCS_ControlProgram" = None, SBCS_SteamBoiler: "SBCS_SteamBoiler_OpenValve" = None, SBCS_SteamBoiler3: "SBCS_SteamBoiler_OpenValve" = None, SBCS_SteamBoiler22: "SBCS_WaterLevelMeasurementDevice" = None):
        self.capacity = capacity
        self.maximalNormal = maximalNormal
        self.valveOpen = valveOpen
        self.SBCS_SteamBoiler9 = SBCS_SteamBoiler9
        self.SBCS_SteamBoiler11 = SBCS_SteamBoiler11
        self.SBCS_SteamBoiler = SBCS_SteamBoiler
        self.SBCS_SteamBoiler3 = SBCS_SteamBoiler3
        self.SBCS_SteamBoiler22 = SBCS_SteamBoiler22
        
        pass
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
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: float):
        self.__capacity = capacity


    @property
    def SBCS_SteamBoiler11(self):
        return self.__SBCS_SteamBoiler11

    @SBCS_SteamBoiler11.setter
    def SBCS_SteamBoiler11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamBoiler__SBCS_SteamBoiler11", None)
        self.__SBCS_SteamBoiler11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_ControlProgram"):
                opp_val = getattr(old_value, "SBCS_ControlProgram", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_ControlProgram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_ControlProgram"):
                opp_val = getattr(value, "SBCS_ControlProgram", None)
                setattr(value, "SBCS_ControlProgram", self)

    @property
    def SBCS_SteamBoiler22(self):
        return self.__SBCS_SteamBoiler22

    @SBCS_SteamBoiler22.setter
    def SBCS_SteamBoiler22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamBoiler__SBCS_SteamBoiler22", None)
        self.__SBCS_SteamBoiler22 = value
        
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
            if hasattr(old_value, "SBCS_SteamBoiler_OpenValve2"):
                opp_val = getattr(old_value, "SBCS_SteamBoiler_OpenValve2", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_SteamBoiler_OpenValve2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_SteamBoiler_OpenValve2"):
                opp_val = getattr(value, "SBCS_SteamBoiler_OpenValve2", None)
                setattr(value, "SBCS_SteamBoiler_OpenValve2", self)

    @property
    def SBCS_SteamBoiler9(self):
        return self.__SBCS_SteamBoiler9

    @SBCS_SteamBoiler9.setter
    def SBCS_SteamBoiler9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamBoiler__SBCS_SteamBoiler9", None)
        self.__SBCS_SteamBoiler9 = value
        
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
    def SBCS_SteamBoiler(self):
        return self.__SBCS_SteamBoiler

    @SBCS_SteamBoiler.setter
    def SBCS_SteamBoiler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamBoiler__SBCS_SteamBoiler", None)
        self.__SBCS_SteamBoiler = value
        
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

class Transition:

    pass
class SBCS_PumpController_OpenPump(Transition):

    pass
class SBCS_ControlProgram_Start(Transition):

    pass
class SBCS_PumpController_ClosePump(Transition):

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
            if hasattr(old_value, "SBCS_WaterLevelMeasurementDevice"):
                opp_val = getattr(old_value, "SBCS_WaterLevelMeasurementDevice", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_WaterLevelMeasurementDevice", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_WaterLevelMeasurementDevice"):
                opp_val = getattr(value, "SBCS_WaterLevelMeasurementDevice", None)
                setattr(value, "SBCS_WaterLevelMeasurementDevice", self)

class SBCS_SteamBoiler_OpenValve(Transition):

    pass