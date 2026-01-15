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
fsmSample_Transition = Class(name="fsmSample::Transition")
fsmSample_Action = Class(name="fsmSample::Action")
fsmSample_FSM = Class(name="fsmSample::FSM")
fsmSample_State = Class(name="fsmSample::State")

# fsmSample_Transition class attributes and methods
fsmSample_Transition_input: Property = Property(name="input", type=StringType)
fsmSample_Transition_output: Property = Property(name="output", type=StringType)
fsmSample_Transition.attributes={fsmSample_Transition_input, fsmSample_Transition_output}

# fsmSample_Action class attributes and methods
fsmSample_Action_name: Property = Property(name="name", type=StringType)
fsmSample_Action.attributes={fsmSample_Action_name}

# fsmSample_FSM class attributes and methods
fsmSample_FSM_name: Property = Property(name="name", type=StringType)
fsmSample_FSM.attributes={fsmSample_FSM_name}

# fsmSample_State class attributes and methods
fsmSample_State_name: Property = Property(name="name", type=StringType)
fsmSample_State.attributes={fsmSample_State_name}

# Relationships
outgoingTransition13: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition13",
    ends={
        Property(name="fsmSample_Transition", type=fsmSample_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmSample_State14", type=fsmSample_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransition15: BinaryAssociation = BinaryAssociation(
    name="incomingTransition15",
    ends={
        Property(name="fsmSample_Transition17", type=fsmSample_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmSample_State16", type=fsmSample_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source18: BinaryAssociation = BinaryAssociation(
    name="source18",
    ends={
        Property(name="fsmSample_State20", type=fsmSample_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmSample_Transition19", type=fsmSample_State, multiplicity=Multiplicity(1, 1))
    }
)
target21: BinaryAssociation = BinaryAssociation(
    name="target21",
    ends={
        Property(name="fsmSample_State23", type=fsmSample_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmSample_Transition22", type=fsmSample_State, multiplicity=Multiplicity(1, 1))
    }
)
action24: BinaryAssociation = BinaryAssociation(
    name="action24",
    ends={
        Property(name="fsmSample_Action", type=fsmSample_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmSample_Transition25", type=fsmSample_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedState0: BinaryAssociation = BinaryAssociation(
    name="ownedState0",
    ends={
        Property(name="fsmSample_State", type=fsmSample_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmSample_FSM", type=fsmSample_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="fsmSample_State3", type=fsmSample_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmSample_FSM2", type=fsmSample_State, multiplicity=Multiplicity(1, 1))
    }
)
finalState4: BinaryAssociation = BinaryAssociation(
    name="finalState4",
    ends={
        Property(name="fsmSample_State6", type=fsmSample_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmSample_FSM5", type=fsmSample_State, multiplicity=Multiplicity(1, 9999))
    }
)
currentState7: BinaryAssociation = BinaryAssociation(
    name="currentState7",
    ends={
        Property(name="fsmSample_State9", type=fsmSample_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmSample_FSM8", type=fsmSample_State, multiplicity=Multiplicity(1, 1))
    }
)
owningFSM10: BinaryAssociation = BinaryAssociation(
    name="owningFSM10",
    ends={
        Property(name="fsmSample_FSM12", type=fsmSample_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmSample_State11", type=fsmSample_FSM, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="fsmSample",
    types={fsmSample_Transition, fsmSample_Action, fsmSample_FSM, fsmSample_State},
    associations={outgoingTransition13, incomingTransition15, source18, target21, action24, ownedState0, initialState1, finalState4, currentState7, owningFSM10},
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