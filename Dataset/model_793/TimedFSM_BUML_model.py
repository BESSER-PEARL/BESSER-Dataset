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
timedfsm_FSM = Class(name="timedfsm::FSM")
timedfsm_State = Class(name="timedfsm::State")
timedfsm_Transition = Class(name="timedfsm::Transition")

# timedfsm_FSM class attributes and methods

# timedfsm_State class attributes and methods
timedfsm_State_name: Property = Property(name="name", type=StringType)
timedfsm_State_waitingTime: Property = Property(name="waitingTime", type=IntegerType)
timedfsm_State.attributes={timedfsm_State_waitingTime, timedfsm_State_name}

# timedfsm_Transition class attributes and methods
timedfsm_Transition_input: Property = Property(name="input", type=StringType)
timedfsm_Transition_output: Property = Property(name="output", type=StringType)
timedfsm_Transition_waitingTime: Property = Property(name="waitingTime", type=IntegerType)
timedfsm_Transition.attributes={timedfsm_Transition_input, timedfsm_Transition_waitingTime, timedfsm_Transition_output}

# Relationships
ownedState0: BinaryAssociation = BinaryAssociation(
    name="ownedState0",
    ends={
        Property(name="1", type=timedfsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=timedfsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState2: BinaryAssociation = BinaryAssociation(
    name="initialState2",
    ends={
        Property(name="timedfsm_State", type=timedfsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="timedfsm_FSM", type=timedfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
finalState3: BinaryAssociation = BinaryAssociation(
    name="finalState3",
    ends={
        Property(name="timedfsm_State5", type=timedfsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="timedfsm_FSM4", type=timedfsm_State, multiplicity=Multiplicity(1, 9999))
    }
)
owningFSM6: BinaryAssociation = BinaryAssociation(
    name="owningFSM6",
    ends={
        Property(name="8", type=timedfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="7", type=timedfsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransition9: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition9",
    ends={
        Property(name="11", type=timedfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="10", type=timedfsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransition12: BinaryAssociation = BinaryAssociation(
    name="incomingTransition12",
    ends={
        Property(name="14", type=timedfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="13", type=timedfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source15: BinaryAssociation = BinaryAssociation(
    name="source15",
    ends={
        Property(name="17", type=timedfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="16", type=timedfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target18: BinaryAssociation = BinaryAssociation(
    name="target18",
    ends={
        Property(name="20", type=timedfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="19", type=timedfsm_State, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="timedfsm",
    types={timedfsm_FSM, timedfsm_State, timedfsm_Transition},
    associations={ownedState0, initialState2, finalState3, owningFSM6, outgoingTransition9, incomingTransition12, source15, target18},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)