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
            EnumerationLiteral(name="SYMNET"),
			EnumerationLiteral(name="COREMODEL"),
			EnumerationLiteral(name="PTNET"),
			EnumerationLiteral(name="HLPN")
    }
)

CSS2Color: Enumeration = Enumeration(
    name="CSS2Color",
    literals={
            EnumerationLiteral(name="AQUA"),
			EnumerationLiteral(name="BLACK"),
			EnumerationLiteral(name="BLUE"),
			EnumerationLiteral(name="FUCHSIA"),
			EnumerationLiteral(name="GRAY"),
			EnumerationLiteral(name="GREEN"),
			EnumerationLiteral(name="LIME"),
			EnumerationLiteral(name="MAROON"),
			EnumerationLiteral(name="NAVY"),
			EnumerationLiteral(name="OLIVE"),
			EnumerationLiteral(name="ORANGE"),
			EnumerationLiteral(name="PURPLE"),
			EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="SILVER"),
			EnumerationLiteral(name="TEAL"),
			EnumerationLiteral(name="WHITE"),
			EnumerationLiteral(name="YELLOW")
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

CSS2FontSize: Enumeration = Enumeration(
    name="CSS2FontSize",
    literals={
            EnumerationLiteral(name="XXSMALL"),
			EnumerationLiteral(name="XSMALL"),
			EnumerationLiteral(name="SMALL"),
			EnumerationLiteral(name="MEDIUM"),
			EnumerationLiteral(name="LARGE"),
			EnumerationLiteral(name="XLARGE"),
			EnumerationLiteral(name="XXLARGE")
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
            EnumerationLiteral(name="LIGHTER"),
			EnumerationLiteral(name="NORMAL"),
			EnumerationLiteral(name="BOLD"),
			EnumerationLiteral(name="BOLDER")
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

LineStyle: Enumeration = Enumeration(
    name="LineStyle",
    literals={
            EnumerationLiteral(name="SOLID"),
			EnumerationLiteral(name="DASH"),
			EnumerationLiteral(name="DOT")
    }
)

# Classes
hlcorestructure_PetriNetDoc = Class(name="hlcorestructure::PetriNetDoc")
hlcorestructure_PetriNet = Class(name="hlcorestructure::PetriNet")
hlcorestructure_Page = Class(name="hlcorestructure::Page")
hlcorestructure_Name = Class(name="hlcorestructure::Name")
hlcorestructure_Declaration = Class(name="hlcorestructure::Declaration")
PnObject = Class(name="PnObject")
hlcorestructure_PnObject = Class(name="hlcorestructure::PnObject", is_abstract=True)
hlcorestructure_ToolInfo = Class(name="hlcorestructure::ToolInfo")
hlcorestructure_NodeGraphics = Class(name="hlcorestructure::NodeGraphics")
Annotation = Class(name="Annotation")
hlcorestructure_Label = Class(name="hlcorestructure::Label", is_abstract=True)
hlcorestructure_AnyObject = Class(name="hlcorestructure::AnyObject", is_abstract=True)
Graphics = Class(name="Graphics")
hlcorestructure_Position = Class(name="hlcorestructure::Position")
hlcorestructure_Dimension = Class(name="hlcorestructure::Dimension")
hlcorestructure_Fill = Class(name="hlcorestructure::Fill")
hlcorestructure_Line = Class(name="hlcorestructure::Line")
hlcorestructure_Node = Class(name="hlcorestructure::Node", is_abstract=True)
hlcorestructure_Graphics = Class(name="hlcorestructure::Graphics", is_abstract=True)
hlcorestructure_Coordinate = Class(name="hlcorestructure::Coordinate", is_abstract=True)
Coordinate = Class(name="Coordinate")
hlcorestructure_ArcGraphics = Class(name="hlcorestructure::ArcGraphics")
hlcorestructure_Offset = Class(name="hlcorestructure::Offset")
hlcorestructure_AnnotationGraphics = Class(name="hlcorestructure::AnnotationGraphics")
hlcorestructure_Font = Class(name="hlcorestructure::Font")
hlcorestructure_Annotation = Class(name="hlcorestructure::Annotation", is_abstract=True)
hlcorestructure_Arc = Class(name="hlcorestructure::Arc")
hlcorestructure_HLAnnotation = Class(name="hlcorestructure::HLAnnotation")
hlcorestructure_PlaceNode = Class(name="hlcorestructure::PlaceNode", is_abstract=True)
Node = Class(name="Node")
hlcorestructure_RefPlace = Class(name="hlcorestructure::RefPlace")
hlcorestructure_TransitionNode = Class(name="hlcorestructure::TransitionNode", is_abstract=True)
hlcorestructure_RefTransition = Class(name="hlcorestructure::RefTransition")
hlcorestructure_Place = Class(name="hlcorestructure::Place")
PlaceNode = Class(name="PlaceNode")
hlcorestructure_Type = Class(name="hlcorestructure::Type")
hlcorestructure_HLMarking = Class(name="hlcorestructure::HLMarking")
TransitionNode = Class(name="TransitionNode")
hlcorestructure_Transition = Class(name="hlcorestructure::Transition")
hlcorestructure_Condition = Class(name="hlcorestructure::Condition")
hlcorestructure_Attribute = Class(name="hlcorestructure::Attribute", is_abstract=True)
Label = Class(name="Label")
hlcorestructure_HLCoreAnnotation = Class(name="hlcorestructure::HLCoreAnnotation", is_abstract=True)
HLCoreAnnotation = Class(name="HLCoreAnnotation")
hlcorestructure_Sort = Class(name="hlcorestructure::Sort")
hlcorestructure_Term = Class(name="hlcorestructure::Term")
hlcorestructure_Declarations = Class(name="hlcorestructure::Declarations")

# hlcorestructure_PetriNetDoc class attributes and methods
hlcorestructure_PetriNetDoc_xmlns: Property = Property(name="xmlns", type=StringType)
hlcorestructure_PetriNetDoc.attributes={hlcorestructure_PetriNetDoc_xmlns}

# hlcorestructure_PetriNet class attributes and methods
hlcorestructure_PetriNet_id: Property = Property(name="id", type=StringType)
hlcorestructure_PetriNet_type: Property = Property(name="type", type=StringType)
hlcorestructure_PetriNet.attributes={hlcorestructure_PetriNet_type, hlcorestructure_PetriNet_id}

# hlcorestructure_Page class attributes and methods

# hlcorestructure_Name class attributes and methods
hlcorestructure_Name_text: Property = Property(name="text", type=StringType)
hlcorestructure_Name.attributes={hlcorestructure_Name_text}

# hlcorestructure_Declaration class attributes and methods

# PnObject class attributes and methods

# hlcorestructure_PnObject class attributes and methods
hlcorestructure_PnObject_id: Property = Property(name="id", type=StringType)
hlcorestructure_PnObject.attributes={hlcorestructure_PnObject_id}

# hlcorestructure_ToolInfo class attributes and methods
hlcorestructure_ToolInfo_tool: Property = Property(name="tool", type=StringType)
hlcorestructure_ToolInfo_version: Property = Property(name="version", type=StringType)
hlcorestructure_ToolInfo_formattedXMLBuffer: Property = Property(name="formattedXMLBuffer", type=StringType)
hlcorestructure_ToolInfo_toolInfoGrammarURI: Property = Property(name="toolInfoGrammarURI", type=StringType)
hlcorestructure_ToolInfo.attributes={hlcorestructure_ToolInfo_formattedXMLBuffer, hlcorestructure_ToolInfo_version, hlcorestructure_ToolInfo_tool, hlcorestructure_ToolInfo_toolInfoGrammarURI}

# hlcorestructure_NodeGraphics class attributes and methods

# Annotation class attributes and methods

# hlcorestructure_Label class attributes and methods

# hlcorestructure_AnyObject class attributes and methods

# Graphics class attributes and methods

# hlcorestructure_Position class attributes and methods

# hlcorestructure_Dimension class attributes and methods

# hlcorestructure_Fill class attributes and methods
hlcorestructure_Fill_color: Property = Property(name="color", type=StringType)
hlcorestructure_Fill_gradientcolor: Property = Property(name="gradientcolor", type=StringType)
hlcorestructure_Fill_gradientrotation: Property = Property(name="gradientrotation", type=StringType)
hlcorestructure_Fill_image: Property = Property(name="image", type=StringType)
hlcorestructure_Fill.attributes={hlcorestructure_Fill_gradientcolor, hlcorestructure_Fill_color, hlcorestructure_Fill_gradientrotation, hlcorestructure_Fill_image}

# hlcorestructure_Line class attributes and methods
hlcorestructure_Line_color: Property = Property(name="color", type=StringType)
hlcorestructure_Line_shape: Property = Property(name="shape", type=StringType)
hlcorestructure_Line_width: Property = Property(name="width", type=StringType)
hlcorestructure_Line_style: Property = Property(name="style", type=StringType)
hlcorestructure_Line.attributes={hlcorestructure_Line_color, hlcorestructure_Line_shape, hlcorestructure_Line_style, hlcorestructure_Line_width}

# hlcorestructure_Node class attributes and methods

# hlcorestructure_Graphics class attributes and methods

# hlcorestructure_Coordinate class attributes and methods
hlcorestructure_Coordinate_x: Property = Property(name="x", type=StringType)
hlcorestructure_Coordinate_y: Property = Property(name="y", type=StringType)
hlcorestructure_Coordinate.attributes={hlcorestructure_Coordinate_x, hlcorestructure_Coordinate_y}

# Coordinate class attributes and methods

# hlcorestructure_ArcGraphics class attributes and methods

# hlcorestructure_Offset class attributes and methods

# hlcorestructure_AnnotationGraphics class attributes and methods

# hlcorestructure_Font class attributes and methods
hlcorestructure_Font_align: Property = Property(name="align", type=StringType)
hlcorestructure_Font_family: Property = Property(name="family", type=StringType)
hlcorestructure_Font_rotation: Property = Property(name="rotation", type=StringType)
hlcorestructure_Font_size: Property = Property(name="size", type=StringType)
hlcorestructure_Font_style: Property = Property(name="style", type=StringType)
hlcorestructure_Font_weight: Property = Property(name="weight", type=StringType)
hlcorestructure_Font_decoration: Property = Property(name="decoration", type=StringType)
hlcorestructure_Font.attributes={hlcorestructure_Font_style, hlcorestructure_Font_weight, hlcorestructure_Font_rotation, hlcorestructure_Font_family, hlcorestructure_Font_size, hlcorestructure_Font_align, hlcorestructure_Font_decoration}

# hlcorestructure_Annotation class attributes and methods

# hlcorestructure_Arc class attributes and methods

# hlcorestructure_HLAnnotation class attributes and methods

# hlcorestructure_PlaceNode class attributes and methods

# Node class attributes and methods

# hlcorestructure_RefPlace class attributes and methods

# hlcorestructure_TransitionNode class attributes and methods

# hlcorestructure_RefTransition class attributes and methods

# hlcorestructure_Place class attributes and methods

# PlaceNode class attributes and methods

# hlcorestructure_Type class attributes and methods

# hlcorestructure_HLMarking class attributes and methods

# TransitionNode class attributes and methods

# hlcorestructure_Transition class attributes and methods

# hlcorestructure_Condition class attributes and methods

# hlcorestructure_Attribute class attributes and methods

# Label class attributes and methods

# hlcorestructure_HLCoreAnnotation class attributes and methods
hlcorestructure_HLCoreAnnotation_text: Property = Property(name="text", type=StringType)
hlcorestructure_HLCoreAnnotation.attributes={hlcorestructure_HLCoreAnnotation_text}

# HLCoreAnnotation class attributes and methods

# hlcorestructure_Sort class attributes and methods

# hlcorestructure_Term class attributes and methods

# hlcorestructure_Declarations class attributes and methods

# Relationships
nets0: BinaryAssociation = BinaryAssociation(
    name="nets0",
    ends={
        Property(name="PetriNet", type=hlcorestructure_PetriNetDoc, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPetriNetDoc", type=hlcorestructure_PetriNet, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
pages1: BinaryAssociation = BinaryAssociation(
    name="pages1",
    ends={
        Property(name="Page", type=hlcorestructure_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPetriNet", type=hlcorestructure_Page, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
name2: BinaryAssociation = BinaryAssociation(
    name="name2",
    ends={
        Property(name="Name", type=hlcorestructure_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNamePetriNet", type=hlcorestructure_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerPetriNetDoc5: BinaryAssociation = BinaryAssociation(
    name="containerPetriNetDoc5",
    ends={
        Property(name="PetriNetDoc", type=hlcorestructure_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="nets", type=hlcorestructure_PetriNetDoc, multiplicity=Multiplicity(1, 1))
    }
)
declaration6: BinaryAssociation = BinaryAssociation(
    name="declaration6",
    ends={
        Property(name="Declaration", type=hlcorestructure_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="containerDeclarationPetriNet", type=hlcorestructure_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objects7: BinaryAssociation = BinaryAssociation(
    name="objects7",
    ends={
        Property(name="PnObject", type=hlcorestructure_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPage", type=hlcorestructure_PnObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerPetriNet8: BinaryAssociation = BinaryAssociation(
    name="containerPetriNet8",
    ends={
        Property(name="PetriNet9", type=hlcorestructure_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="pages", type=hlcorestructure_PetriNet, multiplicity=Multiplicity(0, 1))
    }
)
toolspecifics3: BinaryAssociation = BinaryAssociation(
    name="toolspecifics3",
    ends={
        Property(name="ToolInfo", type=hlcorestructure_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPetriNet4", type=hlcorestructure_ToolInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodegraphics10: BinaryAssociation = BinaryAssociation(
    name="nodegraphics10",
    ends={
        Property(name="NodeGraphics", type=hlcorestructure_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPage11", type=hlcorestructure_NodeGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration12: BinaryAssociation = BinaryAssociation(
    name="declaration12",
    ends={
        Property(name="Declaration13", type=hlcorestructure_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="containerDeclarationPage", type=hlcorestructure_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name14: BinaryAssociation = BinaryAssociation(
    name="name14",
    ends={
        Property(name="Name15", type=hlcorestructure_PnObject, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNamePnObject", type=hlcorestructure_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
toolspecifics16: BinaryAssociation = BinaryAssociation(
    name="toolspecifics16",
    ends={
        Property(name="ToolInfo17", type=hlcorestructure_PnObject, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPnObject", type=hlcorestructure_ToolInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerPage18: BinaryAssociation = BinaryAssociation(
    name="containerPage18",
    ends={
        Property(name="Page19", type=hlcorestructure_PnObject, multiplicity=Multiplicity(1, 1)),
        Property(name="objects", type=hlcorestructure_Page, multiplicity=Multiplicity(0, 1))
    }
)
containerNamePetriNet20: BinaryAssociation = BinaryAssociation(
    name="containerNamePetriNet20",
    ends={
        Property(name="PetriNet21", type=hlcorestructure_Name, multiplicity=Multiplicity(1, 1)),
        Property(name="name", type=hlcorestructure_PetriNet, multiplicity=Multiplicity(0, 1))
    }
)
containerNamePnObject22: BinaryAssociation = BinaryAssociation(
    name="containerNamePnObject22",
    ends={
        Property(name="PnObject24", type=hlcorestructure_Name, multiplicity=Multiplicity(1, 1)),
        Property(name="name23", type=hlcorestructure_PnObject, multiplicity=Multiplicity(0, 1))
    }
)
containerPetriNet25: BinaryAssociation = BinaryAssociation(
    name="containerPetriNet25",
    ends={
        Property(name="PetriNet26", type=hlcorestructure_ToolInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="toolspecifics", type=hlcorestructure_PetriNet, multiplicity=Multiplicity(0, 1))
    }
)
containerLabel30: BinaryAssociation = BinaryAssociation(
    name="containerLabel30",
    ends={
        Property(name="Label", type=hlcorestructure_ToolInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="toolspecifics31", type=hlcorestructure_Label, multiplicity=Multiplicity(0, 1))
    }
)
toolInfoModel32: BinaryAssociation = BinaryAssociation(
    name="toolInfoModel32",
    ends={
        Property(name="AnyObject", type=hlcorestructure_ToolInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="containerToolInfo", type=hlcorestructure_AnyObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
toolspecifics33: BinaryAssociation = BinaryAssociation(
    name="toolspecifics33",
    ends={
        Property(name="ToolInfo34", type=hlcorestructure_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="containerLabel", type=hlcorestructure_ToolInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
position35: BinaryAssociation = BinaryAssociation(
    name="position35",
    ends={
        Property(name="Position", type=hlcorestructure_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPNodeGraphics", type=hlcorestructure_Position, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dimension36: BinaryAssociation = BinaryAssociation(
    name="dimension36",
    ends={
        Property(name="Dimension", type=hlcorestructure_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerDNodeGraphics", type=hlcorestructure_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fill37: BinaryAssociation = BinaryAssociation(
    name="fill37",
    ends={
        Property(name="Fill", type=hlcorestructure_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNodeGraphics", type=hlcorestructure_Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerPnObject27: BinaryAssociation = BinaryAssociation(
    name="containerPnObject27",
    ends={
        Property(name="PnObject29", type=hlcorestructure_ToolInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="toolspecifics28", type=hlcorestructure_PnObject, multiplicity=Multiplicity(0, 1))
    }
)
line38: BinaryAssociation = BinaryAssociation(
    name="line38",
    ends={
        Property(name="Line", type=hlcorestructure_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNodeGraphics39", type=hlcorestructure_Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerNode40: BinaryAssociation = BinaryAssociation(
    name="containerNode40",
    ends={
        Property(name="Node", type=hlcorestructure_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="nodegraphics", type=hlcorestructure_Node, multiplicity=Multiplicity(0, 1))
    }
)
containerPage41: BinaryAssociation = BinaryAssociation(
    name="containerPage41",
    ends={
        Property(name="Page43", type=hlcorestructure_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="nodegraphics42", type=hlcorestructure_Page, multiplicity=Multiplicity(0, 1))
    }
)
containerArcGraphics44: BinaryAssociation = BinaryAssociation(
    name="containerArcGraphics44",
    ends={
        Property(name="ArcGraphics", type=hlcorestructure_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="positions", type=hlcorestructure_ArcGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerPNodeGraphics45: BinaryAssociation = BinaryAssociation(
    name="containerPNodeGraphics45",
    ends={
        Property(name="NodeGraphics46", type=hlcorestructure_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="position", type=hlcorestructure_NodeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerAnnotationGraphics47: BinaryAssociation = BinaryAssociation(
    name="containerAnnotationGraphics47",
    ends={
        Property(name="AnnotationGraphics", type=hlcorestructure_Offset, multiplicity=Multiplicity(1, 1)),
        Property(name="offset", type=hlcorestructure_AnnotationGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerDNodeGraphics48: BinaryAssociation = BinaryAssociation(
    name="containerDNodeGraphics48",
    ends={
        Property(name="NodeGraphics49", type=hlcorestructure_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="dimension", type=hlcorestructure_NodeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
offset50: BinaryAssociation = BinaryAssociation(
    name="offset50",
    ends={
        Property(name="Offset", type=hlcorestructure_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerAnnotationGraphics", type=hlcorestructure_Offset, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fill51: BinaryAssociation = BinaryAssociation(
    name="fill51",
    ends={
        Property(name="Fill53", type=hlcorestructure_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerAnnotationGraphics52", type=hlcorestructure_Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
line54: BinaryAssociation = BinaryAssociation(
    name="line54",
    ends={
        Property(name="Line56", type=hlcorestructure_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerAnnotationGraphics55", type=hlcorestructure_Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
font57: BinaryAssociation = BinaryAssociation(
    name="font57",
    ends={
        Property(name="Font", type=hlcorestructure_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerAnnotationGraphics58", type=hlcorestructure_Font, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerAnnotation59: BinaryAssociation = BinaryAssociation(
    name="containerAnnotation59",
    ends={
        Property(name="Annotation", type=hlcorestructure_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="annotationgraphics", type=hlcorestructure_Annotation, multiplicity=Multiplicity(0, 1))
    }
)
containerNodeGraphics60: BinaryAssociation = BinaryAssociation(
    name="containerNodeGraphics60",
    ends={
        Property(name="NodeGraphics61", type=hlcorestructure_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="fill", type=hlcorestructure_NodeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerAnnotationGraphics62: BinaryAssociation = BinaryAssociation(
    name="containerAnnotationGraphics62",
    ends={
        Property(name="AnnotationGraphics64", type=hlcorestructure_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="fill63", type=hlcorestructure_AnnotationGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerNodeGraphics65: BinaryAssociation = BinaryAssociation(
    name="containerNodeGraphics65",
    ends={
        Property(name="NodeGraphics66", type=hlcorestructure_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="line", type=hlcorestructure_NodeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerArcGraphics67: BinaryAssociation = BinaryAssociation(
    name="containerArcGraphics67",
    ends={
        Property(name="ArcGraphics69", type=hlcorestructure_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="line68", type=hlcorestructure_ArcGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerAnnotationGraphics70: BinaryAssociation = BinaryAssociation(
    name="containerAnnotationGraphics70",
    ends={
        Property(name="AnnotationGraphics72", type=hlcorestructure_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="line71", type=hlcorestructure_AnnotationGraphics, multiplicity=Multiplicity(0, 1))
    }
)
line75: BinaryAssociation = BinaryAssociation(
    name="line75",
    ends={
        Property(name="Line77", type=hlcorestructure_ArcGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerArcGraphics76", type=hlcorestructure_Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerArc78: BinaryAssociation = BinaryAssociation(
    name="containerArc78",
    ends={
        Property(name="Arc", type=hlcorestructure_ArcGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="arcgraphics", type=hlcorestructure_Arc, multiplicity=Multiplicity(0, 1))
    }
)
source79: BinaryAssociation = BinaryAssociation(
    name="source79",
    ends={
        Property(name="Node80", type=hlcorestructure_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="OutArcs", type=hlcorestructure_Node, multiplicity=Multiplicity(1, 1))
    }
)
target81: BinaryAssociation = BinaryAssociation(
    name="target81",
    ends={
        Property(name="Node82", type=hlcorestructure_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="InArcs", type=hlcorestructure_Node, multiplicity=Multiplicity(1, 1))
    }
)
positions73: BinaryAssociation = BinaryAssociation(
    name="positions73",
    ends={
        Property(name="Position74", type=hlcorestructure_ArcGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerArcGraphics", type=hlcorestructure_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hlinscription85: BinaryAssociation = BinaryAssociation(
    name="hlinscription85",
    ends={
        Property(name="HLAnnotation", type=hlcorestructure_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="containerArc86", type=hlcorestructure_HLAnnotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
InArcs87: BinaryAssociation = BinaryAssociation(
    name="InArcs87",
    ends={
        Property(name="Arc88", type=hlcorestructure_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=hlcorestructure_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
OutArcs89: BinaryAssociation = BinaryAssociation(
    name="OutArcs89",
    ends={
        Property(name="Arc90", type=hlcorestructure_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=hlcorestructure_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
nodegraphics91: BinaryAssociation = BinaryAssociation(
    name="nodegraphics91",
    ends={
        Property(name="NodeGraphics92", type=hlcorestructure_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNode", type=hlcorestructure_NodeGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arcgraphics83: BinaryAssociation = BinaryAssociation(
    name="arcgraphics83",
    ends={
        Property(name="ArcGraphics84", type=hlcorestructure_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="containerArc", type=hlcorestructure_ArcGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerAnnotationGraphics93: BinaryAssociation = BinaryAssociation(
    name="containerAnnotationGraphics93",
    ends={
        Property(name="AnnotationGraphics94", type=hlcorestructure_Font, multiplicity=Multiplicity(1, 1)),
        Property(name="font", type=hlcorestructure_AnnotationGraphics, multiplicity=Multiplicity(0, 1))
    }
)
referencingPlaces95: BinaryAssociation = BinaryAssociation(
    name="referencingPlaces95",
    ends={
        Property(name="RefPlace", type=hlcorestructure_PlaceNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ref", type=hlcorestructure_RefPlace, multiplicity=Multiplicity(0, 9999))
    }
)
referencingTransitions96: BinaryAssociation = BinaryAssociation(
    name="referencingTransitions96",
    ends={
        Property(name="RefTransition", type=hlcorestructure_TransitionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ref97", type=hlcorestructure_RefTransition, multiplicity=Multiplicity(0, 9999))
    }
)
type98: BinaryAssociation = BinaryAssociation(
    name="type98",
    ends={
        Property(name="Type", type=hlcorestructure_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPlace", type=hlcorestructure_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
hlinitialMarking99: BinaryAssociation = BinaryAssociation(
    name="hlinitialMarking99",
    ends={
        Property(name="HLMarking", type=hlcorestructure_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPlace100", type=hlcorestructure_HLMarking, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref101: BinaryAssociation = BinaryAssociation(
    name="ref101",
    ends={
        Property(name="TransitionNode", type=hlcorestructure_RefTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="referencingTransitions", type=hlcorestructure_TransitionNode, multiplicity=Multiplicity(1, 1))
    }
)
condition102: BinaryAssociation = BinaryAssociation(
    name="condition102",
    ends={
        Property(name="Condition", type=hlcorestructure_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="containerTransition", type=hlcorestructure_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref103: BinaryAssociation = BinaryAssociation(
    name="ref103",
    ends={
        Property(name="PlaceNode", type=hlcorestructure_RefPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="referencingPlaces", type=hlcorestructure_PlaceNode, multiplicity=Multiplicity(1, 1))
    }
)
annotationgraphics104: BinaryAssociation = BinaryAssociation(
    name="annotationgraphics104",
    ends={
        Property(name="AnnotationGraphics105", type=hlcorestructure_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="containerAnnotation", type=hlcorestructure_AnnotationGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerToolInfo106: BinaryAssociation = BinaryAssociation(
    name="containerToolInfo106",
    ends={
        Property(name="ToolInfo107", type=hlcorestructure_AnyObject, multiplicity=Multiplicity(1, 1)),
        Property(name="toolInfoModel", type=hlcorestructure_ToolInfo, multiplicity=Multiplicity(0, 1))
    }
)
structure108: BinaryAssociation = BinaryAssociation(
    name="structure108",
    ends={
        Property(name="terms.ecoreSort", type=hlcorestructure_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="containerType", type=hlcorestructure_Sort, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerPlace109: BinaryAssociation = BinaryAssociation(
    name="containerPlace109",
    ends={
        Property(name="Place", type=hlcorestructure_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=hlcorestructure_Place, multiplicity=Multiplicity(0, 1))
    }
)
structure110: BinaryAssociation = BinaryAssociation(
    name="structure110",
    ends={
        Property(name="terms.ecoreTerm", type=hlcorestructure_HLMarking, multiplicity=Multiplicity(1, 1)),
        Property(name="containerHLMarking", type=hlcorestructure_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerPlace111: BinaryAssociation = BinaryAssociation(
    name="containerPlace111",
    ends={
        Property(name="Place112", type=hlcorestructure_HLMarking, multiplicity=Multiplicity(1, 1)),
        Property(name="hlinitialMarking", type=hlcorestructure_Place, multiplicity=Multiplicity(0, 1))
    }
)
structure113: BinaryAssociation = BinaryAssociation(
    name="structure113",
    ends={
        Property(name="terms.ecoreTerm114", type=hlcorestructure_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="containerCondition", type=hlcorestructure_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerTransition115: BinaryAssociation = BinaryAssociation(
    name="containerTransition115",
    ends={
        Property(name="Transition", type=hlcorestructure_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="condition", type=hlcorestructure_Transition, multiplicity=Multiplicity(0, 1))
    }
)
structure116: BinaryAssociation = BinaryAssociation(
    name="structure116",
    ends={
        Property(name="terms.ecoreTerm117", type=hlcorestructure_HLAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="containerHLAnnotation", type=hlcorestructure_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerArc118: BinaryAssociation = BinaryAssociation(
    name="containerArc118",
    ends={
        Property(name="Arc119", type=hlcorestructure_HLAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="hlinscription", type=hlcorestructure_Arc, multiplicity=Multiplicity(0, 1))
    }
)
structure120: BinaryAssociation = BinaryAssociation(
    name="structure120",
    ends={
        Property(name="terms.ecoreDeclarations", type=hlcorestructure_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="containerDeclaration", type=hlcorestructure_Declarations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerDeclarationPetriNet121: BinaryAssociation = BinaryAssociation(
    name="containerDeclarationPetriNet121",
    ends={
        Property(name="PetriNet122", type=hlcorestructure_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="declaration", type=hlcorestructure_PetriNet, multiplicity=Multiplicity(0, 1))
    }
)
containerDeclarationPage123: BinaryAssociation = BinaryAssociation(
    name="containerDeclarationPage123",
    ends={
        Property(name="Page125", type=hlcorestructure_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="declaration124", type=hlcorestructure_Page, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_hlcorestructure_Page_PnObject = Generalization(general=PnObject, specific=hlcorestructure_Page)
gen_hlcorestructure_Name_Annotation = Generalization(general=Annotation, specific=hlcorestructure_Name)
gen_hlcorestructure_NodeGraphics_Graphics = Generalization(general=Graphics, specific=hlcorestructure_NodeGraphics)
gen_hlcorestructure_Position_Coordinate = Generalization(general=Coordinate, specific=hlcorestructure_Position)
gen_hlcorestructure_Offset_Coordinate = Generalization(general=Coordinate, specific=hlcorestructure_Offset)
gen_hlcorestructure_Dimension_Coordinate = Generalization(general=Coordinate, specific=hlcorestructure_Dimension)
gen_hlcorestructure_AnnotationGraphics_Graphics = Generalization(general=Graphics, specific=hlcorestructure_AnnotationGraphics)
gen_hlcorestructure_ArcGraphics_Graphics = Generalization(general=Graphics, specific=hlcorestructure_ArcGraphics)
gen_hlcorestructure_Arc_PnObject = Generalization(general=PnObject, specific=hlcorestructure_Arc)
gen_hlcorestructure_Node_PnObject = Generalization(general=PnObject, specific=hlcorestructure_Node)
gen_hlcorestructure_PlaceNode_Node = Generalization(general=Node, specific=hlcorestructure_PlaceNode)
gen_hlcorestructure_TransitionNode_Node = Generalization(general=Node, specific=hlcorestructure_TransitionNode)
gen_hlcorestructure_Place_PlaceNode = Generalization(general=PlaceNode, specific=hlcorestructure_Place)
gen_hlcorestructure_RefTransition_TransitionNode = Generalization(general=TransitionNode, specific=hlcorestructure_RefTransition)
gen_hlcorestructure_Transition_TransitionNode = Generalization(general=TransitionNode, specific=hlcorestructure_Transition)
gen_hlcorestructure_RefPlace_PlaceNode = Generalization(general=PlaceNode, specific=hlcorestructure_RefPlace)
gen_hlcorestructure_Attribute_Label = Generalization(general=Label, specific=hlcorestructure_Attribute)
gen_hlcorestructure_HLCoreAnnotation_Annotation = Generalization(general=Annotation, specific=hlcorestructure_HLCoreAnnotation)
gen_hlcorestructure_Type_HLCoreAnnotation = Generalization(general=HLCoreAnnotation, specific=hlcorestructure_Type)
gen_hlcorestructure_Annotation_Label = Generalization(general=Label, specific=hlcorestructure_Annotation)
gen_hlcorestructure_HLMarking_HLCoreAnnotation = Generalization(general=HLCoreAnnotation, specific=hlcorestructure_HLMarking)
gen_hlcorestructure_Condition_HLCoreAnnotation = Generalization(general=HLCoreAnnotation, specific=hlcorestructure_Condition)
gen_hlcorestructure_HLAnnotation_HLCoreAnnotation = Generalization(general=HLCoreAnnotation, specific=hlcorestructure_HLAnnotation)
gen_hlcorestructure_Declaration_HLCoreAnnotation = Generalization(general=HLCoreAnnotation, specific=hlcorestructure_Declaration)

# Domain Model
domain_model = DomainModel(
    name="hlcorestructure",
    types={hlcorestructure_PetriNetDoc, hlcorestructure_PetriNet, hlcorestructure_Page, hlcorestructure_Name, hlcorestructure_Declaration, PnObject, hlcorestructure_PnObject, hlcorestructure_ToolInfo, hlcorestructure_NodeGraphics, Annotation, hlcorestructure_Label, hlcorestructure_AnyObject, Graphics, hlcorestructure_Position, hlcorestructure_Dimension, hlcorestructure_Fill, hlcorestructure_Line, hlcorestructure_Node, hlcorestructure_Graphics, hlcorestructure_Coordinate, Coordinate, hlcorestructure_ArcGraphics, hlcorestructure_Offset, hlcorestructure_AnnotationGraphics, hlcorestructure_Font, hlcorestructure_Annotation, hlcorestructure_Arc, hlcorestructure_HLAnnotation, hlcorestructure_PlaceNode, Node, hlcorestructure_RefPlace, hlcorestructure_TransitionNode, hlcorestructure_RefTransition, hlcorestructure_Place, PlaceNode, hlcorestructure_Type, hlcorestructure_HLMarking, TransitionNode, hlcorestructure_Transition, hlcorestructure_Condition, hlcorestructure_Attribute, Label, hlcorestructure_HLCoreAnnotation, HLCoreAnnotation, hlcorestructure_Sort, hlcorestructure_Term, hlcorestructure_Declarations, PNType, CSS2Color, Gradient, LineShape, FontAlign, CSS2FontFamily, CSS2FontSize, CSS2FontStyle, CSS2FontWeight, FontDecoration, LineStyle},
    associations={nets0, pages1, name2, containerPetriNetDoc5, declaration6, objects7, containerPetriNet8, toolspecifics3, nodegraphics10, declaration12, name14, toolspecifics16, containerPage18, containerNamePetriNet20, containerNamePnObject22, containerPetriNet25, containerLabel30, toolInfoModel32, toolspecifics33, position35, dimension36, fill37, containerPnObject27, line38, containerNode40, containerPage41, containerArcGraphics44, containerPNodeGraphics45, containerAnnotationGraphics47, containerDNodeGraphics48, offset50, fill51, line54, font57, containerAnnotation59, containerNodeGraphics60, containerAnnotationGraphics62, containerNodeGraphics65, containerArcGraphics67, containerAnnotationGraphics70, line75, containerArc78, source79, target81, positions73, hlinscription85, InArcs87, OutArcs89, nodegraphics91, arcgraphics83, containerAnnotationGraphics93, referencingPlaces95, referencingTransitions96, type98, hlinitialMarking99, ref101, condition102, ref103, annotationgraphics104, containerToolInfo106, structure108, containerPlace109, structure110, containerPlace111, structure113, containerTransition115, structure116, containerArc118, structure120, containerDeclarationPetriNet121, containerDeclarationPage123},
    generalizations={gen_hlcorestructure_Page_PnObject, gen_hlcorestructure_Name_Annotation, gen_hlcorestructure_NodeGraphics_Graphics, gen_hlcorestructure_Position_Coordinate, gen_hlcorestructure_Offset_Coordinate, gen_hlcorestructure_Dimension_Coordinate, gen_hlcorestructure_AnnotationGraphics_Graphics, gen_hlcorestructure_ArcGraphics_Graphics, gen_hlcorestructure_Arc_PnObject, gen_hlcorestructure_Node_PnObject, gen_hlcorestructure_PlaceNode_Node, gen_hlcorestructure_TransitionNode_Node, gen_hlcorestructure_Place_PlaceNode, gen_hlcorestructure_RefTransition_TransitionNode, gen_hlcorestructure_Transition_TransitionNode, gen_hlcorestructure_RefPlace_PlaceNode, gen_hlcorestructure_Attribute_Label, gen_hlcorestructure_HLCoreAnnotation_Annotation, gen_hlcorestructure_Type_HLCoreAnnotation, gen_hlcorestructure_Annotation_Label, gen_hlcorestructure_HLMarking_HLCoreAnnotation, gen_hlcorestructure_Condition_HLCoreAnnotation, gen_hlcorestructure_HLAnnotation_HLCoreAnnotation, gen_hlcorestructure_Declaration_HLCoreAnnotation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)