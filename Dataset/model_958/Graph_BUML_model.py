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
Attributable = Class(name="Attributable")
Adaptable = Class(name="Adaptable")
graph_Graph = Class(name="graph::Graph")
Vertex = Class(name="Vertex")
graph_Edge = Class(name="graph::Edge")
graph_Vertex = Class(name="graph::Vertex")

# Attributable class attributes and methods

# Adaptable class attributes and methods

# graph_Graph class attributes and methods

# Vertex class attributes and methods

# graph_Edge class attributes and methods
graph_Edge_label: Property = Property(name="label", type=StringType)
graph_Edge.attributes={graph_Edge_label}

# graph_Vertex class attributes and methods
graph_Vertex_label: Property = Property(name="label", type=StringType)
graph_Vertex_number: Property = Property(name="number", type=IntegerType)
graph_Vertex.attributes={graph_Vertex_number, graph_Vertex_label}

# Relationships
incoming3: BinaryAssociation = BinaryAssociation(
    name="incoming3",
    ends={
        Property(name="Edge", type=graph_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=graph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing4: BinaryAssociation = BinaryAssociation(
    name="outgoing4",
    ends={
        Property(name="Edge5", type=graph_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=graph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
connecting6: BinaryAssociation = BinaryAssociation(
    name="connecting6",
    ends={
        Property(name="graph_Edge8", type=graph_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Vertex7", type=graph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
predecessors10: BinaryAssociation = BinaryAssociation(
    name="predecessors10",
    ends={
        Property(name="graph_Vertex11", type=graph_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Vertex9", type=graph_Vertex, multiplicity=Multiplicity(0, 9999))
    }
)
successors13: BinaryAssociation = BinaryAssociation(
    name="successors13",
    ends={
        Property(name="graph_Vertex14", type=graph_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Vertex12", type=graph_Vertex, multiplicity=Multiplicity(0, 9999))
    }
)
neighbors16: BinaryAssociation = BinaryAssociation(
    name="neighbors16",
    ends={
        Property(name="graph_Vertex17", type=graph_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Vertex15", type=graph_Vertex, multiplicity=Multiplicity(0, 9999))
    }
)
source18: BinaryAssociation = BinaryAssociation(
    name="source18",
    ends={
        Property(name="Vertex", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=graph_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
target19: BinaryAssociation = BinaryAssociation(
    name="target19",
    ends={
        Property(name="Vertex20", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=graph_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
edges0: BinaryAssociation = BinaryAssociation(
    name="edges0",
    ends={
        Property(name="graph_Edge", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Graph", type=graph_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vertices1: BinaryAssociation = BinaryAssociation(
    name="vertices1",
    ends={
        Property(name="graph_Vertex", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Graph2", type=graph_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_graph_Vertex_Attributable = Generalization(general=Attributable, specific=graph_Vertex)
gen_graph_Vertex_Adaptable = Generalization(general=Adaptable, specific=graph_Vertex)
gen_graph_Edge_Attributable = Generalization(general=Attributable, specific=graph_Edge)
gen_graph_Graph_Vertex = Generalization(general=Vertex, specific=graph_Graph)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={Attributable, Adaptable, graph_Graph, Vertex, graph_Edge, graph_Vertex},
    associations={incoming3, outgoing4, connecting6, predecessors10, successors13, neighbors16, source18, target19, edges0, vertices1},
    generalizations={gen_graph_Vertex_Attributable, gen_graph_Vertex_Adaptable, gen_graph_Edge_Attributable, gen_graph_Graph_Vertex},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)