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
SimpleHierarchicalStateMachine_State = Class(name="SimpleHierarchicalStateMachine::State")
SimpleHierarchicalStateMachine_CompositeState = Class(name="SimpleHierarchicalStateMachine::CompositeState")
SimpleHierarchicalStateMachine_Transition = Class(name="SimpleHierarchicalStateMachine::Transition")
SimpleHierarchicalStateMachine_StateMachine = Class(name="SimpleHierarchicalStateMachine::StateMachine")
SimpleHierarchicalStateMachine_InitialState = Class(name="SimpleHierarchicalStateMachine::InitialState")
SimpleHierarchicalStateMachine_FinalState = Class(name="SimpleHierarchicalStateMachine::FinalState")
State = Class(name="State")

# SimpleHierarchicalStateMachine_State class attributes and methods
SimpleHierarchicalStateMachine_State_name: Property = Property(name="name", type=StringType)
SimpleHierarchicalStateMachine_State.attributes={SimpleHierarchicalStateMachine_State_name}

# SimpleHierarchicalStateMachine_CompositeState class attributes and methods

# SimpleHierarchicalStateMachine_Transition class attributes and methods
SimpleHierarchicalStateMachine_Transition_trigger: Property = Property(name="trigger", type=StringType)
SimpleHierarchicalStateMachine_Transition_effect: Property = Property(name="effect", type=StringType)
SimpleHierarchicalStateMachine_Transition.attributes={SimpleHierarchicalStateMachine_Transition_effect, SimpleHierarchicalStateMachine_Transition_trigger}

# SimpleHierarchicalStateMachine_StateMachine class attributes and methods

# SimpleHierarchicalStateMachine_InitialState class attributes and methods

# SimpleHierarchicalStateMachine_FinalState class attributes and methods

# State class attributes and methods

# Relationships
owningCompositeState0: BinaryAssociation = BinaryAssociation(
    name="owningCompositeState0",
    ends={
        Property(name="SimpleHierarchicalStateMachine_CompositeState", type=SimpleHierarchicalStateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleHierarchicalStateMachine_State", type=SimpleHierarchicalStateMachine_CompositeState, multiplicity=Multiplicity(0, 1))
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="SimpleHierarchicalStateMachine_State2", type=SimpleHierarchicalStateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleHierarchicalStateMachine_Transition", type=SimpleHierarchicalStateMachine_State, multiplicity=Multiplicity(1, 1))
    }
)
ownedSubState6: BinaryAssociation = BinaryAssociation(
    name="ownedSubState6",
    ends={
        Property(name="SimpleHierarchicalStateMachine_State8", type=SimpleHierarchicalStateMachine_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleHierarchicalStateMachine_CompositeState7", type=SimpleHierarchicalStateMachine_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedState9: BinaryAssociation = BinaryAssociation(
    name="ownedState9",
    ends={
        Property(name="SimpleHierarchicalStateMachine_State10", type=SimpleHierarchicalStateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleHierarchicalStateMachine_StateMachine", type=SimpleHierarchicalStateMachine_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedTransition11: BinaryAssociation = BinaryAssociation(
    name="ownedTransition11",
    ends={
        Property(name="SimpleHierarchicalStateMachine_Transition13", type=SimpleHierarchicalStateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleHierarchicalStateMachine_StateMachine12", type=SimpleHierarchicalStateMachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="SimpleHierarchicalStateMachine_State5", type=SimpleHierarchicalStateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleHierarchicalStateMachine_Transition4", type=SimpleHierarchicalStateMachine_State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_SimpleHierarchicalStateMachine_InitialState_State = Generalization(general=State, specific=SimpleHierarchicalStateMachine_InitialState)
gen_SimpleHierarchicalStateMachine_FinalState_State = Generalization(general=State, specific=SimpleHierarchicalStateMachine_FinalState)
gen_SimpleHierarchicalStateMachine_CompositeState_State = Generalization(general=State, specific=SimpleHierarchicalStateMachine_CompositeState)

# Domain Model
domain_model = DomainModel(
    name="SimpleHierarchicalStateMachine",
    types={SimpleHierarchicalStateMachine_State, SimpleHierarchicalStateMachine_CompositeState, SimpleHierarchicalStateMachine_Transition, SimpleHierarchicalStateMachine_StateMachine, SimpleHierarchicalStateMachine_InitialState, SimpleHierarchicalStateMachine_FinalState, State},
    associations={owningCompositeState0, target1, ownedSubState6, ownedState9, ownedTransition11, source3},
    generalizations={gen_SimpleHierarchicalStateMachine_InitialState_State, gen_SimpleHierarchicalStateMachine_FinalState_State, gen_SimpleHierarchicalStateMachine_CompositeState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)