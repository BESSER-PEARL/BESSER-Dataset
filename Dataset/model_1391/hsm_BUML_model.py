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
HSM_InitialState = Class(name="HSM_InitialState")
HSM_State = Class(name="HSM_State")
HSM_CompositeState = Class(name="HSM_CompositeState")
HSM_StateMachine = Class(name="HSM_StateMachine")
HSM_Transition = Class(name="HSM_Transition")
HSM_FinalState = Class(name="HSM_FinalState")

# State class attributes and methods

# HSM_InitialState class attributes and methods

# HSM_State class attributes and methods
HSM_State_name: Property = Property(name="name", type=StringType)
HSM_State.attributes={HSM_State_name}

# HSM_CompositeState class attributes and methods

# HSM_StateMachine class attributes and methods

# HSM_Transition class attributes and methods
HSM_Transition_trigger: Property = Property(name="trigger", type=StringType)
HSM_Transition_effect: Property = Property(name="effect", type=StringType)
HSM_Transition.attributes={HSM_Transition_trigger, HSM_Transition_effect}

# HSM_FinalState class attributes and methods

# Relationships
owningStateMachine7: BinaryAssociation = BinaryAssociation(
    name="owningStateMachine7",
    ends={
        Property(name="StateMachine8", type=HSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTransition", type=HSM_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
owningCompositeState9: BinaryAssociation = BinaryAssociation(
    name="owningCompositeState9",
    ends={
        Property(name="HSM_CompositeState11", type=HSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="HSM_Transition10", type=HSM_CompositeState, multiplicity=Multiplicity(0, 1))
    }
)
ownedSubState12: BinaryAssociation = BinaryAssociation(
    name="ownedSubState12",
    ends={
        Property(name="HSM_State14", type=HSM_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="HSM_CompositeState13", type=HSM_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubTransition15: BinaryAssociation = BinaryAssociation(
    name="ownedSubTransition15",
    ends={
        Property(name="HSM_Transition17", type=HSM_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="HSM_CompositeState16", type=HSM_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedState18: BinaryAssociation = BinaryAssociation(
    name="ownedState18",
    ends={
        Property(name="State", type=HSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="owningStateMachine", type=HSM_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedTransition19: BinaryAssociation = BinaryAssociation(
    name="ownedTransition19",
    ends={
        Property(name="Transition", type=HSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="owningStateMachine20", type=HSM_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningCompositeState0: BinaryAssociation = BinaryAssociation(
    name="owningCompositeState0",
    ends={
        Property(name="HSM_CompositeState", type=HSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="HSM_State", type=HSM_CompositeState, multiplicity=Multiplicity(0, 1))
    }
)
owningStateMachine1: BinaryAssociation = BinaryAssociation(
    name="owningStateMachine1",
    ends={
        Property(name="StateMachine", type=HSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedState", type=HSM_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
target2: BinaryAssociation = BinaryAssociation(
    name="target2",
    ends={
        Property(name="HSM_State3", type=HSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="HSM_Transition", type=HSM_State, multiplicity=Multiplicity(1, 1))
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="HSM_State6", type=HSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="HSM_Transition5", type=HSM_State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_HSM_CompositeState_State = Generalization(general=State, specific=HSM_CompositeState)
gen_HSM_InitialState_State = Generalization(general=State, specific=HSM_InitialState)
gen_HSM_FinalState_State = Generalization(general=State, specific=HSM_FinalState)

# Domain Model
domain_model = DomainModel(
    name="HSM",
    types={State, HSM_InitialState, HSM_State, HSM_CompositeState, HSM_StateMachine, HSM_Transition, HSM_FinalState},
    associations={owningStateMachine7, owningCompositeState9, ownedSubState12, ownedSubTransition15, ownedState18, ownedTransition19, owningCompositeState0, owningStateMachine1, target2, source4},
    generalizations={gen_HSM_CompositeState_State, gen_HSM_InitialState_State, gen_HSM_FinalState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)