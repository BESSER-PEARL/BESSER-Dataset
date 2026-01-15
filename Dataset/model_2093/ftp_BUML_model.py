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
SignalValues: Enumeration = Enumeration(
    name="SignalValues",
    literals={
            EnumerationLiteral(name="off"),
			EnumerationLiteral(name="on"),
			EnumerationLiteral(name="any")
    }
)

VisualValues: Enumeration = Enumeration(
    name="VisualValues",
    literals={
            EnumerationLiteral(name="light"),
			EnumerationLiteral(name="dark"),
			EnumerationLiteral(name="any")
    }
)

# Classes
ftp_FaultTree = Class(name="ftp::FaultTree")
ftp_OrGate = Class(name="ftp::OrGate")
FTNode = Class(name="FTNode")
ftp_AndGate = Class(name="ftp::AndGate")
ftp_Fault = Class(name="ftp::Fault")
ftp_Observation = Class(name="ftp::Observation")
ftp_Component = Class(name="ftp::Component")
ftp_PortValue = Class(name="ftp::PortValue")
ftp_FTNode = Class(name="ftp::FTNode")
ftp_Port = Class(name="ftp::Port")
ftp_Connection = Class(name="ftp::Connection")
ftp_DigintalConnection = Class(name="ftp::DigintalConnection")
Connection = Class(name="Connection")
ftp_AnalogConnection = Class(name="ftp::AnalogConnection")
ftp_SignalConnection = Class(name="ftp::SignalConnection")
DigintalConnection = Class(name="DigintalConnection")
ftp_ElectricalConnection = Class(name="ftp::ElectricalConnection")
AnalogConnection = Class(name="AnalogConnection")
ftp_HydraulicConnection = Class(name="ftp::HydraulicConnection")
ftp_MechanicalConnection = Class(name="ftp::MechanicalConnection")
ftp_PrimitiveComponent = Class(name="ftp::PrimitiveComponent")
Component = Class(name="Component")
CompositionElement = Class(name="CompositionElement")
ftp_TypedPortValue = Class(name="ftp::TypedPortValue")
ftp_Resistor = Class(name="ftp::Resistor")
PrimitiveComponent = Class(name="PrimitiveComponent")
ftp_ElectricalPort = Class(name="ftp::ElectricalPort")
ftp_Capacitor = Class(name="ftp::Capacitor")
ftp_AnalogBattery = Class(name="ftp::AnalogBattery")
ftp_ComposedComponent = Class(name="ftp::ComposedComponent")
ftp_CompositionElement = Class(name="ftp::CompositionElement")
ftp_SignalPort = Class(name="ftp::SignalPort")
ftp_AnalogLamp = Class(name="ftp::AnalogLamp")
ftp_VisualPort = Class(name="ftp::VisualPort")
ftp_DigitalBattery = Class(name="ftp::DigitalBattery")
ftp_AnalogSwitch = Class(name="ftp::AnalogSwitch")
ftp_DigitalLamp = Class(name="ftp::DigitalLamp")
ftp_Not = Class(name="ftp::Not")
ftp_Xor = Class(name="ftp::Xor")
ftp_And = Class(name="ftp::And")
ftp_NTransistor = Class(name="ftp::NTransistor")
ftp_DigitalSwitch = Class(name="ftp::DigitalSwitch")
ftp_PTransistor = Class(name="ftp::PTransistor")
ftp_DFlipFlop = Class(name="ftp::DFlipFlop")
ftp_VisualConnection = Class(name="ftp::VisualConnection")
ftp_FaultTreeContext = Class(name="ftp::FaultTreeContext")
ftp_RootEvent = Class(name="ftp::RootEvent")
ftp_MechanicalPort = Class(name="ftp::MechanicalPort")
ftp_SignalValue = Class(name="ftp::SignalValue")
TypedPortValue = Class(name="TypedPortValue")
ftp_ElectricalValue = Class(name="ftp::ElectricalValue")
Port = Class(name="Port")
ftp_HydraulicPort = Class(name="ftp::HydraulicPort")
ftp_VisualValue = Class(name="ftp::VisualValue")
ftp_FloatValue = Class(name="ftp::FloatValue")
ftp_SignalConstant = Class(name="ftp::SignalConstant")
ftp_HydraulicValue = Class(name="ftp::HydraulicValue")

# ftp_FaultTree class attributes and methods

# ftp_OrGate class attributes and methods

# FTNode class attributes and methods

# ftp_AndGate class attributes and methods

# ftp_Fault class attributes and methods
ftp_Fault_description: Property = Property(name="description", type=StringType)
ftp_Fault.attributes={ftp_Fault_description}

# ftp_Observation class attributes and methods
ftp_Observation_name: Property = Property(name="name", type=StringType)
ftp_Observation_faultLimit: Property = Property(name="faultLimit", type=IntegerType)
ftp_Observation_m_buildFaultTree: Method = Method(name="buildFaultTree", parameters={}, type=StringType)
ftp_Observation.attributes={ftp_Observation_faultLimit, ftp_Observation_name}
ftp_Observation.methods={ftp_Observation_m_buildFaultTree}

# ftp_Component class attributes and methods
ftp_Component_name: Property = Property(name="name", type=StringType)
ftp_Component_type: Property = Property(name="type", type=StringType)
ftp_Component.attributes={ftp_Component_name, ftp_Component_type}

# ftp_PortValue class attributes and methods

# ftp_FTNode class attributes and methods

# ftp_Port class attributes and methods
ftp_Port_name: Property = Property(name="name", type=StringType)
ftp_Port_type: Property = Property(name="type", type=StringType)
ftp_Port_m_newPortValue: Method = Method(name="newPortValue", parameters={}, type=StringType)
ftp_Port.attributes={ftp_Port_name, ftp_Port_type}
ftp_Port.methods={ftp_Port_m_newPortValue}

# ftp_Connection class attributes and methods

# ftp_DigintalConnection class attributes and methods

# Connection class attributes and methods

# ftp_AnalogConnection class attributes and methods

# ftp_SignalConnection class attributes and methods

# DigintalConnection class attributes and methods

# ftp_ElectricalConnection class attributes and methods

# AnalogConnection class attributes and methods

# ftp_HydraulicConnection class attributes and methods

# ftp_MechanicalConnection class attributes and methods

# ftp_PrimitiveComponent class attributes and methods

# Component class attributes and methods

# CompositionElement class attributes and methods

# ftp_TypedPortValue class attributes and methods

# ftp_Resistor class attributes and methods
ftp_Resistor_resistance: Property = Property(name="resistance", type=FloatType)
ftp_Resistor.attributes={ftp_Resistor_resistance}

# PrimitiveComponent class attributes and methods

# ftp_ElectricalPort class attributes and methods

# ftp_Capacitor class attributes and methods

# ftp_AnalogBattery class attributes and methods
ftp_AnalogBattery_voltage: Property = Property(name="voltage", type=FloatType)
ftp_AnalogBattery.attributes={ftp_AnalogBattery_voltage}

# ftp_ComposedComponent class attributes and methods

# ftp_CompositionElement class attributes and methods

# ftp_SignalPort class attributes and methods

# ftp_AnalogLamp class attributes and methods

# ftp_VisualPort class attributes and methods

# ftp_DigitalBattery class attributes and methods

# ftp_AnalogSwitch class attributes and methods

# ftp_DigitalLamp class attributes and methods

# ftp_Not class attributes and methods

# ftp_Xor class attributes and methods

# ftp_And class attributes and methods

# ftp_NTransistor class attributes and methods

# ftp_DigitalSwitch class attributes and methods

# ftp_PTransistor class attributes and methods

# ftp_DFlipFlop class attributes and methods

# ftp_VisualConnection class attributes and methods

# ftp_FaultTreeContext class attributes and methods

# ftp_RootEvent class attributes and methods
ftp_RootEvent_observation: Property = Property(name="observation", type=StringType)
ftp_RootEvent.attributes={ftp_RootEvent_observation}

# ftp_MechanicalPort class attributes and methods

# ftp_SignalValue class attributes and methods
ftp_SignalValue_signal: Property = Property(name="signal", type=StringType)
ftp_SignalValue.attributes={ftp_SignalValue_signal}

# TypedPortValue class attributes and methods

# ftp_ElectricalValue class attributes and methods
ftp_ElectricalValue_current: Property = Property(name="current", type=FloatType)
ftp_ElectricalValue_voltage: Property = Property(name="voltage", type=FloatType)
ftp_ElectricalValue_anyCurrent: Property = Property(name="anyCurrent", type=BooleanType)
ftp_ElectricalValue_anyVoltage: Property = Property(name="anyVoltage", type=BooleanType)
ftp_ElectricalValue.attributes={ftp_ElectricalValue_anyVoltage, ftp_ElectricalValue_voltage, ftp_ElectricalValue_current, ftp_ElectricalValue_anyCurrent}

# Port class attributes and methods

# ftp_HydraulicPort class attributes and methods

# ftp_VisualValue class attributes and methods
ftp_VisualValue_bulb: Property = Property(name="bulb", type=StringType)
ftp_VisualValue.attributes={ftp_VisualValue_bulb}

# ftp_FloatValue class attributes and methods
ftp_FloatValue_value: Property = Property(name="value", type=FloatType)
ftp_FloatValue.attributes={ftp_FloatValue_value}

# ftp_SignalConstant class attributes and methods
ftp_SignalConstant_value: Property = Property(name="value", type=StringType)
ftp_SignalConstant.attributes={ftp_SignalConstant_value}

# ftp_HydraulicValue class attributes and methods
ftp_HydraulicValue_pressure: Property = Property(name="pressure", type=FloatType)
ftp_HydraulicValue_anyFlow: Property = Property(name="anyFlow", type=BooleanType)
ftp_HydraulicValue_anyPressure: Property = Property(name="anyPressure", type=BooleanType)
ftp_HydraulicValue_flow: Property = Property(name="flow", type=FloatType)
ftp_HydraulicValue.attributes={ftp_HydraulicValue_flow, ftp_HydraulicValue_anyFlow, ftp_HydraulicValue_pressure, ftp_HydraulicValue_anyPressure}

# Relationships
inputs4: BinaryAssociation = BinaryAssociation(
    name="inputs4",
    ends={
        Property(name="ftp_FTNode5", type=ftp_OrGate, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_OrGate", type=ftp_FTNode, multiplicity=Multiplicity(2, 9999))
    }
)
inputs6: BinaryAssociation = BinaryAssociation(
    name="inputs6",
    ends={
        Property(name="ftp_FTNode7", type=ftp_AndGate, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_AndGate", type=ftp_FTNode, multiplicity=Multiplicity(2, 9999))
    }
)
component8: BinaryAssociation = BinaryAssociation(
    name="component8",
    ends={
        Property(name="ftp_Component", type=ftp_Observation, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_Observation", type=ftp_Component, multiplicity=Multiplicity(1, 1))
    }
)
portValues9: BinaryAssociation = BinaryAssociation(
    name="portValues9",
    ends={
        Property(name="ftp_PortValue", type=ftp_Observation, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_Observation10", type=ftp_PortValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ftnodes0: BinaryAssociation = BinaryAssociation(
    name="ftnodes0",
    ends={
        Property(name="ftp_FTNode", type=ftp_FaultTree, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_FaultTree", type=ftp_FTNode, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
root1: BinaryAssociation = BinaryAssociation(
    name="root1",
    ends={
        Property(name="ftp_FTNode3", type=ftp_FaultTree, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_FaultTree2", type=ftp_FTNode, multiplicity=Multiplicity(1, 1))
    }
)
fromPort14: BinaryAssociation = BinaryAssociation(
    name="fromPort14",
    ends={
        Property(name="ftp_Port", type=ftp_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_Connection", type=ftp_Port, multiplicity=Multiplicity(1, 1))
    }
)
toPort15: BinaryAssociation = BinaryAssociation(
    name="toPort15",
    ends={
        Property(name="ftp_Port17", type=ftp_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_Connection16", type=ftp_Port, multiplicity=Multiplicity(1, 1))
    }
)
faulttree11: BinaryAssociation = BinaryAssociation(
    name="faulttree11",
    ends={
        Property(name="ftp_FaultTree13", type=ftp_Observation, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_Observation12", type=ftp_FaultTree, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ports19: BinaryAssociation = BinaryAssociation(
    name="ports19",
    ends={
        Property(name="ftp_Port21", type=ftp_ComposedComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_ComposedComponent20", type=ftp_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
port22: BinaryAssociation = BinaryAssociation(
    name="port22",
    ends={
        Property(name="ftp_Port24", type=ftp_PortValue, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_PortValue23", type=ftp_Port, multiplicity=Multiplicity(1, 1))
    }
)
value25: BinaryAssociation = BinaryAssociation(
    name="value25",
    ends={
        Property(name="ftp_TypedPortValue", type=ftp_PortValue, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_PortValue26", type=ftp_TypedPortValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inPort27: BinaryAssociation = BinaryAssociation(
    name="inPort27",
    ends={
        Property(name="ftp_ElectricalPort", type=ftp_Resistor, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_Resistor", type=ftp_ElectricalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outPort28: BinaryAssociation = BinaryAssociation(
    name="outPort28",
    ends={
        Property(name="ftp_ElectricalPort30", type=ftp_Resistor, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_Resistor29", type=ftp_ElectricalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inPort36: BinaryAssociation = BinaryAssociation(
    name="inPort36",
    ends={
        Property(name="ftp_ElectricalPort37", type=ftp_AnalogSwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_AnalogSwitch", type=ftp_ElectricalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
composition18: BinaryAssociation = BinaryAssociation(
    name="composition18",
    ends={
        Property(name="ftp_CompositionElement", type=ftp_ComposedComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_ComposedComponent", type=ftp_CompositionElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
setPort38: BinaryAssociation = BinaryAssociation(
    name="setPort38",
    ends={
        Property(name="ftp_SignalPort", type=ftp_AnalogSwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_AnalogSwitch39", type=ftp_SignalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outPort40: BinaryAssociation = BinaryAssociation(
    name="outPort40",
    ends={
        Property(name="ftp_ElectricalPort42", type=ftp_AnalogSwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_AnalogSwitch41", type=ftp_ElectricalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inPort43: BinaryAssociation = BinaryAssociation(
    name="inPort43",
    ends={
        Property(name="ftp_ElectricalPort44", type=ftp_AnalogLamp, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_AnalogLamp", type=ftp_ElectricalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outPort45: BinaryAssociation = BinaryAssociation(
    name="outPort45",
    ends={
        Property(name="ftp_ElectricalPort47", type=ftp_AnalogLamp, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_AnalogLamp46", type=ftp_ElectricalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lightPort48: BinaryAssociation = BinaryAssociation(
    name="lightPort48",
    ends={
        Property(name="ftp_VisualPort", type=ftp_AnalogLamp, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_AnalogLamp49", type=ftp_VisualPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inPort31: BinaryAssociation = BinaryAssociation(
    name="inPort31",
    ends={
        Property(name="ftp_ElectricalPort32", type=ftp_AnalogBattery, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_AnalogBattery", type=ftp_ElectricalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inPort50: BinaryAssociation = BinaryAssociation(
    name="inPort50",
    ends={
        Property(name="ftp_SignalPort51", type=ftp_DigitalBattery, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_DigitalBattery", type=ftp_SignalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outPort33: BinaryAssociation = BinaryAssociation(
    name="outPort33",
    ends={
        Property(name="ftp_ElectricalPort35", type=ftp_AnalogBattery, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_AnalogBattery34", type=ftp_ElectricalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
setPort57: BinaryAssociation = BinaryAssociation(
    name="setPort57",
    ends={
        Property(name="ftp_SignalPort59", type=ftp_DigitalSwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_DigitalSwitch58", type=ftp_SignalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outPort60: BinaryAssociation = BinaryAssociation(
    name="outPort60",
    ends={
        Property(name="ftp_SignalPort62", type=ftp_DigitalSwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_DigitalSwitch61", type=ftp_SignalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inPort63: BinaryAssociation = BinaryAssociation(
    name="inPort63",
    ends={
        Property(name="ftp_SignalPort64", type=ftp_DigitalLamp, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_DigitalLamp", type=ftp_SignalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outPort65: BinaryAssociation = BinaryAssociation(
    name="outPort65",
    ends={
        Property(name="ftp_SignalPort67", type=ftp_DigitalLamp, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_DigitalLamp66", type=ftp_SignalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lightPort68: BinaryAssociation = BinaryAssociation(
    name="lightPort68",
    ends={
        Property(name="ftp_VisualPort70", type=ftp_DigitalLamp, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_DigitalLamp69", type=ftp_VisualPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
gate71: BinaryAssociation = BinaryAssociation(
    name="gate71",
    ends={
        Property(name="ftp_SignalPort72", type=ftp_NTransistor, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_NTransistor", type=ftp_SignalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outPort52: BinaryAssociation = BinaryAssociation(
    name="outPort52",
    ends={
        Property(name="ftp_SignalPort54", type=ftp_DigitalBattery, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_DigitalBattery53", type=ftp_SignalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inPort55: BinaryAssociation = BinaryAssociation(
    name="inPort55",
    ends={
        Property(name="ftp_SignalPort56", type=ftp_DigitalSwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_DigitalSwitch", type=ftp_SignalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
gate79: BinaryAssociation = BinaryAssociation(
    name="gate79",
    ends={
        Property(name="ftp_SignalPort80", type=ftp_PTransistor, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_PTransistor", type=ftp_SignalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source81: BinaryAssociation = BinaryAssociation(
    name="source81",
    ends={
        Property(name="ftp_SignalPort83", type=ftp_PTransistor, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_PTransistor82", type=ftp_SignalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
drain84: BinaryAssociation = BinaryAssociation(
    name="drain84",
    ends={
        Property(name="ftp_SignalPort86", type=ftp_PTransistor, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_PTransistor85", type=ftp_SignalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inPort87: BinaryAssociation = BinaryAssociation(
    name="inPort87",
    ends={
        Property(name="ftp_SignalPort88", type=ftp_DFlipFlop, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_DFlipFlop", type=ftp_SignalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
clockPort89: BinaryAssociation = BinaryAssociation(
    name="clockPort89",
    ends={
        Property(name="ftp_SignalPort91", type=ftp_DFlipFlop, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_DFlipFlop90", type=ftp_SignalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outPort92: BinaryAssociation = BinaryAssociation(
    name="outPort92",
    ends={
        Property(name="ftp_SignalPort94", type=ftp_DFlipFlop, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_DFlipFlop93", type=ftp_SignalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statePort95: BinaryAssociation = BinaryAssociation(
    name="statePort95",
    ends={
        Property(name="ftp_SignalPort97", type=ftp_DFlipFlop, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_DFlipFlop96", type=ftp_SignalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source73: BinaryAssociation = BinaryAssociation(
    name="source73",
    ends={
        Property(name="ftp_SignalPort75", type=ftp_NTransistor, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_NTransistor74", type=ftp_SignalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
drain76: BinaryAssociation = BinaryAssociation(
    name="drain76",
    ends={
        Property(name="ftp_SignalPort78", type=ftp_NTransistor, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_NTransistor77", type=ftp_SignalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
composition98: BinaryAssociation = BinaryAssociation(
    name="composition98",
    ends={
        Property(name="ftp_ComposedComponent99", type=ftp_FaultTreeContext, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_FaultTreeContext", type=ftp_ComposedComponent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
observations100: BinaryAssociation = BinaryAssociation(
    name="observations100",
    ends={
        Property(name="ftp_Observation102", type=ftp_FaultTreeContext, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_FaultTreeContext101", type=ftp_Observation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputs103: BinaryAssociation = BinaryAssociation(
    name="inputs103",
    ends={
        Property(name="ftp_FTNode104", type=ftp_RootEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_RootEvent", type=ftp_FTNode, multiplicity=Multiplicity(1, 9999))
    }
)
outPort105: BinaryAssociation = BinaryAssociation(
    name="outPort105",
    ends={
        Property(name="ftp_SignalPort106", type=ftp_SignalConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="ftp_SignalConstant", type=ftp_SignalPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_ftp_OrGate_FTNode = Generalization(general=FTNode, specific=ftp_OrGate)
gen_ftp_AndGate_FTNode = Generalization(general=FTNode, specific=ftp_AndGate)
gen_ftp_Fault_FTNode = Generalization(general=FTNode, specific=ftp_Fault)
gen_ftp_Connection_CompositionElement = Generalization(general=CompositionElement, specific=ftp_Connection)
gen_ftp_DigintalConnection_Connection = Generalization(general=Connection, specific=ftp_DigintalConnection)
gen_ftp_AnalogConnection_Connection = Generalization(general=Connection, specific=ftp_AnalogConnection)
gen_ftp_SignalConnection_DigintalConnection = Generalization(general=DigintalConnection, specific=ftp_SignalConnection)
gen_ftp_ElectricalConnection_AnalogConnection = Generalization(general=AnalogConnection, specific=ftp_ElectricalConnection)
gen_ftp_HydraulicConnection_AnalogConnection = Generalization(general=AnalogConnection, specific=ftp_HydraulicConnection)
gen_ftp_MechanicalConnection_AnalogConnection = Generalization(general=AnalogConnection, specific=ftp_MechanicalConnection)
gen_ftp_Component_CompositionElement = Generalization(general=CompositionElement, specific=ftp_Component)
gen_ftp_Resistor_PrimitiveComponent = Generalization(general=PrimitiveComponent, specific=ftp_Resistor)
gen_ftp_Capacitor_PrimitiveComponent = Generalization(general=PrimitiveComponent, specific=ftp_Capacitor)
gen_ftp_AnalogBattery_PrimitiveComponent = Generalization(general=PrimitiveComponent, specific=ftp_AnalogBattery)
gen_ftp_PrimitiveComponent_Component = Generalization(general=Component, specific=ftp_PrimitiveComponent)
gen_ftp_ComposedComponent_Component = Generalization(general=Component, specific=ftp_ComposedComponent)
gen_ftp_AnalogLamp_PrimitiveComponent = Generalization(general=PrimitiveComponent, specific=ftp_AnalogLamp)
gen_ftp_DigitalBattery_PrimitiveComponent = Generalization(general=PrimitiveComponent, specific=ftp_DigitalBattery)
gen_ftp_AnalogSwitch_PrimitiveComponent = Generalization(general=PrimitiveComponent, specific=ftp_AnalogSwitch)
gen_ftp_DigitalLamp_PrimitiveComponent = Generalization(general=PrimitiveComponent, specific=ftp_DigitalLamp)
gen_ftp_Not_PrimitiveComponent = Generalization(general=PrimitiveComponent, specific=ftp_Not)
gen_ftp_Xor_PrimitiveComponent = Generalization(general=PrimitiveComponent, specific=ftp_Xor)
gen_ftp_And_PrimitiveComponent = Generalization(general=PrimitiveComponent, specific=ftp_And)
gen_ftp_NTransistor_PrimitiveComponent = Generalization(general=PrimitiveComponent, specific=ftp_NTransistor)
gen_ftp_DigitalSwitch_PrimitiveComponent = Generalization(general=PrimitiveComponent, specific=ftp_DigitalSwitch)
gen_ftp_PTransistor_PrimitiveComponent = Generalization(general=PrimitiveComponent, specific=ftp_PTransistor)
gen_ftp_DFlipFlop_PrimitiveComponent = Generalization(general=PrimitiveComponent, specific=ftp_DFlipFlop)
gen_ftp_VisualPort_Port = Generalization(general=Port, specific=ftp_VisualPort)
gen_ftp_VisualConnection_Connection = Generalization(general=Connection, specific=ftp_VisualConnection)
gen_ftp_RootEvent_FTNode = Generalization(general=FTNode, specific=ftp_RootEvent)
gen_ftp_MechanicalPort_Port = Generalization(general=Port, specific=ftp_MechanicalPort)
gen_ftp_SignalValue_TypedPortValue = Generalization(general=TypedPortValue, specific=ftp_SignalValue)
gen_ftp_ElectricalValue_TypedPortValue = Generalization(general=TypedPortValue, specific=ftp_ElectricalValue)
gen_ftp_SignalPort_Port = Generalization(general=Port, specific=ftp_SignalPort)
gen_ftp_ElectricalPort_Port = Generalization(general=Port, specific=ftp_ElectricalPort)
gen_ftp_HydraulicPort_Port = Generalization(general=Port, specific=ftp_HydraulicPort)
gen_ftp_VisualValue_TypedPortValue = Generalization(general=TypedPortValue, specific=ftp_VisualValue)
gen_ftp_FloatValue_TypedPortValue = Generalization(general=TypedPortValue, specific=ftp_FloatValue)
gen_ftp_SignalConstant_PrimitiveComponent = Generalization(general=PrimitiveComponent, specific=ftp_SignalConstant)
gen_ftp_HydraulicValue_TypedPortValue = Generalization(general=TypedPortValue, specific=ftp_HydraulicValue)

# Domain Model
domain_model = DomainModel(
    name="ftp",
    types={ftp_FaultTree, ftp_OrGate, FTNode, ftp_AndGate, ftp_Fault, ftp_Observation, ftp_Component, ftp_PortValue, ftp_FTNode, ftp_Port, ftp_Connection, ftp_DigintalConnection, Connection, ftp_AnalogConnection, ftp_SignalConnection, DigintalConnection, ftp_ElectricalConnection, AnalogConnection, ftp_HydraulicConnection, ftp_MechanicalConnection, ftp_PrimitiveComponent, Component, CompositionElement, ftp_TypedPortValue, ftp_Resistor, PrimitiveComponent, ftp_ElectricalPort, ftp_Capacitor, ftp_AnalogBattery, ftp_ComposedComponent, ftp_CompositionElement, ftp_SignalPort, ftp_AnalogLamp, ftp_VisualPort, ftp_DigitalBattery, ftp_AnalogSwitch, ftp_DigitalLamp, ftp_Not, ftp_Xor, ftp_And, ftp_NTransistor, ftp_DigitalSwitch, ftp_PTransistor, ftp_DFlipFlop, ftp_VisualConnection, ftp_FaultTreeContext, ftp_RootEvent, ftp_MechanicalPort, ftp_SignalValue, TypedPortValue, ftp_ElectricalValue, Port, ftp_HydraulicPort, ftp_VisualValue, ftp_FloatValue, ftp_SignalConstant, ftp_HydraulicValue, SignalValues, VisualValues},
    associations={inputs4, inputs6, component8, portValues9, ftnodes0, root1, fromPort14, toPort15, faulttree11, ports19, port22, value25, inPort27, outPort28, inPort36, composition18, setPort38, outPort40, inPort43, outPort45, lightPort48, inPort31, inPort50, outPort33, setPort57, outPort60, inPort63, outPort65, lightPort68, gate71, outPort52, inPort55, gate79, source81, drain84, inPort87, clockPort89, outPort92, statePort95, source73, drain76, composition98, observations100, inputs103, outPort105},
    generalizations={gen_ftp_OrGate_FTNode, gen_ftp_AndGate_FTNode, gen_ftp_Fault_FTNode, gen_ftp_Connection_CompositionElement, gen_ftp_DigintalConnection_Connection, gen_ftp_AnalogConnection_Connection, gen_ftp_SignalConnection_DigintalConnection, gen_ftp_ElectricalConnection_AnalogConnection, gen_ftp_HydraulicConnection_AnalogConnection, gen_ftp_MechanicalConnection_AnalogConnection, gen_ftp_Component_CompositionElement, gen_ftp_Resistor_PrimitiveComponent, gen_ftp_Capacitor_PrimitiveComponent, gen_ftp_AnalogBattery_PrimitiveComponent, gen_ftp_PrimitiveComponent_Component, gen_ftp_ComposedComponent_Component, gen_ftp_AnalogLamp_PrimitiveComponent, gen_ftp_DigitalBattery_PrimitiveComponent, gen_ftp_AnalogSwitch_PrimitiveComponent, gen_ftp_DigitalLamp_PrimitiveComponent, gen_ftp_Not_PrimitiveComponent, gen_ftp_Xor_PrimitiveComponent, gen_ftp_And_PrimitiveComponent, gen_ftp_NTransistor_PrimitiveComponent, gen_ftp_DigitalSwitch_PrimitiveComponent, gen_ftp_PTransistor_PrimitiveComponent, gen_ftp_DFlipFlop_PrimitiveComponent, gen_ftp_VisualPort_Port, gen_ftp_VisualConnection_Connection, gen_ftp_RootEvent_FTNode, gen_ftp_MechanicalPort_Port, gen_ftp_SignalValue_TypedPortValue, gen_ftp_ElectricalValue_TypedPortValue, gen_ftp_SignalPort_Port, gen_ftp_ElectricalPort_Port, gen_ftp_HydraulicPort_Port, gen_ftp_VisualValue_TypedPortValue, gen_ftp_FloatValue_TypedPortValue, gen_ftp_SignalConstant_PrimitiveComponent, gen_ftp_HydraulicValue_TypedPortValue},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)