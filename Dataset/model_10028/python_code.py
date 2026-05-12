from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ValveState(Enum):
    Open = "Open"
    Closed = "Closed"
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


############################################
# Definition of Classes
############################################

class SBCS_SteamBoiler:

    def __init__(self, valveOpen: str, SBCS_SteamBoiler19: "SBCS_SteamBoiler_OpenValve" = None, SBCS_SteamBoiler22: "SBCS_SteamBoiler_OpenValve" = None, SBCS_SteamBoiler: "SBCS_ControlProgram" = None):
        self.valveOpen = valveOpen
        self.SBCS_SteamBoiler19 = SBCS_SteamBoiler19
        self.SBCS_SteamBoiler22 = SBCS_SteamBoiler22
        self.SBCS_SteamBoiler = SBCS_SteamBoiler
        
        pass
    @property
    def valveOpen(self):
        return self.__valveOpen

    @valveOpen.setter
    def valveOpen(self, valveOpen: str):
        self.__valveOpen = valveOpen


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
    def SBCS_SteamBoiler(self):
        return self.__SBCS_SteamBoiler

    @SBCS_SteamBoiler.setter
    def SBCS_SteamBoiler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamBoiler__SBCS_SteamBoiler", None)
        self.__SBCS_SteamBoiler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_ControlProgram15"):
                opp_val = getattr(old_value, "SBCS_ControlProgram15", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_ControlProgram15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_ControlProgram15"):
                opp_val = getattr(value, "SBCS_ControlProgram15", None)
                setattr(value, "SBCS_ControlProgram15", self)

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
            if hasattr(old_value, "SBCS_SteamBoiler_OpenValve21"):
                opp_val = getattr(old_value, "SBCS_SteamBoiler_OpenValve21", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_SteamBoiler_OpenValve21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_SteamBoiler_OpenValve21"):
                opp_val = getattr(value, "SBCS_SteamBoiler_OpenValve21", None)
                setattr(value, "SBCS_SteamBoiler_OpenValve21", self)

class SBCS_Transition:

    pass
class SBCS_ControlProgram:

    def __init__(self, mode: str, smdFailure: bool, pumpFailure: bool, pumpControlerFailure: bool, SBCS_ControlProgram: "SBCS_Snapshot" = None, SBCS_ControlProgram15: "SBCS_SteamBoiler" = None, SBCS_ControlProgram17: "SBCS_ControlProgram_Start" = None, SBCS_ControlProgram24: "SBCS_Snapshot" = None):
        self.mode = mode
        self.smdFailure = smdFailure
        self.pumpFailure = pumpFailure
        self.pumpControlerFailure = pumpControlerFailure
        self.SBCS_ControlProgram = SBCS_ControlProgram
        self.SBCS_ControlProgram15 = SBCS_ControlProgram15
        self.SBCS_ControlProgram17 = SBCS_ControlProgram17
        self.SBCS_ControlProgram24 = SBCS_ControlProgram24
        
        pass
    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode


    @property
    def pumpFailure(self):
        return self.__pumpFailure

    @pumpFailure.setter
    def pumpFailure(self, pumpFailure: bool):
        self.__pumpFailure = pumpFailure


    @property
    def pumpControlerFailure(self):
        return self.__pumpControlerFailure

    @pumpControlerFailure.setter
    def pumpControlerFailure(self, pumpControlerFailure: bool):
        self.__pumpControlerFailure = pumpControlerFailure


    @property
    def smdFailure(self):
        return self.__smdFailure

    @smdFailure.setter
    def smdFailure(self, smdFailure: bool):
        self.__smdFailure = smdFailure


    @property
    def SBCS_ControlProgram15(self):
        return self.__SBCS_ControlProgram15

    @SBCS_ControlProgram15.setter
    def SBCS_ControlProgram15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_ControlProgram__SBCS_ControlProgram15", None)
        self.__SBCS_ControlProgram15 = value
        
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
    def SBCS_ControlProgram24(self):
        return self.__SBCS_ControlProgram24

    @SBCS_ControlProgram24.setter
    def SBCS_ControlProgram24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_ControlProgram__SBCS_ControlProgram24", None)
        self.__SBCS_ControlProgram24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_Snapshot25"):
                opp_val = getattr(old_value, "SBCS_Snapshot25", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_Snapshot25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_Snapshot25"):
                opp_val = getattr(value, "SBCS_Snapshot25", None)
                setattr(value, "SBCS_Snapshot25", self)

    @property
    def SBCS_ControlProgram17(self):
        return self.__SBCS_ControlProgram17

    @SBCS_ControlProgram17.setter
    def SBCS_ControlProgram17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_ControlProgram__SBCS_ControlProgram17", None)
        self.__SBCS_ControlProgram17 = value
        
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
            if hasattr(old_value, "SBCS_Snapshot"):
                opp_val = getattr(old_value, "SBCS_Snapshot", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_Snapshot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_Snapshot"):
                opp_val = getattr(value, "SBCS_Snapshot", None)
                setattr(value, "SBCS_Snapshot", self)

class SBCS_Snapshot:

    def __init__(self, SBCS_Snapshot: "SBCS_ControlProgram" = None, SBCS_Snapshot6: "SBCS_Transition" = None, SBCS_Snapshot25: "SBCS_ControlProgram" = None, SBCS_Snapshot29: "SBCS_Transition" = None):
        self.SBCS_Snapshot = SBCS_Snapshot
        self.SBCS_Snapshot6 = SBCS_Snapshot6
        self.SBCS_Snapshot25 = SBCS_Snapshot25
        self.SBCS_Snapshot29 = SBCS_Snapshot29
        
        pass
    @property
    def SBCS_Snapshot6(self):
        return self.__SBCS_Snapshot6

    @SBCS_Snapshot6.setter
    def SBCS_Snapshot6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__SBCS_Snapshot6", None)
        self.__SBCS_Snapshot6 = value
        
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
    def SBCS_Snapshot25(self):
        return self.__SBCS_Snapshot25

    @SBCS_Snapshot25.setter
    def SBCS_Snapshot25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__SBCS_Snapshot25", None)
        self.__SBCS_Snapshot25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_ControlProgram24"):
                opp_val = getattr(old_value, "SBCS_ControlProgram24", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_ControlProgram24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_ControlProgram24"):
                opp_val = getattr(value, "SBCS_ControlProgram24", None)
                setattr(value, "SBCS_ControlProgram24", self)

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
    def SBCS_Snapshot29(self):
        return self.__SBCS_Snapshot29

    @SBCS_Snapshot29.setter
    def SBCS_Snapshot29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__SBCS_Snapshot29", None)
        self.__SBCS_Snapshot29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_Transition28"):
                opp_val = getattr(old_value, "SBCS_Transition28", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_Transition28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_Transition28"):
                opp_val = getattr(value, "SBCS_Transition28", None)
                setattr(value, "SBCS_Transition28", self)

    def getNext(self) :
        # TODO: Implement getNext method
        pass

class SBCS_PumpControler:

    pass
class Transition:

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
class SBCS_ControlProgram_Start(Transition):

    pass
class SBCS_PumpController_ClosePump(Transition):

    pass
class SBCS_PumpController_OpenPump(Transition):

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
