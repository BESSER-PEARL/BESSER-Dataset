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
			EnumerationLiteral(name="deepHistory"),
			EnumerationLiteral(name="shallowHistory"),
			EnumerationLiteral(name="join"),
			EnumerationLiteral(name="fork"),
			EnumerationLiteral(name="junction"),
			EnumerationLiteral(name="choice"),
			EnumerationLiteral(name="entryPoint"),
			EnumerationLiteral(name="exitPoint"),
			EnumerationLiteral(name="terminate")
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
StateMachines_StateMachine = Class(name="StateMachines::StateMachine")
StateMachines_Region = Class(name="StateMachines::Region")
StateMachines_Vertex = Class(name="StateMachines::Vertex")
StateMachines_Transition = Class(name="StateMachines::Transition")
StateMachines_Trigger = Class(name="StateMachines::Trigger")
StateMachines_Pseudostate = Class(name="StateMachines::Pseudostate")
Vertex = Class(name="Vertex")
StateMachines_State = Class(name="StateMachines::State")
StateMachines_Behavior = Class(name="StateMachines::Behavior")
StateMachines_ConnectionPointReference = Class(name="StateMachines::ConnectionPointReference")
StateMachines_FinalState = Class(name="StateMachines::FinalState")
State = Class(name="State")

# StateMachines_StateMachine class attributes and methods

# StateMachines_Region class attributes and methods

# StateMachines_Vertex class attributes and methods

# StateMachines_Transition class attributes and methods
StateMachines_Transition_kind: Property = Property(name="kind", type=StringType)
StateMachines_Transition.attributes={StateMachines_Transition_kind}

# StateMachines_Trigger class attributes and methods

# StateMachines_Pseudostate class attributes and methods
StateMachines_Pseudostate_kind: Property = Property(name="kind", type=StringType)
StateMachines_Pseudostate.attributes={StateMachines_Pseudostate_kind}

# Vertex class attributes and methods

# StateMachines_State class attributes and methods

# StateMachines_Behavior class attributes and methods

# StateMachines_ConnectionPointReference class attributes and methods

# StateMachines_FinalState class attributes and methods

# State class attributes and methods

# Relationships
incoming8: BinaryAssociation = BinaryAssociation(
    name="incoming8",
    ends={
        Property(name="StateMachines_Transition10", type=StateMachines_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_Vertex9", type=StateMachines_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
region0: BinaryAssociation = BinaryAssociation(
    name="region0",
    ends={
        Property(name="StateMachines_Region", type=StateMachines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_StateMachine", type=StateMachines_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
subvertex1: BinaryAssociation = BinaryAssociation(
    name="subvertex1",
    ends={
        Property(name="StateMachines_Vertex", type=StateMachines_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_Region2", type=StateMachines_Vertex, multiplicity=Multiplicity(0, 9999))
    }
)
transition3: BinaryAssociation = BinaryAssociation(
    name="transition3",
    ends={
        Property(name="StateMachines_Transition", type=StateMachines_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_Region4", type=StateMachines_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing5: BinaryAssociation = BinaryAssociation(
    name="outgoing5",
    ends={
        Property(name="StateMachines_Transition7", type=StateMachines_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_Vertex6", type=StateMachines_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
trigger11: BinaryAssociation = BinaryAssociation(
    name="trigger11",
    ends={
        Property(name="StateMachines_Trigger", type=StateMachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_Transition12", type=StateMachines_Trigger, multiplicity=Multiplicity(0, 9999))
    }
)
region13: BinaryAssociation = BinaryAssociation(
    name="region13",
    ends={
        Property(name="StateMachines_Region14", type=StateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_State", type=StateMachines_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectionPoint15: BinaryAssociation = BinaryAssociation(
    name="connectionPoint15",
    ends={
        Property(name="StateMachines_Pseudostate", type=StateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_State16", type=StateMachines_Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entry17: BinaryAssociation = BinaryAssociation(
    name="entry17",
    ends={
        Property(name="StateMachines_Behavior", type=StateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_State18", type=StateMachines_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit19: BinaryAssociation = BinaryAssociation(
    name="exit19",
    ends={
        Property(name="StateMachines_Behavior21", type=StateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_State20", type=StateMachines_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doActivity22: BinaryAssociation = BinaryAssociation(
    name="doActivity22",
    ends={
        Property(name="StateMachines_Behavior24", type=StateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_State23", type=StateMachines_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connection25: BinaryAssociation = BinaryAssociation(
    name="connection25",
    ends={
        Property(name="StateMachines_ConnectionPointReference", type=StateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_State26", type=StateMachines_ConnectionPointReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deferrableTrigger27: BinaryAssociation = BinaryAssociation(
    name="deferrableTrigger27",
    ends={
        Property(name="StateMachines_Trigger29", type=StateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_State28", type=StateMachines_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
submachine30: BinaryAssociation = BinaryAssociation(
    name="submachine30",
    ends={
        Property(name="StateMachines_StateMachine32", type=StateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_State31", type=StateMachines_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
entry33: BinaryAssociation = BinaryAssociation(
    name="entry33",
    ends={
        Property(name="StateMachines_Pseudostate35", type=StateMachines_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_ConnectionPointReference34", type=StateMachines_Pseudostate, multiplicity=Multiplicity(0, 9999))
    }
)
exit36: BinaryAssociation = BinaryAssociation(
    name="exit36",
    ends={
        Property(name="StateMachines_Pseudostate38", type=StateMachines_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_ConnectionPointReference37", type=StateMachines_Pseudostate, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_StateMachines_Pseudostate_Vertex = Generalization(general=Vertex, specific=StateMachines_Pseudostate)
gen_StateMachines_State_Vertex = Generalization(general=Vertex, specific=StateMachines_State)
gen_StateMachines_ConnectionPointReference_Vertex = Generalization(general=Vertex, specific=StateMachines_ConnectionPointReference)
gen_StateMachines_FinalState_State = Generalization(general=State, specific=StateMachines_FinalState)

# Domain Model
domain_model = DomainModel(
    name="StateMachines",
    types={StateMachines_StateMachine, StateMachines_Region, StateMachines_Vertex, StateMachines_Transition, StateMachines_Trigger, StateMachines_Pseudostate, Vertex, StateMachines_State, StateMachines_Behavior, StateMachines_ConnectionPointReference, StateMachines_FinalState, State, PseudoStateKind, TransitionKind},
    associations={incoming8, region0, subvertex1, transition3, outgoing5, trigger11, region13, connectionPoint15, entry17, exit19, doActivity22, connection25, deferrableTrigger27, submachine30, entry33, exit36},
    generalizations={gen_StateMachines_Pseudostate_Vertex, gen_StateMachines_State_Vertex, gen_StateMachines_ConnectionPointReference_Vertex, gen_StateMachines_FinalState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)