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
simulink_SubSystem = Class(name="simulink_SubSystem")
simulink_Block = Class(name="simulink_Block", is_abstract=True)
Element = Class(name="Element")
simulink_OutPortBlock = Class(name="simulink_OutPortBlock")
simulink_InPortBlock = Class(name="simulink_InPortBlock")
simulink_Line = Class(name="simulink_Line")
simulink_SimulinkModel = Class(name="simulink_SimulinkModel")
SimulinkFile = Class(name="SimulinkFile")
simulink_SimulinkContainer = Class(name="simulink_SimulinkContainer")
simulink_Element = Class(name="simulink_Element", is_abstract=True)
simulink_Parameter = Class(name="simulink_Parameter")
simulink_Bus = Class(name="simulink_Bus")
Block = Class(name="Block")
simulink_SimulinkFile = Class(name="simulink_SimulinkFile", is_abstract=True)
SubSystem = Class(name="SubSystem")
StateflowMachine = Class(name="StateflowMachine")
PortBlock = Class(name="PortBlock")
simulink_EmbeddedMatlabFunction = Class(name="simulink_EmbeddedMatlabFunction")
simulink_MiscBlock = Class(name="simulink_MiscBlock")
simulink_SimulinkLibrary = Class(name="simulink_SimulinkLibrary")
simulink_LibraryReference = Class(name="simulink_LibraryReference")
simulink_ChartBlock = Class(name="simulink_ChartBlock")
Chart = Class(name="Chart")
simulink_BusElement = Class(name="simulink_BusElement")
simulink_BusCreator = Class(name="simulink_BusCreator")
simulink_BusSelector = Class(name="simulink_BusSelector")
simulink_PortBlock = Class(name="simulink_PortBlock")
simulink_UnitDelay = Class(name="simulink_UnitDelay")
simulink_DigitalClock = Class(name="simulink_DigitalClock")
stateflow_simulink_ChartBlock = Class(name="stateflow_simulink_ChartBlock")
simulink_Constant = Class(name="simulink_Constant")
simulink_TriggerPort = Class(name="simulink_TriggerPort")
InPortBlock = Class(name="InPortBlock")
simulink_EnablePort = Class(name="simulink_EnablePort")
simulink_ZeroOrderHold = Class(name="simulink_ZeroOrderHold")
simulink_stateflow_StateflowMachine = Class(name="simulink_stateflow_StateflowMachine")
StateflowElement = Class(name="StateflowElement")
stateflow_simulink_SimulinkFile = Class(name="stateflow_simulink_SimulinkFile")
simulink_stateflow_Chart = Class(name="simulink_stateflow_Chart")
State = Class(name="State")
Data = Class(name="Data")
simulink_stateflow_StateflowElement = Class(name="simulink_stateflow_StateflowElement")
simulink_stateflow_State = Class(name="simulink_stateflow_State")
Node = Class(name="Node")
Transition = Class(name="Transition")
Event = Class(name="Event")
EmbeddedFunction = Class(name="EmbeddedFunction")
Action = Class(name="Action")
simulink_stateflow_Transition = Class(name="simulink_stateflow_Transition")
simulink_stateflow_Junction = Class(name="simulink_stateflow_Junction")
simulink_stateflow_Node = Class(name="simulink_stateflow_Node", is_abstract=True)
simulink_stateflow_Event = Class(name="simulink_stateflow_Event")
simulink_stateflow_History = Class(name="simulink_stateflow_History")
simulink_stateflow_EmbeddedFunction = Class(name="simulink_stateflow_EmbeddedFunction")
simulink_stateflow_Action = Class(name="simulink_stateflow_Action")
simulink_stateflow_Data = Class(name="simulink_stateflow_Data")
simulink_msglib_CommunicationSwitch = Class(name="simulink_msglib_CommunicationSwitch")
simulink_msglib_LinkLayer = Class(name="simulink_msglib_LinkLayer")
simulink_buffer_Enqueue = Class(name="simulink_buffer_Enqueue")
BufferFunction = Class(name="BufferFunction")
simulink_buffer_Dequeue = Class(name="simulink_buffer_Dequeue")
simulink_buffer_CheckQueue = Class(name="simulink_buffer_CheckQueue")
simulink_buffer_SharedEnqueue = Class(name="simulink_buffer_SharedEnqueue")
simulink_buffer_SharedDequeue = Class(name="simulink_buffer_SharedDequeue")
simulink_buffer_SharedCheckQueue = Class(name="simulink_buffer_SharedCheckQueue")
simulink_buffer_BufferFunction = Class(name="simulink_buffer_BufferFunction")
simulink_reconfiguration_MultiSourceControl = Class(name="simulink_reconfiguration_MultiSourceControl")
simulink_reconfiguration_FadingComponent = Class(name="simulink_reconfiguration_FadingComponent")
simulink_reconfiguration_MultiTargetControl = Class(name="simulink_reconfiguration_MultiTargetControl")

# simulink_SubSystem class attributes and methods
simulink_SubSystem_m_getBlockByName: Method = Method(name="getBlockByName", parameters={Parameter(name='simulink_name', type=StringType)}, type=Block)
simulink_SubSystem.methods={simulink_SubSystem_m_getBlockByName}

# simulink_Block class attributes and methods
simulink_Block_name: Property = Property(name="name", type=StringType)
simulink_Block_m_getFullyQualifiedName: Method = Method(name="getFullyQualifiedName", parameters={}, type=StringType)
simulink_Block.attributes={simulink_Block_name}
simulink_Block.methods={simulink_Block_m_getFullyQualifiedName}

# Element class attributes and methods

# simulink_OutPortBlock class attributes and methods

# simulink_InPortBlock class attributes and methods

# simulink_Line class attributes and methods

# simulink_SimulinkModel class attributes and methods

# SimulinkFile class attributes and methods

# simulink_SimulinkContainer class attributes and methods

# simulink_Element class attributes and methods
simulink_Element_id: Property = Property(name="id", type=StringType)
simulink_Element_m_getParameter: Method = Method(name="getParameter", parameters={Parameter(name='simulink_name', type=StringType)}, type=StringType)
simulink_Element.attributes={simulink_Element_id}
simulink_Element.methods={simulink_Element_m_getParameter}

# simulink_Parameter class attributes and methods
simulink_Parameter_name: Property = Property(name="name", type=StringType)
simulink_Parameter_value: Property = Property(name="value", type=StringType)
simulink_Parameter_type: Property = Property(name="type", type=StringType)
simulink_Parameter.attributes={simulink_Parameter_value, simulink_Parameter_type, simulink_Parameter_name}

# simulink_Bus class attributes and methods
simulink_Bus_name: Property = Property(name="name", type=StringType)
simulink_Bus.attributes={simulink_Bus_name}

# Block class attributes and methods

# simulink_SimulinkFile class attributes and methods

# SubSystem class attributes and methods

# StateflowMachine class attributes and methods

# PortBlock class attributes and methods

# simulink_EmbeddedMatlabFunction class attributes and methods
simulink_EmbeddedMatlabFunction_code: Property = Property(name="code", type=StringType)
simulink_EmbeddedMatlabFunction.attributes={simulink_EmbeddedMatlabFunction_code}

# simulink_MiscBlock class attributes and methods
simulink_MiscBlock_type: Property = Property(name="type", type=StringType)
simulink_MiscBlock.attributes={simulink_MiscBlock_type}

# simulink_SimulinkLibrary class attributes and methods

# simulink_LibraryReference class attributes and methods

# simulink_ChartBlock class attributes and methods

# Chart class attributes and methods

# simulink_BusElement class attributes and methods
simulink_BusElement_name: Property = Property(name="name", type=StringType)
simulink_BusElement_dimensions: Property = Property(name="dimensions", type=StringType)
simulink_BusElement_type: Property = Property(name="type", type=StringType)
simulink_BusElement.attributes={simulink_BusElement_name, simulink_BusElement_dimensions, simulink_BusElement_type}

# simulink_BusCreator class attributes and methods

# simulink_BusSelector class attributes and methods

# simulink_PortBlock class attributes and methods
simulink_PortBlock_dimensions: Property = Property(name="dimensions", type=StringType)
simulink_PortBlock_type: Property = Property(name="type", type=StringType)
simulink_PortBlock_initialCondition: Property = Property(name="initialCondition", type=StringType)
simulink_PortBlock.attributes={simulink_PortBlock_initialCondition, simulink_PortBlock_type, simulink_PortBlock_dimensions}

# simulink_UnitDelay class attributes and methods

# simulink_DigitalClock class attributes and methods
simulink_DigitalClock_sampleTime: Property = Property(name="sampleTime", type=FloatType)
simulink_DigitalClock.attributes={simulink_DigitalClock_sampleTime}

# stateflow_simulink_ChartBlock class attributes and methods

# simulink_Constant class attributes and methods
simulink_Constant_value: Property = Property(name="value", type=StringType)
simulink_Constant_type: Property = Property(name="type", type=StringType)
simulink_Constant.attributes={simulink_Constant_type, simulink_Constant_value}

# simulink_TriggerPort class attributes and methods
simulink_TriggerPort_triggerInput: Property = Property(name="triggerInput", type=StringType)
simulink_TriggerPort.attributes={simulink_TriggerPort_triggerInput}

# InPortBlock class attributes and methods

# simulink_EnablePort class attributes and methods

# simulink_ZeroOrderHold class attributes and methods
simulink_ZeroOrderHold_sampleTime: Property = Property(name="sampleTime", type=StringType)
simulink_ZeroOrderHold.attributes={simulink_ZeroOrderHold_sampleTime}

# simulink_stateflow_StateflowMachine class attributes and methods

# StateflowElement class attributes and methods

# stateflow_simulink_SimulinkFile class attributes and methods

# simulink_stateflow_Chart class attributes and methods

# State class attributes and methods

# Data class attributes and methods

# simulink_stateflow_StateflowElement class attributes and methods

# simulink_stateflow_State class attributes and methods
simulink_stateflow_State_subStateType: Property = Property(name="subStateType", type=StringType)
simulink_stateflow_State_name: Property = Property(name="name", type=StringType)
simulink_stateflow_State_priority: Property = Property(name="priority", type=IntegerType)
simulink_stateflow_State_initial: Property = Property(name="initial", type=BooleanType)
simulink_stateflow_State_m_getSubState: Method = Method(name="getSubState", parameters={Parameter(name='simulink_name', type=StringType)}, type=StringType)
simulink_stateflow_State.attributes={simulink_stateflow_State_name, simulink_stateflow_State_initial, simulink_stateflow_State_subStateType, simulink_stateflow_State_priority}
simulink_stateflow_State.methods={simulink_stateflow_State_m_getSubState}

# Node class attributes and methods

# Transition class attributes and methods

# Event class attributes and methods

# EmbeddedFunction class attributes and methods

# Action class attributes and methods

# simulink_stateflow_Transition class attributes and methods
simulink_stateflow_Transition_priority: Property = Property(name="priority", type=IntegerType)
simulink_stateflow_Transition.attributes={simulink_stateflow_Transition_priority}

# simulink_stateflow_Junction class attributes and methods

# simulink_stateflow_Node class attributes and methods

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
simulink_stateflow_Data.attributes={simulink_stateflow_Data_size, simulink_stateflow_Data_type, simulink_stateflow_Data_name, simulink_stateflow_Data_value}

# simulink_msglib_CommunicationSwitch class attributes and methods
simulink_msglib_CommunicationSwitch_debug: Property = Property(name="debug", type=IntegerType)
simulink_msglib_CommunicationSwitch.attributes={simulink_msglib_CommunicationSwitch_debug}

# simulink_msglib_LinkLayer class attributes and methods
simulink_msglib_LinkLayer_delayMin: Property = Property(name="delayMin", type=StringType)
simulink_msglib_LinkLayer_delayMax: Property = Property(name="delayMax", type=StringType)
simulink_msglib_LinkLayer_messageLossProbability: Property = Property(name="messageLossProbability", type=IntegerType)
simulink_msglib_LinkLayer_messageRetransmission: Property = Property(name="messageRetransmission", type=BooleanType)
simulink_msglib_LinkLayer_bufferOverflowPossible: Property = Property(name="bufferOverflowPossible", type=BooleanType)
simulink_msglib_LinkLayer_bufferSize: Property = Property(name="bufferSize", type=IntegerType)
simulink_msglib_LinkLayer_sourceBufferSize: Property = Property(name="sourceBufferSize", type=IntegerType)
simulink_msglib_LinkLayer_messageMapping: Property = Property(name="messageMapping", type=StringType)
simulink_msglib_LinkLayer.attributes={simulink_msglib_LinkLayer_delayMin, simulink_msglib_LinkLayer_messageLossProbability, simulink_msglib_LinkLayer_messageMapping, simulink_msglib_LinkLayer_messageRetransmission, simulink_msglib_LinkLayer_sourceBufferSize, simulink_msglib_LinkLayer_bufferSize, simulink_msglib_LinkLayer_delayMax, simulink_msglib_LinkLayer_bufferOverflowPossible}

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

# simulink_reconfiguration_MultiSourceControl class attributes and methods

# simulink_reconfiguration_FadingComponent class attributes and methods
simulink_reconfiguration_FadingComponent_time: Property = Property(name="time", type=IntegerType)
simulink_reconfiguration_FadingComponent.attributes={simulink_reconfiguration_FadingComponent_time}

# simulink_reconfiguration_MultiTargetControl class attributes and methods

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
inPorts2: BinaryAssociation = BinaryAssociation(
    name="inPorts2",
    ends={
        Property(name="InPortBlock", type=simulink_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="block3", type=simulink_InPortBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
lines17: BinaryAssociation = BinaryAssociation(
    name="lines17",
    ends={
        Property(name="simulink_Line18", type=simulink_SubSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_SubSystem", type=simulink_Line, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
sourceBlock30: BinaryAssociation = BinaryAssociation(
    name="sourceBlock30",
    ends={
        Property(name="simulink_Block31", type=simulink_LibraryReference, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_LibraryReference", type=simulink_Block, multiplicity=Multiplicity(1, 1))
    }
)
stateflowMachine32: BinaryAssociation = BinaryAssociation(
    name="stateflowMachine32",
    ends={
        Property(name="StateflowMachine", type=simulink_SimulinkFile, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=StateflowMachine, multiplicity=Multiplicity(0, 1), is_composite=True)
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
        Property(name="Chart", type=simulink_ChartBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="block38", type=Chart, multiplicity=Multiplicity(1, 1))
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
input54: BinaryAssociation = BinaryAssociation(
    name="input54",
    ends={
        Property(name="Data56", type=simulink_stateflow_Chart, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_Chart55", type=Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bus45: BinaryAssociation = BinaryAssociation(
    name="bus45",
    ends={
        Property(name="simulink_Bus47", type=simulink_BusElement, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_BusElement46", type=simulink_Bus, multiplicity=Multiplicity(0, 1))
    }
)
charts48: BinaryAssociation = BinaryAssociation(
    name="charts48",
    ends={
        Property(name="Chart49", type=simulink_stateflow_StateflowMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="machine", type=Chart, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
model50: BinaryAssociation = BinaryAssociation(
    name="model50",
    ends={
        Property(name="SimulinkFile", type=simulink_stateflow_StateflowMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateflowMachine", type=stateflow_simulink_SimulinkFile, multiplicity=Multiplicity(1, 1))
    }
)
machine51: BinaryAssociation = BinaryAssociation(
    name="machine51",
    ends={
        Property(name="StateflowMachine52", type=simulink_stateflow_Chart, multiplicity=Multiplicity(1, 1)),
        Property(name="charts", type=StateflowMachine, multiplicity=Multiplicity(1, 1))
    }
)
output53: BinaryAssociation = BinaryAssociation(
    name="output53",
    ends={
        Property(name="Data", type=simulink_stateflow_Chart, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_Chart", type=Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard88: BinaryAssociation = BinaryAssociation(
    name="guard88",
    ends={
        Property(name="Action90", type=simulink_stateflow_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_Transition89", type=Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action91: BinaryAssociation = BinaryAssociation(
    name="action91",
    ends={
        Property(name="Action93", type=simulink_stateflow_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_Transition92", type=Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block57: BinaryAssociation = BinaryAssociation(
    name="block57",
    ends={
        Property(name="ChartBlock", type=simulink_stateflow_Chart, multiplicity=Multiplicity(1, 1)),
        Property(name="chart", type=stateflow_simulink_ChartBlock, multiplicity=Multiplicity(0, 1))
    }
)
nodes58: BinaryAssociation = BinaryAssociation(
    name="nodes58",
    ends={
        Property(name="Node", type=simulink_stateflow_State, multiplicity=Multiplicity(1, 1)),
        Property(name="parent59", type=Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions60: BinaryAssociation = BinaryAssociation(
    name="transitions60",
    ends={
        Property(name="Transition", type=simulink_stateflow_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_State", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events61: BinaryAssociation = BinaryAssociation(
    name="events61",
    ends={
        Property(name="Event", type=simulink_stateflow_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_State62", type=Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
embeddedFunctions63: BinaryAssociation = BinaryAssociation(
    name="embeddedFunctions63",
    ends={
        Property(name="EmbeddedFunction", type=simulink_stateflow_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_State64", type=EmbeddedFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entryAction65: BinaryAssociation = BinaryAssociation(
    name="entryAction65",
    ends={
        Property(name="Action", type=simulink_stateflow_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_State66", type=Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exitAction67: BinaryAssociation = BinaryAssociation(
    name="exitAction67",
    ends={
        Property(name="Action69", type=simulink_stateflow_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_State68", type=Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
duringAction70: BinaryAssociation = BinaryAssociation(
    name="duringAction70",
    ends={
        Property(name="Action72", type=simulink_stateflow_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_State71", type=Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
local73: BinaryAssociation = BinaryAssociation(
    name="local73",
    ends={
        Property(name="Data75", type=simulink_stateflow_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_State74", type=Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constant76: BinaryAssociation = BinaryAssociation(
    name="constant76",
    ends={
        Property(name="Data78", type=simulink_stateflow_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_State77", type=Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial_guard79: BinaryAssociation = BinaryAssociation(
    name="initial_guard79",
    ends={
        Property(name="Action81", type=simulink_stateflow_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_State80", type=Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source82: BinaryAssociation = BinaryAssociation(
    name="source82",
    ends={
        Property(name="Node83", type=simulink_stateflow_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=Node, multiplicity=Multiplicity(0, 1))
    }
)
target84: BinaryAssociation = BinaryAssociation(
    name="target84",
    ends={
        Property(name="Node85", type=simulink_stateflow_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=Node, multiplicity=Multiplicity(0, 1))
    }
)
event86: BinaryAssociation = BinaryAssociation(
    name="event86",
    ends={
        Property(name="Event87", type=simulink_stateflow_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_Transition", type=Event, multiplicity=Multiplicity(0, 1))
    }
)
parent94: BinaryAssociation = BinaryAssociation(
    name="parent94",
    ends={
        Property(name="State", type=simulink_stateflow_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=State, multiplicity=Multiplicity(0, 1))
    }
)
incoming95: BinaryAssociation = BinaryAssociation(
    name="incoming95",
    ends={
        Property(name="Transition96", type=simulink_stateflow_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing97: BinaryAssociation = BinaryAssociation(
    name="outgoing97",
    ends={
        Property(name="Transition98", type=simulink_stateflow_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
input99: BinaryAssociation = BinaryAssociation(
    name="input99",
    ends={
        Property(name="Data100", type=simulink_stateflow_EmbeddedFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_EmbeddedFunction", type=Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
output101: BinaryAssociation = BinaryAssociation(
    name="output101",
    ends={
        Property(name="Data103", type=simulink_stateflow_EmbeddedFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_EmbeddedFunction102", type=Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
local104: BinaryAssociation = BinaryAssociation(
    name="local104",
    ends={
        Property(name="Data106", type=simulink_stateflow_EmbeddedFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_EmbeddedFunction105", type=Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constant107: BinaryAssociation = BinaryAssociation(
    name="constant107",
    ends={
        Property(name="Data109", type=simulink_stateflow_EmbeddedFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_stateflow_EmbeddedFunction108", type=Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_simulink_Block_Element = Generalization(general=Element, specific=simulink_Block)
gen_simulink_SimulinkModel_SimulinkFile = Generalization(general=SimulinkFile, specific=simulink_SimulinkModel)
gen_simulink_Line_Element = Generalization(general=Element, specific=simulink_Line)
gen_simulink_SubSystem_Block = Generalization(general=Block, specific=simulink_SubSystem)
gen_simulink_SimulinkFile_SubSystem = Generalization(general=SubSystem, specific=simulink_SimulinkFile)
gen_simulink_InPortBlock_PortBlock = Generalization(general=PortBlock, specific=simulink_InPortBlock)
gen_simulink_EmbeddedMatlabFunction_Block = Generalization(general=Block, specific=simulink_EmbeddedMatlabFunction)
gen_simulink_MiscBlock_Block = Generalization(general=Block, specific=simulink_MiscBlock)
gen_simulink_SimulinkContainer_Element = Generalization(general=Element, specific=simulink_SimulinkContainer)
gen_simulink_SimulinkLibrary_SimulinkFile = Generalization(general=SimulinkFile, specific=simulink_SimulinkLibrary)
gen_simulink_LibraryReference_Block = Generalization(general=Block, specific=simulink_LibraryReference)
gen_simulink_OutPortBlock_PortBlock = Generalization(general=PortBlock, specific=simulink_OutPortBlock)
gen_simulink_ChartBlock_Block = Generalization(general=Block, specific=simulink_ChartBlock)
gen_simulink_Bus_Element = Generalization(general=Element, specific=simulink_Bus)
gen_simulink_BusCreator_Block = Generalization(general=Block, specific=simulink_BusCreator)
gen_simulink_BusSelector_Block = Generalization(general=Block, specific=simulink_BusSelector)
gen_simulink_PortBlock_Block = Generalization(general=Block, specific=simulink_PortBlock)
gen_simulink_UnitDelay_Block = Generalization(general=Block, specific=simulink_UnitDelay)
gen_simulink_DigitalClock_Block = Generalization(general=Block, specific=simulink_DigitalClock)
gen_simulink_Constant_Block = Generalization(general=Block, specific=simulink_Constant)
gen_simulink_TriggerPort_InPortBlock = Generalization(general=InPortBlock, specific=simulink_TriggerPort)
gen_simulink_EnablePort_InPortBlock = Generalization(general=InPortBlock, specific=simulink_EnablePort)
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
gen_simulink_reconfiguration_MultiSourceControl_Block = Generalization(general=Block, specific=simulink_reconfiguration_MultiSourceControl)
gen_simulink_reconfiguration_FadingComponent_Block = Generalization(general=Block, specific=simulink_reconfiguration_FadingComponent)
gen_simulink_reconfiguration_MultiTargetControl_Block = Generalization(general=Block, specific=simulink_reconfiguration_MultiTargetControl)

# Domain Model
domain_model = DomainModel(
    name="simulink",
    types={simulink_SubSystem, simulink_Block, Element, simulink_OutPortBlock, simulink_InPortBlock, simulink_Line, simulink_SimulinkModel, SimulinkFile, simulink_SimulinkContainer, simulink_Element, simulink_Parameter, simulink_Bus, Block, simulink_SimulinkFile, SubSystem, StateflowMachine, PortBlock, simulink_EmbeddedMatlabFunction, simulink_MiscBlock, simulink_SimulinkLibrary, simulink_LibraryReference, simulink_ChartBlock, Chart, simulink_BusElement, simulink_BusCreator, simulink_BusSelector, simulink_PortBlock, simulink_UnitDelay, simulink_DigitalClock, stateflow_simulink_ChartBlock, simulink_Constant, simulink_TriggerPort, InPortBlock, simulink_EnablePort, simulink_ZeroOrderHold, simulink_stateflow_StateflowMachine, StateflowElement, stateflow_simulink_SimulinkFile, simulink_stateflow_Chart, State, Data, simulink_stateflow_StateflowElement, simulink_stateflow_State, Node, Transition, Event, EmbeddedFunction, Action, simulink_stateflow_Transition, simulink_stateflow_Junction, simulink_stateflow_Node, simulink_stateflow_Event, simulink_stateflow_History, simulink_stateflow_EmbeddedFunction, simulink_stateflow_Action, simulink_stateflow_Data, simulink_msglib_CommunicationSwitch, simulink_msglib_LinkLayer, simulink_buffer_Enqueue, BufferFunction, simulink_buffer_Dequeue, simulink_buffer_CheckQueue, simulink_buffer_SharedEnqueue, simulink_buffer_SharedDequeue, simulink_buffer_SharedCheckQueue, simulink_buffer_BufferFunction, simulink_reconfiguration_MultiSourceControl, simulink_reconfiguration_FadingComponent, simulink_reconfiguration_MultiTargetControl, DataType, TriggerEvent, SubStateType},
    associations={parent0, outPorts1, inPorts2, incomingLines4, outgoingLines5, root7, parameters8, sourcePort9, targetPort10, sourceBlock12, targetBlock13, bus15, lines17, blocks19, subSystems22, allBlocks24, block26, models28, libraries29, sourceBlock30, stateflowMachine32, buses33, block35, chart37, elements39, bus41, bus43, input54, bus45, charts48, model50, machine51, output53, guard88, action91, block57, nodes58, transitions60, events61, embeddedFunctions63, entryAction65, exitAction67, duringAction70, local73, constant76, initial_guard79, source82, target84, event86, parent94, incoming95, outgoing97, input99, output101, local104, constant107},
    generalizations={gen_simulink_Block_Element, gen_simulink_SimulinkModel_SimulinkFile, gen_simulink_Line_Element, gen_simulink_SubSystem_Block, gen_simulink_SimulinkFile_SubSystem, gen_simulink_InPortBlock_PortBlock, gen_simulink_EmbeddedMatlabFunction_Block, gen_simulink_MiscBlock_Block, gen_simulink_SimulinkContainer_Element, gen_simulink_SimulinkLibrary_SimulinkFile, gen_simulink_LibraryReference_Block, gen_simulink_OutPortBlock_PortBlock, gen_simulink_ChartBlock_Block, gen_simulink_Bus_Element, gen_simulink_BusCreator_Block, gen_simulink_BusSelector_Block, gen_simulink_PortBlock_Block, gen_simulink_UnitDelay_Block, gen_simulink_DigitalClock_Block, gen_simulink_Constant_Block, gen_simulink_TriggerPort_InPortBlock, gen_simulink_EnablePort_InPortBlock, gen_simulink_ZeroOrderHold_Block, gen_simulink_stateflow_StateflowMachine_StateflowElement, gen_simulink_stateflow_Chart_State, gen_simulink_stateflow_StateflowElement_Element, gen_simulink_stateflow_State_Node, gen_simulink_stateflow_Transition_StateflowElement, gen_simulink_stateflow_Junction_Node, gen_simulink_stateflow_Node_StateflowElement, gen_simulink_stateflow_Event_StateflowElement, gen_simulink_stateflow_History_Node, gen_simulink_stateflow_EmbeddedFunction_StateflowElement, gen_simulink_stateflow_Action_StateflowElement, gen_simulink_stateflow_Data_StateflowElement, gen_simulink_msglib_CommunicationSwitch_Block, gen_simulink_msglib_LinkLayer_Block, gen_simulink_buffer_Enqueue_BufferFunction, gen_simulink_buffer_Dequeue_BufferFunction, gen_simulink_buffer_CheckQueue_BufferFunction, gen_simulink_buffer_SharedEnqueue_BufferFunction, gen_simulink_buffer_SharedDequeue_BufferFunction, gen_simulink_buffer_SharedCheckQueue_BufferFunction, gen_simulink_buffer_BufferFunction_EmbeddedFunction, gen_simulink_reconfiguration_MultiSourceControl_Block, gen_simulink_reconfiguration_FadingComponent_Block, gen_simulink_reconfiguration_MultiTargetControl_Block},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)