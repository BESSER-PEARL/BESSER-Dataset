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
simplefsm_FSM = Class(name="simplefsm::FSM")
simplefsm_State = Class(name="simplefsm::State")
simplefsm_Transition = Class(name="simplefsm::Transition")

# simplefsm_FSM class attributes and methods

# simplefsm_State class attributes and methods
simplefsm_State_name: Property = Property(name="name", type=StringType)
simplefsm_State.attributes={simplefsm_State_name}

# simplefsm_Transition class attributes and methods

# Relationships
ownedState0: BinaryAssociation = BinaryAssociation(
    name="ownedState0",
    ends={
        Property(name="1", type=simplefsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=simplefsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState2: BinaryAssociation = BinaryAssociation(
    name="initialState2",
    ends={
        Property(name="simplefsm_State", type=simplefsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="simplefsm_FSM", type=simplefsm_State, multiplicity=Multiplicity(1, 1))
    }
)
owningFSM3: BinaryAssociation = BinaryAssociation(
    name="owningFSM3",
    ends={
        Property(name="5", type=simplefsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="4", type=simplefsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransition6: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition6",
    ends={
        Property(name="8", type=simplefsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="7", type=simplefsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransition9: BinaryAssociation = BinaryAssociation(
    name="incomingTransition9",
    ends={
        Property(name="11", type=simplefsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="10", type=simplefsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source12: BinaryAssociation = BinaryAssociation(
    name="source12",
    ends={
        Property(name="14", type=simplefsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="13", type=simplefsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target15: BinaryAssociation = BinaryAssociation(
    name="target15",
    ends={
        Property(name="17", type=simplefsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="16", type=simplefsm_State, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="simplefsm",
    types={simplefsm_FSM, simplefsm_State, simplefsm_Transition},
    associations={ownedState0, initialState2, owningFSM3, outgoingTransition6, incomingTransition9, source12, target15},
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