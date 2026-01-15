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
DataType: Enumeration = Enumeration(
    name="DataType",
    literals={
            EnumerationLiteral(name="INHERIT"),
			EnumerationLiteral(name="DOUBLE"),
			EnumerationLiteral(name="SINGLE"),
			EnumerationLiteral(name="INT32"),
			EnumerationLiteral(name="INT16"),
			EnumerationLiteral(name="INT8"),
			EnumerationLiteral(name="UINT32"),
			EnumerationLiteral(name="UINT16"),
			EnumerationLiteral(name="UINT8"),
			EnumerationLiteral(name="BOOLEAN"),
			EnumerationLiteral(name="BUS")
    }
)

TriggerEvent: Enumeration = Enumeration(
    name="TriggerEvent",
    literals={
            EnumerationLiteral(name="Rising"),
			EnumerationLiteral(name="Falling"),
			EnumerationLiteral(name="Either")
    }
)

SubStateType: Enumeration = Enumeration(
    name="SubStateType",
    literals={
            EnumerationLiteral(name="EXCLUSIVE"),
			EnumerationLiteral(name="PARALLEL")
    }
)

# Classes
simulink_Block = Class(name="simulink::Block", is_abstract=True)
Element = Class(name="Element")
simulink_SubSystem = Class(name="simulink::SubSystem")
simulink_OutPortBlock = Class(name="simulink::OutPortBlock")
simulink_InPortBlock = Class(name="simulink::InPortBlock")
simulink_SimulinkModel = Class(name="simulink::SimulinkModel")
SimulinkFile = Class(name="SimulinkFile")
simulink_SimulinkContainer = Class(name="simulink::SimulinkContainer")
simulink_Element = Class(name="simulink::Element", is_abstract=True)
simulink_Parameter = Class(name="simulink::Parameter")
simulink_Bus = Class(name="simulink::Bus")
Block = Class(name="Block")
simulink_Line = Class(name="simulink::Line")
PortBlock = Class(name="PortBlock")
simulink_EmbeddedMatlabFunction = Class(name="simulink::EmbeddedMatlabFunction")
simulink_MiscBlock = Class(name="simulink::MiscBlock")
simulink_SimulinkLibrary = Class(name="simulink::SimulinkLibrary")
simulink_LibraryReference = Class(name="simulink::LibraryReference")
simulink_SimulinkFile = Class(name="simulink::SimulinkFile", is_abstract=True)
SubSystem = Class(name="SubSystem")
StateflowMachine = Class(name="StateflowMachine")
simulink_ChartBlock = Class(name="simulink::ChartBlock")
Chart = Class(name="Chart")
simulink_BusElement = Class(name="simulink::BusElement")
simulink_BusCreator = Class(name="simulink::BusCreator")
simulink_BusSelector = Class(name="simulink::BusSelector")
simulink_DigitalClock = Class(name="simulink::DigitalClock")
simulink_Constant = Class(name="simulink::Constant")
simulink_TriggerPort = Class(name="simulink::TriggerPort")
InPortBlock = Class(name="InPortBlock")
simulink_EnablePort = Class(name="simulink::EnablePort")
simulink_PortBlock = Class(name="simulink::PortBlock")
simulink_UnitDelay = Class(name="simulink::UnitDelay")
simulink_ZeroOrderHold = Class(name="simulink::ZeroOrderHold")
simulink_stateflow_StateflowMachine = Class(name="simulink::stateflow::StateflowMachine")
StateflowElement = Class(name="StateflowElement")
stateflow_simulink_SimulinkFile = Class(name="stateflow::simulink::SimulinkFile")
simulink_stateflow_Chart = Class(name="simulink::stateflow::Chart")
State = Class(name="State")
Data = Class(name="Data")
stateflow_simulink_ChartBlock = Class(name="stateflow::simulink::ChartBlock")
simulink_stateflow_StateflowElement = Class(name="simulink::stateflow::StateflowElement")
simulink_stateflow_State = Class(name="simulink::stateflow::State")
Node = Class(name="Node")
Transition = Class(name="Transition")
EmbeddedFunction = Class(name="EmbeddedFunction")
Action = Class(name="Action")
simulink_stateflow_Transition = Class(name="simulink::stateflow::Transition")
simulink_stateflow_Junction = Class(name="simulink::stateflow::Junction")
simulink_stateflow_Node = Class(name="simulink::stateflow::Node", is_abstract=True)
Event = Class(name="Event")
simulink_stateflow_Event = Class(name="simulink::stateflow::Event")
simulink_stateflow_History = Class(name="simulink::stateflow::History")
simulink_stateflow_EmbeddedFunction = Class(name="simulink::stateflow::EmbeddedFunction")
simulink_stateflow_Action = Class(name="simulink::stateflow::Action")
simulink_stateflow_Data = Class(name="simulink::stateflow::Data")
simulink_msglib_CommunicationSwitch = Class(name="simulink::msglib::CommunicationSwitch")
simulink_msglib_LinkLayer = Class(name="simulink::msglib::LinkLayer")
simulink_buffer_Enqueue = Class(name="simulink::buffer::Enqueue")
BufferFunction = Class(name="BufferFunction")
simulink_buffer_Dequeue = Class(name="simulink::buffer::Dequeue")
simulink_buffer_CheckQueue = Class(name="simulink::buffer::CheckQueue")
simulink_buffer_SharedEnqueue = Class(name="simulink::buffer::SharedEnqueue")
simulink_buffer_SharedDequeue = Class(name="simulink::buffer::SharedDequeue")
simulink_buffer_SharedCheckQueue = Class(name="simulink::buffer::SharedCheckQueue")
simulink_buffer_BufferFunction = Class(name="simulink::buffer::BufferFunction")
simulink_reconfiguration_MultiTargetControl = Class(name="simulink::reconfiguration::MultiTargetControl")
simulink_reconfiguration_MultiSourceControl = Class(name="simulink::reconfiguration::MultiSourceControl")
simulink_reconfiguration_FadingComponent = Class(name="simulink::reconfiguration::FadingComponent")

# simulink_Block class attributes and methods
simulink_Block_name: Property = Property(name="name", type=StringType)
simulink_Block_m_getFullyQualifiedName: Method = Method(name="getFullyQualifiedName", parameters={}, type=StringType)
simulink_Block.attributes={simulink_Block_name}
simulink_Block.methods={simulink_Block_m_getFullyQualifiedName}

# Element class attributes and methods

# simulink_SubSystem class attributes and methods
simulink_SubSystem_m_getBlockByName: Method = Method(name="getBlockByName", parameters={Parameter(name='name')}, type=Block)
simulink_SubSystem.methods={simulink_SubSystem_m_getBlockByName}

# simulink_OutPortBlock class attributes and methods

# simulink_InPortBlock class attributes and methods

# simulink_SimulinkModel class attributes and methods

# SimulinkFile class attributes and methods

# simulink_SimulinkContainer class attributes and methods

# simulink_Element class attributes and methods
simulink_Element_id: Property = Property(name="id", type=StringType)
simulink_Element_m_getParameter: Method = Method(name="getParameter", parameters={Parameter(name='name')}, type=StringType)
simulink_Element.attributes={simulink_Element_id}
simulink_Element.methods={simulink_Element_m_getParameter}

# simulink_Parameter class attributes and methods
simulink_Parameter_name: Property = Property(name="name", type=StringType)
simulink_Parameter_value: Property = Property(name="value", type=StringType)
simulink_Parameter_type: Property = Property(name="type", type=StringType)
simulink_Parameter.attributes={simulink_Parameter_name, simulink_Parameter_value, simulink_Parameter_type}

# simulink_Bus class attributes and methods
simulink_Bus_name: Property = Property(name="name", type=StringType)
simulink_Bus.attributes={simulink_Bus_name}

# Block class attributes and methods

# simulink_Line class attributes and methods

# PortBlock class attributes and methods

# simulink_EmbeddedMatlabFunction class attributes and methods
simulink_EmbeddedMatlabFunction_code: Property = Property(name="code", type=StringType)
simulink_EmbeddedMatlabFunction.attributes={simulink_EmbeddedMatlabFunction_code}

# simulink_MiscBlock class attributes and methods
simulink_MiscBlock_type: Property = Property(name="type", type=StringType)
simulink_MiscBlock.attributes={simulink_MiscBlock_type}

# simulink_SimulinkLibrary class attributes and methods

# simulink_LibraryReference class attributes and methods

# simulink_SimulinkFile class attributes and methods

# SubSystem class attributes and methods

# StateflowMachine class attributes and methods

# simulink_ChartBlock class attributes and methods

# Chart class attributes and methods

# simulink_BusElement class attributes and methods
simulink_BusElement_name: Property = Property(name="name", type=StringType)
simulink_BusElement_dimensions: Property = Property(name="dimensions", type=StringType)
simulink_BusElement_type: Property = Property(name="type", type=StringType)
simulink_BusElement.attributes={simulink_BusElement_type, simulink_BusElement_name, simulink_BusElement_dimensions}

# simulink_BusCreator class attributes and methods

# simulink_BusSelector class attributes and methods

# simulink_DigitalClock class attributes and methods
simulink_DigitalClock_sampleTime: Property = Property(name="sampleTime", type=FloatType)
simulink_DigitalClock.attributes={simulink_DigitalClock_sampleTime}

# simulink_Constant class attributes and methods
simulink_Constant_value: Property = Property(name="value", type=StringType)
simulink_Constant_type: Property = Property(name="type", type=StringType)
simulink_Constant.attributes={simulink_Constant_type, simulink_Constant_value}

# simulink_TriggerPort class attributes and methods
simulink_TriggerPort_triggerInput: Property = Property(name="triggerInput", type=StringType)
simulink_TriggerPort.attributes={simulink_TriggerPort_triggerInput}

# InPortBlock class attributes and methods

# simulink_EnablePort class attributes and methods

# simulink_PortBlock class attributes and methods
simulink_PortBlock_dimensions: Property = Property(name="dimensions", type=StringType)
simulink_PortBlock_type: Property = Property(name="type", type=StringType)
simulink_PortBlock_initialCondition: Property = Property(name="initialCondition", type=StringType)
simulink_PortBlock.attributes={simulink_PortBlock_initialCondition, simulink_PortBlock_type, simulink_PortBlock_dimensions}

# simulink_UnitDelay class attributes and methods

# simulink_ZeroOrderHold class attributes and methods
simulink_ZeroOrderHold_sampleTime: Property = Property(name="sampleTime", type=StringType)
simulink_ZeroOrderHold.attributes={simulink_ZeroOrderHold_sampleTime}

# simulink_stateflow_StateflowMachine class attributes and methods

# StateflowElement class attributes and methods

# stateflow_simulink_SimulinkFile class attributes and methods

# simulink_stateflow_Chart class attributes and methods

# State class attributes and methods

# Data class attributes and methods

# stateflow_simulink_ChartBlock class attributes and methods

# simulink_stateflow_StateflowElement class attributes and methods

# simulink_stateflow_State class attributes and methods
simulink_stateflow_State_subStateType: Property = Property(name="subStateType", type=StringType)
simulink_stateflow_State_name: Property = Property(name="name", type=StringType)
simulink_stateflow_State_priority: Property = Property(name="priority", type=IntegerType)
simulink_stateflow_State_initial: Property = Property(name="initial", type=BooleanType)
simulink_stateflow_State_m_getSubState: Method = Method(name="getSubState", parameters={Parameter(name='name')}, type=StringType)
simulink_stateflow_State.attributes={simulink_stateflow_State_initial, simulink_stateflow_State_subStateType, simulink_stateflow_State_name, simulink_stateflow_State_priority}
simulink_stateflow_State.methods={simulink_stateflow_State_m_getSubState}

# Node class attributes and methods

# Transition class attributes and methods

# EmbeddedFunction class attributes and methods

# Action class attributes and methods

# simulink_stateflow_Transition class attributes and methods
simulink_stateflow_Transition_priority: Property = Property(name="priority", type=IntegerType)
simulink_stateflow_Transition.attributes={simulink_stateflow_Transition_priority}

# simulink_stateflow_Junction class attributes and methods

# simulink_stateflow_Node class attributes and methods

# Event class attributes and methods

# simulink_stateflow_Event class attributes and methods
simulink_stateflow_Event_name: Property = Property(name="name", type=StringType)
simulink_stateflow_Event.attributes={simulink_stateflow_Event_name}

# simulink_stateflow_History class attributes and methods

# simulink_stateflow_EmbeddedFunction class attributes and methods
simulink_stateflow_EmbeddedFunction_name: Property = Property(name="name", type=StringType)
simulink_stateflow_EmbeddedFunction_code: Property = Property(name="code", type=StringType)
simulink_stateflow_EmbeddedFunction.attributes={simulink_stateflow_EmbeddedFunction_name, simulink_stateflow_EmbeddedFunction_code}

# simulink_stateflow_Action class attributes and methods
simulink_stateflow_Action_expression: Property = Property(name="expression", type=StringType)
simulink_stateflow_Action.attributes={simulink_stateflow_Action_expression}

# simulink_stateflow_Data class attributes and methods
simulink_stateflow_Data_name: Property = Property(name="name", type=StringType)
simulink_stateflow_Data_type: Property = Property(name="type", type=StringType)
simulink_stateflow_Data_value: Property = Property(name="value", type=StringType)
simulink_stateflow_Data_size: Property = Property(name="size", type=StringType)
simulink_stateflow_Data.attributes={simulink_stateflow_Data_type, simulink_stateflow_Data_value, simulink_stateflow_Data_name, simulink_stateflow_Data_size}

# simulink_msglib_CommunicationSwitch class attributes and methods
simulink_msglib_CommunicationSwitch_debug: Property = Property(name="debug", type=IntegerType)
simulink_msglib_CommunicationSwitch.attributes={simulink_msglib_CommunicationSwitch_debug}

# simulink_msglib_LinkLayer class attributes and methods
simulink_msglib_LinkLayer_delayMin: Property = Property(name="delayMin", type=StringType)
simulink_msglib_LinkLayer_messageRetransmission: Property = Property(name="messageRetransmission", type=BooleanType)
simulink_msglib_LinkLayer_bufferOverflowPossible: Property = Property(name="bufferOverflowPossible", type=BooleanType)
simulink_msglib_LinkLayer_bufferSize: Property = Property(name="bufferSize", type=IntegerType)
simulink_msglib_LinkLayer_sourceBufferSize: Property = Property(name="sourceBufferSize", type=IntegerType)
simulink_msglib_LinkLayer_messageMapping: Property = Property(name="messageMapping", type=StringType)
simulink_msglib_LinkLayer_delayMax: Property = Property(name="delayMax", type=StringType)
simulink_msglib_LinkLayer_messageLossProbability: Property = Property(name="messageLossProbability", type=IntegerType)
simulink_msglib_LinkLayer.attributes={simulink_msglib_LinkLayer_bufferOverflowPossible, simulink_msglib_LinkLayer_messageMapping, simulink_msglib_LinkLayer_sourceBufferSize, simulink_msglib_LinkLayer_bufferSize, simulink_msglib_LinkLayer_delayMin, simulink_msglib_LinkLayer_delayMax, simulink_msglib_LinkLayer_messageLossProbability, simulink_msglib_LinkLayer_messageRetransmission}

# simulink_buffer_Enqueue class attributes and methods

# BufferFunction class attributes and methods

# simulink_buffer_Dequeue class attributes and methods

# simulink_buffer_CheckQueue class attributes and methods

# simulink_buffer_SharedEnqueue class attributes and methods

# simulink_buffer_SharedDequeue class attributes and methods

# simulink_buffer_SharedCheckQueue class attributes and methods

# simulink_buffer_BufferFunction class attributes and methods
simulink_buffer_BufferFunction_bufferSize: Property = Property(name="bufferSize", type=IntegerType)
simulink_buffer_BufferFunction.attributes={simulink_buffer_BufferFunction_bufferSize}

# simulink_reconfiguration_MultiTargetControl class attributes and methods

# simulink_reconfiguration_MultiSourceControl class attributes and methods

# simulink_reconfiguration_FadingComponent class attributes and methods
simulink_reconfiguration_FadingComponent_time: Property = Property(name="time", type=IntegerType)
simulink_reconfiguration_FadingComponent.attributes={simulink_reconfiguration_FadingComponent_time}

# Relationships
parent0: BinaryAssociation = BinaryAssociation(
    name="parent0",
    ends={
        Property(name="SubSystem", type=simulink_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="blocks", type=simulink_SubSystem, multiplicity=Multiplicity(0, 1))
    }
)
outPorts1: BinaryAssociation = BinaryAssociation(
    name="outPorts1",
    ends={
        Property(name="OutPortBlock", type=simulink_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="block", type=simulink_OutPortBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingLines4: BinaryAssociation = BinaryAssociation(
    name="incomingLines4",
    ends={
        Property(name="Line", type=simulink_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="targetBlock", type=simulink_Line, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingLines5: BinaryAssociation = BinaryAssociation(
    name="outgoingLines5",
    ends={
        Property(name="Line6", type=simulink_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceBlock", type=simulink_Line, multiplicity=Multiplicity(0, 9999))
    }
)
root7: BinaryAssociation = BinaryAssociation(
    name="root7",
    ends={
        Property(name="SimulinkContainer", type=simulink_SimulinkModel, multiplicity=Multiplicity(1, 1)),
        Property(name="models", type=simulink_SimulinkContainer, multiplicity=Multiplicity(0, 1))
    }
)
parameters8: BinaryAssociation = BinaryAssociation(
    name="parameters8",
    ends={
        Property(name="simulink_Parameter", type=simulink_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_Element", type=simulink_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourcePort9: BinaryAssociation = BinaryAssociation(
    name="sourcePort9",
    ends={
        Property(name="simulink_OutPortBlock", type=simulink_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_Line", type=simulink_OutPortBlock, multiplicity=Multiplicity(1, 1))
    }
)
targetPort10: BinaryAssociation = BinaryAssociation(
    name="targetPort10",
    ends={
        Property(name="simulink_InPortBlock", type=simulink_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_Line11", type=simulink_InPortBlock, multiplicity=Multiplicity(1, 1))
    }
)
sourceBlock12: BinaryAssociation = BinaryAssociation(
    name="sourceBlock12",
    ends={
        Property(name="Block", type=simulink_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingLines", type=simulink_Block, multiplicity=Multiplicity(1, 1))
    }
)
targetBlock13: BinaryAssociation = BinaryAssociation(
    name="targetBlock13",
    ends={
        Property(name="Block14", type=simulink_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingLines", type=simulink_Block, multiplicity=Multiplicity(1, 1))
    }
)
bus15: BinaryAssociation = BinaryAssociation(
    name="bus15",
    ends={
        Property(name="simulink_Bus", type=simulink_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_Line16", type=simulink_Bus, multiplicity=Multiplicity(0, 1))
    }
)
inPorts2: BinaryAssociation = BinaryAssociation(
    name="inPorts2",
    ends={
        Property(name="InPortBlock", type=simulink_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="block3", type=simulink_InPortBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blocks19: BinaryAssociation = BinaryAssociation(
    name="blocks19",
    ends={
        Property(name="Block20", type=simulink_SubSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=simulink_Block, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subSystems22: BinaryAssociation = BinaryAssociation(
    name="subSystems22",
    ends={
        Property(name="simulink_SubSystem23", type=simulink_SubSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_SubSystem21", type=simulink_SubSystem, multiplicity=Multiplicity(0, 9999))
    }
)
allBlocks24: BinaryAssociation = BinaryAssociation(
    name="allBlocks24",
    ends={
        Property(name="simulink_Block", type=simulink_SubSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_SubSystem25", type=simulink_Block, multiplicity=Multiplicity(0, 9999))
    }
)
block26: BinaryAssociation = BinaryAssociation(
    name="block26",
    ends={
        Property(name="Block27", type=simulink_InPortBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="inPorts", type=simulink_Block, multiplicity=Multiplicity(1, 1))
    }
)
models28: BinaryAssociation = BinaryAssociation(
    name="models28",
    ends={
        Property(name="SimulinkModel", type=simulink_SimulinkContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="root", type=simulink_SimulinkModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
libraries29: BinaryAssociation = BinaryAssociation(
    name="libraries29",
    ends={
        Property(name="simulink_SimulinkLibrary", type=simulink_SimulinkContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_SimulinkContainer", type=simulink_SimulinkLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lines17: BinaryAssociation = BinaryAssociation(
    name="lines17",
    ends={
        Property(name="simulink_Line18", type=simulink_SubSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_SubSystem", type=simulink_Line, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateflowMachine32: BinaryAssociation = BinaryAssociation(
    name="stateflowMachine32",
    ends={
        Property(name="stateflow", type=simulink_SimulinkFile, multiplicity=Multiplicity(1, 1)),
        Property(name="StateflowMachine", type=StateflowMachine, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
buses33: BinaryAssociation = BinaryAssociation(
    name="buses33",
    ends={
        Property(name="simulink_Bus34", type=simulink_SimulinkFile, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_SimulinkFile", type=simulink_Bus, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block35: BinaryAssociation = BinaryAssociation(
    name="block35",
    ends={
        Property(name="Block36", type=simulink_OutPortBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="outPorts", type=simulink_Block, multiplicity=Multiplicity(1, 1))
    }
)
chart37: BinaryAssociation = BinaryAssociation(
    name="chart37",
    ends={
        Property(name="stateflow38", type=simulink_ChartBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="Chart", type=Chart, multiplicity=Multiplicity(1, 1))
    }
)
elements39: BinaryAssociation = BinaryAssociation(
    name="elements39",
    ends={
        Property(name="simulink_BusElement", type=simulink_Bus, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_Bus40", type=simulink_BusElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bus41: BinaryAssociation = BinaryAssociation(
    name="bus41",
    ends={
        Property(name="simulink_Bus42", type=simulink_BusCreator, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_BusCreator", type=simulink_Bus, multiplicity=Multiplicity(0, 1))
    }
)
bus43: BinaryAssociation = BinaryAssociation(
    name="bus43",
    ends={
        Property(name="simulink_Bus44", type=simulink_BusSelector, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_BusSelector", type=simulink_Bus, multiplicity=Multiplicity(0, 1))
    }
)
sourceBlock30: BinaryAssociation = BinaryAssociation(
    name="sourceBlock30",
    ends={
        Property(name="simulink_Block31", type=simulink_LibraryReference, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_LibraryReference", type=simulink_Block, multiplicity=Multiplicity(1, 1))
    }
)
charts48: BinaryAssociation = BinaryAssociation(
    name="charts48",
    ends={
        Property(name="stateflow50", type=simulink_stateflow_StateflowMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="Chart49", type=Chart, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
model51: BinaryAssociation = BinaryAssociation(
    name="model51",
    ends={
        Property(name="SimulinkFile", type=simulink_stateflow_StateflowMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateflowMachine", type=stateflow_simulink_SimulinkFile, multiplicity=Multiplicity(1, 1))
    }
)
machine52: BinaryAssociation = BinaryAssociation(
    name="machine52",
    ends={
        Property(name="stateflow54", type=simulink_stateflow_Chart, multiplicity=Multiplicity(1, 1)),
        Property(name="StateflowMachine53", type=StateflowMachine, multiplicity=Multiplicity(1, 1))
    }
)
output55: BinaryAssociation = BinaryAssociation(
    name="output55",
    ends={
        Property(name="Data", type=simulink_stateflow_Chart, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_Chart", type=Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input56: BinaryAssociation = BinaryAssociation(
    name="input56",
    ends={
        Property(name="Data58", type=simulink_stateflow_Chart, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_Chart57", type=Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block59: BinaryAssociation = BinaryAssociation(
    name="block59",
    ends={
        Property(name="ChartBlock", type=simulink_stateflow_Chart, multiplicity=Multiplicity(1, 1)),
        Property(name="chart", type=stateflow_simulink_ChartBlock, multiplicity=Multiplicity(0, 1))
    }
)
nodes60: BinaryAssociation = BinaryAssociation(
    name="nodes60",
    ends={
        Property(name="stateflow61", type=simulink_stateflow_State, multiplicity=Multiplicity(1, 1)),
        Property(name="Node", type=Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions62: BinaryAssociation = BinaryAssociation(
    name="transitions62",
    ends={
        Property(name="Transition", type=simulink_stateflow_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_State", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bus45: BinaryAssociation = BinaryAssociation(
    name="bus45",
    ends={
        Property(name="simulink_Bus47", type=simulink_BusElement, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_BusElement46", type=simulink_Bus, multiplicity=Multiplicity(0, 1))
    }
)
embeddedFunctions65: BinaryAssociation = BinaryAssociation(
    name="embeddedFunctions65",
    ends={
        Property(name="EmbeddedFunction", type=simulink_stateflow_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_State66", type=EmbeddedFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entryAction67: BinaryAssociation = BinaryAssociation(
    name="entryAction67",
    ends={
        Property(name="Action", type=simulink_stateflow_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_State68", type=Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exitAction69: BinaryAssociation = BinaryAssociation(
    name="exitAction69",
    ends={
        Property(name="Action71", type=simulink_stateflow_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_State70", type=Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
duringAction72: BinaryAssociation = BinaryAssociation(
    name="duringAction72",
    ends={
        Property(name="Action74", type=simulink_stateflow_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_State73", type=Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
local75: BinaryAssociation = BinaryAssociation(
    name="local75",
    ends={
        Property(name="Data77", type=simulink_stateflow_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_State76", type=Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constant78: BinaryAssociation = BinaryAssociation(
    name="constant78",
    ends={
        Property(name="Data80", type=simulink_stateflow_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_State79", type=Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial_guard81: BinaryAssociation = BinaryAssociation(
    name="initial_guard81",
    ends={
        Property(name="Action83", type=simulink_stateflow_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_State82", type=Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source84: BinaryAssociation = BinaryAssociation(
    name="source84",
    ends={
        Property(name="stateflow86", type=simulink_stateflow_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="Node85", type=Node, multiplicity=Multiplicity(0, 1))
    }
)
target87: BinaryAssociation = BinaryAssociation(
    name="target87",
    ends={
        Property(name="stateflow89", type=simulink_stateflow_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="Node88", type=Node, multiplicity=Multiplicity(0, 1))
    }
)
event90: BinaryAssociation = BinaryAssociation(
    name="event90",
    ends={
        Property(name="Event91", type=simulink_stateflow_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_Transition", type=Event, multiplicity=Multiplicity(0, 1))
    }
)
guard92: BinaryAssociation = BinaryAssociation(
    name="guard92",
    ends={
        Property(name="Action94", type=simulink_stateflow_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_Transition93", type=Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action95: BinaryAssociation = BinaryAssociation(
    name="action95",
    ends={
        Property(name="Action97", type=simulink_stateflow_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_Transition96", type=Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent98: BinaryAssociation = BinaryAssociation(
    name="parent98",
    ends={
        Property(name="stateflow99", type=simulink_stateflow_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="State", type=State, multiplicity=Multiplicity(0, 1))
    }
)
incoming100: BinaryAssociation = BinaryAssociation(
    name="incoming100",
    ends={
        Property(name="stateflow102", type=simulink_stateflow_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="Transition101", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
events63: BinaryAssociation = BinaryAssociation(
    name="events63",
    ends={
        Property(name="Event", type=simulink_stateflow_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_State64", type=Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input106: BinaryAssociation = BinaryAssociation(
    name="input106",
    ends={
        Property(name="Data107", type=simulink_stateflow_EmbeddedFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_EmbeddedFunction", type=Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
output108: BinaryAssociation = BinaryAssociation(
    name="output108",
    ends={
        Property(name="Data110", type=simulink_stateflow_EmbeddedFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_EmbeddedFunction109", type=Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
local111: BinaryAssociation = BinaryAssociation(
    name="local111",
    ends={
        Property(name="Data113", type=simulink_stateflow_EmbeddedFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_EmbeddedFunction112", type=Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constant114: BinaryAssociation = BinaryAssociation(
    name="constant114",
    ends={
        Property(name="Data116", type=simulink_stateflow_EmbeddedFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_EmbeddedFunction115", type=Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing103: BinaryAssociation = BinaryAssociation(
    name="outgoing103",
    ends={
        Property(name="stateflow105", type=simulink_stateflow_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="Transition104", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_simulink_Block_Element = Generalization(general=Element, specific=simulink_Block)
gen_simulink_SimulinkModel_SimulinkFile = Generalization(general=SimulinkFile, specific=simulink_SimulinkModel)
gen_simulink_Line_Element = Generalization(general=Element, specific=simulink_Line)
gen_simulink_SubSystem_Block = Generalization(general=Block, specific=simulink_SubSystem)
gen_simulink_InPortBlock_PortBlock = Generalization(general=PortBlock, specific=simulink_InPortBlock)
gen_simulink_EmbeddedMatlabFunction_Block = Generalization(general=Block, specific=simulink_EmbeddedMatlabFunction)
gen_simulink_MiscBlock_Block = Generalization(general=Block, specific=simulink_MiscBlock)
gen_simulink_SimulinkContainer_Element = Generalization(general=Element, specific=simulink_SimulinkContainer)
gen_simulink_SimulinkLibrary_SimulinkFile = Generalization(general=SimulinkFile, specific=simulink_SimulinkLibrary)
gen_simulink_LibraryReference_Block = Generalization(general=Block, specific=simulink_LibraryReference)
gen_simulink_SimulinkFile_SubSystem = Generalization(general=SubSystem, specific=simulink_SimulinkFile)
gen_simulink_OutPortBlock_PortBlock = Generalization(general=PortBlock, specific=simulink_OutPortBlock)
gen_simulink_ChartBlock_Block = Generalization(general=Block, specific=simulink_ChartBlock)
gen_simulink_Bus_Element = Generalization(general=Element, specific=simulink_Bus)
gen_simulink_BusCreator_Block = Generalization(general=Block, specific=simulink_BusCreator)
gen_simulink_BusSelector_Block = Generalization(general=Block, specific=simulink_BusSelector)
gen_simulink_DigitalClock_Block = Generalization(general=Block, specific=simulink_DigitalClock)
gen_simulink_Constant_Block = Generalization(general=Block, specific=simulink_Constant)
gen_simulink_TriggerPort_InPortBlock = Generalization(general=InPortBlock, specific=simulink_TriggerPort)
gen_simulink_EnablePort_InPortBlock = Generalization(general=InPortBlock, specific=simulink_EnablePort)
gen_simulink_PortBlock_Block = Generalization(general=Block, specific=simulink_PortBlock)
gen_simulink_UnitDelay_Block = Generalization(general=Block, specific=simulink_UnitDelay)
gen_simulink_ZeroOrderHold_Block = Generalization(general=Block, specific=simulink_ZeroOrderHold)
gen_simulink_stateflow_StateflowMachine_StateflowElement = Generalization(general=StateflowElement, specific=simulink_stateflow_StateflowMachine)
gen_simulink_stateflow_Chart_State = Generalization(general=State, specific=simulink_stateflow_Chart)
gen_simulink_stateflow_StateflowElement_Element = Generalization(general=Element, specific=simulink_stateflow_StateflowElement)
gen_simulink_stateflow_State_Node = Generalization(general=Node, specific=simulink_stateflow_State)
gen_simulink_stateflow_Transition_StateflowElement = Generalization(general=StateflowElement, specific=simulink_stateflow_Transition)
gen_simulink_stateflow_Junction_Node = Generalization(general=Node, specific=simulink_stateflow_Junction)
gen_simulink_stateflow_Node_StateflowElement = Generalization(general=StateflowElement, specific=simulink_stateflow_Node)
gen_simulink_stateflow_Event_StateflowElement = Generalization(general=StateflowElement, specific=simulink_stateflow_Event)
gen_simulink_stateflow_History_Node = Generalization(general=Node, specific=simulink_stateflow_History)
gen_simulink_stateflow_EmbeddedFunction_StateflowElement = Generalization(general=StateflowElement, specific=simulink_stateflow_EmbeddedFunction)
gen_simulink_stateflow_Action_StateflowElement = Generalization(general=StateflowElement, specific=simulink_stateflow_Action)
gen_simulink_stateflow_Data_StateflowElement = Generalization(general=StateflowElement, specific=simulink_stateflow_Data)
gen_simulink_msglib_CommunicationSwitch_Block = Generalization(general=Block, specific=simulink_msglib_CommunicationSwitch)
gen_simulink_msglib_LinkLayer_Block = Generalization(general=Block, specific=simulink_msglib_LinkLayer)
gen_simulink_buffer_Enqueue_BufferFunction = Generalization(general=BufferFunction, specific=simulink_buffer_Enqueue)
gen_simulink_buffer_Dequeue_BufferFunction = Generalization(general=BufferFunction, specific=simulink_buffer_Dequeue)
gen_simulink_buffer_CheckQueue_BufferFunction = Generalization(general=BufferFunction, specific=simulink_buffer_CheckQueue)
gen_simulink_buffer_SharedEnqueue_BufferFunction = Generalization(general=BufferFunction, specific=simulink_buffer_SharedEnqueue)
gen_simulink_buffer_SharedDequeue_BufferFunction = Generalization(general=BufferFunction, specific=simulink_buffer_SharedDequeue)
gen_simulink_buffer_SharedCheckQueue_BufferFunction = Generalization(general=BufferFunction, specific=simulink_buffer_SharedCheckQueue)
gen_simulink_buffer_BufferFunction_EmbeddedFunction = Generalization(general=EmbeddedFunction, specific=simulink_buffer_BufferFunction)
gen_simulink_reconfiguration_MultiTargetControl_Block = Generalization(general=Block, specific=simulink_reconfiguration_MultiTargetControl)
gen_simulink_reconfiguration_MultiSourceControl_Block = Generalization(general=Block, specific=simulink_reconfiguration_MultiSourceControl)
gen_simulink_reconfiguration_FadingComponent_Block = Generalization(general=Block, specific=simulink_reconfiguration_FadingComponent)

# Domain Model
domain_model = DomainModel(
    name="simulink",
    types={simulink_Block, Element, simulink_SubSystem, simulink_OutPortBlock, simulink_InPortBlock, simulink_SimulinkModel, SimulinkFile, simulink_SimulinkContainer, simulink_Element, simulink_Parameter, simulink_Bus, Block, simulink_Line, PortBlock, simulink_EmbeddedMatlabFunction, simulink_MiscBlock, simulink_SimulinkLibrary, simulink_LibraryReference, simulink_SimulinkFile, SubSystem, StateflowMachine, simulink_ChartBlock, Chart, simulink_BusElement, simulink_BusCreator, simulink_BusSelector, simulink_DigitalClock, simulink_Constant, simulink_TriggerPort, InPortBlock, simulink_EnablePort, simulink_PortBlock, simulink_UnitDelay, simulink_ZeroOrderHold, simulink_stateflow_StateflowMachine, StateflowElement, stateflow_simulink_SimulinkFile, simulink_stateflow_Chart, State, Data, stateflow_simulink_ChartBlock, simulink_stateflow_StateflowElement, simulink_stateflow_State, Node, Transition, EmbeddedFunction, Action, simulink_stateflow_Transition, simulink_stateflow_Junction, simulink_stateflow_Node, Event, simulink_stateflow_Event, simulink_stateflow_History, simulink_stateflow_EmbeddedFunction, simulink_stateflow_Action, simulink_stateflow_Data, simulink_msglib_CommunicationSwitch, simulink_msglib_LinkLayer, simulink_buffer_Enqueue, BufferFunction, simulink_buffer_Dequeue, simulink_buffer_CheckQueue, simulink_buffer_SharedEnqueue, simulink_buffer_SharedDequeue, simulink_buffer_SharedCheckQueue, simulink_buffer_BufferFunction, simulink_reconfiguration_MultiTargetControl, simulink_reconfiguration_MultiSourceControl, simulink_reconfiguration_FadingComponent, DataType, TriggerEvent, SubStateType},
    associations={parent0, outPorts1, incomingLines4, outgoingLines5, root7, parameters8, sourcePort9, targetPort10, sourceBlock12, targetBlock13, bus15, inPorts2, blocks19, subSystems22, allBlocks24, block26, models28, libraries29, lines17, stateflowMachine32, buses33, block35, chart37, elements39, bus41, bus43, sourceBlock30, charts48, model51, machine52, output55, input56, block59, nodes60, transitions62, bus45, embeddedFunctions65, entryAction67, exitAction69, duringAction72, local75, constant78, initial_guard81, source84, target87, event90, guard92, action95, parent98, incoming100, events63, input106, output108, local111, constant114, outgoing103},
    generalizations={gen_simulink_Block_Element, gen_simulink_SimulinkModel_SimulinkFile, gen_simulink_Line_Element, gen_simulink_SubSystem_Block, gen_simulink_InPortBlock_PortBlock, gen_simulink_EmbeddedMatlabFunction_Block, gen_simulink_MiscBlock_Block, gen_simulink_SimulinkContainer_Element, gen_simulink_SimulinkLibrary_SimulinkFile, gen_simulink_LibraryReference_Block, gen_simulink_SimulinkFile_SubSystem, gen_simulink_OutPortBlock_PortBlock, gen_simulink_ChartBlock_Block, gen_simulink_Bus_Element, gen_simulink_BusCreator_Block, gen_simulink_BusSelector_Block, gen_simulink_DigitalClock_Block, gen_simulink_Constant_Block, gen_simulink_TriggerPort_InPortBlock, gen_simulink_EnablePort_InPortBlock, gen_simulink_PortBlock_Block, gen_simulink_UnitDelay_Block, gen_simulink_ZeroOrderHold_Block, gen_simulink_stateflow_StateflowMachine_StateflowElement, gen_simulink_stateflow_Chart_State, gen_simulink_stateflow_StateflowElement_Element, gen_simulink_stateflow_State_Node, gen_simulink_stateflow_Transition_StateflowElement, gen_simulink_stateflow_Junction_Node, gen_simulink_stateflow_Node_StateflowElement, gen_simulink_stateflow_Event_StateflowElement, gen_simulink_stateflow_History_Node, gen_simulink_stateflow_EmbeddedFunction_StateflowElement, gen_simulink_stateflow_Action_StateflowElement, gen_simulink_stateflow_Data_StateflowElement, gen_simulink_msglib_CommunicationSwitch_Block, gen_simulink_msglib_LinkLayer_Block, gen_simulink_buffer_Enqueue_BufferFunction, gen_simulink_buffer_Dequeue_BufferFunction, gen_simulink_buffer_CheckQueue_BufferFunction, gen_simulink_buffer_SharedEnqueue_BufferFunction, gen_simulink_buffer_SharedDequeue_BufferFunction, gen_simulink_buffer_SharedCheckQueue_BufferFunction, gen_simulink_buffer_BufferFunction_EmbeddedFunction, gen_simulink_reconfiguration_MultiTargetControl_Block, gen_simulink_reconfiguration_MultiSourceControl_Block, gen_simulink_reconfiguration_FadingComponent_Block},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)