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
NHSM_State = Class(name="NHSM::State")
NHSM_StateMachine = Class(name="NHSM::StateMachine")
NHSM_Transition = Class(name="NHSM::Transition")
NHSM_InitialState = Class(name="NHSM::InitialState")
State = Class(name="State")
NHSM_FinalState = Class(name="NHSM::FinalState")

# NHSM_State class attributes and methods
NHSM_State_name: Property = Property(name="name", type=StringType)
NHSM_State_memRequirement: Property = Property(name="memRequirement", type=IntegerType)
NHSM_State.attributes={NHSM_State_name, NHSM_State_memRequirement}

# NHSM_StateMachine class attributes and methods

# NHSM_Transition class attributes and methods
NHSM_Transition_trigger: Property = Property(name="trigger", type=StringType)
NHSM_Transition_effect: Property = Property(name="effect", type=StringType)
NHSM_Transition_cost: Property = Property(name="cost", type=IntegerType)
NHSM_Transition.attributes={NHSM_Transition_trigger, NHSM_Transition_effect, NHSM_Transition_cost}

# NHSM_InitialState class attributes and methods

# State class attributes and methods

# NHSM_FinalState class attributes and methods

# Relationships
owningStateMachine0: BinaryAssociation = BinaryAssociation(
    name="owningStateMachine0",
    ends={
        Property(name="StateMachine", type=NHSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedState", type=NHSM_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="NHSM_State", type=NHSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="NHSM_Transition", type=NHSM_State, multiplicity=Multiplicity(1, 1))
    }
)
source2: BinaryAssociation = BinaryAssociation(
    name="source2",
    ends={
        Property(name="NHSM_State4", type=NHSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="NHSM_Transition3", type=NHSM_State, multiplicity=Multiplicity(1, 1))
    }
)
ownedTransition8: BinaryAssociation = BinaryAssociation(
    name="ownedTransition8",
    ends={
        Property(name="Transition", type=NHSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="owningStateMachine9", type=NHSM_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningStateMachine5: BinaryAssociation = BinaryAssociation(
    name="owningStateMachine5",
    ends={
        Property(name="StateMachine6", type=NHSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTransition", type=NHSM_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
ownedState7: BinaryAssociation = BinaryAssociation(
    name="ownedState7",
    ends={
        Property(name="State", type=NHSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="owningStateMachine", type=NHSM_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_NHSM_InitialState_State = Generalization(general=State, specific=NHSM_InitialState)
gen_NHSM_FinalState_State = Generalization(general=State, specific=NHSM_FinalState)

# Domain Model
domain_model = DomainModel(
    name="NHSM",
    types={NHSM_State, NHSM_StateMachine, NHSM_Transition, NHSM_InitialState, State, NHSM_FinalState},
    associations={owningStateMachine0, target1, source2, ownedTransition8, owningStateMachine5, ownedState7},
    generalizations={gen_NHSM_InitialState_State, gen_NHSM_FinalState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)