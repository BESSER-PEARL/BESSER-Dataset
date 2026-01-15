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
sm2_State = Class(name="sm2::State")
sm2_Transition = Class(name="sm2::Transition")
sm2_StateMachine = Class(name="sm2::StateMachine")

# sm2_State class attributes and methods
sm2_State_name: Property = Property(name="name", type=StringType)
sm2_State.attributes={sm2_State_name}

# sm2_Transition class attributes and methods
sm2_Transition_event: Property = Property(name="event", type=StringType)
sm2_Transition.attributes={sm2_Transition_event}

# sm2_StateMachine class attributes and methods

# Relationships
initialState0: BinaryAssociation = BinaryAssociation(
    name="initialState0",
    ends={
        Property(name="sm2_State", type=sm2_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm2_StateMachine", type=sm2_State, multiplicity=Multiplicity(0, 9999))
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="State", type=sm2_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm", type=sm2_State, multiplicity=Multiplicity(0, 9999))
    }
)
edges2: BinaryAssociation = BinaryAssociation(
    name="edges2",
    ends={
        Property(name="sm2_Transition", type=sm2_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm2_StateMachine3", type=sm2_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sm4: BinaryAssociation = BinaryAssociation(
    name="sm4",
    ends={
        Property(name="StateMachine", type=sm2_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=sm2_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
tgt10: BinaryAssociation = BinaryAssociation(
    name="tgt10",
    ends={
        Property(name="State11", type=sm2_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=sm2_State, multiplicity=Multiplicity(1, 1))
    }
)
outgoing5: BinaryAssociation = BinaryAssociation(
    name="outgoing5",
    ends={
        Property(name="Transition", type=sm2_State, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=sm2_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming6: BinaryAssociation = BinaryAssociation(
    name="incoming6",
    ends={
        Property(name="Transition7", type=sm2_State, multiplicity=Multiplicity(1, 1)),
        Property(name="tgt", type=sm2_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
src8: BinaryAssociation = BinaryAssociation(
    name="src8",
    ends={
        Property(name="State9", type=sm2_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=sm2_State, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="sm2",
    types={sm2_State, sm2_Transition, sm2_StateMachine},
    associations={initialState0, states1, edges2, sm4, tgt10, outgoing5, incoming6, src8},
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