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
pcg_Graph = Class(name="pcg::Graph")
pcg_Vertex = Class(name="pcg::Vertex")
pcg_Edge = Class(name="pcg::Edge")
pcg_Resource = Class(name="pcg::Resource")

# pcg_Graph class attributes and methods

# pcg_Vertex class attributes and methods

# pcg_Edge class attributes and methods
pcg_Edge_kind: Property = Property(name="kind", type=StringType)
pcg_Edge.attributes={pcg_Edge_kind}

# pcg_Resource class attributes and methods
pcg_Resource_id: Property = Property(name="id", type=StringType)
pcg_Resource_title: Property = Property(name="title", type=StringType)
pcg_Resource.attributes={pcg_Resource_title, pcg_Resource_id}

# Relationships
vertices0: BinaryAssociation = BinaryAssociation(
    name="vertices0",
    ends={
        Property(name="pcg_Vertex", type=pcg_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="pcg_Graph", type=pcg_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="pcg_Edge", type=pcg_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="pcg_Graph2", type=pcg_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources3: BinaryAssociation = BinaryAssociation(
    name="resources3",
    ends={
        Property(name="pcg_Resource", type=pcg_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="pcg_Vertex4", type=pcg_Resource, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
target5: BinaryAssociation = BinaryAssociation(
    name="target5",
    ends={
        Property(name="pcg_Vertex7", type=pcg_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="pcg_Edge6", type=pcg_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="pcg_Vertex10", type=pcg_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="pcg_Edge9", type=pcg_Vertex, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="pcg",
    types={pcg_Graph, pcg_Vertex, pcg_Edge, pcg_Resource},
    associations={vertices0, edges1, resources3, target5, source8},
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