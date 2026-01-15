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
scaffolds_Edge = Class(name="scaffolds::Edge")
scaffolds_Vertex = Class(name="scaffolds::Vertex")
scaffolds_ScaffoldGraph = Class(name="scaffolds::ScaffoldGraph")
scaffolds_Contig = Class(name="scaffolds::Contig")

# scaffolds_Edge class attributes and methods
scaffolds_Edge_weight: Property = Property(name="weight", type=IntegerType)
scaffolds_Edge_distance: Property = Property(name="distance", type=IntegerType)
scaffolds_Edge.attributes={scaffolds_Edge_weight, scaffolds_Edge_distance}

# scaffolds_Vertex class attributes and methods
scaffolds_Vertex_num: Property = Property(name="num", type=IntegerType)
scaffolds_Vertex.attributes={scaffolds_Vertex_num}

# scaffolds_ScaffoldGraph class attributes and methods

# scaffolds_Contig class attributes and methods
scaffolds_Contig_length: Property = Property(name="length", type=IntegerType)
scaffolds_Contig_multiplicity: Property = Property(name="multiplicity", type=IntegerType)
scaffolds_Contig.attributes={scaffolds_Contig_multiplicity, scaffolds_Contig_length}

# Relationships
contigs0: BinaryAssociation = BinaryAssociation(
    name="contigs0",
    ends={
        Property(name="scaffolds_ScaffoldGraph", type=scaffolds_Contig, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="scaffolds_Contig", type=scaffolds_ScaffoldGraph, multiplicity=Multiplicity(1, 1))
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="scaffolds_Edge", type=scaffolds_ScaffoldGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="scaffolds_ScaffoldGraph2", type=scaffolds_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vertices3: BinaryAssociation = BinaryAssociation(
    name="vertices3",
    ends={
        Property(name="scaffolds_Vertex", type=scaffolds_Contig, multiplicity=Multiplicity(1, 1)),
        Property(name="scaffolds_Contig4", type=scaffolds_Vertex, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
vertices5: BinaryAssociation = BinaryAssociation(
    name="vertices5",
    ends={
        Property(name="Vertex", type=scaffolds_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edges", type=scaffolds_Vertex, multiplicity=Multiplicity(2, 2))
    }
)
edges6: BinaryAssociation = BinaryAssociation(
    name="edges6",
    ends={
        Property(name="Edge", type=scaffolds_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="vertices", type=scaffolds_Edge, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="scaffolds",
    types={scaffolds_Edge, scaffolds_Vertex, scaffolds_ScaffoldGraph, scaffolds_Contig},
    associations={contigs0, edges1, vertices3, vertices5, edges6},
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