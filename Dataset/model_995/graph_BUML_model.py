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
graph_Graph = Class(name="graph_Graph")
graph_Node = Class(name="graph_Node")
graph_Edge = Class(name="graph_Edge")
GraphElement = Class(name="GraphElement")
graph_GraphElement = Class(name="graph_GraphElement", is_abstract=True)

# graph_Graph class attributes and methods
graph_Graph_name: Property = Property(name="name", type=StringType)
graph_Graph.attributes={graph_Graph_name}

# graph_Node class attributes and methods

# graph_Edge class attributes and methods

# GraphElement class attributes and methods

# graph_GraphElement class attributes and methods
graph_GraphElement_name: Property = Property(name="name", type=StringType)
graph_GraphElement.attributes={graph_GraphElement_name}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="graph_Node", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Graph", type=graph_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="graph_Edge", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Graph2", type=graph_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leavings3: BinaryAssociation = BinaryAssociation(
    name="leavings3",
    ends={
        Property(name="Edge", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceNode", type=graph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
enterings4: BinaryAssociation = BinaryAssociation(
    name="enterings4",
    ends={
        Property(name="Edge5", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="targetNode", type=graph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
sourceNode6: BinaryAssociation = BinaryAssociation(
    name="sourceNode6",
    ends={
        Property(name="Node", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="leavings", type=graph_Node, multiplicity=Multiplicity(0, 1))
    }
)
targetNode7: BinaryAssociation = BinaryAssociation(
    name="targetNode7",
    ends={
        Property(name="Node8", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="enterings", type=graph_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_graph_Node_GraphElement = Generalization(general=GraphElement, specific=graph_Node)
gen_graph_Edge_GraphElement = Generalization(general=GraphElement, specific=graph_Edge)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_Graph, graph_Node, graph_Edge, GraphElement, graph_GraphElement},
    associations={nodes0, edges1, leavings3, enterings4, sourceNode6, targetNode7},
    generalizations={gen_graph_Node_GraphElement, gen_graph_Edge_GraphElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)