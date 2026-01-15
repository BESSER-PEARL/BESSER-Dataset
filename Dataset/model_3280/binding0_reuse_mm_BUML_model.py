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
Node = Class(name="Node")
sm_Transition = Class(name="sm::Transition")
Edge = Class(name="Edge")
sm_Observation = Class(name="sm::Observation")
Mark = Class(name="Mark")
sm_StateMachine = Class(name="sm::StateMachine")
Graph = Class(name="Graph")
sm_State = Class(name="sm::State")
sm_Edge = Class(name="sm::Edge")
sm_Mark = Class(name="sm::Mark")
sm_Graph = Class(name="sm::Graph")
sm_Node = Class(name="sm::Node")

# Node class attributes and methods

# sm_Transition class attributes and methods

# Edge class attributes and methods

# sm_Observation class attributes and methods

# Mark class attributes and methods

# sm_StateMachine class attributes and methods

# Graph class attributes and methods

# sm_State class attributes and methods

# sm_Edge class attributes and methods
sm_Edge_name: Property = Property(name="name", type=StringType)
sm_Edge.attributes={sm_Edge_name}

# sm_Mark class attributes and methods
sm_Mark_time: Property = Property(name="time", type=StringType)
sm_Mark.attributes={sm_Mark_time}

# sm_Graph class attributes and methods
sm_Graph_name: Property = Property(name="name", type=StringType)
sm_Graph.attributes={sm_Graph_name}

# sm_Node class attributes and methods
sm_Node_name: Property = Property(name="name", type=StringType)
sm_Node.attributes={sm_Node_name}

# Relationships
final1: BinaryAssociation = BinaryAssociation(
    name="final1",
    ends={
        Property(name="sm_StateMachine2", type=sm_State, multiplicity=Multiplicity(0, 9999)),
        Property(name="sm_State3", type=sm_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
subMachines4: BinaryAssociation = BinaryAssociation(
    name="subMachines4",
    ends={
        Property(name="sm_StateMachine6", type=sm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_State5", type=sm_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial0: BinaryAssociation = BinaryAssociation(
    name="initial0",
    ends={
        Property(name="sm_State", type=sm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_StateMachine", type=sm_State, multiplicity=Multiplicity(0, 1))
    }
)
edges8: BinaryAssociation = BinaryAssociation(
    name="edges8",
    ends={
        Property(name="Edge", type=sm_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph9", type=sm_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
marks10: BinaryAssociation = BinaryAssociation(
    name="marks10",
    ends={
        Property(name="Mark", type=sm_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph11", type=sm_Mark, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mark12: BinaryAssociation = BinaryAssociation(
    name="mark12",
    ends={
        Property(name="Mark13", type=sm_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=sm_Mark, multiplicity=Multiplicity(0, 1))
    }
)
graph14: BinaryAssociation = BinaryAssociation(
    name="graph14",
    ends={
        Property(name="Graph", type=sm_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=sm_Graph, multiplicity=Multiplicity(1, 1))
    }
)
source15: BinaryAssociation = BinaryAssociation(
    name="source15",
    ends={
        Property(name="sm_Node", type=sm_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_Edge", type=sm_Node, multiplicity=Multiplicity(1, 1))
    }
)
nodes7: BinaryAssociation = BinaryAssociation(
    name="nodes7",
    ends={
        Property(name="Node", type=sm_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=sm_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target16: BinaryAssociation = BinaryAssociation(
    name="target16",
    ends={
        Property(name="sm_Node18", type=sm_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_Edge17", type=sm_Node, multiplicity=Multiplicity(1, 1))
    }
)
graph19: BinaryAssociation = BinaryAssociation(
    name="graph19",
    ends={
        Property(name="Graph20", type=sm_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edges", type=sm_Graph, multiplicity=Multiplicity(1, 1))
    }
)
node21: BinaryAssociation = BinaryAssociation(
    name="node21",
    ends={
        Property(name="Node22", type=sm_Mark, multiplicity=Multiplicity(1, 1)),
        Property(name="mark", type=sm_Node, multiplicity=Multiplicity(1, 1))
    }
)
graph23: BinaryAssociation = BinaryAssociation(
    name="graph23",
    ends={
        Property(name="Graph24", type=sm_Mark, multiplicity=Multiplicity(1, 1)),
        Property(name="marks", type=sm_Graph, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_sm_State_Node = Generalization(general=Node, specific=sm_State)
gen_sm_Transition_Edge = Generalization(general=Edge, specific=sm_Transition)
gen_sm_Observation_Mark = Generalization(general=Mark, specific=sm_Observation)
gen_sm_StateMachine_Graph = Generalization(general=Graph, specific=sm_StateMachine)

# Domain Model
domain_model = DomainModel(
    name="sm",
    types={Node, sm_Transition, Edge, sm_Observation, Mark, sm_StateMachine, Graph, sm_State, sm_Edge, sm_Mark, sm_Graph, sm_Node},
    associations={final1, subMachines4, initial0, edges8, marks10, mark12, graph14, source15, nodes7, target16, graph19, node21, graph23},
    generalizations={gen_sm_State_Node, gen_sm_Transition_Edge, gen_sm_Observation_Mark, gen_sm_StateMachine_Graph},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)