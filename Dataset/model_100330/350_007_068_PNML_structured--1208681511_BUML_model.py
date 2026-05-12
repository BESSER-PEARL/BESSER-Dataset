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
PNML_Color = Class(name="PNML_Color")
PNML_AnyElement = Class(name="PNML_AnyElement")
PNML_IdedElement = Class(name="PNML_IdedElement", is_abstract=True)
PNML_URI = Class(name="PNML_URI")
PNMLDocument = Class(name="PNMLDocument")
NetContent = Class(name="NetContent")
PNML_PNMLDocument = Class(name="PNML_PNMLDocument")
URI = Class(name="URI")
NetElement = Class(name="NetElement")
PNML_NetElement = Class(name="PNML_NetElement")
IdedElement = Class(name="IdedElement")
PNML_LabeledElement = Class(name="PNML_LabeledElement", is_abstract=True)
Label = Class(name="Label")
ToolSpecific = Class(name="ToolSpecific")
NetGraphics = Class(name="NetGraphics")
Name = Class(name="Name")
PNML_NetContent = Class(name="PNML_NetContent", is_abstract=True)
Page = Class(name="Page")
PNML_ToolSpecific = Class(name="PNML_ToolSpecific")
AnyElement = Class(name="AnyElement")
Arc = Class(name="Arc")
Node = Class(name="Node")
PNML_Arc = Class(name="PNML_Arc")
NetContentElement = Class(name="NetContentElement")
AnnotationGraphics = Class(name="AnnotationGraphics")
PNML_Label = Class(name="PNML_Label")
LabeledElement = Class(name="LabeledElement")
PNML_Name = Class(name="PNML_Name")
PNML_Inscription = Class(name="PNML_Inscription")
PNML_InitialMarking = Class(name="PNML_InitialMarking")
Place = Class(name="Place")
PNML_NetContentElement = Class(name="PNML_NetContentElement", is_abstract=True)
NodeGraphics = Class(name="NodeGraphics")
EdgeGraphics = Class(name="EdgeGraphics")
Inscription = Class(name="Inscription")
PNML_Page = Class(name="PNML_Page")
PageGraphics = Class(name="PageGraphics")
PNML_Reference = Class(name="PNML_Reference", is_abstract=True)
PNML_ReferencePlace = Class(name="PNML_ReferencePlace")
Reference = Class(name="Reference")
PNML_ReferenceTransition = Class(name="PNML_ReferenceTransition")
PNML_Node = Class(name="PNML_Node")
PNML_Place = Class(name="PNML_Place")
InitialMarking = Class(name="InitialMarking")
PNML_Transition = Class(name="PNML_Transition")
PNML_Graphics = Class(name="PNML_Graphics", is_abstract=True)
PNML_NetGraphics = Class(name="PNML_NetGraphics")
Graphics = Class(name="Graphics")
PNML_NodeGraphics = Class(name="PNML_NodeGraphics")
Position = Class(name="Position")
Dimension = Class(name="Dimension")
Fill = Class(name="Fill")
Line = Class(name="Line")
PNML_EdgeGraphics = Class(name="PNML_EdgeGraphics")
PNML_Offset = Class(name="PNML_Offset")
PNML_AnnotationGraphics = Class(name="PNML_AnnotationGraphics")
Offset = Class(name="Offset")
Font = Class(name="Font")
PNML_PageGraphics = Class(name="PNML_PageGraphics")
PNML_Coordinate = Class(name="PNML_Coordinate", is_abstract=True)
PNML_Position = Class(name="PNML_Position")
Coordinate = Class(name="Coordinate")
PNML_Dimension = Class(name="PNML_Dimension")
PNML_Fill = Class(name="PNML_Fill")
Color = Class(name="Color")
PNML_Line = Class(name="PNML_Line")
PNML_Font = Class(name="PNML_Font")

# PNML_Color class attributes and methods

# PNML_AnyElement class attributes and methods
PNML_AnyElement_name: Property = Property(name="name", type=StringType)
PNML_AnyElement_text: Property = Property(name="text", type=StringType)
PNML_AnyElement.attributes={PNML_AnyElement_name, PNML_AnyElement_text}

# PNML_IdedElement class attributes and methods
PNML_IdedElement_id: Property = Property(name="id", type=StringType)
PNML_IdedElement.attributes={PNML_IdedElement_id}

# PNML_URI class attributes and methods
PNML_URI_value: Property = Property(name="value", type=StringType)
PNML_URI.attributes={PNML_URI_value}

# PNMLDocument class attributes and methods

# NetContent class attributes and methods

# PNML_PNMLDocument class attributes and methods

# URI class attributes and methods

# NetElement class attributes and methods

# PNML_NetElement class attributes and methods

# IdedElement class attributes and methods

# PNML_LabeledElement class attributes and methods

# Label class attributes and methods

# ToolSpecific class attributes and methods

# NetGraphics class attributes and methods

# Name class attributes and methods

# PNML_NetContent class attributes and methods

# Page class attributes and methods

# PNML_ToolSpecific class attributes and methods
PNML_ToolSpecific_tool: Property = Property(name="tool", type=StringType)
PNML_ToolSpecific_version: Property = Property(name="version", type=StringType)
PNML_ToolSpecific.attributes={PNML_ToolSpecific_tool, PNML_ToolSpecific_version}

# AnyElement class attributes and methods

# Arc class attributes and methods

# Node class attributes and methods

# PNML_Arc class attributes and methods

# NetContentElement class attributes and methods

# AnnotationGraphics class attributes and methods

# PNML_Label class attributes and methods
PNML_Label_text: Property = Property(name="text", type=StringType)
PNML_Label.attributes={PNML_Label_text}

# LabeledElement class attributes and methods

# PNML_Name class attributes and methods

# PNML_Inscription class attributes and methods

# PNML_InitialMarking class attributes and methods

# Place class attributes and methods

# PNML_NetContentElement class attributes and methods

# NodeGraphics class attributes and methods

# EdgeGraphics class attributes and methods

# Inscription class attributes and methods

# PNML_Page class attributes and methods

# PageGraphics class attributes and methods

# PNML_Reference class attributes and methods

# PNML_ReferencePlace class attributes and methods

# Reference class attributes and methods

# PNML_ReferenceTransition class attributes and methods

# PNML_Node class attributes and methods

# PNML_Place class attributes and methods

# InitialMarking class attributes and methods

# PNML_Transition class attributes and methods

# PNML_Graphics class attributes and methods

# PNML_NetGraphics class attributes and methods

# Graphics class attributes and methods

# PNML_NodeGraphics class attributes and methods

# Position class attributes and methods

# Dimension class attributes and methods

# Fill class attributes and methods

# Line class attributes and methods

# PNML_EdgeGraphics class attributes and methods

# PNML_Offset class attributes and methods

# PNML_AnnotationGraphics class attributes and methods

# Offset class attributes and methods

# Font class attributes and methods

# PNML_PageGraphics class attributes and methods

# PNML_Coordinate class attributes and methods
PNML_Coordinate_x: Property = Property(name="x", type=StringType)
PNML_Coordinate_y: Property = Property(name="y", type=StringType)
PNML_Coordinate.attributes={PNML_Coordinate_x, PNML_Coordinate_y}

# PNML_Position class attributes and methods

# Coordinate class attributes and methods

# PNML_Dimension class attributes and methods
PNML_Dimension_width: Property = Property(name="width", type=StringType)
PNML_Dimension_height: Property = Property(name="height", type=StringType)
PNML_Dimension.attributes={PNML_Dimension_width, PNML_Dimension_height}

# PNML_Fill class attributes and methods
PNML_Fill_gradientrotation: Property = Property(name="gradientrotation", type=StringType)
PNML_Fill.attributes={PNML_Fill_gradientrotation}

# Color class attributes and methods

# PNML_Line class attributes and methods
PNML_Line_width: Property = Property(name="width", type=StringType)
PNML_Line_shape: Property = Property(name="shape", type=StringType)
PNML_Line_style: Property = Property(name="style", type=StringType)
PNML_Line.attributes={PNML_Line_style, PNML_Line_width, PNML_Line_shape}

# PNML_Font class attributes and methods
PNML_Font_rotation: Property = Property(name="rotation", type=StringType)
PNML_Font_family: Property = Property(name="family", type=StringType)
PNML_Font_style: Property = Property(name="style", type=StringType)
PNML_Font_weight: Property = Property(name="weight", type=StringType)
PNML_Font_size: Property = Property(name="size", type=StringType)
PNML_Font_decoration: Property = Property(name="decoration", type=StringType)
PNML_Font_align: Property = Property(name="align", type=StringType)
PNML_Font.attributes={PNML_Font_style, PNML_Font_size, PNML_Font_weight, PNML_Font_rotation, PNML_Font_decoration, PNML_Font_align, PNML_Font_family}

# Relationships
document4: BinaryAssociation = BinaryAssociation(
    name="document4",
    ends={
        Property(name="PNMLDocument", type=PNML_NetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="nets", type=PNMLDocument, multiplicity=Multiplicity(1, 1))
    }
)
contents5: BinaryAssociation = BinaryAssociation(
    name="contents5",
    ends={
        Property(name="NetContent", type=PNML_NetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=NetContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xmlns0: BinaryAssociation = BinaryAssociation(
    name="xmlns0",
    ends={
        Property(name="URI", type=PNML_PNMLDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_PNMLDocument", type=URI, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
nets1: BinaryAssociation = BinaryAssociation(
    name="nets1",
    ends={
        Property(name="NetElement", type=PNML_PNMLDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="document", type=NetElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="URI3", type=PNML_NetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_NetElement", type=URI, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
node23: BinaryAssociation = BinaryAssociation(
    name="node23",
    ends={
        Property(name="Node", type=PNML_ToolSpecific, multiplicity=Multiplicity(1, 1)),
        Property(name="tools24", type=Node, multiplicity=Multiplicity(0, 1))
    }
)
page25: BinaryAssociation = BinaryAssociation(
    name="page25",
    ends={
        Property(name="Page27", type=PNML_ToolSpecific, multiplicity=Multiplicity(1, 1)),
        Property(name="tools26", type=Page, multiplicity=Multiplicity(0, 1))
    }
)
labels28: BinaryAssociation = BinaryAssociation(
    name="labels28",
    ends={
        Property(name="Label", type=PNML_LabeledElement, multiplicity=Multiplicity(1, 1)),
        Property(name="namedelement", type=Label, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tools6: BinaryAssociation = BinaryAssociation(
    name="tools6",
    ends={
        Property(name="ToolSpecific", type=PNML_NetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="net7", type=ToolSpecific, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
netgraphics8: BinaryAssociation = BinaryAssociation(
    name="netgraphics8",
    ends={
        Property(name="NetGraphics", type=PNML_NetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="net9", type=NetGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name10: BinaryAssociation = BinaryAssociation(
    name="name10",
    ends={
        Property(name="Name", type=PNML_NetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="net11", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
net12: BinaryAssociation = BinaryAssociation(
    name="net12",
    ends={
        Property(name="NetElement13", type=PNML_NetContent, multiplicity=Multiplicity(1, 1)),
        Property(name="contents", type=NetElement, multiplicity=Multiplicity(1, 1))
    }
)
name14: BinaryAssociation = BinaryAssociation(
    name="name14",
    ends={
        Property(name="Name15", type=PNML_NetContent, multiplicity=Multiplicity(1, 1)),
        Property(name="netcontent", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
page16: BinaryAssociation = BinaryAssociation(
    name="page16",
    ends={
        Property(name="Page", type=PNML_NetContent, multiplicity=Multiplicity(1, 1)),
        Property(name="contents17", type=Page, multiplicity=Multiplicity(0, 1))
    }
)
anyelement18: BinaryAssociation = BinaryAssociation(
    name="anyelement18",
    ends={
        Property(name="AnyElement", type=PNML_ToolSpecific, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_ToolSpecific", type=AnyElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net19: BinaryAssociation = BinaryAssociation(
    name="net19",
    ends={
        Property(name="NetElement20", type=PNML_ToolSpecific, multiplicity=Multiplicity(1, 1)),
        Property(name="tools", type=NetElement, multiplicity=Multiplicity(0, 1))
    }
)
arc21: BinaryAssociation = BinaryAssociation(
    name="arc21",
    ends={
        Property(name="Arc", type=PNML_ToolSpecific, multiplicity=Multiplicity(1, 1)),
        Property(name="tools22", type=Arc, multiplicity=Multiplicity(0, 1))
    }
)
source42: BinaryAssociation = BinaryAssociation(
    name="source42",
    ends={
        Property(name="NetContentElement", type=PNML_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Arc", type=NetContentElement, multiplicity=Multiplicity(1, 1))
    }
)
target43: BinaryAssociation = BinaryAssociation(
    name="target43",
    ends={
        Property(name="NetContentElement45", type=PNML_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Arc44", type=NetContentElement, multiplicity=Multiplicity(1, 1))
    }
)
annotationgraphics29: BinaryAssociation = BinaryAssociation(
    name="annotationgraphics29",
    ends={
        Property(name="AnnotationGraphics", type=PNML_LabeledElement, multiplicity=Multiplicity(1, 1)),
        Property(name="namedelement30", type=AnnotationGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namedelement31: BinaryAssociation = BinaryAssociation(
    name="namedelement31",
    ends={
        Property(name="LabeledElement", type=PNML_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="labels", type=LabeledElement, multiplicity=Multiplicity(1, 1))
    }
)
net32: BinaryAssociation = BinaryAssociation(
    name="net32",
    ends={
        Property(name="NetElement33", type=PNML_Name, multiplicity=Multiplicity(1, 1)),
        Property(name="name", type=NetElement, multiplicity=Multiplicity(0, 1))
    }
)
netcontent34: BinaryAssociation = BinaryAssociation(
    name="netcontent34",
    ends={
        Property(name="NetContent36", type=PNML_Name, multiplicity=Multiplicity(1, 1)),
        Property(name="name35", type=NetContent, multiplicity=Multiplicity(0, 1))
    }
)
arc37: BinaryAssociation = BinaryAssociation(
    name="arc37",
    ends={
        Property(name="Arc38", type=PNML_Inscription, multiplicity=Multiplicity(1, 1)),
        Property(name="inscription", type=Arc, multiplicity=Multiplicity(1, 1))
    }
)
place39: BinaryAssociation = BinaryAssociation(
    name="place39",
    ends={
        Property(name="Place", type=PNML_InitialMarking, multiplicity=Multiplicity(1, 1)),
        Property(name="initialmarking", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
node40: BinaryAssociation = BinaryAssociation(
    name="node40",
    ends={
        Property(name="Node41", type=PNML_NetContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="netcontentelement", type=Node, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
netcontentelement61: BinaryAssociation = BinaryAssociation(
    name="netcontentelement61",
    ends={
        Property(name="NetContentElement62", type=PNML_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=NetContentElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tools63: BinaryAssociation = BinaryAssociation(
    name="tools63",
    ends={
        Property(name="ToolSpecific65", type=PNML_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node64", type=ToolSpecific, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tools46: BinaryAssociation = BinaryAssociation(
    name="tools46",
    ends={
        Property(name="ToolSpecific47", type=PNML_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arc", type=ToolSpecific, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgegraphics48: BinaryAssociation = BinaryAssociation(
    name="edgegraphics48",
    ends={
        Property(name="EdgeGraphics", type=PNML_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arc49", type=EdgeGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inscription50: BinaryAssociation = BinaryAssociation(
    name="inscription50",
    ends={
        Property(name="Inscription", type=PNML_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arc51", type=Inscription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contents52: BinaryAssociation = BinaryAssociation(
    name="contents52",
    ends={
        Property(name="NetContent53", type=PNML_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="page", type=NetContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tools54: BinaryAssociation = BinaryAssociation(
    name="tools54",
    ends={
        Property(name="ToolSpecific56", type=PNML_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="page55", type=ToolSpecific, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pagegraphics57: BinaryAssociation = BinaryAssociation(
    name="pagegraphics57",
    ends={
        Property(name="PageGraphics", type=PNML_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="page58", type=PageGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref59: BinaryAssociation = BinaryAssociation(
    name="ref59",
    ends={
        Property(name="Node60", type=PNML_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Reference", type=Node, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arc81: BinaryAssociation = BinaryAssociation(
    name="arc81",
    ends={
        Property(name="Arc82", type=PNML_EdgeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="edgegraphics", type=Arc, multiplicity=Multiplicity(1, 1))
    }
)
position83: BinaryAssociation = BinaryAssociation(
    name="position83",
    ends={
        Property(name="Position85", type=PNML_EdgeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="edgegraphics84", type=Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fill86: BinaryAssociation = BinaryAssociation(
    name="fill86",
    ends={
        Property(name="Fill88", type=PNML_EdgeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="edgegraphics87", type=Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nodegraphics66: BinaryAssociation = BinaryAssociation(
    name="nodegraphics66",
    ends={
        Property(name="NodeGraphics", type=PNML_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node67", type=NodeGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialmarking68: BinaryAssociation = BinaryAssociation(
    name="initialmarking68",
    ends={
        Property(name="InitialMarking", type=PNML_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="place", type=InitialMarking, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
net69: BinaryAssociation = BinaryAssociation(
    name="net69",
    ends={
        Property(name="NetElement70", type=PNML_NetGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="netgraphics", type=NetElement, multiplicity=Multiplicity(1, 1))
    }
)
node71: BinaryAssociation = BinaryAssociation(
    name="node71",
    ends={
        Property(name="Node72", type=PNML_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="nodegraphics", type=Node, multiplicity=Multiplicity(1, 1))
    }
)
position73: BinaryAssociation = BinaryAssociation(
    name="position73",
    ends={
        Property(name="Position", type=PNML_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="nodegraphics74", type=Position, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dimension75: BinaryAssociation = BinaryAssociation(
    name="dimension75",
    ends={
        Property(name="Dimension", type=PNML_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="nodegraphics76", type=Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fill77: BinaryAssociation = BinaryAssociation(
    name="fill77",
    ends={
        Property(name="Fill", type=PNML_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="nodegraphics78", type=Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
line79: BinaryAssociation = BinaryAssociation(
    name="line79",
    ends={
        Property(name="Line", type=PNML_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="nodegraphics80", type=Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nodegraphics106: BinaryAssociation = BinaryAssociation(
    name="nodegraphics106",
    ends={
        Property(name="NodeGraphics107", type=PNML_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="position", type=NodeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
edgegraphics108: BinaryAssociation = BinaryAssociation(
    name="edgegraphics108",
    ends={
        Property(name="EdgeGraphics110", type=PNML_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="position109", type=EdgeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
line89: BinaryAssociation = BinaryAssociation(
    name="line89",
    ends={
        Property(name="Line91", type=PNML_EdgeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="edgegraphics90", type=Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namedelement92: BinaryAssociation = BinaryAssociation(
    name="namedelement92",
    ends={
        Property(name="LabeledElement93", type=PNML_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="annotationgraphics", type=LabeledElement, multiplicity=Multiplicity(1, 1))
    }
)
offset94: BinaryAssociation = BinaryAssociation(
    name="offset94",
    ends={
        Property(name="Offset", type=PNML_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="annotationgraphics95", type=Offset, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
font96: BinaryAssociation = BinaryAssociation(
    name="font96",
    ends={
        Property(name="Font", type=PNML_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="annotationgraphics97", type=Font, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fill98: BinaryAssociation = BinaryAssociation(
    name="fill98",
    ends={
        Property(name="Fill100", type=PNML_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="annotationgraphics99", type=Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
line101: BinaryAssociation = BinaryAssociation(
    name="line101",
    ends={
        Property(name="Line103", type=PNML_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="annotationgraphics102", type=Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
page104: BinaryAssociation = BinaryAssociation(
    name="page104",
    ends={
        Property(name="Page105", type=PNML_PageGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="pagegraphics", type=Page, multiplicity=Multiplicity(1, 1))
    }
)
color130: BinaryAssociation = BinaryAssociation(
    name="color130",
    ends={
        Property(name="Color131", type=PNML_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Line", type=Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nodegraphics132: BinaryAssociation = BinaryAssociation(
    name="nodegraphics132",
    ends={
        Property(name="NodeGraphics133", type=PNML_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="line", type=NodeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
annotationgraphics111: BinaryAssociation = BinaryAssociation(
    name="annotationgraphics111",
    ends={
        Property(name="AnnotationGraphics112", type=PNML_Offset, multiplicity=Multiplicity(1, 1)),
        Property(name="offset", type=AnnotationGraphics, multiplicity=Multiplicity(1, 1))
    }
)
nodegraphics113: BinaryAssociation = BinaryAssociation(
    name="nodegraphics113",
    ends={
        Property(name="NodeGraphics114", type=PNML_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="dimension", type=NodeGraphics, multiplicity=Multiplicity(1, 1))
    }
)
interiorcolor115: BinaryAssociation = BinaryAssociation(
    name="interiorcolor115",
    ends={
        Property(name="Color", type=PNML_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Fill", type=Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
gradientcolor116: BinaryAssociation = BinaryAssociation(
    name="gradientcolor116",
    ends={
        Property(name="Color118", type=PNML_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Fill117", type=Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
image119: BinaryAssociation = BinaryAssociation(
    name="image119",
    ends={
        Property(name="URI121", type=PNML_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Fill120", type=URI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nodegraphics122: BinaryAssociation = BinaryAssociation(
    name="nodegraphics122",
    ends={
        Property(name="NodeGraphics123", type=PNML_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="fill", type=NodeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
edgegraphics124: BinaryAssociation = BinaryAssociation(
    name="edgegraphics124",
    ends={
        Property(name="EdgeGraphics126", type=PNML_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="fill125", type=EdgeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
annotationgraphics127: BinaryAssociation = BinaryAssociation(
    name="annotationgraphics127",
    ends={
        Property(name="AnnotationGraphics129", type=PNML_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="fill128", type=AnnotationGraphics, multiplicity=Multiplicity(0, 1))
    }
)
annotationgraphics140: BinaryAssociation = BinaryAssociation(
    name="annotationgraphics140",
    ends={
        Property(name="AnnotationGraphics141", type=PNML_Font, multiplicity=Multiplicity(1, 1)),
        Property(name="font", type=AnnotationGraphics, multiplicity=Multiplicity(1, 1))
    }
)
edgegraphics134: BinaryAssociation = BinaryAssociation(
    name="edgegraphics134",
    ends={
        Property(name="EdgeGraphics136", type=PNML_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="line135", type=EdgeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
annotationgraphics137: BinaryAssociation = BinaryAssociation(
    name="annotationgraphics137",
    ends={
        Property(name="AnnotationGraphics139", type=PNML_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="line138", type=AnnotationGraphics, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_PNML_NetElement_IdedElement = Generalization(general=IdedElement, specific=PNML_NetElement)
gen_PNML_Arc_NetContent = Generalization(general=NetContent, specific=PNML_Arc)
gen_PNML_Arc_IdedElement = Generalization(general=IdedElement, specific=PNML_Arc)
gen_PNML_Name_LabeledElement = Generalization(general=LabeledElement, specific=PNML_Name)
gen_PNML_Inscription_LabeledElement = Generalization(general=LabeledElement, specific=PNML_Inscription)
gen_PNML_InitialMarking_LabeledElement = Generalization(general=LabeledElement, specific=PNML_InitialMarking)
gen_PNML_NetContentElement_NetContent = Generalization(general=NetContent, specific=PNML_NetContentElement)
gen_PNML_Page_NetContent = Generalization(general=NetContent, specific=PNML_Page)
gen_PNML_Page_IdedElement = Generalization(general=IdedElement, specific=PNML_Page)
gen_PNML_Reference_Node = Generalization(general=Node, specific=PNML_Reference)
gen_PNML_ReferencePlace_NetContent = Generalization(general=NetContent, specific=PNML_ReferencePlace)
gen_PNML_ReferencePlace_Reference = Generalization(general=Reference, specific=PNML_ReferencePlace)
gen_PNML_ReferenceTransition_NetContent = Generalization(general=NetContent, specific=PNML_ReferenceTransition)
gen_PNML_ReferenceTransition_Reference = Generalization(general=Reference, specific=PNML_ReferenceTransition)
gen_PNML_Node_IdedElement = Generalization(general=IdedElement, specific=PNML_Node)
gen_PNML_Place_NetContentElement = Generalization(general=NetContentElement, specific=PNML_Place)
gen_PNML_Transition_NetContentElement = Generalization(general=NetContentElement, specific=PNML_Transition)
gen_PNML_NetGraphics_Graphics = Generalization(general=Graphics, specific=PNML_NetGraphics)
gen_PNML_NodeGraphics_Graphics = Generalization(general=Graphics, specific=PNML_NodeGraphics)
gen_PNML_EdgeGraphics_Graphics = Generalization(general=Graphics, specific=PNML_EdgeGraphics)
gen_PNML_Offset_Coordinate = Generalization(general=Coordinate, specific=PNML_Offset)
gen_PNML_AnnotationGraphics_Graphics = Generalization(general=Graphics, specific=PNML_AnnotationGraphics)
gen_PNML_PageGraphics_Graphics = Generalization(general=Graphics, specific=PNML_PageGraphics)
gen_PNML_Position_Coordinate = Generalization(general=Coordinate, specific=PNML_Position)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={PNML_Color, PNML_AnyElement, PNML_IdedElement, PNML_URI, PNMLDocument, NetContent, PNML_PNMLDocument, URI, NetElement, PNML_NetElement, IdedElement, PNML_LabeledElement, Label, ToolSpecific, NetGraphics, Name, PNML_NetContent, Page, PNML_ToolSpecific, AnyElement, Arc, Node, PNML_Arc, NetContentElement, AnnotationGraphics, PNML_Label, LabeledElement, PNML_Name, PNML_Inscription, PNML_InitialMarking, Place, PNML_NetContentElement, NodeGraphics, EdgeGraphics, Inscription, PNML_Page, PageGraphics, PNML_Reference, PNML_ReferencePlace, Reference, PNML_ReferenceTransition, PNML_Node, PNML_Place, InitialMarking, PNML_Transition, PNML_Graphics, PNML_NetGraphics, Graphics, PNML_NodeGraphics, Position, Dimension, Fill, Line, PNML_EdgeGraphics, PNML_Offset, PNML_AnnotationGraphics, Offset, Font, PNML_PageGraphics, PNML_Coordinate, PNML_Position, Coordinate, PNML_Dimension, PNML_Fill, Color, PNML_Line, PNML_Font, RotationType, ShapeType, StyleType, DecorationType, AlignType},
    associations={document4, contents5, xmlns0, nets1, type2, node23, page25, labels28, tools6, netgraphics8, name10, net12, name14, page16, anyelement18, net19, arc21, source42, target43, annotationgraphics29, namedelement31, net32, netcontent34, arc37, place39, node40, netcontentelement61, tools63, tools46, edgegraphics48, inscription50, contents52, tools54, pagegraphics57, ref59, arc81, position83, fill86, nodegraphics66, initialmarking68, net69, node71, position73, dimension75, fill77, line79, nodegraphics106, edgegraphics108, line89, namedelement92, offset94, font96, fill98, line101, page104, color130, nodegraphics132, annotationgraphics111, nodegraphics113, interiorcolor115, gradientcolor116, image119, nodegraphics122, edgegraphics124, annotationgraphics127, annotationgraphics140, edgegraphics134, annotationgraphics137},
    generalizations={gen_PNML_NetElement_IdedElement, gen_PNML_Arc_NetContent, gen_PNML_Arc_IdedElement, gen_PNML_Name_LabeledElement, gen_PNML_Inscription_LabeledElement, gen_PNML_InitialMarking_LabeledElement, gen_PNML_NetContentElement_NetContent, gen_PNML_Page_NetContent, gen_PNML_Page_IdedElement, gen_PNML_Reference_Node, gen_PNML_ReferencePlace_NetContent, gen_PNML_ReferencePlace_Reference, gen_PNML_ReferenceTransition_NetContent, gen_PNML_ReferenceTransition_Reference, gen_PNML_Node_IdedElement, gen_PNML_Place_NetContentElement, gen_PNML_Transition_NetContentElement, gen_PNML_NetGraphics_Graphics, gen_PNML_NodeGraphics_Graphics, gen_PNML_EdgeGraphics_Graphics, gen_PNML_Offset_Coordinate, gen_PNML_AnnotationGraphics_Graphics, gen_PNML_PageGraphics_Graphics, gen_PNML_Position_Coordinate},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)