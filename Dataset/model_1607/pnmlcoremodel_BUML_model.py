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
PNType: Enumeration = Enumeration(
    name="PNType",
    literals={
            EnumerationLiteral(name="COREMODEL"),
			EnumerationLiteral(name="PTNET"),
			EnumerationLiteral(name="SYMNET"),
			EnumerationLiteral(name="HLPN")
    }
)

CSS2Color: Enumeration = Enumeration(
    name="CSS2Color",
    literals={
            EnumerationLiteral(name="AQUA"),
			EnumerationLiteral(name="OLIVE"),
			EnumerationLiteral(name="ORANGE"),
			EnumerationLiteral(name="PURPLE"),
			EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="SILVER"),
			EnumerationLiteral(name="TEAL"),
			EnumerationLiteral(name="WHITE"),
			EnumerationLiteral(name="YELLOW"),
			EnumerationLiteral(name="BLACK"),
			EnumerationLiteral(name="BLUE"),
			EnumerationLiteral(name="FUCHSIA"),
			EnumerationLiteral(name="GRAY"),
			EnumerationLiteral(name="GREEN"),
			EnumerationLiteral(name="LIME"),
			EnumerationLiteral(name="MAROON"),
			EnumerationLiteral(name="NAVY")
    }
)

Gradient: Enumeration = Enumeration(
    name="Gradient",
    literals={
            EnumerationLiteral(name="HORIZONTAL"),
			EnumerationLiteral(name="VERTICAL"),
			EnumerationLiteral(name="DIAGONAL")
    }
)

LineShape: Enumeration = Enumeration(
    name="LineShape",
    literals={
            EnumerationLiteral(name="LINE"),
			EnumerationLiteral(name="CURVE")
    }
)

FontAlign: Enumeration = Enumeration(
    name="FontAlign",
    literals={
            EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="CENTER"),
			EnumerationLiteral(name="RIGHT")
    }
)

FontDecoration: Enumeration = Enumeration(
    name="FontDecoration",
    literals={
            EnumerationLiteral(name="UNDERLINE"),
			EnumerationLiteral(name="OVERLINE"),
			EnumerationLiteral(name="LINETHROUGH")
    }
)

CSS2FontFamily: Enumeration = Enumeration(
    name="CSS2FontFamily",
    literals={
            EnumerationLiteral(name="VERDANA"),
			EnumerationLiteral(name="ARIAL"),
			EnumerationLiteral(name="TIMES"),
			EnumerationLiteral(name="GEORGIA"),
			EnumerationLiteral(name="TREBUCHET")
    }
)

CSS2FontStyle: Enumeration = Enumeration(
    name="CSS2FontStyle",
    literals={
            EnumerationLiteral(name="NORMAL"),
			EnumerationLiteral(name="ITALIC"),
			EnumerationLiteral(name="OBLIQUE")
    }
)

CSS2FontWeight: Enumeration = Enumeration(
    name="CSS2FontWeight",
    literals={
            EnumerationLiteral(name="NORMAL"),
			EnumerationLiteral(name="BOLD"),
			EnumerationLiteral(name="BOLDER"),
			EnumerationLiteral(name="LIGHTER")
    }
)

CSS2FontSize: Enumeration = Enumeration(
    name="CSS2FontSize",
    literals={
            EnumerationLiteral(name="MEDIUM"),
			EnumerationLiteral(name="LARGE"),
			EnumerationLiteral(name="XLARGE"),
			EnumerationLiteral(name="XXLARGE"),
			EnumerationLiteral(name="XXSMALL"),
			EnumerationLiteral(name="XSMALL"),
			EnumerationLiteral(name="SMALL")
    }
)

LineStyle: Enumeration = Enumeration(
    name="LineStyle",
    literals={
            EnumerationLiteral(name="SOLID"),
			EnumerationLiteral(name="DASH"),
			EnumerationLiteral(name="DOT")
    }
)

# Classes
pnmlcoremodel_PetriNet = Class(name="pnmlcoremodel::PetriNet")
pnmlcoremodel_PetriNetDoc = Class(name="pnmlcoremodel::PetriNetDoc")
PnObject = Class(name="PnObject")
pnmlcoremodel_Page = Class(name="pnmlcoremodel::Page")
pnmlcoremodel_Name = Class(name="pnmlcoremodel::Name")
pnmlcoremodel_ToolInfo = Class(name="pnmlcoremodel::ToolInfo")
Annotation = Class(name="Annotation")
pnmlcoremodel_PnObject = Class(name="pnmlcoremodel::PnObject", is_abstract=True)
pnmlcoremodel_NodeGraphics = Class(name="pnmlcoremodel::NodeGraphics")
pnmlcoremodel_Label = Class(name="pnmlcoremodel::Label", is_abstract=True)
pnmlcoremodel_Position = Class(name="pnmlcoremodel::Position")
pnmlcoremodel_Dimension = Class(name="pnmlcoremodel::Dimension")
pnmlcoremodel_Fill = Class(name="pnmlcoremodel::Fill")
pnmlcoremodel_Line = Class(name="pnmlcoremodel::Line")
pnmlcoremodel_AnyObject = Class(name="pnmlcoremodel::AnyObject", is_abstract=True)
Graphics = Class(name="Graphics")
pnmlcoremodel_Coordinate = Class(name="pnmlcoremodel::Coordinate", is_abstract=True)
Coordinate = Class(name="Coordinate")
pnmlcoremodel_ArcGraphics = Class(name="pnmlcoremodel::ArcGraphics")
pnmlcoremodel_Node = Class(name="pnmlcoremodel::Node", is_abstract=True)
pnmlcoremodel_Graphics = Class(name="pnmlcoremodel::Graphics", is_abstract=True)
pnmlcoremodel_Offset = Class(name="pnmlcoremodel::Offset")
pnmlcoremodel_AnnotationGraphics = Class(name="pnmlcoremodel::AnnotationGraphics")
pnmlcoremodel_Font = Class(name="pnmlcoremodel::Font")
pnmlcoremodel_Annotation = Class(name="pnmlcoremodel::Annotation", is_abstract=True)
pnmlcoremodel_Arc = Class(name="pnmlcoremodel::Arc")
pnmlcoremodel_RefTransition = Class(name="pnmlcoremodel::RefTransition")
pnmlcoremodel_Place = Class(name="pnmlcoremodel::Place")
PlaceNode = Class(name="PlaceNode")
TransitionNode = Class(name="TransitionNode")
pnmlcoremodel_Transition = Class(name="pnmlcoremodel::Transition")
pnmlcoremodel_PlaceNode = Class(name="pnmlcoremodel::PlaceNode", is_abstract=True)
Node = Class(name="Node")
pnmlcoremodel_RefPlace = Class(name="pnmlcoremodel::RefPlace")
pnmlcoremodel_TransitionNode = Class(name="pnmlcoremodel::TransitionNode", is_abstract=True)
pnmlcoremodel_Attribute = Class(name="pnmlcoremodel::Attribute", is_abstract=True)
Label = Class(name="Label")

# pnmlcoremodel_PetriNet class attributes and methods
pnmlcoremodel_PetriNet_id: Property = Property(name="id", type=StringType)
pnmlcoremodel_PetriNet_type: Property = Property(name="type", type=StringType)
pnmlcoremodel_PetriNet.attributes={pnmlcoremodel_PetriNet_type, pnmlcoremodel_PetriNet_id}

# pnmlcoremodel_PetriNetDoc class attributes and methods
pnmlcoremodel_PetriNetDoc_xmlns: Property = Property(name="xmlns", type=StringType)
pnmlcoremodel_PetriNetDoc.attributes={pnmlcoremodel_PetriNetDoc_xmlns}

# PnObject class attributes and methods

# pnmlcoremodel_Page class attributes and methods

# pnmlcoremodel_Name class attributes and methods
pnmlcoremodel_Name_text: Property = Property(name="text", type=StringType)
pnmlcoremodel_Name.attributes={pnmlcoremodel_Name_text}

# pnmlcoremodel_ToolInfo class attributes and methods
pnmlcoremodel_ToolInfo_tool: Property = Property(name="tool", type=StringType)
pnmlcoremodel_ToolInfo_version: Property = Property(name="version", type=StringType)
pnmlcoremodel_ToolInfo_formattedXMLBuffer: Property = Property(name="formattedXMLBuffer", type=StringType)
pnmlcoremodel_ToolInfo_toolInfoGrammarURI: Property = Property(name="toolInfoGrammarURI", type=StringType)
pnmlcoremodel_ToolInfo.attributes={pnmlcoremodel_ToolInfo_formattedXMLBuffer, pnmlcoremodel_ToolInfo_version, pnmlcoremodel_ToolInfo_toolInfoGrammarURI, pnmlcoremodel_ToolInfo_tool}

# Annotation class attributes and methods

# pnmlcoremodel_PnObject class attributes and methods
pnmlcoremodel_PnObject_id: Property = Property(name="id", type=StringType)
pnmlcoremodel_PnObject.attributes={pnmlcoremodel_PnObject_id}

# pnmlcoremodel_NodeGraphics class attributes and methods

# pnmlcoremodel_Label class attributes and methods

# pnmlcoremodel_Position class attributes and methods

# pnmlcoremodel_Dimension class attributes and methods

# pnmlcoremodel_Fill class attributes and methods
pnmlcoremodel_Fill_gradientcolor: Property = Property(name="gradientcolor", type=StringType)
pnmlcoremodel_Fill_gradientrotation: Property = Property(name="gradientrotation", type=StringType)
pnmlcoremodel_Fill_image: Property = Property(name="image", type=StringType)
pnmlcoremodel_Fill_color: Property = Property(name="color", type=StringType)
pnmlcoremodel_Fill.attributes={pnmlcoremodel_Fill_image, pnmlcoremodel_Fill_gradientrotation, pnmlcoremodel_Fill_gradientcolor, pnmlcoremodel_Fill_color}

# pnmlcoremodel_Line class attributes and methods
pnmlcoremodel_Line_style: Property = Property(name="style", type=StringType)
pnmlcoremodel_Line_color: Property = Property(name="color", type=StringType)
pnmlcoremodel_Line_shape: Property = Property(name="shape", type=StringType)
pnmlcoremodel_Line_width: Property = Property(name="width", type=StringType)
pnmlcoremodel_Line.attributes={pnmlcoremodel_Line_color, pnmlcoremodel_Line_shape, pnmlcoremodel_Line_style, pnmlcoremodel_Line_width}

# pnmlcoremodel_AnyObject class attributes and methods

# Graphics class attributes and methods

# pnmlcoremodel_Coordinate class attributes and methods
pnmlcoremodel_Coordinate_x: Property = Property(name="x", type=StringType)
pnmlcoremodel_Coordinate_y: Property = Property(name="y", type=StringType)
pnmlcoremodel_Coordinate.attributes={pnmlcoremodel_Coordinate_y, pnmlcoremodel_Coordinate_x}

# Coordinate class attributes and methods

# pnmlcoremodel_ArcGraphics class attributes and methods

# pnmlcoremodel_Node class attributes and methods

# pnmlcoremodel_Graphics class attributes and methods

# pnmlcoremodel_Offset class attributes and methods

# pnmlcoremodel_AnnotationGraphics class attributes and methods

# pnmlcoremodel_Font class attributes and methods
pnmlcoremodel_Font_align: Property = Property(name="align", type=StringType)
pnmlcoremodel_Font_decoration: Property = Property(name="decoration", type=StringType)
pnmlcoremodel_Font_family: Property = Property(name="family", type=StringType)
pnmlcoremodel_Font_rotation: Property = Property(name="rotation", type=StringType)
pnmlcoremodel_Font_size: Property = Property(name="size", type=StringType)
pnmlcoremodel_Font_style: Property = Property(name="style", type=StringType)
pnmlcoremodel_Font_weight: Property = Property(name="weight", type=StringType)
pnmlcoremodel_Font.attributes={pnmlcoremodel_Font_family, pnmlcoremodel_Font_align, pnmlcoremodel_Font_weight, pnmlcoremodel_Font_decoration, pnmlcoremodel_Font_size, pnmlcoremodel_Font_style, pnmlcoremodel_Font_rotation}

# pnmlcoremodel_Annotation class attributes and methods

# pnmlcoremodel_Arc class attributes and methods

# pnmlcoremodel_RefTransition class attributes and methods

# pnmlcoremodel_Place class attributes and methods

# PlaceNode class attributes and methods

# TransitionNode class attributes and methods

# pnmlcoremodel_Transition class attributes and methods

# pnmlcoremodel_PlaceNode class attributes and methods

# Node class attributes and methods

# pnmlcoremodel_RefPlace class attributes and methods

# pnmlcoremodel_TransitionNode class attributes and methods

# pnmlcoremodel_Attribute class attributes and methods

# Label class attributes and methods

# Relationships
nets0: BinaryAssociation = BinaryAssociation(
    name="nets0",
    ends={
        Property(name="PetriNet", type=pnmlcoremodel_PetriNetDoc, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPetriNetDoc", type=pnmlcoremodel_PetriNet, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
toolspecifics3: BinaryAssociation = BinaryAssociation(
    name="toolspecifics3",
    ends={
        Property(name="ToolInfo", type=pnmlcoremodel_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPetriNet4", type=pnmlcoremodel_ToolInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerPetriNetDoc5: BinaryAssociation = BinaryAssociation(
    name="containerPetriNetDoc5",
    ends={
        Property(name="PetriNetDoc", type=pnmlcoremodel_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="nets", type=pnmlcoremodel_PetriNetDoc, multiplicity=Multiplicity(1, 1))
    }
)
pages1: BinaryAssociation = BinaryAssociation(
    name="pages1",
    ends={
        Property(name="Page", type=pnmlcoremodel_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPetriNet", type=pnmlcoremodel_Page, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
name2: BinaryAssociation = BinaryAssociation(
    name="name2",
    ends={
        Property(name="Name", type=pnmlcoremodel_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNamePetriNet", type=pnmlcoremodel_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name11: BinaryAssociation = BinaryAssociation(
    name="name11",
    ends={
        Property(name="Name12", type=pnmlcoremodel_PnObject, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNamePnObject", type=pnmlcoremodel_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
toolspecifics13: BinaryAssociation = BinaryAssociation(
    name="toolspecifics13",
    ends={
        Property(name="ToolInfo14", type=pnmlcoremodel_PnObject, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPnObject", type=pnmlcoremodel_ToolInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerPage15: BinaryAssociation = BinaryAssociation(
    name="containerPage15",
    ends={
        Property(name="Page16", type=pnmlcoremodel_PnObject, multiplicity=Multiplicity(1, 1)),
        Property(name="objects", type=pnmlcoremodel_Page, multiplicity=Multiplicity(0, 1))
    }
)
objects6: BinaryAssociation = BinaryAssociation(
    name="objects6",
    ends={
        Property(name="PnObject", type=pnmlcoremodel_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPage", type=pnmlcoremodel_PnObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerPetriNet7: BinaryAssociation = BinaryAssociation(
    name="containerPetriNet7",
    ends={
        Property(name="PetriNet8", type=pnmlcoremodel_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="pages", type=pnmlcoremodel_PetriNet, multiplicity=Multiplicity(0, 1))
    }
)
nodegraphics9: BinaryAssociation = BinaryAssociation(
    name="nodegraphics9",
    ends={
        Property(name="NodeGraphics", type=pnmlcoremodel_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPage10", type=pnmlcoremodel_NodeGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerPetriNet22: BinaryAssociation = BinaryAssociation(
    name="containerPetriNet22",
    ends={
        Property(name="PetriNet23", type=pnmlcoremodel_ToolInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="toolspecifics", type=pnmlcoremodel_PetriNet, multiplicity=Multiplicity(0, 1))
    }
)
containerPnObject24: BinaryAssociation = BinaryAssociation(
    name="containerPnObject24",
    ends={
        Property(name="PnObject26", type=pnmlcoremodel_ToolInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="toolspecifics25", type=pnmlcoremodel_PnObject, multiplicity=Multiplicity(0, 1))
    }
)
containerLabel27: BinaryAssociation = BinaryAssociation(
    name="containerLabel27",
    ends={
        Property(name="Label", type=pnmlcoremodel_ToolInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="toolspecifics28", type=pnmlcoremodel_Label, multiplicity=Multiplicity(0, 1))
    }
)
containerNamePetriNet17: BinaryAssociation = BinaryAssociation(
    name="containerNamePetriNet17",
    ends={
        Property(name="PetriNet18", type=pnmlcoremodel_Name, multiplicity=Multiplicity(1, 1)),
        Property(name="name", type=pnmlcoremodel_PetriNet, multiplicity=Multiplicity(0, 1))
    }
)
containerNamePnObject19: BinaryAssociation = BinaryAssociation(
    name="containerNamePnObject19",
    ends={
        Property(name="PnObject21", type=pnmlcoremodel_Name, multiplicity=Multiplicity(1, 1)),
        Property(name="name20", type=pnmlcoremodel_PnObject, multiplicity=Multiplicity(0, 1))
    }
)
position32: BinaryAssociation = BinaryAssociation(
    name="position32",
    ends={
        Property(name="Position", type=pnmlcoremodel_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPNodeGraphics", type=pnmlcoremodel_Position, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dimension33: BinaryAssociation = BinaryAssociation(
    name="dimension33",
    ends={
        Property(name="Dimension", type=pnmlcoremodel_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerDNodeGraphics", type=pnmlcoremodel_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fill34: BinaryAssociation = BinaryAssociation(
    name="fill34",
    ends={
        Property(name="Fill", type=pnmlcoremodel_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNodeGraphics", type=pnmlcoremodel_Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
toolInfoModel29: BinaryAssociation = BinaryAssociation(
    name="toolInfoModel29",
    ends={
        Property(name="AnyObject", type=pnmlcoremodel_ToolInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="containerToolInfo", type=pnmlcoremodel_AnyObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
toolspecifics30: BinaryAssociation = BinaryAssociation(
    name="toolspecifics30",
    ends={
        Property(name="ToolInfo31", type=pnmlcoremodel_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="containerLabel", type=pnmlcoremodel_ToolInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerPNodeGraphics41: BinaryAssociation = BinaryAssociation(
    name="containerPNodeGraphics41",
    ends={
        Property(name="NodeGraphics42", type=pnmlcoremodel_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="position", type=pnmlcoremodel_NodeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
line35: BinaryAssociation = BinaryAssociation(
    name="line35",
    ends={
        Property(name="Line", type=pnmlcoremodel_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNodeGraphics36", type=pnmlcoremodel_Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerNode37: BinaryAssociation = BinaryAssociation(
    name="containerNode37",
    ends={
        Property(name="Node", type=pnmlcoremodel_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="nodegraphics", type=pnmlcoremodel_Node, multiplicity=Multiplicity(0, 1))
    }
)
containerPage38: BinaryAssociation = BinaryAssociation(
    name="containerPage38",
    ends={
        Property(name="Page40", type=pnmlcoremodel_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="nodegraphics39", type=pnmlcoremodel_Page, multiplicity=Multiplicity(0, 1))
    }
)
containerDNodeGraphics45: BinaryAssociation = BinaryAssociation(
    name="containerDNodeGraphics45",
    ends={
        Property(name="NodeGraphics46", type=pnmlcoremodel_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="dimension", type=pnmlcoremodel_NodeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
offset47: BinaryAssociation = BinaryAssociation(
    name="offset47",
    ends={
        Property(name="Offset", type=pnmlcoremodel_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerAnnotationGraphics", type=pnmlcoremodel_Offset, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fill48: BinaryAssociation = BinaryAssociation(
    name="fill48",
    ends={
        Property(name="Fill50", type=pnmlcoremodel_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerAnnotationGraphics49", type=pnmlcoremodel_Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
line51: BinaryAssociation = BinaryAssociation(
    name="line51",
    ends={
        Property(name="Line53", type=pnmlcoremodel_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerAnnotationGraphics52", type=pnmlcoremodel_Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerArcGraphics43: BinaryAssociation = BinaryAssociation(
    name="containerArcGraphics43",
    ends={
        Property(name="ArcGraphics", type=pnmlcoremodel_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="positions", type=pnmlcoremodel_ArcGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerAnnotationGraphics44: BinaryAssociation = BinaryAssociation(
    name="containerAnnotationGraphics44",
    ends={
        Property(name="AnnotationGraphics", type=pnmlcoremodel_Offset, multiplicity=Multiplicity(1, 1)),
        Property(name="offset", type=pnmlcoremodel_AnnotationGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerNodeGraphics57: BinaryAssociation = BinaryAssociation(
    name="containerNodeGraphics57",
    ends={
        Property(name="NodeGraphics58", type=pnmlcoremodel_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="fill", type=pnmlcoremodel_NodeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerAnnotationGraphics59: BinaryAssociation = BinaryAssociation(
    name="containerAnnotationGraphics59",
    ends={
        Property(name="AnnotationGraphics61", type=pnmlcoremodel_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="fill60", type=pnmlcoremodel_AnnotationGraphics, multiplicity=Multiplicity(0, 1))
    }
)
font54: BinaryAssociation = BinaryAssociation(
    name="font54",
    ends={
        Property(name="Font", type=pnmlcoremodel_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerAnnotationGraphics55", type=pnmlcoremodel_Font, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerAnnotation56: BinaryAssociation = BinaryAssociation(
    name="containerAnnotation56",
    ends={
        Property(name="Annotation", type=pnmlcoremodel_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="annotationgraphics", type=pnmlcoremodel_Annotation, multiplicity=Multiplicity(0, 1))
    }
)
containerArcGraphics64: BinaryAssociation = BinaryAssociation(
    name="containerArcGraphics64",
    ends={
        Property(name="ArcGraphics66", type=pnmlcoremodel_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="line65", type=pnmlcoremodel_ArcGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerAnnotationGraphics67: BinaryAssociation = BinaryAssociation(
    name="containerAnnotationGraphics67",
    ends={
        Property(name="AnnotationGraphics69", type=pnmlcoremodel_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="line68", type=pnmlcoremodel_AnnotationGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerNodeGraphics62: BinaryAssociation = BinaryAssociation(
    name="containerNodeGraphics62",
    ends={
        Property(name="NodeGraphics63", type=pnmlcoremodel_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="line", type=pnmlcoremodel_NodeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerArc75: BinaryAssociation = BinaryAssociation(
    name="containerArc75",
    ends={
        Property(name="arcgraphics", type=pnmlcoremodel_Arc, multiplicity=Multiplicity(0, 1)),
        Property(name="Arc", type=pnmlcoremodel_ArcGraphics, multiplicity=Multiplicity(1, 1))
    }
)
source76: BinaryAssociation = BinaryAssociation(
    name="source76",
    ends={
        Property(name="Node77", type=pnmlcoremodel_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="OutArcs", type=pnmlcoremodel_Node, multiplicity=Multiplicity(1, 1))
    }
)
positions70: BinaryAssociation = BinaryAssociation(
    name="positions70",
    ends={
        Property(name="Position71", type=pnmlcoremodel_ArcGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerArcGraphics", type=pnmlcoremodel_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
line72: BinaryAssociation = BinaryAssociation(
    name="line72",
    ends={
        Property(name="Line74", type=pnmlcoremodel_ArcGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerArcGraphics73", type=pnmlcoremodel_Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
OutArcs84: BinaryAssociation = BinaryAssociation(
    name="OutArcs84",
    ends={
        Property(name="Arc85", type=pnmlcoremodel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=pnmlcoremodel_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
nodegraphics86: BinaryAssociation = BinaryAssociation(
    name="nodegraphics86",
    ends={
        Property(name="NodeGraphics87", type=pnmlcoremodel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNode", type=pnmlcoremodel_NodeGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target78: BinaryAssociation = BinaryAssociation(
    name="target78",
    ends={
        Property(name="Node79", type=pnmlcoremodel_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="InArcs", type=pnmlcoremodel_Node, multiplicity=Multiplicity(1, 1))
    }
)
arcgraphics80: BinaryAssociation = BinaryAssociation(
    name="arcgraphics80",
    ends={
        Property(name="ArcGraphics81", type=pnmlcoremodel_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="containerArc", type=pnmlcoremodel_ArcGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
InArcs82: BinaryAssociation = BinaryAssociation(
    name="InArcs82",
    ends={
        Property(name="Arc83", type=pnmlcoremodel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=pnmlcoremodel_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
containerAnnotationGraphics88: BinaryAssociation = BinaryAssociation(
    name="containerAnnotationGraphics88",
    ends={
        Property(name="AnnotationGraphics89", type=pnmlcoremodel_Font, multiplicity=Multiplicity(1, 1)),
        Property(name="font", type=pnmlcoremodel_AnnotationGraphics, multiplicity=Multiplicity(0, 1))
    }
)
referencingTransitions91: BinaryAssociation = BinaryAssociation(
    name="referencingTransitions91",
    ends={
        Property(name="RefTransition", type=pnmlcoremodel_TransitionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ref92", type=pnmlcoremodel_RefTransition, multiplicity=Multiplicity(0, 9999))
    }
)
ref93: BinaryAssociation = BinaryAssociation(
    name="ref93",
    ends={
        Property(name="TransitionNode", type=pnmlcoremodel_RefTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="referencingTransitions", type=pnmlcoremodel_TransitionNode, multiplicity=Multiplicity(1, 1))
    }
)
referencingPlaces90: BinaryAssociation = BinaryAssociation(
    name="referencingPlaces90",
    ends={
        Property(name="RefPlace", type=pnmlcoremodel_PlaceNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ref", type=pnmlcoremodel_RefPlace, multiplicity=Multiplicity(0, 9999))
    }
)
annotationgraphics95: BinaryAssociation = BinaryAssociation(
    name="annotationgraphics95",
    ends={
        Property(name="AnnotationGraphics96", type=pnmlcoremodel_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="containerAnnotation", type=pnmlcoremodel_AnnotationGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerToolInfo97: BinaryAssociation = BinaryAssociation(
    name="containerToolInfo97",
    ends={
        Property(name="ToolInfo98", type=pnmlcoremodel_AnyObject, multiplicity=Multiplicity(1, 1)),
        Property(name="toolInfoModel", type=pnmlcoremodel_ToolInfo, multiplicity=Multiplicity(0, 1))
    }
)
ref94: BinaryAssociation = BinaryAssociation(
    name="ref94",
    ends={
        Property(name="PlaceNode", type=pnmlcoremodel_RefPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="referencingPlaces", type=pnmlcoremodel_PlaceNode, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_pnmlcoremodel_Page_PnObject = Generalization(general=PnObject, specific=pnmlcoremodel_Page)
gen_pnmlcoremodel_Name_Annotation = Generalization(general=Annotation, specific=pnmlcoremodel_Name)
gen_pnmlcoremodel_NodeGraphics_Graphics = Generalization(general=Graphics, specific=pnmlcoremodel_NodeGraphics)
gen_pnmlcoremodel_Position_Coordinate = Generalization(general=Coordinate, specific=pnmlcoremodel_Position)
gen_pnmlcoremodel_AnnotationGraphics_Graphics = Generalization(general=Graphics, specific=pnmlcoremodel_AnnotationGraphics)
gen_pnmlcoremodel_Offset_Coordinate = Generalization(general=Coordinate, specific=pnmlcoremodel_Offset)
gen_pnmlcoremodel_Dimension_Coordinate = Generalization(general=Coordinate, specific=pnmlcoremodel_Dimension)
gen_pnmlcoremodel_ArcGraphics_Graphics = Generalization(general=Graphics, specific=pnmlcoremodel_ArcGraphics)
gen_pnmlcoremodel_Arc_PnObject = Generalization(general=PnObject, specific=pnmlcoremodel_Arc)
gen_pnmlcoremodel_Node_PnObject = Generalization(general=PnObject, specific=pnmlcoremodel_Node)
gen_pnmlcoremodel_Place_PlaceNode = Generalization(general=PlaceNode, specific=pnmlcoremodel_Place)
gen_pnmlcoremodel_RefTransition_TransitionNode = Generalization(general=TransitionNode, specific=pnmlcoremodel_RefTransition)
gen_pnmlcoremodel_Transition_TransitionNode = Generalization(general=TransitionNode, specific=pnmlcoremodel_Transition)
gen_pnmlcoremodel_RefPlace_PlaceNode = Generalization(general=PlaceNode, specific=pnmlcoremodel_RefPlace)
gen_pnmlcoremodel_PlaceNode_Node = Generalization(general=Node, specific=pnmlcoremodel_PlaceNode)
gen_pnmlcoremodel_TransitionNode_Node = Generalization(general=Node, specific=pnmlcoremodel_TransitionNode)
gen_pnmlcoremodel_Annotation_Label = Generalization(general=Label, specific=pnmlcoremodel_Annotation)
gen_pnmlcoremodel_Attribute_Label = Generalization(general=Label, specific=pnmlcoremodel_Attribute)

# Domain Model
domain_model = DomainModel(
    name="pnmlcoremodel",
    types={pnmlcoremodel_PetriNet, pnmlcoremodel_PetriNetDoc, PnObject, pnmlcoremodel_Page, pnmlcoremodel_Name, pnmlcoremodel_ToolInfo, Annotation, pnmlcoremodel_PnObject, pnmlcoremodel_NodeGraphics, pnmlcoremodel_Label, pnmlcoremodel_Position, pnmlcoremodel_Dimension, pnmlcoremodel_Fill, pnmlcoremodel_Line, pnmlcoremodel_AnyObject, Graphics, pnmlcoremodel_Coordinate, Coordinate, pnmlcoremodel_ArcGraphics, pnmlcoremodel_Node, pnmlcoremodel_Graphics, pnmlcoremodel_Offset, pnmlcoremodel_AnnotationGraphics, pnmlcoremodel_Font, pnmlcoremodel_Annotation, pnmlcoremodel_Arc, pnmlcoremodel_RefTransition, pnmlcoremodel_Place, PlaceNode, TransitionNode, pnmlcoremodel_Transition, pnmlcoremodel_PlaceNode, Node, pnmlcoremodel_RefPlace, pnmlcoremodel_TransitionNode, pnmlcoremodel_Attribute, Label, PNType, CSS2Color, Gradient, LineShape, FontAlign, FontDecoration, CSS2FontFamily, CSS2FontStyle, CSS2FontWeight, CSS2FontSize, LineStyle},
    associations={nets0, toolspecifics3, containerPetriNetDoc5, pages1, name2, name11, toolspecifics13, containerPage15, objects6, containerPetriNet7, nodegraphics9, containerPetriNet22, containerPnObject24, containerLabel27, containerNamePetriNet17, containerNamePnObject19, position32, dimension33, fill34, toolInfoModel29, toolspecifics30, containerPNodeGraphics41, line35, containerNode37, containerPage38, containerDNodeGraphics45, offset47, fill48, line51, containerArcGraphics43, containerAnnotationGraphics44, containerNodeGraphics57, containerAnnotationGraphics59, font54, containerAnnotation56, containerArcGraphics64, containerAnnotationGraphics67, containerNodeGraphics62, containerArc75, source76, positions70, line72, OutArcs84, nodegraphics86, target78, arcgraphics80, InArcs82, containerAnnotationGraphics88, referencingTransitions91, ref93, referencingPlaces90, annotationgraphics95, containerToolInfo97, ref94},
    generalizations={gen_pnmlcoremodel_Page_PnObject, gen_pnmlcoremodel_Name_Annotation, gen_pnmlcoremodel_NodeGraphics_Graphics, gen_pnmlcoremodel_Position_Coordinate, gen_pnmlcoremodel_AnnotationGraphics_Graphics, gen_pnmlcoremodel_Offset_Coordinate, gen_pnmlcoremodel_Dimension_Coordinate, gen_pnmlcoremodel_ArcGraphics_Graphics, gen_pnmlcoremodel_Arc_PnObject, gen_pnmlcoremodel_Node_PnObject, gen_pnmlcoremodel_Place_PlaceNode, gen_pnmlcoremodel_RefTransition_TransitionNode, gen_pnmlcoremodel_Transition_TransitionNode, gen_pnmlcoremodel_RefPlace_PlaceNode, gen_pnmlcoremodel_PlaceNode_Node, gen_pnmlcoremodel_TransitionNode_Node, gen_pnmlcoremodel_Annotation_Label, gen_pnmlcoremodel_Attribute_Label},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)