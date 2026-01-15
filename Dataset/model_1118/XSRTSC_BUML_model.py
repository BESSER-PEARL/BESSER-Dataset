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
rtsc_Clock = Class(name="rtsc::Clock")
Vertex = Class(name="Vertex")
rtsc_Realtimestatechart = Class(name="rtsc::Realtimestatechart")
Behavior = Class(name="Behavior")
rtsc_Transition = Class(name="rtsc::Transition")
rtsc_State = Class(name="rtsc::State")
rtsc_Variable = Class(name="rtsc::Variable")
rtsc_Event = Class(name="rtsc::Event", is_abstract=True)
rtsc_Guard = Class(name="rtsc::Guard")
rtsc_ClockConstraint = Class(name="rtsc::ClockConstraint")
rtsc_MessageType = Class(name="rtsc::MessageType")
rtsc_NamedElement = Class(name="rtsc::NamedElement", is_abstract=True)
rtsc_Vertex = Class(name="rtsc::Vertex")
rtsc_Message = Class(name="rtsc::Message")
rtsc_CoordinationProtocol = Class(name="rtsc::CoordinationProtocol")
rtsc_Port = Class(name="rtsc::Port")
BehavioralElement = Class(name="BehavioralElement")
rtsc_MessageBuffer = Class(name="rtsc::MessageBuffer")
rtsc_Connector = Class(name="rtsc::Connector")
rtsc_MessageEvent = Class(name="rtsc::MessageEvent")
Event = Class(name="Event")
rtsc_ClockResetEvent = Class(name="rtsc::ClockResetEvent")
rtsc_VariableAssignmentEvent = Class(name="rtsc::VariableAssignmentEvent")
rtsc_System = Class(name="rtsc::System")
rtsc_MessageTypeRepository = Class(name="rtsc::MessageTypeRepository")

# rtsc_Behavior class attributes and methods

# rtsc_BehavioralElement class attributes and methods

# NamedElement class attributes and methods

# rtsc_Clock class attributes and methods
rtsc_Clock_uClock: Property = Property(name="uClock", type=BooleanType)
rtsc_Clock_m_initialize: Method = Method(name="initialize", parameters={})
rtsc_Clock_m_printValue: Method = Method(name="printValue", parameters={})
rtsc_Clock_m_reset: Method = Method(name="reset", parameters={})
rtsc_Clock.attributes={rtsc_Clock_uClock}
rtsc_Clock.methods={rtsc_Clock_m_reset, rtsc_Clock_m_initialize, rtsc_Clock_m_printValue}

# Vertex class attributes and methods

# rtsc_Realtimestatechart class attributes and methods
rtsc_Realtimestatechart_rounds: Property = Property(name="rounds", type=IntegerType)
rtsc_Realtimestatechart_m_main: Method = Method(name="main", parameters={})
rtsc_Realtimestatechart_m_initialize: Method = Method(name="initialize", parameters={Parameter(name='args')})
rtsc_Realtimestatechart_m_step: Method = Method(name="step", parameters={})
rtsc_Realtimestatechart_m_sequentialStep: Method = Method(name="sequentialStep", parameters={})
rtsc_Realtimestatechart.attributes={rtsc_Realtimestatechart_rounds}
rtsc_Realtimestatechart.methods={rtsc_Realtimestatechart_m_initialize, rtsc_Realtimestatechart_m_main, rtsc_Realtimestatechart_m_step, rtsc_Realtimestatechart_m_sequentialStep}

# Behavior class attributes and methods

# rtsc_Transition class attributes and methods
rtsc_Transition_hitCount: Property = Property(name="hitCount", type=IntegerType)
rtsc_Transition_m_clocksHold: Method = Method(name="clocksHold", parameters={})
rtsc_Transition_m_checkMessages: Method = Method(name="checkMessages", parameters={})
rtsc_Transition_m_canFire: Method = Method(name="canFire", parameters={})
rtsc_Transition_m_fire: Method = Method(name="fire", parameters={}, type=Vertex)
rtsc_Transition_m_guardsHold: Method = Method(name="guardsHold", parameters={})
rtsc_Transition_m_consumeMessages: Method = Method(name="consumeMessages", parameters={})
rtsc_Transition.attributes={rtsc_Transition_hitCount}
rtsc_Transition.methods={rtsc_Transition_m_consumeMessages, rtsc_Transition_m_fire, rtsc_Transition_m_canFire, rtsc_Transition_m_checkMessages, rtsc_Transition_m_guardsHold, rtsc_Transition_m_clocksHold}

# rtsc_State class attributes and methods
rtsc_State_initial: Property = Property(name="initial", type=BooleanType)
rtsc_State_final: Property = Property(name="final", type=BooleanType)
rtsc_State_m_entry: Method = Method(name="entry", parameters={})
rtsc_State_m_exit: Method = Method(name="exit", parameters={})
rtsc_State.attributes={rtsc_State_final, rtsc_State_initial}
rtsc_State.methods={rtsc_State_m_entry, rtsc_State_m_exit}

# rtsc_Variable class attributes and methods
rtsc_Variable_initialValue: Property = Property(name="initialValue", type=StringType)
rtsc_Variable_runtimeValue: Property = Property(name="runtimeValue", type=StringType)
rtsc_Variable.attributes={rtsc_Variable_initialValue, rtsc_Variable_runtimeValue}

# rtsc_Event class attributes and methods
rtsc_Event_m_execute: Method = Method(name="execute", parameters={})
rtsc_Event.methods={rtsc_Event_m_execute}

# rtsc_Guard class attributes and methods
rtsc_Guard_value: Property = Property(name="value", type=BooleanType)
rtsc_Guard_m_evaluate: Method = Method(name="evaluate", parameters={})
rtsc_Guard.attributes={rtsc_Guard_value}
rtsc_Guard.methods={rtsc_Guard_m_evaluate}

# rtsc_ClockConstraint class attributes and methods
rtsc_ClockConstraint_bound: Property = Property(name="bound", type=IntegerType)
rtsc_ClockConstraint_m_apply: Method = Method(name="apply", parameters={Parameter(name='federation')})
rtsc_ClockConstraint_m_evaluate: Method = Method(name="evaluate", parameters={Parameter(name='checkFederation')})
rtsc_ClockConstraint.attributes={rtsc_ClockConstraint_bound}
rtsc_ClockConstraint.methods={rtsc_ClockConstraint_m_evaluate, rtsc_ClockConstraint_m_apply}

# rtsc_MessageType class attributes and methods

# rtsc_NamedElement class attributes and methods
rtsc_NamedElement_name: Property = Property(name="name", type=StringType)
rtsc_NamedElement.attributes={rtsc_NamedElement_name}

# rtsc_Vertex class attributes and methods
rtsc_Vertex_active: Property = Property(name="active", type=BooleanType)
rtsc_Vertex.attributes={rtsc_Vertex_active}

# rtsc_Message class attributes and methods

# rtsc_CoordinationProtocol class attributes and methods
rtsc_CoordinationProtocol_m_main: Method = Method(name="main", parameters={})
rtsc_CoordinationProtocol_m_initialize: Method = Method(name="initialize", parameters={Parameter(name='arguments')})
rtsc_CoordinationProtocol_m_step: Method = Method(name="step", parameters={})
rtsc_CoordinationProtocol.methods={rtsc_CoordinationProtocol_m_initialize, rtsc_CoordinationProtocol_m_step, rtsc_CoordinationProtocol_m_main}

# rtsc_Port class attributes and methods

# BehavioralElement class attributes and methods

# rtsc_MessageBuffer class attributes and methods
rtsc_MessageBuffer_m_hasMessage: Method = Method(name="hasMessage", parameters={Parameter(name='type')})
rtsc_MessageBuffer_m_addMessage: Method = Method(name="addMessage", parameters={Parameter(name='message')})
rtsc_MessageBuffer_m_getMessage: Method = Method(name="getMessage", parameters={Parameter(name='type')}, type=StringType)
rtsc_MessageBuffer.methods={rtsc_MessageBuffer_m_hasMessage, rtsc_MessageBuffer_m_addMessage, rtsc_MessageBuffer_m_getMessage}

# rtsc_Connector class attributes and methods

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

# rtsc_System class attributes and methods

# rtsc_MessageTypeRepository class attributes and methods

# Relationships
behaviouralElement0: BinaryAssociation = BinaryAssociation(
    name="behaviouralElement0",
    ends={
        Property(name="1", type=rtsc_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=rtsc_BehavioralElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
clocks15: BinaryAssociation = BinaryAssociation(
    name="clocks15",
    ends={
        Property(name="17", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(1, 1)),
        Property(name="16", type=rtsc_Clock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activeTransitions18: BinaryAssociation = BinaryAssociation(
    name="activeTransitions18",
    ends={
        Property(name="rtsc_Transition", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Realtimestatechart19", type=rtsc_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
subStatecharts20: BinaryAssociation = BinaryAssociation(
    name="subStatecharts20",
    ends={
        Property(name="rtsc_Realtimestatechart22", type=rtsc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_State21", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
owningRTSC23: BinaryAssociation = BinaryAssociation(
    name="owningRTSC23",
    ends={
        Property(name="25", type=rtsc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="24", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(1, 1))
    }
)
incomingTransitions26: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions26",
    ends={
        Property(name="28", type=rtsc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="27", type=rtsc_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingTransitions29: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions29",
    ends={
        Property(name="31", type=rtsc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="30", type=rtsc_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
entryEvents32: BinaryAssociation = BinaryAssociation(
    name="entryEvents32",
    ends={
        Property(name="rtsc_Event", type=rtsc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_State33", type=rtsc_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exitEvents34: BinaryAssociation = BinaryAssociation(
    name="exitEvents34",
    ends={
        Property(name="rtsc_Event36", type=rtsc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_State35", type=rtsc_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source37: BinaryAssociation = BinaryAssociation(
    name="source37",
    ends={
        Property(name="39", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="38", type=rtsc_State, multiplicity=Multiplicity(1, 1))
    }
)
target40: BinaryAssociation = BinaryAssociation(
    name="target40",
    ends={
        Property(name="42", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="41", type=rtsc_State, multiplicity=Multiplicity(1, 1))
    }
)
guards43: BinaryAssociation = BinaryAssociation(
    name="guards43",
    ends={
        Property(name="rtsc_Guard", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Transition44", type=rtsc_Guard, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clockConstraints45: BinaryAssociation = BinaryAssociation(
    name="clockConstraints45",
    ends={
        Property(name="rtsc_ClockConstraint", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Transition46", type=rtsc_ClockConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clock57: BinaryAssociation = BinaryAssociation(
    name="clock57",
    ends={
        Property(name="rtsc_Clock", type=rtsc_ClockConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_ClockConstraint58", type=rtsc_Clock, multiplicity=Multiplicity(1, 1))
    }
)
statechart59: BinaryAssociation = BinaryAssociation(
    name="statechart59",
    ends={
        Property(name="61", type=rtsc_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="60", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(0, 1))
    }
)
statechart47: BinaryAssociation = BinaryAssociation(
    name="statechart47",
    ends={
        Property(name="49", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="48", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(1, 1))
    }
)
triggerMessage50: BinaryAssociation = BinaryAssociation(
    name="triggerMessage50",
    ends={
        Property(name="rtsc_MessageType", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Transition51", type=rtsc_MessageType, multiplicity=Multiplicity(0, 9999))
    }
)
events52: BinaryAssociation = BinaryAssociation(
    name="events52",
    ends={
        Property(name="rtsc_Event54", type=rtsc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Transition53", type=rtsc_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable55: BinaryAssociation = BinaryAssociation(
    name="variable55",
    ends={
        Property(name="rtsc_Variable", type=rtsc_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Guard56", type=rtsc_Variable, multiplicity=Multiplicity(0, 1))
    }
)
port72: BinaryAssociation = BinaryAssociation(
    name="port72",
    ends={
        Property(name="74", type=rtsc_MessageBuffer, multiplicity=Multiplicity(1, 1)),
        Property(name="73", type=rtsc_Port, multiplicity=Multiplicity(1, 1))
    }
)
types75: BinaryAssociation = BinaryAssociation(
    name="types75",
    ends={
        Property(name="rtsc_MessageType76", type=rtsc_MessageBuffer, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_MessageBuffer", type=rtsc_MessageType, multiplicity=Multiplicity(1, 9999))
    }
)
allMessages77: BinaryAssociation = BinaryAssociation(
    name="allMessages77",
    ends={
        Property(name="rtsc_Message", type=rtsc_MessageBuffer, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_MessageBuffer78", type=rtsc_Message, multiplicity=Multiplicity(0, 9999))
    }
)
endpoints79: BinaryAssociation = BinaryAssociation(
    name="endpoints79",
    ends={
        Property(name="81", type=rtsc_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="80", type=rtsc_Port, multiplicity=Multiplicity(2, 2))
    }
)
statechart62: BinaryAssociation = BinaryAssociation(
    name="statechart62",
    ends={
        Property(name="64", type=rtsc_Clock, multiplicity=Multiplicity(1, 1)),
        Property(name="63", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(1, 1))
    }
)
behaviour65: BinaryAssociation = BinaryAssociation(
    name="behaviour65",
    ends={
        Property(name="rtsc_Behavior", type=rtsc_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Port", type=rtsc_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
incomingBuffer66: BinaryAssociation = BinaryAssociation(
    name="incomingBuffer66",
    ends={
        Property(name="68", type=rtsc_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="67", type=rtsc_MessageBuffer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connector69: BinaryAssociation = BinaryAssociation(
    name="connector69",
    ends={
        Property(name="71", type=rtsc_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="70", type=rtsc_Connector, multiplicity=Multiplicity(0, 1))
    }
)
messageTypes96: BinaryAssociation = BinaryAssociation(
    name="messageTypes96",
    ends={
        Property(name="rtsc_MessageType98", type=rtsc_MessageTypeRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_MessageTypeRepository97", type=rtsc_MessageType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageType99: BinaryAssociation = BinaryAssociation(
    name="messageType99",
    ends={
        Property(name="rtsc_MessageType100", type=rtsc_MessageEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_MessageEvent", type=rtsc_MessageType, multiplicity=Multiplicity(1, 1))
    }
)
clock101: BinaryAssociation = BinaryAssociation(
    name="clock101",
    ends={
        Property(name="rtsc_Clock102", type=rtsc_ClockResetEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_ClockResetEvent", type=rtsc_Clock, multiplicity=Multiplicity(1, 1))
    }
)
ports82: BinaryAssociation = BinaryAssociation(
    name="ports82",
    ends={
        Property(name="rtsc_Port83", type=rtsc_CoordinationProtocol, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_CoordinationProtocol", type=rtsc_Port, multiplicity=Multiplicity(2, 2))
    }
)
connector84: BinaryAssociation = BinaryAssociation(
    name="connector84",
    ends={
        Property(name="rtsc_Connector", type=rtsc_CoordinationProtocol, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_CoordinationProtocol85", type=rtsc_Connector, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type86: BinaryAssociation = BinaryAssociation(
    name="type86",
    ends={
        Property(name="rtsc_MessageType88", type=rtsc_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_Message87", type=rtsc_MessageType, multiplicity=Multiplicity(1, 1))
    }
)
statecharts89: BinaryAssociation = BinaryAssociation(
    name="statecharts89",
    ends={
        Property(name="rtsc_Realtimestatechart90", type=rtsc_System, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_System", type=rtsc_Realtimestatechart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
protocol91: BinaryAssociation = BinaryAssociation(
    name="protocol91",
    ends={
        Property(name="rtsc_CoordinationProtocol93", type=rtsc_System, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_System92", type=rtsc_CoordinationProtocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageTypeRepo94: BinaryAssociation = BinaryAssociation(
    name="messageTypeRepo94",
    ends={
        Property(name="rtsc_MessageTypeRepository", type=rtsc_System, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_System95", type=rtsc_MessageTypeRepository, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable103: BinaryAssociation = BinaryAssociation(
    name="variable103",
    ends={
        Property(name="rtsc_Variable104", type=rtsc_VariableAssignmentEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="rtsc_VariableAssignmentEvent", type=rtsc_Variable, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_rtsc_BehavioralElement_NamedElement = Generalization(general=NamedElement, specific=rtsc_BehavioralElement)
gen_rtsc_State_Vertex = Generalization(general=Vertex, specific=rtsc_State)
gen_rtsc_State_NamedElement = Generalization(general=NamedElement, specific=rtsc_State)
gen_rtsc_Realtimestatechart_Behavior = Generalization(general=Behavior, specific=rtsc_Realtimestatechart)
gen_rtsc_Realtimestatechart_NamedElement = Generalization(general=NamedElement, specific=rtsc_Realtimestatechart)
gen_rtsc_Transition_NamedElement = Generalization(general=NamedElement, specific=rtsc_Transition)
gen_rtsc_Variable_NamedElement = Generalization(general=NamedElement, specific=rtsc_Variable)
gen_rtsc_CoordinationProtocol_NamedElement = Generalization(general=NamedElement, specific=rtsc_CoordinationProtocol)
gen_rtsc_Clock_NamedElement = Generalization(general=NamedElement, specific=rtsc_Clock)
gen_rtsc_Port_BehavioralElement = Generalization(general=BehavioralElement, specific=rtsc_Port)
gen_rtsc_MessageEvent_Event = Generalization(general=Event, specific=rtsc_MessageEvent)
gen_rtsc_ClockResetEvent_Event = Generalization(general=Event, specific=rtsc_ClockResetEvent)
gen_rtsc_VariableAssignmentEvent_Event = Generalization(general=Event, specific=rtsc_VariableAssignmentEvent)
gen_rtsc_MessageType_NamedElement = Generalization(general=NamedElement, specific=rtsc_MessageType)

# Domain Model
domain_model = DomainModel(
    name="rtsc",
    types={rtsc_Behavior, rtsc_BehavioralElement, NamedElement, rtsc_Clock, Vertex, rtsc_Realtimestatechart, Behavior, rtsc_Transition, rtsc_State, rtsc_Variable, rtsc_Event, rtsc_Guard, rtsc_ClockConstraint, rtsc_MessageType, rtsc_NamedElement, rtsc_Vertex, rtsc_Message, rtsc_CoordinationProtocol, rtsc_Port, BehavioralElement, rtsc_MessageBuffer, rtsc_Connector, rtsc_MessageEvent, Event, rtsc_ClockResetEvent, rtsc_VariableAssignmentEvent, rtsc_System, rtsc_MessageTypeRepository},
    associations={behaviouralElement0, clocks15, activeTransitions18, subStatecharts20, behavior2, transitions5, states8, initialState11, variables12, owningRTSC23, incomingTransitions26, outgoingTransitions29, entryEvents32, exitEvents34, source37, target40, guards43, clockConstraints45, clock57, statechart59, statechart47, triggerMessage50, events52, variable55, port72, types75, allMessages77, endpoints79, statechart62, behaviour65, incomingBuffer66, connector69, messageTypes96, messageType99, clock101, ports82, connector84, type86, statecharts89, protocol91, messageTypeRepo94, variable103},
    generalizations={gen_rtsc_BehavioralElement_NamedElement, gen_rtsc_State_Vertex, gen_rtsc_State_NamedElement, gen_rtsc_Realtimestatechart_Behavior, gen_rtsc_Realtimestatechart_NamedElement, gen_rtsc_Transition_NamedElement, gen_rtsc_Variable_NamedElement, gen_rtsc_CoordinationProtocol_NamedElement, gen_rtsc_Clock_NamedElement, gen_rtsc_Port_BehavioralElement, gen_rtsc_MessageEvent_Event, gen_rtsc_ClockResetEvent_Event, gen_rtsc_VariableAssignmentEvent_Event, gen_rtsc_MessageType_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)