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
sm_Observation = Class(name="sm::Observation")

# sm_StateMachine class attributes and methods
sm_StateMachine_name: Property = Property(name="name", type=StringType)
sm_StateMachine.attributes={sm_StateMachine_name}

# sm_State class attributes and methods
sm_State_name: Property = Property(name="name", type=StringType)
sm_State.attributes={sm_State_name}

# sm_Transition class attributes and methods
sm_Transition_name: Property = Property(name="name", type=StringType)
sm_Transition.attributes={sm_Transition_name}

# sm_Observation class attributes and methods
sm_Observation_time: Property = Property(name="time", type=StringType)
sm_Observation.attributes={sm_Observation_time}

# Relationships
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
marks9: BinaryAssociation = BinaryAssociation(
    name="marks9",
    ends={
        Property(name="sm_Observation", type=sm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_StateMachine10", type=sm_Observation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subMachines11: BinaryAssociation = BinaryAssociation(
    name="subMachines11",
    ends={
        Property(name="sm_StateMachine13", type=sm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_State12", type=sm_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mark14: BinaryAssociation = BinaryAssociation(
    name="mark14",
    ends={
        Property(name="sm_Observation16", type=sm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_State15", type=sm_Observation, multiplicity=Multiplicity(0, 1))
    }
)
graph17: BinaryAssociation = BinaryAssociation(
    name="graph17",
    ends={
        Property(name="sm_StateMachine19", type=sm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_State18", type=sm_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
source20: BinaryAssociation = BinaryAssociation(
    name="source20",
    ends={
        Property(name="sm_State22", type=sm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_Transition21", type=sm_State, multiplicity=Multiplicity(1, 1))
    }
)
target23: BinaryAssociation = BinaryAssociation(
    name="target23",
    ends={
        Property(name="sm_State25", type=sm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_Transition24", type=sm_State, multiplicity=Multiplicity(1, 1))
    }
)
initial0: BinaryAssociation = BinaryAssociation(
    name="initial0",
    ends={
        Property(name="sm_State", type=sm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_StateMachine", type=sm_State, multiplicity=Multiplicity(0, 1))
    }
)
node29: BinaryAssociation = BinaryAssociation(
    name="node29",
    ends={
        Property(name="sm_State31", type=sm_Observation, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_Observation30", type=sm_State, multiplicity=Multiplicity(1, 1))
    }
)
graph32: BinaryAssociation = BinaryAssociation(
    name="graph32",
    ends={
        Property(name="sm_StateMachine34", type=sm_Observation, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_Observation33", type=sm_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
graph26: BinaryAssociation = BinaryAssociation(
    name="graph26",
    ends={
        Property(name="sm_StateMachine28", type=sm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_Transition27", type=sm_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="sm",
    types={sm_StateMachine, sm_State, sm_Transition, sm_Observation},
    associations={final1, nodes4, edges7, marks9, subMachines11, mark14, graph17, source20, target23, initial0, node29, graph32, graph26},
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