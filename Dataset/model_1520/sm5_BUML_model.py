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
sm6_StateMachine = Class(name="sm6::StateMachine")
sm6_State = Class(name="sm6::State")
sm6_Transition = Class(name="sm6::Transition")

# sm6_StateMachine class attributes and methods

# sm6_State class attributes and methods
sm6_State_name: Property = Property(name="name", type=StringType)
sm6_State_isFinal: Property = Property(name="isFinal", type=StringType)
sm6_State.attributes={sm6_State_name, sm6_State_isFinal}

# sm6_Transition class attributes and methods
sm6_Transition_event: Property = Property(name="event", type=StringType)
sm6_Transition.attributes={sm6_Transition_event}

# Relationships
src8: BinaryAssociation = BinaryAssociation(
    name="src8",
    ends={
        Property(name="State9", type=sm6_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=sm6_State, multiplicity=Multiplicity(1, 1))
    }
)
initialState0: BinaryAssociation = BinaryAssociation(
    name="initialState0",
    ends={
        Property(name="sm6_State", type=sm6_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm6_StateMachine", type=sm6_State, multiplicity=Multiplicity(0, 1))
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="State", type=sm6_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm", type=sm6_State, multiplicity=Multiplicity(0, 9999))
    }
)
edges2: BinaryAssociation = BinaryAssociation(
    name="edges2",
    ends={
        Property(name="sm6_Transition", type=sm6_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm6_StateMachine3", type=sm6_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sm4: BinaryAssociation = BinaryAssociation(
    name="sm4",
    ends={
        Property(name="StateMachine", type=sm6_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=sm6_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
outgoing5: BinaryAssociation = BinaryAssociation(
    name="outgoing5",
    ends={
        Property(name="Transition", type=sm6_State, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=sm6_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming6: BinaryAssociation = BinaryAssociation(
    name="incoming6",
    ends={
        Property(name="Transition7", type=sm6_State, multiplicity=Multiplicity(1, 1)),
        Property(name="tgt", type=sm6_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
tgt10: BinaryAssociation = BinaryAssociation(
    name="tgt10",
    ends={
        Property(name="State11", type=sm6_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=sm6_State, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="sm6",
    types={sm6_StateMachine, sm6_State, sm6_Transition},
    associations={src8, initialState0, states1, edges2, sm4, outgoing5, incoming6, tgt10},
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