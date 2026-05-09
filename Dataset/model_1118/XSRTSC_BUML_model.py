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
rtsc_Variable = Class(name="rtsc_Variable")
rtsc_Behavior = Class(name="rtsc_Behavior", is_abstract=True)
rtsc_Clock = Class(name="rtsc_Clock")
rtsc_BehavioralElement = Class(name="rtsc_BehavioralElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
rtsc_Realtimestatechart = Class(name="rtsc_Realtimestatechart")
Behavior = Class(name="Behavior")
rtsc_Transition = Class(name="rtsc_Transition")
rtsc_State = Class(name="rtsc_State")
rtsc_ClockConstraint = Class(name="rtsc_ClockConstraint")
rtsc_MessageType = Class(name="rtsc_MessageType")
Vertex = Class(name="Vertex")
rtsc_Event = Class(name="rtsc_Event", is_abstract=True)
rtsc_Guard = Class(name="rtsc_Guard")
rtsc_MessageBuffer = Class(name="rtsc_MessageBuffer")
rtsc_Connector = Class(name="rtsc_Connector")
rtsc_NamedElement = Class(name="rtsc_NamedElement", is_abstract=True)
rtsc_Vertex = Class(name="rtsc_Vertex")
rtsc_Port = Class(name="rtsc_Port")
BehavioralElement = Class(name="BehavioralElement")
rtsc_Message = Class(name="rtsc_Message")
rtsc_CoordinationProtocol = Class(name="rtsc_CoordinationProtocol")
rtsc_System = Class(name="rtsc_System")
rtsc_MessageTypeRepository = Class(name="rtsc_MessageTypeRepository")
rtsc_MessageEvent = Class(name="rtsc_MessageEvent")
Event = Class(name="Event")
rtsc_ClockResetEvent = Class(name="rtsc_ClockResetEvent")
rtsc_VariableAssignmentEvent = Class(name="rtsc_VariableAssignmentEvent")

# rtsc_Variable class attributes and methods
rtsc_Variable_initialValue: Property = Property(name="initialValue", type=StringType)
rtsc_Variable_runtimeValue: Property = Property(name="runtimeValue", type=StringType)
rtsc_Variable.attributes={rtsc_Variable_initialValue, rtsc_Variable_runtimeValue}

# rtsc_Behavior class attributes and methods

# rtsc_Clock class attributes and methods
rtsc_Clock_uClock: Property = Property(name="uClock", type=BooleanType)
rtsc_Clock_m_initialize: Method = Method(name="initialize", parameters={})
rtsc_Clock_m_printValue: Method = Method(name="printValue", parameters={})
rtsc_Clock_m_reset: Method = Method(name="reset", parameters={})
rtsc_Clock.attributes={rtsc_Clock_uClock}
rtsc_Clock.methods={rtsc_Clock_m_printValue, rtsc_Clock_m_initialize, rtsc_Clock_m_reset}

# rtsc_BehavioralElement class attributes and methods

# NamedElement class attributes and methods

# rtsc_Realtimestatechart class attributes and methods
rtsc_Realtimestatechart_rounds: Property = Property(name="rounds", type=IntegerType)
rtsc_Realtimestatechart_m_main: Method = Method(name="main", parameters={})
rtsc_Realtimestatechart_m_initialize: Method = Method(name="initialize", parameters={Parameter(name='rtsc_args', type=StringType)})
rtsc_Realtimestatechart_m_step: Method = Method(name="step", parameters={})
rtsc_Realtimestatechart_m_sequentialStep: Method = Method(name="sequentialStep", parameters={})
rtsc_Realtimestatechart.attributes={rtsc_Realtimestatechart_rounds}
rtsc_Realtimestatechart.methods={rtsc_Realtimestatechart_m_step, rtsc_Realtimestatechart_m_initialize, rtsc_Realtimestatechart_m_sequentialStep, rtsc_Realtimestatechart_m_main}

# Behavior class attributes and methods

# rtsc_Transition class attributes and methods
rtsc_Transition_hitCount: Property = Property(name="hitCount", type=IntegerType)
rtsc_Transition_m_canFire: Method = Method(name="canFire", parameters={})
rtsc_Transition_m_fire: Method = Method(name="fire", parameters={}, type=Vertex)
rtsc_Transition_m_guardsHold: Method = Method(name="guardsHold", parameters={})
rtsc_Transition_m_clocksHold: Method = Method(name="clocksHold", parameters={})
rtsc_Transition_m_checkMessages: Method = Method(name="checkMessages", parameters={})
rtsc_Transition_m_consumeMessages: Method = Method(name="consumeMessages", parameters={})
rtsc_Transition.attributes={rtsc_Transition_hitCount}
rtsc_Transition.methods={rtsc_Transition_m_fire, rtsc_Transition_m_guardsHold, rtsc_Transition_m_canFire, rtsc_Transition_m_clocksHold, rtsc_Transition_m_checkMessages, rtsc_Transition_m_consumeMessages}

# rtsc_State class attributes and methods
rtsc_State_initial: Property = Property(name="initial", type=BooleanType)
rtsc_State_final: Property = Property(name="final", type=BooleanType)
rtsc_State_m_entry: Method = Method(name="entry", parameters={})
rtsc_State_m_exit: Method = Method(name="exit", parameters={})
rtsc_State.attributes={rtsc_State_final, rtsc_State_initial}
rtsc_State.methods={rtsc_State_m_entry, rtsc_State_m_exit}

# rtsc_ClockConstraint class attributes and methods
rtsc_ClockConstraint_bound: Property = Property(name="bound", type=IntegerType)
rtsc_ClockConstraint_m_evaluate: Method = Method(name="evaluate", parameters={Parameter(name='rtsc_checkFederation', type=StringType)})
rtsc_ClockConstraint_m_apply: Method = Method(name="apply", parameters={Parameter(name='rtsc_federation', type=StringType)})
rtsc_ClockConstraint.attributes={rtsc_ClockConstraint_bound}
rtsc_ClockConstraint.methods={rtsc_ClockConstraint_m_evaluate, rtsc_ClockConstraint_m_apply}

# rtsc_MessageType class attributes and methods

# Vertex class attributes and methods

# rtsc_Event class attributes and methods
rtsc_Event_m_execute: Method = Method(name="execute", parameters={})
rtsc_Event.methods={rtsc_Event_m_execute}

# rtsc_Guard class attributes and methods
rtsc_Guard_value: Property = Property(name="value", type=BooleanType)
rtsc_Guard_m_evaluate: Method = Method(name="evaluate", parameters={})
rtsc_Guard.attributes={rtsc_Guard_value}
rtsc_Guard.methods={rtsc_Guard_m_evaluate}

# rtsc_MessageBuffer class attributes and methods
rtsc_MessageBuffer_m_getMessage: Method = Method(name="getMessage", parameters={Parameter(name='rtsc_type', type=StringType)}, type=StringType)
rtsc_MessageBuffer_m_hasMessage: Method = Method(name="hasMessage", parameters={Parameter(name='rtsc_type', type=StringType)})
rtsc_MessageBuffer_m_addMessage: Method = Method(name="addMessage", parameters={Parameter(name='rtsc_message', type=StringType)})
rtsc_MessageBuffer.methods={rtsc_MessageBuffer_m_getMessage, rtsc_MessageBuffer_m_addMessage, rtsc_MessageBuffer_m_hasMessage}

# rtsc_Connector class attributes and methods

# rtsc_NamedElement class attributes and methods
rtsc_NamedElement_name: Property = Property(name="name", type=StringType)
rtsc_NamedElement.attributes={rtsc_NamedElement_name}

# rtsc_Vertex class attributes and methods
rtsc_Vertex_active: Property = Property(name="active", type=BooleanType)
rtsc_Vertex.attributes={rtsc_Vertex_active}

# rtsc_Port class attributes and methods

# BehavioralElement class attributes and methods

# rtsc_Message class attributes and methods

# rtsc_CoordinationProtocol class attributes and methods
rtsc_CoordinationProtocol_m_main: Method = Method(name="main", parameters={})
rtsc_CoordinationProtocol_m_initialize: Method = Method(name="initialize", parameters={Parameter(name='rtsc_arguments', type=StringType)})
rtsc_CoordinationProtocol_m_step: Method = Method(name="step", parameters={})
rtsc_CoordinationProtocol.methods={rtsc_CoordinationProtocol_m_main, rtsc_CoordinationProtocol_m_step, rtsc_CoordinationProtocol_m_initialize}

# rtsc_System class attributes and methods

# rtsc_MessageTypeRepository class attributes and methods

# rtsc_MessageEvent class attributes and methods
rtsc_MessageEvent_m_execute: Method = Method(name="execute", parameters={})
rtsc_MessageEvent.methods={rtsc_MessageEvent_m_execute}

# Event class attributes and methods

# rtsc_ClockResetEvent class attributes and methods
rtsc_ClockResetEvent_m_execute: Method = Method(name="execute", parameters={})
rtsc_ClockResetEvent.methods={rtsc_ClockResetEvent_m_execute}

# rtsc_VariableAssignmentEvent class attributes and methods
rtsc_VariableAssignmentEvent_value: Property = Property(name="value", type=StringType)
rtsc_VariableAssignmentEvent_m_execute: Method = Method(name="execute", parameters={})
rtsc_VariableAssignmentEvent.attributes={rtsc_VariableAssignmentEvent_value}
rtsc_VariableAssignmentEvent.methods={rtsc_VariableAssignmentEvent_m_execute}

# Relationships
behaviouralElement0: BinaryAssociation = BinaryAssociation(
    name="behaviouralElement0",
    ends={
        Property(name="BehavioralElement", type=rtsc_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior", type=rtsc_BehavioralElement, multiplicity=Multiplicity(0, 1), is_composite=True)
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
clockConstraints30: BinaryAssociation = BinaryAssociation(
    name="clockConstraints30",
    ends={
        Property(name="rtsc_ClockConstraint", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Transition31", type=rtsc_ClockConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statechart32: BinaryAssociation = BinaryAssociation(
    name="statechart32",
    ends={
        Property(name="Realtimestatechart33", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(1, 1))
    }
)
triggerMessage34: BinaryAssociation = BinaryAssociation(
    name="triggerMessage34",
    ends={
        Property(name="rtsc_MessageType", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Transition35", type=rtsc_MessageType, multiplicity=Multiplicity(0, 9999))
    }
)
activeTransitions9: BinaryAssociation = BinaryAssociation(
    name="activeTransitions9",
    ends={
        Property(name="rtsc_Transition", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Realtimestatechart10", type=rtsc_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
subStatecharts11: BinaryAssociation = BinaryAssociation(
    name="subStatecharts11",
    ends={
        Property(name="rtsc_Realtimestatechart13", type=rtsc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_State12", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningRTSC14: BinaryAssociation = BinaryAssociation(
    name="owningRTSC14",
    ends={
        Property(name="Realtimestatechart", type=rtsc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(1, 1))
    }
)
incomingTransitions15: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions15",
    ends={
        Property(name="Transition16", type=rtsc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=rtsc_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingTransitions17: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions17",
    ends={
        Property(name="Transition18", type=rtsc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=rtsc_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
entryEvents19: BinaryAssociation = BinaryAssociation(
    name="entryEvents19",
    ends={
        Property(name="rtsc_Event", type=rtsc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_State20", type=rtsc_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exitEvents21: BinaryAssociation = BinaryAssociation(
    name="exitEvents21",
    ends={
        Property(name="rtsc_Event23", type=rtsc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_State22", type=rtsc_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source24: BinaryAssociation = BinaryAssociation(
    name="source24",
    ends={
        Property(name="State25", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=rtsc_State, multiplicity=Multiplicity(1, 1))
    }
)
target26: BinaryAssociation = BinaryAssociation(
    name="target26",
    ends={
        Property(name="State27", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=rtsc_State, multiplicity=Multiplicity(1, 1))
    }
)
guards28: BinaryAssociation = BinaryAssociation(
    name="guards28",
    ends={
        Property(name="rtsc_Guard", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Transition29", type=rtsc_Guard, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behaviour47: BinaryAssociation = BinaryAssociation(
    name="behaviour47",
    ends={
        Property(name="rtsc_Port", type=rtsc_Behavior, multiplicity=Multiplicity(0, 1)),
        Property(name="rtsc_Behavior", type=rtsc_Port, multiplicity=Multiplicity(1, 1))
    }
)
incomingBuffer48: BinaryAssociation = BinaryAssociation(
    name="incomingBuffer48",
    ends={
        Property(name="MessageBuffer", type=rtsc_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="port", type=rtsc_MessageBuffer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connector49: BinaryAssociation = BinaryAssociation(
    name="connector49",
    ends={
        Property(name="Connector", type=rtsc_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="endpoints", type=rtsc_Connector, multiplicity=Multiplicity(0, 1))
    }
)
events36: BinaryAssociation = BinaryAssociation(
    name="events36",
    ends={
        Property(name="rtsc_Event38", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Transition37", type=rtsc_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable39: BinaryAssociation = BinaryAssociation(
    name="variable39",
    ends={
        Property(name="rtsc_Variable", type=rtsc_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Guard40", type=rtsc_Variable, multiplicity=Multiplicity(0, 1))
    }
)
clock41: BinaryAssociation = BinaryAssociation(
    name="clock41",
    ends={
        Property(name="rtsc_Clock", type=rtsc_ClockConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_ClockConstraint42", type=rtsc_Clock, multiplicity=Multiplicity(1, 1))
    }
)
statechart43: BinaryAssociation = BinaryAssociation(
    name="statechart43",
    ends={
        Property(name="Realtimestatechart44", type=rtsc_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variables", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(0, 1))
    }
)
statechart45: BinaryAssociation = BinaryAssociation(
    name="statechart45",
    ends={
        Property(name="Realtimestatechart46", type=rtsc_Clock, multiplicity=Multiplicity(1, 1)),
        Property(name="clocks", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(1, 1))
    }
)
messageType74: BinaryAssociation = BinaryAssociation(
    name="messageType74",
    ends={
        Property(name="rtsc_MessageType75", type=rtsc_MessageEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_MessageEvent", type=rtsc_MessageType, multiplicity=Multiplicity(1, 1))
    }
)
port50: BinaryAssociation = BinaryAssociation(
    name="port50",
    ends={
        Property(name="Port", type=rtsc_MessageBuffer, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingBuffer", type=rtsc_Port, multiplicity=Multiplicity(1, 1))
    }
)
types51: BinaryAssociation = BinaryAssociation(
    name="types51",
    ends={
        Property(name="rtsc_MessageType52", type=rtsc_MessageBuffer, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_MessageBuffer", type=rtsc_MessageType, multiplicity=Multiplicity(1, 9999))
    }
)
allMessages53: BinaryAssociation = BinaryAssociation(
    name="allMessages53",
    ends={
        Property(name="rtsc_Message", type=rtsc_MessageBuffer, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_MessageBuffer54", type=rtsc_Message, multiplicity=Multiplicity(0, 9999))
    }
)
endpoints55: BinaryAssociation = BinaryAssociation(
    name="endpoints55",
    ends={
        Property(name="Port56", type=rtsc_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="connector", type=rtsc_Port, multiplicity=Multiplicity(2, 2))
    }
)
ports57: BinaryAssociation = BinaryAssociation(
    name="ports57",
    ends={
        Property(name="rtsc_Port58", type=rtsc_CoordinationProtocol, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_CoordinationProtocol", type=rtsc_Port, multiplicity=Multiplicity(2, 2))
    }
)
connector59: BinaryAssociation = BinaryAssociation(
    name="connector59",
    ends={
        Property(name="rtsc_Connector", type=rtsc_CoordinationProtocol, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_CoordinationProtocol60", type=rtsc_Connector, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type61: BinaryAssociation = BinaryAssociation(
    name="type61",
    ends={
        Property(name="rtsc_MessageType63", type=rtsc_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Message62", type=rtsc_MessageType, multiplicity=Multiplicity(1, 1))
    }
)
statecharts64: BinaryAssociation = BinaryAssociation(
    name="statecharts64",
    ends={
        Property(name="rtsc_Realtimestatechart65", type=rtsc_System, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_System", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
protocol66: BinaryAssociation = BinaryAssociation(
    name="protocol66",
    ends={
        Property(name="rtsc_CoordinationProtocol68", type=rtsc_System, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_System67", type=rtsc_CoordinationProtocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageTypeRepo69: BinaryAssociation = BinaryAssociation(
    name="messageTypeRepo69",
    ends={
        Property(name="rtsc_MessageTypeRepository", type=rtsc_System, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_System70", type=rtsc_MessageTypeRepository, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
messageTypes71: BinaryAssociation = BinaryAssociation(
    name="messageTypes71",
    ends={
        Property(name="rtsc_MessageType73", type=rtsc_MessageTypeRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_MessageTypeRepository72", type=rtsc_MessageType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clock76: BinaryAssociation = BinaryAssociation(
    name="clock76",
    ends={
        Property(name="rtsc_Clock77", type=rtsc_ClockResetEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_ClockResetEvent", type=rtsc_Clock, multiplicity=Multiplicity(1, 1))
    }
)
variable78: BinaryAssociation = BinaryAssociation(
    name="variable78",
    ends={
        Property(name="rtsc_Variable79", type=rtsc_VariableAssignmentEvent, multiplicity=Multiplicity(1, 1)),
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
gen_rtsc_Variable_NamedElement = Generalization(general=NamedElement, specific=rtsc_Variable)
gen_rtsc_Clock_NamedElement = Generalization(general=NamedElement, specific=rtsc_Clock)
gen_rtsc_Port_BehavioralElement = Generalization(general=BehavioralElement, specific=rtsc_Port)
gen_rtsc_CoordinationProtocol_NamedElement = Generalization(general=NamedElement, specific=rtsc_CoordinationProtocol)
gen_rtsc_MessageType_NamedElement = Generalization(general=NamedElement, specific=rtsc_MessageType)
gen_rtsc_MessageEvent_Event = Generalization(general=Event, specific=rtsc_MessageEvent)
gen_rtsc_ClockResetEvent_Event = Generalization(general=Event, specific=rtsc_ClockResetEvent)
gen_rtsc_VariableAssignmentEvent_Event = Generalization(general=Event, specific=rtsc_VariableAssignmentEvent)

# Domain Model
domain_model = DomainModel(
    name="rtsc",
    types={rtsc_Variable, rtsc_Behavior, rtsc_Clock, rtsc_BehavioralElement, NamedElement, rtsc_Realtimestatechart, Behavior, rtsc_Transition, rtsc_State, rtsc_ClockConstraint, rtsc_MessageType, Vertex, rtsc_Event, rtsc_Guard, rtsc_MessageBuffer, rtsc_Connector, rtsc_NamedElement, rtsc_Vertex, rtsc_Port, BehavioralElement, rtsc_Message, rtsc_CoordinationProtocol, rtsc_System, rtsc_MessageTypeRepository, rtsc_MessageEvent, Event, rtsc_ClockResetEvent, rtsc_VariableAssignmentEvent},
    associations={behaviouralElement0, variables5, clocks7, behavior1, transitions2, states3, initialState4, clockConstraints30, statechart32, triggerMessage34, activeTransitions9, subStatecharts11, owningRTSC14, incomingTransitions15, outgoingTransitions17, entryEvents19, exitEvents21, source24, target26, guards28, behaviour47, incomingBuffer48, connector49, events36, variable39, clock41, statechart43, statechart45, messageType74, port50, types51, allMessages53, endpoints55, ports57, connector59, type61, statecharts64, protocol66, messageTypeRepo69, messageTypes71, clock76, variable78},
    generalizations={gen_rtsc_BehavioralElement_NamedElement, gen_rtsc_Realtimestatechart_Behavior, gen_rtsc_Realtimestatechart_NamedElement, gen_rtsc_State_Vertex, gen_rtsc_State_NamedElement, gen_rtsc_Transition_NamedElement, gen_rtsc_Variable_NamedElement, gen_rtsc_Clock_NamedElement, gen_rtsc_Port_BehavioralElement, gen_rtsc_CoordinationProtocol_NamedElement, gen_rtsc_MessageType_NamedElement, gen_rtsc_MessageEvent_Event, gen_rtsc_ClockResetEvent_Event, gen_rtsc_VariableAssignmentEvent_Event},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)