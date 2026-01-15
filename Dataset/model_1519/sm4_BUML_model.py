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
sm4_StateMachine = Class(name="sm4::StateMachine")
State = Class(name="State")
sm4_State = Class(name="sm4::State")
sm4_Transition = Class(name="sm4::Transition")

# sm4_StateMachine class attributes and methods

# State class attributes and methods

# sm4_State class attributes and methods
sm4_State_name: Property = Property(name="name", type=StringType)
sm4_State.attributes={sm4_State_name}

# sm4_Transition class attributes and methods
sm4_Transition_event: Property = Property(name="event", type=StringType)
sm4_Transition.attributes={sm4_Transition_event}

# Relationships
initialState0: BinaryAssociation = BinaryAssociation(
    name="initialState0",
    ends={
        Property(name="sm4_State", type=sm4_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm4_StateMachine", type=sm4_State, multiplicity=Multiplicity(0, 1))
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="State", type=sm4_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm", type=sm4_State, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing5: BinaryAssociation = BinaryAssociation(
    name="outgoing5",
    ends={
        Property(name="Transition", type=sm4_State, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=sm4_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming6: BinaryAssociation = BinaryAssociation(
    name="incoming6",
    ends={
        Property(name="Transition7", type=sm4_State, multiplicity=Multiplicity(1, 1)),
        Property(name="tgt", type=sm4_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
edges2: BinaryAssociation = BinaryAssociation(
    name="edges2",
    ends={
        Property(name="sm4_Transition", type=sm4_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm4_StateMachine3", type=sm4_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sm4: BinaryAssociation = BinaryAssociation(
    name="sm4",
    ends={
        Property(name="StateMachine", type=sm4_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=sm4_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
src8: BinaryAssociation = BinaryAssociation(
    name="src8",
    ends={
        Property(name="State9", type=sm4_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=sm4_State, multiplicity=Multiplicity(1, 1))
    }
)
tgt10: BinaryAssociation = BinaryAssociation(
    name="tgt10",
    ends={
        Property(name="State11", type=sm4_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=sm4_State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_sm4_StateMachine_State = Generalization(general=State, specific=sm4_StateMachine)

# Domain Model
domain_model = DomainModel(
    name="sm4",
    types={sm4_StateMachine, State, sm4_State, sm4_Transition},
    associations={initialState0, states1, outgoing5, incoming6, edges2, sm4, src8, tgt10},
    generalizations={gen_sm4_StateMachine_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)