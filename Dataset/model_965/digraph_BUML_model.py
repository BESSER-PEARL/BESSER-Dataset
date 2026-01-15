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
digraph_GraphElement = Class(name="digraph::GraphElement", is_abstract=True)
digraph_Node = Class(name="digraph::Node")
GraphElement = Class(name="GraphElement")
digraph_Edge = Class(name="digraph::Edge")
digraph_Graph = Class(name="digraph::Graph")

# digraph_GraphElement class attributes and methods

# digraph_Node class attributes and methods
digraph_Node_label: Property = Property(name="label", type=StringType)
digraph_Node.attributes={digraph_Node_label}

# GraphElement class attributes and methods

# digraph_Edge class attributes and methods
digraph_Edge_weight: Property = Property(name="weight", type=StringType)
digraph_Edge.attributes={digraph_Edge_weight}

# digraph_Graph class attributes and methods

# Relationships
contents0: BinaryAssociation = BinaryAssociation(
    name="contents0",
    ends={
        Property(name="GraphElement", type=digraph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=digraph_GraphElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graph1: BinaryAssociation = BinaryAssociation(
    name="graph1",
    ends={
        Property(name="Graph", type=digraph_GraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="contents", type=digraph_Graph, multiplicity=Multiplicity(0, 1))
    }
)
outgoing2: BinaryAssociation = BinaryAssociation(
    name="outgoing2",
    ends={
        Property(name="Edge", type=digraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=digraph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming3: BinaryAssociation = BinaryAssociation(
    name="incoming3",
    ends={
        Property(name="Edge4", type=digraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=digraph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
source5: BinaryAssociation = BinaryAssociation(
    name="source5",
    ends={
        Property(name="Node", type=digraph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=digraph_Node, multiplicity=Multiplicity(0, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="Node7", type=digraph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=digraph_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_digraph_Node_GraphElement = Generalization(general=GraphElement, specific=digraph_Node)
gen_digraph_Edge_GraphElement = Generalization(general=GraphElement, specific=digraph_Edge)

# Domain Model
domain_model = DomainModel(
    name="digraph",
    types={digraph_GraphElement, digraph_Node, GraphElement, digraph_Edge, digraph_Graph},
    associations={contents0, graph1, outgoing2, incoming3, source5, target6},
    generalizations={gen_digraph_Node_GraphElement, gen_digraph_Edge_GraphElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)