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
sm1_StateMachine = Class(name="sm1::StateMachine")
sm1_State = Class(name="sm1::State")
sm1_Transition = Class(name="sm1::Transition")

# sm1_StateMachine class attributes and methods

# sm1_State class attributes and methods
sm1_State_name: Property = Property(name="name", type=StringType)
sm1_State.attributes={sm1_State_name}

# sm1_Transition class attributes and methods
sm1_Transition_event: Property = Property(name="event", type=StringType)
sm1_Transition.attributes={sm1_Transition_event}

# Relationships
initialState0: BinaryAssociation = BinaryAssociation(
    name="initialState0",
    ends={
        Property(name="sm1_State", type=sm1_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm1_StateMachine", type=sm1_State, multiplicity=Multiplicity(0, 1))
    }
)
src8: BinaryAssociation = BinaryAssociation(
    name="src8",
    ends={
        Property(name="State9", type=sm1_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=sm1_State, multiplicity=Multiplicity(1, 1))
    }
)
tgt10: BinaryAssociation = BinaryAssociation(
    name="tgt10",
    ends={
        Property(name="State11", type=sm1_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=sm1_State, multiplicity=Multiplicity(1, 1))
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="State", type=sm1_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm", type=sm1_State, multiplicity=Multiplicity(0, 9999))
    }
)
edges2: BinaryAssociation = BinaryAssociation(
    name="edges2",
    ends={
        Property(name="sm1_Transition", type=sm1_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm1_StateMachine3", type=sm1_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sm4: BinaryAssociation = BinaryAssociation(
    name="sm4",
    ends={
        Property(name="StateMachine", type=sm1_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=sm1_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
outgoing5: BinaryAssociation = BinaryAssociation(
    name="outgoing5",
    ends={
        Property(name="Transition", type=sm1_State, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=sm1_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming6: BinaryAssociation = BinaryAssociation(
    name="incoming6",
    ends={
        Property(name="Transition7", type=sm1_State, multiplicity=Multiplicity(1, 1)),
        Property(name="tgt", type=sm1_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="sm1",
    types={sm1_StateMachine, sm1_State, sm1_Transition},
    associations={initialState0, src8, tgt10, states1, edges2, sm4, outgoing5, incoming6},
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