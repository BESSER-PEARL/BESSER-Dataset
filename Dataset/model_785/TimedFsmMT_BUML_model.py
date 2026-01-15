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
fsm_FSM = Class(name="fsm::FSM")
fsm_State = Class(name="fsm::State")
fsm_Transition = Class(name="fsm::Transition")

# fsm_FSM class attributes and methods

# fsm_State class attributes and methods
fsm_State_name: Property = Property(name="name", type=StringType)
fsm_State.attributes={fsm_State_name}

# fsm_Transition class attributes and methods
fsm_Transition_input: Property = Property(name="input", type=StringType)
fsm_Transition_output: Property = Property(name="output", type=StringType)
fsm_Transition_time: Property = Property(name="time", type=IntegerType)
fsm_Transition.attributes={fsm_Transition_output, fsm_Transition_input, fsm_Transition_time}

# Relationships
ownedState0: BinaryAssociation = BinaryAssociation(
    name="ownedState0",
    ends={
        Property(name="State", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingTransition6: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition6",
    ends={
        Property(name="Transition", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransition7: BinaryAssociation = BinaryAssociation(
    name="incomingTransition7",
    ends={
        Property(name="Transition8", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source9: BinaryAssociation = BinaryAssociation(
    name="source9",
    ends={
        Property(name="State10", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransition", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="State12", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransition", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="fsm_State", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
finalState2: BinaryAssociation = BinaryAssociation(
    name="finalState2",
    ends={
        Property(name="fsm_State4", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM3", type=fsm_State, multiplicity=Multiplicity(1, 9999))
    }
)
owningFSM5: BinaryAssociation = BinaryAssociation(
    name="owningFSM5",
    ends={
        Property(name="FSM", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedState", type=fsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_FSM, fsm_State, fsm_Transition},
    associations={ownedState0, outgoingTransition6, incomingTransition7, source9, target11, initialState1, finalState2, owningFSM5},
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