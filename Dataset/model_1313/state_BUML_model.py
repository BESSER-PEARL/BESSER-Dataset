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
PseudoStateKind: Enumeration = Enumeration(
    name="PseudoStateKind",
    literals={
            EnumerationLiteral(name="initial"),
			EnumerationLiteral(name="deep"),
			EnumerationLiteral(name="join"),
			EnumerationLiteral(name="fork"),
			EnumerationLiteral(name="choice"),
			EnumerationLiteral(name="terminate"),
			EnumerationLiteral(name="shallow"),
			EnumerationLiteral(name="none")
    }
)

TransitionKind: Enumeration = Enumeration(
    name="TransitionKind",
    literals={
            EnumerationLiteral(name="internal"),
			EnumerationLiteral(name="local"),
			EnumerationLiteral(name="external")
    }
)

# Classes
state_Trigger = Class(name="state::Trigger")
state_Behaviour = Class(name="state::Behaviour")
state_Vertex = Class(name="state::Vertex", is_abstract=True)
state_StateMachine = Class(name="state::StateMachine")
state_Transition = Class(name="state::Transition")
state_State = Class(name="state::State")
Vertex = Class(name="Vertex")
NamedElement = Class(name="NamedElement")
state_Region = Class(name="state::Region")
state_NamedElement = Class(name="state::NamedElement", is_abstract=True)
state_Constraint = Class(name="state::Constraint")
state_StateModel = Class(name="state::StateModel")
state_PseudoState = Class(name="state::PseudoState")
state_FinalState = Class(name="state::FinalState")
State = Class(name="State")
state_OpaqueExpression = Class(name="state::OpaqueExpression")
state_Event = Class(name="state::Event")

# state_Trigger class attributes and methods

# state_Behaviour class attributes and methods
state_Behaviour_body: Property = Property(name="body", type=StringType)
state_Behaviour_language: Property = Property(name="language", type=StringType)
state_Behaviour.attributes={state_Behaviour_body, state_Behaviour_language}

# state_Vertex class attributes and methods

# state_StateMachine class attributes and methods

# state_Transition class attributes and methods
state_Transition_kind: Property = Property(name="kind", type=StringType)
state_Transition.attributes={state_Transition_kind}

# state_State class attributes and methods
state_State_isSimple: Property = Property(name="isSimple", type=BooleanType)
state_State_isComposite: Property = Property(name="isComposite", type=BooleanType)
state_State.attributes={state_State_isComposite, state_State_isSimple}

# Vertex class attributes and methods

# NamedElement class attributes and methods

# state_Region class attributes and methods

# state_NamedElement class attributes and methods
state_NamedElement_name: Property = Property(name="name", type=StringType)
state_NamedElement_id: Property = Property(name="id", type=StringType)
state_NamedElement.attributes={state_NamedElement_id, state_NamedElement_name}

# state_Constraint class attributes and methods

# state_StateModel class attributes and methods

# state_PseudoState class attributes and methods
state_PseudoState_kind: Property = Property(name="kind", type=StringType)
state_PseudoState.attributes={state_PseudoState_kind}

# state_FinalState class attributes and methods

# State class attributes and methods

# state_OpaqueExpression class attributes and methods
state_OpaqueExpression_body: Property = Property(name="body", type=StringType)
state_OpaqueExpression.attributes={state_OpaqueExpression_body}

# state_Event class attributes and methods
state_Event_body: Property = Property(name="body", type=StringType)
state_Event.attributes={state_Event_body}

# Relationships
defferableTrigger1: BinaryAssociation = BinaryAssociation(
    name="defferableTrigger1",
    ends={
        Property(name="state_Trigger", type=state_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state_State2", type=state_Trigger, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
doActivity3: BinaryAssociation = BinaryAssociation(
    name="doActivity3",
    ends={
        Property(name="state_Behaviour", type=state_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state_State4", type=state_Behaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entry5: BinaryAssociation = BinaryAssociation(
    name="entry5",
    ends={
        Property(name="state_Behaviour7", type=state_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state_State6", type=state_Behaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit8: BinaryAssociation = BinaryAssociation(
    name="exit8",
    ends={
        Property(name="state_Behaviour10", type=state_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state_State9", type=state_Behaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
state11: BinaryAssociation = BinaryAssociation(
    name="state11",
    ends={
        Property(name="state_State13", type=state_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="state_Region12", type=state_State, multiplicity=Multiplicity(0, 1))
    }
)
subVertex14: BinaryAssociation = BinaryAssociation(
    name="subVertex14",
    ends={
        Property(name="state_Vertex", type=state_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="state_Region15", type=state_Vertex, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
stateMachine16: BinaryAssociation = BinaryAssociation(
    name="stateMachine16",
    ends={
        Property(name="state_StateMachine", type=state_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="state_Region17", type=state_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
transition18: BinaryAssociation = BinaryAssociation(
    name="transition18",
    ends={
        Property(name="state_Transition", type=state_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="state_Region19", type=state_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
region20: BinaryAssociation = BinaryAssociation(
    name="region20",
    ends={
        Property(name="state_Region22", type=state_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="state_StateMachine21", type=state_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
region0: BinaryAssociation = BinaryAssociation(
    name="region0",
    ends={
        Property(name="state_Region", type=state_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state_State", type=state_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
target27: BinaryAssociation = BinaryAssociation(
    name="target27",
    ends={
        Property(name="Vertex28", type=state_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=state_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
outgoing23: BinaryAssociation = BinaryAssociation(
    name="outgoing23",
    ends={
        Property(name="Transition", type=state_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=state_Transition, multiplicity=Multiplicity(1, 9999))
    }
)
incoming24: BinaryAssociation = BinaryAssociation(
    name="incoming24",
    ends={
        Property(name="Transition25", type=state_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=state_Transition, multiplicity=Multiplicity(1, 9999))
    }
)
source26: BinaryAssociation = BinaryAssociation(
    name="source26",
    ends={
        Property(name="Vertex", type=state_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=state_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
trigger29: BinaryAssociation = BinaryAssociation(
    name="trigger29",
    ends={
        Property(name="state_Trigger31", type=state_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="state_Transition30", type=state_Trigger, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
guard32: BinaryAssociation = BinaryAssociation(
    name="guard32",
    ends={
        Property(name="state_Constraint", type=state_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="state_Transition33", type=state_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
effect34: BinaryAssociation = BinaryAssociation(
    name="effect34",
    ends={
        Property(name="state_Behaviour36", type=state_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="state_Transition35", type=state_Behaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
packagedElment41: BinaryAssociation = BinaryAssociation(
    name="packagedElment41",
    ends={
        Property(name="state_NamedElement", type=state_StateModel, multiplicity=Multiplicity(1, 1)),
        Property(name="state_StateModel", type=state_NamedElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
specification37: BinaryAssociation = BinaryAssociation(
    name="specification37",
    ends={
        Property(name="state_OpaqueExpression", type=state_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="state_Constraint38", type=state_OpaqueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
event39: BinaryAssociation = BinaryAssociation(
    name="event39",
    ends={
        Property(name="state_Event", type=state_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="state_Trigger40", type=state_Event, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_state_Region_NamedElement = Generalization(general=NamedElement, specific=state_Region)
gen_state_StateMachine_NamedElement = Generalization(general=NamedElement, specific=state_StateMachine)
gen_state_State_Vertex = Generalization(general=Vertex, specific=state_State)
gen_state_State_NamedElement = Generalization(general=NamedElement, specific=state_State)
gen_state_Vertex_NamedElement = Generalization(general=NamedElement, specific=state_Vertex)
gen_state_Transition_NamedElement = Generalization(general=NamedElement, specific=state_Transition)
gen_state_PseudoState_Vertex = Generalization(general=Vertex, specific=state_PseudoState)
gen_state_FinalState_State = Generalization(general=State, specific=state_FinalState)
gen_state_Trigger_NamedElement = Generalization(general=NamedElement, specific=state_Trigger)

# Domain Model
domain_model = DomainModel(
    name="state",
    types={state_Trigger, state_Behaviour, state_Vertex, state_StateMachine, state_Transition, state_State, Vertex, NamedElement, state_Region, state_NamedElement, state_Constraint, state_StateModel, state_PseudoState, state_FinalState, State, state_OpaqueExpression, state_Event, PseudoStateKind, TransitionKind},
    associations={defferableTrigger1, doActivity3, entry5, exit8, state11, subVertex14, stateMachine16, transition18, region20, region0, target27, outgoing23, incoming24, source26, trigger29, guard32, effect34, packagedElment41, specification37, event39},
    generalizations={gen_state_Region_NamedElement, gen_state_StateMachine_NamedElement, gen_state_State_Vertex, gen_state_State_NamedElement, gen_state_Vertex_NamedElement, gen_state_Transition_NamedElement, gen_state_PseudoState_Vertex, gen_state_FinalState_State, gen_state_Trigger_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)