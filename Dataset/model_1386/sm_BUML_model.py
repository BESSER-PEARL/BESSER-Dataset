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
SM_State = Class(name="SM::State")
SM_StateMachine = Class(name="SM::StateMachine")
SM_Transition = Class(name="SM::Transition")
SM_InitialState = Class(name="SM::InitialState")
State = Class(name="State")
SM_FinalState = Class(name="SM::FinalState")

# SM_State class attributes and methods
SM_State_name: Property = Property(name="name", type=StringType)
SM_State.attributes={SM_State_name}

# SM_StateMachine class attributes and methods

# SM_Transition class attributes and methods
SM_Transition_trigger: Property = Property(name="trigger", type=StringType)
SM_Transition_effect: Property = Property(name="effect", type=StringType)
SM_Transition.attributes={SM_Transition_trigger, SM_Transition_effect}

# SM_InitialState class attributes and methods

# State class attributes and methods

# SM_FinalState class attributes and methods

# Relationships
owningStateMachine0: BinaryAssociation = BinaryAssociation(
    name="owningStateMachine0",
    ends={
        Property(name="StateMachine", type=SM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedState", type=SM_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
owningStateMachine5: BinaryAssociation = BinaryAssociation(
    name="owningStateMachine5",
    ends={
        Property(name="StateMachine6", type=SM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTransition", type=SM_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
ownedState7: BinaryAssociation = BinaryAssociation(
    name="ownedState7",
    ends={
        Property(name="State", type=SM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="owningStateMachine", type=SM_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedTransition8: BinaryAssociation = BinaryAssociation(
    name="ownedTransition8",
    ends={
        Property(name="Transition", type=SM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="owningStateMachine9", type=SM_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="SM_State", type=SM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="SM_Transition", type=SM_State, multiplicity=Multiplicity(1, 1))
    }
)
source2: BinaryAssociation = BinaryAssociation(
    name="source2",
    ends={
        Property(name="SM_State4", type=SM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="SM_Transition3", type=SM_State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_SM_InitialState_State = Generalization(general=State, specific=SM_InitialState)
gen_SM_FinalState_State = Generalization(general=State, specific=SM_FinalState)

# Domain Model
domain_model = DomainModel(
    name="SM",
    types={SM_State, SM_StateMachine, SM_Transition, SM_InitialState, State, SM_FinalState},
    associations={owningStateMachine0, owningStateMachine5, ownedState7, ownedTransition8, target1, source2},
    generalizations={gen_SM_InitialState_State, gen_SM_FinalState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)