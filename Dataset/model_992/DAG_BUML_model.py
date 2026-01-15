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
DAG_Graph = Class(name="DAG::Graph")
DAG_Node = Class(name="DAG::Node")
DAG_Edge = Class(name="DAG::Edge")
DAG_Revision = Class(name="DAG::Revision")

# DAG_Graph class attributes and methods
DAG_Graph_name: Property = Property(name="name", type=StringType)
DAG_Graph.attributes={DAG_Graph_name}

# DAG_Node class attributes and methods
DAG_Node_ID: Property = Property(name="ID", type=IntegerType)
DAG_Node_name: Property = Property(name="name", type=StringType)
DAG_Node_level: Property = Property(name="level", type=IntegerType)
DAG_Node.attributes={DAG_Node_name, DAG_Node_ID, DAG_Node_level}

# DAG_Edge class attributes and methods
DAG_Edge_ID: Property = Property(name="ID", type=IntegerType)
DAG_Edge_name: Property = Property(name="name", type=StringType)
DAG_Edge.attributes={DAG_Edge_ID, DAG_Edge_name}

# DAG_Revision class attributes and methods

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="DAG_Node", type=DAG_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="DAG_Graph", type=DAG_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parents2: BinaryAssociation = BinaryAssociation(
    name="parents2",
    ends={
        Property(name="Node", type=DAG_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=DAG_Node, multiplicity=Multiplicity(0, 9999))
    }
)
children4: BinaryAssociation = BinaryAssociation(
    name="children4",
    ends={
        Property(name="Node5", type=DAG_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="parents", type=DAG_Node, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing6: BinaryAssociation = BinaryAssociation(
    name="outgoing6",
    ends={
        Property(name="Edge", type=DAG_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=DAG_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming7: BinaryAssociation = BinaryAssociation(
    name="incoming7",
    ends={
        Property(name="Edge8", type=DAG_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=DAG_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
revision9: BinaryAssociation = BinaryAssociation(
    name="revision9",
    ends={
        Property(name="DAG_Revision", type=DAG_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="DAG_Node10", type=DAG_Revision, multiplicity=Multiplicity(0, 1))
    }
)
from11: BinaryAssociation = BinaryAssociation(
    name="from11",
    ends={
        Property(name="Node12", type=DAG_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=DAG_Node, multiplicity=Multiplicity(0, 1))
    }
)
to13: BinaryAssociation = BinaryAssociation(
    name="to13",
    ends={
        Property(name="Node14", type=DAG_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=DAG_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DAG",
    types={DAG_Graph, DAG_Node, DAG_Edge, DAG_Revision},
    associations={nodes0, parents2, children4, outgoing6, incoming7, revision9, from11, to13},
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