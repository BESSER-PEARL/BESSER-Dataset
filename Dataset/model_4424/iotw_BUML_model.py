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
ConnectionKind: Enumeration = Enumeration(
    name="ConnectionKind",
    literals={
            EnumerationLiteral(name="STATE_FLOW")
    }
)

RouterKind: Enumeration = Enumeration(
    name="RouterKind",
    literals={
            EnumerationLiteral(name="BENDPOINT"),
			EnumerationLiteral(name="MANHATTAN")
    }
)

TypeData: Enumeration = Enumeration(
    name="TypeData",
    literals={
            EnumerationLiteral(name="XML"),
			EnumerationLiteral(name="JSON")
    }
)

# Classes
iotw_Mainboard = Class(name="iotw::Mainboard", is_abstract=True)
iotw_ConnectivityControl = Class(name="iotw::ConnectivityControl", is_abstract=True)
iotw_StateControl = Class(name="iotw::StateControl", is_abstract=True)
iotw_Connection = Class(name="iotw::Connection")
iotw_DataControl = Class(name="iotw::DataControl", is_abstract=True)
iotw_DataExplorer = Class(name="iotw::DataExplorer")
iotw_Control = Class(name="iotw::Control", is_abstract=True)
iotw_IOControl = Class(name="iotw::IOControl", is_abstract=True)
Control = Class(name="Control")
iotw_StateSchema = Class(name="iotw::StateSchema")
iotw_ArduinoUNOR3 = Class(name="iotw::ArduinoUNOR3")
Mainboard = Class(name="Mainboard")
iotw_InputControl = Class(name="iotw::InputControl", is_abstract=True)
IOControl = Class(name="IOControl")
iotw_OutputControl = Class(name="iotw::OutputControl", is_abstract=True)
iotw_Keypad4x4 = Class(name="iotw::Keypad4x4")
InputControl = Class(name="InputControl")
iotw_BluetoothHC06 = Class(name="iotw::BluetoothHC06")
ConnectivityControl = Class(name="ConnectivityControl")
iotw_WifiESP8266 = Class(name="iotw::WifiESP8266")
iotw_Button = Class(name="iotw::Button")
iotw_Buzzer = Class(name="iotw::Buzzer")
iotw_StateFrame = Class(name="iotw::StateFrame")
StateControl = Class(name="StateControl")
iotw_Decision = Class(name="iotw::Decision")
iotw_LED = Class(name="iotw::LED")
OutputControl = Class(name="OutputControl")
iotw_I2CLCD2004 = Class(name="iotw::I2CLCD2004")
iotw_StartPoint = Class(name="iotw::StartPoint")
iotw_EndPoint = Class(name="iotw::EndPoint")

# iotw_Mainboard class attributes and methods
iotw_Mainboard_name: Property = Property(name="name", type=StringType)
iotw_Mainboard_m_addControl: Method = Method(name="addControl", parameters={Parameter(name='control')})
iotw_Mainboard_m_removeControl: Method = Method(name="removeControl", parameters={Parameter(name='control')})
iotw_Mainboard_m_addConnectivity: Method = Method(name="addConnectivity", parameters={Parameter(name='control')})
iotw_Mainboard_m_removeConnectivity: Method = Method(name="removeConnectivity", parameters={Parameter(name='control')})
iotw_Mainboard_m_getPins: Method = Method(name="getPins", parameters={}, type=StringType)
iotw_Mainboard_m_getPinConnecteds: Method = Method(name="getPinConnecteds", parameters={}, type=StringType)
iotw_Mainboard_m_modifyPin: Method = Method(name="modifyPin", parameters={Parameter(name='pin')})
iotw_Mainboard_m_findPin: Method = Method(name="findPin", parameters={Parameter(name='pin')}, type=StringType)
iotw_Mainboard.attributes={iotw_Mainboard_name}
iotw_Mainboard.methods={iotw_Mainboard_m_findPin, iotw_Mainboard_m_getPins, iotw_Mainboard_m_modifyPin, iotw_Mainboard_m_addConnectivity, iotw_Mainboard_m_removeControl, iotw_Mainboard_m_addControl, iotw_Mainboard_m_removeConnectivity, iotw_Mainboard_m_getPinConnecteds}

# iotw_ConnectivityControl class attributes and methods
iotw_ConnectivityControl_constraints: Property = Property(name="constraints", type=StringType)
iotw_ConnectivityControl_m_getPins: Method = Method(name="getPins", parameters={}, type=StringType)
iotw_ConnectivityControl_m_getPinConnecteds: Method = Method(name="getPinConnecteds", parameters={}, type=StringType)
iotw_ConnectivityControl_m_modifyPin: Method = Method(name="modifyPin", parameters={Parameter(name='pin')})
iotw_ConnectivityControl.attributes={iotw_ConnectivityControl_constraints}
iotw_ConnectivityControl.methods={iotw_ConnectivityControl_m_modifyPin, iotw_ConnectivityControl_m_getPinConnecteds, iotw_ConnectivityControl_m_getPins}

# iotw_StateControl class attributes and methods
iotw_StateControl_constraints: Property = Property(name="constraints", type=StringType)
iotw_StateControl.attributes={iotw_StateControl_constraints}

# iotw_Connection class attributes and methods
iotw_Connection_bendpoints: Property = Property(name="bendpoints", type=StringType)
iotw_Connection_routerKind: Property = Property(name="routerKind", type=StringType)
iotw_Connection_kind: Property = Property(name="kind", type=StringType)
iotw_Connection_label: Property = Property(name="label", type=StringType)
iotw_Connection.attributes={iotw_Connection_routerKind, iotw_Connection_label, iotw_Connection_kind, iotw_Connection_bendpoints}

# iotw_DataControl class attributes and methods
iotw_DataControl_constraints: Property = Property(name="constraints", type=StringType)
iotw_DataControl_location: Property = Property(name="location", type=StringType)
iotw_DataControl_type: Property = Property(name="type", type=StringType)
iotw_DataControl.attributes={iotw_DataControl_type, iotw_DataControl_constraints, iotw_DataControl_location}

# iotw_DataExplorer class attributes and methods

# iotw_Control class attributes and methods
iotw_Control_name: Property = Property(name="name", type=StringType)
iotw_Control_id: Property = Property(name="id", type=StringType)
iotw_Control.attributes={iotw_Control_name, iotw_Control_id}

# iotw_IOControl class attributes and methods
iotw_IOControl_constraints: Property = Property(name="constraints", type=StringType)
iotw_IOControl_m_modifyPin: Method = Method(name="modifyPin", parameters={Parameter(name='pin')})
iotw_IOControl_m_getPins: Method = Method(name="getPins", parameters={}, type=StringType)
iotw_IOControl_m_getPinConnecteds: Method = Method(name="getPinConnecteds", parameters={}, type=StringType)
iotw_IOControl.attributes={iotw_IOControl_constraints}
iotw_IOControl.methods={iotw_IOControl_m_getPinConnecteds, iotw_IOControl_m_getPins, iotw_IOControl_m_modifyPin}

# Control class attributes and methods

# iotw_StateSchema class attributes and methods

# iotw_ArduinoUNOR3 class attributes and methods
iotw_ArduinoUNOR3_pin0: Property = Property(name="pin0", type=StringType)
iotw_ArduinoUNOR3_pin1: Property = Property(name="pin1", type=StringType)
iotw_ArduinoUNOR3_pin2: Property = Property(name="pin2", type=StringType)
iotw_ArduinoUNOR3_pin3: Property = Property(name="pin3", type=StringType)
iotw_ArduinoUNOR3_pin4: Property = Property(name="pin4", type=StringType)
iotw_ArduinoUNOR3_pin5: Property = Property(name="pin5", type=StringType)
iotw_ArduinoUNOR3_pin6: Property = Property(name="pin6", type=StringType)
iotw_ArduinoUNOR3_pin7: Property = Property(name="pin7", type=StringType)
iotw_ArduinoUNOR3_pin8: Property = Property(name="pin8", type=StringType)
iotw_ArduinoUNOR3_pin9: Property = Property(name="pin9", type=StringType)
iotw_ArduinoUNOR3_pin10: Property = Property(name="pin10", type=StringType)
iotw_ArduinoUNOR3_pin11: Property = Property(name="pin11", type=StringType)
iotw_ArduinoUNOR3_pin12: Property = Property(name="pin12", type=StringType)
iotw_ArduinoUNOR3_pin13: Property = Property(name="pin13", type=StringType)
iotw_ArduinoUNOR3_pinA0: Property = Property(name="pinA0", type=StringType)
iotw_ArduinoUNOR3_pinA1: Property = Property(name="pinA1", type=StringType)
iotw_ArduinoUNOR3_pinA2: Property = Property(name="pinA2", type=StringType)
iotw_ArduinoUNOR3_pinA3: Property = Property(name="pinA3", type=StringType)
iotw_ArduinoUNOR3_pinA4: Property = Property(name="pinA4", type=StringType)
iotw_ArduinoUNOR3_pinA5: Property = Property(name="pinA5", type=StringType)
iotw_ArduinoUNOR3.attributes={iotw_ArduinoUNOR3_pin3, iotw_ArduinoUNOR3_pin12, iotw_ArduinoUNOR3_pinA0, iotw_ArduinoUNOR3_pin13, iotw_ArduinoUNOR3_pin1, iotw_ArduinoUNOR3_pin5, iotw_ArduinoUNOR3_pin8, iotw_ArduinoUNOR3_pinA1, iotw_ArduinoUNOR3_pinA4, iotw_ArduinoUNOR3_pinA5, iotw_ArduinoUNOR3_pin10, iotw_ArduinoUNOR3_pinA2, iotw_ArduinoUNOR3_pin4, iotw_ArduinoUNOR3_pin6, iotw_ArduinoUNOR3_pin2, iotw_ArduinoUNOR3_pin7, iotw_ArduinoUNOR3_pin9, iotw_ArduinoUNOR3_pin11, iotw_ArduinoUNOR3_pinA3, iotw_ArduinoUNOR3_pin0}

# Mainboard class attributes and methods

# iotw_InputControl class attributes and methods

# IOControl class attributes and methods

# iotw_OutputControl class attributes and methods

# iotw_Keypad4x4 class attributes and methods
iotw_Keypad4x4_keys: Property = Property(name="keys", type=StringType)
iotw_Keypad4x4_rows: Property = Property(name="rows", type=IntegerType)
iotw_Keypad4x4_cols: Property = Property(name="cols", type=IntegerType)
iotw_Keypad4x4_pin1: Property = Property(name="pin1", type=StringType)
iotw_Keypad4x4_pin2: Property = Property(name="pin2", type=StringType)
iotw_Keypad4x4_pin3: Property = Property(name="pin3", type=StringType)
iotw_Keypad4x4_pin4: Property = Property(name="pin4", type=StringType)
iotw_Keypad4x4_pin5: Property = Property(name="pin5", type=StringType)
iotw_Keypad4x4_pin6: Property = Property(name="pin6", type=StringType)
iotw_Keypad4x4_pin7: Property = Property(name="pin7", type=StringType)
iotw_Keypad4x4_pin8: Property = Property(name="pin8", type=StringType)
iotw_Keypad4x4_nameButton1: Property = Property(name="nameButton1", type=StringType)
iotw_Keypad4x4_nameButton2: Property = Property(name="nameButton2", type=StringType)
iotw_Keypad4x4_nameButton3: Property = Property(name="nameButton3", type=StringType)
iotw_Keypad4x4_nameButton4: Property = Property(name="nameButton4", type=StringType)
iotw_Keypad4x4_nameButton5: Property = Property(name="nameButton5", type=StringType)
iotw_Keypad4x4_nameButton6: Property = Property(name="nameButton6", type=StringType)
iotw_Keypad4x4_nameButton7: Property = Property(name="nameButton7", type=StringType)
iotw_Keypad4x4_nameButton8: Property = Property(name="nameButton8", type=StringType)
iotw_Keypad4x4_nameButton9: Property = Property(name="nameButton9", type=StringType)
iotw_Keypad4x4_nameButton0: Property = Property(name="nameButton0", type=StringType)
iotw_Keypad4x4_nameButtonA: Property = Property(name="nameButtonA", type=StringType)
iotw_Keypad4x4_nameButtonB: Property = Property(name="nameButtonB", type=StringType)
iotw_Keypad4x4_nameButtonC: Property = Property(name="nameButtonC", type=StringType)
iotw_Keypad4x4_nameButtonD: Property = Property(name="nameButtonD", type=StringType)
iotw_Keypad4x4_nameButtonHash: Property = Property(name="nameButtonHash", type=StringType)
iotw_Keypad4x4_nameButtonAsterisk: Property = Property(name="nameButtonAsterisk", type=StringType)
iotw_Keypad4x4_m_getButton: Method = Method(name="getButton", parameters={Parameter(name='name')}, type=StringType)
iotw_Keypad4x4.attributes={iotw_Keypad4x4_pin2, iotw_Keypad4x4_nameButton3, iotw_Keypad4x4_nameButtonAsterisk, iotw_Keypad4x4_pin7, iotw_Keypad4x4_nameButtonHash, iotw_Keypad4x4_pin6, iotw_Keypad4x4_nameButton5, iotw_Keypad4x4_nameButtonA, iotw_Keypad4x4_nameButton2, iotw_Keypad4x4_pin8, iotw_Keypad4x4_keys, iotw_Keypad4x4_rows, iotw_Keypad4x4_cols, iotw_Keypad4x4_nameButton1, iotw_Keypad4x4_pin1, iotw_Keypad4x4_nameButton8, iotw_Keypad4x4_pin3, iotw_Keypad4x4_nameButton6, iotw_Keypad4x4_nameButton0, iotw_Keypad4x4_nameButtonD, iotw_Keypad4x4_nameButton4, iotw_Keypad4x4_nameButtonC, iotw_Keypad4x4_nameButtonB, iotw_Keypad4x4_nameButton7, iotw_Keypad4x4_nameButton9, iotw_Keypad4x4_pin5, iotw_Keypad4x4_pin4}
iotw_Keypad4x4.methods={iotw_Keypad4x4_m_getButton}

# InputControl class attributes and methods

# iotw_BluetoothHC06 class attributes and methods
iotw_BluetoothHC06_pinTXD: Property = Property(name="pinTXD", type=StringType)
iotw_BluetoothHC06_pinRXD: Property = Property(name="pinRXD", type=StringType)
iotw_BluetoothHC06_pinGND: Property = Property(name="pinGND", type=StringType)
iotw_BluetoothHC06_pinVCC: Property = Property(name="pinVCC", type=StringType)
iotw_BluetoothHC06.attributes={iotw_BluetoothHC06_pinGND, iotw_BluetoothHC06_pinTXD, iotw_BluetoothHC06_pinRXD, iotw_BluetoothHC06_pinVCC}

# ConnectivityControl class attributes and methods

# iotw_WifiESP8266 class attributes and methods
iotw_WifiESP8266_pinTX: Property = Property(name="pinTX", type=StringType)
iotw_WifiESP8266_pinRX: Property = Property(name="pinRX", type=StringType)
iotw_WifiESP8266_pinVcc: Property = Property(name="pinVcc", type=StringType)
iotw_WifiESP8266_pinGND: Property = Property(name="pinGND", type=StringType)
iotw_WifiESP8266_pinCHPD: Property = Property(name="pinCHPD", type=StringType)
iotw_WifiESP8266_SSID: Property = Property(name="SSID", type=StringType)
iotw_WifiESP8266_Password: Property = Property(name="Password", type=StringType)
iotw_WifiESP8266_Host: Property = Property(name="Host", type=StringType)
iotw_WifiESP8266_Port: Property = Property(name="Port", type=IntegerType)
iotw_WifiESP8266.attributes={iotw_WifiESP8266_Host, iotw_WifiESP8266_Password, iotw_WifiESP8266_pinRX, iotw_WifiESP8266_pinGND, iotw_WifiESP8266_pinTX, iotw_WifiESP8266_pinCHPD, iotw_WifiESP8266_pinVcc, iotw_WifiESP8266_Port, iotw_WifiESP8266_SSID}

# iotw_Button class attributes and methods
iotw_Button_pin1: Property = Property(name="pin1", type=StringType)
iotw_Button.attributes={iotw_Button_pin1}

# iotw_Buzzer class attributes and methods
iotw_Buzzer_pin1: Property = Property(name="pin1", type=StringType)
iotw_Buzzer_pin2: Property = Property(name="pin2", type=StringType)
iotw_Buzzer.attributes={iotw_Buzzer_pin1, iotw_Buzzer_pin2}

# iotw_StateFrame class attributes and methods
iotw_StateFrame_content: Property = Property(name="content", type=StringType)
iotw_StateFrame.attributes={iotw_StateFrame_content}

# StateControl class attributes and methods

# iotw_Decision class attributes and methods

# iotw_LED class attributes and methods
iotw_LED_pin1: Property = Property(name="pin1", type=StringType)
iotw_LED_pin2: Property = Property(name="pin2", type=StringType)
iotw_LED.attributes={iotw_LED_pin1, iotw_LED_pin2}

# OutputControl class attributes and methods

# iotw_I2CLCD2004 class attributes and methods
iotw_I2CLCD2004_pinSCL: Property = Property(name="pinSCL", type=StringType)
iotw_I2CLCD2004_pinGND: Property = Property(name="pinGND", type=StringType)
iotw_I2CLCD2004_pinVcc: Property = Property(name="pinVcc", type=StringType)
iotw_I2CLCD2004_pinSDA: Property = Property(name="pinSDA", type=StringType)
iotw_I2CLCD2004.attributes={iotw_I2CLCD2004_pinSCL, iotw_I2CLCD2004_pinSDA, iotw_I2CLCD2004_pinVcc, iotw_I2CLCD2004_pinGND}

# iotw_StartPoint class attributes and methods

# iotw_EndPoint class attributes and methods

# Relationships
mainboard0: BinaryAssociation = BinaryAssociation(
    name="mainboard0",
    ends={
        Property(name="Mainboard", type=iotw_IOControl, multiplicity=Multiplicity(1, 1)),
        Property(name="controls", type=iotw_Mainboard, multiplicity=Multiplicity(0, 1))
    }
)
mainboard1: BinaryAssociation = BinaryAssociation(
    name="mainboard1",
    ends={
        Property(name="Mainboard2", type=iotw_ConnectivityControl, multiplicity=Multiplicity(1, 1)),
        Property(name="connectivities", type=iotw_Mainboard, multiplicity=Multiplicity(0, 1))
    }
)
incomings3: BinaryAssociation = BinaryAssociation(
    name="incomings3",
    ends={
        Property(name="iotw_Connection", type=iotw_StateControl, multiplicity=Multiplicity(1, 1)),
        Property(name="iotw_StateControl", type=iotw_Connection, multiplicity=Multiplicity(0, 9999))
    }
)
outgoings4: BinaryAssociation = BinaryAssociation(
    name="outgoings4",
    ends={
        Property(name="iotw_Connection6", type=iotw_StateControl, multiplicity=Multiplicity(1, 1)),
        Property(name="iotw_StateControl5", type=iotw_Connection, multiplicity=Multiplicity(0, 9999))
    }
)
dataExplorer7: BinaryAssociation = BinaryAssociation(
    name="dataExplorer7",
    ends={
        Property(name="DataExplorer", type=iotw_DataControl, multiplicity=Multiplicity(1, 1)),
        Property(name="datas", type=iotw_DataExplorer, multiplicity=Multiplicity(0, 1))
    }
)
datas8: BinaryAssociation = BinaryAssociation(
    name="datas8",
    ends={
        Property(name="DataControl", type=iotw_DataExplorer, multiplicity=Multiplicity(1, 1)),
        Property(name="dataExplorer", type=iotw_DataControl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectivities10: BinaryAssociation = BinaryAssociation(
    name="connectivities10",
    ends={
        Property(name="ConnectivityControl", type=iotw_Mainboard, multiplicity=Multiplicity(1, 1)),
        Property(name="mainboard11", type=iotw_ConnectivityControl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controls12: BinaryAssociation = BinaryAssociation(
    name="controls12",
    ends={
        Property(name="iotw_StateControl13", type=iotw_StateSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="iotw_StateSchema", type=iotw_StateControl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connnections14: BinaryAssociation = BinaryAssociation(
    name="connnections14",
    ends={
        Property(name="Connection", type=iotw_StateSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="stateSchema", type=iotw_Connection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controls9: BinaryAssociation = BinaryAssociation(
    name="controls9",
    ends={
        Property(name="IOControl", type=iotw_Mainboard, multiplicity=Multiplicity(1, 1)),
        Property(name="mainboard", type=iotw_IOControl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source15: BinaryAssociation = BinaryAssociation(
    name="source15",
    ends={
        Property(name="iotw_Control", type=iotw_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="iotw_Connection16", type=iotw_Control, multiplicity=Multiplicity(0, 1))
    }
)
target17: BinaryAssociation = BinaryAssociation(
    name="target17",
    ends={
        Property(name="iotw_Control19", type=iotw_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="iotw_Connection18", type=iotw_Control, multiplicity=Multiplicity(0, 1))
    }
)
stateSchema20: BinaryAssociation = BinaryAssociation(
    name="stateSchema20",
    ends={
        Property(name="StateSchema", type=iotw_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="connnections", type=iotw_StateSchema, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_iotw_ConnectivityControl_Control = Generalization(general=Control, specific=iotw_ConnectivityControl)
gen_iotw_StateControl_Control = Generalization(general=Control, specific=iotw_StateControl)
gen_iotw_DataControl_Control = Generalization(general=Control, specific=iotw_DataControl)
gen_iotw_IOControl_Control = Generalization(general=Control, specific=iotw_IOControl)
gen_iotw_ArduinoUNOR3_Mainboard = Generalization(general=Mainboard, specific=iotw_ArduinoUNOR3)
gen_iotw_InputControl_IOControl = Generalization(general=IOControl, specific=iotw_InputControl)
gen_iotw_OutputControl_IOControl = Generalization(general=IOControl, specific=iotw_OutputControl)
gen_iotw_Keypad4x4_InputControl = Generalization(general=InputControl, specific=iotw_Keypad4x4)
gen_iotw_BluetoothHC06_ConnectivityControl = Generalization(general=ConnectivityControl, specific=iotw_BluetoothHC06)
gen_iotw_WifiESP8266_ConnectivityControl = Generalization(general=ConnectivityControl, specific=iotw_WifiESP8266)
gen_iotw_Button_InputControl = Generalization(general=InputControl, specific=iotw_Button)
gen_iotw_Buzzer_OutputControl = Generalization(general=OutputControl, specific=iotw_Buzzer)
gen_iotw_StateFrame_StateControl = Generalization(general=StateControl, specific=iotw_StateFrame)
gen_iotw_Decision_StateControl = Generalization(general=StateControl, specific=iotw_Decision)
gen_iotw_LED_OutputControl = Generalization(general=OutputControl, specific=iotw_LED)
gen_iotw_I2CLCD2004_OutputControl = Generalization(general=OutputControl, specific=iotw_I2CLCD2004)
gen_iotw_StartPoint_StateControl = Generalization(general=StateControl, specific=iotw_StartPoint)
gen_iotw_EndPoint_StateControl = Generalization(general=StateControl, specific=iotw_EndPoint)

# Domain Model
domain_model = DomainModel(
    name="iotw",
    types={iotw_Mainboard, iotw_ConnectivityControl, iotw_StateControl, iotw_Connection, iotw_DataControl, iotw_DataExplorer, iotw_Control, iotw_IOControl, Control, iotw_StateSchema, iotw_ArduinoUNOR3, Mainboard, iotw_InputControl, IOControl, iotw_OutputControl, iotw_Keypad4x4, InputControl, iotw_BluetoothHC06, ConnectivityControl, iotw_WifiESP8266, iotw_Button, iotw_Buzzer, iotw_StateFrame, StateControl, iotw_Decision, iotw_LED, OutputControl, iotw_I2CLCD2004, iotw_StartPoint, iotw_EndPoint, ConnectionKind, RouterKind, TypeData},
    associations={mainboard0, mainboard1, incomings3, outgoings4, dataExplorer7, datas8, connectivities10, controls12, connnections14, controls9, source15, target17, stateSchema20},
    generalizations={gen_iotw_ConnectivityControl_Control, gen_iotw_StateControl_Control, gen_iotw_DataControl_Control, gen_iotw_IOControl_Control, gen_iotw_ArduinoUNOR3_Mainboard, gen_iotw_InputControl_IOControl, gen_iotw_OutputControl_IOControl, gen_iotw_Keypad4x4_InputControl, gen_iotw_BluetoothHC06_ConnectivityControl, gen_iotw_WifiESP8266_ConnectivityControl, gen_iotw_Button_InputControl, gen_iotw_Buzzer_OutputControl, gen_iotw_StateFrame_StateControl, gen_iotw_Decision_StateControl, gen_iotw_LED_OutputControl, gen_iotw_I2CLCD2004_OutputControl, gen_iotw_StartPoint_StateControl, gen_iotw_EndPoint_StateControl},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)