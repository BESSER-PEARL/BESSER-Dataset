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
RotationType: Enumeration = Enumeration(
    name="RotationType",
    literals={
            EnumerationLiteral(name="rtvertical"),
			EnumerationLiteral(name="rthorizontal"),
			EnumerationLiteral(name="rtdiagonal")
    }
)

ShapeType: Enumeration = Enumeration(
    name="ShapeType",
    literals={
            EnumerationLiteral(name="shtline"),
			EnumerationLiteral(name="shtcurve")
    }
)

StyleType: Enumeration = Enumeration(
    name="StyleType",
    literals={
            EnumerationLiteral(name="sttsolid"),
			EnumerationLiteral(name="sttdash"),
			EnumerationLiteral(name="sttdot")
    }
)

DecorationType: Enumeration = Enumeration(
    name="DecorationType",
    literals={
            EnumerationLiteral(name="dtunderligne"),
			EnumerationLiteral(name="dtoverligne"),
			EnumerationLiteral(name="dtlinethrough")
    }
)

AlignType: Enumeration = Enumeration(
    name="AlignType",
    literals={
            EnumerationLiteral(name="atleft"),
			EnumerationLiteral(name="atcenter"),
			EnumerationLiteral(name="atright")
    }
)

# Classes
PNML_URI = Class(name="PNML_URI")
PNML_Color = Class(name="PNML_Color")
PNML_AnyElement = Class(name="PNML_AnyElement")
PNML_NCName = Class(name="PNML_NCName")
PNML_PNMLDocument = Class(name="PNML_PNMLDocument")
URI = Class(name="URI")
PNML_IdedElement = Class(name="PNML_IdedElement", is_abstract=True)
PNML_Module = Class(name="PNML_Module")
IdedElement = Class(name="IdedElement")
Interface = Class(name="Interface")
NetContent = Class(name="NetContent")
PNMLDocument = Class(name="PNMLDocument")
PNML_Interface = Class(name="PNML_Interface")
Node = Class(name="Node")
Reference = Class(name="Reference")
PNML_NetElement = Class(name="PNML_NetElement")
NetElement = Class(name="NetElement")
Module = Class(name="Module")
PNML_NetContent = Class(name="PNML_NetContent", is_abstract=True)
Page = Class(name="Page")
PNML_ToolSpecific = Class(name="PNML_ToolSpecific")
AnyElement = Class(name="AnyElement")
Arc = Class(name="Arc")
PNML_LabeledElement = Class(name="PNML_LabeledElement", is_abstract=True)
Label = Class(name="Label")
AnnotationGraphics = Class(name="AnnotationGraphics")
ToolSpecific = Class(name="ToolSpecific")
NetGraphics = Class(name="NetGraphics")
Name = Class(name="Name")
PNML_Page = Class(name="PNML_Page")
PNML_Name = Class(name="PNML_Name")
PNML_Inscription = Class(name="PNML_Inscription")
PageGraphics = Class(name="PageGraphics")
PNML_InitialMarking = Class(name="PNML_InitialMarking")
Place = Class(name="Place")
PNML_NetContentElement = Class(name="PNML_NetContentElement", is_abstract=True)
PNML_Arc = Class(name="PNML_Arc")
NetContentElement = Class(name="NetContentElement")
PNML_Label = Class(name="PNML_Label")
EdgeGraphics = Class(name="EdgeGraphics")
Inscription = Class(name="Inscription")
LabeledElement = Class(name="LabeledElement")
Instance = Class(name="Instance")
PNML_Node = Class(name="PNML_Node")
PNML_Reference = Class(name="PNML_Reference", is_abstract=True)
NCName = Class(name="NCName")
ImportNode = Class(name="ImportNode")
PNML_ReferencePlace = Class(name="PNML_ReferencePlace")
PNML_ReferenceTransition = Class(name="PNML_ReferenceTransition")
PNML_Instance = Class(name="PNML_Instance")
PNML_ImportNode = Class(name="PNML_ImportNode")
Position = Class(name="Position")
Dimension = Class(name="Dimension")
Fill = Class(name="Fill")
Line = Class(name="Line")
PNML_EdgeGraphics = Class(name="PNML_EdgeGraphics")
NodeGraphics = Class(name="NodeGraphics")
PNML_Place = Class(name="PNML_Place")
InitialMarking = Class(name="InitialMarking")
PNML_Transition = Class(name="PNML_Transition")
PNML_Graphics = Class(name="PNML_Graphics", is_abstract=True)
PNML_NetGraphics = Class(name="PNML_NetGraphics")
Graphics = Class(name="Graphics")
PNML_NodeGraphics = Class(name="PNML_NodeGraphics")
PNML_Coordinate = Class(name="PNML_Coordinate", is_abstract=True)
PNML_Position = Class(name="PNML_Position")
Coordinate = Class(name="Coordinate")
PNML_Offset = Class(name="PNML_Offset")
PNML_AnnotationGraphics = Class(name="PNML_AnnotationGraphics")
Offset = Class(name="Offset")
Font = Class(name="Font")
PNML_PageGraphics = Class(name="PNML_PageGraphics")
PNML_Line = Class(name="PNML_Line")
PNML_Dimension = Class(name="PNML_Dimension")
PNML_Fill = Class(name="PNML_Fill")
Color = Class(name="Color")
PNML_Font = Class(name="PNML_Font")

# PNML_URI class attributes and methods
PNML_URI_value: Property = Property(name="value", type=StringType)
PNML_URI.attributes={PNML_URI_value}

# PNML_Color class attributes and methods

# PNML_AnyElement class attributes and methods
PNML_AnyElement_name: Property = Property(name="name", type=StringType)
PNML_AnyElement_text: Property = Property(name="text", type=StringType)
PNML_AnyElement.attributes={PNML_AnyElement_text, PNML_AnyElement_name}

# PNML_NCName class attributes and methods
PNML_NCName_value: Property = Property(name="value", type=StringType)
PNML_NCName.attributes={PNML_NCName_value}

# PNML_PNMLDocument class attributes and methods

# URI class attributes and methods

# PNML_IdedElement class attributes and methods
PNML_IdedElement_id: Property = Property(name="id", type=StringType)
PNML_IdedElement.attributes={PNML_IdedElement_id}

# PNML_Module class attributes and methods

# IdedElement class attributes and methods

# Interface class attributes and methods

# NetContent class attributes and methods

# PNMLDocument class attributes and methods

# PNML_Interface class attributes and methods

# Node class attributes and methods

# Reference class attributes and methods

# PNML_NetElement class attributes and methods

# NetElement class attributes and methods

# Module class attributes and methods

# PNML_NetContent class attributes and methods

# Page class attributes and methods

# PNML_ToolSpecific class attributes and methods
PNML_ToolSpecific_tool: Property = Property(name="tool", type=StringType)
PNML_ToolSpecific_version: Property = Property(name="version", type=StringType)
PNML_ToolSpecific.attributes={PNML_ToolSpecific_version, PNML_ToolSpecific_tool}

# AnyElement class attributes and methods

# Arc class attributes and methods

# PNML_LabeledElement class attributes and methods

# Label class attributes and methods

# AnnotationGraphics class attributes and methods

# ToolSpecific class attributes and methods

# NetGraphics class attributes and methods

# Name class attributes and methods

# PNML_Page class attributes and methods

# PNML_Name class attributes and methods

# PNML_Inscription class attributes and methods

# PageGraphics class attributes and methods

# PNML_InitialMarking class attributes and methods

# Place class attributes and methods

# PNML_NetContentElement class attributes and methods

# PNML_Arc class attributes and methods

# NetContentElement class attributes and methods

# PNML_Label class attributes and methods
PNML_Label_text: Property = Property(name="text", type=StringType)
PNML_Label.attributes={PNML_Label_text}

# EdgeGraphics class attributes and methods

# Inscription class attributes and methods

# LabeledElement class attributes and methods

# Instance class attributes and methods

# PNML_Node class attributes and methods

# PNML_Reference class attributes and methods

# NCName class attributes and methods

# ImportNode class attributes and methods

# PNML_ReferencePlace class attributes and methods

# PNML_ReferenceTransition class attributes and methods

# PNML_Instance class attributes and methods

# PNML_ImportNode class attributes and methods

# Position class attributes and methods

# Dimension class attributes and methods

# Fill class attributes and methods

# Line class attributes and methods

# PNML_EdgeGraphics class attributes and methods

# NodeGraphics class attributes and methods

# PNML_Place class attributes and methods

# InitialMarking class attributes and methods

# PNML_Transition class attributes and methods

# PNML_Graphics class attributes and methods

# PNML_NetGraphics class attributes and methods

# Graphics class attributes and methods

# PNML_NodeGraphics class attributes and methods

# PNML_Coordinate class attributes and methods
PNML_Coordinate_x: Property = Property(name="x", type=StringType)
PNML_Coordinate_y: Property = Property(name="y", type=StringType)
PNML_Coordinate.attributes={PNML_Coordinate_y, PNML_Coordinate_x}

# PNML_Position class attributes and methods

# Coordinate class attributes and methods

# PNML_Offset class attributes and methods

# PNML_AnnotationGraphics class attributes and methods

# Offset class attributes and methods

# Font class attributes and methods

# PNML_PageGraphics class attributes and methods

# PNML_Line class attributes and methods
PNML_Line_width: Property = Property(name="width", type=StringType)
PNML_Line_shape: Property = Property(name="shape", type=StringType)
PNML_Line_style: Property = Property(name="style", type=StringType)
PNML_Line.attributes={PNML_Line_width, PNML_Line_style, PNML_Line_shape}

# PNML_Dimension class attributes and methods
PNML_Dimension_width: Property = Property(name="width", type=StringType)
PNML_Dimension_height: Property = Property(name="height", type=StringType)
PNML_Dimension.attributes={PNML_Dimension_height, PNML_Dimension_width}

# PNML_Fill class attributes and methods
PNML_Fill_gradientrotation: Property = Property(name="gradientrotation", type=StringType)
PNML_Fill.attributes={PNML_Fill_gradientrotation}

# Color class attributes and methods

# PNML_Font class attributes and methods
PNML_Font_family: Property = Property(name="family", type=StringType)
PNML_Font_style: Property = Property(name="style", type=StringType)
PNML_Font_weight: Property = Property(name="weight", type=StringType)
PNML_Font_size: Property = Property(name="size", type=StringType)
PNML_Font_decoration: Property = Property(name="decoration", type=StringType)
PNML_Font_align: Property = Property(name="align", type=StringType)
PNML_Font_rotation: Property = Property(name="rotation", type=StringType)
PNML_Font.attributes={PNML_Font_style, PNML_Font_weight, PNML_Font_align, PNML_Font_decoration, PNML_Font_rotation, PNML_Font_size, PNML_Font_family}

# Relationships
xmlns0: BinaryAssociation = BinaryAssociation(
    name="xmlns0",
    ends={
        Property(name="URI", type=PNML_PNMLDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_PNMLDocument", type=URI, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
interfaces4: BinaryAssociation = BinaryAssociation(
    name="interfaces4",
    ends={
        Property(name="Interface", type=PNML_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="module", type=Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
netcontents5: BinaryAssociation = BinaryAssociation(
    name="netcontents5",
    ends={
        Property(name="NetContent", type=PNML_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="module6", type=NetContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
document7: BinaryAssociation = BinaryAssociation(
    name="document7",
    ends={
        Property(name="PNMLDocument", type=PNML_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="modules", type=PNMLDocument, multiplicity=Multiplicity(1, 1))
    }
)
module8: BinaryAssociation = BinaryAssociation(
    name="module8",
    ends={
        Property(name="Module9", type=PNML_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interfaces", type=Module, multiplicity=Multiplicity(1, 1))
    }
)
importplace10: BinaryAssociation = BinaryAssociation(
    name="importplace10",
    ends={
        Property(name="Node", type=PNML_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Interface", type=Node, multiplicity=Multiplicity(0, 9999))
    }
)
exportplace11: BinaryAssociation = BinaryAssociation(
    name="exportplace11",
    ends={
        Property(name="Reference", type=PNML_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Interface12", type=Reference, multiplicity=Multiplicity(0, 9999))
    }
)
importtransition13: BinaryAssociation = BinaryAssociation(
    name="importtransition13",
    ends={
        Property(name="Node15", type=PNML_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Interface14", type=Node, multiplicity=Multiplicity(0, 9999))
    }
)
exporttransition16: BinaryAssociation = BinaryAssociation(
    name="exporttransition16",
    ends={
        Property(name="Reference18", type=PNML_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Interface17", type=Reference, multiplicity=Multiplicity(0, 9999))
    }
)
type19: BinaryAssociation = BinaryAssociation(
    name="type19",
    ends={
        Property(name="URI20", type=PNML_NetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_NetElement", type=URI, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
document21: BinaryAssociation = BinaryAssociation(
    name="document21",
    ends={
        Property(name="PNMLDocument22", type=PNML_NetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="nets", type=PNMLDocument, multiplicity=Multiplicity(1, 1))
    }
)
contents23: BinaryAssociation = BinaryAssociation(
    name="contents23",
    ends={
        Property(name="NetContent24", type=PNML_NetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=NetContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nets1: BinaryAssociation = BinaryAssociation(
    name="nets1",
    ends={
        Property(name="NetElement", type=PNML_PNMLDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="document", type=NetElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
modules2: BinaryAssociation = BinaryAssociation(
    name="modules2",
    ends={
        Property(name="Module", type=PNML_PNMLDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="document3", type=Module, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
net31: BinaryAssociation = BinaryAssociation(
    name="net31",
    ends={
        Property(name="NetElement32", type=PNML_NetContent, multiplicity=Multiplicity(1, 1)),
        Property(name="contents", type=NetElement, multiplicity=Multiplicity(1, 1))
    }
)
name33: BinaryAssociation = BinaryAssociation(
    name="name33",
    ends={
        Property(name="Name34", type=PNML_NetContent, multiplicity=Multiplicity(1, 1)),
        Property(name="netcontent", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
page35: BinaryAssociation = BinaryAssociation(
    name="page35",
    ends={
        Property(name="Page", type=PNML_NetContent, multiplicity=Multiplicity(1, 1)),
        Property(name="contents36", type=Page, multiplicity=Multiplicity(0, 1))
    }
)
module37: BinaryAssociation = BinaryAssociation(
    name="module37",
    ends={
        Property(name="Module38", type=PNML_NetContent, multiplicity=Multiplicity(1, 1)),
        Property(name="netcontents", type=Module, multiplicity=Multiplicity(0, 1))
    }
)
anyelement39: BinaryAssociation = BinaryAssociation(
    name="anyelement39",
    ends={
        Property(name="AnyElement", type=PNML_ToolSpecific, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_ToolSpecific", type=AnyElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net40: BinaryAssociation = BinaryAssociation(
    name="net40",
    ends={
        Property(name="NetElement41", type=PNML_ToolSpecific, multiplicity=Multiplicity(1, 1)),
        Property(name="tools", type=NetElement, multiplicity=Multiplicity(0, 1))
    }
)
arc42: BinaryAssociation = BinaryAssociation(
    name="arc42",
    ends={
        Property(name="Arc", type=PNML_ToolSpecific, multiplicity=Multiplicity(1, 1)),
        Property(name="tools43", type=Arc, multiplicity=Multiplicity(0, 1))
    }
)
node44: BinaryAssociation = BinaryAssociation(
    name="node44",
    ends={
        Property(name="Node46", type=PNML_ToolSpecific, multiplicity=Multiplicity(1, 1)),
        Property(name="tools45", type=Node, multiplicity=Multiplicity(0, 1))
    }
)
page47: BinaryAssociation = BinaryAssociation(
    name="page47",
    ends={
        Property(name="Page49", type=PNML_ToolSpecific, multiplicity=Multiplicity(1, 1)),
        Property(name="tools48", type=Page, multiplicity=Multiplicity(0, 1))
    }
)
labels50: BinaryAssociation = BinaryAssociation(
    name="labels50",
    ends={
        Property(name="Label", type=PNML_LabeledElement, multiplicity=Multiplicity(1, 1)),
        Property(name="namedelement", type=Label, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tools25: BinaryAssociation = BinaryAssociation(
    name="tools25",
    ends={
        Property(name="ToolSpecific", type=PNML_NetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="net26", type=ToolSpecific, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
netgraphics27: BinaryAssociation = BinaryAssociation(
    name="netgraphics27",
    ends={
        Property(name="NetGraphics", type=PNML_NetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="net28", type=NetGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name29: BinaryAssociation = BinaryAssociation(
    name="name29",
    ends={
        Property(name="Name", type=PNML_NetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="net30", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namedelement53: BinaryAssociation = BinaryAssociation(
    name="namedelement53",
    ends={
        Property(name="labels", type=LabeledElement, multiplicity=Multiplicity(1, 1)),
        Property(name="LabeledElement", type=PNML_Label, multiplicity=Multiplicity(1, 1))
    }
)
net54: BinaryAssociation = BinaryAssociation(
    name="net54",
    ends={
        Property(name="NetElement55", type=PNML_Name, multiplicity=Multiplicity(1, 1)),
        Property(name="name", type=NetElement, multiplicity=Multiplicity(0, 1))
    }
)
contents74: BinaryAssociation = BinaryAssociation(
    name="contents74",
    ends={
        Property(name="NetContent75", type=PNML_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="page", type=NetContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
netcontent56: BinaryAssociation = BinaryAssociation(
    name="netcontent56",
    ends={
        Property(name="NetContent58", type=PNML_Name, multiplicity=Multiplicity(1, 1)),
        Property(name="name57", type=NetContent, multiplicity=Multiplicity(0, 1))
    }
)
tools76: BinaryAssociation = BinaryAssociation(
    name="tools76",
    ends={
        Property(name="ToolSpecific78", type=PNML_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="page77", type=ToolSpecific, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pagegraphics79: BinaryAssociation = BinaryAssociation(
    name="pagegraphics79",
    ends={
        Property(name="PageGraphics", type=PNML_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="page80", type=PageGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arc59: BinaryAssociation = BinaryAssociation(
    name="arc59",
    ends={
        Property(name="Arc60", type=PNML_Inscription, multiplicity=Multiplicity(1, 1)),
        Property(name="inscription", type=Arc, multiplicity=Multiplicity(1, 1))
    }
)
place61: BinaryAssociation = BinaryAssociation(
    name="place61",
    ends={
        Property(name="Place", type=PNML_InitialMarking, multiplicity=Multiplicity(1, 1)),
        Property(name="initialmarking", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
node62: BinaryAssociation = BinaryAssociation(
    name="node62",
    ends={
        Property(name="Node63", type=PNML_NetContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="netcontentelement", type=Node, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source64: BinaryAssociation = BinaryAssociation(
    name="source64",
    ends={
        Property(name="NetContentElement", type=PNML_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Arc", type=NetContentElement, multiplicity=Multiplicity(1, 1))
    }
)
target65: BinaryAssociation = BinaryAssociation(
    name="target65",
    ends={
        Property(name="NetContentElement67", type=PNML_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Arc66", type=NetContentElement, multiplicity=Multiplicity(1, 1))
    }
)
annotationgraphics51: BinaryAssociation = BinaryAssociation(
    name="annotationgraphics51",
    ends={
        Property(name="AnnotationGraphics", type=PNML_LabeledElement, multiplicity=Multiplicity(1, 1)),
        Property(name="namedelement52", type=AnnotationGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tools68: BinaryAssociation = BinaryAssociation(
    name="tools68",
    ends={
        Property(name="ToolSpecific69", type=PNML_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arc", type=ToolSpecific, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgegraphics70: BinaryAssociation = BinaryAssociation(
    name="edgegraphics70",
    ends={
        Property(name="EdgeGraphics", type=PNML_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arc71", type=EdgeGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inscription72: BinaryAssociation = BinaryAssociation(
    name="inscription72",
    ends={
        Property(name="Inscription", type=PNML_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arc73", type=Inscription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter92: BinaryAssociation = BinaryAssociation(
    name="parameter92",
    ends={
        Property(name="NCName93", type=PNML_ImportNode, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_ImportNode", type=NCName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ref94: BinaryAssociation = BinaryAssociation(
    name="ref94",
    ends={
        Property(name="Reference95", type=PNML_ImportNode, multiplicity=Multiplicity(1, 1)),
        Property(name="importnode", type=Reference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instanceplace96: BinaryAssociation = BinaryAssociation(
    name="instanceplace96",
    ends={
        Property(name="Instance", type=PNML_ImportNode, multiplicity=Multiplicity(1, 1)),
        Property(name="importplace", type=Instance, multiplicity=Multiplicity(0, 1))
    }
)
instancetransition97: BinaryAssociation = BinaryAssociation(
    name="instancetransition97",
    ends={
        Property(name="Instance98", type=PNML_ImportNode, multiplicity=Multiplicity(1, 1)),
        Property(name="importtransition", type=Instance, multiplicity=Multiplicity(0, 1))
    }
)
netcontentelement99: BinaryAssociation = BinaryAssociation(
    name="netcontentelement99",
    ends={
        Property(name="NetContentElement100", type=PNML_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=NetContentElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instance81: BinaryAssociation = BinaryAssociation(
    name="instance81",
    ends={
        Property(name="Node82", type=PNML_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Reference", type=Node, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref83: BinaryAssociation = BinaryAssociation(
    name="ref83",
    ends={
        Property(name="NCName", type=PNML_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Reference84", type=NCName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
importnode85: BinaryAssociation = BinaryAssociation(
    name="importnode85",
    ends={
        Property(name="ImportNode", type=PNML_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="ref", type=ImportNode, multiplicity=Multiplicity(0, 1))
    }
)
ref86: BinaryAssociation = BinaryAssociation(
    name="ref86",
    ends={
        Property(name="URI87", type=PNML_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Instance", type=URI, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
importplace88: BinaryAssociation = BinaryAssociation(
    name="importplace88",
    ends={
        Property(name="ImportNode89", type=PNML_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="instanceplace", type=ImportNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importtransition90: BinaryAssociation = BinaryAssociation(
    name="importtransition90",
    ends={
        Property(name="ImportNode91", type=PNML_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="instancetransition", type=ImportNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
position111: BinaryAssociation = BinaryAssociation(
    name="position111",
    ends={
        Property(name="Position", type=PNML_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="nodegraphics112", type=Position, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dimension113: BinaryAssociation = BinaryAssociation(
    name="dimension113",
    ends={
        Property(name="Dimension", type=PNML_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="nodegraphics114", type=Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fill115: BinaryAssociation = BinaryAssociation(
    name="fill115",
    ends={
        Property(name="Fill", type=PNML_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="nodegraphics116", type=Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
line117: BinaryAssociation = BinaryAssociation(
    name="line117",
    ends={
        Property(name="Line", type=PNML_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="nodegraphics118", type=Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arc119: BinaryAssociation = BinaryAssociation(
    name="arc119",
    ends={
        Property(name="Arc120", type=PNML_EdgeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="edgegraphics", type=Arc, multiplicity=Multiplicity(1, 1))
    }
)
tools101: BinaryAssociation = BinaryAssociation(
    name="tools101",
    ends={
        Property(name="ToolSpecific103", type=PNML_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node102", type=ToolSpecific, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodegraphics104: BinaryAssociation = BinaryAssociation(
    name="nodegraphics104",
    ends={
        Property(name="NodeGraphics", type=PNML_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node105", type=NodeGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialmarking106: BinaryAssociation = BinaryAssociation(
    name="initialmarking106",
    ends={
        Property(name="InitialMarking", type=PNML_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="place", type=InitialMarking, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
net107: BinaryAssociation = BinaryAssociation(
    name="net107",
    ends={
        Property(name="NetElement108", type=PNML_NetGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="netgraphics", type=NetElement, multiplicity=Multiplicity(1, 1))
    }
)
node109: BinaryAssociation = BinaryAssociation(
    name="node109",
    ends={
        Property(name="Node110", type=PNML_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="nodegraphics", type=Node, multiplicity=Multiplicity(1, 1))
    }
)
page142: BinaryAssociation = BinaryAssociation(
    name="page142",
    ends={
        Property(name="Page143", type=PNML_PageGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="pagegraphics", type=Page, multiplicity=Multiplicity(1, 1))
    }
)
nodegraphics144: BinaryAssociation = BinaryAssociation(
    name="nodegraphics144",
    ends={
        Property(name="NodeGraphics145", type=PNML_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="position", type=NodeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
edgegraphics146: BinaryAssociation = BinaryAssociation(
    name="edgegraphics146",
    ends={
        Property(name="EdgeGraphics148", type=PNML_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="position147", type=EdgeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
position121: BinaryAssociation = BinaryAssociation(
    name="position121",
    ends={
        Property(name="Position123", type=PNML_EdgeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="edgegraphics122", type=Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fill124: BinaryAssociation = BinaryAssociation(
    name="fill124",
    ends={
        Property(name="Fill126", type=PNML_EdgeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="edgegraphics125", type=Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
line127: BinaryAssociation = BinaryAssociation(
    name="line127",
    ends={
        Property(name="Line129", type=PNML_EdgeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="edgegraphics128", type=Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namedelement130: BinaryAssociation = BinaryAssociation(
    name="namedelement130",
    ends={
        Property(name="LabeledElement131", type=PNML_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="annotationgraphics", type=LabeledElement, multiplicity=Multiplicity(1, 1))
    }
)
offset132: BinaryAssociation = BinaryAssociation(
    name="offset132",
    ends={
        Property(name="Offset", type=PNML_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="annotationgraphics133", type=Offset, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
font134: BinaryAssociation = BinaryAssociation(
    name="font134",
    ends={
        Property(name="Font", type=PNML_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="annotationgraphics135", type=Font, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fill136: BinaryAssociation = BinaryAssociation(
    name="fill136",
    ends={
        Property(name="Fill138", type=PNML_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="annotationgraphics137", type=Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
line139: BinaryAssociation = BinaryAssociation(
    name="line139",
    ends={
        Property(name="Line141", type=PNML_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="annotationgraphics140", type=Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotationgraphics165: BinaryAssociation = BinaryAssociation(
    name="annotationgraphics165",
    ends={
        Property(name="AnnotationGraphics167", type=PNML_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="fill166", type=AnnotationGraphics, multiplicity=Multiplicity(0, 1))
    }
)
color168: BinaryAssociation = BinaryAssociation(
    name="color168",
    ends={
        Property(name="Color169", type=PNML_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Line", type=Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nodegraphics170: BinaryAssociation = BinaryAssociation(
    name="nodegraphics170",
    ends={
        Property(name="NodeGraphics171", type=PNML_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="line", type=NodeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
edgegraphics172: BinaryAssociation = BinaryAssociation(
    name="edgegraphics172",
    ends={
        Property(name="EdgeGraphics174", type=PNML_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="line173", type=EdgeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
annotationgraphics149: BinaryAssociation = BinaryAssociation(
    name="annotationgraphics149",
    ends={
        Property(name="AnnotationGraphics150", type=PNML_Offset, multiplicity=Multiplicity(1, 1)),
        Property(name="offset", type=AnnotationGraphics, multiplicity=Multiplicity(1, 1))
    }
)
nodegraphics151: BinaryAssociation = BinaryAssociation(
    name="nodegraphics151",
    ends={
        Property(name="NodeGraphics152", type=PNML_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="dimension", type=NodeGraphics, multiplicity=Multiplicity(1, 1))
    }
)
interiorcolor153: BinaryAssociation = BinaryAssociation(
    name="interiorcolor153",
    ends={
        Property(name="Color", type=PNML_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Fill", type=Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
gradientcolor154: BinaryAssociation = BinaryAssociation(
    name="gradientcolor154",
    ends={
        Property(name="Color156", type=PNML_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Fill155", type=Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
image157: BinaryAssociation = BinaryAssociation(
    name="image157",
    ends={
        Property(name="URI159", type=PNML_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Fill158", type=URI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nodegraphics160: BinaryAssociation = BinaryAssociation(
    name="nodegraphics160",
    ends={
        Property(name="NodeGraphics161", type=PNML_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="fill", type=NodeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
edgegraphics162: BinaryAssociation = BinaryAssociation(
    name="edgegraphics162",
    ends={
        Property(name="EdgeGraphics164", type=PNML_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="fill163", type=EdgeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
annotationgraphics175: BinaryAssociation = BinaryAssociation(
    name="annotationgraphics175",
    ends={
        Property(name="AnnotationGraphics177", type=PNML_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="line176", type=AnnotationGraphics, multiplicity=Multiplicity(0, 1))
    }
)
annotationgraphics178: BinaryAssociation = BinaryAssociation(
    name="annotationgraphics178",
    ends={
        Property(name="AnnotationGraphics179", type=PNML_Font, multiplicity=Multiplicity(1, 1)),
        Property(name="font", type=AnnotationGraphics, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_PNML_Module_IdedElement = Generalization(general=IdedElement, specific=PNML_Module)
gen_PNML_NetElement_IdedElement = Generalization(general=IdedElement, specific=PNML_NetElement)
gen_PNML_Page_NetContent = Generalization(general=NetContent, specific=PNML_Page)
gen_PNML_Name_LabeledElement = Generalization(general=LabeledElement, specific=PNML_Name)
gen_PNML_Page_IdedElement = Generalization(general=IdedElement, specific=PNML_Page)
gen_PNML_Inscription_LabeledElement = Generalization(general=LabeledElement, specific=PNML_Inscription)
gen_PNML_InitialMarking_LabeledElement = Generalization(general=LabeledElement, specific=PNML_InitialMarking)
gen_PNML_NetContentElement_NetContent = Generalization(general=NetContent, specific=PNML_NetContentElement)
gen_PNML_Arc_NetContent = Generalization(general=NetContent, specific=PNML_Arc)
gen_PNML_Arc_IdedElement = Generalization(general=IdedElement, specific=PNML_Arc)
gen_PNML_Node_IdedElement = Generalization(general=IdedElement, specific=PNML_Node)
gen_PNML_Reference_Node = Generalization(general=Node, specific=PNML_Reference)
gen_PNML_ReferencePlace_NetContent = Generalization(general=NetContent, specific=PNML_ReferencePlace)
gen_PNML_ReferencePlace_Reference = Generalization(general=Reference, specific=PNML_ReferencePlace)
gen_PNML_ReferenceTransition_NetContent = Generalization(general=NetContent, specific=PNML_ReferenceTransition)
gen_PNML_ReferenceTransition_Reference = Generalization(general=Reference, specific=PNML_ReferenceTransition)
gen_PNML_Instance_NetContent = Generalization(general=NetContent, specific=PNML_Instance)
gen_PNML_Instance_IdedElement = Generalization(general=IdedElement, specific=PNML_Instance)
gen_PNML_EdgeGraphics_Graphics = Generalization(general=Graphics, specific=PNML_EdgeGraphics)
gen_PNML_Place_NetContentElement = Generalization(general=NetContentElement, specific=PNML_Place)
gen_PNML_Transition_NetContentElement = Generalization(general=NetContentElement, specific=PNML_Transition)
gen_PNML_NetGraphics_Graphics = Generalization(general=Graphics, specific=PNML_NetGraphics)
gen_PNML_NodeGraphics_Graphics = Generalization(general=Graphics, specific=PNML_NodeGraphics)
gen_PNML_Position_Coordinate = Generalization(general=Coordinate, specific=PNML_Position)
gen_PNML_AnnotationGraphics_Graphics = Generalization(general=Graphics, specific=PNML_AnnotationGraphics)
gen_PNML_PageGraphics_Graphics = Generalization(general=Graphics, specific=PNML_PageGraphics)
gen_PNML_Offset_Coordinate = Generalization(general=Coordinate, specific=PNML_Offset)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={PNML_URI, PNML_Color, PNML_AnyElement, PNML_NCName, PNML_PNMLDocument, URI, PNML_IdedElement, PNML_Module, IdedElement, Interface, NetContent, PNMLDocument, PNML_Interface, Node, Reference, PNML_NetElement, NetElement, Module, PNML_NetContent, Page, PNML_ToolSpecific, AnyElement, Arc, PNML_LabeledElement, Label, AnnotationGraphics, ToolSpecific, NetGraphics, Name, PNML_Page, PNML_Name, PNML_Inscription, PageGraphics, PNML_InitialMarking, Place, PNML_NetContentElement, PNML_Arc, NetContentElement, PNML_Label, EdgeGraphics, Inscription, LabeledElement, Instance, PNML_Node, PNML_Reference, NCName, ImportNode, PNML_ReferencePlace, PNML_ReferenceTransition, PNML_Instance, PNML_ImportNode, Position, Dimension, Fill, Line, PNML_EdgeGraphics, NodeGraphics, PNML_Place, InitialMarking, PNML_Transition, PNML_Graphics, PNML_NetGraphics, Graphics, PNML_NodeGraphics, PNML_Coordinate, PNML_Position, Coordinate, PNML_Offset, PNML_AnnotationGraphics, Offset, Font, PNML_PageGraphics, PNML_Line, PNML_Dimension, PNML_Fill, Color, PNML_Font, RotationType, ShapeType, StyleType, DecorationType, AlignType},
    associations={xmlns0, interfaces4, netcontents5, document7, module8, importplace10, exportplace11, importtransition13, exporttransition16, type19, document21, contents23, nets1, modules2, net31, name33, page35, module37, anyelement39, net40, arc42, node44, page47, labels50, tools25, netgraphics27, name29, namedelement53, net54, contents74, netcontent56, tools76, pagegraphics79, arc59, place61, node62, source64, target65, annotationgraphics51, tools68, edgegraphics70, inscription72, parameter92, ref94, instanceplace96, instancetransition97, netcontentelement99, instance81, ref83, importnode85, ref86, importplace88, importtransition90, position111, dimension113, fill115, line117, arc119, tools101, nodegraphics104, initialmarking106, net107, node109, page142, nodegraphics144, edgegraphics146, position121, fill124, line127, namedelement130, offset132, font134, fill136, line139, annotationgraphics165, color168, nodegraphics170, edgegraphics172, annotationgraphics149, nodegraphics151, interiorcolor153, gradientcolor154, image157, nodegraphics160, edgegraphics162, annotationgraphics175, annotationgraphics178},
    generalizations={gen_PNML_Module_IdedElement, gen_PNML_NetElement_IdedElement, gen_PNML_Page_NetContent, gen_PNML_Name_LabeledElement, gen_PNML_Page_IdedElement, gen_PNML_Inscription_LabeledElement, gen_PNML_InitialMarking_LabeledElement, gen_PNML_NetContentElement_NetContent, gen_PNML_Arc_NetContent, gen_PNML_Arc_IdedElement, gen_PNML_Node_IdedElement, gen_PNML_Reference_Node, gen_PNML_ReferencePlace_NetContent, gen_PNML_ReferencePlace_Reference, gen_PNML_ReferenceTransition_NetContent, gen_PNML_ReferenceTransition_Reference, gen_PNML_Instance_NetContent, gen_PNML_Instance_IdedElement, gen_PNML_EdgeGraphics_Graphics, gen_PNML_Place_NetContentElement, gen_PNML_Transition_NetContentElement, gen_PNML_NetGraphics_Graphics, gen_PNML_NodeGraphics_Graphics, gen_PNML_Position_Coordinate, gen_PNML_AnnotationGraphics_Graphics, gen_PNML_PageGraphics_Graphics, gen_PNML_Offset_Coordinate},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)