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
mgraph_MGraph = Class(name="mgraph::MGraph")
mgraph_MNode = Class(name="mgraph::MNode")
mgraph_MEdge = Class(name="mgraph::MEdge")

# mgraph_MGraph class attributes and methods
mgraph_MGraph_name: Property = Property(name="name", type=StringType)
mgraph_MGraph.attributes={mgraph_MGraph_name}

# mgraph_MNode class attributes and methods
mgraph_MNode_name: Property = Property(name="name", type=StringType)
mgraph_MNode.attributes={mgraph_MNode_name}

# mgraph_MEdge class attributes and methods
mgraph_MEdge_name: Property = Property(name="name", type=StringType)
mgraph_MEdge.attributes={mgraph_MEdge_name}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="MNode", type=mgraph_MGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=mgraph_MNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outGoing5: BinaryAssociation = BinaryAssociation(
    name="outGoing5",
    ends={
        Property(name="MNode6", type=mgraph_MEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=mgraph_MNode, multiplicity=Multiplicity(1, 1))
    }
)
graph7: BinaryAssociation = BinaryAssociation(
    name="graph7",
    ends={
        Property(name="MGraph", type=mgraph_MEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="edges", type=mgraph_MGraph, multiplicity=Multiplicity(1, 1))
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="MEdge", type=mgraph_MGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph2", type=mgraph_MEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graph8: BinaryAssociation = BinaryAssociation(
    name="graph8",
    ends={
        Property(name="MGraph9", type=mgraph_MNode, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=mgraph_MGraph, multiplicity=Multiplicity(1, 1))
    }
)
inComing3: BinaryAssociation = BinaryAssociation(
    name="inComing3",
    ends={
        Property(name="MNode4", type=mgraph_MEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=mgraph_MNode, multiplicity=Multiplicity(1, 1))
    }
)
from10: BinaryAssociation = BinaryAssociation(
    name="from10",
    ends={
        Property(name="MEdge11", type=mgraph_MNode, multiplicity=Multiplicity(1, 1)),
        Property(name="outGoing", type=mgraph_MEdge, multiplicity=Multiplicity(0, 9999))
    }
)
to12: BinaryAssociation = BinaryAssociation(
    name="to12",
    ends={
        Property(name="MEdge13", type=mgraph_MNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inComing", type=mgraph_MEdge, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="mgraph",
    types={mgraph_MGraph, mgraph_MNode, mgraph_MEdge},
    associations={nodes0, outGoing5, graph7, edges1, graph8, inComing3, from10, to12},
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