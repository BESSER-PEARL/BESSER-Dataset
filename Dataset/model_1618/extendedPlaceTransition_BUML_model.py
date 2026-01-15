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
            EnumerationLiteral(name="PTNET"),
			EnumerationLiteral(name="COREMODEL"),
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
			EnumerationLiteral(name="BLACK"),
			EnumerationLiteral(name="BLUE"),
			EnumerationLiteral(name="FUCHSIA"),
			EnumerationLiteral(name="GRAY"),
			EnumerationLiteral(name="GREEN"),
			EnumerationLiteral(name="LIME"),
			EnumerationLiteral(name="MAROON"),
			EnumerationLiteral(name="NAVY"),
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
            EnumerationLiteral(name="CURVE"),
			EnumerationLiteral(name="LINE")
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

LineStyle: Enumeration = Enumeration(
    name="LineStyle",
    literals={
            EnumerationLiteral(name="DOT"),
			EnumerationLiteral(name="SOLID"),
			EnumerationLiteral(name="DASH")
    }
)

# Classes
ptnet_Place = Class(name="ptnet::Place")
ptnet_PTMarking = Class(name="ptnet::PTMarking")
Annotation = Class(name="Annotation")
ptnet_PetriNetDoc = Class(name="ptnet::PetriNetDoc")
ptnet_PetriNet = Class(name="ptnet::PetriNet")
ptnet_PTArcAnnotation = Class(name="ptnet::PTArcAnnotation")
ptnet_Arc = Class(name="ptnet::Arc")
ptnet_Name = Class(name="ptnet::Name")
ptnet_ToolInfo = Class(name="ptnet::ToolInfo")
ptnet_Page = Class(name="ptnet::Page")
ptnet_PnObject = Class(name="ptnet::PnObject", is_abstract=True)
PnObject = Class(name="PnObject")
ptnet_NodeGraphics = Class(name="ptnet::NodeGraphics")
ptnet_Label = Class(name="ptnet::Label", is_abstract=True)
ptnet_AnyObject = Class(name="ptnet::AnyObject", is_abstract=True)
ptnet_Fill = Class(name="ptnet::Fill")
ptnet_Line = Class(name="ptnet::Line")
ptnet_Node = Class(name="ptnet::Node", is_abstract=True)
Graphics = Class(name="Graphics")
ptnet_Position = Class(name="ptnet::Position")
ptnet_Dimension = Class(name="ptnet::Dimension")
Coordinate = Class(name="Coordinate")
ptnet_Graphics = Class(name="ptnet::Graphics", is_abstract=True)
ptnet_Coordinate = Class(name="ptnet::Coordinate", is_abstract=True)
ptnet_Offset = Class(name="ptnet::Offset")
ptnet_ArcGraphics = Class(name="ptnet::ArcGraphics")
ptnet_AnnotationGraphics = Class(name="ptnet::AnnotationGraphics")
ptnet_Annotation = Class(name="ptnet::Annotation", is_abstract=True)
ptnet_Font = Class(name="ptnet::Font")
ptnet_ArcNature = Class(name="ptnet::ArcNature")
ptnet_PlaceNode = Class(name="ptnet::PlaceNode", is_abstract=True)
Node = Class(name="Node")
ptnet_RefPlace = Class(name="ptnet::RefPlace")
ptnet_TransitionNode = Class(name="ptnet::TransitionNode", is_abstract=True)
TransitionNode = Class(name="TransitionNode")
ptnet_Transition = Class(name="ptnet::Transition")
ptnet_RefTransition = Class(name="ptnet::RefTransition")
PlaceNode = Class(name="PlaceNode")
ptnet_Capacity = Class(name="ptnet::Capacity")
ptnet_Attribute = Class(name="ptnet::Attribute", is_abstract=True)
Label = Class(name="Label")

# ptnet_Place class attributes and methods

# ptnet_PTMarking class attributes and methods
ptnet_PTMarking_text: Property = Property(name="text", type=StringType)
ptnet_PTMarking.attributes={ptnet_PTMarking_text}

# Annotation class attributes and methods

# ptnet_PetriNetDoc class attributes and methods
ptnet_PetriNetDoc_xmlns: Property = Property(name="xmlns", type=StringType)
ptnet_PetriNetDoc.attributes={ptnet_PetriNetDoc_xmlns}

# ptnet_PetriNet class attributes and methods
ptnet_PetriNet_id: Property = Property(name="id", type=StringType)
ptnet_PetriNet_type: Property = Property(name="type", type=StringType)
ptnet_PetriNet.attributes={ptnet_PetriNet_type, ptnet_PetriNet_id}

# ptnet_PTArcAnnotation class attributes and methods
ptnet_PTArcAnnotation_text: Property = Property(name="text", type=StringType)
ptnet_PTArcAnnotation.attributes={ptnet_PTArcAnnotation_text}

# ptnet_Arc class attributes and methods

# ptnet_Name class attributes and methods
ptnet_Name_text: Property = Property(name="text", type=StringType)
ptnet_Name.attributes={ptnet_Name_text}

# ptnet_ToolInfo class attributes and methods
ptnet_ToolInfo_tool: Property = Property(name="tool", type=StringType)
ptnet_ToolInfo_version: Property = Property(name="version", type=StringType)
ptnet_ToolInfo_formattedXMLBuffer: Property = Property(name="formattedXMLBuffer", type=StringType)
ptnet_ToolInfo_toolInfoGrammarURI: Property = Property(name="toolInfoGrammarURI", type=StringType)
ptnet_ToolInfo.attributes={ptnet_ToolInfo_toolInfoGrammarURI, ptnet_ToolInfo_tool, ptnet_ToolInfo_formattedXMLBuffer, ptnet_ToolInfo_version}

# ptnet_Page class attributes and methods

# ptnet_PnObject class attributes and methods
ptnet_PnObject_id: Property = Property(name="id", type=StringType)
ptnet_PnObject.attributes={ptnet_PnObject_id}

# PnObject class attributes and methods

# ptnet_NodeGraphics class attributes and methods

# ptnet_Label class attributes and methods

# ptnet_AnyObject class attributes and methods

# ptnet_Fill class attributes and methods
ptnet_Fill_gradientcolor: Property = Property(name="gradientcolor", type=StringType)
ptnet_Fill_gradientrotation: Property = Property(name="gradientrotation", type=StringType)
ptnet_Fill_color: Property = Property(name="color", type=StringType)
ptnet_Fill_image: Property = Property(name="image", type=StringType)
ptnet_Fill.attributes={ptnet_Fill_gradientcolor, ptnet_Fill_gradientrotation, ptnet_Fill_color, ptnet_Fill_image}

# ptnet_Line class attributes and methods
ptnet_Line_color: Property = Property(name="color", type=StringType)
ptnet_Line_shape: Property = Property(name="shape", type=StringType)
ptnet_Line_width: Property = Property(name="width", type=StringType)
ptnet_Line_style: Property = Property(name="style", type=StringType)
ptnet_Line.attributes={ptnet_Line_shape, ptnet_Line_color, ptnet_Line_style, ptnet_Line_width}

# ptnet_Node class attributes and methods

# Graphics class attributes and methods

# ptnet_Position class attributes and methods

# ptnet_Dimension class attributes and methods

# Coordinate class attributes and methods

# ptnet_Graphics class attributes and methods

# ptnet_Coordinate class attributes and methods
ptnet_Coordinate_y: Property = Property(name="y", type=StringType)
ptnet_Coordinate_x: Property = Property(name="x", type=StringType)
ptnet_Coordinate.attributes={ptnet_Coordinate_y, ptnet_Coordinate_x}

# ptnet_Offset class attributes and methods

# ptnet_ArcGraphics class attributes and methods

# ptnet_AnnotationGraphics class attributes and methods

# ptnet_Annotation class attributes and methods

# ptnet_Font class attributes and methods
ptnet_Font_rotation: Property = Property(name="rotation", type=StringType)
ptnet_Font_size: Property = Property(name="size", type=StringType)
ptnet_Font_style: Property = Property(name="style", type=StringType)
ptnet_Font_weight: Property = Property(name="weight", type=StringType)
ptnet_Font_align: Property = Property(name="align", type=StringType)
ptnet_Font_decoration: Property = Property(name="decoration", type=StringType)
ptnet_Font_family: Property = Property(name="family", type=StringType)
ptnet_Font.attributes={ptnet_Font_align, ptnet_Font_family, ptnet_Font_style, ptnet_Font_weight, ptnet_Font_size, ptnet_Font_decoration, ptnet_Font_rotation}

# ptnet_ArcNature class attributes and methods

# ptnet_PlaceNode class attributes and methods

# Node class attributes and methods

# ptnet_RefPlace class attributes and methods

# ptnet_TransitionNode class attributes and methods

# TransitionNode class attributes and methods

# ptnet_Transition class attributes and methods

# ptnet_RefTransition class attributes and methods

# PlaceNode class attributes and methods

# ptnet_Capacity class attributes and methods

# ptnet_Attribute class attributes and methods

# Label class attributes and methods

# Relationships
containerPlace0: BinaryAssociation = BinaryAssociation(
    name="containerPlace0",
    ends={
        Property(name="Place", type=ptnet_PTMarking, multiplicity=Multiplicity(1, 1)),
        Property(name="initialMarking", type=ptnet_Place, multiplicity=Multiplicity(0, 1))
    }
)
nets2: BinaryAssociation = BinaryAssociation(
    name="nets2",
    ends={
        Property(name="PetriNet", type=ptnet_PetriNetDoc, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPetriNetDoc", type=ptnet_PetriNet, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
containerArc1: BinaryAssociation = BinaryAssociation(
    name="containerArc1",
    ends={
        Property(name="Arc", type=ptnet_PTArcAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="inscription", type=ptnet_Arc, multiplicity=Multiplicity(0, 1))
    }
)
name4: BinaryAssociation = BinaryAssociation(
    name="name4",
    ends={
        Property(name="Name", type=ptnet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNamePetriNet", type=ptnet_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
toolspecifics5: BinaryAssociation = BinaryAssociation(
    name="toolspecifics5",
    ends={
        Property(name="ToolInfo", type=ptnet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPetriNet6", type=ptnet_ToolInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pages3: BinaryAssociation = BinaryAssociation(
    name="pages3",
    ends={
        Property(name="Page", type=ptnet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPetriNet", type=ptnet_Page, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
objects8: BinaryAssociation = BinaryAssociation(
    name="objects8",
    ends={
        Property(name="PnObject", type=ptnet_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPage", type=ptnet_PnObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerPetriNetDoc7: BinaryAssociation = BinaryAssociation(
    name="containerPetriNetDoc7",
    ends={
        Property(name="PetriNetDoc", type=ptnet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="nets", type=ptnet_PetriNetDoc, multiplicity=Multiplicity(0, 1))
    }
)
containerPetriNet9: BinaryAssociation = BinaryAssociation(
    name="containerPetriNet9",
    ends={
        Property(name="PetriNet10", type=ptnet_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="pages", type=ptnet_PetriNet, multiplicity=Multiplicity(0, 1))
    }
)
nodegraphics11: BinaryAssociation = BinaryAssociation(
    name="nodegraphics11",
    ends={
        Property(name="NodeGraphics", type=ptnet_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPage12", type=ptnet_NodeGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
toolspecifics15: BinaryAssociation = BinaryAssociation(
    name="toolspecifics15",
    ends={
        Property(name="ToolInfo16", type=ptnet_PnObject, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPnObject", type=ptnet_ToolInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name13: BinaryAssociation = BinaryAssociation(
    name="name13",
    ends={
        Property(name="Name14", type=ptnet_PnObject, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNamePnObject", type=ptnet_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerNamePetriNet19: BinaryAssociation = BinaryAssociation(
    name="containerNamePetriNet19",
    ends={
        Property(name="PetriNet20", type=ptnet_Name, multiplicity=Multiplicity(1, 1)),
        Property(name="name", type=ptnet_PetriNet, multiplicity=Multiplicity(0, 1))
    }
)
containerNamePnObject21: BinaryAssociation = BinaryAssociation(
    name="containerNamePnObject21",
    ends={
        Property(name="PnObject23", type=ptnet_Name, multiplicity=Multiplicity(1, 1)),
        Property(name="name22", type=ptnet_PnObject, multiplicity=Multiplicity(0, 1))
    }
)
containerPage17: BinaryAssociation = BinaryAssociation(
    name="containerPage17",
    ends={
        Property(name="Page18", type=ptnet_PnObject, multiplicity=Multiplicity(1, 1)),
        Property(name="objects", type=ptnet_Page, multiplicity=Multiplicity(0, 1))
    }
)
containerPnObject26: BinaryAssociation = BinaryAssociation(
    name="containerPnObject26",
    ends={
        Property(name="PnObject28", type=ptnet_ToolInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="toolspecifics27", type=ptnet_PnObject, multiplicity=Multiplicity(0, 1))
    }
)
containerLabel29: BinaryAssociation = BinaryAssociation(
    name="containerLabel29",
    ends={
        Property(name="Label", type=ptnet_ToolInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="toolspecifics30", type=ptnet_Label, multiplicity=Multiplicity(0, 1))
    }
)
toolInfoModel31: BinaryAssociation = BinaryAssociation(
    name="toolInfoModel31",
    ends={
        Property(name="AnyObject", type=ptnet_ToolInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="containerToolInfo", type=ptnet_AnyObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerPetriNet24: BinaryAssociation = BinaryAssociation(
    name="containerPetriNet24",
    ends={
        Property(name="PetriNet25", type=ptnet_ToolInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="toolspecifics", type=ptnet_PetriNet, multiplicity=Multiplicity(0, 1))
    }
)
fill36: BinaryAssociation = BinaryAssociation(
    name="fill36",
    ends={
        Property(name="Fill", type=ptnet_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNodeGraphics", type=ptnet_Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
line37: BinaryAssociation = BinaryAssociation(
    name="line37",
    ends={
        Property(name="Line", type=ptnet_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNodeGraphics38", type=ptnet_Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerNode39: BinaryAssociation = BinaryAssociation(
    name="containerNode39",
    ends={
        Property(name="Node", type=ptnet_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="nodegraphics", type=ptnet_Node, multiplicity=Multiplicity(0, 1))
    }
)
toolspecifics32: BinaryAssociation = BinaryAssociation(
    name="toolspecifics32",
    ends={
        Property(name="ToolInfo33", type=ptnet_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="containerLabel", type=ptnet_ToolInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
position34: BinaryAssociation = BinaryAssociation(
    name="position34",
    ends={
        Property(name="Position", type=ptnet_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPNodeGraphics", type=ptnet_Position, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dimension35: BinaryAssociation = BinaryAssociation(
    name="dimension35",
    ends={
        Property(name="Dimension", type=ptnet_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerDNodeGraphics", type=ptnet_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerPage40: BinaryAssociation = BinaryAssociation(
    name="containerPage40",
    ends={
        Property(name="Page42", type=ptnet_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="nodegraphics41", type=ptnet_Page, multiplicity=Multiplicity(0, 1))
    }
)
containerPNodeGraphics44: BinaryAssociation = BinaryAssociation(
    name="containerPNodeGraphics44",
    ends={
        Property(name="NodeGraphics45", type=ptnet_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="position", type=ptnet_NodeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerArcGraphics43: BinaryAssociation = BinaryAssociation(
    name="containerArcGraphics43",
    ends={
        Property(name="ArcGraphics", type=ptnet_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="positions", type=ptnet_ArcGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerDNodeGraphics47: BinaryAssociation = BinaryAssociation(
    name="containerDNodeGraphics47",
    ends={
        Property(name="NodeGraphics48", type=ptnet_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="dimension", type=ptnet_NodeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerAnnotationGraphics46: BinaryAssociation = BinaryAssociation(
    name="containerAnnotationGraphics46",
    ends={
        Property(name="AnnotationGraphics", type=ptnet_Offset, multiplicity=Multiplicity(1, 1)),
        Property(name="offset", type=ptnet_AnnotationGraphics, multiplicity=Multiplicity(0, 1))
    }
)
fill50: BinaryAssociation = BinaryAssociation(
    name="fill50",
    ends={
        Property(name="Fill52", type=ptnet_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerAnnotationGraphics51", type=ptnet_Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
offset49: BinaryAssociation = BinaryAssociation(
    name="offset49",
    ends={
        Property(name="Offset", type=ptnet_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerAnnotationGraphics", type=ptnet_Offset, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerAnnotation58: BinaryAssociation = BinaryAssociation(
    name="containerAnnotation58",
    ends={
        Property(name="Annotation", type=ptnet_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="annotationgraphics", type=ptnet_Annotation, multiplicity=Multiplicity(0, 1))
    }
)
line53: BinaryAssociation = BinaryAssociation(
    name="line53",
    ends={
        Property(name="Line55", type=ptnet_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerAnnotationGraphics54", type=ptnet_Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
font56: BinaryAssociation = BinaryAssociation(
    name="font56",
    ends={
        Property(name="Font", type=ptnet_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerAnnotationGraphics57", type=ptnet_Font, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerAnnotationGraphics61: BinaryAssociation = BinaryAssociation(
    name="containerAnnotationGraphics61",
    ends={
        Property(name="AnnotationGraphics63", type=ptnet_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="fill62", type=ptnet_AnnotationGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerNodeGraphics59: BinaryAssociation = BinaryAssociation(
    name="containerNodeGraphics59",
    ends={
        Property(name="NodeGraphics60", type=ptnet_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="fill", type=ptnet_NodeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerNodeGraphics64: BinaryAssociation = BinaryAssociation(
    name="containerNodeGraphics64",
    ends={
        Property(name="NodeGraphics65", type=ptnet_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="line", type=ptnet_NodeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerArcGraphics66: BinaryAssociation = BinaryAssociation(
    name="containerArcGraphics66",
    ends={
        Property(name="ArcGraphics68", type=ptnet_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="line67", type=ptnet_ArcGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerAnnotationGraphics69: BinaryAssociation = BinaryAssociation(
    name="containerAnnotationGraphics69",
    ends={
        Property(name="AnnotationGraphics71", type=ptnet_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="line70", type=ptnet_AnnotationGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerArc77: BinaryAssociation = BinaryAssociation(
    name="containerArc77",
    ends={
        Property(name="Arc78", type=ptnet_ArcGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="arcgraphics", type=ptnet_Arc, multiplicity=Multiplicity(0, 1))
    }
)
positions72: BinaryAssociation = BinaryAssociation(
    name="positions72",
    ends={
        Property(name="Position73", type=ptnet_ArcGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerArcGraphics", type=ptnet_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
line74: BinaryAssociation = BinaryAssociation(
    name="line74",
    ends={
        Property(name="Line76", type=ptnet_ArcGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerArcGraphics75", type=ptnet_Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target81: BinaryAssociation = BinaryAssociation(
    name="target81",
    ends={
        Property(name="Node82", type=ptnet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="InArcs", type=ptnet_Node, multiplicity=Multiplicity(1, 1))
    }
)
arcgraphics83: BinaryAssociation = BinaryAssociation(
    name="arcgraphics83",
    ends={
        Property(name="ArcGraphics84", type=ptnet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="containerArc", type=ptnet_ArcGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inscription85: BinaryAssociation = BinaryAssociation(
    name="inscription85",
    ends={
        Property(name="PTArcAnnotation", type=ptnet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="containerArc86", type=ptnet_PTArcAnnotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nature87: BinaryAssociation = BinaryAssociation(
    name="nature87",
    ends={
        Property(name="attributeExtensions.ecoreArcNature", type=ptnet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="cointainerArc", type=ptnet_ArcNature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source79: BinaryAssociation = BinaryAssociation(
    name="source79",
    ends={
        Property(name="Node80", type=ptnet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="OutArcs", type=ptnet_Node, multiplicity=Multiplicity(1, 1))
    }
)
containerAnnotationGraphics94: BinaryAssociation = BinaryAssociation(
    name="containerAnnotationGraphics94",
    ends={
        Property(name="AnnotationGraphics95", type=ptnet_Font, multiplicity=Multiplicity(1, 1)),
        Property(name="font", type=ptnet_AnnotationGraphics, multiplicity=Multiplicity(0, 1))
    }
)
InArcs88: BinaryAssociation = BinaryAssociation(
    name="InArcs88",
    ends={
        Property(name="Arc89", type=ptnet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=ptnet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
OutArcs90: BinaryAssociation = BinaryAssociation(
    name="OutArcs90",
    ends={
        Property(name="Arc91", type=ptnet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=ptnet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
nodegraphics92: BinaryAssociation = BinaryAssociation(
    name="nodegraphics92",
    ends={
        Property(name="NodeGraphics93", type=ptnet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNode", type=ptnet_NodeGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referencingPlaces96: BinaryAssociation = BinaryAssociation(
    name="referencingPlaces96",
    ends={
        Property(name="RefPlace", type=ptnet_PlaceNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ref", type=ptnet_RefPlace, multiplicity=Multiplicity(0, 9999))
    }
)
ref102: BinaryAssociation = BinaryAssociation(
    name="ref102",
    ends={
        Property(name="TransitionNode", type=ptnet_RefTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="referencingTransitions", type=ptnet_TransitionNode, multiplicity=Multiplicity(1, 1))
    }
)
referencingTransitions97: BinaryAssociation = BinaryAssociation(
    name="referencingTransitions97",
    ends={
        Property(name="RefTransition", type=ptnet_TransitionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ref98", type=ptnet_RefTransition, multiplicity=Multiplicity(0, 9999))
    }
)
initialMarking99: BinaryAssociation = BinaryAssociation(
    name="initialMarking99",
    ends={
        Property(name="PTMarking", type=ptnet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPlace", type=ptnet_PTMarking, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
capacity100: BinaryAssociation = BinaryAssociation(
    name="capacity100",
    ends={
        Property(name="annotationExtensions.ecoreCapacity", type=ptnet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPlace101", type=ptnet_Capacity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotationgraphics104: BinaryAssociation = BinaryAssociation(
    name="annotationgraphics104",
    ends={
        Property(name="AnnotationGraphics105", type=ptnet_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="containerAnnotation", type=ptnet_AnnotationGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref103: BinaryAssociation = BinaryAssociation(
    name="ref103",
    ends={
        Property(name="PlaceNode", type=ptnet_RefPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="referencingPlaces", type=ptnet_PlaceNode, multiplicity=Multiplicity(1, 1))
    }
)
containerToolInfo106: BinaryAssociation = BinaryAssociation(
    name="containerToolInfo106",
    ends={
        Property(name="ToolInfo107", type=ptnet_AnyObject, multiplicity=Multiplicity(1, 1)),
        Property(name="toolInfoModel", type=ptnet_ToolInfo, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ptnet_PTMarking_Annotation = Generalization(general=Annotation, specific=ptnet_PTMarking)
gen_ptnet_PTArcAnnotation_Annotation = Generalization(general=Annotation, specific=ptnet_PTArcAnnotation)
gen_ptnet_Page_PnObject = Generalization(general=PnObject, specific=ptnet_Page)
gen_ptnet_Name_Annotation = Generalization(general=Annotation, specific=ptnet_Name)
gen_ptnet_NodeGraphics_Graphics = Generalization(general=Graphics, specific=ptnet_NodeGraphics)
gen_ptnet_Offset_Coordinate = Generalization(general=Coordinate, specific=ptnet_Offset)
gen_ptnet_Position_Coordinate = Generalization(general=Coordinate, specific=ptnet_Position)
gen_ptnet_Dimension_Coordinate = Generalization(general=Coordinate, specific=ptnet_Dimension)
gen_ptnet_AnnotationGraphics_Graphics = Generalization(general=Graphics, specific=ptnet_AnnotationGraphics)
gen_ptnet_ArcGraphics_Graphics = Generalization(general=Graphics, specific=ptnet_ArcGraphics)
gen_ptnet_Arc_PnObject = Generalization(general=PnObject, specific=ptnet_Arc)
gen_ptnet_Node_PnObject = Generalization(general=PnObject, specific=ptnet_Node)
gen_ptnet_PlaceNode_Node = Generalization(general=Node, specific=ptnet_PlaceNode)
gen_ptnet_TransitionNode_Node = Generalization(general=Node, specific=ptnet_TransitionNode)
gen_ptnet_RefTransition_TransitionNode = Generalization(general=TransitionNode, specific=ptnet_RefTransition)
gen_ptnet_Transition_TransitionNode = Generalization(general=TransitionNode, specific=ptnet_Transition)
gen_ptnet_Place_PlaceNode = Generalization(general=PlaceNode, specific=ptnet_Place)
gen_ptnet_Annotation_Label = Generalization(general=Label, specific=ptnet_Annotation)
gen_ptnet_RefPlace_PlaceNode = Generalization(general=PlaceNode, specific=ptnet_RefPlace)
gen_ptnet_Attribute_Label = Generalization(general=Label, specific=ptnet_Attribute)

# Domain Model
domain_model = DomainModel(
    name="ptnet",
    types={ptnet_Place, ptnet_PTMarking, Annotation, ptnet_PetriNetDoc, ptnet_PetriNet, ptnet_PTArcAnnotation, ptnet_Arc, ptnet_Name, ptnet_ToolInfo, ptnet_Page, ptnet_PnObject, PnObject, ptnet_NodeGraphics, ptnet_Label, ptnet_AnyObject, ptnet_Fill, ptnet_Line, ptnet_Node, Graphics, ptnet_Position, ptnet_Dimension, Coordinate, ptnet_Graphics, ptnet_Coordinate, ptnet_Offset, ptnet_ArcGraphics, ptnet_AnnotationGraphics, ptnet_Annotation, ptnet_Font, ptnet_ArcNature, ptnet_PlaceNode, Node, ptnet_RefPlace, ptnet_TransitionNode, TransitionNode, ptnet_Transition, ptnet_RefTransition, PlaceNode, ptnet_Capacity, ptnet_Attribute, Label, PNType, CSS2Color, Gradient, LineShape, CSS2FontFamily, CSS2FontSize, FontAlign, FontDecoration, CSS2FontStyle, CSS2FontWeight, LineStyle},
    associations={containerPlace0, nets2, containerArc1, name4, toolspecifics5, pages3, objects8, containerPetriNetDoc7, containerPetriNet9, nodegraphics11, toolspecifics15, name13, containerNamePetriNet19, containerNamePnObject21, containerPage17, containerPnObject26, containerLabel29, toolInfoModel31, containerPetriNet24, fill36, line37, containerNode39, toolspecifics32, position34, dimension35, containerPage40, containerPNodeGraphics44, containerArcGraphics43, containerDNodeGraphics47, containerAnnotationGraphics46, fill50, offset49, containerAnnotation58, line53, font56, containerAnnotationGraphics61, containerNodeGraphics59, containerNodeGraphics64, containerArcGraphics66, containerAnnotationGraphics69, containerArc77, positions72, line74, target81, arcgraphics83, inscription85, nature87, source79, containerAnnotationGraphics94, InArcs88, OutArcs90, nodegraphics92, referencingPlaces96, ref102, referencingTransitions97, initialMarking99, capacity100, annotationgraphics104, ref103, containerToolInfo106},
    generalizations={gen_ptnet_PTMarking_Annotation, gen_ptnet_PTArcAnnotation_Annotation, gen_ptnet_Page_PnObject, gen_ptnet_Name_Annotation, gen_ptnet_NodeGraphics_Graphics, gen_ptnet_Offset_Coordinate, gen_ptnet_Position_Coordinate, gen_ptnet_Dimension_Coordinate, gen_ptnet_AnnotationGraphics_Graphics, gen_ptnet_ArcGraphics_Graphics, gen_ptnet_Arc_PnObject, gen_ptnet_Node_PnObject, gen_ptnet_PlaceNode_Node, gen_ptnet_TransitionNode_Node, gen_ptnet_RefTransition_TransitionNode, gen_ptnet_Transition_TransitionNode, gen_ptnet_Place_PlaceNode, gen_ptnet_Annotation_Label, gen_ptnet_RefPlace_PlaceNode, gen_ptnet_Attribute_Label},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)