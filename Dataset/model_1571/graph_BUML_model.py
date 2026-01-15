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
Graph_Graph = Class(name="Graph::Graph")
Graph_Vertices = Class(name="Graph::Vertices")
Graph_Edges = Class(name="Graph::Edges")

# Graph_Graph class attributes and methods

# Graph_Vertices class attributes and methods
Graph_Vertices_name: Property = Property(name="name", type=StringType)
Graph_Vertices.attributes={Graph_Vertices_name}

# Graph_Edges class attributes and methods
Graph_Edges_name: Property = Property(name="name", type=StringType)
Graph_Edges.attributes={Graph_Edges_name}

# Relationships
vertice4: BinaryAssociation = BinaryAssociation(
    name="vertice4",
    ends={
        Property(name="edge", type=Graph_Vertices, multiplicity=Multiplicity(2, 2)),
        Property(name="Vertices", type=Graph_Edges, multiplicity=Multiplicity(1, 1))
    }
)
vertice0: BinaryAssociation = BinaryAssociation(
    name="vertice0",
    ends={
        Property(name="Graph_Vertices", type=Graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="Graph_Graph", type=Graph_Vertices, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge1: BinaryAssociation = BinaryAssociation(
    name="edge1",
    ends={
        Property(name="Graph_Edges", type=Graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="Graph_Graph2", type=Graph_Edges, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge3: BinaryAssociation = BinaryAssociation(
    name="edge3",
    ends={
        Property(name="Edges", type=Graph_Vertices, multiplicity=Multiplicity(1, 1)),
        Property(name="vertice", type=Graph_Edges, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Graph",
    types={Graph_Graph, Graph_Vertices, Graph_Edges},
    associations={vertice4, vertice0, edge1, edge3},
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