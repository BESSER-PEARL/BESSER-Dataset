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
mtm_di_DiagramElement = Class(name="mtm::di::DiagramElement", is_abstract=True)
mtm_di_ExtensionType = Class(name="mtm::di::ExtensionType")
mtm_di_Edge = Class(name="mtm::di::Edge", is_abstract=True)
DiagramElement = Class(name="DiagramElement")
mtm_di_Point = Class(name="mtm::di::Point")
mtm_di_Diagram = Class(name="mtm::di::Diagram", is_abstract=True)
mtm_di_LabeledEdge = Class(name="mtm::di::LabeledEdge", is_abstract=True)
Edge = Class(name="Edge")
mtm_di_LabeledShape = Class(name="mtm::di::LabeledShape", is_abstract=True)
Shape = Class(name="Shape")
mtm_di_Node = Class(name="mtm::di::Node", is_abstract=True)
mtm_di_Plane = Class(name="mtm::di::Plane", is_abstract=True)
mtm_di_Shape = Class(name="mtm::di::Shape", is_abstract=True)
mtm_di_Style = Class(name="mtm::di::Style", is_abstract=True)
mtm_di_Label = Class(name="mtm::di::Label", is_abstract=True)
Node = Class(name="Node")
mtm_di_Bounds = Class(name="mtm::di::Bounds")
mtm_di_DocumentRoot = Class(name="mtm::di::DocumentRoot")
mtm_di_EStringToStringMapEntry = Class(name="mtm::di::EStringToStringMapEntry")

# mtm_di_DiagramElement class attributes and methods
mtm_di_DiagramElement_id: Property = Property(name="id", type=StringType)
mtm_di_DiagramElement_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
mtm_di_DiagramElement.attributes={mtm_di_DiagramElement_anyAttribute, mtm_di_DiagramElement_id}

# mtm_di_ExtensionType class attributes and methods
mtm_di_ExtensionType_any: Property = Property(name="any", type=StringType)
mtm_di_ExtensionType.attributes={mtm_di_ExtensionType_any}

# mtm_di_Edge class attributes and methods

# DiagramElement class attributes and methods

# mtm_di_Point class attributes and methods

# mtm_di_Diagram class attributes and methods
mtm_di_Diagram_name: Property = Property(name="name", type=StringType)
mtm_di_Diagram_resolution: Property = Property(name="resolution", type=StringType)
mtm_di_Diagram_documentation: Property = Property(name="documentation", type=StringType)
mtm_di_Diagram_id: Property = Property(name="id", type=StringType)
mtm_di_Diagram.attributes={mtm_di_Diagram_name, mtm_di_Diagram_documentation, mtm_di_Diagram_id, mtm_di_Diagram_resolution}

# mtm_di_LabeledEdge class attributes and methods

# Edge class attributes and methods

# mtm_di_LabeledShape class attributes and methods

# Shape class attributes and methods

# mtm_di_Node class attributes and methods

# mtm_di_Plane class attributes and methods
mtm_di_Plane_diagramElementGroup: Property = Property(name="diagramElementGroup", type=StringType)
mtm_di_Plane.attributes={mtm_di_Plane_diagramElementGroup}

# mtm_di_Shape class attributes and methods

# mtm_di_Style class attributes and methods
mtm_di_Style_id: Property = Property(name="id", type=StringType)
mtm_di_Style.attributes={mtm_di_Style_id}

# mtm_di_Label class attributes and methods

# Node class attributes and methods

# mtm_di_Bounds class attributes and methods

# mtm_di_DocumentRoot class attributes and methods
mtm_di_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
mtm_di_DocumentRoot.attributes={mtm_di_DocumentRoot_mixed}

# mtm_di_EStringToStringMapEntry class attributes and methods

# Relationships
extension0: BinaryAssociation = BinaryAssociation(
    name="extension0",
    ends={
        Property(name="mtm_di_ExtensionType", type=mtm_di_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="mtm_di_DiagramElement", type=mtm_di_ExtensionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
waypoint1: BinaryAssociation = BinaryAssociation(
    name="waypoint1",
    ends={
        Property(name="mtm_di_Point", type=mtm_di_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="mtm_di_Edge", type=mtm_di_Point, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
diagramElement3: BinaryAssociation = BinaryAssociation(
    name="diagramElement3",
    ends={
        Property(name="mtm_di_DiagramElement4", type=mtm_di_Plane, multiplicity=Multiplicity(1, 1)),
        Property(name="mtm_di_Plane", type=mtm_di_DiagramElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bounds5: BinaryAssociation = BinaryAssociation(
    name="bounds5",
    ends={
        Property(name="mtm_di_Bounds6", type=mtm_di_Shape, multiplicity=Multiplicity(1, 1)),
        Property(name="mtm_di_Shape", type=mtm_di_Bounds, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bounds2: BinaryAssociation = BinaryAssociation(
    name="bounds2",
    ends={
        Property(name="mtm_di_Bounds", type=mtm_di_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="mtm_di_Label", type=mtm_di_Bounds, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xSISchemaLocation8: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation8",
    ends={
        Property(name="mtm_di_EStringToStringMapEntry10", type=mtm_di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="mtm_di_DocumentRoot9", type=mtm_di_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagramElement11: BinaryAssociation = BinaryAssociation(
    name="diagramElement11",
    ends={
        Property(name="mtm_di_DiagramElement13", type=mtm_di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="mtm_di_DocumentRoot12", type=mtm_di_DiagramElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagram14: BinaryAssociation = BinaryAssociation(
    name="diagram14",
    ends={
        Property(name="mtm_di_Diagram", type=mtm_di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="mtm_di_DocumentRoot15", type=mtm_di_Diagram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge16: BinaryAssociation = BinaryAssociation(
    name="edge16",
    ends={
        Property(name="mtm_di_Edge18", type=mtm_di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="mtm_di_DocumentRoot17", type=mtm_di_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label19: BinaryAssociation = BinaryAssociation(
    name="label19",
    ends={
        Property(name="mtm_di_Label21", type=mtm_di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="mtm_di_DocumentRoot20", type=mtm_di_Label, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labeledEdge22: BinaryAssociation = BinaryAssociation(
    name="labeledEdge22",
    ends={
        Property(name="mtm_di_LabeledEdge", type=mtm_di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="mtm_di_DocumentRoot23", type=mtm_di_LabeledEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labeledShape24: BinaryAssociation = BinaryAssociation(
    name="labeledShape24",
    ends={
        Property(name="mtm_di_LabeledShape", type=mtm_di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="mtm_di_DocumentRoot25", type=mtm_di_LabeledShape, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node26: BinaryAssociation = BinaryAssociation(
    name="node26",
    ends={
        Property(name="mtm_di_Node", type=mtm_di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="mtm_di_DocumentRoot27", type=mtm_di_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap7: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap7",
    ends={
        Property(name="mtm_di_EStringToStringMapEntry", type=mtm_di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="mtm_di_DocumentRoot", type=mtm_di_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
style34: BinaryAssociation = BinaryAssociation(
    name="style34",
    ends={
        Property(name="mtm_di_Style", type=mtm_di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="mtm_di_DocumentRoot35", type=mtm_di_Style, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
plane28: BinaryAssociation = BinaryAssociation(
    name="plane28",
    ends={
        Property(name="mtm_di_Plane30", type=mtm_di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="mtm_di_DocumentRoot29", type=mtm_di_Plane, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
shape31: BinaryAssociation = BinaryAssociation(
    name="shape31",
    ends={
        Property(name="mtm_di_Shape33", type=mtm_di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="mtm_di_DocumentRoot32", type=mtm_di_Shape, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_mtm_di_Edge_DiagramElement = Generalization(general=DiagramElement, specific=mtm_di_Edge)
gen_mtm_di_LabeledEdge_Edge = Generalization(general=Edge, specific=mtm_di_LabeledEdge)
gen_mtm_di_LabeledShape_Shape = Generalization(general=Shape, specific=mtm_di_LabeledShape)
gen_mtm_di_Node_DiagramElement = Generalization(general=DiagramElement, specific=mtm_di_Node)
gen_mtm_di_Plane_Node = Generalization(general=Node, specific=mtm_di_Plane)
gen_mtm_di_Shape_Node = Generalization(general=Node, specific=mtm_di_Shape)
gen_mtm_di_Label_Node = Generalization(general=Node, specific=mtm_di_Label)

# Domain Model
domain_model = DomainModel(
    name="mtm_di",
    types={mtm_di_DiagramElement, mtm_di_ExtensionType, mtm_di_Edge, DiagramElement, mtm_di_Point, mtm_di_Diagram, mtm_di_LabeledEdge, Edge, mtm_di_LabeledShape, Shape, mtm_di_Node, mtm_di_Plane, mtm_di_Shape, mtm_di_Style, mtm_di_Label, Node, mtm_di_Bounds, mtm_di_DocumentRoot, mtm_di_EStringToStringMapEntry},
    associations={extension0, waypoint1, diagramElement3, bounds5, bounds2, xSISchemaLocation8, diagramElement11, diagram14, edge16, label19, labeledEdge22, labeledShape24, node26, xMLNSPrefixMap7, style34, plane28, shape31},
    generalizations={gen_mtm_di_Edge_DiagramElement, gen_mtm_di_LabeledEdge_Edge, gen_mtm_di_LabeledShape_Shape, gen_mtm_di_Node_DiagramElement, gen_mtm_di_Plane_Node, gen_mtm_di_Shape_Node, gen_mtm_di_Label_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)