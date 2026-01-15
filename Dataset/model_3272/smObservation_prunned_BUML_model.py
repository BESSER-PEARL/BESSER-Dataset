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
sm_StateMachine = Class(name="sm::StateMachine")
sm_State = Class(name="sm::State")
sm_Transition = Class(name="sm::Transition")

# sm_StateMachine class attributes and methods
sm_StateMachine_name: Property = Property(name="name", type=StringType)
sm_StateMachine.attributes={sm_StateMachine_name}

# sm_State class attributes and methods
sm_State_name: Property = Property(name="name", type=StringType)
sm_State.attributes={sm_State_name}

# sm_Transition class attributes and methods
sm_Transition_name: Property = Property(name="name", type=StringType)
sm_Transition.attributes={sm_Transition_name}

# Relationships
target15: BinaryAssociation = BinaryAssociation(
    name="target15",
    ends={
        Property(name="sm_State17", type=sm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_Transition16", type=sm_State, multiplicity=Multiplicity(1, 1))
    }
)
initial0: BinaryAssociation = BinaryAssociation(
    name="initial0",
    ends={
        Property(name="sm_State", type=sm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_StateMachine", type=sm_State, multiplicity=Multiplicity(0, 1))
    }
)
final1: BinaryAssociation = BinaryAssociation(
    name="final1",
    ends={
        Property(name="sm_State3", type=sm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_StateMachine2", type=sm_State, multiplicity=Multiplicity(0, 9999))
    }
)
nodes4: BinaryAssociation = BinaryAssociation(
    name="nodes4",
    ends={
        Property(name="sm_State6", type=sm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_StateMachine5", type=sm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges7: BinaryAssociation = BinaryAssociation(
    name="edges7",
    ends={
        Property(name="sm_Transition", type=sm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_StateMachine8", type=sm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subMachines9: BinaryAssociation = BinaryAssociation(
    name="subMachines9",
    ends={
        Property(name="sm_StateMachine11", type=sm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_State10", type=sm_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source12: BinaryAssociation = BinaryAssociation(
    name="source12",
    ends={
        Property(name="sm_State14", type=sm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_Transition13", type=sm_State, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="sm",
    types={sm_StateMachine, sm_State, sm_Transition},
    associations={target15, initial0, final1, nodes4, edges7, subMachines9, source12},
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