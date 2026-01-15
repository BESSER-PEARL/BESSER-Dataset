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
graph_Vertex = Class(name="graph::Vertex")
graph_Edge = Class(name="graph::Edge")

# graph_Graph class attributes and methods

# graph_Vertex class attributes and methods
graph_Vertex_label: Property = Property(name="label", type=StringType)
graph_Vertex_weigth: Property = Property(name="weigth", type=IntegerType)
graph_Vertex.attributes={graph_Vertex_weigth, graph_Vertex_label}

# graph_Edge class attributes and methods

# Relationships
vertices0: BinaryAssociation = BinaryAssociation(
    name="vertices0",
    ends={
        Property(name="graph_Vertex", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Graph", type=graph_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from3: BinaryAssociation = BinaryAssociation(
    name="from3",
    ends={
        Property(name="graph_Edge4", type=graph_Vertex, multiplicity=Multiplicity(0, 1)),
        Property(name="graph_Vertex5", type=graph_Edge, multiplicity=Multiplicity(1, 1))
    }
)
to6: BinaryAssociation = BinaryAssociation(
    name="to6",
    ends={
        Property(name="graph_Vertex8", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Edge7", type=graph_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="graph_Edge", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Graph2", type=graph_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_Graph, graph_Vertex, graph_Edge},
    associations={vertices0, from3, to6, edges1},
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