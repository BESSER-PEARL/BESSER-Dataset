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
TransitionKind: Enumeration = Enumeration(
    name="TransitionKind",
    literals={
            EnumerationLiteral(name="internal"),
			EnumerationLiteral(name="local"),
			EnumerationLiteral(name="external")
    }
)

PseudostateKind: Enumeration = Enumeration(
    name="PseudostateKind",
    literals={
            EnumerationLiteral(name="deepHistory"),
			EnumerationLiteral(name="shallowHistory"),
			EnumerationLiteral(name="join"),
			EnumerationLiteral(name="fork"),
			EnumerationLiteral(name="junction"),
			EnumerationLiteral(name="choice"),
			EnumerationLiteral(name="entryPoint"),
			EnumerationLiteral(name="exitPoint"),
			EnumerationLiteral(name="terminate"),
			EnumerationLiteral(name="initial")
    }
)

# Classes
umlstatemachineselect_StateMachine = Class(name="umlstatemachineselect::StateMachine")
Behavior = Class(name="Behavior")
umlstatemachineselect_Region = Class(name="umlstatemachineselect::Region")
umlstatemachineselect_Vertex = Class(name="umlstatemachineselect::Vertex", is_abstract=True)
umlstatemachineselect_Transition = Class(name="umlstatemachineselect::Transition")
umlstatemachineselect_State = Class(name="umlstatemachineselect::State")
umlstatemachineselect_PseudoState = Class(name="umlstatemachineselect::PseudoState")
umlstatemachineselect_Behavior = Class(name="umlstatemachineselect::Behavior")
umlstatemachineselect_Constraint = Class(name="umlstatemachineselect::Constraint")
umlstatemachineselect_Trigger = Class(name="umlstatemachineselect::Trigger")
Vertex = Class(name="Vertex")
umlstatemachineselect_ConnectionPointReference = Class(name="umlstatemachineselect::ConnectionPointReference")
umlstatemachineselect_FinalState = Class(name="umlstatemachineselect::FinalState")
State = Class(name="State")
umlstatemachineselect_Event = Class(name="umlstatemachineselect::Event")

# umlstatemachineselect_StateMachine class attributes and methods

# Behavior class attributes and methods

# umlstatemachineselect_Region class attributes and methods

# umlstatemachineselect_Vertex class attributes and methods

# umlstatemachineselect_Transition class attributes and methods
umlstatemachineselect_Transition_kind: Property = Property(name="kind", type=StringType)
umlstatemachineselect_Transition.attributes={umlstatemachineselect_Transition_kind}

# umlstatemachineselect_State class attributes and methods
umlstatemachineselect_State_isComposite: Property = Property(name="isComposite", type=BooleanType)
umlstatemachineselect_State_isOrthogonal: Property = Property(name="isOrthogonal", type=BooleanType)
umlstatemachineselect_State_isSimple: Property = Property(name="isSimple", type=BooleanType)
umlstatemachineselect_State_isSubmachineState: Property = Property(name="isSubmachineState", type=BooleanType)
umlstatemachineselect_State.attributes={umlstatemachineselect_State_isSimple, umlstatemachineselect_State_isComposite, umlstatemachineselect_State_isOrthogonal, umlstatemachineselect_State_isSubmachineState}

# umlstatemachineselect_PseudoState class attributes and methods
umlstatemachineselect_PseudoState_kind: Property = Property(name="kind", type=StringType)
umlstatemachineselect_PseudoState.attributes={umlstatemachineselect_PseudoState_kind}

# umlstatemachineselect_Behavior class attributes and methods

# umlstatemachineselect_Constraint class attributes and methods

# umlstatemachineselect_Trigger class attributes and methods

# Vertex class attributes and methods

# umlstatemachineselect_ConnectionPointReference class attributes and methods

# umlstatemachineselect_FinalState class attributes and methods

# State class attributes and methods

# umlstatemachineselect_Event class attributes and methods

# Relationships
region0: BinaryAssociation = BinaryAssociation(
    name="region0",
    ends={
        Property(name="Region", type=umlstatemachineselect_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=umlstatemachineselect_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
stateMachine4: BinaryAssociation = BinaryAssociation(
    name="stateMachine4",
    ends={
        Property(name="StateMachine", type=umlstatemachineselect_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="region", type=umlstatemachineselect_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
subvertex5: BinaryAssociation = BinaryAssociation(
    name="subvertex5",
    ends={
        Property(name="Vertex", type=umlstatemachineselect_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=umlstatemachineselect_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition6: BinaryAssociation = BinaryAssociation(
    name="transition6",
    ends={
        Property(name="Transition", type=umlstatemachineselect_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="container7", type=umlstatemachineselect_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state8: BinaryAssociation = BinaryAssociation(
    name="state8",
    ends={
        Property(name="State10", type=umlstatemachineselect_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="region9", type=umlstatemachineselect_State, multiplicity=Multiplicity(0, 1))
    }
)
container11: BinaryAssociation = BinaryAssociation(
    name="container11",
    ends={
        Property(name="Region12", type=umlstatemachineselect_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="subvertex", type=umlstatemachineselect_Region, multiplicity=Multiplicity(0, 1))
    }
)
submachineState1: BinaryAssociation = BinaryAssociation(
    name="submachineState1",
    ends={
        Property(name="State", type=umlstatemachineselect_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="submachine", type=umlstatemachineselect_State, multiplicity=Multiplicity(0, 9999))
    }
)
connectionPoint2: BinaryAssociation = BinaryAssociation(
    name="connectionPoint2",
    ends={
        Property(name="PseudoState", type=umlstatemachineselect_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine3", type=umlstatemachineselect_PseudoState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target19: BinaryAssociation = BinaryAssociation(
    name="target19",
    ends={
        Property(name="Vertex20", type=umlstatemachineselect_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=umlstatemachineselect_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
source21: BinaryAssociation = BinaryAssociation(
    name="source21",
    ends={
        Property(name="Vertex22", type=umlstatemachineselect_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=umlstatemachineselect_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
effect23: BinaryAssociation = BinaryAssociation(
    name="effect23",
    ends={
        Property(name="umlstatemachineselect_Behavior", type=umlstatemachineselect_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlstatemachineselect_Transition", type=umlstatemachineselect_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard24: BinaryAssociation = BinaryAssociation(
    name="guard24",
    ends={
        Property(name="umlstatemachineselect_Constraint", type=umlstatemachineselect_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlstatemachineselect_Transition25", type=umlstatemachineselect_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trigger26: BinaryAssociation = BinaryAssociation(
    name="trigger26",
    ends={
        Property(name="umlstatemachineselect_Trigger", type=umlstatemachineselect_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlstatemachineselect_Transition27", type=umlstatemachineselect_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing13: BinaryAssociation = BinaryAssociation(
    name="outgoing13",
    ends={
        Property(name="Transition14", type=umlstatemachineselect_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=umlstatemachineselect_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming15: BinaryAssociation = BinaryAssociation(
    name="incoming15",
    ends={
        Property(name="Transition16", type=umlstatemachineselect_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=umlstatemachineselect_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
container17: BinaryAssociation = BinaryAssociation(
    name="container17",
    ends={
        Property(name="Region18", type=umlstatemachineselect_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=umlstatemachineselect_Region, multiplicity=Multiplicity(1, 1))
    }
)
submachine32: BinaryAssociation = BinaryAssociation(
    name="submachine32",
    ends={
        Property(name="StateMachine33", type=umlstatemachineselect_State, multiplicity=Multiplicity(1, 1)),
        Property(name="submachineState", type=umlstatemachineselect_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
entry34: BinaryAssociation = BinaryAssociation(
    name="entry34",
    ends={
        Property(name="umlstatemachineselect_Behavior35", type=umlstatemachineselect_State, multiplicity=Multiplicity(1, 1)),
        Property(name="umlstatemachineselect_State", type=umlstatemachineselect_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
region28: BinaryAssociation = BinaryAssociation(
    name="region28",
    ends={
        Property(name="Region29", type=umlstatemachineselect_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=umlstatemachineselect_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connection30: BinaryAssociation = BinaryAssociation(
    name="connection30",
    ends={
        Property(name="ConnectionPointReference", type=umlstatemachineselect_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state31", type=umlstatemachineselect_ConnectionPointReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exit36: BinaryAssociation = BinaryAssociation(
    name="exit36",
    ends={
        Property(name="umlstatemachineselect_Behavior38", type=umlstatemachineselect_State, multiplicity=Multiplicity(1, 1)),
        Property(name="umlstatemachineselect_State37", type=umlstatemachineselect_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doActivity39: BinaryAssociation = BinaryAssociation(
    name="doActivity39",
    ends={
        Property(name="umlstatemachineselect_Behavior41", type=umlstatemachineselect_State, multiplicity=Multiplicity(1, 1)),
        Property(name="umlstatemachineselect_State40", type=umlstatemachineselect_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stateInvariant42: BinaryAssociation = BinaryAssociation(
    name="stateInvariant42",
    ends={
        Property(name="umlstatemachineselect_Constraint44", type=umlstatemachineselect_State, multiplicity=Multiplicity(1, 1)),
        Property(name="umlstatemachineselect_State43", type=umlstatemachineselect_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deferrableTrigger45: BinaryAssociation = BinaryAssociation(
    name="deferrableTrigger45",
    ends={
        Property(name="umlstatemachineselect_Trigger47", type=umlstatemachineselect_State, multiplicity=Multiplicity(1, 1)),
        Property(name="umlstatemachineselect_State46", type=umlstatemachineselect_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine48: BinaryAssociation = BinaryAssociation(
    name="stateMachine48",
    ends={
        Property(name="StateMachine49", type=umlstatemachineselect_PseudoState, multiplicity=Multiplicity(1, 1)),
        Property(name="connectionPoint", type=umlstatemachineselect_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
state50: BinaryAssociation = BinaryAssociation(
    name="state50",
    ends={
        Property(name="State51", type=umlstatemachineselect_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="connection", type=umlstatemachineselect_State, multiplicity=Multiplicity(0, 1))
    }
)
entry52: BinaryAssociation = BinaryAssociation(
    name="entry52",
    ends={
        Property(name="umlstatemachineselect_PseudoState", type=umlstatemachineselect_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="umlstatemachineselect_ConnectionPointReference", type=umlstatemachineselect_PseudoState, multiplicity=Multiplicity(0, 9999))
    }
)
exit53: BinaryAssociation = BinaryAssociation(
    name="exit53",
    ends={
        Property(name="umlstatemachineselect_PseudoState55", type=umlstatemachineselect_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="umlstatemachineselect_ConnectionPointReference54", type=umlstatemachineselect_PseudoState, multiplicity=Multiplicity(0, 9999))
    }
)
event56: BinaryAssociation = BinaryAssociation(
    name="event56",
    ends={
        Property(name="umlstatemachineselect_Event", type=umlstatemachineselect_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="umlstatemachineselect_Trigger57", type=umlstatemachineselect_Event, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_umlstatemachineselect_StateMachine_Behavior = Generalization(general=Behavior, specific=umlstatemachineselect_StateMachine)
gen_umlstatemachineselect_State_Vertex = Generalization(general=Vertex, specific=umlstatemachineselect_State)
gen_umlstatemachineselect_ConnectionPointReference_Vertex = Generalization(general=Vertex, specific=umlstatemachineselect_ConnectionPointReference)
gen_umlstatemachineselect_FinalState_State = Generalization(general=State, specific=umlstatemachineselect_FinalState)
gen_umlstatemachineselect_PseudoState_Vertex = Generalization(general=Vertex, specific=umlstatemachineselect_PseudoState)

# Domain Model
domain_model = DomainModel(
    name="umlstatemachineselect",
    types={umlstatemachineselect_StateMachine, Behavior, umlstatemachineselect_Region, umlstatemachineselect_Vertex, umlstatemachineselect_Transition, umlstatemachineselect_State, umlstatemachineselect_PseudoState, umlstatemachineselect_Behavior, umlstatemachineselect_Constraint, umlstatemachineselect_Trigger, Vertex, umlstatemachineselect_ConnectionPointReference, umlstatemachineselect_FinalState, State, umlstatemachineselect_Event, TransitionKind, PseudostateKind},
    associations={region0, stateMachine4, subvertex5, transition6, state8, container11, submachineState1, connectionPoint2, target19, source21, effect23, guard24, trigger26, outgoing13, incoming15, container17, submachine32, entry34, region28, connection30, exit36, doActivity39, stateInvariant42, deferrableTrigger45, stateMachine48, state50, entry52, exit53, event56},
    generalizations={gen_umlstatemachineselect_StateMachine_Behavior, gen_umlstatemachineselect_State_Vertex, gen_umlstatemachineselect_ConnectionPointReference_Vertex, gen_umlstatemachineselect_FinalState_State, gen_umlstatemachineselect_PseudoState_Vertex},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)