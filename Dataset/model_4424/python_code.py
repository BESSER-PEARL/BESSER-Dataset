from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RouterKind(Enum):
    BENDPOINT = "BENDPOINT"
    MANHATTAN = "MANHATTAN"
class ConnectionKind(Enum):
    STATE_FLOW = "STATE_FLOW"
class TypeData(Enum):
    XML = "XML"
    JSON = "JSON"


############################################
# Definition of Classes
############################################

class OutputControl:

    pass
class iotw_I2CLCD2004(OutputControl):

    def __init__(self, pinSCL: str, pinGND: str, pinVcc: str, pinSDA: str):
        self.pinSCL = pinSCL
        self.pinGND = pinGND
        self.pinVcc = pinVcc
        self.pinSDA = pinSDA
        
    @property
    def pinSCL(self) -> str:
        return self.__pinSCL

    @pinSCL.setter
    def pinSCL(self, pinSCL: str):
        self.__pinSCL = pinSCL

    @property
    def pinSDA(self) -> str:
        return self.__pinSDA

    @pinSDA.setter
    def pinSDA(self, pinSDA: str):
        self.__pinSDA = pinSDA

    @property
    def pinVcc(self) -> str:
        return self.__pinVcc

    @pinVcc.setter
    def pinVcc(self, pinVcc: str):
        self.__pinVcc = pinVcc

    @property
    def pinGND(self) -> str:
        return self.__pinGND

    @pinGND.setter
    def pinGND(self, pinGND: str):
        self.__pinGND = pinGND

class iotw_LED(OutputControl):

    def __init__(self, pin1: str, pin2: str):
        self.pin1 = pin1
        self.pin2 = pin2
        
    @property
    def pin1(self) -> str:
        return self.__pin1

    @pin1.setter
    def pin1(self, pin1: str):
        self.__pin1 = pin1

    @property
    def pin2(self) -> str:
        return self.__pin2

    @pin2.setter
    def pin2(self, pin2: str):
        self.__pin2 = pin2

class StateControl:

    pass
class iotw_Decision(StateControl):

    pass
class iotw_StartPoint(StateControl):

    pass
class iotw_EndPoint(StateControl):

    pass
class iotw_StateFrame(StateControl):

    def __init__(self, content: str):
        self.content = content
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

class iotw_Buzzer(OutputControl):

    def __init__(self, pin1: str, pin2: str):
        self.pin1 = pin1
        self.pin2 = pin2
        
    @property
    def pin1(self) -> str:
        return self.__pin1

    @pin1.setter
    def pin1(self, pin1: str):
        self.__pin1 = pin1

    @property
    def pin2(self) -> str:
        return self.__pin2

    @pin2.setter
    def pin2(self, pin2: str):
        self.__pin2 = pin2

class ConnectivityControl:

    pass
class iotw_WifiESP8266(ConnectivityControl):

    def __init__(self, pinTX: str, pinRX: str, pinVcc: str, pinGND: str, pinCHPD: str, SSID: str, Password: str, Host: str, Port: int):
        self.pinTX = pinTX
        self.pinRX = pinRX
        self.pinVcc = pinVcc
        self.pinGND = pinGND
        self.pinCHPD = pinCHPD
        self.SSID = SSID
        self.Password = Password
        self.Host = Host
        self.Port = Port
        
    @property
    def Host(self) -> str:
        return self.__Host

    @Host.setter
    def Host(self, Host: str):
        self.__Host = Host

    @property
    def Password(self) -> str:
        return self.__Password

    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def pinRX(self) -> str:
        return self.__pinRX

    @pinRX.setter
    def pinRX(self, pinRX: str):
        self.__pinRX = pinRX

    @property
    def pinGND(self) -> str:
        return self.__pinGND

    @pinGND.setter
    def pinGND(self, pinGND: str):
        self.__pinGND = pinGND

    @property
    def pinTX(self) -> str:
        return self.__pinTX

    @pinTX.setter
    def pinTX(self, pinTX: str):
        self.__pinTX = pinTX

    @property
    def pinCHPD(self) -> str:
        return self.__pinCHPD

    @pinCHPD.setter
    def pinCHPD(self, pinCHPD: str):
        self.__pinCHPD = pinCHPD

    @property
    def pinVcc(self) -> str:
        return self.__pinVcc

    @pinVcc.setter
    def pinVcc(self, pinVcc: str):
        self.__pinVcc = pinVcc

    @property
    def Port(self) -> int:
        return self.__Port

    @Port.setter
    def Port(self, Port: int):
        self.__Port = Port

    @property
    def SSID(self) -> str:
        return self.__SSID

    @SSID.setter
    def SSID(self, SSID: str):
        self.__SSID = SSID

class iotw_BluetoothHC06(ConnectivityControl):

    def __init__(self, pinTXD: str, pinRXD: str, pinGND: str, pinVCC: str):
        self.pinTXD = pinTXD
        self.pinRXD = pinRXD
        self.pinGND = pinGND
        self.pinVCC = pinVCC
        
    @property
    def pinGND(self) -> str:
        return self.__pinGND

    @pinGND.setter
    def pinGND(self, pinGND: str):
        self.__pinGND = pinGND

    @property
    def pinTXD(self) -> str:
        return self.__pinTXD

    @pinTXD.setter
    def pinTXD(self, pinTXD: str):
        self.__pinTXD = pinTXD

    @property
    def pinRXD(self) -> str:
        return self.__pinRXD

    @pinRXD.setter
    def pinRXD(self, pinRXD: str):
        self.__pinRXD = pinRXD

    @property
    def pinVCC(self) -> str:
        return self.__pinVCC

    @pinVCC.setter
    def pinVCC(self, pinVCC: str):
        self.__pinVCC = pinVCC

class InputControl:

    pass
class iotw_Button(InputControl):

    def __init__(self, pin1: str):
        self.pin1 = pin1
        
    @property
    def pin1(self) -> str:
        return self.__pin1

    @pin1.setter
    def pin1(self, pin1: str):
        self.__pin1 = pin1

class iotw_Keypad4x4(InputControl):

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
        
    @property
    def pin2(self) -> str:
        return self.__pin2

    @pin2.setter
    def pin2(self, pin2: str):
        self.__pin2 = pin2

    @property
    def nameButton3(self) -> str:
        return self.__nameButton3

    @nameButton3.setter
    def nameButton3(self, nameButton3: str):
        self.__nameButton3 = nameButton3

    @property
    def nameButtonAsterisk(self) -> str:
        return self.__nameButtonAsterisk

    @nameButtonAsterisk.setter
    def nameButtonAsterisk(self, nameButtonAsterisk: str):
        self.__nameButtonAsterisk = nameButtonAsterisk

    @property
    def pin7(self) -> str:
        return self.__pin7

    @pin7.setter
    def pin7(self, pin7: str):
        self.__pin7 = pin7

    @property
    def nameButtonHash(self) -> str:
        return self.__nameButtonHash

    @nameButtonHash.setter
    def nameButtonHash(self, nameButtonHash: str):
        self.__nameButtonHash = nameButtonHash

    @property
    def pin6(self) -> str:
        return self.__pin6

    @pin6.setter
    def pin6(self, pin6: str):
        self.__pin6 = pin6

    @property
    def nameButton5(self) -> str:
        return self.__nameButton5

    @nameButton5.setter
    def nameButton5(self, nameButton5: str):
        self.__nameButton5 = nameButton5

    @property
    def nameButtonA(self) -> str:
        return self.__nameButtonA

    @nameButtonA.setter
    def nameButtonA(self, nameButtonA: str):
        self.__nameButtonA = nameButtonA

    @property
    def nameButton2(self) -> str:
        return self.__nameButton2

    @nameButton2.setter
    def nameButton2(self, nameButton2: str):
        self.__nameButton2 = nameButton2

    @property
    def pin8(self) -> str:
        return self.__pin8

    @pin8.setter
    def pin8(self, pin8: str):
        self.__pin8 = pin8

    @property
    def keys(self) -> str:
        return self.__keys

    @keys.setter
    def keys(self, keys: str):
        self.__keys = keys

    @property
    def rows(self) -> int:
        return self.__rows

    @rows.setter
    def rows(self, rows: int):
        self.__rows = rows

    @property
    def cols(self) -> int:
        return self.__cols

    @cols.setter
    def cols(self, cols: int):
        self.__cols = cols

    @property
    def nameButton1(self) -> str:
        return self.__nameButton1

    @nameButton1.setter
    def nameButton1(self, nameButton1: str):
        self.__nameButton1 = nameButton1

    @property
    def pin1(self) -> str:
        return self.__pin1

    @pin1.setter
    def pin1(self, pin1: str):
        self.__pin1 = pin1

    @property
    def nameButton8(self) -> str:
        return self.__nameButton8

    @nameButton8.setter
    def nameButton8(self, nameButton8: str):
        self.__nameButton8 = nameButton8

    @property
    def pin3(self) -> str:
        return self.__pin3

    @pin3.setter
    def pin3(self, pin3: str):
        self.__pin3 = pin3

    @property
    def nameButton6(self) -> str:
        return self.__nameButton6

    @nameButton6.setter
    def nameButton6(self, nameButton6: str):
        self.__nameButton6 = nameButton6

    @property
    def nameButton0(self) -> str:
        return self.__nameButton0

    @nameButton0.setter
    def nameButton0(self, nameButton0: str):
        self.__nameButton0 = nameButton0

    @property
    def nameButtonD(self) -> str:
        return self.__nameButtonD

    @nameButtonD.setter
    def nameButtonD(self, nameButtonD: str):
        self.__nameButtonD = nameButtonD

    @property
    def nameButton4(self) -> str:
        return self.__nameButton4

    @nameButton4.setter
    def nameButton4(self, nameButton4: str):
        self.__nameButton4 = nameButton4

    @property
    def nameButtonC(self) -> str:
        return self.__nameButtonC

    @nameButtonC.setter
    def nameButtonC(self, nameButtonC: str):
        self.__nameButtonC = nameButtonC

    @property
    def nameButtonB(self) -> str:
        return self.__nameButtonB

    @nameButtonB.setter
    def nameButtonB(self, nameButtonB: str):
        self.__nameButtonB = nameButtonB

    @property
    def nameButton7(self) -> str:
        return self.__nameButton7

    @nameButton7.setter
    def nameButton7(self, nameButton7: str):
        self.__nameButton7 = nameButton7

    @property
    def nameButton9(self) -> str:
        return self.__nameButton9

    @nameButton9.setter
    def nameButton9(self, nameButton9: str):
        self.__nameButton9 = nameButton9

    @property
    def pin5(self) -> str:
        return self.__pin5

    @pin5.setter
    def pin5(self, pin5: str):
        self.__pin5 = pin5

    @property
    def pin4(self) -> str:
        return self.__pin4

    @pin4.setter
    def pin4(self, pin4: str):
        self.__pin4 = pin4

    def getButton(self, name: str) -> str:
        # TODO: Implement getButton method
        pass

class IOControl:

    pass
class iotw_OutputControl(IOControl):

    pass
class iotw_InputControl(IOControl):

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
        
    @property
    def pin3(self) -> str:
        return self.__pin3

    @pin3.setter
    def pin3(self, pin3: str):
        self.__pin3 = pin3

    @property
    def pin12(self) -> str:
        return self.__pin12

    @pin12.setter
    def pin12(self, pin12: str):
        self.__pin12 = pin12

    @property
    def pinA0(self) -> str:
        return self.__pinA0

    @pinA0.setter
    def pinA0(self, pinA0: str):
        self.__pinA0 = pinA0

    @property
    def pin13(self) -> str:
        return self.__pin13

    @pin13.setter
    def pin13(self, pin13: str):
        self.__pin13 = pin13

    @property
    def pin1(self) -> str:
        return self.__pin1

    @pin1.setter
    def pin1(self, pin1: str):
        self.__pin1 = pin1

    @property
    def pin5(self) -> str:
        return self.__pin5

    @pin5.setter
    def pin5(self, pin5: str):
        self.__pin5 = pin5

    @property
    def pin8(self) -> str:
        return self.__pin8

    @pin8.setter
    def pin8(self, pin8: str):
        self.__pin8 = pin8

    @property
    def pinA1(self) -> str:
        return self.__pinA1

    @pinA1.setter
    def pinA1(self, pinA1: str):
        self.__pinA1 = pinA1

    @property
    def pinA4(self) -> str:
        return self.__pinA4

    @pinA4.setter
    def pinA4(self, pinA4: str):
        self.__pinA4 = pinA4

    @property
    def pinA5(self) -> str:
        return self.__pinA5

    @pinA5.setter
    def pinA5(self, pinA5: str):
        self.__pinA5 = pinA5

    @property
    def pin10(self) -> str:
        return self.__pin10

    @pin10.setter
    def pin10(self, pin10: str):
        self.__pin10 = pin10

    @property
    def pinA2(self) -> str:
        return self.__pinA2

    @pinA2.setter
    def pinA2(self, pinA2: str):
        self.__pinA2 = pinA2

    @property
    def pin4(self) -> str:
        return self.__pin4

    @pin4.setter
    def pin4(self, pin4: str):
        self.__pin4 = pin4

    @property
    def pin6(self) -> str:
        return self.__pin6

    @pin6.setter
    def pin6(self, pin6: str):
        self.__pin6 = pin6

    @property
    def pin2(self) -> str:
        return self.__pin2

    @pin2.setter
    def pin2(self, pin2: str):
        self.__pin2 = pin2

    @property
    def pin7(self) -> str:
        return self.__pin7

    @pin7.setter
    def pin7(self, pin7: str):
        self.__pin7 = pin7

    @property
    def pin9(self) -> str:
        return self.__pin9

    @pin9.setter
    def pin9(self, pin9: str):
        self.__pin9 = pin9

    @property
    def pin11(self) -> str:
        return self.__pin11

    @pin11.setter
    def pin11(self, pin11: str):
        self.__pin11 = pin11

    @property
    def pinA3(self) -> str:
        return self.__pinA3

    @pinA3.setter
    def pinA3(self, pinA3: str):
        self.__pinA3 = pinA3

    @property
    def pin0(self) -> str:
        return self.__pin0

    @pin0.setter
    def pin0(self, pin0: str):
        self.__pin0 = pin0

class iotw_StateSchema:

    pass
class Control:

    pass
class iotw_IOControl(Control):

    def __init__(self, constraints: str, controls: "iotw_Mainboard" = None, IOControl: "iotw_Mainboard" = None):
        self.constraints = constraints
        self.controls = controls
        self.IOControl = IOControl
        
    @property
    def constraints(self) -> str:
        return self.__constraints

    @constraints.setter
    def constraints(self, constraints: str):
        self.__constraints = constraints

    @property
    def controls(self):
        return self.__controls

    @controls.setter
    def controls(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_IOControl__controls", None)
        self.__controls = value
        
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
    def IOControl(self):
        return self.__IOControl

    @IOControl.setter
    def IOControl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_IOControl__IOControl", None)
        self.__IOControl = value
        
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

    def getPinConnecteds(self) -> str:
        # TODO: Implement getPinConnecteds method
        pass

    def getPins(self) -> str:
        # TODO: Implement getPins method
        pass

    def modifyPin(self, pin: str):
        # TODO: Implement modifyPin method
        pass

class iotw_Control(ABC):

    def __init__(self, name: str, id: str, iotw_Control: "iotw_Connection" = None, iotw_Control19: "iotw_Connection" = None):
        self.name = name
        self.id = id
        self.iotw_Control = iotw_Control
        self.iotw_Control19 = iotw_Control19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def iotw_Control19(self):
        return self.__iotw_Control19

    @iotw_Control19.setter
    def iotw_Control19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_Control__iotw_Control19", None)
        self.__iotw_Control19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotw_Connection18"):
                opp_val = getattr(old_value, "iotw_Connection18", None)
                if opp_val == self:
                    setattr(old_value, "iotw_Connection18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotw_Connection18"):
                opp_val = getattr(value, "iotw_Connection18", None)
                setattr(value, "iotw_Connection18", self)

    @property
    def iotw_Control(self):
        return self.__iotw_Control

    @iotw_Control.setter
    def iotw_Control(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_Control__iotw_Control", None)
        self.__iotw_Control = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotw_Connection16"):
                opp_val = getattr(old_value, "iotw_Connection16", None)
                if opp_val == self:
                    setattr(old_value, "iotw_Connection16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotw_Connection16"):
                opp_val = getattr(value, "iotw_Connection16", None)
                setattr(value, "iotw_Connection16", self)

class iotw_DataExplorer:

    pass
class iotw_DataControl(Control):

    def __init__(self, constraints: str, location: str, type: str, datas: "iotw_DataExplorer" = None, DataControl: "iotw_DataExplorer" = None):
        self.constraints = constraints
        self.location = location
        self.type = type
        self.datas = datas
        self.DataControl = DataControl
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def constraints(self) -> str:
        return self.__constraints

    @constraints.setter
    def constraints(self, constraints: str):
        self.__constraints = constraints

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def DataControl(self):
        return self.__DataControl

    @DataControl.setter
    def DataControl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_DataControl__DataControl", None)
        self.__DataControl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataExplorer"):
                opp_val = getattr(old_value, "dataExplorer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataExplorer"):
                opp_val = getattr(value, "dataExplorer", None)
                if opp_val is None:
                    setattr(value, "dataExplorer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datas(self):
        return self.__datas

    @datas.setter
    def datas(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_DataControl__datas", None)
        self.__datas = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataExplorer"):
                opp_val = getattr(old_value, "DataExplorer", None)
                if opp_val == self:
                    setattr(old_value, "DataExplorer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataExplorer"):
                opp_val = getattr(value, "DataExplorer", None)
                setattr(value, "DataExplorer", self)

class iotw_Connection:

    def __init__(self, bendpoints: str, routerKind: str, kind: str, label: str, iotw_Connection: "iotw_StateControl" = None, iotw_Connection6: "iotw_StateControl" = None, Connection: "iotw_StateSchema" = None, iotw_Connection16: "iotw_Control" = None, iotw_Connection18: "iotw_Control" = None, connnections: "iotw_StateSchema" = None):
        self.bendpoints = bendpoints
        self.routerKind = routerKind
        self.kind = kind
        self.label = label
        self.iotw_Connection = iotw_Connection
        self.iotw_Connection6 = iotw_Connection6
        self.Connection = Connection
        self.iotw_Connection16 = iotw_Connection16
        self.iotw_Connection18 = iotw_Connection18
        self.connnections = connnections
        
    @property
    def routerKind(self) -> str:
        return self.__routerKind

    @routerKind.setter
    def routerKind(self, routerKind: str):
        self.__routerKind = routerKind

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def bendpoints(self) -> str:
        return self.__bendpoints

    @bendpoints.setter
    def bendpoints(self, bendpoints: str):
        self.__bendpoints = bendpoints

    @property
    def iotw_Connection6(self):
        return self.__iotw_Connection6

    @iotw_Connection6.setter
    def iotw_Connection6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_Connection__iotw_Connection6", None)
        self.__iotw_Connection6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotw_StateControl5"):
                opp_val = getattr(old_value, "iotw_StateControl5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotw_StateControl5"):
                opp_val = getattr(value, "iotw_StateControl5", None)
                if opp_val is None:
                    setattr(value, "iotw_StateControl5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iotw_Connection16(self):
        return self.__iotw_Connection16

    @iotw_Connection16.setter
    def iotw_Connection16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_Connection__iotw_Connection16", None)
        self.__iotw_Connection16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotw_Control"):
                opp_val = getattr(old_value, "iotw_Control", None)
                if opp_val == self:
                    setattr(old_value, "iotw_Control", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotw_Control"):
                opp_val = getattr(value, "iotw_Control", None)
                setattr(value, "iotw_Control", self)

    @property
    def iotw_Connection18(self):
        return self.__iotw_Connection18

    @iotw_Connection18.setter
    def iotw_Connection18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_Connection__iotw_Connection18", None)
        self.__iotw_Connection18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotw_Control19"):
                opp_val = getattr(old_value, "iotw_Control19", None)
                if opp_val == self:
                    setattr(old_value, "iotw_Control19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotw_Control19"):
                opp_val = getattr(value, "iotw_Control19", None)
                setattr(value, "iotw_Control19", self)

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
    def iotw_Connection(self):
        return self.__iotw_Connection

    @iotw_Connection.setter
    def iotw_Connection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_Connection__iotw_Connection", None)
        self.__iotw_Connection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotw_StateControl"):
                opp_val = getattr(old_value, "iotw_StateControl", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotw_StateControl"):
                opp_val = getattr(value, "iotw_StateControl", None)
                if opp_val is None:
                    setattr(value, "iotw_StateControl", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class iotw_StateControl(Control):

    def __init__(self, constraints: str, iotw_StateControl: set["iotw_Connection"] = None, iotw_StateControl5: set["iotw_Connection"] = None, iotw_StateControl13: "iotw_StateSchema" = None):
        self.constraints = constraints
        self.iotw_StateControl = iotw_StateControl if iotw_StateControl is not None else set()
        self.iotw_StateControl5 = iotw_StateControl5 if iotw_StateControl5 is not None else set()
        self.iotw_StateControl13 = iotw_StateControl13
        
    @property
    def constraints(self) -> str:
        return self.__constraints

    @constraints.setter
    def constraints(self, constraints: str):
        self.__constraints = constraints

    @property
    def iotw_StateControl5(self):
        return self.__iotw_StateControl5

    @iotw_StateControl5.setter
    def iotw_StateControl5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_StateControl__iotw_StateControl5", None)
        self.__iotw_StateControl5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iotw_Connection6"):
                    opp_val = getattr(item, "iotw_Connection6", None)
                    
                    if opp_val == self:
                        setattr(item, "iotw_Connection6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iotw_Connection6"):
                    opp_val = getattr(item, "iotw_Connection6", None)
                    
                    setattr(item, "iotw_Connection6", self)
                    

    @property
    def iotw_StateControl13(self):
        return self.__iotw_StateControl13

    @iotw_StateControl13.setter
    def iotw_StateControl13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_StateControl__iotw_StateControl13", None)
        self.__iotw_StateControl13 = value
        
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
    def iotw_StateControl(self):
        return self.__iotw_StateControl

    @iotw_StateControl.setter
    def iotw_StateControl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_StateControl__iotw_StateControl", None)
        self.__iotw_StateControl = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iotw_Connection"):
                    opp_val = getattr(item, "iotw_Connection", None)
                    
                    if opp_val == self:
                        setattr(item, "iotw_Connection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iotw_Connection"):
                    opp_val = getattr(item, "iotw_Connection", None)
                    
                    setattr(item, "iotw_Connection", self)
                    

class iotw_ConnectivityControl(Control):

    def __init__(self, constraints: str, connectivities: "iotw_Mainboard" = None, ConnectivityControl: "iotw_Mainboard" = None):
        self.constraints = constraints
        self.connectivities = connectivities
        self.ConnectivityControl = ConnectivityControl
        
    @property
    def constraints(self) -> str:
        return self.__constraints

    @constraints.setter
    def constraints(self, constraints: str):
        self.__constraints = constraints

    @property
    def ConnectivityControl(self):
        return self.__ConnectivityControl

    @ConnectivityControl.setter
    def ConnectivityControl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_ConnectivityControl__ConnectivityControl", None)
        self.__ConnectivityControl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mainboard11"):
                opp_val = getattr(old_value, "mainboard11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mainboard11"):
                opp_val = getattr(value, "mainboard11", None)
                if opp_val is None:
                    setattr(value, "mainboard11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connectivities(self):
        return self.__connectivities

    @connectivities.setter
    def connectivities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_ConnectivityControl__connectivities", None)
        self.__connectivities = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Mainboard2"):
                opp_val = getattr(old_value, "Mainboard2", None)
                if opp_val == self:
                    setattr(old_value, "Mainboard2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Mainboard2"):
                opp_val = getattr(value, "Mainboard2", None)
                setattr(value, "Mainboard2", self)

    def modifyPin(self, pin: str):
        # TODO: Implement modifyPin method
        pass

    def getPinConnecteds(self) -> str:
        # TODO: Implement getPinConnecteds method
        pass

    def getPins(self) -> str:
        # TODO: Implement getPins method
        pass

class iotw_Mainboard(ABC):

    def __init__(self, name: str, Mainboard: "iotw_IOControl" = None, Mainboard2: "iotw_ConnectivityControl" = None, mainboard11: set["iotw_ConnectivityControl"] = None, mainboard: set["iotw_IOControl"] = None):
        self.name = name
        self.Mainboard = Mainboard
        self.Mainboard2 = Mainboard2
        self.mainboard11 = mainboard11 if mainboard11 is not None else set()
        self.mainboard = mainboard if mainboard is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mainboard11(self):
        return self.__mainboard11

    @mainboard11.setter
    def mainboard11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_Mainboard__mainboard11", None)
        self.__mainboard11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConnectivityControl"):
                    opp_val = getattr(item, "ConnectivityControl", None)
                    
                    if opp_val == self:
                        setattr(item, "ConnectivityControl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConnectivityControl"):
                    opp_val = getattr(item, "ConnectivityControl", None)
                    
                    setattr(item, "ConnectivityControl", self)
                    

    @property
    def Mainboard2(self):
        return self.__Mainboard2

    @Mainboard2.setter
    def Mainboard2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotw_Mainboard__Mainboard2", None)
        self.__Mainboard2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connectivities"):
                opp_val = getattr(old_value, "connectivities", None)
                if opp_val == self:
                    setattr(old_value, "connectivities", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connectivities"):
                opp_val = getattr(value, "connectivities", None)
                setattr(value, "connectivities", self)

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
            if hasattr(old_value, "controls"):
                opp_val = getattr(old_value, "controls", None)
                if opp_val == self:
                    setattr(old_value, "controls", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "controls"):
                opp_val = getattr(value, "controls", None)
                setattr(value, "controls", self)

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
                if hasattr(item, "IOControl"):
                    opp_val = getattr(item, "IOControl", None)
                    
                    if opp_val == self:
                        setattr(item, "IOControl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IOControl"):
                    opp_val = getattr(item, "IOControl", None)
                    
                    setattr(item, "IOControl", self)
                    

    def findPin(self, pin: str) -> str:
        # TODO: Implement findPin method
        pass

    def getPins(self) -> str:
        # TODO: Implement getPins method
        pass

    def modifyPin(self, pin: str):
        # TODO: Implement modifyPin method
        pass

    def addConnectivity(self, control: str):
        # TODO: Implement addConnectivity method
        pass

    def removeControl(self, control: str):
        # TODO: Implement removeControl method
        pass

    def addControl(self, control: str):
        # TODO: Implement addControl method
        pass

    def removeConnectivity(self, control: str):
        # TODO: Implement removeConnectivity method
        pass

    def getPinConnecteds(self) -> str:
        # TODO: Implement getPinConnecteds method
        pass
