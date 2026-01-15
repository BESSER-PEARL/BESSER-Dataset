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

# graph_Graph class attributes and methods
graph_Graph_graphName: Property = Property(name="graphName", type=StringType)
graph_Graph.attributes={graph_Graph_graphName}

# graph_Vertex class attributes and methods
graph_Vertex_internalId: Property = Property(name="internalId", type=StringType)
graph_Vertex.attributes={graph_Vertex_internalId}

# Relationships
vertices0: BinaryAssociation = BinaryAssociation(
    name="vertices0",
    ends={
        Property(name="graph_Vertex", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Graph", type=graph_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root1: BinaryAssociation = BinaryAssociation(
    name="root1",
    ends={
        Property(name="graph_Vertex3", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Graph2", type=graph_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
edges5: BinaryAssociation = BinaryAssociation(
    name="edges5",
    ends={
        Property(name="graph_Vertex6", type=graph_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Vertex4", type=graph_Vertex, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_Graph, graph_Vertex},
    associations={vertices0, root1, edges5},
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