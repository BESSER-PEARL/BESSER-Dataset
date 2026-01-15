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
        Property(name="State", type=sm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=sm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges5: BinaryAssociation = BinaryAssociation(
    name="edges5",
    ends={
        Property(name="Transition", type=sm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="graph6", type=sm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
marks7: BinaryAssociation = BinaryAssociation(
    name="marks7",
    ends={
        Property(name="Observation", type=sm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="graph8", type=sm_Observation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subMachines9: BinaryAssociation = BinaryAssociation(
    name="subMachines9",
    ends={
        Property(name="sm_StateMachine11", type=sm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_State10", type=sm_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graph20: BinaryAssociation = BinaryAssociation(
    name="graph20",
    ends={
        Property(name="StateMachine21", type=sm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="edges", type=sm_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
node22: BinaryAssociation = BinaryAssociation(
    name="node22",
    ends={
        Property(name="State23", type=sm_Observation, multiplicity=Multiplicity(1, 1)),
        Property(name="mark", type=sm_State, multiplicity=Multiplicity(1, 1))
    }
)
graph24: BinaryAssociation = BinaryAssociation(
    name="graph24",
    ends={
        Property(name="StateMachine25", type=sm_Observation, multiplicity=Multiplicity(1, 1)),
        Property(name="marks", type=sm_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
mark12: BinaryAssociation = BinaryAssociation(
    name="mark12",
    ends={
        Property(name="Observation13", type=sm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=sm_Observation, multiplicity=Multiplicity(0, 1))
    }
)
graph14: BinaryAssociation = BinaryAssociation(
    name="graph14",
    ends={
        Property(name="StateMachine", type=sm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=sm_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
source15: BinaryAssociation = BinaryAssociation(
    name="source15",
    ends={
        Property(name="sm_State16", type=sm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_Transition", type=sm_State, multiplicity=Multiplicity(1, 1))
    }
)
target17: BinaryAssociation = BinaryAssociation(
    name="target17",
    ends={
        Property(name="sm_State19", type=sm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_Transition18", type=sm_State, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="sm",
    types={sm_StateMachine, sm_State, sm_Transition, sm_Observation},
    associations={initial0, final1, nodes4, edges5, marks7, subMachines9, graph20, node22, graph24, mark12, graph14, source15, target17},
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