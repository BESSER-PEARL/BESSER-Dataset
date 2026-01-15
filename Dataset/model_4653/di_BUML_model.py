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
di_Diagram = Class(name="di::Diagram", is_abstract=True)
di_DiagramElement = Class(name="di::DiagramElement", is_abstract=True)
di_ExtensionType = Class(name="di::ExtensionType")
di_Edge = Class(name="di::Edge", is_abstract=True)
DiagramElement = Class(name="DiagramElement")
di_Point = Class(name="di::Point")
di_DocumentRoot = Class(name="di::DocumentRoot")
di_Label = Class(name="di::Label", is_abstract=True)
Node = Class(name="Node")
di_Bounds = Class(name="di::Bounds")
di_LabeledEdge = Class(name="di::LabeledEdge", is_abstract=True)
Edge = Class(name="Edge")
di_LabeledShape = Class(name="di::LabeledShape", is_abstract=True)
Shape = Class(name="Shape")
di_Node = Class(name="di::Node", is_abstract=True)
di_Plane = Class(name="di::Plane", is_abstract=True)
di_Shape = Class(name="di::Shape", is_abstract=True)
di_Style = Class(name="di::Style", is_abstract=True)
di_EStringToStringMapEntry = Class(name="di::EStringToStringMapEntry")

# di_Diagram class attributes and methods
di_Diagram_documentation: Property = Property(name="documentation", type=StringType)
di_Diagram_id: Property = Property(name="id", type=StringType)
di_Diagram_name: Property = Property(name="name", type=StringType)
di_Diagram_resolution: Property = Property(name="resolution", type=StringType)
di_Diagram.attributes={di_Diagram_name, di_Diagram_documentation, di_Diagram_id, di_Diagram_resolution}

# di_DiagramElement class attributes and methods
di_DiagramElement_id: Property = Property(name="id", type=StringType)
di_DiagramElement_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
di_DiagramElement.attributes={di_DiagramElement_id, di_DiagramElement_anyAttribute}

# di_ExtensionType class attributes and methods
di_ExtensionType_any: Property = Property(name="any", type=StringType)
di_ExtensionType.attributes={di_ExtensionType_any}

# di_Edge class attributes and methods

# DiagramElement class attributes and methods

# di_Point class attributes and methods

# di_DocumentRoot class attributes and methods
di_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
di_DocumentRoot.attributes={di_DocumentRoot_mixed}

# di_Label class attributes and methods

# Node class attributes and methods

# di_Bounds class attributes and methods

# di_LabeledEdge class attributes and methods

# Edge class attributes and methods

# di_LabeledShape class attributes and methods

# Shape class attributes and methods

# di_Node class attributes and methods

# di_Plane class attributes and methods
di_Plane_diagramElementGroup: Property = Property(name="diagramElementGroup", type=StringType)
di_Plane.attributes={di_Plane_diagramElementGroup}

# di_Shape class attributes and methods

# di_Style class attributes and methods
di_Style_id: Property = Property(name="id", type=StringType)
di_Style.attributes={di_Style_id}

# di_EStringToStringMapEntry class attributes and methods

# Relationships
extension0: BinaryAssociation = BinaryAssociation(
    name="extension0",
    ends={
        Property(name="di_ExtensionType", type=di_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DiagramElement", type=di_ExtensionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
waypoint1: BinaryAssociation = BinaryAssociation(
    name="waypoint1",
    ends={
        Property(name="di_Point", type=di_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Edge", type=di_Point, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
bounds2: BinaryAssociation = BinaryAssociation(
    name="bounds2",
    ends={
        Property(name="di_Bounds", type=di_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Label", type=di_Bounds, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
diagramElement3: BinaryAssociation = BinaryAssociation(
    name="diagramElement3",
    ends={
        Property(name="di_DiagramElement4", type=di_Plane, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Plane", type=di_DiagramElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bounds5: BinaryAssociation = BinaryAssociation(
    name="bounds5",
    ends={
        Property(name="di_Bounds6", type=di_Shape, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Shape", type=di_Bounds, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
node26: BinaryAssociation = BinaryAssociation(
    name="node26",
    ends={
        Property(name="di_Node", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot27", type=di_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap7: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap7",
    ends={
        Property(name="di_EStringToStringMapEntry", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot", type=di_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation8: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation8",
    ends={
        Property(name="di_EStringToStringMapEntry10", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot9", type=di_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagramElement11: BinaryAssociation = BinaryAssociation(
    name="diagramElement11",
    ends={
        Property(name="di_DiagramElement13", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot12", type=di_DiagramElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagram14: BinaryAssociation = BinaryAssociation(
    name="diagram14",
    ends={
        Property(name="di_Diagram", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot15", type=di_Diagram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge16: BinaryAssociation = BinaryAssociation(
    name="edge16",
    ends={
        Property(name="di_Edge18", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot17", type=di_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label19: BinaryAssociation = BinaryAssociation(
    name="label19",
    ends={
        Property(name="di_Label21", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot20", type=di_Label, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labeledEdge22: BinaryAssociation = BinaryAssociation(
    name="labeledEdge22",
    ends={
        Property(name="di_LabeledEdge", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot23", type=di_LabeledEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labeledShape24: BinaryAssociation = BinaryAssociation(
    name="labeledShape24",
    ends={
        Property(name="di_LabeledShape", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot25", type=di_LabeledShape, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
plane28: BinaryAssociation = BinaryAssociation(
    name="plane28",
    ends={
        Property(name="di_Plane30", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot29", type=di_Plane, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
shape31: BinaryAssociation = BinaryAssociation(
    name="shape31",
    ends={
        Property(name="di_Shape33", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot32", type=di_Shape, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
style34: BinaryAssociation = BinaryAssociation(
    name="style34",
    ends={
        Property(name="di_Style", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot35", type=di_Style, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_di_Edge_DiagramElement = Generalization(general=DiagramElement, specific=di_Edge)
gen_di_Label_Node = Generalization(general=Node, specific=di_Label)
gen_di_LabeledEdge_Edge = Generalization(general=Edge, specific=di_LabeledEdge)
gen_di_LabeledShape_Shape = Generalization(general=Shape, specific=di_LabeledShape)
gen_di_Node_DiagramElement = Generalization(general=DiagramElement, specific=di_Node)
gen_di_Plane_Node = Generalization(general=Node, specific=di_Plane)
gen_di_Shape_Node = Generalization(general=Node, specific=di_Shape)

# Domain Model
domain_model = DomainModel(
    name="di",
    types={di_Diagram, di_DiagramElement, di_ExtensionType, di_Edge, DiagramElement, di_Point, di_DocumentRoot, di_Label, Node, di_Bounds, di_LabeledEdge, Edge, di_LabeledShape, Shape, di_Node, di_Plane, di_Shape, di_Style, di_EStringToStringMapEntry},
    associations={extension0, waypoint1, bounds2, diagramElement3, bounds5, node26, xMLNSPrefixMap7, xSISchemaLocation8, diagramElement11, diagram14, edge16, label19, labeledEdge22, labeledShape24, plane28, shape31, style34},
    generalizations={gen_di_Edge_DiagramElement, gen_di_Label_Node, gen_di_LabeledEdge_Edge, gen_di_LabeledShape_Shape, gen_di_Node_DiagramElement, gen_di_Plane_Node, gen_di_Shape_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)