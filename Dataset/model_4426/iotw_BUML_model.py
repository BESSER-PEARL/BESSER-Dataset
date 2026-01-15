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
            EnumerationLiteral(name="STATE_FLOW"),
			EnumerationLiteral(name="OUTSIDE_FLOW")
    }
)

RouterKind: Enumeration = Enumeration(
    name="RouterKind",
    literals={
            EnumerationLiteral(name="BENDPOINT"),
			EnumerationLiteral(name="MANHATTAN")
    }
)

WifiMode: Enumeration = Enumeration(
    name="WifiMode",
    literals={
            EnumerationLiteral(name="Station"),
			EnumerationLiteral(name="Access_Point"),
			EnumerationLiteral(name="Both")
    }
)

WifiIDConnection: Enumeration = Enumeration(
    name="WifiIDConnection",
    literals={
            EnumerationLiteral(name="id_0"),
			EnumerationLiteral(name="id_1"),
			EnumerationLiteral(name="id_2"),
			EnumerationLiteral(name="id_3"),
			EnumerationLiteral(name="id_4")
    }
)

ListBaud: Enumeration = Enumeration(
    name="ListBaud",
    literals={
            EnumerationLiteral(name="baud_9600"),
			EnumerationLiteral(name="baud_19200"),
			EnumerationLiteral(name="baud_38400"),
			EnumerationLiteral(name="baud_57600"),
			EnumerationLiteral(name="baud_74880"),
			EnumerationLiteral(name="baud_115200"),
			EnumerationLiteral(name="baud_230400"),
			EnumerationLiteral(name="baud_250000")
    }
)

ListConnectionChannel: Enumeration = Enumeration(
    name="ListConnectionChannel",
    literals={
            EnumerationLiteral(name="Single"),
			EnumerationLiteral(name="Multiple")
    }
)

ListProtocol: Enumeration = Enumeration(
    name="ListProtocol",
    literals={
            EnumerationLiteral(name="TCP"),
			EnumerationLiteral(name="UDP")
    }
)

I2CLCDType: Enumeration = Enumeration(
    name="I2CLCDType",
    literals={
            EnumerationLiteral(name="I2CLCD2004"),
			EnumerationLiteral(name="I2CLCD1602")
    }
)

ESP8266WiFiMode: Enumeration = Enumeration(
    name="ESP8266WiFiMode",
    literals={
            EnumerationLiteral(name="WIFI_OFF"),
			EnumerationLiteral(name="WIFI_AP"),
			EnumerationLiteral(name="WIFI_STA"),
			EnumerationLiteral(name="WIFI_AP_STA")
    }
)

# Classes
iotw_Connection = Class(name="iotw::Connection")
iotw_StateSchema = Class(name="iotw::StateSchema")
iotw_Component = Class(name="iotw::Component", is_abstract=True)
iotw_ArduinoWiFiESP8266WeMosD1 = Class(name="iotw::ArduinoWiFiESP8266WeMosD1")
Mainboard = Class(name="Mainboard")
iotw_StateComponent = Class(name="iotw::StateComponent", is_abstract=True)
Component = Class(name="Component")
iotw_Device = Class(name="iotw::Device", is_abstract=True)
iotw_Mainboard = Class(name="iotw::Mainboard", is_abstract=True)
iotw_IODevice = Class(name="iotw::IODevice", is_abstract=True)
Device = Class(name="Device")
iotw_InputDevice = Class(name="iotw::InputDevice", is_abstract=True)
IODevice = Class(name="IODevice")
iotw_OutputDevice = Class(name="iotw::OutputDevice", is_abstract=True)
iotw_Connectivity = Class(name="iotw::Connectivity", is_abstract=True)
iotw_Keypad4x4 = Class(name="iotw::Keypad4x4")
InputDevice = Class(name="InputDevice")
iotw_ArduinoUNOR3 = Class(name="iotw::ArduinoUNOR3")
iotw_CDS = Class(name="iotw::CDS")
iotw_LED = Class(name="iotw::LED")
OutputDevice = Class(name="OutputDevice")
iotw_Button = Class(name="iotw::Button")
iotw_LM35 = Class(name="iotw::LM35")
iotw_DHT11 = Class(name="iotw::DHT11")
iotw_Decision = Class(name="iotw::Decision")
iotw_StartPoint = Class(name="iotw::StartPoint")
iotw_EndPoint = Class(name="iotw::EndPoint")
iotw_I2CLCD = Class(name="iotw::I2CLCD")
iotw_Buzzer = Class(name="iotw::Buzzer")
iotw_BluetoothHC06 = Class(name="iotw::BluetoothHC06")
Connectivity = Class(name="Connectivity")
iotw_WifiESP8266 = Class(name="iotw::WifiESP8266")
iotw_StateFrame = Class(name="iotw::StateFrame")
StateComponent = Class(name="StateComponent")

# iotw_Connection class attributes and methods
iotw_Connection_bendpoints: Property = Property(name="bendpoints", type=StringType)
iotw_Connection_routerKind: Property = Property(name="routerKind", type=StringType)
iotw_Connection_kind: Property = Property(name="kind", type=StringType)
iotw_Connection_label: Property = Property(name="label", type=StringType)
iotw_Connection.attributes={iotw_Connection_kind, iotw_Connection_bendpoints, iotw_Connection_label, iotw_Connection_routerKind}

# iotw_StateSchema class attributes and methods

# iotw_Component class attributes and methods
iotw_Component_id: Property = Property(name="id", type=StringType)
iotw_Component_constraints: Property = Property(name="constraints", type=StringType)
iotw_Component.attributes={iotw_Component_constraints, iotw_Component_id}

# iotw_ArduinoWiFiESP8266WeMosD1 class attributes and methods
iotw_ArduinoWiFiESP8266WeMosD1_pinA0: Property = Property(name="pinA0", type=StringType)
iotw_ArduinoWiFiESP8266WeMosD1_pinD0: Property = Property(name="pinD0", type=StringType)
iotw_ArduinoWiFiESP8266WeMosD1_pinD1: Property = Property(name="pinD1", type=StringType)
iotw_ArduinoWiFiESP8266WeMosD1_pinD2: Property = Property(name="pinD2", type=StringType)
iotw_ArduinoWiFiESP8266WeMosD1_pinD3: Property = Property(name="pinD3", type=StringType)
iotw_ArduinoWiFiESP8266WeMosD1_pinD4: Property = Property(name="pinD4", type=StringType)
iotw_ArduinoWiFiESP8266WeMosD1_pinD5: Property = Property(name="pinD5", type=StringType)
iotw_ArduinoWiFiESP8266WeMosD1_pinD6: Property = Property(name="pinD6", type=StringType)
iotw_ArduinoWiFiESP8266WeMosD1_pinD7: Property = Property(name="pinD7", type=StringType)
iotw_ArduinoWiFiESP8266WeMosD1_pinD8: Property = Property(name="pinD8", type=StringType)
iotw_ArduinoWiFiESP8266WeMosD1_pinSDA: Property = Property(name="pinSDA", type=StringType)
iotw_ArduinoWiFiESP8266WeMosD1_pinSCL: Property = Property(name="pinSCL", type=StringType)
iotw_ArduinoWiFiESP8266WeMosD1_wifiMode: Property = Property(name="wifiMode", type=StringType)
iotw_ArduinoWiFiESP8266WeMosD1_ssid: Property = Property(name="ssid", type=StringType)
iotw_ArduinoWiFiESP8266WeMosD1_password: Property = Property(name="password", type=StringType)
iotw_ArduinoWiFiESP8266WeMosD1_ip: Property = Property(name="ip", type=StringType)
iotw_ArduinoWiFiESP8266WeMosD1_dns: Property = Property(name="dns", type=StringType)
iotw_ArduinoWiFiESP8266WeMosD1_gateway: Property = Property(name="gateway", type=StringType)
iotw_ArduinoWiFiESP8266WeMosD1_subnet: Property = Property(name="subnet", type=StringType)
iotw_ArduinoWiFiESP8266WeMosD1_baud: Property = Property(name="baud", type=IntegerType)
iotw_ArduinoWiFiESP8266WeMosD1.attributes={iotw_ArduinoWiFiESP8266WeMosD1_pinD4, iotw_ArduinoWiFiESP8266WeMosD1_pinD6, iotw_ArduinoWiFiESP8266WeMosD1_password, iotw_ArduinoWiFiESP8266WeMosD1_pinD7, iotw_ArduinoWiFiESP8266WeMosD1_ssid, iotw_ArduinoWiFiESP8266WeMosD1_dns, iotw_ArduinoWiFiESP8266WeMosD1_subnet, iotw_ArduinoWiFiESP8266WeMosD1_pinSCL, iotw_ArduinoWiFiESP8266WeMosD1_pinSDA, iotw_ArduinoWiFiESP8266WeMosD1_pinA0, iotw_ArduinoWiFiESP8266WeMosD1_gateway, iotw_ArduinoWiFiESP8266WeMosD1_pinD2, iotw_ArduinoWiFiESP8266WeMosD1_ip, iotw_ArduinoWiFiESP8266WeMosD1_pinD8, iotw_ArduinoWiFiESP8266WeMosD1_pinD3, iotw_ArduinoWiFiESP8266WeMosD1_pinD0, iotw_ArduinoWiFiESP8266WeMosD1_pinD5, iotw_ArduinoWiFiESP8266WeMosD1_wifiMode, iotw_ArduinoWiFiESP8266WeMosD1_pinD1, iotw_ArduinoWiFiESP8266WeMosD1_baud}

# Mainboard class attributes and methods

# iotw_StateComponent class attributes and methods
iotw_StateComponent_name: Property = Property(name="name", type=StringType)
iotw_StateComponent.attributes={iotw_StateComponent_name}

# Component class attributes and methods

# iotw_Device class attributes and methods
iotw_Device_name: Property = Property(name="name", type=StringType)
iotw_Device_m_getPins: Method = Method(name="getPins", parameters={}, type=StringType)
iotw_Device_m_getPinConnecteds: Method = Method(name="getPinConnecteds", parameters={}, type=StringType)
iotw_Device_m_modifyPin: Method = Method(name="modifyPin", parameters={Parameter(name='pin')})
iotw_Device.attributes={iotw_Device_name}
iotw_Device.methods={iotw_Device_m_getPinConnecteds, iotw_Device_m_modifyPin, iotw_Device_m_getPins}

# iotw_Mainboard class attributes and methods
iotw_Mainboard_name: Property = Property(name="name", type=StringType)
iotw_Mainboard_m_findPin: Method = Method(name="findPin", parameters={Parameter(name='pin')}, type=StringType)
iotw_Mainboard_m_addDevice: Method = Method(name="addDevice", parameters={Parameter(name='device')})
iotw_Mainboard_m_removeDevice: Method = Method(name="removeDevice", parameters={Parameter(name='device')})
iotw_Mainboard_m_getPins: Method = Method(name="getPins", parameters={}, type=StringType)
iotw_Mainboard_m_getPinConnecteds: Method = Method(name="getPinConnecteds", parameters={}, type=StringType)
iotw_Mainboard_m_modifyPin: Method = Method(name="modifyPin", parameters={Parameter(name='pin')})
iotw_Mainboard.attributes={iotw_Mainboard_name}
iotw_Mainboard.methods={iotw_Mainboard_m_modifyPin, iotw_Mainboard_m_getPins, iotw_Mainboard_m_getPinConnecteds, iotw_Mainboard_m_addDevice, iotw_Mainboard_m_removeDevice, iotw_Mainboard_m_findPin}

# iotw_IODevice class attributes and methods

# Device class attributes and methods

# iotw_InputDevice class attributes and methods

# IODevice class attributes and methods

# iotw_OutputDevice class attributes and methods

# iotw_Connectivity class attributes and methods

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
iotw_Keypad4x4.attributes={iotw_Keypad4x4_nameButtonHash, iotw_Keypad4x4_nameButtonB, iotw_Keypad4x4_nameButton1, iotw_Keypad4x4_pin6, iotw_Keypad4x4_nameButton6, iotw_Keypad4x4_pin7, iotw_Keypad4x4_nameButton4, iotw_Keypad4x4_nameButton7, iotw_Keypad4x4_pin1, iotw_Keypad4x4_pin4, iotw_Keypad4x4_nameButtonAsterisk, iotw_Keypad4x4_nameButtonA, iotw_Keypad4x4_pin2, iotw_Keypad4x4_rows, iotw_Keypad4x4_nameButton0, iotw_Keypad4x4_nameButton5, iotw_Keypad4x4_nameButton2, iotw_Keypad4x4_nameButtonC, iotw_Keypad4x4_nameButtonD, iotw_Keypad4x4_nameButton3, iotw_Keypad4x4_cols, iotw_Keypad4x4_keys, iotw_Keypad4x4_pin5, iotw_Keypad4x4_pin3, iotw_Keypad4x4_nameButton8, iotw_Keypad4x4_pin8, iotw_Keypad4x4_nameButton9}
iotw_Keypad4x4.methods={iotw_Keypad4x4_m_getButton}

# InputDevice class attributes and methods

# iotw_ArduinoUNOR3 class attributes and methods
iotw_ArduinoUNOR3_pinA2: Property = Property(name="pinA2", type=StringType)
iotw_ArduinoUNOR3_pinA3: Property = Property(name="pinA3", type=StringType)
iotw_ArduinoUNOR3_pinA4: Property = Property(name="pinA4", type=StringType)
iotw_ArduinoUNOR3_pinA5: Property = Property(name="pinA5", type=StringType)
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
iotw_ArduinoUNOR3.attributes={iotw_ArduinoUNOR3_pin7, iotw_ArduinoUNOR3_pin1, iotw_ArduinoUNOR3_pin10, iotw_ArduinoUNOR3_pin13, iotw_ArduinoUNOR3_pin9, iotw_ArduinoUNOR3_pinA1, iotw_ArduinoUNOR3_pinA4, iotw_ArduinoUNOR3_pin5, iotw_ArduinoUNOR3_pin8, iotw_ArduinoUNOR3_pin2, iotw_ArduinoUNOR3_pinA2, iotw_ArduinoUNOR3_pinA0, iotw_ArduinoUNOR3_pin12, iotw_ArduinoUNOR3_pin3, iotw_ArduinoUNOR3_pin6, iotw_ArduinoUNOR3_pin4, iotw_ArduinoUNOR3_pinA3, iotw_ArduinoUNOR3_pinA5, iotw_ArduinoUNOR3_pin11, iotw_ArduinoUNOR3_pin0}

# iotw_CDS class attributes and methods
iotw_CDS_pinGND: Property = Property(name="pinGND", type=StringType)
iotw_CDS_pinVcc: Property = Property(name="pinVcc", type=StringType)
iotw_CDS_pinD0: Property = Property(name="pinD0", type=StringType)
iotw_CDS.attributes={iotw_CDS_pinD0, iotw_CDS_pinGND, iotw_CDS_pinVcc}

# iotw_LED class attributes and methods
iotw_LED_pin1: Property = Property(name="pin1", type=StringType)
iotw_LED_pin2: Property = Property(name="pin2", type=StringType)
iotw_LED.attributes={iotw_LED_pin2, iotw_LED_pin1}

# OutputDevice class attributes and methods

# iotw_Button class attributes and methods
iotw_Button_pin1: Property = Property(name="pin1", type=StringType)
iotw_Button.attributes={iotw_Button_pin1}

# iotw_LM35 class attributes and methods
iotw_LM35_pin1: Property = Property(name="pin1", type=StringType)
iotw_LM35.attributes={iotw_LM35_pin1}

# iotw_DHT11 class attributes and methods
iotw_DHT11_pinGND: Property = Property(name="pinGND", type=StringType)
iotw_DHT11_pinVcc: Property = Property(name="pinVcc", type=StringType)
iotw_DHT11_pinData: Property = Property(name="pinData", type=StringType)
iotw_DHT11.attributes={iotw_DHT11_pinGND, iotw_DHT11_pinData, iotw_DHT11_pinVcc}

# iotw_Decision class attributes and methods

# iotw_StartPoint class attributes and methods

# iotw_EndPoint class attributes and methods

# iotw_I2CLCD class attributes and methods
iotw_I2CLCD_pinGND: Property = Property(name="pinGND", type=StringType)
iotw_I2CLCD_pinVcc: Property = Property(name="pinVcc", type=StringType)
iotw_I2CLCD_pinSDA: Property = Property(name="pinSDA", type=StringType)
iotw_I2CLCD_pinSCL: Property = Property(name="pinSCL", type=StringType)
iotw_I2CLCD_type: Property = Property(name="type", type=StringType)
iotw_I2CLCD.attributes={iotw_I2CLCD_pinSCL, iotw_I2CLCD_pinGND, iotw_I2CLCD_type, iotw_I2CLCD_pinSDA, iotw_I2CLCD_pinVcc}

# iotw_Buzzer class attributes and methods
iotw_Buzzer_pin1: Property = Property(name="pin1", type=StringType)
iotw_Buzzer_pin2: Property = Property(name="pin2", type=StringType)
iotw_Buzzer_Tone: Property = Property(name="Tone", type=IntegerType)
iotw_Buzzer_Time: Property = Property(name="Time", type=IntegerType)
iotw_Buzzer.attributes={iotw_Buzzer_pin2, iotw_Buzzer_pin1, iotw_Buzzer_Tone, iotw_Buzzer_Time}

# iotw_BluetoothHC06 class attributes and methods
iotw_BluetoothHC06_pinTXD: Property = Property(name="pinTXD", type=StringType)
iotw_BluetoothHC06_pinRXD: Property = Property(name="pinRXD", type=StringType)
iotw_BluetoothHC06_pinGND: Property = Property(name="pinGND", type=StringType)
iotw_BluetoothHC06_pinVCC: Property = Property(name="pinVCC", type=StringType)
iotw_BluetoothHC06.attributes={iotw_BluetoothHC06_pinVCC, iotw_BluetoothHC06_pinGND, iotw_BluetoothHC06_pinRXD, iotw_BluetoothHC06_pinTXD}

# Connectivity class attributes and methods

# iotw_WifiESP8266 class attributes and methods
iotw_WifiESP8266_pinTX: Property = Property(name="pinTX", type=StringType)
iotw_WifiESP8266_pinRX: Property = Property(name="pinRX", type=StringType)
iotw_WifiESP8266_pinVcc: Property = Property(name="pinVcc", type=StringType)
iotw_WifiESP8266_pinGND: Property = Property(name="pinGND", type=StringType)
iotw_WifiESP8266_pinCHPD: Property = Property(name="pinCHPD", type=StringType)
iotw_WifiESP8266_sSID_ST: Property = Property(name="sSID_ST", type=StringType)
iotw_WifiESP8266_password_ST: Property = Property(name="password_ST", type=StringType)
iotw_WifiESP8266_mode: Property = Property(name="mode", type=StringType)
iotw_WifiESP8266_idConnection: Property = Property(name="idConnection", type=StringType)
iotw_WifiESP8266_password_AccessPoint: Property = Property(name="password_AccessPoint", type=StringType)
iotw_WifiESP8266_sSID_AccessPoint: Property = Property(name="sSID_AccessPoint", type=StringType)
iotw_WifiESP8266_port: Property = Property(name="port", type=IntegerType)
iotw_WifiESP8266_iP: Property = Property(name="iP", type=StringType)
iotw_WifiESP8266_baud: Property = Property(name="baud", type=StringType)
iotw_WifiESP8266_connectedChannel: Property = Property(name="connectedChannel", type=StringType)
iotw_WifiESP8266_protocol: Property = Property(name="protocol", type=StringType)
iotw_WifiESP8266.attributes={iotw_WifiESP8266_pinGND, iotw_WifiESP8266_protocol, iotw_WifiESP8266_sSID_ST, iotw_WifiESP8266_pinCHPD, iotw_WifiESP8266_port, iotw_WifiESP8266_idConnection, iotw_WifiESP8266_connectedChannel, iotw_WifiESP8266_pinTX, iotw_WifiESP8266_pinRX, iotw_WifiESP8266_iP, iotw_WifiESP8266_pinVcc, iotw_WifiESP8266_password_ST, iotw_WifiESP8266_mode, iotw_WifiESP8266_password_AccessPoint, iotw_WifiESP8266_sSID_AccessPoint, iotw_WifiESP8266_baud}

# iotw_StateFrame class attributes and methods
iotw_StateFrame_content: Property = Property(name="content", type=StringType)
iotw_StateFrame.attributes={iotw_StateFrame_content}

# StateComponent class attributes and methods

# Relationships
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="iotw_Component", type=iotw_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="iotw_Connection", type=iotw_Component, multiplicity=Multiplicity(0, 1))
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="iotw_Component3", type=iotw_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="iotw_Connection2", type=iotw_Component, multiplicity=Multiplicity(0, 1))
    }
)
devices14: BinaryAssociation = BinaryAssociation(
    name="devices14",
    ends={
        Property(name="Device", type=iotw_Mainboard, multiplicity=Multiplicity(1, 1)),
        Property(name="mainboard", type=iotw_Device, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateSchema4: BinaryAssociation = BinaryAssociation(
    name="stateSchema4",
    ends={
        Property(name="StateSchema", type=iotw_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="connnections", type=iotw_StateSchema, multiplicity=Multiplicity(0, 1))
    }
)
components5: BinaryAssociation = BinaryAssociation(
    name="components5",
    ends={
        Property(name="iotw_StateComponent", type=iotw_StateSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="iotw_StateSchema", type=iotw_StateComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connnections6: BinaryAssociation = BinaryAssociation(
    name="connnections6",
    ends={
        Property(name="Connection", type=iotw_StateSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="stateSchema", type=iotw_Connection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomings7: BinaryAssociation = BinaryAssociation(
    name="incomings7",
    ends={
        Property(name="iotw_Connection9", type=iotw_StateComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="iotw_StateComponent8", type=iotw_Connection, multiplicity=Multiplicity(0, 9999))
    }
)
outgoings10: BinaryAssociation = BinaryAssociation(
    name="outgoings10",
    ends={
        Property(name="iotw_Connection12", type=iotw_StateComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="iotw_StateComponent11", type=iotw_Connection, multiplicity=Multiplicity(0, 9999))
    }
)
mainboard13: BinaryAssociation = BinaryAssociation(
    name="mainboard13",
    ends={
        Property(name="Mainboard", type=iotw_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="devices", type=iotw_Mainboard, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_iotw_ArduinoWiFiESP8266WeMosD1_Mainboard = Generalization(general=Mainboard, specific=iotw_ArduinoWiFiESP8266WeMosD1)
gen_iotw_StateComponent_Component = Generalization(general=Component, specific=iotw_StateComponent)
gen_iotw_Device_Component = Generalization(general=Component, specific=iotw_Device)
gen_iotw_IODevice_Device = Generalization(general=Device, specific=iotw_IODevice)
gen_iotw_InputDevice_IODevice = Generalization(general=IODevice, specific=iotw_InputDevice)
gen_iotw_OutputDevice_IODevice = Generalization(general=IODevice, specific=iotw_OutputDevice)
gen_iotw_Connectivity_Device = Generalization(general=Device, specific=iotw_Connectivity)
gen_iotw_Keypad4x4_InputDevice = Generalization(general=InputDevice, specific=iotw_Keypad4x4)
gen_iotw_ArduinoUNOR3_Mainboard = Generalization(general=Mainboard, specific=iotw_ArduinoUNOR3)
gen_iotw_CDS_InputDevice = Generalization(general=InputDevice, specific=iotw_CDS)
gen_iotw_LED_OutputDevice = Generalization(general=OutputDevice, specific=iotw_LED)
gen_iotw_Button_InputDevice = Generalization(general=InputDevice, specific=iotw_Button)
gen_iotw_LM35_InputDevice = Generalization(general=InputDevice, specific=iotw_LM35)
gen_iotw_DHT11_InputDevice = Generalization(general=InputDevice, specific=iotw_DHT11)
gen_iotw_StateFrame_StateComponent = Generalization(general=StateComponent, specific=iotw_StateFrame)
gen_iotw_Decision_StateComponent = Generalization(general=StateComponent, specific=iotw_Decision)
gen_iotw_StartPoint_StateComponent = Generalization(general=StateComponent, specific=iotw_StartPoint)
gen_iotw_EndPoint_StateComponent = Generalization(general=StateComponent, specific=iotw_EndPoint)
gen_iotw_I2CLCD_OutputDevice = Generalization(general=OutputDevice, specific=iotw_I2CLCD)
gen_iotw_Buzzer_OutputDevice = Generalization(general=OutputDevice, specific=iotw_Buzzer)
gen_iotw_BluetoothHC06_Connectivity = Generalization(general=Connectivity, specific=iotw_BluetoothHC06)
gen_iotw_WifiESP8266_Connectivity = Generalization(general=Connectivity, specific=iotw_WifiESP8266)

# Domain Model
domain_model = DomainModel(
    name="iotw",
    types={iotw_Connection, iotw_StateSchema, iotw_Component, iotw_ArduinoWiFiESP8266WeMosD1, Mainboard, iotw_StateComponent, Component, iotw_Device, iotw_Mainboard, iotw_IODevice, Device, iotw_InputDevice, IODevice, iotw_OutputDevice, iotw_Connectivity, iotw_Keypad4x4, InputDevice, iotw_ArduinoUNOR3, iotw_CDS, iotw_LED, OutputDevice, iotw_Button, iotw_LM35, iotw_DHT11, iotw_Decision, iotw_StartPoint, iotw_EndPoint, iotw_I2CLCD, iotw_Buzzer, iotw_BluetoothHC06, Connectivity, iotw_WifiESP8266, iotw_StateFrame, StateComponent, ConnectionKind, RouterKind, WifiMode, WifiIDConnection, ListBaud, ListConnectionChannel, ListProtocol, I2CLCDType, ESP8266WiFiMode},
    associations={source0, target1, devices14, stateSchema4, components5, connnections6, incomings7, outgoings10, mainboard13},
    generalizations={gen_iotw_ArduinoWiFiESP8266WeMosD1_Mainboard, gen_iotw_StateComponent_Component, gen_iotw_Device_Component, gen_iotw_IODevice_Device, gen_iotw_InputDevice_IODevice, gen_iotw_OutputDevice_IODevice, gen_iotw_Connectivity_Device, gen_iotw_Keypad4x4_InputDevice, gen_iotw_ArduinoUNOR3_Mainboard, gen_iotw_CDS_InputDevice, gen_iotw_LED_OutputDevice, gen_iotw_Button_InputDevice, gen_iotw_LM35_InputDevice, gen_iotw_DHT11_InputDevice, gen_iotw_StateFrame_StateComponent, gen_iotw_Decision_StateComponent, gen_iotw_StartPoint_StateComponent, gen_iotw_EndPoint_StateComponent, gen_iotw_I2CLCD_OutputDevice, gen_iotw_Buzzer_OutputDevice, gen_iotw_BluetoothHC06_Connectivity, gen_iotw_WifiESP8266_Connectivity},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)