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
timedfsm_FSM = Class(name="timedfsm_FSM")
timedfsm_State = Class(name="timedfsm_State")
timedfsm_Transition = Class(name="timedfsm_Transition")

# timedfsm_FSM class attributes and methods

# timedfsm_State class attributes and methods
timedfsm_State_name: Property = Property(name="name", type=StringType)
timedfsm_State_waitingTime: Property = Property(name="waitingTime", type=IntegerType)
timedfsm_State.attributes={timedfsm_State_name, timedfsm_State_waitingTime}

# timedfsm_Transition class attributes and methods
timedfsm_Transition_input: Property = Property(name="input", type=StringType)
timedfsm_Transition_output: Property = Property(name="output", type=StringType)
timedfsm_Transition_waitingTime: Property = Property(name="waitingTime", type=IntegerType)
timedfsm_Transition.attributes={timedfsm_Transition_output, timedfsm_Transition_input, timedfsm_Transition_waitingTime}

# Relationships
ownedState0: BinaryAssociation = BinaryAssociation(
    name="ownedState0",
    ends={
        Property(name="State", type=timedfsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=timedfsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="timedfsm_State", type=timedfsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="timedfsm_FSM", type=timedfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
finalState2: BinaryAssociation = BinaryAssociation(
    name="finalState2",
    ends={
        Property(name="timedfsm_State4", type=timedfsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="timedfsm_FSM3", type=timedfsm_State, multiplicity=Multiplicity(1, 9999))
    }
)
owningFSM5: BinaryAssociation = BinaryAssociation(
    name="owningFSM5",
    ends={
        Property(name="FSM", type=timedfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedState", type=timedfsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransition6: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition6",
    ends={
        Property(name="Transition", type=timedfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=timedfsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="State12", type=timedfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransition", type=timedfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
incomingTransition7: BinaryAssociation = BinaryAssociation(
    name="incomingTransition7",
    ends={
        Property(name="Transition8", type=timedfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=timedfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source9: BinaryAssociation = BinaryAssociation(
    name="source9",
    ends={
        Property(name="State10", type=timedfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransition", type=timedfsm_State, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="timedfsm",
    types={timedfsm_FSM, timedfsm_State, timedfsm_Transition},
    associations={ownedState0, initialState1, finalState2, owningFSM5, outgoingTransition6, target11, incomingTransition7, source9},
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