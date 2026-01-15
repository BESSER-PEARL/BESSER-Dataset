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
kfsm_Action = Class(name="kfsm::Action")
kfsm_FSM = Class(name="kfsm::FSM")
kfsm_State = Class(name="kfsm::State")
kfsm_Transition = Class(name="kfsm::Transition")

# kfsm_Action class attributes and methods
kfsm_Action_id: Property = Property(name="id", type=StringType)
kfsm_Action.attributes={kfsm_Action_id}

# kfsm_FSM class attributes and methods

# kfsm_State class attributes and methods
kfsm_State_name: Property = Property(name="name", type=StringType)
kfsm_State.attributes={kfsm_State_name}

# kfsm_Transition class attributes and methods
kfsm_Transition_input: Property = Property(name="input", type=StringType)
kfsm_Transition_output: Property = Property(name="output", type=StringType)
kfsm_Transition.attributes={kfsm_Transition_output, kfsm_Transition_input}

# Relationships
s_action9: BinaryAssociation = BinaryAssociation(
    name="s_action9",
    ends={
        Property(name="kfsm_Action", type=kfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="kfsm_State10", type=kfsm_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source11: BinaryAssociation = BinaryAssociation(
    name="source11",
    ends={
        Property(name="State12", type=kfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransition", type=kfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target13: BinaryAssociation = BinaryAssociation(
    name="target13",
    ends={
        Property(name="State14", type=kfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransition", type=kfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
ownedState0: BinaryAssociation = BinaryAssociation(
    name="ownedState0",
    ends={
        Property(name="State", type=kfsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=kfsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="kfsm_State", type=kfsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="kfsm_FSM", type=kfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
finalState2: BinaryAssociation = BinaryAssociation(
    name="finalState2",
    ends={
        Property(name="kfsm_State4", type=kfsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="kfsm_FSM3", type=kfsm_State, multiplicity=Multiplicity(1, 9999))
    }
)
owningFSM5: BinaryAssociation = BinaryAssociation(
    name="owningFSM5",
    ends={
        Property(name="FSM", type=kfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedState", type=kfsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransition6: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition6",
    ends={
        Property(name="Transition", type=kfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=kfsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransition7: BinaryAssociation = BinaryAssociation(
    name="incomingTransition7",
    ends={
        Property(name="Transition8", type=kfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=kfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="kfsm",
    types={kfsm_Action, kfsm_FSM, kfsm_State, kfsm_Transition},
    associations={s_action9, source11, target13, ownedState0, initialState1, finalState2, owningFSM5, outgoingTransition6, incomingTransition7},
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