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
State = Class(name="State")
UHSM_StateMachine = Class(name="UHSM_StateMachine")
UHSM_State = Class(name="UHSM_State")
TracedClass = Class(name="TracedClass")
UHSM_CompositeState = Class(name="UHSM_CompositeState")
UHSM_UTransition = Class(name="UHSM_UTransition")
Transition = Class(name="Transition")
UHSM_Transition = Class(name="UHSM_Transition")
UHSM_InitialState = Class(name="UHSM_InitialState")
UHSM_FinalState = Class(name="UHSM_FinalState")
UHSM_UState = Class(name="UHSM_UState")
UHSM_UStateMachine = Class(name="UHSM_UStateMachine")
StateMachine = Class(name="StateMachine")
UHSM_TracedClass = Class(name="UHSM_TracedClass", is_abstract=True)
UHSM_EObject = Class(name="UHSM_EObject")

# State class attributes and methods

# UHSM_StateMachine class attributes and methods
UHSM_StateMachine_name: Property = Property(name="name", type=StringType)
UHSM_StateMachine.attributes={UHSM_StateMachine_name}

# UHSM_State class attributes and methods
UHSM_State_name: Property = Property(name="name", type=StringType)
UHSM_State.attributes={UHSM_State_name}

# TracedClass class attributes and methods

# UHSM_CompositeState class attributes and methods

# UHSM_UTransition class attributes and methods

# Transition class attributes and methods

# UHSM_Transition class attributes and methods
UHSM_Transition_trigger: Property = Property(name="trigger", type=StringType)
UHSM_Transition_effect: Property = Property(name="effect", type=StringType)
UHSM_Transition_name: Property = Property(name="name", type=StringType)
UHSM_Transition.attributes={UHSM_Transition_name, UHSM_Transition_trigger, UHSM_Transition_effect}

# UHSM_InitialState class attributes and methods

# UHSM_FinalState class attributes and methods

# UHSM_UState class attributes and methods

# UHSM_UStateMachine class attributes and methods

# StateMachine class attributes and methods

# UHSM_TracedClass class attributes and methods
UHSM_TracedClass_trace: Property = Property(name="trace", type=StringType)
UHSM_TracedClass.attributes={UHSM_TracedClass_trace}

# UHSM_EObject class attributes and methods

# Relationships
ownedSubState8: BinaryAssociation = BinaryAssociation(
    name="ownedSubState8",
    ends={
        Property(name="UHSM_State10", type=UHSM_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="UHSM_CompositeState9", type=UHSM_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningCompositeState0: BinaryAssociation = BinaryAssociation(
    name="owningCompositeState0",
    ends={
        Property(name="UHSM_CompositeState", type=UHSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UHSM_State", type=UHSM_CompositeState, multiplicity=Multiplicity(0, 1))
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="UHSM_Transition", type=UHSM_UTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="UHSM_UTransition", type=UHSM_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
target2: BinaryAssociation = BinaryAssociation(
    name="target2",
    ends={
        Property(name="UHSM_State4", type=UHSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="UHSM_Transition3", type=UHSM_State, multiplicity=Multiplicity(0, 1))
    }
)
source5: BinaryAssociation = BinaryAssociation(
    name="source5",
    ends={
        Property(name="UHSM_State7", type=UHSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="UHSM_Transition6", type=UHSM_State, multiplicity=Multiplicity(0, 1))
    }
)
ownedState11: BinaryAssociation = BinaryAssociation(
    name="ownedState11",
    ends={
        Property(name="UHSM_State12", type=UHSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="UHSM_StateMachine", type=UHSM_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTransition13: BinaryAssociation = BinaryAssociation(
    name="ownedTransition13",
    ends={
        Property(name="UHSM_Transition15", type=UHSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="UHSM_StateMachine14", type=UHSM_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
States16: BinaryAssociation = BinaryAssociation(
    name="States16",
    ends={
        Property(name="UHSM_State17", type=UHSM_UState, multiplicity=Multiplicity(1, 1)),
        Property(name="UHSM_UState", type=UHSM_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
stateMachines18: BinaryAssociation = BinaryAssociation(
    name="stateMachines18",
    ends={
        Property(name="UHSM_StateMachine19", type=UHSM_UStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="UHSM_UStateMachine", type=UHSM_StateMachine, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ref20: BinaryAssociation = BinaryAssociation(
    name="ref20",
    ends={
        Property(name="UHSM_EObject", type=UHSM_TracedClass, multiplicity=Multiplicity(1, 1)),
        Property(name="UHSM_TracedClass", type=UHSM_EObject, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_UHSM_CompositeState_State = Generalization(general=State, specific=UHSM_CompositeState)
gen_UHSM_StateMachine_TracedClass = Generalization(general=TracedClass, specific=UHSM_StateMachine)
gen_UHSM_State_TracedClass = Generalization(general=TracedClass, specific=UHSM_State)
gen_UHSM_UTransition_Transition = Generalization(general=Transition, specific=UHSM_UTransition)
gen_UHSM_Transition_TracedClass = Generalization(general=TracedClass, specific=UHSM_Transition)
gen_UHSM_InitialState_State = Generalization(general=State, specific=UHSM_InitialState)
gen_UHSM_FinalState_State = Generalization(general=State, specific=UHSM_FinalState)
gen_UHSM_UState_State = Generalization(general=State, specific=UHSM_UState)
gen_UHSM_UStateMachine_StateMachine = Generalization(general=StateMachine, specific=UHSM_UStateMachine)

# Domain Model
domain_model = DomainModel(
    name="UHSM",
    types={State, UHSM_StateMachine, UHSM_State, TracedClass, UHSM_CompositeState, UHSM_UTransition, Transition, UHSM_Transition, UHSM_InitialState, UHSM_FinalState, UHSM_UState, UHSM_UStateMachine, StateMachine, UHSM_TracedClass, UHSM_EObject},
    associations={ownedSubState8, owningCompositeState0, transitions1, target2, source5, ownedState11, ownedTransition13, States16, stateMachines18, ref20},
    generalizations={gen_UHSM_CompositeState_State, gen_UHSM_StateMachine_TracedClass, gen_UHSM_State_TracedClass, gen_UHSM_UTransition_Transition, gen_UHSM_Transition_TracedClass, gen_UHSM_InitialState_State, gen_UHSM_FinalState_State, gen_UHSM_UState_State, gen_UHSM_UStateMachine_StateMachine},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)