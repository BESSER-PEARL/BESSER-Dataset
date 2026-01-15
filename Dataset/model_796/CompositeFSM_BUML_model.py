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
compositefsm_FSM = Class(name="compositefsm::FSM")
compositefsm_State = Class(name="compositefsm::State")
compositefsm_Transition = Class(name="compositefsm::Transition")

# compositefsm_FSM class attributes and methods

# compositefsm_State class attributes and methods
compositefsm_State_name: Property = Property(name="name", type=StringType)
compositefsm_State.attributes={compositefsm_State_name}

# compositefsm_Transition class attributes and methods
compositefsm_Transition_input: Property = Property(name="input", type=StringType)
compositefsm_Transition_output: Property = Property(name="output", type=StringType)
compositefsm_Transition.attributes={compositefsm_Transition_input, compositefsm_Transition_output}

# Relationships
ownedState0: BinaryAssociation = BinaryAssociation(
    name="ownedState0",
    ends={
        Property(name="State", type=compositefsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=compositefsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="compositefsm_State", type=compositefsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="compositefsm_FSM", type=compositefsm_State, multiplicity=Multiplicity(1, 1))
    }
)
finalState2: BinaryAssociation = BinaryAssociation(
    name="finalState2",
    ends={
        Property(name="compositefsm_State4", type=compositefsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="compositefsm_FSM3", type=compositefsm_State, multiplicity=Multiplicity(1, 9999))
    }
)
owningFSM5: BinaryAssociation = BinaryAssociation(
    name="owningFSM5",
    ends={
        Property(name="FSM", type=compositefsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedState", type=compositefsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransition6: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition6",
    ends={
        Property(name="Transition", type=compositefsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=compositefsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransition7: BinaryAssociation = BinaryAssociation(
    name="incomingTransition7",
    ends={
        Property(name="Transition8", type=compositefsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=compositefsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
subStates10: BinaryAssociation = BinaryAssociation(
    name="subStates10",
    ends={
        Property(name="State11", type=compositefsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="superState", type=compositefsm_State, multiplicity=Multiplicity(0, 9999))
    }
)
superState13: BinaryAssociation = BinaryAssociation(
    name="superState13",
    ends={
        Property(name="State14", type=compositefsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="subStates", type=compositefsm_State, multiplicity=Multiplicity(0, 1))
    }
)
source15: BinaryAssociation = BinaryAssociation(
    name="source15",
    ends={
        Property(name="State16", type=compositefsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransition", type=compositefsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target17: BinaryAssociation = BinaryAssociation(
    name="target17",
    ends={
        Property(name="State18", type=compositefsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransition", type=compositefsm_State, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="compositefsm",
    types={compositefsm_FSM, compositefsm_State, compositefsm_Transition},
    associations={ownedState0, initialState1, finalState2, owningFSM5, outgoingTransition6, incomingTransition7, subStates10, superState13, source15, target17},
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