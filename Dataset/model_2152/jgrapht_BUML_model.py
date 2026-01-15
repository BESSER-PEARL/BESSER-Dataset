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
jgrapht_Edge = Class(name="jgrapht::Edge")
jgrapht_Vertex = Class(name="jgrapht::Vertex")
jgrapht_Graph = Class(name="jgrapht::Graph")

# jgrapht_Edge class attributes and methods
jgrapht_Edge_relation: Property = Property(name="relation", type=StringType)
jgrapht_Edge.attributes={jgrapht_Edge_relation}

# jgrapht_Vertex class attributes and methods
jgrapht_Vertex_name: Property = Property(name="name", type=StringType)
jgrapht_Vertex.attributes={jgrapht_Vertex_name}

# jgrapht_Graph class attributes and methods

# Relationships
edges0: BinaryAssociation = BinaryAssociation(
    name="edges0",
    ends={
        Property(name="jgrapht_Edge", type=jgrapht_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="jgrapht_Graph", type=jgrapht_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vertices1: BinaryAssociation = BinaryAssociation(
    name="vertices1",
    ends={
        Property(name="jgrapht_Vertex", type=jgrapht_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="jgrapht_Graph2", type=jgrapht_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from3: BinaryAssociation = BinaryAssociation(
    name="from3",
    ends={
        Property(name="jgrapht_Vertex5", type=jgrapht_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="jgrapht_Edge4", type=jgrapht_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
to6: BinaryAssociation = BinaryAssociation(
    name="to6",
    ends={
        Property(name="jgrapht_Vertex8", type=jgrapht_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="jgrapht_Edge7", type=jgrapht_Vertex, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="jgrapht",
    types={jgrapht_Edge, jgrapht_Vertex, jgrapht_Graph},
    associations={edges0, vertices1, from3, to6},
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