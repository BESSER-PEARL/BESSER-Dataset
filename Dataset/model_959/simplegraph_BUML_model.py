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
simplegraph_Graph = Class(name="simplegraph::Graph")
simplegraph_Node = Class(name="simplegraph::Node")
simplegraph_Edge = Class(name="simplegraph::Edge")

# simplegraph_Graph class attributes and methods

# simplegraph_Node class attributes and methods
simplegraph_Node_name: Property = Property(name="name", type=StringType)
simplegraph_Node.attributes={simplegraph_Node_name}

# simplegraph_Edge class attributes and methods

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="simplegraph_Node", type=simplegraph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="simplegraph_Graph", type=simplegraph_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing1: BinaryAssociation = BinaryAssociation(
    name="outgoing1",
    ends={
        Property(name="Edge", type=simplegraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=simplegraph_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming2: BinaryAssociation = BinaryAssociation(
    name="incoming2",
    ends={
        Property(name="Edge3", type=simplegraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=simplegraph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="Node", type=simplegraph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=simplegraph_Node, multiplicity=Multiplicity(0, 1))
    }
)
target5: BinaryAssociation = BinaryAssociation(
    name="target5",
    ends={
        Property(name="Node6", type=simplegraph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=simplegraph_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="simplegraph",
    types={simplegraph_Graph, simplegraph_Node, simplegraph_Edge},
    associations={nodes0, outgoing1, incoming2, source4, target5},
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