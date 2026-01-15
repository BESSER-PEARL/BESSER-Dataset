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
            EnumerationLiteral(name="initial"),
			EnumerationLiteral(name="join"),
			EnumerationLiteral(name="fork"),
			EnumerationLiteral(name="junction"),
			EnumerationLiteral(name="choice")
    }
)

# Classes
statemachines_CustomEvent = Class(name="statemachines::CustomEvent")
Event = Class(name="Event")
statemachines_almostuml_StateMachine = Class(name="statemachines::almostuml::StateMachine")
NamedElement = Class(name="NamedElement")
Region = Class(name="Region")
statemachines_almostuml_Region = Class(name="statemachines::almostuml::Region")
Vertex = Class(name="Vertex")
Transition = Class(name="Transition")
statemachines_CustomSystem = Class(name="statemachines::CustomSystem")
StateMachine = Class(name="StateMachine")
statemachines_almostuml_Vertex = Class(name="statemachines::almostuml::Vertex", is_abstract=True)
statemachines_almostuml_Transition = Class(name="statemachines::almostuml::Transition")
Trigger = Class(name="Trigger")
statemachines_almostuml_State = Class(name="statemachines::almostuml::State")
almostuml_NamedElement = Class(name="almostuml::NamedElement")
almostuml_Vertex = Class(name="almostuml::Vertex")
Behavior = Class(name="Behavior")
statemachines_almostuml_Trigger = Class(name="statemachines::almostuml::Trigger")
statemachines_almostuml_Constraint = Class(name="statemachines::almostuml::Constraint", is_abstract=True)
statemachines_almostuml_Behavior = Class(name="statemachines::almostuml::Behavior", is_abstract=True)
statemachines_almostuml_NamedElement = Class(name="statemachines::almostuml::NamedElement", is_abstract=True)
statemachines_almostuml_Event = Class(name="statemachines::almostuml::Event", is_abstract=True)
statemachines_almostuml_FinalState = Class(name="statemachines::almostuml::FinalState")
State = Class(name="State")
statemachines_almostuml_Pseudostate = Class(name="statemachines::almostuml::Pseudostate")
Constraint = Class(name="Constraint")

# statemachines_CustomEvent class attributes and methods

# Event class attributes and methods

# statemachines_almostuml_StateMachine class attributes and methods

# NamedElement class attributes and methods

# Region class attributes and methods

# statemachines_almostuml_Region class attributes and methods

# Vertex class attributes and methods

# Transition class attributes and methods

# statemachines_CustomSystem class attributes and methods

# StateMachine class attributes and methods

# statemachines_almostuml_Vertex class attributes and methods

# statemachines_almostuml_Transition class attributes and methods

# Trigger class attributes and methods

# statemachines_almostuml_State class attributes and methods

# almostuml_NamedElement class attributes and methods

# almostuml_Vertex class attributes and methods

# Behavior class attributes and methods

# statemachines_almostuml_Trigger class attributes and methods

# statemachines_almostuml_Constraint class attributes and methods

# statemachines_almostuml_Behavior class attributes and methods

# statemachines_almostuml_NamedElement class attributes and methods
statemachines_almostuml_NamedElement_name: Property = Property(name="name", type=StringType)
statemachines_almostuml_NamedElement.attributes={statemachines_almostuml_NamedElement_name}

# statemachines_almostuml_Event class attributes and methods

# statemachines_almostuml_FinalState class attributes and methods

# State class attributes and methods

# statemachines_almostuml_Pseudostate class attributes and methods
statemachines_almostuml_Pseudostate_kind: Property = Property(name="kind", type=StringType)
statemachines_almostuml_Pseudostate.attributes={statemachines_almostuml_Pseudostate_kind}

# Constraint class attributes and methods

# Relationships
events1: BinaryAssociation = BinaryAssociation(
    name="events1",
    ends={
        Property(name="statemachines_CustomEvent", type=statemachines_CustomSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_CustomSystem2", type=statemachines_CustomEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
region3: BinaryAssociation = BinaryAssociation(
    name="region3",
    ends={
        Property(name="4", type=statemachines_almostuml_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
subvertex5: BinaryAssociation = BinaryAssociation(
    name="subvertex5",
    ends={
        Property(name="7", type=statemachines_almostuml_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="6", type=Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition8: BinaryAssociation = BinaryAssociation(
    name="transition8",
    ends={
        Property(name="Transition", type=statemachines_almostuml_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_Region", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine9: BinaryAssociation = BinaryAssociation(
    name="stateMachine9",
    ends={
        Property(name="11", type=statemachines_almostuml_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="10", type=StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
statemachine0: BinaryAssociation = BinaryAssociation(
    name="statemachine0",
    ends={
        Property(name="StateMachine", type=statemachines_CustomSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_CustomSystem", type=StateMachine, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exit13: BinaryAssociation = BinaryAssociation(
    name="exit13",
    ends={
        Property(name="Behavior15", type=statemachines_almostuml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_State14", type=Behavior, multiplicity=Multiplicity(0, 1))
    }
)
doActivity16: BinaryAssociation = BinaryAssociation(
    name="doActivity16",
    ends={
        Property(name="Behavior18", type=statemachines_almostuml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_State17", type=Behavior, multiplicity=Multiplicity(0, 1))
    }
)
region19: BinaryAssociation = BinaryAssociation(
    name="region19",
    ends={
        Property(name="Region", type=statemachines_almostuml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_State20", type=Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container21: BinaryAssociation = BinaryAssociation(
    name="container21",
    ends={
        Property(name="23", type=statemachines_almostuml_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="22", type=Region, multiplicity=Multiplicity(0, 1))
    }
)
source24: BinaryAssociation = BinaryAssociation(
    name="source24",
    ends={
        Property(name="Vertex", type=statemachines_almostuml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_Transition", type=Vertex, multiplicity=Multiplicity(1, 1))
    }
)
target25: BinaryAssociation = BinaryAssociation(
    name="target25",
    ends={
        Property(name="Vertex27", type=statemachines_almostuml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_Transition26", type=Vertex, multiplicity=Multiplicity(1, 1))
    }
)
trigger28: BinaryAssociation = BinaryAssociation(
    name="trigger28",
    ends={
        Property(name="Trigger", type=statemachines_almostuml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_Transition29", type=Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entry12: BinaryAssociation = BinaryAssociation(
    name="entry12",
    ends={
        Property(name="Behavior", type=statemachines_almostuml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_State", type=Behavior, multiplicity=Multiplicity(0, 1))
    }
)
event35: BinaryAssociation = BinaryAssociation(
    name="event35",
    ends={
        Property(name="Event", type=statemachines_almostuml_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_Trigger", type=Event, multiplicity=Multiplicity(1, 1))
    }
)
guard30: BinaryAssociation = BinaryAssociation(
    name="guard30",
    ends={
        Property(name="Constraint", type=statemachines_almostuml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_Transition31", type=Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
effect32: BinaryAssociation = BinaryAssociation(
    name="effect32",
    ends={
        Property(name="Behavior34", type=statemachines_almostuml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_Transition33", type=Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_statemachines_CustomEvent_Event = Generalization(general=Event, specific=statemachines_CustomEvent)
gen_statemachines_almostuml_StateMachine_NamedElement = Generalization(general=NamedElement, specific=statemachines_almostuml_StateMachine)
gen_statemachines_almostuml_Region_NamedElement = Generalization(general=NamedElement, specific=statemachines_almostuml_Region)
gen_statemachines_almostuml_Vertex_NamedElement = Generalization(general=NamedElement, specific=statemachines_almostuml_Vertex)
gen_statemachines_almostuml_Transition_NamedElement = Generalization(general=NamedElement, specific=statemachines_almostuml_Transition)
gen_statemachines_almostuml_State_almostuml_NamedElement = Generalization(general=almostuml_NamedElement, specific=statemachines_almostuml_State)
gen_statemachines_almostuml_State_almostuml_Vertex = Generalization(general=almostuml_Vertex, specific=statemachines_almostuml_State)
gen_statemachines_almostuml_Trigger_NamedElement = Generalization(general=NamedElement, specific=statemachines_almostuml_Trigger)
gen_statemachines_almostuml_Behavior_NamedElement = Generalization(general=NamedElement, specific=statemachines_almostuml_Behavior)
gen_statemachines_almostuml_Event_NamedElement = Generalization(general=NamedElement, specific=statemachines_almostuml_Event)
gen_statemachines_almostuml_FinalState_State = Generalization(general=State, specific=statemachines_almostuml_FinalState)
gen_statemachines_almostuml_Pseudostate_State = Generalization(general=State, specific=statemachines_almostuml_Pseudostate)

# Domain Model
domain_model = DomainModel(
    name="statemachines",
    types={statemachines_CustomEvent, Event, statemachines_almostuml_StateMachine, NamedElement, Region, statemachines_almostuml_Region, Vertex, Transition, statemachines_CustomSystem, StateMachine, statemachines_almostuml_Vertex, statemachines_almostuml_Transition, Trigger, statemachines_almostuml_State, almostuml_NamedElement, almostuml_Vertex, Behavior, statemachines_almostuml_Trigger, statemachines_almostuml_Constraint, statemachines_almostuml_Behavior, statemachines_almostuml_NamedElement, statemachines_almostuml_Event, statemachines_almostuml_FinalState, State, statemachines_almostuml_Pseudostate, Constraint, PseudostateKind},
    associations={events1, region3, subvertex5, transition8, stateMachine9, statemachine0, exit13, doActivity16, region19, container21, source24, target25, trigger28, entry12, event35, guard30, effect32},
    generalizations={gen_statemachines_CustomEvent_Event, gen_statemachines_almostuml_StateMachine_NamedElement, gen_statemachines_almostuml_Region_NamedElement, gen_statemachines_almostuml_Vertex_NamedElement, gen_statemachines_almostuml_Transition_NamedElement, gen_statemachines_almostuml_State_almostuml_NamedElement, gen_statemachines_almostuml_State_almostuml_Vertex, gen_statemachines_almostuml_Trigger_NamedElement, gen_statemachines_almostuml_Behavior_NamedElement, gen_statemachines_almostuml_Event_NamedElement, gen_statemachines_almostuml_FinalState_State, gen_statemachines_almostuml_Pseudostate_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)