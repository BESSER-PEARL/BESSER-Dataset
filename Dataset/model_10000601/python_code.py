from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Microcontroller:

    def __init__(self, sendData__: str, sensor23: "Sensor" = None, houseHolds24: "HouseHolds" = None, system26: "System" = None):
        self.sendData__ = sendData__
        self.sensor23 = sensor23
        self.houseHolds24 = houseHolds24
        self.system26 = system26
        
        pass
    @property
    def sendData__(self):
        return self.__sendData__
    @sendData__.setter
    def sendData__(self, sendData__: str):
        self.__sendData__ = sendData__

    @property
    def sensor23(self):
        return self.__sensor23
    @sensor23.setter
    def sensor23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Microcontroller__sensor23", None)
        self.__sensor23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "microcontroller22"):
                opp_val = getattr(old_value, "microcontroller22", None)
                if opp_val == self:
                    setattr(old_value, "microcontroller22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "microcontroller22"):
                opp_val = getattr(value, "microcontroller22", None)
                setattr(value, "microcontroller22", self)

    @property
    def system26(self):
        return self.__system26
    @system26.setter
    def system26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Microcontroller__system26", None)
        self.__system26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "microcontroller27"):
                opp_val = getattr(old_value, "microcontroller27", None)
                if opp_val == self:
                    setattr(old_value, "microcontroller27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "microcontroller27"):
                opp_val = getattr(value, "microcontroller27", None)
                setattr(value, "microcontroller27", self)

    @property
    def houseHolds24(self):
        return self.__houseHolds24
    @houseHolds24.setter
    def houseHolds24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Microcontroller__houseHolds24", None)
        self.__houseHolds24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "microcontroller25"):
                opp_val = getattr(old_value, "microcontroller25", None)
                if opp_val == self:
                    setattr(old_value, "microcontroller25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "microcontroller25"):
                opp_val = getattr(value, "microcontroller25", None)
                setattr(value, "microcontroller25", self)



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
                    



class HouseHolds:

    def __init__(self, TimeID: str, Fan: str, Computer: str, Light: str, microcontroller25: "Microcontroller" = None, start_Of_Day6: "Start_Of_Day" = None, end_Of_Day8: "End_Of_Day" = None, system13: "System" = None):
        self.TimeID = TimeID
        self.Fan = Fan
        self.Computer = Computer
        self.Light = Light
        self.microcontroller25 = microcontroller25
        self.start_Of_Day6 = start_Of_Day6
        self.end_Of_Day8 = end_Of_Day8
        self.system13 = system13
        
        pass
    @property
    def Fan(self):
        return self.__Fan
    @Fan.setter
    def Fan(self, Fan: str):
        self.__Fan = Fan

    @property
    def TimeID(self):
        return self.__TimeID
    @TimeID.setter
    def TimeID(self, TimeID: str):
        self.__TimeID = TimeID

    @property
    def Light(self):
        return self.__Light
    @Light.setter
    def Light(self, Light: str):
        self.__Light = Light

    @property
    def Computer(self):
        return self.__Computer
    @Computer.setter
    def Computer(self, Computer: str):
        self.__Computer = Computer

    @property
    def system13(self):
        return self.__system13
    @system13.setter
    def system13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HouseHolds__system13", None)
        self.__system13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "houseHolds12"):
                opp_val = getattr(old_value, "houseHolds12", None)
                if opp_val == self:
                    setattr(old_value, "houseHolds12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "houseHolds12"):
                opp_val = getattr(value, "houseHolds12", None)
                setattr(value, "houseHolds12", self)

    @property
    def end_Of_Day8(self):
        return self.__end_Of_Day8
    @end_Of_Day8.setter
    def end_Of_Day8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HouseHolds__end_Of_Day8", None)
        self.__end_Of_Day8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "houseHolds9"):
                opp_val = getattr(old_value, "houseHolds9", None)
                if opp_val == self:
                    setattr(old_value, "houseHolds9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "houseHolds9"):
                opp_val = getattr(value, "houseHolds9", None)
                setattr(value, "houseHolds9", self)

    @property
    def microcontroller25(self):
        return self.__microcontroller25
    @microcontroller25.setter
    def microcontroller25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HouseHolds__microcontroller25", None)
        self.__microcontroller25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "houseHolds24"):
                opp_val = getattr(old_value, "houseHolds24", None)
                if opp_val == self:
                    setattr(old_value, "houseHolds24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "houseHolds24"):
                opp_val = getattr(value, "houseHolds24", None)
                setattr(value, "houseHolds24", self)

    @property
    def start_Of_Day6(self):
        return self.__start_Of_Day6
    @start_Of_Day6.setter
    def start_Of_Day6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HouseHolds__start_Of_Day6", None)
        self.__start_Of_Day6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "houseHolds7"):
                opp_val = getattr(old_value, "houseHolds7", None)
                if opp_val == self:
                    setattr(old_value, "houseHolds7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "houseHolds7"):
                opp_val = getattr(value, "houseHolds7", None)
                setattr(value, "houseHolds7", self)



class HomeTheatre:

    def __init__(self, HTID: str, system14: "System" = None, entertainment20: "Entertainment" = None, tV2: "TV" = None, speakers4: "Speakers" = None):
        self.HTID = HTID
        self.system14 = system14
        self.entertainment20 = entertainment20
        self.tV2 = tV2
        self.speakers4 = speakers4
        
        pass
    @property
    def HTID(self):
        return self.__HTID
    @HTID.setter
    def HTID(self, HTID: str):
        self.__HTID = HTID

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

    @property
    def system14(self):
        return self.__system14
    @system14.setter
    def system14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HomeTheatre__system14", None)
        self.__system14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "homeTheatre15"):
                opp_val = getattr(old_value, "homeTheatre15", None)
                if opp_val == self:
                    setattr(old_value, "homeTheatre15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "homeTheatre15"):
                opp_val = getattr(value, "homeTheatre15", None)
                setattr(value, "homeTheatre15", self)

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
                    



class End_Of_Day:

    def __init__(self, EOT: int, houseHolds9: "HouseHolds" = None):
        self.EOT = EOT
        self.houseHolds9 = houseHolds9
        
        pass
    @property
    def EOT(self):
        return self.__EOT
    @EOT.setter
    def EOT(self, EOT: int):
        self.__EOT = EOT

    @property
    def houseHolds9(self):
        return self.__houseHolds9
    @houseHolds9.setter
    def houseHolds9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_End_Of_Day__houseHolds9", None)
        self.__houseHolds9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "end_Of_Day8"):
                opp_val = getattr(old_value, "end_Of_Day8", None)
                if opp_val == self:
                    setattr(old_value, "end_Of_Day8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "end_Of_Day8"):
                opp_val = getattr(value, "end_Of_Day8", None)
                setattr(value, "end_Of_Day8", self)



class Start_Of_Day:

    def __init__(self, SOT: int, houseHolds7: "HouseHolds" = None):
        self.SOT = SOT
        self.houseHolds7 = houseHolds7
        
        pass
    @property
    def SOT(self):
        return self.__SOT
    @SOT.setter
    def SOT(self, SOT: int):
        self.__SOT = SOT

    @property
    def houseHolds7(self):
        return self.__houseHolds7
    @houseHolds7.setter
    def houseHolds7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Start_Of_Day__houseHolds7", None)
        self.__houseHolds7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "start_Of_Day6"):
                opp_val = getattr(old_value, "start_Of_Day6", None)
                if opp_val == self:
                    setattr(old_value, "start_Of_Day6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "start_Of_Day6"):
                opp_val = getattr(value, "start_Of_Day6", None)
                setattr(value, "start_Of_Day6", self)



class Light:

    def __init__(self, LightID: str):
        self.LightID = LightID
        
        pass
    @property
    def LightID(self):
        return self.__LightID
    @LightID.setter
    def LightID(self, LightID: str):
        self.__LightID = LightID



class MicroPhone:

    def __init__(self, MicID: str, system10: "System" = None):
        self.MicID = MicID
        self.system10 = system10
        
        pass
    @property
    def MicID(self):
        return self.__MicID
    @MicID.setter
    def MicID(self, MicID: str):
        self.__MicID = MicID

    @property
    def system10(self):
        return self.__system10
    @system10.setter
    def system10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicroPhone__system10", None)
        self.__system10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "microPhone11"):
                opp_val = getattr(old_value, "microPhone11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "microPhone11"):
                opp_val = getattr(value, "microPhone11", None)
                if opp_val is None:
                    setattr(value, "microPhone11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Speakers:

    def __init__(self, SpeakerID: int, entertainment18: "Entertainment" = None, homeTheatre5: set["HomeTheatre"] = None):
        self.SpeakerID = SpeakerID
        self.entertainment18 = entertainment18
        self.homeTheatre5 = homeTheatre5 if homeTheatre5 is not None else set()
        
        pass
    @property
    def SpeakerID(self):
        return self.__SpeakerID
    @SpeakerID.setter
    def SpeakerID(self, SpeakerID: int):
        self.__SpeakerID = SpeakerID

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



class Camera:

    def __init__(self, CameraID: int):
        self.CameraID = CameraID
        
        pass
    @property
    def CameraID(self):
        return self.__CameraID
    @CameraID.setter
    def CameraID(self, CameraID: int):
        self.__CameraID = CameraID



class Door:

    def __init__(self, DoorID: int, sensor1: "Sensor" = None):
        self.DoorID = DoorID
        self.sensor1 = sensor1
        
        pass
    @property
    def DoorID(self):
        return self.__DoorID
    @DoorID.setter
    def DoorID(self, DoorID: int):
        self.__DoorID = DoorID

    @property
    def sensor1(self):
        return self.__sensor1
    @sensor1.setter
    def sensor1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Door__sensor1", None)
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



class PressureSensor:

    pass


class Motion_Sensor:

    pass


class Light_Sensor:

    def __init__(self, DetectLight__: int):
        self.DetectLight__ = DetectLight__
        
        pass
    @property
    def DetectLight__(self):
        return self.__DetectLight__
    @DetectLight__.setter
    def DetectLight__(self, DetectLight__: int):
        self.__DetectLight__ = DetectLight__



class Sensor:

    def __init__(self, SensorID: int, SensorType: int, microcontroller22: "Microcontroller" = None, door0: "Door" = None):
        self.SensorID = SensorID
        self.SensorType = SensorType
        self.microcontroller22 = microcontroller22
        self.door0 = door0
        
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
    def microcontroller22(self):
        return self.__microcontroller22
    @microcontroller22.setter
    def microcontroller22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sensor__microcontroller22", None)
        self.__microcontroller22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sensor23"):
                opp_val = getattr(old_value, "sensor23", None)
                if opp_val == self:
                    setattr(old_value, "sensor23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sensor23"):
                opp_val = getattr(value, "sensor23", None)
                setattr(value, "sensor23", self)

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



class System:

    def __init__(self, Status: bool, Update: float, homeTheatre15: "HomeTheatre" = None, microPhone11: set["MicroPhone"] = None, houseHolds12: "HouseHolds" = None, microcontroller27: "Microcontroller" = None):
        self.Status = Status
        self.Update = Update
        self.homeTheatre15 = homeTheatre15
        self.microPhone11 = microPhone11 if microPhone11 is not None else set()
        self.houseHolds12 = houseHolds12
        self.microcontroller27 = microcontroller27
        
        pass
    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: bool):
        self.__Status = Status

    @property
    def Update(self):
        return self.__Update
    @Update.setter
    def Update(self, Update: float):
        self.__Update = Update

    @property
    def microcontroller27(self):
        return self.__microcontroller27
    @microcontroller27.setter
    def microcontroller27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__microcontroller27", None)
        self.__microcontroller27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system26"):
                opp_val = getattr(old_value, "system26", None)
                if opp_val == self:
                    setattr(old_value, "system26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system26"):
                opp_val = getattr(value, "system26", None)
                setattr(value, "system26", self)

    @property
    def houseHolds12(self):
        return self.__houseHolds12
    @houseHolds12.setter
    def houseHolds12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__houseHolds12", None)
        self.__houseHolds12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system13"):
                opp_val = getattr(old_value, "system13", None)
                if opp_val == self:
                    setattr(old_value, "system13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system13"):
                opp_val = getattr(value, "system13", None)
                setattr(value, "system13", self)

    @property
    def homeTheatre15(self):
        return self.__homeTheatre15
    @homeTheatre15.setter
    def homeTheatre15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__homeTheatre15", None)
        self.__homeTheatre15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system14"):
                opp_val = getattr(old_value, "system14", None)
                if opp_val == self:
                    setattr(old_value, "system14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system14"):
                opp_val = getattr(value, "system14", None)
                setattr(value, "system14", self)

    @property
    def microPhone11(self):
        return self.__microPhone11
    @microPhone11.setter
    def microPhone11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__microPhone11", None)
        self.__microPhone11 = value if value is not None else set()
        
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
                    

