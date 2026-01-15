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

# Enumerations
EdgeType: Enumeration = Enumeration(
    name="EdgeType",
    literals={
            EnumerationLiteral(name="IS_A_TYPE"),
			EnumerationLiteral(name="AKO_TYPE"),
			EnumerationLiteral(name="ROLE_CONSTRAINT_TYPE")
    }
)

# Classes
model_Diagram = Class(name="model::Diagram")
model_BendPoint = Class(name="model::BendPoint")
model_Node = Class(name="model::Node")
model_Edge = Class(name="model::Edge")
model_TypeNode = Class(name="model::TypeNode")
Node = Class(name="Node")
model_AssociationNode = Class(name="model::AssociationNode")

# model_Diagram class attributes and methods
model_Diagram_topicMapSchema: Property = Property(name="topicMapSchema", type=StringType)
model_Diagram.attributes={model_Diagram_topicMapSchema}

# model_BendPoint class attributes and methods
model_BendPoint_posX: Property = Property(name="posX", type=IntegerType)
model_BendPoint_posY: Property = Property(name="posY", type=IntegerType)
model_BendPoint.attributes={model_BendPoint_posX, model_BendPoint_posY}

# model_Node class attributes and methods
model_Node_posY: Property = Property(name="posY", type=IntegerType)
model_Node_posX: Property = Property(name="posX", type=IntegerType)
model_Node.attributes={model_Node_posX, model_Node_posY}

# model_Edge class attributes and methods
model_Edge_type: Property = Property(name="type", type=StringType)
model_Edge.attributes={model_Edge_type}

# model_TypeNode class attributes and methods
model_TypeNode_topicType: Property = Property(name="topicType", type=StringType)
model_TypeNode.attributes={model_TypeNode_topicType}

# Node class attributes and methods

# model_AssociationNode class attributes and methods
model_AssociationNode_associationTypeConstraint: Property = Property(name="associationTypeConstraint", type=StringType)
model_AssociationNode.attributes={model_AssociationNode_associationTypeConstraint}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="model_Node", type=model_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Diagram", type=model_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="model_Edge", type=model_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Diagram2", type=model_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bendpoints3: BinaryAssociation = BinaryAssociation(
    name="bendpoints3",
    ends={
        Property(name="model_BendPoint", type=model_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Edge4", type=model_BendPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source5: BinaryAssociation = BinaryAssociation(
    name="source5",
    ends={
        Property(name="model_Node7", type=model_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Edge6", type=model_Node, multiplicity=Multiplicity(1, 1))
    }
)
target8: BinaryAssociation = BinaryAssociation(
    name="target8",
    ends={
        Property(name="model_Node10", type=model_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Edge9", type=model_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_model_AssociationNode_Node = Generalization(general=Node, specific=model_AssociationNode)
gen_model_TypeNode_Node = Generalization(general=Node, specific=model_TypeNode)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Diagram, model_BendPoint, model_Node, model_Edge, model_TypeNode, Node, model_AssociationNode, EdgeType},
    associations={nodes0, edges1, bendpoints3, source5, target8},
    generalizations={gen_model_AssociationNode_Node, gen_model_TypeNode_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)