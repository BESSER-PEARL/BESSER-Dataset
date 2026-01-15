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
notation_Edge = Class(name="notation::Edge")
View = Class(name="View")
notation_Bounds = Class(name="notation::Bounds")
notation_CategorySeparator = Class(name="notation::CategorySeparator")
Node = Class(name="Node")
notation_Diagram = Class(name="notation::Diagram")
notation_NotationElement = Class(name="notation::NotationElement", is_abstract=True)
notation_View = Class(name="notation::View", is_abstract=True)
NotationElement = Class(name="NotationElement")
notation_Node = Class(name="notation::Node")
notation_EObject = Class(name="notation::EObject")
notation_LayoutConstraint = Class(name="notation::LayoutConstraint", is_abstract=True)
notation_Location = Class(name="notation::Location")
LayoutConstraint = Class(name="LayoutConstraint")
Location = Class(name="Location")
notation_Note = Class(name="notation::Note")
notation_MindMapNode = Class(name="notation::MindMapNode")
notation_ExpandableNode = Class(name="notation::ExpandableNode")

# notation_Edge class attributes and methods

# View class attributes and methods

# notation_Bounds class attributes and methods
notation_Bounds_width: Property = Property(name="width", type=IntegerType)
notation_Bounds_height: Property = Property(name="height", type=IntegerType)
notation_Bounds.attributes={notation_Bounds_width, notation_Bounds_height}

# notation_CategorySeparator class attributes and methods
notation_CategorySeparator_category: Property = Property(name="category", type=StringType)
notation_CategorySeparator_newChildCodeSyncType: Property = Property(name="newChildCodeSyncType", type=StringType)
notation_CategorySeparator_newChildIcon: Property = Property(name="newChildIcon", type=StringType)
notation_CategorySeparator.attributes={notation_CategorySeparator_newChildCodeSyncType, notation_CategorySeparator_category, notation_CategorySeparator_newChildIcon}

# Node class attributes and methods

# notation_Diagram class attributes and methods
notation_Diagram_name: Property = Property(name="name", type=StringType)
notation_Diagram_locationForNewElements: Property = Property(name="locationForNewElements", type=StringType)
notation_Diagram_showLocationForNewElementsDialog: Property = Property(name="showLocationForNewElementsDialog", type=BooleanType)
notation_Diagram.attributes={notation_Diagram_locationForNewElements, notation_Diagram_showLocationForNewElementsDialog, notation_Diagram_name}

# notation_NotationElement class attributes and methods
notation_NotationElement_id: Property = Property(name="id", type=StringType)
notation_NotationElement_idBeforeRemoval: Property = Property(name="idBeforeRemoval", type=StringType)
notation_NotationElement.attributes={notation_NotationElement_id, notation_NotationElement_idBeforeRemoval}

# notation_View class attributes and methods
notation_View_viewType: Property = Property(name="viewType", type=StringType)
notation_View_viewDetails: Property = Property(name="viewDetails", type=StringType)
notation_View_m_getAllChildren: Method = Method(name="getAllChildren", parameters={}, type=StringType)
notation_View.attributes={notation_View_viewType, notation_View_viewDetails}
notation_View.methods={notation_View_m_getAllChildren}

# NotationElement class attributes and methods

# notation_Node class attributes and methods

# notation_EObject class attributes and methods

# notation_LayoutConstraint class attributes and methods

# notation_Location class attributes and methods
notation_Location_x: Property = Property(name="x", type=IntegerType)
notation_Location_y: Property = Property(name="y", type=IntegerType)
notation_Location.attributes={notation_Location_y, notation_Location_x}

# LayoutConstraint class attributes and methods

# Location class attributes and methods

# notation_Note class attributes and methods
notation_Note_text: Property = Property(name="text", type=StringType)
notation_Note.attributes={notation_Note_text}

# notation_MindMapNode class attributes and methods

# notation_ExpandableNode class attributes and methods
notation_ExpandableNode_expanded: Property = Property(name="expanded", type=BooleanType)
notation_ExpandableNode_hasChildren: Property = Property(name="hasChildren", type=BooleanType)
notation_ExpandableNode_template: Property = Property(name="template", type=StringType)
notation_ExpandableNode.attributes={notation_ExpandableNode_expanded, notation_ExpandableNode_hasChildren, notation_ExpandableNode_template}

# Relationships
diagrammableElement1: BinaryAssociation = BinaryAssociation(
    name="diagrammableElement1",
    ends={
        Property(name="notation_View2", type=notation_EObject, multiplicity=Multiplicity(0, 1)),
        Property(name="notation_EObject", type=notation_View, multiplicity=Multiplicity(1, 1))
    }
)
sourceEdges3: BinaryAssociation = BinaryAssociation(
    name="sourceEdges3",
    ends={
        Property(name="Edge", type=notation_View, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=notation_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
targetEdges4: BinaryAssociation = BinaryAssociation(
    name="targetEdges4",
    ends={
        Property(name="Edge5", type=notation_View, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=notation_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
layoutConstraint6: BinaryAssociation = BinaryAssociation(
    name="layoutConstraint6",
    ends={
        Property(name="notation_Bounds", type=notation_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Node7", type=notation_Bounds, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="View", type=notation_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceEdges", type=notation_View, multiplicity=Multiplicity(0, 1))
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="View10", type=notation_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="targetEdges", type=notation_View, multiplicity=Multiplicity(0, 1))
    }
)
persistentChildren0: BinaryAssociation = BinaryAssociation(
    name="persistentChildren0",
    ends={
        Property(name="notation_Node", type=notation_View, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_View", type=notation_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
persistentEdges11: BinaryAssociation = BinaryAssociation(
    name="persistentEdges11",
    ends={
        Property(name="notation_Edge", type=notation_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Diagram", type=notation_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_notation_Node_View = Generalization(general=View, specific=notation_Node)
gen_notation_CategorySeparator_Node = Generalization(general=Node, specific=notation_CategorySeparator)
gen_notation_Edge_View = Generalization(general=View, specific=notation_Edge)
gen_notation_Diagram_View = Generalization(general=View, specific=notation_Diagram)
gen_notation_View_NotationElement = Generalization(general=NotationElement, specific=notation_View)
gen_notation_Location_NotationElement = Generalization(general=NotationElement, specific=notation_Location)
gen_notation_Location_LayoutConstraint = Generalization(general=LayoutConstraint, specific=notation_Location)
gen_notation_Bounds_Location = Generalization(general=Location, specific=notation_Bounds)
gen_notation_Note_Node = Generalization(general=Node, specific=notation_Note)
gen_notation_MindMapNode_Node = Generalization(general=Node, specific=notation_MindMapNode)
gen_notation_ExpandableNode_Node = Generalization(general=Node, specific=notation_ExpandableNode)

# Domain Model
domain_model = DomainModel(
    name="notation",
    types={notation_Edge, View, notation_Bounds, notation_CategorySeparator, Node, notation_Diagram, notation_NotationElement, notation_View, NotationElement, notation_Node, notation_EObject, notation_LayoutConstraint, notation_Location, LayoutConstraint, Location, notation_Note, notation_MindMapNode, notation_ExpandableNode},
    associations={diagrammableElement1, sourceEdges3, targetEdges4, layoutConstraint6, source8, target9, persistentChildren0, persistentEdges11},
    generalizations={gen_notation_Node_View, gen_notation_CategorySeparator_Node, gen_notation_Edge_View, gen_notation_Diagram_View, gen_notation_View_NotationElement, gen_notation_Location_NotationElement, gen_notation_Location_LayoutConstraint, gen_notation_Bounds_Location, gen_notation_Note_Node, gen_notation_MindMapNode_Node, gen_notation_ExpandableNode_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)