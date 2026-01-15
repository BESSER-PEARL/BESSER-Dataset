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
rtsc_Behavior = Class(name="rtsc::Behavior", is_abstract=True)
rtsc_BehavioralElement = Class(name="rtsc::BehavioralElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
rtsc_Realtimestatechart = Class(name="rtsc::Realtimestatechart")
Behavior = Class(name="Behavior")
rtsc_Transition = Class(name="rtsc::Transition")
rtsc_State = Class(name="rtsc::State")
rtsc_Variable = Class(name="rtsc::Variable")
rtsc_Clock = Class(name="rtsc::Clock")
Vertex = Class(name="Vertex")
rtsc_NamedElement = Class(name="rtsc::NamedElement", is_abstract=True)
rtsc_Vertex = Class(name="rtsc::Vertex", is_abstract=True)
rtsc_Event = Class(name="rtsc::Event", is_abstract=True)
rtsc_Guard = Class(name="rtsc::Guard")
rtsc_ClockConstraint = Class(name="rtsc::ClockConstraint")
rtsc_MessageType = Class(name="rtsc::MessageType")
rtsc_CoordinationProtocol = Class(name="rtsc::CoordinationProtocol")
rtsc_Port = Class(name="rtsc::Port")
BehavioralElement = Class(name="BehavioralElement")
rtsc_MessageBuffer = Class(name="rtsc::MessageBuffer")
rtsc_Connector = Class(name="rtsc::Connector")
rtsc_Message = Class(name="rtsc::Message")
rtsc_System = Class(name="rtsc::System")
rtsc_MessageTypeRepository = Class(name="rtsc::MessageTypeRepository")
rtsc_MessageEvent = Class(name="rtsc::MessageEvent")
Event = Class(name="Event")
rtsc_ClockResetEvent = Class(name="rtsc::ClockResetEvent")
rtsc_VariableAssignmentEvent = Class(name="rtsc::VariableAssignmentEvent")

# rtsc_Behavior class attributes and methods

# rtsc_BehavioralElement class attributes and methods

# NamedElement class attributes and methods

# rtsc_Realtimestatechart class attributes and methods

# Behavior class attributes and methods

# rtsc_Transition class attributes and methods

# rtsc_State class attributes and methods
rtsc_State_initial: Property = Property(name="initial", type=BooleanType)
rtsc_State_final: Property = Property(name="final", type=BooleanType)
rtsc_State.attributes={rtsc_State_final, rtsc_State_initial}

# rtsc_Variable class attributes and methods
rtsc_Variable_initialValue: Property = Property(name="initialValue", type=StringType)
rtsc_Variable.attributes={rtsc_Variable_initialValue}

# rtsc_Clock class attributes and methods

# Vertex class attributes and methods

# rtsc_NamedElement class attributes and methods
rtsc_NamedElement_name: Property = Property(name="name", type=StringType)
rtsc_NamedElement.attributes={rtsc_NamedElement_name}

# rtsc_Vertex class attributes and methods

# rtsc_Event class attributes and methods

# rtsc_Guard class attributes and methods
rtsc_Guard_value: Property = Property(name="value", type=StringType)
rtsc_Guard.attributes={rtsc_Guard_value}

# rtsc_ClockConstraint class attributes and methods
rtsc_ClockConstraint_bound: Property = Property(name="bound", type=IntegerType)
rtsc_ClockConstraint.attributes={rtsc_ClockConstraint_bound}

# rtsc_MessageType class attributes and methods

# rtsc_CoordinationProtocol class attributes and methods

# rtsc_Port class attributes and methods

# BehavioralElement class attributes and methods

# rtsc_MessageBuffer class attributes and methods

# rtsc_Connector class attributes and methods

# rtsc_Message class attributes and methods

# rtsc_System class attributes and methods

# rtsc_MessageTypeRepository class attributes and methods

# rtsc_MessageEvent class attributes and methods

# Event class attributes and methods

# rtsc_ClockResetEvent class attributes and methods

# rtsc_VariableAssignmentEvent class attributes and methods
rtsc_VariableAssignmentEvent_value: Property = Property(name="value", type=StringType)
rtsc_VariableAssignmentEvent.attributes={rtsc_VariableAssignmentEvent_value}

# Relationships
subStatecharts18: BinaryAssociation = BinaryAssociation(
    name="subStatecharts18",
    ends={
        Property(name="rtsc_Realtimestatechart20", type=rtsc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_State19", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behaviouralElement0: BinaryAssociation = BinaryAssociation(
    name="behaviouralElement0",
    ends={
        Property(name="1", type=rtsc_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=rtsc_BehavioralElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
behavior2: BinaryAssociation = BinaryAssociation(
    name="behavior2",
    ends={
        Property(name="4", type=rtsc_BehavioralElement, multiplicity=Multiplicity(1, 1)),
        Property(name="3", type=rtsc_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
transitions5: BinaryAssociation = BinaryAssociation(
    name="transitions5",
    ends={
        Property(name="7", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(1, 1)),
        Property(name="6", type=rtsc_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states8: BinaryAssociation = BinaryAssociation(
    name="states8",
    ends={
        Property(name="10", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(1, 1)),
        Property(name="9", type=rtsc_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState11: BinaryAssociation = BinaryAssociation(
    name="initialState11",
    ends={
        Property(name="rtsc_State", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Realtimestatechart", type=rtsc_State, multiplicity=Multiplicity(1, 1))
    }
)
variables12: BinaryAssociation = BinaryAssociation(
    name="variables12",
    ends={
        Property(name="14", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(1, 1)),
        Property(name="13", type=rtsc_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clocks15: BinaryAssociation = BinaryAssociation(
    name="clocks15",
    ends={
        Property(name="17", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(1, 1)),
        Property(name="16", type=rtsc_Clock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningRTSC21: BinaryAssociation = BinaryAssociation(
    name="owningRTSC21",
    ends={
        Property(name="23", type=rtsc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="22", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(1, 1))
    }
)
incomingTransitions24: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions24",
    ends={
        Property(name="26", type=rtsc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="25", type=rtsc_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingTransitions27: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions27",
    ends={
        Property(name="29", type=rtsc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="28", type=rtsc_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
entryEvents30: BinaryAssociation = BinaryAssociation(
    name="entryEvents30",
    ends={
        Property(name="rtsc_Event", type=rtsc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_State31", type=rtsc_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exitEvents32: BinaryAssociation = BinaryAssociation(
    name="exitEvents32",
    ends={
        Property(name="rtsc_Event34", type=rtsc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_State33", type=rtsc_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source35: BinaryAssociation = BinaryAssociation(
    name="source35",
    ends={
        Property(name="37", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="36", type=rtsc_State, multiplicity=Multiplicity(1, 1))
    }
)
target38: BinaryAssociation = BinaryAssociation(
    name="target38",
    ends={
        Property(name="40", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="39", type=rtsc_State, multiplicity=Multiplicity(1, 1))
    }
)
guards41: BinaryAssociation = BinaryAssociation(
    name="guards41",
    ends={
        Property(name="rtsc_Guard", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Transition", type=rtsc_Guard, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clockConstraints42: BinaryAssociation = BinaryAssociation(
    name="clockConstraints42",
    ends={
        Property(name="rtsc_ClockConstraint", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Transition43", type=rtsc_ClockConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statechart44: BinaryAssociation = BinaryAssociation(
    name="statechart44",
    ends={
        Property(name="46", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="45", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(1, 1))
    }
)
triggerMessage47: BinaryAssociation = BinaryAssociation(
    name="triggerMessage47",
    ends={
        Property(name="rtsc_MessageType", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Transition48", type=rtsc_MessageType, multiplicity=Multiplicity(0, 9999))
    }
)
events49: BinaryAssociation = BinaryAssociation(
    name="events49",
    ends={
        Property(name="rtsc_Event51", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Transition50", type=rtsc_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ports77: BinaryAssociation = BinaryAssociation(
    name="ports77",
    ends={
        Property(name="rtsc_Port78", type=rtsc_CoordinationProtocol, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_CoordinationProtocol", type=rtsc_Port, multiplicity=Multiplicity(2, 2))
    }
)
variable52: BinaryAssociation = BinaryAssociation(
    name="variable52",
    ends={
        Property(name="rtsc_Variable", type=rtsc_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Guard53", type=rtsc_Variable, multiplicity=Multiplicity(0, 1))
    }
)
clock54: BinaryAssociation = BinaryAssociation(
    name="clock54",
    ends={
        Property(name="rtsc_Clock", type=rtsc_ClockConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_ClockConstraint55", type=rtsc_Clock, multiplicity=Multiplicity(1, 1))
    }
)
statechart56: BinaryAssociation = BinaryAssociation(
    name="statechart56",
    ends={
        Property(name="58", type=rtsc_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="57", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(0, 1))
    }
)
statechart59: BinaryAssociation = BinaryAssociation(
    name="statechart59",
    ends={
        Property(name="61", type=rtsc_Clock, multiplicity=Multiplicity(1, 1)),
        Property(name="60", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(1, 1))
    }
)
behaviour62: BinaryAssociation = BinaryAssociation(
    name="behaviour62",
    ends={
        Property(name="rtsc_Behavior", type=rtsc_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Port", type=rtsc_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
incomingBuffer63: BinaryAssociation = BinaryAssociation(
    name="incomingBuffer63",
    ends={
        Property(name="65", type=rtsc_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="64", type=rtsc_MessageBuffer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connector66: BinaryAssociation = BinaryAssociation(
    name="connector66",
    ends={
        Property(name="68", type=rtsc_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="67", type=rtsc_Connector, multiplicity=Multiplicity(0, 1))
    }
)
port69: BinaryAssociation = BinaryAssociation(
    name="port69",
    ends={
        Property(name="71", type=rtsc_MessageBuffer, multiplicity=Multiplicity(1, 1)),
        Property(name="70", type=rtsc_Port, multiplicity=Multiplicity(1, 1))
    }
)
types72: BinaryAssociation = BinaryAssociation(
    name="types72",
    ends={
        Property(name="rtsc_MessageType73", type=rtsc_MessageBuffer, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_MessageBuffer", type=rtsc_MessageType, multiplicity=Multiplicity(1, 9999))
    }
)
endpoints74: BinaryAssociation = BinaryAssociation(
    name="endpoints74",
    ends={
        Property(name="76", type=rtsc_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="75", type=rtsc_Port, multiplicity=Multiplicity(2, 2))
    }
)
connector79: BinaryAssociation = BinaryAssociation(
    name="connector79",
    ends={
        Property(name="rtsc_Connector", type=rtsc_CoordinationProtocol, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_CoordinationProtocol80", type=rtsc_Connector, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type81: BinaryAssociation = BinaryAssociation(
    name="type81",
    ends={
        Property(name="rtsc_MessageType82", type=rtsc_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Message", type=rtsc_MessageType, multiplicity=Multiplicity(1, 1))
    }
)
statecharts83: BinaryAssociation = BinaryAssociation(
    name="statecharts83",
    ends={
        Property(name="rtsc_Realtimestatechart84", type=rtsc_System, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_System", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
protocol85: BinaryAssociation = BinaryAssociation(
    name="protocol85",
    ends={
        Property(name="rtsc_CoordinationProtocol87", type=rtsc_System, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_System86", type=rtsc_CoordinationProtocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageTypeRepo88: BinaryAssociation = BinaryAssociation(
    name="messageTypeRepo88",
    ends={
        Property(name="rtsc_MessageTypeRepository", type=rtsc_System, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_System89", type=rtsc_MessageTypeRepository, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
messageTypes90: BinaryAssociation = BinaryAssociation(
    name="messageTypes90",
    ends={
        Property(name="rtsc_MessageType92", type=rtsc_MessageTypeRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_MessageTypeRepository91", type=rtsc_MessageType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageType93: BinaryAssociation = BinaryAssociation(
    name="messageType93",
    ends={
        Property(name="rtsc_MessageType94", type=rtsc_MessageEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_MessageEvent", type=rtsc_MessageType, multiplicity=Multiplicity(1, 1))
    }
)
clock95: BinaryAssociation = BinaryAssociation(
    name="clock95",
    ends={
        Property(name="rtsc_Clock96", type=rtsc_ClockResetEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_ClockResetEvent", type=rtsc_Clock, multiplicity=Multiplicity(1, 1))
    }
)
variable97: BinaryAssociation = BinaryAssociation(
    name="variable97",
    ends={
        Property(name="rtsc_Variable98", type=rtsc_VariableAssignmentEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_VariableAssignmentEvent", type=rtsc_Variable, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_rtsc_BehavioralElement_NamedElement = Generalization(general=NamedElement, specific=rtsc_BehavioralElement)
gen_rtsc_Realtimestatechart_Behavior = Generalization(general=Behavior, specific=rtsc_Realtimestatechart)
gen_rtsc_Realtimestatechart_NamedElement = Generalization(general=NamedElement, specific=rtsc_Realtimestatechart)
gen_rtsc_State_Vertex = Generalization(general=Vertex, specific=rtsc_State)
gen_rtsc_State_NamedElement = Generalization(general=NamedElement, specific=rtsc_State)
gen_rtsc_Transition_NamedElement = Generalization(general=NamedElement, specific=rtsc_Transition)
gen_rtsc_CoordinationProtocol_NamedElement = Generalization(general=NamedElement, specific=rtsc_CoordinationProtocol)
gen_rtsc_Variable_NamedElement = Generalization(general=NamedElement, specific=rtsc_Variable)
gen_rtsc_Clock_NamedElement = Generalization(general=NamedElement, specific=rtsc_Clock)
gen_rtsc_Port_BehavioralElement = Generalization(general=BehavioralElement, specific=rtsc_Port)
gen_rtsc_MessageType_NamedElement = Generalization(general=NamedElement, specific=rtsc_MessageType)
gen_rtsc_MessageEvent_Event = Generalization(general=Event, specific=rtsc_MessageEvent)
gen_rtsc_ClockResetEvent_Event = Generalization(general=Event, specific=rtsc_ClockResetEvent)
gen_rtsc_VariableAssignmentEvent_Event = Generalization(general=Event, specific=rtsc_VariableAssignmentEvent)

# Domain Model
domain_model = DomainModel(
    name="rtsc",
    types={rtsc_Behavior, rtsc_BehavioralElement, NamedElement, rtsc_Realtimestatechart, Behavior, rtsc_Transition, rtsc_State, rtsc_Variable, rtsc_Clock, Vertex, rtsc_NamedElement, rtsc_Vertex, rtsc_Event, rtsc_Guard, rtsc_ClockConstraint, rtsc_MessageType, rtsc_CoordinationProtocol, rtsc_Port, BehavioralElement, rtsc_MessageBuffer, rtsc_Connector, rtsc_Message, rtsc_System, rtsc_MessageTypeRepository, rtsc_MessageEvent, Event, rtsc_ClockResetEvent, rtsc_VariableAssignmentEvent},
    associations={subStatecharts18, behaviouralElement0, behavior2, transitions5, states8, initialState11, variables12, clocks15, owningRTSC21, incomingTransitions24, outgoingTransitions27, entryEvents30, exitEvents32, source35, target38, guards41, clockConstraints42, statechart44, triggerMessage47, events49, ports77, variable52, clock54, statechart56, statechart59, behaviour62, incomingBuffer63, connector66, port69, types72, endpoints74, connector79, type81, statecharts83, protocol85, messageTypeRepo88, messageTypes90, messageType93, clock95, variable97},
    generalizations={gen_rtsc_BehavioralElement_NamedElement, gen_rtsc_Realtimestatechart_Behavior, gen_rtsc_Realtimestatechart_NamedElement, gen_rtsc_State_Vertex, gen_rtsc_State_NamedElement, gen_rtsc_Transition_NamedElement, gen_rtsc_CoordinationProtocol_NamedElement, gen_rtsc_Variable_NamedElement, gen_rtsc_Clock_NamedElement, gen_rtsc_Port_BehavioralElement, gen_rtsc_MessageType_NamedElement, gen_rtsc_MessageEvent_Event, gen_rtsc_ClockResetEvent_Event, gen_rtsc_VariableAssignmentEvent_Event},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)