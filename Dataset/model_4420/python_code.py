from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class PWM_MODE(Enum):
    HIGH = "HIGH"
    LOW = "LOW"
    NONE = "NONE"
    UNKNOWN = "UNKNOWN"
class PIN_MODE(Enum):
    INPUT = "INPUT"
    OUTPUT = "OUTPUT"
    ANALOG = "ANALOG"
    PWM = "PWM"
    SERVO = "SERVO"
    SHIFT = "SHIFT"
    I2C = "I2C"
    UNKNOWN = "UNKNOWN"
class ARDUINO_BOARD_KIND(Enum):
    LILYPAD_168 = "LILYPAD_168"
    MINI_328P = "MINI_328P"
    MINI_168 = "MINI_168"
    UNKNOWN = "UNKNOWN"
    ATMEGA_168 = "ATMEGA_168"
    ATMEGA_8 = "ATMEGA_8"
    BT_ATMEGA_168 = "BT_ATMEGA_168"
class ARDUINO_STATUS_MODE(Enum):
    CONNECTED = "CONNECTED"
    DISCONNECTED = "DISCONNECTED"
    TRANSMITTING = "TRANSMITTING"
class ARDUINO_FIRMWARE_MODE(Enum):
    ARDUINO_FIRMATA_V22_I2C = "ARDUINO_FIRMATA_V22_I2C"
    ARDUINO_FIRMATA_V21_I2C = "ARDUINO_FIRMATA_V21_I2C"
    ARDUINO_FIRMATA_V10_SERVO = "ARDUINO_FIRMATA_V10_SERVO"
    ARDUINO_FIRMATA_V20_SERVO = "ARDUINO_FIRMATA_V20_SERVO"
    ARDUINO_FIRMATA_V11_SERVO = "ARDUINO_FIRMATA_V11_SERVO"
    ARDUINO_FIRMATA_V23_SERVO = "ARDUINO_FIRMATA_V23_SERVO"
    ARDUINO_FIRMATA_V22_SERVO = "ARDUINO_FIRMATA_V22_SERVO"
    ARDUINO_FIRMATA_V21_SERVO = "ARDUINO_FIRMATA_V21_SERVO"
    ARDUINO_DEFAULT = "ARDUINO_DEFAULT"
    ARDUINO_FIRMATA_V10 = "ARDUINO_FIRMATA_V10"
    ARDUINO_FIRMATA_V20 = "ARDUINO_FIRMATA_V20"
    ARDUINO_FIRMATA_V11 = "ARDUINO_FIRMATA_V11"
    ARDUINO_FIRMATA_V23 = "ARDUINO_FIRMATA_V23"
    ARDUINO_FIRMATA_V22 = "ARDUINO_FIRMATA_V22"
    ARDUINO_FIRMATA_V21 = "ARDUINO_FIRMATA_V21"
    ARDUINO_FIRMATA_V10_I2C = "ARDUINO_FIRMATA_V10_I2C"
    ARDUINO_FIRMATA_V11_I2C = "ARDUINO_FIRMATA_V11_I2C"
    ARDUINO_FIRMATA_V20_I2C = "ARDUINO_FIRMATA_V20_I2C"
    ARDUINO_FIRMATA_V23_I2C = "ARDUINO_FIRMATA_V23_I2C"
class PIN_MAPPING(Enum):
    PIN_AREF = "PIN_AREF"
    PIN_TX_I = "PIN_TX_I"
    PIN_TX = "PIN_TX"
    PIN_RX = "PIN_RX"
    PIN_D2 = "PIN_D2"
    PIN_D3 = "PIN_D3"
    PIN_D4 = "PIN_D4"
    PIN_D5 = "PIN_D5"
    PIN_D6 = "PIN_D6"
    PIN_D7 = "PIN_D7"
    PIN_D8 = "PIN_D8"
    PIN_D9 = "PIN_D9"
    PIN_D10 = "PIN_D10"
    PIN_D11 = "PIN_D11"
    PIN_D12 = "PIN_D12"
    PIN_D13 = "PIN_D13"
    PIN_D14 = "PIN_D14"
    PIN_D15 = "PIN_D15"
    PIN_D16 = "PIN_D16"
    PIN_D17 = "PIN_D17"
    PIN_D18 = "PIN_D18"
    PIN_D19 = "PIN_D19"
    PIN_D20 = "PIN_D20"
    PIN_A3 = "PIN_A3"
    PIN_A4 = "PIN_A4"
    PIN_A5 = "PIN_A5"
    PIN_A6 = "PIN_A6"
    PIN_A7 = "PIN_A7"
    PIN_A8 = "PIN_A8"
    PIN_A9 = "PIN_A9"
    PIN_A10 = "PIN_A10"
    PIN_A11 = "PIN_A11"
    PIN_A12 = "PIN_A12"
    PIN_A13 = "PIN_A13"
    PIN_A14 = "PIN_A14"
    PIN_A15 = "PIN_A15"
    PIN_VIN = "PIN_VIN"
    PIN_TX_O = "PIN_TX_O"
    PIN_D22 = "PIN_D22"
    PIN_D23 = "PIN_D23"
    PIN_D24 = "PIN_D24"
    PIN_D25 = "PIN_D25"
    PIN_D26 = "PIN_D26"
    PIN_D27 = "PIN_D27"
    PIN_D28 = "PIN_D28"
    PIN_D29 = "PIN_D29"
    PIN_D30 = "PIN_D30"
    PIN_D31 = "PIN_D31"
    PIN_D32 = "PIN_D32"
    PIN_D33 = "PIN_D33"
    PIN_D34 = "PIN_D34"
    PIN_D35 = "PIN_D35"
    PIN_D36 = "PIN_D36"
    PIN_D37 = "PIN_D37"
    PIN_D38 = "PIN_D38"
    PIN_D39 = "PIN_D39"
    PIN_D40 = "PIN_D40"
    PIN_D21 = "PIN_D21"
    PIN_GND_D = "PIN_GND_D"
    PIN_3V3_1 = "PIN_3V3_1"
    PIN_3V3_2 = "PIN_3V3_2"
    PIN_5V = "PIN_5V"
    PIN_9V = "PIN_9V"
    PIN_GND_9V = "PIN_GND_9V"
    PIN_GND_3V = "PIN_GND_3V"
    PIN_RST = "PIN_RST"
    PIN_A0 = "PIN_A0"
    PIN_A1 = "PIN_A1"
    PIN_A2 = "PIN_A2"
    PIN_D48 = "PIN_D48"
    PIN_D49 = "PIN_D49"
    PIN_D50 = "PIN_D50"
    PIN_D51 = "PIN_D51"
    PIN_D52 = "PIN_D52"
    PIN_IO7 = "PIN_IO7"
    UNKNOWN = "UNKNOWN"
    PIN_A16 = "PIN_A16"
    PIN_A17 = "PIN_A17"
    PIN_A18 = "PIN_A18"
    PIN_A19 = "PIN_A19"
    PIN_A20 = "PIN_A20"
    PIN_A21 = "PIN_A21"
    PIN_A22 = "PIN_A22"
    PIN_A23 = "PIN_A23"
    PIN_A24 = "PIN_A24"
    PIN_D41 = "PIN_D41"
    PIN_D42 = "PIN_D42"
    PIN_D43 = "PIN_D43"
    PIN_D44 = "PIN_D44"
    PIN_D45 = "PIN_D45"
    PIN_D46 = "PIN_D46"
    PIN_D47 = "PIN_D47"
class ARDUINO_VER_BRAND_NAME(Enum):
    ARDUINO_DIECIMILA = "ARDUINO_DIECIMILA"
    ARDUINO_DUEMILANOVE = "ARDUINO_DUEMILANOVE"
    ARDUINO_NANO = "ARDUINO_NANO"
    FUNNEL_IO = "FUNNEL_IO"
    LILYPAD = "LILYPAD"
    ARDUINO_MINI = "ARDUINO_MINI"
    ARDUINO_UNO = "ARDUINO_UNO"
    ARDUINO_LEONARDO = "ARDUINO_LEONARDO"
    ARDUINO_PRO = "ARDUINO_PRO"
    UNKNOWN = "UNKNOWN"
class ARDUINO_ATMEGA_168_SERIES(Enum):
    _168_ATMEGA_32U4 = "_168_ATMEGA_32U4"
    _168_ATMEGA_1280 = "_168_ATMEGA_1280"
    _168_ATMEGA_328_PRO_8MHz = "_168_ATMEGA_328_PRO_8MHz"
    _168_ATMEGA_328 = "_168_ATMEGA_328"
    _168_ATMEGA_DIECIMILA = "_168_ATMEGA_DIECIMILA"
    _168_NG = "_168_NG"
    _168_PRO = "_168_PRO"
    UNKNOWN = "UNKNOWN"
    _168_ATMEGA_168 = "_168_ATMEGA_168"
class ARDUINO_REPORT_MODE(Enum):
    ACTIVATE = "ACTIVATE"
    DEACTIVATE = "DEACTIVATE"
class ARDUINO_COMM(Enum):
    USB = "USB"
    NONE = "NONE"
    XBEE_SERIES_1 = "XBEE_SERIES_1"
    XBEE_PRO = "XBEE_PRO"
    ETHERNET = "ETHERNET"
    BLUETOOTH = "BLUETOOTH"
    MINI_USB = "MINI_USB"
    UART = "UART"
class ARDUINO_BOARD_UID(Enum):
    DUEMILANOVE_ATMEGA_328 = "DUEMILANOVE_ATMEGA_328"
    DUEMILANOVE_ATMEGA_168 = "DUEMILANOVE_ATMEGA_168"
    MINI_PRO_ATMEGA_168 = "MINI_PRO_ATMEGA_168"
    NANO_30_ATMEGA328 = "NANO_30_ATMEGA328"
    NANO_23_ATMEGA168 = "NANO_23_ATMEGA168"
    FUNNEL_IO_ATMEGA328P = "FUNNEL_IO_ATMEGA328P"
    PRO_ATMEGA_168 = "PRO_ATMEGA_168"
    PRO_ATMEGA_328 = "PRO_ATMEGA_328"
    BT_ATMEGA_168 = "BT_ATMEGA_168"
    PRO_MINI_ATMEGA_168 = "PRO_MINI_ATMEGA_168"
    UNO_ATMEGA328 = "UNO_ATMEGA328"
    LEONARDO_ATMEGA32U4 = "LEONARDO_ATMEGA32U4"
    PLACEHOLDER_VOID_BOARD = "PLACEHOLDER_VOID_BOARD"
    DIECMILA_ATMEGA_168 = "DIECMILA_ATMEGA_168"
    DIECIMILA_ATMEGA328 = "DIECIMILA_ATMEGA328"
    DIECIMILA_ATMEGA_328P = "DIECIMILA_ATMEGA_328P"
    MINI_ATMEGA_168 = "MINI_ATMEGA_168"
    MEGA_ATMEGA_1280 = "MEGA_ATMEGA_1280"
    LILIPAD_ATMEGA_328V = "LILIPAD_ATMEGA_328V"


############################################
# Definition of Classes
############################################

class arduino_Bench:

    def __init__(self, name: str, arduino_Bench: set["arduino_Arduino"] = None):
        self.name = name
        self.arduino_Bench = arduino_Bench if arduino_Bench is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def arduino_Bench(self):
        return self.__arduino_Bench

    @arduino_Bench.setter
    def arduino_Bench(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Bench__arduino_Bench", None)
        self.__arduino_Bench = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_Arduino24"):
                    opp_val = getattr(item, "arduino_Arduino24", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_Arduino24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_Arduino24"):
                    opp_val = getattr(item, "arduino_Arduino24", None)
                    
                    setattr(item, "arduino_Arduino24", self)
                    

class Port:

    pass
class arduino_Port:

    def __init__(self, map: str, report: str, channel: int, name: str):
        self.map = map
        self.report = report
        self.channel = channel
        self.name = name
        
        pass
    @property
    def report(self):
        return self.__report

    @report.setter
    def report(self, report: str):
        self.__report = report


    @property
    def map(self):
        return self.__map

    @map.setter
    def map(self, map: str):
        self.__map = map


    @property
    def channel(self):
        return self.__channel

    @channel.setter
    def channel(self, channel: int):
        self.__channel = channel


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class arduino_AREFPort(Port):

    pass
class arduino_PortVIN(Port):

    pass
class arduino_PortIO7(Port):

    pass
class arduino_Port5V(Port):

    pass
class arduino_Port9V(Port):

    pass
class arduino_TxPort(Port):

    pass
class arduino_AnalogPort(Port):

    def __init__(self, value: float, arduino_AnalogPort: "arduino_Arduino" = None):
        self.value = value
        self.arduino_AnalogPort = arduino_AnalogPort
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value


    @property
    def arduino_AnalogPort(self):
        return self.__arduino_AnalogPort

    @arduino_AnalogPort.setter
    def arduino_AnalogPort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_AnalogPort__arduino_AnalogPort", None)
        self.__arduino_AnalogPort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Arduino2"):
                opp_val = getattr(old_value, "arduino_Arduino2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Arduino2"):
                opp_val = getattr(value, "arduino_Arduino2", None)
                if opp_val is None:
                    setattr(value, "arduino_Arduino2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class arduino_DigitalPort(Port):

    def __init__(self, value: int, arduino_DigitalPort: "arduino_Arduino" = None):
        self.value = value
        self.arduino_DigitalPort = arduino_DigitalPort
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


    @property
    def arduino_DigitalPort(self):
        return self.__arduino_DigitalPort

    @arduino_DigitalPort.setter
    def arduino_DigitalPort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_DigitalPort__arduino_DigitalPort", None)
        self.__arduino_DigitalPort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Arduino"):
                opp_val = getattr(old_value, "arduino_Arduino", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Arduino"):
                opp_val = getattr(value, "arduino_Arduino", None)
                if opp_val is None:
                    setattr(value, "arduino_Arduino", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class arduino_RstPort(Port):

    pass
class arduino_Port3V3(Port):

    pass
class arduino_RxPort(Port):

    pass
class arduino_GndPort(Port):

    pass
class arduino_Arduino:

    def __init__(self, label: str, comm: str, ver: str, board: str, series: str, firmataMode: str, lockedPin: str, synchronizing: bool, status: str, kind: str, name: str, arduino_Arduino6: set["arduino_GndPort"] = None, arduino_Arduino8: "arduino_RxPort" = None, arduino_Arduino10: "arduino_Port3V3" = None, arduino_Arduino: set["arduino_DigitalPort"] = None, arduino_Arduino2: set["arduino_AnalogPort"] = None, arduino_Arduino4: "arduino_TxPort" = None, arduino_Arduino14: "arduino_Port9V" = None, arduino_Arduino16: "arduino_Port5V" = None, arduino_Arduino18: "arduino_PortIO7" = None, arduino_Arduino20: "arduino_PortVIN" = None, arduino_Arduino22: "arduino_AREFPort" = None, arduino_Arduino12: "arduino_RstPort" = None, arduino_Arduino24: "arduino_Bench" = None):
        self.label = label
        self.comm = comm
        self.ver = ver
        self.board = board
        self.series = series
        self.firmataMode = firmataMode
        self.lockedPin = lockedPin
        self.synchronizing = synchronizing
        self.status = status
        self.kind = kind
        self.name = name
        self.arduino_Arduino6 = arduino_Arduino6 if arduino_Arduino6 is not None else set()
        self.arduino_Arduino8 = arduino_Arduino8
        self.arduino_Arduino10 = arduino_Arduino10
        self.arduino_Arduino = arduino_Arduino if arduino_Arduino is not None else set()
        self.arduino_Arduino2 = arduino_Arduino2 if arduino_Arduino2 is not None else set()
        self.arduino_Arduino4 = arduino_Arduino4
        self.arduino_Arduino14 = arduino_Arduino14
        self.arduino_Arduino16 = arduino_Arduino16
        self.arduino_Arduino18 = arduino_Arduino18
        self.arduino_Arduino20 = arduino_Arduino20
        self.arduino_Arduino22 = arduino_Arduino22
        self.arduino_Arduino12 = arduino_Arduino12
        self.arduino_Arduino24 = arduino_Arduino24
        
        pass
    @property
    def firmataMode(self):
        return self.__firmataMode

    @firmataMode.setter
    def firmataMode(self, firmataMode: str):
        self.__firmataMode = firmataMode


    @property
    def comm(self):
        return self.__comm

    @comm.setter
    def comm(self, comm: str):
        self.__comm = comm


    @property
    def ver(self):
        return self.__ver

    @ver.setter
    def ver(self, ver: str):
        self.__ver = ver


    @property
    def synchronizing(self):
        return self.__synchronizing

    @synchronizing.setter
    def synchronizing(self, synchronizing: bool):
        self.__synchronizing = synchronizing


    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def board(self):
        return self.__board

    @board.setter
    def board(self, board: str):
        self.__board = board


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status


    @property
    def series(self):
        return self.__series

    @series.setter
    def series(self, series: str):
        self.__series = series


    @property
    def lockedPin(self):
        return self.__lockedPin

    @lockedPin.setter
    def lockedPin(self, lockedPin: str):
        self.__lockedPin = lockedPin


    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def arduino_Arduino8(self):
        return self.__arduino_Arduino8

    @arduino_Arduino8.setter
    def arduino_Arduino8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Arduino__arduino_Arduino8", None)
        self.__arduino_Arduino8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_RxPort"):
                opp_val = getattr(old_value, "arduino_RxPort", None)
                if opp_val == self:
                    setattr(old_value, "arduino_RxPort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_RxPort"):
                opp_val = getattr(value, "arduino_RxPort", None)
                setattr(value, "arduino_RxPort", self)

    @property
    def arduino_Arduino20(self):
        return self.__arduino_Arduino20

    @arduino_Arduino20.setter
    def arduino_Arduino20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Arduino__arduino_Arduino20", None)
        self.__arduino_Arduino20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_PortVIN"):
                opp_val = getattr(old_value, "arduino_PortVIN", None)
                if opp_val == self:
                    setattr(old_value, "arduino_PortVIN", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_PortVIN"):
                opp_val = getattr(value, "arduino_PortVIN", None)
                setattr(value, "arduino_PortVIN", self)

    @property
    def arduino_Arduino22(self):
        return self.__arduino_Arduino22

    @arduino_Arduino22.setter
    def arduino_Arduino22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Arduino__arduino_Arduino22", None)
        self.__arduino_Arduino22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_AREFPort"):
                opp_val = getattr(old_value, "arduino_AREFPort", None)
                if opp_val == self:
                    setattr(old_value, "arduino_AREFPort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_AREFPort"):
                opp_val = getattr(value, "arduino_AREFPort", None)
                setattr(value, "arduino_AREFPort", self)

    @property
    def arduino_Arduino4(self):
        return self.__arduino_Arduino4

    @arduino_Arduino4.setter
    def arduino_Arduino4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Arduino__arduino_Arduino4", None)
        self.__arduino_Arduino4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_TxPort"):
                opp_val = getattr(old_value, "arduino_TxPort", None)
                if opp_val == self:
                    setattr(old_value, "arduino_TxPort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_TxPort"):
                opp_val = getattr(value, "arduino_TxPort", None)
                setattr(value, "arduino_TxPort", self)

    @property
    def arduino_Arduino16(self):
        return self.__arduino_Arduino16

    @arduino_Arduino16.setter
    def arduino_Arduino16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Arduino__arduino_Arduino16", None)
        self.__arduino_Arduino16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Port5V"):
                opp_val = getattr(old_value, "arduino_Port5V", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Port5V", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Port5V"):
                opp_val = getattr(value, "arduino_Port5V", None)
                setattr(value, "arduino_Port5V", self)

    @property
    def arduino_Arduino14(self):
        return self.__arduino_Arduino14

    @arduino_Arduino14.setter
    def arduino_Arduino14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Arduino__arduino_Arduino14", None)
        self.__arduino_Arduino14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Port9V"):
                opp_val = getattr(old_value, "arduino_Port9V", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Port9V", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Port9V"):
                opp_val = getattr(value, "arduino_Port9V", None)
                setattr(value, "arduino_Port9V", self)

    @property
    def arduino_Arduino12(self):
        return self.__arduino_Arduino12

    @arduino_Arduino12.setter
    def arduino_Arduino12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Arduino__arduino_Arduino12", None)
        self.__arduino_Arduino12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_RstPort"):
                opp_val = getattr(old_value, "arduino_RstPort", None)
                if opp_val == self:
                    setattr(old_value, "arduino_RstPort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_RstPort"):
                opp_val = getattr(value, "arduino_RstPort", None)
                setattr(value, "arduino_RstPort", self)

    @property
    def arduino_Arduino24(self):
        return self.__arduino_Arduino24

    @arduino_Arduino24.setter
    def arduino_Arduino24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Arduino__arduino_Arduino24", None)
        self.__arduino_Arduino24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Bench"):
                opp_val = getattr(old_value, "arduino_Bench", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Bench"):
                opp_val = getattr(value, "arduino_Bench", None)
                if opp_val is None:
                    setattr(value, "arduino_Bench", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def arduino_Arduino6(self):
        return self.__arduino_Arduino6

    @arduino_Arduino6.setter
    def arduino_Arduino6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Arduino__arduino_Arduino6", None)
        self.__arduino_Arduino6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_GndPort"):
                    opp_val = getattr(item, "arduino_GndPort", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_GndPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_GndPort"):
                    opp_val = getattr(item, "arduino_GndPort", None)
                    
                    setattr(item, "arduino_GndPort", self)
                    

    @property
    def arduino_Arduino18(self):
        return self.__arduino_Arduino18

    @arduino_Arduino18.setter
    def arduino_Arduino18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Arduino__arduino_Arduino18", None)
        self.__arduino_Arduino18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_PortIO7"):
                opp_val = getattr(old_value, "arduino_PortIO7", None)
                if opp_val == self:
                    setattr(old_value, "arduino_PortIO7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_PortIO7"):
                opp_val = getattr(value, "arduino_PortIO7", None)
                setattr(value, "arduino_PortIO7", self)

    @property
    def arduino_Arduino2(self):
        return self.__arduino_Arduino2

    @arduino_Arduino2.setter
    def arduino_Arduino2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Arduino__arduino_Arduino2", None)
        self.__arduino_Arduino2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_AnalogPort"):
                    opp_val = getattr(item, "arduino_AnalogPort", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_AnalogPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_AnalogPort"):
                    opp_val = getattr(item, "arduino_AnalogPort", None)
                    
                    setattr(item, "arduino_AnalogPort", self)
                    

    @property
    def arduino_Arduino10(self):
        return self.__arduino_Arduino10

    @arduino_Arduino10.setter
    def arduino_Arduino10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Arduino__arduino_Arduino10", None)
        self.__arduino_Arduino10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Port3V3"):
                opp_val = getattr(old_value, "arduino_Port3V3", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Port3V3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Port3V3"):
                opp_val = getattr(value, "arduino_Port3V3", None)
                setattr(value, "arduino_Port3V3", self)

    @property
    def arduino_Arduino(self):
        return self.__arduino_Arduino

    @arduino_Arduino.setter
    def arduino_Arduino(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Arduino__arduino_Arduino", None)
        self.__arduino_Arduino = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_DigitalPort"):
                    opp_val = getattr(item, "arduino_DigitalPort", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_DigitalPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_DigitalPort"):
                    opp_val = getattr(item, "arduino_DigitalPort", None)
                    
                    setattr(item, "arduino_DigitalPort", self)
                    

    def getPorts(self) :
        # TODO: Implement getPorts method
        pass

    def getCommPorts(self) :
        # TODO: Implement getCommPorts method
        pass

    def getAnalogicPortFromChannel(self, arduino_channel) :
        # TODO: Implement getAnalogicPortFromChannel method
        pass

    def getDigitalPort(self, arduino_pin) :
        # TODO: Implement getDigitalPort method
        pass

    def synchronizingArduinoHardware(self, arduino_pin) :
        # TODO: Implement synchronizingArduinoHardware method
        pass

    def synchronizingArduinoModel(self, arduino_pin) :
        # TODO: Implement synchronizingArduinoModel method
        pass

    def getAnalogicPort(self, arduino_pin) :
        # TODO: Implement getAnalogicPort method
        pass

    def reportDigitalPin(self, arduino_mode, arduino_pin):
        # TODO: Implement reportDigitalPin method
        pass

    def analogIOMessage(self, arduino_pin, arduino_data):
        # TODO: Implement analogIOMessage method
        pass

    def reportAnalogPin(self, arduino_mode, arduino_pin):
        # TODO: Implement reportAnalogPin method
        pass

    def digitalIOMessage(self, arduino_pin, arduino_data):
        # TODO: Implement digitalIOMessage method
        pass

    def getDigitalPortFromChannel(self, arduino_channel) :
        # TODO: Implement getDigitalPortFromChannel method
        pass
