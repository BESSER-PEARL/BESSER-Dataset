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
sm3_StateMachine = Class(name="sm3::StateMachine")
sm3_State = Class(name="sm3::State")
sm3_Transition = Class(name="sm3::Transition")

# sm3_StateMachine class attributes and methods

# sm3_State class attributes and methods
sm3_State_name: Property = Property(name="name", type=StringType)
sm3_State.attributes={sm3_State_name}

# sm3_Transition class attributes and methods
sm3_Transition_event: Property = Property(name="event", type=StringType)
sm3_Transition.attributes={sm3_Transition_event}

# Relationships
edges2: BinaryAssociation = BinaryAssociation(
    name="edges2",
    ends={
        Property(name="sm3_Transition", type=sm3_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm3_StateMachine3", type=sm3_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sm4: BinaryAssociation = BinaryAssociation(
    name="sm4",
    ends={
        Property(name="StateMachine", type=sm3_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=sm3_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
initialState0: BinaryAssociation = BinaryAssociation(
    name="initialState0",
    ends={
        Property(name="sm3_State", type=sm3_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm3_StateMachine", type=sm3_State, multiplicity=Multiplicity(1, 1))
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="State", type=sm3_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm", type=sm3_State, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing5: BinaryAssociation = BinaryAssociation(
    name="outgoing5",
    ends={
        Property(name="Transition", type=sm3_State, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=sm3_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming6: BinaryAssociation = BinaryAssociation(
    name="incoming6",
    ends={
        Property(name="Transition7", type=sm3_State, multiplicity=Multiplicity(1, 1)),
        Property(name="tgt", type=sm3_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
src8: BinaryAssociation = BinaryAssociation(
    name="src8",
    ends={
        Property(name="State9", type=sm3_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=sm3_State, multiplicity=Multiplicity(1, 1))
    }
)
tgt10: BinaryAssociation = BinaryAssociation(
    name="tgt10",
    ends={
        Property(name="State11", type=sm3_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=sm3_State, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="sm3",
    types={sm3_StateMachine, sm3_State, sm3_Transition},
    associations={edges2, sm4, initialState0, states1, outgoing5, incoming6, src8, tgt10},
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