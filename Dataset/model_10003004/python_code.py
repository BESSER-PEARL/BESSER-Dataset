from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Gateway_01_Interface:

    pass


class Gateway2_Interface:

    pass


class MQTT_Broker:

    def __init__(self, DeviceID: int, Publish: str, Subscribe: str):
        self.DeviceID = DeviceID
        self.Publish = Publish
        self.Subscribe = Subscribe
        
        pass
    @property
    def DeviceID(self):
        return self.__DeviceID
    @DeviceID.setter
    def DeviceID(self, DeviceID: int):
        self.__DeviceID = DeviceID

    @property
    def Publish(self):
        return self.__Publish
    @Publish.setter
    def Publish(self, Publish: str):
        self.__Publish = Publish

    @property
    def Subscribe(self):
        return self.__Subscribe
    @Subscribe.setter
    def Subscribe(self, Subscribe: str):
        self.__Subscribe = Subscribe



class FactoryHolds:

    def __init__(self, Time: float, Control_panel: str, Alarm: str, Conveyor1: str, Conveyor2: str, system5: "Gateway" = None):
        self.Time = Time
        self.Control_panel = Control_panel
        self.Alarm = Alarm
        self.Conveyor1 = Conveyor1
        self.Conveyor2 = Conveyor2
        self.system5 = system5
        
        pass
    @property
    def Conveyor1(self):
        return self.__Conveyor1
    @Conveyor1.setter
    def Conveyor1(self, Conveyor1: str):
        self.__Conveyor1 = Conveyor1

    @property
    def Alarm(self):
        return self.__Alarm
    @Alarm.setter
    def Alarm(self, Alarm: str):
        self.__Alarm = Alarm

    @property
    def Control_panel(self):
        return self.__Control_panel
    @Control_panel.setter
    def Control_panel(self, Control_panel: str):
        self.__Control_panel = Control_panel

    @property
    def Conveyor2(self):
        return self.__Conveyor2
    @Conveyor2.setter
    def Conveyor2(self, Conveyor2: str):
        self.__Conveyor2 = Conveyor2

    @property
    def Time(self):
        return self.__Time
    @Time.setter
    def Time(self, Time: float):
        self.__Time = Time

    @property
    def system5(self):
        return self.__system5
    @system5.setter
    def system5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FactoryHolds__system5", None)
        self.__system5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "houseHolds4"):
                opp_val = getattr(old_value, "houseHolds4", None)
                if opp_val == self:
                    setattr(old_value, "houseHolds4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "houseHolds4"):
                opp_val = getattr(value, "houseHolds4", None)
                setattr(value, "houseHolds4", self)



class UPS_SNMP:

    def __init__(self, IP: str):
        self.IP = IP
        
        pass
    @property
    def IP(self):
        return self.__IP
    @IP.setter
    def IP(self, IP: str):
        self.__IP = IP



class OPC_UA:

    def __init__(self, PC_ID: int):
        self.PC_ID = PC_ID
        
        pass
    @property
    def PC_ID(self):
        return self.__PC_ID
    @PC_ID.setter
    def PC_ID(self, PC_ID: int):
        self.__PC_ID = PC_ID



class End_Of_Day:

    def __init__(self, EOT: int, gateway10: "Gateway" = None):
        self.EOT = EOT
        self.gateway10 = gateway10
        
        pass
    @property
    def EOT(self):
        return self.__EOT
    @EOT.setter
    def EOT(self, EOT: int):
        self.__EOT = EOT

    @property
    def gateway10(self):
        return self.__gateway10
    @gateway10.setter
    def gateway10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_End_Of_Day__gateway10", None)
        self.__gateway10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "end_Of_Day11"):
                opp_val = getattr(old_value, "end_Of_Day11", None)
                if opp_val == self:
                    setattr(old_value, "end_Of_Day11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "end_Of_Day11"):
                opp_val = getattr(value, "end_Of_Day11", None)
                setattr(value, "end_Of_Day11", self)



class Start_Of_Day:

    def __init__(self, SOT: int, gateway8: "Gateway" = None):
        self.SOT = SOT
        self.gateway8 = gateway8
        
        pass
    @property
    def SOT(self):
        return self.__SOT
    @SOT.setter
    def SOT(self, SOT: int):
        self.__SOT = SOT

    @property
    def gateway8(self):
        return self.__gateway8
    @gateway8.setter
    def gateway8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Start_Of_Day__gateway8", None)
        self.__gateway8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "start_Of_Day9"):
                opp_val = getattr(old_value, "start_Of_Day9", None)
                if opp_val == self:
                    setattr(old_value, "start_Of_Day9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "start_Of_Day9"):
                opp_val = getattr(value, "start_Of_Day9", None)
                setattr(value, "start_Of_Day9", self)



class Modbus_Meter:

    def __init__(self, MAC_ID: int):
        self.MAC_ID = MAC_ID
        
        pass
    @property
    def MAC_ID(self):
        return self.__MAC_ID
    @MAC_ID.setter
    def MAC_ID(self, MAC_ID: int):
        self.__MAC_ID = MAC_ID



class Door_relay:

    def __init__(self, DoorID: int, DoorOpen: str):
        self.DoorID = DoorID
        self.DoorOpen = DoorOpen
        
        pass
    @property
    def DoorOpen(self):
        return self.__DoorOpen
    @DoorOpen.setter
    def DoorOpen(self, DoorOpen: str):
        self.__DoorOpen = DoorOpen

    @property
    def DoorID(self):
        return self.__DoorID
    @DoorID.setter
    def DoorID(self, DoorID: int):
        self.__DoorID = DoorID



class Alert:

    def __init__(self, AlertID: int, home_Security_System1: "Factory_Security_System" = None):
        self.AlertID = AlertID
        self.home_Security_System1 = home_Security_System1
        
        pass
    @property
    def AlertID(self):
        return self.__AlertID
    @AlertID.setter
    def AlertID(self, AlertID: int):
        self.__AlertID = AlertID

    @property
    def home_Security_System1(self):
        return self.__home_Security_System1
    @home_Security_System1.setter
    def home_Security_System1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Alert__home_Security_System1", None)
        self.__home_Security_System1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alert0"):
                opp_val = getattr(old_value, "alert0", None)
                if opp_val == self:
                    setattr(old_value, "alert0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alert0"):
                opp_val = getattr(value, "alert0", None)
                setattr(value, "alert0", self)



class Factory_Security_System:

    def __init__(self, UserID: int, alert0: "Alert" = None, system6: "Gateway" = None):
        self.UserID = UserID
        self.alert0 = alert0
        self.system6 = system6
        
        pass
    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: int):
        self.__UserID = UserID

    @property
    def system6(self):
        return self.__system6
    @system6.setter
    def system6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Factory_Security_System__system6", None)
        self.__system6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Factory_Security_System7"):
                opp_val = getattr(old_value, "Factory_Security_System7", None)
                if opp_val == self:
                    setattr(old_value, "Factory_Security_System7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Factory_Security_System7"):
                opp_val = getattr(value, "Factory_Security_System7", None)
                setattr(value, "Factory_Security_System7", self)

    @property
    def alert0(self):
        return self.__alert0
    @alert0.setter
    def alert0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Factory_Security_System__alert0", None)
        self.__alert0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "home_Security_System1"):
                opp_val = getattr(old_value, "home_Security_System1", None)
                if opp_val == self:
                    setattr(old_value, "home_Security_System1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "home_Security_System1"):
                opp_val = getattr(value, "home_Security_System1", None)
                setattr(value, "home_Security_System1", self)



class FireAlarm_Sensor:

    def __init__(self, SmokeAlarm: bool, DispenseSprinkler: bool):
        self.SmokeAlarm = SmokeAlarm
        self.DispenseSprinkler = DispenseSprinkler
        
        pass
    @property
    def SmokeAlarm(self):
        return self.__SmokeAlarm
    @SmokeAlarm.setter
    def SmokeAlarm(self, SmokeAlarm: bool):
        self.__SmokeAlarm = SmokeAlarm

    @property
    def DispenseSprinkler(self):
        return self.__DispenseSprinkler
    @DispenseSprinkler.setter
    def DispenseSprinkler(self, DispenseSprinkler: bool):
        self.__DispenseSprinkler = DispenseSprinkler



class Sensor:

    def __init__(self, SensorID: int, SensorType: int, system2: "Gateway" = None):
        self.SensorID = SensorID
        self.SensorType = SensorType
        self.system2 = system2
        
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
    def system2(self):
        return self.__system2
    @system2.setter
    def system2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sensor__system2", None)
        self.__system2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sensor3"):
                opp_val = getattr(old_value, "sensor3", None)
                if opp_val == self:
                    setattr(old_value, "sensor3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sensor3"):
                opp_val = getattr(value, "sensor3", None)
                setattr(value, "sensor3", self)



class Datalog:

    pass


class Alarm:

    pass


class Gateway:

    def __init__(self, Status: Gateway_01_Interface, Update: float, WebPLC_configure: Gateway_01_Interface, houseHolds4: "FactoryHolds" = None, Factory_Security_System7: "Factory_Security_System" = None, start_Of_Day9: "Start_Of_Day" = None, end_Of_Day11: "End_Of_Day" = None, sensor3: "Sensor" = None):
        self.Status = Status
        self.Update = Update
        self.WebPLC_configure = WebPLC_configure
        self.houseHolds4 = houseHolds4
        self.Factory_Security_System7 = Factory_Security_System7
        self.start_Of_Day9 = start_Of_Day9
        self.end_Of_Day11 = end_Of_Day11
        self.sensor3 = sensor3
        
        pass
    @property
    def WebPLC_configure(self):
        return self.__WebPLC_configure
    @WebPLC_configure.setter
    def WebPLC_configure(self, WebPLC_configure: Gateway_01_Interface):
        self.__WebPLC_configure = WebPLC_configure

    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: Gateway_01_Interface):
        self.__Status = Status

    @property
    def Update(self):
        return self.__Update
    @Update.setter
    def Update(self, Update: float):
        self.__Update = Update

    @property
    def end_Of_Day11(self):
        return self.__end_Of_Day11
    @end_Of_Day11.setter
    def end_Of_Day11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Gateway__end_Of_Day11", None)
        self.__end_Of_Day11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gateway10"):
                opp_val = getattr(old_value, "gateway10", None)
                if opp_val == self:
                    setattr(old_value, "gateway10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gateway10"):
                opp_val = getattr(value, "gateway10", None)
                setattr(value, "gateway10", self)

    @property
    def Factory_Security_System7(self):
        return self.__Factory_Security_System7
    @Factory_Security_System7.setter
    def Factory_Security_System7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Gateway__Factory_Security_System7", None)
        self.__Factory_Security_System7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system6"):
                opp_val = getattr(old_value, "system6", None)
                if opp_val == self:
                    setattr(old_value, "system6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system6"):
                opp_val = getattr(value, "system6", None)
                setattr(value, "system6", self)

    @property
    def sensor3(self):
        return self.__sensor3
    @sensor3.setter
    def sensor3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Gateway__sensor3", None)
        self.__sensor3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system2"):
                opp_val = getattr(old_value, "system2", None)
                if opp_val == self:
                    setattr(old_value, "system2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system2"):
                opp_val = getattr(value, "system2", None)
                setattr(value, "system2", self)

    @property
    def start_Of_Day9(self):
        return self.__start_Of_Day9
    @start_Of_Day9.setter
    def start_Of_Day9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Gateway__start_Of_Day9", None)
        self.__start_Of_Day9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gateway8"):
                opp_val = getattr(old_value, "gateway8", None)
                if opp_val == self:
                    setattr(old_value, "gateway8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gateway8"):
                opp_val = getattr(value, "gateway8", None)
                setattr(value, "gateway8", self)

    @property
    def houseHolds4(self):
        return self.__houseHolds4
    @houseHolds4.setter
    def houseHolds4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Gateway__houseHolds4", None)
        self.__houseHolds4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system5"):
                opp_val = getattr(old_value, "system5", None)
                if opp_val == self:
                    setattr(old_value, "system5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system5"):
                opp_val = getattr(value, "system5", None)
                setattr(value, "system5", self)

