from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ConnectionKind(Enum):
    STATE_FLOW = "STATE_FLOW"
    OUTSIDE_FLOW = "OUTSIDE_FLOW"
class I2CLCDType(Enum):
    I2CLCD2004 = "I2CLCD2004"
    I2CLCD1602 = "I2CLCD1602"
class RouterKind(Enum):
    BENDPOINT = "BENDPOINT"
    MANHATTAN = "MANHATTAN"
class WifiMode(Enum):
    Station = "Station"
    Access_Point = "Access_Point"
    Both = "Both"
class ListBaud(Enum):
    baud_9600 = "baud_9600"
    baud_19200 = "baud_19200"
    baud_38400 = "baud_38400"
    baud_57600 = "baud_57600"
    baud_74880 = "baud_74880"
    baud_115200 = "baud_115200"
    baud_230400 = "baud_230400"
    baud_250000 = "baud_250000"
class WifiIDConnection(Enum):
    id_0 = "id_0"
    id_1 = "id_1"
    id_2 = "id_2"
    id_3 = "id_3"
    id_4 = "id_4"
class ListProtocol(Enum):
    TCP = "TCP"
    UDP = "UDP"
class ListConnectionChannel(Enum):
    Single = "Single"
    Multiple = "Multiple"


############################################
# Definition of Classes
############################################

class StateComponent:

    pass
class iotw_StartPoint(StateComponent):

    pass
class iotw_EndPoint(StateComponent):

    pass
class iotw_Decision(StateComponent):

    pass
class iotw_StateFrame(StateComponent):

    def __init__(self, content: str):
        self.content = content
        
        pass
    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content


class Connectivity:

    pass
class iotw_WifiESP8266(Connectivity):

    def __init__(self, pinTX: str, pinRX: str, pinVcc: str, pinGND: str, pinCHPD: str, sSID_ST: str, password_ST: str, mode: str, idConnection: str, password_AccessPoint: str, sSID_AccessPoint: str, port: int, iP: str, baud: str, connectedChannel: str, protocol: str):
        self.pinTX = pinTX
        self.pinRX = pinRX
        self.pinVcc = pinVcc
        self.pinGND = pinGND
        self.pinCHPD = pinCHPD
        self.sSID_ST = sSID_ST
        self.password_ST = password_ST
        self.mode = mode
        self.idConnection = idConnection
        self.password_AccessPoint = password_AccessPoint
        self.sSID_AccessPoint = sSID_AccessPoint
        self.port = port
        self.iP = iP
        self.baud = baud
        self.connectedChannel = connectedChannel
        self.protocol = protocol
        
        pass
    @property
    def sSID_AccessPoint(self):
        return self.__sSID_AccessPoint

    @sSID_AccessPoint.setter
    def sSID_AccessPoint(self, sSID_AccessPoint: str):
        self.__sSID_AccessPoint = sSID_AccessPoint


    @property
    def idConnection(self):
        return self.__idConnection

    @idConnection.setter
    def idConnection(self, idConnection: str):
        self.__idConnection = idConnection


    @property
    def baud(self):
        return self.__baud

    @baud.setter
    def baud(self, baud: str):
        self.__baud = baud


    @property
    def connectedChannel(self):
        return self.__connectedChannel

    @connectedChannel.setter
    def connectedChannel(self, connectedChannel: str):
        self.__connectedChannel = connectedChannel


    @property
    def pinVcc(self):
        return self.__pinVcc

    @pinVcc.setter
    def pinVcc(self, pinVcc: str):
        self.__pinVcc = pinVcc


    @property
    def sSID_ST(self):
        return self.__sSID_ST

    @sSID_ST.setter
    def sSID_ST(self, sSID_ST: str):
        self.__sSID_ST = sSID_ST


    @property
    def pinGND(self):
        return self.__pinGND

    @pinGND.setter
    def pinGND(self, pinGND: str):
        self.__pinGND = pinGND


    @property
    def password_ST(self):
        return self.__password_ST

    @password_ST.setter
    def password_ST(self, password_ST: str):
        self.__password_ST = password_ST


    @property
    def pinRX(self):
        return self.__pinRX

    @pinRX.setter
    def pinRX(self, pinRX: str):
        self.__pinRX = pinRX


    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port: int):
        self.__port = port


    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode


    @property
    def pinCHPD(self):
        return self.__pinCHPD

    @pinCHPD.setter
    def pinCHPD(self, pinCHPD: str):
        self.__pinCHPD = pinCHPD


    @property
    def iP(self):
        return self.__iP

    @iP.setter
    def iP(self, iP: str):
        self.__iP = iP


    @property
    def protocol(self):
        return self.__protocol

    @protocol.setter
    def protocol(self, protocol: str):
        self.__protocol = protocol


    @property
    def pinTX(self):
        return self.__pinTX

    @pinTX.setter
    def pinTX(self, pinTX: str):
        self.__pinTX = pinTX


    @property
    def password_AccessPoint(self):
        return self.__password_AccessPoint

    @password_AccessPoint.setter
    def password_AccessPoint(self, password_AccessPoint: str):
        self.__password_AccessPoint = password_AccessPoint


class iotw_BluetoothHC06(Connectivity):

    def __init__(self, pinTXD: str, pinRXD: str, pinGND: str, pinVCC: str):
        self.pinTXD = pinTXD
        self.pinRXD = pinRXD
        self.pinGND = pinGND
        self.pinVCC = pinVCC
        
        pass
    @property
    def pinTXD(self):
        return self.__pinTXD

    @pinTXD.setter
    def pinTXD(self, pinTXD: str):
        self.__pinTXD = pinTXD


    @property
    def pinVCC(self):
        return self.__pinVCC

    @pinVCC.setter
    def pinVCC(self, pinVCC: str):
        self.__pinVCC = pinVCC


    @property
    def pinGND(self):
        return self.__pinGND

    @pinGND.setter
    def pinGND(self, pinGND: str):
        self.__pinGND = pinGND


    @property
    def pinRXD(self):
        return self.__pinRXD

    @pinRXD.setter
    def pinRXD(self, pinRXD: str):
        self.__pinRXD = pinRXD


class OutputDevice:

    pass
class iotw_I2CLCD(OutputDevice):

    def __init__(self, type: str, pinGND: str, pinVcc: str, pinSDA: str, pinSCL: str):
        self.type = type
        self.pinGND = pinGND
        self.pinVcc = pinVcc
        self.pinSDA = pinSDA
        self.pinSCL = pinSCL
        
        pass
    @property
    def pinVcc(self):
        return self.__pinVcc

    @pinVcc.setter
    def pinVcc(self, pinVcc: str):
        self.__pinVcc = pinVcc


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def pinSCL(self):
        return self.__pinSCL

    @pinSCL.setter
    def pinSCL(self, pinSCL: str):
        self.__pinSCL = pinSCL


    @property
    def pinGND(self):
        return self.__pinGND

    @pinGND.setter
    def pinGND(self, pinGND: str):
        self.__pinGND = pinGND


    @property
    def pinSDA(self):
        return self.__pinSDA

    @pinSDA.setter
    def pinSDA(self, pinSDA: str):
        self.__pinSDA = pinSDA


class iotw_LED(OutputDevice):

    def __init__(self, pin1: str, pin2: str):
        self.pin1 = pin1
        self.pin2 = pin2
        
        pass
    @property
    def pin1(self):
        return self.__pin1

    @pin1.setter
    def pin1(self, pin1: str):
        self.__pin1 = pin1


    @property
    def pin2(self):
        return self.__pin2

    @pin2.setter
    def pin2(self, pin2: str):
        self.__pin2 = pin2


class iotw_Buzzer(OutputDevice):

    def __init__(self, pin1: str, pin2: str, Tone: int, Time: int):
        self.pin1 = pin1
        self.pin2 = pin2
        self.Tone = Tone
        self.Time = Time
        
        pass
    @property
    def Time(self):
        return self.__Time

    @Time.setter
    def Time(self, Time: int):
        self.__Time = Time


    @property
    def Tone(self):
        return self.__Tone

    @Tone.setter
    def Tone(self, Tone: int):
        self.__Tone = Tone


    @property
    def pin2(self):
        return self.__pin2

    @pin2.setter
    def pin2(self, pin2: str):
        self.__pin2 = pin2


    @property
    def pin1(self):
        return self.__pin1

    @pin1.setter
    def pin1(self, pin1: str):
        self.__pin1 = pin1


class InputDevice:

    pass
class iotw_Button(InputDevice):

    def __init__(self, pin1: str):
        self.pin1 = pin1
        
        pass
    @property
    def pin1(self):
        return self.__pin1

    @pin1.setter
    def pin1(self, pin1: str):
        self.__pin1 = pin1


class iotw_Keypad4x4(InputDevice):

    def __init__(self, keys: str, rows: int, cols: int, pin1: str, pin2: str, pin3: str, pin4: str, pin5: str, pin6: str, pin7: str, pin8: str, nameButton1: str, nameButton2: str, nameButton3: str, nameButton4: str, nameButton5: str, nameButton6: str, nameButton7: str, nameButton8: str, nameButton9: str, nameButton0: str, nameButtonA: str, nameButtonB: str, nameButtonC: str, nameButtonD: str, nameButtonHash: str, nameButtonAsterisk: str):
        self.keys = keys
        self.rows = rows
        self.cols = cols
        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.pin4 = pin4
        self.pin5 = pin5
        self.pin6 = pin6
        self.pin7 = pin7
        self.pin8 = pin8
        self.nameButton1 = nameButton1
        self.nameButton2 = nameButton2
        self.nameButton3 = nameButton3
        self.nameButton4 = nameButton4
        self.nameButton5 = nameButton5
        self.nameButton6 = nameButton6
        self.nameButton7 = nameButton7
        self.nameButton8 = nameButton8
        self.nameButton9 = nameButton9
        self.nameButton0 = nameButton0
        self.nameButtonA = nameButtonA
        self.nameButtonB = nameButtonB
        self.nameButtonC = nameButtonC
        self.nameButtonD = nameButtonD
        self.nameButtonHash = nameButtonHash
        self.nameButtonAsterisk = nameButtonAsterisk
        
        pass
    @property
    def nameButton6(self):
        return self.__nameButton6

    @nameButton6.setter
    def nameButton6(self, nameButton6: str):
        self.__nameButton6 = nameButton6


    @property
    def nameButton0(self):
        return self.__nameButton0

    @nameButton0.setter
    def nameButton0(self, nameButton0: str):
        self.__nameButton0 = nameButton0


    @property
    def nameButton9(self):
        return self.__nameButton9

    @nameButton9.setter
    def nameButton9(self, nameButton9: str):
        self.__nameButton9 = nameButton9


    @property
    def pin6(self):
        return self.__pin6

    @pin6.setter
    def pin6(self, pin6: str):
        self.__pin6 = pin6


    @property
    def nameButton2(self):
        return self.__nameButton2

    @nameButton2.setter
    def nameButton2(self, nameButton2: str):
        self.__nameButton2 = nameButton2


    @property
    def pin2(self):
        return self.__pin2

    @pin2.setter
    def pin2(self, pin2: str):
        self.__pin2 = pin2


    @property
    def nameButton5(self):
        return self.__nameButton5

    @nameButton5.setter
    def nameButton5(self, nameButton5: str):
        self.__nameButton5 = nameButton5


    @property
    def nameButton1(self):
        return self.__nameButton1

    @nameButton1.setter
    def nameButton1(self, nameButton1: str):
        self.__nameButton1 = nameButton1


    @property
    def nameButton7(self):
        return self.__nameButton7

    @nameButton7.setter
    def nameButton7(self, nameButton7: str):
        self.__nameButton7 = nameButton7


    @property
    def nameButtonB(self):
        return self.__nameButtonB

    @nameButtonB.setter
    def nameButtonB(self, nameButtonB: str):
        self.__nameButtonB = nameButtonB


    @property
    def nameButton4(self):
        return self.__nameButton4

    @nameButton4.setter
    def nameButton4(self, nameButton4: str):
        self.__nameButton4 = nameButton4


    @property
    def pin1(self):
        return self.__pin1

    @pin1.setter
    def pin1(self, pin1: str):
        self.__pin1 = pin1


    @property
    def nameButtonD(self):
        return self.__nameButtonD

    @nameButtonD.setter
    def nameButtonD(self, nameButtonD: str):
        self.__nameButtonD = nameButtonD


    @property
    def nameButtonAsterisk(self):
        return self.__nameButtonAsterisk

    @nameButtonAsterisk.setter
    def nameButtonAsterisk(self, nameButtonAsterisk: str):
        self.__nameButtonAsterisk = nameButtonAsterisk


    @property
    def nameButtonHash(self):
        return self.__nameButtonHash

    @nameButtonHash.setter
    def nameButtonHash(self, nameButtonHash: str):
        self.__nameButtonHash = nameButtonHash


    @property
    def keys(self):
        return self.__keys

    @keys.setter
    def keys(self, keys: str):
        self.__keys = keys


    @property
    def nameButtonA(self):
        return self.__nameButtonA

    @nameButtonA.setter
    def nameButtonA(self, nameButtonA: str):
        self.__nameButtonA = nameButtonA


    @property
    def nameButtonC(self):
        return self.__nameButtonC

    @nameButtonC.setter
    def nameButtonC(self, nameButtonC: str):
        self.__nameButtonC = nameButtonC


    @property
    def nameButton3(self):
        return self.__nameButton3

    @nameButton3.setter
    def nameButton3(self, nameButton3: str):
        self.__nameButton3 = nameButton3


    @property
    def cols(self):
        return self.__cols

    @cols.setter
    def cols(self, cols: int):
        self.__cols = cols


    @property
    def pin5(self):
        return self.__pin5

    @pin5.setter
    def pin5(self, pin5: str):
        self.__pin5 = pin5


    @property
    def pin3(self):
        return self.__pin3

    @pin3.setter
    def pin3(self, pin3: str):
        self.__pin3 = pin3


    @property
    def rows(self):
        return self.__rows

    @rows.setter
    def rows(self, rows: int):
        self.__rows = rows


    @property
    def pin8(self):
        return self.__pin8

    @pin8.setter
    def pin8(self, pin8: str):
        self.__pin8 = pin8


    @property
    def pin7(self):
        return self.__pin7

    @pin7.setter
    def pin7(self, pin7: str):
        self.__pin7 = pin7


    @property
    def pin4(self):
        return self.__pin4

    @pin4.setter
    def pin4(self, pin4: str):
        self.__pin4 = pin4


    @property
    def nameButton8(self):
        return self.__nameButton8

    @nameButton8.setter
    def nameButton8(self, nameButton8: str):
        self.__nameButton8 = nameButton8


    def getButton(self, iotw_name) :
        # TODO: Implement getButton method
        pass

class Mainboard:

    pass
class iotw_ArduinoUNOR3(Mainboard):

    def __init__(self, pin0: str, pin1: str, pin2: str, pin3: str, pin4: str, pin5: str, pin6: str, pin7: str, pin8: str, pin9: str, pin10: str, pin11: str, pin12: str, pin13: str, pinA0: str, pinA1: str, pinA2: str, pinA3: str, pinA4: str, pinA5: str):
        self.pin0 = pin0
        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.pin4 = pin4
        self.pin5 = pin5
        self.pin6 = pin6
        self.pin7 = pin7
        self.pin8 = pin8
        self.pin9 = pin9
        self.pin10 = pin10
        self.pin11 = pin11
        self.pin12 = pin12
        self.pin13 = pin13
        self.pinA0 = pinA0
        self.pinA1 = pinA1
        self.pinA2 = pinA2
        self.pinA3 = pinA3
        self.pinA4 = pinA4
        self.pinA5 = pinA5
        
        pass
    @property
    def pinA2(self):
        return self.__pinA2

    @pinA2.setter
    def pinA2(self, pinA2: str):
        self.__pinA2 = pinA2


    @property
    def pin11(self):
        return self.__pin11

    @pin11.setter
    def pin11(self, pin11: str):
        self.__pin11 = pin11


    @property
    def pinA4(self):
        return self.__pinA4

    @pinA4.setter
    def pinA4(self, pinA4: str):
        self.__pinA4 = pinA4


    @property
    def pinA1(self):
        return self.__pinA1

    @pinA1.setter
    def pinA1(self, pinA1: str):
        self.__pinA1 = pinA1


    @property
    def pin2(self):
        return self.__pin2

    @pin2.setter
    def pin2(self, pin2: str):
        self.__pin2 = pin2


    @property
    def pin0(self):
        return self.__pin0

    @pin0.setter
    def pin0(self, pin0: str):
        self.__pin0 = pin0


    @property
    def pin1(self):
        return self.__pin1

    @pin1.setter
    def pin1(self, pin1: str):
        self.__pin1 = pin1


    @property
    def pinA0(self):
        return self.__pinA0

    @pinA0.setter
    def pinA0(self, pinA0: str):
        self.__pinA0 = pinA0


    @property
    def pin9(self):
        return self.__pin9

    @pin9.setter
    def pin9(self, pin9: str):
        self.__pin9 = pin9


    @property
    def pin6(self):
        return self.__pin6

    @pin6.setter
    def pin6(self, pin6: str):
        self.__pin6 = pin6


    @property
    def pinA3(self):
        return self.__pinA3

    @pinA3.setter
    def pinA3(self, pinA3: str):
        self.__pinA3 = pinA3


    @property
    def pin5(self):
        return self.__pin5

    @pin5.setter
    def pin5(self, pin5: str):
        self.__pin5 = pin5


    @property
    def pin4(self):
        return self.__pin4

    @pin4.setter
    def pin4(self, pin4: str):
        self.__pin4 = pin4


    @property
    def pin7(self):
        return self.__pin7

    @pin7.setter
    def pin7(self, pin7: str):
        self.__pin7 = pin7


    @property
    def pin8(self):
        return self.__pin8

    @pin8.setter
    def pin8(self, pin8: str):
        self.__pin8 = pin8


    @property
    def pin12(self):
        return self.__pin12

    @pin12.setter
    def pin12(self, pin12: str):
        self.__pin12 = pin12


    @property
    def pinA5(self):
        return self.__pinA5

    @pinA5.setter
    def pinA5(self, pinA5: str):
        self.__pinA5 = pinA5


    @property
    def pin3(self):
        return self.__pin3

    @pin3.setter
    def pin3(self, pin3: str):
        self.__pin3 = pin3


    @property
    def pin10(self):
        return self.__pin10

    @pin10.setter
    def pin10(self, pin10: str):
        self.__pin10 = pin10


    @property
    def pin13(self):
        return self.__pin13

    @pin13.setter
    def pin13(self, pin13: str):
        self.__pin13 = pin13


class IODevice:

    pass
class iotw_OutputDevice(IODevice):

    pass
class iotw_InputDevice(IODevice):

    pass
class Device:

    pass
class iotw_Connectivity(Device):

    pass
class iotw_IODevice(Device):

    pass
class iotw_Mainboard(ABC):

    def __init__(self, name: str, Mainboard: "iotw_Device" = None, mainboard: set["iotw_Device"] = None):
        self.name = name
        self.Mainboard = Mainboard
        self.mainboard = mainboard if mainboard is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def mainboard(self):
        return self.__mainboard

    @mainboard.setter
    def mainboard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_Mainboard__mainboard", None)
        self.__mainboard = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Device"):
                    opp_val = getattr(item, "Device", None)
                    
                    if opp_val == self:
                        setattr(item, "Device", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Device"):
                    opp_val = getattr(item, "Device", None)
                    
                    setattr(item, "Device", self)
                    

    @property
    def Mainboard(self):
        return self.__Mainboard

    @Mainboard.setter
    def Mainboard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_Mainboard__Mainboard", None)
        self.__Mainboard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "devices"):
                opp_val = getattr(old_value, "devices", None)
                if opp_val == self:
                    setattr(old_value, "devices", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "devices"):
                opp_val = getattr(value, "devices", None)
                setattr(value, "devices", self)

    def removeDevice(self, iotw_device):
        # TODO: Implement removeDevice method
        pass

    def getPins(self) :
        # TODO: Implement getPins method
        pass

    def getPinConnecteds(self) :
        # TODO: Implement getPinConnecteds method
        pass

    def addDevice(self, iotw_device):
        # TODO: Implement addDevice method
        pass

    def modifyPin(self, iotw_pin):
        # TODO: Implement modifyPin method
        pass

    def findPin(self, iotw_pin) :
        # TODO: Implement findPin method
        pass

class Component:

    pass
class iotw_Device(Component):

    def __init__(self, name: str, devices: "iotw_Mainboard" = None, Device: "iotw_Mainboard" = None):
        self.name = name
        self.devices = devices
        self.Device = Device
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def devices(self):
        return self.__devices

    @devices.setter
    def devices(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_Device__devices", None)
        self.__devices = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Mainboard"):
                opp_val = getattr(old_value, "Mainboard", None)
                if opp_val == self:
                    setattr(old_value, "Mainboard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Mainboard"):
                opp_val = getattr(value, "Mainboard", None)
                setattr(value, "Mainboard", self)

    @property
    def Device(self):
        return self.__Device

    @Device.setter
    def Device(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_Device__Device", None)
        self.__Device = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mainboard"):
                opp_val = getattr(old_value, "mainboard", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mainboard"):
                opp_val = getattr(value, "mainboard", None)
                if opp_val is None:
                    setattr(value, "mainboard", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def modifyPin(self, iotw_pin):
        # TODO: Implement modifyPin method
        pass

    def getPinConnecteds(self) :
        # TODO: Implement getPinConnecteds method
        pass

    def getPins(self) :
        # TODO: Implement getPins method
        pass

class iotw_StateComponent(Component):

    def __init__(self, name: str, iotw_StateComponent: "iotw_StateSchema" = None, iotw_StateComponent8: set["iotw_Connection"] = None, iotw_StateComponent11: set["iotw_Connection"] = None):
        self.name = name
        self.iotw_StateComponent = iotw_StateComponent
        self.iotw_StateComponent8 = iotw_StateComponent8 if iotw_StateComponent8 is not None else set()
        self.iotw_StateComponent11 = iotw_StateComponent11 if iotw_StateComponent11 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def iotw_StateComponent11(self):
        return self.__iotw_StateComponent11

    @iotw_StateComponent11.setter
    def iotw_StateComponent11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_StateComponent__iotw_StateComponent11", None)
        self.__iotw_StateComponent11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iotw_Connection12"):
                    opp_val = getattr(item, "iotw_Connection12", None)
                    
                    if opp_val == self:
                        setattr(item, "iotw_Connection12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iotw_Connection12"):
                    opp_val = getattr(item, "iotw_Connection12", None)
                    
                    setattr(item, "iotw_Connection12", self)
                    

    @property
    def iotw_StateComponent(self):
        return self.__iotw_StateComponent

    @iotw_StateComponent.setter
    def iotw_StateComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_StateComponent__iotw_StateComponent", None)
        self.__iotw_StateComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotw_StateSchema"):
                opp_val = getattr(old_value, "iotw_StateSchema", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotw_StateSchema"):
                opp_val = getattr(value, "iotw_StateSchema", None)
                if opp_val is None:
                    setattr(value, "iotw_StateSchema", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iotw_StateComponent8(self):
        return self.__iotw_StateComponent8

    @iotw_StateComponent8.setter
    def iotw_StateComponent8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_StateComponent__iotw_StateComponent8", None)
        self.__iotw_StateComponent8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iotw_Connection9"):
                    opp_val = getattr(item, "iotw_Connection9", None)
                    
                    if opp_val == self:
                        setattr(item, "iotw_Connection9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iotw_Connection9"):
                    opp_val = getattr(item, "iotw_Connection9", None)
                    
                    setattr(item, "iotw_Connection9", self)
                    

class iotw_StateSchema:

    pass
class iotw_Component(ABC):

    def __init__(self, id: str, constraints: str, iotw_Component: "iotw_Connection" = None, iotw_Component3: "iotw_Connection" = None):
        self.id = id
        self.constraints = constraints
        self.iotw_Component = iotw_Component
        self.iotw_Component3 = iotw_Component3
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def constraints(self):
        return self.__constraints

    @constraints.setter
    def constraints(self, constraints: str):
        self.__constraints = constraints


    @property
    def iotw_Component3(self):
        return self.__iotw_Component3

    @iotw_Component3.setter
    def iotw_Component3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_Component__iotw_Component3", None)
        self.__iotw_Component3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotw_Connection2"):
                opp_val = getattr(old_value, "iotw_Connection2", None)
                if opp_val == self:
                    setattr(old_value, "iotw_Connection2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotw_Connection2"):
                opp_val = getattr(value, "iotw_Connection2", None)
                setattr(value, "iotw_Connection2", self)

    @property
    def iotw_Component(self):
        return self.__iotw_Component

    @iotw_Component.setter
    def iotw_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_Component__iotw_Component", None)
        self.__iotw_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotw_Connection"):
                opp_val = getattr(old_value, "iotw_Connection", None)
                if opp_val == self:
                    setattr(old_value, "iotw_Connection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotw_Connection"):
                opp_val = getattr(value, "iotw_Connection", None)
                setattr(value, "iotw_Connection", self)

class iotw_Connection:

    def __init__(self, bendpoints: str, routerKind: str, kind: str, label: str, iotw_Connection: "iotw_Component" = None, iotw_Connection2: "iotw_Component" = None, connnections: "iotw_StateSchema" = None, Connection: "iotw_StateSchema" = None, iotw_Connection9: "iotw_StateComponent" = None, iotw_Connection12: "iotw_StateComponent" = None):
        self.bendpoints = bendpoints
        self.routerKind = routerKind
        self.kind = kind
        self.label = label
        self.iotw_Connection = iotw_Connection
        self.iotw_Connection2 = iotw_Connection2
        self.connnections = connnections
        self.Connection = Connection
        self.iotw_Connection9 = iotw_Connection9
        self.iotw_Connection12 = iotw_Connection12
        
        pass
    @property
    def bendpoints(self):
        return self.__bendpoints

    @bendpoints.setter
    def bendpoints(self, bendpoints: str):
        self.__bendpoints = bendpoints


    @property
    def routerKind(self):
        return self.__routerKind

    @routerKind.setter
    def routerKind(self, routerKind: str):
        self.__routerKind = routerKind


    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def Connection(self):
        return self.__Connection

    @Connection.setter
    def Connection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_Connection__Connection", None)
        self.__Connection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateSchema"):
                opp_val = getattr(old_value, "stateSchema", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateSchema"):
                opp_val = getattr(value, "stateSchema", None)
                if opp_val is None:
                    setattr(value, "stateSchema", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iotw_Connection(self):
        return self.__iotw_Connection

    @iotw_Connection.setter
    def iotw_Connection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_Connection__iotw_Connection", None)
        self.__iotw_Connection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotw_Component"):
                opp_val = getattr(old_value, "iotw_Component", None)
                if opp_val == self:
                    setattr(old_value, "iotw_Component", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotw_Component"):
                opp_val = getattr(value, "iotw_Component", None)
                setattr(value, "iotw_Component", self)

    @property
    def connnections(self):
        return self.__connnections

    @connnections.setter
    def connnections(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_Connection__connnections", None)
        self.__connnections = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateSchema"):
                opp_val = getattr(old_value, "StateSchema", None)
                if opp_val == self:
                    setattr(old_value, "StateSchema", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateSchema"):
                opp_val = getattr(value, "StateSchema", None)
                setattr(value, "StateSchema", self)

    @property
    def iotw_Connection9(self):
        return self.__iotw_Connection9

    @iotw_Connection9.setter
    def iotw_Connection9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_Connection__iotw_Connection9", None)
        self.__iotw_Connection9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotw_StateComponent8"):
                opp_val = getattr(old_value, "iotw_StateComponent8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotw_StateComponent8"):
                opp_val = getattr(value, "iotw_StateComponent8", None)
                if opp_val is None:
                    setattr(value, "iotw_StateComponent8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iotw_Connection12(self):
        return self.__iotw_Connection12

    @iotw_Connection12.setter
    def iotw_Connection12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_Connection__iotw_Connection12", None)
        self.__iotw_Connection12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotw_StateComponent11"):
                opp_val = getattr(old_value, "iotw_StateComponent11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotw_StateComponent11"):
                opp_val = getattr(value, "iotw_StateComponent11", None)
                if opp_val is None:
                    setattr(value, "iotw_StateComponent11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iotw_Connection2(self):
        return self.__iotw_Connection2

    @iotw_Connection2.setter
    def iotw_Connection2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_Connection__iotw_Connection2", None)
        self.__iotw_Connection2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotw_Component3"):
                opp_val = getattr(old_value, "iotw_Component3", None)
                if opp_val == self:
                    setattr(old_value, "iotw_Component3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotw_Component3"):
                opp_val = getattr(value, "iotw_Component3", None)
                setattr(value, "iotw_Component3", self)
