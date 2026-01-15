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
fsm_State_initial: Property = Property(name="initial", type=BooleanType)
fsm_State_final: Property = Property(name="final", type=BooleanType)
fsm_State.attributes={fsm_State_name, fsm_State_initial, fsm_State_final}

# fsm_Transition class attributes and methods
fsm_Transition_input: Property = Property(name="input", type=StringType)
fsm_Transition_output: Property = Property(name="output", type=StringType)
fsm_Transition.attributes={fsm_Transition_output, fsm_Transition_input}

# Relationships
ownedState0: BinaryAssociation = BinaryAssociation(
    name="ownedState0",
    ends={
        Property(name="State", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningFSM1: BinaryAssociation = BinaryAssociation(
    name="owningFSM1",
    ends={
        Property(name="FSM", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedState", type=fsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransition2: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition2",
    ends={
        Property(name="Transition", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransition3: BinaryAssociation = BinaryAssociation(
    name="incomingTransition3",
    ends={
        Property(name="Transition4", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source5: BinaryAssociation = BinaryAssociation(
    name="source5",
    ends={
        Property(name="State6", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransition", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target7: BinaryAssociation = BinaryAssociation(
    name="target7",
    ends={
        Property(name="State8", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransition", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_FSM, fsm_State, fsm_Transition},
    associations={ownedState0, owningFSM1, outgoingTransition2, incomingTransition3, source5, target7},
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