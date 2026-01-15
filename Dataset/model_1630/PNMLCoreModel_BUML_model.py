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
LineShape: Enumeration = Enumeration(
    name="LineShape",
    literals={
            EnumerationLiteral(name="line"),
			EnumerationLiteral(name="curve")
    }
)

# Classes
pnmlcoremodel_PetriNetDoc = Class(name="pnmlcoremodel::PetriNetDoc")
pnmlcoremodel_Page = Class(name="pnmlcoremodel::Page")
pnmlcoremodel_ToolInfo = Class(name="pnmlcoremodel::ToolInfo", is_abstract=True)
pnmlcoremodel_AnyType = Class(name="pnmlcoremodel::AnyType")
Node = Class(name="Node")
pnmlcoremodel_Object = Class(name="pnmlcoremodel::Object", is_abstract=True)
pnmlcoremodel_PageLabelProxy = Class(name="pnmlcoremodel::PageLabelProxy")
pnmlcoremodel_PetriNet = Class(name="pnmlcoremodel::PetriNet")
ID = Class(name="ID")
pnmlcoremodel_PetriNetType = Class(name="pnmlcoremodel::PetriNetType", is_abstract=True)
pnmlcoremodel_Name = Class(name="pnmlcoremodel::Name")
pnmlcoremodel_Label = Class(name="pnmlcoremodel::Label", is_abstract=True)
pnmlcoremodel_Node = Class(name="pnmlcoremodel::Node", is_abstract=True)
Object = Class(name="Object")
pnmlcoremodel_LabelProxy = Class(name="pnmlcoremodel::LabelProxy")
pnmlcoremodel_Graphics = Class(name="pnmlcoremodel::Graphics", is_abstract=True)
pnmlcoremodel_PlaceNode = Class(name="pnmlcoremodel::PlaceNode", is_abstract=True)
pnmlcoremodel_TransitionNode = Class(name="pnmlcoremodel::TransitionNode", is_abstract=True)
pnmlcoremodel_Place = Class(name="pnmlcoremodel::Place")
PlaceNode = Class(name="PlaceNode")
pnmlcoremodel_RefPlace = Class(name="pnmlcoremodel::RefPlace")
pnmlcoremodel_RefTransition = Class(name="pnmlcoremodel::RefTransition")
TransitionNode = Class(name="TransitionNode")
pnmlcoremodel_Arc = Class(name="pnmlcoremodel::Arc")
pnmlcoremodel_ArcGraphics = Class(name="pnmlcoremodel::ArcGraphics")
Graphics = Class(name="Graphics")
pnmlcoremodel_Line = Class(name="pnmlcoremodel::Line")
pnmlcoremodel_Coordinate = Class(name="pnmlcoremodel::Coordinate")
pnmlcoremodel_NodeGraphics = Class(name="pnmlcoremodel::NodeGraphics")
pnmlcoremodel_Transition = Class(name="pnmlcoremodel::Transition")
Label = Class(name="Label")
pnmlcoremodel_Font = Class(name="pnmlcoremodel::Font")
pnmlcoremodel_Fill = Class(name="pnmlcoremodel::Fill")
pnmlcoremodel_AnnotationGraphics = Class(name="pnmlcoremodel::AnnotationGraphics")
pnmlcoremodel_EmptyType = Class(name="pnmlcoremodel::EmptyType")
PetriNetType = Class(name="PetriNetType")
pnmlcoremodel_ToolInfoText = Class(name="pnmlcoremodel::ToolInfoText")
ToolInfo = Class(name="ToolInfo")
pnmlcoremodel_Attribute = Class(name="pnmlcoremodel::Attribute", is_abstract=True)
pnmlcoremodel_ID = Class(name="pnmlcoremodel::ID", is_abstract=True)

# pnmlcoremodel_PetriNetDoc class attributes and methods

# pnmlcoremodel_Page class attributes and methods

# pnmlcoremodel_ToolInfo class attributes and methods
pnmlcoremodel_ToolInfo_tool: Property = Property(name="tool", type=StringType)
pnmlcoremodel_ToolInfo_version: Property = Property(name="version", type=StringType)
pnmlcoremodel_ToolInfo.attributes={pnmlcoremodel_ToolInfo_tool, pnmlcoremodel_ToolInfo_version}

# pnmlcoremodel_AnyType class attributes and methods

# Node class attributes and methods

# pnmlcoremodel_Object class attributes and methods

# pnmlcoremodel_PageLabelProxy class attributes and methods
pnmlcoremodel_PageLabelProxy_text: Property = Property(name="text", type=StringType)
pnmlcoremodel_PageLabelProxy.attributes={pnmlcoremodel_PageLabelProxy_text}

# pnmlcoremodel_PetriNet class attributes and methods

# ID class attributes and methods

# pnmlcoremodel_PetriNetType class attributes and methods

# pnmlcoremodel_Name class attributes and methods
pnmlcoremodel_Name_text: Property = Property(name="text", type=StringType)
pnmlcoremodel_Name.attributes={pnmlcoremodel_Name_text}

# pnmlcoremodel_Label class attributes and methods

# pnmlcoremodel_Node class attributes and methods

# Object class attributes and methods

# pnmlcoremodel_LabelProxy class attributes and methods
pnmlcoremodel_LabelProxy_text: Property = Property(name="text", type=StringType)
pnmlcoremodel_LabelProxy.attributes={pnmlcoremodel_LabelProxy_text}

# pnmlcoremodel_Graphics class attributes and methods

# pnmlcoremodel_PlaceNode class attributes and methods

# pnmlcoremodel_TransitionNode class attributes and methods

# pnmlcoremodel_Place class attributes and methods

# PlaceNode class attributes and methods

# pnmlcoremodel_RefPlace class attributes and methods

# pnmlcoremodel_RefTransition class attributes and methods

# TransitionNode class attributes and methods

# pnmlcoremodel_Arc class attributes and methods

# pnmlcoremodel_ArcGraphics class attributes and methods

# Graphics class attributes and methods

# pnmlcoremodel_Line class attributes and methods
pnmlcoremodel_Line_shape: Property = Property(name="shape", type=StringType)
pnmlcoremodel_Line_color: Property = Property(name="color", type=StringType)
pnmlcoremodel_Line_width: Property = Property(name="width", type=FloatType)
pnmlcoremodel_Line_style: Property = Property(name="style", type=StringType)
pnmlcoremodel_Line.attributes={pnmlcoremodel_Line_shape, pnmlcoremodel_Line_width, pnmlcoremodel_Line_color, pnmlcoremodel_Line_style}

# pnmlcoremodel_Coordinate class attributes and methods
pnmlcoremodel_Coordinate_x: Property = Property(name="x", type=FloatType)
pnmlcoremodel_Coordinate_y: Property = Property(name="y", type=FloatType)
pnmlcoremodel_Coordinate.attributes={pnmlcoremodel_Coordinate_y, pnmlcoremodel_Coordinate_x}

# pnmlcoremodel_NodeGraphics class attributes and methods

# pnmlcoremodel_Transition class attributes and methods

# Label class attributes and methods

# pnmlcoremodel_Font class attributes and methods
pnmlcoremodel_Font_style: Property = Property(name="style", type=StringType)
pnmlcoremodel_Font_weight: Property = Property(name="weight", type=StringType)
pnmlcoremodel_Font_size: Property = Property(name="size", type=StringType)
pnmlcoremodel_Font_decoration: Property = Property(name="decoration", type=StringType)
pnmlcoremodel_Font_align: Property = Property(name="align", type=StringType)
pnmlcoremodel_Font_rotation: Property = Property(name="rotation", type=FloatType)
pnmlcoremodel_Font_family: Property = Property(name="family", type=StringType)
pnmlcoremodel_Font.attributes={pnmlcoremodel_Font_decoration, pnmlcoremodel_Font_weight, pnmlcoremodel_Font_align, pnmlcoremodel_Font_style, pnmlcoremodel_Font_rotation, pnmlcoremodel_Font_family, pnmlcoremodel_Font_size}

# pnmlcoremodel_Fill class attributes and methods
pnmlcoremodel_Fill_color: Property = Property(name="color", type=StringType)
pnmlcoremodel_Fill_image: Property = Property(name="image", type=StringType)
pnmlcoremodel_Fill_gradientColor: Property = Property(name="gradientColor", type=StringType)
pnmlcoremodel_Fill_gradientrotation: Property = Property(name="gradientrotation", type=StringType)
pnmlcoremodel_Fill.attributes={pnmlcoremodel_Fill_color, pnmlcoremodel_Fill_gradientrotation, pnmlcoremodel_Fill_image, pnmlcoremodel_Fill_gradientColor}

# pnmlcoremodel_AnnotationGraphics class attributes and methods

# pnmlcoremodel_EmptyType class attributes and methods

# PetriNetType class attributes and methods

# pnmlcoremodel_ToolInfoText class attributes and methods
pnmlcoremodel_ToolInfoText_info: Property = Property(name="info", type=StringType)
pnmlcoremodel_ToolInfoText.attributes={pnmlcoremodel_ToolInfoText_info}

# ToolInfo class attributes and methods

# pnmlcoremodel_Attribute class attributes and methods

# pnmlcoremodel_ID class attributes and methods
pnmlcoremodel_ID_id: Property = Property(name="id", type=StringType)
pnmlcoremodel_ID.attributes={pnmlcoremodel_ID_id}

# Relationships
page5: BinaryAssociation = BinaryAssociation(
    name="page5",
    ends={
        Property(name="pnmlcoremodel_Page", type=pnmlcoremodel_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_PetriNet6", type=pnmlcoremodel_Page, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
toolspecific7: BinaryAssociation = BinaryAssociation(
    name="toolspecific7",
    ends={
        Property(name="pnmlcoremodel_ToolInfo", type=pnmlcoremodel_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_PetriNet8", type=pnmlcoremodel_ToolInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unknown9: BinaryAssociation = BinaryAssociation(
    name="unknown9",
    ends={
        Property(name="pnmlcoremodel_AnyType", type=pnmlcoremodel_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_PetriNet10", type=pnmlcoremodel_AnyType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object11: BinaryAssociation = BinaryAssociation(
    name="object11",
    ends={
        Property(name="pnmlcoremodel_Object", type=pnmlcoremodel_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_Page12", type=pnmlcoremodel_Object, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pageLabelProxy13: BinaryAssociation = BinaryAssociation(
    name="pageLabelProxy13",
    ends={
        Property(name="pnmlcoremodel_PageLabelProxy", type=pnmlcoremodel_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_Page14", type=pnmlcoremodel_PageLabelProxy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net0: BinaryAssociation = BinaryAssociation(
    name="net0",
    ends={
        Property(name="pnmlcoremodel_PetriNet", type=pnmlcoremodel_PetriNetDoc, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_PetriNetDoc", type=pnmlcoremodel_PetriNet, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type1: BinaryAssociation = BinaryAssociation(
    name="type1",
    ends={
        Property(name="pnmlcoremodel_PetriNetType", type=pnmlcoremodel_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_PetriNet2", type=pnmlcoremodel_PetriNetType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name3: BinaryAssociation = BinaryAssociation(
    name="name3",
    ends={
        Property(name="pnmlcoremodel_Name", type=pnmlcoremodel_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_PetriNet4", type=pnmlcoremodel_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
graphics23: BinaryAssociation = BinaryAssociation(
    name="graphics23",
    ends={
        Property(name="pnmlcoremodel_Graphics", type=pnmlcoremodel_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_Object24", type=pnmlcoremodel_Graphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unknown25: BinaryAssociation = BinaryAssociation(
    name="unknown25",
    ends={
        Property(name="pnmlcoremodel_AnyType27", type=pnmlcoremodel_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_Object26", type=pnmlcoremodel_AnyType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label28: BinaryAssociation = BinaryAssociation(
    name="label28",
    ends={
        Property(name="pnmlcoremodel_Label", type=pnmlcoremodel_LabelProxy, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_LabelProxy29", type=pnmlcoremodel_Label, multiplicity=Multiplicity(1, 1))
    }
)
object30: BinaryAssociation = BinaryAssociation(
    name="object30",
    ends={
        Property(name="pnmlcoremodel_Object32", type=pnmlcoremodel_LabelProxy, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_LabelProxy31", type=pnmlcoremodel_Object, multiplicity=Multiplicity(0, 1))
    }
)
labelproxy15: BinaryAssociation = BinaryAssociation(
    name="labelproxy15",
    ends={
        Property(name="pnmlcoremodel_LabelProxy", type=pnmlcoremodel_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_Page16", type=pnmlcoremodel_LabelProxy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name17: BinaryAssociation = BinaryAssociation(
    name="name17",
    ends={
        Property(name="pnmlcoremodel_Name19", type=pnmlcoremodel_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_Object18", type=pnmlcoremodel_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
toolspecific20: BinaryAssociation = BinaryAssociation(
    name="toolspecific20",
    ends={
        Property(name="pnmlcoremodel_ToolInfo22", type=pnmlcoremodel_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_Object21", type=pnmlcoremodel_ToolInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source36: BinaryAssociation = BinaryAssociation(
    name="source36",
    ends={
        Property(name="out", type=pnmlcoremodel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="Node", type=pnmlcoremodel_Arc, multiplicity=Multiplicity(1, 1))
    }
)
target37: BinaryAssociation = BinaryAssociation(
    name="target37",
    ends={
        Property(name="Node38", type=pnmlcoremodel_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="in", type=pnmlcoremodel_Node, multiplicity=Multiplicity(1, 1))
    }
)
ref39: BinaryAssociation = BinaryAssociation(
    name="ref39",
    ends={
        Property(name="pnmlcoremodel_PlaceNode", type=pnmlcoremodel_RefPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_RefPlace", type=pnmlcoremodel_PlaceNode, multiplicity=Multiplicity(1, 1))
    }
)
out33: BinaryAssociation = BinaryAssociation(
    name="out33",
    ends={
        Property(name="Arc", type=pnmlcoremodel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=pnmlcoremodel_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
in34: BinaryAssociation = BinaryAssociation(
    name="in34",
    ends={
        Property(name="Arc35", type=pnmlcoremodel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=pnmlcoremodel_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
graphics44: BinaryAssociation = BinaryAssociation(
    name="graphics44",
    ends={
        Property(name="pnmlcoremodel_Graphics46", type=pnmlcoremodel_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_Label45", type=pnmlcoremodel_Graphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unknown47: BinaryAssociation = BinaryAssociation(
    name="unknown47",
    ends={
        Property(name="pnmlcoremodel_AnyType49", type=pnmlcoremodel_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_Label48", type=pnmlcoremodel_AnyType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
line50: BinaryAssociation = BinaryAssociation(
    name="line50",
    ends={
        Property(name="pnmlcoremodel_Line", type=pnmlcoremodel_ArcGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_ArcGraphics", type=pnmlcoremodel_Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
position51: BinaryAssociation = BinaryAssociation(
    name="position51",
    ends={
        Property(name="pnmlcoremodel_Coordinate", type=pnmlcoremodel_ArcGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_ArcGraphics52", type=pnmlcoremodel_Coordinate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
position53: BinaryAssociation = BinaryAssociation(
    name="position53",
    ends={
        Property(name="pnmlcoremodel_Coordinate54", type=pnmlcoremodel_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_NodeGraphics", type=pnmlcoremodel_Coordinate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref40: BinaryAssociation = BinaryAssociation(
    name="ref40",
    ends={
        Property(name="pnmlcoremodel_TransitionNode", type=pnmlcoremodel_RefTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_RefTransition", type=pnmlcoremodel_TransitionNode, multiplicity=Multiplicity(1, 1))
    }
)
toolspecific41: BinaryAssociation = BinaryAssociation(
    name="toolspecific41",
    ends={
        Property(name="pnmlcoremodel_ToolInfo43", type=pnmlcoremodel_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_Label42", type=pnmlcoremodel_ToolInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
line65: BinaryAssociation = BinaryAssociation(
    name="line65",
    ends={
        Property(name="pnmlcoremodel_Line67", type=pnmlcoremodel_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_AnnotationGraphics66", type=pnmlcoremodel_Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
offset68: BinaryAssociation = BinaryAssociation(
    name="offset68",
    ends={
        Property(name="pnmlcoremodel_Coordinate70", type=pnmlcoremodel_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_AnnotationGraphics69", type=pnmlcoremodel_Coordinate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
font71: BinaryAssociation = BinaryAssociation(
    name="font71",
    ends={
        Property(name="pnmlcoremodel_Font", type=pnmlcoremodel_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_AnnotationGraphics72", type=pnmlcoremodel_Font, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dimension55: BinaryAssociation = BinaryAssociation(
    name="dimension55",
    ends={
        Property(name="pnmlcoremodel_Coordinate57", type=pnmlcoremodel_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_NodeGraphics56", type=pnmlcoremodel_Coordinate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
line58: BinaryAssociation = BinaryAssociation(
    name="line58",
    ends={
        Property(name="pnmlcoremodel_Line60", type=pnmlcoremodel_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_NodeGraphics59", type=pnmlcoremodel_Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fill61: BinaryAssociation = BinaryAssociation(
    name="fill61",
    ends={
        Property(name="pnmlcoremodel_Fill", type=pnmlcoremodel_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_NodeGraphics62", type=pnmlcoremodel_Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fill63: BinaryAssociation = BinaryAssociation(
    name="fill63",
    ends={
        Property(name="pnmlcoremodel_Fill64", type=pnmlcoremodel_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_AnnotationGraphics", type=pnmlcoremodel_Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label73: BinaryAssociation = BinaryAssociation(
    name="label73",
    ends={
        Property(name="pnmlcoremodel_Label75", type=pnmlcoremodel_PageLabelProxy, multiplicity=Multiplicity(1, 1)),
        Property(name="pnmlcoremodel_PageLabelProxy74", type=pnmlcoremodel_Label, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_pnmlcoremodel_Page_Node = Generalization(general=Node, specific=pnmlcoremodel_Page)
gen_pnmlcoremodel_PetriNet_ID = Generalization(general=ID, specific=pnmlcoremodel_PetriNet)
gen_pnmlcoremodel_Node_Object = Generalization(general=Object, specific=pnmlcoremodel_Node)
gen_pnmlcoremodel_Object_ID = Generalization(general=ID, specific=pnmlcoremodel_Object)
gen_pnmlcoremodel_PlaceNode_Node = Generalization(general=Node, specific=pnmlcoremodel_PlaceNode)
gen_pnmlcoremodel_TransitionNode_Node = Generalization(general=Node, specific=pnmlcoremodel_TransitionNode)
gen_pnmlcoremodel_Place_PlaceNode = Generalization(general=PlaceNode, specific=pnmlcoremodel_Place)
gen_pnmlcoremodel_RefPlace_PlaceNode = Generalization(general=PlaceNode, specific=pnmlcoremodel_RefPlace)
gen_pnmlcoremodel_Arc_Object = Generalization(general=Object, specific=pnmlcoremodel_Arc)
gen_pnmlcoremodel_ArcGraphics_Graphics = Generalization(general=Graphics, specific=pnmlcoremodel_ArcGraphics)
gen_pnmlcoremodel_NodeGraphics_Graphics = Generalization(general=Graphics, specific=pnmlcoremodel_NodeGraphics)
gen_pnmlcoremodel_RefTransition_TransitionNode = Generalization(general=TransitionNode, specific=pnmlcoremodel_RefTransition)
gen_pnmlcoremodel_Transition_TransitionNode = Generalization(general=TransitionNode, specific=pnmlcoremodel_Transition)
gen_pnmlcoremodel_Name_Label = Generalization(general=Label, specific=pnmlcoremodel_Name)
gen_pnmlcoremodel_AnnotationGraphics_Graphics = Generalization(general=Graphics, specific=pnmlcoremodel_AnnotationGraphics)
gen_pnmlcoremodel_EmptyType_PetriNetType = Generalization(general=PetriNetType, specific=pnmlcoremodel_EmptyType)
gen_pnmlcoremodel_ToolInfoText_ToolInfo = Generalization(general=ToolInfo, specific=pnmlcoremodel_ToolInfoText)
gen_pnmlcoremodel_Attribute_Label = Generalization(general=Label, specific=pnmlcoremodel_Attribute)

# Domain Model
domain_model = DomainModel(
    name="pnmlcoremodel",
    types={pnmlcoremodel_PetriNetDoc, pnmlcoremodel_Page, pnmlcoremodel_ToolInfo, pnmlcoremodel_AnyType, Node, pnmlcoremodel_Object, pnmlcoremodel_PageLabelProxy, pnmlcoremodel_PetriNet, ID, pnmlcoremodel_PetriNetType, pnmlcoremodel_Name, pnmlcoremodel_Label, pnmlcoremodel_Node, Object, pnmlcoremodel_LabelProxy, pnmlcoremodel_Graphics, pnmlcoremodel_PlaceNode, pnmlcoremodel_TransitionNode, pnmlcoremodel_Place, PlaceNode, pnmlcoremodel_RefPlace, pnmlcoremodel_RefTransition, TransitionNode, pnmlcoremodel_Arc, pnmlcoremodel_ArcGraphics, Graphics, pnmlcoremodel_Line, pnmlcoremodel_Coordinate, pnmlcoremodel_NodeGraphics, pnmlcoremodel_Transition, Label, pnmlcoremodel_Font, pnmlcoremodel_Fill, pnmlcoremodel_AnnotationGraphics, pnmlcoremodel_EmptyType, PetriNetType, pnmlcoremodel_ToolInfoText, ToolInfo, pnmlcoremodel_Attribute, pnmlcoremodel_ID, LineShape},
    associations={page5, toolspecific7, unknown9, object11, pageLabelProxy13, net0, type1, name3, graphics23, unknown25, label28, object30, labelproxy15, name17, toolspecific20, source36, target37, ref39, out33, in34, graphics44, unknown47, line50, position51, position53, ref40, toolspecific41, line65, offset68, font71, dimension55, line58, fill61, fill63, label73},
    generalizations={gen_pnmlcoremodel_Page_Node, gen_pnmlcoremodel_PetriNet_ID, gen_pnmlcoremodel_Node_Object, gen_pnmlcoremodel_Object_ID, gen_pnmlcoremodel_PlaceNode_Node, gen_pnmlcoremodel_TransitionNode_Node, gen_pnmlcoremodel_Place_PlaceNode, gen_pnmlcoremodel_RefPlace_PlaceNode, gen_pnmlcoremodel_Arc_Object, gen_pnmlcoremodel_ArcGraphics_Graphics, gen_pnmlcoremodel_NodeGraphics_Graphics, gen_pnmlcoremodel_RefTransition_TransitionNode, gen_pnmlcoremodel_Transition_TransitionNode, gen_pnmlcoremodel_Name_Label, gen_pnmlcoremodel_AnnotationGraphics_Graphics, gen_pnmlcoremodel_EmptyType_PetriNetType, gen_pnmlcoremodel_ToolInfoText_ToolInfo, gen_pnmlcoremodel_Attribute_Label},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)