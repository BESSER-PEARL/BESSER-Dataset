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
notation_DiagramElement = Class(name="notation::DiagramElement", is_abstract=True)
Identifier = Class(name="Identifier")
notation_EObject = Class(name="notation::EObject")
notation_Node = Class(name="notation::Node")
DiagramElement = Class(name="DiagramElement")
notation_Edge = Class(name="notation::Edge")
notation_HierarchicalNode = Class(name="notation::HierarchicalNode")
notation_Anchor = Class(name="notation::Anchor")
notation_BendPoint = Class(name="notation::BendPoint", is_abstract=True)
Node = Class(name="Node")
notation_RelativeBendPoint = Class(name="notation::RelativeBendPoint")
BendPoint = Class(name="BendPoint")
notation_AbsoluteBendPoint = Class(name="notation::AbsoluteBendPoint")

# notation_DiagramElement class attributes and methods
notation_DiagramElement_visible: Property = Property(name="visible", type=BooleanType)
notation_DiagramElement_persistent: Property = Property(name="persistent", type=BooleanType)
notation_DiagramElement.attributes={notation_DiagramElement_visible, notation_DiagramElement_persistent}

# Identifier class attributes and methods

# notation_EObject class attributes and methods

# notation_Node class attributes and methods
notation_Node_x: Property = Property(name="x", type=IntegerType)
notation_Node_y: Property = Property(name="y", type=IntegerType)
notation_Node_width: Property = Property(name="width", type=IntegerType)
notation_Node_height: Property = Property(name="height", type=IntegerType)
notation_Node.attributes={notation_Node_width, notation_Node_y, notation_Node_x, notation_Node_height}

# DiagramElement class attributes and methods

# notation_Edge class attributes and methods

# notation_HierarchicalNode class attributes and methods

# notation_Anchor class attributes and methods
notation_Anchor_x: Property = Property(name="x", type=IntegerType)
notation_Anchor_y: Property = Property(name="y", type=IntegerType)
notation_Anchor.attributes={notation_Anchor_y, notation_Anchor_x}

# notation_BendPoint class attributes and methods

# Node class attributes and methods

# notation_RelativeBendPoint class attributes and methods
notation_RelativeBendPoint_sourceX: Property = Property(name="sourceX", type=IntegerType)
notation_RelativeBendPoint_sourceY: Property = Property(name="sourceY", type=IntegerType)
notation_RelativeBendPoint_targetX: Property = Property(name="targetX", type=IntegerType)
notation_RelativeBendPoint_targetY: Property = Property(name="targetY", type=IntegerType)
notation_RelativeBendPoint.attributes={notation_RelativeBendPoint_targetY, notation_RelativeBendPoint_targetX, notation_RelativeBendPoint_sourceY, notation_RelativeBendPoint_sourceX}

# BendPoint class attributes and methods

# notation_AbsoluteBendPoint class attributes and methods
notation_AbsoluteBendPoint_x: Property = Property(name="x", type=IntegerType)
notation_AbsoluteBendPoint_y: Property = Property(name="y", type=IntegerType)
notation_AbsoluteBendPoint.attributes={notation_AbsoluteBendPoint_y, notation_AbsoluteBendPoint_x}

# Relationships
model0: BinaryAssociation = BinaryAssociation(
    name="model0",
    ends={
        Property(name="notation_EObject", type=notation_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_DiagramElement", type=notation_EObject, multiplicity=Multiplicity(0, 1))
    }
)
outgoing1: BinaryAssociation = BinaryAssociation(
    name="outgoing1",
    ends={
        Property(name="Edge", type=notation_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=notation_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming2: BinaryAssociation = BinaryAssociation(
    name="incoming2",
    ends={
        Property(name="Edge3", type=notation_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=notation_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
parent4: BinaryAssociation = BinaryAssociation(
    name="parent4",
    ends={
        Property(name="HierarchicalNode", type=notation_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=notation_HierarchicalNode, multiplicity=Multiplicity(0, 1))
    }
)
source5: BinaryAssociation = BinaryAssociation(
    name="source5",
    ends={
        Property(name="Node", type=notation_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=notation_Node, multiplicity=Multiplicity(1, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="Node7", type=notation_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=notation_Node, multiplicity=Multiplicity(1, 1))
    }
)
parent8: BinaryAssociation = BinaryAssociation(
    name="parent8",
    ends={
        Property(name="HierarchicalNode9", type=notation_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edges", type=notation_HierarchicalNode, multiplicity=Multiplicity(0, 1))
    }
)
sourceAnchor10: BinaryAssociation = BinaryAssociation(
    name="sourceAnchor10",
    ends={
        Property(name="notation_Anchor", type=notation_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Edge", type=notation_Anchor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetAnchor11: BinaryAssociation = BinaryAssociation(
    name="targetAnchor11",
    ends={
        Property(name="notation_Anchor13", type=notation_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Edge12", type=notation_Anchor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bendPoints14: BinaryAssociation = BinaryAssociation(
    name="bendPoints14",
    ends={
        Property(name="BendPoint", type=notation_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge", type=notation_BendPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes15: BinaryAssociation = BinaryAssociation(
    name="nodes15",
    ends={
        Property(name="Node16", type=notation_HierarchicalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=notation_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges17: BinaryAssociation = BinaryAssociation(
    name="edges17",
    ends={
        Property(name="Edge19", type=notation_HierarchicalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="parent18", type=notation_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge20: BinaryAssociation = BinaryAssociation(
    name="edge20",
    ends={
        Property(name="Edge21", type=notation_BendPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="bendPoints", type=notation_Edge, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_notation_DiagramElement_Identifier = Generalization(general=Identifier, specific=notation_DiagramElement)
gen_notation_Node_DiagramElement = Generalization(general=DiagramElement, specific=notation_Node)
gen_notation_Edge_DiagramElement = Generalization(general=DiagramElement, specific=notation_Edge)
gen_notation_HierarchicalNode_Node = Generalization(general=Node, specific=notation_HierarchicalNode)
gen_notation_RelativeBendPoint_BendPoint = Generalization(general=BendPoint, specific=notation_RelativeBendPoint)
gen_notation_AbsoluteBendPoint_BendPoint = Generalization(general=BendPoint, specific=notation_AbsoluteBendPoint)

# Domain Model
domain_model = DomainModel(
    name="notation",
    types={notation_DiagramElement, Identifier, notation_EObject, notation_Node, DiagramElement, notation_Edge, notation_HierarchicalNode, notation_Anchor, notation_BendPoint, Node, notation_RelativeBendPoint, BendPoint, notation_AbsoluteBendPoint},
    associations={model0, outgoing1, incoming2, parent4, source5, target6, parent8, sourceAnchor10, targetAnchor11, bendPoints14, nodes15, edges17, edge20},
    generalizations={gen_notation_DiagramElement_Identifier, gen_notation_Node_DiagramElement, gen_notation_Edge_DiagramElement, gen_notation_HierarchicalNode_Node, gen_notation_RelativeBendPoint_BendPoint, gen_notation_AbsoluteBendPoint_BendPoint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)