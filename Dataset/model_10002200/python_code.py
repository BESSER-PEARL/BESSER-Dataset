from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class FloorCoordinates:

    def __init__(self, XcoordinatePosition: int, YcoordinatePosition: int):
        self.XcoordinatePosition = XcoordinatePosition
        self.YcoordinatePosition = YcoordinatePosition
        
        pass
    @property
    def XcoordinatePosition(self):
        return self.__XcoordinatePosition
    @XcoordinatePosition.setter
    def XcoordinatePosition(self, XcoordinatePosition: int):
        self.__XcoordinatePosition = XcoordinatePosition

    @property
    def YcoordinatePosition(self):
        return self.__YcoordinatePosition
    @YcoordinatePosition.setter
    def YcoordinatePosition(self, YcoordinatePosition: int):
        self.__YcoordinatePosition = YcoordinatePosition



class Segment:

    pass


class FloorPlan:

    def __init__(self, floorName: str, config3: "config" = None, segment4: "Segment" = None):
        self.floorName = floorName
        self.config3 = config3
        self.segment4 = segment4
        
        pass
    @property
    def floorName(self):
        return self.__floorName
    @floorName.setter
    def floorName(self, floorName: str):
        self.__floorName = floorName

    @property
    def config3(self):
        return self.__config3
    @config3.setter
    def config3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FloorPlan__config3", None)
        self.__config3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "floorPlan2"):
                opp_val = getattr(old_value, "floorPlan2", None)
                if opp_val == self:
                    setattr(old_value, "floorPlan2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "floorPlan2"):
                opp_val = getattr(value, "floorPlan2", None)
                setattr(value, "floorPlan2", self)

    @property
    def segment4(self):
        return self.__segment4
    @segment4.setter
    def segment4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FloorPlan__segment4", None)
        self.__segment4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "floorPlan5"):
                opp_val = getattr(old_value, "floorPlan5", None)
                if opp_val == self:
                    setattr(old_value, "floorPlan5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "floorPlan5"):
                opp_val = getattr(value, "floorPlan5", None)
                setattr(value, "floorPlan5", self)



class ActivationCode:

    def __init__(self, code: int, config1: "config" = None):
        self.code = code
        self.config1 = config1
        
        pass
    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self, code: int):
        self.__code = code

    @property
    def config1(self):
        return self.__config1
    @config1.setter
    def config1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActivationCode__config1", None)
        self.__config1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activationCode0"):
                opp_val = getattr(old_value, "activationCode0", None)
                if opp_val == self:
                    setattr(old_value, "activationCode0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activationCode0"):
                opp_val = getattr(value, "activationCode0", None)
                setattr(value, "activationCode0", self)



class Home_Theatre:

    def __init__(self, companyName: str):
        self.companyName = companyName
        
        pass
    @property
    def companyName(self):
        return self.__companyName
    @companyName.setter
    def companyName(self, companyName: str):
        self.__companyName = companyName



class Television:

    def __init__(self, companyName: str):
        self.companyName = companyName
        
        pass
    @property
    def companyName(self):
        return self.__companyName
    @companyName.setter
    def companyName(self, companyName: str):
        self.__companyName = companyName



class Home_Entertainment_Devices:

    pass


class HeatAirConditioning:

    def __init__(self, voltage: int):
        self.voltage = voltage
        
        pass
    @property
    def voltage(self):
        return self.__voltage
    @voltage.setter
    def voltage(self, voltage: int):
        self.__voltage = voltage



class Lights:

    def __init__(self, brightness: int):
        self.brightness = brightness
        
        pass
    @property
    def brightness(self):
        return self.__brightness
    @brightness.setter
    def brightness(self, brightness: int):
        self.__brightness = brightness



class Telephone_Answering_machine:

    def __init__(self, number: int):
        self.number = number
        
        pass
    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number



class Camera:

    def __init__(self, panAngle: int, zoomSetting: int):
        self.panAngle = panAngle
        self.zoomSetting = zoomSetting
        
        pass
    @property
    def zoomSetting(self):
        return self.__zoomSetting
    @zoomSetting.setter
    def zoomSetting(self, zoomSetting: int):
        self.__zoomSetting = zoomSetting

    @property
    def panAngle(self):
        return self.__panAngle
    @panAngle.setter
    def panAngle(self, panAngle: int):
        self.__panAngle = panAngle



class Alarm_Signaler:

    def __init__(self, frequency: int):
        self.frequency = frequency
        
        pass
    @property
    def frequency(self):
        return self.__frequency
    @frequency.setter
    def frequency(self, frequency: int):
        self.__frequency = frequency



class Sensor:

    def __init__(self, detectingAnomaly: bool):
        self.detectingAnomaly = detectingAnomaly
        
        pass
    @property
    def detectingAnomaly(self):
        return self.__detectingAnomaly
    @detectingAnomaly.setter
    def detectingAnomaly(self, detectingAnomaly: bool):
        self.__detectingAnomaly = detectingAnomaly



class Automation_System:

    pass


class Device_Configuration:

    def __init__(self, zone: int, activeOnStay: bool, activeOnAway: bool, alarmIfoff: bool):
        self.zone = zone
        self.activeOnStay = activeOnStay
        self.activeOnAway = activeOnAway
        self.alarmIfoff = alarmIfoff
        
        pass
    @property
    def activeOnAway(self):
        return self.__activeOnAway
    @activeOnAway.setter
    def activeOnAway(self, activeOnAway: bool):
        self.__activeOnAway = activeOnAway

    @property
    def alarmIfoff(self):
        return self.__alarmIfoff
    @alarmIfoff.setter
    def alarmIfoff(self, alarmIfoff: bool):
        self.__alarmIfoff = alarmIfoff

    @property
    def zone(self):
        return self.__zone
    @zone.setter
    def zone(self, zone: int):
        self.__zone = zone

    @property
    def activeOnStay(self):
        return self.__activeOnStay
    @activeOnStay.setter
    def activeOnStay(self, activeOnStay: bool):
        self.__activeOnStay = activeOnStay



class securitySystem:

    pass


class config:

    def __init__(self, configurationName: str, activationCode0: "ActivationCode" = None, floorPlan2: "FloorPlan" = None):
        self.configurationName = configurationName
        self.activationCode0 = activationCode0
        self.floorPlan2 = floorPlan2
        
        pass
    @property
    def configurationName(self):
        return self.__configurationName
    @configurationName.setter
    def configurationName(self, configurationName: str):
        self.__configurationName = configurationName

    @property
    def floorPlan2(self):
        return self.__floorPlan2
    @floorPlan2.setter
    def floorPlan2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_config__floorPlan2", None)
        self.__floorPlan2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "config3"):
                opp_val = getattr(old_value, "config3", None)
                if opp_val == self:
                    setattr(old_value, "config3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "config3"):
                opp_val = getattr(value, "config3", None)
                setattr(value, "config3", self)

    @property
    def activationCode0(self):
        return self.__activationCode0
    @activationCode0.setter
    def activationCode0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_config__activationCode0", None)
        self.__activationCode0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "config1"):
                opp_val = getattr(old_value, "config1", None)
                if opp_val == self:
                    setattr(old_value, "config1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "config1"):
                opp_val = getattr(value, "config1", None)
                setattr(value, "config1", self)



class SAFE_HOME_SYSTEM:

    def __init__(self, userId: str, masterPwd: str, streetAddress: str, activationState: str):
        self.userId = userId
        self.masterPwd = masterPwd
        self.streetAddress = streetAddress
        self.activationState = activationState
        
        pass
    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def activationState(self):
        return self.__activationState
    @activationState.setter
    def activationState(self, activationState: str):
        self.__activationState = activationState

    @property
    def streetAddress(self):
        return self.__streetAddress
    @streetAddress.setter
    def streetAddress(self, streetAddress: str):
        self.__streetAddress = streetAddress

    @property
    def masterPwd(self):
        return self.__masterPwd
    @masterPwd.setter
    def masterPwd(self, masterPwd: str):
        self.__masterPwd = masterPwd

