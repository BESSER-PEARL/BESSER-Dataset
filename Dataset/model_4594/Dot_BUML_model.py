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
dot_GraphModel = Class(name="dot::GraphModel")
dot_Graph = Class(name="dot::Graph")
dot_UndirectedGraph = Class(name="dot::UndirectedGraph")
Graph = Class(name="Graph")
dot_UnDirectedEdge = Class(name="dot::UnDirectedEdge")
dot_DirectedGraph = Class(name="dot::DirectedGraph")
dot_DirectedEdge = Class(name="dot::DirectedEdge")
dot_Node = Class(name="dot::Node")
dot_Attribute = Class(name="dot::Attribute")

# dot_GraphModel class attributes and methods

# dot_Graph class attributes and methods
dot_Graph_name: Property = Property(name="name", type=StringType)
dot_Graph.attributes={dot_Graph_name}

# dot_UndirectedGraph class attributes and methods

# Graph class attributes and methods

# dot_UnDirectedEdge class attributes and methods

# dot_DirectedGraph class attributes and methods

# dot_DirectedEdge class attributes and methods

# dot_Node class attributes and methods
dot_Node_name: Property = Property(name="name", type=StringType)
dot_Node.attributes={dot_Node_name}

# dot_Attribute class attributes and methods
dot_Attribute_weight: Property = Property(name="weight", type=IntegerType)
dot_Attribute.attributes={dot_Attribute_weight}

# Relationships
src10: BinaryAssociation = BinaryAssociation(
    name="src10",
    ends={
        Property(name="dot_Node12", type=dot_DirectedEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_DirectedEdge11", type=dot_Node, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tgt13: BinaryAssociation = BinaryAssociation(
    name="tgt13",
    ends={
        Property(name="dot_Node15", type=dot_DirectedEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_DirectedEdge14", type=dot_Node, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes16: BinaryAssociation = BinaryAssociation(
    name="attributes16",
    ends={
        Property(name="dot_Attribute18", type=dot_DirectedEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_DirectedEdge17", type=dot_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graph0: BinaryAssociation = BinaryAssociation(
    name="graph0",
    ends={
        Property(name="dot_Graph", type=dot_GraphModel, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_GraphModel", type=dot_Graph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge1: BinaryAssociation = BinaryAssociation(
    name="edge1",
    ends={
        Property(name="dot_UnDirectedEdge", type=dot_UndirectedGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_UndirectedGraph", type=dot_UnDirectedEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge2: BinaryAssociation = BinaryAssociation(
    name="edge2",
    ends={
        Property(name="dot_DirectedEdge", type=dot_DirectedGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_DirectedGraph", type=dot_DirectedEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
src3: BinaryAssociation = BinaryAssociation(
    name="src3",
    ends={
        Property(name="dot_Node", type=dot_UnDirectedEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_UnDirectedEdge4", type=dot_Node, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tgt5: BinaryAssociation = BinaryAssociation(
    name="tgt5",
    ends={
        Property(name="dot_Node7", type=dot_UnDirectedEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_UnDirectedEdge6", type=dot_Node, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes8: BinaryAssociation = BinaryAssociation(
    name="attributes8",
    ends={
        Property(name="dot_Attribute", type=dot_UnDirectedEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_UnDirectedEdge9", type=dot_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_dot_UndirectedGraph_Graph = Generalization(general=Graph, specific=dot_UndirectedGraph)
gen_dot_DirectedGraph_Graph = Generalization(general=Graph, specific=dot_DirectedGraph)

# Domain Model
domain_model = DomainModel(
    name="dot",
    types={dot_GraphModel, dot_Graph, dot_UndirectedGraph, Graph, dot_UnDirectedEdge, dot_DirectedGraph, dot_DirectedEdge, dot_Node, dot_Attribute},
    associations={src10, tgt13, attributes16, graph0, edge1, edge2, src3, tgt5, attributes8},
    generalizations={gen_dot_UndirectedGraph_Graph, gen_dot_DirectedGraph_Graph},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)