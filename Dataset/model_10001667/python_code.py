from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class int:

    pass


class UDP_Socket:

    def __init__(self, socket: int):
        self.socket = socket
        
        pass
    @property
    def socket(self):
        return self.__socket
    @socket.setter
    def socket(self, socket: int):
        self.__socket = socket



class UDP_Controller:

    def __init__(self, ip_session: str):
        self.ip_session = ip_session
        
        pass
    @property
    def ip_session(self):
        return self.__ip_session
    @ip_session.setter
    def ip_session(self, ip_session: str):
        self.__ip_session = ip_session



class RFID_Sensor:

    pass


class Employee:

    def __init__(self, EmployeeID: int):
        self.EmployeeID = EmployeeID
        
        pass
    @property
    def EmployeeID(self):
        return self.__EmployeeID
    @EmployeeID.setter
    def EmployeeID(self, EmployeeID: int):
        self.__EmployeeID = EmployeeID



class Display:

    def __init__(self, TimeID: str, Coffee: str, DishWasher: str, Alarm: str, WashingMachine: str, start_Of_Day8: "Start_Of_Day" = None, end_Of_Day10: "End_Of_Day" = None, system17: "Hub_Device" = None):
        self.TimeID = TimeID
        self.Coffee = Coffee
        self.DishWasher = DishWasher
        self.Alarm = Alarm
        self.WashingMachine = WashingMachine
        self.start_Of_Day8 = start_Of_Day8
        self.end_Of_Day10 = end_Of_Day10
        self.system17 = system17
        
        pass
    @property
    def Coffee(self):
        return self.__Coffee
    @Coffee.setter
    def Coffee(self, Coffee: str):
        self.__Coffee = Coffee

    @property
    def Alarm(self):
        return self.__Alarm
    @Alarm.setter
    def Alarm(self, Alarm: str):
        self.__Alarm = Alarm

    @property
    def WashingMachine(self):
        return self.__WashingMachine
    @WashingMachine.setter
    def WashingMachine(self, WashingMachine: str):
        self.__WashingMachine = WashingMachine

    @property
    def TimeID(self):
        return self.__TimeID
    @TimeID.setter
    def TimeID(self, TimeID: str):
        self.__TimeID = TimeID

    @property
    def DishWasher(self):
        return self.__DishWasher
    @DishWasher.setter
    def DishWasher(self, DishWasher: str):
        self.__DishWasher = DishWasher

    @property
    def end_Of_Day10(self):
        return self.__end_Of_Day10
    @end_Of_Day10.setter
    def end_Of_Day10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Display__end_Of_Day10", None)
        self.__end_Of_Day10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "houseHolds11"):
                opp_val = getattr(old_value, "houseHolds11", None)
                if opp_val == self:
                    setattr(old_value, "houseHolds11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "houseHolds11"):
                opp_val = getattr(value, "houseHolds11", None)
                setattr(value, "houseHolds11", self)

    @property
    def start_Of_Day8(self):
        return self.__start_Of_Day8
    @start_Of_Day8.setter
    def start_Of_Day8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Display__start_Of_Day8", None)
        self.__start_Of_Day8 = value
        
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
    def system17(self):
        return self.__system17
    @system17.setter
    def system17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Display__system17", None)
        self.__system17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "houseHolds16"):
                opp_val = getattr(old_value, "houseHolds16", None)
                if opp_val == self:
                    setattr(old_value, "houseHolds16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "houseHolds16"):
                opp_val = getattr(value, "houseHolds16", None)
                setattr(value, "houseHolds16", self)



class Users:

    def __init__(self, HTID: str, tV4: "Admin" = None, speakers6: "Manager" = None, system18: "Hub_Device" = None):
        self.HTID = HTID
        self.tV4 = tV4
        self.speakers6 = speakers6
        self.system18 = system18
        
        pass
    @property
    def HTID(self):
        return self.__HTID
    @HTID.setter
    def HTID(self, HTID: str):
        self.__HTID = HTID

    @property
    def system18(self):
        return self.__system18
    @system18.setter
    def system18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Users__system18", None)
        self.__system18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "homeTheatre19"):
                opp_val = getattr(old_value, "homeTheatre19", None)
                if opp_val == self:
                    setattr(old_value, "homeTheatre19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "homeTheatre19"):
                opp_val = getattr(value, "homeTheatre19", None)
                setattr(value, "homeTheatre19", self)

    @property
    def tV4(self):
        return self.__tV4
    @tV4.setter
    def tV4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Users__tV4", None)
        self.__tV4 = value
        
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
    def speakers6(self):
        return self.__speakers6
    @speakers6.setter
    def speakers6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Users__speakers6", None)
        self.__speakers6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "homeTheatre7"):
                opp_val = getattr(old_value, "homeTheatre7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "homeTheatre7"):
                opp_val = getattr(value, "homeTheatre7", None)
                if opp_val is None:
                    setattr(value, "homeTheatre7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Admin:

    def __init__(self, AdminID: int, homeTheatre5: set["Users"] = None):
        self.AdminID = AdminID
        self.homeTheatre5 = homeTheatre5 if homeTheatre5 is not None else set()
        
        pass
    @property
    def AdminID(self):
        return self.__AdminID
    @AdminID.setter
    def AdminID(self, AdminID: int):
        self.__AdminID = AdminID

    @property
    def homeTheatre5(self):
        return self.__homeTheatre5
    @homeTheatre5.setter
    def homeTheatre5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__homeTheatre5", None)
        self.__homeTheatre5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tV4"):
                    opp_val = getattr(item, "tV4", None)
                    
                    if opp_val == self:
                        setattr(item, "tV4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tV4"):
                    opp_val = getattr(item, "tV4", None)
                    
                    setattr(item, "tV4", self)
                    



class End_Of_Day:

    def __init__(self, EOT: int, houseHolds11: "Display" = None):
        self.EOT = EOT
        self.houseHolds11 = houseHolds11
        
        pass
    @property
    def EOT(self):
        return self.__EOT
    @EOT.setter
    def EOT(self, EOT: int):
        self.__EOT = EOT

    @property
    def houseHolds11(self):
        return self.__houseHolds11
    @houseHolds11.setter
    def houseHolds11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_End_Of_Day__houseHolds11", None)
        self.__houseHolds11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "end_Of_Day10"):
                opp_val = getattr(old_value, "end_Of_Day10", None)
                if opp_val == self:
                    setattr(old_value, "end_Of_Day10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "end_Of_Day10"):
                opp_val = getattr(value, "end_Of_Day10", None)
                setattr(value, "end_Of_Day10", self)



class Start_Of_Day:

    def __init__(self, SOT: int, houseHolds9: "Display" = None):
        self.SOT = SOT
        self.houseHolds9 = houseHolds9
        
        pass
    @property
    def SOT(self):
        return self.__SOT
    @SOT.setter
    def SOT(self, SOT: int):
        self.__SOT = SOT

    @property
    def houseHolds9(self):
        return self.__houseHolds9
    @houseHolds9.setter
    def houseHolds9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Start_Of_Day__houseHolds9", None)
        self.__houseHolds9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "start_Of_Day8"):
                opp_val = getattr(old_value, "start_Of_Day8", None)
                if opp_val == self:
                    setattr(old_value, "start_Of_Day8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "start_Of_Day8"):
                opp_val = getattr(value, "start_Of_Day8", None)
                setattr(value, "start_Of_Day8", self)



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



class Manager:

    def __init__(self, MangagerID: int, homeTheatre7: set["Users"] = None):
        self.MangagerID = MangagerID
        self.homeTheatre7 = homeTheatre7 if homeTheatre7 is not None else set()
        
        pass
    @property
    def MangagerID(self):
        return self.__MangagerID
    @MangagerID.setter
    def MangagerID(self, MangagerID: int):
        self.__MangagerID = MangagerID

    @property
    def homeTheatre7(self):
        return self.__homeTheatre7
    @homeTheatre7.setter
    def homeTheatre7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manager__homeTheatre7", None)
        self.__homeTheatre7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "speakers6"):
                    opp_val = getattr(item, "speakers6", None)
                    
                    if opp_val == self:
                        setattr(item, "speakers6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "speakers6"):
                    opp_val = getattr(item, "speakers6", None)
                    
                    setattr(item, "speakers6", self)
                    



class Camera:

    def __init__(self, CameraID: int, door3: "Door" = None):
        self.CameraID = CameraID
        self.door3 = door3
        
        pass
    @property
    def CameraID(self):
        return self.__CameraID
    @CameraID.setter
    def CameraID(self, CameraID: int):
        self.__CameraID = CameraID

    @property
    def door3(self):
        return self.__door3
    @door3.setter
    def door3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Camera__door3", None)
        self.__door3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "camera2"):
                opp_val = getattr(old_value, "camera2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "camera2"):
                opp_val = getattr(value, "camera2", None)
                if opp_val is None:
                    setattr(value, "camera2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Door:

    def __init__(self, DoorID: int, sensor1: "Sensor" = None, camera2: set["Camera"] = None):
        self.DoorID = DoorID
        self.sensor1 = sensor1
        self.camera2 = camera2 if camera2 is not None else set()
        
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

    @property
    def camera2(self):
        return self.__camera2
    @camera2.setter
    def camera2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Door__camera2", None)
        self.__camera2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "door3"):
                    opp_val = getattr(item, "door3", None)
                    
                    if opp_val == self:
                        setattr(item, "door3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "door3"):
                    opp_val = getattr(item, "door3", None)
                    
                    setattr(item, "door3", self)
                    



class Alert:

    def __init__(self, AlertID: int, home_Security_System13: "Home_Security_System" = None):
        self.AlertID = AlertID
        self.home_Security_System13 = home_Security_System13
        
        pass
    @property
    def AlertID(self):
        return self.__AlertID
    @AlertID.setter
    def AlertID(self, AlertID: int):
        self.__AlertID = AlertID

    @property
    def home_Security_System13(self):
        return self.__home_Security_System13
    @home_Security_System13.setter
    def home_Security_System13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Alert__home_Security_System13", None)
        self.__home_Security_System13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alert12"):
                opp_val = getattr(old_value, "alert12", None)
                if opp_val == self:
                    setattr(old_value, "alert12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alert12"):
                opp_val = getattr(value, "alert12", None)
                setattr(value, "alert12", self)



class Home_Security_System:

    def __init__(self, UserID: int, alert12: "Alert" = None, system20: "Hub_Device" = None):
        self.UserID = UserID
        self.alert12 = alert12
        self.system20 = system20
        
        pass
    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: int):
        self.__UserID = UserID

    @property
    def alert12(self):
        return self.__alert12
    @alert12.setter
    def alert12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Home_Security_System__alert12", None)
        self.__alert12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "home_Security_System13"):
                opp_val = getattr(old_value, "home_Security_System13", None)
                if opp_val == self:
                    setattr(old_value, "home_Security_System13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "home_Security_System13"):
                opp_val = getattr(value, "home_Security_System13", None)
                setattr(value, "home_Security_System13", self)

    @property
    def system20(self):
        return self.__system20
    @system20.setter
    def system20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Home_Security_System__system20", None)
        self.__system20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "home_Security_System21"):
                opp_val = getattr(old_value, "home_Security_System21", None)
                if opp_val == self:
                    setattr(old_value, "home_Security_System21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "home_Security_System21"):
                opp_val = getattr(value, "home_Security_System21", None)
                setattr(value, "home_Security_System21", self)



class PressureSensor:

    pass


class Motion_Sensor:

    pass


class Sensor:

    def __init__(self, SensorID: int, SensorType: int, door0: "Door" = None, system14: "Hub_Device" = None):
        self.SensorID = SensorID
        self.SensorType = SensorType
        self.door0 = door0
        self.system14 = system14
        
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
    def system14(self):
        return self.__system14
    @system14.setter
    def system14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sensor__system14", None)
        self.__system14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sensor15"):
                opp_val = getattr(old_value, "sensor15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sensor15"):
                opp_val = getattr(value, "sensor15", None)
                if opp_val is None:
                    setattr(value, "sensor15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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



class Hub_Device:

    def __init__(self, Status: bool, Update: float, sensor15: set["Sensor"] = None, houseHolds16: "Display" = None, homeTheatre19: "Users" = None, home_Security_System21: "Home_Security_System" = None):
        self.Status = Status
        self.Update = Update
        self.sensor15 = sensor15 if sensor15 is not None else set()
        self.houseHolds16 = houseHolds16
        self.homeTheatre19 = homeTheatre19
        self.home_Security_System21 = home_Security_System21
        
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
    def sensor15(self):
        return self.__sensor15
    @sensor15.setter
    def sensor15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hub_Device__sensor15", None)
        self.__sensor15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "system14"):
                    opp_val = getattr(item, "system14", None)
                    
                    if opp_val == self:
                        setattr(item, "system14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "system14"):
                    opp_val = getattr(item, "system14", None)
                    
                    setattr(item, "system14", self)
                    

    @property
    def homeTheatre19(self):
        return self.__homeTheatre19
    @homeTheatre19.setter
    def homeTheatre19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hub_Device__homeTheatre19", None)
        self.__homeTheatre19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system18"):
                opp_val = getattr(old_value, "system18", None)
                if opp_val == self:
                    setattr(old_value, "system18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system18"):
                opp_val = getattr(value, "system18", None)
                setattr(value, "system18", self)

    @property
    def home_Security_System21(self):
        return self.__home_Security_System21
    @home_Security_System21.setter
    def home_Security_System21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hub_Device__home_Security_System21", None)
        self.__home_Security_System21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system20"):
                opp_val = getattr(old_value, "system20", None)
                if opp_val == self:
                    setattr(old_value, "system20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system20"):
                opp_val = getattr(value, "system20", None)
                setattr(value, "system20", self)

    @property
    def houseHolds16(self):
        return self.__houseHolds16
    @houseHolds16.setter
    def houseHolds16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hub_Device__houseHolds16", None)
        self.__houseHolds16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system17"):
                opp_val = getattr(old_value, "system17", None)
                if opp_val == self:
                    setattr(old_value, "system17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system17"):
                opp_val = getattr(value, "system17", None)
                setattr(value, "system17", self)

