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
simplefsm_FSM = Class(name="simplefsm_FSM")
simplefsm_State = Class(name="simplefsm_State")
simplefsm_Transition = Class(name="simplefsm_Transition")

# simplefsm_FSM class attributes and methods

# simplefsm_State class attributes and methods
simplefsm_State_name: Property = Property(name="name", type=StringType)
simplefsm_State.attributes={simplefsm_State_name}

# simplefsm_Transition class attributes and methods

# Relationships
ownedState0: BinaryAssociation = BinaryAssociation(
    name="ownedState0",
    ends={
        Property(name="State", type=simplefsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=simplefsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="simplefsm_State", type=simplefsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="simplefsm_FSM", type=simplefsm_State, multiplicity=Multiplicity(1, 1))
    }
)
owningFSM2: BinaryAssociation = BinaryAssociation(
    name="owningFSM2",
    ends={
        Property(name="FSM", type=simplefsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedState", type=simplefsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransition3: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition3",
    ends={
        Property(name="Transition", type=simplefsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=simplefsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransition4: BinaryAssociation = BinaryAssociation(
    name="incomingTransition4",
    ends={
        Property(name="Transition5", type=simplefsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=simplefsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source6: BinaryAssociation = BinaryAssociation(
    name="source6",
    ends={
        Property(name="State7", type=simplefsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransition", type=simplefsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target8: BinaryAssociation = BinaryAssociation(
    name="target8",
    ends={
        Property(name="State9", type=simplefsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransition", type=simplefsm_State, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="simplefsm",
    types={simplefsm_FSM, simplefsm_State, simplefsm_Transition},
    associations={ownedState0, initialState1, owningFSM2, outgoingTransition3, incomingTransition4, source6, target8},
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