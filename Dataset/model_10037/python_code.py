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

class Transition:

    pass
class SBCS_WaterLevelMeaurementDevice_getLevel(Transition):

    def __init__(self, ret: float, SBCS_WaterLevelMeaurementDevice_getLevel: "SBCS_WaterLevelMeasurementDevice" = None, SBCS_WaterLevelMeaurementDevice_getLevel69: "SBCS_WaterLevelMeasurementDevice" = None):
        self.ret = ret
        self.SBCS_WaterLevelMeaurementDevice_getLevel = SBCS_WaterLevelMeaurementDevice_getLevel
        self.SBCS_WaterLevelMeaurementDevice_getLevel69 = SBCS_WaterLevelMeaurementDevice_getLevel69
        
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

    @property
    def SBCS_WaterLevelMeaurementDevice_getLevel69(self):
        return self.__SBCS_WaterLevelMeaurementDevice_getLevel69

    @SBCS_WaterLevelMeaurementDevice_getLevel69.setter
    def SBCS_WaterLevelMeaurementDevice_getLevel69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_WaterLevelMeaurementDevice_getLevel__SBCS_WaterLevelMeaurementDevice_getLevel69", None)
        self.__SBCS_WaterLevelMeaurementDevice_getLevel69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_WaterLevelMeasurementDevice70"):
                opp_val = getattr(old_value, "SBCS_WaterLevelMeasurementDevice70", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_WaterLevelMeasurementDevice70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_WaterLevelMeasurementDevice70"):
                opp_val = getattr(value, "SBCS_WaterLevelMeasurementDevice70", None)
                setattr(value, "SBCS_WaterLevelMeasurementDevice70", self)

class SBCS_SteamBoiler_OpenValve(Transition):

    pass
class SBCS_PumpController_ClosePump(Transition):

    pass
class SBCS_PumpController_OpenPump(Transition):

    pass
class SBCS_ControlProgram_Start(Transition):

    pass
class SBCS_WaterLevelMeasurementDevice:

    def __init__(self, ready: bool, waterLevel: float, WaterLevelMeasurementDevice23: "SBCS_ControlProgram" = None, WaterLevelMeasurementDevice: "SBCS_SteamBoiler" = None, WaterLevelMeasurementDevice11: "SBCS_Snapshot" = None, SBCS_WaterLevelMeasurementDevice: "SBCS_WaterLevelMeaurementDevice_getLevel" = None, SBCS_WaterLevelMeasurementDevice70: "SBCS_WaterLevelMeaurementDevice_getLevel" = None, WLMDSnapshot: "SBCS_Snapshot" = None, ControlProgramWLMD: "SBCS_ControlProgram" = None, SteamBoilerWLMD: "SBCS_SteamBoiler" = None):
        self.ready = ready
        self.waterLevel = waterLevel
        self.WaterLevelMeasurementDevice23 = WaterLevelMeasurementDevice23
        self.WaterLevelMeasurementDevice = WaterLevelMeasurementDevice
        self.WaterLevelMeasurementDevice11 = WaterLevelMeasurementDevice11
        self.SBCS_WaterLevelMeasurementDevice = SBCS_WaterLevelMeasurementDevice
        self.SBCS_WaterLevelMeasurementDevice70 = SBCS_WaterLevelMeasurementDevice70
        self.WLMDSnapshot = WLMDSnapshot
        self.ControlProgramWLMD = ControlProgramWLMD
        self.SteamBoilerWLMD = SteamBoilerWLMD
        
        pass
    @property
    def ready(self):
        return self.__ready

    @ready.setter
    def ready(self, ready: bool):
        self.__ready = ready


    @property
    def waterLevel(self):
        return self.__waterLevel

    @waterLevel.setter
    def waterLevel(self, waterLevel: float):
        self.__waterLevel = waterLevel


    @property
    def SteamBoilerWLMD(self):
        return self.__SteamBoilerWLMD

    @SteamBoilerWLMD.setter
    def SteamBoilerWLMD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_WaterLevelMeasurementDevice__SteamBoilerWLMD", None)
        self.__SteamBoilerWLMD = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SteamBoiler62"):
                opp_val = getattr(old_value, "SteamBoiler62", None)
                if opp_val == self:
                    setattr(old_value, "SteamBoiler62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SteamBoiler62"):
                opp_val = getattr(value, "SteamBoiler62", None)
                setattr(value, "SteamBoiler62", self)

    @property
    def WaterLevelMeasurementDevice23(self):
        return self.__WaterLevelMeasurementDevice23

    @WaterLevelMeasurementDevice23.setter
    def WaterLevelMeasurementDevice23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_WaterLevelMeasurementDevice__WaterLevelMeasurementDevice23", None)
        self.__WaterLevelMeasurementDevice23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WLMDControlProgram"):
                opp_val = getattr(old_value, "WLMDControlProgram", None)
                if opp_val == self:
                    setattr(old_value, "WLMDControlProgram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WLMDControlProgram"):
                opp_val = getattr(value, "WLMDControlProgram", None)
                setattr(value, "WLMDControlProgram", self)

    @property
    def WaterLevelMeasurementDevice11(self):
        return self.__WaterLevelMeasurementDevice11

    @WaterLevelMeasurementDevice11.setter
    def WaterLevelMeasurementDevice11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_WaterLevelMeasurementDevice__WaterLevelMeasurementDevice11", None)
        self.__WaterLevelMeasurementDevice11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SnapshotWLMD"):
                opp_val = getattr(old_value, "SnapshotWLMD", None)
                if opp_val == self:
                    setattr(old_value, "SnapshotWLMD", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SnapshotWLMD"):
                opp_val = getattr(value, "SnapshotWLMD", None)
                setattr(value, "SnapshotWLMD", self)

    @property
    def WaterLevelMeasurementDevice(self):
        return self.__WaterLevelMeasurementDevice

    @WaterLevelMeasurementDevice.setter
    def WaterLevelMeasurementDevice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_WaterLevelMeasurementDevice__WaterLevelMeasurementDevice", None)
        self.__WaterLevelMeasurementDevice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WLMDSteamBoiler"):
                opp_val = getattr(old_value, "WLMDSteamBoiler", None)
                if opp_val == self:
                    setattr(old_value, "WLMDSteamBoiler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WLMDSteamBoiler"):
                opp_val = getattr(value, "WLMDSteamBoiler", None)
                setattr(value, "WLMDSteamBoiler", self)

    @property
    def SBCS_WaterLevelMeasurementDevice70(self):
        return self.__SBCS_WaterLevelMeasurementDevice70

    @SBCS_WaterLevelMeasurementDevice70.setter
    def SBCS_WaterLevelMeasurementDevice70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_WaterLevelMeasurementDevice__SBCS_WaterLevelMeasurementDevice70", None)
        self.__SBCS_WaterLevelMeasurementDevice70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_WaterLevelMeaurementDevice_getLevel69"):
                opp_val = getattr(old_value, "SBCS_WaterLevelMeaurementDevice_getLevel69", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_WaterLevelMeaurementDevice_getLevel69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_WaterLevelMeaurementDevice_getLevel69"):
                opp_val = getattr(value, "SBCS_WaterLevelMeaurementDevice_getLevel69", None)
                setattr(value, "SBCS_WaterLevelMeaurementDevice_getLevel69", self)

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
    def ControlProgramWLMD(self):
        return self.__ControlProgramWLMD

    @ControlProgramWLMD.setter
    def ControlProgramWLMD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_WaterLevelMeasurementDevice__ControlProgramWLMD", None)
        self.__ControlProgramWLMD = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ControlProgram60"):
                opp_val = getattr(old_value, "ControlProgram60", None)
                if opp_val == self:
                    setattr(old_value, "ControlProgram60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ControlProgram60"):
                opp_val = getattr(value, "ControlProgram60", None)
                setattr(value, "ControlProgram60", self)

    @property
    def WLMDSnapshot(self):
        return self.__WLMDSnapshot

    @WLMDSnapshot.setter
    def WLMDSnapshot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_WaterLevelMeasurementDevice__WLMDSnapshot", None)
        self.__WLMDSnapshot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Snapshot58"):
                opp_val = getattr(old_value, "Snapshot58", None)
                if opp_val == self:
                    setattr(old_value, "Snapshot58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Snapshot58"):
                opp_val = getattr(value, "Snapshot58", None)
                setattr(value, "Snapshot58", self)

class SBCS_SteamMeasurementDevice:

    def __init__(self, ready: bool, evaporationRate: bool, waterLevel: float, SteamMeasurementDevice25: "SBCS_ControlProgram" = None, SteamMeasurementDevice: "SBCS_SteamBoiler" = None, SteamMeasurementDevice13: "SBCS_Snapshot" = None, SteamBoilerMeasurementDeviceSnapshot: "SBCS_Snapshot" = None, ControlProgramSMD: "SBCS_ControlProgram" = None, SteamBoilerSMD: "SBCS_SteamBoiler" = None):
        self.ready = ready
        self.evaporationRate = evaporationRate
        self.waterLevel = waterLevel
        self.SteamMeasurementDevice25 = SteamMeasurementDevice25
        self.SteamMeasurementDevice = SteamMeasurementDevice
        self.SteamMeasurementDevice13 = SteamMeasurementDevice13
        self.SteamBoilerMeasurementDeviceSnapshot = SteamBoilerMeasurementDeviceSnapshot
        self.ControlProgramSMD = ControlProgramSMD
        self.SteamBoilerSMD = SteamBoilerSMD
        
        pass
    @property
    def waterLevel(self):
        return self.__waterLevel

    @waterLevel.setter
    def waterLevel(self, waterLevel: float):
        self.__waterLevel = waterLevel


    @property
    def ready(self):
        return self.__ready

    @ready.setter
    def ready(self, ready: bool):
        self.__ready = ready


    @property
    def evaporationRate(self):
        return self.__evaporationRate

    @evaporationRate.setter
    def evaporationRate(self, evaporationRate: bool):
        self.__evaporationRate = evaporationRate


    @property
    def SteamMeasurementDevice25(self):
        return self.__SteamMeasurementDevice25

    @SteamMeasurementDevice25.setter
    def SteamMeasurementDevice25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamMeasurementDevice__SteamMeasurementDevice25", None)
        self.__SteamMeasurementDevice25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SMDControlProgram"):
                opp_val = getattr(old_value, "SMDControlProgram", None)
                if opp_val == self:
                    setattr(old_value, "SMDControlProgram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SMDControlProgram"):
                opp_val = getattr(value, "SMDControlProgram", None)
                setattr(value, "SMDControlProgram", self)

    @property
    def SteamBoilerMeasurementDeviceSnapshot(self):
        return self.__SteamBoilerMeasurementDeviceSnapshot

    @SteamBoilerMeasurementDeviceSnapshot.setter
    def SteamBoilerMeasurementDeviceSnapshot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamMeasurementDevice__SteamBoilerMeasurementDeviceSnapshot", None)
        self.__SteamBoilerMeasurementDeviceSnapshot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Snapshot52"):
                opp_val = getattr(old_value, "Snapshot52", None)
                if opp_val == self:
                    setattr(old_value, "Snapshot52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Snapshot52"):
                opp_val = getattr(value, "Snapshot52", None)
                setattr(value, "Snapshot52", self)

    @property
    def SteamMeasurementDevice13(self):
        return self.__SteamMeasurementDevice13

    @SteamMeasurementDevice13.setter
    def SteamMeasurementDevice13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamMeasurementDevice__SteamMeasurementDevice13", None)
        self.__SteamMeasurementDevice13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SnapshotSBMD"):
                opp_val = getattr(old_value, "SnapshotSBMD", None)
                if opp_val == self:
                    setattr(old_value, "SnapshotSBMD", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SnapshotSBMD"):
                opp_val = getattr(value, "SnapshotSBMD", None)
                setattr(value, "SnapshotSBMD", self)

    @property
    def SteamMeasurementDevice(self):
        return self.__SteamMeasurementDevice

    @SteamMeasurementDevice.setter
    def SteamMeasurementDevice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamMeasurementDevice__SteamMeasurementDevice", None)
        self.__SteamMeasurementDevice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SMDSteamBoiler"):
                opp_val = getattr(old_value, "SMDSteamBoiler", None)
                if opp_val == self:
                    setattr(old_value, "SMDSteamBoiler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SMDSteamBoiler"):
                opp_val = getattr(value, "SMDSteamBoiler", None)
                setattr(value, "SMDSteamBoiler", self)

    @property
    def ControlProgramSMD(self):
        return self.__ControlProgramSMD

    @ControlProgramSMD.setter
    def ControlProgramSMD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamMeasurementDevice__ControlProgramSMD", None)
        self.__ControlProgramSMD = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ControlProgram54"):
                opp_val = getattr(old_value, "ControlProgram54", None)
                if opp_val == self:
                    setattr(old_value, "ControlProgram54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ControlProgram54"):
                opp_val = getattr(value, "ControlProgram54", None)
                setattr(value, "ControlProgram54", self)

    @property
    def SteamBoilerSMD(self):
        return self.__SteamBoilerSMD

    @SteamBoilerSMD.setter
    def SteamBoilerSMD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamMeasurementDevice__SteamBoilerSMD", None)
        self.__SteamBoilerSMD = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SteamBoiler56"):
                opp_val = getattr(old_value, "SteamBoiler56", None)
                if opp_val == self:
                    setattr(old_value, "SteamBoiler56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SteamBoiler56"):
                opp_val = getattr(value, "SteamBoiler56", None)
                setattr(value, "SteamBoiler56", self)

class SBCS_Transition:

    pass
class SBCS_PumpControler:

    def __init__(self, ready: bool, circulating: bool, PumpControlSnapshot: "SBCS_Snapshot" = None, PumpControler29: "SBCS_ControlProgram" = None, PumpControler36: "SBCS_Pump" = None, ControlProgramPumpControler: "SBCS_ControlProgram" = None, PumpPumpControler: "SBCS_Pump" = None, PumpControler: "SBCS_Snapshot" = None, SBCS_PumpControler80: "SBCS_PumpController_OpenPump" = None, SBCS_PumpControler83: "SBCS_PumpController_OpenPump" = None, SBCS_PumpControler: "SBCS_PumpController_ClosePump" = None, SBCS_PumpControler78: "SBCS_PumpController_ClosePump" = None):
        self.ready = ready
        self.circulating = circulating
        self.PumpControlSnapshot = PumpControlSnapshot
        self.PumpControler29 = PumpControler29
        self.PumpControler36 = PumpControler36
        self.ControlProgramPumpControler = ControlProgramPumpControler
        self.PumpPumpControler = PumpPumpControler
        self.PumpControler = PumpControler
        self.SBCS_PumpControler80 = SBCS_PumpControler80
        self.SBCS_PumpControler83 = SBCS_PumpControler83
        self.SBCS_PumpControler = SBCS_PumpControler
        self.SBCS_PumpControler78 = SBCS_PumpControler78
        
        pass
    @property
    def circulating(self):
        return self.__circulating

    @circulating.setter
    def circulating(self, circulating: bool):
        self.__circulating = circulating


    @property
    def ready(self):
        return self.__ready

    @ready.setter
    def ready(self, ready: bool):
        self.__ready = ready


    @property
    def PumpControlSnapshot(self):
        return self.__PumpControlSnapshot

    @PumpControlSnapshot.setter
    def PumpControlSnapshot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_PumpControler__PumpControlSnapshot", None)
        self.__PumpControlSnapshot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Snapshot46"):
                opp_val = getattr(old_value, "Snapshot46", None)
                if opp_val == self:
                    setattr(old_value, "Snapshot46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Snapshot46"):
                opp_val = getattr(value, "Snapshot46", None)
                setattr(value, "Snapshot46", self)

    @property
    def SBCS_PumpControler(self):
        return self.__SBCS_PumpControler

    @SBCS_PumpControler.setter
    def SBCS_PumpControler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_PumpControler__SBCS_PumpControler", None)
        self.__SBCS_PumpControler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_PumpController_ClosePump"):
                opp_val = getattr(old_value, "SBCS_PumpController_ClosePump", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_PumpController_ClosePump", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_PumpController_ClosePump"):
                opp_val = getattr(value, "SBCS_PumpController_ClosePump", None)
                setattr(value, "SBCS_PumpController_ClosePump", self)

    @property
    def PumpControler(self):
        return self.__PumpControler

    @PumpControler.setter
    def PumpControler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_PumpControler__PumpControler", None)
        self.__PumpControler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SnapshotPumpControl"):
                opp_val = getattr(old_value, "SnapshotPumpControl", None)
                if opp_val == self:
                    setattr(old_value, "SnapshotPumpControl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SnapshotPumpControl"):
                opp_val = getattr(value, "SnapshotPumpControl", None)
                setattr(value, "SnapshotPumpControl", self)

    @property
    def PumpControler29(self):
        return self.__PumpControler29

    @PumpControler29.setter
    def PumpControler29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_PumpControler__PumpControler29", None)
        self.__PumpControler29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PumpControlerControlProgram"):
                opp_val = getattr(old_value, "PumpControlerControlProgram", None)
                if opp_val == self:
                    setattr(old_value, "PumpControlerControlProgram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PumpControlerControlProgram"):
                opp_val = getattr(value, "PumpControlerControlProgram", None)
                setattr(value, "PumpControlerControlProgram", self)

    @property
    def SBCS_PumpControler78(self):
        return self.__SBCS_PumpControler78

    @SBCS_PumpControler78.setter
    def SBCS_PumpControler78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_PumpControler__SBCS_PumpControler78", None)
        self.__SBCS_PumpControler78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_PumpController_ClosePump77"):
                opp_val = getattr(old_value, "SBCS_PumpController_ClosePump77", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_PumpController_ClosePump77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_PumpController_ClosePump77"):
                opp_val = getattr(value, "SBCS_PumpController_ClosePump77", None)
                setattr(value, "SBCS_PumpController_ClosePump77", self)

    @property
    def PumpPumpControler(self):
        return self.__PumpPumpControler

    @PumpPumpControler.setter
    def PumpPumpControler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_PumpControler__PumpPumpControler", None)
        self.__PumpPumpControler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pump50"):
                opp_val = getattr(old_value, "Pump50", None)
                if opp_val == self:
                    setattr(old_value, "Pump50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pump50"):
                opp_val = getattr(value, "Pump50", None)
                setattr(value, "Pump50", self)

    @property
    def SBCS_PumpControler80(self):
        return self.__SBCS_PumpControler80

    @SBCS_PumpControler80.setter
    def SBCS_PumpControler80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_PumpControler__SBCS_PumpControler80", None)
        self.__SBCS_PumpControler80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_PumpController_OpenPump"):
                opp_val = getattr(old_value, "SBCS_PumpController_OpenPump", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_PumpController_OpenPump", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_PumpController_OpenPump"):
                opp_val = getattr(value, "SBCS_PumpController_OpenPump", None)
                setattr(value, "SBCS_PumpController_OpenPump", self)

    @property
    def SBCS_PumpControler83(self):
        return self.__SBCS_PumpControler83

    @SBCS_PumpControler83.setter
    def SBCS_PumpControler83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_PumpControler__SBCS_PumpControler83", None)
        self.__SBCS_PumpControler83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_PumpController_OpenPump82"):
                opp_val = getattr(old_value, "SBCS_PumpController_OpenPump82", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_PumpController_OpenPump82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_PumpController_OpenPump82"):
                opp_val = getattr(value, "SBCS_PumpController_OpenPump82", None)
                setattr(value, "SBCS_PumpController_OpenPump82", self)

    @property
    def PumpControler36(self):
        return self.__PumpControler36

    @PumpControler36.setter
    def PumpControler36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_PumpControler__PumpControler36", None)
        self.__PumpControler36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PumpControlerPump"):
                opp_val = getattr(old_value, "PumpControlerPump", None)
                if opp_val == self:
                    setattr(old_value, "PumpControlerPump", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PumpControlerPump"):
                opp_val = getattr(value, "PumpControlerPump", None)
                setattr(value, "PumpControlerPump", self)

    @property
    def ControlProgramPumpControler(self):
        return self.__ControlProgramPumpControler

    @ControlProgramPumpControler.setter
    def ControlProgramPumpControler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_PumpControler__ControlProgramPumpControler", None)
        self.__ControlProgramPumpControler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ControlProgram48"):
                opp_val = getattr(old_value, "ControlProgram48", None)
                if opp_val == self:
                    setattr(old_value, "ControlProgram48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ControlProgram48"):
                opp_val = getattr(value, "ControlProgram48", None)
                setattr(value, "ControlProgram48", self)

class SBCS_SteamBoiler:

    def __init__(self, ready: bool, capacity: float, minimalNormal: float, maximalNormal: float, maximumIncrease: float, maximumDecrease: float, minimalLimit: float, maximalLimit: float, valveOpen: str, PumpSteamBoiler: "SBCS_Pump" = None, SMDSteamBoiler: "SBCS_SteamMeasurementDevice" = None, WLMDSteamBoiler: "SBCS_WaterLevelMeasurementDevice" = None, SteamBoiler: "SBCS_Snapshot" = None, SteamBoiler38: "SBCS_Pump" = None, SteamBoiler27: "SBCS_ControlProgram" = None, SteamBoilerSnapshot: "SBCS_Snapshot" = None, ControlProgramSteamBoiler: "SBCS_ControlProgram" = None, SteamBoiler56: "SBCS_SteamMeasurementDevice" = None, SteamBoiler62: "SBCS_WaterLevelMeasurementDevice" = None, SBCS_SteamBoiler: "SBCS_SteamBoiler_OpenValve" = None, SBCS_SteamBoiler74: "SBCS_SteamBoiler_OpenValve" = None):
        self.ready = ready
        self.capacity = capacity
        self.minimalNormal = minimalNormal
        self.maximalNormal = maximalNormal
        self.maximumIncrease = maximumIncrease
        self.maximumDecrease = maximumDecrease
        self.minimalLimit = minimalLimit
        self.maximalLimit = maximalLimit
        self.valveOpen = valveOpen
        self.PumpSteamBoiler = PumpSteamBoiler
        self.SMDSteamBoiler = SMDSteamBoiler
        self.WLMDSteamBoiler = WLMDSteamBoiler
        self.SteamBoiler = SteamBoiler
        self.SteamBoiler38 = SteamBoiler38
        self.SteamBoiler27 = SteamBoiler27
        self.SteamBoilerSnapshot = SteamBoilerSnapshot
        self.ControlProgramSteamBoiler = ControlProgramSteamBoiler
        self.SteamBoiler56 = SteamBoiler56
        self.SteamBoiler62 = SteamBoiler62
        self.SBCS_SteamBoiler = SBCS_SteamBoiler
        self.SBCS_SteamBoiler74 = SBCS_SteamBoiler74
        
        pass
    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: float):
        self.__capacity = capacity


    @property
    def maximumDecrease(self):
        return self.__maximumDecrease

    @maximumDecrease.setter
    def maximumDecrease(self, maximumDecrease: float):
        self.__maximumDecrease = maximumDecrease


    @property
    def maximumIncrease(self):
        return self.__maximumIncrease

    @maximumIncrease.setter
    def maximumIncrease(self, maximumIncrease: float):
        self.__maximumIncrease = maximumIncrease


    @property
    def ready(self):
        return self.__ready

    @ready.setter
    def ready(self, ready: bool):
        self.__ready = ready


    @property
    def maximalLimit(self):
        return self.__maximalLimit

    @maximalLimit.setter
    def maximalLimit(self, maximalLimit: float):
        self.__maximalLimit = maximalLimit


    @property
    def maximalNormal(self):
        return self.__maximalNormal

    @maximalNormal.setter
    def maximalNormal(self, maximalNormal: float):
        self.__maximalNormal = maximalNormal


    @property
    def valveOpen(self):
        return self.__valveOpen

    @valveOpen.setter
    def valveOpen(self, valveOpen: str):
        self.__valveOpen = valveOpen


    @property
    def minimalNormal(self):
        return self.__minimalNormal

    @minimalNormal.setter
    def minimalNormal(self, minimalNormal: float):
        self.__minimalNormal = minimalNormal


    @property
    def minimalLimit(self):
        return self.__minimalLimit

    @minimalLimit.setter
    def minimalLimit(self, minimalLimit: float):
        self.__minimalLimit = minimalLimit


    @property
    def SMDSteamBoiler(self):
        return self.__SMDSteamBoiler

    @SMDSteamBoiler.setter
    def SMDSteamBoiler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamBoiler__SMDSteamBoiler", None)
        self.__SMDSteamBoiler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SteamMeasurementDevice"):
                opp_val = getattr(old_value, "SteamMeasurementDevice", None)
                if opp_val == self:
                    setattr(old_value, "SteamMeasurementDevice", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SteamMeasurementDevice"):
                opp_val = getattr(value, "SteamMeasurementDevice", None)
                setattr(value, "SteamMeasurementDevice", self)

    @property
    def SteamBoilerSnapshot(self):
        return self.__SteamBoilerSnapshot

    @SteamBoilerSnapshot.setter
    def SteamBoilerSnapshot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamBoiler__SteamBoilerSnapshot", None)
        self.__SteamBoilerSnapshot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Snapshot"):
                opp_val = getattr(old_value, "Snapshot", None)
                if opp_val == self:
                    setattr(old_value, "Snapshot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Snapshot"):
                opp_val = getattr(value, "Snapshot", None)
                setattr(value, "Snapshot", self)

    @property
    def SteamBoiler27(self):
        return self.__SteamBoiler27

    @SteamBoiler27.setter
    def SteamBoiler27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamBoiler__SteamBoiler27", None)
        self.__SteamBoiler27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SteamBoilerControlProgram"):
                opp_val = getattr(old_value, "SteamBoilerControlProgram", None)
                if opp_val == self:
                    setattr(old_value, "SteamBoilerControlProgram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SteamBoilerControlProgram"):
                opp_val = getattr(value, "SteamBoilerControlProgram", None)
                setattr(value, "SteamBoilerControlProgram", self)

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

    @property
    def SteamBoiler(self):
        return self.__SteamBoiler

    @SteamBoiler.setter
    def SteamBoiler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamBoiler__SteamBoiler", None)
        self.__SteamBoiler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SnapshotSteamBoiler"):
                opp_val = getattr(old_value, "SnapshotSteamBoiler", None)
                if opp_val == self:
                    setattr(old_value, "SnapshotSteamBoiler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SnapshotSteamBoiler"):
                opp_val = getattr(value, "SnapshotSteamBoiler", None)
                setattr(value, "SnapshotSteamBoiler", self)

    @property
    def WLMDSteamBoiler(self):
        return self.__WLMDSteamBoiler

    @WLMDSteamBoiler.setter
    def WLMDSteamBoiler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamBoiler__WLMDSteamBoiler", None)
        self.__WLMDSteamBoiler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WaterLevelMeasurementDevice"):
                opp_val = getattr(old_value, "WaterLevelMeasurementDevice", None)
                if opp_val == self:
                    setattr(old_value, "WaterLevelMeasurementDevice", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WaterLevelMeasurementDevice"):
                opp_val = getattr(value, "WaterLevelMeasurementDevice", None)
                setattr(value, "WaterLevelMeasurementDevice", self)

    @property
    def ControlProgramSteamBoiler(self):
        return self.__ControlProgramSteamBoiler

    @ControlProgramSteamBoiler.setter
    def ControlProgramSteamBoiler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamBoiler__ControlProgramSteamBoiler", None)
        self.__ControlProgramSteamBoiler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ControlProgram"):
                opp_val = getattr(old_value, "ControlProgram", None)
                if opp_val == self:
                    setattr(old_value, "ControlProgram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ControlProgram"):
                opp_val = getattr(value, "ControlProgram", None)
                setattr(value, "ControlProgram", self)

    @property
    def SteamBoiler62(self):
        return self.__SteamBoiler62

    @SteamBoiler62.setter
    def SteamBoiler62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamBoiler__SteamBoiler62", None)
        self.__SteamBoiler62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SteamBoilerWLMD"):
                opp_val = getattr(old_value, "SteamBoilerWLMD", None)
                if opp_val == self:
                    setattr(old_value, "SteamBoilerWLMD", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SteamBoilerWLMD"):
                opp_val = getattr(value, "SteamBoilerWLMD", None)
                setattr(value, "SteamBoilerWLMD", self)

    @property
    def PumpSteamBoiler(self):
        return self.__PumpSteamBoiler

    @PumpSteamBoiler.setter
    def PumpSteamBoiler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamBoiler__PumpSteamBoiler", None)
        self.__PumpSteamBoiler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pump"):
                opp_val = getattr(old_value, "Pump", None)
                if opp_val == self:
                    setattr(old_value, "Pump", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pump"):
                opp_val = getattr(value, "Pump", None)
                setattr(value, "Pump", self)

    @property
    def SteamBoiler38(self):
        return self.__SteamBoiler38

    @SteamBoiler38.setter
    def SteamBoiler38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamBoiler__SteamBoiler38", None)
        self.__SteamBoiler38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SteqmBoilerPump"):
                opp_val = getattr(old_value, "SteqmBoilerPump", None)
                if opp_val == self:
                    setattr(old_value, "SteqmBoilerPump", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SteqmBoilerPump"):
                opp_val = getattr(value, "SteqmBoilerPump", None)
                setattr(value, "SteqmBoilerPump", self)

    @property
    def SBCS_SteamBoiler74(self):
        return self.__SBCS_SteamBoiler74

    @SBCS_SteamBoiler74.setter
    def SBCS_SteamBoiler74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamBoiler__SBCS_SteamBoiler74", None)
        self.__SBCS_SteamBoiler74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_SteamBoiler_OpenValve73"):
                opp_val = getattr(old_value, "SBCS_SteamBoiler_OpenValve73", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_SteamBoiler_OpenValve73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_SteamBoiler_OpenValve73"):
                opp_val = getattr(value, "SBCS_SteamBoiler_OpenValve73", None)
                setattr(value, "SBCS_SteamBoiler_OpenValve73", self)

    @property
    def SteamBoiler56(self):
        return self.__SteamBoiler56

    @SteamBoiler56.setter
    def SteamBoiler56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_SteamBoiler__SteamBoiler56", None)
        self.__SteamBoiler56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SteamBoilerSMD"):
                opp_val = getattr(old_value, "SteamBoilerSMD", None)
                if opp_val == self:
                    setattr(old_value, "SteamBoilerSMD", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SteamBoilerSMD"):
                opp_val = getattr(value, "SteamBoilerSMD", None)
                setattr(value, "SteamBoilerSMD", self)

class SBCS_Pump:

    def __init__(self, ready: bool, capacity: float, mode: str, Pump21: "SBCS_ControlProgram" = None, Pump: "SBCS_SteamBoiler" = None, Pump9: "SBCS_Snapshot" = None, SteqmBoilerPump: "SBCS_SteamBoiler" = None, PumpSnapshot31: "SBCS_Snapshot" = None, ControlProgramPump: "SBCS_ControlProgram" = None, PumpControlerPump: "SBCS_PumpControler" = None, Pump50: "SBCS_PumpControler" = None):
        self.ready = ready
        self.capacity = capacity
        self.mode = mode
        self.Pump21 = Pump21
        self.Pump = Pump
        self.Pump9 = Pump9
        self.SteqmBoilerPump = SteqmBoilerPump
        self.PumpSnapshot31 = PumpSnapshot31
        self.ControlProgramPump = ControlProgramPump
        self.PumpControlerPump = PumpControlerPump
        self.Pump50 = Pump50
        
        pass
    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode


    @property
    def ready(self):
        return self.__ready

    @ready.setter
    def ready(self, ready: bool):
        self.__ready = ready


    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: float):
        self.__capacity = capacity


    @property
    def ControlProgramPump(self):
        return self.__ControlProgramPump

    @ControlProgramPump.setter
    def ControlProgramPump(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Pump__ControlProgramPump", None)
        self.__ControlProgramPump = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ControlProgram34"):
                opp_val = getattr(old_value, "ControlProgram34", None)
                if opp_val == self:
                    setattr(old_value, "ControlProgram34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ControlProgram34"):
                opp_val = getattr(value, "ControlProgram34", None)
                setattr(value, "ControlProgram34", self)

    @property
    def PumpSnapshot31(self):
        return self.__PumpSnapshot31

    @PumpSnapshot31.setter
    def PumpSnapshot31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Pump__PumpSnapshot31", None)
        self.__PumpSnapshot31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Snapshot32"):
                opp_val = getattr(old_value, "Snapshot32", None)
                if opp_val == self:
                    setattr(old_value, "Snapshot32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Snapshot32"):
                opp_val = getattr(value, "Snapshot32", None)
                setattr(value, "Snapshot32", self)

    @property
    def Pump9(self):
        return self.__Pump9

    @Pump9.setter
    def Pump9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Pump__Pump9", None)
        self.__Pump9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PumpSnapshot"):
                opp_val = getattr(old_value, "PumpSnapshot", None)
                if opp_val == self:
                    setattr(old_value, "PumpSnapshot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PumpSnapshot"):
                opp_val = getattr(value, "PumpSnapshot", None)
                setattr(value, "PumpSnapshot", self)

    @property
    def SteqmBoilerPump(self):
        return self.__SteqmBoilerPump

    @SteqmBoilerPump.setter
    def SteqmBoilerPump(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Pump__SteqmBoilerPump", None)
        self.__SteqmBoilerPump = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SteamBoiler38"):
                opp_val = getattr(old_value, "SteamBoiler38", None)
                if opp_val == self:
                    setattr(old_value, "SteamBoiler38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SteamBoiler38"):
                opp_val = getattr(value, "SteamBoiler38", None)
                setattr(value, "SteamBoiler38", self)

    @property
    def Pump21(self):
        return self.__Pump21

    @Pump21.setter
    def Pump21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Pump__Pump21", None)
        self.__Pump21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PumpControlProgram"):
                opp_val = getattr(old_value, "PumpControlProgram", None)
                if opp_val == self:
                    setattr(old_value, "PumpControlProgram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PumpControlProgram"):
                opp_val = getattr(value, "PumpControlProgram", None)
                setattr(value, "PumpControlProgram", self)

    @property
    def Pump(self):
        return self.__Pump

    @Pump.setter
    def Pump(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Pump__Pump", None)
        self.__Pump = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PumpSteamBoiler"):
                opp_val = getattr(old_value, "PumpSteamBoiler", None)
                if opp_val == self:
                    setattr(old_value, "PumpSteamBoiler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PumpSteamBoiler"):
                opp_val = getattr(value, "PumpSteamBoiler", None)
                setattr(value, "PumpSteamBoiler", self)

    @property
    def PumpControlerPump(self):
        return self.__PumpControlerPump

    @PumpControlerPump.setter
    def PumpControlerPump(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Pump__PumpControlerPump", None)
        self.__PumpControlerPump = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PumpControler36"):
                opp_val = getattr(old_value, "PumpControler36", None)
                if opp_val == self:
                    setattr(old_value, "PumpControler36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PumpControler36"):
                opp_val = getattr(value, "PumpControler36", None)
                setattr(value, "PumpControler36", self)

    @property
    def Pump50(self):
        return self.__Pump50

    @Pump50.setter
    def Pump50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Pump__Pump50", None)
        self.__Pump50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PumpPumpControler"):
                opp_val = getattr(old_value, "PumpPumpControler", None)
                if opp_val == self:
                    setattr(old_value, "PumpPumpControler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PumpPumpControler"):
                opp_val = getattr(value, "PumpPumpControler", None)
                setattr(value, "PumpPumpControler", self)

class SBCS_ControlProgram:

    def __init__(self, mode: str, ready: bool, failureDetected: bool, wlmdFailure: bool, smdFailure: bool, pumpFailure: bool, pumpControlerFailure: bool, ControlProgramSnapshot: "SBCS_Snapshot" = None, PumpControlProgram: "SBCS_Pump" = None, WLMDControlProgram: "SBCS_WaterLevelMeasurementDevice" = None, SMDControlProgram: "SBCS_SteamMeasurementDevice" = None, ControlProgram7: "SBCS_Snapshot" = None, SteamBoilerControlProgram: "SBCS_SteamBoiler" = None, PumpControlerControlProgram: "SBCS_PumpControler" = None, ControlProgram34: "SBCS_Pump" = None, SBCS_ControlProgram: "SBCS_ControlProgram_Start" = None, SBCS_ControlProgram66: "SBCS_ControlProgram_Start" = None, ControlProgram48: "SBCS_PumpControler" = None, ControlProgram: "SBCS_SteamBoiler" = None, ControlProgram54: "SBCS_SteamMeasurementDevice" = None, ControlProgram60: "SBCS_WaterLevelMeasurementDevice" = None):
        self.mode = mode
        self.ready = ready
        self.failureDetected = failureDetected
        self.wlmdFailure = wlmdFailure
        self.smdFailure = smdFailure
        self.pumpFailure = pumpFailure
        self.pumpControlerFailure = pumpControlerFailure
        self.ControlProgramSnapshot = ControlProgramSnapshot
        self.PumpControlProgram = PumpControlProgram
        self.WLMDControlProgram = WLMDControlProgram
        self.SMDControlProgram = SMDControlProgram
        self.ControlProgram7 = ControlProgram7
        self.SteamBoilerControlProgram = SteamBoilerControlProgram
        self.PumpControlerControlProgram = PumpControlerControlProgram
        self.ControlProgram34 = ControlProgram34
        self.SBCS_ControlProgram = SBCS_ControlProgram
        self.SBCS_ControlProgram66 = SBCS_ControlProgram66
        self.ControlProgram48 = ControlProgram48
        self.ControlProgram = ControlProgram
        self.ControlProgram54 = ControlProgram54
        self.ControlProgram60 = ControlProgram60
        
        pass
    @property
    def failureDetected(self):
        return self.__failureDetected

    @failureDetected.setter
    def failureDetected(self, failureDetected: bool):
        self.__failureDetected = failureDetected


    @property
    def pumpFailure(self):
        return self.__pumpFailure

    @pumpFailure.setter
    def pumpFailure(self, pumpFailure: bool):
        self.__pumpFailure = pumpFailure


    @property
    def ready(self):
        return self.__ready

    @ready.setter
    def ready(self, ready: bool):
        self.__ready = ready


    @property
    def wlmdFailure(self):
        return self.__wlmdFailure

    @wlmdFailure.setter
    def wlmdFailure(self, wlmdFailure: bool):
        self.__wlmdFailure = wlmdFailure


    @property
    def smdFailure(self):
        return self.__smdFailure

    @smdFailure.setter
    def smdFailure(self, smdFailure: bool):
        self.__smdFailure = smdFailure


    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode


    @property
    def pumpControlerFailure(self):
        return self.__pumpControlerFailure

    @pumpControlerFailure.setter
    def pumpControlerFailure(self, pumpControlerFailure: bool):
        self.__pumpControlerFailure = pumpControlerFailure


    @property
    def ControlProgram60(self):
        return self.__ControlProgram60

    @ControlProgram60.setter
    def ControlProgram60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_ControlProgram__ControlProgram60", None)
        self.__ControlProgram60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ControlProgramWLMD"):
                opp_val = getattr(old_value, "ControlProgramWLMD", None)
                if opp_val == self:
                    setattr(old_value, "ControlProgramWLMD", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ControlProgramWLMD"):
                opp_val = getattr(value, "ControlProgramWLMD", None)
                setattr(value, "ControlProgramWLMD", self)

    @property
    def ControlProgram48(self):
        return self.__ControlProgram48

    @ControlProgram48.setter
    def ControlProgram48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_ControlProgram__ControlProgram48", None)
        self.__ControlProgram48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ControlProgramPumpControler"):
                opp_val = getattr(old_value, "ControlProgramPumpControler", None)
                if opp_val == self:
                    setattr(old_value, "ControlProgramPumpControler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ControlProgramPumpControler"):
                opp_val = getattr(value, "ControlProgramPumpControler", None)
                setattr(value, "ControlProgramPumpControler", self)

    @property
    def ControlProgram34(self):
        return self.__ControlProgram34

    @ControlProgram34.setter
    def ControlProgram34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_ControlProgram__ControlProgram34", None)
        self.__ControlProgram34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ControlProgramPump"):
                opp_val = getattr(old_value, "ControlProgramPump", None)
                if opp_val == self:
                    setattr(old_value, "ControlProgramPump", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ControlProgramPump"):
                opp_val = getattr(value, "ControlProgramPump", None)
                setattr(value, "ControlProgramPump", self)

    @property
    def SteamBoilerControlProgram(self):
        return self.__SteamBoilerControlProgram

    @SteamBoilerControlProgram.setter
    def SteamBoilerControlProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_ControlProgram__SteamBoilerControlProgram", None)
        self.__SteamBoilerControlProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SteamBoiler27"):
                opp_val = getattr(old_value, "SteamBoiler27", None)
                if opp_val == self:
                    setattr(old_value, "SteamBoiler27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SteamBoiler27"):
                opp_val = getattr(value, "SteamBoiler27", None)
                setattr(value, "SteamBoiler27", self)

    @property
    def ControlProgramSnapshot(self):
        return self.__ControlProgramSnapshot

    @ControlProgramSnapshot.setter
    def ControlProgramSnapshot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_ControlProgram__ControlProgramSnapshot", None)
        self.__ControlProgramSnapshot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Snapshot19"):
                opp_val = getattr(old_value, "Snapshot19", None)
                if opp_val == self:
                    setattr(old_value, "Snapshot19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Snapshot19"):
                opp_val = getattr(value, "Snapshot19", None)
                setattr(value, "Snapshot19", self)

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

    @property
    def PumpControlProgram(self):
        return self.__PumpControlProgram

    @PumpControlProgram.setter
    def PumpControlProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_ControlProgram__PumpControlProgram", None)
        self.__PumpControlProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pump21"):
                opp_val = getattr(old_value, "Pump21", None)
                if opp_val == self:
                    setattr(old_value, "Pump21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pump21"):
                opp_val = getattr(value, "Pump21", None)
                setattr(value, "Pump21", self)

    @property
    def WLMDControlProgram(self):
        return self.__WLMDControlProgram

    @WLMDControlProgram.setter
    def WLMDControlProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_ControlProgram__WLMDControlProgram", None)
        self.__WLMDControlProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WaterLevelMeasurementDevice23"):
                opp_val = getattr(old_value, "WaterLevelMeasurementDevice23", None)
                if opp_val == self:
                    setattr(old_value, "WaterLevelMeasurementDevice23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WaterLevelMeasurementDevice23"):
                opp_val = getattr(value, "WaterLevelMeasurementDevice23", None)
                setattr(value, "WaterLevelMeasurementDevice23", self)

    @property
    def PumpControlerControlProgram(self):
        return self.__PumpControlerControlProgram

    @PumpControlerControlProgram.setter
    def PumpControlerControlProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_ControlProgram__PumpControlerControlProgram", None)
        self.__PumpControlerControlProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PumpControler29"):
                opp_val = getattr(old_value, "PumpControler29", None)
                if opp_val == self:
                    setattr(old_value, "PumpControler29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PumpControler29"):
                opp_val = getattr(value, "PumpControler29", None)
                setattr(value, "PumpControler29", self)

    @property
    def ControlProgram54(self):
        return self.__ControlProgram54

    @ControlProgram54.setter
    def ControlProgram54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_ControlProgram__ControlProgram54", None)
        self.__ControlProgram54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ControlProgramSMD"):
                opp_val = getattr(old_value, "ControlProgramSMD", None)
                if opp_val == self:
                    setattr(old_value, "ControlProgramSMD", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ControlProgramSMD"):
                opp_val = getattr(value, "ControlProgramSMD", None)
                setattr(value, "ControlProgramSMD", self)

    @property
    def ControlProgram7(self):
        return self.__ControlProgram7

    @ControlProgram7.setter
    def ControlProgram7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_ControlProgram__ControlProgram7", None)
        self.__ControlProgram7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SnapshotControlProgram"):
                opp_val = getattr(old_value, "SnapshotControlProgram", None)
                if opp_val == self:
                    setattr(old_value, "SnapshotControlProgram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SnapshotControlProgram"):
                opp_val = getattr(value, "SnapshotControlProgram", None)
                setattr(value, "SnapshotControlProgram", self)

    @property
    def SMDControlProgram(self):
        return self.__SMDControlProgram

    @SMDControlProgram.setter
    def SMDControlProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_ControlProgram__SMDControlProgram", None)
        self.__SMDControlProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SteamMeasurementDevice25"):
                opp_val = getattr(old_value, "SteamMeasurementDevice25", None)
                if opp_val == self:
                    setattr(old_value, "SteamMeasurementDevice25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SteamMeasurementDevice25"):
                opp_val = getattr(value, "SteamMeasurementDevice25", None)
                setattr(value, "SteamMeasurementDevice25", self)

    @property
    def SBCS_ControlProgram66(self):
        return self.__SBCS_ControlProgram66

    @SBCS_ControlProgram66.setter
    def SBCS_ControlProgram66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_ControlProgram__SBCS_ControlProgram66", None)
        self.__SBCS_ControlProgram66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SBCS_ControlProgram_Start65"):
                opp_val = getattr(old_value, "SBCS_ControlProgram_Start65", None)
                if opp_val == self:
                    setattr(old_value, "SBCS_ControlProgram_Start65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SBCS_ControlProgram_Start65"):
                opp_val = getattr(value, "SBCS_ControlProgram_Start65", None)
                setattr(value, "SBCS_ControlProgram_Start65", self)

    @property
    def ControlProgram(self):
        return self.__ControlProgram

    @ControlProgram.setter
    def ControlProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_ControlProgram__ControlProgram", None)
        self.__ControlProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ControlProgramSteamBoiler"):
                opp_val = getattr(old_value, "ControlProgramSteamBoiler", None)
                if opp_val == self:
                    setattr(old_value, "ControlProgramSteamBoiler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ControlProgramSteamBoiler"):
                opp_val = getattr(value, "ControlProgramSteamBoiler", None)
                setattr(value, "ControlProgramSteamBoiler", self)

class SBCS_Snapshot:

    def __init__(self, Snapshot19: "SBCS_ControlProgram" = None, SnapshotSteamBoiler: "SBCS_SteamBoiler" = None, SnapshotControlProgram: "SBCS_ControlProgram" = None, PumpSnapshot: "SBCS_Pump" = None, SnapshotWLMD: "SBCS_WaterLevelMeasurementDevice" = None, Snapshot41: "SBCS_Transition" = None, Snapshot44: "SBCS_Transition" = None, Snapshot46: "SBCS_PumpControler" = None, Snapshot32: "SBCS_Pump" = None, Snapshot: "SBCS_SteamBoiler" = None, SnapshotSBMD: "SBCS_SteamMeasurementDevice" = None, SnapshotPumpControl: "SBCS_PumpControler" = None, BeforeTrans: "SBCS_Transition" = None, AfterTrans: "SBCS_Transition" = None, Snapshot52: "SBCS_SteamMeasurementDevice" = None, Snapshot58: "SBCS_WaterLevelMeasurementDevice" = None):
        self.Snapshot19 = Snapshot19
        self.SnapshotSteamBoiler = SnapshotSteamBoiler
        self.SnapshotControlProgram = SnapshotControlProgram
        self.PumpSnapshot = PumpSnapshot
        self.SnapshotWLMD = SnapshotWLMD
        self.Snapshot41 = Snapshot41
        self.Snapshot44 = Snapshot44
        self.Snapshot46 = Snapshot46
        self.Snapshot32 = Snapshot32
        self.Snapshot = Snapshot
        self.SnapshotSBMD = SnapshotSBMD
        self.SnapshotPumpControl = SnapshotPumpControl
        self.BeforeTrans = BeforeTrans
        self.AfterTrans = AfterTrans
        self.Snapshot52 = Snapshot52
        self.Snapshot58 = Snapshot58
        
        pass
    @property
    def Snapshot46(self):
        return self.__Snapshot46

    @Snapshot46.setter
    def Snapshot46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__Snapshot46", None)
        self.__Snapshot46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PumpControlSnapshot"):
                opp_val = getattr(old_value, "PumpControlSnapshot", None)
                if opp_val == self:
                    setattr(old_value, "PumpControlSnapshot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PumpControlSnapshot"):
                opp_val = getattr(value, "PumpControlSnapshot", None)
                setattr(value, "PumpControlSnapshot", self)

    @property
    def Snapshot58(self):
        return self.__Snapshot58

    @Snapshot58.setter
    def Snapshot58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__Snapshot58", None)
        self.__Snapshot58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WLMDSnapshot"):
                opp_val = getattr(old_value, "WLMDSnapshot", None)
                if opp_val == self:
                    setattr(old_value, "WLMDSnapshot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WLMDSnapshot"):
                opp_val = getattr(value, "WLMDSnapshot", None)
                setattr(value, "WLMDSnapshot", self)

    @property
    def SnapshotSteamBoiler(self):
        return self.__SnapshotSteamBoiler

    @SnapshotSteamBoiler.setter
    def SnapshotSteamBoiler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__SnapshotSteamBoiler", None)
        self.__SnapshotSteamBoiler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SteamBoiler"):
                opp_val = getattr(old_value, "SteamBoiler", None)
                if opp_val == self:
                    setattr(old_value, "SteamBoiler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SteamBoiler"):
                opp_val = getattr(value, "SteamBoiler", None)
                setattr(value, "SteamBoiler", self)

    @property
    def Snapshot(self):
        return self.__Snapshot

    @Snapshot.setter
    def Snapshot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__Snapshot", None)
        self.__Snapshot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SteamBoilerSnapshot"):
                opp_val = getattr(old_value, "SteamBoilerSnapshot", None)
                if opp_val == self:
                    setattr(old_value, "SteamBoilerSnapshot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SteamBoilerSnapshot"):
                opp_val = getattr(value, "SteamBoilerSnapshot", None)
                setattr(value, "SteamBoilerSnapshot", self)

    @property
    def AfterTrans(self):
        return self.__AfterTrans

    @AfterTrans.setter
    def AfterTrans(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__AfterTrans", None)
        self.__AfterTrans = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transition17"):
                opp_val = getattr(old_value, "Transition17", None)
                if opp_val == self:
                    setattr(old_value, "Transition17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transition17"):
                opp_val = getattr(value, "Transition17", None)
                setattr(value, "Transition17", self)

    @property
    def Snapshot44(self):
        return self.__Snapshot44

    @Snapshot44.setter
    def Snapshot44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__Snapshot44", None)
        self.__Snapshot44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AfterTrans43"):
                opp_val = getattr(old_value, "AfterTrans43", None)
                if opp_val == self:
                    setattr(old_value, "AfterTrans43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AfterTrans43"):
                opp_val = getattr(value, "AfterTrans43", None)
                setattr(value, "AfterTrans43", self)

    @property
    def Snapshot19(self):
        return self.__Snapshot19

    @Snapshot19.setter
    def Snapshot19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__Snapshot19", None)
        self.__Snapshot19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ControlProgramSnapshot"):
                opp_val = getattr(old_value, "ControlProgramSnapshot", None)
                if opp_val == self:
                    setattr(old_value, "ControlProgramSnapshot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ControlProgramSnapshot"):
                opp_val = getattr(value, "ControlProgramSnapshot", None)
                setattr(value, "ControlProgramSnapshot", self)

    @property
    def SnapshotControlProgram(self):
        return self.__SnapshotControlProgram

    @SnapshotControlProgram.setter
    def SnapshotControlProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__SnapshotControlProgram", None)
        self.__SnapshotControlProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ControlProgram7"):
                opp_val = getattr(old_value, "ControlProgram7", None)
                if opp_val == self:
                    setattr(old_value, "ControlProgram7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ControlProgram7"):
                opp_val = getattr(value, "ControlProgram7", None)
                setattr(value, "ControlProgram7", self)

    @property
    def SnapshotWLMD(self):
        return self.__SnapshotWLMD

    @SnapshotWLMD.setter
    def SnapshotWLMD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__SnapshotWLMD", None)
        self.__SnapshotWLMD = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WaterLevelMeasurementDevice11"):
                opp_val = getattr(old_value, "WaterLevelMeasurementDevice11", None)
                if opp_val == self:
                    setattr(old_value, "WaterLevelMeasurementDevice11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WaterLevelMeasurementDevice11"):
                opp_val = getattr(value, "WaterLevelMeasurementDevice11", None)
                setattr(value, "WaterLevelMeasurementDevice11", self)

    @property
    def Snapshot32(self):
        return self.__Snapshot32

    @Snapshot32.setter
    def Snapshot32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__Snapshot32", None)
        self.__Snapshot32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PumpSnapshot31"):
                opp_val = getattr(old_value, "PumpSnapshot31", None)
                if opp_val == self:
                    setattr(old_value, "PumpSnapshot31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PumpSnapshot31"):
                opp_val = getattr(value, "PumpSnapshot31", None)
                setattr(value, "PumpSnapshot31", self)

    @property
    def SnapshotSBMD(self):
        return self.__SnapshotSBMD

    @SnapshotSBMD.setter
    def SnapshotSBMD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__SnapshotSBMD", None)
        self.__SnapshotSBMD = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SteamMeasurementDevice13"):
                opp_val = getattr(old_value, "SteamMeasurementDevice13", None)
                if opp_val == self:
                    setattr(old_value, "SteamMeasurementDevice13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SteamMeasurementDevice13"):
                opp_val = getattr(value, "SteamMeasurementDevice13", None)
                setattr(value, "SteamMeasurementDevice13", self)

    @property
    def BeforeTrans(self):
        return self.__BeforeTrans

    @BeforeTrans.setter
    def BeforeTrans(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__BeforeTrans", None)
        self.__BeforeTrans = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transition"):
                opp_val = getattr(old_value, "Transition", None)
                if opp_val == self:
                    setattr(old_value, "Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transition"):
                opp_val = getattr(value, "Transition", None)
                setattr(value, "Transition", self)

    @property
    def Snapshot52(self):
        return self.__Snapshot52

    @Snapshot52.setter
    def Snapshot52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__Snapshot52", None)
        self.__Snapshot52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SteamBoilerMeasurementDeviceSnapshot"):
                opp_val = getattr(old_value, "SteamBoilerMeasurementDeviceSnapshot", None)
                if opp_val == self:
                    setattr(old_value, "SteamBoilerMeasurementDeviceSnapshot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SteamBoilerMeasurementDeviceSnapshot"):
                opp_val = getattr(value, "SteamBoilerMeasurementDeviceSnapshot", None)
                setattr(value, "SteamBoilerMeasurementDeviceSnapshot", self)

    @property
    def Snapshot41(self):
        return self.__Snapshot41

    @Snapshot41.setter
    def Snapshot41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__Snapshot41", None)
        self.__Snapshot41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BeforeTrans40"):
                opp_val = getattr(old_value, "BeforeTrans40", None)
                if opp_val == self:
                    setattr(old_value, "BeforeTrans40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BeforeTrans40"):
                opp_val = getattr(value, "BeforeTrans40", None)
                setattr(value, "BeforeTrans40", self)

    @property
    def PumpSnapshot(self):
        return self.__PumpSnapshot

    @PumpSnapshot.setter
    def PumpSnapshot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__PumpSnapshot", None)
        self.__PumpSnapshot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pump9"):
                opp_val = getattr(old_value, "Pump9", None)
                if opp_val == self:
                    setattr(old_value, "Pump9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pump9"):
                opp_val = getattr(value, "Pump9", None)
                setattr(value, "Pump9", self)

    @property
    def SnapshotPumpControl(self):
        return self.__SnapshotPumpControl

    @SnapshotPumpControl.setter
    def SnapshotPumpControl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SBCS_Snapshot__SnapshotPumpControl", None)
        self.__SnapshotPumpControl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PumpControler"):
                opp_val = getattr(old_value, "PumpControler", None)
                if opp_val == self:
                    setattr(old_value, "PumpControler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PumpControler"):
                opp_val = getattr(value, "PumpControler", None)
                setattr(value, "PumpControler", self)

    def getNext(self) :
        # TODO: Implement getNext method
        pass

    def getPrevious(self) :
        # TODO: Implement getPrevious method
        pass

    def getPost(self) :
        # TODO: Implement getPost method
        pass

    def futureClosure(self, SBCS_s) :
        # TODO: Implement futureClosure method
        pass

    def previousClosure(self, SBCS_s) :
        # TODO: Implement previousClosure method
        pass

    def getPre(self) :
        # TODO: Implement getPre method
        pass
