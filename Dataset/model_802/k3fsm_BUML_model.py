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
k3fsm_FSM = Class(name="k3fsm_FSM")
k3fsm_State = Class(name="k3fsm_State")
k3fsm_Transition = Class(name="k3fsm_Transition")

# k3fsm_FSM class attributes and methods
k3fsm_FSM_name: Property = Property(name="name", type=StringType)
k3fsm_FSM_unprocessedString: Property = Property(name="unprocessedString", type=StringType)
k3fsm_FSM_consummedString: Property = Property(name="consummedString", type=StringType)
k3fsm_FSM_producedString: Property = Property(name="producedString", type=StringType)
k3fsm_FSM.attributes={k3fsm_FSM_consummedString, k3fsm_FSM_unprocessedString, k3fsm_FSM_name, k3fsm_FSM_producedString}

# k3fsm_State class attributes and methods
k3fsm_State_name: Property = Property(name="name", type=StringType)
k3fsm_State.attributes={k3fsm_State_name}

# k3fsm_Transition class attributes and methods
k3fsm_Transition_input: Property = Property(name="input", type=StringType)
k3fsm_Transition_name: Property = Property(name="name", type=StringType)
k3fsm_Transition_output: Property = Property(name="output", type=StringType)
k3fsm_Transition.attributes={k3fsm_Transition_output, k3fsm_Transition_name, k3fsm_Transition_input}

# Relationships
finalState2: BinaryAssociation = BinaryAssociation(
    name="finalState2",
    ends={
        Property(name="k3fsm_State4", type=k3fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="k3fsm_FSM3", type=k3fsm_State, multiplicity=Multiplicity(0, 1))
    }
)
ownedStates0: BinaryAssociation = BinaryAssociation(
    name="ownedStates0",
    ends={
        Property(name="State", type=k3fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=k3fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="k3fsm_State", type=k3fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="k3fsm_FSM", type=k3fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
currentState5: BinaryAssociation = BinaryAssociation(
    name="currentState5",
    ends={
        Property(name="k3fsm_State7", type=k3fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="k3fsm_FSM6", type=k3fsm_State, multiplicity=Multiplicity(0, 1))
    }
)
outgoingTransitions8: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions8",
    ends={
        Property(name="Transition", type=k3fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=k3fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransitions9: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions9",
    ends={
        Property(name="Transition10", type=k3fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=k3fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
owningFSM11: BinaryAssociation = BinaryAssociation(
    name="owningFSM11",
    ends={
        Property(name="FSM", type=k3fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedStates", type=k3fsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="State13", type=k3fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=k3fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
source14: BinaryAssociation = BinaryAssociation(
    name="source14",
    ends={
        Property(name="State15", type=k3fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=k3fsm_State, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="k3fsm",
    types={k3fsm_FSM, k3fsm_State, k3fsm_Transition},
    associations={finalState2, ownedStates0, initialState1, currentState5, outgoingTransitions8, incomingTransitions9, owningFSM11, target12, source14},
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