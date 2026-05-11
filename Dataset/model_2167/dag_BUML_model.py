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
dag_DAG = Class(name="dag_DAG")
dag_Vertex = Class(name="dag_Vertex")
dag_Edge = Class(name="dag_Edge")

# dag_DAG class attributes and methods

# dag_Vertex class attributes and methods
dag_Vertex_id: Property = Property(name="id", type=StringType)
dag_Vertex.attributes={dag_Vertex_id}

# dag_Edge class attributes and methods
dag_Edge_id: Property = Property(name="id", type=StringType)
dag_Edge.attributes={dag_Edge_id}

# Relationships
vertices0: BinaryAssociation = BinaryAssociation(
    name="vertices0",
    ends={
        Property(name="dag_Vertex", type=dag_DAG, multiplicity=Multiplicity(1, 1)),
        Property(name="dag_DAG", type=dag_Vertex, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="dag_Edge", type=dag_DAG, multiplicity=Multiplicity(1, 1)),
        Property(name="dag_DAG2", type=dag_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing3: BinaryAssociation = BinaryAssociation(
    name="outgoing3",
    ends={
        Property(name="Edge", type=dag_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="from_", type=dag_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming4: BinaryAssociation = BinaryAssociation(
    name="incoming4",
    ends={
        Property(name="Edge5", type=dag_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=dag_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
from_6: BinaryAssociation = BinaryAssociation(
    name="from_6",
    ends={
        Property(name="Vertex", type=dag_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=dag_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
to7: BinaryAssociation = BinaryAssociation(
    name="to7",
    ends={
        Property(name="Vertex8", type=dag_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=dag_Vertex, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="dag",
    types={dag_DAG, dag_Vertex, dag_Edge},
    associations={vertices0, edges1, outgoing3, incoming4, from_6, to7},
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