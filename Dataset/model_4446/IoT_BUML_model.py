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

# Classes
ioT_Model = Class(name="ioT::Model")
ioT_ExternalDeclaration = Class(name="ioT::ExternalDeclaration")
ioT_Config = Class(name="ioT::Config")
ioT_Device = Class(name="ioT::Device")
ioT_Loop = Class(name="ioT::Loop")
ioT_ExpressionRight = Class(name="ioT::ExpressionRight")
ioT_ConnectionConfig = Class(name="ioT::ConnectionConfig")
ioT_Address = Class(name="ioT::Address")
ioT_Declaration = Class(name="ioT::Declaration")
ioT_Program = Class(name="ioT::Program")
ioT_ControllerDevice = Class(name="ioT::ControllerDevice")
Device = Class(name="Device")
ioT_IoTDevice = Class(name="ioT::IoTDevice")
ioT_WifiStatement = Class(name="ioT::WifiStatement")
ioT_ConnectStatement = Class(name="ioT::ConnectStatement")
ioT_VarOrList = Class(name="ioT::VarOrList")
ioT_ListenStatement = Class(name="ioT::ListenStatement")
ioT_ReadConnection = Class(name="ioT::ReadConnection")
ioT_ExternalOf = Class(name="ioT::ExternalOf")
ioT_ReadSensor = Class(name="ioT::ReadSensor")
ioT_SENSOR = Class(name="ioT::SENSOR")
ioT_Block = Class(name="ioT::Block")
ExpressionRight = Class(name="ExpressionRight")
ioT_ExternalRight = Class(name="ioT::ExternalRight")
ioT_Expression = Class(name="ioT::Expression")
ioT_TIMEUNIT = Class(name="ioT::TIMEUNIT")
ioT_Command = Class(name="ioT::Command")
ioT_Action = Class(name="ioT::Action")
Command = Class(name="Command")
ioT_ExpressionLeft = Class(name="ioT::ExpressionLeft")
ExpressionLeft = Class(name="ExpressionLeft")
ioT_BoolExpression = Class(name="ioT::BoolExpression")
Expression = Class(name="Expression")
ioT_Bool = Class(name="ioT::Bool")
ioT_IntExpression = Class(name="ioT::IntExpression")
ioT_ReadVariable = Class(name="ioT::ReadVariable")
ioT_Variable = Class(name="ioT::Variable")
ioT_ElseBlock = Class(name="ioT::ElseBlock")
ioT_Comparison = Class(name="ioT::Comparison")
ioT_ComparisonOp = Class(name="ioT::ComparisonOp")
ioT_DeviceConfig = Class(name="ioT::DeviceConfig")
Config = Class(name="Config")
ioT_IpAddress = Class(name="ioT::IpAddress")
Address = Class(name="Address")
ioT_WindowsSerialAddress = Class(name="ioT::WindowsSerialAddress")
ioT_UnixSerialAddress = Class(name="ioT::UnixSerialAddress")
VarOrList = Class(name="VarOrList")
ioT_PyList = Class(name="ioT::PyList")
ioT_MILLISECONDS = Class(name="ioT::MILLISECONDS")
TIMEUNIT = Class(name="TIMEUNIT")
ioT_LIGHTSENSOR = Class(name="ioT::LIGHTSENSOR")
SENSOR = Class(name="SENSOR")
ioT_TEMPERATURE = Class(name="ioT::TEMPERATURE")
ioT_HUMIDITY = Class(name="ioT::HUMIDITY")
ioT_ToVar = Class(name="ioT::ToVar")
ioT_AddToList = Class(name="ioT::AddToList")
ioT_SendCommand = Class(name="ioT::SendCommand")
ioT_IfStatement = Class(name="ioT::IfStatement")
ioT_SECONDS = Class(name="ioT::SECONDS")
ioT_MINUTES = Class(name="ioT::MINUTES")
ioT_HOURS = Class(name="ioT::HOURS")
ioT_DAYS = Class(name="ioT::DAYS")
ioT_WEEKS = Class(name="ioT::WEEKS")
ioT_ClearListAction = Class(name="ioT::ClearListAction")
Action = Class(name="Action")
ioT_LEDAction = Class(name="ioT::LEDAction")
ioT_ArrowCommand = Class(name="ioT::ArrowCommand")
ioT_VarAccess = Class(name="ioT::VarAccess")
ioT_ItemBool = Class(name="ioT::ItemBool")
ioT_GT = Class(name="ioT::GT")
ComparisonOp = Class(name="ComparisonOp")
ioT_LT = Class(name="ioT::LT")
ioT_LE = Class(name="ioT::LE")
ioT_GE = Class(name="ioT::GE")
ioT_EQ = Class(name="ioT::EQ")
ioT_NE = Class(name="ioT::NE")
ioT_True = Class(name="ioT::True")
Bool = Class(name="Bool")
ioT_False = Class(name="ioT::False")
ioT_OR = Class(name="ioT::OR")
Comparison = Class(name="Comparison")
ioT_AND = Class(name="ioT::AND")
ioT_EQL = Class(name="ioT::EQL")
ioT_ItemVariable = Class(name="ioT::ItemVariable")
ioT_ItemInt = Class(name="ioT::ItemInt")

# ioT_Model class attributes and methods

# ioT_ExternalDeclaration class attributes and methods
ioT_ExternalDeclaration_name: Property = Property(name="name", type=StringType)
ioT_ExternalDeclaration.attributes={ioT_ExternalDeclaration_name}

# ioT_Config class attributes and methods
ioT_Config_name: Property = Property(name="name", type=StringType)
ioT_Config.attributes={ioT_Config_name}

# ioT_Device class attributes and methods
ioT_Device_name: Property = Property(name="name", type=StringType)
ioT_Device.attributes={ioT_Device_name}

# ioT_Loop class attributes and methods

# ioT_ExpressionRight class attributes and methods

# ioT_ConnectionConfig class attributes and methods
ioT_ConnectionConfig_type: Property = Property(name="type", type=StringType)
ioT_ConnectionConfig.attributes={ioT_ConnectionConfig_type}

# ioT_Address class attributes and methods
ioT_Address_value: Property = Property(name="value", type=StringType)
ioT_Address.attributes={ioT_Address_value}

# ioT_Declaration class attributes and methods
ioT_Declaration_key: Property = Property(name="key", type=StringType)
ioT_Declaration_value: Property = Property(name="value", type=StringType)
ioT_Declaration.attributes={ioT_Declaration_value, ioT_Declaration_key}

# ioT_Program class attributes and methods

# ioT_ControllerDevice class attributes and methods

# Device class attributes and methods

# ioT_IoTDevice class attributes and methods

# ioT_WifiStatement class attributes and methods

# ioT_ConnectStatement class attributes and methods

# ioT_VarOrList class attributes and methods
ioT_VarOrList_name: Property = Property(name="name", type=StringType)
ioT_VarOrList.attributes={ioT_VarOrList_name}

# ioT_ListenStatement class attributes and methods
ioT_ListenStatement_ip: Property = Property(name="ip", type=StringType)
ioT_ListenStatement_port: Property = Property(name="port", type=IntegerType)
ioT_ListenStatement.attributes={ioT_ListenStatement_port, ioT_ListenStatement_ip}

# ioT_ReadConnection class attributes and methods

# ioT_ExternalOf class attributes and methods

# ioT_ReadSensor class attributes and methods

# ioT_SENSOR class attributes and methods

# ioT_Block class attributes and methods

# ExpressionRight class attributes and methods

# ioT_ExternalRight class attributes and methods

# ioT_Expression class attributes and methods

# ioT_TIMEUNIT class attributes and methods

# ioT_Command class attributes and methods

# ioT_Action class attributes and methods

# Command class attributes and methods

# ioT_ExpressionLeft class attributes and methods

# ExpressionLeft class attributes and methods

# ioT_BoolExpression class attributes and methods

# Expression class attributes and methods

# ioT_Bool class attributes and methods

# ioT_IntExpression class attributes and methods
ioT_IntExpression_value: Property = Property(name="value", type=IntegerType)
ioT_IntExpression.attributes={ioT_IntExpression_value}

# ioT_ReadVariable class attributes and methods

# ioT_Variable class attributes and methods

# ioT_ElseBlock class attributes and methods

# ioT_Comparison class attributes and methods

# ioT_ComparisonOp class attributes and methods
ioT_ComparisonOp_op: Property = Property(name="op", type=StringType)
ioT_ComparisonOp.attributes={ioT_ComparisonOp_op}

# ioT_DeviceConfig class attributes and methods

# Config class attributes and methods

# ioT_IpAddress class attributes and methods

# Address class attributes and methods

# ioT_WindowsSerialAddress class attributes and methods

# ioT_UnixSerialAddress class attributes and methods

# VarOrList class attributes and methods

# ioT_PyList class attributes and methods

# ioT_MILLISECONDS class attributes and methods

# TIMEUNIT class attributes and methods

# ioT_LIGHTSENSOR class attributes and methods

# SENSOR class attributes and methods

# ioT_TEMPERATURE class attributes and methods

# ioT_HUMIDITY class attributes and methods

# ioT_ToVar class attributes and methods

# ioT_AddToList class attributes and methods

# ioT_SendCommand class attributes and methods

# ioT_IfStatement class attributes and methods

# ioT_SECONDS class attributes and methods

# ioT_MINUTES class attributes and methods

# ioT_HOURS class attributes and methods

# ioT_DAYS class attributes and methods

# ioT_WEEKS class attributes and methods

# ioT_ClearListAction class attributes and methods

# Action class attributes and methods

# ioT_LEDAction class attributes and methods
ioT_LEDAction_state: Property = Property(name="state", type=StringType)
ioT_LEDAction.attributes={ioT_LEDAction_state}

# ioT_ArrowCommand class attributes and methods

# ioT_VarAccess class attributes and methods

# ioT_ItemBool class attributes and methods

# ioT_GT class attributes and methods

# ComparisonOp class attributes and methods

# ioT_LT class attributes and methods

# ioT_LE class attributes and methods

# ioT_GE class attributes and methods

# ioT_EQ class attributes and methods

# ioT_NE class attributes and methods

# ioT_True class attributes and methods

# Bool class attributes and methods

# ioT_False class attributes and methods

# ioT_OR class attributes and methods

# Comparison class attributes and methods

# ioT_AND class attributes and methods

# ioT_EQL class attributes and methods

# ioT_ItemVariable class attributes and methods

# ioT_ItemInt class attributes and methods
ioT_ItemInt_value: Property = Property(name="value", type=IntegerType)
ioT_ItemInt.attributes={ioT_ItemInt_value}

# Relationships
externalDeclarations0: BinaryAssociation = BinaryAssociation(
    name="externalDeclarations0",
    ends={
        Property(name="ioT_ExternalDeclaration", type=ioT_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_Model", type=ioT_ExternalDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configs1: BinaryAssociation = BinaryAssociation(
    name="configs1",
    ends={
        Property(name="ioT_Config", type=ioT_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_Model2", type=ioT_Config, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
devices3: BinaryAssociation = BinaryAssociation(
    name="devices3",
    ends={
        Property(name="ioT_Device", type=ioT_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_Model4", type=ioT_Device, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listenStatements15: BinaryAssociation = BinaryAssociation(
    name="listenStatements15",
    ends={
        Property(name="ioT_ListenStatement", type=ioT_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_Program16", type=ioT_ListenStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loops17: BinaryAssociation = BinaryAssociation(
    name="loops17",
    ends={
        Property(name="ioT_Loop", type=ioT_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_Program18", type=ioT_Loop, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body19: BinaryAssociation = BinaryAssociation(
    name="body19",
    ends={
        Property(name="ioT_ExpressionRight", type=ioT_ListenStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_ListenStatement20", type=ioT_ExpressionRight, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connectionConfig21: BinaryAssociation = BinaryAssociation(
    name="connectionConfig21",
    ends={
        Property(name="ioT_ConnectionConfig", type=ioT_WifiStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_WifiStatement22", type=ioT_ConnectionConfig, multiplicity=Multiplicity(0, 1))
    }
)
device23: BinaryAssociation = BinaryAssociation(
    name="device23",
    ends={
        Property(name="ioT_Device25", type=ioT_ConnectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_ConnectStatement24", type=ioT_Device, multiplicity=Multiplicity(0, 1))
    }
)
address26: BinaryAssociation = BinaryAssociation(
    name="address26",
    ends={
        Property(name="ioT_Address", type=ioT_ConnectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_ConnectStatement27", type=ioT_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
configuration28: BinaryAssociation = BinaryAssociation(
    name="configuration28",
    ends={
        Property(name="ioT_ConnectionConfig30", type=ioT_ConnectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_ConnectStatement29", type=ioT_ConnectionConfig, multiplicity=Multiplicity(0, 1))
    }
)
declarations5: BinaryAssociation = BinaryAssociation(
    name="declarations5",
    ends={
        Property(name="ioT_Declaration", type=ioT_Config, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_Config6", type=ioT_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
program7: BinaryAssociation = BinaryAssociation(
    name="program7",
    ends={
        Property(name="ioT_Program", type=ioT_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_Device8", type=ioT_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wifiStatements9: BinaryAssociation = BinaryAssociation(
    name="wifiStatements9",
    ends={
        Property(name="ioT_WifiStatement", type=ioT_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_Program10", type=ioT_WifiStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connectStatements11: BinaryAssociation = BinaryAssociation(
    name="connectStatements11",
    ends={
        Property(name="ioT_ConnectStatement", type=ioT_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_Program12", type=ioT_ConnectStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables13: BinaryAssociation = BinaryAssociation(
    name="variables13",
    ends={
        Property(name="ioT_VarOrList", type=ioT_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_Program14", type=ioT_VarOrList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source39: BinaryAssociation = BinaryAssociation(
    name="source39",
    ends={
        Property(name="ioT_Device40", type=ioT_ReadConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_ReadConnection", type=ioT_Device, multiplicity=Multiplicity(0, 1))
    }
)
method41: BinaryAssociation = BinaryAssociation(
    name="method41",
    ends={
        Property(name="ioT_ExternalDeclaration42", type=ioT_ExternalOf, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_ExternalOf", type=ioT_ExternalDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
target43: BinaryAssociation = BinaryAssociation(
    name="target43",
    ends={
        Property(name="ioT_VarOrList45", type=ioT_ExternalOf, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_ExternalOf44", type=ioT_VarOrList, multiplicity=Multiplicity(0, 1))
    }
)
sensor46: BinaryAssociation = BinaryAssociation(
    name="sensor46",
    ends={
        Property(name="ioT_SENSOR", type=ioT_ReadSensor, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_ReadSensor", type=ioT_SENSOR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands47: BinaryAssociation = BinaryAssociation(
    name="commands47",
    ends={
        Property(name="ioT_Command48", type=ioT_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_Block", type=ioT_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method49: BinaryAssociation = BinaryAssociation(
    name="method49",
    ends={
        Property(name="ioT_ExternalDeclaration50", type=ioT_ExternalRight, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_ExternalRight", type=ioT_ExternalDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
timeVal31: BinaryAssociation = BinaryAssociation(
    name="timeVal31",
    ends={
        Property(name="ioT_Expression", type=ioT_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_Loop32", type=ioT_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeUnit33: BinaryAssociation = BinaryAssociation(
    name="timeUnit33",
    ends={
        Property(name="ioT_TIMEUNIT", type=ioT_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_Loop34", type=ioT_TIMEUNIT, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
command35: BinaryAssociation = BinaryAssociation(
    name="command35",
    ends={
        Property(name="ioT_Command", type=ioT_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_Loop36", type=ioT_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value37: BinaryAssociation = BinaryAssociation(
    name="value37",
    ends={
        Property(name="ioT_Bool", type=ioT_BoolExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_BoolExpression", type=ioT_Bool, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value38: BinaryAssociation = BinaryAssociation(
    name="value38",
    ends={
        Property(name="ioT_Variable", type=ioT_ReadVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_ReadVariable", type=ioT_Variable, multiplicity=Multiplicity(0, 1))
    }
)
commands51: BinaryAssociation = BinaryAssociation(
    name="commands51",
    ends={
        Property(name="ioT_Command52", type=ioT_ElseBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_ElseBlock", type=ioT_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value53: BinaryAssociation = BinaryAssociation(
    name="value53",
    ends={
        Property(name="ioT_Expression55", type=ioT_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_Variable54", type=ioT_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableName61: BinaryAssociation = BinaryAssociation(
    name="variableName61",
    ends={
        Property(name="ioT_VarOrList62", type=ioT_VarAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_VarAccess", type=ioT_VarOrList, multiplicity=Multiplicity(0, 1))
    }
)
variable63: BinaryAssociation = BinaryAssociation(
    name="variable63",
    ends={
        Property(name="ioT_Variable64", type=ioT_ToVar, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_ToVar", type=ioT_Variable, multiplicity=Multiplicity(0, 1))
    }
)
list65: BinaryAssociation = BinaryAssociation(
    name="list65",
    ends={
        Property(name="ioT_PyList66", type=ioT_AddToList, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_AddToList", type=ioT_PyList, multiplicity=Multiplicity(0, 1))
    }
)
target67: BinaryAssociation = BinaryAssociation(
    name="target67",
    ends={
        Property(name="ioT_Device68", type=ioT_SendCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_SendCommand", type=ioT_Device, multiplicity=Multiplicity(0, 1))
    }
)
condition69: BinaryAssociation = BinaryAssociation(
    name="condition69",
    ends={
        Property(name="ioT_Comparison", type=ioT_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_IfStatement", type=ioT_Comparison, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands70: BinaryAssociation = BinaryAssociation(
    name="commands70",
    ends={
        Property(name="ioT_Command72", type=ioT_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_IfStatement71", type=ioT_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseBlock73: BinaryAssociation = BinaryAssociation(
    name="elseBlock73",
    ends={
        Property(name="ioT_ElseBlock75", type=ioT_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_IfStatement74", type=ioT_ElseBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
list56: BinaryAssociation = BinaryAssociation(
    name="list56",
    ends={
        Property(name="ioT_PyList", type=ioT_ClearListAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_ClearListAction", type=ioT_PyList, multiplicity=Multiplicity(0, 1))
    }
)
left57: BinaryAssociation = BinaryAssociation(
    name="left57",
    ends={
        Property(name="ioT_ExpressionLeft", type=ioT_ArrowCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_ArrowCommand", type=ioT_ExpressionLeft, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right58: BinaryAssociation = BinaryAssociation(
    name="right58",
    ends={
        Property(name="ioT_ExpressionRight60", type=ioT_ArrowCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_ArrowCommand59", type=ioT_ExpressionRight, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value95: BinaryAssociation = BinaryAssociation(
    name="value95",
    ends={
        Property(name="ioT_Bool96", type=ioT_ItemBool, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_ItemBool", type=ioT_Bool, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left76: BinaryAssociation = BinaryAssociation(
    name="left76",
    ends={
        Property(name="ioT_Comparison77", type=ioT_OR, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_OR", type=ioT_Comparison, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right78: BinaryAssociation = BinaryAssociation(
    name="right78",
    ends={
        Property(name="ioT_Comparison80", type=ioT_OR, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_OR79", type=ioT_Comparison, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left81: BinaryAssociation = BinaryAssociation(
    name="left81",
    ends={
        Property(name="ioT_Comparison82", type=ioT_AND, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_AND", type=ioT_Comparison, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right83: BinaryAssociation = BinaryAssociation(
    name="right83",
    ends={
        Property(name="ioT_Comparison85", type=ioT_AND, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_AND84", type=ioT_Comparison, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left86: BinaryAssociation = BinaryAssociation(
    name="left86",
    ends={
        Property(name="ioT_Comparison87", type=ioT_EQL, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_EQL", type=ioT_Comparison, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op88: BinaryAssociation = BinaryAssociation(
    name="op88",
    ends={
        Property(name="ioT_ComparisonOp", type=ioT_EQL, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_EQL89", type=ioT_ComparisonOp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right90: BinaryAssociation = BinaryAssociation(
    name="right90",
    ends={
        Property(name="ioT_Comparison92", type=ioT_EQL, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_EQL91", type=ioT_Comparison, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value93: BinaryAssociation = BinaryAssociation(
    name="value93",
    ends={
        Property(name="ioT_Variable94", type=ioT_ItemVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_ItemVariable", type=ioT_Variable, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ioT_ControllerDevice_Device = Generalization(general=Device, specific=ioT_ControllerDevice)
gen_ioT_IoTDevice_Device = Generalization(general=Device, specific=ioT_IoTDevice)
gen_ioT_ReadConnection_ExpressionLeft = Generalization(general=ExpressionLeft, specific=ioT_ReadConnection)
gen_ioT_ExternalOf_ExpressionLeft = Generalization(general=ExpressionLeft, specific=ioT_ExternalOf)
gen_ioT_ReadSensor_ExpressionLeft = Generalization(general=ExpressionLeft, specific=ioT_ReadSensor)
gen_ioT_Block_ExpressionRight = Generalization(general=ExpressionRight, specific=ioT_Block)
gen_ioT_ExternalRight_ExpressionRight = Generalization(general=ExpressionRight, specific=ioT_ExternalRight)
gen_ioT_Action_Command = Generalization(general=Command, specific=ioT_Action)
gen_ioT_Expression_ExpressionLeft = Generalization(general=ExpressionLeft, specific=ioT_Expression)
gen_ioT_BoolExpression_Expression = Generalization(general=Expression, specific=ioT_BoolExpression)
gen_ioT_IntExpression_Expression = Generalization(general=Expression, specific=ioT_IntExpression)
gen_ioT_ReadVariable_ExpressionLeft = Generalization(general=ExpressionLeft, specific=ioT_ReadVariable)
gen_ioT_DeviceConfig_Config = Generalization(general=Config, specific=ioT_DeviceConfig)
gen_ioT_ConnectionConfig_Config = Generalization(general=Config, specific=ioT_ConnectionConfig)
gen_ioT_IpAddress_Address = Generalization(general=Address, specific=ioT_IpAddress)
gen_ioT_WindowsSerialAddress_Address = Generalization(general=Address, specific=ioT_WindowsSerialAddress)
gen_ioT_UnixSerialAddress_Address = Generalization(general=Address, specific=ioT_UnixSerialAddress)
gen_ioT_Variable_VarOrList = Generalization(general=VarOrList, specific=ioT_Variable)
gen_ioT_PyList_VarOrList = Generalization(general=VarOrList, specific=ioT_PyList)
gen_ioT_MILLISECONDS_TIMEUNIT = Generalization(general=TIMEUNIT, specific=ioT_MILLISECONDS)
gen_ioT_LIGHTSENSOR_SENSOR = Generalization(general=SENSOR, specific=ioT_LIGHTSENSOR)
gen_ioT_TEMPERATURE_SENSOR = Generalization(general=SENSOR, specific=ioT_TEMPERATURE)
gen_ioT_HUMIDITY_SENSOR = Generalization(general=SENSOR, specific=ioT_HUMIDITY)
gen_ioT_ToVar_ExpressionRight = Generalization(general=ExpressionRight, specific=ioT_ToVar)
gen_ioT_AddToList_ExpressionRight = Generalization(general=ExpressionRight, specific=ioT_AddToList)
gen_ioT_SendCommand_ExpressionRight = Generalization(general=ExpressionRight, specific=ioT_SendCommand)
gen_ioT_IfStatement_Command = Generalization(general=Command, specific=ioT_IfStatement)
gen_ioT_SECONDS_TIMEUNIT = Generalization(general=TIMEUNIT, specific=ioT_SECONDS)
gen_ioT_MINUTES_TIMEUNIT = Generalization(general=TIMEUNIT, specific=ioT_MINUTES)
gen_ioT_HOURS_TIMEUNIT = Generalization(general=TIMEUNIT, specific=ioT_HOURS)
gen_ioT_DAYS_TIMEUNIT = Generalization(general=TIMEUNIT, specific=ioT_DAYS)
gen_ioT_WEEKS_TIMEUNIT = Generalization(general=TIMEUNIT, specific=ioT_WEEKS)
gen_ioT_ClearListAction_Action = Generalization(general=Action, specific=ioT_ClearListAction)
gen_ioT_LEDAction_Action = Generalization(general=Action, specific=ioT_LEDAction)
gen_ioT_ArrowCommand_Command = Generalization(general=Command, specific=ioT_ArrowCommand)
gen_ioT_VarAccess_Expression = Generalization(general=Expression, specific=ioT_VarAccess)
gen_ioT_ItemInt_Comparison = Generalization(general=Comparison, specific=ioT_ItemInt)
gen_ioT_ItemBool_Comparison = Generalization(general=Comparison, specific=ioT_ItemBool)
gen_ioT_GT_ComparisonOp = Generalization(general=ComparisonOp, specific=ioT_GT)
gen_ioT_LT_ComparisonOp = Generalization(general=ComparisonOp, specific=ioT_LT)
gen_ioT_LE_ComparisonOp = Generalization(general=ComparisonOp, specific=ioT_LE)
gen_ioT_GE_ComparisonOp = Generalization(general=ComparisonOp, specific=ioT_GE)
gen_ioT_EQ_ComparisonOp = Generalization(general=ComparisonOp, specific=ioT_EQ)
gen_ioT_NE_ComparisonOp = Generalization(general=ComparisonOp, specific=ioT_NE)
gen_ioT_True_Bool = Generalization(general=Bool, specific=ioT_True)
gen_ioT_False_Bool = Generalization(general=Bool, specific=ioT_False)
gen_ioT_OR_Comparison = Generalization(general=Comparison, specific=ioT_OR)
gen_ioT_AND_Comparison = Generalization(general=Comparison, specific=ioT_AND)
gen_ioT_EQL_Comparison = Generalization(general=Comparison, specific=ioT_EQL)
gen_ioT_ItemVariable_Comparison = Generalization(general=Comparison, specific=ioT_ItemVariable)

# Domain Model
domain_model = DomainModel(
    name="ioT",
    types={ioT_Model, ioT_ExternalDeclaration, ioT_Config, ioT_Device, ioT_Loop, ioT_ExpressionRight, ioT_ConnectionConfig, ioT_Address, ioT_Declaration, ioT_Program, ioT_ControllerDevice, Device, ioT_IoTDevice, ioT_WifiStatement, ioT_ConnectStatement, ioT_VarOrList, ioT_ListenStatement, ioT_ReadConnection, ioT_ExternalOf, ioT_ReadSensor, ioT_SENSOR, ioT_Block, ExpressionRight, ioT_ExternalRight, ioT_Expression, ioT_TIMEUNIT, ioT_Command, ioT_Action, Command, ioT_ExpressionLeft, ExpressionLeft, ioT_BoolExpression, Expression, ioT_Bool, ioT_IntExpression, ioT_ReadVariable, ioT_Variable, ioT_ElseBlock, ioT_Comparison, ioT_ComparisonOp, ioT_DeviceConfig, Config, ioT_IpAddress, Address, ioT_WindowsSerialAddress, ioT_UnixSerialAddress, VarOrList, ioT_PyList, ioT_MILLISECONDS, TIMEUNIT, ioT_LIGHTSENSOR, SENSOR, ioT_TEMPERATURE, ioT_HUMIDITY, ioT_ToVar, ioT_AddToList, ioT_SendCommand, ioT_IfStatement, ioT_SECONDS, ioT_MINUTES, ioT_HOURS, ioT_DAYS, ioT_WEEKS, ioT_ClearListAction, Action, ioT_LEDAction, ioT_ArrowCommand, ioT_VarAccess, ioT_ItemBool, ioT_GT, ComparisonOp, ioT_LT, ioT_LE, ioT_GE, ioT_EQ, ioT_NE, ioT_True, Bool, ioT_False, ioT_OR, Comparison, ioT_AND, ioT_EQL, ioT_ItemVariable, ioT_ItemInt},
    associations={externalDeclarations0, configs1, devices3, listenStatements15, loops17, body19, connectionConfig21, device23, address26, configuration28, declarations5, program7, wifiStatements9, connectStatements11, variables13, source39, method41, target43, sensor46, commands47, method49, timeVal31, timeUnit33, command35, value37, value38, commands51, value53, variableName61, variable63, list65, target67, condition69, commands70, elseBlock73, list56, left57, right58, value95, left76, right78, left81, right83, left86, op88, right90, value93},
    generalizations={gen_ioT_ControllerDevice_Device, gen_ioT_IoTDevice_Device, gen_ioT_ReadConnection_ExpressionLeft, gen_ioT_ExternalOf_ExpressionLeft, gen_ioT_ReadSensor_ExpressionLeft, gen_ioT_Block_ExpressionRight, gen_ioT_ExternalRight_ExpressionRight, gen_ioT_Action_Command, gen_ioT_Expression_ExpressionLeft, gen_ioT_BoolExpression_Expression, gen_ioT_IntExpression_Expression, gen_ioT_ReadVariable_ExpressionLeft, gen_ioT_DeviceConfig_Config, gen_ioT_ConnectionConfig_Config, gen_ioT_IpAddress_Address, gen_ioT_WindowsSerialAddress_Address, gen_ioT_UnixSerialAddress_Address, gen_ioT_Variable_VarOrList, gen_ioT_PyList_VarOrList, gen_ioT_MILLISECONDS_TIMEUNIT, gen_ioT_LIGHTSENSOR_SENSOR, gen_ioT_TEMPERATURE_SENSOR, gen_ioT_HUMIDITY_SENSOR, gen_ioT_ToVar_ExpressionRight, gen_ioT_AddToList_ExpressionRight, gen_ioT_SendCommand_ExpressionRight, gen_ioT_IfStatement_Command, gen_ioT_SECONDS_TIMEUNIT, gen_ioT_MINUTES_TIMEUNIT, gen_ioT_HOURS_TIMEUNIT, gen_ioT_DAYS_TIMEUNIT, gen_ioT_WEEKS_TIMEUNIT, gen_ioT_ClearListAction_Action, gen_ioT_LEDAction_Action, gen_ioT_ArrowCommand_Command, gen_ioT_VarAccess_Expression, gen_ioT_ItemInt_Comparison, gen_ioT_ItemBool_Comparison, gen_ioT_GT_ComparisonOp, gen_ioT_LT_ComparisonOp, gen_ioT_LE_ComparisonOp, gen_ioT_GE_ComparisonOp, gen_ioT_EQ_ComparisonOp, gen_ioT_NE_ComparisonOp, gen_ioT_True_Bool, gen_ioT_False_Bool, gen_ioT_OR_Comparison, gen_ioT_AND_Comparison, gen_ioT_EQL_Comparison, gen_ioT_ItemVariable_Comparison},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)