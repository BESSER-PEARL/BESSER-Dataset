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
fsm_FSM_name: Property = Property(name="name", type=StringType)
fsm_FSM.attributes={fsm_FSM_name}

# fsm_State class attributes and methods
fsm_State_name: Property = Property(name="name", type=StringType)
fsm_State.attributes={fsm_State_name}

# fsm_Transition class attributes and methods
fsm_Transition_input: Property = Property(name="input", type=StringType)
fsm_Transition_output: Property = Property(name="output", type=StringType)
fsm_Transition.attributes={fsm_Transition_output, fsm_Transition_input}

# Relationships
initialState5: BinaryAssociation = BinaryAssociation(
    name="initialState5",
    ends={
        Property(name="fsm_State", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransitions6: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions6",
    ends={
        Property(name="8", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="7", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions9: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions9",
    ends={
        Property(name="11", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="10", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
containingFSM12: BinaryAssociation = BinaryAssociation(
    name="containingFSM12",
    ends={
        Property(name="14", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="13", type=fsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)
target15: BinaryAssociation = BinaryAssociation(
    name="target15",
    ends={
        Property(name="17", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="16", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="1", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions2: BinaryAssociation = BinaryAssociation(
    name="transitions2",
    ends={
        Property(name="4", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="3", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source18: BinaryAssociation = BinaryAssociation(
    name="source18",
    ends={
        Property(name="20", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="19", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
containingFSM21: BinaryAssociation = BinaryAssociation(
    name="containingFSM21",
    ends={
        Property(name="23", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="22", type=fsm_FSM, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_FSM, fsm_State, fsm_Transition},
    associations={initialState5, outgoingTransitions6, incomingTransitions9, containingFSM12, target15, states0, transitions2, source18, containingFSM21},
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