####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
ARDUINO_VER_BRAND_NAME: Enumeration = Enumeration(
    name="ARDUINO_VER_BRAND_NAME",
    literals={
            EnumerationLiteral(name="ARDUINO_DIECIMILA"),
			EnumerationLiteral(name="ARDUINO_DUEMILANOVE"),
			EnumerationLiteral(name="ARDUINO_NANO"),
			EnumerationLiteral(name="FUNNEL_IO"),
			EnumerationLiteral(name="LILYPAD"),
			EnumerationLiteral(name="ARDUINO_MINI"),
			EnumerationLiteral(name="ARDUINO_UNO"),
			EnumerationLiteral(name="ARDUINO_LEONARDO"),
			EnumerationLiteral(name="ARDUINO_PRO"),
			EnumerationLiteral(name="UNKNOWN")
    }
)

ARDUINO_BOARD_KIND: Enumeration = Enumeration(
    name="ARDUINO_BOARD_KIND",
    literals={
            EnumerationLiteral(name="ATMEGA_168"),
			EnumerationLiteral(name="ATMEGA_8"),
			EnumerationLiteral(name="BT_ATMEGA_168"),
			EnumerationLiteral(name="LILYPAD_168"),
			EnumerationLiteral(name="MINI_328P"),
			EnumerationLiteral(name="MINI_168"),
			EnumerationLiteral(name="UNKNOWN")
    }
)

ARDUINO_COMM: Enumeration = Enumeration(
    name="ARDUINO_COMM",
    literals={
            EnumerationLiteral(name="USB"),
			EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="XBEE_SERIES_1"),
			EnumerationLiteral(name="XBEE_PRO"),
			EnumerationLiteral(name="ETHERNET"),
			EnumerationLiteral(name="BLUETOOTH"),
			EnumerationLiteral(name="MINI_USB"),
			EnumerationLiteral(name="UART")
    }
)

PIN_MAPPING: Enumeration = Enumeration(
    name="PIN_MAPPING",
    literals={
            EnumerationLiteral(name="PIN_D18"),
			EnumerationLiteral(name="PIN_D19"),
			EnumerationLiteral(name="PIN_D20"),
			EnumerationLiteral(name="PIN_D21"),
			EnumerationLiteral(name="PIN_GND_D"),
			EnumerationLiteral(name="PIN_3V3_1"),
			EnumerationLiteral(name="PIN_3V3_2"),
			EnumerationLiteral(name="PIN_5V"),
			EnumerationLiteral(name="PIN_9V"),
			EnumerationLiteral(name="PIN_GND_9V"),
			EnumerationLiteral(name="PIN_GND_3V"),
			EnumerationLiteral(name="PIN_RST"),
			EnumerationLiteral(name="PIN_A0"),
			EnumerationLiteral(name="PIN_A1"),
			EnumerationLiteral(name="PIN_A2"),
			EnumerationLiteral(name="PIN_A3"),
			EnumerationLiteral(name="PIN_AREF"),
			EnumerationLiteral(name="PIN_TX_I"),
			EnumerationLiteral(name="PIN_TX"),
			EnumerationLiteral(name="PIN_RX"),
			EnumerationLiteral(name="PIN_D2"),
			EnumerationLiteral(name="PIN_D3"),
			EnumerationLiteral(name="PIN_D4"),
			EnumerationLiteral(name="PIN_D5"),
			EnumerationLiteral(name="PIN_D6"),
			EnumerationLiteral(name="PIN_D7"),
			EnumerationLiteral(name="PIN_D8"),
			EnumerationLiteral(name="PIN_D9"),
			EnumerationLiteral(name="PIN_D10"),
			EnumerationLiteral(name="PIN_D11"),
			EnumerationLiteral(name="PIN_D12"),
			EnumerationLiteral(name="PIN_D13"),
			EnumerationLiteral(name="PIN_D14"),
			EnumerationLiteral(name="PIN_D15"),
			EnumerationLiteral(name="PIN_D16"),
			EnumerationLiteral(name="PIN_D17"),
			EnumerationLiteral(name="PIN_D44"),
			EnumerationLiteral(name="PIN_D45"),
			EnumerationLiteral(name="PIN_D46"),
			EnumerationLiteral(name="PIN_D47"),
			EnumerationLiteral(name="PIN_D48"),
			EnumerationLiteral(name="PIN_D49"),
			EnumerationLiteral(name="PIN_D50"),
			EnumerationLiteral(name="PIN_D51"),
			EnumerationLiteral(name="PIN_D52"),
			EnumerationLiteral(name="PIN_IO7"),
			EnumerationLiteral(name="UNKNOWN"),
			EnumerationLiteral(name="PIN_A16"),
			EnumerationLiteral(name="PIN_A17"),
			EnumerationLiteral(name="PIN_A18"),
			EnumerationLiteral(name="PIN_A4"),
			EnumerationLiteral(name="PIN_A5"),
			EnumerationLiteral(name="PIN_A6"),
			EnumerationLiteral(name="PIN_A7"),
			EnumerationLiteral(name="PIN_A8"),
			EnumerationLiteral(name="PIN_A9"),
			EnumerationLiteral(name="PIN_A10"),
			EnumerationLiteral(name="PIN_A11"),
			EnumerationLiteral(name="PIN_A12"),
			EnumerationLiteral(name="PIN_A13"),
			EnumerationLiteral(name="PIN_A14"),
			EnumerationLiteral(name="PIN_A15"),
			EnumerationLiteral(name="PIN_VIN"),
			EnumerationLiteral(name="PIN_TX_O"),
			EnumerationLiteral(name="PIN_D22"),
			EnumerationLiteral(name="PIN_D23"),
			EnumerationLiteral(name="PIN_D24"),
			EnumerationLiteral(name="PIN_D25"),
			EnumerationLiteral(name="PIN_D26"),
			EnumerationLiteral(name="PIN_D27"),
			EnumerationLiteral(name="PIN_D28"),
			EnumerationLiteral(name="PIN_D29"),
			EnumerationLiteral(name="PIN_D30"),
			EnumerationLiteral(name="PIN_D31"),
			EnumerationLiteral(name="PIN_D32"),
			EnumerationLiteral(name="PIN_D33"),
			EnumerationLiteral(name="PIN_D34"),
			EnumerationLiteral(name="PIN_D35"),
			EnumerationLiteral(name="PIN_D36"),
			EnumerationLiteral(name="PIN_D37"),
			EnumerationLiteral(name="PIN_D38"),
			EnumerationLiteral(name="PIN_D39"),
			EnumerationLiteral(name="PIN_D40"),
			EnumerationLiteral(name="PIN_D41"),
			EnumerationLiteral(name="PIN_D42"),
			EnumerationLiteral(name="PIN_D43"),
			EnumerationLiteral(name="PIN_A19"),
			EnumerationLiteral(name="PIN_A20"),
			EnumerationLiteral(name="PIN_A21"),
			EnumerationLiteral(name="PIN_A22"),
			EnumerationLiteral(name="PIN_A23"),
			EnumerationLiteral(name="PIN_A24")
    }
)

ARDUINO_ATMEGA_168_SERIES: Enumeration = Enumeration(
    name="ARDUINO_ATMEGA_168_SERIES",
    literals={
            EnumerationLiteral(name="_168_ATMEGA_1280"),
			EnumerationLiteral(name="_168_ATMEGA_328_PRO_8MHz"),
			EnumerationLiteral(name="_168_ATMEGA_328"),
			EnumerationLiteral(name="_168_ATMEGA_DIECIMILA"),
			EnumerationLiteral(name="_168_NG"),
			EnumerationLiteral(name="_168_PRO"),
			EnumerationLiteral(name="UNKNOWN"),
			EnumerationLiteral(name="_168_ATMEGA_168"),
			EnumerationLiteral(name="_168_ATMEGA_32U4")
    }
)

ARDUINO_BOARD_UID: Enumeration = Enumeration(
    name="ARDUINO_BOARD_UID",
    literals={
            EnumerationLiteral(name="MINI_PRO_ATMEGA_168"),
			EnumerationLiteral(name="NANO_30_ATMEGA328"),
			EnumerationLiteral(name="NANO_23_ATMEGA168"),
			EnumerationLiteral(name="FUNNEL_IO_ATMEGA328P"),
			EnumerationLiteral(name="PRO_ATMEGA_168"),
			EnumerationLiteral(name="PRO_ATMEGA_328"),
			EnumerationLiteral(name="BT_ATMEGA_168"),
			EnumerationLiteral(name="PRO_MINI_ATMEGA_168"),
			EnumerationLiteral(name="UNO_ATMEGA328"),
			EnumerationLiteral(name="LEONARDO_ATMEGA32U4"),
			EnumerationLiteral(name="PLACEHOLDER_VOID_BOARD"),
			EnumerationLiteral(name="DIECMILA_ATMEGA_168"),
			EnumerationLiteral(name="DIECIMILA_ATMEGA328"),
			EnumerationLiteral(name="DIECIMILA_ATMEGA_328P"),
			EnumerationLiteral(name="MINI_ATMEGA_168"),
			EnumerationLiteral(name="MEGA_ATMEGA_1280"),
			EnumerationLiteral(name="LILIPAD_ATMEGA_328V"),
			EnumerationLiteral(name="DUEMILANOVE_ATMEGA_328"),
			EnumerationLiteral(name="DUEMILANOVE_ATMEGA_168")
    }
)

ARDUINO_REPORT_MODE: Enumeration = Enumeration(
    name="ARDUINO_REPORT_MODE",
    literals={
            EnumerationLiteral(name="ACTIVATE"),
			EnumerationLiteral(name="DEACTIVATE")
    }
)

ARDUINO_FIRMWARE_MODE: Enumeration = Enumeration(
    name="ARDUINO_FIRMWARE_MODE",
    literals={
            EnumerationLiteral(name="ARDUINO_FIRMATA_V10"),
			EnumerationLiteral(name="ARDUINO_FIRMATA_V20"),
			EnumerationLiteral(name="ARDUINO_FIRMATA_V11"),
			EnumerationLiteral(name="ARDUINO_FIRMATA_V23"),
			EnumerationLiteral(name="ARDUINO_FIRMATA_V22"),
			EnumerationLiteral(name="ARDUINO_FIRMATA_V21"),
			EnumerationLiteral(name="ARDUINO_FIRMATA_V10_I2C"),
			EnumerationLiteral(name="ARDUINO_FIRMATA_V11_I2C"),
			EnumerationLiteral(name="ARDUINO_FIRMATA_V20_I2C"),
			EnumerationLiteral(name="ARDUINO_FIRMATA_V23_I2C"),
			EnumerationLiteral(name="ARDUINO_FIRMATA_V22_I2C"),
			EnumerationLiteral(name="ARDUINO_FIRMATA_V21_I2C"),
			EnumerationLiteral(name="ARDUINO_FIRMATA_V10_SERVO"),
			EnumerationLiteral(name="ARDUINO_FIRMATA_V20_SERVO"),
			EnumerationLiteral(name="ARDUINO_FIRMATA_V11_SERVO"),
			EnumerationLiteral(name="ARDUINO_FIRMATA_V23_SERVO"),
			EnumerationLiteral(name="ARDUINO_FIRMATA_V22_SERVO"),
			EnumerationLiteral(name="ARDUINO_FIRMATA_V21_SERVO"),
			EnumerationLiteral(name="ARDUINO_DEFAULT")
    }
)

ARDUINO_STATUS_MODE: Enumeration = Enumeration(
    name="ARDUINO_STATUS_MODE",
    literals={
            EnumerationLiteral(name="CONNECTED"),
			EnumerationLiteral(name="DISCONNECTED"),
			EnumerationLiteral(name="TRANSMITTING")
    }
)

PIN_MODE: Enumeration = Enumeration(
    name="PIN_MODE",
    literals={
            EnumerationLiteral(name="INPUT"),
			EnumerationLiteral(name="OUTPUT"),
			EnumerationLiteral(name="ANALOG"),
			EnumerationLiteral(name="PWM"),
			EnumerationLiteral(name="SERVO"),
			EnumerationLiteral(name="SHIFT"),
			EnumerationLiteral(name="I2C"),
			EnumerationLiteral(name="UNKNOWN")
    }
)

PWM_MODE: Enumeration = Enumeration(
    name="PWM_MODE",
    literals={
            EnumerationLiteral(name="HIGH"),
			EnumerationLiteral(name="LOW"),
			EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="UNKNOWN")
    }
)

# Classes
arduino_DigitalPort = Class(name="arduino::DigitalPort")
arduino_Arduino = Class(name="arduino::Arduino")
arduino_Port = Class(name="arduino::Port")
arduino_AnalogPort = Class(name="arduino::AnalogPort")
arduino_TxPort = Class(name="arduino::TxPort")
arduino_GndPort = Class(name="arduino::GndPort")
arduino_RxPort = Class(name="arduino::RxPort")
arduino_Port3V3 = Class(name="arduino::Port3V3")
arduino_RstPort = Class(name="arduino::RstPort")
arduino_Port9V = Class(name="arduino::Port9V")
arduino_Port5V = Class(name="arduino::Port5V")
arduino_PortIO7 = Class(name="arduino::PortIO7")
arduino_PortVIN = Class(name="arduino::PortVIN")
arduino_AREFPort = Class(name="arduino::AREFPort")
Port = Class(name="Port")
arduino_Bench = Class(name="arduino::Bench")

# arduino_DigitalPort class attributes and methods
arduino_DigitalPort_value: Property = Property(name="value", type=IntegerType)
arduino_DigitalPort.attributes={arduino_DigitalPort_value}

# arduino_Arduino class attributes and methods
arduino_Arduino_ver: Property = Property(name="ver", type=StringType)
arduino_Arduino_board: Property = Property(name="board", type=StringType)
arduino_Arduino_series: Property = Property(name="series", type=StringType)
arduino_Arduino_kind: Property = Property(name="kind", type=StringType)
arduino_Arduino_name: Property = Property(name="name", type=StringType)
arduino_Arduino_label: Property = Property(name="label", type=StringType)
arduino_Arduino_comm: Property = Property(name="comm", type=StringType)
arduino_Arduino_firmataMode: Property = Property(name="firmataMode", type=StringType)
arduino_Arduino_lockedPin: Property = Property(name="lockedPin", type=StringType)
arduino_Arduino_synchronizing: Property = Property(name="synchronizing", type=BooleanType)
arduino_Arduino_status: Property = Property(name="status", type=StringType)
arduino_Arduino_m_getDigitalPort: Method = Method(name="getDigitalPort", parameters={Parameter(name='pin')}, type=StringType)
arduino_Arduino_m_getPorts: Method = Method(name="getPorts", parameters={}, type=StringType)
arduino_Arduino_m_getCommPorts: Method = Method(name="getCommPorts", parameters={}, type=StringType)
arduino_Arduino_m_getDigitalPortFromChannel: Method = Method(name="getDigitalPortFromChannel", parameters={Parameter(name='channel')}, type=StringType)
arduino_Arduino_m_getAnalogicPortFromChannel: Method = Method(name="getAnalogicPortFromChannel", parameters={Parameter(name='channel')}, type=StringType)
arduino_Arduino_m_digitalIOMessage: Method = Method(name="digitalIOMessage", parameters={Parameter(name='data'), Parameter(name='pin')})
arduino_Arduino_m_analogIOMessage: Method = Method(name="analogIOMessage", parameters={Parameter(name='data'), Parameter(name='pin')})
arduino_Arduino_m_reportAnalogPin: Method = Method(name="reportAnalogPin", parameters={Parameter(name='pin'), Parameter(name='mode')})
arduino_Arduino_m_reportDigitalPin: Method = Method(name="reportDigitalPin", parameters={Parameter(name='pin'), Parameter(name='mode')})
arduino_Arduino_m_synchronizingArduinoModel: Method = Method(name="synchronizingArduinoModel", parameters={Parameter(name='pin')}, type=BooleanType)
arduino_Arduino_m_synchronizingArduinoHardware: Method = Method(name="synchronizingArduinoHardware", parameters={Parameter(name='pin')}, type=BooleanType)
arduino_Arduino_m_getAnalogicPort: Method = Method(name="getAnalogicPort", parameters={Parameter(name='pin')}, type=StringType)
arduino_Arduino_m_getDigitalPort: Method = Method(name="getDigitalPort", parameters={Parameter(name='pin')}, type=StringType)
arduino_Arduino_m_getAnalogicPort: Method = Method(name="getAnalogicPort", parameters={Parameter(name='pin')}, type=StringType)
arduino_Arduino.attributes={arduino_Arduino_label, arduino_Arduino_ver, arduino_Arduino_name, arduino_Arduino_status, arduino_Arduino_series, arduino_Arduino_firmataMode, arduino_Arduino_lockedPin, arduino_Arduino_synchronizing, arduino_Arduino_kind, arduino_Arduino_board, arduino_Arduino_comm}
arduino_Arduino.methods={arduino_Arduino_m_reportAnalogPin, arduino_Arduino_m_getAnalogicPort, arduino_Arduino_m_getDigitalPort, arduino_Arduino_m_getAnalogicPortFromChannel, arduino_Arduino_m_reportDigitalPin, arduino_Arduino_m_digitalIOMessage, arduino_Arduino_m_analogIOMessage, arduino_Arduino_m_getDigitalPortFromChannel, arduino_Arduino_m_getCommPorts, arduino_Arduino_m_getPorts, arduino_Arduino_m_synchronizingArduinoModel, arduino_Arduino_m_synchronizingArduinoHardware, arduino_Arduino_m_getDigitalPort, arduino_Arduino_m_getAnalogicPort}

# arduino_Port class attributes and methods
arduino_Port_map: Property = Property(name="map", type=StringType)
arduino_Port_report: Property = Property(name="report", type=StringType)
arduino_Port_channel: Property = Property(name="channel", type=IntegerType)
arduino_Port_name: Property = Property(name="name", type=StringType)
arduino_Port.attributes={arduino_Port_map, arduino_Port_channel, arduino_Port_report, arduino_Port_name}

# arduino_AnalogPort class attributes and methods
arduino_AnalogPort_value: Property = Property(name="value", type=FloatType)
arduino_AnalogPort.attributes={arduino_AnalogPort_value}

# arduino_TxPort class attributes and methods

# arduino_GndPort class attributes and methods

# arduino_RxPort class attributes and methods

# arduino_Port3V3 class attributes and methods

# arduino_RstPort class attributes and methods

# arduino_Port9V class attributes and methods

# arduino_Port5V class attributes and methods

# arduino_PortIO7 class attributes and methods

# arduino_PortVIN class attributes and methods

# arduino_AREFPort class attributes and methods

# Port class attributes and methods

# arduino_Bench class attributes and methods
arduino_Bench_name: Property = Property(name="name", type=StringType)
arduino_Bench.attributes={arduino_Bench_name}

# Relationships
digitalPorts0: BinaryAssociation = BinaryAssociation(
    name="digitalPorts0",
    ends={
        Property(name="arduino_DigitalPort", type=arduino_Arduino, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Arduino", type=arduino_DigitalPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
analogPorts1: BinaryAssociation = BinaryAssociation(
    name="analogPorts1",
    ends={
        Property(name="arduino_AnalogPort", type=arduino_Arduino, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Arduino2", type=arduino_AnalogPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tx3: BinaryAssociation = BinaryAssociation(
    name="tx3",
    ends={
        Property(name="arduino_TxPort", type=arduino_Arduino, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Arduino4", type=arduino_TxPort, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groundPorts5: BinaryAssociation = BinaryAssociation(
    name="groundPorts5",
    ends={
        Property(name="arduino_GndPort", type=arduino_Arduino, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Arduino6", type=arduino_GndPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rx7: BinaryAssociation = BinaryAssociation(
    name="rx7",
    ends={
        Property(name="arduino_RxPort", type=arduino_Arduino, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Arduino8", type=arduino_RxPort, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pwm3V39: BinaryAssociation = BinaryAssociation(
    name="pwm3V39",
    ends={
        Property(name="arduino_Port3V3", type=arduino_Arduino, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Arduino10", type=arduino_Port3V3, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resetPort11: BinaryAssociation = BinaryAssociation(
    name="resetPort11",
    ends={
        Property(name="arduino_RstPort", type=arduino_Arduino, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Arduino12", type=arduino_RstPort, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pwm9V13: BinaryAssociation = BinaryAssociation(
    name="pwm9V13",
    ends={
        Property(name="arduino_Port9V", type=arduino_Arduino, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Arduino14", type=arduino_Port9V, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pwm5V15: BinaryAssociation = BinaryAssociation(
    name="pwm5V15",
    ends={
        Property(name="arduino_Port5V", type=arduino_Arduino, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Arduino16", type=arduino_Port5V, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
io717: BinaryAssociation = BinaryAssociation(
    name="io717",
    ends={
        Property(name="arduino_PortIO7", type=arduino_Arduino, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Arduino18", type=arduino_PortIO7, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vin19: BinaryAssociation = BinaryAssociation(
    name="vin19",
    ends={
        Property(name="arduino_PortVIN", type=arduino_Arduino, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Arduino20", type=arduino_PortVIN, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aref21: BinaryAssociation = BinaryAssociation(
    name="aref21",
    ends={
        Property(name="arduino_AREFPort", type=arduino_Arduino, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Arduino22", type=arduino_AREFPort, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
boards23: BinaryAssociation = BinaryAssociation(
    name="boards23",
    ends={
        Property(name="arduino_Arduino24", type=arduino_Bench, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Bench", type=arduino_Arduino, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_arduino_Port5V_Port = Generalization(general=Port, specific=arduino_Port5V)
gen_arduino_Port9V_Port = Generalization(general=Port, specific=arduino_Port9V)
gen_arduino_PortIO7_Port = Generalization(general=Port, specific=arduino_PortIO7)
gen_arduino_AREFPort_Port = Generalization(general=Port, specific=arduino_AREFPort)
gen_arduino_PortVIN_Port = Generalization(general=Port, specific=arduino_PortVIN)
gen_arduino_DigitalPort_Port = Generalization(general=Port, specific=arduino_DigitalPort)
gen_arduino_AnalogPort_Port = Generalization(general=Port, specific=arduino_AnalogPort)
gen_arduino_RxPort_Port = Generalization(general=Port, specific=arduino_RxPort)
gen_arduino_TxPort_Port = Generalization(general=Port, specific=arduino_TxPort)
gen_arduino_GndPort_Port = Generalization(general=Port, specific=arduino_GndPort)
gen_arduino_Port3V3_Port = Generalization(general=Port, specific=arduino_Port3V3)
gen_arduino_RstPort_Port = Generalization(general=Port, specific=arduino_RstPort)

# Domain Model
domain_model = DomainModel(
    name="arduino",
    types={arduino_DigitalPort, arduino_Arduino, arduino_Port, arduino_AnalogPort, arduino_TxPort, arduino_GndPort, arduino_RxPort, arduino_Port3V3, arduino_RstPort, arduino_Port9V, arduino_Port5V, arduino_PortIO7, arduino_PortVIN, arduino_AREFPort, Port, arduino_Bench, ARDUINO_VER_BRAND_NAME, ARDUINO_BOARD_KIND, ARDUINO_COMM, PIN_MAPPING, ARDUINO_ATMEGA_168_SERIES, ARDUINO_BOARD_UID, ARDUINO_REPORT_MODE, ARDUINO_FIRMWARE_MODE, ARDUINO_STATUS_MODE, PIN_MODE, PWM_MODE},
    associations={digitalPorts0, analogPorts1, tx3, groundPorts5, rx7, pwm3V39, resetPort11, pwm9V13, pwm5V15, io717, vin19, aref21, boards23},
    generalizations={gen_arduino_Port5V_Port, gen_arduino_Port9V_Port, gen_arduino_PortIO7_Port, gen_arduino_AREFPort_Port, gen_arduino_PortVIN_Port, gen_arduino_DigitalPort_Port, gen_arduino_AnalogPort_Port, gen_arduino_RxPort_Port, gen_arduino_TxPort_Port, gen_arduino_GndPort_Port, gen_arduino_Port3V3_Port, gen_arduino_RstPort_Port},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)