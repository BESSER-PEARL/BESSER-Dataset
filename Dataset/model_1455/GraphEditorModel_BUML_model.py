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
grapheditormodel_Graph = Class(name="grapheditormodel::Graph")
grapheditormodel_Node = Class(name="grapheditormodel::Node")
grapheditormodel_Edge = Class(name="grapheditormodel::Edge")

# grapheditormodel_Graph class attributes and methods

# grapheditormodel_Node class attributes and methods
grapheditormodel_Node_Name: Property = Property(name="Name", type=StringType)
grapheditormodel_Node.attributes={grapheditormodel_Node_Name}

# grapheditormodel_Edge class attributes and methods
grapheditormodel_Edge_Value: Property = Property(name="Value", type=StringType)
grapheditormodel_Edge.attributes={grapheditormodel_Edge_Value}

# Relationships
GraphNodes0: BinaryAssociation = BinaryAssociation(
    name="GraphNodes0",
    ends={
        Property(name="grapheditormodel_Node", type=grapheditormodel_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="grapheditormodel_Graph", type=grapheditormodel_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Start1: BinaryAssociation = BinaryAssociation(
    name="Start1",
    ends={
        Property(name="grapheditormodel_Node3", type=grapheditormodel_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="grapheditormodel_Graph2", type=grapheditormodel_Node, multiplicity=Multiplicity(1, 1))
    }
)
End4: BinaryAssociation = BinaryAssociation(
    name="End4",
    ends={
        Property(name="grapheditormodel_Node6", type=grapheditormodel_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="grapheditormodel_Graph5", type=grapheditormodel_Node, multiplicity=Multiplicity(1, 1))
    }
)
OutGoingEdges7: BinaryAssociation = BinaryAssociation(
    name="OutGoingEdges7",
    ends={
        Property(name="grapheditormodel_Edge", type=grapheditormodel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="grapheditormodel_Node8", type=grapheditormodel_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IncomingEdges9: BinaryAssociation = BinaryAssociation(
    name="IncomingEdges9",
    ends={
        Property(name="grapheditormodel_Edge11", type=grapheditormodel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="grapheditormodel_Node10", type=grapheditormodel_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
Target12: BinaryAssociation = BinaryAssociation(
    name="Target12",
    ends={
        Property(name="grapheditormodel_Node14", type=grapheditormodel_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="grapheditormodel_Edge13", type=grapheditormodel_Node, multiplicity=Multiplicity(1, 1))
    }
)
Source15: BinaryAssociation = BinaryAssociation(
    name="Source15",
    ends={
        Property(name="grapheditormodel_Node17", type=grapheditormodel_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="grapheditormodel_Edge16", type=grapheditormodel_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="grapheditormodel",
    types={grapheditormodel_Graph, grapheditormodel_Node, grapheditormodel_Edge},
    associations={GraphNodes0, Start1, End4, OutGoingEdges7, IncomingEdges9, Target12, Source15},
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