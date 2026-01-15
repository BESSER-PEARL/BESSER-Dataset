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
grapho_GraphO = Class(name="grapho::GraphO")
GraphElement = Class(name="GraphElement")
grapho_GraphElement = Class(name="grapho::GraphElement", is_abstract=True)
grapho_Node = Class(name="grapho::Node")
grapho_Edge = Class(name="grapho::Edge")

# grapho_GraphO class attributes and methods

# GraphElement class attributes and methods

# grapho_GraphElement class attributes and methods
grapho_GraphElement_name: Property = Property(name="name", type=StringType)
grapho_GraphElement.attributes={grapho_GraphElement_name}

# grapho_Node class attributes and methods
grapho_Node_style: Property = Property(name="style", type=StringType)
grapho_Node_color: Property = Property(name="color", type=StringType)
grapho_Node_shape: Property = Property(name="shape", type=StringType)
grapho_Node_label: Property = Property(name="label", type=StringType)
grapho_Node.attributes={grapho_Node_shape, grapho_Node_color, grapho_Node_label, grapho_Node_style}

# grapho_Edge class attributes and methods
grapho_Edge_color: Property = Property(name="color", type=StringType)
grapho_Edge_style: Property = Property(name="style", type=StringType)
grapho_Edge_constraintRank: Property = Property(name="constraintRank", type=BooleanType)
grapho_Edge.attributes={grapho_Edge_constraintRank, grapho_Edge_color, grapho_Edge_style}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="grapho_GraphElement", type=grapho_GraphO, multiplicity=Multiplicity(1, 1)),
        Property(name="grapho_GraphO", type=grapho_GraphElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeA1: BinaryAssociation = BinaryAssociation(
    name="nodeA1",
    ends={
        Property(name="grapho_Node", type=grapho_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="grapho_Edge", type=grapho_Node, multiplicity=Multiplicity(1, 1))
    }
)
nodeB2: BinaryAssociation = BinaryAssociation(
    name="nodeB2",
    ends={
        Property(name="grapho_Node4", type=grapho_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="grapho_Edge3", type=grapho_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_grapho_GraphO_GraphElement = Generalization(general=GraphElement, specific=grapho_GraphO)
gen_grapho_Node_GraphElement = Generalization(general=GraphElement, specific=grapho_Node)
gen_grapho_Edge_GraphElement = Generalization(general=GraphElement, specific=grapho_Edge)

# Domain Model
domain_model = DomainModel(
    name="grapho",
    types={grapho_GraphO, GraphElement, grapho_GraphElement, grapho_Node, grapho_Edge},
    associations={elements0, nodeA1, nodeB2},
    generalizations={gen_grapho_GraphO_GraphElement, gen_grapho_Node_GraphElement, gen_grapho_Edge_GraphElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)