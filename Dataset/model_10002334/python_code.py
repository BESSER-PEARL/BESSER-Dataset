from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class User__SMS_:

    def __init__(self, Status: str):
        self.Status = Status
        
        pass
    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: str):
        self.__Status = Status



class GSM_Module:

    def __init__(self, Status: str, Update: float, CmdMatch: str, microcontroller12: "Microcontroller" = None):
        self.Status = Status
        self.Update = Update
        self.CmdMatch = CmdMatch
        self.microcontroller12 = microcontroller12
        
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
    def Status(self, Status: str):
        self.__Status = Status

    @property
    def CmdMatch(self):
        return self.__CmdMatch
    @CmdMatch.setter
    def CmdMatch(self, CmdMatch: str):
        self.__CmdMatch = CmdMatch

    @property
    def microcontroller12(self):
        return self.__microcontroller12
    @microcontroller12.setter
    def microcontroller12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GSM_Module__microcontroller12", None)
        self.__microcontroller12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gSM_Module13"):
                opp_val = getattr(old_value, "gSM_Module13", None)
                if opp_val == self:
                    setattr(old_value, "gSM_Module13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gSM_Module13"):
                opp_val = getattr(value, "gSM_Module13", None)
                setattr(value, "gSM_Module13", self)



class Fan:

    def __init__(self, FanID: str, light15: "Light" = None):
        self.FanID = FanID
        self.light15 = light15
        
        pass
    @property
    def FanID(self):
        return self.__FanID
    @FanID.setter
    def FanID(self, FanID: str):
        self.__FanID = FanID

    @property
    def light15(self):
        return self.__light15
    @light15.setter
    def light15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Fan__light15", None)
        self.__light15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fan14"):
                opp_val = getattr(old_value, "fan14", None)
                if opp_val == self:
                    setattr(old_value, "fan14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fan14"):
                opp_val = getattr(value, "fan14", None)
                setattr(value, "fan14", self)



class Entertainment_System:

    def __init__(self, DeviceID: int, tV7: set["TV"] = None, speakers9: set["Speakers"] = None, homeTheatre11: set["HomeTheatre"] = None):
        self.DeviceID = DeviceID
        self.tV7 = tV7 if tV7 is not None else set()
        self.speakers9 = speakers9 if speakers9 is not None else set()
        self.homeTheatre11 = homeTheatre11 if homeTheatre11 is not None else set()
        
        pass
    @property
    def DeviceID(self):
        return self.__DeviceID
    @DeviceID.setter
    def DeviceID(self, DeviceID: int):
        self.__DeviceID = DeviceID

    @property
    def speakers9(self):
        return self.__speakers9
    @speakers9.setter
    def speakers9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entertainment_System__speakers9", None)
        self.__speakers9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entertainment8"):
                    opp_val = getattr(item, "entertainment8", None)
                    
                    if opp_val == self:
                        setattr(item, "entertainment8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entertainment8"):
                    opp_val = getattr(item, "entertainment8", None)
                    
                    setattr(item, "entertainment8", self)
                    

    @property
    def homeTheatre11(self):
        return self.__homeTheatre11
    @homeTheatre11.setter
    def homeTheatre11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entertainment_System__homeTheatre11", None)
        self.__homeTheatre11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entertainment10"):
                    opp_val = getattr(item, "entertainment10", None)
                    
                    if opp_val == self:
                        setattr(item, "entertainment10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entertainment10"):
                    opp_val = getattr(item, "entertainment10", None)
                    
                    setattr(item, "entertainment10", self)
                    

    @property
    def tV7(self):
        return self.__tV7
    @tV7.setter
    def tV7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entertainment_System__tV7", None)
        self.__tV7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entertainment6"):
                    opp_val = getattr(item, "entertainment6", None)
                    
                    if opp_val == self:
                        setattr(item, "entertainment6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entertainment6"):
                    opp_val = getattr(item, "entertainment6", None)
                    
                    setattr(item, "entertainment6", self)
                    



class HomeTheatre:

    def __init__(self, HTID: str, tV2: "TV" = None, speakers4: "Speakers" = None, entertainment10: "Entertainment_System" = None):
        self.HTID = HTID
        self.tV2 = tV2
        self.speakers4 = speakers4
        self.entertainment10 = entertainment10
        
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
    def entertainment10(self):
        return self.__entertainment10
    @entertainment10.setter
    def entertainment10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HomeTheatre__entertainment10", None)
        self.__entertainment10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "homeTheatre11"):
                opp_val = getattr(old_value, "homeTheatre11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "homeTheatre11"):
                opp_val = getattr(value, "homeTheatre11", None)
                if opp_val is None:
                    setattr(value, "homeTheatre11", set([self]))
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



class TV:

    def __init__(self, TVID: int, homeTheatre3: set["HomeTheatre"] = None, entertainment6: "Entertainment_System" = None):
        self.TVID = TVID
        self.homeTheatre3 = homeTheatre3 if homeTheatre3 is not None else set()
        self.entertainment6 = entertainment6
        
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
    def entertainment6(self):
        return self.__entertainment6
    @entertainment6.setter
    def entertainment6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TV__entertainment6", None)
        self.__entertainment6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tV7"):
                opp_val = getattr(old_value, "tV7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tV7"):
                opp_val = getattr(value, "tV7", None)
                if opp_val is None:
                    setattr(value, "tV7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Light:

    def __init__(self, LightID: str, fan14: "Fan" = None):
        self.LightID = LightID
        self.fan14 = fan14
        
        pass
    @property
    def LightID(self):
        return self.__LightID
    @LightID.setter
    def LightID(self, LightID: str):
        self.__LightID = LightID

    @property
    def fan14(self):
        return self.__fan14
    @fan14.setter
    def fan14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Light__fan14", None)
        self.__fan14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "light15"):
                opp_val = getattr(old_value, "light15", None)
                if opp_val == self:
                    setattr(old_value, "light15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "light15"):
                opp_val = getattr(value, "light15", None)
                setattr(value, "light15", self)



class Geyser:

    def __init__(self, GeyserID: str):
        self.GeyserID = GeyserID
        
        pass
    @property
    def GeyserID(self):
        return self.__GeyserID
    @GeyserID.setter
    def GeyserID(self, GeyserID: str):
        self.__GeyserID = GeyserID



class Speakers:

    def __init__(self, SpeakerID: int, homeTheatre5: set["HomeTheatre"] = None, entertainment8: "Entertainment_System" = None):
        self.SpeakerID = SpeakerID
        self.homeTheatre5 = homeTheatre5 if homeTheatre5 is not None else set()
        self.entertainment8 = entertainment8
        
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
    def entertainment8(self):
        return self.__entertainment8
    @entertainment8.setter
    def entertainment8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Speakers__entertainment8", None)
        self.__entertainment8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "speakers9"):
                opp_val = getattr(old_value, "speakers9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "speakers9"):
                opp_val = getattr(value, "speakers9", None)
                if opp_val is None:
                    setattr(value, "speakers9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Camera:

    def __init__(self, CameraID: int, door1: "Door" = None):
        self.CameraID = CameraID
        self.door1 = door1
        
        pass
    @property
    def CameraID(self):
        return self.__CameraID
    @CameraID.setter
    def CameraID(self, CameraID: int):
        self.__CameraID = CameraID

    @property
    def door1(self):
        return self.__door1
    @door1.setter
    def door1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Camera__door1", None)
        self.__door1 = value
        
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



class Door:

    def __init__(self, DoorID: int, camera0: set["Camera"] = None):
        self.DoorID = DoorID
        self.camera0 = camera0 if camera0 is not None else set()
        
        pass
    @property
    def DoorID(self):
        return self.__DoorID
    @DoorID.setter
    def DoorID(self, DoorID: int):
        self.__DoorID = DoorID

    @property
    def camera0(self):
        return self.__camera0
    @camera0.setter
    def camera0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Door__camera0", None)
        self.__camera0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "door1"):
                    opp_val = getattr(item, "door1", None)
                    
                    if opp_val == self:
                        setattr(item, "door1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "door1"):
                    opp_val = getattr(item, "door1", None)
                    
                    setattr(item, "door1", self)
                    



class Microcontroller:

    def __init__(self, Status: str, Update: float, gSM_Module13: "GSM_Module" = None):
        self.Status = Status
        self.Update = Update
        self.gSM_Module13 = gSM_Module13
        
        pass
    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: str):
        self.__Status = Status

    @property
    def Update(self):
        return self.__Update
    @Update.setter
    def Update(self, Update: float):
        self.__Update = Update

    @property
    def gSM_Module13(self):
        return self.__gSM_Module13
    @gSM_Module13.setter
    def gSM_Module13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Microcontroller__gSM_Module13", None)
        self.__gSM_Module13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "microcontroller12"):
                opp_val = getattr(old_value, "microcontroller12", None)
                if opp_val == self:
                    setattr(old_value, "microcontroller12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "microcontroller12"):
                opp_val = getattr(value, "microcontroller12", None)
                setattr(value, "microcontroller12", self)

