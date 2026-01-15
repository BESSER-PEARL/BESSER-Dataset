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
PseudostateKind: Enumeration = Enumeration(
    name="PseudostateKind",
    literals={
            EnumerationLiteral(name="fork"),
			EnumerationLiteral(name="junction"),
			EnumerationLiteral(name="choice"),
			EnumerationLiteral(name="initial"),
			EnumerationLiteral(name="join")
    }
)

# Classes
StateMachine = Class(name="StateMachine")
statemachines_CustomEvent = Class(name="statemachines::CustomEvent")
Event = Class(name="Event")
statemachines_CustomSystem = Class(name="statemachines::CustomSystem")
Behavior = Class(name="Behavior")
statemachines_almostuml_Vertex = Class(name="statemachines::almostuml::Vertex", is_abstract=True)
statemachines_EventOccurrence = Class(name="statemachines::EventOccurrence")
statemachines_Util = Class(name="statemachines::Util")
statemachines_almostuml_StateMachine = Class(name="statemachines::almostuml::StateMachine")
NamedElement = Class(name="NamedElement")
Region = Class(name="Region")
almostuml_statemachines_EventOccurrence = Class(name="almostuml::statemachines::EventOccurrence")
statemachines_almostuml_Region = Class(name="statemachines::almostuml::Region")
Vertex = Class(name="Vertex")
Transition = Class(name="Transition")
State = Class(name="State")
statemachines_almostuml_State = Class(name="statemachines::almostuml::State")
almostuml_NamedElement = Class(name="almostuml::NamedElement")
almostuml_Vertex = Class(name="almostuml::Vertex")
statemachines_almostuml_Transition = Class(name="statemachines::almostuml::Transition")
Trigger = Class(name="Trigger")
Constraint = Class(name="Constraint")
statemachines_almostuml_Trigger = Class(name="statemachines::almostuml::Trigger")
statemachines_almostuml_Constraint = Class(name="statemachines::almostuml::Constraint", is_abstract=True)
statemachines_almostuml_Behavior = Class(name="statemachines::almostuml::Behavior", is_abstract=True)
statemachines_almostuml_NamedElement = Class(name="statemachines::almostuml::NamedElement", is_abstract=True)
statemachines_almostuml_Event = Class(name="statemachines::almostuml::Event", is_abstract=True)
statemachines_almostuml_FinalState = Class(name="statemachines::almostuml::FinalState")
statemachines_almostuml_Pseudostate = Class(name="statemachines::almostuml::Pseudostate")

# StateMachine class attributes and methods

# statemachines_CustomEvent class attributes and methods

# Event class attributes and methods

# statemachines_CustomSystem class attributes and methods
statemachines_CustomSystem_m_main: Method = Method(name="main", parameters={})
statemachines_CustomSystem_m_initialize: Method = Method(name="initialize", parameters={Parameter(name='args')})
statemachines_CustomSystem.methods={statemachines_CustomSystem_m_main, statemachines_CustomSystem_m_initialize}

# Behavior class attributes and methods

# statemachines_almostuml_Vertex class attributes and methods

# statemachines_EventOccurrence class attributes and methods

# statemachines_Util class attributes and methods
statemachines_Util_m_log: Method = Method(name="log", parameters={Parameter(name='l')})
statemachines_Util.methods={statemachines_Util_m_log}

# statemachines_almostuml_StateMachine class attributes and methods
statemachines_almostuml_StateMachine_m_run: Method = Method(name="run", parameters={})
statemachines_almostuml_StateMachine.methods={statemachines_almostuml_StateMachine_m_run}

# NamedElement class attributes and methods

# Region class attributes and methods

# almostuml_statemachines_EventOccurrence class attributes and methods

# statemachines_almostuml_Region class attributes and methods
statemachines_almostuml_Region_m_initialize: Method = Method(name="initialize", parameters={})
statemachines_almostuml_Region_m_handleEvent: Method = Method(name="handleEvent", parameters={Parameter(name='eventOccurrence')})
statemachines_almostuml_Region.methods={statemachines_almostuml_Region_m_initialize, statemachines_almostuml_Region_m_handleEvent}

# Vertex class attributes and methods

# Transition class attributes and methods

# State class attributes and methods

# statemachines_almostuml_State class attributes and methods
statemachines_almostuml_State_m_handle: Method = Method(name="handle", parameters={Parameter(name='eventOccurrence')})
statemachines_almostuml_State_m_setAsCurrent: Method = Method(name="setAsCurrent", parameters={})
statemachines_almostuml_State.methods={statemachines_almostuml_State_m_handle, statemachines_almostuml_State_m_setAsCurrent}

# almostuml_NamedElement class attributes and methods

# almostuml_Vertex class attributes and methods

# statemachines_almostuml_Transition class attributes and methods
statemachines_almostuml_Transition_m_fire: Method = Method(name="fire", parameters={})
statemachines_almostuml_Transition.methods={statemachines_almostuml_Transition_m_fire}

# Trigger class attributes and methods

# Constraint class attributes and methods

# statemachines_almostuml_Trigger class attributes and methods

# statemachines_almostuml_Constraint class attributes and methods

# statemachines_almostuml_Behavior class attributes and methods

# statemachines_almostuml_NamedElement class attributes and methods
statemachines_almostuml_NamedElement_name: Property = Property(name="name", type=StringType)
statemachines_almostuml_NamedElement.attributes={statemachines_almostuml_NamedElement_name}

# statemachines_almostuml_Event class attributes and methods

# statemachines_almostuml_FinalState class attributes and methods
statemachines_almostuml_FinalState_m_handle: Method = Method(name="handle", parameters={Parameter(name='eventOccurrence')})
statemachines_almostuml_FinalState.methods={statemachines_almostuml_FinalState_m_handle}

# statemachines_almostuml_Pseudostate class attributes and methods
statemachines_almostuml_Pseudostate_kind: Property = Property(name="kind", type=StringType)
statemachines_almostuml_Pseudostate.attributes={statemachines_almostuml_Pseudostate_kind}

# Relationships
statemachine0: BinaryAssociation = BinaryAssociation(
    name="statemachine0",
    ends={
        Property(name="StateMachine", type=statemachines_CustomSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_CustomSystem", type=StateMachine, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
events1: BinaryAssociation = BinaryAssociation(
    name="events1",
    ends={
        Property(name="statemachines_CustomEvent", type=statemachines_CustomSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_CustomSystem2", type=statemachines_CustomEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entry17: BinaryAssociation = BinaryAssociation(
    name="entry17",
    ends={
        Property(name="Behavior", type=statemachines_almostuml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_State", type=Behavior, multiplicity=Multiplicity(0, 1))
    }
)
exit18: BinaryAssociation = BinaryAssociation(
    name="exit18",
    ends={
        Property(name="Behavior20", type=statemachines_almostuml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_State19", type=Behavior, multiplicity=Multiplicity(0, 1))
    }
)
doActivity21: BinaryAssociation = BinaryAssociation(
    name="doActivity21",
    ends={
        Property(name="Behavior23", type=statemachines_almostuml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_State22", type=Behavior, multiplicity=Multiplicity(0, 1))
    }
)
region24: BinaryAssociation = BinaryAssociation(
    name="region24",
    ends={
        Property(name="Region", type=statemachines_almostuml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_State25", type=Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container26: BinaryAssociation = BinaryAssociation(
    name="container26",
    ends={
        Property(name="28", type=statemachines_almostuml_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="27", type=Region, multiplicity=Multiplicity(0, 1))
    }
)
event3: BinaryAssociation = BinaryAssociation(
    name="event3",
    ends={
        Property(name="statemachines_CustomEvent4", type=statemachines_EventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_EventOccurrence", type=statemachines_CustomEvent, multiplicity=Multiplicity(1, 1))
    }
)
region5: BinaryAssociation = BinaryAssociation(
    name="region5",
    ends={
        Property(name="6", type=statemachines_almostuml_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
queue7: BinaryAssociation = BinaryAssociation(
    name="queue7",
    ends={
        Property(name="almostuml_statemachines_EventOccurrence", type=statemachines_almostuml_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_StateMachine", type=almostuml_statemachines_EventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subvertex8: BinaryAssociation = BinaryAssociation(
    name="subvertex8",
    ends={
        Property(name="10", type=statemachines_almostuml_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="9", type=Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition11: BinaryAssociation = BinaryAssociation(
    name="transition11",
    ends={
        Property(name="Transition", type=statemachines_almostuml_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_Region", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine12: BinaryAssociation = BinaryAssociation(
    name="stateMachine12",
    ends={
        Property(name="14", type=statemachines_almostuml_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="13", type=StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
currentState15: BinaryAssociation = BinaryAssociation(
    name="currentState15",
    ends={
        Property(name="State", type=statemachines_almostuml_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_Region16", type=State, multiplicity=Multiplicity(0, 1))
    }
)
source29: BinaryAssociation = BinaryAssociation(
    name="source29",
    ends={
        Property(name="Vertex", type=statemachines_almostuml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_Transition", type=Vertex, multiplicity=Multiplicity(1, 1))
    }
)
target30: BinaryAssociation = BinaryAssociation(
    name="target30",
    ends={
        Property(name="Vertex32", type=statemachines_almostuml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_Transition31", type=Vertex, multiplicity=Multiplicity(1, 1))
    }
)
trigger33: BinaryAssociation = BinaryAssociation(
    name="trigger33",
    ends={
        Property(name="Trigger", type=statemachines_almostuml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_Transition34", type=Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard35: BinaryAssociation = BinaryAssociation(
    name="guard35",
    ends={
        Property(name="Constraint", type=statemachines_almostuml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_Transition36", type=Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
effect37: BinaryAssociation = BinaryAssociation(
    name="effect37",
    ends={
        Property(name="Behavior39", type=statemachines_almostuml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_Transition38", type=Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
event40: BinaryAssociation = BinaryAssociation(
    name="event40",
    ends={
        Property(name="Event", type=statemachines_almostuml_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_Trigger", type=Event, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_statemachines_CustomEvent_Event = Generalization(general=Event, specific=statemachines_CustomEvent)
gen_statemachines_almostuml_Vertex_NamedElement = Generalization(general=NamedElement, specific=statemachines_almostuml_Vertex)
gen_statemachines_almostuml_StateMachine_NamedElement = Generalization(general=NamedElement, specific=statemachines_almostuml_StateMachine)
gen_statemachines_almostuml_Region_NamedElement = Generalization(general=NamedElement, specific=statemachines_almostuml_Region)
gen_statemachines_almostuml_State_almostuml_NamedElement = Generalization(general=almostuml_NamedElement, specific=statemachines_almostuml_State)
gen_statemachines_almostuml_State_almostuml_Vertex = Generalization(general=almostuml_Vertex, specific=statemachines_almostuml_State)
gen_statemachines_almostuml_Transition_NamedElement = Generalization(general=NamedElement, specific=statemachines_almostuml_Transition)
gen_statemachines_almostuml_Trigger_NamedElement = Generalization(general=NamedElement, specific=statemachines_almostuml_Trigger)
gen_statemachines_almostuml_Behavior_NamedElement = Generalization(general=NamedElement, specific=statemachines_almostuml_Behavior)
gen_statemachines_almostuml_Event_NamedElement = Generalization(general=NamedElement, specific=statemachines_almostuml_Event)
gen_statemachines_almostuml_FinalState_State = Generalization(general=State, specific=statemachines_almostuml_FinalState)
gen_statemachines_almostuml_Pseudostate_State = Generalization(general=State, specific=statemachines_almostuml_Pseudostate)

# Domain Model
domain_model = DomainModel(
    name="statemachines",
    types={StateMachine, statemachines_CustomEvent, Event, statemachines_CustomSystem, Behavior, statemachines_almostuml_Vertex, statemachines_EventOccurrence, statemachines_Util, statemachines_almostuml_StateMachine, NamedElement, Region, almostuml_statemachines_EventOccurrence, statemachines_almostuml_Region, Vertex, Transition, State, statemachines_almostuml_State, almostuml_NamedElement, almostuml_Vertex, statemachines_almostuml_Transition, Trigger, Constraint, statemachines_almostuml_Trigger, statemachines_almostuml_Constraint, statemachines_almostuml_Behavior, statemachines_almostuml_NamedElement, statemachines_almostuml_Event, statemachines_almostuml_FinalState, statemachines_almostuml_Pseudostate, PseudostateKind},
    associations={statemachine0, events1, entry17, exit18, doActivity21, region24, container26, event3, region5, queue7, subvertex8, transition11, stateMachine12, currentState15, source29, target30, trigger33, guard35, effect37, event40},
    generalizations={gen_statemachines_CustomEvent_Event, gen_statemachines_almostuml_Vertex_NamedElement, gen_statemachines_almostuml_StateMachine_NamedElement, gen_statemachines_almostuml_Region_NamedElement, gen_statemachines_almostuml_State_almostuml_NamedElement, gen_statemachines_almostuml_State_almostuml_Vertex, gen_statemachines_almostuml_Transition_NamedElement, gen_statemachines_almostuml_Trigger_NamedElement, gen_statemachines_almostuml_Behavior_NamedElement, gen_statemachines_almostuml_Event_NamedElement, gen_statemachines_almostuml_FinalState_State, gen_statemachines_almostuml_Pseudostate_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)