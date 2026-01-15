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
fsm_RuntimeConcept2 = Class(name="fsm::RuntimeConcept2")
fsm_RuntimeConcept1 = Class(name="fsm::RuntimeConcept1")
fsm_Transition = Class(name="fsm::Transition")
fsm_FSM = Class(name="fsm::FSM")
fsm_State = Class(name="fsm::State")

# fsm_RuntimeConcept2 class attributes and methods
fsm_RuntimeConcept2_bar: Property = Property(name="bar", type=StringType)
fsm_RuntimeConcept2.attributes={fsm_RuntimeConcept2_bar}

# fsm_RuntimeConcept1 class attributes and methods
fsm_RuntimeConcept1_foo: Property = Property(name="foo", type=IntegerType)
fsm_RuntimeConcept1.attributes={fsm_RuntimeConcept1_foo}

# fsm_Transition class attributes and methods
fsm_Transition_input: Property = Property(name="input", type=StringType)
fsm_Transition_output: Property = Property(name="output", type=StringType)
fsm_Transition.attributes={fsm_Transition_output, fsm_Transition_input}

# fsm_FSM class attributes and methods

# fsm_State class attributes and methods
fsm_State_name: Property = Property(name="name", type=StringType)
fsm_State.attributes={fsm_State_name}

# Relationships
initialState2: BinaryAssociation = BinaryAssociation(
    name="initialState2",
    ends={
        Property(name="fsm_FSM", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State", type=fsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)
finalState3: BinaryAssociation = BinaryAssociation(
    name="finalState3",
    ends={
        Property(name="fsm_State5", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM4", type=fsm_State, multiplicity=Multiplicity(1, 9999))
    }
)
myFoos6: BinaryAssociation = BinaryAssociation(
    name="myFoos6",
    ends={
        Property(name="fsm_RuntimeConcept1", type=fsm_RuntimeConcept2, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_RuntimeConcept2", type=fsm_RuntimeConcept1, multiplicity=Multiplicity(0, 9999))
    }
)
owningFSM7: BinaryAssociation = BinaryAssociation(
    name="owningFSM7",
    ends={
        Property(name="9", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="8", type=fsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransition10: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition10",
    ends={
        Property(name="12", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="11", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransition13: BinaryAssociation = BinaryAssociation(
    name="incomingTransition13",
    ends={
        Property(name="15", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="14", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source16: BinaryAssociation = BinaryAssociation(
    name="source16",
    ends={
        Property(name="18", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="17", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
ownedState0: BinaryAssociation = BinaryAssociation(
    name="ownedState0",
    ends={
        Property(name="1", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target19: BinaryAssociation = BinaryAssociation(
    name="target19",
    ends={
        Property(name="21", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="20", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
myState22: BinaryAssociation = BinaryAssociation(
    name="myState22",
    ends={
        Property(name="fsm_State24", type=fsm_RuntimeConcept1, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_RuntimeConcept123", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_RuntimeConcept2, fsm_RuntimeConcept1, fsm_Transition, fsm_FSM, fsm_State},
    associations={initialState2, finalState3, myFoos6, owningFSM7, outgoingTransition10, incomingTransition13, source16, ownedState0, target19, myState22},
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