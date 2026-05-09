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
StateMachinesProv_StateMachine = Class(name="StateMachinesProv_StateMachine")
StateMachinesProv_Region = Class(name="StateMachinesProv_Region")
StateMachinesProv_Pseudostate = Class(name="StateMachinesProv_Pseudostate")
StateMachinesProv_State = Class(name="StateMachinesProv_State")
StateMachinesProv_Vertex = Class(name="StateMachinesProv_Vertex", is_abstract=True)
StateMachinesProv_Transition = Class(name="StateMachinesProv_Transition")
StateMachinesProv_ConnectionPointReference = Class(name="StateMachinesProv_ConnectionPointReference")
StateMachinesProv_FinalState = Class(name="StateMachinesProv_FinalState")
State = Class(name="State")
StateMachinesProv_TimeEvent = Class(name="StateMachinesProv_TimeEvent")
StateMachinesProv_ProtocolStateMachine = Class(name="StateMachinesProv_ProtocolStateMachine")
StateMachine = Class(name="StateMachine")
StateMachinesProv_ProtocolConformance = Class(name="StateMachinesProv_ProtocolConformance")
StateMachinesProv_ProtocolTransition = Class(name="StateMachinesProv_ProtocolTransition")
Transition = Class(name="Transition")
Vertex = Class(name="Vertex")

# StateMachinesProv_StateMachine class attributes and methods

# StateMachinesProv_Region class attributes and methods

# StateMachinesProv_Pseudostate class attributes and methods

# StateMachinesProv_State class attributes and methods
StateMachinesProv_State_isComposite: Property = Property(name="isComposite", type=BooleanType)
StateMachinesProv_State_isOrthogonal: Property = Property(name="isOrthogonal", type=BooleanType)
StateMachinesProv_State_isSimple: Property = Property(name="isSimple", type=BooleanType)
StateMachinesProv_State_isSubmachineState: Property = Property(name="isSubmachineState", type=BooleanType)
StateMachinesProv_State.attributes={StateMachinesProv_State_isSimple, StateMachinesProv_State_isComposite, StateMachinesProv_State_isOrthogonal, StateMachinesProv_State_isSubmachineState}

# StateMachinesProv_Vertex class attributes and methods

# StateMachinesProv_Transition class attributes and methods

# StateMachinesProv_ConnectionPointReference class attributes and methods

# StateMachinesProv_FinalState class attributes and methods

# State class attributes and methods

# StateMachinesProv_TimeEvent class attributes and methods

# StateMachinesProv_ProtocolStateMachine class attributes and methods

# StateMachine class attributes and methods

# StateMachinesProv_ProtocolConformance class attributes and methods

# StateMachinesProv_ProtocolTransition class attributes and methods

# Transition class attributes and methods

# Vertex class attributes and methods

# Relationships
region0: BinaryAssociation = BinaryAssociation(
    name="region0",
    ends={
        Property(name="StateMachinesProv_Region", type=StateMachinesProv_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_StateMachine", type=StateMachinesProv_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
connectionPoint1: BinaryAssociation = BinaryAssociation(
    name="connectionPoint1",
    ends={
        Property(name="StateMachinesProv_Pseudostate", type=StateMachinesProv_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_StateMachine2", type=StateMachinesProv_Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
submachineState3: BinaryAssociation = BinaryAssociation(
    name="submachineState3",
    ends={
        Property(name="StateMachinesProv_State", type=StateMachinesProv_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_StateMachine4", type=StateMachinesProv_State, multiplicity=Multiplicity(0, 9999))
    }
)
extendedStateMachine6: BinaryAssociation = BinaryAssociation(
    name="extendedStateMachine6",
    ends={
        Property(name="StateMachinesProv_StateMachine7", type=StateMachinesProv_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_StateMachine5", type=StateMachinesProv_StateMachine, multiplicity=Multiplicity(0, 9999))
    }
)
subvertex8: BinaryAssociation = BinaryAssociation(
    name="subvertex8",
    ends={
        Property(name="StateMachinesProv_Vertex", type=StateMachinesProv_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_Region9", type=StateMachinesProv_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine10: BinaryAssociation = BinaryAssociation(
    name="stateMachine10",
    ends={
        Property(name="StateMachinesProv_StateMachine12", type=StateMachinesProv_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_Region11", type=StateMachinesProv_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
transition13: BinaryAssociation = BinaryAssociation(
    name="transition13",
    ends={
        Property(name="StateMachinesProv_Transition", type=StateMachinesProv_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_Region14", type=StateMachinesProv_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state15: BinaryAssociation = BinaryAssociation(
    name="state15",
    ends={
        Property(name="StateMachinesProv_State17", type=StateMachinesProv_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_Region16", type=StateMachinesProv_State, multiplicity=Multiplicity(0, 1))
    }
)
extendedRegion19: BinaryAssociation = BinaryAssociation(
    name="extendedRegion19",
    ends={
        Property(name="StateMachinesProv_Region20", type=StateMachinesProv_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_Region18", type=StateMachinesProv_Region, multiplicity=Multiplicity(0, 1))
    }
)
outgoing21: BinaryAssociation = BinaryAssociation(
    name="outgoing21",
    ends={
        Property(name="StateMachinesProv_Transition23", type=StateMachinesProv_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_Vertex22", type=StateMachinesProv_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming24: BinaryAssociation = BinaryAssociation(
    name="incoming24",
    ends={
        Property(name="StateMachinesProv_Transition26", type=StateMachinesProv_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_Vertex25", type=StateMachinesProv_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
container27: BinaryAssociation = BinaryAssociation(
    name="container27",
    ends={
        Property(name="StateMachinesProv_Region29", type=StateMachinesProv_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_Vertex28", type=StateMachinesProv_Region, multiplicity=Multiplicity(0, 1))
    }
)
source30: BinaryAssociation = BinaryAssociation(
    name="source30",
    ends={
        Property(name="StateMachinesProv_Vertex32", type=StateMachinesProv_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_Transition31", type=StateMachinesProv_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
target33: BinaryAssociation = BinaryAssociation(
    name="target33",
    ends={
        Property(name="StateMachinesProv_Vertex35", type=StateMachinesProv_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_Transition34", type=StateMachinesProv_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
container36: BinaryAssociation = BinaryAssociation(
    name="container36",
    ends={
        Property(name="StateMachinesProv_Region38", type=StateMachinesProv_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_Transition37", type=StateMachinesProv_Region, multiplicity=Multiplicity(0, 1))
    }
)
exit45: BinaryAssociation = BinaryAssociation(
    name="exit45",
    ends={
        Property(name="StateMachinesProv_Pseudostate46", type=StateMachinesProv_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_ConnectionPointReference", type=StateMachinesProv_Pseudostate, multiplicity=Multiplicity(0, 1))
    }
)
entry47: BinaryAssociation = BinaryAssociation(
    name="entry47",
    ends={
        Property(name="StateMachinesProv_Pseudostate49", type=StateMachinesProv_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_ConnectionPointReference48", type=StateMachinesProv_Pseudostate, multiplicity=Multiplicity(0, 1))
    }
)
state50: BinaryAssociation = BinaryAssociation(
    name="state50",
    ends={
        Property(name="StateMachinesProv_State52", type=StateMachinesProv_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_ConnectionPointReference51", type=StateMachinesProv_State, multiplicity=Multiplicity(0, 1))
    }
)
connection53: BinaryAssociation = BinaryAssociation(
    name="connection53",
    ends={
        Property(name="StateMachinesProv_ConnectionPointReference55", type=StateMachinesProv_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_State54", type=StateMachinesProv_ConnectionPointReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectionPoint56: BinaryAssociation = BinaryAssociation(
    name="connectionPoint56",
    ends={
        Property(name="StateMachinesProv_Pseudostate58", type=StateMachinesProv_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_State57", type=StateMachinesProv_Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
submachine59: BinaryAssociation = BinaryAssociation(
    name="submachine59",
    ends={
        Property(name="StateMachinesProv_StateMachine61", type=StateMachinesProv_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_State60", type=StateMachinesProv_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
region62: BinaryAssociation = BinaryAssociation(
    name="region62",
    ends={
        Property(name="StateMachinesProv_Region64", type=StateMachinesProv_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_State63", type=StateMachinesProv_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
redefinedState66: BinaryAssociation = BinaryAssociation(
    name="redefinedState66",
    ends={
        Property(name="StateMachinesProv_State67", type=StateMachinesProv_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_State65", type=StateMachinesProv_State, multiplicity=Multiplicity(0, 1))
    }
)
conformance68: BinaryAssociation = BinaryAssociation(
    name="conformance68",
    ends={
        Property(name="StateMachinesProv_ProtocolConformance", type=StateMachinesProv_ProtocolStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_ProtocolStateMachine", type=StateMachinesProv_ProtocolConformance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specificMachine69: BinaryAssociation = BinaryAssociation(
    name="specificMachine69",
    ends={
        Property(name="StateMachinesProv_ProtocolStateMachine71", type=StateMachinesProv_ProtocolConformance, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_ProtocolConformance70", type=StateMachinesProv_ProtocolStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
generalMachine72: BinaryAssociation = BinaryAssociation(
    name="generalMachine72",
    ends={
        Property(name="StateMachinesProv_ProtocolStateMachine74", type=StateMachinesProv_ProtocolConformance, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_ProtocolConformance73", type=StateMachinesProv_ProtocolStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
redefinedTransition40: BinaryAssociation = BinaryAssociation(
    name="redefinedTransition40",
    ends={
        Property(name="StateMachinesProv_Transition41", type=StateMachinesProv_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_Transition39", type=StateMachinesProv_Transition, multiplicity=Multiplicity(0, 1))
    }
)
state42: BinaryAssociation = BinaryAssociation(
    name="state42",
    ends={
        Property(name="StateMachinesProv_State44", type=StateMachinesProv_Pseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesProv_Pseudostate43", type=StateMachinesProv_State, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_StateMachinesProv_ConnectionPointReference_Vertex = Generalization(general=Vertex, specific=StateMachinesProv_ConnectionPointReference)
gen_StateMachinesProv_State_Vertex = Generalization(general=Vertex, specific=StateMachinesProv_State)
gen_StateMachinesProv_FinalState_State = Generalization(general=State, specific=StateMachinesProv_FinalState)
gen_StateMachinesProv_ProtocolStateMachine_StateMachine = Generalization(general=StateMachine, specific=StateMachinesProv_ProtocolStateMachine)
gen_StateMachinesProv_ProtocolTransition_Transition = Generalization(general=Transition, specific=StateMachinesProv_ProtocolTransition)
gen_StateMachinesProv_Pseudostate_Vertex = Generalization(general=Vertex, specific=StateMachinesProv_Pseudostate)

# Domain Model
domain_model = DomainModel(
    name="StateMachinesProv",
    types={StateMachinesProv_StateMachine, StateMachinesProv_Region, StateMachinesProv_Pseudostate, StateMachinesProv_State, StateMachinesProv_Vertex, StateMachinesProv_Transition, StateMachinesProv_ConnectionPointReference, StateMachinesProv_FinalState, State, StateMachinesProv_TimeEvent, StateMachinesProv_ProtocolStateMachine, StateMachine, StateMachinesProv_ProtocolConformance, StateMachinesProv_ProtocolTransition, Transition, Vertex},
    associations={region0, connectionPoint1, submachineState3, extendedStateMachine6, subvertex8, stateMachine10, transition13, state15, extendedRegion19, outgoing21, incoming24, container27, source30, target33, container36, exit45, entry47, state50, connection53, connectionPoint56, submachine59, region62, redefinedState66, conformance68, specificMachine69, generalMachine72, redefinedTransition40, state42},
    generalizations={gen_StateMachinesProv_ConnectionPointReference_Vertex, gen_StateMachinesProv_State_Vertex, gen_StateMachinesProv_FinalState_State, gen_StateMachinesProv_ProtocolStateMachine_StateMachine, gen_StateMachinesProv_ProtocolTransition_Transition, gen_StateMachinesProv_Pseudostate_Vertex},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)