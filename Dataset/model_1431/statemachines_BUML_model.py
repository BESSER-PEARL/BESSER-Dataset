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
statemachines_CustomSystem = Class(name="statemachines_CustomSystem")
StateMachine = Class(name="StateMachine")
statemachines_CustomEvent = Class(name="statemachines_CustomEvent")
Event = Class(name="Event")
statemachines_almostuml_StateMachine = Class(name="statemachines_almostuml_StateMachine")
NamedElement = Class(name="NamedElement")
Region = Class(name="Region")
statemachines_almostuml_Vertex = Class(name="statemachines_almostuml_Vertex", is_abstract=True)
statemachines_almostuml_Transition = Class(name="statemachines_almostuml_Transition")
Trigger = Class(name="Trigger")
statemachines_almostuml_Region = Class(name="statemachines_almostuml_Region")
Vertex = Class(name="Vertex")
Transition = Class(name="Transition")
statemachines_almostuml_State = Class(name="statemachines_almostuml_State")
almostuml_NamedElement = Class(name="almostuml_NamedElement")
almostuml_Vertex = Class(name="almostuml_Vertex")
Behavior = Class(name="Behavior")
Constraint = Class(name="Constraint")
statemachines_almostuml_Trigger = Class(name="statemachines_almostuml_Trigger")
statemachines_almostuml_Constraint = Class(name="statemachines_almostuml_Constraint", is_abstract=True)
statemachines_almostuml_Behavior = Class(name="statemachines_almostuml_Behavior", is_abstract=True)
statemachines_almostuml_NamedElement = Class(name="statemachines_almostuml_NamedElement", is_abstract=True)
statemachines_almostuml_Event = Class(name="statemachines_almostuml_Event", is_abstract=True)
statemachines_almostuml_FinalState = Class(name="statemachines_almostuml_FinalState")
State = Class(name="State")
statemachines_almostuml_Pseudostate = Class(name="statemachines_almostuml_Pseudostate")

# statemachines_CustomSystem class attributes and methods

# StateMachine class attributes and methods

# statemachines_CustomEvent class attributes and methods

# Event class attributes and methods

# statemachines_almostuml_StateMachine class attributes and methods

# NamedElement class attributes and methods

# Region class attributes and methods

# statemachines_almostuml_Vertex class attributes and methods

# statemachines_almostuml_Transition class attributes and methods

# Trigger class attributes and methods

# statemachines_almostuml_Region class attributes and methods

# Vertex class attributes and methods

# Transition class attributes and methods

# statemachines_almostuml_State class attributes and methods

# almostuml_NamedElement class attributes and methods

# almostuml_Vertex class attributes and methods

# Behavior class attributes and methods

# Constraint class attributes and methods

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
exit9: BinaryAssociation = BinaryAssociation(
    name="exit9",
    ends={
        Property(name="Behavior11", type=statemachines_almostuml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_State10", type=Behavior, multiplicity=Multiplicity(0, 1))
    }
)
doActivity12: BinaryAssociation = BinaryAssociation(
    name="doActivity12",
    ends={
        Property(name="Behavior14", type=statemachines_almostuml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_State13", type=Behavior, multiplicity=Multiplicity(0, 1))
    }
)
region15: BinaryAssociation = BinaryAssociation(
    name="region15",
    ends={
        Property(name="Region17", type=statemachines_almostuml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_State16", type=Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container18: BinaryAssociation = BinaryAssociation(
    name="container18",
    ends={
        Property(name="Region19", type=statemachines_almostuml_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="subvertex", type=Region, multiplicity=Multiplicity(0, 1))
    }
)
source20: BinaryAssociation = BinaryAssociation(
    name="source20",
    ends={
        Property(name="Vertex21", type=statemachines_almostuml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_Transition", type=Vertex, multiplicity=Multiplicity(1, 1))
    }
)
target22: BinaryAssociation = BinaryAssociation(
    name="target22",
    ends={
        Property(name="Vertex24", type=statemachines_almostuml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_Transition23", type=Vertex, multiplicity=Multiplicity(1, 1))
    }
)
trigger25: BinaryAssociation = BinaryAssociation(
    name="trigger25",
    ends={
        Property(name="Trigger", type=statemachines_almostuml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_Transition26", type=Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
region3: BinaryAssociation = BinaryAssociation(
    name="region3",
    ends={
        Property(name="Region", type=statemachines_almostuml_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
subvertex4: BinaryAssociation = BinaryAssociation(
    name="subvertex4",
    ends={
        Property(name="Vertex", type=statemachines_almostuml_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition5: BinaryAssociation = BinaryAssociation(
    name="transition5",
    ends={
        Property(name="Transition", type=statemachines_almostuml_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_Region", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine6: BinaryAssociation = BinaryAssociation(
    name="stateMachine6",
    ends={
        Property(name="StateMachine7", type=statemachines_almostuml_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="region", type=StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
entry8: BinaryAssociation = BinaryAssociation(
    name="entry8",
    ends={
        Property(name="Behavior", type=statemachines_almostuml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_State", type=Behavior, multiplicity=Multiplicity(0, 1))
    }
)
guard27: BinaryAssociation = BinaryAssociation(
    name="guard27",
    ends={
        Property(name="Constraint", type=statemachines_almostuml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_Transition28", type=Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
effect29: BinaryAssociation = BinaryAssociation(
    name="effect29",
    ends={
        Property(name="Behavior31", type=statemachines_almostuml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_Transition30", type=Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
event32: BinaryAssociation = BinaryAssociation(
    name="event32",
    ends={
        Property(name="Event", type=statemachines_almostuml_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_almostuml_Trigger", type=Event, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_statemachines_CustomEvent_Event = Generalization(general=Event, specific=statemachines_CustomEvent)
gen_statemachines_almostuml_StateMachine_NamedElement = Generalization(general=NamedElement, specific=statemachines_almostuml_StateMachine)
gen_statemachines_almostuml_Vertex_NamedElement = Generalization(general=NamedElement, specific=statemachines_almostuml_Vertex)
gen_statemachines_almostuml_Transition_NamedElement = Generalization(general=NamedElement, specific=statemachines_almostuml_Transition)
gen_statemachines_almostuml_Region_NamedElement = Generalization(general=NamedElement, specific=statemachines_almostuml_Region)
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
    types={statemachines_CustomSystem, StateMachine, statemachines_CustomEvent, Event, statemachines_almostuml_StateMachine, NamedElement, Region, statemachines_almostuml_Vertex, statemachines_almostuml_Transition, Trigger, statemachines_almostuml_Region, Vertex, Transition, statemachines_almostuml_State, almostuml_NamedElement, almostuml_Vertex, Behavior, Constraint, statemachines_almostuml_Trigger, statemachines_almostuml_Constraint, statemachines_almostuml_Behavior, statemachines_almostuml_NamedElement, statemachines_almostuml_Event, statemachines_almostuml_FinalState, State, statemachines_almostuml_Pseudostate, PseudostateKind},
    associations={statemachine0, events1, exit9, doActivity12, region15, container18, source20, target22, trigger25, region3, subvertex4, transition5, stateMachine6, entry8, guard27, effect29, event32},
    generalizations={gen_statemachines_CustomEvent_Event, gen_statemachines_almostuml_StateMachine_NamedElement, gen_statemachines_almostuml_Vertex_NamedElement, gen_statemachines_almostuml_Transition_NamedElement, gen_statemachines_almostuml_Region_NamedElement, gen_statemachines_almostuml_State_almostuml_NamedElement, gen_statemachines_almostuml_State_almostuml_Vertex, gen_statemachines_almostuml_Trigger_NamedElement, gen_statemachines_almostuml_Behavior_NamedElement, gen_statemachines_almostuml_Event_NamedElement, gen_statemachines_almostuml_FinalState_State, gen_statemachines_almostuml_Pseudostate_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)