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
minifsm_FSM = Class(name="minifsm::FSM")
minifsm_State = Class(name="minifsm::State")
minifsm_Transition = Class(name="minifsm::Transition")
minifsm_FinalState = Class(name="minifsm::FinalState")
State = Class(name="State")

# minifsm_FSM class attributes and methods

# minifsm_State class attributes and methods
minifsm_State_name: Property = Property(name="name", type=StringType)
minifsm_State.attributes={minifsm_State_name}

# minifsm_Transition class attributes and methods
minifsm_Transition_event: Property = Property(name="event", type=StringType)
minifsm_Transition.attributes={minifsm_Transition_event}

# minifsm_FinalState class attributes and methods

# State class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="State", type=minifsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm", type=minifsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="Transition", type=minifsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm2", type=minifsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState3: BinaryAssociation = BinaryAssociation(
    name="initialState3",
    ends={
        Property(name="minifsm_State", type=minifsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="minifsm_FSM", type=minifsm_State, multiplicity=Multiplicity(1, 1))
    }
)
fsm4: BinaryAssociation = BinaryAssociation(
    name="fsm4",
    ends={
        Property(name="FSM", type=minifsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=minifsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)
input5: BinaryAssociation = BinaryAssociation(
    name="input5",
    ends={
        Property(name="minifsm_State6", type=minifsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="minifsm_Transition", type=minifsm_State, multiplicity=Multiplicity(1, 1))
    }
)
output7: BinaryAssociation = BinaryAssociation(
    name="output7",
    ends={
        Property(name="minifsm_State9", type=minifsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="minifsm_Transition8", type=minifsm_State, multiplicity=Multiplicity(1, 1))
    }
)
fsm10: BinaryAssociation = BinaryAssociation(
    name="fsm10",
    ends={
        Property(name="FSM11", type=minifsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=minifsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_minifsm_FinalState_State = Generalization(general=State, specific=minifsm_FinalState)

# Domain Model
domain_model = DomainModel(
    name="minifsm",
    types={minifsm_FSM, minifsm_State, minifsm_Transition, minifsm_FinalState, State},
    associations={states0, transitions1, initialState3, fsm4, input5, output7, fsm10},
    generalizations={gen_minifsm_FinalState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)