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
NamedElement = Class(name="NamedElement")
rtsc_Realtimestatechart = Class(name="rtsc_Realtimestatechart")
Behavior = Class(name="Behavior")
rtsc_Transition = Class(name="rtsc_Transition")
rtsc_State = Class(name="rtsc_State")
rtsc_Behavior = Class(name="rtsc_Behavior", is_abstract=True)
rtsc_BehavioralElement = Class(name="rtsc_BehavioralElement", is_abstract=True)
rtsc_MessageType = Class(name="rtsc_MessageType")
rtsc_NamedElement = Class(name="rtsc_NamedElement", is_abstract=True)
rtsc_Variable = Class(name="rtsc_Variable")
rtsc_Clock = Class(name="rtsc_Clock")
Vertex = Class(name="Vertex")
rtsc_Event = Class(name="rtsc_Event", is_abstract=True)
rtsc_Guard = Class(name="rtsc_Guard")
rtsc_ClockConstraint = Class(name="rtsc_ClockConstraint")
rtsc_Message = Class(name="rtsc_Message")
rtsc_System = Class(name="rtsc_System")
rtsc_Vertex = Class(name="rtsc_Vertex", is_abstract=True)
rtsc_Port = Class(name="rtsc_Port")
BehavioralElement = Class(name="BehavioralElement")
rtsc_MessageBuffer = Class(name="rtsc_MessageBuffer")
rtsc_Connector = Class(name="rtsc_Connector")
rtsc_CoordinationProtocol = Class(name="rtsc_CoordinationProtocol")
rtsc_MessageTypeRepository = Class(name="rtsc_MessageTypeRepository")
rtsc_MessageEvent = Class(name="rtsc_MessageEvent")
Event = Class(name="Event")
rtsc_ClockResetEvent = Class(name="rtsc_ClockResetEvent")
rtsc_VariableAssignmentEvent = Class(name="rtsc_VariableAssignmentEvent")

# NamedElement class attributes and methods

# rtsc_Realtimestatechart class attributes and methods

# Behavior class attributes and methods

# rtsc_Transition class attributes and methods

# rtsc_State class attributes and methods
rtsc_State_initial: Property = Property(name="initial", type=BooleanType)
rtsc_State_final: Property = Property(name="final", type=BooleanType)
rtsc_State.attributes={rtsc_State_initial, rtsc_State_final}

# rtsc_Behavior class attributes and methods

# rtsc_BehavioralElement class attributes and methods

# rtsc_MessageType class attributes and methods

# rtsc_NamedElement class attributes and methods
rtsc_NamedElement_name: Property = Property(name="name", type=StringType)
rtsc_NamedElement.attributes={rtsc_NamedElement_name}

# rtsc_Variable class attributes and methods
rtsc_Variable_initialValue: Property = Property(name="initialValue", type=StringType)
rtsc_Variable.attributes={rtsc_Variable_initialValue}

# rtsc_Clock class attributes and methods

# Vertex class attributes and methods

# rtsc_Event class attributes and methods

# rtsc_Guard class attributes and methods
rtsc_Guard_value: Property = Property(name="value", type=StringType)
rtsc_Guard.attributes={rtsc_Guard_value}

# rtsc_ClockConstraint class attributes and methods
rtsc_ClockConstraint_bound: Property = Property(name="bound", type=IntegerType)
rtsc_ClockConstraint.attributes={rtsc_ClockConstraint_bound}

# rtsc_Message class attributes and methods

# rtsc_System class attributes and methods

# rtsc_Vertex class attributes and methods

# rtsc_Port class attributes and methods

# BehavioralElement class attributes and methods

# rtsc_MessageBuffer class attributes and methods

# rtsc_Connector class attributes and methods

# rtsc_CoordinationProtocol class attributes and methods

# rtsc_MessageTypeRepository class attributes and methods

# rtsc_MessageEvent class attributes and methods

# Event class attributes and methods

# rtsc_ClockResetEvent class attributes and methods

# rtsc_VariableAssignmentEvent class attributes and methods
rtsc_VariableAssignmentEvent_value: Property = Property(name="value", type=StringType)
rtsc_VariableAssignmentEvent.attributes={rtsc_VariableAssignmentEvent_value}

# Relationships
behavior1: BinaryAssociation = BinaryAssociation(
    name="behavior1",
    ends={
        Property(name="Behavior", type=rtsc_BehavioralElement, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralElement", type=rtsc_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
transitions2: BinaryAssociation = BinaryAssociation(
    name="transitions2",
    ends={
        Property(name="Transition", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart", type=rtsc_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behaviouralElement0: BinaryAssociation = BinaryAssociation(
    name="behaviouralElement0",
    ends={
        Property(name="BehavioralElement", type=rtsc_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior", type=rtsc_BehavioralElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
clockConstraints27: BinaryAssociation = BinaryAssociation(
    name="clockConstraints27",
    ends={
        Property(name="rtsc_Transition28", type=rtsc_ClockConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="rtsc_ClockConstraint", type=rtsc_Transition, multiplicity=Multiplicity(1, 1))
    }
)
statechart29: BinaryAssociation = BinaryAssociation(
    name="statechart29",
    ends={
        Property(name="Realtimestatechart30", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(1, 1))
    }
)
triggerMessage31: BinaryAssociation = BinaryAssociation(
    name="triggerMessage31",
    ends={
        Property(name="rtsc_MessageType", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Transition32", type=rtsc_MessageType, multiplicity=Multiplicity(0, 9999))
    }
)
events33: BinaryAssociation = BinaryAssociation(
    name="events33",
    ends={
        Property(name="rtsc_Event35", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Transition34", type=rtsc_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states3: BinaryAssociation = BinaryAssociation(
    name="states3",
    ends={
        Property(name="State", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(1, 1)),
        Property(name="owningRTSC", type=rtsc_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState4: BinaryAssociation = BinaryAssociation(
    name="initialState4",
    ends={
        Property(name="rtsc_State", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Realtimestatechart", type=rtsc_State, multiplicity=Multiplicity(1, 1))
    }
)
variables5: BinaryAssociation = BinaryAssociation(
    name="variables5",
    ends={
        Property(name="Variable", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart6", type=rtsc_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clocks7: BinaryAssociation = BinaryAssociation(
    name="clocks7",
    ends={
        Property(name="Clock", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart8", type=rtsc_Clock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subStatecharts9: BinaryAssociation = BinaryAssociation(
    name="subStatecharts9",
    ends={
        Property(name="rtsc_Realtimestatechart11", type=rtsc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_State10", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningRTSC12: BinaryAssociation = BinaryAssociation(
    name="owningRTSC12",
    ends={
        Property(name="Realtimestatechart", type=rtsc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(1, 1))
    }
)
incomingTransitions13: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions13",
    ends={
        Property(name="Transition14", type=rtsc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=rtsc_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingTransitions15: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions15",
    ends={
        Property(name="Transition16", type=rtsc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=rtsc_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
entryEvents17: BinaryAssociation = BinaryAssociation(
    name="entryEvents17",
    ends={
        Property(name="rtsc_Event", type=rtsc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_State18", type=rtsc_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exitEvents19: BinaryAssociation = BinaryAssociation(
    name="exitEvents19",
    ends={
        Property(name="rtsc_Event21", type=rtsc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_State20", type=rtsc_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source22: BinaryAssociation = BinaryAssociation(
    name="source22",
    ends={
        Property(name="State23", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=rtsc_State, multiplicity=Multiplicity(1, 1))
    }
)
target24: BinaryAssociation = BinaryAssociation(
    name="target24",
    ends={
        Property(name="State25", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=rtsc_State, multiplicity=Multiplicity(1, 1))
    }
)
guards26: BinaryAssociation = BinaryAssociation(
    name="guards26",
    ends={
        Property(name="rtsc_Guard", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Transition", type=rtsc_Guard, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ports52: BinaryAssociation = BinaryAssociation(
    name="ports52",
    ends={
        Property(name="rtsc_CoordinationProtocol", type=rtsc_Port, multiplicity=Multiplicity(2, 2)),
        Property(name="rtsc_Port53", type=rtsc_CoordinationProtocol, multiplicity=Multiplicity(1, 1))
    }
)
connector54: BinaryAssociation = BinaryAssociation(
    name="connector54",
    ends={
        Property(name="rtsc_Connector", type=rtsc_CoordinationProtocol, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_CoordinationProtocol55", type=rtsc_Connector, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type56: BinaryAssociation = BinaryAssociation(
    name="type56",
    ends={
        Property(name="rtsc_MessageType57", type=rtsc_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Message", type=rtsc_MessageType, multiplicity=Multiplicity(1, 1))
    }
)
statecharts58: BinaryAssociation = BinaryAssociation(
    name="statecharts58",
    ends={
        Property(name="rtsc_Realtimestatechart59", type=rtsc_System, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_System", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable36: BinaryAssociation = BinaryAssociation(
    name="variable36",
    ends={
        Property(name="rtsc_Variable", type=rtsc_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Guard37", type=rtsc_Variable, multiplicity=Multiplicity(0, 1))
    }
)
clock38: BinaryAssociation = BinaryAssociation(
    name="clock38",
    ends={
        Property(name="rtsc_Clock", type=rtsc_ClockConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_ClockConstraint39", type=rtsc_Clock, multiplicity=Multiplicity(1, 1))
    }
)
statechart40: BinaryAssociation = BinaryAssociation(
    name="statechart40",
    ends={
        Property(name="Realtimestatechart41", type=rtsc_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variables", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(0, 1))
    }
)
statechart42: BinaryAssociation = BinaryAssociation(
    name="statechart42",
    ends={
        Property(name="Realtimestatechart43", type=rtsc_Clock, multiplicity=Multiplicity(1, 1)),
        Property(name="clocks", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(1, 1))
    }
)
behaviour44: BinaryAssociation = BinaryAssociation(
    name="behaviour44",
    ends={
        Property(name="rtsc_Behavior", type=rtsc_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Port", type=rtsc_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
incomingBuffer45: BinaryAssociation = BinaryAssociation(
    name="incomingBuffer45",
    ends={
        Property(name="MessageBuffer", type=rtsc_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="port", type=rtsc_MessageBuffer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connector46: BinaryAssociation = BinaryAssociation(
    name="connector46",
    ends={
        Property(name="Connector", type=rtsc_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="endpoints", type=rtsc_Connector, multiplicity=Multiplicity(0, 1))
    }
)
port47: BinaryAssociation = BinaryAssociation(
    name="port47",
    ends={
        Property(name="Port", type=rtsc_MessageBuffer, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingBuffer", type=rtsc_Port, multiplicity=Multiplicity(1, 1))
    }
)
types48: BinaryAssociation = BinaryAssociation(
    name="types48",
    ends={
        Property(name="rtsc_MessageType49", type=rtsc_MessageBuffer, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_MessageBuffer", type=rtsc_MessageType, multiplicity=Multiplicity(1, 9999))
    }
)
endpoints50: BinaryAssociation = BinaryAssociation(
    name="endpoints50",
    ends={
        Property(name="Port51", type=rtsc_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="connector", type=rtsc_Port, multiplicity=Multiplicity(2, 2))
    }
)
protocol60: BinaryAssociation = BinaryAssociation(
    name="protocol60",
    ends={
        Property(name="rtsc_CoordinationProtocol62", type=rtsc_System, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_System61", type=rtsc_CoordinationProtocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageTypeRepo63: BinaryAssociation = BinaryAssociation(
    name="messageTypeRepo63",
    ends={
        Property(name="rtsc_MessageTypeRepository", type=rtsc_System, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_System64", type=rtsc_MessageTypeRepository, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
messageTypes65: BinaryAssociation = BinaryAssociation(
    name="messageTypes65",
    ends={
        Property(name="rtsc_MessageType67", type=rtsc_MessageTypeRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_MessageTypeRepository66", type=rtsc_MessageType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageType68: BinaryAssociation = BinaryAssociation(
    name="messageType68",
    ends={
        Property(name="rtsc_MessageType69", type=rtsc_MessageEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_MessageEvent", type=rtsc_MessageType, multiplicity=Multiplicity(1, 1))
    }
)
clock70: BinaryAssociation = BinaryAssociation(
    name="clock70",
    ends={
        Property(name="rtsc_Clock71", type=rtsc_ClockResetEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_ClockResetEvent", type=rtsc_Clock, multiplicity=Multiplicity(1, 1))
    }
)
variable72: BinaryAssociation = BinaryAssociation(
    name="variable72",
    ends={
        Property(name="rtsc_Variable73", type=rtsc_VariableAssignmentEvent, multiplicity=Multiplicity(1, 1)),
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
gen_rtsc_MessageType_NamedElement = Generalization(general=NamedElement, specific=rtsc_MessageType)
gen_rtsc_Variable_NamedElement = Generalization(general=NamedElement, specific=rtsc_Variable)
gen_rtsc_Clock_NamedElement = Generalization(general=NamedElement, specific=rtsc_Clock)
gen_rtsc_Port_BehavioralElement = Generalization(general=BehavioralElement, specific=rtsc_Port)
gen_rtsc_CoordinationProtocol_NamedElement = Generalization(general=NamedElement, specific=rtsc_CoordinationProtocol)
gen_rtsc_MessageEvent_Event = Generalization(general=Event, specific=rtsc_MessageEvent)
gen_rtsc_ClockResetEvent_Event = Generalization(general=Event, specific=rtsc_ClockResetEvent)
gen_rtsc_VariableAssignmentEvent_Event = Generalization(general=Event, specific=rtsc_VariableAssignmentEvent)

# Domain Model
domain_model = DomainModel(
    name="rtsc",
    types={NamedElement, rtsc_Realtimestatechart, Behavior, rtsc_Transition, rtsc_State, rtsc_Behavior, rtsc_BehavioralElement, rtsc_MessageType, rtsc_NamedElement, rtsc_Variable, rtsc_Clock, Vertex, rtsc_Event, rtsc_Guard, rtsc_ClockConstraint, rtsc_Message, rtsc_System, rtsc_Vertex, rtsc_Port, BehavioralElement, rtsc_MessageBuffer, rtsc_Connector, rtsc_CoordinationProtocol, rtsc_MessageTypeRepository, rtsc_MessageEvent, Event, rtsc_ClockResetEvent, rtsc_VariableAssignmentEvent},
    associations={behavior1, transitions2, behaviouralElement0, clockConstraints27, statechart29, triggerMessage31, events33, states3, initialState4, variables5, clocks7, subStatecharts9, owningRTSC12, incomingTransitions13, outgoingTransitions15, entryEvents17, exitEvents19, source22, target24, guards26, ports52, connector54, type56, statecharts58, variable36, clock38, statechart40, statechart42, behaviour44, incomingBuffer45, connector46, port47, types48, endpoints50, protocol60, messageTypeRepo63, messageTypes65, messageType68, clock70, variable72},
    generalizations={gen_rtsc_BehavioralElement_NamedElement, gen_rtsc_Realtimestatechart_Behavior, gen_rtsc_Realtimestatechart_NamedElement, gen_rtsc_State_Vertex, gen_rtsc_State_NamedElement, gen_rtsc_Transition_NamedElement, gen_rtsc_MessageType_NamedElement, gen_rtsc_Variable_NamedElement, gen_rtsc_Clock_NamedElement, gen_rtsc_Port_BehavioralElement, gen_rtsc_CoordinationProtocol_NamedElement, gen_rtsc_MessageEvent_Event, gen_rtsc_ClockResetEvent_Event, gen_rtsc_VariableAssignmentEvent_Event},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)