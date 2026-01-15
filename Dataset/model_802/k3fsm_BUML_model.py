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
k3fsm_FSM = Class(name="k3fsm::FSM")
k3fsm_State = Class(name="k3fsm::State")
k3fsm_Transition = Class(name="k3fsm::Transition")

# k3fsm_FSM class attributes and methods
k3fsm_FSM_name: Property = Property(name="name", type=StringType)
k3fsm_FSM_unprocessedString: Property = Property(name="unprocessedString", type=StringType)
k3fsm_FSM_consummedString: Property = Property(name="consummedString", type=StringType)
k3fsm_FSM_producedString: Property = Property(name="producedString", type=StringType)
k3fsm_FSM.attributes={k3fsm_FSM_consummedString, k3fsm_FSM_producedString, k3fsm_FSM_unprocessedString, k3fsm_FSM_name}

# k3fsm_State class attributes and methods
k3fsm_State_name: Property = Property(name="name", type=StringType)
k3fsm_State.attributes={k3fsm_State_name}

# k3fsm_Transition class attributes and methods
k3fsm_Transition_input: Property = Property(name="input", type=StringType)
k3fsm_Transition_name: Property = Property(name="name", type=StringType)
k3fsm_Transition_output: Property = Property(name="output", type=StringType)
k3fsm_Transition.attributes={k3fsm_Transition_output, k3fsm_Transition_input, k3fsm_Transition_name}

# Relationships
ownedStates0: BinaryAssociation = BinaryAssociation(
    name="ownedStates0",
    ends={
        Property(name="1", type=k3fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=k3fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState2: BinaryAssociation = BinaryAssociation(
    name="initialState2",
    ends={
        Property(name="k3fsm_State", type=k3fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="k3fsm_FSM", type=k3fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
finalState3: BinaryAssociation = BinaryAssociation(
    name="finalState3",
    ends={
        Property(name="k3fsm_State5", type=k3fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="k3fsm_FSM4", type=k3fsm_State, multiplicity=Multiplicity(0, 1))
    }
)
currentState6: BinaryAssociation = BinaryAssociation(
    name="currentState6",
    ends={
        Property(name="k3fsm_State8", type=k3fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="k3fsm_FSM7", type=k3fsm_State, multiplicity=Multiplicity(0, 1))
    }
)
source21: BinaryAssociation = BinaryAssociation(
    name="source21",
    ends={
        Property(name="23", type=k3fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="22", type=k3fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransitions9: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions9",
    ends={
        Property(name="11", type=k3fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="10", type=k3fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransitions12: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions12",
    ends={
        Property(name="14", type=k3fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="13", type=k3fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
owningFSM15: BinaryAssociation = BinaryAssociation(
    name="owningFSM15",
    ends={
        Property(name="17", type=k3fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="16", type=k3fsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)
target18: BinaryAssociation = BinaryAssociation(
    name="target18",
    ends={
        Property(name="20", type=k3fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="19", type=k3fsm_State, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="k3fsm",
    types={k3fsm_FSM, k3fsm_State, k3fsm_Transition},
    associations={ownedStates0, initialState2, finalState3, currentState6, source21, outgoingTransitions9, incomingTransitions12, owningFSM15, target18},
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