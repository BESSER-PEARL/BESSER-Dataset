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
graph_Graph = Class(name="graph::Graph")
Named = Class(name="Named")
graph_Node = Class(name="graph::Node")
graph_Edge = Class(name="graph::Edge")
graph_Named = Class(name="graph::Named", is_abstract=True)
graph_Typed = Class(name="graph::Typed", is_abstract=True)
Typed = Class(name="Typed")

# graph_Graph class attributes and methods

# Named class attributes and methods

# graph_Node class attributes and methods

# graph_Edge class attributes and methods

# graph_Named class attributes and methods
graph_Named_name: Property = Property(name="name", type=StringType)
graph_Named.attributes={graph_Named_name}

# graph_Typed class attributes and methods
graph_Typed_type: Property = Property(name="type", type=StringType)
graph_Typed.attributes={graph_Typed_type}

# Typed class attributes and methods

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="Node", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=graph_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="Edge", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="parent2", type=graph_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent3: BinaryAssociation = BinaryAssociation(
    name="parent3",
    ends={
        Property(name="Graph", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=graph_Graph, multiplicity=Multiplicity(1, 1))
    }
)
outgoingEdges4: BinaryAssociation = BinaryAssociation(
    name="outgoingEdges4",
    ends={
        Property(name="Edge5", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=graph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
ingoingEdges6: BinaryAssociation = BinaryAssociation(
    name="ingoingEdges6",
    ends={
        Property(name="Edge7", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=graph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
parent8: BinaryAssociation = BinaryAssociation(
    name="parent8",
    ends={
        Property(name="Graph9", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edges", type=graph_Graph, multiplicity=Multiplicity(1, 1))
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="Node11", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingEdges", type=graph_Node, multiplicity=Multiplicity(1, 1))
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="Node13", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="ingoingEdges", type=graph_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_graph_Graph_Named = Generalization(general=Named, specific=graph_Graph)
gen_graph_Typed_Named = Generalization(general=Named, specific=graph_Typed)
gen_graph_Node_Typed = Generalization(general=Typed, specific=graph_Node)
gen_graph_Edge_Typed = Generalization(general=Typed, specific=graph_Edge)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_Graph, Named, graph_Node, graph_Edge, graph_Named, graph_Typed, Typed},
    associations={nodes0, edges1, parent3, outgoingEdges4, ingoingEdges6, parent8, source10, target12},
    generalizations={gen_graph_Graph_Named, gen_graph_Typed_Named, gen_graph_Node_Typed, gen_graph_Edge_Typed},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)