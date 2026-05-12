from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ValveState(Enum):
    Open = "Open"
    Closed = "Closed"
class State(Enum):
    On = "On"
    Off = "Off"
class Mode(Enum):
    Initialization = "Initialization"
    Rescue = "Rescue"
    EmergencyStop = "EmergencyStop"
    Normal = "Normal"
    Dameged = "Dameged"
    Degraded = "Degraded"


############################################
# Definition of Classes
############################################

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
            if hasattr(old_value, "SBCS_PumpControler29"):
                opp_val = getattr(old_value, "SBCS_PumpControler29", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_PumpControler29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_PumpControler29"):
                opp_val = getattr(value, "SBCS_PumpControler29", None)
                setattr(value, "SBCS_PumpControler29", self)

class SBCS_SteamBoiler:

    def __init__(self, valveOpen: str, SBCS_SteamBoiler: "SBCS_ControlProgram" = None, SBCS_SteamBoiler16: "SBCS_SteamBoiler_OpenValve" = None, SBCS_SteamBoiler19: "SBCS_SteamBoiler_OpenValve" = None):
        self.valveOpen = valveOpen
        self.SBCS_SteamBoiler = SBCS_SteamBoiler
        self.SBCS_SteamBoiler16 = SBCS_SteamBoiler16
        self.SBCS_SteamBoiler19 = SBCS_SteamBoiler19
        
        pass
    @property
    def valveOpen(self):
        return self.__valveOpen

    @valveOpen.setter
    def valveOpen(self, valveOpen: str):
        self.__valveOpen = valveOpen


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
            if hasattr(old_value, "SBCS_ControlProgram8"):
                opp_val = getattr(old_value, "SBCS_ControlProgram8", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_ControlProgram8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_ControlProgram8"):
                opp_val = getattr(value, "SBCS_ControlProgram8", None)
                setattr(value, "SBCS_ControlProgram8", self)

    @property
    def SBCS_SteamBoiler19(self):
        return self.__SBCS_SteamBoiler19

    @SBCS_SteamBoiler19.setter
    def SBCS_SteamBoiler19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamBoiler__SBCS_SteamBoiler19", None)
        self.__SBCS_SteamBoiler19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_SteamBoiler_OpenValve18"):
                opp_val = getattr(old_value, "SBCS_SteamBoiler_OpenValve18", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_SteamBoiler_OpenValve18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_SteamBoiler_OpenValve18"):
                opp_val = getattr(value, "SBCS_SteamBoiler_OpenValve18", None)
                setattr(value, "SBCS_SteamBoiler_OpenValve18", self)

    @property
    def SBCS_SteamBoiler16(self):
        return self.__SBCS_SteamBoiler16

    @SBCS_SteamBoiler16.setter
    def SBCS_SteamBoiler16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamBoiler__SBCS_SteamBoiler16", None)
        self.__SBCS_SteamBoiler16 = value
        
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

class SBCS_ControlProgram:

    def __init__(self, mode: str, wlmdFailure: bool, SBCS_ControlProgram: "SBCS_ControlProgram_Start" = None, SBCS_ControlProgram8: "SBCS_SteamBoiler" = None, SBCS_ControlProgram11: "SBCS_Snapshot" = None, SBCS_ControlProgram26: "SBCS_Snapshot" = None):
        self.mode = mode
        self.wlmdFailure = wlmdFailure
        self.SBCS_ControlProgram = SBCS_ControlProgram
        self.SBCS_ControlProgram8 = SBCS_ControlProgram8
        self.SBCS_ControlProgram11 = SBCS_ControlProgram11
        self.SBCS_ControlProgram26 = SBCS_ControlProgram26
        
        pass
    @property
    def wlmdFailure(self):
        return self.__wlmdFailure

    @wlmdFailure.setter
    def wlmdFailure(self, wlmdFailure: bool):
        self.__wlmdFailure = wlmdFailure


    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode


    @property
    def SBCS_ControlProgram11(self):
        return self.__SBCS_ControlProgram11

    @SBCS_ControlProgram11.setter
    def SBCS_ControlProgram11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_ControlProgram__SBCS_ControlProgram11", None)
        self.__SBCS_ControlProgram11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_Snapshot10"):
                opp_val = getattr(old_value, "SBCS_Snapshot10", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_Snapshot10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_Snapshot10"):
                opp_val = getattr(value, "SBCS_Snapshot10", None)
                setattr(value, "SBCS_Snapshot10", self)

    @property
    def SBCS_ControlProgram8(self):
        return self.__SBCS_ControlProgram8

    @SBCS_ControlProgram8.setter
    def SBCS_ControlProgram8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_ControlProgram__SBCS_ControlProgram8", None)
        self.__SBCS_ControlProgram8 = value
        
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

    @property
    def SBCS_ControlProgram26(self):
        return self.__SBCS_ControlProgram26

    @SBCS_ControlProgram26.setter
    def SBCS_ControlProgram26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_ControlProgram__SBCS_ControlProgram26", None)
        self.__SBCS_ControlProgram26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_Snapshot27"):
                opp_val = getattr(old_value, "SBCS_Snapshot27", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_Snapshot27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_Snapshot27"):
                opp_val = getattr(value, "SBCS_Snapshot27", None)
                setattr(value, "SBCS_Snapshot27", self)

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

class SBCS_WaterLevelMeasurementDevice:

    def __init__(self, waterLevel: float, SBCS_WaterLevelMeasurementDevice: "SBCS_WaterLevelMeaurementDevice_getLevel" = None):
        self.waterLevel = waterLevel
        self.SBCS_WaterLevelMeasurementDevice = SBCS_WaterLevelMeasurementDevice
        
        pass
    @property
    def waterLevel(self):
        return self.__waterLevel

    @waterLevel.setter
    def waterLevel(self, waterLevel: float):
        self.__waterLevel = waterLevel


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

class SBCS_PumpControler:

    pass
class Transition:

    pass
class SBCS_ControlProgram_Start(Transition):

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
class SBCS_PumpController_OpenPump(Transition):

    pass
class SBCS_PumpController_ClosePump(Transition):

    pass
class SBCS_Snapshot:

    def __init__(self, SBCS_Snapshot: "SBCS_Transition" = None, SBCS_Snapshot10: "SBCS_ControlProgram" = None, SBCS_Snapshot13: "SBCS_Transition" = None, SBCS_Snapshot27: "SBCS_ControlProgram" = None):
        self.SBCS_Snapshot = SBCS_Snapshot
        self.SBCS_Snapshot10 = SBCS_Snapshot10
        self.SBCS_Snapshot13 = SBCS_Snapshot13
        self.SBCS_Snapshot27 = SBCS_Snapshot27
        
        pass
    @property
    def SBCS_Snapshot10(self):
        return self.__SBCS_Snapshot10

    @SBCS_Snapshot10.setter
    def SBCS_Snapshot10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__SBCS_Snapshot10", None)
        self.__SBCS_Snapshot10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_ControlProgram11"):
                opp_val = getattr(old_value, "SBCS_ControlProgram11", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_ControlProgram11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_ControlProgram11"):
                opp_val = getattr(value, "SBCS_ControlProgram11", None)
                setattr(value, "SBCS_ControlProgram11", self)

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
    def SBCS_Snapshot13(self):
        return self.__SBCS_Snapshot13

    @SBCS_Snapshot13.setter
    def SBCS_Snapshot13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__SBCS_Snapshot13", None)
        self.__SBCS_Snapshot13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_Transition14"):
                opp_val = getattr(old_value, "SBCS_Transition14", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_Transition14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_Transition14"):
                opp_val = getattr(value, "SBCS_Transition14", None)
                setattr(value, "SBCS_Transition14", self)

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
            if hasattr(old_value, "SBCS_ControlProgram26"):
                opp_val = getattr(old_value, "SBCS_ControlProgram26", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_ControlProgram26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_ControlProgram26"):
                opp_val = getattr(value, "SBCS_ControlProgram26", None)
                setattr(value, "SBCS_ControlProgram26", self)

    def getNext(self) :
        # TODO: Implement getNext method
        pass

class SBCS_Transition:

    pass